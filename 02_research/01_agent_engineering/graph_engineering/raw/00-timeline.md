# raw/00-timeline.md — Graph Engineering 演进与关键事件时间线

> **维护约定**：Append-only。每条记录包含：明确时间、事件发起人/机构、核心事件、一手证据出处、证据强度评级（[S] 一手代码/官方发布；[A] 权威专家/KOL公开表态；[B] 一线同行工程实录；[C] 二手报道/转述）。

---

## 时间线谱系

### 2023 年（Prompt Engineering 时代）
- **事件**：GPT-4 发布与单轮提示词爆发。
- **核心焦点**：System Prompt、Few-shot、Chain-of-Thought (CoT)。
- **瓶颈**：单轮 Token 限制，无法处理长程任务与代码库上下文。
- **强度**：`[S]` 行业通识。

### 2024 年 – 2025 年中（Context Engineering 时代）
- **事件**：1M+ 长上下文模型商用化、向量数据库 RAG、代码库 AST 结构化索引。
- **核心焦点**：上下文拼接、知识检索注入、Prompt Caching。
- **瓶颈**：“迷失在中间（Lost in the Middle）”、注意力衰减，塞入再多上下文模型依然无法在真实执行中闭环。
- **强度**：`[S]` 行业通识。

### 2025 年末 – 2026 年初（Harness Engineering 时代）
- **事件**：Anthropic 推出 MCP（Model Context Protocol）、Engelberg Retreat 2026 正式定调脚手架工程。
- **核心焦点**：把约束写进运行环境。建立沙箱隔离、代码执行门禁、环境状态清理与漂移抹除。确立“模型不够，脚手架（Harness）来凑”。
- **瓶颈**：单步调用的环境虽然干净安全，但模型无法自主根据测试反馈自愈。
- **强度**：`[S]` MCP Spec & Engelberg 2026 纪要。

### 2026 年 6 月（Loop Engineering 时代）
- **事件**：2026-06-30 Andrew Ng 公开发帖定名 Loop Engineering，倡导从单次调用走向自主闭环（Plan-Execute-Verify-Retry）。
- **核心焦点**：停止条件（Stop Conditions）、机器可核判据（Machine Gates）、有限退避重试、三环反馈理论。
- **瓶颈**：单体 Agent 循环运行到 10~20 轮后，由于无法物理隔离子任务，上下文迅速腐烂，陷入 Doom Loop（死循环反驳），无法胜任百文件级别的跨模块系统工程。
- **强度**：`[A]` Andrew Ng 2026-06-30 官方帖。

### 2026 年 7 月 18 日（Graph Engineering 命名与行业破局发问）
- **事件**：Peter Steinberger（OpenClaw 创作者）在 X 公开发出破局提问：
  > *"Are we still talking loops or did we shift to graphs yet?"*
- **反响**：在工业界和 AI 架构师圈层引发剧烈地震。LangChain 创始人 Harrison Chase、各大 Agent 开源作者、工业自动化工程师纷纷入局讨论。
- **核心共识雏形**：单体 Loop 在复杂工程中必死；真正的生产级系统必须引入图拓扑（DAG 与 Cyclic Graph）、显式状态机与多 Agent 组织分工。
- **强度**：`[A]` Peter Steinberger X 原始讨论串。

### 2026 年 8 月（状态机与工作流工业界整合）
- **事件**：LangGraph 发布大规模企业生产案例，Temporal 等微服务工作流引擎被大量集成到 Agent 外层调度。
- **核心观点**：Harrison Chase 指出“Graph 与 Loop 不是对立的”，宏观上是有向图或状态机（前驱后继、审批门禁），微观上每个 Node 是一个包含有限重试的 Loop。
- **强度**：`[S]` LangGraph Release Notes & Case Studies.

### 2026 年 10 月 1 日（一线工程实践爆发：摒弃自由聊天与分层自愈实证）
- **事件**：EverMind-AI/Raven 开源框架 A2A 协作层开发者与社区一线工程师（Jarvan 日成、Willis、Ethan 等）展开技术交流。
- **核心结论**：
  1. 彻底否定“多 Agent 聊天（Chat-based）”作为生产方案（极其昂贵、Token爆炸、无收敛性）；
  2. 确立“DAG 状态机”推进机制；
  3. 确立“两层分级自愈”机制（Worker 局部有限重试退避 + 编排者改 DAG 重试）；
  4. 揭示异构模型汇报冲动差异（Opus 5.5 / Gemini 6 Astra 具备收敛性，Grok 4.7 频繁汇报导致两小时烧光 Heavy 配额）；
  5. 明确 DAG 是人类工程岗位分工与交付物审批的同构代码化。
- **强度**：`[B]` 2026-10-01 技术社区一线交流实录与 Raven 开源仓库代码。
