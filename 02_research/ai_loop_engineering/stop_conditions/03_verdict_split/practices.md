# ③ 验收与干活分离 — 工程实践做法库

> 每行：谁 | 做法一句 | 机制细节 | 强度 | 指针。
> **逐字引句回 evidence 档案**。初盘 2026-09-28，全部来自既有回源，未做新抓取。

| 谁 | 做法 | 机制细节 | 强度 | 指针 |
|---|---|---|---|---|
| Anthropic 2024 | **evaluator-optimizer 工作流** | 一个 LLM 调用生成、另一个做评估并反馈，循环；适用条件：有清晰评估标准＋迭代可测收益 | 一手 · 官方博客 | [evidence-b](../../raw/evidence-2026-09-26-b-stop-and-scheduling.md) §2 |
| Anthropic 2025 · Effective harnesses | **写权限收窄到单字段** | 干活 agent 对判据文件只被允许改 `passes` 字段；标记通过的前置＝careful testing | 一手 · 官方博客 | evidence-b §3 |
| Claude Code `/goal` | **独立小模型每轮判定** | separate evaluator——fresh model 而非干活者；三值 verdict（Not yet met / Met / Impossible，各带短理由）；**evaluator 只核 transcript 里的 hard rules，不判内容好坏** | 一手 · 厂商文档＋Osmani 澄清 | evidence-b §4a；[evidence-a](../../raw/evidence-2026-09-26-a-originators.md)（澄清句） |
| Osmani | **maker/checker 落到停止条件本身** | "the maker and checker split applied to the stop condition itself"——把工程实践里的产销分离搬到"何时算完"这个判定上 | 一手 · 作者原文 | evidence-a |
| OpenAI auto-review | **"The separation of roles matters"（官方给出理由）** | 主 agent 优化完成任务，"会把审批边界当又一个要克服的障碍"；判定放独立模型调用，更易评估/监控/改进；**被审批方提出、审批方判定** | 一手 · 官方博客 | evidence-b §4d |
| LangChain | **grader 与 agent 分置** | verification loop 里 grader 独立于 agent 存在（deterministic 或 agentic），不合格带反馈打回 | 一手 · 厂商博客 | evidence-b §4e |
| Claude Code auto mode | **裁判输入防操纵** | 分类器只看 user messages ＋ tool calls，剥掉 Claude 自己的消息与 tool outputs——"reasoning-blind by design"，防止评估器被当事人的叙述带跑 | 一手 · 官方博客 | evidence-b §4b |
| Spec Kit / OpenSpec | **reviewer-owned checklist**（SDD 阵营同构做法） | 验收清单归 reviewer 所有；按关键歧义、converge 缺口介入 | 一手 · 工具文档 | [evidence-f](../../raw/evidence-2026-09-27-f-autonomy-gates.md) |
| Claude Code `/loop` | **干活模型自停（自判极的产品形态）** | self-paced 模式下 Claude 判任务完成即调 `ScheduleWakeup(stop: true)` 取消待唤醒来 | 一手 · 厂商文档 | evidence-b §4c |
| Codex | **assistant message 终止态（自判极的候选机制）** | 候选摘录称：turn 以 assistant message 收尾即"从 agent 视角工作完成、控制交还用户"；但 assistant message 也可以是追问 | ⚠️ 候选 · 未独立复核（直接页面 403） | [evidence-k](../../raw/evidence-2026-09-27-k-unrolling-codex-agent-loop.md) |
| Huntley · Ralph | **无内建验收，终止＝操作者 taste** | TODO 清单耗尽/跑偏由人判（"a matter of taste"），清单可整删重生成；`git reset --hard` 是最终裁判 | 一手 · 个人实践 | evidence-b §1 |

**裁判权五极**（未收敛·设计空间，判定权威在 [`digested/03`](../../digested/03-构件.md) §一）：
人判 taste（Huntley）／文件清单逐条（Anthropic feature_list）／独立小模型三值（`/goal`）／干活模型自判（Anthropic 2024 默认、`/loop` stop:true、Codex 候选）／审批方判定（auto-review）。
