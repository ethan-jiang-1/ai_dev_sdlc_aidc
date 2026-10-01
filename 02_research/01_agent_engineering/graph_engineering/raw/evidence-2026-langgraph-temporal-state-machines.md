---
type: evidence_record
category: graph_engineering
date: 2026-08-15
status: verified
evidence_level: S
source_channel: official_documentation_and_benchmarks
participants:
  - LangChain / LangGraph Team
  - Temporal Technologies
topics:
  - Stateful Cyclic Graphs
  - Durable Execution (持久化执行)
  - Time-traveling & Human-in-the-Loop
  - Event Sourcing 状态溯源
  - Saga 模式与事务补偿
---

# raw/evidence-2026-langgraph-temporal-state-machines.md — 工业运行时底座：LangGraph 与 Temporal 状态机实践

> **观测时间**：2026 年中  
> **数据源**：LangGraph 架构规范、Temporal AI Workflow 白皮书、生产级 Agent 调度引擎源码

---

## 1. LangGraph：Stateful Cyclic Graph 规范

### 核心机制拆解：
1. **状态定义（State Schema）**：
   - 全局状态通过强类型结构（如 Pydantic BaseModel 或 TypedDict）定义；
   - 支持字段级 **Reducer**（例如：`messages: Annotated[list, add_messages]`，表示新消息追加而非全量覆盖；或者工件字段的更新替换）。
2. **条件边（Conditional Edges）**：
   - 图流转不依赖写死的前进顺序，而是通过计算函数（Decision Function）检查当前 State，动态决定下一跳节点名或终止标记（`END`）。
3. **持久化检查点（Durable Checkpointing）**：
   - 每一个节点执行完毕，状态机将完整的 Snapshot 写入 Checkpointer 存储（如 Postgres、Redis、Sqlite）；
   - **时间旅行（Time-traveling）**：允许开发者回溯到历史任一版本，人工篡改状态变量后从该历史分支重新分叉执行；
   - **人机在环（HITL Interrupt）**：通过 `interrupt_before` 或 `interrupt_after` 在敏感节点前挂起，等待外部审批信号（Approve/Reject）。

---

## 2. Temporal：分布式高可靠确定性执行（Durable Execution）

在大型企业生产级场景中，Python 原生图引擎常因进程崩溃、断网或长时间挂起（数天级审批）而面临状态丢失。许多高严苛团队引入 Temporal 作为图工程的外层控制底座：

### 核心机制拆解：
1. **Workflow as Graph（代码即拓扑）**：
   - 编排逻辑编写为纯确定性 Python/Go 代码（工作流内不允许存在非确定性随机数或裸网络 I/O）；
   - 每一个 Agent 调用、Tool 执行、代码测试均被封装为 **Activity**。
2. **事件溯源（Event Sourcing）**：
   - 引擎只记录历史事件日志（ActivityScheduled, ActivityCompleted, SignalReceived）；
   - 当编排服务重启或发生故障，Temporal 通过瞬时重放事件流恢复精确的图执行上下文，真正实现“长生不老的工作流”。
3. **Saga 模式与分布式补偿**：
   - 当 Worker 节点在下游发生不可逆错误且编排者判定无法自愈时，触发 Saga 补偿事务（例如：自动回滚 Git 分支、释放占用的测试环境沙箱、清理外部数据库临时表）。
