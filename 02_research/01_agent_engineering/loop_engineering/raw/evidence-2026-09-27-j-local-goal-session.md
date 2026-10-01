---
type: evidence_archive
collected_by: 主代理·本地 session 事后编码（J 路）
collected_at: 2026-09-27
serves: digested/07 §五 · research-plan P0.3 / P2.9
status: 本地日志 n=1。对话内 goal 事后编码。外置一行对照臂未跑
quality_bar: P-mechanism（这一条 session 里字段在不在）；不是 P-outcome
---

# 本地观察 J：一条真实 goal 的七个字段

> 观测日期：2026-09-27。材料是本机 DSH session 日志，不是公开一手。FAQ 15 未使用。实践层未改。I-2 人名未扫。

## 观察对象

- 日志：`/Users/bowhead/.dsh/sessions/--Users-bowhead-ai_dev_sdlc_aidc--/session-02bd1d4a-6a81-4b50-b0fa-1005b2e5c62e/session.v4.jsonl.zstd`
- session 创建：2026-09-27 10:01:17 +08
- goal：`goal-8c9940ff-2b6c-44a2-a8a7-dc4833849285`
- `create_goal`：2026-09-27 10:06:59 +08，seq 26，发生在 turn 1
- `maxGoalRounds`：12（不是 package 默认 256）
- objective 全文（四次 `goal/change` 的文本相同）：

> 系统研究 loop engineering：先在 02_research/ai_loop_engineering/raw 建立可持续推进的研究计划、来源与协作框架，深挖 Addy Osmani 文章及一手实践/理论证据，形成可回溯的 digested 结论，并为 03_practice/loop_governance 提供稳固输入；本轮先完成研究路径和第一批研究记录，不提前定稿实践规范。

这条 objective 不引用任何外置工作行。

## 两臂

| 臂 | 做了什么 |
|---|---|
| 对话内 goal | 事后编码上面这条已经发生的 session。工作发生时没有外置行 |
| 外置一行 + goal 引用 | **未跑**。同一件已经做完的工作不能再跑一遍还叫对照。本会话是 Cursor，不能给这条历史 session 武装 `goal-round-driver` |

所以下面的计数只描述这一条日志。它们不是「外置行减少了催问」的结果。

## 七个字段

| 字段 | 对话内 goal | 外置行 |
|---|---|---|
| `source` | 人在对话里开了这项研究；objective 由 `create_goal` 写入。不是文件里的未完成项，也不是定时器 | 未跑 |
| `authorized` | **空**。四次 `goal/change` 都没有批准人、批准范围、是否一次有效、撤销。create 落在含开场用户消息的 turn 1 里，事件本身读不出批准了什么 | 未跑 |
| `priority` | **未变更**。revision 1–4 的 objective 文本相同，没有 priority 字段，也没有前后值和理由。对话后段又加了新问题，目标文本没有跟着改 | 未跑 |
| `blocked_reason` | **空**。`update_goal` 传入的 `blocked_reason` 是空字符串。phase 从未变成 `blocked` | 未跑 |
| `stop_reason` | goal phase 始终是 `active`，没有 `complete`。6 个 turn 的结束原因依次是 error、error、error、error、completed、error。五次 error 的日志文字是：server overload、timeout、server error、server error、server error。turn 5 的 `completed` 只是这一个 turn 结束，goal 仍是 active。没有一条 goal 状态写成「模型自称完成」 | 未跑 |
| `accepted_by` | **空**。没有测试门、独立清单或人的验收事件。`todo_write` 把清单标成 completed（seq 682、721、738）时，goal 仍是 active。清单完成不是验收 | 未跑 |
| 催问 | **2**。`source.kind=user` 的消息共 6 条；其中 2 条正文只有「继续」（seq 300 开 turn 3，seq 535 开 turn 4）。另外 4 条是新指示，不算催问 | 未跑 |
| 续轮 | **0**。四次 `goal/change` 的 `roundsStarted` 都是 0。session 的 6 个 turn 不计入续轮 | 未跑 |
| 返工 | **未测**。`workspace/changes` 有 6 次，那是文件变更事件，不是返工 | 未跑 |
| 人工分钟 | **未测**。日志没有人离开和回来的时长 | 未跑 |

## 日志里和「续轮」有关的事件

`goal/change` 四次，`roundsStarted` 全是 0：

| seq | 操作 | revision | 时间 (+08) | 紧邻的工具 |
|---|---|---|---|---|
| 27 | create | 1 | 10:06:59 | `create_goal`（seq 26） |
| 190 | resume | 2 | 10:25:34 | 窗口内没有 goal 工具；前一条工具是 `edit` |
| 313 | resume | 3 | 11:19:44 | `update_goal` action=resume（seq 307 带完整 objective 与空 `blocked_reason`；seq 312 带 `revision: 2`） |
| 536 | resume | 4 | 11:36:02 | 没有 goal 工具。上一条是用户消息「继续」（seq 535） |

`get_goal` 一次（seq 302）。没有 `source.kind=goal` 的用户消息，也就是 driver 没有往对话里插过续轮提示。

seq 190 和 seq 536 这两次 resume 的发出者，日志窗口里看不出来。这里只记录「事件在、工具调用不在」，不解释成产品缺陷。

## 这能说明什么

- 这条 session 里，goal 对象被创建并 resume，对话仍在往下走，但 driver 没有计过一轮。有 goal ≠ driver 已计轮。这不推翻 evidence-g：那边写的是 driver 跑起来之后如何计轮、如何停止；这次它没有计轮。
- 四列在这条真实日志里仍是空：授权史、priority 变更、业务阻塞原因、验收者。provider 的 server error / timeout 留在 turn 结束原因里，不填进 `blocked_reason`。
- objective 文本冻结，对话里的新问题没有写回 goal。漂移发生在对话，不在目标记录。

## 这不能说明什么

- 不能说明外置一行会减少催问、返工或人工时间。对照臂没跑，计数没有对照。
- 不能把 2 次「继续」说成这项研究的效果量。两次都紧跟 turn 级 provider 错误。
- 不能把 `todo` 标成 completed 说成验收，也不能把 turn `completed` 说成 goal 完成。
- 不能外推到别的 session。n=1，事后编码。
