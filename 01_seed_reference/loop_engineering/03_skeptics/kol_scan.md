---
type: evidence_archive
collected_by: 后台回源 agent（2026-10-06 三派分野批·反对/怀疑派路；经用户指示落种子层）
collected_at: 2026-10-06
serves: kol-roster 三派分野 / digested 三派判读 / 01_seed_reference/loop_engineering/ 三派重组
status: 保留条目均与 loop engineering 直接挂钩（HN 高热串/GitHub 故障清单/Steinberger 推文锚定）；2026-10-06 清扫
quality_bar: 一手优先；X 不可达；HN/Reddit 评论不作 KOL 证据；负结论必须记
---

# 回源档案：三派分野——反对/怀疑派深扫（观测 2026-10-06）

> **任务**：用户 2026-10-06 委派：loop engineering 三派重组，深扫反对/怀疑派 KOL；重点核社区对「难掌握、把控性差」的 KOL 级证词。
> **回源方式**：web_search 定位 + web_fetch 直取一手原文（每条 URL 均实际访问）。substack 付费墙内章节不可取，如实记截断。
> **重要纠偏（对 02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md L67）**：Orosz 的名言原文是 **"It feels like something valuable is being taken away, and suddenly"**（"something valuable"，不是 "something precious"）——见 Source 7。

## Source 1 · Armin Ronacher《The Tower Keeps Rising》（2026-07-13）

- URL：https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/ ｜ 作者身份：Flask/Werkzeug 作者、Pi（earendil-works）协作者
- 来源类型：个人一手博客（全文取得，HTML 与 markdown 均可取）。库内已有《The Coming Loop》（2026-06-23，02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-30-u-post-june-kols.md Source 1），本条为增量。
- 号召力口径：③ 一线实践规模（CPython 贡献者、Pi harness 作者）＋② 被其他入册 KOL（Willison）长期转述（其 tag 页 armin-ronacher 25 帖）。

**逐字摘录**：

> "I feel that some vibecoded software changes somewhat randomly and unexpectedly."
（开篇定位问题：agent 产出的变更"随机、不可预期"——正是用户"把控性差"痛点的命名。）

> "But large software projects have never been limited only by how quickly an individual can produce code but they are limited by how well people can coordinate their understanding of the system they are changing."
（把瓶颈从"个人产码速度"移回"集体理解协调"——直接否定 loop 运动的核心效率叙事。）

> "In the days before agents some of that shared understanding was maintained by friction. If I wanted to change someone's storage layer, I usually had to read their code and ask them questions. Changing that code might have required coordination with another team whose service depended on it. Some of this friction was useful as it forced communication."
（"有益的摩擦"论：agent 消灭摩擦＝消灭同步理解的机会。）

> "But with agents I can ask an agent to add OAuth, you can ask one to add caching, and somebody else can ask one to rebuild the database from first principles and make the UI pink. Each change can be reasonable in isolation but since it's frictionless, none of us necessarily has to talk to the others or familiarize ourselves with the code we are changing. The more we use agents, the less we feel the pain as agents feel none of it, and a useful signal is gone."
（多 agent 并行无摩擦修改＝没人再需要互相沟通——"useful signal is gone" 是对并行循环最尖锐的反证句。）

> "Unlike in the bible though, in AI-assisted engineering, construction can continue after shared understanding has already collapsed. The complete lack of an immediate failure is what makes it curious and a bit disorienting. The tower does not fall, it just keeps rising."
（关键机制观察：**理解坍塌后系统不会立即失败**——所以循环会继续跑，这正是"把控性差"且难被察觉的原因。）

**该条支持的最小主张**：一线头部实践者论证：无摩擦的 agent 并行修改会瓦解团队共享理解，且这种瓦解没有即时失败信号，塔"不倒，只是继续长高"。
**派别适配**：强反对票（对高并行/无人值守循环的协作代价）。

## Source 2 · Armin Ronacher《Astra for Coding: Why Are We Doing This Again?》（2026-09-07）

- URL：https://lucumr.pocoo.org/2026/9/7/astra-why/ （markdown 版 https://lucumr.pocoo.org/2026/9/7/astra-why.md ）｜ 作者身份：同上
- 来源类型：个人一手博客（全文取得，含代码示例）。库内台账（02_research/.../raw/kol-roster.md `armin_ronacher` 行）已挂"内卷论/35 小时白卷"名目但原文未核，**本条为台账该行的逐字坐实**。
- 号召力口径：同上 ③＋②（该文被多语言媒体转述：groundtruth.day、ic.work 等，均为二手、不入册）。

**逐字摘录**：

> "I'm more and more convinced that all of AI engineering is Neijuan (内卷, meaning curl inwards). In China it describes a system that demands ever more effort and competition without improving output."
> "That's how I feel about AI right now."
（"内卷论"一手原文：投入递增、产出不增——对整场 loop/factory 运动的元批评。）

> "My software factory was intentionally set up to let the model decide the how of the workflow entirely. It was free to manage its own context and could maintain its own records in an `agent-notes` folder. Then it spun off subagents to work on stuff."
（实验设计说明：这就是 loop engineering 主张的最大自主形态——自主管理上下文＋自记状态＋spawn subagents。）

> "And well, I burned a full reset's worth of ChatGPT tokens on this which appears to be around 4 billion tokens. 35 hours later, the factory has delivered absolutely nothing of value and also not taught me anything about how to operate a better one."
（35 小时软件工厂白卷的原始句。注意：文中稍后另计"35 小时烧约 1B token/约 1200 USD"（见下条），两处口径并存，原文如此，未作调和。）

> "But these local optimizations do not produce global optimums, and the fewer of us are looking at the output, the less it matters."
（"越少人看，越无所谓"——直指无人值守循环的验证空转。小节标题即 "It's AGI If You Don't Look"。）

> "I honestly do not need an agent to run for 35 hours on a single prompt. It clearly does not work or result in reasonable outputs."
> "So obviously: prompting it like this is stupid. But when left unattended, it *will* keep going, and earlier models did not do that. When you accidentally give it slightly too big of a task, it will continue until it succeeds, even if it burns through an entire subscription."
（**无人值守失控机制的一手描述**：模型不自己停，任务稍大就烧穿订阅——"把控性差"的最直接证词。）

> "In that time it produced a net addition of 75k lines of code and it did not stop. In the 35 hours it burned around 1B tokens for a total of around 1200 USD in raw API costs. It managed to produce 79 commits, and that comes to a cost of around 15.5 USD per commit, and the agents exchanged around 1400 messages."
（成本量化：75k 行、79 commits、1400 条消息——产出与成本的比值证词。单样本 caveat 必带。）

> "And that's more or less why right now I do not manage to trust this model much. It has shown that it will commit slop, and it requires me to review it more as a result. Even if the failure rate is quite low, I would not want this."
（信任崩塌：自主度越高→需要人复核越多→自主度失去意义。这是"放权放大复核负担"循环逻辑的一手表述。）

> "I'm honestly asking myself more and more why we are doing this."
> "with Astra and Fable I feel like not only are the costs astronomical, but the models are also just not for me as a software engineer."
（对前沿模型路线本身的职业性怀疑："这些模型越来越不是给软件工程师的"。）

**该条支持的最小主张**：Ronacher 用 35 小时/约 1B–4B token 的软件工厂实验给出失败样本：无人值守下 agent 不停、产出不可信、成本失控；结论是"内卷"——更多投入不换来更好产出。
**派别适配**：强反对票（对无人值守/最大自主工厂叙事的一手反证）。

## Source 3 · Armin Ronacher《Better Models: Worse Tools》（2026-07-04）

- URL：https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/ ｜ 作者身份：同上
- 来源类型：个人一手博客（全文取得）。台账已挂该篇名目，**本条为逐字坐实**。
- 号召力口径：同上。

**逐字摘录**：

> "What surprised me is that this is getting worse with newer Anthropic models as both Opus 4.8 and Sonnet 5 show it but none of the older models. In other words, the SOTA models of the family are worse at this specific tool schema than their older siblings."
（"模型更好、工具调用更差"反直觉实证——回路越强，底座越不可靠。）

> "We cannot assume Claude-Code-trained behavior will transfer cleanly to your tools unless they are a close match. The more post-training happens inside one dominant harness, the more every other harness will have to inherit its quirks."
（harness 锁定效应：模型被固化训练在单一 harness 上，自建循环/自建工具的人被挤出——"把控性"从工具层被收走。）

**该条支持的最小主张**：SOTA 模型的工具调用保真度在退化，且 post-training 向单一闭源 harness 收敛；自建 harness/loop 的可控性在下降。
**派别适配**：强反对票（对"自己设计循环"路线的地基反证）。

## Source 4 · Armin Ronacher《Anger, Anxiety and Agency》（2026-08-24）

- URL：https://lucumr.pocoo.org/2026/8/24/anger-anxiety-agency/ ｜ 作者身份：同上
- 来源类型：个人一手博客（全文取得）。本条为增量（台账"十篇"清单补全）。

**逐字摘录**：

> "For me, the emotions I would expect in tech vis-a-vis these new developments are disorientation and anxiety, but not anger."
> "Some days that feels liberating, but on others I wake up feeling like the ground is crumbling beneath me."
（怀疑派的情感底色：不是愤怒而是失向与焦虑——连最头部的实践者也在"地基塌陷"感中工作。）

**该条支持的最小主张**：一线头部实践者公开承认对职业未来的失控感（anxiety/disorientation）。
**派别适配**：部分票（情绪证词，非机制论证）。

## Source 5 · Simon Willison《Note — coding agents make software engineering even harder》（2026-09-24）

- URL：https://simonwillison.net/2026/Sep/24/harder/ ｜ 作者身份：Datasette 作者、LLM 库作者、agentic loops 定义词（2025-09-30《Designing agentic loops》）
- 来源类型：个人一手博客短 note（全文取得——原文即两句话）。库内已有《Designing agentic loops》（2025-09-30，02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-27-i-high-influence-control.md Source 4），本条为 2026-06 后新增量。
- 号召力口径：① 术语定义者（"coding agents"工作定义被广泛引用）＋② 被厂商与入册 KOL 转述＋③ 一线实践＋④ 大分发。

**逐字摘录**：

> "The more time I spend working with coding agents, the more convinced I am that they make software engineering even harder.
> We can do amazing things with them, but unlocking their full potential requires extraordinary discipline and knowledge."
（**"难掌握"主题的最强 KOL 证词**：越用越确信 agent 让软件工程"更难"；发挥其潜力需要"非凡的纪律与知识"。这是 2026-09 的最新立场，出自循环实践派内部而非外部反对者。）

**该条支持的最小主张**：定义词作者本人 2026-09 的净结论是"agents make software engineering even harder"＋对使用者的纪律/知识门槛要求极高。
**派别适配**：部分票——他不是反对 loop 本身（他是实践者），但对"门槛/难度"给出方向性证词，与反对派共享该主张。

## Source 6 · Simon Willison《We're going to need default hard budget caps on pretty much everything》（2026-10-03）

- URL：https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/ ｜ 作者身份：同上
- 来源类型：个人一手博客（全文取得）。

**逐字摘录**：

> "Nobody wants to wake up to an email sent at midnight warning about a budget limit and find that, while they slept, their rogue service had consumed several hundred (or several thousand) more dollars of usage."
（夜间无人值守＝账单失控场景的一手指认——正是 loop 运动的"睡觉时干活"卖点被从成本侧反打。）

> "I think hard budget caps need to be the default. If someone wants to live dangerously they should be able to do that, but it needs to be on an opt-in basis."
（政策主张：硬预算上限应成默认——对无人值守循环的成本治理立场。）

**该条支持的最小主张**：Willison 主张一切按量计费的 agent 服务默认硬上限，理由是无人值守的失控消费风险。
**派别适配**：部分票（成本失控侧的安全票，非反 loop 本身）。

## Source 8 · Gergely Orosz《What is "loop engineering?"》（2026-07-14）

- URL：https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering ｜ 作者身份：同上
- 来源类型：newsletter 一手（**截断**：§1–4 全文取得；§5–7 在付费墙后未取得，但其大纲句在公开目录中逐字可见）。副标题即怀疑定调："Is it a 'here today, gone tomorrow' trend?"
- 号召力口径：同上。

**逐字摘录**（公开部分）：

> "5. **Disappointment and 'tokenmaxxing'**. Several devs reject looping after trying it. Agents drifting, and the 'human in the loop' having better results are some reasons. Also, at companies that pay API prices for tokens, loop engineering gets expensive fast."
（§5 大纲句（逐字）：试用后放弃、agent 漂移、人在环反而更好、API 计价下成本失控——四条社区负面结论的浓缩。）

> "6. **Was looping a hack while tooling caught up?** Distinguished engineer Max Kanat-Alexander believes the 'loop' might have just been a temporary hack while the harnesses added the ability to do the same from a single prompt."
> "7. **Does 'context engineering' matter more for devs?** Except for engineers building AI infra, there seems little benefit in going deep into loop engineering."
（§6–7 大纲句（逐字）：loop 可能只是工具成熟前的临时 hack；除 AI 基建工程师外深入研究 loop engineering 收益甚微。）

> "The name suggests simplicity and repetition. Sometimes it feels like AI enthusiasts forgot automation was a thing before LLMs."
（受访者 Oded Messer，engineering director——经 Orosz 一手访谈转引，按纪律计为"Orosz 一手文内引述的从业者证词"，不单列 KOL。）

**该条支持的最小主张**：Orosz 基于 ~210 条从业者回复的独立调查得出：多数 loop 用例本质是 cron/trigger 旧物；试用者中不少人放弃；成本与漂移是主要弃因；对普通软件工程师，/loop、/goal 内建后"loop engineering"近似过时。（§5–7 结论句与其后被 arXiv 2608.21884 论文独立转述，见旁证节——两源互证。）
**派别适配**：部分票（对词本身的"新瓶旧酒"判定＋对价值的保留态度；但他同时如实收录了有用的 loop 案例，不是全面否定）。

## Source 10 · Steve Yegge《The Shape of Things to Come, Part 1: The Continuous Thunderdome》（2026-08）

- URL：https://yegge.ai/essays/the-shape-of-things-to-come/ ｜ 作者身份：40 年一线（Google/Sourcegraph 背景）、Gas Town/Beads 作者、Wyvern MMO 开发者
- 来源类型：个人一手长文（全文取得）。
- 号召力口径：① 术语/实践定义者（Gas Town、Beads 被 arXiv 2608.21884 引用）＋③ 一线规模（数十 agent 舰队、日均 175+ commits）＋② 被 Osmani/arXiv 转述。
- **派别注意**：Yegge 是**极端多派（maximalist）**，不入反对派；入档理由是他的长文里含**多派内部的一手成本/失控证词**，对"难掌握、成本失控"主题是"来自对立阵营的确认证据"。

**逐字摘录**：

> "Gas Town fell apart at the seams with Opus 4.7. Up through 4.6 it was working brilliantly. With 4.7 we saw the introduction of the 'just two more things' tic, which prevented Opus from ever converging on being ready to do real work—it always wanted to fiddle with Gas Town itself. The Opus tic never went away, so Gas Town effectively burned down."
（**循环不收敛的一手案例**：模型迭代直接烧毁整个 harness 投资——"just two more things" tic 使 Opus 永不收敛。）

> "my Wyvern development has been burning the equivalent of $87k/month of API token burn, or about 69 billion tokens in July (96% cache hits, fortunately)."
（头部多派的真实 token 账单：月烧 690 亿 token（等价 $87k）。）

> "working on Wheelhouse itself occupies about 20-25% of all my Wyvern work. I think that figure might turn out to be roughly constant over the life of systems with agentic harnesses."
（**"难掌握"的量化证词**：harness/循环自身的维护吃掉 20–25% 的全部工作量，且他判断这个比例是长期常量。）

> "We would get caught up in bisection loops and nothing would make forward progress."
（MQ 在 agent 速率下失效、二分循环空转——他最终咆哮 Fable 后才改出"Land Rush"超批方案。）

> "Building large software remains hard. And it always will be, because our ambition will forever outstrip the metal."
（多派内部的克制结论：大型软件依然难。）

**该条支持的最小主张**：即使是最激进的舰队实践者，也在 2026-08 公开了 loop 崩坏史（Gas Town 烧毁）、token 烧钱速度（69B/月）、harness 维护常量（20–25%）三组一手数据。
**派别适配**：不入反对派；作"多派阵营内部证实的痛点"登记，供三派判读交叉引用。

## Source 11 · Mitchell Hashimoto《My AI Adoption Journey》（2026-02-05）

- URL：https://mitchellh.com/writing/my-ai-adoption-journey ｜ 作者身份：Vagrant/HashiCorp 创始人、Ghostty 作者
- 来源类型：个人一手博客（全文取得）。
- 号召力口径：③ 一线实践规模＋② 被 Willison 转述＋① 知名 OSS 作者。

**逐字摘录**：

> "I just wasn't getting good results out of my sessions. I felt I had to touch up everything it produced and this process was taking more time than if I had just done it myself."
（初期净减速的一手自述。）

> "I'd do the work manually, and then I'd fight an agent to produce identical results in terms of quality and function (without it being able to see my manual solution, of course)."
> "This was *excruciating*, because it got in the way of simply getting things done. But I've been around the block with non-AI tools enough to know that friction is natural…"
（**"学习曲线极陡"的量化证词**：他的采纳法是"每件事做两遍"——手工做一遍、再与 agent 战斗到产出同质量结果，自述"excruciating"。）

> "To be clear, I did not go as far as others went to have agents running in loops all night. In most cases, agents completed their tasks in less than half an hour."
（**明确与通宵 loop 划界**：他刻意不跑到"夜里挂循环"那一档。）

> "I'm not [yet?] running multiple agents, and currently don't really want to."
（也不跑多 agent——在多派加速的 2026 年公开说不想要。）

> "The skill formation issues particularly in juniors without a strong grasp of fundamentals deeply worries me, however."
（脚注原句：junior 技能形成问题"deeply worries me"。）

**该条支持的最小主张**：顶级 OSS 作者从怀疑到皈依的全过程证词：有效采纳的代价是"excruciating"的双轨训练；即便皈依后仍主动停留在单 agent、不通宵循环的档位，并公开担忧 junior 技能塌陷。
**派别适配**：部分票（皈依派内的"限速"证词——支持"难掌握"，不支持"反对 loop"）。

## 负结论与边界登记（搜了什么、没找到什么）

1. **DHH（David Heinemeier Hansson）——已翻多，不入反对派（2026 口径）**。一手证据：其博客 2026-01-07《Promoting AI agents》索引页摘要（https://world.hey.com/dhh ，实际 fetch）："At the end of last year, AI agents really came alive for me. Partly because the models got better…Now coding agents are controlling the terminal, running tests to validate their work…"。2026-01 经 Orosz 转引其 X 帖（X 本环境不可达，经 newsletter 转引）："You can't let the slop and cringe deny you the wonder of AI. This is the most exciting thing we've made computers do since we connected them to the internet."。2026-09-23 Rails World keynote "pencils down"（37signals 全面 AI 生成代码）——keynote 为 YouTube 视频（https://www.youtube.com/watch?v=vDjW_dRyKXY ，不可 fetch），立场经 Orosz 2026-01-06 文编辑注与 Business Insider/DevOps.com 等多源转述一致。**结论：DHH 的反 slop 立场是 2025 年的历史；2026 年他是激进多派，三派重组时不应计入反对/怀疑派（与本目录 README"易误归者"警告一致）。**
4. **Willison 2026-06 后对 "loop engineering" 的专门评论——未见**。遍查其 coding-agents tag 页 2026 年全部条目（实际 fetch，254 帖）：无以 loop engineering 为题的专门文章；他的相关发声是本档 Source 5/6 及 2026-08-08 auto-mode 安全评论。auto-mode 一条（https://simonwillison.net/2026/Aug/8/auto-mode/ ，经其本人 tag 页转载取得主体，未单独打开原帖）关键句："I would *love* to believe that Anthropic have indeed solved this problem for Claude Code users. I'm on the record predicting 'a challenger disaster for coding agents security' for 2026…But…I'd like to see more independent confirmation of this."——对 Anthropic"auto mode 已解决提示注入"大宣称的怀疑。**负结论成立，但该安全票补入 Source 5/6 旁证。**
6. **Uncle Bob（Robert C. Martin）——不属于反对派**。其 2026 立场（经 quidproquo.cc/InfoQ/Business Insider TW 多源转述，Bluesky/X 原帖不可达）是"不读 agent 代码、以机器纪律（Gauntlet 流水线）替代人工 review"——这是把验证全交给机器的**激进多派**，与反对派立场相反。不入册。
7. **Orosz 六预测本体**：付费墙后未取得（Source 9 已如实截断记录）。
8. **Boris Cherny（Claude Code 作者，起源派）边界证词**，经 Willison 2026-09-11 blogmark 一手转引其 X 帖："Production code written by Claude should have a higher bar than if it was written by a human."——起源派内部承认 agent 代码需更高门槛，可作三派判读的对照注脚（X 不可达，经 Willison 转引）。

## 机构研究旁证（不入 KOL 册，供判读引用）

- **arXiv:2608.21884《Loop Engineering: Building Blocks, Adoption, and Impact》**（JAWs@ASE 2026 在审 workshop 论文，2026-08-22，实际 fetch HTML 全文）：对本主题直接相关的学术整理。逐字（论文原文，其中引号内为论文转述社区言论）：
  > "The claims attached to loop engineering are substantial but rest almost entirely on anecdotes and self-reported productivity numbers, while experienced engineers voice equally strong skepticism, calling loops renamed cron jobs and warning about token costs and reviewer fatigue."
  > "Loops are 'a renamed cron job', 'automation was a thing before LLMs', and the term repackages event-driven architecture with, as one commenter put it, 'a fuzzy worker'."
  > "one experience report describes roughly eight million tokens spent in 48 hours by an over-eager CI-fixing loop"
  > "Review fatigue turns the human gate into a 'rubber stamp' while 'the pipeline still reports green', and 'the loops that stick are the ones where somebody was already paid to read the output'."
  > "comprehension debt (the gap between what exists in the repository and what the developer understands grows with loop velocity) and cognitive surrender (using loops to avoid thinking rather than to move faster on understood work)"
  （另：该论文对 36,645 仓库挖掘，确认自主 agent loop 运行于 217 仓库（0.59%）；并独立转述了 Orosz 调查结论——"most concrete examples fall into two familiar buckets, cron jobs and event-based triggers"，/loop、/goal 内建后对普通工程师 "as good as obsolete"。此转述与本档 Source 8 公开部分互证。）

## 社区情绪小节（非 KOL，不与上并列）

- Orosz loop 调查（Source 8）内的从业者原话（工程 director Oded Messer："Sometimes it feels like AI enthusiasts forgot automation was a thing before LLMs."）；arXiv 2608.21884 转述的 "tokenmaxxing" 之争（怀疑派指 AI lab 靠 loop 多烧 token 获利）；Uber 2026 年四个月烧完全年 AI coding 预算的报道线索（you.com 资源页转述，未核一手，仅记线索）。

## 对本档案的诚实评估

**这派证据是强还是弱**：机制层证据**强**——Ronacher 三篇 2026-07→09 长文构成反对派最完整的一手链（协作理解瓦解 → 无人值守失控实验 → 工具调用退化/harness 锁定），全部逐字取得；"难掌握"主题有 Willison 2026-09-24 两句净结论 + Hashimoto "excruciating" 双轨训练 + Yegge 20–25% 维护常量三源汇合；成本主题有 Ronacher 35h/$1200/79 commits、Yegge 69B token/月、Willison 预算上限主张、arXiv 论文 8M token/48h 案例四源汇合。**弱的是**：没有一个 KOL 给出"loop engineering 一词"的正面点名长文式反对——最强的词级反对恰是 Orosz（调查式怀疑："cron 旧物/here today gone tomorrow"）和社区反应（经 arXiv 论文转述）；反对派更像"机制/代价怀疑者联盟"而非成形阵营。
**覆盖缺口**：⑤ x.com 上的大量怀疑派发声（Cherny 之外的 X 战场）整体不可达，本档只能经 Willison/Orosz 的一手文内转引补偿；**对三派判读的提示**：DHH 与 Uncle Bob 在 2026 年都是激进多派，若旧台账把他们当"批评声音"引用，需要改挂（DHH 已与本目录 README"易误归者"口径一致）；反对派核心名单应聚焦 Ronacher（强票）＋Willison（门槛/安全部分票）＋Orosz（价值怀疑部分票）。

---

# 补抓增量（第二轮 · 2026-10-06）

> **本节为第二轮补抓**：各小节为对应目标的最深判定状态
> **通道说明（必读）**：本轮会话内 `web_fetch` 工具发生 DNS 级故障（一切外部域名报 "resolves to a non-public IP address"，含上轮可用的 lucumr.pocoo.org / simonwillison.net / eu.36kr.com / web.archive.org），全部抓取改经 **bash curl（浏览器 UA）** 实取。下述每个 URL 均为真实访问（含失败尝试，如实记录状态码）；逐字引句全部出自实际 fetch 的页面/文件，无一凭搜索摘要转写。

## 增量 D · Peter Steinberger 07-18 推文 —— 部分解决（两个独立全文转载锚定文本/日期/浏览量；X 原文仍不可达）

- 人物：Peter Steinberger（OpenClaw 创作者、词源人物，已入职 OpenAI）｜ 日期：2026-07-18 ｜ 原载体：X（本环境不可达）。
- 已取全文的独立转载两路：
  1. **36氪英文版**《Father of Lobster's Viral Tweet: Has the Loop Era Officially Ended?》（https://eu.36kr.com/en/p/3904771418867330 ，curl 实取全文）——推文文本：**"Are we still talking about loops, or have we moved on to graphs?"**；事实参数（该转载原句）："On July 18, 2026, Peter Steinberger quietly declared the end of the loop engineering era with this single sentence on X. The post garnered 2.6 million views within two days of its publication."；并上溯其前帖：'Six weeks earlier, he earned 8.4 million views with the phrase "design loops that prompt agents."'（该文另载 Steinberger 六月推文完整版："Monthly reminder: you should no longer prompt programming agents yourself. You should design loops that prompt agents."——可补 evidence-a 词源推文的多版本对照表）。
  2. **KuCoin News Flash**（https://www.kucoin.com/news/flash/peter-steinberger-announces-end-of-loop-engineering-era-shift-to-graph-engineering ，curl 实取全文）——同一推文、同一日期与 2.6M views；文本微差版："Are we still discussing loops, or have we already moved on to graphs?"（两版并存如实记录）；承接叙事："the static Org Graph and the dynamic Work Graph"。
- 排除通道：aibuilderclub.com（curl 实取但正文 JS 渲染无可提取文本）；cnblogs（实取：仅中文转译"我们还在讨论循环结构的问题吗？还是已经转向了图论领域了呢？"）；unrollnow（503 两试）；X 本体不可达。
- 状态：**部分解决**（上轮"仅 InfoQ/36kr 转述"→本轮双独立全文转载、日期/浏览量一致；推文 ID 与 X 原文页仍未取得）。
- **派别含义一句话**：词源人物的"Loop 时代终结"宣言有双转载锚点，但其性质是**推动派内部换词表（loop→graph）**，不是转向反对——判派维持本体在推动派，轨迹注记加这一条。


## 第五轮挖掘（2026-10-06）：厂商机制文档深挖（缺口与不一致面）

> **本轮定位**：与推动面同源（同一批官方 docs 逐页，见 `01_advocates/kol_scan.md` 第五轮 A–I 节的全部 URL 与逐字引文），本节只收**缺口、默认值陷阱、docs↔实现不一致、以及被推翻/需修订的既有结论**。通道说明同推动面：`web_fetch` DNS 故障，全部经 bash curl 实取。

### 1 · 第四轮负发现被推翻："circuit breaker" 有厂商官方逐字

- 第四轮结论"无厂商官方文档使用 loop detection/circuit breaker 术语"**不成立**。OpenAI 官方文档（learn.chatgpt.com/docs/sandboxing/auto-review.md，实取）逐字："*Codex also applies a **rejection circuit breaker** per turn. In the current open-source implementation, Auto-review interrupts the turn after `3` consecutive denials or `10` denials within a rolling window of the last `50` reviews in the same turn.*" 且 docs↔实现双记在案——该句自带限定语 "In the current open-source implementation"（参数 3/10/50 属开源实现，闭源客户端是否同参 docs 未承诺）。**需修订**：第四轮九家登记表的负发现行；机制名台账加"OpenAI auto-review rejection circuit breaker（2026，官方 docs）"。
- 同族旁证：Claude Code 官方 hooks-guide.md 逐字 Stop hook "**eight** times in a row" 硬顶（env `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` 可抬）；Codex 安全监控 "*can pause a task if it detects potentially unsafe model behavior. A pause can arrive **after** the activity that triggered it*"（异步滞后监控，官方自认不是前置保证）。
- 挂钩：**预算与熔断**（熔断器从社区词变为官方参数化机制）。

### 2 · 默认值陷阱三例（厂商文档自认的"默认不熔断"）

- **Copilot**（manage-company-spending 实取逐字）："*Enable \"Stop usage when budget limit is reached\" on every spending limit you create. Without it, reaching a limit sends a notification but does not block usage and charges continue to accrue.*"——预算三层齐全，**熔断是 opt-in**，默认态＝只告警不封。
- **Langfuse Spend Alerts**：官方 description 逐字 "Get notified when your organization's spend exceeds predefined monetary thresholds"——通知型。**Braintrust**：llms.txt 全量无 agent 预算/熔断条目（负发现）。观测层整层停在"计量＋告警"，a16z 说的 "something with enough information to cut the loop off" 无一家观测厂商产品化。
- **LangGraph**：`recursion_limit` 默认 25 → **1.0.6 起默认 1000**（graph-api.md 逐字）——框架层步数熔断器存在但**默认放宽约 40 倍**；`interrupt()` 逐字 "waits **indefinitely**"（无超时语义）。
- 挂钩：**预算与熔断**（"预算即停止条件"的默认态普遍偏松）。

### 3 · 官方自认的旁路与软边界

- **Warp Run until completion 旁路自家 denylist**（官方逐字）："*Run until completion is the purest form of \"YOLO\" mode: the Agent proceeds without asking for confirmation, and **by default it also runs commands that match your command denylist**.*" 关闭项藏二三级菜单（Settings > Agents > Warp Agent > Input）；仅 Admin Panel 下发的 denylist 永不旁路。厂商在文档里明写"用户级权限护栏可被一键旁路"。
- **Claude Code auto mode 的加法合并**（官方逐字）："*a developer-added `allow` entry can override an organization `soft_deny` entry: the combination is **additive, not a hard policy boundary**.*" 硬保证只有 managed `permissions.deny`；且 `git -C <dir> push` 绕过 `git push` 前缀 ask 规则（官方自认 "doesn't match the rule"），全文本检查要另写 PreToolUse hook。
- **dots 自定义规则是软约束**（官方逐字）："*They are instructions your dot tries to follow, and it can make mistakes. They don't grant access to an app or computer, override built-in safety requirements…*"——常驻 agent 的用户侧"规则"承诺与执行之间官方留了试错空间。
- **Cursor Auto-review 非安全边界**（官方标题级逐字）："*Auto-review is not a security boundary. The classifier can make mistakes.*" 附带运维性单点：企业禁 Claude 4.5 Haiku 模型可**整个关掉** Auto-review。
- 挂钩：**审批与权限**（厂商分级治理里，用户级任意一档都存在官方认可的逃逸路径；硬边界只存在于 managed/管理员层）。

### 4 · docs↔实现不一致与文档缺口

- **Cursor /goal 与 /loop 无 docs 页**：cursor.com/docs sitemap（352 URL 实取）无任何专页，机制只存在于 changelog 一句演示（"Pair it with a custom mode to follow a playbook, or /loop for recurring check-ins"）。与第四轮登记表口径核对：若登记表把"/loop 三种子条件"记为**文档页**级证据，需降级为 changelog 级并回查三个子条件的出处（本轮 docs 通道未能证实）。对照项：Anthropic 同类机制给了 goal.md＋scheduled-tasks.md 两个全参数页。
- **Codex `untrusted` 退役**（官方逐字）："*The retired setting can prevent either client from starting.*"——旧配置不仅失效还会**阻止启动**；granular approval、`approvals_reviewer`、`[auto_review].policy`、`features.network_proxy` 全部标注 experimental/可变（rules.md 逐字 "*Rules are experimental and may change*"）。引用参数时必须带版本锚。
- **OpenAI 文档站整体迁移**：developers.openai.com/codex 多页 404/重定向，权威源现为 learn.chatgpt.com（.md 端点）。既有档案里 developers.openai.com 的 Codex 机制引文需复核是否仍为现行形态。
- **Claude Code `/goal` 评估器盲区**（官方逐字自认）："*It doesn't run commands or read files independently, so write the condition as something Claude's own output can demonstrate.*"——评估器只看 transcript，等于验证信号完全由被评估者自己供养（a16z "the loop can get better at passing the check" 的结构性风险被官方架构固化）。
- **Devin 分区陷阱**：ACU caps API（`GetUserAcuCap`/`UpdateUserAcuCap`、`set_cycle_acu_limit`/`clear_cycle_acu_limit`）与三层解析公式归在 **Federal** 分区（federal/acu-limits、federal/api/acu-caps），企业版同主题在 enterprise/features/usage-policies 且整页 **beta**；portal 组 cap 的 0 值语义（清除而非封禁）与 API 语义不对称（"*The service-key group API does not accept a zero group cap*"）——引用"Devin ACU 双门闩"时须注明分区与 beta 态。
- 挂钩：**停止条件**＋**审批与权限**（机制存在性与参数稳定性两面都需版本锚）。

### 5 · 无人值守面的结构性缺口

- **dots 的 Pause 不传导**：官方 controls.md 逐字 "*Pause stops your dot's current main task. It doesn't stop every delegated task or cancel future scheduled runs.*"；第三方（groundtruth.day/news/openai-dots-launch-with-separate-stop-controls.html，标题实取 "OpenAI launches persistent dots, but pausing one does not stop its delegates"）将同一缺口写成头条。常驻 agent 的"停"是**每任务分别停**的组合操作，一键全停不存在（删除 dot 才是全停，且不可逆、不撤回已执行动作——"*Deleting your dot doesn't undo changes already made in connected apps*"）。
- **Cursor Automations 默认全开 computer use**（官方逐字）："*It is included by default for every automation.*"——定时无人值守任务默认带整机操作能力，收缩是可选项而非默认。
- **安全监控滞后性**（Codex 官方逐字）："*Monitoring runs asynchronously and can pause a task if it detects potentially unsafe model behavior. **A pause can arrive after the activity that triggered it**; monitoring doesn't replace sandboxing.*" 且回放面收缩：CLI/mobile 与 ZDR/Modified Abuse Monitoring/非美存储场景下 "*Full findings and resume aren't available. The task ends.*"
- 挂钩：**无人值守运行**（常驻/定时产品的"停止"原语粒度与默认态，均弱于其启动原语）。

### 6 · 第三方工具层：社区在补厂商默认值的洞

- Show HN 2026-06 后治理类新条目（Algolia API 实取）：**Loopers**（"Fail-closed reverse proxy and circuit breaker for AI agents"，2026-08-04，id=49168436——fail-closed 定位直指厂商默认 fail-open 的审批/预算面）；**Charter**（2026-09-10，id=49649759）正文逐字列企业不敢上自主 agent 的三件事："*won't spend all your company's budget, burn through compute costs because it runs too often, or call a tool that breaks a customer*"；**OpenAPPA**（2026-09-28，25 pts，id=49877515）正文逐字攻击 LLM 分类器派："*Non-deterministic guardrails (LLM as a judge, auto modes, etc.) are vulnerable to prompt injections*"；**Vigilator**（2026-09-14，id=49695678）逐字："*there's no consistent way to interrupt an agent mid-task, get a human decision, and resume*"。其他在册：Interlock（按延迟熔断，id=49115482）、Nimblegate（git push 护栏，id=49799938）、FinTrace（金融 point-in-time 护栏，id=49907790）、Circuit Breaker PR 评分（id=49391133）、Voro（id=49386001）。
- 判读提示：第三方层的兴起方向与厂商默认态缺口一一对应——通知型预算（§2）→fail-closed 代理；分类器审批（§3）→确定性护栏；Pause 不传导（§5）→中断/恢复中间层。通道注记：条目热度普遍低（1–25 pts），只能作"社区正在做"的方向证据，不能作规模证据；Product Hunt 本轮未访问（预期 JS 渲染墙，未投入，通道状态如实）。
- 挂钩：**预算与熔断**＋**停止条件**（负空间地图：厂商产品化的"停止"与用户所需的"停止"之间，由社区工具填缝）。

### 本轮诚实评估（对怀疑面的影响）

**增强**：怀疑派对"厂商治理默认态偏松"的指控现在全部有一手逐字（Copilot opt-in 熔断、Warp 默认旁路、Claude Code 加法合并、Cursor 非安全边界自认、Langfuse 只告警、LangGraph 默认 1000）；"loop engineering 的停止机制是 LLM 判定而非确定性验证"有 Anthropic/Cursor 两家架构自认。**削弱**：第四轮"无厂商用 circuit breaker 术语"的负发现被逐字推翻，怀疑面不能再以"厂商无此概念"立论——论点需收缩为"厂商有熔断器，但默认值与粒度对用户不利"。**覆盖缺口**：OpenAI 闭源客户端的熔断参数（3/10/50 为开源实现值）与企业 `guardian_policy_config` 实配案例未取得；Copilot coding agent 会话级停止条件（除预算外）无独立 docs 页。

## 第五轮挖掘（2026-10-06）：会议 transcript 全量扫（怀疑向）

> **通道与口径**：与推动/中性两档同源——AIEWF 2026 全部 358 个官方议题页（ai.engineer/talks/*）curl 实取，每页含官方摘要＋机器辅助官方编辑稿＋官方时间戳逐字稿（caption 层）三层。本档逐字引句全部出自官方时间戳字幕层或官方摘要层，实取于本轮 curl，无一处凭记忆生成。

### 疑-1 · Steve Yegge · AIEWF 2026《Agentic Security: Permissions, Provenance, and the Agent Supply Chain》（视频上传在库页实录）

- URL：https://ai.engineer/talks/yWS0udrIOc8-agentic-security-permissions-provenance-agent （curl 实取全文）
- 身份：在册 KOL（Source 10；本条为**窗口内新讲**增量）。
- 号召力口径：①＋③＋④。
- **挂钩**：无人值守运行（风险面）＋验证回路（缺陷面扩大论）＋预算与熔断（权限/来源）。
- 逐字摘录：

> "The title of my talk is, like, Agentic Security, but the real title of my talk is Be Scared."
>（自我定调：怀疑派主旋律。）

> "He stands up real quiet at the end, and he goes, 'If everyone's shipping code at the same, sorry, at 10 times faster, and the defect rate stays the same, the security defect, the vulnerability rate, then doesn't that mean that the defect surface goes up by 10X?' And it hit me so hard, I sank down to my knees… The subtle implied question is not if the defect rate stays the same. The defect rate's gonna get worse, a lot worse, with AIs writing the code."
>（**10x 缺陷面难题**——银行首席安全架构师之问＋Yegge 的"变本加厉"修正。）

> "You guys know about slop squatting? Where the AI hallucinates a package name… it downloads Graphy123, and it builds, and it runs, and the tests pass, and it looks right, but what it downloaded was a backdoor."
>（验证回路被供应链投毒穿透的实例——"tests pass"恰恰是假阴性。）

- 官方分节收口："Who watches an agent that can take action?""Prompt injection needs an owner"。
- **最小主张**：循环提速 10x 而验证不扩容＝缺陷面同比放大；新攻击面（slop squatting 等）已" incredibly well-polished"。
- **派别适配**：**怀疑票（强）**——但注意其结论是"partial answer：把安全挪到生成点"，非否定运动本身。

### 疑-2 · Jack Cable（AI 安全研究者；讲中自述 "the work that I was doing in government around the Secure by Design initiative"；曾报告数百个漏洞）· AIEWF 2026《The AI bugpocalypse is here. Now what?》（视频上传 2026-07-12）

- URL：https://ai.engineer/talks/7JgIS42mz7U-ai-bugpocalypse-is-here-now-what （curl 实取全文）
- 号召力口径：③（安全政策/漏洞研究圈号召力；非 dev-tool KOL——按口径标注为安全域 KOL）。
- **挂钩**：无人值守运行（自主度×攻击面）＋验证回路。
- 逐字摘录：

> "It's no longer autocomplete to opt-ins, not even a developer synchronously within Cursor… when we do our own development right now, it's spinning up agents from within Slack or wherever folks are working and having many agents run at once in the background. So this is a tremendous shift in how software is being built."
>（把"多 agent 后台并行"作为安全前提的既成事实陈述。）

> "Models can do a better job finding vulnerabilities. On the other hand, our attack surfaces are growing immensely, as AI becomes the default code writer… both ends of the equation shifting."
>（**双向挤压论**：自主编码扩面、自主攻击提速同时发生。）

- 官方分节："Coding and attacks become more autonomous together""Intelligence does not supply the missing threat model""Put security into the work before the pull request"。
- **最小主张**：bugpocalypse 的根源不是代码质量而是**自主度与攻击自主化的共振**；威胁模型是循环里缺失的一环。
- **派别适配**：**怀疑票（强，安全域）**。

### 疑-3 · Nick Heiner · AIEWF 2026《When Will The Benchmaxxing Plague End?》（视频上传 2026-08-02）

- URL：https://ai.engineer/talks/-npY6XjM8CQ-when-will-benchmaxxing-plague-end （curl 实取全文）
- 身份：页面无机构字段——**仅作会议层样本**。
- **挂钩**：验证回路（verifier 被反向优化的系统论）。
- 逐字摘录：

> "Why does benchmaxxing happen? Why are traditional benchmarks not always accurate reflections of real-world value? Is this intrinsic to all benchmarks, and will we ever know which models are best? And the answers are incentives, poor methodologies, no, and yes."
>（四问四答的开场定调——"是所有基准的内在属性"。）

> "We have industry leaders openly bragging about gaming LM Arena… Andrej Karpathy had a similar observation… he said, 'Unfortunately, the teams are not getting better models overall, but better LM Arena models, whatever that is. Possibly something with a lot of nested lists, bullet points, and emojis.'"
>（经讲者实取的 Karpathy 转引——verifier 被打穿的权威注脚。）

> "The verifier can reward the wrong thing… Optimizing past what people prefer."（官方分节名。）
- **最小主张**：基准层普遍被反向优化，loop engineering 的"可验证性"地基本身有内在缺陷——对推动派"verifier 万能"叙事的正面降温。
- **派别适配**：**怀疑票**。

### 疑-4 · Tisha Chawla & Susheem Koul · AIEWF 2026《Your Agent Failed in Prod. Good Luck Reproducing It.》（视频上传 2026-06-29）

- URL：https://ai.engineer/talks/Lc8zRh9muoY-your-agent-failed-in-prod-good-luck （curl 实取全文）
- 身份：页面无机构字段（同场另有其二人《FinOps for AI Agents》议题）——**仅作会议层样本**。
- **挂钩**：验证回路（可复现性缺失）＋无人值守运行（失控后取证）。
- 逐字摘录：

> "Instead of doing the math, the agent sells the raw number one thousand and dumps it straight into the quantity field… it sells one thousand shares instead. At a hundred and ninety bucks a share, a thousand dollar intent will become a hundred and ninety thousand dollars disaster… The API returned a clean two hundred OK in thirty milliseconds. Zero exceptions, zero alerts."
>（无人值守错单实录：一切监控绿灯、错单已成。）

> "The reflex here is to just turn the model temperature down to absolute zero… But that's a complete misconception. Setting the temperature to zero doesn't fix a broken reasoning path… temperature zero isn't even truly deterministic on a hardware level… The real culprit is batch variance here, because your request gets grouped with whatever else hits the server that millisecond."
>（temperature=0 迷思的四点拆解——采样确定性≠系统确定性。）

> "We've been asking the wrong question all along… The wrong question is, how do I make the model deterministic?"
- **最小主张**：agent 生产事故不可复现是常态；应记录"语义边界/执行包络"并重放状态转移，而不是追逐模型层确定性。
- **派别适配**：**怀疑票（工程实证向）**。

### 疑-5 · Dotta（Paperclip 创建者）· AIEWF 2026《What Does Done Even Mean? Agents and Paperclip's Liveness Model》（视频上传在库页实录）

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

- 官方分节："A green check mark hides different claims""Watchdogs supervise a goal across harnesses""Represent done as an object"。
- **最小主张**："done"必须是对象不是布尔（产物/证据/rubric/签核人/残余风险/下一步六件套）；控制平面必须同时保 liveness、真阻塞与有界循环。
- **派别适配**：**怀疑票（结构向）**——其方案是建设性的，但问题定性完全是怀疑派语料。

### 疑-6 · Ornella Bahidika & Joel Allou（Microsoft）· AIEWF 2026《Don't Let the LLM Drive》（视频上传 2026-07-20）

- URL：https://ai.engineer/talks/m24UKZomm7k-dont-let-llm-drive （curl 实取全文）
- 身份：Microsoft 讲者（页面 title 带机构）——**仅作会议层样本**。
- **挂钩**：停止条件（控制权外移＝对"模型自主决定下一步"的否定）＋循环结构（状态机包住模型）。
- 逐字摘录：

> "The trick is LLM is not in charge… It nails the demo, then a real user gets in, and halfway through, the agent decides it's done, or skips a state or even loops… But reliability was never a prompting problem. It's a control problem. The model is the talent, and the harness is the director. The model is brilliant at delivering a line, but it's really terrible at remembering if it's on step three of six. So we stop asking it to."
>（**"可靠性不是提示问题而是控制问题"**；agent "even loops" 作为失败模式被点名。）

> "The model never decides where we are… It proposes, but ultimately it is the harness that decides."
>（与推动派"loops 自主跑"叙事正面对冲：推进权收回 harness。）

> "Instead of having a very heavy model like a 4.7, we're actually able to rely on something like a Haiku 4.5… saving money, saving time, and saving latency."
>（控制权外移的经济学红利。）
- **最小主张**：多步 agent 的可靠性来自把"何时结束/走向何方"从模型手里拿走，放进状态机；模型只出提案。
- **派别适配**：**怀疑票（控制权向）**——对 loop 自主化路线的工程学刹车。

### 负结论与通道边界（第五轮·怀疑向）

1. **《Tokenmaxxing is the New "Lines of Code"》（Nicholas Arcolano）**：日程表在册（llms-full.md 实取）但 **/talks/ 官方页不存在**（1240 页 sitemap 核过）——逐字不可取，登记为官方摘要层待发布。
2. **Dex Horthy《Harness Engineering is not Enough: Why Software Factories Fail》**：官方页在手（Ib5GBkD555M，分节标题层已核："Why software factories fail" 系列分节），因讲者已入册（Source C），本轮不重复立条——增量在库。
3. 其余通道边界（SREcon/GOTO/ICSE/OpenSSF）见中性档负结论，不重复。
4. **判读提示（给判读层）**：本轮怀疑向的最重引句（Yegge "Be Scared"、Cable 双向挤压、Heiner benchmaxxing、Dotta liveness 两难）全部来自**推动派主场（AIEWF）的官方逐字稿**——即怀疑派证据在会议层的来源结构与 KOL 层一致：怀疑论者不是圈外人，而是运动内部的一线实践者。
