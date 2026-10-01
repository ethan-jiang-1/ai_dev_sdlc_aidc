---
type: evidence_archive
collected_by: 委派研究代理（W 路 · capability_ladder runtime detail）
collected_at: 2026-09-30
serves: capability_ladder/{00-map,rung-01..03}；补齐输入/状态/决策/动作/出口/失败模式的运行时卡片
status: 新增一手官方文档；Cursor Run Modes/Automations；Claude Managed Agents overview/sessions/events/permissions/outcomes/budgets/scheduled deployments/reference
quality_bar: 官方 docs/API 示例；页面未标发布日期时明确记录；观测日期统一为 2026-09-30；产品名不推断未写出的能力
---

# Evidence W：三档运行时机制细节（观测 2026-09-30）

> 本档不重抄 evidence-b/f/l/u 已有原句：新增的是官方运行时文档/API 对“输入 → 外部状态 → 决策 → 动作 → 出口/失败”的可教学细节。Cursor Run Modes 是对 evidence-u S4a changelog 的 docs 级补强；Managed Agents 是新的 API/运行时来源，不能与 Claude Code `/goal`、`/loop` 自动视为同一实现。

## Source W1 · Cursor Run Modes（LE1：动作授权）

- URL：https://cursor.com/docs/agent/security/run-modes
- 发布日期：页面未标单页发布日期；观测日期：2026-09-30（HTTP 200）
- 来源类型：Cursor 官方 docs

### 逐字片段

> “Run Modes control how the Cursor agent runs tool calls, and when Cursor interrupts you for approval.”

> “Use them to decide how much autonomy the agent gets for shell commands, MCP tools, and Fetch calls.”

官方模式表：

> “**Auto-review** | Allowlisted calls run immediately. Other shell commands run in the sandbox when possible. Calls that do not use the sandbox go to the Auto-review classifier. | Yes, for shell commands | Yes”
>
> “**Allowlist** | Actions in your allowlist run without approval. With sandboxing enabled, supported shell commands can run in the sandbox. | Optional, for shell commands | No”
>
> “**Run Everything** | Every tool call runs automatically. | No | No”

> “Cursor checks each call in this order:”

> “When the classifier blocks a call, Cursor can try another approach. If the agent decides that the action makes sense despite what the classifier said, Cursor will show you an approval prompt.”

> “Auto-review is not a security boundary”

> “`permissions.json` and `sandbox.json` do different jobs”

> “`permissions.json` steers which calls Auto-review runs automatically and which it reviews. `sandbox.json` controls what a sandboxed command can reach, like network domains and extra readable or writable paths.”

配置原句与参数：

```json
{  "autoRun": {    "allow_instructions": [],    "block_instructions": [      "Every AWS CLI command should go through approval first.",      "Every command that modifies Kubernetes resources should go through approval first."    ]  }}
```

> “Auto-review reads `permissions.json` from two locations: `~/.cursor/permissions.json` … `<project-dir>/.cursor/permissions.json`.”

### 机制卡（W1）

- **输入**：tool call（shell/MCP/Fetch）＋ run mode；可选 `permissions.json` 的 `allow_instructions` / `block_instructions`；shell 另受 `sandbox.json` 访问范围约束。
- **状态**：allowlist、可沙箱化与否、classifier 是否启用、当前 project/user policy；该 docs 明确把 permissions 与 sandbox 分成两个控制面。
- **决策**：allowlist 直行；可沙箱 shell 在 sandbox；其余 Auto-review 进 classifier；classifier 可 allow、要求换路、或发起人工 approval。
- **动作**：立即执行、沙箱执行、换一种 agent 路径、或暂停等人批准。
- **出口**：动作完成；classifier 放行/阻断；阻断后 agent 改路；若 agent 仍要求执行则出现 approval prompt。
- **失败模式**：官方明确 classifier 可能误放行或误阻断；Auto-review “is not a security boundary”。`Run Everything` 明确无 sandbox/classifier，不能当成 Auto-review 的更宽版本来继承其保护。
- **支持**：LE1 动作授权面与人在环出口。
- **不支持**：没有声称会启动下一轮、保存跨会话状态、定义完成条件或定时唤醒；不能把 Run Mode 当 LE2/LE3。

## Source W2 · Cursor Automations（LE3：跨会话事件/时间触发）

- URL：https://cursor.com/docs/cloud-agent/automations
- 发布日期：页面未标单页发布日期；观测日期：2026-09-30（HTTP 200）
- 来源类型：Cursor 官方 docs

### 逐字片段

> “Cursor Automations run cloud agents in the background, either on a schedule or in response to events from GitHub, GitLab, Slack, webhooks, Linear, and more.”

> “For any path: 1. Choose a trigger, e.g. every hour or when a pull request is opened. 2. Write a prompt with instructions for the automation. 3. Choose optional tools the agent is able to use … 4. Choose whether the automation needs a repository, multiple repositories, or no repository at all. 5. Save and activate the automation.”

> “Scheduled triggers run on a recurring schedule. Choose from preset options or enter a cron expression for precise control.”

> “Scheduled triggers may run with a delay but will not start before the indicated time.”

> “Webhook triggers create a private HTTP endpoint for your automation. POST to the endpoint to start a run. You can use webhooks to connect automations to internal systems, CI pipelines, monitoring tools, and more.”

> “To retrieve the webhook URL, you must save the automation first, which will then generate a webhook URL to call and an API key for authentication.”

> “Pull request triggers don't run on PRs opened from forks. These runs fail with a ‘Fork pull requests not supported’ error because the branch only exists on the fork, and running external code with the repo's permissions isn't safe.”

### 机制卡（W2）

- **输入**：cron/预设时间、GitHub/GitLab/Slack/Linear/外部 webhook 事件；prompt；可选 tools；repo/多 repo/无 repo；webhook 还要求保存后生成 URL＋API key。
- **状态**：已保存且 activated 的 automation 配置；cloud-agent run；repo 绑定；服务身份与用量计费（页面说明 automations 创建 cloud agents）。
- **决策**：任一 trigger fire 即启动；cron 只保证“不早于指定时间”，可能延迟；源代码事件按连接 provider 的事件类型过滤。
- **动作**：后台启动 cloud agent，按 prompt 使用所选 tools，在绑定资源上运行。
- **出口**：run 完成/失败；automation 可继续等待下一次 trigger。页面未给出统一的完成验收或跨 run 状态恢复契约。
- **失败模式**：fork PR 直接失败；webhook 未先保存 automation 无 URL/API key；未指定 repo 时，Slack/cron 默认可能不使用 repo，若需改代码必须显式指定 repo。
- **支持**：LE3 跨会话的时间/事件唤醒存在，并给出输入、触发、资源绑定与失败出口。
- **不支持**：不等于 Cursor 本地 `/loop`；不提供 LE2 的“达到目标才继续”判定，也不证明 cloud run 自动继承本地 Run Mode/审批设置。

## Source W3 · Claude Managed Agents overview/sessions/events（LE2/LE3：持久会话运行时）

- URLs：
  - https://platform.claude.com/docs/en/managed-agents/overview
  - https://platform.claude.com/docs/en/managed-agents/sessions
  - https://platform.claude.com/docs/en/managed-agents/events-and-streaming
  - https://platform.claude.com/docs/en/managed-agents/session-operations
- 发布日期：各页未标单页发布日期；页面统一显示 beta header `managed-agents-2026-04-01`；观测日期：2026-09-30（HTTP 200）
- 来源类型：Anthropic Claude Platform 官方 docs/API 示例

### 逐字片段

> “Pre-built, configurable agent harness that runs in managed infrastructure. Best for long-running tasks and asynchronous work.”

> “A session is an agent instance within an environment. Each session references an agent and an environment … and maintains conversation history across multiple interactions.”

> “Sessions follow a two-step lifecycle: first create the session, then send a user event to start work.”

创建会话参数（官方 Python 示例）：

```python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
)
```

> “Send a `user.message` event to start or continue the agent's work:”

```python
client.beta.sessions.events.send(
    session.id,
    events=[
        {
            "type": "user.message",
            "content": [
                {
                    "type": "text",
                    "text": "Analyze the performance of the sort function in utils.py",
                },
            ],
        },
    ],
)
```

> “Every persisted event includes a `processed_at` timestamp set when the event finishes processing. On events you send, `processed_at` is null while the event is still queued behind earlier events.”

会话状态表原句：

> “`idle` | Agent is waiting for input, including user messages or tool confirmations.”
>
> “`running` | Agent is actively executing.”
>
> “`rescheduling` | Transient error occurred, retrying automatically.”
>
> “`terminated` | Session has ended, either because of an unrecoverable error or because it was archived.”

持久状态与操作：

> “Event history is persisted server-side and can be fetched in full.”

> “Send a `user.interrupt` event to stop the agent mid-execution, then follow up with a `user.message` event to redirect it.”

### 机制卡（W3）

- **输入**：创建时 `agent` ID＋`environment_id`；随后 `user.message`、`user.interrupt`、`user.tool_confirmation`、`user.define_outcome` 等事件。
- **状态**：server-side event history；会话状态 `idle/running/rescheduling/terminated`；environment 与 session conversation history 独立持久化。
- **决策**：事件排队后按 session 处理；`rescheduling` 表示 transient error 自动重试；`user.interrupt` 改变当前执行方向。
- **动作**：harness 在 managed/self-hosted environment 执行工具并回传 agent/session events；应用通过 SSE/事件流观察状态。
- **出口**：正常结束回到 `idle`，而不是自动 `terminated`；不可恢复错误或 archive 才到 `terminated`；事件可再次送入以恢复/续跑。
- **失败模式**：服务端不可恢复错误导致 `terminated`；事件可能排队（`processed_at=null`），不能把“已提交”当“已执行”；会话的 agent 配置变更有边界——运行中需先 `user.interrupt` 等回 `idle`；页面还明确该能力为 beta。
- **支持**：LE2 的持久目标/状态/事件续跑基础；LE3 跨会话唤醒的可持久 session runtime。
- **不支持**：session 持久化本身不等于定时/事件 scheduler；必须另有 scheduled deployment 或外部事件发送。也不等于 Claude Code 本地 `/goal` 的 session-scoped Stop hook。

## Source W4 · Claude Managed Agents permission policies（LE1：服务端工具动作门）

- URL：https://platform.claude.com/docs/en/managed-agents/permission-policies
- 发布日期：页面未标单页发布日期；文档版本标识 `managed-agents-2026-04-01`；观测日期：2026-09-30
- 来源类型：Anthropic 官方 docs

### 逐字片段

> “Permission policies control whether server-executed tools (the pre-built agent toolset and MCP toolset) run automatically, wait for your approval, or have each call evaluated by the server.”

> “Custom tools are executed by your application and controlled by you, so they are not governed by permission policies.”

> “`always_allow` | The tool executes automatically with no confirmation.”
>
> “`always_ask` | The session pauses and waits for your approval before executing.”
>
> “`auto` | The server evaluates each call and runs it, denies it, or pauses for your approval.”

> “Each toolset kind has its own default: the agent toolset defaults to `always_allow`, and MCP toolsets default to `always_ask`.”

配置示例：

```yaml
name: Coding Assistant
model: claude-opus-5-5
tools:
  - type: agent_toolset_20260401
    default_config:
      permission_policy:
        type: always_ask
```

### 机制卡（W4）

- **输入**：server-executed agent/MCP tool call＋toolset policy；custom tool call 由应用自己控制。
- **状态**：policy 类型 `always_allow/always_ask/auto`；默认值随 toolset 不同。
- **决策**：自动执行、暂停等待确认、或 server 评估后执行/拒绝/暂停。
- **动作**：工具执行、拒绝、等待 `user.tool_confirmation`。
- **出口**：执行结果回到 agent；确认/拒绝事件结束该工具门；custom tool 不走此 policy。
- **失败模式**：把 MCP 的默认 `always_ask` 当成 agent toolset 默认值会错；把 custom tools 当作平台自动审查也会错。
- **支持**：LE1 工具动作授权。
- **不支持**：不是 goal 完成判定；不是 scheduler；不提供“自动执行即质量正确”的保证。

## Source W5 · Claude Managed Agents outcomes（LE2：目标/评估续跑）

- URL：https://platform.claude.com/docs/en/managed-agents/define-outcomes
- 发布日期：页面未标单页发布日期；文档版本标识 `managed-agents-2026-04-01`；观测日期：2026-09-30
- 来源类型：Anthropic 官方 docs/API 示例

### 逐字片段

> “An outcome tells the session what the end result should look like and how to measure its quality. The agent works toward that target, self-evaluating and iterating until the outcome is met.”

> “When you define an outcome, the harness automatically provisions a _grader_ to evaluate the artifact against a rubric. The grader uses a separate context window to avoid being influenced by the main agent's implementation choices.”

> “The grader returns an explanation summarizing which criteria passed or failed, or confirming that the artifact satisfies the rubric. That feedback is handed back to the agent for the next iteration.”

> “A rubric is a markdown document describing per-criterion scoring. The rubric is required.”

> “Pass the rubric as inline text on `user.define_outcome` … or upload it through the Files API for reuse across sessions.”

### 机制卡（W5）

- **输入**：`user.define_outcome`＋required markdown rubric（inline 或 Files API）；session/agent/environment。
- **状态**：rubric、每项 grader 反馈、持久 session history；grader 使用独立 context window。
- **决策**：grader 按 rubric 返回哪些 criteria passed/failed；反馈驱动下一轮。
- **动作**：agent 继续迭代 artifact，或在 outcome met 后结束该目标。
- **出口**：outcome met；每轮反馈后继续；真实 session 仍可能因 interrupt、budget、不可恢复错误而停。
- **失败模式**：rubric 是 required，空泛目标不能由该 API 自动补成可验条件；grader 的“满足 rubric”不是人对业务质量的最终验收；不能把 grader 与 LE1 permission policy 混成同一裁判。
- **支持**：LE2 有界目标续跑的输入、独立评估、反馈与停止出口。
- **不支持**：没有声明固定轮数；“outcome met”不等于所有业务风险已验收；不能据此推出 Claude Code `/goal` 的具体三值 verdict。

## Source W6 · Claude Managed Agents budgets（LE2/LE3：硬成本出口）

- URL：https://platform.claude.com/docs/en/managed-agents/budgets
- 发布日期：页面未标单页发布日期；文档版本标识 `managed-agents-2026-04-01`；观测日期：2026-09-30
- 来源类型：Anthropic 官方 docs/API 示例

### 逐字片段

```python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    budget={
        "type": "limit",
        "max_list_cost": {"amount": "125", "currency": "USD"},
    },
)
```

> “`amount` is a whole number of US cents written as a string with no leading zeros (`"125"` is $1.25 and `"50"` is 50 cents) … `USD` is the only supported currency.”

> “The request in flight when the cap is crossed still finishes, so the final list cost can land a fraction past the budget.”

> “A session that reaches its budget goes idle with a `stop_reason` of `budget_reached`; it is not terminated, and its history and sandbox are preserved…”

> “Any event that would start new work, such as `user.message`, is rejected with a 400 error…”

> “Both automatically resume work that paused when the session reached its cap.”

### 机制卡（W6）

- **输入**：session create 的 `budget.type="limit"`＋`max_list_cost.amount`（整数美分字符串）＋`currency="USD"`。
- **状态**：持续计算 list cost；cap 前允许模型请求；达到 cap 后 session `idle`、`stop_reason=budget_reached`，history/sandbox 保留。
- **决策**：每次新模型请求前检查 consumed list cost；达到上限不再发新请求。
- **动作**：在途请求完成；随后暂停；只接受 `user.tool_confirmation`、`user.tool_result`、`user.custom_tool_result`、`user.interrupt` 等结算在途工作的事件。
- **出口**：预算暂停（可调高/移除后自动恢复）；不是 terminated。
- **失败模式**：在途请求造成 bounded overshoot（每线程最多一请求的余量）；把 budget 当精确停止点会误判；达到 cap 时新的 `user.message` 会 400，不能把“发消息”当恢复动作。
- **支持**：LE2/LE3 必须有的硬预算与可恢复出口。
- **不支持**：budget 是花费上限，不是完成条件；不能用它替代 outcome/grader 或 scheduler。

## Source W7 · Claude Managed Agents scheduled deployments（LE3：跨会话定时唤醒）

- URL：https://platform.claude.com/docs/en/managed-agents/scheduled-deployments
- 发布日期：页面未标单页发布日期；文档版本标识 `managed-agents-2026-04-01`；观测日期：2026-09-30
- 来源类型：Anthropic 官方 docs/API 示例

### 逐字片段

> “A scheduled deployment allows an agent to start sessions autonomously, enabling task completion over a predictable cadence.”

> “Deployments also require at least one initial event, a `user.message` or `user.define_outcome`, that starts each session's work.”

> “In the `schedule`, you define a cron `expression` and a `timezone`. Maximum granularity supported is at the minute level.”

官方 CLI 示例：

```text
ant apply deployment.md
```

```yaml
name: Weekly compliance scan
agent: agent_011CYm1BLqPXpQRk5khsSXrs
environment_id: env_01595EKxaaTTGwwY3kyXdtbs
schedule:
  type: cron
  expression: "0 20 * * 5"
  timezone: America/New_York
---

Run the weekly compliance scan.
```

> “The response includes a deployment object with a populated `schedule.upcoming_runs_at` with the next upcoming fire times, to confirm your schedule was set correctly.”

### 机制卡（W7）

- **输入**：agent＋environment；至少一个初始 `user.message` 或 `user.define_outcome`；cron `expression`＋`timezone`。
- **状态**：deployment `active/paused`（示例对象含 `status`、`paused_reason`、`last_run_at`、`upcoming_runs_at`）；每次触发创建 session。
- **决策**：scheduler 按 cron 在分钟粒度唤醒；部署对象的 upcoming runs 可供检查。
- **动作**：自主启动 session，执行初始 event 指定的工作。
- **出口**：每次 run 的 session 自己按 outcome、interrupt、budget、错误等出口结束/暂停；deployment 仍可等待下一次计划。
- **失败模式**：没有 initial event 不能启动工作；cron 语义是跨 session scheduler，不是本地 `/loop`；官方页没有声称任意云端任务都拥有 `/loop` 的 7 天过期或 20 分钟 fallback。
- **支持**：LE3 跨会话持久唤醒的实际 API/CLI 机制。
- **不支持**：不证明所有会话内定时任务都能跨会话；不自动赋予 LE1 高风险动作权限；具体 permission policy 仍由 agent/tool 配置决定。

## Source W8 · Claude Managed Agents worker reference（LE1/LE3：执行环境与守护出口）

- URL：https://platform.claude.com/docs/en/managed-agents/reference
- 发布日期：页面未标单页发布日期；文档版本标识 `managed-agents-2026-04-01`；观测日期：2026-09-30
- 来源类型：Anthropic 官方 docs

### 逐字片段

> “`--workdir` | Directory where skills are downloaded and tools read and write files. Defaults to `.` (the current directory); the system default working directory is `/workspace`.”
>
> “`--unrestricted-paths` | Allow the file tools to read and write paths outside `--workdir`. The workdir check is a guardrail for the file tools only, not a sandbox; it does not constrain bash.”
>
> “`--max-idle` | How long to wait after the session goes idle with an `end_turn` stop reason before shutting down. Defaults to `60s`.”

> “The CLI worker does not mount memory stores … To use memory stores in sessions on a self-hosted environment, run the SDK worker instead.”

### 最小主张

- **支持**：运行时的 workdir、idle shutdown 与 self-hosted worker 选项是独立的环境/守护面；`--unrestricted-paths` 不是完整 sandbox。
- **不支持**：不能把 `--workdir` 当作 bash 的全局隔离；不能把 CLI worker 的 memory-store 缺失推成 Managed Agents 全部实现缺失；不能把 `--max-idle` 当作任务完成判定。

## 三档精炼机制卡（教学版；来源指针，不替代上面逐字档案）

### LE1 · 有界执行：把“能做什么”交给动作门

- **输入**：tool call＋allowlist/sandbox/classifier 或 `always_allow/always_ask/auto`。
- **状态**：动作类别、目标路径/网络、sandbox 与 policy 状态；审批是否待决。
- **决策**：allow / sandbox / classifier；或 auto 执行、deny、pause for approval。
- **动作**：执行、拒绝、换路、暂停等确认；custom tool 另由应用控制。
- **出口**：结果返回；拒绝后换路；人确认/拒绝；硬边界停下。
- **失败**：误放行/误阻断；权限策略默认值混淆；`Run Everything` 无安全审查；`--unrestricted-paths` 不约束 bash。
- **不混用**：LE1 只回答“这一动作现在能否执行”；不回答“下一轮何时启动”或“产出是否完成”。见 W1/W4/W8 与既有 evidence-f。

### LE2 · 有界目标续跑：把“是否值得再跑”交给目标/评估器＋硬预算

- **输入**：goal/outcome＋可观察 rubric/check；Managed Agents 用 `user.define_outcome`，Claude Code `/goal` 仍是另一套 session-scoped Stop hook（见 evidence-b）。
- **状态**：每轮 artifact、独立 grader feedback、session event history、list cost、暂停/恢复状态。
- **决策**：grader 反馈驱动继续或 outcome met；预算达到即暂停，不以 cost 充当质量 verdict。
- **动作**：继续迭代、回传反馈、人工 interrupt/redirect；预算更新后恢复。
- **出口**：outcome met；预算 `budget_reached`→idle；不可恢复错误→terminated；人 interrupt。
- **失败**：rubric 空泛；grader 误判；预算在途 overshoot；把已排队事件当已处理；把预算当完成条件。
- **不混用**：LE2 的“再跑”是条件/反馈驱动；没有 scheduler 就不会因日历/外部事件在会话外重新起跑。见 W3/W5/W6 与既有 evidence-b/l。

### LE3 · 定时/事件唤醒：把“什么时候再跑”交给 scheduler

- **输入**：cron/timezone、webhook/event、initial event、repo/resource binding。
- **状态**：deployment/automation active、next run、session history、cancel/interrupt、budget 与 policy。
- **决策**：任一 trigger fire 或 cron 到点（可能延迟）；每次新 session 由 initial event 定义工作。
- **动作**：后台 cloud agent / scheduled deployment 启动 session；本地 `/loop` 则仅在原 session 内重复 prompt（既有 evidence-b/u）。
- **出口**：单次 run 完成/暂停/失败；deployment/automation 留待下一触发；可由 webhook/API/取消动作停下。
- **失败**：fork PR 不支持；webhook 未保存无 URL/API key；无 initial event 不起跑；事件排队/状态丢接手；未继承 LE1 policy 或无预算；跨会话系统可能没有本地 `/loop` 的 7 天/20 分钟保护。
- **不混用**：LE3 只交出“何时唤醒”，不自动授予动作权限，也不自动定义完成条件；会话内 `/loop`、Cursor Automations、Claude Managed Agents scheduled deployment 是三种不同运行边界，不能互相套参数。见 W2/W3/W7 与既有 evidence-b/u。

## 回源纪律与负结论

- 页面未标发布日期的官方 docs，统一写“未标单页发布日期”，不把观测日期冒充发布日期。
- `managed-agents-2026-04-01` 是 docs/API beta header/version anchor，不等于页面发布日期或 GA 承诺。
- Cursor Run Modes docs 的“Auto-review is not a security boundary”只支持该产品文档的限定性警告，不推导其他产品的 classifier 安全性质。
- Anthropic Managed Agents 的 `user.define_outcome`、budget、scheduled deployment 是 Managed Agents API 机制；不能把它们的参数、状态名、出口冒充 Claude Code `/goal` 或 `/loop` 的参数/默认值。
- Cursor Automations 的 cloud agent trigger、repo 绑定与 fork 失败属于 Automations docs；不能反推本地 Cursor `/loop` 有相同状态存储、API 或失败出口。
- 未取得独立 P-outcome：这些 docs/API 示例证明机制存在与边界，不证明质量效果、普遍采用率或跨产品可迁移性。
