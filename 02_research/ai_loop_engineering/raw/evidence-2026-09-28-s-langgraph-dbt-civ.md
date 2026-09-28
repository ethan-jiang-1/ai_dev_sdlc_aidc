# evidence-s — LangGraph 预算感知管理、dbt 外部质检闸门与 CIV 架构深化

> 路别：s（工程实现与运行时框架深入）  
> 观测日期：2026-09-28  
> 回源代理：主代理（Antigravity）  
> 承重引文标注：见各条  

---

## 来源清单

| # | 类型 | 来源 | 发布/观测日期 | 强度 |
|---|---|---|---|---|
| S1 | 官方框架/文档/代码 | LangGraph `RemainingSteps` & `GraphRecursionError` 防御机制 | 2026（观测） | 一手·官方 API + 生产代码模式已复核 |
| S2 | 官方文档/行业实践 | dbt Core / Cloud 退出码与 Gate-Prompted Validation（dbt / Great Expectations） | 2026（观测） | 一手·官方规范（getdbt.com）+ 2026 工程实践已复核 |
| S3 | 官方发布/平台文档 | Intent (`intentapp.dev`) & Augment Code Cosmos CIV 架构 | 2026（观测） | 一手·平台页面抓取（intentapp.dev）+ 架构分析已复核 |

---

## S1 · LangGraph `RemainingSteps` Managed Value 与循环防御（2026）

### 机制背景
在 LangGraph 中，当图执行的 super-steps 超过 `recursion_limit`（默认配置常见为 25 或高阶运行时的 1000）而未达到 `END` 状态时，运行时会抛出 `GraphRecursionError`。
单纯抛出异常是被动崩溃（reactive crash）：
1. 丢失当轮尚未持久化的上下文或诊断信息；
2. 留下悬挂的外部 side-effects；
3. 将未处理的错误直接暴露给用户或上层调用者。

### 核心实现：主动预算感知（Proactive Stop Condition）
LangGraph 2026 推荐在 `AgentState` 中注入托管值（Managed Value）`RemainingSteps`：

```python
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.managed import RemainingSteps

class AgentState(TypedDict):
    messages: Annotated[list, lambda x, y: x + y]
    # LangGraph 运行时自动注入剩余步数
    remaining_steps: RemainingSteps 

def reasoning_node(state: AgentState) -> dict:
    steps_left = state.get("remaining_steps")
    # 主动预算防御：在耗尽前 1 步做优雅降级/落盘，而非等待运行时抛出异常崩溃
    if steps_left is not None and steps_left <= 1:
        return {"messages": ["Finalizing output and persisting partial state due to step budget limit."]}
    return {"messages": ["Continuing task execution..."]}

def should_continue(state: AgentState) -> str:
    if state.get("remaining_steps", 1) <= 0:
        return END
    return "reasoning_node"
```

### 生产工程洞察与负结论
1. **负结论：调大 `recursion_limit` 是掩耳盗铃**：
   - 生产排查共识指出，单纯将 `recursion_limit` 从 25 改为 1000 并不能解决死循环，往往只会延缓失败并成倍增加 API 账单。
   - 死循环的根因往往是**状态停滞（State Stagnation）**：如果连续多个 step 中 state payload 没有发生有效变异（如模型反复收到相同的 403 错误或空工具响应），模型就无法获得跳出循环的信息。
2. **防御分层**：
   - 静态/外层：`recursion_limit` 硬上限（底线熔断）；
   - 动态/内层：`RemainingSteps` 感知（主动降级、落盘与生成部分解释）；
   - 行为层面：滑动窗口工具哈希比对（检测相同 tool call 循环）。

---

## S2 · 数据域机器判据：dbt 退出码与 Gate-Prompted Validation（2026）

### 官方退出码契约（getdbt.com 规范）
- `0`：Success（所有选择的 model/test 成功执行并断言通过）。
- `1`：Invocation completed but failed（命令执行完成但至少有一个 test 失败，或存在捕获的运行时错误）。
- `2`：Invocation unhandled error（命令因未捕获异常、网络中断或信号退出）。

### 2026 数据智能体实践：从 Prompting 转向外部硬闸门（Stop Hook）
在数据管道治理中，让 Agent 自主判断 SQL 或转换是否正确已被证明极不可靠。2026 年行业演进为 **Gate-Prompted Validation**：
1. **确定性命令调用**：
   - Agent 修改 SQL/模型后，执行 `dbt test --select state:modified+`（只测试被改动模型及其下游）。
2. **机器可读报告解析（非仅依赖文本输出）**：
   - Agent 或宿主容器不解析终端输出文本，而是直接读取结构化的 `run_results.json`，核验各 node 的 `status == "pass"` 与 `failures == 0`。
3. **阈值控制与震荡防御**：
   - 配置 `config(error_if=">10", warn_if=">0")`，区分业务容忍警告与阻断性错误。
   - **Lineage 震荡死循环（Fix-break oscillation loop）**：Agent 修复了 A 表的 `not_null`，导致 B 表的引用级联失败。必须引入 DAG Lineage 约束，当修改产生下游新失败时强制回滚并触发升级。

---

## S3 · Intent (`intentapp.dev`) & Cosmos CIV 模式演化（2026）

### 平台定位
- Intent（原 Augment Code Intent，2026 迁移至 `intentapp.dev`，开源客户端与专有运行时结合）。
- 标语："Large-scale agent coordination for developers. For decades, the job was writing code. When AI handles that, the job becomes something bigger: setting direction, deciding outcomes… operating at the level of intent."

### CIV 三角角色的停止与验收机制
1. **Coordinator（协调者）**：
   - 依据上下文引擎生成有依赖向的执行图与 **Living Spec**（动态规格文档）。
2. **Implementor（执行者）**：
   - 在**隔离的 git worktree** 中并行干活，确保文件修改与状态不发生交叉污染。
3. **Verifier（验证者）**：
   - 独立于 Implementor，不参与代码编写。
   - **验收契约**：直接以 Living Spec 为唯一真理来源，结合运行环境测试、linter 和构建结果进行核验。
   - **渐进式升级策略**：
     - **Advisory Mode**：在早期仅产出 PR 审查评论与建议，用于测量与校准规格与误报率；
     - **Blocking Hard Gate**：当可信度经过验证后，升级为强制阻断分支合并的硬闸门。
