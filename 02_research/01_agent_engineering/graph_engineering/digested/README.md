# digested — 消化与判读

> **本层是什么**：把 `raw/` 中的一手素材、现场实录与论战交锋，消化为深度的工程判断与机制剖析。
> **判读权威在本层**。定调在 [`../README.md`](../README.md) §1，问题树在 [`../raw/research-plan.md`](../raw/research-plan.md)。一议题一篇，编号 = 创建序。

---

## 增长规则

- 新议题判读 → 建 `0N-<slug>.md`（编号取当前最大 +1）→ 下表加一行。不改已有编号。
- 每一个判读文件必须做到：矛盾识别、机制剖析、正反手权衡、代码或伪代码形态落地、一线实证锚定。

---

## 问题看板

| # | 核心议题 | 状态 | 核心工程结论 | 文件 |
|---|---|---|---|---|
| **01** | **为什么抛弃“自由聊天”走向“DAG 状态机与强类型工件”？** | ✅ 已收口 | 自由群聊存在 Token 指数爆炸、注意力客套稀释、Doom Loop 无法收敛等致命缺陷；DAG 状态机提供确定性拓扑与强类型工件交付门禁。 | [`01-dag-state-machine-vs-free-chat.md`](01-dag-state-machine-vs-free-chat.md) |
| **02** | **两层自愈体系：Worker 局部 Loop vs 编排者动态 DAG 重排** | ✅ 已收口 | Loop 与 Graph 的交接点在于异常分级升级：L1 是 Worker 内有限退避重试（微循环）；L2 是向上抛出异常后由编排者动态改图（宏观拓扑重排）。 | [`02-two-tier-self-healing-architecture.md`](02-two-tier-self-healing-architecture.md) |
| **03** | **Session 内 Tool 编排 vs Session 外 外部状态机/运行时** | ✅ 已收口 | Session 内 Tool 编排易受 Context Rot 与注意力衰减拖垮；Session 外状态机（Temporal / 外部运行时）实现物理上下文隔离与长生不老的工作流。 | [`03-session-internal-vs-external-state-machine.md`](03-session-internal-vs-external-state-machine.md) |
| **04** | **工件契约、A2A 协作协议与全局共享黑板状态机** | ✅ 已收口 | 节点之间交接必须通过强类型 Schema 声明；全局状态通过共享黑板（Blackboard）管理，并借助 Git 分支实现单写多读的物理版本隔离。 | [`04-artifact-contract-and-blackboard.md`](04-artifact-contract-and-blackboard.md) |
| **05** | **异构模型拓扑分工与通信治理（汇报冲动与配额约束）** | ✅ 已收口 | 异构模型存在巨大汇报倾向差异（如 Grok 4.7 频繁汇报烧光额度，Opus 5.5 静默闭环）；图协议层必须强制实现 Chatter Throttling 与配额熔断。 | [`05-heterogeneous-model-governance.md`](05-heterogeneous-model-governance.md) |
| **06** | **2026顶级模型在图工程中的真实病态行为与防御工程实操** | ✅ 已收口 | 实测 Opus 5.5 / Sonnet 5 / Sol / Astra 的五大病态行为（过度架构侵占、推理中断脆弱、长上下文坏味道锚定、汇报风暴、合规性伪造）；建立 AST 局部差异锁、只读测试与影子门禁。 | [`06-sota-model-pathologies-and-defenses.md`](06-sota-model-pathologies-and-defenses.md) |
| **07** | **L2 拓扑自愈实操：局部子图切片替换与防死锁算法** | ✅ 已收口 | 彻底摒弃全量重新生图的灾难做法；确立冻结已成功节点、局部子图切片替换（Sub-graph Splicing）、受限改图三大原子操作与全局重规划硬预算（Max <= 2）。 | [`07-dynamic-dag-replanning-mechanics.md`](07-dynamic-dag-replanning-mechanics.md) |
| **08** | **工业落地样本解剖：从理论图编排到“超级智能体底座”** | ✅ 已收口 | 深入字节跳动 DeerFlow 2.0 与 LangGraph 工业衍生生态：确立“外层确定性程序控流程、内层智能体干活”、Docker 物理沙箱隔离、Lead-Subagent 动态任务切片与渐进式技能装配。 | [`08-superagent-harness-deerflow-langgraph.md`](08-superagent-harness-deerflow-langgraph.md) |
| **09** | **血泪反思：纯动态图编译的生产陷阱与“固定元图+动态任务DAG”终局** | ✅ 已收口 | 剖析学院派“现场编译新图”的致命死穴（Checkpointer断裂、Trace无法监控、元状态抖动）；确立“静态编译固定元图（Meta-Graph）+ 状态消费动态任务数据（Task DAG）”的工业终局解法。 | [`09-meta-graph-vs-dynamic-task-dag.md`](09-meta-graph-vs-dynamic-task-dag.md) |
