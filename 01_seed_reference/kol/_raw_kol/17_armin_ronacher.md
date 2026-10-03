---
type: kol_deep_dive
person: Armin Ronacher
organization: Independent (Flask/Werkzeug author; Pi/earendil-works collaborator)
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://lucumr.pocoo.org/2026/9/7/astra-why/
  - https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/
key_concepts:
  - neijuan_involution
  - slop_factory
  - better_models_worse_tools
  - human_taste_gatekeeping
---

# Armin Ronacher — "内卷派"主笔：模型更强，工具更糟，工厂交白卷

> Flask/Werkzeug 作者，Rust/CPython 社区活跃者，Pi（earendil-works）协作者。2026-07-04 → 09-29 密集发出十篇长文，是"宽自主工厂叙事"最重要的质量反证派——他用"内卷（Neijuan）"与"slop factory"给过热的话语场泼冷水，并与 Thorsten Ball（`19`）形成公开互驳轴。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。建卡日 2026-10-03。

## 当前立场小结（2026-10-03 建卡）

1. **AI engineering = 内卷**："I'm more and more convinced that all of AI engineering is **Neijuan (内卷, meaning curl inwards)**. … That's how I feel about AI right now."（09-07）
2. **自己的软件工厂交了白卷**："My software factory was intentionally set up to let the model decide the how of the workflow entirely. … **35 hours later, the factory has delivered absolutely nothing of value** and also not taught me anything about how to operate a better one."
3. **对"agent-only 代码库"留了一个口子**："Astra is in my mind 'objectively bad'. But it's objectively bad **by my human sense**. Maybe it's objectively good for a codebase that is entirely written by agents and only needs to be understood by agents."
4. **工具侧反证**："What surprised me is that this is getting **worse with newer Anthropic models** as both Opus 4.8 and Sonnet 5 show it but none of the older models."（07-04《Better Models: Worse Tools》——SOTA 模型工具调用反而退化，给 harness 侧提供一手反例）

---

## 与库内其他人物的立场对照

- **与 Thorsten Ball（`19`）直接对立**：Thorsten 在 Register Spill #99 点名引他泼冷水再反驳——本库最清晰的一条"能力极 vs 经济-质量极"对立轴。
- **同向 Osmani（loop 台账 §A）、Searls（观察名单）**：人的品味、验收与"为什么做"的提问权不可外包；对"让模型决定 workflow"持质量反证。
- **对 harness/loop 治理的价值**：他提供了"工厂叙事失败的一手标本"（35 小时白卷），是 loop 治理研究"停止条件/收益判据"的反面样本。

---

## 关键引用汇总

> *"All of AI engineering is Neijuan (内卷)."* — 2026-09-07

> *"35 hours later, the factory has delivered absolutely nothing of value."* — 2026-09-07

> *"Better models, worse tools."* — 2026-07-04

---

**Source:** [Astra: why?（2026-09-07，lucumr.pocoo.org）](https://lucumr.pocoo.org/2026/9/7/astra-why/) · [Better Models: Worse Tools（2026-07-04）](https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/)
