# 02 · DeepSeek Harness (`dsh`)：Cordis 插件底座与显式 Task DAG 调度深度解密

> **摘要**：系统解剖 DeepSeek 官方开源的 Agent 运行底座 **DeepSeek Harness (`dsh`)**。深度解密其基于 **Cordis** 微内核的“一切皆插件”时空组合性架构、`dsh-agent-teams` 插件构建的显式 Task DAG 依赖建模与 Kahn 拓扑就绪调度引擎、基于 Append-only 事件溯源（Event-Sourcing）的会话日志与精准局部回退机制，以及 Web 端动态 DAG 实时可视化看板与 KV Cache 前缀共享优化实战。

---

## 1. 核心设计哲学：“Agent = Model + Harness”

在 DeepSeek 的工程体系中，大模型被明确定义为“无状态的概率推理引擎（算子）”，而真正的系统确定性必须由 **Harness（基座底盘）** 承担：

```
┌──────────────────────────────────────────────────────────────────┐
│                   DeepSeek Harness (dsh 运行时宿主)               │
│                                                                  │
│  [Cordis 微内核服务总线 (Service Bus & Context Injection)]        │
│                                                                  │
│  ┌───────────────────┬───────────────────┬────────────────────┐  │
│  │ Model Adapter 插件 │ Tool Registry 插件│ Sandbox (沙箱) 插件 │  │
│  │ (DeepSeek V3/R1 /  │ (Bash / Git / AST │ (Local / Docker /  │  │
│  │  第三方异构模型)  │  Linter / Search) │  E2B / BoxLite)    │  │
│  └───────────────────┴───────────────────┴────────────────────┘  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │         dsh-agent-teams 插件 (显式 Task DAG 调度引擎)      │  │
│  │  - Captain 动态拓扑规划器                                   │  │
│  │  - Kahn 入度就绪队列 (In-Degree = 0 Queue)                  │  │
│  │  - Reviewer 工件验收门禁                                    │  │
│  └────────────────────────────────────────────────────────────┘  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │       Session Event-Sourcing 日志系统 (Append-Only)        │  │
│  │  - 纯事件溯源 / 状态机快照 / 精准拓扑回退 (Rollback)         │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                │ WebSocket / Server-Sent Events  │
│                                ▼                                 │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │   npx @deepseek-ai/dsh web 交互式动态 DAG 监控与调试看板   │  │
│  │   - 实时拓扑染色 / KV Cache 命中监控 / 节点级手动干预      │  │
│  └────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 2. Cordis 插件架构与事件驱动机制

`dsh` 基于 **Cordis** 框架构建，其核心抽象是：**系统内部无固定死板的主循环，一切能力皆为监听总线事件的服务插件**。

### 2.1 核心插件注册与生命周期（TypeScript）
```typescript
import { Context, Service } from 'cordis';

// dsh 核心上下文扩展
export interface DshContext extends Context {
  scheduler: TaskSchedulerService;
  sandbox: SandboxService;
  eventLog: EventSourceLogService;
}

// dsh-agent-teams 插件核心结构
export class AgentTeamsPlugin extends Service {
  constructor(ctx: DshContext) {
    super(ctx, 'agentTeams', true);

    // 监听任务就绪事件，触发沙箱 Worker 派发
    ctx.on('task/ready', async (task) => {
      ctx.logger.info(`[Scheduler] 任务就绪: ${task.id}，准备派发 Worker`);
      await this.dispatchWorker(task);
    });

    // 监听 Worker 完成事件，触发验收门禁与拓扑入度更新
    ctx.on('worker/finished', async ({ taskId, artifacts, output }) => {
      const isAccepted = await this.runReviewerGate(taskId, artifacts);
      if (isAccepted) {
        ctx.emit('task/success', { taskId, artifacts });
        this.updateDownstreamInDegrees(taskId); // 下游任务入度减 1
      } else {
        ctx.emit('task/failed', { taskId, error: '验收未通过' });
      }
    });
  }
}
```

---

## 3. 动态工作流核心：`dsh-agent-teams` 显式 Task DAG

与 DeerFlow 扁平的 `todos` 和纯文本 Prompt 隐式规划不同，`dsh` 强制将动态工作流建模为**显式的有向无环图数据结构（Task DAG Data Structure）**。

### 3.1 任务节点完整生命周期状态机
每个子任务拥有严格受控的 7 状态转移矩阵：

```
                ┌────────────────────────┐
                │        PENDING         │ (等待前驱依赖完成)
                └───────────┬────────────┘
                            │ 入度 In-Degree 归零
                            ▼
                ┌────────────────────────┐
                │         READY          │ (进入可执行就绪池)
                └───────────┬────────────┘
                            │ 调度器分配沙箱与 Token 租约
                            ▼
                ┌────────────────────────┐
                │        RUNNING         │ (Worker 独立沙箱执行)
                └───────────┬────────────┘
                            │ 执行完毕生成工件
                            ▼
                ┌────────────────────────┐
                │       REVIEWING        │ (Reviewer 门禁校验)
                └───────┬────────┬───────┘
          Pass 验收通过 │        │ Fail 验收不通过
                        ▼        ▼
       ┌──────────────────┐    ┌──────────────────┐
       │     SUCCESS      │    │      FAILED      │
       └──────────────────┘    └────────┬─────────┘
                                        │ 触发 L2 拓扑重排
                                        ▼
                               ┌──────────────────┐
                               │    REPLANNING    │ (Captain 动态手术改图)
                               └──────────────────┘
```

### 3.2 动态 DAG 拓扑定义 Schema（JSON/YAML）
```yaml
# Captain 规划模型生成的动态 DAG 规范
dag_id: "dag_refactor_order_service_20261001"
objective: "重构订单支付超时流水线，增加分布式幂等校验"
nodes:
  - id: step_1_schema
    title: "设计幂等表与 Redis Key 规范"
    role: "Architect"
    dependencies: []
    inputs: ["docs/payment_flow.md"]
    expected_artifacts: ["schemas/idempotent.sql", "specs/redis_keys.json"]
    timeout_sec: 120

  - id: step_2_repo_impl
    title: "编写 Go 数据访问层 (DAO) 及单元测试"
    role: "Coder"
    dependencies: ["step_1_schema"] # 显式前置依赖
    inputs: ["schemas/idempotent.sql"]
    expected_artifacts: ["internal/repo/idempotent.go", "internal/repo/idempotent_test.go"]
    timeout_sec: 300

  - id: step_3_handler_impl
    title: "修改业务 Controller 注入幂等检查中间件"
    role: "Coder"
    dependencies: ["step_1_schema"] # 与 step_2 并行！
    inputs: ["specs/redis_keys.json"]
    expected_artifacts: ["internal/handler/order.go"]
    timeout_sec: 300

  - id: step_4_integration_test
    title: "启动 Docker Compose 运行全链路并发防重测试"
    role: "QA"
    dependencies: ["step_2_repo_impl", "step_3_handler_impl"] # 汇聚等待
    inputs: ["internal/repo/idempotent.go", "internal/handler/order.go"]
    expected_artifacts: ["test_results/concurrency_report.json"]
    timeout_sec: 600
```

### 3.3 调度器内核：Kahn 算法与就绪队列驱动
调度器引擎在收到 DAG 定义后，执行如下确定性调度逻辑：
1. **拓扑死环检查**：使用 Kahn 算法计算全局拓扑排序，若存在环路（Cycle），直接判定 DAG 语法非法，要求 Captain 重新规划；
2. **就绪入队**：初始入度为 0 的节点进入 `ready_queue`；
3. **并发派发**：调度器从 `ready_queue` 出队任务，挂载独立沙箱，实例化 Worker 并发执行；
4. **汇聚解冻**：当一个 Worker 成功通过 Reviewer 验收后，遍历其所有后继节点（Successors），后继节点的入度计数值减 1。一旦入度降为 0，该后继节点立刻从未激活态被“解冻”并推入就绪队列。

---

## 4. 事件溯源（Event-Sourcing）与精准拓扑回滚

DeepSeek Harness 最具工程韧性的设计在于其**纯事件溯源的持久化体系**：

- **Append-only 会话事件流**：系统的状态不在内存中做破坏性覆盖，所有流转均落地为结构化事件：
  ```json
  {"type": "TASK_CREATED", "taskId": "step_1_schema", "timestamp": 1790870001}
  {"type": "TASK_READY", "taskId": "step_1_schema", "timestamp": 1790870002}
  {"type": "TASK_DISPATCHED", "taskId": "step_1_schema", "workerId": "worker-42"}
  {"type": "ARTIFACT_COMMITTED", "taskId": "step_1_schema", "path": "schemas/idempotent.sql"}
  {"type": "TASK_SUCCESS", "taskId": "step_1_schema", "timestamp": 1790870045}
  ```
- **局部外科手术式回退（Surgical Rollback）**：
  如果 `step_4_integration_test` 暴露出数据访问层有逻辑 Bug，系统**不需要重跑整个任务**，也不需要将所有文件回滚；
  操作员或 Captain 发出回退指令：`dsh rollback --task step_2_repo_impl`：
  - 调度器**保留** `step_1_schema` 的全部成果与上下文；
  - 调度器**保留**与它并行的 `step_3_handler_impl` 的成果；
  - 仅将 `step_2_repo_impl` 与依赖它的下游 `step_4_integration_test` 状态重置为 `PENDING`，清除其生成的局部工作区，重新派发修补。

---

## 5. Web 端动态 DAG 看板与 KV Cache 优化

通过命令 `npx @deepseek-ai/dsh web` 启动的控制台，是业界首个将**模型推理指标与图工程拓扑合二为一**的可观测性平台：

```
┌────────────────────────────────────────────────────────────────────────┐
│  dsh Web Studio - DAG 实时拓扑看板                                     │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   [step_1_schema] (✅ 43s)                                             │
│          │                                                             │
│          ├───────────────────────────────┐                             │
│          ▼                               ▼                             │
│   [step_2_repo_impl] (🟡 RUNNING 65%)   [step_3_handler] (✅ 110s)    │
│          │                               │                             │
│          └───────────────┬───────────────┘                             │
│                          ▼                                             │
│                [step_4_integration] (⏳ WAITING)                       │
│                                                                        │
├────────────────────────────────────────────────────────────────────────┤
│ 节点 Telemetry 详情: [step_2_repo_impl]                                 │
│ - 模型: DeepSeek-Coder-V3 (fp8)                                        │
│ - 生成速率: 82 tokens/sec | 首字延迟 (TTFT): 380ms                     │
│ - KV Cache 命中率 (Prefix Cache Hit): 92.4% (节省 ~18,000 prompt tokens)│
│ - 活跃沙箱: Docker Container (ID: c89f1a2, Memory: 210MB)              │
│ - 租约状态: Active (剩余 185s) | 重试配额: 1/2                          │
└────────────────────────────────────────────────────────────────────────┘
```

### 关键优化：跨节点的 KV Cache 前缀对齐（Prefix Cache Optimization）
DeepSeek 模型原生具备强大的多轮 KV Cache 缓存机制。在 `dsh` 中，调度器做了针对性的 Prompt 布局治理：
- 所有同属一个 DAG 的任务节点，其 System Prompt、仓库整体结构描述（Repo Skeleton）、全局契约规范被固定排列在 Prompt 最前端；
- 使得并行拉起的多个 Worker 在请求 API 时，**命中高达 85%~95% 的前缀缓存**，大幅削减了调度延迟与整体 Token 费用。
