---
type: evidence_archive
collected_by: 委派回源子代理（P0 · 跨 feature 在途可见性）
collected_at: 2026-09-27
serves: research-plan.md P0「跨 feature 在途可见性」；补充 digested/03 的外层调度判读
status: 两个独立产品/机构的一手实现：Anthropic Managed Agents（单 session 长跑）＋ OpenClaw Background Tasks/Task Flow（跨 detached work 的任务账本与 flow）；另以 Anthropic feature_list 作为单项目长跑对照
quality_bar: URL、发布日期/版本锚点、观测日期、逐字摘录、P-existence/P-mechanism/P-outcome、来源独立性、负结论与偏差均分开记录；不把产品文档或源码设计当采用率/效果证据
---

# P0 回源：跨 feature 在途可见性

## 0. 问题边界与判读口径

本档案问的不是“一个 feature 是否能在多轮里继续”，而是：当系统同时面对多个 feature / detached work 时，外部操作者能否看到每项工作的候选、授权、在途、阻塞、验收、完成、取消、恢复、优先级变化。必须区分三种尺度：

1. **单 feature 长跑**：一个 session 自己反复迭代，能看到该 session 的状态或 outcome。
2. **项目内多 feature 规格**：一个持久化 feature list 记录多个 feature，下一轮从中选一项；这不等于多个 feature 的运行实例队列。
3. **跨 feature 队列/任务账本**：多个 detached task / flow 作为可独立列出、筛选、检查、取消、恢复的对象；这是本 P0 的强证据。

证据等级沿研究计划：

- **P-existence**：一手实现/设计确实存在该状态或对象。
- **P-mechanism**：一手接口、命令、事件或持久化字段使外部可观察/可操作。
- **P-outcome**：一手材料给出实际运行结果、完成/失败转移或运营结果。产品文档里的“支持”只算设计 outcome，不算真实采用率或效果。

观测日期统一为 **2026-09-27**（页面与官方仓库在该日取得）。

---

## 1. 一手来源 A：Anthropic Managed Agents（session/outcome API）

### 来源元数据

- **机构/来源**：Anthropic，Claude Platform 官方 Managed Agents 文档；配套官方工程文《Scaling Managed Agents: Decoupling the brain from the hands》。
- **URL**：
  - https://platform.claude.com/docs/en/managed-agents/overview.md
  - https://platform.claude.com/docs/en/managed-agents/session-operations.md
  - https://platform.claude.com/docs/en/managed-agents/events-and-streaming.md
  - https://platform.claude.com/docs/en/managed-agents/define-outcomes.md
  - https://platform.claude.com/docs/en/managed-agents/permission-policies.md
  - https://www.anthropic.com/engineering/managed-agents
- **发布日期**：工程博客 **2026-04-08**（页面明确标注 Published Apr 08, 2026）；Managed Agents 文档单页未标注发布日期，页面 beta header 为 `managed-agents-2026-04-01`，只作为 API 版本/时间锚，不冒充文章发布日期。
- **观测日期**：2026-09-27。
- **来源类型**：官方产品 API 文档＋官方工程设计文；一手设计/接口证据。
- **范围判定**：这是**单 session 长跑的强证据**，不是跨 feature 队列的强证据。一个 session 可有一个当前 outcome；文档明确“Only one outcome is supported at a time, but you may chain outcomes in sequence”。

### 逐字摘录与证据判定

1. **session 的外部化与恢复（P-existence/P-mechanism）**

> “Session | A running agent instance within an environment, performing a specific task and generating outputs”
>
> “Events | Messages exchanged between your application and the agent (user turns, tool results, status updates)”

来源：https://platform.claude.com/docs/en/managed-agents/overview.md

> “Sessions progress through these statuses.”
>
> “`idle` | Agent is waiting for input, including user messages or tool confirmations.”
>
> “`running` | Agent is actively executing.”
>
> “`rescheduling` | Transient error occurred, retrying automatically.”
>
> “`terminated` | Session has ended, either because of an unrecoverable error or because it was archived. A session that finishes its work goes `idle`, not `terminated`.”

来源：https://platform.claude.com/docs/en/managed-agents/session-operations.md

> “When one fails, a new one can be rebooted with `wake(sessionId)`, use `getSession(id)` to get back the event log, and resume from the last event.”
>
> “During the agent loop, the harness writes to the session with `emitEvent(id, event)` in order to keep a durable record of events.”

来源：https://www.anthropic.com/engineering/managed-agents

判定：session status、事件日志、恢复接口均是外部可见机制。`idle` 同时覆盖“等待输入/工具确认”和“完成后空闲”，因此仅看 session status 不能把阻塞、完成、等待新工作三者完全区分；必须结合事件/stop reason/outcome。

2. **授权与阻塞（P-existence/P-mechanism）**

> “`always_ask` | The session pauses and waits for your approval before executing.”
>
> “`auto` | The server evaluates each call and runs it, denies it, or pauses for your approval.”

来源：https://platform.claude.com/docs/en/managed-agents/permission-policies.md

> “A `user.interrupt` event pauses work on the current outcome and marks the `span.outcome_evaluation_end.result` as `interrupted`, allowing you to kick off a new outcome.”

来源：https://platform.claude.com/docs/en/managed-agents/define-outcomes.md

判定：授权/阻塞可见到 session 级别，且可通过事件恢复或启动新 outcome。文档没有提供跨 session 的“待授权 feature 总表”。

3. **验收、完成、失败、恢复（P-existence/P-mechanism/P-outcome〔设计 outcome〕）**

> “When you define an outcome, the harness automatically provisions a *grader* to evaluate the artifact against a rubric.”
>
> “The grader returns an explanation summarizing which criteria passed or failed, or confirming that the artifact satisfies the rubric.”

来源：https://platform.claude.com/docs/en/managed-agents/define-outcomes.md

> “Only one outcome is supported at a time, but you may chain outcomes in sequence.”

来源：https://platform.claude.com/docs/en/managed-agents/define-outcomes.md

> “`satisfied` | Session transitions to `idle`.”
>
> “`needs_revision` | Agent starts a new iteration cycle.”
>
> “`max_iterations_reached` | One final acknowledgment turn follows before the session transitions to `idle`. No further evaluation runs.”
>
> “`failed` | Session transitions to `idle`.”
>
> “`interrupted` | Emitted when the session is interrupted while an outcome is active.”

来源：https://platform.claude.com/docs/en/managed-agents/define-outcomes.md

> “Until an evaluation completes, `result` reports `pending`, `running`, or `evaluating`”

来源：https://platform.claude.com/docs/en/managed-agents/define-outcomes.md

判定：验收状态和独立 grader 的机制明确；完成可通过 `satisfied` 看到，但 session 本身随后回到 `idle`。这解决单 feature 的验收可见性，不解决跨 feature 的总体完成率。

4. **事件排队的有限可见性（P-existence/P-mechanism）**

> “On events you send, `processed_at` is null while the event is still queued behind earlier events.”

来源：https://platform.claude.com/docs/en/managed-agents/events-and-streaming.md

判定：单 session 内事件在途/排队可由 `processed_at` 间接观察；文档未给出跨 session 的排队顺序、优先级、资源分配或 feature-level queue view。

### A 的状态覆盖矩阵

| 目标状态 | Anthropic Managed Agents 可被外部看见？ | 机制/限制 |
|---|---|---|
| 候选 | **部分** | 可创建 session、给 `title`、发送 `user.define_outcome`；但没有公开的跨 session 候选池/待排队 feature 列表。 |
| 授权 | **是，session/工具级** | `always_allow` / `always_ask` / `auto`；工具确认事件会使 session `idle` 等待。不是跨 feature 授权台账。 |
| 在途 | **是，单 session** | `running`、事件流、agent/span events。 |
| 阻塞 | **部分到是** | 工具确认等待、`user.interrupt`、`pending/running/evaluating` 可见；`idle` 把多种原因合并，需读事件。 |
| 验收 | **是** | rubric + 独立 grader；`outcome_evaluation_*` 事件、`pending/running/evaluating`。 |
| 完成 | **是，outcome 级** | `satisfied`，随后 session `idle`；没有统一的跨 feature 完成总览。 |
| 取消 | **部分** | `interrupted` 明确；session 可 archive/delete/terminate，但不等价于 feature queue 的 cancel reason/历史。 |
| 恢复 | **是，单 session** | `wake(sessionId)`、从最后事件恢复；Outcome 可在中断后启动新 outcome。 |
| 优先级变化 | **否/未发现** | 文档未公开 feature/session priority、重排、抢占或 priority-change event。 |

### A 的 P 结论

- **P-existence：强（单 session）**。session、状态、事件、outcome、grader 都是公开 API 设计。
- **P-mechanism：强（单 session）**。状态查询、SSE/webhook 事件、`processed_at`、interrupt、wake、outcome result 均可回读。
- **P-outcome：中（设计/接口 outcome，不是采用率）**。文档定义了满意/需修订/失败/中断后的转移和恢复，但没有公开真实运行样本、跨项目吞吐、阻塞率或采用率。
- **对 P0 的边界**：不能把 Managed Agents 的多个 session 误称为跨 feature 队列；官方材料只证明每个 session 的独立可见性。跨 feature 总览、优先级重排、候选到授权的队列历史仍缺。

---

## 2. 一手来源 B：OpenClaw Background Tasks + Task Flow + Standing Orders

### 来源元数据

- **机构/来源**：OpenClaw 官方文档与官方 GitHub 源码仓库 `openclaw/openclaw`。
- **URL**：
  - https://raw.githubusercontent.com/openclaw/openclaw/main/docs/automation/tasks.md
  - https://raw.githubusercontent.com/openclaw/openclaw/main/docs/cli/tasks.md
  - https://raw.githubusercontent.com/openclaw/openclaw/main/docs/automation/taskflow.md
  - https://raw.githubusercontent.com/openclaw/openclaw/main/docs/automation/standing-orders.md
  - https://raw.githubusercontent.com/openclaw/openclaw/main/docs/automation/index.md
  - https://docs.openclaw.ai/cli/cron
- **发布日期/版本锚点**：文档页没有发布日期；按官方 GitHub API 的该路径最近提交记录作“最近更新”锚点（不是原始发布日期）：`tasks.md` 2026-09-26（commit `047c88d`）；`taskflow.md` 2026-09-23（`3e4ab6b`）；`standing-orders.md` 2026-09-09（`2393e17`）；`cli/tasks.md` 2026-09-10（`0cb59d8`）。
- **观测日期**：2026-09-27。
- **来源类型**：官方产品设计文档＋可公开访问的官方仓库文档/提交；一手机制证据。文档与同一仓库提交不能算彼此独立来源。
- **范围判定**：这是本轮最接近**跨 feature / 跨 detached work 可见性**的公开实现：background task ledger 可收纳 ACP、subagent、automation、CLI 多种运行；Task Flow 可在一个 flow 生命周期内协调多个 child tasks，并持久化到 Gateway 重启后。它仍不是一个“feature product backlog”：feature 语义、依赖图、优先级排序不由该接口统一定义。

### 逐字摘录与证据判定

1. **跨运行任务账本与生命周期（P-existence/P-mechanism）**

> “Background tasks track work that runs **outside your main conversation session**: ACP runs, subagent spawns, automation job runs, and CLI-initiated operations.”
>
> “Each task moves through `queued → running → terminal` (succeeded, failed, timed_out, cancelled, or lost).”
>
> “`openclaw tasks list` shows all tasks”

来源：https://raw.githubusercontent.com/openclaw/openclaw/main/docs/automation/tasks.md

> “`openclaw tasks list --status blocked`”
>
> “`openclaw tasks show <lookup>`”
>
> “`openclaw tasks cancel <lookup>`”
>
> “`openclaw tasks retry <lookup> [lookup...]`”
>
> “`openclaw tasks dismiss <lookup> [lookup...]`”

来源：https://raw.githubusercontent.com/openclaw/openclaw/main/docs/automation/tasks.md

> “Use `--status blocked` to find completed tasks whose result delivery is blocked. These tasks retain their stored `succeeded` status and also remain included in `--status succeeded` results; JSON task records keep the same stored status and `terminalOutcome` fields.”

来源：https://raw.githubusercontent.com/openclaw/openclaw/main/docs/cli/tasks.md

判定：这是明确的跨 detached work 外部列表、过滤、详情、取消、结果投递阻塞和重试机制。`blocked` 不是执行本体阻塞，而是已完成结果的 delivery blocked，必须在读档时保持语义区分。

2. **跨多步工作持久化与恢复/取消（P-existence/P-mechanism）**

> “Task Flow is the orchestration layer above [background tasks]. A flow is a durable record of multi-step work with its own status, JSON state, revision counter, and linked task records.”
>
> “Flows survive gateway restarts; individual tasks remain the unit of detached work.”

来源：https://raw.githubusercontent.com/openclaw/openclaw/main/docs/automation/taskflow.md

> “The controller advances between running, waiting and terminal states”
>
> “State transitions (`setWaiting`, `resume`, `finish`, `fail`, `requestCancel`) require the latest expected revision.”
>
> “Cancellation intent refuses new child links. The flow finalizes as cancelled once its active children have settled.”

来源：https://raw.githubusercontent.com/openclaw/openclaw/main/docs/automation/taskflow.md

> “`openclaw tasks flow list`”
>
> “`openclaw tasks flow show <lookup>`”
>
> “`openclaw tasks flow cancel <lookup>`”

来源：https://raw.githubusercontent.com/openclaw/openclaw/main/docs/cli/tasks.md

判定：flow 级别提供 waiting/resume/cancel、revision、child task 链接和 Gateway 重启后的持久性，外部可以查看一个多 feature-like 多步骤流程的在途状态。但文档没有说 flow 本身是产品 feature 队列，也没有要求所有 feature 都挂在 flow 下。

3. **授权候选与升级边界（P-existence/P-mechanism）**

> “Standing orders grant your agent **permanent operating authority** for defined programs.”
>
> “Each program specifies: 1. **Scope** - what the agent is authorized to do 2. **Triggers** - when to execute (schedule, event, or condition) 3. **Approval gates** - what requires human sign-off before acting 4. **Escalation rules** - when to stop and ask for help”

来源：https://raw.githubusercontent.com/openclaw/openclaw/main/docs/automation/standing-orders.md

> “Standing orders are defined in your agent workspace files.”
>
> “Standing orders define **what** the agent is authorized to do. Automations define **when** it happens.”

来源：https://raw.githubusercontent.com/openclaw/openclaw/main/docs/automation/standing-orders.md

判定：OpenClaw 把候选程序、授权边界、触发器和人工升级写入 workspace 文件，并由 automations 触发；这是**授权设计可见**，但不是一个单独的 feature approval queue。候选的外部可见性依赖用户能读 workspace/automation 定义，任务进入 ledger 后才有统一状态。

4. **调度与独立任务集合的明确分层（P-existence/P-mechanism）**

> “Tasks are **records**, not schedulers - automations and heartbeat decide _when_ work runs, tasks track _what happened_.”
>
> “Multi-step research then summarize | Task Flow | Durable orchestration with revision tracking”

来源：https://raw.githubusercontent.com/openclaw/openclaw/main/docs/automation/tasks.md

> “OpenClaw runs work in the background through tasks, scheduled jobs, event hooks, and standing instructions.”

来源：https://raw.githubusercontent.com/openclaw/openclaw/main/docs/automation/index.md

判定：任务账本和 scheduler 分开，避免把“可列出的任务”误写成“队列调度器”。这也是 P0 的重要负结论：可见不等于可排序或会自动决定下一项 feature。

### B 的状态覆盖矩阵

| 目标状态 | OpenClaw 可被外部看见？ | 机制/限制 |
|---|---|---|
| 候选 | **部分** | standing order program + automation definition 可见；background task 在进入运行账本后可见；没有统一的 feature backlog/candidate entity。 |
| 授权 | **是，程序/审批级** | scope、approval gates、escalation rules；但授权定义在 workspace 文件，不是 task ledger 的独立状态字段。 |
| 在途 | **是，强** | `tasks list`、`queued`、`running`、`show`；Task Flow 有 linked task records。 |
| 阻塞 | **是，但有两种语义** | flow `waiting` / `blocked`；task `blocked` 特指成功结果的 delivery blocked，原始 task 仍 `succeeded`。可用 audit/show 分辨。 |
| 验收 | **部分** | terminal outcome、succeeded/failed、flow finish/fail；没有通用 feature rubric。具体 workflow/plugin 可自行定义。 |
| 完成 | **是，任务/flow 级** | task `succeeded` 或其他 terminal；flow `finish`，列表/详情可读。 |
| 取消 | **是，强** | `tasks cancel`、`flow cancel`；flow cancellation intent 阻止新 child links，待 active children settle 后 finalizes cancelled。 |
| 恢复 | **是，强** | Task Flow `resume`；blocked delivery 用 `retry` 或 `dismiss`；flow durable across Gateway restart。注意 retry 是投递恢复，不是重跑原执行。 |
| 优先级变化 | **否/未发现** | cited task/flow/automation docs 没有 feature priority 字段、排序变更事件、抢占或依赖优先级；`tasks list` 的 newest-first 是查看排序，不是工作优先级。 |

### B 的 P 结论

- **P-existence：强（跨 detached work/task ledger）**。至少 ACP、subagent、automation、CLI 四类后台工作进入统一 task 记录；flow 进一步连接多个 child task。
- **P-mechanism：强**。列表、状态过滤、详情、取消、flow show/cancel、waiting/resume、revision 和 delivery retry/dismiss 都是公开接口；状态持久化跨 Gateway restart。
- **P-outcome：中到强（机制 outcome，不是业务效果）**。文档明确 queued/running/terminal、succeeded/failed/timed_out/cancelled/lost、waiting/blocked 的转移和维护；没有独立运行数据来证明真实用户采用率、吞吐或减少催问。
- **对 P0 的边界**：它回答“多个后台运行实例当前去哪了”，但没有回答“产品 feature backlog 中谁应该先做、谁已被授权、优先级为何变化、跨 feature 验收是否满足”。需要把 task ledger 与 feature-level work source 另行建模。

---

## 3. 对照来源 C：Anthropic long-running agents 的 feature_list/progress（单项目多 feature，不算跨 feature 队列）

该来源已在本主题既有 [`evidence-2026-09-26-b-stop-and-scheduling.md`](evidence-2026-09-26-b-stop-and-scheduling.md) §3 与 §问题 2.1 建档；本档案只作 P0 的尺度对照，不复制完整回源材料。

- **URL**：https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **发布日期**：2025-11-26（页面标注）；**观测日期**：既有档案 2026-09-26。
- **既有逐字证据指针**：evidence-b §102–127（`feature_list.json`、初始 `passes: false`、端到端验收）与 §241–258（每轮读取 progress/git、选择最高优先级未完成 feature）。
- **关键机制（沿用既有证据，不升级强度）**：`feature_list.json` 是一个项目内多 feature 的持久化进度规格；coding agent 每轮从未完成项中选择最高优先级 feature，并通过 progress log/git 跨 session 记忆。
- **尺度判定**：这是“**单项目长跑 + 多 feature 规格**”，不是多个 feature 同时在途的队列/任务账本。它能回答：候选/未完成项、优先级选择、逐 feature 验收（`passes`）和项目级“尚未全完成”；不能回答：每个 feature 是否已授权、是否正在被哪个并发 session 执行、阻塞原因、取消/恢复历史、优先级变化审计。
- **来源独立性**：与 Anthropic Managed Agents 同一机构，只计 **Anthropic 一票**；两者不是独立组织的交叉验证。Anthropic feature_list 的实际采用/效果也未在公开材料中以统计数据证明。

---

## 4. 跨来源状态覆盖总表

| 状态 | Anthropic feature_list（单项目多 feature） | Managed Agents（单 session） | OpenClaw tasks/flow（跨 detached work） | P0 当前判定 |
|---|---|---|---|---|
| 候选 | 未完成 feature 可见 | 可创建 session/outcome，但无候选池 | standing order/automation 可见，task 入账后统一可见 | **部分回答**；统一候选实体仍缺 |
| 授权 | 未见独立授权状态 | 工具 permission policy、确认等待 | scope/approval gate/escalation | **回答机制，未回答 feature 级授权历史** |
| 在途 | 下一轮选中的 feature 可推断，非运行实例列表 | `running`、事件流 | `queued`/`running`、list/show | **OpenClaw 最强** |
| 阻塞 | 未见标准阻塞字段 | idle/confirmation/interrupt，需结合事件 | flow waiting/blocked；task blocked=delivery blocked | **回答，但需区分阻塞语义** |
| 验收 | `passes` + E2E 测试 | rubric + 独立 grader + outcome result | terminal outcome/自定义 workflow，缺通用 rubric | **回答机制；跨 feature 验收总览缺** |
| 完成 | 所有 feature passes 可推断项目完成 | `satisfied`，session 回 idle | `succeeded` / flow finish | **回答** |
| 取消 | 未见 feature cancel 历史 | interrupted/archive/delete，语义不完全同一 | task/flow cancel 明确 | **OpenClaw 最完整** |
| 恢复 | progress/git 可冷启动恢复，但无 resume 状态 | wake、事件日志、续 outcome | flow resume、delivery retry/dismiss、重启后持久 | **回答** |
| 优先级变化 | “选最高优先级未完成”但无变更审计 | 未见 priority | 未见 priority 字段/变更事件 | **核心缺口仍在** |

---

## 5. 来源独立性、去重与偏差

### 来源独立性

- **独立计数 1：Anthropic**。feature_list/progress、Managed Agents engineering blog、Managed Agents API docs、Claude Code docs 都属于 Anthropic 生态；即使页面不同，也不把它们计作多个独立组织。Managed Agents docs 与 blog 是同一官方设计线的不同表面。
- **独立计数 2：OpenClaw**。官方 docs、raw GitHub 文档和同仓库 commit 属同一实现，只计一个产品/组织的一票；不能把 `tasks.md`、`taskflow.md`、`cli/tasks.md` 当成三种独立采用证据。
- **本轮满足“至少两种公开一手实现/官方设计”**：Anthropic Managed Agents 与 OpenClaw task/flow ledger 是两个独立实现/组织；但它们的共同点只证明设计空间，不证明行业采用率或最佳实践。
- 既有 Anthropic feature_list 与本档案的 Managed Agents 不用于凑独立性；它们只用于比较“单 feature/项目多 feature”与“跨 detached work ledger”的尺度差异。

### 偏差与限制

- **文档偏差**：所有主要材料是官方 docs/design，倾向展示理想接口和支持路径；没有真实团队的完整队列截图、失败率、催问次数、feature priority churn 或采用率。
- **状态语义偏差**：`idle` 在 Managed Agents 同时表示等待输入、等待确认和完成后空闲；OpenClaw `blocked` 在 task 层特指结果投递受阻，而 flow 的 `blocked/waiting` 是编排状态，不能直接横向等价。
- **对象偏差**：OpenClaw task 是 detached execution record，不是 feature；Anthropic session 是特定任务实例，不是 backlog item。将它们直接命名为 feature 状态会扩大证据。
- **时间偏差**：OpenClaw 文档为持续更新的 main 分支；记录的 GitHub commit 是最近更新锚点，不是该设计首次发布日。Managed Agents 文档为 beta，行为可能继续改变。
- **结果偏差**：`succeeded`、`satisfied`、`finish` 是系统记录的执行/评估结果，不是产品功能已经被真实用户验收或发布；业务验收仍需外部 rubric、review 或发布门。
- **优先级偏差**：feature_list 的“最高优先级”是一个项目内 prompt/文件约定；没有看到公开的优先级变更事件、排序理由或抢占机制，因此不得把它写成可审计 priority management。

---

## 6. 负结论（本轮明确没有证据的部分）

1. **没有找到一个公开一手实现同时提供完整的跨 feature 状态机**：候选 → 授权 → 在途 → 阻塞 → 验收 → 完成/取消/恢复，并且带可审计的优先级变化历史。
2. **Anthropic feature_list/progress 不等于跨 feature 队列**：它让后续 session 看见多个 feature 的完成标记和最高优先级未完成项，但没有公开的并发运行实例、每 feature owner、阻塞原因、cancel/resume 记录。
3. **Anthropic Managed Agents 不等于跨 session backlog**：它的 session/outcome API 解决单任务长跑的状态、验收和恢复；公开文档没有跨 session feature queue、priority、reordering 或统一授权台账。
4. **OpenClaw task/flow ledger 不等于产品 feature management**：它能列出/过滤多个后台执行，支持 waiting/blocked/cancelled/resume，但不定义 feature 的业务候选、依赖、优先级变化和统一验收 rubric。
5. **没有效果/采用率结论**：没有一手统计证明这些状态机制减少催问、提前完成、返工或人工时间；“可见性存在”不能升级为“机制有效”。
6. **没有把 Claude Code schedules/Routines 计成第三个独立跨 feature 实现**：官方文档显示 routine 是保存的 prompt/repository/connectors 配置与触发器，适合定时/API/GitHub 触发；它回答触发与运行管理，但本轮取得的公开页没有足够完整的 feature-level 状态/优先级/跨 routine 队列证据，且与 Anthropic Managed Agents/Claude Code 同属 Anthropic，不能增加独立性票数。
7. **没有重复 Osmani/词源工作**：本档案不讨论 loop engineering 词源，也不复述 Osmani 的定义/模式；只引用既有 evidence-b 的 feature_list 指针作为尺度对照。

---

## 7. 本轮回答了什么、仍缺什么

### 已回答字段

- **在途**：OpenClaw `queued/running` + `tasks list/show`；Anthropic Managed Agents `running` + event stream；feature_list 可见下一项但不见并发实例。
- **阻塞**：OpenClaw flow `waiting/blocked` 与 task delivery `blocked`；Anthropic confirmation/interrupt/idle + outcome pending/running/evaluating。
- **验收**：Anthropic outcome rubric + 独立 grader + `satisfied/needs_revision/failed/interrupted`；feature_list `passes` 的项目内单项验收；OpenClaw 只有 task/flow terminal outcome 或自定义 workflow，通用 rubric 缺失。
- **完成**：Anthropic `satisfied`（session 回 idle）；OpenClaw `succeeded`/flow `finish`；feature_list 全部 passes 是项目级推断。
- **取消**：OpenClaw task/flow cancel 机制明确；Anthropic outcome `interrupted` 明确，但 feature-level cancel 历史弱。
- **恢复**：Anthropic `wake(sessionId)`/事件日志/续 outcome；OpenClaw `resume`、Gateway restart 持久、delivery retry/dismiss。
- **授权**：Anthropic permission policies/confirmation；OpenClaw standing order scope/approval gate/escalation；feature_list 未见独立授权态。
- **候选**：只部分回答，分别存在 outcome/session 创建、standing order/automation 定义和 feature list 未完成项，但没有统一跨 feature candidate entity。

### 仍缺字段

1. **跨 feature 的统一候选实体与授权历史**：谁提出、谁批准、何时进入队列、授权是否撤回。
2. **跨 feature 的 owner/worker 映射**：某 feature 当前由哪个 session/task/agent 执行，是否并发、是否互斥、依赖谁。
3. **跨 feature 阻塞的业务原因**：等待人、等待依赖、环境坏、资源不足、权限拒绝等原因码和持续时间。
4. **优先级变化审计**：priority 字段、排序/抢占、变更前后值、变更人/理由、是否影响在途工作。
5. **跨 feature 验收总览**：统一 rubric/证据链接、独立验收者、部分通过/回归、发布门与业务验收的关联。
6. **取消/恢复的完整历史**：取消请求者、取消原因、active child 收敛、恢复是否新建执行、旧结果是否仍可见。
7. **真实运行结果与采用率**：至少需要公开运行样本或 DSH 小实验，测量“外部看得见”是否减少催问、漂移、返工和提前完成。

## 一句话判读

**P0 已从“没有成型做法”的空白缩小为两个不同层次的公开答案：Anthropic 把单 session 的运行/验收/恢复做成可观察 API，OpenClaw 把多个 detached execution 做成可列出、过滤、取消、恢复的持久任务账本；但截至 2026-09-27，仍没有一条独立一手证据把跨 feature 的候选、授权、业务阻塞、验收、完成和优先级变化统一成可审计状态机。**
