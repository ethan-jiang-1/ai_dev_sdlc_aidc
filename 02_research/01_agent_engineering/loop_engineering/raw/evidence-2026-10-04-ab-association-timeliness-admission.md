---
type: evidence_archive
collected_by: 委派研究子代理（T2 路 · 反馈路径问题·关联时效与准入）
collected_at: 2026-10-04
serves: 计划中的 digested/09-feedback-harness-interface.md ＋ 实践层准入表（主代理撰写；本档只供证据底座）
status: 已有档案深挖（P/F/W 三档逐条抽取「关联与时效」机制）＋ LangGraph persistence 补源（直抓被网络策略拦截，登记待核）
quality_bar: 引句逐字，双重锚＝本仓库档案行锚＋原始 URL/commit；原观测日期与本轮复核观测日期分开记；本轮无新增一手抓取（补源尝试失败已登记）；单源标单源；不把机制存在写成效果已证
---

# Evidence AB：反馈的关联、时效与准入（T2，观测 2026-10-04）

> **研究问题**：产品/框架如何把一条检查结果绑定到「当前目标 × 工件版本 × 判据版本 × 环境」？迟到结果、旧版结果、重复结果各自有哪些显式处置机制？
>
> **方法**：本档不新增一手来源，是对计划指定档案（evidence-p / evidence-w / evidence-f）的逐条深挖抽取；每条引句保持逐字，锚到本仓库档案行＋原始 URL。补源目标 LangGraph persistence 页面（任务指定）直抓失败，见 §三。

## 零、本轮复核口径

- 观测日期（本轮复核）：**2026-10-04**；各引句的**原始观测日期**以来源档案为准（evidence-p＝2026-09-28，evidence-f＝2026-09-27，evidence-w＝2026-09-30）。
- 引句均逐字转引自本仓库回源档案；档案本身为逐字摘录（evidence-p Source 1 标注「★主代理全文复核」）。转引不新增证据强度，强度继承原档标注。
- 术语口径：**绑定对象**指机制显式写入的字段/键（会话、环境、树哈希、工具名、事件类型等）；**准入**指一条结果/事件有没有资格开始或进入下一轮工作。

---

## 一、关联机制清单（机制 → 绑定对象 → 锚 → 证据强度）

### M1 · 签名回执绑定工作树哈希（isitdone）

- **绑定对象**：检查结果 ↔ **工作树内容哈希**（既不是 commit、不是 CI、也不是会话）。
- **逐字**（[evidence-p:24](evidence-2026-09-28-p-practitioner-gates.md#L24)；原文 https://dev.to/raimondasl/69-of-my-coding-agents-done-claims-werent-here-is-the-gate-i-put-in-front-of-them-lho ）：
  > "Every pass writes a small signed receipt bound to the hash of the working tree… change one file and the receipt reads STALE."
- **逐字（时点绑定）**（[evidence-p:20](evidence-2026-09-28-p-practitioner-gates.md#L20)）：
  > "**At the moment of the claim.** Not at commit time, not in CI… / **On the exact working tree.**… / **With the repository's own commands.** `npm test`, `pytest`, `cargo test`… **No second opinion from a model.** / **Unable to loop forever.**"
- **强度**：实践者一手（dev.to 长文＋工具与语料公开；原档强度 high）。
- **时效语义**：工作树任一文件改变 → 回执转 STALE。注意触发条件是**树内容哈希改变**（工作树粒度），不是「任何 commit 改变一律使所有证据失效」；原档未记录 commit 粒度的失效规则。

### M2 · 结果缓存按树哈希键（isitdone）

- **绑定对象**：通过结果 ↔ 树哈希（同哈希树不重跑）。
- **逐字**（[evidence-p:22](evidence-2026-09-28-p-practitioner-gates.md#L22)）：
  > "Fast checks (typecheck, lint) run on every stop. The full suite runs only when the final message contains a completion claim… A passing tree is cached by a hash of the working tree."
- **强度**：实践者一手。
- **关联语义**：这同时是**重复结果的显式处置**（同一工作树状态的重复完成宣告走缓存，不重跑全量），以及**触发条件绑定**（全量套件只在最终消息含完成宣告时运行——结果资格绑到"声称时刻"这一事件）。

### M3 · 测试输出持久化到日志，防重复执行（Ian Johnson 实战）

- **绑定对象**：检查结果 ↔ 日志文件（会话外的持久位置，替代"会上滚屏记忆"）。
- **逐字**（[evidence-p:33](evidence-2026-09-28-p-practitioner-gates.md#L33)；原文 https://dev.to/tacoda/what-breaks-when-you-skip-the-harness-3237 ）：
  > "The agent kept running the tests, watching them go red, scrolling up to find the failure, and then running the tests again because it had already lost the output. … I had Claude tee the test command to a log file. After that it read the log instead of re-running."
- **强度**：实践者一手定性（原档 medium-high）。
- **关联语义**：失败的根因是结果与"哪一次运行"的绑定缺失（输出滚丢）→ 处置是把结果落到带命令的日志，使旧结果可复读、不重跑。**显式工程建议＋第一人称战报，非产品机制。**

### M4 · 事件排队字段 `processed_at`（Claude Managed Agents sessions）

- **绑定对象**：每条持久化事件 ↔ 处理时间戳＋所属 session 的事件队列；"已提交"与"已执行"由该字段区分。
- **逐字**（[evidence-w:142](evidence-2026-09-30-w-ladder-runtime-detail.md#L142)；原文 https://platform.claude.com/docs/en/managed-agents/events-and-streaming ）：
  > "Every persisted event includes a `processed_at` timestamp set when the event finishes processing. On events you send, `processed_at` is null while the event is still queued behind earlier events."
- **强度**：官方文档（beta header `managed-agents-2026-04-01`）。
- **时效语义**：事件可以迟到（排队），平台用显式字段暴露"尚未处理"状态——**迟到结果的显式处置＝可观测的排队态，而不是静默丢弃**。

### M5 · 会话三元绑定：agent × environment × 会话历史（Claude Managed Agents sessions）

- **绑定对象**：一条会话的运行结果 ↔ `agent` ID＋`environment_id`＋server-side 会话历史。
- **逐字**（[evidence-w:110](evidence-2026-09-30-w-ladder-runtime-detail.md#L110)；原文 https://platform.claude.com/docs/en/managed-agents/sessions ）：
  > "A session is an agent instance within an environment. Each session references an agent and an environment … and maintains conversation history across multiple interactions."
- **逐字**（[evidence-w:156](evidence-2026-09-30-w-ladder-runtime-detail.md#L156)）：
  > "Event history is persisted server-side and can be fetched in full."
- **强度**：官方文档。
- **关联语义**：结果归属的最小单位是 session（含 agent 与 environment 两个绑定维度）；环境与会话历史**独立持久化**（原档机制卡）。未见工件版本号字段。

### M6 · 中断状态按 checkpointer/thread 恢复（LangChain HITL middleware）

- **绑定对象**：暂停时的图状态 ↔ checkpointer（thread ID 维度）。
- **逐字**（[evidence-f:406-408](evidence-2026-09-27-f-autonomy-gates.md#L406-L408)；原文 https://raw.githubusercontent.com/langchain-ai/docs/933a2f9217f6293a54fa59d40ce69b619aaa1172/src/oss/langgraph/human-in-the-loop.mdx ）：
  > "The graph state is saved using LangGraph's persistence layer, so execution can pause safely and resume later."
  > "You must provide a checkpointer to persist the graph state across interrupts."
- **强度**：官方文档固定 commit。
- **关联语义**：interrupt 产生的人工决定（approve/edit/reject）要能回到下一次执行，前提是状态按 thread 持久化；**绑定粒度是 thread/checkpointer，未见 commit 或环境字段**。

### M7 · 判据（rubric）作为可跨会话复用的绑定对象（Claude Managed Agents outcomes）

- **绑定对象**：评估判据 ↔ `user.define_outcome` 事件（inline）或 Files API 对象（跨 session 复用）；grader 反馈 ↔ 同一 session 的下一轮。
- **逐字**（[evidence-w:230](evidence-2026-09-30-w-ladder-runtime-detail.md#L230)；原文 https://platform.claude.com/docs/en/managed-agents/define-outcomes ）：
  > "Pass the rubric as inline text on `user.define_outcome` … or upload it through the Files API for reuse across sessions."
- **逐字（反馈到达下一轮的通路）**（[evidence-w:226](evidence-2026-09-30-w-ladder-runtime-detail.md#L226)）：
  > "The grader returns an explanation summarizing which criteria passed or failed, or confirming that the artifact satisfies the rubric. That feedback is handed back to the agent for the next iteration."
- **强度**：官方文档。
- **关联语义**：这是全部三个档案中最接近「判据版本」的机制——rubric 可作为持久对象复用，**但公开文档未见版本号字段，也未见「判据更新后旧结果是否失效」的规则**（负结论，见 §四）。

### M8 · 授权结果按来源归因字段分离（OpenAI Codex PR #20672，未合并）

- **绑定对象**：一次审批决定 ↔ `source` 字段（机器拒绝 vs 人决定分账）。
- **逐字**（[evidence-f:134](evidence-2026-09-27-f-autonomy-gates.md#L134)；原文 https://github.com/openai/codex/pull/20672 ）：
  > "preserve approval attribution across escalation: the breaker-triggering Auto-review denial is still recorded as `source=AutomatedReviewer`; the final manual decision is recorded separately as `source=User`."
- **强度**：官方仓库 PR（**未合并**，不能写成已发布行为）。
- **关联语义**：把「哪一方产生的检查结果」做成持久归因字段，供升级链路区分机器判定与人工判定——关联的对象是**决定来源**，不是工件版本。

### M9 · 可复用批准的边界约束（OpenAI Codex exec_policy.rs 源码）

- **绑定对象**：一次批准的复用范围 ↔ 命令前缀规则＋模型是否遵守前缀规则＋逐 segment 校验。
- **逐字**（[evidence-f:88](evidence-2026-09-27-f-autonomy-gates.md#L88)；源码 https://raw.githubusercontent.com/openai/codex/1f4c47343a1bff2d8cddc429c5d39503fb5a6c30/codex-rs/core/src/exec_policy.rs ）：
  > "Avoid reusable approvals when this model does not honor prefix rules."
- **逐字**（[evidence-f:84](evidence-2026-09-27-f-autonomy-gates.md#L84)）：
  > "Bypass sandbox only when every parsed command segment is explicitly allowed by execpolicy."
- **强度**：官方源码固定 commit（P-existence＋P-mechanism）。
- **关联语义**：重复发生的同类动作**不自动继承**上一次的放行——复用被显式约束；这是对「重复结果/重复动作准入」的产品级处置（约束粒度是命令，不是检查结果）。

### M10 · 触发与资源的绑定字段（Cursor Automations / Claude scheduled deployments）

- **绑定对象**：一次 run ↔ 触发器类型（cron/webhook/PR 事件）＋repo 绑定＋initial event；deployment 对象带 `last_run_at` / `upcoming_runs_at`。
- **逐字**（[evidence-w:73](evidence-2026-09-30-w-ladder-runtime-detail.md#L73)；原文 https://cursor.com/docs/cloud-agent/automations ）：
  > "For any path: 1. Choose a trigger, e.g. every hour or when a pull request is opened. 2. Write a prompt with instructions for the automation. … 4. Choose whether the automation needs a repository, multiple repositories, or no repository at all."
- **逐字**（[evidence-w:293](evidence-2026-09-30-w-ladder-runtime-detail.md#L293)；原文 https://platform.claude.com/docs/en/managed-agents/scheduled-deployments ）：
  > "Deployments also require at least one initial event, a `user.message` or `user.define_outcome`, that starts each session's work."
- **逐字**（[evidence-w:316](evidence-2026-09-30-w-ladder-runtime-detail.md#L316)）：
  > "The response includes a deployment object with a populated `schedule.upcoming_runs_at` with the next upcoming fire times, to confirm your schedule was set correctly."
- **强度**：官方文档（两家分别计）。
- **关联语义**：跨会话 run 的"结果属于哪次运行"由触发器＋repo＋initial event 三者界定；时效字段只有运行时刻（last/upcoming），**未见 run 之间的结果继承或失效规则**。

---

## 二、三类异常的显式处置（或登记「未见显式处置」）

### 2.1 迟到结果（结果产生晚于其对应的状态/轮次）

| 机制 | 处置 | 锚 | 强度 |
|---|---|---|---|
| `processed_at` 排队字段（M4） | 迟到事件不丢弃，以 `processed_at=null` 暴露"仍在排队"；不能把已提交当已执行 | [evidence-w:142](evidence-2026-09-30-w-ladder-runtime-detail.md#L142)、失败模式归纳 [evidence-w:167](evidence-2026-09-30-w-ladder-runtime-detail.md#L167) | 官方文档 |
| 在途请求有界超出（预算场景） | cap 跨越瞬间在途的请求**仍会完成**，最终成本可小幅越过预算——迟到结果被显式接受并计入 | [evidence-w:264](evidence-2026-09-30-w-ladder-runtime-detail.md#L264)："The request in flight when the cap is crossed still finishes, so the final list cost can land a fraction past the budget." | 官方文档 |
| `rescheduling` 自动重试态 | transient error 不终局，进入自动重试状态 | [evidence-w:150](evidence-2026-09-30-w-ladder-runtime-detail.md#L150)："`rescheduling` | Transient error occurred, retrying automatically." | 官方文档 |
| 计划触发允许延迟、不提前 | cron 触发的时效语义写明"可能延迟但不会早于指定时间" | [evidence-w:77](evidence-2026-09-30-w-ladder-runtime-detail.md#L77)："Scheduled triggers may run with a delay but will not start before the indicated time." | 官方文档 |
| 输出滚丢→日志复读（M3） | 实战层迟到/丢失的处置＝持久日志，读旧结果代替重跑 | [evidence-p:33](evidence-2026-09-28-p-practitioner-gates.md#L33) | 实践者一手（显式工程建议，非产品机制） |

### 2.2 旧版结果（结果对应的状态已被后续改动取代）

| 机制 | 处置 | 锚 | 强度 |
|---|---|---|---|
| 回执 STALE（M1） | 树哈希不匹配 → 回执读作 STALE；触发条件是**工作树任一文件改变**（工作树粒度，非"任何 commit 一律全失效"） | [evidence-p:24](evidence-2026-09-28-p-practitioner-gates.md#L24) | 实践者一手 |
| 授权不随时间沉淀（用户主张） | 一次 push 授权不应成为后续 push 的常驻授权——**这是 issue 中的用户主张/诉求，非已实现机制** | [evidence-f:242](evidence-2026-09-27-f-autonomy-gates.md#L242)："Authorization for one push must not become standing authorization for later pushes."（[issue #95749](https://github.com/anthropics/claude-code/issues/95749)，单用户报告） | 用户报告 |
| **未见显式处置** | 检索范围内，**没有任何产品文档给出「工件/判据更新后，旧检查结果按什么规则批量失效」的机制**；最接近的只有 isitdone 的树哈希回执（实践者工具，非平台机制）与 Codex 的批准复用约束（命令粒度，M9） | 本档 §四 负结论 1 | — |

### 2.3 重复结果（同一状态/同一动作的重复检查、重复宣告）

| 机制 | 处置 | 锚 | 强度 |
|---|---|---|---|
| 树哈希结果缓存（M2） | 同一哈希的通过树直接复用缓存判定，不重跑全量 | [evidence-p:22](evidence-2026-09-28-p-practitioner-gates.md#L22) | 实践者一手 |
| 日志复读代替重跑（M3） | 会话失忆导致的重复执行，用 tee 日志打断"再跑一遍"循环 | [evidence-p:33](evidence-2026-09-28-p-practitioner-gates.md#L33) | 实践者一手（显式工程建议，非产品机制） |
| 拒绝熔断计数＋重置（M8 相关状态机） | 重复**拒绝**（不是重复通过）达阈值触发 breaker；人工决定后重置计数——重复事件以计数＋重置显式管理 | [evidence-f:136](evidence-2026-09-27-f-autonomy-gates.md#L136)："reset the Auto-review denial breaker after the manual approval flow resolves"（PR 未合并） | 官方仓库 PR（未合并） |
| **未见显式处置** | 重复**通过**结果的平台级去重（如"同输入同判据的结果直接复用"）在检索范围内未见产品文档显式描述；仅 isitdone 以树哈希缓存实现（实践者工具） | 本档 §四 负结论 2 | — |

---

## 三、补源失败登记（LangGraph persistence，待核）

- **任务指定补源**：https://docs.langchain.com/oss/python/langgraph/persistence —— 需要逐字记录 checkpoint/thread 机制中「结果属于哪一次运行、恢复后旧状态是否复用」的表述。
- **观测 2026-10-04**：`web_fetch` 对 `docs.langchain.com` 与 `langchain-ai.github.io`、`raw.githubusercontent.com` 均报错 "URL hostname resolves to a non-public IP address"（本会话网络策略拦截，三次尝试、三种域名，非页面不存在）。
- **已获得的最小线索（web_search 摘要级，非逐字，不作为引句证据）**：
  - 官方 docs 源文件存在于固定 commit：[docs/src/oss/langgraph/persistence.mdx @ 933a2f9](https://github.com/langchain-ai/docs/blob/933a2f9217f6293a54fa59d40ce69b619aaa1172/src/oss/langgraph/persistence.mdx)（与 evidence-f Source 7 的 HITL 文档同一 commit）。
  - 旧版概念页镜像线索：[Persistence - LangGraph (mintlify.wiki)](https://mintlify.wiki/langchain-ai/langgraph/guides/persistence)、[Checkpointing (mintlify.wiki)](https://mintlify.wiki/langchain-ai/langgraph/concepts/checkpointing)。
- **待核动作（留给主代理或下一轮）**：换网络环境抓取上述固定 commit 的 `persistence.mdx`，逐字抽取 thread/checkpoint 的归属与恢复语义；在此之前，本主题对「恢复后旧状态是否复用」**只有 M6 的间接证据**（"pause safely and resume later"），**没有逐字引句**。

## 四、负结论与"未见显式处置"清单

1. **旧版结果的批量失效规则未见产品机制。** 检索范围内（P/F/W 三档全部来源），除 isitdone 的树哈希回执（实践者工具）外，没有任何官方文档定义「工件/判据更新后，旧检查结果按什么规则失效或降级」。rubric 可跨会话复用（M7），但无版本字段、无失效条件。
2. **重复通过结果的平台级去重未见显式描述。** 平台侧只有"事件排队/持久化"（M4/M5）与"批准复用约束"（M9，命令粒度）；同输入同判据的结果复用只在实践者层（树哈希缓存、日志复读）出现。
3. **绑定字段里没有工件版本号。** 三档档案中最细的绑定键是：session（agent×environment×历史，M5）、thread/checkpointer（M6）、树哈希（M1/M2）、事件类型＋repo＋initial event（M10）、命令前缀＋segment（M9）。**未见显式 `artifact_version` / `run_id` / `resume_pointer` 命名字段**；task_id/run_id 一类字段仅出现在 issue 报告的诉求层（evidence-f #45167 的 "action/thread ID、parent-child 可见性和恢复指针"，[evidence-f:183](evidence-2026-09-27-f-autonomy-gates.md#L183)——用户报告提出的 P0 机制字段主张，非产品已实现）。
4. **"任何 commit 改变→所有证据失效"没有被任何来源支持。** 实际触发条件各不相同：isitdone 按工作树哈希（任一文件）；Codex 按命令前缀/segment 复用约束；Managed Agents 干脆不做工件级失效，靠 session 边界隔离。准入表不得写普适失效规则。
5. **强度提示**：M8 的 PR 未合并、M9 是固定 commit 源码、M1/M2/M3 是实践者一手——三者都不能互推；三档负结论原文（evidence-f §反例总表、evidence-w §回源纪律）在本轮复核中无一被推翻。

## 五、对准入表材料的齐备性自评（供主代理）

计划完成条件：「准入表每行有触发、机制锚或显式工程建议」。逐行评估：

| 准入表行（建议的行切分） | 触发 | 机制锚/工程建议 | 齐备？ |
|---|---|---|---|
| 结果有资格进入下一轮（反馈回灌通路） | grader 反馈 → 下一轮 | M7（evidence-w:226，官方）＋ evidence-b 既有 back pressure/grader（原档已登记） | ✅ |
| 声称完成时才跑全量门（时点准入） | 最终消息含完成宣告 | M2/M1（evidence-p:20,22，实践者一手＋工具公开） | ✅ |
| 同状态的重复检查准入 | 树哈希相同 | M2 缓存（实践者一手）；平台级去重＝未见（负结论 2 可作为「显式工程建议」行） | ✅（含负结论行） |
| 旧结果准入 | 树哈希改变 → STALE | M1（实践者一手）；平台级＝未见（负结论 1） | ✅（含负结论行） |
| 迟到结果准入 | 事件排队/在途 | M4 `processed_at`、在途 overshoot、`rescheduling`（官方） | ✅ |
| 暂停后新工作的准入 | budget_reached / interrupt | evidence-w:266-268："A session that reaches its budget goes idle with a `stop_reason` of `budget_reached`; it is not terminated, and its history and sandbox are preserved…"／"Any event that would start new work, such as `user.message`, is rejected with a 400 error…"（官方） | ✅ |
| 重复动作的授权准入 | 同类动作再次发生 | M9（源码，固定 commit）；M8 归因（PR 未合并，须标提案） | ✅（M8 标未合并） |
| 跨会话 run 的结果归属 | cron/webhook 触发 | M10（官方）＋ fork PR 失败处置（[evidence-w:83](evidence-2026-09-30-w-ladder-runtime-detail.md#L83)） | ✅ |
| 恢复后旧状态是否复用 | checkpointer/thread 恢复 | **仅 M6 间接证据；LangGraph persistence 逐字缺位** | ⚠️ **缺**——需按 §三 待核动作补抓后才能定稿该行 |
| 判据版本切换后的结果失效 | 判据更新 | **无任何来源**；只能写「显式工程建议」（rubric 版本化＋失效规则需自行设计，标非产品机制） | ⚠️ **缺一手锚**——建议该行只给显式工程建议并如实标注 |

**结论**：10 行中 8 行材料齐备；2 行缺——「恢复后旧状态是否复用」（等 LangGraph persistence 补抓）与「判据版本切换后的失效」（无来源，只能以显式工程建议行落地）。
