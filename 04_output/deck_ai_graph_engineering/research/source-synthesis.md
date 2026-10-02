---
title: Phase 0 — Graph 治理与图工程素材合成
stage: phase_0
status: completed
created: 2026-10-02
source:
  - 02_research/01_agent_engineering/graph_engineering/result/landscape.md
  - 02_research/01_agent_engineering/graph_engineering/digested/01-09
  - 02_research/01_agent_engineering/graph_engineering/harness_langgraph_ecosystem/
  - 02_research/01_agent_engineering/graph_engineering/harness_frontier_systems/
  - 03_practice/graph_governance/result/backbone.md
  - 03_practice/graph_governance/result/manual.md
feeds_into:
  - intro/outline/outline-intro.md
  - advanced/outline/outline-advanced.md
---

# Phase 0：素材合成（Graph Engineering & Governance）

> 信号从成稿抽，不从回源档案另起主张。逐字引句与代码分析留在研究层与实践层。
> 本文件回答：这场 keynote 可以讲什么、不能讲什么、对客要怎么说。

---

## 1. 可以上屏的核心信号

### 1.1 核心定义与演进必然
- **单体 Loop 的尽头**：长程任务（如跨模块功能开发、系统重构）必然遭遇单 Agent 的**上下文腐朽（Context Rot）、注意力稀释、缺乏物理隔离与反驳死锁（Doom Loop）**。单 Agent 跑微循环无法承担组织级研发。
- **图治理的本质**：Graph 层管“多节点协同与拓扑推进”——定义谁先谁后（依赖）、工件如何契约化交接（接口）、全局状态由谁推进（状态机）、失败如何跨节点动态自愈（L2 拓扑切片）。
- **一句话公式**：Node 内部是 Harness + Loop；Node 之间是 Graph / DAG；驱动边转移的是 Goal / Eval。

### 1.2 工业终局：固定元图（Meta-Graph）+ 动态任务数据（Task DAG as Data）
- **批判学院派动态编译**：大模型运行时现场写 Python 代码（`builder.add_node / compile()`）被证明是生产反模式：导致 Checkpointer 检查点断裂、监控 APM 崩溃、诱发全图推翻的元死锁（Meta Doom Loop）。
- **双轨解耦架构**：
  - **外层元图（Meta-Graph）**：100% 确定性硬编码（Planner / Dispatcher / Worker / Reviewer / Aggregator），静态编译一次；
  - **内层任务数据（Task DAG as Data）**：大模型动态生成与修改的是 `State.task_dag` 字典中的结构化数据。改图本质是“对状态数据做外科手术”，外层代码结构纹丝不动。
  - **实证支撑**：字节跳动 DeerFlow 2.0（两节点极简元图）、LangGraph 原生 `Send()` API 与 Temporal 子工作流。

### 1.3 状态机分层：Session 内短期执行 vs Session 外持久化运行时
- **分界线**：区分 Demo 原型与工业级生产系统的关键分水岭。
- **Session 内（Ephemeral）**：单次推理与短程工具调用，消费干净上下文，产出工件后销毁沙箱，禁止长程跨阶段状态驻留。
- **Session 外（Durable）**：外部强可靠引擎（Temporal 或带持久化 Checkpointer 的 LangGraph），负责 100% 确定性流转、跨天跨周长程挂起等待人类审批、进程崩溃后的原位事件溯源重放（Event Sourcing Replay）。

### 1.4 工件契约与共享黑板：彻底消灭自然语言群聊
- **批判伪 Multi-Agent 群聊**：不同 Agent 在同一个会话里自由聊天是成本与确定性的灾难（Token 二次方爆炸、幻觉相互放大）。
- **强类型工件契约（Typed Artifacts）**：节点间零自然语言对话，仅通过强 Schema 校验的工件交接（TaskSpec、PatchManifest、TestReport）。未通过校验直接阻断，绝不污染下游。
- **共享黑板（Blackboard）与物理隔离**：全局单一事实来源，遵循单写多读（Single-Writer, Multi-Reader）；并发 Worker 必须在独立的 **Git Worktree** 或 Docker 沙箱中物理隔离执行。

### 1.5 两层自愈协议（Two-tier Self-Healing）
- **L1 局部微循环（Loop 层）**：Worker 在物理沙箱内进行有限退避重试（Hard Cap ≤ 3 次），以客观机器命令（`pytest`, `tsc`）为绝对闸门。
- **升级信封（Failure Envelope）**：L1 耗尽或发现前置条件矛盾，Worker 格式化抛出强类型错误信封，停止盲目重试。
- **L2 全局拓扑自愈（Graph 层）**：
  - **绝对冻结成功节点**：成功的节点及其工件不可变（Immutable）；
  - **三大原子切片替换（Sub-graph Splicing）**：`INJECT_PRE_NODE`（前置补丁注入）、`SPLIT_AND_DEGRADE`（任务分裂降级）、`ROLLBACK_AND_AMEND`（回滚修订）；
  - **防死锁硬约束**：L2 重排预算 ≤ 2 次；同类错误连击直接熔断唤醒人类。
- **汇聚冲突治理（Fan-in Merge Protocol）**：Git 文本冲突由专职临时 Worker 解决；语义隐式冲突由独立的集成回归门禁（Integration Gate）裁定。

### 1.6 2026 SOTA 模型五大病理的机器级防御体系
顶级前沿模型（Opus 5.5, Sonnet 5, Sol, Astra）在图节点中存在自发破坏确定性的病态冲动：
1. **汇报风暴（Chatter Storm）** → 强制 Hook 拦截器，非标准工件阻断并强制重定向；
2. **反驳死锁（Doom Loop）** → 物理单向管道，消灭直接会话，QA 仅出 AST 堆栈；
3. **偷跑假完成（False Done）** → 只读测试挂载与独立干净容器（Clean Container）影子门禁；
4. **越权架构侵占（Scope Creep）** → AST 差异白名单锁，拦截未经授权的文件修改；
5. **长程注意力腐败（Context Rot）** → 编排者无状态算子化重置，不保留历史改图会话。

### 1.7 人机协作（HITL）与安全熔断
- **三级审批门禁**：P0 架构方案门禁（Pre-Code）、P1 破坏性变更门禁（Destructive）、P2 最终集成发布门禁（Release）。
- **熔断不毁灭现场**：熔断时完整冻结沙箱，导出包含 DAG 快照与 AST 堆栈的排错 Bundle，平稳交接人类。
- **图级 Token 与财务双硬上限**：全局硬顶（如 1M Tokens / $10）防止财务灾难。

---

## 2. 坚决不上屏清单（反模式与红线）

1. **坚决不讲“一人公司 / 虚拟公司”**：这属于廉价营销噱头，工程落地只谈组织架构同构与确定性研发流水线。
2. **坚决不把“拓扑复杂”当作“系统成熟”**：画出 50 个互相连接的 Agent 节点不是工程牛逼，而是架构失控。好系统的原则是：能单体 Loop 搞定的坚决不上图，能扁平委派的坚决不上重型 DAG。
3. **不搞现场图编译的代码演示**：不误导听众去写 `builder.add_node` 的动态生成，明确指出那是 Demo 阶段的死胡同。
4. **不使用未复核的 KOL 署名**：引用观点时保留完整作者、出处与时间（如 Peter Steinberger 2026-07 发问、Harrison Chase 状态机论断、Armin Ronacher 对自由聊天的批评）。

---

## 3. 对客表达转化（研究术语 → Keynote 讲法）

| 研究/实践层术语 | Keynote 对客生动讲法 | 为什么这么说 |
|---|---|---|
| Meta-Graph + Data DAG | **“外层是铁打的规章制度，内层是流动的任务工单”** | 听众立刻理解程序不变、数据在流动的解耦本质 |
| Typed Artifact Contract | **“消灭微信工作群，只认带章交付物”** | 击中企业痛点：群聊里全是“收到/好的”，最后代码合不进生产 |
| Sub-graph Splicing | **“局部微创手术，不推翻重来”** | 形象解释为什么绝不能因为一个子任务失败就重新规划全图 |
| Ephemeral vs Durable | **“打工人干完就下班，档案库长生不老”** | 通俗说明为什么执行沙箱要用完即毁，而外部状态机要持久化 |
| Failure Envelope | **“带着病历卡向上求援”** | 说明 Worker 停机时不能只喊失败，必须带结构化 AST 诊断数据 |

---

## 4. 承重证据与一手锚点速查

- **Peter Steinberger（2026-07-18）**：“我们什么时候才能告别单上下文死循环，走向真正的 DAG 状态机编排？”（图工程思潮发端）
- **Harrison Chase（LangChain/LangGraph）**：“多智能体系统的本质不是自治代理自由恋爱，而是显式有向图与确定性持久化状态机。”
- **Temporal 官方工业白皮书**：“Non-deterministic Agent activity + Deterministic Durable Workflow.”
- **字节跳动 DeerFlow 2.0 源码**：“外层仅保留 Coordinator 与 Worker 两个确定性静态节点，内层调度 Docker 实例。”
- **Anthropic 官方（2026-03）**：“Orchestrator-Workers、Routing、Parallelization、Evaluator-Optimizer 五大拓扑模式。”
