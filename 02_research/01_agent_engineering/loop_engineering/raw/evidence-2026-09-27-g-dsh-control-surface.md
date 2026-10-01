---
type: evidence_archive
collected_by: 主代理·DSH 一手对照（G 路）
collected_at: 2026-09-27
serves: research-plan Q5（DSH 对照与真实体感）·digested/03（外层调度与自主度边界）·digested/05（loop/SDD/harness 分工）
status: 已取得 DSH 官方 package README / subsystem docs；这是产品机制证据，不是用户采用率或效果证据
quality_bar: P-existence + P-mechanism；未作 P-outcome 声称
---

# 回源报告 G：DSH 原生控制面与跨 feature 边界

> 观测日期：2026-09-27。以下来源均来自 `/Users/bowhead/deepseek-harness` 当前 checkout 的官方 package README 或 generated subsystem reference；页面/文件未统一提供独立发布日期，故不伪造发布日。与仓库外 FAQ 15 的 owner 口述分开：本档案只记录 DSH 机制能做什么、明确不做什么。

## 1. `dsh-goal`：单 session 的一个长期目标

来源：`packages/goal/goal/README.md`。

- 原文最小主张：`dsh-goal` 让一个 long-running completion objective 跨 turns、session resume、fork 与 process restart 持久化；当前 session 最多一个 goal；默认 round cap 为 256，可配置。
- 生命周期：`active` / `paused` / `blocked` / `complete`；goal 状态写入 session log，`GoalView` 暴露 objective、phase、roundsStarted、maxGoalRounds、blocked reason 与 process-local activation。
- 重要边界：README 明文称 package **stores goal state but does not schedule work**；continuation permission 是 process-local，而不是 durable。一个 goal 可以跨 session 存在，但 resume/fork 后 active goal 默认 disarmed，需要显式 human-authorized resume。
- `P-existence`：官方 package contract 存在。
- `P-mechanism`：event-sourced `goal/change`、compare-and-set revision、round cap、durable phase 与 process-local activation 分离；可观察性由 `ctx.goals.get(agent)` 提供。
- `P-outcome`：无。README 没有证明 goal 提升质量、减少返工或改善人的把控感。

## 2. `goal-round-driver`：目标续轮器，不是跨 feature 调度器

来源：`packages/goal/goal-round-driver/README.md`。

- 原文最小主张：driver 在 agent idle、goal active、continuation armed 且尚有 round allowance 时，自动排入一个 goal-round prompt；每轮围绕同一个 objective 继续工作。
- 续轮控制：whole-agent idle 才启动；completion / pause / blocking / cap exhaustion / cancellation / durability failure / plugin unload 会停止或 disarm；resume/fork 后不会自己重新 armed。
- 安全与一致性：reservation + admission、revision fence、session flush durability checkpoint、teardown fail-closed。
- 明确边界：same-session execution only；**does not spawn a fresh agent, fork a session prefix, or implement Ralph-style independent attempts**；**no abnormal auto-retry**；README 的 known limitations 写明没有 independent evaluator，model-facing goal policy 负责判断 evidence 是否足够。
- `P-existence`：自动续轮与停止状态存在。
- `P-mechanism`：round 只在进入 history 的 goal-sourced user message 后消耗 cap；人类输入会让自动工作让路；取消不会自动重启；durability failure 会 disarm。
- `P-outcome`：无。设计说明不等于真实长程任务效果。

## 3. `dsh-tool-goal`：授权点与自我阻塞下限

来源：`packages/goal/tool-goal/README.md` 与 `docs/config-catalog.zh.md`。

- `get_goal` 读取当前目标；`create_goal` / `edit` / `pause` / `resume` 要求 runtime-root agent 当前 top-level turn 中有 direct human message；`complete` / `blocked` 可在 autonomous goal round 中执行。
- `blockedAfterConsecutiveRounds` 默认 3；运行时只机械保证连续 admitted rounds 的下限，**same condition 的语义判断仍是 model judgment**，不是独立 evaluator 的判断。
- `resume` 需要 exact `{goal_id, revision}`；active-but-disarmed 可重新 armed，durable paused goal 由用户面 `/goal` 或 Web resume。
- 这形成了一个真实的人介入点：创建/改目标/暂停/恢复需要人类请求；但“目标是否足够清楚”“是否真的完成”“阻塞是否语义相同”并未由独立裁判自动证明。
- `P-existence`：授权规则和三轮 blocked 下限均有官方文档。
- `P-mechanism`：执行时检查 live agent、initiator、open turn、human source；不允许模型在没有当前人类消息时自行 create/edit/pause/resume。
- `P-outcome`：无效果实验。

## 4. `todo` 与 `plan`：反馈面/呈批面，不是跨 feature 控制面

来源：`packages/todo/README.md`、`packages/plan/README.md`。

- `todo` 官方定位是 session-level task list；列表跨 turns 与 reopened sessions 持久，但属于创建它的 agent session；每次 update 替换 whole list；产品包本身没有 UI，只由 interactive hosts 展示 standing plan。
- `plan mode` 让 agent 在执行前 explore/design，并呈现 finished plan 供用户 approve 或要求继续 planning；它是 guidance，不是 tool restriction，plan mode active 时所有 tools 仍可用。
- 机制含义：todo 可以成为单 session 反馈面，plan 可以成为一次呈批面；二者都不能单独表达多个 feature 的全局候选、优先级、在途、阻塞、完成、回滚和跨 repo 总览。
- `P-existence`：官方 package contract 明确。
- `P-mechanism`：todo 的 session ownership/whole-list replacement 与 plan 的 approval flow 明确。
- `P-outcome`：无，不能从功能存在推导 owner 实际使用或把控感改善。

## 5. `session-persistence`：可靠记忆底座，不是工作语义队列

来源：`packages/session/session-persistence/README.md`、`docs/subsystems/goal.md`。

- session persistence 提供 append-only session event log、list/stat/read/append/flush/close、single-writer ownership、durability barrier、resume/crash recovery；goal domain 以 durable `goal/change` 事件作为唯一状态权威。
- 这解决“上一轮发生了什么能否恢复”的持久性问题，但没有把 `feature`、`priority`、`authorized`、`in_progress`、`blocked`、`accepted`、`rolled_back` 作为通用跨 feature 工作状态模型提供出来。
- `GoalSnapshot` 保存 objective、phase、round cap；它没有全局 feature queue、多个并行 objectives、下一项选择器或独立完成认证。
- `P-mechanism`：事件模型与存储保证有一手文档；“没有工作队列语义”是对公开 API/README 范围的边界判读，不是宣称产品禁止插件自建队列。

## 6. 与 loop engineering 研究问题的暂定对位

| 控制问题 | DSH 原生有 | DSH 原生未提供/未证明 |
|---|---|---|
| 一个目标如何跨轮继续 | `goal` + same-session `goal-round-driver` | 多目标/并行目标的统一调度 |
| 目标如何跨重启恢复 | durable goal/session log；resume/fork 保留状态 | 自动恢复授权；resume 后默认 disarmed |
| 何时停止 | complete / blocked / pause / cap / failure / cancel | 独立 evaluator 认证内容质量 |
| 谁能改目标 | top-level direct human turn 才能 create/edit/pause/resume | “目标是否合适/范围是否越界”的语义裁判 |
| 何时阻塞 | 默认至少 3 个相同条件的 admitted goal rounds | 模型对“相同条件”的判断不是独立验证 |
| 跨 feature 下一项 | 插件可用 todo/roadmap/queue 自建 | goal/todo/plan/session persistence 没有统一 feature queue contract |
| 在途状态 | session/goal/todo 对单 session 可见 | 全局多 repo/multi-feature current pointer、priority、blocked reason、验收汇总 |

## 7. 负结论与限制

- 没有从 DSH 官方 package docs 得出“DSH 官方流程就是 loop engineering”；文档描述的是可组合机制与边界。
- 没有从 `todo`/`plan`/`goal` 的存在得出 owner 实际使用；FAQ 15 的 session sample 需要作为独立行为证据。
- 没有把 `session persistence` 的 durable log 等同于跨 feature work ledger；事件可恢复不等于工作语义可见。
- 这是一手机制档案，不是 outcome 证据；要回答“更清楚/更高质量/更少返工”，仍需真实工作样本或受控比较。
