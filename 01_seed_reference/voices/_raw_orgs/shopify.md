---
type: org_deep_dive
organization: Shopify
content_type: engineering_blog_analysis
verification_status: verified
source_urls:
  - https://shopify.engineering/back-to-native
  - https://shopify.engineering/building-an-agentic-harness-that-outlasts-the-model
  - https://shopify.engineering/under-the-river
  - https://shopify.engineering/helix
  - https://shopify.engineering/river-vulnerability-remediation
  - https://shopify.engineering/shop-app-migration
key_concepts:
  - back_to_native
  - agentic_harness
  - helix_checkpoints
  - river_pr_coauthorship
  - monorepo_world_nix
  - human_judgment_gate
---

# Shopify — 以 agent 成本曲线重算技术栈的最大 Rails 实践者

> 与 ThoughtWorks 当量相当（**实践样本权威**）：Rails 生态最大生产实践者——单体 Rails 于 BFCM 规模运行，模块化单体 packwerk（2020）、Sorbet（2020）、YJIT 生产化（2022–23）、Remix 收编（2022）。TW 是「如何交付」的方法论权威（CD/DORA 血统＋Tech Radar），Shopify 是「极端规模下的实践样本权威」——practitioner 而非 consultant；shopify.engineering ≈ TW 工程文化输出的产品公司对应物。2026 年的动作极具样本价值：**2020 年全押 React Native、2025 年还在写 RN 五年回顾的组织，2026-09 因「agents 把写两遍的成本压坍」整体回撤 native**，同期公开 monorepo＋Nix 的 agent-substrate 押注与「harness > model」论断。

---

## 思想变迁轨迹（2026）

> 机构卡。全年高密度系列（官方工程博客，署名 "Engineering at Shopify"），从 agent 基建自述走到组织级技术栈断代。

| 阶段 | 日期 | 立场标记 | 锚点 |
|------|------|---------|------|
| agent 基建定调 | 2026-05-28 | Under the River：Slack 原生 agent **River**——*"one in eight merged pull requests across Shopify is coauthored by it"*；把 2024 年 monorepo「World」＋全 Nix 押注定性为 **agent substrate**（*"our infrastructure needs to be the substrate for that"*） | Under the River 节 |
| harness > model | 2026-07-29 | **"The models are getting better, but the most important piece of the system remains the harness."**（单次审计 30+ 候选漏洞全部降级/判假；300+ findings 估值 $400k） | agentic harness 节 |
| 人机分工锚定 | 2026-09-02 | River 安全工作流：*"A good patch isn't the same as a fixed vulnerability."*——工程师聚焦*"the product and the risk decisions that require human judgement"* | River 安全节 |
| **技术栈断代** | 2026-09-10 | **Back to native**：*"Coding agents changed what it costs to build mobile apps twice."*——*"agents have reduced the advantages of sharing implementation, while the advantages of building for each platform remain"*；姊妹篇：Shop app 12 周 Swift/Kotlin 重写上线 | Back to native 节 |
| 大迁移工程化 | 2026-09-21 | **Helix**：*"Helix builds a loop where an imperfect attempt cannot move forward until it becomes a good result."* | Helix 节 |

**判语**：2026 年 Shopify 的立场不是口号而是**决策序列**——基建押注（agent substrate）→ harness 论断（模型会换、harness 沉淀）→ 断代决策（agent 重写经济学推翻 6 年前的跨平台全押）→ 工程化（checkpoint 循环）。「LLM 改变了我们 2020 年决策的一个核心假设，所以从第一性原理重估技术栈」——这是把 agent 成本曲线当**选型变量**的第一批组织级样本。

> 📎 本文全部内容来源：见文末 "Source:" 节及 frontmatter `source_urls`。全部证据逐条一手核验（shopify.engineering，日期读自页面 datePublished）。评估底稿：`.tmp-orgcards-research/`（工作档，已随本批收口清理）。

---

## Back to native：agent 成本曲线推翻跨平台押注（2026-09-10）

组织级断代决策文：

> *"Coding agents changed what it costs to build mobile apps twice. Here's why Shopify is moving from React Native back to Swift and Kotlin."*
> *"LLMs changed one of the core assumptions behind our 2020 decision, so we reevaluated our mobile tech stack from first principles."*
> *"We are making this change because agents have reduced the advantages of sharing implementation, while the advantages of building for each platform remain."*

姊妹篇《Migrating Shop app from React Native to native》：*"We migrated the Shop app from React Native to Swift and Kotlin, going from proof-of-concept to publishing in 12 weeks with the help of AI."*——跨平台的核心论据（写一遍跑两端）被 agent 时代「写两遍也不贵」拆掉，选型逻辑从「省人力」翻转为「每平台最优」。

## Harness > model：审计 harness 的实证（2026-07-29）

> *"The models are getting better, but the most important piece of the system remains the harness."*

组织级 agentic code review＋test oracle harness 的复盘：单次审计 30+ 候选漏洞全部降级/判假（对抗误报的工程），300+ findings 估值 $400k——「harness 比 model 长寿」论断带自家账本。与 TW「harness 学科化」、GitHub「harness 产品化」、Google「harness 正史化」并列的 Shopify 版本：**harness 是可审计资产**。

## River 家族：agent 进生产 PR 流（05-28 / 09-02）

- **Under the River（05-28）**：Slack 原生 agent River 走进合并流（1/8 PR coauthored，官方页面与 agent 共同署名）；文末把 monorepo World＋全 Nix 基建定性为 agent substrate——2024 年基建押注的 agent 时代追认。
- **How River takes security work from a fix to merge（09-02）**：*"A good patch isn't the same as a fixed vulnerability."*——从修复到合并的闭环里，人保留的是「需要人类判断的风险决策」。

## Helix：LLM 大迁移的工程化（2026-09-21）

> *"We're using LLMs to rebuild it because they are really capable now; but getting consistent, high-quality, and maintainable results out of the box is difficult. They need tooling and guardrails."*
> *"Helix builds a loop where an imperfect attempt cannot move forward until it becomes a good result."*

checkpoint 循环：必须过测试＋视觉比对＋两道对抗性代码评审＋人工批准——「不完美的尝试不能前进」的循环门设计，是 loop 治理主题的产品公司实证（与 [`02_research/.../loop_engineering`](../../../02_research/01_agent_engineering/loop_engineering/README.md) 台账互指）。

## 口径分级注记与勘误（读卡须知）

- **勘误（本库候选清单原条目）**：「生产事故回溯研究——agent 评审的 PR 出更少事故」**核不到**：已核验 shopify.engineering 2026 年全部 25 篇 sitemap，无此文。最接近的真实对应物是 agentic harness 文（**安全**发现回溯，非生产事故率研究）与 Helix 对抗性评审闭环。疑为第三方转述误记（BI 2026-09-17 对 Tobi 访谈的报道），第三方报道不作证据。
- **Tobi Lütke 2026 组织署名断档**：2025 年初 AI 备忘录（窗口外背景）之后，2026 年无组织署名后续；9 月中旬 "slop grenades" 表态出自第三方播客访谈（The Knowledge Project），非组织署名，仅人物卡线索。
- River PR 占比一手数字为 **1/8 coauthored**（05-28 文）；「一半 production PR」仅见第三方访谈转述——两数须分开标注。
- Gisting（08-19）、ShopGym（10-01）等为产品/基准向次要文，未列主证。

---

## 关键引用

> *"Coding agents changed what it costs to build mobile apps twice."* — Engineering at Shopify, 2026-09-10

> *"The models are getting better, but the most important piece of the system remains the harness."* — Engineering at Shopify, 2026-07-29

> *"Helix builds a loop where an imperfect attempt cannot move forward until it becomes a good result."* — Engineering at Shopify, 2026-09-21

---

**Source:** [Native is now the future of mobile at Shopify（2026-09-10）](https://shopify.engineering/back-to-native) · [Migrating Shop app from React Native to native（2026-09-10）](https://shopify.engineering/shop-app-migration) · [Building an agentic harness that outlasts the model（2026-07-29）](https://shopify.engineering/building-an-agentic-harness-that-outlasts-the-model) · [Under the River（2026-05-28）](https://shopify.engineering/under-the-river) · [How River takes security work from a fix to merge（2026-09-02）](https://shopify.engineering/river-vulnerability-remediation) · [Helix: The internal tool powering our Shopify app's native migration（2026-09-21）](https://shopify.engineering/helix)
