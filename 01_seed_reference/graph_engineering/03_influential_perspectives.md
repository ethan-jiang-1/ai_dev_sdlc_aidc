# 03. 权威阵营与先驱论述汇编（广泛且有影响力）

---

## 1. Harrison Chase（LangChain / LangGraph 联合创始人兼 CEO）

### 核心论断：从单向 DAG 到带状态的循环图（Stateful Cyclic Graphs）
> *“在真实生产环境中，简单的单向 DAG 几乎无法解决严肃的 AI 任务。Agent 必须拥有 cycles（循环回退能力）——无论是因为工具调用失败重试、代码审查被拒，还是等待人类在环输入。生产级 Agent 架构必须建立在状态机（State Machine）之上，而不是僵硬的流水线上。”*

### 关键贡献与观点：
1. **揭开“Graph Engineering”的炒作面纱**：
   - 针对 2026 年夏天“Graph Engineering”术语的热炒，Harrison Chase 指出：这个概念听起来很酷炫，但它本质上正是 LangGraph 多年来所构建的——通过**显式状态机、图节点（Nodes）和条件边（Conditional Edges）**对非确定性模型强加确定性约束。
2. **控制杠杆（Levers of Control）**：
   - 企业级 AI 工程的核心诉求是“控制感（Controllability）”。开发者需要在图中植入关键控制点：
     - **持久化检查点（Checkpoints / Time-traveling）**：允许在任意历史节点暂停、审查、甚至人工改写状态后分叉重跑；
     - **状态隔离（Scoped State）**：防止单个子任务的噪音污染全局状态。

---

## 2. Anthropic 官方指南《Building Effective Agents》

### 核心哲学：工作流（Workflows）优先于盲目自治（Autonomous Agents）
Anthropic 在其影响深远的架构指南中强调：**不要一上来就追求全自治黑盒 Agent，而应优先将任务建模为明确的结构化图工作流**。

### 奠定 Graph 基础的五大拓扑模式（Architectural Patterns）：
1. **Prompt Chaining（链式拓扑）**：线性有向链，上一节点的输出作为下一节点的输入；
2. **Routing（分类路由拓扑）**：中央路由器根据输入特征将任务派发给专门的下游处理节点；
3. **Parallelization（并行扇出与汇聚拓扑）**：
   - Sectioning（切片并行）：将大任务拆分为互不依赖的子节点并行执行后合并；
   - Voting（多数表决）：多个独立节点生成结果后做一致性仲裁；
4. **Orchestrator-Workers（编排者-工作者拓扑）**：
   - 核心图结构：动态生成子任务 DAG。中央编排模型分析任务 -> 动态派发异构子智能体 -> 汇聚综合产物；
   - 适用场景：无法事先静态穷举执行路径的复杂编程与多源研究任务；
5. **Evaluator-Optimizer（评估者-优化者回路）**：
   - 核心图结构：生成节点与评估节点之间的带条件反馈闭环（Cycles）。只有当评估节点判定达标，流程才突破循环向终点前进。

---

## 3. Peter Steinberger（OpenClaw 创作者，知名 iOS 资深工程师）

### 核心事件：2026-07-18 的行业破局一问
> *"Are we still talking loops or did we shift to graphs yet?"*

### 核心见解与工程实践：
1. **从玩具走向生产的必然**：
   - 单纯在 CLI 里跑一个 `while (true)` 的 Prompt-Retry 循环，写写小脚本还行；一旦面对数万行代码的大型重构或多系统联动，单循环迅速崩溃。
2. **组织架构的代码化**：
   - 软件系统规模化靠的是团队拓扑（Team Topologies），Agentic SDLC 规模化靠的是图工程（Graph Topologies）。
   - 让专业的人做专业的事，在图上体现为专职的小模型/小 Agent 处理独立子图，最后由集成者在汇聚节点完成契约合并。

---

## 4. Andrew Ng（吴恩达）

### 核心观点：从单模型 Prompting 到 Agentic Workflow 的多环反馈
- Andrew Ng 在 2026 年持续推进 Agentic 流程的普及，他在定义 Loop Engineering 时提出了著名的**三环反馈理论（Three Feedback Loops）**：
  - 秒/分钟级反馈：模型自我反思与工具输出对比；
  - 小时级反馈：代码测试套件与静态分析执行器；
  - 天/周级反馈：真实业务与人工验收回流。
- **与 Graph 的延展**：随着三环反馈被工程化，业界发现不同时间尺度的反馈环无法在一个单体 Session 中运行，必须通过系统图（System Graph）跨时间、跨存储、跨节点地进行状态中继与调度。
