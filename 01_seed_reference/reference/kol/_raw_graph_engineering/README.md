---
type: index
content_type: readme
directory: reference/kol/_raw_graph_engineering
description: Graph Engineering 一波声音（2026-07 起）——从单循环走向显式拓扑编排与 DAG 的一手素材集合
research_date: 2026-10-01
---

# _raw_graph_engineering — Graph Engineering 一波声音（2026-07 起）

> 本集合收 **2026-07 起**围绕 "graph engineering"、"DAG 拓扑编排"、"From Loops to Graphs" 发声的一手素材与命名种子。
> 它是继 [`_raw_loop_engineering/`](../_raw_loop_engineering/README.md)（2026-06 循环工程）之后的**系统架构级演化波次**。

**分工定位**：
- 本目录是**冷启动种子素材库**：记录这一波发声的事件锚点、核心讨论线索与一手源。
- 理论与机制研究在 [`02_research/01_agent_engineering/graph_engineering/`](../../../../02_research/01_agent_engineering/graph_engineering/README.md)。

---

## 1. 命名事件与背景（2026-07）

- **2026-06（前置波次）**：Andrew Ng 等人推动了 **Loop Engineering**（单体自主循环：Think-Act-Observe、Eval 驱动重试）。
- **2026-07-18（引爆事件）**：Peter Steinberger（OpenClaw 创作者）在 X 上公开提问：
  > *"Are we still talking loops or did we shift to graphs yet?"*
  这一提问迅速在 AI 工程圈引爆讨论，宣告了软件工程焦点从“单循环迭代（Loop）”向“系统拓扑与有向图编排（Graph / DAG）”的外延扩展。

---

## 2. 演进脉络：AI 原生工程五层光谱

在 2026 年中期的业界共识中，AI 工程范式呈现清晰的“层层包裹”递进关系：

| 范式层级 | 出现/成熟期 | 解决的核心问题 | 治理维度 |
|---|---|---|---|
| **1. Prompt Engineering** | 2023 | 单次模型调用的输入表达与质量 | 输入调优（Single Turn） |
| **2. Context Engineering** | 2024–2025 | 上下文窗口管理、RAG 注入、长程记忆装配 | 知识供给（Context & Memory） |
| **3. Harness Engineering** | 2025底–2026初 | 沙箱环境、工具协议（MCP）、状态追踪与漂移清洗 | **环境轴**（约束写进环境） |
| **4. Loop Engineering** | 2026-06 | 单智能体自主循环（Plan-Execute-Verify-Retry）、停止条件、机器闸门 | **控制轴**（局部自愈与迭代） |
| **5. Graph Engineering** | 2026-07 起 | 多智能体拓扑编排、DAG 依赖分解、条件路由、确定性状态机与全局共享状态 | **拓扑/协同轴**（系统级组织与编排） |

---

## 3. 为什么单靠 Loop 走不下去了？（演化驱动力）

1. **上下文腐败（Context Rot / Drift）**：单个 Agent 长时间循环，历史上下文无限膨胀，极易出现注意力漂移与死循环（Doom Loops）。
2. **职责混杂与专业隔离**：单个大模型既当架构师又当编码员还当测试员，无法建立互不信任的“对抗与双检”机制；Graph 通过节点分工实现关注点分离。
3. **确定性治理（Deterministic Governance）**：不能把全流程完全赌在非确定性 LLM 的“自觉”上，必须用显式图结构（有向边、条件路由、阶段检查点 HITL）强制执行工程规范。
4. **并发与扇出（Fan-out / Fan-in）**：单循环本质是串行的，而复杂软件开发需要基于 DAG 的任务并行化（如解耦模块并行实现后汇总合并）。

---

## 4. Graph Engineering 的核心构件

```text
               ┌────────────────────────────────────────────────┐
               │           Shared State / Blackboard            │
               └───────────────────────┬────────────────────────┘
                                       │
      ┌───────────────┐        ┌───────▼────────┐        ┌───────────────┐
      │  Planner Node │ ─────► │ Task DAG Gen   │ ─────► │ Subtask A (L) │
      └───────────────┘  DAG   └────────────────┘        └───────┬───────┘
                                         │                       │
                                         │ Fan-out               │ Fan-in
                                         ▼                       ▼
                               ┌──────────────────┐      ┌───────────────┐
                               │ Subtask B (Loop) │ ───► │  Integration  │
                               └──────────────────┘      │  & Test Gate  │
                                                         └───────┬───────┘
                                                                 │ Pass
                                                                 ▼
                                                         ┌───────────────┐
                                                         │  HITL Review  │
                                                         └───────────────┘
```

- **Nodes（节点）**：
  - **Agent 节点**：专职智能体（Harness 包裹，内部执行特定任务的思考与局部 Loop）。
  - **Deterministic 函数节点**：纯代码执行、测试运行（`pytest`）、静态检查（Linter / Typecheck）。
  - **Gate / Evaluator 节点**：独立裁决节点（验证与干活分离）。
  - **HITL Checkpoint（人在环检查点）**：显式挂起，等待人类批准或调整参数。
- **Edges（边与路由）**：
  - **DAG 依赖边**：前序产物就绪后触发下游（拓扑前向推进）。
  - **Conditional / Feedback Edges（条件与回退边）**：根据判定结果（Pass/Fail）路由回特定节点进行返工自愈。
- **State Machine & Shared State（共享状态）**：
  - 具备版本快照、可追溯、可回滚的全局黑板。

---

## 5. 与兄弟工程的互补关系

- **一句话总结**：
  > **Node 内部是 Harness + Loop；Node 之间是 Graph / DAG。**
- **Harness Engineering** 管**环境**（环境提供工具、沙箱与环境断言）；
- **Loop Engineering** 管**单点自愈**（单个节点或小闭环内的局部迭代与终止）；
- **Graph Engineering** 管**全局拓扑**（多节点之间的拓扑依赖、并发调度、跨阶段流转与组织治理）。

---

## 6. 一手素材与实践样本归档

| 文件 / 样本 | 类型 | 核心内容 | 关联项目/人物 |
|---|---|---|---|
| [`field_exchange_20261001_dag_orchestration.md`](field_exchange_20261001_dag_orchestration.md) | 一线技术交流实录 (2026-10-01) | 拒绝多 Agent 自由聊天、改用 DAG 状态机推进；Worker 有限退避重试（Loop）与编排者改 DAG 重试（Graph）的分层自愈；Session 内 Tool vs Session 外架构之辩 | Jarvan 日成、Willis、李奕晨 Ethan / [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) |

---

## 7. 收录纪律与追踪清单

- 遵守 `reference/kol/README.md` 一手源铁律。
- 跟踪候选对象：
  - Peter Steinberger（OpenClaw 创作者，2026-07 讨论引爆者）
  - LangGraph / 状态机工作流代表性工程实践
  - AI-native SDLC 中基于 DAG 的任务规划与合并机制

