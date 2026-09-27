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
| `boris_cherny` | 2026-01-02 帖（窗边）：给干活的 Claude 一条核对通道，停在代码能工作且体验好；长任务可用另一只 agent、Stop hook 或 ralph。2026-07-17 全文仍是核对自己的工作，并默认自动代码审和安全审；`/loop` 在更高一档。前沿依据：Claude Code 作者。六月访谈句仍无逐字稿。步骤表构件页没打开 | 核对通道要先建好；「体验好」留在停的句子里，不是硬规则 | A4 Source 2–3。不把他的帖算成 `/goal` 文档的第二票 |
| `shreya_shankar` | 2026-07-03 口播：失败类型由人在 trace 上标出来，agent 只把已说出的类型铺开，不新增类型。前沿依据：与 Hamel 共同开 AI Evals 课；这场是她自己的做法，不是转述 | 标准长在看数据之后；人保留哪种失败算数 | [`evidence-2026-09-27-a5-shankar-talk.md`](evidence-2026-09-27-a5-shankar-talk.md) |
| `eugene_yan` | 2026-06-21 长文把开放任务收成四件套：沙箱目标、用提示多少控制难度、工具、看环境结果的确定性裁判；结果太粗就沿过程拆部分分，并审 transcript 防抄近路。前沿依据：一手里的构造；他是 Applied LLMs 的共同作者。文中成功率是所引基准的数字 | 开放任务的成功句写在环境状态上，不写在路径上 | [`evidence-2026-09-27-b-eval-shape.md`](evidence-2026-09-27-b-eval-shape.md) Source 1 |
| `yuval_yeret` | 2026-05-27（窗边）：写 goal 前先问停的是产出还是结果；看不见结果时 agent 交还，人留在那一层。前沿依据：一手长文对着 Claude `/goal` 写的问法，不是转述 | 判不了的业务结果先不要写成 agent 的完成条件 | [`evidence-2026-09-27-c-hard.md`](evidence-2026-09-27-c-hard.md) Source 2 |
| `peter_steinberger` | 2026-06-12 原帖给出一句 `/goal`：每步实机测、autoreview 后提交、进度写进文件。2026-06-07 那条只有「去设计循环」，没有完成条件。前沿依据：六月热度由他的帖带起；完成条件在他自己的回复里，不是转述 | 停的句子可以仍是「架构让你满意」；旁边的节拍是实机测、自动审、记进度 | [`evidence-2026-09-27-a9-x-goal.md`](evidence-2026-09-27-a9-x-goal.md) |
| `dominik_kundel` | 2026-06-04 X 长文写了七条 `/goal` 用法：退出条件要可核、最好带一个数、给测量工具、防假完成、视觉目标改用清单。前沿依据：Codex goal mode 的推出者自己写的用法，不是文档摘要 | goal 那句话就是退出条件；数让它可核，测量工具让中途看得到进度 | [`evidence-2026-09-27-a9-x-goal.md`](evidence-2026-09-27-a9-x-goal.md) Source 2 |
| `andrej_karpathy` | 2026-01-26 与 2026-03-06 两帖（都窗边）：成功标准写成先写测试再通过，或损失尽量低且不许回退耗时、内存和简洁。前沿依据：本人原帖。6 月以后没有另写完成条件的帖。衍生 CLAUDE.md 仓库里的准确率不入 | 先给可核对的标准，再让它循环。他仍在旁边看着 | [`evidence-2026-09-27-a10-karpathy.md`](evidence-2026-09-27-a10-karpathy.md) |

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
| Cursor | 2026-08-19 changelog：`/goal` 直到「完全完成」，例子是修不稳定测试并让 CI 变绿。2026-08-06 路由帖是另一套：用满意信号校准 Compass，不是任务做完没有 | Source 4；[B3](evidence-2026-09-27-b3-engineering.md) | `/goal` 与路由分不是同一机制 |
| Ramp | 2026-04-13（窗边）：收据检查从三字段一次布尔，拆成三次单字段加一段不采用的理由（评测集精确率 35% → 83%，上线 66%），再把日期和金额改成确定性抽取（上线精确率 87%，召回 44%） | [B3 Source 1](evidence-2026-09-27-b3-engineering.md) | 召回一起到了 83%；上线等于评测集 |
| Harvey | 2026-09-02：律师写的风险分类加逐条红线 rubric，三只模型投票。换架构后 59% → 77%，53% → 87% | [B3 Source 2](evidence-2026-09-27-b3-engineering.md) | 升幅来自改了某一句 prompt |
| Shopify | 2026-04-22（窗边）：300 条手写例子，语义用裁判、语法用程序。1% 流量的打开率低 35%，随后不把打开率当模型分 | [B3 Source 3](evidence-2026-09-27-b3-engineering.md) | 两周后打开率回到原水平 |
| Abridge | 2026-08-17：按就诊写「必须出现某事实」，模型逐条过/不过。裁判对过 300 条规则（真阳性 0.78，假阳性 0.07）。一次改 agent 之后专家盲比 91% 更倾向新稿 | [B4](evidence-2026-09-27-b4-abridge.md) | 91% 是人的偏好，不是规则通过率；0.78 能外推 |

## 候选 · 未入

| 谁 | 为何先不入 |
|---|---|
| swyx | 活链 https://www.latent.space/p/loopcraft 。公开部分只把 goal 说成要叠的一层，付费墙后未读，还没有可操作的完成条件 |
| Shreya 的个人站 sh-reya.com | 站已打开，是学术主页，没有完成条件写法。做法仍以 2026-07-03 口播为准 |
| Antaripa Saha | 与 Hamel 同一篇实验的共同作者，不另算一家做法 |
| Satya | 只出现在别人的点名和主题演讲二手摘要里。没有他写下完成条件的原文 |
| Cookbook 作者 Pathak / Fabbri | 官方文档的署名作者。机构行已覆盖，不另开人物 |
| cws5026 | issue 作者。社区第一人称，不是有影响力的构造者 |
