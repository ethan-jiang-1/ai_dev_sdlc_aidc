# graph_engineering — 拓扑编排、多智能体工作流与状态机研究

**定位**：围绕 Agent 复杂有向图调度（DAG）、工作流编排、状态机控制与多智能体拓扑链路的机制研究。

## 核心关注

- **拓扑/状态机维**：从单一线性循环跨入复杂有向图编排、多步骤分支与合并。
- **通信与状态沉淀**：智能体之间的消息契约、共享工作区与全局状态机持久化。
- **与兄弟主题的分工**：
  - 本主题管**拓扑结构与多步路由**；
  - [`../loop_engineering/`](../loop_engineering/README.md) 管**单节点/局部的循环迭代与停止条件**；
  - [`../goal_eval_engineering/`](../goal_eval_engineering/README.md) 管**驱动链路流转的目标与评估判定**；
  - [`../harness_engineering/`](../harness_engineering/README.md) 管**单节点/环境级别的约束与工具脚手架**。

## 种子与素材入口

- 一手声音与事件种子：[`../../../01_seed_reference/reference/kol/_raw_graph_engineering/`](../../../01_seed_reference/reference/kol/_raw_graph_engineering/README.md)
  - 命名事件：2026-07 Peter Steinberger 提出 *"From Loops to Graphs"*
  - 一线样本：DAG 状态机替代多 Agent 聊天、Worker 有限退避重试与编排者改 DAG 重试的分层自愈机制

