# Graph Governance —— Graph 层的实践主干

> **定位（2026-10-02 用户定）**：五层框架（Prompt → Context → Harness → Loop → **Graph**）第 5 层的实践主题——
> 治理 **多智能体拓扑编排、强类型工件契约、状态机推进与两层自愈体系**：
> 拓扑依赖（DAG 分支/扇出/汇聚）、工件契约（消灭自然语言群聊）、状态机分层（Session 外部持久化运行时）、
> 两层自愈协议（L1 局部微循环与 L2 局部子图切片替换）、异构模型病态防御与人机协作（HITL）门禁。
>
> **命名理由**：不沿用 KOL 词 "graph engineering"——在研究层该词被作为技术思潮与机制进行横向剖析；
> 在实践层，核心关注的是**工程落地中的确定性控制与反腐败规范**。按仓库五层框架命名，
> 与 [`../harness_governance/`](../harness_governance/README.md) 和 [`../loop_governance/`](../loop_governance/README.md) **同构成对，合称三层治理闭环（Governance Triad）**：
> - **`harness_governance`（环境轴）**：单次运行受控——约束写进物理沙箱（门禁 / 传感器 / 漂移清理）；
> - **`loop_governance`（控制轴）**：单节点迭代受控——循环怎么跑、停止条件、外层调度、人在哪一站；
> - **`graph_governance`（拓扑轴）**：多节点协同受控——拓扑依赖流转、工件契约交付、状态机持久化推进、全局自愈重排。
> 机制证据权威在 [`02_research/01_agent_engineering/graph_engineering/`](../../02_research/01_agent_engineering/graph_engineering/README.md)。

## 一句话分界

**沙箱是环境的边界（Harness），重试是节点的微循环（Loop）；跨节点依赖谁先谁后、工件如何契约化交接、失败时如何切片局部图自愈，是 Graph 的治理。**

## 目录结构

```text
graph_governance/
├── README.md            # 你在这里：定位 / 命名 / 分工 / 信息流
├── CURRENT.md           # 热区：当前态 / 下一步 / 缺口 / 铁律速记
└── result/
    ├── README.md        # 入层判据与命名规则
    ├── backbone.md      # ★ 实践主干（§0 定义与判据 / §1 拓扑双轨骨架 / §2 状态机分层 / §3 工件契约与黑板 / §4 两层自愈协议 / §5 2026模型病态防御 / §6 HITL与熔断）
    └── manual.md        # ★ 操作规程（§0 诊断自检 / §1 运行时选型决策 / §2 Schema 规范 / §3 子图切片突变 SOP / §4 角色配额隔离 / §5 机器级防御实施 / §6 落地梯子 P0-P3 / §7 反过度工程警告）
```

**没有 `research/` 层**：图工程机制、一线实证档案与 9 大核心议题判读在 [`02_research/01_agent_engineering/graph_engineering/`](../../02_research/01_agent_engineering/graph_engineering/README.md)；生态样本剖析在 `harness_langgraph_ecosystem/` 与 `harness_frontier_systems/`。本主题只引用其成熟结论与控制接口，不复制研究正文，确保单一事实来源。

## 分工边界（与兄弟主题，冲突时以本表为准）

| 主题 | 它管 | 本主题不管 |
|---|---|---|
| [`harness_governance`](../harness_governance/README.md) | 单次运行受控：沙箱环境、门禁工具、上下文漂移清理（环境轴） | 节点内的自主微循环（→loop）；跨节点的拓扑依赖与多 Agent 调度（→本主题） |
| [`loop_governance`](../loop_governance/README.md) | 单节点内部多轮迭代受控：停止条件、退避重试、自主度阶梯（控制轴） | 跨节点的拓扑依赖流转、A2A 工件契约、全局状态机与 L2 动态图自愈（→本主题） |
| **本主题** | **多节点系统的拓扑与状态机治理**：元图与任务数据分离、强类型工件交接、L2 局部子图切片、模型病态防御、HITL 门禁 | 节点内部的微循环算法（→loop）；单节点沙箱执行脚手架（→harness）；需求/规格编写语法（→requirements/spec） |
| [`spec_driven_development`](../spec_driven_development/README.md) | SDD 工具生态与工件生命周期规范 | 动态图执行时的状态机运行时与异常恢复（→本主题） |

## 核心主张速览（展开在 [`result/backbone.md`](result/backbone.md)）

1. **单体 Loop 的尽头是 Graph 治理**：长程任务中单 Agent 的单一上下文必然遭遇注意力腐蚀与反驳死锁；工程落地必须通过显式有向图拓扑（DAG / Cyclic Graph）与状态机实现物理隔离。
2. **彻底消灭自然语言群聊，全面确立强类型工件契约**：让不同 Agent 在同一个会话里自由聊天是成本与确定性的灾难；生产级系统的节点间只交接通过模式校验（Schema Validated）的强类型交付物（Spec JSON、Git Patch、测试报告）。
3. **“固定元图（Meta-Graph）+ 动态任务数据（Task DAG as Data）”工业终局**：外层状态机是 100% 确定性的静态编译程序；大模型只在局部充当算子，负责动态生成或修订状态中的任务清单数据，严禁内存现场重新编译代码图。
4. **两层分级自愈协议（Two-tier Self-Healing）**：
   - **L1 局部微循环（Loop 层）**：Worker 在物理沙箱内进行有限退避重试（Hard Cap ≤ 3 次），以客观命令（pytest/tsc）为闸门；
   - **L2 全局拓扑自愈（Graph 层）**：Worker 抛出强类型 `Failure Envelope`，编排者**绝对冻结成功节点**，只针对失败节点执行**局部子图切片替换（Sub-graph Splicing）**（前置注入、任务降级、检查点回滚）；限制全局重排预算（Max Replanning ≤ 2）。
5. **Session 外部独立状态机运行时**：核心生产链路必须从易碎的“Session 内 Tool 调用”迁移至“Session 外外部持久化状态机（如 Temporal / 数据库黑板）”，保证崩溃可重放、状态长生不老、审计可追踪。
6. **2026 SOTA 模型五大病理的机器级硬核防御**：针对顶级模型的汇报冲动、死锁反驳、幻觉假完成、跨权写入与长上下文注意力腐朽，建立非模型依赖的确定性 Hook 拦截、只读影子门禁与物理 Worktree 隔离。

## 信息流

1. **单向加工**：对应研究主题的 evidence / digested → 本主题 result（backbone + manual）；review 若修正实践主干 → 反向核对并同步研究层判读。
2. **result/ 只收过筛结论**：必须具备真实工业级系统落地佐证（如 LangGraph, Temporal, 字节 DeerFlow, Claude Code 等）；反例与纯理论设想明确标注。
3. **过程件不入流**：遵循仓库根 `.tmp-` 纪律。
