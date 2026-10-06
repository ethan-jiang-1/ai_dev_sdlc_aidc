---
type: evidence_archive
collected_by: 后台回源 agent（2026-10-06 三派分野批·反对/怀疑派路；经用户指示落种子层）
collected_at: 2026-10-06
serves: kol-roster 三派分野 / digested 三派判读 / 01_seed_reference/loop_engineering/ 三派重组
status: 全文取得 11 条（Ronacher×4、Willison×2、Orosz grief、Yegge、Hashimoto、DHH 博客索引、Ronacher Anger）；截断 3 条（Orosz what-is-loop-engineering §5–7 付费墙、Orosz 六预测 §3 后付费墙、Willison auto-mode 经本人 tag 页转载主体）；未得 5 条负结论（Kelsey Hightower、Dave Farley 逐字、DHH Rails World keynote 原文、Uncle Bob 一手、David Searls 一手——后三条本身不属于反对派或线索未核）
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

## Source 7 · Gergely Orosz《The grief when AI writes most of the code》（2026-01-07）

- URL：https://blog.pragmaticengineer.com/the-grief-when-ai-writes-most-of-the-code/ ｜ 作者身份：Pragmatic Engineer（Substack 软件工程类第一）、前 Uber/Microsoft 工程经理
- 来源类型：个人一手博客（全文取得；系 2026-01-06 newsletter 长文《When AI writes almost all code…》的单节摘出）。
- 号召力口径：④ 大分发（#1 SE newsletter）＋② 被 Fortune 等主流媒体与 arXiv 论文引用＋③ 一线访谈规模（~210 从业者回复的 loop 调查，见 Source 8）。

**逐字摘录**：

> "I'm coming to terms with the high probability that AI will write most of *my* code which I ship to prod, going forward."
（注意：Orosz 不是拒用派——他已接受 AI 写码，这正是其"损失感"证词的分量所在。）

> "It feels like something valuable is being taken away, and suddenly. It took a lot of effort to get good at coding and to learn how to write code that works, to read and understand complex code, and to debug and fix when code doesn't work as it should."
（**台账 L67 引文纠偏：原文 "something valuable"，非 "precious"**。"被夺走感"的一手原句。）

> "I wonder if I'll still get the same sense of satisfaction from the fact that writing complicated code is *hard*? Yes, AI is convenient, but there's also a loss."
（"方便但有损失"——人的角色/意义侧的怀疑票。）

**该条支持的最小主张**：分发量最大的 SE 观察者公开记录"有价值之物被突然夺走"的哀伤（grief），构成"人的角色被架空"主题的中枢证词。
**派别适配**：部分票（对 AI 写码本身不反对，反对的是对其人文代价的忽视）。

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

## Source 9 · Gergely Orosz《The Future of Software Engineering with AI: Six Predictions》（2026-02-24）

- URL：https://newsletter.pragmaticengineer.com/p/the-future-of-software-engineering-with-ai ｜ 作者身份：同上
- 来源类型：newsletter 一手（**截断**：§1–3 及 Kent Beck 峰会宣言取得；六预测本体在付费区，仅得目录句）。
- 号召力口径：同上。

**逐字摘录**：

> "Organizations are constrained by human and systems-level problems. We remain skeptical of the promise of any technology to improve organizational performance without first addressing human and systems-level constraints.
> We remain skeptical and we remain human". – Kent Beck, Laura Tacho, and Steve Yegge.
（三位入册级 KOL 在 2026-02 Fowler 峰会上联署的怀疑宣言（经 Orosz 一手报道）——对"任何技术（含 agent loop）能绕开人与系统约束提升组织绩效"的正面拒斥。）

> "Mid-level engineers' quiet crisis. Something I heard that engineering leaders talk about behind closed doors a lot is that mid-career engineers are being left behind by the AI wave."
（目录句（逐字）：中级工程师"静悄悄的危机"——人的角色分化证据。）

**该条支持的最小主张**：Kent Beck/Laura Tacho/Steve Yegge 三人 2026-02 公开联署的克制怀疑宣言；Orosz 记录的中级工程师边缘化趋势。注意：**"六个预测"本体在付费墙后未取得，本档不引用任何具体预测内容**。
**派别适配**：部分票（宣言是组织绩效层面的怀疑，不针对 loop 机制本身）。

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
2. **Kelsey Hightower——未取得一手**。搜索定位到 2026-06-12 两条警告性言论（"当 AI Agent 拿到 AWS Console 权限：『你连它搞了什么都不知道』"；"拿 Claude 取代 Terraform 管理云端，准备收拾烂摊子"，均为 ain3xt.com 对其短视频的转述）——该站 Cloudflare 403（web_fetch 实际尝试），原始发布疑在 X/短视频（不可达）。**负结论：只有二手标题级线索，逐字与一手 URL 均未核，不入册。**
3. **Dave Farley——线索已核、逐字未得**。三处独立印证其批评立场存在：① 他本人的 YouTube 频道视频《Vibe Coding Is The WORST IDEA OF 2025》（经 arXiv 2512.23982 引用表收录该视频 URL）；② GOTO G^K25 讲题《Vibe Coding – ¿De verdad esto es lo mejor que podemos hacer?》（2025-10，经 lilys.ai 转写页与 BelTech 演讲者页印证）；③ AI DevCon London 2026 讲题《Vibe Coding: Best We Can Do?》（经 Tessl registry 讲题文件印证，tessl 页面为 JS 应用，quote 文件 fetch 后无正文）。**负结论：批评对象是 vibe coding 的工程质量（而非 agent loop 机制本身）；本人视频/演讲 transcript 逐字未取得（YouTube 不可 fetch），不入册，待 transcript 回源。**
4. **Willison 2026-06 后对 "loop engineering" 的专门评论——未见**。遍查其 coding-agents tag 页 2026 年全部条目（实际 fetch，254 帖）：无以 loop engineering 为题的专门文章；他的相关发声是本档 Source 5/6 及 2026-08-08 auto-mode 安全评论。auto-mode 一条（https://simonwillison.net/2026/Aug/8/auto-mode/ ，经其本人 tag 页转载取得主体，未单独打开原帖）关键句："I would *love* to believe that Anthropic have indeed solved this problem for Claude Code users. I'm on the record predicting 'a challenger disaster for coding agents security' for 2026…But…I'd like to see more independent confirmation of this."——对 Anthropic"auto mode 已解决提示注入"大宣称的怀疑。**负结论成立，但该安全票补入 Source 5/6 旁证。**
5. **David Searls——一手未定位（本目录 README 挂"待回源"候选）**。快搜 "David Searls dark factory 2026" / "today's agents are nowhere close"：未找到承载该两句的播客/博客一手页（搜索结果只回收录了 jPl6 不相关条目与 Doc Searls 的 Wikipedia 词条）。README 所引两句（"dark factory" 10-02 播客；"today's agents are nowhere close to being able to write software that won't fall over without supervision" 02-26）线索来自库内 Ronacher 人物卡（01_seed_reference/voices/_raw_people/17_armin_ronacher.md）的卡内对照，**本档未核到一手 URL，维持"待回源"，不入册**。
6. **Uncle Bob（Robert C. Martin）——不属于反对派**。其 2026 立场（经 quidproquo.cc/InfoQ/Business Insider TW 多源转述，Bluesky/X 原帖不可达）是"不读 agent 代码、以机器纪律（Gauntlet 流水线）替代人工 review"——这是把验证全交给机器的**激进多派**，与反对派立场相反。不入册。
7. **Orosz 六预测本体**：付费墙后未取得（Source 9 已如实截断记录）。
8. **Boris Cherny（Claude Code 作者，起源派）边界证词**，经 Willison 2026-09-11 blogmark 一手转引其 X 帖："Production code written by Claude should have a higher bar than if it was written by a human."——起源派内部承认 agent 代码需更高门槛，可作三派判读的对照注脚（X 不可达，经 Willison 转引）。

## 机构研究旁证（不入 KOL 册，供判读引用）

- **METR《Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity》**（arXiv:2507.09089，2025-07-12 v1 / 07-25 v2，实际 fetch 摘要）："Before starting tasks, developers forecast that allowing AI will reduce completion time by 24%. After completing the study, developers estimate that allowing AI reduced completion time by 20%. Surprisingly, we find that allowing AI actually increases completion time by 19%--AI tooling slowed developers down."（RCT：16 名资深 OSS 开发者、246 任务，AI 使完成时间**增加 19%**，且开发者事前事后都相信是加速——感知与实际的系统性背离。）
- **arXiv:2608.21884《Loop Engineering: Building Blocks, Adoption, and Impact》**（JAWs@ASE 2026 在审 workshop 论文，2026-08-22，实际 fetch HTML 全文）：对本主题直接相关的学术整理。逐字（论文原文，其中引号内为论文转述社区言论）：
  > "The claims attached to loop engineering are substantial but rest almost entirely on anecdotes and self-reported productivity numbers, while experienced engineers voice equally strong skepticism, calling loops renamed cron jobs and warning about token costs and reviewer fatigue."
  > "Loops are 'a renamed cron job', 'automation was a thing before LLMs', and the term repackages event-driven architecture with, as one commenter put it, 'a fuzzy worker'."
  > "one experience report describes roughly eight million tokens spent in 48 hours by an over-eager CI-fixing loop"
  > "Review fatigue turns the human gate into a 'rubber stamp' while 'the pipeline still reports green', and 'the loops that stick are the ones where somebody was already paid to read the output'."
  > "comprehension debt (the gap between what exists in the repository and what the developer understands grows with loop velocity) and cognitive surrender (using loops to avoid thinking rather than to move faster on understood work)"
  （另：该论文对 36,645 仓库挖掘，确认自主 agent loop 运行于 217 仓库（0.59%）；并独立转述了 Orosz 调查结论——"most concrete examples fall into two familiar buckets, cron jobs and event-based triggers"，/loop、/goal 内建后对普通工程师 "as good as obsolete"。此转述与本档 Source 8 公开部分互证。）
- **arXiv:2512.23982《Coding with AI…》**（2025-12-30，57 条 YouTube 从业者视频的定性研究，实际 fetch HTML 主体）：主题级佐证"code review 成为新瓶颈""junior 训练场被移除""AI 削弱编程乐趣"（"AI coding is undermining the enjoyment of programming"——论文转述受访者句）。仅作氛围旁证。

## 社区情绪小节（非 KOL，不与上并列）

- Orosz loop 调查（Source 8）内的从业者原话（工程 director Oded Messer："Sometimes it feels like AI enthusiasts forgot automation was a thing before LLMs."）；arXiv 2608.21884 转述的 "tokenmaxxing" 之争（怀疑派指 AI lab 靠 loop 多烧 token 获利）；Uber 2026 年四个月烧完全年 AI coding 预算的报道线索（you.com 资源页转述，未核一手，仅记线索）。

## 对本档案的诚实评估

**这派证据是强还是弱**：机制层证据**强**——Ronacher 三篇 2026-07→09 长文构成反对派最完整的一手链（协作理解瓦解 → 无人值守失控实验 → 工具调用退化/harness 锁定），全部逐字取得；"难掌握"主题有 Willison 2026-09-24 两句净结论 + Hashimoto "excruciating" 双轨训练 + Yegge 20–25% 维护常量三源汇合；成本主题有 Ronacher 35h/$1200/79 commits、Yegge 69B token/月、Willison 预算上限主张、arXiv 论文 8M token/48h 案例四源汇合。**弱的是**：没有一个 KOL 给出"loop engineering 一词"的正面点名长文式反对——最强的词级反对恰是 Orosz（调查式怀疑："cron 旧物/here today gone tomorrow"）和社区反应（经 arXiv 论文转述）；反对派更像"机制/代价怀疑者联盟"而非成形阵营。
**覆盖缺口**：① Kelsey Hightower 的警告只有不可达的二手转述；② Dave Farley 逐字未得（需 transcript 回源）；③ Orosz 六预测付费墙内本体与 §5–7 全文未读；④ David Searls 两句线索未核到一手（README 候选位继续挂"待回源"）；⑤ x.com 上的大量怀疑派发声（Cherny 之外的 X 战场）整体不可达，本档只能经 Willison/Orosz 的一手文内转引补偿；⑥ 非英语圈（中文/日文社区）KOL 未扫——gigazine/ic.work 均为转述媒体，按纪律排除。**对三派判读的提示**：DHH 与 Uncle Bob 在 2026 年都是激进多派，若旧台账把他们当"批评声音"引用，需要改挂（DHH 已与本目录 README"易误归者"口径一致）；反对派核心名单应聚焦 Ronacher（强票）＋Willison（门槛/安全部分票）＋Orosz（价值怀疑部分票）＋Beck/Tacho/Yegge 宣言（组织层部分票）。

---

# 补抓增量（第二轮 · 2026-10-06）

> **本节为第二轮补抓，前置负结论中对应条目状态以此节为准**：上轮"负结论与边界登记" #2（Hightower）、#3（Farley）、#5（Searls）与 Source 8/9 的 Orosz 付费墙截断，状态一律以本节各小节的最新判定覆盖。
> **通道说明（必读）**：本轮会话内 `web_fetch` 工具发生 DNS 级故障（一切外部域名报 "resolves to a non-public IP address"，含上轮可用的 lucumr.pocoo.org / simonwillison.net / eu.36kr.com / web.archive.org），全部抓取改经 **bash curl（浏览器 UA）** 实取。下述每个 URL 均为真实访问（含失败尝试，如实记录状态码）；逐字引句全部出自实际 fetch 的页面/文件，无一凭搜索摘要转写。

## 增量 A · David "Doc" Searls —— 仍开放（身份已坐实；两句一手仍未定位）

- 人物：**Doc Searls ＝ David Searls**——上轮"很可能是 Doc Searls"的猜测**坐实**：Wikipedia 词条 https://en.wikipedia.org/wiki/Doc_Searls （curl 实取）载 "David (born July 29, 1947) is an American journalist, author, and blogger"，Linux Journal 长期编辑、Project VRM 创立者、Cluetrain Manifesto 合著者（后三项亦见 The AI & I Show 官方 guest bio，zeno.fm 实取）。
- 待核线索（来源：Ronacher 人物卡 01_seed_reference/voices/_raw_people/17_armin_ronacher.md）：**"dark factory"（2026-10-02 播客自嘲："how I've accidentally constructed a dark factory with agents building and maintaining my iOS apps"）**；**"today's agents are nowhere close to being able to write software that won't fall over without supervision"（2026-02-26）**。
- 已尝试通道（全部实际 fetch，未命中目标句）：
  1. **doc.searls.com WordPress 全文检索 API**（curl 实取）：`/wp-json/wp/v2/search?search="dark factory"` → **0 命中**——该词在其博客全文中不存在；`search=nowhere close` → 唯一命中《The Kids Take Over》（https://doc.searls.com/2026/04/13/the-kids-take-over-2/ ，实取全文核读：讲高中生构建 app 的纪实，**无该句**，系无关词碰撞）。
  2. **2026-02-26 当日归档与其唯一帖《Back and (Go) Forth》**（https://doc.searls.com/2026/02/26/back-and-go-forth/ ，实取全文）：内容为 MyTerms/隐私主张、白内障手术恢复自述、Summit on Human Agency 上与 Sheila Warren 的 15 分钟访谈要点——**无 agents 句**。（上下文收获：02-26 前后他正忙于隐私议题与人身恢复，与"02-26 发表 agent 定调句"的场景难吻合，卡内日期存疑。）
  3. **2026-10-02 帖《Lintlinks》**（https://doc.searls.com/2026/10/02/lintlinks/ ，实取全文）：Zoom"workspace"吐槽＋债市＋Meta 广告杂拌——**无播客预告、无 dark factory**。
  4. **category/ai 页第 1–2 页**（实取）：无 iOS app/agent 自述帖（仅链接他人文《The Week AI Agents Got Hands》）。
  5. **播客侧三路排查**：Reality 2.0 官网 reality2cast.com（实取：最新 Ep159 = 2025-10-08，2026 年休眠，无 10-02 集）；The AI & I Show 的 Doc 单集（zeno.fm 实取：2025-11-02 首集，主题 Personal AI/隐私，日期与主题均不符，排除）；podnews《Podcasts with Doc Searls》（实取：仅列 2023 年条目）。
  6. **精确短语 web_search**（"accidentally constructed a dark factory" / "agents building and maintaining my iOS apps" / "nowhere close to being able to write software" / "won't fall over without supervision" 四组）：**全部零命中**。
- 状态：**仍开放**。两句逐字的一手载体（播客音频页/转写页/博客帖）均未定位，且"10-02 播客"究竟是哪个节目未能确认（两条最像的线 Reality 2.0 与 AI & I Show 均排除）。维持"待回源"，**不入册**。
- **派别含义一句话**：候选资格与怀疑倾向继续挂起——没有一手，此人仍不产生任何票。

## 增量 B · Dave Farley —— 部分解决（两场演讲逐字到手；载体为第三方转写，引用须降半级标注）

- 人物：Dave Farley（Continuous Delivery 先驱、YouTube 频道作者）｜ 日期：GOTO G^K25（转写页 slug `vibe-coding-20251026`，即 2025-10-26）与 AI DevCon London 2026（会期第 5 天末场）。
- **通道突破①（AIDEvCon London 2026《Vibe Coding: Is this really the best we can do?》）**：tessl.io registry 本体是 JS 应用壳（直接 quote.md 路径、`?raw=true`、`/api/` 端点三种姿势 curl 实取均只回壳页）——但经 api.github.com 树检索定位其 **GitHub 镜像仓库 jscraik/Agent-Skills**，`raw.githubusercontent.com` 实取三件套（`quote.md` 5.1KB / `outline.md` 9.8KB / `transcript.md` 31.9KB，路径 `Plugins/aidevcon/skills/talk-farley-vibe-coding-best-we-can-do/`）。逐字（quote.md 自注"All quotes are verbatim from transcript.md"）：

> "I would argue that vibe coding programming with natural languages. While having a place. Are also kind of bad ideas."（§3）

> "Vibe coding alone is simply not good enough if we're just chatting with the computer to express our needs. That's not enough."（§8）

> "AI generated tests. If the code is the only input, we can only verify that the code remains the same. … So they're mostly a dumb idea. They have a, they have a place, but mostly a dumb idea. They tend to be a copper [cop-out] for people who don't, can't be bothered to state their goals."（§4；转写自注 "copper" 为 "cop-out" 误转）

> "He reckons he may, he writes 12,000 lines of code per day. No human being can review 12,000 lines of code per day. No human being can test, manually test the output of 12,000 lines a day behaviorally to figure out whether it's doing the right things."（§10）

> "We sped up the coding bit. That was the easy part of software development … But it also moves the bottleneck. If you've ever read The Goal, the theory of constraints, that's what we've done."（§9）

- **通道突破②（GOTO G^K25）**：lilys.ai 转写页（https://lilys.ai/es/notes/vibe-coding-20251026/dave-farley-vibe-coding-future-programming ，curl 实取 329KB）逐字：

> "I think vibe coding, programming with natural languages, all of these, this is essentially my agenda … I am going to explain why I think these are bad ideas, but I do think that they're bad ideas."

> "Everybody's talking about vibe coding a lot at the moment, and that's kind of instructing a computer via natural language and having a conversation with it until it comes up with with with a solution that we like … does it help us to organize our thinking about a problem? No, because natural language is too vague."

> "There are some of the agentic tools that are a little bit more predictable than most of the LLMs, but most of the LLMs, if you diff the code that was generated between even a small change, it's basically all of it, it changes."

- 正面纲领（同一 transcript，§11–12）：**"A program will be a precise description of what it is that we want, I think, and coded as specifications translated into execute or [executable] instructions by the AI that will verify that we got what we wanted."**＋"We can verify that the AI is doing the right thing by giving test test values that it hasn't seen before, so it can't cheat the tests."
- 排除通道：davefarley.net（实取：2022 年后停更的旧 weblog，无 2026 内容）。
- ⚠️ 引用纪律：transcript 自带 attribution 警告（无逐说话人标注、含语音转写伪影；MC 场务话术不得归 Farley）。两场转写均为第三方转写级，入册按"本人演讲·经转写"降半级标注。
- 状态：**部分解决**（上轮"逐字未得"→本轮两场逐字到手；YouTube 原片仍不可达）。
- **派别含义一句话**：Farley 的反对票坐实为"对 vibe coding 工程质量的反对"——其正面纲领是 executable specification / ATDD（spec-driven 词表），与"反对 agent loop 机制"不是同一命题，判派时须分列。

## 增量 C · Kelsey Hightower —— 仍开放（通道穷尽式失败，负结论加固）

- 待核线索（同上轮）：2026-06-12 两条警告——AWS Console 权限"你连它搞了什么都不知道"；拿 Claude 取代 Terraform"准备收拾烂摊子"（载体疑为其 28 秒短视频）。
- 已尝试通道（全部实际 fetch/attempt）：
  1. ain3xt.com 两篇原文直取（curl 实取）：**403（Cloudflare）**；换 Googlebot UA 重试：仍 403。
  2. web.archive.org 快照查询两篇 URL：**404 无快照**。
  3. r.jina.ai 阅读代理：**403**（源站 Cloudflare 连代理一并拦截）。
  4. 其他转载排查：腾讯云《DevOps重构：从Vibe Coding到VibeOps》（cloud.tencent.cn，实取全文）只有他另一句 "如果20年后我们还在谈论Kubernetes，那是技术界的悲哀"——非目标句；threadreaderapp/unrollnow 无其 thread 命中（unrollnow 本身 503 两试）；kelseyhightower.com 域名解析失败（curl 000，无站点）。
- 新线索（仅搜索层，未 fetch 到正文）：ain3xt 另有第三篇《28 秒讲完一个道理》（证实原始载体为 28 秒短视频）及其 tag 页 `ain3xt.com/tags/kelsey-hightower/`。
- 状态：**仍开放**。两条警告的逐字与一手 URL 均未核得，**不入册**；ain3xt 三篇的标题级信息继续只作检索线索。
- **派别含义一句话**：云运维侧的"失控警告"候选继续挂起，无票。

## 增量 D · Peter Steinberger 07-18 推文 —— 部分解决（两个独立全文转载锚定文本/日期/浏览量；X 原文仍不可达）

- 人物：Peter Steinberger（OpenClaw 创作者、词源人物，已入职 OpenAI）｜ 日期：2026-07-18 ｜ 原载体：X（本环境不可达）。
- 已取全文的独立转载两路：
  1. **36氪英文版**《Father of Lobster's Viral Tweet: Has the Loop Era Officially Ended?》（https://eu.36kr.com/en/p/3904771418867330 ，curl 实取全文）——推文文本：**"Are we still talking about loops, or have we moved on to graphs?"**；事实参数（该转载原句）："On July 18, 2026, Peter Steinberger quietly declared the end of the loop engineering era with this single sentence on X. The post garnered 2.6 million views within two days of its publication."；并上溯其前帖：'Six weeks earlier, he earned 8.4 million views with the phrase "design loops that prompt agents."'（该文另载 Steinberger 六月推文完整版："Monthly reminder: you should no longer prompt programming agents yourself. You should design loops that prompt agents."——可补 evidence-a 词源推文的多版本对照表）。
  2. **KuCoin News Flash**（https://www.kucoin.com/news/flash/peter-steinberger-announces-end-of-loop-engineering-era-shift-to-graph-engineering ，curl 实取全文）——同一推文、同一日期与 2.6M views；文本微差版："Are we still discussing loops, or have we already moved on to graphs?"（两版并存如实记录）；承接叙事："the static Org Graph and the dynamic Work Graph"。
- 排除通道：aibuilderclub.com（curl 实取但正文 JS 渲染无可提取文本）；cnblogs（实取：仅中文转译"我们还在讨论循环结构的问题吗？还是已经转向了图论领域了呢？"）；unrollnow（503 两试）；X 本体不可达。
- 状态：**部分解决**（上轮"仅 InfoQ/36kr 转述"→本轮双独立全文转载、日期/浏览量一致；推文 ID 与 X 原文页仍未取得）。
- **派别含义一句话**：词源人物的"Loop 时代终结"宣言有双转载锚点，但其性质是**推动派内部换词表（loop→graph）**，不是转向反对——判派维持本体在推动派，轨迹注记加这一条。

## 增量 E · Orosz 付费墙 —— 仍开放（边界双通道复证；无新的公开节选）

- 人物：Gergely Orosz（The Pragmatic Engineer）｜ 对象：07-14《What is "loop engineering?"》§5–7 与 02-24《The Future of Software Engineering with AI: Six Predictions》本体。
- 已尝试通道（全部实际 fetch）：
  1. https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering （curl 直取全文 HTML）：公开部分仍止于 §5–7 大纲句（"Disappointment and 'tokenmaxxing'"／Max Kanat-Alexander "temporary hack"／"Does 'context engineering' matter more for devs?"——与上轮逐字一致），正文止于 **"This post is for paid subscribers"**。
  2. 六预测文的 `isFreemail=true` 邮件变体 URL（curl 实取全文 HTML）：免费部分（Fowler 峰会、"Mid-level engineers' quiet crisis"、Beck/Tacho/Yegge 宣言）同上轮；**付费墙位置不变**。
  3. 韩文转载候选 wikidocs.net（curl）：403；其余搜索命中的韩文/中评论帖均为评论文章非原文节选。
- 状态：**仍开放**（维持上轮截断记录；六预测本体与 §5–7 正文继续**不可引用**）。
- **派别含义一句话**：Orosz 的"中性偏怀疑"判定不受影响——付费墙内内容继续缺席判定依据。

## 第三轮挖掘（2026-10-06）：新 KOL（怀疑向）

> **本轮通道状态总览**：web_fetch 对多数域名报解析异常，全部改 curl＋浏览器 UA 实取；x.com 不可达维持已知事实。本轮怀疑向最大新增载体是 **The Weekly Dev's Brew Ep20（David Cramer，2026-06-30）**——主持人页内自备 Pull Quotes 与全 transcript，逐字层级高于媒体转述、低于本人署名博客。

### 增量 F · David Cramer（Sentry 联合创始人/CTO）· The Weekly Dev's Brew Ep20（2026-06-30）

- 主票 URL：https://www.wordman.dev/podcast/david-cramer-ship-real-production-code-with-ai/ （curl 实取：官方 Key Takeaways＋Pull Quotes＋页内全 transcript；页标 30 Jun 2026，Episode 20）
- 身份：Sentry 联合创始人（主持人 bio：co-founder and CTO；另档 Insecure Agents 标 CPO——两说并存如实登记）；bio 自述 "one of the few people on a C-level who's actually using AI to ship production software at Sentry"。
- 号召力口径：③＋④（近 10 万家公司使用的监控平台创始人；开发者社区高可见度）。
- 逐字摘录（Pull Quotes，页面实取）：

> "So this 100X thing is BS. The only way you get more done is when you generate junk that you don't need."

> "LLMs are not making it faster for me to build software. Despite what the internet would like to say, I'll sit here all day long on a single patch."

> "If I ship something that has massive vulnerabilities in Sentry, that could cause the company to disappear."

> "There is nobody that is credible that says software engineering as a craft is completely changing."
>（直接否认"软件工程手艺剧变"论——对整个 loop engineering 运动的元层面降温。）

- transcript 开场段（页面实取）："Because we went from like tab complete to instantly we just don't write code anymore. And it's like, maybe we should have stopped somewhere in between."
- 官方 Key Takeaways（host 撰）："The 100x developer narrative breaks down once you optimize for quality, security, and maintainability instead of raw output."＋"David built Warden inside Sentry and used it to find more than 100 previously unknown vulnerabilities in production code, including auth bypasses."＋"Search and internal knowledge tools may be the highest-leverage LLM use case inside a company today, **not autonomous code generation**."
- 章节锚点："7:00 · No 100X developers"、"35:29 · Vibe coding limits"。
- 辅票 1（存在性已核、正文未取——iHeart 406）：Insecure Agents（Socket 出品，host Allie Howe）单集《It's the Harness, Not the Model: David Cramer, CPO of Sentry, on Agents, Expectations vs Reality》。
- 辅票 2（**窗口前**，2026-03-17，经快讯转述）：KuCoin/BlockBeats 快讯（KuCoin 页实取）："Sentry co-founder David Cramer warned that large language models (LLMs) may harm long-term…He criticized 'agentic engineering' and cited OpenClaw as an example of unsustainable code generation."——窗口前发声，佐证其立场连贯性，不计窗口票。
- **最小主张**：100x 是 BS；LLM 未让他更快造软件；自主代码生成不是企业最高杠杆用例；质量/安全/可维护性优先时"产能叙事"崩塌。
- **派别适配**：**怀疑票（强）**——质量与安全轴上对 loop engineering 前提（更多代码=更多进展）的正面否定，同时保留"自己用 AI 发生产软件"的采纳面（判读时两面分开）。

### 增量 G · Greg Pstrucha（Subroutine）· AIEWF "great loops debate" 反方经济学质疑（2026-07-02 场）

- URL：https://www.latent.space/p/aiewf-daily-dispatch-locomotives （Richard MacManus 现场稿，07-03 发，curl 实取全文）
- 身份：Subroutine（agent 基础设施公司）代表；AIEWF 收官辩论反方席（与 Dex Horthy 同侧）。
- 号召力口径：②（AIEWF 主舞台辩手）；①③④均弱——新名，个人一手未取。
- 逐字（经现场稿转述）：

> "orchestrate your problems away by buying more tokens"
>（现场稿记其立场：agentic loops 的**经济可持续性**不成立，"was mainly concerned about the economic viability of agentic loops, which he said wasn't sustainable"。）

- **最小主张**：loop 不解决的恰恰是成本结构——"买更多 token"不能把问题编排掉。
- **派别适配**：**怀疑票（会议层票）**——怀疑派此轮唯一的经济轴正面发言；其余一手开放。

### 增量 H · Dillon Mulroy（Cloudflare 首席工程师）· The Weekly Dev's Brew Ep22（2026-09-10）

- URL：https://www.wordman.dev/podcast/dillon-mulroy-i-enjoy-coding-less-than-ever/ （curl 实取：Key Takeaways＋章节＋页内全 transcript；页标 10 Sep 2026，Episode 22；@dillon_mulroy / @dmmulroy）
- 身份：Cloudflare principal engineer。
- 号召力口径：③。
- 逐字/半逐字（官方 Key Takeaways，host 撰、页面实取）：

> "Lab-style agent loops are impractical for a median developer at today's prices. He wants receipts before treating them as the default."

> "Anthropic Fable is a non-starter for a company like Cloudflare, he says, because it does not ship with zero data retention and can drop a session onto Opus 4.8."

> "A single human still owns the output. Greater reach in less time means more review, not less."

> "He is more productive and less happy because the small implementation hits that created flow are gone. The day is one hard design problem after another."

- 页面定位句（host）："…why **lab-style agent loops are a poor default for most teams**, and how he keeps a model on a short leash with Ghostty, Herdr, Pi, and Plannotator."
- 章节锚点："1:18 · From bearish to all-in"、"10:02 · I enjoy this work less"。
- **最小主张**：对"无人值守 lab 式 loop 默认化"要收据（receipts）；一条人命仍对产出负责→更多产出=更多 review；个人产出上升与职业幸福感下降并存（一手实证的"产能-幸福感背离"）。
- **派别适配**：**怀疑票（对 loop 默认化）**——注意拆分：对 AI 采纳本身是推动（"from bearish to all-in"、已数月不亲写代码），怀疑的靶心是"把 lab 式 loop 当默认工程实践"；判读层引用时两半都要写。

### 负结论（第三轮·怀疑向）

1. **Cramer 的 X 原文**不可达（环境已知事实）；2026-03-17 快讯为两级转述链（X→KuCoin/BlockBeats→本档），只作立场连贯性旁证。
2. **Insecure Agents Cramer 单集**日期未核（iHeart 406）——开放。
3. **Greg Pstrucha** 除现场稿外无任何一手（Subroutine 公司博客未扫）——开放。
4. **撞名与身份核查**：sindre-ai（GitHub API 实核 2026-03-25 注册、0 followers）≠ Sindre Sorhus，maskin 仓库不入册；Kent Beck ≠ Kent C. Dodds 已在库。
5. 本轮新怀疑票均非"loop 时代终结"式宣言（那条仍在册的 Steinberger 头上）——本轮怀疑派的声音集中在**质量轴（Cramer）、经济轴（Pstrucha）、默认化轴（Mulroy）**三轴，恰好补齐怀疑派对 loop engineering 三类反对理由的样本。

## 第三轮挖掘（2026-10-06）：厂商自认边界与限制

> 本轮面：coding agent 厂商官方一手内容中"承认限制/回撤/风险"的条目（2026-06-01 之后；无日期 docs 页标注"living docs，实取 2026-10-06"）。与推动面文件（01_advocates/raw_scan_2026-10-06_advocates.md 第三轮节）同源同通道：curl＋浏览器 UA 直取，`.md`/API 官方载体优先；全部引句实取，未编造。厂商推送面（产品卖点）证据在推动面文件，本文件只收自认面。

### 增量 A · OpenAI —— 官方回撤：`untrusted` approval policy 废止

- 厂商/产品：OpenAI / Codex CLI & ChatGPT Work
- URL：https://learn.chatgpt.com/docs/agent-approvals-security.md （官方 `.md` 直取，living docs，实取 2026-10-06；页面自述 "Markdown versions of documentation pages are available by appending `.md`"）
- 逐字摘录：

> "Codex and ChatGPT Work no longer support `approval_policy = "untrusted"`. The retired setting can prevent either client from starting. Remove it from user or project configuration, profile files, startup scripts, and managed defaults."

> "With `on-request`, commands allowed by the sandbox can run without approval, read accessible files, and use network access if enabled."

- 该条支持的最小主张：OpenAI 官方**废止了一个审批档位**（untrusted→retired），且替代路径 `on-request` 允许沙箱内命令免审批直接跑（含网络）——审批门的最新演进方向是收窄而非收紧，属于厂商对自身安全档位的主动回撤（用户侧须自行改配置，改不动会"prevent either client from starting"）。
- 派别适配：**怀疑·厂商自认**（机制回撤；与推动面增量 E 的"must stop and ask"并存——官方一手同时呈现"有门"与"门在变窄"）。

### 增量 B · OpenAI dots —— 自主规则"尽力遵循、会出错"＋停止语义三层切割

- 厂商/产品：OpenAI / dots（常驻自主 agent）
- URL：https://learn.chatgpt.com/docs/dots/controls.md ＋ https://learn.chatgpt.com/docs/dots/tasks-and-memory.md （官方 `.md` 直取，living docs，实取 2026-10-06）
- 逐字摘录：

> "They are instructions your dot tries to follow, and it can make mistakes. They don't grant access to an app or computer, override built-in safety requirements, or remove required confirmations such as approval to use a saved login."

> "**Pause** stops your dot's current main task. It doesn't stop every delegated task or cancel future scheduled runs."＋"Open a delegated task in **Activity** to inspect and stop that task."＋"Stopping work doesn't undo completed actions. Review active tasks and schedules separately."

> "Deleting your dot doesn't undo changes already made in connected apps or recall messages already delivered to other people."

- 该条支持的最小主张：常驻自主 agent 的"停止"在官方文档里不是单一开关，而是**三层各自为政**（pause 主任务≠停委派任务≠停计划任务），且规则层明示"尽力遵循、会出错"、外溢后果不可撤——厂商自认"停下"与"收回"是两个问题（停止≠回滚）。
- 派别适配：**怀疑·厂商自认**（把控性主题一手：常驻 agent 的停止语义缺口由官方亲手写出）。

### 增量 C · Warp —— "Run until completion" 默认击穿自家 denylist

- 厂商/产品：Warp / Agent（Run until completion）
- URL：https://docs.warp.dev/agents/capabilities/agent-profiles-permissions （官方 `.md` 直取，页面页脚 "Last updated Oct 6, 2026"）
- 逐字摘录：

> "Caution: *Run until completion* is the purest form of "YOLO" mode: the Agent proceeds without asking for confirmation, and by default it also runs commands that match your command denylist."

> "To keep your denylist in force during *Run until completion*, turn off **Allow auto-approve to bypass command denylist** in **Settings** > **Agents** > **Warp Agent** > **Input**. Denylist rules your team enforces through the Admin Panel always require approval and are never bypassed."

- 该条支持的最小主张：Warp 官方文档以 Caution 自认：任务级全自主模式**默认绕过用户自设的黑名单**（企业 Admin 层除外）——安全层是否生效取决于用户是否找到并关闭一个默认开启的设置项。
- 派别适配：**怀疑·厂商自认**（"把控性"最锋利的一手：厂商把"最纯粹 YOLO"做成默认击穿安全层的开关并自己标警）。

### 增量 D · Factory —— 官方自认"命令规则不是操作系统级隔离"

- 厂商/产品：Factory / Droid（Autonomy Level & permission rules）
- URL：https://docs.factory.ai/cli/user-guides/auto-run （living docs，实取 2026-10-06）
- 逐字摘录：

> "Warning: Command rules are not operating-system isolation. Prefixes do not cover every equivalent command spelling or inspect arbitrary script behavior. Use sandboxing, managed hooks, and least-privilege credentials for additional protection."

> "An allow rule grants permission; it does not prove a command is read-only."

> "`--skip-permissions-unsafe` skips all permission prompts, but command blocks still apply."

- 该条支持的最小主张：权限闸（allowlist/denylist/autonomy 分档）的**语义边界**由厂商亲口承认——规则匹配挡不住等价拼写与脚本内行为，allow 也不蕴含只读；自主度分档之上还需要沙箱/凭证层，否则闸门是"匹配级"而非"隔离级"。
- 派别适配：**怀疑·厂商自认**。

### 增量 E · Replit —— 并行委派的官方边界（"Parallel building is a tool, not a rule"）

- 厂商/产品：Replit / Agent tasks（Build in parallel docs）
- URL：https://docs.replit.com/learn/build-in-parallel （living docs，实取 2026-10-06）
- 逐字摘录（"When to stay sequential"整节）：

> "Parallel building is a tool, not a rule. Stay in the main conversation, one thing at a time, when: Two ideas touch the same screen. "Redesign the home page" and "change the navigation" will collide. Do them in order."

> "You're exploring. In design work, the result of one attempt changes what you want next. Exploration is a conversation, not a work order."

> "You can't describe the task in one sentence. If you can't state it simply, you're not ready to delegate it."

> "Your attention is a limit, too. Start with two tasks. If reviewing them feels comfortable, try three. You don't need to supervise every step, but you still need to test each result before applying it."

- 该条支持的最小主张：把并行无人值守做成卖点的同一家厂商，在官方文档里承认委派有三个硬前提（互不碰撞、非探索、一句话可说清），且**人的注意力是并发上限的一部分**（官方建议并发从 2 开始）——"review 是新瓶颈"的厂商侧一手表述。
- 派别适配：**怀疑·厂商自认**（与推动面增量 B4 同页两面并存）。

### 增量 F · Replit —— 单分数评测被官方判不可靠（评测被迫移入 improvement loop）

- 厂商/产品：Replit / Agent 评测体系
- URL：https://replit.com/blog/evaluating-and-improving-agent-at-scale （2026-06-23/24 实取）
- 逐字摘录：

> "The old loop made evaluation feel bounded. But Replit Agent changes too quickly for a single score to carry the whole decision. A score can compare two candidates on one slice of tasks. It cannot explain what users care about, where production is breaking, or what to improve next."

> "The shape is analogous to the Swiss cheese model in safety engineering: each layer has holes, but together they catch more than any one layer can."

> "No layer is enough on its own."

- 该条支持的最小主张：厂商官方承认单点 eval 分数不足以支撑发布决策（模型/提示词/工具/产品面变得太快），被迫把评测改造成多层冗余的连续环——**"评测不可靠"是改进环的成因**，不是其优点。
- 派别适配：**怀疑·厂商自认**（对 goal/eval 主题：厂商自己论证了"单一 goal 分数会失效"）。

### 增量 G · Devin/Cognition —— 生产力测量方法论自认（LLM 时间估计不可靠、个体预测不完美）

- 厂商/产品：Cognition / Devin（AI Productivity Guarantee & estimator）
- URL/日期：① https://cognition.com/blog/ai-guarantee ② https://cognition.com/blog/ai-productivity （均 datePublished 2026-06-04，JSON-LD 实取）
- 逐字摘录（②方法学）：

> "LLMs are notoriously bad at time estimates — so we expected this to be a struggle."

> "Individual predictions aren't perfect, but the model is good enough to be used for estimating aggregated totals."

> "Ideally, we'd measure dollar impact directly, such as revenue attributable to features shipped or costs avoided by bugs fixed. In practice, this is still an unsolved problem in our field. It's incredibly hard for an engineer to know how many dollars of business value they created through the PRs shipped last week."

（①边界节）：

> "No single estimate is perfect, but across many tasks with varying complexity, the highs and lows average out. This produces an estimate of engineering productivity from agents — hours of useful output. It does not replace measuring ROI, which requires deeper context on the business value of each task."

（②浪费面）：

> "not every token delivers real value. Some save engineering hours and accelerate projects; others are wasted on useless sessions and bad prompting."

- 该条支持的最小主张：厂商在为自主 agent 生产力做 $10M 担保的同一篇套文里自认： Dollars 级 ROI "仍是本领域未解问题"、LLM 时间估计"出了名地差"、单会话预测不完美只宜聚合使用、且"不是每个 token 都有真实价值"——**担保的置信基础是聚合统计而非单次可靠性**（数据集仅 258 sessions / 126 users，页面实取）。
- 派别适配：**怀疑·厂商自认**（一手承认自主环产出的度量基础薄弱；判定时与推动面增量 F1 的对赌主张配对使用）。

### 增量 H · Devin —— ACU 双门闩控制机制整体处于 beta

- 厂商/产品：Cognition / Devin Enterprise（Usage policies）
- URL：https://docs.devin.ai/enterprise/features/usage-policies （living docs，实取 2026-10-06）
- 逐字摘录：

> "Per-user ACU limits are in beta and require enablement for your enterprise. Reach out to your account team to turn them on."

> "and new work is blocked on all surfaces once the limit is reached."

- 该条支持的最小主张：预算硬阻断机制（任一上限触顶即全表面阻断）官方标注 **beta 且需联系客户团队才能开**——把"烧钱环"关掉的能力尚未默认在所有企业客户手中。
- 派别适配：**怀疑·厂商自认**（把控机制的成熟度自认；机制本体见推动面增量 F4）。

### 增量 I · Kiro —— Automations 官方承认无人值守模式会被仓库内恶意指令劫持

- 厂商/产品：AWS / Kiro Web（Automations＝定时自主运行）
- URL：https://kiro.dev/docs/web/automations/ （living docs，实取 2026-10-06）
- 逐字摘录（官方 Warning 原文）：

> "Warning: Only select repositories you trust, especially when mixing public and private repos. The agent learns from and follows instructions in the repository code, even if those instructions are malicious."

- 该条支持的最小主张：AWS 系厂商在"无人在场的定时自主环"产品文档里以 Warning 形式自认：agent 会遵循仓库内的恶意指令——无人值守环的 prompt-injection 风险被官方写成使用前提（用户须以"信任仓库"自担）。
- 派别适配：**怀疑·厂商自认**（loop 治理"环境轴"的一手风险表述）。

### 增量 J · GitHub Copilot —— 官方文档自认"日志不能替代你的审查与测试"

- 厂商/产品：GitHub / Copilot cloud agent（coding agent）
- URL：https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent （living docs，实取 2026-10-06；现行页面用词 "Copilot cloud agent"，与 changelog 的 "coding agent" 并存）
- 逐字摘录：

> "Logs do not replace your own review and testing. See Managing agent sessions."

- 该条支持的最小主张：官方在 agent 会话可观测性文档中自认：会话日志只是证据面，审查与测试义务仍在人——自主任务的"透明度"不等于"通过验收"。
- 派别适配：**怀疑·厂商自认**（一句话级，但位置在 agent 主文档正文）。

### 增量 K · Gemini CLI —— 官方 release note 自证"auth 无限循环"失控 bug

- 厂商/产品：Google / Gemini CLI（官方仓库 google-gemini/gemini-cli）
- 通道：https://api.github.com/repos/google-gemini/gemini-cli/releases （官方仓库 release note，2026-09-29，v0.63.0-nightly.20260929.gfe6350238 实取）
- 逐字摘录：

> "fix(auth): prevent infinite auth loop from file contention, headless keyring, and supervisor state drops (#28341)"

- 该条支持的最小主张：官方一手修复记录承认该 agent CLI 曾出现**无限循环**（auth loop，由文件争用/无头钥匙串/监督态掉落触发）——"环不终止"在工具自身基础设施层的实证案例（与模型行为无关，是 harness 层失稳）。
- 派别适配：**怀疑·官方一手**（非 CEO 姿态表达，而是 changelog 级自证；引用时注明 nightly release 载体）。

### 增量 L · 本轮负发现与缺口（逐条列通道，供第四轮）

- **术语缺口**：本轮全部官方载体中，无一家厂商文档使用 "loop detection" 或 "circuit breaker" 术语；最接近的官方机制为 Kiro PreToolUse 阻断（docs）、Factory safety checks（docs）、Devin 双门闩（docs）、OpenAI dots action review（docs）、Sierra merge approval＋split traffic（2026-08-20 博客）。"把控性"主题若要引"循环检测/熔断"，目前只能落在机制层而非术语层——如实登记。
- **openai.com/index/dots/**：直取被 JS 盾拦截（9969 字节空壳，浏览器 UA 两式同）；wayback 查询 429 限流——dots 发布日期未在一手核实（docs 状态 "rolling out gradually"，实取 2026-10-06）。第四轮可走 wayback 退避重试或 help.openai.com 通道。
- **"/bo" 未定位**：最接近候选为博云 BoClaw（bocloud.com.cn 官方页实取，发布时间 2026/3/9——窗口外，且为个人 AI 助手平台非 coding agent loop 面）；若另有所指仍开放。
- **窗口外机制在册**（引用须标窗口外）：Jules Planning Critic for Auto-Approved Plans（2026-01-26）、Scheduled Tasks（2025-12-10）、Devin Manage Devins（2026-03-19）、Replit Agent 4 并行任务系统（2026-03-23）、GitHub budget tracking changelog（2025-11-03，见上轮库存）。
- **Gemini CLI 判读注记**：窗口内官方增量以 nightly release note 为主（"autonomous plan execution in non-interactive mode"，2026-09-30）——载体级别低半档，引用时注明。
