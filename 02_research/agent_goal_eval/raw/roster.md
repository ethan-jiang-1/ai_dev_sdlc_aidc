# 名单

> 收录判据与时间窗在 [`../README.md`](../README.md) §3。本文件只登记谁入了、为什么。引句在 evidence，不抄到这里。
>
> 2026-09-27 首轮。机构不因为写了官方文档就获得人物行。

## 人

| slug | 为什么入 | 对本主题的一句 | 证据 |
|---|---|---|---|
| `addy_osmani` | 2026-08-14 长文给出可操作写法：goal 用于「可证明做完」的一件工作；点明裁判只核 transcript 硬规则、不判好坏；含糊的「设计好」排除在外。前沿依据：该文是他本人的实践叙述，并被本轮公司文档对照 | goal 要写成硬规则才让循环停得下来；好坏仍由人看 | [`evidence-2026-09-27-a-goal-frontier.md`](evidence-2026-09-27-a-goal-frontier.md) Source 2 |
| `hamel_husain` | 2026-06-29《“It’s Hard to Eval” Is a Product Smell》：把「很难 eval」收成产品问题，主张先让产物容易核对，再写 eval。前沿依据：与 Shreya Shankar 共同做 AI Evals 课；此文在主证据窗内，且直接回答定调里的「设计不出来」 | 验不了，先改产品让输出可核对 | [`evidence-2026-09-27-a-goal-frontier.md`](evidence-2026-09-27-a-goal-frontier.md) 登记节。判读留给 Q3 |
| `sydney_runkle` | 2026-06-16 LangChain《The Art of Loop Engineering》：verification loop 写成 rubric + grader（确定性或 LLM-as-judge），失败则退回并给反馈；人判断受众是否接得住。前沿依据：LangChain 工程博客署名，并给出他们内部 docs agent 的检查项 | 检查是对着 rubric 打分；好坏里「对不对受众」仍给人 | [`evidence-2026-09-27-a2-goal-more.md`](evidence-2026-09-27-a2-goal-more.md) Source 3 |
| `andrew_ng` | 2026-06-26 The Batch 公开信：内环停在「符合规格且无 bug」；eval 是可选数据集，同一类问题反复出现后才建。前沿依据：他在信里直接回应 Cherny / Steinberger 带起来的 loop engineering | 完成条件是规格，不是一句可核终态；外环靠人的上下文 | [`evidence-2026-09-27-a4-loop-speakers.md`](evidence-2026-09-27-a4-loop-speakers.md) Source 1 |
| `boris_cherny` | 2026-01-02 帖（窗边）：给干活的 Claude 一条核对通道，停在代码能工作且体验好；长任务可用另一只 agent、Stop hook 或 ralph。2026-07-17 预览仍写「核对自己的工作」。前沿依据：Claude Code 作者；六月的热度由他的访谈句带起，但那句本轮没有逐字稿 | 核对通道要先建好；「体验好」留在停的句子里，不是硬规则 | 同档 Source 2–3。不把他的帖算成 `/goal` 文档的第二票 |
| `shreya_shankar` | 2026-07-03 口播：失败类型由人在 trace 上标出来，agent 只把已说出的类型铺开，不新增类型。前沿依据：与 Hamel 共同开 AI Evals 课；这场是她自己的做法，不是转述 | 标准长在看数据之后；人保留哪种失败算数 | [`evidence-2026-09-27-a5-shankar-talk.md`](evidence-2026-09-27-a5-shankar-talk.md) |

## 社区

不进人物表。两处都在谈，都还不是团体章程：

- 个人复现：`anthropics/claude-code#93744`（cws5026，2026-09-11），见 A 档 Source 5
- 通讯汇总：Latent Space AINews《Loopcraft》（公开部分 2026-06-10/11），见 [`evidence-2026-09-27-a3-citation-map.md`](evidence-2026-09-27-a3-citation-map.md)。swyx 在用它汇总别人，全文在付费墙后

## 机构

| 机构 | 窗内机制 | 证据 | 不证明 |
|---|---|---|---|
| Anthropic · Claude Code | `/goal`：可核终态、对话内可见的检查、约束、另一只模型三值判定。功能发布在 2026-05（窗边），活文档观测于 2026-09-27。团队博客 2026-06-30 把适用面写成「知道怎样算做完」；2026-07-22 写「写不出检查就先起草再改」 | [A Source 1](evidence-2026-09-27-a-goal-frontier.md)、[A2 Source 1–2](evidence-2026-09-27-a2-goal-more.md) | 结果因此更好。博客与文档是同一机构 |
| LangChain | 2026-06-16：rubric + grader；trace 被设计成以后改 grader 的输入 | [A2 Source 3](evidence-2026-09-27-a2-goal-more.md) | 这样调优已经有效 |
| OpenAI · Codex | 2026-05-09 cookbook：终态、验证面、约束、边界、迭代策略、卡住即停。窗边 | Source 3 | 裁判是否独立于干活模型 |
| Cursor | 2026-08-19 changelog：`/goal` 直到「完全完成」，例子是修不稳定测试并让 CI 变绿 | Source 4 | 与上两家是同一机制 |

## 候选 · 未入

| 谁 | 为何先不入 |
|---|---|
| Yuval Yeret | 文中区分技术完成条件与业务结果，但本次未见发布日期，不能确认在 2026-06 以后 |
| swyx | 活链 https://www.latent.space/p/loopcraft 。公开部分只把 goal 说成要叠的一层，付费墙后未读，还没有可操作的完成条件 |
| Shreya 的个人站 sh-reya.com | 只出现在视频描述里。站未打开。做法已由 2026-07-03 口播覆盖 |
| Antaripa Saha | 与 Hamel 同一篇实验的共同作者，不另算一家做法 |
| Peter Steinberger | Ng 的信点了他。本轮没打开原帖。转述只有「去设计循环」，没有完成条件 |
| Andrej Karpathy / Satya | 只出现在别人的点名里。原帖未打开 |
| Cookbook 作者 Pathak / Fabbri | 官方文档的署名作者。机构行已覆盖，不另开人物 |
| cws5026 | issue 作者。社区第一人称，不是有影响力的构造者 |
