---
type: org_evidence
directory: 01_advocates/orgs
observation_date: 2026-10-06
---

# amp — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

### Sourcegraph Amp——The Dial、threads、automations 与事件驱动 orb

来源：ampcode.com docs（sitemap 定位，直取 200），2026-10-06。Thorsten Ball 团队一手 docs。

- **The Dial（自主度/算力分档的正式文档，/docs/the-dial）**。四档逐字："**low** is for small, well-defined tasks … **medium** is the default for most work … **high** is for hard tasks where a subtle miss would be expensive … **ultra** is for hard, open-ended work where the outcome is clear but the path is not. Use it for migrations, architecture, and changes that cross many files or systems." 线程内锁定逐字："**A thread keeps the mode you chose when you sent its first message. You cannot change the mode later in that thread.**" 理由逐字："each mode has its own system prompt and tool definitions. Switching mid-thread would mean rewriting them, which **invalidates the prompt cache and makes the thread more expensive**." CLI 键位：Ctrl+S（首条消息前）。每档三角色可钉模型逐字："Main Agent runs the conversation.／Oracle handles the second opinions requested through the oracle tool.／Subagents covers every other subagent."
  **挂钩：预算与熔断**（把"烧多少算力"做成四档拨盘＋线程级不可回改——自主度分档的循环产品化机制样本）。
- **Threads（/docs/threads）**。steering 语义逐字："When the agent is working, any message you send is **steered: it is sent after the current step** instead of waiting for the agent to completely finish. Press ⌘+Enter or Ctrl+Enter to instead queue the message …, or press **Esc twice to interrupt**." 跨端唤醒逐字："amp threads continue T-… -ox 'The deploy finished, verify the fix in production'"（"a simple way to wake a thread from a CI job or a shell script"）。公告 **Steer, Don't Queue（2026-09-08）逐字**："When you send a message while the agent is working, it's now delivered at the next possible opportunity, instead of being queued until the agent finishes its turn. … **Ship, Review, and other builtin actions still queue**, because usually you want to wait until the agent is done before shipping or getting a review."
  **挂钩：外层调度**（人在环插话从"排队等轮次完"改为"步间注入"——人机调度语义的一次官方变更，带日期）。
- **Automations（/docs/orbs/automations）**。机制逐字："Amp saves the schedule and a prompt on the current thread. When the schedule fires, Amp wakes the agent with a short message. The agent reads the saved prompt with the **get_schedule** tool … **The agent keeps the thread's context and history**." 停止条件逐字："A repeating schedule runs until you pause or delete it, it reaches its configured end, **or Amp clears it after reaching a completion condition you gave it.**" 失败语义逐字："If a run fails, Amp pauses the automation and shows the error." 监控示例 prompt 逐字要求官方模板含四要素："What Amp should inspect … What result Amp should report, **including what to do when nothing changed** … Where Amp should send the result … **When a monitoring task is complete and the schedule should stop**."
  **挂钩：无人值守运行＋停止条件**（定时唤醒、完成条件自清、失败自暂停——外环自动化的官方参数面）。
- **Event-Driven Orbs（/docs/orbs/event-driven）**。投递语义逐字："**Delivery is at least once.** Store event.id with the action that the handler performs so a retry cannot apply the same action twice." 重试退避逐字："A thrown handler defers only that event. **Amp retries it after 5 seconds and doubles the wait on each rejection, up to 5 minutes**, while later events keep being delivered. … An event that the handler keeps rejecting for **1 hour is dropped and logged**." 限流逐字："Each endpoint accepts **a burst of 10 new events and refills at 10 events per minute**. Amp returns HTTP 429 … A request body can be at most 1 MB. Send a stable **Idempotency-Key** header." handler 时限 30 seconds（`ctx.signal`）。长跑开关逐字："For CLI execute mode, pass **--no-archive-after-execute**. For SDK execute mode, set noArchiveAfterExecute in TypeScript or no_archive_after_execute in Python."
  **挂钩：无人值守运行＋预算与熔断**（webhook→agent 唤醒链路的投递保证/退避/丢弃时限全参数化，agent-as-endpoint 的运行语义）。
