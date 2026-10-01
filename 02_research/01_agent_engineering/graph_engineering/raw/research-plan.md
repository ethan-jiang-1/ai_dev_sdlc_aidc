# raw/research-plan.md — Graph Engineering 研究推进计划

> **状态**：v1.0，2026-10-01。定调全文在 [`../README.md`](../README.md) §1。
> **原则**：一手源驱动、问题树牵引、拒绝空中楼阁，每一项判读均锚定真实代码实现、权威公开发言或一线工程实录。

---

## 1. 问题树（Problem Tree）

对应 [`../digested/`](../digested/README.md) 核心议题 01 ~ 05。一手证据归纳在 `raw/evidence-*`，判读权威在 `digested/`，综合综述在 `result/`。

### Q1：为什么必须彻底抛弃“多 Agent 自由聊天”，转向“DAG 状态机”？
- **核心矛盾**：Multi-Agent 早期原型（AutoGen/ChatDev 等）让角色在同一 Context 内自由群聊，为何在工业生产中被证明是死路？
- **机制答案**：Token 爆炸、注意力稀释、死循环反驳、缺乏确定性门禁；替代为由编排者生成带合法性校验的 DAG 状态机，节点间只传递强类型工件。
- **判读收敛**：[`../digested/01-dag-state-machine-vs-free-chat.md`](../digested/01-dag-state-machine-vs-free-chat.md)

### Q2：两层自愈体系（Two-tier Self-Healing）如何运行与协同？
- **核心矛盾**：Loop Engineering（局部迭代）与 Graph Engineering（全局调度）在容错机制上的交界点在哪里？
- **机制答案**：L1 Worker 局部有限退避重试（带 Hard Cap 与机器判据闸门）；L2 Worker 失败后抛出异常，由编排者动态重写 DAG 图（Dynamic DAG Replanning）重新调度。
- **判读收敛**：[`../digested/02-two-tier-self-healing-architecture.md`](../digested/02-two-tier-self-healing-architecture.md)

### Q3：Session 内 Tool 编排 vs Session 外 外部独立状态机？
- **核心矛盾**：图编排逻辑是做在主 Agent 自身的上下文（Session）内作为 Tool，还是做在独立的外部运行时（如 Python/Go 引擎或 Temporal）？
- **机制答案**：Session 内灵活性高但受 Context Rot 与注意力衰减致命制约；Session 外状态机实现硬隔离、可持久化重放与工业级高可用。
- **判读收敛**：[`../digested/03-session-internal-vs-external-state-machine.md`](../digested/03-session-internal-vs-external-state-machine.md)

### Q4：多 Agent 协作中的工件契约与黑板状态机如何设计？
- **核心矛盾**：节点之间不靠聊天，靠什么传递状态？如何防止并发写冲突与状态污染？
- **机制答案**：强类型工件契约（Typed Artifacts / JSON Schema）、单写多读共享黑板（Blackboard Architecture）、基于 Git Branch/Worktree 的物理文件隔离。
- **判读收敛**：[`../digested/04-artifact-contract-and-blackboard.md`](../digested/04-artifact-contract-and-blackboard.md)

### Q5：异构模型拓扑分工与通信治理如何解决？
- **核心矛盾**：不同模型在拓扑中表现出的自主性、汇报策略和 Token 消耗差异极大（如 Opus 5.5 vs Grok 4.7），如何治理？
- **机制答案**：通信频率协议（Chatter Throttling）、差异化模型梯次挂载（主控 vs 专职 Worker）、通信配额熔断。
- **判读收敛**：[`../digested/05-heterogeneous-model-governance.md`](../digested/05-heterogeneous-model-governance.md)

### Q6：2026顶级模型（Opus 5.5 / Sonnet 5 / OpenAI Sol / Astra）在图节点中的真实病态行为与防御工程？
- **核心矛盾**：即使用最顶级的推理与编码模型，真实图执行中依然频繁出现“架构过度侵占”、“推理停顿中断脆弱”、“长上下文坏味道锚定”、“汇报风暴”等反直觉缺陷，如何构建防御脚手架？
- **机制答案**：AST 局部差异锁、测试文件物理只读挂载与影子评估、Git Worktree 隔离与写入白名单硬拦截、思维链擦除与 Schema 强类型提纯。
- **判读收敛**：[`../digested/06-sota-model-pathologies-and-defenses.md`](../digested/06-sota-model-pathologies-and-defenses.md)

### Q7：L2 拓扑自愈如何避免“重规划元死锁”？动态改图的工程实现？
- **核心矛盾**：当 Worker 失败触发 L2 改图时，如果重编排模型产生幻觉或与 Worker 相互推诿，系统会陷入 Meta Doom Loop；如何实现局部子图切片替换（Sub-graph Splicing）与状态回滚？
- **机制答案**：禁止全量重写 DAG，严格采用“局部子图切片替换（Sub-graph Splicing）”；设置全局重规划预算计数器（Max Replanning Budget <= 2）；强类型 Failure Envelope 携带 AST 切片与退出码。
- **判读收敛**：[`../digested/07-dynamic-dag-replanning-mechanics.md`](../digested/07-dynamic-dag-replanning-mechanics.md)

### Q8：工业落地收敛：从理论图编排到“超级智能体底座（SuperAgent Harness）”？
- **核心矛盾**：工业界真实落地的 Agent 系统（如字节跳动 DeerFlow 2.0、LangGraph 衍生系统）如何实现“传统程序控流程、智能体干活”？
- **机制答案**：确定性状态机（LangGraph）硬控调度 + Lead Agent 动态任务切片 + Docker 物理沙箱隔离并发 + 渐进式技能装配（Progressive Skill Registry）。
- **判读收敛**：[`../digested/08-superagent-harness-deerflow-langgraph.md`](../digested/08-superagent-harness-deerflow-langgraph.md)

---

## 2. 研究分路（Tracks）

| 分路 | 对应问题 | 目标与范围 | 当前状态 |
|---|---|---|---|
| **分路 A：拓扑推进与状态机机理** | Q1 | 对比自由聊天与 DAG 状态机，分析拓扑合法性静态校验 | ✅ 完成回源与判读 |
| **分路 B：两层分级自愈体系** | Q2, Q7 | 解构 L1 局部退避重试与 L2 动态 DAG 重编排、子图切片替换机制 | ✅ 完成回源与判读 |
| **分路 C：宿主边界与 Session 内外架构** | Q3 | 对比 Session 内 Tool 驱动与 Session 外状态机（Temporal / Raven / Sentry） | ✅ 完成回源与判读 |
| **分路 D：工件契约与通信协议治理** | Q4, Q5 | 分析工件契约、A2A 协议、黑板架构以及异构模型通信节流 | ✅ 完成回源与判读 |
| **分路 E：SOTA 模型实战行为与攻防** | Q6 | 挖掘 Opus 5.5 / Sonnet 5 / Sol / Astra 等 2026 顶级模型在图节点中的真实病态行为与硬核防御脚手架 | ✅ 完成回源与判读 |
| **分路 F：工业超级底座落地实证** | Q8 | 解剖字节跳动 DeerFlow 2.0 与 LangGraph 工业衍生：外层确定性状态机与 Docker 物理沙箱闭环 | ✅ 完成回源与判读 |

---

## 3. 回源档案索引（Evidence Register）

| 档案文件名 | 分路 | 回答的核心事实 | 证据级别 |
|---|---|---|---|
| [`evidence-20261001-field-exchange.md`](evidence-20261001-field-exchange.md) | A, B, C, D | 2026-10-01 Raven A2A 开发者（Jarvan 日成、Willis、Ethan）一线交流实录：DAG 状态机替代聊天、分层重试、Grok 汇报消耗、Session 内外权衡 | `[B]` |
| [`evidence-20260718-steinberger-graph-shift.md`](evidence-20260718-steinberger-graph-shift.md) | A, B | Peter Steinberger 提出 *"From Loops to Graphs"* 引发的行业大论战一手证据与观点碰撞 | `[A]` |
| [`evidence-202603-anthropic-workflow-patterns.md`](evidence-202603-anthropic-workflow-patterns.md) | A, C | Anthropic 官方指南《Building Effective Agents》五大拓扑模式（Chaining, Routing, Parallel, Orchestrator-Workers, Evaluator-Optimizer） | `[S]` |
| [`evidence-2026-langgraph-temporal-state-machines.md`](evidence-2026-langgraph-temporal-state-machines.md) | B, C | LangGraph 持久化检查点、时间旅行与 Temporal 工业级确定性事件溯源架构分析 | `[S]` |
| [`evidence-2026-sota-model-behaviors-in-graphs.md`](evidence-2026-sota-model-behaviors-in-graphs.md) | E | 2026 顶级模型（Opus 5.5 / Sonnet 5 / Sol / Astra）在图节点中的五大病态行为（架构过度重构、推理停顿、测试作弊）与硬核防御脚手架 | `[S]` |
| [`evidence-2026-kol-armin-swyx-hashimoto.md`](evidence-2026-kol-armin-swyx-hashimoto.md) | A, C | 系统架构师阵营（Armin Ronacher 状态机对抗混沌、Swyx 流程工程、Hashimoto 持久化工作流、Zaharia 复合系统） | `[A]` |
| [`evidence-2026-bytedance-deerflow-langgraph.md`](evidence-2026-bytedance-deerflow-langgraph.md) | F | 字节跳动 DeerFlow 2.0 超级智能体底座开源实证：基于 LangGraph 的 Lead-Subagent 动态任务图与 Docker 沙箱物理隔离 | `[S]` |

---

## 4. 质量门禁（Quality Gates）

1. **一手锚点**：不收录无出处的空泛二手推论；所有工程断言必须溯源到具体项目、原帖或实操转写。
2. **反思批判**：坚决破除行业“名词包装（Buzzword）”迷信，直面 Graph 的静态开销、状态机复杂性与动态改图的不可停机风险。
3. **闭环验证**：每一条 digested 结论必须能在真实代码或架构设计中找到可验证的技术对应物。
