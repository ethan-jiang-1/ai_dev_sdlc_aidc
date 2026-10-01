# 07. L2 拓扑自愈实操：局部子图切片替换（Sub-graph Splicing）与防死锁算法

> **判读依据**：`raw/evidence-20261001-field-exchange.md`（Jarvan 日成：“Worker 修不了的让编排者改 DAG 再重试”）、`raw/evidence-2026-langgraph-temporal-state-machines.md`。

---

## 0. 核心痛点：为什么“全量重新生图（Full Graph Regeneration）”是灾难？

当 Worker 节点在 L1 局部重试耗尽（如 3 次单测均失败）向上抛出异常时，初级编排系统往往会犯一个严重错误：
- **反模式**：把当前报错扔回给顶层 Planner 模型，让其“根据错误重新为整个项目生成一份全新的 DAG”。
- **灾难后果**：
  1. **状态抖动（State Churn）**：大模型的非确定性会导致它改写原本已经成功运行通过的前驱节点，导致系统无谓地重跑大量已有成果；
  2. **元死循环（Meta Doom Loop）**：编排模型和 Worker 互相推诿——Worker 报错说 Spec 不清，Planner 改了 Spec 后 Worker 报错缺少依赖，系统在宏观重规划上无限消耗预算；
  3. **拓扑失控**：频繁全量重排极易在复杂图拓扑中引入隐式循环引用（Deadlock Cycles）。

---

## 1. 生产级解法：局部子图切片替换（Sub-graph Splicing）

生产级 Graph Engineering 采用**局部子图切片替换（Sub-graph Splicing）**：
- **绝对冻结已成功的节点**：所有处于 `SUCCESS` 状态的节点及其生成的工件被标记为不可变（Immutable）；
- **仅针对失败节点进行受限手术**：编排器只能在失败节点与其直接前驱/后继之间进行局部拓扑切片改造。

```text
[初始状态: Worker B 失败]
   Node A (SUCCESS - 已冻结) ───► [Node B (FAILED)] ───► Node C (PENDING - 挂起)

[L2 局部子图切片替换: 编排者介入]
   Node A (SUCCESS - 保持冻结)
       │
       ▼
   ┌────────────────────────────────────────────────────────┐
   │ 替换生成的子图切片 (Sub-graph Splice)                  │
   │                                                        │
   │  [Node B.1: 诊断环境并生成补丁]                         │
   │            │                                           │
   │            ▼                                           │
   │  [Node B.2: 降低粒度重试实现]                           │
   └───────────────────────────┬────────────────────────────┘
                               │
                               ▼
                        Node C (恢复调度)
```

---

## 2. 强类型异常信封（Failure Envelope）规范

L1 失败向 L2 升级时，必须携带机器可判读的结构化异常包，绝不允许使用散漫的纯文本自然语言：

```json
{
  "$schema": "https://specs.sdlc.ai/v1/failure-envelope.json",
  "node_id": "worker_db_migration_user_tenant",
  "status": "EXHAUSTED_L1_RETRIES",
  "attempts_made": 3,
  "last_exit_code": 1,
  "failure_classification": "MISSING_PREREQUISITE_DEPENDENCY",
  "failing_command": "alembic upgrade head",
  "error_telemetry": {
    "stdout_tail": "Running migrations...",
    "stderr_tail": "sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: organizations"
  },
  "context_state": {
    "git_commit": "e83f2a1b",
    "worktree_path": "/tmp/wt-worker-db"
  },
  "suggested_replanning_action": "INJECT_PREREQUISITE_NODE"
}
```

---

## 3. 编排者改图的三大受限原子操作（Atomic Graph Mutations）

编排模型在调用图重排工具时，只能在以下三种预定义的原子操作中选择，不允许自由发挥：

### 原子操作 1：注入前置补丁节点（`INJECT_PRE_NODE`）
- **触发场景**：错误分类为 `MISSING_PREREQUISITE`（例如：缺少组织表）。
- **动作**：在当前失败节点前，动态注入一个 `Node_Fix_Org_Table`，并自动把前驱输出和依赖关系连接上。
- **验证**：注入的新节点完成后，原失败节点以重置后的上下文重新触发。

### 原子操作 2：节点分裂与降级（`SPLIT_AND_DEGRADE`）
- **触发场景**：错误分类为 `TASK_TOO_COMPLEX` 或 `TIMEOUT`。
- **动作**：将单个大任务切片为两个串行的更小粒度节点（例如：先写数据结构与接口桩，再写核心逻辑）；
- **参数约束**：降低每个子任务的上下文范围与预计代码行数。

### 原子操作 3：回滚检查点并修订规范（`ROLLBACK_AND_AMEND`）
- **触发场景**：错误分类为 `SPEC_LOGIC_CONTRADICTION`（需求本身自相矛盾）。
- **动作**：
  1. 状态机借助持久化检查点，将代码库与共享状态回退到 `PLAN_INITIALIZED` 的版本；
  2. 针对性修改 Spec JSON 中的冲突字段；
  3. 重新激活调度流程。

---

## 4. 防死锁与收敛性保障算法

为了确保图工程不会因为动态改图而在生产中变成无限消耗算力的黑洞，系统必须内置三道硬性防死锁规则：

### 规则一：全局重规划预算硬上限（Global Replanning Budget）
```python
class GraphExecutionController:
    MAX_GLOBAL_REPLANS = 2

    def handle_l2_failure(self, failure_envelope: FailureEnvelope):
        self.replanning_counter += 1
        if self.replanning_counter > self.MAX_GLOBAL_REPLANS:
            # 耗尽重规划预算，坚决终止自动重排，强制升级为人工审批 (HITL)
            self.transition_to_state("PAUSED_AWAITING_HUMAN_INTERVENTION", {
                "reason": "Exceeded maximum global replanning budget (2).",
                "last_failure": failure_envelope
            })
            return
        
        # 执行受限子图切片替换
        self.apply_subgraph_splice(failure_envelope)
```

### 规则二：改图后静态拓扑校验器（Static DAG Validator）
任何由大模型生成的子图切片在应用前，必须经过确定性算法检验：
1. **拓扑排序（Topological Sort / Kahn's Algorithm）**：检查是否存在循环依赖；
2. **端点可达性检查（Sink Reachability）**：确保从起始节点到最终验收节点（Integration Gate）存在连续路径，不存在孤立悬挂节点。

### 规则三：单调收敛性递减约束（Monotonic Convergence Check）
- 如果连续两次改图产生的错误类型相同（例如：两次重规划后仍然报错组织表不存在），状态机立即熔断，不再尝试第三次，直接转人工。这彻底斩断了“模型自我安慰式重试”的可能。
