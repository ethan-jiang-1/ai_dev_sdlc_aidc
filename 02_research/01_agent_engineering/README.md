# 01_agent_engineering — 智能体工程（运行时与控制机制）

**定位**：围绕 Agent 怎么运行、怎么受控、怎么形成闭环的底层机制研究。四维一体构成智能体控制论（Cybernetics）的完整技术底座。

## 目录分工

| 模块 | 核心维度 | 讲什么 | 入口 |
|---|---|---|---|
| `loop_engineering/` | **时间 / 迭代维** | 循环治理（2026-06 起实践运动，**活跃**）：命名谱系、KOL 实战、构件、停止条件、外层调度与自主度分档 | `raw/kol-roster.md` + `digested/README.md` |
| `harness_engineering/` | **空间 / 环境维** | 环境治理：约束写进环境、规则机器级阻断、沙箱隔离与上下文挂载机制 | `README.md` |
| `graph_engineering/` | **拓扑 / 状态机维** | 拓扑编排（2026-10-01 升级定调，**活跃**）：从单体 Loop 到 DAG 状态机、两层自愈、Session 内外架构与异构治理 | `README.md` §1 + `CURRENT.md` |
| `goal_eval_engineering/` | **目标 / 驱动维** | 目标与评估（**活跃**）：前沿来源如何构造 goal 与 eval，让 loop 跑起来，量化后调优与闭环收敛 | `README.md` §1 + `CURRENT.md` |
| `repo_agent_friendliness/` | **成熟度 / 评估体系** | 仓库 Agent-Friendly **评估系统**（**活跃**）：九维框架 + A/B 分型 + 门禁/加权分离打分体系与测量工具 | `README.md`（体系权威 `10-spec/framework.md`） |
