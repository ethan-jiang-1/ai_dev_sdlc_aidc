# 02 · DeepSeek Harness (`dsh`)：Cordis 插件底座与显式 Task DAG

> **摘要**：深度剖析 DeepSeek 官方开源的 Agent 运行基座 **DeepSeek Harness (`dsh`)**。解密其基于 **Cordis** 的“一切皆插件”时空组合性架构、`dsh-agent-teams` 插件实现的显式依赖 Task DAG 动态调度、事件溯源（Event-Sourcing）会话日志以及 Web 端动态 DAG 实时可视化看板。

---

## 1. 核心设计哲学：“Agent = Model + Harness”

DeepSeek 官方在推出 `dsh` 时，明确界定了模型与运行环境的边界：
- **模型（Model）是马，基座（Harness）是缰绳与底盘**；
- 无论底层接入的是 DeepSeek 模型还是第三方异构模型，复杂工程任务的稳定性 80% 取决于 Harness 提供的上下文隔离、工具沙箱和拓扑调度。

基于这一哲学，`dsh` 基于 **Cordis** 框架构建，其最大技术特色是 **“一切皆插件（Spatiotemporal Composability）”**：
- 模型适配器（Model Adapter）、工具注册表（Tool Registry）、会话日志（Session Log）、执行沙箱（Sandbox）、甚至整个 Agent 循环本身（Agent Loop）都是可插拔的模块；
- 开发者可以通过一份 YAML 配置文件或动态指令，彻底替换系统某一部件的运行逻辑。

---

## 2. 动态工作流与 `dsh-agent-teams` 的显式 Task DAG

在动态任务编排上，DeepSeek Harness 彻底摒弃了弱类型的扁平待办清单，通过 `dsh-agent-teams` 插件构建了**具备拓扑就绪驱动的显式 Task DAG 调度系统**。

```
[User Objective]
      │
      ▼
[Captain (主控规划者)] ──(动态分析并生成 Task DAG JSON)──┐
      │                                                │
      ▼                                                ▼
[拓扑依赖就绪队列 (In-Degree = 0)]               [交互式 Web DAG 看板]
      │                                                │ (实时动态高亮)
      ├──> [Task A (无依赖)] ──> 调度 Worker 1 ───────┤
      │                                                │
      ├──> [Task B (依赖 A)] ──> [挂起等待 A 完成] ────┤
      │                                                │
      └──> [Task C (无依赖)] ──> 调度 Worker 2 ───────┘
```

### 2.1 Task DAG 的动态生成与依赖校验
当 Captain 接收任务后，输出标准化的依赖图元数据：
```yaml
# dsh-agent-teams 动态生成的任务依赖图示例
tasks:
  - id: analyze_schema
    name: "解析数据库旧版 Schema"
    dependencies: []
    assigned_role: "DBArchitect"
  - id: generate_migration_ddl
    name: "编写增量迁移 SQL"
    dependencies: ["analyze_schema"] # 显式前置依赖
    assigned_role: "SQLCoder"
  - id: write_rollback_script
    name: "编写回滚逻辑"
    dependencies: ["analyze_schema"] # 并行分支依赖
    assigned_role: "SQLCoder"
  - id: dry_run_migration
    name: "在隔离沙箱中执行演练与对账"
    dependencies: ["generate_migration_ddl", "write_rollback_script"] # 汇聚等待
    assigned_role: "QAEngineer"
```
调度器内核持续运行入度检测：
- 任务初始时，`dependencies` 为空的节点（如 `analyze_schema`）直接进入 **Ready 队列**；
- 拥有前置依赖的任务处于 **Pending 阻塞态**；
- 当上游节点交付合格工件并被 Reviewer 验收后，下游任务的入度减 1，一旦归零立即自动激活。

### 2.2 事件溯源（Event-Sourcing）与拓扑级断点回滚
- **Append-only 会话日志**：`dsh` 的所有状态流转都是只追加的事件流（TaskCreated, TaskReady, TaskAssigned, TaskSuccess, TaskFailed）；
- **拓扑级 Session Rollback**：如果 `dry_run_migration` 演练失败，用户或 Captain 可以精准指定将状态回退到 `generate_migration_ddl` 重新生成，而**无须推翻或重跑已经确认为成功的 `analyze_schema`**，做到了精准的局部拓扑手术。

### 2.3 沉浸式 Web 动态 DAG 可视化界面
通过 `npx @deepseek-ai/dsh web` 启动时，系统提供第一视角的实时 DAG 看板：
- **节点拓扑实时染色**：灰色（Pending）、黄色（Running）、绿色（Success）、红色（Failed）；
- **深度硬核 Telemetry 暴露**：直接在界面展示每个节点的生成速率（Tokens/sec）、KV Cache 命中率、会话轮数、沙箱内存占用，让图工程从“黑盒抓瞎”变为“白盒透明调优”。

---

## 3. 对比：DeepSeek Harness vs DeerFlow vs Claude Code

| 维度 | DeepSeek Harness (`dsh`) | 字节跳动 DeerFlow 2.0 | Anthropic Claude Code |
|---|---|---|---|
| **任务数据结构** | **显式 Task DAG**（前驱/后继依赖拓扑） | 扁平 `todos`（无依赖边） | 代码脚本内原生 `async/await` 依赖 |
| **调度触发机制** | 拓扑入度清零（In-degree = 0）自动派发 | LLM 在单 Context 里主动 Tool Call | JS 引擎执行 `Promise.all` 等控制流 |
| **可观测性** | Web 端实时交互式 DAG 拓扑图 + 指标 | TUI 文本日志流 + LangSmith | 终端进度条 + 最终聚合文件 |
| **回滚与自愈** | 拓扑级节点回退（保留已成功节点） | 全靠模型在对话里重新派任务 | 脚本级 `try-catch` 重试 |

---

## 4. 总结与启示

DeepSeek Harness 展现了国内顶尖团队在开源 Harness 领域的工程深度：它证明了通过**“插件化架构 + 显式 Task DAG 调度 + 事件溯源日志”**，能够将原本不可控的大模型多步骤协作，驯化为高度可预测、可审计、可局部回滚的工业级研发流水线。
