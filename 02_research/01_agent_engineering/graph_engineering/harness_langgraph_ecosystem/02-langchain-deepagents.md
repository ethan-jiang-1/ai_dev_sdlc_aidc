# 02 · LangChain 官方 Harness: Deep Agents 架构解剖与能力边界

> **摘要**：深度解密 LangChain 官方推出的高阶 Agent 基座——**Deep Agents (`langchain-ai/deepagents`)**。剖析其构建在 LangGraph 之上的“中间件洋葱链（Middleware Onion Chain）”、`write_todos` 待办规划状态同步机制、`task` 子代理递归隔离派发底层实现，以及其采用“扁平待办清单”在面对高复杂度非线性 DAG 依赖时的工程局限与扩展方案。

---

## 1. 架构定位：LangGraph 之上的“开箱即用”应用基座

如果说 **LangGraph** 是操作系统底层的“进程调度器与状态机虚拟机”，那么 **Deep Agents** 就是官方封装的“标准用户态运行时环境（User-Space Runtime）”。

Deep Agents 旨在解决开发者使用原生 LangGraph 时面临的“样板代码冗余（Boilerplate Bloat）”与“生产级防御设施缺失”的问题：
- 默认提供经过压力测试的系统中间件管道（Middleware Pipeline）；
- 默认集成基于内存/沙箱的虚拟文件系统；
- 默认打通长程任务规划工具与子代理隔离沙箱。

```
┌────────────────────────────────────────────────────────────────────────┐
│                   Deep Agents 运行时封装 (Compiled Agent)               │
│                                                                        │
│  [外部请求] ──> [输入验证与 Token 预估]                                  │
│                       │                                                │
│                       ▼                                                │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                     中间件洋葱链 (Middleware Onion Chain)         │  │
│  │                                                                  │  │
│  │  1. SummarizationMiddleware: 上下文超限自动触发摘要与裁剪        │  │
│  │  2. DoomLoopMiddleware: 检测连续重复调用或报错，触发强制熔断     │  │
│  │  3. FilesystemMiddleware: 拦截文件操作，重定向至虚拟工作区沙箱    │  │
│  │  4. TodoSyncMiddleware: 拦截 write_todos，实时同步 State.todos   │  │
│  │  5. SubagentLimitMiddleware: 限制并发派发的子代理进程数          │  │
│  └──────────────────────────────────┬───────────────────────────────┘  │
│                                     │                                  │
│                                     ▼                                  │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │          底层固定元图运行时 (LangGraph Runtime Core)              │  │
│  │                                                                  │  │
│  │            [Model Node] <───(Tool Calls / Returns)───> [Tools Node]│
│  │                  │                                           │      │
│  │                  ▼                                           ▼      │
│  │         (write_todos 状态同步)                    (task 派发子代理) │  │
│  └──────────────────────────────────┬───────────────────────────────┘  │
│                                     │                                  │
│                                     ▼                                  │
│  [Checkpointer 持久化] (Sqlite / Postgres 检查点 + 独立命名空间)        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. 核心动态编排机制深度解密

### 2.1 任务动态规划机制：`write_todos` 工具与状态同步
Deep Agents 内置了一套标准化的待办事项状态机，其底层并不依赖复杂的 Graph 边，而是直接将 `todos` 作为 LangGraph `State` 的核心 Channel：

#### 源码级工具定义与契约：
```python
from pydantic import BaseModel, Field
from typing import List, Literal

class TodoItem(BaseModel):
    id: str = Field(description="任务全局唯一 ID，如 task_1")
    title: str = Field(description="任务简要描述")
    status: Literal["pending", "in_progress", "completed", "cancelled"] = Field(
        default="pending",
        description="任务流转状态"
    )

class WriteTodosInput(BaseModel):
    todos: List[TodoItem] = Field(description="更新后的全量待办任务列表")

def write_todos_tool(todos: List[TodoItem], state: DeepAgentState):
    """
    模型在执行每一步前或后调用的核心工具。
    中间件拦截该工具调用，并将数据合并入 State.todos。
    """
    return {
        "status": "SUCCESS",
        "message": f"成功同步 {len(todos)} 项待办任务状态",
        "active_todos": [t.dict() for t in todos]
    }
```
- **工作机理**：主模型在接收大任务后，首先调用 `write_todos` 输出任务列表。每一次执行工具前，主模型将某一项置为 `in_progress`；完成并验证后置为 `completed`；
- **状态透明度**：在 LangSmith 中，每次 `write_todos` 调用都会产生显式的快照记录，运营人员可以清晰看到模型对当前进度的理解。

### 2.2 子代理派发机制：`task` 工具的递归隔离调用
为了解决单模型处理长程任务时的上下文污染，Deep Agents 提供了 `task` 原语。主模型可以通过调用 `task` 工具派发专职 Subagent。

#### `task` 工具在 LangGraph 内核中的实现逻辑：
```python
async def task_tool(
    prompt: str,
    subagent_type: str,
    parent_config: RunnableConfig,
    state: DeepAgentState
):
    """
    在独立的 Checkpoint Namespace 下实例化并运行子 Agent
    """
    parent_thread_id = parent_config["configurable"]["thread_id"]
    # 构造独立的子图检查点命名空间
    child_thread_id = f"{parent_thread_id}:subtask_{uuid.uuid4().hex[:8]}"
    
    # 复制受限的环境配置，挂载共享的虚拟文件系统
    child_config = {
        "configurable": {
            "thread_id": child_thread_id,
            "filesystem": state["virtual_filesystem"]
        }
    }
    
    # 获取专职子 Agent 的编译图实例 (Compiled Graph)
    child_agent = get_specialized_subagent(subagent_type)
    
    # 运行子代理（子代理内部可经历多达 20 轮微循环）
    final_child_state = await child_agent.ainvoke(
        {"messages": [HumanMessage(content=prompt)]},
        config=child_config
    )
    
    # 核心隔离机制：剥离所有过程调试消息，仅提取最终回答作为工具返回值
    last_message = final_child_state["messages"][-1]
    return f"子代理 [{subagent_type}] 执行完成。\n最终产物摘要: {last_message.content}"
```
- **上下文防火墙**：子代理在执行过程中尝试的十几条 Bash 命令、编译报错日志、反复重试过程，全部被封闭在 `child_thread_id` 的隔离命名空间中。主 Agent 的上下文仅接收最后数十个字的“最终产物摘要”，彻底杜绝了上下文爆炸。

---

## 3. Deep Agents 的能力边界：扁平待办清单的局限

尽管 Deep Agents 架构成熟、体验丝滑，但从严格的**图工程（Graph Engineering）**标尺来审视，它依然存在明显的结构性边界：

| 评估维度 | Deep Agents 现状 | 引发的问题与翻车现场 |
|---|---|---|
| **任务依赖关系（Dependencies）** | `TodoItem` 仅有 `id`、`title`、`status`，**无 `dependencies` 字段** | 任务是线性扁平数组，无法表达“Task C 必须等待 Task A 与 Task B 同时完成才能执行”的汇聚依赖。 |
| **并发调度机制** | 缺乏基于入度的拓扑调度器 | 并发完全依赖主模型在一次输出中调用多个 `task(...)` 工具；如果模型漏调或顺序调错，系统无底层拓扑保障。 |
| **执行时序保证** | 依赖 LLM 在 Prompt 中自行心智推理执行顺序 | 在长程复杂场景中，模型极易产生“跳步”幻觉（例如尚未完成“定义接口”，就直接开始执行“编写接口调用代码”）。 |
| **失败切片与局部重排** | 依赖主模型在下一轮自行重新调用 `write_todos` | 缺乏强类型的失败信封（Failure Envelope），当子任务失败时，模型容易在错误的待办项上不断原地打转。 |

---

## 4. 扩展方案：如何将 Deep Agents 升级为强 DAG Harness？

如果企业希望在现有的 Deep Agents 代码基础上，支持真正的复杂动态 DAG 调度，推荐的最小侵入扩展路径如下：

```python
# 扩展 TodoItem，赋予其显式拓扑属性
class DagTaskItem(BaseModel):
    id: str
    title: str
    dependencies: List[str] = Field(default_factory=list) # 增加前置依赖定义
    status: Literal["pending", "ready", "running", "completed", "failed"] = "pending"
    assigned_subagent: str = "GeneralWorker"

# 新增拓扑调度中间件 (DagSchedulerMiddleware)
class DagSchedulerMiddleware:
    def on_task_completed(self, state: DeepAgentState, completed_task_id: str):
        # 1. 标记当前任务为 completed
        state.task_dag[completed_task_id].status = "completed"
        # 2. 遍历所有 pending 任务，重新计算依赖满足度
        for tid, task in state.task_dag.items():
            if task.status == "pending":
                if all(state.task_dag[dep].status == "completed" for dep in task.dependencies):
                    task.status = "ready"
        # 3. 自动触发就绪任务的 Send() 并发派发
```

通过这一轻量级扩展，即可将 Deep Agents 从一个通用的“扁平任务型基座”，平滑演进为具备严格依赖拓扑调度与容错能力的“工业级动态 DAG Harness”。
