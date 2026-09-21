# Requirements Engineering Final Report System Execution Queue
> 状态：本轮已收口（completed / closed_for_current_round）。过程件仅作回溯，修改 final/ 勿据本文，以 final/ 现状为准。

> 对应计划：`requirements_engineering/plan/final-report-system.plan.md`
> 对应状态：`requirements_engineering/plan/final-report-system.status.md`
> 本文件只记录连续执行动作、当前任务、下一任务与提升规则；不替代设计态 plan 或运行态 status。

## 🚩 Handoff Entry

> 当前 package 已重新通过 final review 并处于关闭终态。先读 `final-report-system.status.md` 顶部的 `Resume Protocol`；只有当出现新的质量 finding、结构争议或用户明确要求继续修改时，才按 reopen / rollback contract 重开。

- 当前 gate：`final_review_passed`
- 下一 gate：`not_applicable`
- 当前任务：`user-directed or defect-driven reopen only`
- 当前 execution_surface：`package_polish`
- drafting_permission：`yes`

## Active Queue

- queue_health: `parked_closed`

### current_task

- action: `user-directed or defect-driven reopen only`
- done_condition: `only activate if the user explicitly requests further package changes or a new reader-facing / structural finding is identified; otherwise keep the package closed at final_review_passed`
- writes_to:
  `requirements_engineering/plan/final-report-system.status.md`, `requirements_engineering/plan/final-report-system.queue.md`, `requirements_engineering/final/*.md as needed`
- status_sync:
  `if reopened, roll back to the earliest legal gate, record the trigger in STATUS_PATH.pending_reopen_trigger, and rewrite current_task/next_task before touching final/`
- execution_guard:
  `do not modify the package while it remains closed; only reopen through the recorded rollback contract`

### next_task

- action: `targeted reopen fix pass on the identified package issue`
- done_condition: `the reopened issue is fixed or explicitly deferred, and status / queue / final surface are synchronized to the new legal gate`
- writes_to:
  `requirements_engineering/final/*.md`, `requirements_engineering/plan/final-report-system.status.md`, `requirements_engineering/plan/final-report-system.queue.md`
- status_sync:
  `update current_gate, package polish / final review checklists, and reopen findings honestly`
- execution_guard:
  `only valid after current_task has actually activated a reopen branch`

## Blocked State

- blocked_reason: `not_applicable`
- interrupt_condition_matched: `not_applicable`
- unblock_trigger: `not_applicable`

## Refill Pool

`none while the package remains closed`


## Promotion Rules

- when_current_finishes:
  `promote next_task -> current_task, next_after_next -> next_task, then refill next_after_next from Refill Pool`
- when_blocked:
  `write blocked state explicitly into status + queue`
- when_new_findings_appear:
  `do not silently skip them; add to status findings ledger and evaluate whether plan 0.10 requires reopen before advancing gate`
- when_resuming:
  `trust status + queue for live next step; consult plan only for structure or acceptance disputes`
- when_execution_surface_is_non_drafting:
  `do not write requirements_engineering/final/*.md`
- when_reopen_required:
  `roll back to the earliest affected legal gate, rewrite current_task/next_task accordingly, and record the trigger in status.pending_reopen_trigger`
- when_final_review_passes:
  `queue may transition to parked_closed with no further active task`

## No-Empty-Queue Rule

- before_closing_current_task:
  `refill active queue first when a further legal task exists`
- must_refill_to:
  `default is current_task / next_task / next_after_next; terminal tail may shrink to the remaining legal tasks only`
- only_allowed_empty_condition:
  `true blockage with explicit unblock trigger, or normal terminal state after final_review_passed`
