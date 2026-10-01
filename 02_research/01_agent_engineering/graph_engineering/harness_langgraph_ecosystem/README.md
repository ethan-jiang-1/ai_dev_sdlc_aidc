# LangGraph 及其衍生基座生态（Harness LangGraph Ecosystem）

> 本目录对 **LangGraph 原生运行时及其衍生 Agent Harness（Deep Agents、DeerFlow、GPT Researcher 等）** 进行垂直深度解剖，聚焦其在**动态工作流（Dynamic Workflow）与动态 DAG（Dynamic DAG）**上的真实工程落地与架构选型。

---

## 1. 核心问题意识

在探讨“基于 LangGraph 的 Agent Harness”时，工业界普遍经历了一场痛苦的认知纠偏：
1. **伪动态认知陷阱**：直觉上认为动态 DAG 是指在运行时让 LLM 动态调用 Python API 拼接图结构（`builder.add_node()` 并 `builder.compile()`）。在生产环境中，这被证明是灾难性的：**Checkpointer 状态版本映射断裂、Time-travel 时间旅行回溯失效、LangSmith/OpenTelemetry 链路追踪拓扑漂移崩溃、编译冷启动开销巨大**。
2. **真动态工业标准解**：**“固定 Meta-Graph + 状态（State）内 Task DAG 数据结构”**。图的静态骨架（如 Planner -> Dispatcher -> Worker -> Evaluator，或双节点循环）在应用初始化时一次性编译完成；动态性完全由 State 内部的 Task DAG 字典承载，结合 LangGraph 原生的 `Send()` API 或 `Command(goto=...)` 原语进行动态并行派发与拓扑流转。

---

## 2. 目录文件全景

| 文件 | 核心剖析对象 | 核心工程结论 |
|---|---|---|
| [01-langgraph-native-dynamic.md](01-langgraph-native-dynamic.md) | LangGraph 原生动态原语 | 深度解析 `Send()` API（动态 Map-Reduce Fan-out）、`Command(goto=...)` 动态交接与 Compiled Subgraph 隔离调度的底层实现机制 |
| [02-langchain-deepagents.md](02-langchain-deepagents.md) | LangChain 官方 Harness: Deep Agents | 官方标准 Agent 基座如何处理动态任务：`write_todos` 动态规划、`task` 子代理沙箱隔离、虚拟文件系统与上下文挤压防护 |
| [03-bytedance-deerflow.md](03-bytedance-deerflow.md) | 字节跳动 DeerFlow 2.0 架构回源 | 深度复盘 DeerFlow 为何选择“2 固定节点 + 工具层涌现”，其放弃 DAG 的代价清单，以及未来接入 `task_dag` 状态通道的演进路线 |
| [04-gpt-researcher-case.md](04-gpt-researcher-case.md) | 生产实战标杆: GPT Researcher v3 | 深度剖析开源标杆如何利用 LangGraph 的 Plan-and-Execute + `Send` API 实现未知并发度的动态研究 DAG 派发与聚合 |

---

## 3. 架构对比速查

| 维度 | LangGraph 原生 (Plan-and-Execute) | Deep Agents (LangChain) | DeerFlow 2.0 (字节跳动) | GPT Researcher v3 |
|---|---|---|---|---|
| **图拓扑形态** | 3~4 节点静态元图 (Plan/Execute/Replan) | 预编译 Agent 运行时 (Model ↔ Tools) | 极小 2 节点元图 (Model ↔ Tools) + 中间件链 | 静态多角色元图 (Planner -> Sub-researchers -> Publisher) |
| **动态任务承载** | `State.plan: List[str]` | `State.todos` + `write_todos` 工具 | `ThreadState.todos` (扁平清单无依赖边) | 动态子主题大纲列表 (`State.subtopics`) |
| **并发 Fan-out 机制** | `Send()` 动态派发 Worker | `task` 工具调用子代理 (独立 Context) | `task_tool` / `batch_task_tool` (后台线程池/Durable) | `Send("researcher_node", task)` 原生 Map-Reduce |
| **依赖拓扑校验** | 弱（多靠顺序循环） | 弱（无依赖关系，状态标记） | ❌ 缺席（无 Kahn 校验，无 DAG 边） | 强（子任务独立，结果在 Joiner 严格汇聚） |
| **状态机与持久化** | Checkpointer 级快照恢复 | LangGraph Checkpointer + Virtual Filesystem | Checkpointer (SQLite/PG) + 7 种物理沙箱 | Checkpointer 异步状态落地 |
