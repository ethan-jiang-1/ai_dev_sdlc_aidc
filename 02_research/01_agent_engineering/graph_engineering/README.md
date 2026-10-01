# graph_engineering — 拓扑编排、状态机控制与多智能体图工程

**定位**：围绕 **2026-07 起爆发的 Graph Engineering（图工程）**——从单体 Agent 的局部死循环和上下文腐败，走向显式 DAG/拓扑图、状态机治理与异构多智能体协作机制研究。
研究层·分析，不是单一工具操作手册（分工见 §2）。

**分法**：`raw/`（一手素材/档案/台账）→ `digested/`（议题深度消化与判读）→ `result/`（过筛成稿综述）。
双轴独立增长：**轴一「人/框架/实证」＝台账加一行；轴二「工程问题」＝加一个议题编号文件。**

```text
graph_engineering/
├── README.md                  # 你在这里：定调 / 边界 / 架构 / 增长规则
├── CURRENT.md                 # 热区：做到哪、下一步动哪个文件、缺口
│
├── raw/                       # 一手层：一手原文/实录 + 时间线/控制面/回源档案
│   ├── 00-timeline.md         #   命名与事件时间线（append-only，每条带日期 + 出处 + 强度）
│   ├── research-plan.md        #   ★ 研究推进控制面：问题树 / 分路 / 质量门 / backlog
│   ├── roster.md              #   ★ 人选、机构与框架台账＝唯一名单权威
│   ├── evidence-20261001-field-exchange.md          # 2026-10-01 一线工程交流回源档案（Raven A2A）
│   ├── evidence-20260718-steinberger-graph-shift.md # 2026-07-18 Peter Steinberger 破局发问与论战
│   ├── evidence-202603-anthropic-workflow-patterns.md # Anthropic 五大工作流拓扑模式一手档案
│   └── evidence-2026-langgraph-temporal-state-machines.md # LangGraph 与 Temporal 状态机实践档案
│
├── digested/                  # 消化层：关键工程问题横向综合判读
│   ├── README.md              #   问题看板：已答 / 在答 / 待答
│   ├── 01-dag-state-machine-vs-free-chat.md         # 议题 01：为什么抛弃“自由聊天”走向“DAG 状态机与强类型工件”？
│   ├── 02-two-tier-self-healing-architecture.md     # 议题 02：两层自愈体系：Worker 局部 Loop vs 编排者动态 DAG 重排
│   ├── 03-session-internal-vs-external-state-machine.md # 议题 03：Session 内 Tool 编排 vs Session 外 外部状态机/运行时
│   ├── 04-artifact-contract-and-blackboard.md       # 议题 04：工件契约、A2A 协议与全局共享黑板状态机
│   └── 05-heterogeneous-model-governance.md         # 议题 05：异构模型拓扑分工与通信治理（汇报冲动与配额约束）
│
└── result/                    # 成稿层
    └── landscape.md           # Graph Engineering 全景技术白皮书（过筛综述）
```

---

## 1. 定调（唯一权威）

> 2026-10-01 定。改本节之前先与用户对齐。其他文件只放指针，不复制本节。

本主题研究**为什么生产级 Agent 系统必须从“单体自主循环（Loop）”走向“显式图拓扑与状态机编排（Graph Engineering）”，以及图工程的核心机制如何运作**。

1. **单体 Loop 的必然上限**：在复杂的长程任务（如大型代码库重构、多模块并发开发、跨业务流水线）中，单 Agent 的自主循环必然面临**上下文腐败（Context Rot）、缺乏物理隔离、死循环反驳（Doom Loop）与无全局视野**。
2. **图工程的核心本质**：
   - 彻底摒弃让不同角色在同一 Context 中自由对话的“伪 Multi-Agent 聊天模式”；
   - 采用**显式有向图拓扑（DAG / Cyclic Graph）与状态机（State Machine）**推进任务；
   - 节点之间只通过**强类型契约工件（Typed Artifacts）**交接，严格实行单任务上下文隔离；
   - **两层分级自愈**：节点内由 Worker 做有限退避微循环（L1 局部自愈）；节点失败后由编排者动态修改 DAG 重试（L2 全局拓扑自愈）。
3. **架构终局与业务映射**：
   - DAG 不是冰冷的算法流水线，而是**人类软件工程组织结构（岗位职责、PR 评审、测试门禁）在机器侧的代码化同构**；
   - 企业级高可靠系统必将从“Session 内 Tool 调用”走向“Session 外独立状态机硬编排（如 Temporal / 外部引擎）”。

---

## 2. 边界与兄弟主题分工

在 `02_research/01_agent_engineering/` 的四维一体控制体系中，各模块严格遵守单一事实来源分工：

| 模块 | 核心维度 | 职责边界 | 与本主题的关系 |
|---|---|---|---|
| **`graph_engineering/`（本主题）** | **拓扑 / 状态机维** | 关注**Node 之间**的图拓扑、依赖流转、分支/扇出/汇聚、全局状态机与组织级治理 | **宏观编排层** |
| [`loop_engineering/`](../loop_engineering/README.md) | **时间 / 迭代维** | 关注**Node 内部**的微循环（Think-Act-Observe）、有限退避重试与停止条件 | 节点内部的 L1 自愈算子 |
| [`harness_engineering/`](../harness_engineering/README.md) | **空间 / 环境维** | 关注**Node 内部**运行时的沙箱隔离、代码执行环境、约束与工具脚手架 | 节点执行的物理环境与工具集 |
| [`goal_eval_engineering/`](../goal_eval_engineering/README.md) | **目标 / 驱动维** | 关注驱动链路流转的 Goal 定义与可量化 Eval 判定闸门 | 状态转移条件边（Edge）的判据来源 |

> **一句话公式：Node 内部是 Harness + Loop；Node 之间是 Graph / DAG；驱动边转移的是 Goal / Eval。**

---

## 3. 核心架构大图与两层自愈速览

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

## 4. 增长规则与双轴扩展

1. **一手素材先行（`raw/`）**：
   - 任何结论必须有一手材料支撑（原帖、访谈、开源代码实现、一线工程实录）；
   - 人物/机构收录进入 `raw/roster.md`，事件入 `raw/00-timeline.md`，深度摘录进 `raw/evidence-*.md`。
2. **议题深度消化（`digested/`）**：
   - 跨框架、跨派别进行机制横向对齐；
   - 针对架构核心矛盾（如 Session 内外之争、异构模型汇报治理）形成编号议题判读。
3. **综述提炼（`result/`）**：
   - 当核心议题收口后，收敛为面向工业落地的高确定性综述文档。
