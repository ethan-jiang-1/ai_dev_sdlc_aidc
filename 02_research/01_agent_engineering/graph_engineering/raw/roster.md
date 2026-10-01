# raw/roster.md — 权威阵营、核心人物与代表性项目台账

> **定位**：Graph Engineering（图工程）研究的唯一名单与项目权威。
> **收录判据**：公开提出关键理论/命题、主导或构建主流生产级图编排框架、或在一线工程落地中贡献核心实证机制者。

---

## 1. 核心人物与思想领袖（Key Figures）

| 姓名 / 标识 | 机构 / 身份 | 核心贡献 / 标志性论断 | 号召力与证据出处 |
|---|---|---|---|
| **Peter Steinberger** | OpenClaw 创作者，知名资深 iOS/系统架构师 | 2026-07-18 发出行业灵魂破局之问：*"Are we still talking loops or did we shift to graphs yet?"*，率先将讨论从单体 Loop 推向 Graph | X 原帖引发全行业 AI 架构师大论战；开源 OpenClaw 实践 |
| **Harrison Chase** | LangChain / LangGraph 联合创始人兼 CEO | 论断“生产级系统必须建立在 Stateful Cyclic Graphs 之上”；提出 Checkpoints、Time-traveling、Scoped State 等图工程控制杠杆 | LangGraph 框架与官方系列技术架构白皮书 |
| **Andrew Ng（吴恩达）** | AI Fund / DeepLearning.AI | 提出 Agentic Workflow 的三环反馈理论（分钟级、小时级、天周级），奠定了跨尺度图调度的理论基础 | 2026 系列公开演讲、Newsletter |
| **Jarvan 日成** | EverMind-AI / Raven 核心开发者 | 主导开发 Raven Agent 的 A2A（Agent-to-Agent）协作层；提出“编排者生成 DAG 图校验 + Worker 局部退避重试 + 编排者改 DAG 重试”两层自愈机制 | 2026-10-01 技术社区一线对话实录；Raven 源码 |
| **Willis** | 一线架构师 / 社区专家 | 提出“DAG 图即业务逻辑，类似于人岗位的对接关系”；指出多 Agent 聊天方案昂贵不可行 | 2026-10-01 技术社区一线对话实录 |
| **Maxim Fateev** | Temporal Technologies 联合创始人兼 CEO | 工作流与 Durable Execution（持久化执行）教父；将事件溯源（Event Sourcing）与高可靠确定性状态机引入 AI 长任务编排 | Temporal 官方架构设计与 AI 工作流落地案例 |
| **Armin Ronacher** | Sentry 首席架构师，Flask 创作者 | 倡导“Agentic State Machines”，主张用显式确定性状态机包装非确定性 LLM 算子，彻底否定黑盒随机游走循环 | Sentry 架构博客与技术播客 |
| **Shawn Wang (Swyx)** | Latent Space 主理人，AI 工程师社区领袖 | 提出 Flow Engineering（流程工程）；倡导确定性代码控制骨架 + 概率性 LLM 节点，论证结构化 Flow 超越单纯大模型能力 | Latent Space 研讨与行业复盘 |
| **Mitchell Hashimoto** | HashiCorp 创始人，Ghostty 创作者 | 论断自动化系统必须将瞬态故障（Transient Failures）视为常态；强调 Durable Workflow 检查点恢复的生产必要性 | 自动化架构系列文章与访谈 |
| **Boris Cherny** | Anthropic 资深工程师，Claude Code 核心架构师 | 主导 Claude Code 终端编排；设计任务解耦、无交互子任务与外部确定性测试工具门禁 | Anthropic 工程系列博客与 Claude Code 实践 |
| **Graham Neubig** | CMU 教授，All-Hands AI / OpenHands 联合创始人 | 开源 OpenHands（原 OpenDevin），提出基于 Event Stream（事件流）的 Planner-Worker 解耦架构与代码评估脚手架 | OpenHands 开源架构与系列基准测试论文 |

---

## 2. 机构与先驱实验室（Organizations & Labs）

| 机构 | 核心产出 / 贡献 | 代表作 / 论文 |
|---|---|---|
| **Anthropic** | 确立 Agentic Workflow 的五大核心拓扑模式（链式、路由、并行、编排-工人、评估-优化），主张“工作流优先于盲目黑盒自治” | 《Building Effective Agents》（官方架构指南） |
| **LangChain** | 研发 LangGraph，开创 Stateful Cyclic Graph 编程模型，支持强类型 State、条件边与持久化 Checkpoint | LangGraph 开源框架与云端运行时 |
| **Temporal Technologies** | 提供分布式确定性状态机引擎，支持百万级 Agent Activity 的调度、补偿（Saga）与故障自愈 | Temporal Workflow SDK |
| **EverMind-AI** | 开发 Raven Agent 及其 A2A 协作层，探索多主去中心化架构与显式 DAG 任务图状态机 | `EverMind-AI/Raven` 开源项目 |
| **LlamaIndex** | 开发 LlamaIndex Workflows，基于事件驱动（Event-driven）隐式拓扑实现异步解耦的多智能体状态流转 | LlamaIndex Workflows |
| **Berkeley AI Research (BAIR)** | 提出“复合 AI 系统（Compound AI Systems）”，论证系统架构与图编排对单体模型的性能超越 | BAIR Research Paper & Blog |
| **All-Hands AI (OpenHands)** | 构建基于 Event Stream 事件总线的开发助手，解耦任务规划与终端执行沙箱 | OpenHands (formerly OpenDevin) |
| **ByteDance (字节跳动)** | 开源 DeerFlow 2.0（超级智能体底座 SuperAgent Harness），深度集成 LangGraph 状态机与 Docker 沙箱执行环境 | `bytedance/deer-flow` 开源项目 |

---

## 3. 代表性框架与生态选型矩阵

| 框架 | 架构模式 | 状态管理机制 | 自愈与重试机制 | 人机协同 (HITL) |
|---|---|---|---|---|
| **LangGraph** | 显式图（Nodes + Conditional Edges），支持循环 | 强类型全局 State + Reducer，Checkpointer 落盘 | 节点内重试 + 边条件重定向 | `interrupt_before/after` 原生断点拦截 |
| **DeerFlow (ByteDance)** | Lead-Subagent 动态任务图 (基于 LangGraph) + Docker 物理沙箱 | 状态机 Checkpoint + 渐进式技能装配 (Skill Registry) | 子任务容器内有限重试 + 主控动态子图重新切片 | 原生集成飞书/Slack/Web 异步审批中断 |
| **Temporal** | 确定性代码即工作流（Workflow + Activities） | Event Sourcing 事件溯源，任意时刻确定性重放 | Activity 自动重试 + Saga 事务补偿 | Signal & Query 原生支持外部人工信号挂起与恢复 |
| **Raven (A2A)** | 编排者生成任务 DAG + 状态机推进 | 节点间强类型交付物契约 + 去中心化状态 | Worker 局部有限退避重试 + 编排者改图重排 | 节点任务级状态挂起与审批 |
| **OpenHands** | Event Stream 事件总线驱动多 Agent | Event Log 顺序日志存储 | 观察反馈循环 + 动作异常捕获 | 交互式终端与 Web 确认门禁 |
| **LlamaIndex Workflows** | 事件驱动隐式拓扑（Event-based Emit & Listen） | 内存 Context / 外部存储挂载 | 依赖 Step 内部捕获重试 | 异步 Event 挂起与等待 |
