---
type: kol_evidence
directory: 03_skeptics/kol_tech
observation_date: 2026-10-06
---

# ronacher — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

**对抗轴**：与 Thorsten Ball（[_raw_people/19](../../../../01_seed_reference/voices/_raw_people/19_thorsten_ball.md)，Amp/乐观极）公开互驳——#99 点名引 Astra 冷水面，Armin 零回应，单向敞开。

## Armin Ronacher《Better Models: Worse Tools》（2026-07-04）

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

## Armin Ronacher《The Tower Keeps Rising》（2026-07-13）

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

## Armin Ronacher《Anger, Anxiety and Agency》（2026-08-24）

- URL：https://lucumr.pocoo.org/2026/8/24/anger-anxiety-agency/ ｜ 作者身份：同上
- 来源类型：个人一手博客（全文取得）。本条为增量（台账"十篇"清单补全）。

**逐字摘录**：

> "For me, the emotions I would expect in tech vis-a-vis these new developments are disorientation and anxiety, but not anger."
> "Some days that feels liberating, but on others I wake up feeling like the ground is crumbling beneath me."
（怀疑派的情感底色：不是愤怒而是失向与焦虑——连最头部的实践者也在"地基塌陷"感中工作。）

**该条支持的最小主张**：一线头部实践者公开承认对职业未来的失控感（anxiety/disorientation）。
**派别适配**：部分票（情绪证词，非机制论证）。

## Armin Ronacher《Astra for Coding: Why Are We Doing This Again?》（2026-09-07）

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
