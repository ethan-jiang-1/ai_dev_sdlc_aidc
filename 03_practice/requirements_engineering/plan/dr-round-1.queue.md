# 需求工程 Topics Deep Research 一轮 Execution Queue
> 状态：本轮已收口（completed / closed_for_current_round）。过程件仅作回溯，修改 final/ 勿据本文，以 final/ 现状为准。

> 对应计划：`requirements_engineering/plan/dr-round-1.plan.md`
> 对应状态：`requirements_engineering/plan/dr-round-1.status.md`
> 本文件只记录连续执行动作、补队列候选与提升规则；不替代设计态蓝图或完整状态面。

## 🚩 Handoff Entry（新接手的 Agent 从这里开始）

> **不要直接读本文件 current_task 就动手**。先跑一遍 [`dr-round-1.status.md` 顶部的 Resume Protocol](dr-round-1.status.md#-resume-protocol接手此轮-dr-的-agent-第一眼读这里) 5 步检查，再回来执行 `current_task`。

- **当前 gate**：`closed_for_current_round`
- **下一 gate**：`user-directed deferred-gap reopen`
- **当前动作**：见下方 `Active Queue.current_task`（= 当前轮次已正式结束；仅在用户继续推进时，按需重开一个 deferred gap）
- **前置硬盘核对**（3 项，全部通过才能开工）：
  - `ls requirements_engineering/deep_research_topics/_reference/00-shared-*.md | wc -l` == 12
  - `requirements_engineering/deep_research_topics/_reference/_INDEX.md` `## 快速计数` 的 total 行 == 74
  - `status.md.Worklog` 最后一条包含最新 deferred-gap upgrade / narrowing 记录
- **完成 current_task 的硬判据**：看 `done_condition` 字段，不要自行缩放标准；若真正激活 reopened branch，则每完成一份 AC 立即刷新 `_INDEX.md` + `status.md.Worklog` + 对应研究线计数块。
- **完成后的晋升顺序**：把 `next_task` 提到 `current_task`、`next_after_next` 提到 `next_task`，从 `Refill Pool` 第一个 Candidate Block 补入新的 `next_after_next`，然后才开始新 `current_task`。这条规则在本文件底部 `Promotion Rules` + `No-Empty-Queue Rule` 有形式化版本。

## Active Queue

- queue_health: `parked_ready_for_reopen`

### current_task

- action: `user-directed deferred-gap reopen`
- done_condition: `activate only if the user explicitly wants another evidence-upgrade pass; otherwise keep the round closed and handoff-ready`
- writes_to: `plan/dr-round-1.status.md; plan/dr-round-1.queue.md; targeted deep_research_topics/_reference/*.md, deep_research_topics/_artifacts/*.md, and deep_research_topics/topic-*.md as needed`
- status_sync: `the current round remains closed until a reopened branch is explicitly activated and re-synchronized back into the packaged deliverable surface`

### next_task

- action: `targeted deferred-gap upgrade on one selected residual gap`
- done_condition: `one residual gap is either upgraded with new authoritative evidence or re-deferred after a bounded search pass, with all source-of-record files synchronized`
- writes_to: `deep_research_topics/_reference/*.md; deep_research_topics/_artifacts/*.md; deep_research_topics/topic-*.md; plan/dr-round-1.status.md; plan/dr-round-1.queue.md`
- status_sync: `the round temporarily exits closed state and re-enters evidence-upgrade execution on one explicit branch`

### next_after_next

- action: `post-reopen packaging and closeout re-sync`
- done_condition: `all affected seed/artifact/source-of-record files are re-normalized after the reopened gap pass and the round returns to closed-for-current-round handoff-ready state`
- writes_to: `deep_research_topics/topic-*.md; deep_research_topics/_artifacts/*.md; plan/dr-round-1.status.md; plan/dr-round-1.queue.md`
- status_sync: `the reopened branch is reabsorbed into the packaged deliverable surface`

## Blocked State

- blocked_reason: `not_applicable`
- interrupt_condition_matched: `not_applicable`
- unblock_trigger: `not_applicable`

When this section is active, `STATUS_PATH.state` must be `blocked`, `STATUS_PATH.blocking_issue` must summarize the same blocker, and `STATUS_PATH.Resume Checkpoint.safe_to_interrupt` must match the actual interrupt safety.

## Refill Pool

### Candidate Block

- candidate: `additional deferred-gap reopen after one reopened branch closes`
- done_condition: `not_applicable`
- writes_to: `not_applicable`
- status_sync: `not_applicable`
- why_next: `after one reopened branch is processed and re-packaged, the queue should either park again or move to one further explicit residual gap only if the user keeps pushing`
- prerequisite: `a first reopened branch has completed and the deliverable surface has been re-synchronized`
- promotion_trigger: `post-reopen packaging and closeout re-sync reaches done_condition`

## Promotion Rules

- when_current_finishes: `promote next_task, shift next_after_next, refill immediately`
- when_queue_becomes_thin: `promote highest-value ready candidate and replenish the third slot`
- when_blocked: `write blocked state explicitly and keep unblock trigger concrete`
- when_to_suspend_branch: `when a branch no longer advances the mainline or cannot be unblocked cheaply`

## No-Empty-Queue Rule

- before_closing_current_task: `refill active queue first`
- must_refill_to: `current_task / next_task / next_after_next`
- only_allowed_empty_condition: `true mainline blockage that satisfies Autonomous Execution Protocol interrupt conditions`
