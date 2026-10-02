# 技术与架构场练习讲者卡与标准实现（Facilitator Guide）

> 本文件供技术场 Keynote 讲者使用，包含硬核判分标准、官方标准 JSON/脚本参考实现与深水区原理解析。

---

## 练习一（双轨元图任务数据 Schema 构造）

### 判分红线
- 任务数据必须是纯 JSON，绝不能输出 Python 图编译代码；
- 任务 1 的 `dependencies` 为空数组 `[]`；任务 2 和 3 的 `dependencies` 必须显式声明包含 `["task_api_spec"]`；
- 必须包含清晰的 `allowed_files` 路径白名单与 `token_budget` 配额。

### 官方标准参考实现
```json
{
  "$schema": "https://specs.sdlc.ai/v1/task-dag-spec.json",
  "dag_id": "dag_trade_microservice_refactoring_001",
  "created_at": "2026-10-02T10:00:00Z",
  "tasks": [
    {
      "task_id": "task_api_spec",
      "name": "Design Inter-Service API Contract",
      "dependencies": [],
      "allowed_files": ["specs/api/v1/trade_contracts.json"],
      "token_budget": 50000,
      "status": "PENDING"
    },
    {
      "task_id": "task_order_impl",
      "name": "Refactor Order Fulfillment Service",
      "dependencies": ["task_api_spec"],
      "allowed_files": ["services/order/**/*"],
      "token_budget": 150000,
      "status": "PENDING"
    },
    {
      "task_id": "task_points_impl",
      "name": "Implement Points Settlement Service",
      "dependencies": ["task_api_spec"],
      "allowed_files": ["services/points/**/*"],
      "token_budget": 150000,
      "status": "PENDING"
    }
  ]
}
```

---

## 练习二（Failure Envelope 与 L2 子图切片变异）

### 判分红线
- **信封字段完备**：包含 `node_id`、`attempts_made: 3`、`error_category`、精确的 AST 报错行；
- **受限原子变异**：操作算子必须为 `INJECT_PRE_NODE`；
- **依赖重连与冻结**：动态注入的补丁节点 `task_inject_auth_dependency` 的依赖继承自原节点（即依赖 `task_api_spec`），而原失败节点 `task_points_impl` 的 `dependencies` 被更新重连为 `["task_inject_auth_dependency"]`；原成功的 `task_order_impl` 保持 `SUCCESS` 且只读上锁。

### 官方标准参考实现
#### 1. FailureEnvelope JSON
```json
{
  "$schema": "https://specs.sdlc.ai/v1/failure-envelope.json",
  "node_id": "task_points_impl",
  "status": "EXHAUSTED_L1_RETRIES",
  "attempts_made": 3,
  "exit_code": 1,
  "error_category": "MISSING_PREREQUISITE_DEPENDENCY",
  "failing_command": "pytest services/points/tests/",
  "diagnostic_ast_slice": "ImportError: cannot import name 'TenantContext' from 'common.auth'",
  "suggested_l2_action": "INJECT_PRE_NODE"
}
```

#### 2. L2 切片变异声明（Sub-graph Splicing）
```json
{
  "mutation_type": "INJECT_PRE_NODE",
  "target_node_id": "task_points_impl",
  "injected_node": {
    "task_id": "task_inject_auth_dependency",
    "name": "Install and Configure common.auth Dependency",
    "dependencies": ["task_api_spec"],
    "allowed_files": ["services/points/pyproject.toml", "common/auth/**/*"],
    "token_budget": 40000,
    "status": "PENDING"
  },
  "dependency_rewiring": {
    "task_points_impl": {
      "dependencies": ["task_inject_auth_dependency"],
      "status": "WAITING_PREREQUISITE"
    }
  },
  "immutable_nodes": ["task_api_spec", "task_order_impl"]
}
```

---

## 练习三（针对 SOTA 模型病理的机器级防御）

### 判分红线
- **只读挂载**：必须给出操作系统/容器层针对测试目录的只读设置，说明模型在沙箱内无论执行何种写操作都会被系统内核拒绝；
- **白名单比对**：必须给出 Git Hook 中针对 `git diff --name-only` 与白名单集合的比对逻辑，越界文件必须直接中断退出。

### 官方标准参考实现
#### 1. 测试目录只读挂载（Docker / Linux 容器配置）
```bash
# 在拉起 Worker 沙箱容器时，将包含测试用例的目录挂载为严格只读 (:ro)
docker run -d \
  -v $(pwd)/src:/workspace/src:rw \
  -v $(pwd)/tests:/workspace/tests:ro \
  --name worker-points-sandbox \
  worker-agent-image:latest
```

#### 2. AST / 文件白名单 Git Pre-commit Hook 脚本
```bash
#!/usr/bin/env bash
set -euo pipefail

# 从当前 TaskSpec 中提取声明的允许修改白名单列表 (例如从环境变量中读取)
ALLOWED_PATTERN="services/points/"

# 检查当前 Git Staged 变更的所有文件列表
CHANGED_FILES=$(git diff --cached --name-only)

for FILE in $CHANGED_FILES; do
  # 规则一：严禁任何对 tests/ 目录的修改写入
  if [[ "$FILE" =~ ^tests/ ]]; then
    echo "❌ [Shadow Gate 拦截]: 检测到模型试图篡改测试用例 '$FILE'！" >&2
    exit 1
  fi

  # 规则二：严禁超出 TaskSpec 白名单范围修改核心代码
  if [[ ! "$FILE" =~ ^$ALLOWED_PATTERN ]]; then
    echo "❌ [AST 白名单拦截]: 越权架构侵占！文件 '$FILE' 超出本子任务授权范围！" >&2
    exit 1
  fi
done

echo "✅ [防御检验通过]: 代码变更完全符合 TaskSpec 白名单约束。"
exit 0
```
