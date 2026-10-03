# 01_seed_reference/graph_engineering — Graph Engineering & DAG 拓扑编排（种子库）

**定位**：围绕 **2026-07 起爆发的 Graph Engineering（图工程）与 DAG 状态机编排** 的初始种子物料、一手源汇编与广泛权威观点库。

> **背景**：在经历 Prompt Engineering（2023）、Context Engineering（2024–2025）、Harness Engineering（2025–2026）和 Loop Engineering（2026-06）之后，单智能体自主循环遭遇了“上下文腐败”、“死循环打转”与“缺乏确定性门禁”的上限。2026 年 7 月起，业界工程重心从“单体智能体的闭环自治”外延扩展为**“显式图拓扑、状态机编排与异构多 Agent 协作（Graph Engineering）”**。

---

## 目录一览

| 文件 | 核心内容 | 关键看点 |
|---|---|---|
| [`01_origins_and_timeline.md`](01_origins_and_timeline.md) | **命名起源与时间线** | 2026-06 Loop 到 2026-07-18 Peter Steinberger 关键一问；五层演化光谱；工业界大论战 |
| [`02_dag_vs_loop_mechanisms.md`](02_dag_vs_loop_mechanisms.md) | **核心机制拆解** | DAG 状态机 vs 自由聊天；两层自愈机制（Worker 局部 Loop + 编排者改 DAG 重试）；Session 内外架构之争 |
| [`03_influential_perspectives.md`](03_influential_perspectives.md) | **前沿权威声音汇编** | Harrison Chase（LangChain/LangGraph）、Anthropic 工作流设计模式、Peter Steinberger（OpenClaw）、Andrew Ng |
| [`04_frameworks_and_ecosystem.md`](04_frameworks_and_ecosystem.md) | **主流框架与工程实践** | LangGraph（Stateful Cyclic Graph）、LlamaIndex Workflows、EverMind-AI/Raven（A2A 协作层）、Temporal 状态机思想 |
| [`05_field_exchange_20261001.md`](05_field_exchange_20261001.md) | **一线真实工程对话实录** | 2026-10-01 开发者交流：DAG 合法校验、有限退避重试、业务岗位映射、模型异构性汇报摩擦 |

---

## 核心架构大图：从 Loop 到 Graph

```text
               ┌────────────────────────────────────────────────────────┐
               │          Shared State / Blackboard (全局状态机)         │
               └───────────────────────────┬────────────────────────────┘
                                           │
          ┌─────────────────┐      ┌───────▼────────┐      ┌─────────────────────────┐
          │  Planner Node   │ ───► │  Task DAG Gen  │ ───► │  Worker Node A (Loop)   │
          │ (编排/架构设计)  │ DAG  │  (拓扑合法校验) │      │ (Harness环境+局部重试)   │
          └─────────────────┘      └────────────────┘      └────────────┬────────────┘
                                           │                            │
                                           │ Fan-out 并发               │ Fan-in 汇聚
                                           ▼                            ▼
                                 ┌──────────────────┐      ┌─────────────────────────┐
                                 │Worker Node B(Loop│ ───► │ Integration & Test Gate │
                                 │(专职编码/子任务) │      │ (确定性函数: pytest/lint)│
                                 └──────────────────┘      └────────────┬────────────┘
                                                                        │ Pass
                                                                        ▼
                                                           ┌─────────────────────────┐
                                                           │   HITL Checkpoint 门禁  │
                                                           │      (人机协同审批)      │
                                                           └─────────────────────────┘
```

---

## 一句话边界分工

- **Harness Engineering** 管**“环境”**（约束写进环境，单次调用的工具/沙箱脚手架）；
- **Loop Engineering** 管**“局部自愈”**（节点内部的 Think-Act-Observe、有限退避重试与停止条件）；
- **Graph Engineering** 管**“全局拓扑”**（节点之间的 DAG 依赖、分支与合并、条件路由、全局状态机与组织级治理）。

> **总结：Node 内部是 Harness + Loop；Node 之间是 Graph / DAG。**

---

## 收录纪律与追踪候选

> 2026-10-03：原 `01_seed_reference/graph_engineering/` 集合整体并入本目录——其一线交流实录即 [05_field_exchange_20261001.md](05_field_exchange_20261001.md)（此前为逐字重复件），命名事件与五层光谱见 [01_origins_and_timeline.md](01_origins_and_timeline.md)，机制拆解见 [02_dag_vs_loop_mechanisms.md](02_dag_vs_loop_mechanisms.md)。收录纪律沿用 [`../kol/README.md`](../voices/README.md) 的一手源铁律；理论与机制研究在 [`../../02_research/01_agent_engineering/graph_engineering/`](../../02_research/01_agent_engineering/graph_engineering/)。

**追踪候选**：
- Peter Steinberger（OpenClaw 创作者，2026-07 讨论引爆者）
- LangGraph / 状态机工作流代表性工程实践
- AI-native SDLC 中基于 DAG 的任务规划与合并机制
