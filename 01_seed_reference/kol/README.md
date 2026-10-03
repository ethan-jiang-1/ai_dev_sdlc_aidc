---
type: index
content_type: readme
directory: kol
description: 人物、事件、合成——围绕 AIDLC 的影响力个体、线下聚会与跨源分析
research_date: 2026-07-08
---

# kol — 人物与事件参考材料库

> 这是围绕 AI 驱动软件开发生命周期（AIDLC）的**人物与事件**参考材料库。
> 九个子目录覆盖：影响力个体、跨公司合成、模型变革信号、两波命名事件（loop / graph）、三场 2026 年关键线下聚会。
>
> **企业/厂商/分析机构**的材料在兄弟目录 `../corp/`。

---

## 目录全景

```
kol/
├── README.md                              ← 你在这里
├── _raw_kol/                              ← 13 位影响力人物深度拆解
├── _raw_frontier/                         ← 跨公司变革共识合成（7 人 + 3 深度研究）
├── _raw_fable5/                           ← Fable 5 模型变革信号合成（16 样本）
├── _raw_loop_engineering/                 ← Loop Engineering 一波声音（2026-06 起，一人一目录）
├── _raw_graph_engineering/                ← Graph Engineering 一波声音（2026-07 起，DAG 与拓扑编排）
├── _raw_promatic_summit_2026/             ← Pragmatic Summit 2026（Beck+Fowler 同台）
├── _raw_agile_manifesto_2026/             ← Deer Valley Retreat 2026（Agile Manifesto 25 年后）
├── _raw_engelberg_2026/                   ← Engelberg Retreat 2026（从实验到生产的转折点）
└── _abandoned_no_reference/               ← 无源可溯的内容收容所

../corp/                   ← 企业与生态（兄弟目录）
├── _raw_aws/                              ← AWS 官方 AI-DLC 方法论
└── _raw_ecosystem/                        ← 非 AWS 生态全景
```

---

## ⚠️ 来源铁律（不可破例）

> **本库所有材料今后会被分享。每一条内容，不论以什么方式写、不论用什么口吻说，都必须有可验证的来源。**

| 情况 | 处置 | 说明 |
|---|---|---|
| **有来源** | 放入对应 `_raw_*` 子目录 | 必须在文件中标注来源 URL/出处，可回溯验证 |
| **没有来源** | 只能放入 `_abandoned_no_reference/` | 不得混入任何 `_raw_*` 目录 |

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

没有一手源 = 进 `_abandoned_no_reference/`。没有例外。

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

### `_raw_kol/` — 影响力人物深度拆解

**是什么**：12 位历史上塑造了 SDLC 话语权的人/公司在 AI 时代的言论（人物卡 12 张；导航表另含 06 综合篇与 11 峰会篇两个非人物条目）。从 ThoughtWorks 到 Martin Fowler，从 Kent Beck 到 Karpathy，从 Simon Willison 到前 GitHub CEO。

**源头特征**：人物/组织的公开言论（博客、演讲、访谈、社交媒体）。每人有独立立场——先看 README 的共识/分歧矩阵再读个人。

**当前状态**：全部有 frontmatter + verified source_urls + 文末 `**Source:**` 节。

---

### `_raw_frontier/` — 跨公司变革共识合成 ⚠️ 二次合成

**是什么**：从 Anthropic/OpenAI/Cursor/Google 七位前沿人物的材料中提取的变革共识。

**源头特征**：二次合成——每个 insight 在 README 中标注了来源人物和 URL，可回溯验证。共识部分可信度高（多人独立验证），死亡清单基于单人宣布。

**当前状态**：全部有 frontmatter + section 级 citations + verified URLs。

---

### `_raw_fable5/` — Fable 5 模型变革信号合成 ⚠️ 二次合成

**是什么**：从 16 个真实使用 Fable 5 的样本中提取的变革信号（核心信号 + 流程模式 + 粗糙信号）。

**源头特征**：二次合成——README 标注了每个 insight 的证据强度（⭐~⭐⭐⭐）。Simon Willison 的案例有完整 transcript（可信度最高）。

**当前状态**：全部有 frontmatter + section 级 citations + verified URLs。

---

### `_raw_loop_engineering/` — Loop Engineering 一波声音（2026-06 起）

**是什么**：2026-06 "loop engineering" 成为公开名字后围绕它发声的人的一手素材，**一人一目录**（`profile.md` + `quotes.md` + `sources.md` + `raw_*.md`，与 `../../field_samples/fable5/run_*/` 同构）。

**源头特征**：一手优先（原帖 / 博客原文 / 官方发布 / 播客原版 / 演讲 transcript）；中文编译只作交叉验证。**时间窗 2026-06 起**——更早的谱系背景（Ralph Wiggum loop、Anthropic《Building effective agents》）不入本集合。

**与 `_raw_kol/` 的分工**：`_raw_kol/` 按**人**铺全景（12 位）；本集合按**一次命名事件**收一波声音。已在 `_raw_kol/` 有卡片的人（Boris Cherny、Kief Morris、Ryan Lopopolo、Karpathy、Gergely Orosz）**不重复建目录**，只写指针 + loop 专项增量。

**唯一名单权威不在本集合**——谁入册、号召力依据、每人主张一句话，在 [`02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md`](../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。本集合只管素材。

**当前状态**：`andrew_ng/` 四件套齐；**当前无待建卡**（建卡规则见集合 README——素材常态在研究主题的 evidence 回源档案）。

---

### `_raw_graph_engineering/` — Graph Engineering 一波声音（2026-07 起）

**是什么**：2026-07 起关于 "graph engineering" / "DAG 状态机编排" / "From Loops to Graphs" 的一手讨论与实操记录。

**源头特征**：一手优先（Peter Steinberger 的 2026-07-18 X 提问、真实一线开发团队关于 DAG 状态机替代多 Agent 聊天的工程对话、开源项目 A2A 协议等）。**时间窗 2026-07 起**。

**当前状态**：README 架构定义已建；已归档 2026-10-01 一线工程交流实录（DAG 状态机与两层自愈机制）。

---

### `_raw_promatic_summit_2026/` — Pragmatic Summit 2026

**是什么**：Gergely Orosz 主办的首届线下大会。Beck+Fowler 同台、Simon Willison、Dohmke+Rajan 圆桌、Laura Tacho DX 数据。

**源头特征**：一手事件报道 + 播客 transcript + 官方 newsletter。14 个验证 URL。

**当前状态**：6 文件（4 session + 跨 session 主题 + README），全部有 frontmatter + verified URLs。

---

### `_raw_agile_manifesto_2026/` — Deer Valley Retreat 2026

**是什么**：Martin Fowler 在 Agile Manifesto 诞生 25 年后的同一片山召集的闭门 retreat。"严苛去哪儿了？"、Supervisory Engineering、Cognitive Debt 等概念的发源地。

**源头特征**：Fowler 的 bliki/fragments + 参会者回顾 + 第三方分析。19 个验证 URL。

**当前状态**：8 文件（4 概念深挖 + 3 参会者/分析 + README），全部有 frontmatter + verified URLs。

---

### `_raw_engelberg_2026/` — Engelberg Retreat 2026

**是什么**：Deer Valley 五个月后的欧洲续篇。"证据在握"——从实验到生产的转折点。Optimiser vs Learner、Galaxy Brain 辩论、Harness Engineering 术语的诞生。

**源头特征**：Fowler Fragments + Giles Edwards-Alexander 笔记 + 第三方总结。7 个验证 URL。

**当前状态**：9 文件（5 概念深挖 + 3 实践/治理 + README），全部有 frontmatter + verified URLs。

---

## 与兄弟目录的关系

| | `kol` | `corp` |
|---|---|---|
| **视角** | 个体——人、对话、事件 | 组织——公司、厂商、分析机构 |
| **材料性质** | 个人言论 + 合成分析 + 事件拆解 | 厂商方法论 + 生态全景 |
| **偏向性处理** | 标注证据强度 + 分歧矩阵 | 对抗性验证（claim_verification 文件） |
| **URL 状态** | 大部分已完成 frontmatter + URL | _raw_aws 有 URL，_raw_ecosystem 部分待补 |

---

## 信息处理指南

### 按使用场景选目录

| 场景 | 先看 |
|---|---|
| 想知道具体的人在说什么 | `_raw_kol/`（12 人）、`_raw_frontier/`（7 人共识） |
| 想知道 2026-06 后 loop engineering 这波谁在说、说什么 | `_raw_loop_engineering/`（素材）→ [`02_research/01_agent_engineering/loop_engineering/`](../../02_research/01_agent_engineering/loop_engineering/README.md)（判读与台账） |
| 想知道 Fable 5 具体改变了什么 | `_raw_fable5/` |
| 想知道 2026 年 AI 软件工程的关键事件 | `_raw_promatic_summit_2026/` + `_raw_agile_manifesto_2026/` |
| 想知道 agentic engineering 从实验到生产的转折 | `_raw_engelberg_2026/` |
| 想知道 Agile 社区怎么回应 AI | `_raw_agile_manifesto_2026/` + `_raw_kol/`（Fowler, Beck, Farley, ThoughtWorks） |
| 想知道组织/厂商的框架设计 | `../corp/_raw_aws/` + `_raw_ecosystem/` |

---

## 滚动更新规矩（2026-10-03 定）

> 触发场景："某位 KOL 最近有新言论了"。按下面的固定动作处理；**更新只落在人物卡里，不开新散文件**。前提是先过上面两条铁律（一手源 + 时间窗）。

1. **回源核查先行**：逐条 web 回源到原帖/原文，核实 URL、日期与引文；搜索结果摘要不能直接当证据。查不到就明说"窗口内无新增"，不拿旧料凑数。
2. **更新只进人物卡，以「思想转变」为组织单位**：口径在变时，先给轨迹表（阶段 × 日期 × 立场标记 × 一手锚点）+ 转变判语，证据小节挂在阶段下；单纯增量才以带日期小节追加（`## 2026-MM <主题>`）。frontmatter `source_urls` 同步追加。卡片是该人言论的单一事实来源。
3. **新人入册**：库内没有的人，新建卡片于 `_raw_kol/`，编号 = 现有最大号 + 1，开头先给「当前立场小结」节；`_raw_kol/README.md` 导航表同步登记。
4. **口径变化显式标注**：新言论若与本卡已有结论有关，在小节内写明「确认 / 延伸 / 修正已有口径」，不悄悄改写旧结论。
5. **判读不进种子层**：本库只收"谁在哪天说了什么（带源）"；跨人的分析与判读沉淀在 `02_research/` 对应主题，本库不做。

---

## 最后更新

- 2026-10-03：**Böckeler 入册（`20`）+ `_raw_kol/README.md` 补写作思路节**——"为什么是人是口径的单一事实来源 / 卡片标准结构 / 思想变迁轨迹方法论与六种轨迹类型 / 库的边界"；六人深挖（Farley / Lopopolo / Morris / Orosz / Huntley / Ronacher）进行中。
- 2026-10-03：**新面孔入册 ×4 + 全员轨迹覆盖**——`16` Huntley / `17` Ronacher / `18` Valim / `19` Thorsten Ball（按当日开荒扫描建卡）；全部 19 张卡补齐「思想变迁轨迹（2026）」节（阶段×日期×立场标记×一手锚点+判语；≤2025 按时间铁律压缩为背景行）；观察名单落入 `_raw_kol/README.md`。
- 2026-10-03：**存量卡扫描批**——Willison（`04`：思想转变节——守门锚从人审换成 harness/eval，auto mode 默认化 + 年度综述）、Cherny（`08`："已死"论细化为质量守门）、Dohmke（`14`：SDLC 重审 + forge 治理件）、Orosz（`12`：OpenAI 软件工厂一手取样 + 评审制度议程）、Tacho（`13`：J 曲线 + 任职更新为 AWS）；Karpathy（`07`）加术语谱系勘误（"agentic engineering" 系 Zed/Sobo 2025-06 引入，Karpathy 为扩散者）。Farley / Lopopolo / Morris / ThoughtWorks 窗口内无可核验新增（渠道受限明细见当日扫描档）。
- 2026-10-03：**扁平化提层**——本库自 `reference/kol/` 移至种子层顶层 `kol/`（`reference/` 薄壳撤销，与 `corp/` 一同上移）；库内全部外向相对链接与 frontmatter `directory` 已同步改写。
- 2026-10-03：「滚动更新规矩」落地（见上节）；Fowler（`02`）与 Beck（`05`）两卡按窗口 2026-07～10 增量回源并追加带日期更新小节；新增 DHH 卡 `_raw_kol/15_dhh.md`（库内首个条目——Rails World 2026 "Pencils down"、Lex #501、agent-accelerated development）；`_raw_kol/README.md` 导航表与共识/分歧矩阵同步登记 DHH 列。

- 2026-09-26：新增 `_raw_loop_engineering/`（Loop Engineering 一波声音，2026-06 起，一人一目录）；Andrew Ng 四件套入库（自 `02_research/01_agent_engineering/loop_engineering/andrew_ng/` 迁入，原目录撤销）。**名单权威在** [`02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md`](../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。
- 2026-07-08：**一手源大清洗**——全库删除所有中文二手源（36kr、微信、BAAI、CSDN、toutiao 等），补充 30+ 条原始英文一手 URL。Simon Willison (2→8 URLs)、Dave Farley (2→6 URLs)。来源铁律新增"一手源优先"硬要求。Erik Schluntz 源从 36kr 编译切换到 YouTube 原视频。
- 2026-07-08：更名为 `aidlc_reference_kol`（历史名，现为 `kol`），`_raw_aws`/`_raw_ecosystem` 移出到 `aidlc_reference_corp/`（现为 `corp`）。新增 `_raw_promatic_summit_2026/`、`_raw_agile_manifesto_2026/`、`_raw_engelberg_2026/`。Deer Valley 深挖完成（5→8 文件）。
- 2026-07-07：创建 `_raw_fable5/` 和 `_raw_frontier/`，全库 frontmatter + section citations + URL 溯源运动
