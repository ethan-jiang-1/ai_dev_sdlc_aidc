---
type: index
content_type: readme
directory: voices
description: 声音库——围绕 AIDLC 的人物、组织与线下聚会（意见来源库：人/组织/事件）
research_date: 2026-07-08
---

# voices — 人物、组织与事件参考材料库（声音库）

> 这是围绕 AI 驱动软件开发生命周期（AIDLC）的**声音库**：谁在说、说了什么、立场怎么变。
> 本库只收**意见有明确来源实体**的材料：人（`_raw_people/`）、组织（`_raw_orgs/`）与线下聚会（`_raw_event_*`，三场 2026 事件）。
> **话题与跨人合成不进本库**（2026-10-03 净化，见文末迁移记录）：两波命名事件在
> [`../loop_engineering/`](../loop_engineering/README.md) 与 [`../graph_engineering/`](../graph_engineering/README.md)，
> 跨人判读在 `02_research/`，模型使用样本在 [`../field_samples/`](../field_samples/README.md)。
>
> **企业/厂商/分析机构**的材料在兄弟目录 `../corp/`。

---

## 目录全景

```
voices/
├── README.md                              ← 你在这里
├── _raw_people/                           ← 人物深度卡（轨迹中心，见其 README 导航表）
├── _raw_orgs/                             ← 组织卡（机构作为发声体；6 张 top 卡——次级组织收档于其 README 收档表）
├── _raw_event_pragmatic_summit_2026/      ← Pragmatic Summit 2026（Beck+Fowler 同台）
├── _raw_event_deer_valley_2026/           ← Deer Valley Retreat 2026（Agile Manifesto 25 年后）
└── _raw_event_engelberg_2026/             ← Engelberg Retreat 2026（从实验到生产的转折点）

../corp/                   ← 企业与生态（兄弟目录）
├── _raw_aws/                              ← AWS 官方 AI-DLC 方法论
└── _raw_ecosystem/                        ← 非 AWS 生态全景

../_abandoned_no_reference/                ← 无源可溯的内容收容所（种子层公共设施，2026-10-03 上移）

# 2026-10-03 迁出的话题类目录（去向指针）
../loop_engineering/                       ← Loop Engineering 一波声音（自 _raw_loop_engineering 上移）
../graph_engineering/                      ← Graph Engineering 与 DAG 编排（_raw_graph_engineering 并入）
../field_samples/fable5/synthesis/         ← Fable 5 变革信号合成（自 _raw_fable5 并入样本池）
../../02_research/02_ai_sdlc/01_evolution/paradigm_evolution/frontier_synthesis_2026-07/
                                           ← 跨公司变革共识合成（自 _raw_frontier 迁入研究层）
```

---

## ⚠️ 来源铁律（不可破例）

> **本库所有材料今后会被分享。每一条内容，不论以什么方式写、不论用什么口吻说，都必须有可验证的来源。**

| 情况 | 处置 | 说明 |
|---|---|---|
| **有来源** | 放入对应 `_raw_*` 子目录 | 必须在文件中标注来源 URL/出处，可回溯验证 |
| **没有来源** | 只能放入 [`../_abandoned_no_reference/`](../_abandoned_no_reference/README.md) | 不得混入任何 `_raw_*` 目录 |

**一手源优先（硬要求）**：
- **只接受原始英文一手源**——博客原文、官方发布、演讲视频/transcript、播客原版、X/Twitter 原帖
- **禁止二手源**——中文编译/翻译（36kr、机器之心、InfoQ 中文站、CSDN、知乎、微信公众号、今日头条等）、聚合站转述、第三方摘要
- 二手源不可靠：翻译可能曲解原意，转述丢失上下文，聚合站添加编辑偏见
- 唯一的例外：如果你**读得懂**中文且需要用它来交叉验证另一条一手源中的内容——但**不能**作为唯一引用

**零容忍**：
- 不可"先写进去，来源以后补"
- 不可"我觉得是这样，不用来源"
- 不可"来源忘了，但内容很重要所以留着"
- 不可"中文翻译更方便读者，留着吧"

没有一手源 = 进 [`../_abandoned_no_reference/`](../_abandoned_no_reference/README.md)。没有例外。

---

## ⚠️ 时间铁律（不可破例）

> **本库只关心 2026 年以后的内容。底线：2026 年 1 月。**

| 情况 | 处置 |
|---|---|
| **2026 年 3 月及以后** | ✅ 首选——最近 3~4 个月内的材料 |
| **2026 年 1 月 ~ 2 月** | ⚠️ 可采纳，但优先用更新的 |
| **2025 年及以前** | ❌ 不得入库——即使有来源也不行 |

**为什么**：AIDLC 领域变化极快。2025 年的观点、框架、数据到 2026 年可能已被推翻。本库聚焦**当前时刻**的真实信号，不做历史档案。2026 年 1 月是硬底线。

---

## 各目录定位与源头特征

### `_raw_people/` — 影响力人物深度拆解（组织卡在 [`../_raw_orgs/`](_raw_orgs/README.md)）

**是什么**：17 位历史上塑造了 SDLC 话语权的人在 AI 时代的言论（人物卡 17 张；组织的声音在 [`../_raw_orgs/`](_raw_orgs/README.md)——6 张 top 组织卡；峰会专题在 [`_raw_event_pragmatic_summit_2026/`](_raw_event_pragmatic_summit_2026/README.md)）。从 Martin Fowler 到 Kent Beck，从 Karpathy 到前 GitHub CEO。

**源头特征**：人物/组织的公开言论（博客、演讲、访谈、社交媒体）。每人有独立立场——先看 README 的共识/分歧矩阵再读个人。

**当前状态**：全部有 frontmatter + verified source_urls + 文末 `**Source:**` 节。

---

### 2026-10-03 迁出的目录（话题不进人物库）

> 本库收窄为「意见来源库」后，四类话题/合成材料迁出。内容未删，去向如下：

| 原目录 | 是什么 | 新家 | 迁移动机 |
|---|---|---|---|
| `_raw_frontier/` | 跨 7 人变革共识合成（共识矩阵、死亡清单） | [`../../02_research/02_ai_sdlc/01_evolution/paradigm_evolution/frontier_synthesis_2026-07/`](../../02_research/02_ai_sdlc/01_evolution/paradigm_evolution/frontier_synthesis_2026-07/README.md) | 跨人判读归研究层（本 README 规矩 #5） |
| `_raw_fable5/` | Fable 5 变革信号合成（16 样本） | [`../field_samples/fable5/synthesis/`](../field_samples/fable5/synthesis/README.md) | 回到它综合的样本池旁，raw→digested 一处完成 |
| `_raw_loop_engineering/` | Loop Engineering 一波声音（2026-06 起，一人一目录；唯一名单权威在 [`02_research/.../loop_engineering/raw/kol-roster.md`](../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)） | [`../loop_engineering/`](../loop_engineering/README.md) | 组织轴是命名事件不是人；上移为种子层话题目录 |
| `_raw_graph_engineering/` | Graph Engineering 一波声音（2026-07 起） | [`../graph_engineering/`](../graph_engineering/README.md) | 与该话题目录大面积重复（一线实录为逐字重复件），并入去重 |

---

### `_raw_event_pragmatic_summit_2026/` — Pragmatic Summit 2026

**是什么**：Gergely Orosz 主办的首届线下大会。Beck+Fowler 同台、Simon Willison、Dohmke+Rajan 圆桌、Laura Tacho DX 数据。

**源头特征**：一手事件报道 + 播客 transcript + 官方 newsletter。14 个验证 URL。

**当前状态**：6 文件（4 session + 跨 session 主题 + README），全部有 frontmatter + verified URLs。

---

### `_raw_event_deer_valley_2026/` — Deer Valley Retreat 2026

**是什么**：Martin Fowler 在 Agile Manifesto 诞生 25 年后的同一片山召集的闭门 retreat。"严苛去哪儿了？"、Supervisory Engineering、Cognitive Debt 等概念的发源地。

**源头特征**：Fowler 的 bliki/fragments + 参会者回顾 + 第三方分析。19 个验证 URL。

**当前状态**：8 文件（4 概念深挖 + 3 参会者/分析 + README），全部有 frontmatter + verified URLs。

---

### `_raw_event_engelberg_2026/` — Engelberg Retreat 2026

**是什么**：Deer Valley 五个月后的欧洲续篇。"证据在握"——从实验到生产的转折点。Optimiser vs Learner、Galaxy Brain 辩论、Harness Engineering 术语的诞生。

**源头特征**：Fowler Fragments + Giles Edwards-Alexander 笔记 + 第三方总结。7 个验证 URL。

**当前状态**：9 文件（5 概念深挖 + 3 实践/治理 + README），全部有 frontmatter + verified URLs。

---

## 与兄弟目录的关系

| | `voices` | `corp` |
|---|---|---|
| **视角** | 个体与聚会——人、组织、事件 | 组织——公司、厂商、分析机构 |
| **材料性质** | 个人/机构言论 + 事件拆解 | 厂商方法论 + 生态全景 |
| **偏向性处理** | 标注证据强度 + 分歧矩阵 | 对抗性验证（claim_verification 文件） |
| **URL 状态** | 大部分已完成 frontmatter + URL | _raw_aws 有 URL，_raw_ecosystem 部分待补 |

---

## 信息处理指南

### 按使用场景选目录

| 场景 | 先看 |
|---|---|
| 想知道具体的人在说什么 | `_raw_people/`（17 张人物卡）＋ `_raw_orgs/`（组织卡） |
| 想知道 2026-06 后 loop engineering 这波谁在说、说什么 | [`../loop_engineering/`](../loop_engineering/README.md)（素材）→ [`02_research/01_agent_engineering/loop_engineering/`](../../02_research/01_agent_engineering/loop_engineering/README.md)（判读与台账） |
| 想知道 graph engineering / DAG 编排这波在说什么 | [`../graph_engineering/`](../graph_engineering/README.md)（素材与判读入口） |
| 想知道 Fable 5 具体改变了什么 | [`../field_samples/fable5/`](../field_samples/fable5/README.md)（样本池 + synthesis/） |
| 想知道四家前沿公司达成了什么共识 | [`02_research/.../paradigm_evolution/frontier_synthesis_2026-07/`](../../02_research/02_ai_sdlc/01_evolution/paradigm_evolution/frontier_synthesis_2026-07/README.md) |
| 想知道 2026 年 AI 软件工程的关键事件 | `_raw_event_pragmatic_summit_2026/` + `_raw_event_deer_valley_2026/` |
| 想知道 agentic engineering 从实验到生产的转折 | `_raw_event_engelberg_2026/` |
| 想知道 Agile 社区怎么回应 AI | `_raw_event_deer_valley_2026/` + `_raw_people/`（Fowler, Beck, Farley）+ `_raw_orgs/`（ThoughtWorks） |
| 想知道组织/厂商的框架设计 | `../corp/_raw_aws/` + `_raw_ecosystem/` |

---

## 滚动更新规矩（2026-10-03 定）

> 触发场景："某位 KOL 最近有新言论了"。按下面的固定动作处理；**更新只落在人物卡里，不开新散文件**。前提是先过上面两条铁律（一手源 + 时间窗）。

1. **回源核查先行**：逐条 web 回源到原帖/原文，核实 URL、日期与引文；搜索结果摘要不能直接当证据。查不到就明说"窗口内无新增"，不拿旧料凑数。
2. **更新只进人物卡，以「思想转变」为组织单位**：口径在变时，先给轨迹表（阶段 × 日期 × 立场标记 × 一手锚点）+ 转变判语，证据小节挂在阶段下；单纯增量才以带日期小节追加（`## 2026-MM <主题>`）。frontmatter `source_urls` 同步追加。卡片是该人言论的单一事实来源。
3. **新人入册**：库内没有的人，新建卡片于 `_raw_people/`，编号 = 现有最大号 + 1，开头先给「当前立场小结」节；`_raw_people/README.md` 导航表同步登记。
4. **口径变化显式标注**：新言论若与本卡已有结论有关，在小节内写明「确认 / 延伸 / 修正已有口径」，不悄悄改写旧结论。
5. **判读不进种子层**：本库只收"谁在哪天说了什么（带源）"；跨人的分析与判读沉淀在 `02_research/` 对应主题，本库不做。

### 轮查渠道速查表（2026-10-03 首版，轮查时的探路成果）

> 判新通用规则：以 **feed `<item>` 内日期**为准（勿读 lastBuildDate/页脚）；web_search 摘要不作证据；web_fetch 故障→curl + Chrome UA；X 全员登录墙，只认转载页间接核验。

| 人物/机构 | 轮查入口 | 节奏 | 已知墙/备注 |
|---|---|---|---|
| Fowler | martinfowler.com 各单页直抓（无站内 feed；recentChanges 页不存在已核）＋ **feeder.co/discover/ac76a49582/martinfowler-com**（第三方 RSS 发现渠道，2026-10-03 实测可用） | 周 | 站点对脚本 UA 偶发 403；/articles/exploring-gen-ai/ 目录索引 403 但**单页可抓**；新篇靠 RSS/镜像发现（镜像常带 ?aid= 追踪参数，剥掉用规范 URL） |
| Farley | Bluesky `davefarley77.bsky.social`（public.api.bsky.app 无登录可读）＋ YouTube 频道 RSS `feeds/videos.xml?channel_id=UCCfqyGl3nq_V0bo64CjZh8g` | 周多更 | 频道列表有 consent 墙；**频道多主播**（AI briefing 期引用须核主讲人）；字幕均 [asr] |
| Willison | simonwillison.net 首页 | 日 | 无墙，最高性价比轮查 |
| Beck | newsletter.kentbeck.com/feed | 周 | X/Medium 双墙；Medium 写作已迁出 |
| Karpathy | karpathy.bearblog.dev/blog/ | 不定 | X 双墙，轮查性价比最低 |
| Cherny | X 墙→经 Willison 转载页间接 | 不定 | |
| Lopopolo | hyperbo.la/contact/（自述页）＋ github.com/lopopolo/harness-engineering（lineage） | 月 | GC 官方博客只在大事件时更新 |
| Morris | infrastructure-as-code.com/posts/ ＋ bsky（剔转帖） | 周 | |
| Orosz | newsletter.pragmaticengineer.com/feed | 日 | 免费层即可判增量；深度文常付费墙 |
| Tacho | lauratacho.com ＋ Stellar Work 档案页 | 月 | 任职信息以 Stellar Work 自述为准 |
| Dohmke | entire.io 博客 ＋ linearb/testmu 等演讲页 | 周 | Bloomberg/LinkedIn 墙 |
| DHH | world.hey.com/dhh/feed.atom | 周 | X 墙；HEY World 无反爬 |
| Huntley | ghuntley.com/feed/（**判新读 `<item>` 日期**，lastBuildDate 是构建时间戳） | 周多更 | /livid/ 等 - 付费墙；RSS 覆盖全年 |
| Ronacher | lucumr.pocoo.org/2026/ | 周 | 无墙，月归档即全列表 |
| Valim | dashbit.co/blog | 月 | |
| Thorsten Ball | registerspill.thorstenball.com/p/joy-and-curiosity-NNN（**编号连续，直接探 +1**） | 周（周六） | |
| Böckeler | martinfowler.com 单页直抓 ＋ bsky（她有转帖出现） | 不定 | 系列索引页 403，新篇靠 feed/镜像发现 |
| ThoughtWorks | thoughtworks.com/radar ＋ insights 博客 | 季/周 | Vol 35 待出（2026-10-03 核验未出） |
| **组织卡轮查行（2026-10-03 挖掘批新增、同日收束为 top 6；判新同样以页面本体日期为准，web_fetch DNS 故障一律 curl + Chrome UA）** | | | |
| Google | developers.googleblog.com（日期在页面 JSON 内）＋ cloud.google.com/blog ＋ sre.google ＋ dora.dev/insights | 周 | DORA 线并入 `google.md` 卡（dora.dev 直连无墙）；2026 年报 9–11 月出 |
| Microsoft+GitHub | github.blog（datePublished meta）＋ developer.microsoft.com/blog | 周 | Octoverse 2026 / Universe 2026（10-28/29）待出——待回查日历见 [`_raw_orgs/README.md`](_raw_orgs/README.md) |
| 37signals | 37signals.com/podcast（REWORK 归档页）＋ Ruby on Rails 官方频道 | 周 | pencils down 无公司署名书面版（软肋已注记） |
| Shopify | shopify.engineering（datePublished meta） | 周 | |
| Stripe | stripe.dev/blog（日期在页面 JSON "date"）＋ stripe.com/blog | 月 | |

---

## 最后更新

- 2026-10-06：**`loop_engineering/` 集合重组为三派结构**（用户定）——推动派（发起者＋吹捧者，`01_advocates/`）／中性派（`02_neutral/`）／反对与怀疑派（`03_skeptics/`）；`andrew_ng/` 四件套随派迁入 `01_advocates/`。**派别判定权威在研究层台账** [`02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md`](../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md) §三派分野（2026-10-06 新增）；派别目录只做素材索引。本库人物卡（`04`/`12`/`15`/`16`/`17`/`19`/`20` 等）被三派素材索引引用，卡片本身不动、不复制。

- 2026-10-04：**corp 边界判据全层统一 + AWS 双卡位定案**——「主张什么进 voices，怎么做 / 卖什么进 corp」一句话判据上门面（本 README、`_raw_orgs/README.md`、`corp/README.md`、种子层 README 四处对齐，入座判据总表见 [`../README.md`](../README.md)）；AWS 悬案定案：**允许双卡位**（AI-DLC 方法论留 `corp/_raw_aws/`，Vogels 修订 Working Backwards / Swami frontier 文等立场性主张可在 `_raw_orgs/` 开卡，开卡时遵循其入册判据）。同日种子层 `weixin/` → `zh_discourse/` 更名（中文圈话语快照，本库一手源铁律的例外收容区；详情见种子层 README 迁移记录）。

- 2026-10-03（深夜·二）：**`_raw_orgs` 收束为 top 卡位（13 → 6 张，用户定调）**——新增判据 #5「话语塑造力」：只留改变别人怎么做的组织。保留 thoughtworks / google / microsoft_github / 37signals / shopify / stripe 六张；Stack Overflow（被 AI 淘汰的当事人）、JetBrains（数据权威非立场权威）、Atlassian（产品护城河喉舌）、GitLab、Spotify、O'Reilly 收档为「一行一信号」表（最强单条＋主 URL，保留重启开卡线索）；DORA 立场线（amplifier 论、反 tokenmaxxing）并入 `google.md`。评估结论未丢：当量分组、负发现（Pivotal 消亡、Netflix 官方失声）、跨卡发现（harness 四家收编路径等）仍在 [`_raw_orgs/README.md`](_raw_orgs/README.md)。

- 2026-10-03（深夜）：**`_raw_orgs` 当量对标挖掘批——组织卡 1 → 13 张**。以「ThoughtWorks 同当量组织是否存在、其 2026+ 影响是什么」为题，6 路并行回源（约 80 个一手页面逐条核验，全部过 2026 时间窗＋一手源铁律，载荷 URL 二次抽验），新增 12 张组织卡：Google / Microsoft+GitHub（生态卡）/ 37signals / Shopify / Spotify / Stripe / GitLab / Atlassian / JetBrains / Stack Overflow / DORA / O'Reilly。跨卡发现与当量分组（当量高+有声 12 家／当量高+无声：Pivotal 消亡、Netflix 官方失声／新生当量：AI 原生待开卡）登记在 [`_raw_orgs/README.md`](_raw_orgs/README.md)「当量对标」节；候选清单勘误一条（Shopify「agent 评审 PR 更少事故」研究核不到，系第三方转述误记）；AWS 意见面证据备齐（Vogels 修订 Working Backwards＋Swami frontier 文）待切磋是否双卡位；待回查日历（Octoverse 2026 / SO Survey / GitLab 第 10 届 / DORA 年报 / QCon Netflix talk 11-18 等 8 项）入库；thoughtworks 卡 frontmatter 归一为 org 类型。评估底稿 `.tmp-*` 已清理。

- 2026-10-03（夜）：**事件目录统一 `_raw_event_` 前缀，三轴命名全部显式**——`_raw_promatic_summit_2026/` → `_raw_event_pragmatic_summit_2026/`（修正 promatic 拼写）、`_raw_agile_manifesto_2026/` → `_raw_event_deer_valley_2026/`（事件官方名 Future of Software Development Retreat @ Deer Valley，与 engelberg 地名命名对称）、`_raw_engelberg_2026/` → `_raw_event_engelberg_2026/`。库内外引用全量同步（产出层旧稿 6 文件 13 处一并扫尾）；顺带修复 `_raw_kol` 活引用（corp 相邻树、loop/graph README、两事件 README、andrew_ng sources 断链、本 README 滚动更新规矩）、deer_valley overview 两处悬空 follow_up 指针（改指 `../_raw_event_engelberg_2026/README.md`）、人物卡计数修正（12/19 → 17，实际卡数）。

- 2026-10-03（晚）：**`kol` → `voices` 更名 + 意见来源库三分落地**——人物（`_raw_people/`，原 `_raw_kol/`）、组织（`_raw_orgs/`，新建）、事件（三场 2026 聚会）三轴成型；ThoughtWorks 卡自 `_raw_kol/01` 迁入 `_raw_orgs/thoughtworks.md`（组织非个人，归属修正）；组织候选清单（Anthropic / OpenAI / GC / LangChain / 37signals / Stripe / Shopify…）在 [`_raw_orgs/README.md`](_raw_orgs/README.md) 备切磋。全库 27 个引用文件路径已同步改写。

- 2026-10-03：**净化收窄为「意见来源库」（人/组织/事件）**——四类话题/合成材料迁出：`_raw_frontier/` → `02_research/.../paradigm_evolution/frontier_synthesis_2026-07/`（跨人判读归研究层，本 README 规矩 #5 的执行）；`_raw_fable5/` → `../field_samples/fable5/synthesis/`（回归其样本池）；`_raw_loop_engineering/` → `../loop_engineering/`（上移为种子层话题目录，与 graph 同构）；`_raw_graph_engineering/` → 并入 `../graph_engineering/`（一线实录系逐字重复件，去重）。`_abandoned_no_reference/` 上移至种子层顶层（收容内容跨 kol/corp，公共设施）。本库现仅含 `_raw_kol/` + 三场 2026 事件；库内全部外向链接已同步改写。
- 2026-10-03：**六人深挖集成批**——Farley（`03`：8-10 月 20 条一手入卡；归属勘误两条——8-19/9-23 热门视频系 Emily Bache 主讲非第一人称；安全工程转向 08-05 "the engineering discipline is the safety"；Bluesky 成最高质量一手源）；Lopopolo（`09`：org 一手核验 OpenAI→Google Cloud Principal Engineer、Symphony 开源 27.5k stars、Zechner–Lopopolo Continuum、GC 官方 "coined the term agent harness"）；Morris（`10`：勘误两条——PlatformCon 实为 06-23、"build the system…" 系转述口号化；三级演进 on the loop→管道化→决策参数化）；Orosz（`12`：回源校正——01 长文≠调查（调查 04-14/05-19）、Meta 文实为 06-17；09-15 工厂七受访者事实）；Huntley（`16`：全年 15 篇八阶段弧线 + 07-23 加入 Antithesis 验证转向）；Ronacher（`17`：32 篇 P1-P6 转冷弧线 + 对照节深化——与 Searls/Osmani"独立同词异源"零互引、工厂实验四组数字）。工作档暂存 `.tmp-kol-deep-2026-10/`（同日夜已清理）。
- 2026-10-03：**Böckeler 入册（`20`）+ `_raw_kol/README.md` 补写作思路节**——"为什么是人是口径的单一事实来源 / 卡片标准结构 / 思想变迁轨迹方法论与六种轨迹类型 / 库的边界"；六人深挖（Farley / Lopopolo / Morris / Orosz / Huntley / Ronacher）**已完成并集成**（见上方深挖集成批条目）。
- 2026-10-03：**新面孔入册 ×4 + 全员轨迹覆盖**——`16` Huntley / `17` Ronacher / `18` Valim / `19` Thorsten Ball（按当日开荒扫描建卡）；全部 19 张卡补齐「思想变迁轨迹（2026）」节（阶段×日期×立场标记×一手锚点+判语；≤2025 按时间铁律压缩为背景行）；观察名单落入 `_raw_kol/README.md`。
- 2026-10-03：**存量卡扫描批**——Willison（`04`：思想转变节——守门锚从人审换成 harness/eval，auto mode 默认化 + 年度综述）、Cherny（`08`："已死"论细化为质量守门）、Dohmke（`14`：SDLC 重审 + forge 治理件）、Orosz（`12`：OpenAI 软件工厂一手取样 + 评审制度议程）、Tacho（`13`：J 曲线 + 任职更新为 AWS）；Karpathy（`07`）加术语谱系勘误（"agentic engineering" 系 Zed/Sobo 2025-06 引入，Karpathy 为扩散者）。Farley / Lopopolo / Morris / ThoughtWorks 窗口内无可核验新增（渠道受限明细见当日扫描档）。
- 2026-10-03：**扁平化提层**——本库自 `reference/kol/` 移至种子层顶层 `kol/`（`reference/` 薄壳撤销，与 `corp/` 一同上移）；库内全部外向相对链接与 frontmatter `directory` 已同步改写。
- 2026-10-03：「滚动更新规矩」落地（见上节）；Fowler（`02`）与 Beck（`05`）两卡按窗口 2026-07～10 增量回源并追加带日期更新小节；新增 DHH 卡 `_raw_kol/15_dhh.md`（库内首个条目——Rails World 2026 "Pencils down"、Lex #501、agent-accelerated development）；`_raw_kol/README.md` 导航表与共识/分歧矩阵同步登记 DHH 列。

- 2026-09-26：新增 `_raw_loop_engineering/`（Loop Engineering 一波声音，2026-06 起，一人一目录）；Andrew Ng 四件套入库（自 `02_research/01_agent_engineering/loop_engineering/andrew_ng/` 迁入，原目录撤销）。**名单权威在** [`02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md`](../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。
- 2026-07-08：**一手源大清洗**——全库删除所有中文二手源（36kr、微信、BAAI、CSDN、toutiao 等），补充 30+ 条原始英文一手 URL。Simon Willison (2→8 URLs)、Dave Farley (2→6 URLs)。来源铁律新增"一手源优先"硬要求。Erik Schluntz 源从 36kr 编译切换到 YouTube 原视频。
- 2026-07-08：更名为 `aidlc_reference_kol`（历史名，现为 `voices`），`_raw_aws`/`_raw_ecosystem` 移出到 `aidlc_reference_corp/`（现为 `corp`）。新增 `_raw_event_pragmatic_summit_2026/`、`_raw_event_deer_valley_2026/`、`_raw_event_engelberg_2026/`。Deer Valley 深挖完成（5→8 文件）。
- 2026-07-07：创建 `_raw_fable5/` 和 `_raw_frontier/`，全库 frontmatter + section citations + URL 溯源运动
