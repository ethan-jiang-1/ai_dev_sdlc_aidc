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

> Flask/Werkzeug 作者，Rust/CPython 社区活跃者，Pi（earendil-works）协作者。2026 年发文 32 篇（01-14 → 09-29），其中 7→9 月的密集批判期——"Better Models: Worse Tools"、"内卷（Neijuan）"、"slop factory"——使他成为"宽自主工厂叙事"最重要的质量反证派，并与 Thorsten Ball（`19`）形成公开互驳轴。**2026 年内的弧线是本库最清晰的"转冷"轨迹**（见轨迹表）。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。建卡日 2026-10-03。

## 当前立场小结（2026-10-03 建卡）

1. **AI engineering = 内卷**："I'm more and more convinced that all of AI engineering is **Neijuan (内卷, meaning curl inwards)**. … That's how I feel about AI right now."（09-07）
2. **自己的软件工厂交了白卷**："My software factory was intentionally set up to let the model decide the how of the workflow entirely. … **35 hours later, the factory has delivered absolutely nothing of value** and also not taught me anything about how to operate a better one."
3. **对"agent-only 代码库"留了一个口子**："Astra is in my mind 'objectively bad'. But it's objectively bad **by my human sense**. Maybe it's objectively good for a codebase that is entirely written by agents and only needs to be understood by agents."
4. **工具侧反证**："What surprised me is that this is getting **worse with newer Anthropic models** as both Opus 4.8 and Sonnet 5 show it but none of the older models."（07-04《Better Models: Worse Tools》——SOTA 模型工具调用反而退化，给 harness 侧提供一手反例）
5. **忧虑的对象是人，不是灭绝**："**I don't think AI is going to usher in an extinction event.**"（09-12《P(doom)》，反 Dario pacing、"total regulatory failure"——忧的是 "what this does to us as humans"）
6. **情绪摆动的一手自述**："Some days that feels liberating, but on others I wake up feeling like **the ground is crumbling beneath me**."（08-24）；Bluesky 一周内从 "cool shit is happening"（09-03）摆到 "cannot trust it"（09-09）
7. **收束回纯工程**：09-29《Deser》后至 10-03 无新篇——对 Thorsten #99 的点名反驳，博客/Bluesky 全 grep 零回应

---

## 思想变迁轨迹（2026）

> 2026-10-03 深挖：lucumr.pocoo.org 全年 32 篇逐篇核日期（curl 实取；X 登录墙不采；Bluesky @mitsuhiko.at 作旁证）。≤2025 压缩为一行背景。

| 阶段 | 日期 | 立场标记 | 关键原句 / 锚点 |
|------|------|---------|----------------|
| 背景（≤2025） | 2025-06→12 | 乐观期："doubling down" on agentic coding；教人让 agent 写一次性代码 | 《A Year Of Vibes》(2025-12-22)；《…Throwaway Code》(2025-10-17) |
| P1 重度信徒 + 同步警告 | 2026-01→02 | "addicted"、为 Pi 代言；但警告 slop/成瘾/评审瓶颈 | 01-18："AI agents are amazing and a huge productivity boost. They are also **massive slop machines** if you turn off your brain and let go completely." |
| P2 批判线成型 | 2026-03→06 | 兴奋仍在，"时间被竞争捕获"、"loops 会到来而我 resent it" | 03-20："**Any time saved gets immediately captured by competition.**"；06-23《The Coming Loop》："this looping future is going to be our future **despite the fact that I presently resent it.**" |
| P3 工具退化判词 | 2026-07 | 转折点：SOTA 新模型在第三方工具 schema 上**比旧模型差** | 07-04；07-13："The tower does not fall, it just keeps rising." |
| P4 情绪摆动 | 2026-08 | "excited + ground crumbling" 并存 | 08-24《Anger, Anxiety and Agency》 |
| P5 **内卷判词 + 工厂失败** | 2026-09 上旬 | "**all of AI engineering is Neijuan (内卷)**"；自家软件工厂：35 小时 / ~1B tokens / ~$1200 / 79 commits ≈ **$15.5 per commit** / 净增 75k LOC，"delivered **absolutely nothing of value**" | 09-07《Astra: why?》 |
| P6 收束与沉默 | 2026-09-12→10-03 | P(doom)：反 pacing、忧"对人做什么"；09-29 回到纯工程（Deser）；10 月无新篇；对 Thorsten 点名反驳零回应 | 09-12 · 09-14 · 09-29 |

**判语**：2026 年内从 "doubling down" 到 "Neijuan" 的**转冷弧线**，且每阶段都有一手锚点——他是"多数人转暖时转冷"的样本；转冷不是否定 AI（"extinction event 不会来"），而是判定**经济与质量机制跟不上能力曲线**。P5 的工厂实验（$15.5/commit 的白卷）是本库对"软件工厂叙事"最有杀伤力的单条证据。

---

## 与库内其他人物的立场对照

- **与 Thorsten Ball（`19`）直接对立**：RS #99（09-12）点名 "Armin with some cold water to splash on the golden geese"，并反问 "Shouldn't present-day software engineering processes change to wield the power of these models…? **And these aren't rhetorical questions.**"——截至 10-03，Armin 博客/Bluesky **零回应**（P(doom) 的靶子是 Dario 不是 Thorsten，勿误读）；对立保持单向敞开。
- **同向 Osmani（loop 台账 §A）、Searls（观察名单）**：人的品味、验收与"为什么做"的提问权不可外包；对"让模型决定 workflow"持质量反证。
- **对 harness/loop 治理的价值**：他提供了"工厂叙事失败的一手标本"（35 小时白卷），是 loop 治理研究"停止条件/收益判据"的反面样本。

---

## 关键引用汇总

> *"All of AI engineering is Neijuan (内卷)."* — 2026-09-07

> *"35 hours later, the factory has delivered absolutely nothing of value."* — 2026-09-07

> *"Better models, worse tools."* — 2026-07-04

> *"Any time saved gets immediately captured by competition."* — 2026-03-20（内卷论的前声）

> *"I don't think AI is going to usher in an extinction event."* — 2026-09-12，忧虑的对象是人

---

**Source:** [Astra: why?（2026-09-07，lucumr.pocoo.org）](https://lucumr.pocoo.org/2026/9/7/astra-why/) · [Better Models: Worse Tools（2026-07-04）](https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/) · [The Coming Loop（2026-06-23）](https://lucumr.pocoo.org/2026/6/23/the-coming-loop/) · [Anger, Anxiety and Agency（2026-08-24）](https://lucumr.pocoo.org/2026/8/24/anger-anxiety-agency/) · [P(doom)（2026-09-12）](https://lucumr.pocoo.org/2026/9/12/pdoom/) · [Agent Psychosis（2026-01-18）](https://lucumr.pocoo.org/2026/1/18/agent-psychosis/) · [Deser（2026-09-29）](https://lucumr.pocoo.org/2026/9/29/deser/)
