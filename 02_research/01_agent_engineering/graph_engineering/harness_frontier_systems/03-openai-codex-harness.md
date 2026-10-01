# 03 · OpenAI Codex 体系：Worktree 物理隔离与 Manifest 任务流深度解密

> **摘要**：系统解剖 OpenAI Codex Agent Harness（驱动终端 Codex CLI、Operator 及后台 App Server 的脚手架工程层）。深度解析其基于 **Git Worktrees 的物理并发拓扑引擎**、**Plan-First 模式下的强类型 Manifest 任务依赖规范**、通过 **JSON-RPC App Server 与外部状态机（如 Temporal / CI）** 的双向拦截门禁，以及针对 OpenAI Sol / o 系列模型“深度推理冻结（Reasoning Freeze）”的工程级心跳防御。

---

## 1. 架构定调：Scaffolding（脚手架）作为 Agent 生产底盘

OpenAI 在工程演进中深刻认识到：**代码大模型绝不能直接裸露操作宿主环境**。驱动 Codex CLI 与自动化流水线的核心是底层的 **Codex Harness (Scaffolding)**。

该 Harness 在逻辑上被严密划分为三层：

```
┌────────────────────────────────────────────────────────────────────────┐
│                        外部调度面 (External Control Plane)             │
│   - CI/CD 流水线 / 企业工单系统 / Temporal 外部状态机 / 人工终端 TUI    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ JSON-RPC 2.0 (stdio / Unix Socket)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                     Codex App Server (常驻 Harness 守护进程)            │
│                                                                        │
│  - 状态机控制器 (State Engine): 会话快照、单步断点、暂停与恢复         │
│  - 契约治理器 (Policy Engine): 加载 AGENTS.md 规则、权限白名单          │
│  - 心跳探测器 (Heartbeat Fencing): 监测 Sol/o3 模型深度思考死锁        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ 本地文件系统 / Git API / Shell 子进程
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                 Git Worktrees 物理并行沙箱矩阵 (Execution Matrix)       │
│                                                                        │
│  ┌─────────────────────────┬─────────────────────────┬──────────────┐  │
│  │ .worktrees/task-feat-1  │ .worktrees/task-feat-2  │ ...          │  │
│  │ (Branch: codex/task-1)  │ (Branch: codex/task-2)  │              │  │
│  │ - 物理独立的工作目录    │ - 物理独立的工作目录    │              │  │
│  │ - 独立的 AST Diff 监控  │ - 独立的 AST Diff 监控  │              │  │
│  │ - 独立的单测执行进程    │ - 独立的单测执行进程    │              │  │
│  └────────────┬────────────┴────────────┬────────────┴───────┬──────┘  │
│               │                         │                    │         │
│               └─────────────────────────┼────────────────────┘         │
│                                         ▼                              │
│             [Fan-in 汇聚引擎: AST 冲突检测 -> 自动化 Rebase 合并]        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Git Worktrees 物理并发拓扑引擎

传统 Agent 尝试并发修改同一个仓库时，必然引发 `git status` 脏读、文件写入覆盖以及未提交代码冲突。Codex Harness 从底层操作系统和 Git 特性出发，设计了 **基于 Git Worktrees 的物理并发调度模式**。

### 2.1 任务生命周期与底层 Git 编排命令
当主控决定并发派发 N 个独立的子任务时，Harness 底层自动执行确定性的 Git 状态流转：

```bash
# 1. 为 Task 1 创建物理隔离工作区及独立分支
git worktree add -b codex/task-auth-fix .worktrees/task-auth-fix HEAD
# 2. 为 Task 2 创建物理隔离工作区及独立分支
git worktree add -b codex/task-cache-impl .worktrees/task-cache-impl HEAD

# 3. 各子代理进入独立工作目录执行修改并提交
cd .worktrees/task-auth-fix && git commit -am "fix(auth): update token expiration logic"
cd .worktrees/task-cache-impl && git commit -am "feat(cache): add redis lru adapter"

# 4. 主控调度 Fan-in 汇聚：逐个 Rebase 回主干
git checkout master
git merge --ff-only codex/task-auth-fix
git rebase master codex/task-cache-impl
git merge --ff-only codex/task-cache-impl

# 5. 任务清理：强制销毁临时工作树与分支
git worktree remove --force .worktrees/task-auth-fix
git worktree remove --force .worktrees/task-cache-impl
git branch -D codex/task-auth-fix codex/task-cache-impl
```

### 2.2 为什么 Git Worktrees 彻底优于内存虚拟文件系统？
1. **绝对的物理级读写隔离**：每个子代理拥有独立的进程工作目录与独立的文件描述符，互不影响；
2. **原生编译器与测试工具链兼容**：诸如 `cargo test`、`go test`、`npm run build` 等需要读取真实物理磁盘文件的工具链可以直接就地运行，不需要重写任何 VFS 拦截层；
3. **天然的版本回滚与审计能力**：每个子任务生成标准的 Git Commit，任何失败步骤只需简单的 `git reset --hard` 或删除工作区，状态清零成本为零。

---

## 3. Plan-First 模式下的 Manifest 任务规范

Codex CLI 严禁模型在复杂任务中“端上来就盲目改代码”，而是强制执行 **Plan-First**：先生成严格强类型的 Manifest 文件，经校验通过后再驱动执行。

### 3.1 工业级 Manifest 拓扑规范（TOML Schema）
```toml
[workflow]
id = "wf_20261001_auth_refactor"
objective = "重构用户认证鉴权模块，迁移至 JWT RS256 签名"
max_replan_limit = 2

[[workflow.step]]
id = "step_1_keygen"
title = "生成公私钥对生成工具与配置载入"
assigned_role = "SecurityEngineer"
dependencies = [] # 根节点，无前驱
workspace_files = ["pkg/crypto/keys.go", "config/auth.yaml"]
assertions = [
  "go vet ./pkg/crypto/...",
  "go test -v ./pkg/crypto/ -run TestKeyGeneration"
]
rollback_action = "git checkout -- pkg/crypto/ config/auth.yaml"

[[workflow.step]]
id = "step_2_jwt_signer"
title = "实现 RS256 签名器与校验器"
assigned_role = "BackendEngineer"
dependencies = ["step_1_keygen"] # 显式前置依赖
workspace_files = ["internal/auth/jwt.go", "internal/auth/jwt_test.go"]
assertions = [
  "go test -v ./internal/auth/ -run TestSignAndVerify",
  "golangci-lint run internal/auth/..."
]
rollback_action = "git checkout -- internal/auth/"

[[workflow.step]]
id = "step_3_middleware"
title = "Gin 路由中间件接入鉴权逻辑"
assigned_role = "BackendEngineer"
dependencies = ["step_2_jwt_signer"] # 强顺序依赖
workspace_files = ["internal/middleware/auth.go"]
assertions = [
  "go test -v ./internal/middleware/ -run TestAuthMiddleware"
]
rollback_action = "git checkout -- internal/middleware/"
```

### 3.2 强断言门禁（Assertion Runner）
调度器执行每一个 `step` 时，模型修改完毕后必须原地触发 `assertions` 数组里的每一条 Shell 命令：
- 若全部命令返回 exit code 0，该 Step 标记为 `PASSED`，生成 Git Commit；
- 若任意命令报错，直接捕获 stderr，注入模型重试槽位（最多 3 次局部微循环）；
- 若 3 次重试依然失败，触发 `rollback_action`，任务暂停并向上抛出中断异常。

---

## 4. JSON-RPC App Server 协议与外部状态机集成

Codex App Server 提供了工业标准的 JSON-RPC 2.0 接口，使得企业级编排引擎（如 Temporal、Camunda、Airflow 或自研 CI Runner）能够将 Codex 作为受控算子挂载进更大的企业业务流中。

### 4.1 核心协议报文示例
```json
// 外部调度器向 Codex App Server 下发：启动受控任务
{
  "jsonrpc": "2.0",
  "id": "req-101",
  "method": "codex/task.start",
  "params": {
    "manifestPath": "workflows/auth_refactor.toml",
    "executionMode": "STEP_BY_STEP",
    "gitWorktreeRoot": ".worktrees/"
  }
}

// Codex App Server 实时向外部上报步骤状态流
{
  "jsonrpc": "2.0",
  "method": "codex/step.status",
  "params": {
    "stepId": "step_1_keygen",
    "status": "ASSERTIONS_PASSED",
    "commitHash": "a1b2c3d4",
    "tokensUsed": 4520
  }
}

// 外部状态机下发强干预指令（例如门禁未批复，要求暂停执行）
{
  "jsonrpc": "2.0",
  "id": "req-102",
  "method": "codex/session.pause",
  "params": {
    "reason": "WAITING_FOR_SECURITY_LEAD_APPROVAL"
  }
}
```

---

## 5. 顶级模型行为攻防：OpenAI Sol 深度推理冻结（Reasoning Freeze）

在接入 2026 年 OpenAI Sol 及 o 系列深度推理模型时，Codex Harness 重点解决了著名的 **“深度推理冻结（Reasoning Freeze）”** 陷阱：

### 5.1 现场病理
- 当面对极复杂的算法逻辑或并发竞争排查时，Sol 模型会展开长达 120~240 秒的深层思维链（Deep Thought Chain）；
- 在此期间，模型**不输出任何 Token、不调用任何工具**，从外部观察宛如系统假死或网络超时挂断；
- 传统的 HTTP Client 会因为 Read Timeout 暴力掐断连接，导致昂贵的深思过程全部报废。

### 5.2 Harness 层防御：心跳租约与思维流泵（Thinking Heartbeat Pump）
- **心跳流式保活（Progress Ping）**：Harness 在与模型服务通信时强制启用底层 Stream 传输，捕获模型的思维链心跳信号（Reasoning Chunks）；
- **动态超时退避租约**：根据当前任务的复杂度标签，动态将外部沙箱的硬超时上限从默认的 60 秒扩容至 300 秒，避免被杀；
- **防抢占保护（Preemption Lock）**：在 Sol 进行深度推理期间，Harness 锁定当前 Worktree 的状态，禁止外部任何异步事件抢占打断模型的推理上下文。
