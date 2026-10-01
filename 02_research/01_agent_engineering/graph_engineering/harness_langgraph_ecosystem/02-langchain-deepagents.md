# 02 · LangChain 官方 Harness: Deep Agents 剖析

> **摘要**：深度剖析 LangChain 官方推出的生产级 Agent 基座——**Deep Agents (`langchain-ai/deepagents`)**。解剖其基于 LangGraph 的核心调度机制、`write_todos` 动态规划工具、`task` 子代理沙箱隔离原语，以及其在面对非线性 DAG 依赖时的能力边界与妥协。

---

## 1. Deep Agents 的定位与架构形态

在 LangGraph 成为底层编排底座之后，开发者普遍面临“组装成本过高”的问题（需要手写大量的 Node、Edge、StateSchema、Checkpointer 配置）。为此，LangChain 官方推出了 **Deep Agents**。

*   **本质定位**：一个 **“开箱即用（Batteries-included）的 Agent Harness”**。
*   **分工关系**：
    *   **LangGraph** 是底层的**编排虚拟机 / 状态机运行时（Runtime Engine）**；
    *   **Deep Agents** 是运行在 LangGraph 之上的**顶层应用脚手架（Agent Harness）**，封装了生产环境必须的沙箱管理、上下文截断中间件、规划工具链与多智能体派发原语。

---

## 2. 动态任务与编排机制解剖

Deep Agents 在处理长周期复杂任务（如大型代码库研发、跨多文件分析）时，没有暴露繁琐的底层图构建接口，而是内置了三大核心能力：

### 2.1 任务动态规划原语：`write_todos`
Deep Agents 没有让模型自由在对话文本中随意发挥，而是通过系统工具注入了结构化的待办规划能力：
- 主 Agent 在接收复杂目标后，第一反应是调用 `write_todos` 工具；
- 系统维护结构化的状态字典：
  ```python
  class TodoItem(BaseModel):
      id: str
      content: str
      status: Literal["pending", "in_progress", "completed", "cancelled"]
  ```
- 模型在执行每个阶段前，必须显式调用更新状态，确保执行轨迹在 LangSmith Trace 中可追溯。

### 2.2 动态子代理派发原语：`task`
当任务规模庞大，继续由主 Agent 在单个 Context 中执行会导致严重的**上下文挤压（Context Compression）和指令漂移（Instruction Drift）**。Deep Agents 引入了 `task` 原语：
- **动态上下文隔离（Isolated Context Windows）**：
  主 Agent 调用 `task(prompt, tools, files)` 时，底层运行时会在一个全新的、干净的上下文空间中实例化一个子 Agent；
- **文件系统持久记忆（Virtual Filesystem）**：
  主 Agent 与子 Agent 之间不传递冗长的中间输出，而是通过挂载的工作区文件系统进行工件交接；
- **聚合结果交付**：子 Agent 执行完毕后，只向主 Agent 返回精简的执行摘要（Summary）和状态码，保持主上下文清爽。

### 2.3 上下文熔断与中间件管道（Context Middleware）
为了防止陷入死循环，Deep Agents 在 LangGraph 节点之间注入了专职中间件：
- **自动截断与总结（Auto-summarization Middleware）**：当上下文达到 Token 阈值时，自动触发后台摘要节点；
- **死循环检测器（Doom-loop Detector）**：检测到连续 3 次相同的工具调用报错时，强制中断并转为报错反思模式。

---

## 3. Deep Agents 的能力边界：为什么它依然是“弱 DAG”？

尽管 Deep Agents 在长周期任务上比简单的 ReAct 框架稳定得多，但从**图工程（Graph Engineering）**的严格标尺来看，它与字节跳动的 DeerFlow 一样，**在任务拓扑上依然属于“弱 DAG / 扁平清单”形态**：

| 评估维度 | Deep Agents 现状 | 带来的工程局限 |
|---|---|---|
| **任务依赖关系** | 仅维护扁平的 `todos: List[TodoItem]`，**无显式依赖边（Dependencies）** | 无法自动计算并行拓扑。哪些任务可以并发执行、哪些必须串行等待，全靠 LLM 在 Prompt 中自行心智推理，容易发生执行顺序倒错。 |
| **并发调度机制** | 依赖 LLM 连续产生多个 `task` 工具调用进行批量派发 | 缺乏调度器层面的拓扑入度检查（In-degree = 0 自动触发），并发派发受限于单次模型输出的 Tool Call 数量。 |
| **失败重试与切片** | 任务失败后，依赖主 Agent 在下一轮对话中重新修改 Todo | 没有结构化失败信封（Failure Envelope），缺乏局部的子图重排与局部快照回滚能力。 |

---

## 4. 对工业级架构的启示

LangChain 官方在设计 Deep Agents 时，优先满足的是 **“通用高易用性”**：
- 采用“极简固定图 + 扁平 Todos + 隔离 Subagent”的架构，能够在极低的心智负担下跑通 80% 的通用 Coding 与 Research 场景；
- 但在面对**数百个微服务协同构建、带复杂跨模块前置依赖的代码库重构**时，扁平 Todos 的心智负荷会迅速击垮模型。
- 这正是 DeepSeek Harness (`dsh`) 和 OpenHands 选择更进一步、引入**显式 Task DAG** 的分水岭所在。
