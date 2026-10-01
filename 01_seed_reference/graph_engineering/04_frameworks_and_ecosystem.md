# 04. 典型框架、工程实践与生态矩阵

---

## 1. 代表性框架及其架构哲学

### ① LangGraph（LangChain 出品）
- **核心定位**：专为带有循环（Cycles）与状态管理的多智能体系统设计的图引擎。
- **关键设计**：
  - **StateGraph（状态图）**：强类型定义的全局 State，支持声明字段的 Reducer（如追加、覆盖、合并）；
  - **Conditional Edges（条件边）**：根据节点返回结果动态决定下一跳；
  - **Durable Checkpointing（持久化检查点）**：每一步状态均落盘，原生支持 Time-travel（时间旅行调试）与人机在环中断恢复（Interrupt & Resume）。

### ② Temporal / Cadence（微服务工作流哲学的 AI 迁移）
- **核心定位**：分布式高可靠确定性工作流引擎。
- **关键设计**：
  - 将每个 Agent 执行封装为一个 **Activity**，整个编排逻辑编写为纯确定性的 **Workflow** 代码；
  - 即使 Worker 崩溃、超时、断网，引擎也能通过事件重放（Event Sourcing）完全恢复图执行状态；
  - 工业界共识：在最严苛的生产环境中，许多团队放弃纯 Python 玩具图框架，直接选用 Temporal 作为外层 Graph 调度器。

### ③ LlamaIndex Workflows（事件驱动图）
- **核心定位**：事件驱动（Event-driven）的声明式异步图。
- **关键设计**：
  - 不强制画显式的边，而是通过 `@step` 装饰器监听事件（Event Emit & Listen）；
  - 事件的流动隐式构成了有向拓扑，天然支持多智能体异步解耦与扇出。

### ④ EverMind-AI/Raven（A2A 协作层与多智能体网络）
- **核心定位**：面向异构 Agent 的去中心化/多主协作框架。
- **关键设计**：
  - 摒弃简单主从架构，提供标准化的 **A2A（Agent-to-Agent）协议层**；
  - 编排者生成带合法性约束的 DAG 拓扑，Worker 节点基于状态机推进，避免无序闲聊。

---

## 2. 框架选型与机制对比矩阵

| 特性维度 | LangGraph | Temporal + Custom Agent | LlamaIndex Workflows | Raven (A2A 拓扑) |
|---|---|---|---|---|
| **图结构支持** | DAG + 任意循环图 (Cycles) | 确定性代码流 (代码即 DAG/图) | 事件驱动隐式拓扑 | DAG 任务图 + 状态机 |
| **状态持久化** | 数据库/键值 Checkpointer | 事件溯源 (Event Sourcing) | 内存 / 外部上下文 | 分布式状态机与节点契约 |
| **局部自愈 (L1)** | 支持节点内重试与后备分支 | 原生 Activity 重试策略 | 需节点内自行捕获 | 有限退避与重试机制 |
| **全局自愈 (L2)** | 重新路由到规划节点 | 工作流级补偿（Saga 模式） | 发送重规划事件 | 编排者动态改图重新调度 |
| **HITL 人机在环** | 原生 `interrupt_before/after` | 原生 Signal & Query | 异步等待事件 | 节点级挂起审批 |
| **适用场景** | 复杂多角色交互、长程研究/编码 | 严苛企业生产、分布式流水线 | 数据检索管道与多工具流 | 异构模型协作与专业分工 |

---

## 3. 在 AI Coding 中的实践蓝图（从需求到 PR 的标准 DAG）

```text
[1. PRD / Issue 入口]
        │
        ▼
[2. Spec & Architecture Node] ── (生成系统设计规范)
        │
        ▼
[3. Task DAG Planner Node]   ── (将任务解耦为拓扑依赖子图)
        │
        ├──────────────────────┬──────────────────────┐
        ▼                      ▼                      ▼
  [4a. 数据层变更]       [4b. 业务逻辑实现]     [4c. 前端 UI 组件]
  (Worker Loop 编码)    (Worker Loop 编码)    (Worker Loop 编码)
        │                      │                      │
        └──────────────────────┼──────────────────────┘
                               │ (Fan-in 汇聚)
                               ▼
                   [5. 集成编译与单元测试节点]
                     (确定性门禁: pytest/tsc)
                               │
                ┌──────────────┴──────────────┐
                │ Pass                        │ Fail
                ▼                             ▼
     [6. 安全与规范扫描 Gate]        [触发 L1 退避修补 或]
                │                   [L2 编排者重排 DAG]
                ▼ Pass
     [7. 人机评审 HITL (PR)]
                │
                ▼ Approved
     [8. 部署交付 / Merge]
```
