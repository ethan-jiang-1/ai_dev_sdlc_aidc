# 04 · OpenHands：Manager DAG 分解、委托原语与会话树虚拟化

> **摘要**：深度剖析开源软件工程基座标杆 **OpenHands (原 OpenDevin)**。系统解密其 Manager-Worker 架构下的 **Subtask DAG 依赖分解**、核心委托原语 **`AgentDelegateAction`** 的生命周期流转，以及为了防止超长周期编码会话上下文腐败而引入的 **上下文树形虚拟化（Contextual Memory Virtualization as DAG）**。

---

## 1. 业务背景：攻坚长程软件工程（SWE-bench）

在 SWE-bench 级别的复杂 Issue 攻克场景中，一个典型的任务往往需要经历：
“定位 Bug 根因 $\rightarrow$ 重现问题编写 Failing Test $\rightarrow$ 跨多个模块打补丁 $\rightarrow$ 运行全量回归单测 $\rightarrow$ 整理 PR 描述”。

如果仅用一个单体 Agent 在一个单一上下文里执行到底：
- 会话轮数通常会超过 40~50 轮；
- 漫长的编译报错和代码翻查会迅速使 Context 达到饱和，引发严重的**上下文失忆（Contextual Amnesia）**与指令衰减；
- 遇到修复死胡同无法干净地回滚到初始状态。

---

## 2. 动态工作流与 DAG 核心实现

OpenHands 通过三层工程机制，彻底重构了执行链路：

### 2.1 显式 Subtask DAG 任务分解
在 OpenHands 的高级执行器中，**Manager Agent** 负责全局宏观把控：
1. **生成有向无环依赖图**：Manager 接收 Issue 后，动态输出一份包含明确依赖关系的 Subtask DAG；
2. **拓扑调度引擎**：系统检测所有处于就绪态（无未完成依赖）的子任务，将其分配给专职的 Subagent 执行；
3. **并发吞吐**：各个独立的 Subagent 可以在不同的 Docker 沙箱中并行启动，互不阻塞。

### 2.2 核心委派原语：`AgentDelegateAction`
OpenHands 没有将子智能体的派发简单视作一个普通的终端 Bash 命令，而是在其事件总线（Event Stream）中将其升格为**一等公民（First-class Action Primitive）**：

```python
# OpenHands 事件流中的委托原语
class AgentDelegateAction(Action):
    agent_type: str         # 委派的角色（如 "CoderAgent", "TestRunnerAgent", "RefactorAgent"）
    task: str               # 具体子任务目标
    context: Dict[str, Any] # 传递给子代理的必要工件契约与变量

class AgentDelegateObservation(Observation):
    agent_type: str
    status: Literal["success", "failed", "timeout"]
    artifacts: List[str]    # 产生的具体文件变动路径
    summary: str            # 精简摘要（不包含子代理的全部过程吐字）
```
- **生命周期完全受控**：主 Agent 发射 `AgentDelegateAction` 后，自身状态机进入等待；底层沙箱拉起子代理执行完成后，生成 `AgentDelegateObservation` 唤醒主控；
- **信息截断与蒸馏**：子代理在执行单测时即使输出了数千行报错，返回给主控的也只是结构化的摘要与测试覆盖率结论，彻底杜绝了父级上下文膨胀。

### 2.3 会话历史树形虚拟化（Contextual Memory Virtualization as a DAG）
这是 OpenHands 在工程层最具启发性的创新之一：**彻底抛弃扁平线性的 Chat History，将整个会话在内存中建模为一棵 DAG 树**。

```
                    [Root: Initial Issue Prompt]
                                 │
                   [Node 1: Repo Structure Scan]
                                 │
                   [Node 2: Root Cause Hypotheses]
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
       [Branch A: 方案一打补丁]         [Branch B: 方案二重构接口]
                 │                               │
       [Node A3: 回归测试失败 ❌]       [Node B3: 回归测试通过 ✅]
                 │                               │
           (剪枝 Pruned! 废弃)                   ▼
                                       [Node B4: 生成最终 PR 产物]
```
- **分支探索与剪枝**：当 Agent 尝试方案 A 发现走入死胡同（测试无法通过）时，系统可以在 DAG 上直接回溯到 Node 2，切换到 Branch B。
- **动态上下文投影**：输入给当前 LLM 的 Prompt，**只由当前活动叶子节点到根节点的单一直线路径构成**。Branch A 产生的所有错误尝试和大量垃圾 Token 在视图中被完全裁剪，模型在 Branch B 中始终保持最高专注度。

---

## 3. 总结与四体系收敛结论

通过对 OpenHands、Claude Code、DeepSeek Harness 以及 OpenAI Codex 的横向审视，我们可以得出全行业在 Agent Harness 进化上的统一收敛趋势：

1. **扁平清单必将走向显式 DAG**：无论是通过代码脚本控制（Claude Code），还是通过数据结构与拓扑队列控制（DeepSeek / OpenHands），**依赖关系（Dependencies）的显式化是多任务稳定执行的前提**；
2. **信息传递必须强制蒸馏**：父子 Agent 之间绝不能共享全量对话，必须通过 `DelegateAction -> Observation` 或文件工件进行隔离交接；
3. **状态机支持拓扑级回滚**：长周期研发必须允许局部试错，依靠会话 DAG 虚拟化或 Git 提交树实现低成本的“后悔药”机制。
