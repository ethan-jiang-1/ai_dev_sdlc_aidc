# 03 · OpenAI Codex 体系：Worktree 物理隔离与 Manifest 任务流

> **摘要**：深度剖析 OpenAI Codex Agent Harness（驱动 Codex CLI、终端 Operator 及后台 App Server 的脚手架工程层）。系统解析其基于 **Git Worktrees 的物理并发拓扑**、**Plan-First 模式下的结构化 Manifest 任务依赖**、以及通过 **JSON-RPC App Server 与 MCP 协议** 实现的外部状态机硬拦截门禁。

---

## 1. 架构定位：Scaffolding（脚手架）作为 Agent 生产底盘

OpenAI 在推动 Codex 从简单的“代码补全”进化到“全自主研发 Agent”的过程中，其核心工程突破在于构建了一套工业级的 **Harness / Scaffolding 层**。该层负责：
- 隔离模型认知与本地物理环境（文件系统、终端命令、环境变量）；
- 管理状态机在时间跨度上的持久化；
- 在多步骤、长周期研发中实施安全沙箱与门禁治理。

---

## 2. 动态工作流与并发拓扑机制

面对复杂的跨文件、多阶段代码工程，Codex 体系没有选择在单一的终端会话里死扛，而是发展出了以下三大核心机制：

### 2.1 Git Worktrees 物理并行调度（Fan-out / Fan-in）
在需要同时重构多个模块或并发运行多个测试套件时，Codex 的主控 Agent 会在操作系统层调用 Git 底层能力：

```
[Main Repository Branch: master]
                │
                ▼
        [Controller Agent]
                │
    ┌───────────┴───────────┐
    ▼                       ▼
[Worktree A 沙箱]       [Worktree B 沙箱]
(Branch: feat/auth)     (Branch: feat/db)
(Subagent 1 独立修改)   (Subagent 2 独立修改)
    │                       │
    ▼                       ▼
[Local Unit Tests]      [Local Unit Tests]
    │                       │
    └───────────┬───────────┘
                │ (Fan-in 汇聚)
                ▼
    [Controller 差异对齐与 Rebase 合并]
                │
                ▼
        [Global PR 生成与门禁验证]
```
- **真正的文件系统隔离**：Subagent 1 修改 `auth.py`，Subagent 2 修改 `db.py`，彼此工作在物理隔离的文件目录中，互不产生文件读写锁冲突和未提交代码污染；
- **分支级可追溯**：每个子任务拥有独立的 Git Commit 历史，失败时直接执行 `git worktree remove`，状态清除彻底且干净。

### 2.2 结构化任务流：Plan-First 模式与 Manifest 依赖
针对复杂歧义任务，Codex CLI 强制引入 **Plan-First** 交互范式：
- 用户输入 `/plan` 指令后，模型不会直接修改代码，而是生成一份**包含显式步骤依赖的 Manifest 方案图**；
- Manifest 明确声明：
  ```toml
  # 结构化任务步骤 Manifest 示例
  [[step]]
  id = "step_1_interface_definition"
  desc = "定义 RPC 接口 protobuf 契约"
  artifacts = ["proto/service.proto"]
  assertions = ["protoc --lint proto/service.proto"]

  [[step]]
  id = "step_2_server_impl"
  desc = "编写服务端业务实现"
  dependencies = ["step_1_interface_definition"] # 显式依赖前置步骤
  artifacts = ["server/service.go"]
  assertions = ["go vet ./...", "go test -run TestServiceBasic"]
  ```
- **硬性断言门禁（Assertion Gates）**：执行器在完成每一步后，必须自动运行 `assertions` 脚本。断言未全部通过前，依赖该步骤的后续 Task 绝对处于冻结状态。

### 2.3 JSON-RPC App Server 与外部状态机协议
为了让外部系统（如企业级 CI/CD、自动化工单系统、Temporal）能够调度 Codex，OpenAI 提供了后台常驻的 **Codex App Server**：
- **JSON-RPC 通信流**：外部编排引擎可以通过标准的 JSON-RPC 协议订阅 Codex 的内部决策事件流；
- **外部强干预能力**：支持外部状态机随时注入 `pause`、`step_rollback`、`inject_feedback` 指令，实现严格的“人机协作（HITL）”或“高阶调度器外部接管”。

---

## 3. 落地对比与启示

Codex 体系给行业的启示在于：**不要试图在内存中虚拟一切，而是善用开发者环境已有的成熟基础设施（Git 分支、Worktrees、Shell 断言、标准 RPC 协议）**：
- 依靠 `git worktree`，用极低的成本换取了绝对的物理并发安全；
- 依靠 Manifest 显式步骤与 Shell 断言，把不可靠的大模型生成约束在了确定性的测试用例铁律之中。
