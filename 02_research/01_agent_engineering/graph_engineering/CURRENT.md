# 当前状态（热区）

> 最近一次更新：**2026-10-01**。已完成从 `01_seed_reference/graph_engineering/` 的素材深度消化，并建立标准研究层架构（`raw/`、`digested/`、`result/`）。

## 一句话

**单体 Loop 无法承担长程复杂工程任务；Graph Engineering 通过显式 DAG 状态机、隔离强类型工件与两层分级自愈（Worker 局部 Loop + 编排者改图重试），实现高可靠 Agentic SDLC。**

## 状态

| 件 | 状态 | 核心要点 |
|---|---|---|
| [`README.md`](README.md) | ✅ 定调已立 | 定调在 §1（唯一权威）；明确与 Loop / Harness / Goal-Eval 四维分工 |
| [`raw/00-timeline.md`](raw/00-timeline.md) | ✅ 已收录 | 2023-2026 五层演进光谱；2026-07-18 Peter Steinberger 发问；2026-10-01 一线工程交流 |
| [`raw/research-plan.md`](raw/research-plan.md) | ✅ 已规划 | 四大分路（状态机推进、两层自愈、Session内外架构、协议与模型治理）、质量门禁与 backlog |
| [`raw/roster.md`](raw/roster.md) | ✅ 名单建立 | 核心 KOL（Harrison Chase, Peter Steinberger, Andrew Ng, Armin Ronacher, Swyx, Mitchell Hashimoto）与开源实践者（ByteDance DeerFlow, Jarvan/Raven, Temporal, OpenHands） |
| [`raw/evidence-*.md`](raw/) | ✅ 7 份档案 | 一线实录（20261001 Raven A2A）、Steinberger 论辩、Anthropic 工作流、LangGraph/Temporal 状态机、2026 SOTA 顶级模型行为攻防、架构师阵营（Armin/Swyx/Hashimoto）、字节跳动 DeerFlow 2.0 实证 |
| [`digested/01-dag-state-machine-vs-free-chat.md`](digested/01-dag-state-machine-vs-free-chat.md) | ✅ 已判读 | 彻底否定自由群聊；确立 DAG 状态机与强类型工件交付范式 |
| [`digested/02-two-tier-self-healing-architecture.md`](digested/02-two-tier-self-healing-architecture.md) | ✅ 已判读 | 深度解构 L1 Worker 局部 Loop 重试退避 vs L2 编排者动态改图重试 |
| [`digested/03-session-internal-vs-external-state-machine.md`](digested/03-session-internal-vs-external-state-machine.md) | ✅ 已判读 | Session 内 Tool 编排 vs Session 外 外部状态机（Temporal / 外部引擎）核心权衡 |
| [`digested/04-artifact-contract-and-blackboard.md`](digested/04-artifact-contract-and-blackboard.md) | ✅ 已判读 | 工件契约规范、A2A 协作协议与全局共享黑板状态机（Blackboard） |
| [`digested/05-heterogeneous-model-governance.md`](digested/05-heterogeneous-model-governance.md) | ✅ 已判读 | 异构模型拓扑分工与通信治理（汇报冲动/Chatter 抑制与 Token 配额） |
| [`digested/06-sota-model-pathologies-and-defenses.md`](digested/06-sota-model-pathologies-and-defenses.md) | ✅ 已判读 | 2026顶级模型（Opus 5.5 / Sonnet 5 / Sol / Astra）在图节点中的五大病态行为（过度架构侵占、推理中断脆弱、上下文锚定、汇报风暴）与硬核防御工程 |
| [`digested/07-dynamic-dag-replanning-mechanics.md`](digested/07-dynamic-dag-replanning-mechanics.md) | ✅ 已判读 | L2 拓扑自愈实操：局部子图切片替换（Sub-graph Splicing）与防死锁单调收敛算法 |
| [`digested/08-superagent-harness-deerflow-langgraph.md`](digested/08-superagent-harness-deerflow-langgraph.md) | ✅ 已判读 | 工业落地样本解剖：字节跳动 DeerFlow 2.0 与 LangGraph 衍生架构——确立“外层传统程序控流程、内层智能体干活”与 Docker 沙箱闭环 |
| [`digested/09-meta-graph-vs-dynamic-task-dag.md`](digested/09-meta-graph-vs-dynamic-task-dag.md) | ✅ 已判读 | 血泪反思：纯动态编译的生产陷阱与“固定元图+动态任务DAG”终局——解决检查点失效、Trace观测性崩溃与元状态抖动 |
| [`result/landscape.md`](result/landscape.md) | ✅ 过筛综述成稿 | 工业级 Graph Engineering 全景架构白皮书（含 2026 顶级模型攻防、子图切片、DeerFlow 超级底座与元图数据分离终局架构） |

## 下一步

1. 持续跟踪开源领域具有动态 DAG 生成与重规划能力的新兴框架（关注 Raven A2A 的后续迭代、LangGraph 的时间旅行工业案例）。
2. 深挖 Session 外外部状态机在大型工程团队落地时的持久化开销与调试工具链（如类似 Temporal Web UI 的 Agent 运行观测平台）。
3. 补充更多一线关于异构模型（如 Opus 5.5 vs Grok 4.7）在多 Agent 拓扑中的沟通策略调优案例。

## 缺口

1. 缺少针对百个节点以上大规模超长程 DAG 运行中状态膨胀（State Bloat）的量化测量数据。
2. 动态 DAG 重新规划（L2 拓扑自愈）目前多依赖启发式 Prompt 或特定模型能力，尚缺乏形式化验证工具保障改图后的可终止性。

## 铁律速记

- **定调在 `README.md` §1。**
- **Node 内部是 Harness + Loop；Node 之间是 Graph / DAG。**
- 一手引据留在 `raw/`，深度机理判读在 `digested/`，综合结论收敛于 `result/`。
- 不搞凭空臆测，每个判断都基于开源工程实践、权威一手发声或一线工程师真实手感。
