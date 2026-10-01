---
title: Framed Autonomy — 从学术概念到工程实现
date: 2026-07-08
source: web_search (Round 9)
type: deep_dive
status: draft
---

# Framed Autonomy：从学术概念到工程实现

> Round 9 深挖。Framed Autonomy 不再只是学术概念——2026 年有多篇论文给出了具体的工程架构。本文拆解 Operational Frame 和 Normative Frame 在真实系统里的实现方式。

---

## 一、概念回顾

来自 Calvanese 等 18 位作者（Dagstuhl Seminar, 2026）：

> "确保 APM 系统中流程感知和目标对齐的主要机制，通过对 Agent 的知识和目标施加限制来约束其自主性。"

四个并列的 APM 能力：Framed Autonomy + Explainability + Conversational Actionability + Self-Modification。

---

## 二、Operational Frame vs Normative Frame

**Fournier & Limonad（June 2026）的 CUGA FLO 架构**给出了最精确的工程区分：

| Frame 类型 | 管辖什么 | 实现方式 |
|-----------|---------|---------|
| **Operational Frame** | 确定性工作流执行；结构合规 | **命令式需求**，由底层工作流引擎强制执行 |
| **Normative Frame** | 在指定控制点的策略治理式 Agent 推理 | **声明式策略**，LLM Agent 在其范围内推理——所有 LLM 调用的聚合策略集（即 **Process FRAME**） |

> *"The process harness uniquely reconciles imperative requirements, realized through deterministic workflow execution that enforces structural compliance, with normative requirements, realized through policy-framed agentic autonomy invoked at designated control points wherever the process demands it."*

### 关键架构决策：谁持有结构权威？

**工作流引擎**持有结构权威——流程骨架是确定性的。
**Agent 层**在拦截的控制点上贡献推理、适应和监督——但工作在引擎定义的"框"内。

这跟 SDLC 的 CI/CD 管道完全同构：**CI 规则是确定性的（Operational Frame），Agent 在管道内自主编码和测试（Normative Frame）。**

---

## 三、CUGA FLO 的 TDF 模型

Task-Decision-Flow（TDF）模型定义了三种 Agent 角色：

| Agent 类型 | 职责 | 在 Frame 中的位置 |
|-----------|------|------------------|
| **TaskAgent** | 执行单个任务（调用工具、处理数据） | 工作在 Normative Frame 内——每个调用前拉取相关策略 |
| **DecisionAgent** | 在分支点做决策（审批、路由、异常判断） | 在 Operational Frame 的控制点被调用——结构由引擎决定，决策由 Agent 做 |
| **FlowAgent** | 编排端到端流程，协调 TaskAgent 和 DecisionAgent | 持有 Operational Frame 的结构定义，同时分发 Normative Frame 的策略给子 Agent |

**TDF 的核心创新**：不是 Agent 自由编排流程——是**流程引擎定义骨架，Agent 在控制点上被调用**。每个 Agent 调用时都从 Process FRAME 拉取显式策略。

---

## 四、Frame Agent + Operational Agent 模式

**Skolik & Müller 等（2026）**的模块化架构：

```
BPMN 模型 / 自然语言
        ↓
   Frame Agent（生成流程描述 + 约束）
        ↓
   Operational Agent（在 Frame 约束内自主执行）
        ↓
   [未来] Tactical Agent（完全自主的流程自适应）
```

**德国能源网公司 meter-to-cash 真实案例**：
- Frame Agent 从 BPMN 生成流程规则
- Operational Agent 自主执行
- **预定义规则下 99% 成功执行率**
- 相比传统 RPA，适应性和灵活性有显著提升

---

## 五、Process FRAME 的内部结构

从两篇论文综合出的 Frame 的内部组成：

| Frame 组件 | 类型 | 例子 |
|-----------|------|------|
| **Hard constraints** | 必须满足 | "发票金额 > $10,000 必须经过二级审批" |
| **Soft constraints** | 可以违反，但有代价 | "优先使用供应商 A，除非价格差异 > 15%" |
| **Role assignments** | 哪个 Agent 做什么 | "DecisionAgent 负责审批，TaskAgent 负责数据提取" |
| **Segregation of duties** | 冲突约束 | "生成付款指令的 Agent 不能同时审批相同付款" |
| **Lifecycle rules** | Agent 生命周期 | "任务完成后 TaskAgent 被释放，审批超时 DecisionAgent 升级" |

**Meta-frame**：覆盖整个 ABPMS 的顶层约束——比如"所有 Agent 推理必须在 30 秒内完成"或"任何单个 Agent 不能花费超过 $500 的 API 成本"。

---

## 六、ABPMS 生命周期

Manifesto 定义的 Agentic BPM 生命周期：

```
Basic steps（操作层，流程感知执行）:
  Perceive → Reason → Enact

Advanced steps（策略层，持续优化）:
  Adapt → Improve → Explain
```

Framed Autonomy 横跨所有六步：
- 在 **Perceive/Reason/Enact**：Agent 在 Frame 内感知、推理、执行
- 在 **Adapt**：Frame 本身被评估和调整（"这个约束还合理吗？"）
- 在 **Improve/Explain**：Frame 的变更需要可解释

---

## 七、与 SDLC 的精确映射

| Framed Autonomy 概念 | SDLC 等价 | 成熟度 |
|---------------------|----------|--------|
| Operational Frame（命令式流程骨架） | CI/CD Pipeline（lint → test → build → deploy） | SDLC 侧**更成熟** |
| Normative Frame（声明式策略） | `.editorconfig`, `eslintrc`, `CODEOWNERS`, CI rules | SDLC 侧**有等价物但分散** |
| Hard constraints | CI 必须通过的检查（不能跳过） | 成熟 |
| Soft constraints | Lint warnings, code style suggestions | 成熟 |
| Control point（引擎拦截→Agent 决策） | PR review, deployment approval | SDLC 侧**更成熟** |
| Meta-frame | Org-level security policy, SOC 2 compliance rules | 两边都在早期 |
| Frame Agent + Operational Agent | CI 配置 + AI coding agent 在管道内执行 | SDLC 侧正在出现 |
| Agent 委托链衰减 | — | **SDLC 侧缺少** |

---

## 八、对 AI-SDLC 的启示

1. **CI/CD 管道就是 Operational Frame。** 管线步骤（lint→test→build→deploy）是确定性的流程骨架。Agent 在管线内自主编码和测试——这是 Framed Autonomy 在 SDLC 的精确实现。

2. **Normative Frame 在 SDLC 侧是分散的。** `.editorconfig`、`eslintrc`、`CODEOWNERS`、CI rules——每个都是声明式策略，但没有统一的 Process FRAME 概念把它们聚合起来。

3. **Control Point 是 SDLC 的强项。** PR review、deployment approval、protected branches——SDLC 侧在"关键节点人策展"上比企业侧成熟得多。

4. **缺少 Agent 委托链衰减。** 当一个 AI coding agent 调用另一个 agent 执行子任务时，权限应该衰减——SDLC 侧还没有这个形式化。

5. **Meta-frame 是两边共同的空白。** 对"整个 AI-SDLC 系统"的顶层约束——比如"Agent 不能单次 PR 修改超过 500 行"或"自主 merge 只能在测试通过率 > 95% 时发生"——还没有系统化。
