---
type: index
content_type: readme
directory: reference/kol
description: 人物、事件、合成——围绕 AIDLC 的影响力个体、线下聚会与跨源分析
research_date: 2026-07-08
---

# reference/kol — 人物与事件参考材料库

> 这是围绕 AI 驱动软件开发生命周期（AIDLC）的**人物与事件**参考材料库。
> 七个子目录覆盖：影响力个体、跨公司合成、模型变革信号、三场 2026 年关键线下聚会。
>
> **企业/厂商/分析机构**的材料在兄弟目录 `../corp/`。

---

## 目录全景

```
reference/kol/
├── README.md                              ← 你在这里
├── _raw_kol/                              ← 12 位影响力人物深度拆解
├── _raw_frontier/                         ← 跨公司变革共识合成（7 人 + 3 深度研究）
├── _raw_fable5/                           ← Fable 5 模型变革信号合成（16 样本）
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

**是什么**：14 位历史上塑造了 SDLC 话语权的人/公司在 AI 时代的言论。从 ThoughtWorks 到 Martin Fowler，从 Kent Beck 到 Karpathy，从 Simon Willison 到前 GitHub CEO。

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

| | `reference/kol` | `reference/corp` |
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
| 想知道具体的人在说什么 | `_raw_kol/`（14 人）、`_raw_frontier/`（7 人共识） |
| 想知道 Fable 5 具体改变了什么 | `_raw_fable5/` |
| 想知道 2026 年 AI 软件工程的关键事件 | `_raw_promatic_summit_2026/` + `_raw_agile_manifesto_2026/` |
| 想知道 agentic engineering 从实验到生产的转折 | `_raw_engelberg_2026/` |
| 想知道 Agile 社区怎么回应 AI | `_raw_agile_manifesto_2026/` + `_raw_kol/`（Fowler, Beck, Farley, ThoughtWorks） |
| 想知道组织/厂商的框架设计 | `../corp/_raw_aws/` + `_raw_ecosystem/` |

---

## 最后更新

- 2026-07-08：**一手源大清洗**——全库删除所有中文二手源（36kr、微信、BAAI、CSDN、toutiao 等），补充 30+ 条原始英文一手 URL。Simon Willison (2→8 URLs)、Dave Farley (2→6 URLs)。来源铁律新增"一手源优先"硬要求。Erik Schluntz 源从 36kr 编译切换到 YouTube 原视频。
- 2026-07-08：更名为 `aidlc_reference_kol`（历史名，现为 `reference/kol`），`_raw_aws`/`_raw_ecosystem` 移出到 `aidlc_reference_corp/`（现为 `reference/corp`）。新增 `_raw_promatic_summit_2026/`、`_raw_agile_manifesto_2026/`、`_raw_engelberg_2026/`。Deer Valley 深挖完成（5→8 文件）。
- 2026-07-07：创建 `_raw_fable5/` 和 `_raw_frontier/`，全库 frontmatter + section citations + URL 溯源运动
