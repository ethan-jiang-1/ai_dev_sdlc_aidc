# 01 · LangGraph 原生动态 DAG 与工作流机制

> **摘要**：系统解剖 LangGraph 原生运行时如何支撑动态工作流（Dynamic Workflow）与动态有向无环图（Dynamic DAG）。剖析 `Send()` API、`Command()` 原语与 Compiled Subgraphs 的底层机制，并给出为什么“现场编译新图”是生产毒药的底层架构解释。

---

## 1. 为什么“现场编译新图（Runtime Compilation）”是生产毒药

许多初学者接触 LangGraph 时，直觉认为“动态 DAG”等于：
```python
# ⚠️ 生产反模式：运行时现场编译
async def handle_user_request(user_input: str):
    plan = await planner_llm.generate_plan(user_input)
    builder = StateGraph(State)
    for step in plan.steps:
        builder.add_node(step.id, create_step_node(step))
        for dep in step.dependencies:
            builder.add_edge(dep, step.id)
    # 每次请求现场编译图！
    graph = builder.compile(checkpointer=MemorySaver())
    return await graph.ainvoke(...)
```

这种方案在生产环境中会瞬间导致系统崩溃，核心原因有四：
1. **Checkpointer 状态版本映射断裂**：LangGraph 的持久化检查点（SqliteSaver / PostgresSaver）是基于图编译时确定的 `node_name`、`channel_name` 和步骤序列哈希进行索引的。动态编译出来的图每次哈希与拓扑不同，根本无法执行 `graph.ainvoke(..., config={"configurable": {"thread_id": "xxx"}})` 的断点恢复，Time-travel（时间旅行回退调试）直接失效。
2. **APM 与链路追踪（Telemetry）拓扑漂移**：在 LangSmith 或 OpenTelemetry 中，静态编译的图拥有清晰稳定的调用栈和拓扑看板；每次动态生成的节点名会让 Trace 拓扑呈现无序爆炸，根本无法做按节点的聚合延迟、Token 消耗统计和异常熔断。
3. **严重冷启动开销**：图编译包含大量的静态校验（入度出度检查、死循环环路检测、Reducers 绑定、Channel 内存初始化），高并发请求下每次动态编译会严重占用 CPU。
4. **编译期校验无法捕获运行时动态故障**：如果 LLM 在动态生成图时引入了逻辑死环或非法节点引用，错误发生在编译期或调度核心，直接拖死整个进程。

---

## 2. LangGraph 原生动态编排的三大核心原语

工业界使用 LangGraph 实现动态工作流，依靠的是**固定图拓扑之下的三大运行时动态控制原语**：

### 2.1 原语一：`Send()` API（动态 Map-Reduce Fan-out）
当主控节点在运行时动态拆分出未知数量的并发任务时，LangGraph 提供了 `Send()` 原语。

```python
from langgraph.types import Send
from langgraph.graph import StateGraph, START, END

def orchestrator_node(state: OverallState):
    # LLM 在运行时动态拆解出 N 个子任务（N 无法在静态编译时确定）
    tasks: list[SubTask] = analyze_and_decompose(state.query)
    # 动态并发派发：返回一组 Send 对象
    return [Send("worker_node", {"task": t, "workspace_id": state.workspace_id}) for t in tasks]

def worker_node(task_state: WorkerState):
    # 并行执行具体的子任务
    result = execute_task(task_state["task"])
    return {"completed_results": [result]}

# 静态骨架编译一次，运行期通过 Send() 实现动态展开
builder = StateGraph(OverallState)
builder.add_node("orchestrator", orchestrator_node)
builder.add_node("worker", worker_node)
builder.add_node("synthesizer", synthesizer_node)

builder.add_edge(START, "orchestrator")
builder.add_conditional_edges("orchestrator", orchestrator_node)
builder.add_edge("worker", "synthesizer")
builder.add_edge("synthesizer", END)
graph = builder.compile(checkpointer=checkpointer)
```
- **工作机理**：`Send("node_name", arg)` 是一个调度指令。LangGraph 引擎在处理条件边时，如果捕获到 `List[Send]`，会自动为列表中的每一个 `Send` 在当前 Step 中动态实例化一个并发任务分支，并以非阻塞方式异步并发执行，最终在带 Reducer 的目标节点（如 `synthesizer`）进行 Fan-in 聚合。
- **价值**：**图是静态编译的，但任务并发度是完全动态的**。Checkpointer 将所有 `Send` 分支作为子任务树保存，完全支持状态断点。

### 2.2 原语二：`Command(goto=..., update=...)`（状态驱动的动态跳跃）
LangGraph 引入的 `Command` 原语彻底消除了复杂的外部条件边逻辑，允许节点在执行完后，同时完成“更新状态”与“动态决定下一跳”：

```python
from langgraph.types import Command

def dynamic_router_agent(state: AgentState):
    decision = evaluate_environment_and_next_step(state)
    
    if decision.action == "need_clarification":
        # 动态跳转至人工介入或澄清节点，并更新状态
        return Command(
            update={"history": [AIMessage(content=decision.question)]},
            goto="human_feedback_node"
        )
    elif decision.action == "spawn_subtask":
        # 动态流转至执行节点
        return Command(
            update={"active_subtask": decision.subtask},
            goto="subagent_execution_node"
        )
    else:
        return Command(goto=END)
```
- **工作机理**：`Command` 将控制权下放到了节点内部的业务逻辑，避免在编译期穷举所有复杂的条件边网络。

### 2.3 原语三：Compiled Subgraphs（编译子图的动态隔离调用）
对于极其复杂的企业级流程，每一个阶段本身是一个图（例如“需求分析子图”、“单元测试与修复子图”）：
- **状态空间隔离**：子图拥有自己独立的 `State` 定义，不污染父图的全局 `OverallState`。
- **独立 Checkpoint 命名空间**：父图调用子图时，子图在独立的 Checkpoint Namespace（例如 `thread_id:subgraph_id`）下推进，子图内部的循环死斗（doom loop）与频繁状态变更不会膨胀父图的事件流。

---

## 3. Plan-and-Execute 模式：状态内 Task DAG 的标准实现

LangGraph 官方推荐的动态 DAG 落地模式是 **Plan-and-Execute Pattern**。它的架构精髓在于：**图节点固定为 3 个角色，动态 DAG 存放在 State 字典中**。

```
[START] ──> (1. Planner) ──> (2. Dynamic Dispatcher) ──> (3. Worker Node)
                                     ▲                         │
                                     │                         ▼
                              (5. Evaluator/Re-planner) <── (4. Joiner)
                                     │ (All tasks completed)
                                     ▼
                                   [END]
```

### 3.1 核心数据结构（State 内的 Task DAG）
```python
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Literal

class TaskNode(BaseModel):
    task_id: str
    description: str
    dependencies: List[str] = Field(default_factory=list) # 前驱依赖任务 ID
    assigned_worker: str
    status: Literal["pending", "ready", "running", "success", "failed"] = "pending"
    result: Optional[str] = None
    retry_count: int = 0

class PlanAndExecuteState(BaseModel):
    objective: str
    task_dag: Dict[str, TaskNode] # 显式有向无环图数据结构
    active_batch: List[str]       # 当前就绪并发执行的任务 ID 集合
    final_output: Optional[str] = None
```

### 3.2 动态流转逻辑
1. **Planner 节点**：主控模型解析目标，输出 `task_dag` JSON。系统使用 Kahn 拓扑排序算法做就地无环校验（确保无循环依赖）。
2. **Dynamic Dispatcher 节点**：读取 `task_dag`，筛选出所有“状态为 `pending` 且其所有 `dependencies` 均为 `success`”的节点，标记为 `ready`。如果就绪集合大于 1，直接调用 `Send("worker", task)` 并发执行。
3. **Re-planner / Evaluator 节点**：
   - 检查执行结果。如果某节点执行失败，**不重跑整个任务**，而是执行局部拓扑手术：
     - 若重试次数未超限，标记该节点重新重试；
     - 若需要修复，动态向 `task_dag` 插入一个补丁子节点（Patch Subtask），并将原失败节点的后继任务依赖指向该补丁节点；
   - 重新计算就绪集，继续驱动循环。

---

## 4. 结论

LangGraph 在底层设计上**完全具备支撑工业级 Dynamic DAG 的能力**。关键在于架构师必须分清：
- **静态的是执行引擎与元图框架（Execution Engine & Meta-Graph）**；
- **动态的是任务依赖数据结构与流转指令（Task DAG State & Send/Command Primitives）**。
这一工程原则构成了后续分析 Deep Agents、DeerFlow 以及生产系统设计的分水岭。
