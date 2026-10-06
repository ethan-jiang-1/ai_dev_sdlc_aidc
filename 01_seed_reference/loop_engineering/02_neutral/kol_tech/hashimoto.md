---
type: kol_evidence
directory: 02_neutral/kol_tech
observation_date: 2026-10-06
---

# hashimoto — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：Vagrant/HashiCorp 创始人、Ghostty 作者
> **号召力**：③＋② OSS 基础设施领袖
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**方向**：升温·越线（皈依→限速→越过自己划的线）
**起点**：02-05'excruciating'双轨训练后皈依＋'不通宵/不多 agent'划线
**终点**：08-11'600 review nightly agents, start new'——越过自己 2 月的划线
**弧线**：02-05 划线（'not running multiple agents, don't really want to'）→ 07-29 创办 Superlogical（durable session 层）→ 08-11 越线（600 review nightly agents）→ 10-05 Rex 公测
**关键转折**：08-11 越线——从'刻意不通宵'到'600 个夜间 review agent'，六个月内立场实质升级

## 《My AI Adoption Journey》（2026-02-05）

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

---

# 增量补挖（2026-10-07 第二轮：06 月后立场更新——实践者兼基础设施供给方）

> 通道：mitchellh.com feed.xml（窗口内无新博文——最后核对确认）、superlogical.com 首页与 updates 页、三条推文双通道缓存（x.com status 页 og:description ＋ cdn.syndication.twimg.com tweet-result JSON）。**结论：窗口内他未直接使用 loop engineering 术语，但立场沿实践/产品两条线实质强化**——相比 02-05《My AI Adoption Journey》的个人使用叙事，已升级为实践者兼基础设施供给方。

## Superlogical 公司公告：为「所有工作」建多路复用器（2026-07-29）

- URL：https://www.superlogical.com/ （首页实取；"I authored the announcement post on the Superlogical homepage" 出自其 2026-07-29 博文缓存 hashimoto-superlogical.txt——本人执笔确认）
- **与 loop engineering 的挂钩**：**循环产品化机制**——把 agent 并行工作、后台作业所需的持久会话层（durable session、人可见可控）做成产品基础设施。
- 逐字摘录：

> "local development. remote access. coding agents. background jobs. production applications. live debugging. sandboxes. shared terminals. incident response. humans and machines."

> "It has many modes of operation: interactively with a human developer, automatically through CI and background processes, and increasingly through agents working in parallel."

> "We believe the missing layer is a durable session around the work itself: one that can span applications and environments, provide relevant context by default, expose structured data and actions, preserve history, and be driven by software while remaining visible and controllable by people."
（「无人值守工作＋人可见可控」愿景与 loop engineering 的治理命题同构——注意他 02-05 自述"刻意不通宵跑 loop"，此处已越过该线。）

- 立场：**支持（agent 运行基础设施供给）**。

## 推文：更新版日程表——清晨 review 通宵 agent 并启动新一轮（2026-08-11）

- URL：https://x.com/mitchellh/status/2087227139154448436 （**双通道实取**：x.com status 页 og:description ＋ cdn.syndication.twimg.com/tweet-result JSON；长推文在 ~280 字符处截断——两个通道同断，如实记录，日程后半段不可见）
- **挂钩**：**无人值守运行**——agent 通宵无人值守执行，晨间 6:00 人工 review 并启动新一轮，人作为外层调度节拍。
- 逐字摘录：

> "I've been asked for an updated daily schedule given Superlogical, second kid, and AI usage. Here you go:"

> "- 600 review nightly agents, start new"
（对比其 2025-09 旧日程（同缓存内 quoted_tweet），新增「review nightly agents」一项：通宵 agent 循环已成日常固定节拍。）

- 立场：**支持（通宵循环日常化）**——窗口内最直接的实践证据，且与他 02-05"明确与通宵 loop 划界"形成显式态度变化。

## Superlogical 公测开始：Rex 终端落地持久会话层（2026-10-05）

- URL：https://www.superlogical.com/updates/public-testing-beginning （updates 页实取；Superlogical Team 署名——公司层，非个人署名，如实标注）
- **挂钩**：**循环产品化机制**——首页愿景的首个可用产品形态，persistent sessions 与 program activity status 面向无人值守工作监控。
- 逐字摘录：

> "capabilities such as persistent sessions, performant and responsive remote connections, program activity status, and more."

- 立场：**支持（产品化推进）**。

**本轮最小主张**：Hashimoto 06 月后的立场更新＝从"皈依＋限速"（02-05：不通宵、单 agent）升级为"通宵循环日常化＋建公司供给 agent 运行基础设施"——弧线越过自己 2 月划的线，全程未用专名。
