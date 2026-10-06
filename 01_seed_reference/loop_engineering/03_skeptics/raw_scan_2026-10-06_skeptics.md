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

