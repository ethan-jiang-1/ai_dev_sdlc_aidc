# Graph Governance 实践手册（定稿层·操作规程）

> **本文件是什么**：Graph 治理操作规程的定稿——把 [`backbone.md`](backbone.md) §0–§6 的主张展开成**工业级可照做的步骤、Schema 规范、代码模板与反模式清算**。
> 主张与原理在 `backbone.md`；本文件只管**怎么做（SOP）**。

```yaml
topic: Graph Governance —— 实践手册（backbone §0–§6 的工程操作化）
doc_layer: result（定稿层 · 操作规程，SOP 级）
produced_at: 2026-10-02
provenance: >
  研究层 02_research/01_agent_engineering/graph_engineering/digested 01-09 与 landscape；
  工业实证（LangGraph Checkpointer / Send API、Temporal Durable Execution、字节 DeerFlow 2.0 源码校准口径、Claude Code 物理沙箱）。
filter: 工业实战检验有效 > 框架官方规范 > 本主题规程编排
---
```

---

## 0. 用法与导航

- **新场景准入**：从 **§1 诊断准则** 进入，判断是否达到上 Graph 的复杂度阈值；
- **技术选型**：按 **§2 状态机运行时选型决策树** 确定架构底座（进程级 vs 分布式持久化）；
- **系统落地**：
  - 定义契约：照搬 **§3 核心工件与黑板 Schema 规范**；
  - 实现自愈：按照 **§4 L2 局部子图切片替换 SOP** 配置三大原子改图算子；
  - 角色防护：按 **§5 异构模型治理与防御实施规范** 配置拦截器与沙箱锁；
- **演进路线**：遵循 **§6 工业落地演进梯子（P0 → P3）** 逐步升档，严禁跨级过度设计；
- **红线自查**：参考 **§7 反过度工程清算** 排查 7 种典型反模式。

---

## 1. Phase 0 · 诊断准则（要不要 Graph 治理）

### 1.1 三项硬性准入门槛（三条皆满足才允许立图）

1. **上下文边界超载**：单次任务无法在单个 LLM 上下文窗口内高保真完成，代码或检索背景跨越多个不相关子域；
2. **存在显式拓扑依赖或并发**：任务包含两个以上并行分支（Fan-out），或严格的前驱交付物依赖（A 完成生成契约工件，B 才能启动）；
3. **存在结构化交付物契约**：节点之间交接的是可机检的结构化数据（JSON / Patch / 测试报告），而非发散的情绪或自然语言讨论。

### 1.2 系统病征自检清单（对号入座）

| 序号 | 你的系统是否出现以下病征？ | 诊断结论 |
|---|---|---|
| 1 | 试图让“Product Manager Agent”和“Coder Agent”在同一个聊天窗口里讨论需求 | **立即叫停伪群聊**，转为 SDD 静态工件交接（§3） |
| 2 | Worker 在同一个沙箱中修改代码，反复跑挂测试，甚至改坏原本正常的模块 | **缺失 L1/L2 异常隔离**，配置 Worktree 与局部切片（§4） |
| 3 | 任务进行到 80% 时因为某个节点报 429 或网络断开，整条链路全部丢失必须重来 | **缺失 Session 外持久化状态机**，引入 Checkpointer（§2） |
| 4 | 模型经常自行输出“我已经全部完成并测试通过”，但实际上根本没运行测试 | **偷跑虚假完成**，实施只读测试与独立影子门禁（§5） |
| 5 | 当某个子任务失败时，编排模型把前面已经做好的 5 个模块全推翻重新生成一遍 | **全量重规划灾难**，强制实行已成功节点绝对冻结（§4） |

---

## 2. 状态机运行时选型决策树（Session 外持久化底座）

```text
                      [任务长程性与业务容灾需求评估]
                                    │
            ┌───────────────────────┴───────────────────────┐
            ▼                                               ▼
   [进程级任务 / 单机任务]                           [跨服务 / 跨天 / 人机审批流]
   - 典型代表: CLI 终端开发助手                    - 典型代表: 企业级 Issue-to-PR
   - 执行时长: < 30 分钟                           - 执行时长: 数小时至数天
   - 恢复粒度: 单机断点续跑                        - 恢复粒度: 集群级无损漂移恢复
            │                                               │
            ▼                                               ▼
   【选型 A: LangGraph + PG/SQLite】              【选型 B: Temporal / Cadence】
   - 优点: 轻量、与 LLM 原语深度集成               - 优点: 工业级 Durable Execution
   - 机制: Checkpointer 状态持久化                 - 机制: Event Sourcing 事件回放
   - 动态派发: Send() API                          - 动态派发: Child Workflow 并发
```

### 选型落地准则：
- **场景 A（单代码库自动化研发助手）**：推荐 **LangGraph 配合 SQLite/Postgres Checkpointer**。采用固定 Coordinator-Worker 元图，使用 `Send()` 动态扇出 Worker，开发调试成本低。
- **场景 B（企业级跨系统协同与严肃 SDLC）**：必须选用 **Temporal**。工作流作为纯确定性代码（Deterministic Workflow），LLM 调用、Docker 命令作为无状态 Activity，支持长达数周的人工审批挂起而不占用活动资源。

---

## 3. 核心工件与黑板 Schema 规范（Typed Artifacts）

生产节点之间严禁传递自由自然语言，必须遵守强类型 Pydantic / JSON Schema 约束。

### 3.1 任务拓扑规范（`TaskDAGSpec`）

```python
from typing import List, Dict, Optional
from pydantic import BaseModel, Field

class TaskNodeSpec(BaseModel):
    task_id: str = Field(..., description="唯一任务ID，形如 task_auth_middleware")
    role: str = Field(..., description="执行角色，如 backend_dev, db_migrator")
    intent: str = Field(..., description="简明动作目标声明")
    dependencies: List[str] = Field(default_factory=list, description="前置依赖的 task_id 列表")
    input_artifacts: List[str] = Field(default_factory=list, description="消费前驱工件及版本，如 ['TaskSpec@v1', 'AuthSchema@v2']")
    declared_outputs: List[str] = Field(..., description="承诺产出的工件及版本，如 ['AuthMiddlewarePatch@v1']")
    allowed_file_patterns: List[str] = Field(..., description="受保护的文件修改范围白名单 (Glob)")
    hard_timeout_seconds: int = Field(default=300, description="单节点硬超时时间")
    token_budget: int = Field(default=50000, description="单节点最大 Token 消耗预算")
    cost_cap_usd: float = Field(default=1.0, description="单节点财务成本上限 (美元)")

class TaskDAGSpec(BaseModel):
    version: str = "2026-10-02"
    project_id: str
    nodes: Dict[str, TaskNodeSpec]
    status: str = Field(default="PENDING", enum=["PENDING", "RUNNING", "FAILED", "SUCCESS"])
    total_token_cap: int = Field(default=1000000, description="图全局累计 Token 硬上限")
    total_cost_cap_usd: float = Field(default=15.0, description="图全局累计财务硬上限 (美元)")
```

### 3.2 异常升级信封（`FailureEnvelope`）

```python
class FailureEnvelope(BaseModel):
    node_id: str
    status: str = "EXHAUSTED_L1_RETRIES"
    attempts_made: int = Field(..., le=3, description="L1 局部重试次数，最大为 3")
    last_exit_code: int
    error_category: str = Field(
        ..., 
        enum=[
            "MISSING_PREREQUISITE_DEPENDENCY",  # 缺少数据表或第三方库
            "SPEC_LOGIC_CONTRADICTION",         # 需求内部存在逻辑断裂
            "TASK_COMPLEXITY_TIMEOUT",          # 任务粒度过大无法单次完成
            "ENV_PERMISSION_DENIED"             # 外部权限阻断
        ]
    )
    failing_command: str
    stderr_tail: str
    ast_slice_context: Optional[str] = Field(None, description="裁剪后的 AST 出错切片")
    suggested_l2_action: str = Field(
        ...,
        enum=["INJECT_PRE_NODE", "SPLIT_AND_DEGRADE", "ROLLBACK_AND_AMEND", "ESCALATE_TO_HUMAN"]
    )
```

### 3.3 全局共享黑板状态（`BlackboardState`）

```python
class BlackboardState(BaseModel):
    project_spec: dict                # 根需求不可变蓝图
    task_dag: TaskDAGSpec             # 动态任务数据图
    artifacts: Dict[str, dict]        # 已归档工件: {artifact_key: json_payload}
    replanning_budget: int = 2        # L2 动态改图剩余配额 (默认 <= 2)
    execution_history: List[str]      # 不可变事件追踪日志
```

---

## 4. L2 局部子图切片替换 SOP（Sub-graph Splicing）

当 Worker 抛出 `FailureEnvelope` 升级至 L2 时，编排器按以下标准流程执行手术式改图：

```text
[Step 1: 冻结与验权]
  ├── 读取当前 BlackboardState
  ├── 严格校验 replanning_budget > 0 (否则直接触发熔断 §6)
  └── 将所有 status == "SUCCESS" 的节点锁定为只读不可变 (IsImmutable = True)

[Step 2: 匹配受限原子变异算子]
  ├── Case A (MISSING_PREREQUISITE) -> 执行 INJECT_PRE_NODE
  ├── Case B (TASK_COMPLEXITY_TIMEOUT) -> 执行 SPLIT_AND_DEGRADE
  └── Case C (SPEC_LOGIC_CONTRADICTION) -> 执行 ROLLBACK_AND_AMEND

[Step 3: 静态 DAG 合规性机检]
  ├── NetworkX 校验: nx.is_directed_acyclic_graph(dag) == True (绝不允许环)
  ├── 契约覆盖校验: 新注入节点的 declared_outputs 是否精确补齐缺失的 input_artifacts
  └── 预算递减: replanning_budget -= 1

[Step 4: 状态机写回与唤醒]
  └── 更新 State.task_dag，由 Dispatcher 重新计算拓扑入度为 0 的节点派发
```

### 4.1 三大原子改图代码模式（Python 参考实现）

```python
def apply_inject_pre_node(dag: TaskDAGSpec, envelope: FailureEnvelope, fix_node: TaskNodeSpec):
    """原子算子 1: 注入前置修复节点"""
    failed_node_id = envelope.node_id
    # 1. 注册新节点
    dag.nodes[fix_node.task_id] = fix_node
    # 2. 将原失败节点的依赖指向新节点
    dag.nodes[failed_node_id].dependencies.append(fix_node.task_id)
    # 3. 重置原节点重试状态
    dag.nodes[failed_node_id].status = "PENDING"
    return dag

def apply_split_and_degrade(dag: TaskDAGSpec, envelope: FailureEnvelope, sub_a: TaskNodeSpec, sub_b: TaskNodeSpec):
    """原子算子 2: 任务分裂与降级 (A -> B 串行切片)"""
    failed_node_id = envelope.node_id
    orig_deps = dag.nodes[failed_node_id].dependencies
    
    # 继承原始前驱
    sub_a.dependencies = orig_deps
    sub_b.dependencies = [sub_a.task_id]
    
    # 将原本依赖 failed_node 的后继节点重定向依赖 sub_b
    for nid, node in dag.nodes.items():
        if failed_node_id in node.dependencies:
            node.dependencies.remove(failed_node_id)
            node.dependencies.append(sub_b.task_id)
            
    # 移除原大任务，注入切片子任务
    del dag.nodes[failed_node_id]
    dag.nodes[sub_a.task_id] = sub_a
    dag.nodes[sub_b.task_id] = sub_b
    return dag
```

### 4.2 汇聚代码冲突解决器（Merge Conflict Resolver SOP）

当并发 Worker 在 `Aggregator` 发生代码文本冲突时，严禁让 Planner 介入，按以下 SOP 触发专职解冲突算子：

```python
def handle_fan_in_conflict(base_branch: str, patch_a_branch: str, patch_b_branch: str, worktree_dir: str):
    """汇聚合并冲突自动处置流程"""
    import subprocess
    
    # 1. 尝试机械自动合并
    res = subprocess.run(["git", "merge", patch_a_branch], cwd=worktree_dir, capture_output=True)
    res_b = subprocess.run(["git", "merge", patch_b_branch], cwd=worktree_dir, capture_output=True)
    
    if res_b.returncode == 0:
        return {"status": "SUCCESS", "merged_commit": "HEAD"}
        
    # 2. 捕获冲突文件列表
    conflict_files = subprocess.check_output(
        ["git", "diff", "--name-only", "--diff-filter=U"], cwd=worktree_dir
    ).decode().splitlines()
    
    # 3. 动态实例化局部 Resolver Worker (只喂入冲突文件与两方 TaskSpec)
    resolver_spec = TaskNodeSpec(
        task_id="resolver_merge_conflict",
        role="conflict_resolver",
        intent=f"Resolve syntax conflicts in: {conflict_files}",
        allowed_file_patterns=conflict_files,
        hard_timeout_seconds=120,
        token_budget=20000
    )
    
    # 4. 执行受限解决 (仅限 1 次尝试)；若仍冲突，硬性熔断并交还人类开发者
    return {"status": "DELEGATE_TO_RESOLVER", "spec": resolver_spec}
```

---

## 5. 异构模型治理与防御实施规范（防病态攻防）

### 5.1 防汇报冲动拦截器（Chatter Throttling Hook）

在调度器层注入中间件，拦截 Worker 的非规范输出：
```python
def output_guardrail_middleware(raw_response: str) -> dict:
    """强制阻断自然语言闲聊，仅放行结构化工件或工具调用"""
    try:
        parsed = json.loads(raw_response)
        if "artifact_key" in parsed or "tool_call" in parsed:
            return parsed
    except Exception:
        pass
    
    # 拦截并静默处理汇报闲聊，返回警告并迫使模型聚焦工具
    return {
        "action": "SYSTEM_WARNING",
        "message": "Protocol Violation: Conversational chatter is strictly prohibited. Output must be valid JSON Artifact."
    }
```

### 5.2 物理只读测试与影子门禁（Anti-False-Done）

1. **测试目录物理挂载为 Read-Only**：
   在启动 Worker 容器或分配沙箱时，使用操作系统权限锁死测试集：
   ```bash
   # Docker 启动参数示例：测试用例只读挂载
   docker run --rm -v $(pwd)/tests:/workspace/tests:ro -v $(pwd)/src:/workspace/src:rw worker-image
   ```
2. **影子验证门禁（Shadow Acceptance Gate）**：
   Worker 汇报测试全绿后，系统在独立的无大模型环境（Clean Runner）中拉取干净代码镜像，执行完整的独立测试套件。若退出码非 0，判定该 Worker 存在欺诈，立即撤销其提交并抛出安全告警。

### 5.3 AST 差异文件范围锁（Anti-Scope-Creep）

在 Git Worktree 的 `pre-commit` 钩子中强制核对变更文件白名单：
```bash
#!/bin/bash
# 检查本次提交的文件是否超出 TaskSpec 声明的 allowed_file_patterns
CHANGED_FILES=$(git diff --cached --name-only)
for FILE in $CHANGED_FILES; do
    if ! [[ "$FILE" =~ ^(src/modules/auth/.*|tests/modules/auth/.*)$ ]]; then
        echo "SECURITY VIOLATION: Unauthorized edit outside task boundary: $FILE"
        exit 1
    fi
done
```

### 5.4 节点级最小特权原则（Node RBAC & Action Boundary Matrix）

为了杜绝跨角色越权污染，不同节点角色在图运行中必须被严格限制在最小动作边界内：

| 节点角色 (Role) | 典型推荐模型 | 黑板读写权限 (Blackboard RBAC) | 沙箱文件写入权限 (File System) | 外部网络与命令权限 (Exec & Net) |
|---|---|---|---|---|
| **Planner (主控架构)** | 顶尖推理模型 (Opus 5.5 / Sol / o3) | **读**：全量黑板<br>**写**：仅限 `task_dag` 字典 | **禁止** 任何文件写入 | **禁止** 执行任何代码命令 |
| **Worker (专职代码)** | 高代码吞吐模型 (Sonnet 5 / DeepSeek V3) | **读**：仅限前驱 `input_artifacts`<br>**写**：仅限 `declared_outputs` | **允许**：仅限声明的白名单文件 | **允许**：执行局部沙箱内单测（测试目录只读） |
| **Reviewer / Gate** | 100% 确定性无模型程序 / 规则引擎 | **读**：待审 Patch 与工件<br>**写**：仅限测试报告与通过/拒绝状态 | **只读**：代码库全量只读挂载 | **允许**：干净容器内执行回归与 Lint |
| **Conflict Resolver** | 专注于微调解决的代码模型 | **读**：冲突 diff 与双边 Spec<br>**写**：仅限冲突解决后 Commit 引用 | **允许**：仅限标记冲突的 Unmerged 文件 | **允许**：执行 `git add` 与冲突单测 |

---

## 6. 工业落地演进梯子（P0 → P3）

团队必须按以下梯子逐步递进，切忌直接在生产盲目上最高级动态重规划：

```text
[P3: 工业级分布式持久化与动态子图切片]
  - Temporal 驱动、持久化黑板、L2 动态切片、生产多仓库并发
  ▲
[P2: 固定元图 + 局部 L1/L2 异常自愈]
  - LangGraph 驱动、Worker 内 3 次重试、Failure Envelope 向上汇报
  ▲
[P1: 固定元图 + 静态 Task DAG 数据派发]
  - 静态编译元图、任务数据一次性生成、无动态重排、Worktree 并发
  ▲
[P0: 纯串行确定性流水线 (Baseline)]
  - 单 Agent 串行执行、静态测试门禁、人工逐步 Review
```

- **P0 阶段**：验证单步骤的 Prompt 与 Harness 是否健壮，跑通线性流水线；
- **P1 阶段**：引入任务 DAG 数据化与并发扇出，消除人工单步介入；
- **P2 阶段**：接入两层自愈协议与受限原子改图，实现无人值守长程运行；
- **P3 阶段**：企业级部署，接入分布式持久化工作流引擎（Temporal），抗击基础设施故障。

---

## 7. 反过度工程清算（7 种典型反模式警告）

| 反模式 | 愚蠢的做法 | 正确的做法 |
|---|---|---|
| **1. 伪 Multi-Agent 聊天** | 实例化 5 个不同角色的 Agent 在群里开会 | 废除群聊；改为基于文件的单向工件流水线 |
| **2. 运行时现场编译新图** | 让模型现场写 Python 代码 `builder.add_node` | 静态编译固定元图，模型只动态输出任务 JSON 数据 |
| **3. 全量 DAG 重写** | Worker 报错后让 Planner 重新生成整个工程的 DAG | 绝对冻结已完成节点，实施局部子图切片替换（Sub-graph Splicing） |
| **4. 无上限的动态改图** | 允许编排模型无限次改图尝试修复 | 设定重规划硬上限（Max Replanning ≤ 2），超时坚决熔断 |
| **5. 内存瞬态状态机** | 把工作流状态保存在全局字典，无落盘支持 | 接入带持久化的 Checkpointer（Postgres/SQLite）或 Temporal |
| **6. 信任模型的自我验收** | 让同一个编写代码的 Agent 来判断“是否完成” | 验收与干活完全物理分离，使用原生测试命令判定 |
| **7. 共享同一脏文件目录** | 多个并发 Worker 直接在同一个项目根目录修改文件 | 必须为并发 Worker 分配独立的 `git worktree` 或沙箱容器 |
