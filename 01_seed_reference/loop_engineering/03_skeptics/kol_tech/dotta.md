---
type: kol_evidence
directory: 03_skeptics/kol_tech
observation_date: 2026-10-06
---

# dotta — loop engineering 证据轨迹（2026-06 后，时间正序）


> **背景**：Dotta（化名，真名未公开；自述做 Paperclip 前在 NFT 领域工作）——Paperclip 创建者/联合创始人：开源 agent 任务/编排系统（“human control plane for AI labor”，github.com/paperclipai/paperclip），2026-03 三周内获 3 万 GitHub stars；GitHub cryppadotta、X @dotta。化名身份，公开履历有限。（履历核：ai.engineer 讲者页＋ThursdAI，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察（AIEWF 讲稿）；第九轮（2026-10-07）补全讲内处方面＋done 对象件数勘误（六→八，见下）。
### Dotta（Paperclip 创建者）· AIEWF 2026《What Does Done Even Mean? Agents and Paperclip's Liveness Model》（视频上传在库页实录）

- URL：https://ai.engineer/talks/7P0elyLIxXo-what-does-done-even-mean-agents-paperclips （curl 实取全文）
- 身份：Paperclip（agent 任务协议）创建者——**仅作会议层样本**（机制价值高）。
- **挂钩**：停止条件（正题名级："done"的形式化）＋验证回路。
- 逐字摘录：

> "An agent opens a pull request. It passes the tests. It updates the documentation. It closes the issue and comments, 'Looks done to me.' But is it actually done? … These are fundamentally different operational claims, and most agent systems just flatten it to a single green check mark."

> "Programming is solved, and agents can now produce more code and documentation faster than any human can ever verify… agents can actually create more work than humans have time to verify."
>（**"编程已解决、验证成为瓶颈"**——本运动的对称命题，怀疑派判读关键引句。）

> "If you have humans verifying all the tasks… eventually what you just get is a form of verification theater."

> "If you have tasks that are completely alive with no approvals, then what you get is this classic AI slop… But if you have pure review, then you have this enormous review queue where humans can't actually review it by hand anyway."
>（**liveness vs verification 的两难**——停止条件理论的最干净表述。）

> "Three invariants…: You wanna ensure that productive work continues, you wanna make sure that only real blockers stop work, and you wanna make sure that infinite loops are bounded."
>（**"infinite loops are bounded"**——熔断三不变量。）

- 官方分节（第九轮全列）："A green check mark hides different claims"／"Completion has contents and levels"／"Keep work moving without abandoning verification"／"A task loop needs enforced rules"／"Watchdogs supervise a goal across harnesses"／"Represent done as an object"／"Give independent verifiers the tools to check"／"Make the next owner explicit"。
- **最小主张**："done"必须是对象不是布尔（**八件套**：工件 artifact／范围 scope／标准 rubric／证据 evidence／验证者 verifier／签核权 sign-off／剩余风险 remaining risk／下一步 next action——2026-10-07 第九轮按逐字稿勘误，旧记"六件套"作废）；控制平面必须同时保 liveness、真阻塞与有界循环。
- **派别适配**：**怀疑票（结构向）**——其方案是建设性的，但问题定性完全是怀疑派语料。

---

# 增量补挖（2026-10-07 第九轮·怀疑者替代推荐专项：推荐面）

> 通道：ai.engineer 讲稿页重取（官方逐字稿＋全部分节名，fetch 成功）。本轮引句全部当日 fetch 逐字取得；报告语（页面 article voice）与逐字稿分开标注。

## 处方面（怀疑的建设侧——讲稿后五个分节的机制细节）

**逐字摘录（均为仓库新引句）**：

> "So one of the best pieces of advice we have is that you stop treating done as a Boolean and treat it more like an object. This isn't specific to Paperclip, it's just advice on how you think about what is done."
（**总处方**：done 从布尔升级为对象——且明说这不是 Paperclip 专属，是普适建议。）

> "it's important that your agents can distinguish between the different pieces of what they're claiming when they say something is done, the artifact that they're saying is complete, the scope, the rubric or the standard, the evidence that it's done, who verified the work, who has the authority to sign off on the work, and what risk might be left, and really, what's the next action going to be?"
（**八件套逐字连排**：artifact／scope／rubric／evidence／verifier／sign-off authority／remaining risk／next action——页面 JSON 示例 8 键（artifact/scope/rubric/evidence/verifier/signOff/remainingRisk/nextAction）一一对应。）

> "The record preserves the producer's work without upgrading it into approval. It also gives the next agent a specific assignment. A single done: true cannot express those distinctions."（页面 article voice，非逐字稿）
（done 对象的设计理由：记录保留"生产者的完成声明"但不升格为"批准"，并给下一个 agent 明确交接种——单个 `done: true` 表达不了这些区分。）

> "We also have the idea of watchdogs, which is this maximizer mode, which says, um, 'Try as hard as you can to make sure that this happens.' When you have a watchdog, it's another agent, um, who is given a goal, and it enforces that all of your agents continue to work until that goal has been achieved."
（**watchdog 机制**：另一个 agent 持 goal 监督所有 agent 持续推进到目标达成。）

> "The important thing here is that the watchdog within Paperclip is harness agnostic. You can use it with Pi, OpenClaw, Hermes, Claude Code, Codex. Whatever you're using, you have one consistent interface for ensuring that goal is complete."
（watchdog **跨 harness**：Pi/OpenClaw/Hermes/Claude Code/Codex 统一接口——外层监督层不绑定单一 harness。）

> "So if you wanna get a hundred times more work done, you should steal this checklist. You need to define exactly what does done mean for this task. You definitely wanna separate the verifier from the author."
（**验证清单第一条**：定义 done＋**验证者与作者分离**。）

> "Often this means you're using a different model. So if you're coding using Claude, have Codex verify. You wanna ask your agents to provide evidence. Don't just ask them to say, 'Is this done?'"
（**跨模型验证＋索要证据**：Claude 写、Codex 验。）

> "But give them the tools they need to verify that the work is done. Write the code to have the custom browser harness. Write the code to take the screenshots." ＋ "Make sure they have access to a browser. Make sure that they have custom agent hooks or custom agent tooling to actually run through and click the buttons and try it out themselves and verify that the work is truly done."
（**给验证者配工具**：浏览器、截图、自定义 hooks——验证者要能亲手点按钮。）

> "Make sure you have a clear chain of custody, that every agent knows that as soon as they're done, who they're supposed to give the work to next."
（**链式责任**：每个 agent 完成后知道交接给谁。）

> "eventually what you just get is a form of verification theater. What you need is a protocol for defining how tasks actually progress through a system."
（对纯人审的替代：不是更多 review，而是**任务如何流过系统的协议**。）

**控制面三不变量**（已在上方主节归档，不重复；本轮处方化补充：这三条是"control plane for your agentic work"的设计目标，watchdog＋done 对象＋chain of custody 是其落地件）。

### 同人 2026-10 新发声（Paperclip release notes，情报级）

- URL：https://github.com/paperclipai/paperclip/releases/tag/v2026.1005.0 ｜ fetch 成功（curl）。挂钩：停止条件＋循环产品化机制。
> "@-mentioning an agent no longer starts a run. Mentions in task comments are kept as context for the assignee; only explicit assignment and review requests start work."
（**运行触发入口收紧**：@-mention 不再启动运行——只有显式指派/审查请求才开工作。把"意外触发无人值守"的口子焊上。）
> "Installed snapshots mean agents never fetch GitHub mid-run, and a failed refresh leaves the last good version in place"
（skill 源快照化：运行中不外取，刷新失败保旧版——无人值守的供给面稳定化。）

## 本轮推荐面小结（一句）

Dotta 的替代方案是一套完整协议：**done 八件套对象化＋验证者/作者分离（跨模型）＋证据与工具武装验证者＋watchdog 跨 harness 外层监督＋chain of custody 交接链**——三不变量（工作继续/真阻塞才停/循环有界）是设计目标，以上是落地件。

---

# 增量补挖（2026-10-07 goal 第二批·单点→稳定复核）

> 判定：**单点解除 → 稳定**——AIEWF 讲稿 → 08-31/09-16/10-01/10-05 release 序列，控制面哲学全程一致并加固。
> **勘误**：线索所称"06-09 release 序列"不成立——仓库首个 release 即 08-31（GitHub API 实核）。
> **轴选注记（留判读层）**：若取"harness 默认自主度"轴，08-31 收紧→10-01 放开构成反向小弧；但触发门控（10-05）与恢复权（08-31）同步收紧——两轴合读仍是"执行放开、控制权收拢"。

## Paperclip releases 完整序列（GitHub API 实取）

> 08-31："Grok no longer defaults --permission-mode to dontAsk"＋"Stranded-task recovery…stops automatic takeovers"（**默认权限收紧＋搁浅任务停止自动接管**）
> 09-16：GitHub 共享 token → 按人持久身份（供给链身份化）
> 10-01："Execution harnesses now default to full auto…Paperclip's own approval decisions still enforce controller authority"（**执行默认放开、审批权仍归控制面**）
> 10-05：@-mention 不再启动运行（已在第九轮增量归档）
