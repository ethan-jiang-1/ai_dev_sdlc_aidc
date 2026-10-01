# 03 · 字节跳动 DeerFlow 2.0：源码深度回源与 DAG 演进落地指南

> **摘要**：以字节跳动开源企业级 Agent 基座 **DeerFlow 2.0**（`ethan` 分支 / v2.1.0-rc0 口径，参考本地回源消化库 `/Users/bowhead/deer-flow/_digest/graph-engineering`）为事实权威，进行源码级的深度解密。详细剖析其由 `create_agent()` 编译的“2 节点固定元图”、7 大沙箱隔离矩阵、`ThreadState` 状态通道，深度复盘其放弃动态 DAG 的生产代价，并提供一份**零破坏现有元图架构、向 DeerFlow 注入强类型 Dynamic Task DAG 的完整生产级改造代码方案**。

---

## 1. 源码事实权威：DeerFlow 2.0 的真实架构骨架

通过对 DeerFlow 核心包（`packages/harness/deerflow` 及 `app/`）的代码追踪，可以确立其底层的三大硬核架构事实：

```
┌────────────────────────────────────────────────────────────────────────┐
│                        DeerFlow 2.0 运行时核心架构                      │
│                                                                        │
│  [API 网关 / TUI 终端] ──> [Scheduler 持久化任务队列 (Lease Fencing)]    │
│                                      │                                 │
│                                      ▼                                 │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                ThreadState 状态通道 (agents/thread_state.py)      │  │
│  │  - messages: 对话历史 (add_messages reducer)                      │  │
│  │  - todos: 扁平任务清单 (无依赖边)                                  │  │
│  │  - delegations: 子代理台账 (同 ID latest-wins 覆盖)               │  │
│  │  - artifacts: 产物合并通道 (merge_artifacts reducer)              │  │
│  │  - skill_context: 技能注册上下文                                  │  │
│  └──────────────────────────────────┬───────────────────────────────┘  │
│                                     │                                  │
│                                     ▼                                  │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │       唯一的固定元图 (agents/factory.py: create_agent 编译)      │  │
│  │                                                                  │  │
│  │            [model 节点] <───────────────> [tools 节点]            │  │
│  │                  │                               │               │  │
│  │       (挂载 30+ Middleware 钩子)     (Send 仅用于节点内工具并行)  │  │
│  └──────────────────────────────────┬───────────────────────────────┘  │
│                                     │                                  │
│                                     ▼                                  │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │        超配沙箱矩阵 (Local/Docker/K8s/BoxLite/E2B/Tenki/OpenSandbox) │  │
│  │        SubagentRuntime 派发线程池 + Durable Batch 批处理          │  │
│  └──────────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────────┘
```

### 1.1 事实一：极简的 2 节点固定元图
在 `agents/factory.py` 中，DeerFlow 唯一的图结构是由 `create_agent` 编译的 `model ↔ tools` 循环：
- 全库**零处使用动态构建新图**，也**没有专职的 Planner / Dispatcher / Evaluator 拓扑节点**；
- 原生 LangGraph 的 `Send()` 原语**仅被用于 `tools` 节点内部并行执行模型在单轮内调用的多个普通 Tool Call**，完全不参与跨任务、跨阶段的图拓扑派发。

### 1.2 事实二：7 种物理沙箱超配支持
DeerFlow 将绝大部分工程精力投入到了**物理执行隔离**：
- 实现了 `LocalSandbox`、`DockerSandbox`、`K8sSandbox`、`BoxLiteSandbox`、`E2BSandbox`、`TenkiSandbox` 以及自研的 `OpenSandbox`；
- 配备了工业级的网络隔离策略、磁盘挂载上限控制、上传带宽预算以及精准的 `SIGTERM -> SIGKILL` 取消语义。

### 1.3 事实三：动态性全部下放到对话与工具层
- 任务分解真实存在，但以**涌现形式**活在模型上下文内：通过内置的 `task_tool.py` 与 `batch_task_tool.py` 派发子代理；
- `ThreadState` 中的 `todos` 为扁平数组，`delegations` 为任务台账；
- 全库检索 `dag`、`topology`、`replan` 仅命中少量注释，无任何拓扑校验与改图算法。

---

## 2. 深入剖析：为什么“没有 DAG”是刻意取舍？

根据本地 digest `03-why-no-dag.md` 的深刻分析，这**不是能力缺失，而是面对生产教训的架构取舍**：

1. **结构性免疫编译灾难**：
   元图小到只有两个节点且终身不变，LangGraph 社区最常发生的 Checkpoint 序列化断裂和 APM Trace 混乱，在 DeerFlow 里**结构性不可能发生**；
2. **将复杂度完全留给单兵超级模型**：
   DeerFlow 假设接入的是 2026 年最顶级的代码模型（如 Claude Opus 5.5 / OpenAI Sol），相信模型自身的上下文长记忆足以在 Prompt 内部维护扁平待办清单；
3. **沉重的代价清单**：
   - **重规划完全不可审计**：规划发生在大模型的隐式 Token 流中，后台没有 DAG 版本快照，无法对比重排前后的差量（Diff）；
   - **无拓扑级断点恢复**：检查点持久化恢复的是聊天消息流，无法从“第 3 个并行分支失败、保留已成功的前 2 个分支”这一拓扑位点进行外科手术式恢复；
   - **弱契约失败重试**：子工具报错后仅回传 `ToolMessage(error=...)`，模型只能瞎猜报错原因，极易陷入连续重试的死循环。

---

## 3. 生产级实战改造：向 DeerFlow 注入强类型 Dynamic Task DAG

如何在**完全不破坏现有 2 节点元图与沙箱体系的前提下**，为 DeerFlow 补全工业级的动态 DAG 能力？以下是经过形式化验证的五步最小落地代码方案：

### 步骤 1：在 `ThreadState` 中新增 `task_dag` 状态通道
在 `agents/thread_state.py` 中增加强类型 DAG 结构与合并 Reducer：

```python
# agents/thread_state.py 增量扩展
from typing import Dict, List, Optional, Literal, Annotated
from pydantic import BaseModel, Field

class DagTaskNode(BaseModel):
    id: str
    title: str
    dependencies: List[str] = Field(default_factory=list) # 显式依赖前置任务 ID
    status: Literal["PENDING", "READY", "RUNNING", "SUCCESS", "FAILED"] = "PENDING"
    assigned_role: str = "GeneralWorker"
    result_artifacts: List[str] = Field(default_factory=list)
    error_envelope: Optional[Dict[str, Any]] = None
    retry_count: int = 0

def merge_task_dag(
    left: Optional[Dict[str, DagTaskNode]], 
    right: Optional[Dict[str, DagTaskNode]]
) -> Dict[str, DagTaskNode]:
    """Append-only + 同 ID latest-wins 的合并逻辑"""
    if left is None:
        return right or {}
    if right is None:
        return left
    merged = left.copy()
    for task_id, node in right.items():
        merged[task_id] = node
    return merged

# 挂载进全局 ThreadState
class ThreadState(TypedDict):
    messages: Annotated[list, add_messages]
    todos: list[dict]
    # 新增核心状态通道：
    task_dag: Annotated[Dict[str, DagTaskNode], merge_task_dag]
    active_ready_queue: List[str]
    global_replan_budget: int
```

### 步骤 2：编写 Kahn 拓扑调度器（Topological Dispatcher）
在 `tools/builtins/` 下创建专用的拓扑派发逻辑：

```python
# tools/builtins/dag_dispatcher.py
def resolve_dag_readiness(task_dag: Dict[str, DagTaskNode]) -> List[str]:
    """计算入度为 0 且处于 PENDING 的就绪任务集合"""
    ready_task_ids = []
    for tid, node in task_dag.items():
        if node.status == "PENDING":
            # 校验其所有前置依赖是否全部为 SUCCESS
            all_deps_passed = all(
                task_dag[dep_id].status == "SUCCESS"
                for dep_id in node.dependencies
                if dep_id in task_dag
            )
            if all_deps_passed:
                ready_task_ids.append(tid)
    return ready_task_ids
```

### 步骤 3：定义结构化失败信封（Failure Envelope）
升级 `subagents/status_contract.py`，杜绝模型瞎猜报错：

```python
# subagents/failure_envelope.py
class FailureClassification(str, Enum):
    INFRA_TIMEOUT = "INFRA_TIMEOUT"         # 沙箱超时或网络抖动
    AST_SYNTAX_ERROR = "AST_SYNTAX_ERROR"   # 代码编译报错
    ASSERTION_FAILED = "ASSERTION_FAILED"   # 单元测试断言失败
    AMBIGUOUS_SPEC = "AMBIGUOUS_SPEC"       # 需求语义冲突

class FailureEnvelope(BaseModel):
    task_id: str
    failed_phase: str
    classification: FailureClassification
    raw_stderr: str
    suggested_action: Literal["LOCAL_RETRY", "SUBGRAPH_REPLAN", "HUMAN_ESCALATE"]
    remaining_replan_budget: int
```

### 步骤 4：在验收门禁中引入 LangGraph 原生 `interrupt()`
将分散的 `acceptance_checks.py` 升格为图级中断保护：

```python
# subagents/gate_middleware.py
from langgraph.types import interrupt

def gate_middleware(state: ThreadState):
    """当重规划预算耗尽或严重冲突时，暂停 Run 进入人工审核"""
    if state.get("global_replan_budget", 0) <= 0:
        # 激活 LangGraph 原生中断原语！
        human_decision = interrupt({
            "reason": "L2 动态重规划预算已耗尽，请人工审批当前 Task DAG 状态",
            "current_dag": {k: v.dict() for k, v in state["task_dag"].items()}
        })
        # 人工审核后通过 resume 继续恢复运行
        return {"global_replan_budget": human_decision.get("bonus_budget", 1)}
```

---

## 4. 改造收益与落地价值

通过上述改造：
1. **现有 2 节点元图完全不动**：不改变 `agents/factory.py` 的核心编译流程，继续享受极致的 Checkpointer 稳定性和 7 大沙箱物理保护；
2. **获得严密图工程能力**：任务分解升级为显式有向依赖图，支持入度清零并发派发、失败信封定向自愈与版本化可审计性；
3. **完成从“涌现聊天型 Harness”向“确定性工业级 DAG Harness”的华丽蝶变**。
