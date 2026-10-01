# 04. 工件契约、A2A 协作协议与全局共享黑板状态机

> **判读依据**：`raw/evidence-20261001-field-exchange.md`（Raven A2A 协议）、`raw/evidence-2026-langgraph-temporal-state-machines.md`。

---

## 1. 从“自然语言闲聊”到“强类型工件（Typed Artifacts）”

在 Graph Engineering 中，多智能体之间的协作介质发生了根本性的范式转移：
- **反模式**：上游 Agent 用一段 Markdown 提示词告诉下游：“我已经把接口写好了，你顺便写个前端组件吧”；
- **生产范式**：上游 Agent 产出标准化的结构化工件，写入全局存储，由状态机校验其 JSON Schema 与物理文件完整性后，才向后继节点传递。

```text
               ┌────────────────────────────────────────────────────────┐
               │         Shared Blackboard / State (黑板存储)            │
               │   - artifacts/specs/v1_auth_spec.json                  │
               │   - artifacts/patches/feat_auth_login.patch            │
               │   - artifacts/reports/test_coverage_report.json        │
               └───────────▲────────────────────────────────┬───────────┘
                           │ Write (原子性写入)              │ Read (按需只读投影)
                           │                                │
                 ┌─────────┴─────────┐            ┌─────────▼─────────┐
                 │  Upstream Worker  │            │ Downstream Worker │
                 │  (只写特定工件)   │            │ (只读依赖工件)    │
                 └───────────────────┘            └───────────────────┘
```

---

## 2. 强类型工件契约设计（Artifact Schema Specification）

在图拓扑中流转的工件必须满足机器可判的 Schema。常见的核心工件类型包括：

### ① 需求与架构规范工件（Spec Artifact）
```json
{
  "$schema": "https://specs.sdlc.ai/v1/task-spec.json",
  "task_id": "feat_jwt_auth_service",
  "goal": "Implement JWT authentication with refresh token rotation.",
  "contracts": {
    "interfaces": [
      "POST /api/v1/auth/login",
      "POST /api/v1/auth/refresh"
    ],
    "database_tables": ["users", "refresh_tokens"]
  },
  "acceptance_criteria": [
    "pytest tests/test_auth.py passes with 100% assertions",
    "zero ruff lint errors in src/auth/"
  ]
}
```

### ② 代码补丁工件（Code Patch Artifact）
- 不直接覆盖工作树，而是生成标准 Unified Diff / Git Patch；
- 状态机可调用 `git apply --check` 进行无副作用的预检。

### ③ 测试与诊断报告工件（Verification Report Artifact）
- 包含标准化的测试执行摘要、代码覆盖率与失败用例的结构化断言。

---

## 3. 全局共享黑板架构（Blackboard Architecture）

为了避免多 Agent 之间点对点（P2P）全连接通信带来的复杂度和状态不一致，Graph Engineering 普遍采用经典**黑板架构（Blackboard Pattern）**：

1. **状态单点事实来源（Single Source of Truth）**：
   - 所有节点的执行状态（`PENDING`、`RUNNING`、`SUCCESS`、`FAILED`、`RETRYING`）和交付工件统一注册在黑板上；
2. **读写权限严格单向控制（Least Privilege Access）**：
   - 每个 Worker 节点在启动时，只被授予对黑板上其“直接前驱节点工件”的**只读访问权**；
   - 每个 Worker 仅被授予对其“自身目标工件”的**写权限**；严禁任何 Worker 修改其他节点的历史输出或篡改黑板全局变量。
3. **版本化快照（Immutable Snapshots）**：
   - 每次节点写入都会生成黑板状态的新版本号（Revision）；
   - 支持图状态机任意时刻回溯至某一 Revision 执行分支。

---

## 4. 物理文件系统隔离机制：基于 Git Worktree 的解耦

在 AI Coding 任务中，如果两个并发 Worker（Fan-out）在同一个本地文件夹内同时读写文件，必然造成不可挽回的写入覆盖与冲突。

生产级 Graph Engineering 采用**基于 Git 的物理隔离策略**：

```text
[主仓库 Repository: main branch]
       │
       ├─ git worktree add ../wt-worker-backend (分支: agent/backend-task)
       │  └── Backend Worker 在此目录隔离运行与单测
       │
       └─ git worktree add ../wt-worker-frontend (分支: agent/frontend-task)
          └── Frontend Worker 在此目录隔离运行与单测
```

### 协作流转：
1. **并发隔离**：编排器为每个并发 Worker 派生独立的 `git worktree` 和临时功能分支；
2. **局部验证**：Worker 在自己专属的沙箱目录内运行 `npm test` 或 `pytest`；
3. **汇聚节点合并（Integration Merge Gate）**：
   - 当两边的工件均通过单测后，流程流转至汇聚节点；
   - 汇聚节点执行 `git merge`，若遇到冲突，调用专门的代码合并与冲突裁决 Agent；
   - 最终跑全量集成测试套件，合格后提 PR。

---

## 5. A2A（Agent-to-Agent）协作协议的轻量化演进

参考 Raven 框架的 A2A 实践，节点间的交互协议必须满足：
- **无状态请求（Stateless RPC）**：调用方不假设被调用方拥有对话记忆；
- **自包含上下文包（Self-contained Payload）**：每次调度携带该任务所需的一切输入工件 URI 与边界约束；
- **异步响应与心跳（Async Completion & Liveness）**：对于长耗时代码编写任务，采用轮询状态机或 Webhook 回调，杜绝长连接阻塞与超时浪费。
