# SDD 权威第三方评判（authoritative verdicts）

```
topic:        Spec-Driven Development (SDD) 的权威机构/意见领袖评判
accessed_at:  2026-09-20
author:       delegated research agent（DeepSeek Harness）
method:       web_search + web_fetch + curl 抓取 TW Radar 条目页内嵌 blipDetail JSON
scope:        ThoughtWorks Radar / martinfowler.com / InfoQ·QCon / arXiv / 分析师
证据强度图例:  ★★★ 一手原文直接抓到原文；★★ 一手页面确认但内容部分受限；★ 第三方转述/未完全核验
```

---

## 1. ThoughtWorks Technology Radar

### 1.1 Spec-driven development（technique 条目）

- **日期**：2025-11-05（Vol.33 首次入榜）；截至 2026-09-20 条目时间线**仅此一条**
- **定级**：**Assess**（"Worth exploring with the goal of understanding how it will affect your enterprise."）
- **原文要点**（条目描述原文，curl 抓取自条目页内嵌数据）：
  - SDD 是"新兴的 AI 辅助编码工作流"，以结构化功能规格为起点，再分解为解决方案与任务；定义仍在演化。
  - TW 提到 Kiro（requirements→design→tasks 三段）、GitHub spec-kit（类似三步+编排+constitution）、Tessl（spec 本身成为被维护的制品，而非代码）三种不同解读；"have one of our own that we're sharing internally"。
  - **判断核心句**："We find this space fascinating, though the workflows remain elaborate and opinionated. … some generate lengthy spec files that are hard to review … We may be relearning a bitter lesson — that handcrafting detailed rules for AI ultimately doesn't scale."（这个领域迷人但工作流繁琐且强观点化；长 spec 难评审；给 AI 手写细规则可能终究无法规模化。）
  - 条目正文直接链接 martinfowler.com 的 sdd-3-tools 文作为参照源。
- **来源**：https://www.thoughtworks.com/radar/techniques/spec-driven-development
- **证据强度**：★★★（blipDetail JSON：`blipRing: Assess, blipUpdatedDate: Nov 05, 2025`，时间线仅 1 条）

**Vol.34（2026-04-15）是否移动 ring：**
- 条目页时间线**没有新增 Apr 2026 条目**，`blipUpdatedDate` 仍为 Nov 05 2025 → SDD 在 Vol.34 中**未被重新点评、未移动 ring（维持 Assess 惯例延续）**。这是从条目页数据结构得出的推断（TW 惯例：ring 变动会产生新时间线条目），非官方声明，**标注为推断、存疑等级 ★★**。
- ⚠ 勘误（2026-09-21）：上条推断已被官方条目页直读**推翻**——SDD 在 Vol.34 压根未在册（NOT ON CURRENT EDITION），并非「未移动 ring」，见文末补遗。
- 但 Vol.34 新增独立 SDD 工具条目（OpenSpec 获官方直读确认；Spec Kit 条目页未命中、仅 Vol.33 正文点名，见文末补遗），且整期主题转向"harness engineering / 对抗认知债务、回归工程基本功"（TW 新闻稿），对 SDD 空间是间接触地：**方向利好但不升级**。
  - TW Vol.34 新闻稿：https://www.thoughtworks.com/en-ec/about-us/news/2026/combat-ai-cognitive-debt-radar-v34 （★★，正文 JS 渲染仅取到标题与主题）
  - 第三方解读（腾讯云开发者社区《Thoughtworks 技术雷达 Vol.34 深度分析报告》）：https://cloud.tencent.com/developer/article/2655851 （★，未逐句核验）

### 1.2 GitHub Spec Kit（languages-and-frameworks 独立条目，Vol.34 新增）

- **日期**：2026-04-15；**定级：Assess（新增）**
- **来源**：https://www.thoughtworks.com/pt-br/radar/languages-and-frameworks/github-spec-kit （英文区同路径）
- **证据强度**：★★★（blipDetail JSON：`blipRing: Assess, blipPublishedDate: Apr 15, 2026`）

> ⚠ 勘误（2026-09-21）：该条目页未在本目录补遗核查中命中（猜测 slug 下未定位到），本项维持★★口径——即"Spec Kit 独立条目"未获核验、仅 Vol.33 正文点名 spec-kit；见文末补遗节。OpenSpec 独立条目（§1.3）则获官方直读确认。

### 1.3 OpenSpec（tools 独立条目，Vol.34 新增）

- **日期**：2026-04-15；**定级：Assess（新增）**
- **原文要点**：条目开头称 OpenSpec 为"an open-source SDD framework that introduces a lightweight specification layer, ensuring human …"（轻量规格层，人工可审）。
- **来源**：https://www.thoughtworks.com/radar/tools/openspec
- **证据强度**：★★★（blipDetail JSON 同上方式抓取）

**小结**：Vol.33→Vol.34，TW 对 SDD 的态度 = 技术本身停在 Assess 未动，但 2026-04 起对具体 SDD 工具逐个立项评估（OpenSpec 确认新增；Spec Kit 待核）——即"概念观望、工具开始逐个体检"。 TW 对该领域"工作流繁琐、spec 难评审、可能不可规模化"的保留意见（Vol.33 原文）至今未被收回。

---

## 2. martinfowler.com

- **日期**：2025-10/11（页内标注 October 2025；社区摘录多为 2025-11-11）
- **人物/文章**：Birgitta Böckeler《Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl》
- **定性**：解释+审慎批评并存。梳理 Kiro/spec-kit/Tessl 三种 SDD 形态，并给出 TW Radar 后来引用的同类保留意见：工作流重、spec 产物难评审、"为 AI 手写规则"是否可规模化存疑。**注意：TW Radar 的 SDD 条目直接以本文为参照源**——Fowler 站与 TW 的口径同源。
- **来源**：https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- **证据强度**：★★（正文抓到标题与年份，作者与完整论点部分来自第三方一致摘录）

- **Fowler 站其他 SDD 专文**：本次检索（站内 tags 页 + 全网搜索）**未发现** 2026 年新的 SDD 专文或对 Böckeler 文的后续更新。**标注：未检出，存疑**——不排除有未索引的 newsletter 提及。

---

## 3. InfoQ / QCon / 大会

- **2026-02-19 | InfoQ |《Spec-Driven Development – Adoption at Enterprise Scale》**
  - 要点：SDD 有助于人与 AI 之间的意图对齐，但**企业级落地需要文化变革、工作流集成、可规模化的协作模式**——即编辑立场是"方向对，落地成本在组织侧而非个人侧"。
  - URL：https://www.infoq.com/articles/enterprise-spec-driven-development/
  - 强度：★★（meta description 直读；正文有登录墙）
  - **团队/工程控制关联**：✅ 明确谈企业规模化、工作流集成与协作模式，是本次所有来源中**最直接讨论团队落地**的编辑内容。

- **2026-09-10 | InfoQ（Nitin Garg）|《When Spec-Driven Development Pays Off》**
  - 要点：瓶颈已从"AI 生成代码"移到"**验证 AI 生成代码**"；文章讨论当 AI 生成行为偏离意图时如何缓解——即 SDD 的价值要放在验证/治理环节衡量，不是无条件 payoff。
  - URL：https://www.infoq.com/articles/when-spec-driven-development-pays-off/
  - 强度：★★（datePublished + meta description 直读；正文有墙）
  - **团队/工程控制关联**：✅ 核心论点就是验证瓶颈与偏离缓解（评审/验收视角）。

- **QCon 北京（InfoQ 中国报道）| 网易智企《从 Vibe Coding 到 Spec Driven：智能化软件工厂的思考和实践》**
  - 要点：国内一线团队实践案例，从 vibe coding 转向 spec driven 的工厂化软件生产；属从业者实践证言而非机构评级。
  - URL：https://www.infoq.cn/article/lpZPLmhGsOYWKApQrqY2
  - 强度：★（未打开正文核验日期，约为 2025Q4–2026）
  - **团队/工程控制关联**：✅ 组织级"软件工厂"实践。

- **QCon 2026 认证课程**："AI-Assisted Engineering Certification — Your coding agent moves fast. Who checks whether it's making the codebase better?" 体现大会侧议题重心在**校验与治理**而非生成侧（来自 InfoQ 页头广告位，★）。

---

## 4. 学术界（arXiv 等）

- **2026-08-31 | arXiv 2609.00252 |《Spec-Driven Development for Agentic Software Engineering: Harnessing Human-Agent Teamwork》**
  - 要点（摘要原文直读）：从 vibe coding（个人提效）走向 Agentic SE 时，行业出现**生产力悖论**——个人生产力上升但团队吞吐、评审容量、稳定性下降，因为**团队级工程纪律被忽略**；论文旨在把 SDD 奠基为团队规模的使能学科，并刻画 **harness**（团队治理 agent 行为的技术+方法机制）。
  - URL：https://arxiv.org/abs/2609.00252
  - 强度：★★★（摘要全文抓取；概念分析型论文，以灰色文献为主，非实证）
  - **团队/工程控制关联**：✅✅ 本文件所有来源中**最正面且最聚焦团队规模化与治理**的一份。

- **2026 | SSRN/Zenodo |《Does Spec-Driven Development Reduce Defects? An Empirical Test of Industry Claims Across 119 Open-Source Repositories》**
  - 要点：对 119 个开源仓库的实证检验，标题即"null result"——**未发现 SDD 降低缺陷的行业宣称获得实证支持**。注意：SSRN 预印本，未经同行评审，作者背景未核验。
  - URL：https://zenodo.org/records/19432099/files/ssrn-sdd-null-result.pdf
  - 强度：★（仅从搜索结果与文件名确认，未读全文）
  - **团队/工程控制关联**：⚠️ 待读，但从设计看是对"个人/仓库级收益宣称"的实证反证。

- **背景（不满足"仅 2026"但值得一提）**：ACM 2026 出版《LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering》（https://dl.acm.org/doi/abs/10.1145/3803437.3805567 ，★ 未读全文）。

---

## 5. Gartner / Forrester 类分析师

- **结论：未检出**。2026-09-20 检索未发现 Gartner 或 Forrester 就 SDD 发布的公开报告、Hype Cycle 条目或可引用的公开表态。公开可查的"分析师级"判断目前仍以 ThoughtWorks Radar 为最强来源。**如实标注：存疑——分析师报告多为付费墙内容，不排除已发布但不可公开检索。**

---

## 权威判断汇总表

| 机构 | 日期 | 定性 | 强度 | 与团队协作/工程控制的关联 |
|---|---|---|---|---|
| ThoughtWorks Radar | 2025-11-05 | SDD 条目 **Assess**；"迷人但工作流繁琐、spec 难评审、手写规则可能不可规模化" | ★★★ | ⚠️ 部分：点名 spec 难评审（评审门禁视角），但整体偏个人工作流体验 |
| ThoughtWorks Radar Vol.34 | 2026-04-15 | SDD 未移动 ring（推断，维持 Assess）；OpenSpec 新增条目（Assess，官方直读确认）；GitHub Spec Kit 条目页后经补遗核查未命中、维持正文点名（★★，见文末补遗）；整期主题"回归工程基本功、对抗认知债务" | ★★（OpenSpec 新增条目）/★★（未移动为推断，Spec Kit 条目维持★★，见文末补遗） | ✅ 间接：Vol.34 主题即 harness/工程治理 |
| martinfowler.com（Böckeler） | 2025-10/11 | 审慎批评：三种 SDD 形态梳理 + 规模化存疑；被 TW Radar 引为参照源 | ★★ | ⚠️ 偏个人开发体验，评审成本有提及 |
| InfoQ | 2026-02-19 | 方向对，但企业落地靠文化变革+工作流集成+可规模化协作模式 | ★★ | ✅ 直接谈团队规模化落地 |
| InfoQ（Nitin Garg） | 2026-09-10 | 瓶颈已从生成移到**验证**；SDD payoff 取决于验证/治理环节 | ★★ | ✅ 验证瓶颈、偏离缓解（工程控制视角） |
| QCon 北京 / InfoQ 中国（网易智企） | ~2025Q4–2026 | 实践证言：vibe coding → spec driven 的工厂化生产 | ★ | ✅ 组织级实践 |
| arXiv 2609.00252 | 2026-08-31 | 最正面：SDD 是团队规模 Agentic SE 的使能学科，核心在 harness 治理 | ★★★（摘要直读） | ✅✅ 直指团队吞吐/评审容量/稳定性与 agent 治理 |
| SSRN 预印本（119 仓库实证） | 2026 | Null result：SDD 降缺陷的行业宣称未获实证支持 | ★ | ⚠️ 仓库级实证，未经同行评审 |
| Gartner / Forrester | — | **未检出**公开表态 | — | — |

### 对选型的含义（供上游参考）
1. **无人背书、无人否决**：TW 停在 Assess 且 Vol.34 未升级——概念仍处观望期，但工具层（OpenSpec 确认新增；Spec Kit 待核）2026-04 起被逐个立项评估，说明生态在进入主流视野。
2. **共同保留意见集中在两处**：spec 制品难评审、工作流繁琐——这恰是"工程控制（评审门禁/CI 校验/spec 版本管理）"要补的位。
3. **对团队规模化最有利的证据是 2026 年的**：InfoQ 企业篇、Garg 验证瓶颈论、arXiv harness 论文三者同向：SDD 的价值主张正从"个人写好 prompt"转向"团队治理 agent 的工程纪律"。

---

## § Vol.34 定级官方确认补遗（2026-09-20 二轮）

前轮"Vol.34 SDD 主条目维持 Assess"是高置信推断，本轮直接抓到官方条目页，**结果修正了前轮结论**：

- **官方条目页直读**（https://www.thoughtworks.com/radar/techniques/spec-driven-development ，2026-09-20 抓取，HTTP 200）：页面明文 **"Published: Nov 05, 2025 — NOT ON THE CURRENT EDITION. This blip is not on the current edition of the Radar."** blip timeline 仅一格 **Nov 2025 / Assess**。⇒ 前轮"Vol.34 未移动 ring、维持 Assess"的表述**不准确**：官方口径是 **Vol.34（2026-04-15）压根未收录 SDD 条目**；SDD 的最新官方定级仍停留在 **Vol.33（2025-11-05）Assess**。官方提示语同时说明"若近期版本在册则大概率仍相关"——所以 Assess 判词仍是最新可用官方口径，但"Vol.34 复审维持"没有官方依据。
- **Vol.33 官方判词全文（本次完整抓取，可直接引用）**："Spec-driven development is an emerging approach to AI-assisted coding workflows… We've seen many developers adopt this style (and have one of our own that we're sharing internally at Thoughtworks). Three tools in particular have recently explored distinct interpretations… Amazon's Kiro… GitHub's spec-kit… Tessl Framework… We find this space fascinating, though the workflows remain elaborate and opinionated… some generate lengthy spec files that are hard to review… **We may be relearning a bitter lesson — that handcrafting detailed rules for AI ultimately doesn't scale.**"（注意：点名 Kiro/spec-kit/Tessl 三工具的是 Vol.33 条目正文，非 Vol.34 新增。）
- **官方 PDF 已定位但正文仍未能读**：https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2026/04/tr_technology_radar_vol_34_en.pdf （Vol.34 = 2026-04 出版，径直确认了前轮的日期口径）；本环境 web_fetch 不支持 `application/pdf` 内容类型，正文条目转载未获取。未找到 Vol.34 发布公告/官方社媒对 SDD 的点名文本。
- **Vol.34 新增条目的官方确认（部分）**：OpenSpec 官方条目页 https://www.thoughtworks.com/radar/tools/openspec 直读：**Published Apr 15, 2026，Apr 2026 / Assess** ——前轮"Vol.34 新增 OpenSpec（Assess）"获官方直接确认，★→★★★。GitHub Spec Kit 条目页未在猜测 slug（/tools/spec-kit、/tools/github-spec-kit）下命中，前轮该项维持★★。
- **对汇总表的更正**：TW Vol.34 行应改为"SDD 未在册（官方 NOT ON CURRENT EDITION，★★★ 直读）；新增 OpenSpec（Assess，官方确认）"；"无人背书、无人停评"的解读不变——概念仍处观望期，且 TW 明示"没带宽逐版复审旧 blip"，Vol.34 未评≠通过也未否决。
