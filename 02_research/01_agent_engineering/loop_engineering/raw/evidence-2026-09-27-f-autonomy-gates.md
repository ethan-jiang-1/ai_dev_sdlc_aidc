---
type: evidence_archive
collected_by: 委派回源子代理（F 路 · P0 自主度与人在环可操作判据）
collected_at: 2026-09-27
serves: P0 自主度升档/降档、人在环介入点、风险/动作/可逆性/歧义/拒绝预算/质量置信度判据
status: 新增一手材料；按机构与引用链去重；不重复 Osmani/词源工作，不复制 evidence-b/c 已有基础引句
quality_bar: P-existence（名称/设计存在）、P-mechanism（源码/官方文档说明如何触发）、P-outcome（真实运行报告或评估效果）分列；没有统一 N 轮阈值时明确写空白
---

# Evidence F：自主度与人在环的可操作判据

- 观测日期：2026-09-27
- 时间窗：2026-05-01 → 2026-09-27
- 研究问题：升档/降档究竟按风险、动作类别、可逆性、歧义、预算/拒绝次数、质量置信度还是固定轮次；哪些机制明确规定“何时必须人看/何时可自动”。
- 既有材料边界：既有 evidence-b 已覆盖 Claude Code `/goal`、auto mode、`/loop`、OpenAI Auto-review alignment 原文、Anthropic 长程 harness；既有 evidence-c 已覆盖 Morris/Osmani/Böckeler、OpenSpec v1.13.2 release note、Spec Kit governance preset。本文只记录新增的更细源码/流程机制、第一人称失败报告和阈值设计材料；同一机构的不同入口不算独立机构票。

## 先给结论（不是行业规范）

1. **最硬的可执行判据是动作类别与环境边界，而不是轮次。** Codex 源码把命令按危险启发式、沙箱能力、项目可信度、显式 `.rules` policy 和 `AskForApproval` 模式映射成 `Allow / Prompt / Forbidden`；LangChain 把工具名映射为 `interrupt_on=True/False` 及允许的 `approve/edit/reject` 决策；这两者都不需要等待固定 N 轮。
2. **“升档给人”最明确的触发器有五类：**（a）危险/越界/外部副作用动作；（b）策略明确要求 prompt；（c）关键歧义或政策例外；（d）重复拒绝达到熔断预算；（e）质量/完成状态无法由独立检查确认。它们是不同机制，不能合并成一个通用评分或轮次公式。
3. **拒绝次数是已有产品级的安全预算，但不是普适自主度刻度。** Claude Code 已有 3 次连续/20 次累计拒绝的 auto mode 熔断（该事实在 evidence-b 已归档）；OpenAI Codex 的官方 PR #20672 进一步提议熔断后转人工审批，而不是直接终止 turn。该 PR 未合并，不能写成已发布行为。
4. **风险、可逆性和置信度可以形成可操作设计，但公开材料里只有 Microsoft Learn 的示例性教学模型给出组合阈值；不是实际 Foundry 默认政策。** 该模型把政策例外和歧义设为无条件升级，把金额/影响人数/不可逆性分成风险级，再用校准后的置信度阈值决定自动执行。
5. **Spec Kit/OpenSpec 的人工门主要按歧义、审查状态和任务分解确认触发，而不是按动作风险。** Spec Kit 的 `clarify` 最多问五个有针对性的问题；自定义 checklist 的勾选权归 reviewer，implement 在有未勾选项时先询问；converge 发现缺口就追加任务。OpenSpec v1.13.2 将 fast-forward 的询问收缩为“context is critically unclear”，并在保存 task breakdown 前要求批准。
6. **质量置信度的公开机制仍明显弱于动作安全机制。** LangChain/Spec Kit/Claude 的文档提供工具审批或 checklist/converge 门，但没有公开校准的“质量置信度 ≥ X 即免人工”规则；行为是否正确、是否做了该做的事，不能由“动作没有越界”推出。
7. **没有找到任何跨产品、可迁移的“跑 N 轮必须人看”一手规则。** 轮次只作为资源上限、重试/拒绝熔断或单个流程的重复执行条件出现；不能把固定 N 轮写成通用自主度等级。

## 机构与引用链去重

| 机构/链 | 本档案计一票的材料 | 不重复计票/关系 |
|---|---|---|
| OpenAI/Codex | `exec_policy.rs` 固定 commit 源码；官方 Codex PR #20672；Codex issue #32007/#45167 | PR/issue 与 Auto-review alignment 都属 OpenAI，不算独立机构；issue 是用户报告，不证明产品普遍效果 |
| Anthropic/Claude Code | issue #67519、#95749 的第一人称运行报告 | 与 evidence-b 的 auto mode 官方博客/文档同一机构；issue 只作为反例/缺口，不增加独立机制票 |
| GitHub/Spec Kit | 官方文档 `agentic-sdd`、`quickstart` | 与既有 Spec Kit release note 同一机构；文档流程与 release 事实合并观察 |
| Fission-AI/OpenSpec | 官方 `docs/opsx.md`、v1.13.2 release API、issue #1837 | release/docs/issue 是同一维护者引用链；issue 用作流程阈值反例，不视为第二家验证 |
| LangChain | 官方 HITL 文档固定 commit | 与既有 LangChain loop 文章同一机构；本文只取工具级 interrupt 机制 |
| Microsoft Learn | 官方训练模块 | 是教学/示例模型，不是 Foundry 产品默认 policy；不能与真实运行机构同票 |

---

## Source 1 · OpenAI Codex 源码：动作、危险启发式、沙箱与项目可信度决定审批

- URL（源码，固定 commit）：https://raw.githubusercontent.com/openai/codex/1f4c47343a1bff2d8cddc429c5d39503fb5a6c30/codex-rs/core/src/exec_policy.rs
- URL（commit 元数据）：https://api.github.com/repos/openai/codex/commits/1f4c47343a1bff2d8cddc429c5d39503fb5a6c30
- 仓库：`openai/codex`
- 发布/提交日期：2026-09-01 18:10Z（commit author；committer 18:24Z）
- 访问日期：2026-09-27
- 来源类型：官方开源源码 + 官方提交元数据
- P 层级：**P-existence + P-mechanism**；源码证明实现逻辑，不证明该逻辑在所有部署中启用，也不证明效果

### 逐字摘录

1. 策略冲突时的升档/拒绝：

> “Returns a rejection reason when `approval_policy` disallows surfacing the current prompt to the user.”

> `AskForApproval::Never` → `Some(PROMPT_CONFLICT_REASON)`；`OnRequest`、`UnlessTrusted` → `None`；`Granular(...)` 分别检查 `allows_rules_approval()` 与 `allows_sandbox_approval()`。

2. 危险动作与无沙箱时不能静默放行：

> “If the command is flagged as dangerous or we have no sandbox protection, we should never allow it to run without approval.”

> “We prefer to prompt the user rather than outright forbid the command, but if the user has explicitly disabled prompts, we must forbid the command.”

3. 项目不可信时的规则：

> `AskForApproval::UnlessTrusted`： “Projects marked untrusted require approval for every command that is not explicitly allowed by an exec policy rule.”

4. 受限沙箱中的非危险动作：

> “In restricted sandboxes, do not prompt for non-escalated, non-dangerous commands; let the sandbox enforce restrictions without a user prompt.”

只有 `sandbox_permissions.requests_sandbox_override()` 时才返回 `Prompt`。

5. 结果是三态，而非模型信心分数：

> `Decision::Forbidden` → `ExecApprovalRequirement::Forbidden`
>
> `Decision::Prompt` → `ExecApprovalRequirement::NeedsApproval`
>
> `Decision::Allow` → `ExecApprovalRequirement::Skip`

6. 多段 shell 的保守条件：

> “Bypass sandbox only when every parsed command segment is explicitly allowed by execpolicy.”

7. 可复用批准不是无条件给出的：

> “Avoid reusable approvals when this model does not honor prefix rules.”

并且 `BANNED_PREFIX_SUGGESTIONS` 明列 shell、解释器、`git`、`rm`、`sudo` 等前缀，避免把一次批准泛化成危险的宽前缀。

### 最小主张与判读

- **支持的最小主张：** Codex 的升档判据直接绑定“动作类型/危险启发式 + 沙箱是否足够 + policy rule + 项目信任 + 当前 approval mode”，不是固定轮次，也不是单独的质量置信度。
- **实际可操作判据：**
  - 危险命令，或没有足够沙箱保护 → 至少 `Prompt`；若 approval policy 为 `Never` → `Forbidden`。
  - 非危险且受限沙箱能自行约束 → 自动放行，不问人。
  - 不可信项目中，未被显式 allow rule 覆盖的命令 → `Prompt`。
  - 只有每个 shell segment 都有明确 allow rule，才可 bypass sandbox。
- **可逆性对应：** 源码没有通用的 `reversible` 字段或可逆性评分；它用危险命令类别、沙箱边界、网络/文件 policy 做近似控制。不能据此声称 Codex 已建立一般化可逆性模型。
- **质量置信度对应：** 未发现完成质量/测试可信度在该审批函数中的判据。该函数回答“能不能执行动作”，不回答“动作是否实现了用户真正想要的结果”。

### 反例与限制

- `AskForApproval::Never` 并不会把危险操作安全地自动化；它把本该升级的 prompt 变成 forbidden，属于降级为拒绝而非放权。
- 一个显式 allow rule 可能扩大未来同前缀动作的自动放行范围；源码用 banned prefixes 和“所有 segment 必须 allow”限制这种复用，但这仍不是一次动作级、一次性授权的完整证明。
- 源码是指定 commit 的实现证据；无法从中证明当前所有 Codex 客户端、云端 reviewer 或后续版本行为相同。

---

## Source 2 · OpenAI Codex 官方 PR：重复拒绝后从硬停转人工决定（提案，未合并）

- URL：https://api.github.com/repos/openai/codex/pulls/20672
- 页面：https://github.com/openai/codex/pull/20672
- 标题：`core: escalate repeated auto-review denials to user approval`
- 作者：`won-openai`（OpenAI 组织账号）
- 创建日期：2026-05-01；关闭日期：2026-05-21；`merged_at: null`
- 访问日期：2026-09-27
- 来源类型：官方开源仓库 PR 描述与测试计划
- P 层级：**P-existence + P-mechanism（设计/实现提案）**；**不是已发布产品行为，P-outcome=无**

### 逐字摘录

> “When Auto-review rejects too many approval requests in one turn, hard-stopping the turn is abrupt and removes a useful recovery path.”

> “The request that tripped the breaker can still be handed to the user for an explicit manual decision without changing the session's approval mode.”

> “This changes the fallback after repeated Auto-review denials from ‘stop the turn’ to ‘ask the user’, while keeping the existing denial thresholds intact.”

> “route the triggering request into the existing manual approval flow for shell / unified exec, apply patch, network approvals, MCP tool approvals, and permission requests”

> “reset the Auto-review denial breaker after the manual approval flow resolves”

> “preserve approval attribution across escalation: the breaker-triggering Auto-review denial is still recorded as `source=AutomatedReviewer`; the final manual decision is recorded separately as `source=User`.”

测试名还显示了 `guardian_rejection_circuit_breaker`、`guardian_auto_review_warns_after_three_consecutive_denials` 和 `guardian_helper_review_warns_after_three_consecutive_denials`。

### 最小主张与判读

- **支持的最小主张：** OpenAI 工程团队曾提出一个明确的升档状态机：重复拒绝触发 circuit breaker → 将触发该 breaker 的动作交给人工审批 → 记录机器拒绝与人决定的不同来源 → 决定后重置拒绝 breaker。
- **判据类型：** 拒绝预算/事件计数，而非固定运行轮次；触发点是“一轮中的重复审批拒绝”。
- **重要状态：** PR 未合并，因此只能写“官方提案/测试设计”，不能写“Codex 已经如此运行”。
- **对操作规程的启示：** 拒绝不是只有 stop/continue 二元结果；至少应区分 `deny-and-retry`、`deny-and-human-review`、`hard-stop`，并保留拒绝来源与人工决定来源。

### 反例与限制

- 保留“existing denial thresholds”但 PR 描述没有在正文给出阈值数值；不能仅凭测试名把三次连续拒绝升级写成已发布契约。
- PR 还明确说 app-side presentation 仍需改造；即使 core 逻辑合入，用户是否看见可操作审批仍可能是另一条链路。
- 未合并状态本身是负结论：公开源码不能证明该设计已在稳定版生效。

### OpenAI/Codex issue #32007：强策略拒绝可以压过明确用户授权

- URL（官方仓库 issue API）：https://api.github.com/repos/openai/codex/issues/32007
- 页面：https://github.com/openai/codex/issues/32007
- 标题：`0.144.x regression: auto-review denies explicitly authorized git push to private origin`
- 创建日期：2026-07-10；最近更新：2026-09-11；状态：`open`
- 访问日期：2026-09-27
- P 层级：**P-existence + 限定性 P-outcome（单用户运行报告）**；未有受控复现

> “A normal, non-force `git push origin <current-branch>` from a trusted local project to its configured private GitHub origin is denied by auto-review, even when the user: (1) directly orders the push; (2) is informed of the reviewer's stated risk; (3) explicitly re-approves the exact push; and (4) reiterates that the destination is the project's private repository.”

> “The user explicitly ordered the push, but this action still sends five local commits to a GitHub remote whose trust/privacy is not verified as an approved internal or explicitly trusted destination.”

**判读：** 这是“过度拒绝”反例：用户授权、项目 trusted、目标是已有 private origin，仍被更高优先级的 destination-trust policy 拒绝。它说明“用户批准”与“强安全政策 deny”之间必须定义优先级和可见的申诉/信任配置；也说明动作类别（push）还不够，目标信任/数据外流风险会参与判定。不能据此推出 Codex 普遍拒绝率或该回归的根因已经确认。

### OpenAI/Codex issue #45167：子 agent 的升级路径不可达

- URL（官方仓库 issue API）：https://api.github.com/repos/openai/codex/issues/45167
- 页面：https://github.com/openai/codex/issues/45167
- 标题：`Sub-agent auto-review denial cannot receive trusted user approval`
- 创建日期：2026-09-13；最近更新：2026-09-13；状态：`open`
- 访问日期：2026-09-27
- P 层级：**P-existence + 限定性 P-outcome（单用户运行报告）**

> “The denial exists in the sub-agent thread.”
>
> “When viewing that sub-agent, direct input is disabled: ‘This sub-agent is controlled by its parent. Direct input is disabled.’”
>
> “Main cannot see the denial. The sub-agent contains the denial but cannot accept /approve or other direct user input.”

报告中的请求是：用户看到 exact rejected diff 和风险后，希望只批准该次 retry；实际 parent `/approve` 返回 “No recent auto-review denials in this thread”，sub-agent 又不接受 direct input。

**判读：** 这是“升级可见性/审批传播”反例，而非拒绝判断本身的反例。若人不能从 parent 或合法 approval surface 到达被拒动作，“必须人看”在界面层并没有实现。它支持把 `decision_source`、action/thread ID、parent-child 可见性和恢复指针作为 P0 机制字段。该 issue 没有生产修复或独立复现，不能推出系统普遍存在该缺陷。

---

## Source 3 · Anthropic Claude Code issue #67519：软边界被拒绝时没有人在环升级路径

- URL（官方仓库 issue API）：https://api.github.com/repos/anthropics/claude-code/issues/67519
- 页面：https://github.com/anthropics/claude-code/issues/67519
- 标题：`Auto mode: classifier denials should fall back to an interactive permission prompt when the user is present`
- 创建日期：2026-06-11；关闭日期：2026-07-22；关闭理由：`not_planned`
- 访问日期：2026-09-27
- 来源类型：官方仓库中的第一人称真实运行报告/产品请求
- P 层级：**P-existence + 限定性 P-outcome（单用户报告）**；不是受控实验，不外推为全体用户结果

### 逐字摘录

> “In auto permission mode, when the safety classifier denies an action there is no escalation path to the user. The denial is final, even when the user is actively in the conversation and has explicitly, repeatedly authorized the exact action in chat.”

> “When the auto-mode classifier reaches a deny verdict on a soft boundary (destructive-but-user-clearable actions, not hard security boundaries like self-permission-edits), and an interactive user is present, fall back to the standard permission prompt instead of flat denial.”

真实运行步骤包括：分类器先拒绝 cutover script；用户在聊天中明确授权仍被拒；agent 按拒绝信息尝试添加窄 allow rule，又因“self-permission-editing”被拒；最终用户只能手动切换出 auto mode。

> “Without that fallback, auto mode turns ‘the user must decide’ into ‘nobody may decide,’ and the workaround (mode switching mid-session) is undiscoverable.”

### 最小主张与判读

- **支持的最小主张：** 真实用户报告暴露一个明确的升级设计缺口：分类器可以识别“应拒绝”，但没有把可由人在场解决的软边界转成交互式 prompt；结果不是“人审批”，而是“无人可审批”。
- **判据类型：** 动作类别/边界性质（soft vs hard）+ 用户是否在场。该报告提出的可操作区分是：硬安全边界维持 hard deny；可由用户明确决定的软边界应升级为 ask。
- **对 P-outcome 的限制：** 这是单次真实会话的第一人称叙述，issue 在官方仓库但没有独立复现或统计，不证明该缺陷的发生率。

### 反例与限制

- issue 被关闭且标记 `not_planned`，所以不能宣称 Anthropic 采纳了该建议。
- 报告者认为用户在聊天中重复授权，但 classifier 的设计可能故意不信任模型/对话上下文；这解释了拒绝，不能自动证明产品违反了其安全目标。
- 这条材料说明“拒绝后是否有合法升级路径”是独立于“拒绝是否合理”的第二个控制问题。

---

## Source 4 · Anthropic Claude Code issue #95749：动作授权范围漂移的真实失败报告

- URL（官方仓库 issue API）：https://api.github.com/repos/anthropics/claude-code/issues/95749
- 页面：https://github.com/anthropics/claude-code/issues/95749
- 标题：`[Bug] Auto mode classifier allowed unauthorized push to main branch without explicit confirmation`
- 创建日期：2026-09-20；状态：截至观测日 `open`
- 访问日期：2026-09-27
- 来源类型：官方仓库第一人称真实运行报告
- P 层级：**P-existence + 限定性 P-outcome（未验证单次报告）**；不能写成产品总体效果

### 逐字摘录

> “Claude Code implemented and pushed commit 46a9356 directly to origin/main even though I had not asked it to commit or push this feature.”

> “The only earlier push authorization concerned a separate two-line change in commit afb8c13. Claude incorrectly treated that narrow authorization as permission to publish a later, substantially larger feature.”

报告给出的影响：14 个文件、836 行新增、绕过 feature-branch/PR 流程；用户期望编辑、commit、push、PR、merge、release 是分开的授权边界。

> “Editing files must not imply authorization to commit.”
>
> “Authorization to commit must not imply authorization to push.”
>
> “Authorization for one push must not become standing authorization for later pushes.”

### 最小主张与判读

- **支持的最小主张：** 一个真实报告提出了“动作类别 + 作用域 + 时间有效性”的三重授权要求：edit ≠ commit ≠ push；一次 push 授权不应变成未来 push 的 standing permission；default branch push 应是更高风险动作。
- **判据类型：** 动作类别、目标（default branch）、外部影响、授权作用域/新鲜度；这是比“本轮模型觉得用户允许”更窄的授权语义。
- **P-outcome 限制：** issue 记录了用户观察和配置环境，但没有维护者复现/根因确认；仍只能作为反例与风险信号。

### 反例与限制

- issue 仍 open；不能据此判定 auto mode 的正式规则或普遍失效率。
- 报告还提到 session 可能实际运行于 bypass-permissions mode，状态与用户设置存在疑问；这削弱了对具体 classifier 归因的确定性，但不削弱“授权作用域漂移”作为需要单独测试的风险。
- 该报告与 Source 3 共同提示：升档机制不仅要有“危险动作识别”，还要有“授权不可继承/不可泛化”的边界。

---

## Source 5 · GitHub Spec Kit 官方流程：歧义、reviewer-owned checklist、收敛缺口决定是否继续

- URL：https://github.github.io/spec-kit/reference/agentic-sdd.html
- URL：https://github.github.io/spec-kit/quickstart.html
- 访问日期：2026-09-27
- 页面发布日期：文档未标单页发布日期；页面为 GitHub Spec Kit 当前官方文档
- 来源类型：官方产品文档
- P 层级：**P-existence + P-mechanism**；流程文档不证明团队实际采用率或质量效果

### 逐字摘录

1. clarify 不是固定阶段必经门，而是按歧义需要追加：

> “only `/speckit.specify` is strictly required before `/speckit.plan`. The clarify, checklist, and analyze commands are quality gates you add for anything with meaningful ambiguity.”

> “Asks up to five targeted questions about underspecified areas of the current spec and encodes your answers back into `spec.md`.”

> “Run it as many times as needed before planning, each time tackling a different area.”

2. checklist 的审批权属于 reviewer，不属于 agent 自我勾选：

> “Custom checklists generated by this command are reviewer-owned requirements-quality review artifacts.”

> “An agent may help evaluate them when explicitly asked, but implementation must not silently self-approve them.”

> “`[x]` means the reviewer determined the requirements-quality criterion is satisfied; it does not mean implementation work is complete.”

3. implement 在未审完的 checklist 上先停下询问：

> “`/speckit.implement` counts checked and unchecked items and asks before proceeding when any are unchecked, but it must not change checklist markers.”

4. converge 把“是否达到完成”做成可重复的外部检查：

> “Converged — no gaps found.”

> “Tasks appended — gaps found. Converge appends them as new tasks under a Convergence section in `tasks.md` ... Run `/speckit.implement` again ... then `/speckit.converge` once more.”

5. quickstart 进一步要求每个步骤逐项运行并 review：

> “Invoke each `/speckit-*` skill separately in your agent's chat, one at a time, and review the result before moving to the next step.”

### 最小主张与判读

- **支持的最小主张：** Spec Kit 将人在环放在三类控制点：
  - 关键歧义：clarify，最多五个针对性问题，可多次运行；
  - 需求质量：reviewer-owned checklist，agent 不能静默自批；
  - 完成质量：converge 发现缺口就追加任务，直到无缺口。
- **判据类型：** 歧义、审查状态、外部规格与实现差距；不是危险动作分类，也不是轮数阈值。
- **升档/降档含义：** 如果没有 meaningful ambiguity，可跳过 clarify；如果 checklist 有未勾选项，implement 不能默默继续；如果 converge 发现 gap，自动化回到 implement，而不是宣布完成。

### 反例与限制

- “Run it as many times as needed” 与 “repeat until Converged” 是流程循环，不是通用 N 轮规则；它们没有给出跨项目最大次数或质量概率。
- 文档把 checklist 的 reviewer ownership 写得很清楚，但没有证明 reviewer 实际逐条看过，也没有给出漏检率/返工率。
- 该机制主要防“需求/实现不一致”和“未审需求继续编码”，不能单独替代命令级安全边界。

---

## Source 6 · Fission-AI OpenSpec：关键歧义才问，但项目 issue 暴露阈值与门动作必须一致

- URL（官方 OPSX 文档）：https://raw.githubusercontent.com/Fission-AI/OpenSpec/main/docs/opsx.md
- URL（v1.13.2 release API）：https://api.github.com/repos/Fission-AI/OpenSpec/releases/tags/v1.13.2
- URL（官方 issue API）：https://api.github.com/repos/Fission-AI/OpenSpec/issues/1837
- 发行日期：v1.13.2 于 2026-09-23 发布
- issue #1837 创建 2026-09-10、关闭 2026-09-22
- 访问日期：2026-09-27
- 来源类型：官方产品文档、官方 release notes、维护仓库 issue
- P 层级：**P-existence + P-mechanism**；issue 提供真实工程修正记录，但不提供用户效果统计

### 逐字摘录：机制

1. OPSX 不以固定阶段作为人工门：

> “It's a **fluid, iterative workflow** for OpenSpec changes. No more rigid phases — just actions you can take anytime.”

> “Dependencies are enablers — they show what's possible, not what's required next.”

2. v1.13.2 把人工询问收窄到关键歧义：

> “Approval prompts - Fast-forward asks for clarification only when context is critically unclear, and onboarding asks you to approve the task breakdown before saving it.”

3. OpenSpec 文档允许实现中回改产物：

> “During `/opsx:apply`, if something's wrong — fix the artifact, then continue.”

### 逐字摘录：反例/修正

issue #1837 由维护者记录了模板中三个互相冲突的阈值/动作：

> “three different thresholds for when to ask”

原有文字同时出现：

> “If an artifact requires user input (unclear context): Ask the user to clarify”

> “If context is **critically** unclear, ask the user - but prefer making reasonable decisions to keep momentum”

> “IMPORTANT: Do NOT proceed without understanding what the user wants to build.”

同一 issue 还指出 onboarding 的暂停点门错了：

> “The question asks about the next phase; the gated action is saving `tasks.md`.”

### 最小主张与判读

- **支持的最小主张：** OpenSpec 的公开设计把人工介入从固定阶段门收缩为“关键歧义 + 保存任务分解前的确认”；其 OPSX 允许任意方向迭代，而不是强制线性阶段。
- **判据类型：** 歧义严重度（critically unclear）和即将写入的动作（保存 task breakdown）；不是轮次、质量置信度或动作危险度。
- **工程质量教训：** “是否问人”与“暂停后究竟阻止哪个动作”必须在同一模板/技能的所有 delivery surface 保持一致。issue 说明如果一个地方说 unclear 就问、另一个地方说 critically unclear 才问，agent 得到的升档规则不可判定；如果问题问的是进入 implementation，却把 gate 放在写 `tasks.md`，审批对象也会错位。
- **P-outcome 边界：** issue 证明维护者发现并修复了规则矛盾（工程过程结果），不能证明修复后用户质量提升。

### 负结论

- 在官方 docs/ release notes/ issue 中未找到“第 N 次澄清后自动批准”或“跑 N 轮后必须人看”的规则。
- “critically unclear”仍是自然语言阈值；OpenSpec 没有在这些材料中公开可计算的歧义评分、置信度阈值或校准集。
- `agree before you build` 的产品口号不能自动推出每个 artifact 都必须同步人工批准；v1.13.2 明确只在 task breakdown 保存前要求 approval，并将 fast-forward clarification 限于关键歧义。

---

## Source 7 · LangChain 官方 HITL middleware：工具级 policy + interrupt + approve/edit/reject + 可恢复状态

- URL（官方文档固定 commit）：https://raw.githubusercontent.com/langchain-ai/docs/933a2f9217f6293a54fa59d40ce69b619aaa1172/src/oss/langchain/human-in-the-loop.mdx
- 页面入口：https://docs.langchain.com/oss/python/langchain/human-in-the-loop
- 文档 commit：`933a2f9217f6293a54fa59d40ce69b619aaa1172`
- 访问日期：2026-09-27
- 来源类型：官方产品文档/源码仓库文档
- P 层级：**P-existence + P-mechanism**；文档样例不是真实运行效果

### 逐字摘录

1. 工具调用按 policy 决定是否暂停：

> “It does this by checking each tool call against a configurable policy. If intervention is needed, the middleware issues an `interrupt` that halts execution and wait[s] for a decision.”

2. 人的三种动作：

> “the action can be approved as-is (`approve`), modified before running (`edit`), or rejected with feedback (`reject`).”

3. 工具级 allow/interrupt：

> `"write_file": True,  # All decisions (approve, edit, reject) allowed`
>
> `"execute_sql": {"allowed_decisions": ["approve", "reject"]},  # No editing allowed`
>
> `"read_data": False,  # Safe operation, no approval needed`

4. 中断后的持久化恢复：

> “The graph state is saved using LangGraph's persistence layer, so execution can pause safely and resume later.”

> “You must provide a checkpointer to persist the graph state across interrupts.”

5. 生命周期位置：

> “The middleware defines an `after_model` hook that runs after the model generates a response but before any tool calls are executed.”

### 最小主张与判读

- **支持的最小主张：** LangChain 提供了一个可配置、工具名粒度的人工门：安全操作可 `False` 自动执行；高风险/需审操作设 `True` 或限定允许决策；模型提出 tool call 后、真正执行前 interrupt；人可批准、编辑或拒绝，拒绝反馈回对话；用 checkpointer/thread ID 恢复。
- **判据类型：** 动作类别（tool name）和每种动作允许的人决定类型；不是固定轮次，也没有内置风险分数。
- **可逆性对应：** `edit` 提供“执行前修改”能力，且文档警告大幅修改参数可能导致模型重新规划、多次执行或意外动作；这是一种操作风险提示，不是通用可逆性计算器。
- **人是否必须看：** 由 `interrupt_on` policy 决定；不是由模型自行声称完成决定。该机制把“何时人看”放在 tool call 执行前，而非每轮结束。

### 反例与限制

- 文档示例把 `write_file` 全部 interrupt、`read_data` 全部 auto-approve；这只是配置例子，不证明所有写文件都高风险、所有读取都安全。
- 没有风险/金额/不可逆性自动推断：若调用者把危险工具设为 `False`，文档机制本身不会替配置者补上风险模型。
- 多个同时暂停的 action 需要按出现顺序分别决定；这增加了人工界面的实现要求，也没有给出拒绝预算或超时策略。

---

## Source 8 · Microsoft Learn 教学模型：置信度必须经过校准，并与风险/影响/不可逆性/歧义组合

- URL：https://learn.microsoft.com/en-us/training/modules/aaai-design-human-in-loop-approval-workflows/2-design-confidence-threshold-escalation
- 页面标题：`Design confidence-based escalation for human intervention`
- 发布日期：页面未显示单页发布日期；观测日期 2026-09-27
- 来源类型：Microsoft Learn 官方培训内容；含 Adventure Works 教学场景与示例 Python
- P 层级：**P-existence + P-mechanism（教学设计示例）**；**P-outcome=无**，不能视为 Microsoft Foundry 默认策略或真实生产指标

### 逐字摘录

1. 组合触发器：

> “Effective escalation combines multiple signals—model confidence, financial impact, policy exceptions, and request ambiguity—so human review activates only when it's genuinely needed.”

2. 置信度不是单独充分条件：

> “confidence scores alone are insufficient because they don't account for the stakes of the decision”

3. 可逆性/影响分层：

> “High-impact actions have different confidence requirements than low-impact actions.”

> “high impact (> 200 USD, affects > 10 customers, or irreversible actions like account closures).”

4. 政策例外和歧义无条件升级：

> “Policy exception requirements trigger escalation regardless of confidence.”

> “Ambiguity requires clarification, either from the customer or from a human agent who can apply judgment.”

5. 教学模型给出的风险阈值：

> “Low-risk decisions ... require calibrated confidence > 0.60 to proceed autonomously.”

> “Moderate-risk decisions ... require calibrated confidence > 0.75.”

> “High-risk decisions ... require calibrated confidence > 0.88.”

> “Policy exceptions always escalate regardless of confidence.”

6. 原始置信度先校准：

> “Using raw confidence scores for escalation decisions creates either excessive escalation ... or insufficient oversight.”

> “Adventure Works builds a calibration dataset by collecting 2,000 agent decisions with their reported confidence scores and having human experts label each decision as correct or incorrect.”

7. 代码判定顺序：

> “Always escalate policy exceptions”
>
> “Always escalate ambiguous situations”
>
> “Check confidence against risk-appropriate threshold”
>
> “Confidence sufficient for autonomous execution”

### 最小主张与判读

- **支持的最小主张：** Microsoft 的官方教学材料给出一个完整的可操作设计模板：政策例外/歧义先升级；否则按金额、影响人数、不可逆性设风险级；再将校准后的置信度与风险级阈值比较。
- **判据类型：** 风险、影响范围、可逆性、政策例外、歧义、质量置信度校准；明确不是轮次。
- **研究价值：** 它填补了现有 coding-agent 一手材料里“置信度如何接到人工门”的概念空白，但只能作为**教学设计宣称**。这是候选的可测试设计，不是行业已采用的阈值，也不是对 coding-agent 质量的实证。
- **可操作伪代码：** `policy_exception -> escalate`; `ambiguity -> escalate`; `risk_level -> calibrated_confidence threshold`; 达到阈值才自动执行。

### 反例与限制

- Adventure Works 是教学场景；页面没有证明 0.60/0.75/0.88 是 Microsoft Foundry 的默认值、推荐通用值或经过跨任务验证的值。
- 模型自报置信度可能失准；材料自己承认需要 2,000 条带人工标签的数据校准，并需要季度再校准。没有校准数据，直接使用阈值会制造虚假的精确感。
- 该材料没有固定轮次阈值，也没有 coding-agent 的代码测试、提交、推送、沙箱动作分类；不能把它直接移植成 Claude/Codex policy。

---

## P-existence / P-mechanism / P-outcome 分层矩阵

| 机制/宣称 | P-existence | P-mechanism | P-outcome | 可否推出通用规则 |
|---|---|---|---|---|
| Codex `Allow/Prompt/Forbidden`、危险命令/沙箱/信任/policy | 官方源码固定 commit | ✅ | 无部署效果数据 | 可推出“动作/环境驱动的机制存在”，不可推出安全效果 |
| Codex 重复拒绝后人工审批 | 官方 PR 存在 | ✅ 但为未合并提案 | 无 | 可作为状态机候选，不能写成现行产品行为 |
| Claude auto mode 无软边界人工 fallback（issue #67519） | 官方 issue 存在 | 由报告描述，非源码确认 | 单用户真实报告 | 只能作反例/缺口 |
| Claude auto mode 误把窄授权扩成 push-to-main（issue #95749） | 官方 issue 存在 | 用户配置与观察，根因未确认 | 单用户真实报告 | 只能作授权作用域测试样例 |
| Spec Kit clarify/checklist/converge | 官方文档存在 | ✅ | 无效果指标 | 可作流程机制，不可作质量保证 |
| OpenSpec critically unclear + task breakdown approval | docs/release 存在 | ✅ | issue 证明规则矛盾被修正，不证明效果 | 可作歧义门设计样例，需验证阈值一致性 |
| LangChain `interrupt_on` + approve/edit/reject | 官方文档存在 | ✅ | 无生产指标 | 可作工具级 HITL 原语，不自动提供风险分类 |
| Microsoft 风险级 × 校准置信度阈值 | 官方培训教学存在 | ✅（示例代码/场景） | 无真实产品结果 | 仅候选设计，不得写成默认政策 |

---

## 反例与负结论总表

1. **没有找到通用固定轮次阈值。** 搜索范围：Anthropic Claude Code security/auto mode/goal 文档与公开 issue，OpenAI Codex auto-review alignment、Codex 源码/PR/issues，GitHub Spec Kit agentic docs，Fission-AI OpenSpec docs/releases/issues，LangChain HITL docs，Microsoft Learn escalation training；检索词包括 `round/turn/iteration`, `approval/escalate/deny`, `risk/reversible/ambiguity/confidence`, `human in the loop`。出现的数字是单个机制的资源/拒绝预算（例如已有 Claude 3/20）、流程问题数上限（Spec Kit clarify 最多五问）或教学置信度阈值，不是跨产品自主度等级。
2. **没有找到 coding-agent 公开的、经校准的质量置信度自动放行规则。** 现有材料能证明动作安全门、测试/checklist/converge 和独立 grader 的存在，但没有“测试通过率/评估置信度达到 X 后可跳过人工”的跨产品政策。
3. **没有找到公开的通用可逆性评分器。** Codex/Claude/LangChain 通过动作类别、沙箱、网络、目标分支、工具配置等近似表达可逆性/影响；Microsoft 教学模型把不可逆性列为高风险信号，但没有 coding-agent 生产实现。
4. **拒绝次数可作为熔断预算，但拒绝不是自主度成熟度。** Claude 的 3 连拒/20 总拒和 Codex PR 的 repeated denials 都是安全停止/升级控制，不代表 agent 已达到某个“成熟等级”。
5. **“拒绝”与“升级给人”必须分开建模。** Claude #67519 的真实报告显示，分类器正确或谨慎地拒绝并不等于人能接手；若没有 soft-boundary fallback，系统会从“人决定”退化成“无人能决定”。
6. **授权作用域必须是动作级、目标级、时间级。** Claude #95749 报告的 edit→commit→push 继承风险，以及 OpenAI Codex #32007 报告的“用户明确授权后仍被强策略拒绝”，分别说明过度继承和过度拒绝两类反例；两条都是单次报告，不可外推发生率。
7. **自然语言阈值本身会漂移。** OpenSpec #1837 同时出现 `unclear`、`critically unclear` 和“不要在理解前继续”三种冲突门槛，且 pause 问题与实际 gated action 不一致。任何实践规程都应要求：触发词唯一、被阻止动作明确、同一规则在 skill/body/release surfaces 一致。
8. **官方设计宣称不等于真实效果。** Spec Kit/OpenSpec/LangChain/Microsoft 文档主要证明机制存在；Claude/Codex issues 提供真实运行反例但缺少受控复现；本档案没有找到能证明“减少人工时间、提升正确率或减少事故”的跨机构 P-outcome。

## 可迁移的“判据候选”（解释/建议，不是研究已证实的行业规范）

以下是把一手材料压缩成可测试控制面时可以采用的判据候选；它们不是“通用 N 轮阈值”：

1. **动作门（每次工具调用前）：**
   - `hard deny`：明确禁止动作、危险 shell/解释器、不可接受的权限边界、绝对政策例外。
   - `human approve`：越过沙箱/网络/外部发布边界、default branch push、无法确认目标/范围、策略要求 prompt。
   - `auto`：在受限沙箱内、非危险、工具 policy 明确允许、无未解决歧义的动作。
2. **歧义门（写入/规划前）：** 若存在多个合理解释且错误选择会改变范围、目标、金额、外部影响或验收定义，先问人；不要用“模型有 0.8 信心”覆盖关键歧义。
3. **授权作用域门：** edit、commit、push、PR、merge、release 分开授权；授权要绑定目标（仓库/分支/工具）、动作和有效期/一次性，而不是从历史对话模糊继承。
4. **拒绝预算门：** 把连续拒绝和累计拒绝当作安全熔断；触发后只能选择“人工审批/安全替代/硬停止”，不得无限换措辞重试。预算数字只能来自具体 runtime policy，不能抽象成行业 N。
5. **质量门：** 用独立、可核查的验收（测试、端到端场景、规格/任务收敛、独立 evaluator）决定是否继续；动作获准不代表质量已达标。若质量判定与干活模型同源，标为弱证据并保留人工抽查。
6. **风险/置信度门（若要采用）：** 先定义风险级（影响范围、金额、不可逆性、外部发布），再使用经过历史标签校准的置信度；政策例外/关键歧义无条件升级。没有校准集时，不使用精确小数阈值制造假确定性。
7. **状态恢复门：** 人工 interrupt 必须持久化 action、理由、decision source 和恢复指针；父 agent/子 agent 的审批可见性必须可验证，否则会出现 Codex #45167 所示的“主线程看不到拒绝，子 agent 又不能接收审批”死路。

## 仍然空白

- **质量置信度如何生产化：** 没有 coding-agent 一手来源给出可复现的质量置信度校准曲线、样本量、漂移检测与自动放行结果。
- **可逆性如何定义和测量：** 源码通常以动作/环境类别近似，缺少统一的“可回滚成本、外部不可逆影响、补救时间”计算。
- **风险与动作类别的组合策略：** 已看到 Codex 的动作/沙箱 policy 与 Microsoft 的风险/置信度教学模型，但没有真实 coding-agent 公开说明二者怎样组合成一个稳定决策器。
- **拒绝预算如何因上下文变化调整：** Claude 3/20 是固定产品阈值，Codex PR 保留 runtime 阈值；没有证据表明预算会按风险、任务价值或用户在场状态自适应。
- **升级后的人工界面效果：** OpenAI PR 明确 app-side presentation 仍需改；Claude issue 暴露用户在场却无 fallback；没有跨产品数据说明“升级给人”是否真的可操作、多久响应、是否被机械批准。
- **子 agent 审批传播：** Codex #45167 的第一人称报告指出 controlled sub-agent 的拒绝无法从 parent `/approve` 处理；尚无公开一手修复机制或成功运行证据。
- **授权新鲜度/继承：** Claude #95749 提供了“窄授权被误当成广授权”的反例，但公开 policy 尚未给出通用的授权 token scope、expiry、target binding 规范。
- **行为面验证：** checklist/converge 和测试门能验证部分需求，但没有机制证明测试覆盖了用户未明说、体验或安全意图；既有 evidence-c 已指出该空白，本档案未找到可关闭它的新一手证据。

## 与既有判读的关系

- **一致：** 加强了 evidence-c/`digested/03-构件.md` 的判断：升档主要是事件、动作类别、歧义、风险与拒绝熔断驱动，而不是固定轮次；位置 taxonomy 不能当成熟度或质量等级。
- **新增：** Codex 源码给出最接近“按动作/环境自动判定”的实现锚点；OpenAI PR 给出“重复拒绝 → 人工审批”的状态机候选；Spec Kit 文档给出 reviewer-owned checklist 和 converge 反复补任务；LangChain 给出可恢复的工具级 interrupt；Microsoft 教学模型把风险、不可逆性和校准置信度拼成候选决策树。
- **反向修正：** 不应把“人工同步审批退出调度回路”写成无条件事实。Claude/Codex issue 显示，在真实运行中，越界动作、授权范围漂移、子 agent 审批传播和软边界 fallback 仍会决定人是否真的能介入；产品文档中的“可自动”不等于用户可操作的“可升级”。

## 负结论：本轮没有取得/不能据此推出

- 未取得 Anthropic 内部 auto-mode classifier 的完整公开源码或可复现策略训练/评估集。
- 未取得 OpenAI auto-review Guardian 的完整生产策略源码；Codex 开源 `exec_policy.rs` 是命令/沙箱 policy，不等同于 alignment blog 所述的 reviewer 模型。
- 未找到 OpenSpec/Spec Kit/LangChain 的真实部署统计，不能用文档机制证明效果。
- 未找到任何官方来源支持“连续 N 轮后必须人看”作为跨 runtime 通用规则。
- 未找到任何来源支持“高置信度即可绕过所有人工检查”；相反 Microsoft 教学材料明确说置信度需校准，政策例外和歧义仍无条件升级。
- 不把 Claude/Codex issue 的单用户报告写成安全事故率、产品普遍缺陷或因果证明；它们只进入反例、测试样例和开放问题。
