---
type: org_deep_dive
organization: 37signals
content_type: company_podcast_and_keynote_analysis
verification_status: verified
source_urls:
  - https://www.youtube.com/watch?v=vDjW_dRyKXY
  - https://37signals.com/podcast/ai-challenges-in-software/
  - https://37signals.com/podcast/pencils-down/
  - https://37signals.com/podcast/ai-revisited-part-2
  - https://rubyonrails.org/2026/10/1/rails-world-2026-recap
key_concepts:
  - pencils_down
  - ai_accelerated_development
  - agent_first_architecture
  - convention_over_configuration_for_agents
  - knowing_when_to_stop
---

# 37signals — 方法论出版商的公司级断代宣言

> 与 ThoughtWorks 当量相当（同为「方法论出版商」谱系）：Rails（2004 开源）创造者，《Getting Real》(2006)、《REMOTE》(2013)、《Shape Up》(2019) 与 Signal v. Noise 博客构成「做给你看再写下来」的方法论出版传统。TW 教行业怎么做（咨询交付＋Tech Radar＋Fowler 写作传统），37signals 演示自己做（Shape Up ≈ TW 方法论书的产品公司版）。2026 年 9 月 23 日，这家以 Rails 为生的公司在 Rails World 2026 开幕 keynote 官宣 **"pencils down on hand-written code"**——窗口内最重的公司级断代宣言之一。
> 双卡位说明：DHH 个人言论线（从抵制到 pencils down 的 180° 转变）在 [`../_raw_people/15_dhh.md`](../_raw_people/15_dhh.md)；本卡只收**组织署名**输出（REWORK 公司播客、公司级 keynote 决策）。

---

## 思想变迁轨迹（2026）

> 机构卡。公司播客 REWORK 全年系列铺垫 → 9 月 keynote 收口为断代宣言。

| 阶段 | 日期 | 立场标记 | 锚点 |
|------|------|---------|------|
| 采用节奏立场 | 2026-01-21 / 03-04 | REWORK S2E180「AI Revisited」＋S2E186："Using AI to **reclaim time, not replace thinking**"；"Why rushing adoption can backfire" | 公司播客（Fried 主持） |
| 产品 agent 化 | 2026-03-25 | S2E189「Bring your AI agents to Basecamp」（产品向，口径降权） | 公司播客 |
| 何时停手 | 2026-04-01 | S2E190「Pencils down」：*"Knowing when to stop is harder than it sounds… the moment when more work stops helping and starts getting in the way"*（章节含 AI Workflow & vibe coding / Speed vs durability） | 公司播客 |
| 全 AI 加速自述 | 2026-07-01 | S2E194：*"Basecamp 5 was the first fully AI accelerated development process that we've had."*＋「功能越容易做、说『不』越难」的新挑战 | 公司播客（含官方 transcript） |
| **断代宣言** | 2026-09-23 | **Rails World 2026 开幕 keynote：37signals "pencils down on hand-written code"**；"Rethinking software architecture for the age of agents"；"Bring your own agent: why every app needs a CLI" | 本卡 keynote 节 |
| 生态旁证 | 2026-10-01 | Rails Foundation 官方 recap：*"While all four keynotes got everyone talking about AI…"*（第三方官方渠道，旁证） | Rails 基金会博客 |

**判语**：从 1 月「AI 是回收时间的工具」到 9 月「手写代码退役」——与 DHH 个人线同步但以公司决策形态落地。宣言的独特点在于**架构论证**：不是「AI 写得快」而是「Rails 的 convention over configuration 生来就是 agent 友好的」（可预测的约定 = agent 可依赖的环境）——把自家 20 年技术资产重新论证为 agent 时代优势。

> 📎 本文全部内容来源：见文末 "Source:" 节及 frontmatter `source_urls`。评估底稿：`.tmp-orgcards-research/`（工作档，已随本批收口清理）。播客引句取自官方页面要点与章节标题（逐字讲稿未取得，已在口径注记标注）；keynote 视频为 Ruby on Rails 官方频道上传（2026-09-23）。

---

## Rails World 2026 开幕 keynote："Pencils down"（2026-09-23）

会议 9/22–24（Austin），视频 9-23 官方上传。官方描述：

> *"DHH opens Rails World 2026 in Austin with a keynote on the age of AI agents: why 37signals has gone 'pencils down' on handwritten code, why Rails' convention over configuration is built for this moment, and why the only play left is total optimism."*

章节标题即立场结构："37signals goes pencils down on hand-written code"（00:20:45）→ "Rethinking software architecture for the age of agents"（00:42:49）→ "Bring your own agent: why every app needs a CLI" → "English: the programming language DHH likes better than Ruby"。个人叙事细节（"the Kodak Brownie of our era"、Basecamp 5 vibe 教训）在 DHH 人物卡，此处不复制。

## REWORK 公司播客线：执行自述（全年）

公司频道对 AI 采用节奏的立场序列：S2E186（03-04）"reclaim time, not replace thinking" / "rushing adoption can backfire"——**采用节奏的克制立场**；S2E190（04-01）把「pencils down」用于**产品收笔时机**（注意与 9 月宣言的命名陷阱：同名不同意）；S2E194（07-01）自述 Basecamp 5 是「首个全 AI 加速开发流程」并诚实交代反噬（说「不」变难、token 成本）——宣言前的执行底账。

## 口径分级注记（读卡须知）

- **无公司署名书面版**（截至 2026-10-03）：pencils down 宣言的载体是 keynote 演讲（Rails 基金会官方频道），37signals 自有渠道（37signals.com / dev.37signals.com）无对应博文——本卡判据 #1 按「机构决策 + 官方会议舞台」口径收，标注此软肋。
- keynote 确切演讲日（9/22 vs 9/23）未从官方页确认；可确认会议 9/22–24、视频上传 2026-09-23。
- S2E180（01-21）/ S2E189（03-25）仅经播客归档页核验（标题+日期），未逐集抓取。
- dev.37signals.com 2026 年 6 篇均为技术/产品文，无宣言性立场文。

---

## 关键引用

> *"Knowing when to stop is harder than it sounds… the moment when more work stops helping and starts getting in the way."* — REWORK S2E190, 2026-04-01

> *"Basecamp 5 was the first fully AI accelerated development process that we've had."* — REWORK S2E194, 2026-07-01

> *"…why 37signals has gone 'pencils down' on handwritten code, why Rails' convention over configuration is built for this moment."* — Rails World 2026 keynote 官方描述, 2026-09-23

---

**Source:** [Rails World 2026 Opening Keynote（Ruby on Rails 官方频道，视频上传 2026-09-23）](https://www.youtube.com/watch?v=vDjW_dRyKXY) · [Rails World 2026 agenda（官方议程页）](https://rubyonrails.org/world/2026/agenda) · [Rails World 2026 recap（Rails Foundation，2026-10-01，旁证）](https://rubyonrails.org/2026/10/1/rails-world-2026-recap) · [REWORK S2E194: AI challenges in software development（2026-07-01）](https://37signals.com/podcast/ai-challenges-in-software/) · [REWORK S2E190: Pencils down（2026-04-01）](https://37signals.com/podcast/pencils-down/) · [REWORK S2E186: AI Revisited – Part 2（2026-03-04）](https://37signals.com/podcast/ai-revisited-part-2) · [REWORK 播客归档页](https://37signals.com/podcast)
