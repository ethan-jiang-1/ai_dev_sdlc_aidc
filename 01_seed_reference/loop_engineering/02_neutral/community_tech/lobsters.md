---
type: community_sentiment
directory: 02_neutral/community_tech
observation_date: 2026-10-06
---

# lobsters — community_tech（专业程序员群众）·中性向

> 非 KOL：一般开发者体感。派别判定权威：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。只收 2026-06 后。

**（补抓增量（第二轮 · 2026-10-06）：通道重试）**

### 一、Lobsters 通道翻案＋四个月全量扫描（已解决——低热但存在）

上轮"Lobsters 不可达"需改写：**搜索路径**（`/search`、`/search.json`、`/search.rss`）本轮实测仍全部被 **Anubis 工作量证明**拦截（仍开放）；但**首页、标签页（`/t/<tag>/page/N`）与单帖 JSON（`/s/<id>.json`）均可直接抓取**。本轮对两个相关标签逐页枚举：`/t/ai`（2026-06-14 → 09-29，3 页）＋`/t/vibecoding`（2026-06-16 → 10-06，26 页），命中 6 条 loop 相关串（热度均 ≤30 分——Lobsters 对 loop 议题"存在但低热"，与 HN 同构）：

| 串（/s/id） | 日期 / 热度 | 内容 |
|---|---|---|
| [The Coming Loop](https://lobste.rs/s/a7thxr)（Ronacher 原文 lucumr.pocoo.org 2026-06-23） | 06-24 / 30 分·20 评论 | 本批最高分 |
| [AI Agents Push Humans Out of the Loop](https://lobste.rs/s/iqqqbg)（arXiv 2608.23642） | 09-26 / 21 分·3 评论 | 学术：现行 human oversight 设计本身阻碍有效监督 |
| [AI Review Loops Don't Always Stabilise](https://lobste.rs/s/52povq) | 08-25 / 7 分·5 评论 | review loop 发散实例 |
| ['Human In The Loop' is not enough](https://lobste.rs/s/cvyif0) | 09-19 / 5 分·5 评论 | HITL 的 burnout 论 |
| [TDD inside the agent loop - theater or actual value?](https://lobste.rs/s/xl5grm)（martinfowler.com） | 09-07 / 0 分·1 评论 | |
| [The Prompt-Wait-Evaluate Loop: How AI Kills Flow Without You Noticing](https://lobste.rs/s/idjph9) | 07-15 / 0 分·0 评论 | |

社区评论引句（`/s/<id>.json` 实取，逐字）：

> "In any case, it reinforces that these full-auto loops just don't work for most interesting tasks."—— u/wrs（The Coming Loop 串；同评详述 Opus 4.7 "would even unilaterally cancel part of the agreed implementation plan, and hide that decision in the 'thinking'"）
> "'Human in the Loop' also inherently causes burnout: GenAI models can output so much code, you can't expect someone to read it all and actually understand it, unless it is *very* rote."—— u/lumi（is not enough 串，7 分）
> "It isn't just passive. The bubble is built up on the idea 'stop hiring humans, totally autonomous agents.' No one is going to want to pay for agents which don't give you the freedom to reduce head count."—— u/composite_higgs（arXiv 串，11 分——把"自主 loop"热归因于资本激励）
> "This posted a few hours before https://danluu.com/agentic-testing/ which also finds TDD doesn't help agents do better. But at least having tests before letting an agent go wild does make me feel better about the work I'm trying to hand over."—— u/wwfn（TDD 串）
> review loop 失稳的一手实例（u/freddyb，AI Review Loops 串，8 分）："The first reviewer threw it through an LLM, rewriting big chunks into a different style, apparently mostly for taste. I kept some, undid some other. Next approver: same thing."
