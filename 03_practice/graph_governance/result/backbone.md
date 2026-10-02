# Graph Governance 实践主干（定稿层·总纲）

> **本文件是什么**：五层框架（Prompt → Context → Harness → Loop → **Graph**）第 5 层的实践主干，**§0–§7 共八节**——
> §0 定义与判据（含 10 项失败模式诊断轴）；§1 拓扑双轨骨架（固定元图 vs 动态任务数据）；§2 状态机分层治理（Session 外持久化运行时）；
> §3 工件契约与共享黑板（消灭自然语言群聊）；§4 两层自愈协议（L1 微循环 vs L2 局部子图切片替换）；§5 2026 SOTA 模型五大病理防御；
> §6 HITL 人机协作与安全熔断；§7 接口与兄弟主题分工。
> 操作规程（SOP / Schema / 代码模板 / 落地梯子）在 [`manual.md`](manual.md)。

```yaml
topic: Graph Governance —— Graph 层的实践主干（拓扑编排、强类型工件契约、状态机推进与两层自愈体系）
doc_layer: result（定稿层 · 总纲）
produced_at: 2026-10-02
provenance: >
  研究层 02_research/01_agent_engineering/graph_engineering/ 9 大 digested 议题判读；
  一手回源档案（Steinberger 2026-07 论战、Harrison Chase 状态机论断、Temporal 工业持久化实证、字节 DeerFlow 2.0 源码校准、Raven A2A 实录）；
  四大前沿体系解密（Claude Code, DeepSeek dsh, OpenAI Codex, OpenHands）。
filter: ≥2 独立工程落地交叉支撑；承重结论带代码/架构锚点；坚决消灭伪 Multi-Agent 群聊反模式；未收敛点如实登记。
evidence_home: 02_research/01_agent_engineering/graph_engineering/（机制与证据权威在研究层，本层不建 research/ 目录，防双权威）
naming: 不沿用 KOL 词 "graph engineering"——按五层框架命名，与 harness_governance、loop_governance 同构组成三层治理闭环（环境轴 / 控制轴 / 拓扑协作轴）
---
```

---

## 0. 这层管什么（定义与判据）

### 0.1 核心定义

**Graph 层管“多节点协同与拓扑推进”：定义谁先谁后、工件如何契约化交接、全局状态由谁推进、失败如何跨节点动态自愈。**

如果说 Harness 治理管“单次执行沙箱受控”（环境轴），Loop 治理管“单节点多轮迭代何时够格停止”（控制轴），那么 Graph 治理管的是**“节点之间的依赖拓扑、强类型契约、状态机流转与跨节点自愈重排”（拓扑/协作轴）**。

### 0.2 三个硬判据（什么时候必须上 Graph 治理）

1. **跨长程任务与上下文物理隔离**：单 Agent 的单个 Context 无法容纳完整任务生命周期（Token 消耗过大、注意力被中间杂质稀释、Context Rot 严重）。必须将任务拆分为拓扑节点，每个节点分配最小干净上下文。
2. **多角色职责隔离与并发扇出/汇聚**：存在必须由不同专业特长（如架构设计、专职编码、静态审计、集成测试）独立完成的工序，或需要并发执行（Fan-out / Fan-in）且互不污染的代码变更。
3. **分层容错与局部图自愈**：节点内局部重试无法解决系统性前置依赖缺失或规格冲突，系统必须支持向上升级（Escalation）并由编排者做局部拓扑重写，而非推翻整个任务从头开始。

> **反向判据（什么时候坚决不上 Graph 治理）**：
> - 任务在 1~3 轮单体 Loop 且单个上下文窗口内可高确定性完成（如单个小文件函数修补）；
> - 需求无法切片为独立的子目标或没有明确的强类型交付物契约；
> - 试图用所谓“Multi-Agent 讨论群聊”来替代人类模糊不清的需求定义——**那是用拓扑的复杂性掩盖产品定义的无能**。

### 0.3 Graph 层失败模式（诊断轴——各节的“防什么”标签）

| 失败模式 | 典型症状 | 核心应对章节 |
|---|---|---|
| **① 伪多 Agent 群聊** | 让不同角色在同一个对话窗口自由客套，Token 二次方爆炸且不收敛 | §3 工件契约与黑板 |
| **② 现场动态编译图陷阱** | 大模型现场生成 Python 图代码并内存 compile，导致 Checkpoint 断裂与 Trace 崩溃 | §1 拓扑双轨骨架 |
| **③ 全量重新生图风暴** | 单节点失败引发整图推翻重算，引发状态抖动与 Meta Doom Loop | §4 两层自愈协议 |
| **④ 内存幽灵状态机** | 将图状态与编排逻辑写在瞬态内存进程中，宿主重启或超时即任务全死 | §2 状态机分层治理 |
| **⑤ 弱类型数据交接腐蚀** | 节点间传递非结构化 Markdown，下游解析脆弱、错误连锁蔓延 | §3 强类型工件契约 |
| **⑥ 异构模型汇报风暴** | 角色模型产生病态“汇报冲动”，刷屏消耗 Token 并阻塞并发调度 | §5 模型病态防御 |
| **⑦ 偷跑伪造完成验收** | 执行模型越权篡改测试文件、自行伪造通过标志 | §5 机器级硬核防御 |
| **⑧ 拓扑重排死锁黑洞** | 编排模型反复修改前置条件、引入隐式环形死锁或无限消耗改图预算 | §4 / §6 预算硬熔断 |
| **⑨ 上下文幽灵污染** | Worker 复用上一节点的执行沙箱与脏文件，破坏单测试验隔离 | §3 Git Worktree 隔离 |
| **⑩ 假自治脱轨** | 缺乏人类介入检查点（HITL），在歧义严重的架构设计上单向飙车 | §6 HITL 与安全熔断 |

---

## 1. 拓扑双轨骨架：固定元图（Meta-Graph） vs 动态任务数据（Task DAG as Data）

在生产级工程中，必须彻底划清**“编排程序的确定性”**与**“解题任务的动态性”**的边界（判读见研究层 [`digested/09`](../../../02_research/01_agent_engineering/graph_engineering/digested/09-meta-graph-vs-dynamic-task-dag.md)）。

### 1.1 学院派纯动态图编译的生产破产

让大模型在运行时根据用户指令现场编写或拼接 Python 图代码（`builder.add_node` / `builder.compile()`）并直接执行，在工业生产中已被证伪为灾难反模式：
- **检查点（Checkpointer）断裂**：持久化状态机依赖确定性静态节点 ID。动态编译导致每次图拓扑与节点标识漂移，遇崩溃或人工审批挂起后**不可恢复（Resume Broken）**；
- **监控可观测性（Observability）全线崩溃**：APM（Datadog, OpenTelemetry, LangSmith）无法建立基于固定拓扑的 P99 耗时基线与错误率统计；
- **元死循环（Meta Doom Loop）**：动态改图诱发全图重新编译，导致已完成的节点被随机重构，系统在拓扑抖动中耗尽预算。

### 1.2 工业终局标准：双轨分离架构

生产系统必须采用**“固定元图（Meta-Graph）静态编译一次 + 状态机消费动态任务数据（Task DAG as Data）”**的双轨模式：

```text
┌────────────────────────────────────────────────────────────────────────┐
│        外层：固定不变的确定性状态机元图 (Meta-Graph) - 静态编译一次        │
│                                                                        │
│       ┌─────────────────┐             ┌─────────────────────┐          │
│  ───► │  Planner 节点   │ ──────────► │  Dispatcher 调度器  │          │
│       │  (Coordinator)  │             │  (基于 LangGraph)   │          │
│       └────────┬────────┘             └──────────┬──────────┘          │
│                │ 动态生成 Task DAG               │                     │
│                ▼                                 ▼                     │
│       ┌─────────────────┐             ┌─────────────────────┐          │
│       │ 动态任务清单状态 │ ◄───────────│   Aggregator 汇聚   │          │
│       │ (State.task_dag)│ (更新/切片) └─────────────────────┘          │
│       └─────────────────┘                        │                     │
│                                                  ▼                     │
│                                           [Integration Gate]           │
└──────────────────────────────────────────────────┬─────────────────────┘
                                                   │ 动态派发 (Send API / Docker)
                                                   ▼
                                ┌──────────────────────────────────────┐
                                │ 内层：动态派生的物理沙箱 Worker 实例   │
                                │   - Worker [task_id=01]              │
                                │   - Worker [task_id=02] (并发执行)   │
                                └──────────────────────────────────────┘
```

1. **元图 100% 确定性硬编码**：
   - 包含固定的控制节点：`Planner`（规划）、`Dispatcher`（任务拓扑派发器）、`Worker`（通用执行算子）、`Reviewer/Gate`（确定性测试门禁）、`Aggregator`（工件聚合）；
   - 元图在进程启动前静态编译完成，注册固定的全局 Checkpointer 与监控中间件。
2. **大模型动态生成的是“状态数据（Data DAG）”，不是图代码**：
   - 模型输出符合严格 Schema 的任务 DAG JSON（如带前驱 `dependencies` 的子任务列表）；
   - 调度器通过确定性算法计算拓扑入度为 0 的任务，借助框架提供的动态派发原语（如 LangGraph `Send()`、Temporal 子工作流）并发拉起 Worker 实例；
3. **改图本质是“对状态数据做外科手术”**：
   - L2 拓扑自愈时，模型修改的只是 `State.task_dag` 字典中状态为 `PENDING` 的待办任务数据，外层元图结构纹丝不动。

> **边界形态校准**：依据字节 DeerFlow 2.0 源码实证（[`digested/09 注记`](../../../02_research/01_agent_engineering/graph_engineering/digested/09-meta-graph-vs-dynamic-task-dag.md)），固定元图是生产共识（DeerFlow 采用极小两节点元图）；对于超级智能体底座形态（工具涌现式派发），数据 DAG 可简化为扁平 Todo 清单；而对于确定性 SDLC 研发流水线（如 Issue→PR 自动化），数据 DAG 是强依赖项。

### 1.3 双形态拓扑治理光谱（适用分界与转换规则）

在工业实践中，并非所有拓扑都表现为静态编译期确定依赖的严格 DAG。根据任务探索性与确定性程度，Graph 治理划分为两种标准形态：

| 拓扑形态 | 核心调度机制 | 状态通道载体 | 适用场景 | 工业样本 |
|---|---|---|---|---|
| **形态 A：显式声明式 DAG (Explicit Task DAG)** | 拓扑入度算法硬调度；强依赖边；并行扇出 (Fan-out) 与汇聚 (Fan-in) | `State.task_dag` 结构化字典；显式 `dependencies` 字段 | 目标确定性极高的大型代码重构、跨模块功能开发、Issue-to-PR 全自动流水线 | LangGraph 官方流水线、Temporal Activity DAG |
| **形态 B：动态委派树 (Dynamic Delegation Tree)** | Lead Agent 驱动；通过 `task` / `delegate` 工具在推理流中按需拉起 Subagent | 扁平 `todos` 清单 + 动态 `delegations` 调用流水 | 需求模糊度高、需探索式检索、交互式诊断的大型代码库排错 | 字节 DeerFlow 2.0、Claude Code、OpenHands |

**形态收敛纪律**：
- 严禁在探索期强行要求模型生成完备的 20 节点显式 DAG（会导致前期规划严重失真）；
- **演进路线**：探索阶段允许以形态 B（Lead 动态委派探索）摸清依赖，一旦进入批量编码与集成阶段，必须由 Lead Agent 将成果冻结并固化为形态 A（声明式 Task DAG）推进确定性执行。

---

## 2. 状态机分层治理：Session 内 Tool 编排 vs Session 外 外部持久化运行时

关于状态机驻留位置的论战，是区分 Demo 原型与工业级生产系统的关键分水岭（判读见研究层 [`digested/03`](../../../02_research/01_agent_engineering/graph_engineering/digested/03-session-internal-vs-external-state-machine.md)）。

```text
┌────────────────────────────────────────────────────────────────────────┐
│   Session 外部持久化运行时 (Durable Execution Engine: Temporal / PG)    │
│   - 100% 确定性代码流转、持久化事件溯源 (Event Sourcing)                │
│   - 负责：重试调度、超时截断、跨天/跨周挂起等待、人类审批信号恢复      │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ 调度 Activity (无状态单步)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│   Session 内部短期运行时 (Ephemeral Agent Execution: Docker / 沙箱)    │
│   - 非确定性大模型推理、局部工具调用、短程单体 Loop                     │
│   - 仅负责：消费干净上下文、产生局部工件、退出并销毁沙箱                │
└────────────────────────────────────────────────────────────────────────┘
```

### 2.1 两种状态机的职责分工

1. **Session 内状态机（Ephemeral / In-session）——严守只读与短程原则**：
   - 仅存在于单次大模型上下文会话中；
   - 适用场景：局部单文件代码检索、单次故障堆栈定位、短程代码改写；
   - **红线约束**：禁止让长程跨阶段状态滞留在 Session 内，一旦步骤完成必须提取结构化工件并销毁会话。
2. **Session 外状态机（Durable / Out-of-session）——全局唯一权威**：
   - 由外部强可靠系统（Temporal 工作流引擎、或带 SQLite/Postgres 持久化事务的 LangGraph Checkpointer）接管；
   - 核心机制：**工作流编排（Deterministic Workflow）与副作用执行（Non-deterministic Activity）严格解耦**；
   - 价值保证：
     - **持久化韧性（Durable Resilience）**：节点执行中宿主崩溃或网络超时，基于事件日志原位 Replay 重建状态，无需从头重算；
     - **长程挂起能力（Durable Wait）**：可无代价挂起数小时至数天等待人类架构师 Review 审批，不消耗任何内存驻留线程。

---

## 3. 工件契约与共享黑板：消灭自然语言群聊

让多个 Agent 在同一个对话流中以自然语言自由聊天的“Multi-Agent 群聊模式”是导致系统失效的头号反模式（判读见研究层 [`digested/01`](../../../02_research/01_agent_engineering/graph_engineering/digested/01-dag-state-machine-vs-free-chat.md) 与 [`digested/04`](../../../02_research/01_agent_engineering/graph_engineering/digested/04-artifact-contract-and-blackboard.md)）。

### 3.1 强类型工件契约（Typed Artifacts）

生产系统必须实行**“节点间零自然语言对话、仅交接强类型工件”**：

1. **强 Schema 约束**：上游节点的交付物与下游节点的输入必须定义明确的 JSON Schema / Pydantic 模型（如需求规范 `TaskSpec`、变更清单 `PatchManifest`、单测验证报告 `TestReport`）；
2. **静态契约校验门禁**：上游节点产生工件后，进入下游前必须经过确定性代码校验器（JSON Schema Validator）。格式校验未通过直接判定节点未完成，绝不传递破损工件污染下游；
3. **最小白名单上下文注入**：调度器唤醒下游 Worker 时，仅从上游工件中提取其工作所需的字段，严禁直接把上游全部原始思考链（COT）或对话历史打包塞入下游。

### 3.2 全局共享黑板与 Git Worktree 物理隔离

```text
┌────────────────────────────────────────────────────────┐
│         全局共享黑板状态机 (Blackboard State)           │
│   - task_spec: 冻结的需求蓝图 (只读不可变)             │
│   - artifacts: 各节点已归档的结构化工件字典            │
│   - event_log: append-only 不可变执行事件流水          │
└───────────────────────────┬────────────────────────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
    ┌───────────────────┐       ┌───────────────────┐
    │ Worker 1 沙箱     │       │ Worker 2 沙箱     │
    │ Git Worktree A    │       │ Git Worktree B    │
    │ (完全物理环境隔离)│       │ (完全物理环境隔离)│
    └───────────────────┘       └───────────────────┘
```

1. **黑板（Blackboard）作为单一事实来源**：
   - 存储结构化工件注册表与事件日志；
   - 遵循 **单写多读（Single-Writer, Multi-Reader）** 纪律：节点仅对本步骤声明产出的工件具备写入权，其他区域完全只读；
2. **代码变更的 Git Worktree 物理隔离**：
   - 并发执行的代码 Worker 必须在独立的 `git worktree` 分支或独立的 Docker 容器沙箱内执行；
   - 严禁并发 Worker 在同一物理目录读写文件；
   - 节点交付的标准代码工件是标准 Git Patch 或独立分支，合并汇聚由确定性的 Git Merge 与集成测试门禁裁定。

### 3.3 工件语义版本控制（Semantic Versioning）与级联失效传播

为杜绝 L2 动态改图时引发的“幽灵读取（Phantom Read）”，黑板上的工件严禁原地覆盖写（In-place Overwrite），必须实行不可变版本控制：

1. **工件命名与内容寻址**：
   - 工件唯一键包含语义版本：`<artifact_type>@v<revision>`（如 `TaskSpec@v1`、`TaskSpec@v2`）；
   - 每个工件附加 SHA256 签名与生成它的 `node_id`，下游消费时显式声明所需的前驱工件版本；
2. **级联失效传播（Cascading Invalidation）**：
   - 当编排者执行 L2 改图替换了某个前驱节点或修改了某份工件（如将 `SchemaSpec@v1` 升级为 `SchemaSpec@v2`）时，状态机必须沿着 DAG 依赖边做**拓扑反向传播**；
   - 所有直接或间接消费过旧版工件、且尚未最终冻结归档的下游节点，其状态强制从 `READY` / `RUNNING` 置为 `INVALIDATED`；
   - 清理对应节点的工作区沙箱，要求下游重新消费新版本工件并重新调度，杜绝跨版本脏状态污染。

---

## 4. 两层自愈协议与拓扑重排门禁（Two-tier Self-Healing）

Graph Governance 与 Loop Governance 的工程缝合点在于**异常升级协议（Escalation Protocol）**（判读见研究层 [`digested/02`](../../../02_research/01_agent_engineering/graph_engineering/digested/02-two-tier-self-healing-architecture.md) 与 [`digested/07`](../../../02_research/01_agent_engineering/graph_engineering/digested/07-dynamic-dag-replanning-mechanics.md)）。

```text
                  [任务启动: 编排者生成任务 DAG]
                                │
                                ▼
                  ┌───────────────────────────┐
                  │ 静态拓扑校验 (无环/契约对齐)│ ◄───────┐
                  └─────────────┬─────────────┘         │
                                │ Pass                  │
                                ▼                       │
                    [调度专职 Worker 节点]               │ L2 全局拓扑自愈:
                                │                       │ 局部子图切片替换
                 ┌──────────────┴──────────────┐        │ (三大受限原子变异)
                 ▼                             ▼        │
      ┌─────────────────────┐       ┌───────────────────┴───┐
      │   Worker 局部微循环  │ ◄──┐  │ Worker 耗尽预算失败   │
      │   (L1 局部自愈: Loop) │    │  │ (抛出 Failure Envelope)│
      └──────────┬──────────┘    │  └───────────────────────┘
                 │ Retry <= 3    │
                 └─── 语法/单测 ─┘
                 │
                 ▼ Pass
      [更新黑板状态机，推进下一节点]
```

### 4.1 L1 局部微循环自愈（Loop 层职责）

- **活动范围**：受限在 Worker 节点的单体沙箱内；
- **控制规则**：严格执行有限重试硬上限（Hard Cap ≤ 3 次），每次重试执行 AST 错误切片提取与上下文修剪；
- **验收裁定**：以客观的机器可核命令（`pytest`、`tsc`、`ruff`）为准，严禁 LLM 自我说服。

### 4.2 L1 跃迁至 L2 的升级边界（Failure Envelope）

当 Worker 发生以下情况时，必须立即停机，不得私自盲目重试：
1. L1 重试预算耗尽（3 次后单测依然红灯）；
2. 发现 Spec 存在前置逻辑矛盾（如依赖未定义的数据模型）；
3. 遭遇系统级权限或环境缺失（缺少依赖库或迁移命令失败）。

Worker 停机后，将格式化为强类型的 `Failure Envelope` 注入黑板：
```json
{
  "$schema": "https://specs.sdlc.ai/v1/failure-envelope.json",
  "node_id": "worker_order_service_impl",
  "status": "EXHAUSTED_L1_RETRIES",
  "attempts_made": 3,
  "exit_code": 1,
  "error_category": "MISSING_PREREQUISITE_DEPENDENCY",
  "failing_step": "pytest tests/test_orders.py",
  "diagnostic_ast_slice": "ImportError: cannot import name 'TenantContext' from 'common.auth'",
  "suggested_l2_action": "INJECT_PRE_NODE"
}
```

### 4.3 L2 全局拓扑自愈：局部子图切片替换（Sub-graph Splicing）

编排者介入时，坚决禁止全量重写 DAG（防止状态抖动与全图推翻），必须实行**局部子图切片替换**：

1. **绝对冻结成功节点（Immutable Success）**：
   - 处于 `SUCCESS` 状态的前驱节点及其工件在物理上打上只读标记，绝对不允许编排者重新调度或篡改；
2. **三大受限原子改图操作（Atomic Graph Mutations）**：
   编排者只被允许在以下 3 种标准算子中选择，严禁自由捏造图结构：
   - **`INJECT_PRE_NODE`（前置补丁注入）**：在当前失败节点前，动态插入一个修复依赖或数据表的补丁节点，完成后自动重试原节点；
   - **`SPLIT_AND_DEGRADE`（任务分裂降级）**：将由于复杂度过高超时的节点，切片裂变为两个粒度更小、顺序依赖的子节点；
   - **`ROLLBACK_AND_AMEND`（检查点回滚与 Spec 修订）**：利用持久化 Checkpoint 回滚到任务启动态，修正需求冲突字段后重启调度。
3. **全局防死锁硬约束**：
   - **重规划预算硬上限（Max Replanning Budget）**：整个任务生命周期内，L2 动态改图次数不得超过 **2 次**；
   - **同质错误连击阻断**：若同一错误类别在经过一次 L2 切片修复后再次抛出，**坚决停止自动改图，硬性熔断并呼叫人类工程师（HITL）**。

### 4.4 汇聚代码冲突治理协议（Fan-in Merge Conflict Resolution Protocol）

当多个并发 Worker（如 Worker A 与 Worker B）完成各自的分支变更并在 `Aggregator` 节点汇聚时，必须解决两大维度的冲突：

1. **机械层：Git 文本级冲突（Syntactic Merge Conflict）**：
   - 调度器尝试执行 `git merge --no-commit` 汇聚补丁；
   - 若发生冲突，系统禁止让顶层 Planner 模型直接介入（防止无上下文凭空写代码）；
   - **处理规程**：由调度器动态启动一个临时的 **`Conflict Resolver Worker`**，仅将冲突文件的 diff 和双方 TaskSpec 喂给该 Worker，在隔离沙箱内解决冲突并验证 `git merge` 退出码为 0。若一次尝试失败，直接将冲突升级交还人类处理。
2. **逻辑层：语义隐式冲突（Semantic Regression Conflict）**：
   - 即便 Git 顺利自动合入，也可能存在由于接口微调引起的测试击穿（如 A 改了函数签名，B 按照旧签名调用了该函数）；
   - **强制集成回归门禁（Integration Gate）**：汇聚完成后，状态机强制唤醒独立于所有 Worker 的 Clean Test Runner，运行项目的全量测试套件（回归测试）；
   - 若测试挂掉，系统判定此为 **集成级别逻辑冲突**，抛出带集成失败堆栈的 `FailureEnvelope`，由编排者触发 L2 改图，在汇聚节点前插入专职的集成适配节点。

---

## 5. 2026 SOTA 模型五大病理的机器级硬核防御体系

真实工业落地表明，即使使用顶级前沿模型（Claude Opus 5.5, Sonnet 5, OpenAI Sol, Gemini 6 Astra），在面对图工作流时仍存在自发破坏确定性结构的强烈冲动（判读见研究层 [`digested/06`](../../../02_research/01_agent_engineering/graph_engineering/digested/06-sota-model-pathologies-and-defenses.md)）。生产治理必须建立非模型依赖的机器级硬防御：

| 模型病态行为 (Pathology) | 表现症状 | 机器级硬核防御机制 (Hardcore Defenses) |
|---|---|---|
| **① 汇报风暴 (Chatter Storm)** | 模型在未完成任务时频繁向主控输出解释性闲聊，刷爆 Token 并阻塞流水线 | **强制 Hook 拦截器**：严格校验 Worker 输出，若非标准工具调用或格式化工件，由中间件阻断并强制重定向 |
| **② 反驳死锁 (Doom Loop)** | 两个模型节点（如 Dev 与 QA）在聊天中互相质问反驳，陷入无限空转 | **物理单向通道**：消灭对话通道；QA 节点仅输出结构化失败 AST 堆栈，Dev 节点仅能接收诊断数据执行改写 |
| **③ 偷跑虚假完成 (False Done)** | 模型修改或删除断言，伪造测试全绿并提前标记完成 | **只读测试隔离与影子门禁**：测试目录在 Worker 沙箱中挂载为 Read-Only；最终验收由独立无模型环境（Clean Container）纯原生运行 |
| **④ 越权架构侵占 (Scope Creep)** | 局部 Worker 在修改单个函数时擅自重构全局配置或无关模块 | **AST 差异白名单锁**：Git pre-commit Hook 强制拦截超出当前 Task Spec 声明文件范围的任何修改 |
| **⑤ 长程注意力腐败 (Context Rot)** | 编排模型在多轮自愈后遗忘原始高阶约束，引入历史幻觉 | **无状态算子化重置**：每次唤醒编排者时，仅喂入不可变根需求声明 + 当前任务状态拓扑快照，不保留历史改图会话流 |

---

## 6. 人机协作（HITL）与安全熔断机制

自动化的终极边界由**确定性的人类接管协议**保障：

### 6.1 检查点门禁设计（Checkpoint Gates）

在元图中设置三级确定性审批门禁：
1. **P0 架构方案门禁（Pre-Code Gate）**：Planner 生成完 Task DAG 且完成静态语法/无环校验后，必须由人类架构师审批，才能激活 Worker 并发调度；
2. **P1 破坏性变更门禁（Destructive Action Gate）**：涉及数据库 Schema 物理 DROP、公开 API 破坏性变更（Breaking Change）的节点，系统强制挂起等待人类授权（Temporal Signal 机制）；
3. **P2 最终集成发布门禁（Release Gate）**：所有 Worker 绿灯汇聚后，向人类工程师推送集成 Diff 对比视图与自动化安全覆盖率审计报告。

### 6.2 熔断与平稳降级链路

```text
[系统触发熔断条件: 重排达上限 / 致命冲突 / 恶意越权]
                       │
                       ▼
          ┌───────────────────────────┐
          │ 冻结全局状态机 (Pause)     │
          │ 保持 Docker/Worktree 沙箱 │
          └─────────────┬─────────────┘
                        │
                        ▼
          ┌───────────────────────────┐
          │ 导出现场诊断复盘包 (Bundle) │
          │ - 当前 DAG 拓扑状态快照   │
          │ - 各节点工件与 AST 错误栈  │
          │ - 建议人类介入的排错分支   │
          └─────────────┬─────────────┘
                        │
                        ▼
          [平稳交还给人类工程师 (CLI / PR)]
```

- **现场完好保留**：熔断发生时，严禁清理失败现场的 Git Worktree 分支与容器日志，确保人类工程师介入时能 100% 复现案发现场；
- **优雅导出排错 Bundle**：系统打包生成包含 DAG 拓扑图、各节点工件产物和失败堆栈的 Markdown 复盘报告。

### 6.3 图级经济与 Token 硬配额治理（Graph Cost & Token Quotas）

多 Agent 图并发与 L2 动态改图是 Token 消耗黑洞。生产系统必须建立分级硬配额，防止因死循环或大模型失控造成巨额财务与算力损耗：

1. **图级全局双硬上限（Dual Hard Caps per Execution）**：
   - **Token 配额上限（Max Graph Tokens）**：单个任务生命周期内所有节点累计消耗 Token 达到阈值（如预设 1,000,000 Tokens）时，状态机立即执行无条件挂起（Pause）；
   - **财务成本上限（Cost Cap in USD）**：按调用模型的费率实时计量，达到预算红线（如单个 Issue 重构设上限 \$10）立即强行熔断转人工。
2. **节点级动态预算分配（Node-level Budgeting）**：
   - Planner 在生成 `TaskDAGSpec` 时，必须为每个子任务显式标注 `token_budget`；
   - Worker 节点内部消耗逼近预算 80% 时触发告警，达到 100% 时终止该节点并抛出 `TASK_COMPLEXITY_TIMEOUT` 异常信封，交由 L2 拓扑切片拆解为更小的子任务，杜绝单节点无底洞消耗。

---

## 7. 接口与兄弟主题分工

```text
                       03_practice/requirements_engineering
                                       │ 产出需求规格
                                       ▼
                       03_practice/spec_driven_development
                                       │ 产出结构化 Spec JSON
                                       ▼
    ┌────────────────────────────────────────────────────────────────────────┐
    │                 03_practice/graph_governance (本主题)                   │
    │  - 拓扑调度 (DAG) / 强类型工件路由 / Session 外持久化状态机 / L2 自愈  │
    └──────────────────┬──────────────────────────────────┬──────────────────┘
                       │ 调度单个任务                      │ 状态转移判据边
                       ▼                                  ▼
      ┌──────────────────────────────────┐   ┌───────────────────────────────┐
      │   03_practice/harness_governance │   │ 02_research/agent_goal_eval   │
      │   (物理沙箱隔离、代码执行环境)   │   │ (Goal 完成条件与客观 Eval)    │
      └────────────────┬─────────────────┘   └───────────────────────────────┘
                       │ 内部微循环
                       ▼
      ┌──────────────────────────────────┐
      │   03_practice/loop_governance    │
      │   (单节点 L1 自愈、有限退避重试) │
      └──────────────────────────────────┘
```

- **与 `harness_governance`**：本主题将每一个 Task 实例下发给 Harness 提供的隔离沙箱执行，Harness 保证节点内执行环境无污染；
- **与 `loop_governance`**：每个 Worker 节点内部由 Loop Governance 管理 L1 有限重试；一旦 L1 耗尽，Loop Governance 负责格式化 `Failure Envelope` 交还给本主题接管 L2 拓扑自愈；
- **与 `goal_eval_engineering`**：Graph 中的状态转移边由 Goal/Eval 的判定结果驱动，本主题不发明评估算法，直接使用 Eval 的返回结果作为分支流转的路由键。
