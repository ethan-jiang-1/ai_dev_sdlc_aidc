---
type: kol_deep_dive
person: Armin Ronacher
organization: Independent (Flask/Werkzeug author; Pi/earendil-works collaborator)
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://lucumr.pocoo.org/2026/9/7/astra-why/
  - https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/
  - https://lucumr.pocoo.org/2026/6/23/the-coming-loop/
  - https://lucumr.pocoo.org/2026/8/24/anger-anxiety-agency/
  - https://lucumr.pocoo.org/2026/9/12/pdoom/
  - https://lucumr.pocoo.org/2026/1/18/agent-psychosis/
key_concepts:
  - neijuan_involution
  - slop_factory
  - better_models_worse_tools
  - human_taste_gatekeeping
  - the_coming_loop
  - ground_crumbling
---

# Armin Ronacher — "内卷派"主笔：模型更强，工具更糟，工厂交白卷

> Flask/Werkzeug 作者，Rust/CPython 社区活跃者，Pi（earendil-works）协作者。2026 年发文 32 篇（01-14 → 09-29），其中 7→9 月的密集批判期——"Better Models: Worse Tools"、"内卷（Neijuan）"、"slop factory"——使他成为"宽自主工厂叙事"最重要的质量反证派，并与 Thorsten Ball（`19`）形成公开互驳轴。**2026 年内的弧线是本库最清晰的"转冷"轨迹**：从年初的重度信徒，走到 9 月判定 AI 工程是一场内卷。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。建卡日 2026-10-03；同日按 32 篇全年清单 + Bluesky 旁证深挖重构。

## 当前立场小结（2026-10-03）

1. **AI engineering = 内卷**："I'm more and more convinced that all of AI engineering is **Neijuan (内卷, meaning curl inwards)**. … That's how I feel about AI right now."（09-07）
2. **对"agent-only 代码库"留了一个口子**："Astra is in my mind 'objectively bad'. But it's objectively bad **by my human sense**. Maybe it's objectively good for a codebase that is entirely written by agents and only needs to be understood by agents."
3. **工具侧反证**：SOTA 新模型（Opus 4.8 / Sonnet 5）在第三方工具 schema 上反而比旧模型差（07-04，详见轨迹 P3）。
4. **忧虑的对象是人，不是灭绝**："**I don't think AI is going to usher in an extinction event.**"（09-12，反 Dario pacing——忧的是 "what this does to us as humans"）。
5. **收束回纯工程**：09-29《Deser》（Rust 序列化）之后回归纯工程写作，10 月无新篇；情绪上兴奋与失地基并存（详见情绪框架节）。

---

## 思想变迁轨迹（2026）

> 全年 32 篇逐篇核日期（curl 实取；X 登录墙不采；Bluesky @mitsuhiko.at 作旁证）。≤2025 压缩为一行背景。**本表是索引——三个关键节点各有专节展开**（工厂实验 / 情绪框架 / Thorsten 互驳）。

| 阶段 | 日期 | 立场标记 |
|------|------|---------|
| 背景（≤2025） | 2025-06→12 | 乐观期："doubling down" on agentic coding（《A Year Of Vibes》2025-12-22；教人让 agent 写一次性代码） |
| P1 重度信徒 + 同步警告 | 2026-01→02 | "addicted"、为 Pi 代言；但已警告——"AI agents are amazing and a huge productivity boost. They are also **massive slop machines** if you turn off your brain and let go completely."（01-18） |
| P2 批判线成型 | 2026-03→06 | 兴奋仍在，但"**Any time saved gets immediately captured by competition.**"（03-20）；《The Coming Loop》（06-23）："this looping future is going to be our future **despite the fact that I presently resent it**." |
| P3 工具退化判词 | 2026-07 | 转折点：SOTA 新模型工具调用**比旧模型差**（07-04）；"The tower does not fall, it just keeps rising."（07-13） |
| P4 情绪摆动 | 2026-08 | "excited + ground crumbling" 并存；给出三情绪框架（→ 详见**情绪框架节**） |
| P5 **内卷判词 + 工厂失败** | 2026-09 上旬 | "all of AI engineering is Neijuan"；自家工厂 35 小时白卷（→ 详见**工厂实验节**） |
| P6 收束与沉默 | 2026-09-12→10-03 | P(doom) 反 pacing、忧人；09-29 回纯工程；对 Thorsten #99 零回应（→ 详见**互驳节**） |

**判语**：2026 年内从 "doubling down" 到 "Neijuan" 的**转冷弧线**，每阶段有一手锚点——他是"多数人转暖时转冷"的样本。转冷不是否定 AI（"extinction event 不会来"），而是判定**经济与质量机制跟不上能力曲线**。P5 的工厂实验（$15.5/commit 的白卷）是本库对"软件工厂叙事"最有杀伤力的单条证据。

---

## 工厂实验：一份白卷的完整账目（2026-09-07《Astra: why?》）

他把自己的软件工厂完全交给模型决策，然后把失败原原本本公布出来——这是"软件工厂叙事"目前唯一一份来自实践者自身的失败账本。

**实验设置**（他自己的话，非外部批评）：

> "My software factory was intentionally set up to **let the model decide the how of the workflow entirely**."

**投入**：
- 35 小时连续运行，烧掉 ~1B tokens、~$1200 API 成本；
- 整个项目累计 "a full reset's worth of ChatGPT tokens… **around 4 billion tokens**"。

**产出**：
- 79 commits ≈ **$15.5 per commit**；agent 间 ~1400 条消息；净增 ~75k 行代码；
- 结果："**35 hours later, the factory has delivered absolutely nothing of value** and also **not taught me anything about how to operate a better one**."

**收束问句**：

> "**Which is why I'm honestly asking myself more and more why we are doing this.**"

**对 loop 治理的含义**（指针，判读在 `02_research/01_agent_engineering/loop_engineering/` 停止条件区）：这是"**无停止条件、无收益判据的无限执行**"的一手标本——与 Osmani 的 outer-loop 裁决、Cherny 的质量守门同题对照。⚠️ 引用必须带 caveat：**单样本、单人、任务域未公开**。

---

## 情绪框架：Anger, Anxiety, Agency（2026-08-24）

《Anger, Anxiety and Agency》是他对自己 2026 年精神状态的结构化自剖（回应 Sean Goedecke 的"工作时永远不要愤怒"论，他表示强烈同意）：

- **anger = 带反派的安慰性故事**："It turns a loss of control into **a comforting story with a villain**."——而 AI 时代最容易**选错反派**："Your engineering manager or leadership team might themselves feel uncertain about their future and just try to bolster their own confidence by projecting clar[ity]."
- **anxiety 虽难受但诚实**："Anxiety is an uncomfortable emotion because it acknowledges that **you do not know what will happen and might not be able to stop it**."
- **agency 是第三条路**（标题的答案，也是他继续写下去的理由）。

他自己的矛盾（原句）："I am simultaneously **tremendously excited**, but I am also unsure what will happen next… Much of what I learned over the years is changing rapidly, including ideas I considered **fundamental to my craft and business**. Some days that feels liberating, but on others I wake up feeling like **the ground is crumbling beneath me**."

情绪侧的旁证：Bluesky 一周内从 "cool shit is happening"（09-03）摆到 "cannot trust it"（09-09）。

---

## 与 Thorsten Ball 的互驳（2026-09-12 起，单向敞开）

Thorsten 在 Register Spill #99（09-12）点名反驳他：

> "Armin with some cold water to splash on the golden geese: Astra for Coding: Why Are We Doing This Again?"
> "Shouldn't present-day software engineering processes change to wield the power of these models…? **And these aren't rhetorical questions.**"

**截至 10-03，Armin 零回应**——博客 32 篇 + Bluesky 全量 grep 均 0 命中；RS #100/#101 也没再提他。⚠️ 防误读：同期《P(doom)》（09-12）的靶子是 **Dario 的 pacing 论**，不是 Thorsten——不要把那篇当成回应。对立轴（能力极 vs 经济-质量极）保持单向敞开。

---

## 与库内其他人物的立场对照

- **与 Thorsten Ball（`19`）直接对立**——见上节。
- **同向 Osmani（loop 台账 §A）、Searls（观察名单）——"独立同词异源"，截至 10-03 无任何直接互引**（本卡 32 篇 + bsky 全量 grep：Searls / Osmani 均 0 命中）。三人各自独立命名了同一种担忧：
  - Armin "**slop factory**"（09-07，质量/经济向：内卷判词 + $15.5/commit 白卷）；
  - Searls "**dark factory**"（10-02 播客自嘲："how I've accidentally constructed a dark factory with agents building and maintaining my iOS apps"；其 02-26 定调句 "today's agents are nowhere close to being able to write software that won't fall over without supervision"）；
  - Osmani "**skill decay**"（08-31："Agents can finish the task without teaching you anything… **A completed task is not necessarily a rep.**"，并引 Anthropic Trio 研究 AI 组测验 50% vs 手写组 67%）。
  - 共同点（各卡可回源）：品味、验收与"为什么做"的提问权不可外包——Armin 的版本是 "let the model decide the how" 实验失败后的自我诊断，Osmani 的版本是 outer-loop 所有权论，Searls 的版本是退役前的个人清算。

---

## 关键引用汇总

> *"All of AI engineering is Neijuan (内卷)."* — 2026-09-07

> *"35 hours later, the factory has delivered absolutely nothing of value."* — 2026-09-07

> *"Better models, worse tools."* — 2026-07-04

> *"Any time saved gets immediately captured by competition."* — 2026-03-20（内卷论的前声）

> *"I don't think AI is going to usher in an extinction event."* — 2026-09-12，忧虑的对象是人

---

**Source:** [Astra: why?（2026-09-07，lucumr.pocoo.org）](https://lucumr.pocoo.org/2026/9/7/astra-why/) · [Better Models: Worse Tools（2026-07-04）](https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/) · [The Coming Loop（2026-06-23）](https://lucumr.pocoo.org/2026/6/23/the-coming-loop/) · [Anger, Anxiety and Agency（2026-08-24）](https://lucumr.pocoo.org/2026/8/24/anger-anxiety-agency/) · [P(doom)（2026-09-12）](https://lucumr.pocoo.org/2026/9/12/pdoom/) · [Agent Psychosis（2026-01-18）](https://lucumr.pocoo.org/2026/1/18/agent-psychosis/) · [Deser（2026-09-29）](https://lucumr.pocoo.org/2026/9/29/deser/)
