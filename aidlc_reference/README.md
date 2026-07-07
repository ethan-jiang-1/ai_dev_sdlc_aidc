# aidlc_reference — AIDLC 参考材料库

> 这是一个围绕 AI 驱动的软件开发生命周期（AIDLC）的多源参考材料库。
> 五个子目录各自覆盖不同的证据类型和来源生态。

---

## 目录全景

```
aidlc_reference/
├── README.md                          ← 你在这里
├── _raw_aws/                          ← AWS 官方 AI-DLC 方法论（一手厂商材料）
├── _raw_ecosystem/                    ← 非 AWS 生态全景（多厂商、分析机构、社区）
├── _raw_kol/                          ← 历史/当前影响力人物深度拆解（14 人）
├── _raw_frontier/                     ← 跨公司变革共识合成（7 人 + 3 深度研究）
├── _raw_fable5/                       ← Fable 5 模型变革信号合成（16 样本）
└── _abandoned_no_reference/           ← 无源可溯的内容收容所
```

---

## 各目录定位与源头特征

### `_raw_aws/` — AWS 官方方法论

**是什么**：AWS 及合作伙伴（CI&T）发布的 AI-DLC 框架原始材料。三阶段模型、14-Node AgentCore、自适应执行、开源实现。

**源头特征**：
- 来源类型：**厂商一手材料**（AWS 官方博客、GitHub 开源仓库、合作伙伴白皮书）
- 可信度：高（官方发布，可公开访问）
- 偏向性：**强**——这是 AWS 的产品和思想领导力输出，不是独立研究
- 处理建议：用其理解 AWS 的框架设计逻辑，但不要把它当成"唯一正确的 AIDLC"。需要与其他来源交叉验证

**当前状态**：已有 README 索引，图片和 PDF 原始文件保留在 `figures/`

---

### `_raw_ecosystem/` — 非 AWS 生态全景

**是什么**：Google、Microsoft、Gartner、Forrester、Atlassian、EPAM、学术论文、社区反应的横向对比和综合分析。

**源头特征**：
- 来源类型：**混合**——厂商材料（Google/Microsoft）、分析机构报告（Gartner/Forrester）、学术论文（arXiv）、社区讨论（Reddit/Hacker News）、第三方博客
- 可信度：分层。厂商材料可信但偏向；学术论文可信但滞后；社区讨论真实但碎片化
- 偏向性：已被 `07_synthesis.md` 做过一轮对抗性验证和交叉检查
- 处理建议：`claim_verification*.md` 文件是声称验证记录——优先看这些。原始厂商声明和社区反应作为背景

**当前状态**：已有 README 索引 + `00_index_summary.md` 总索引。包含术语全景、成熟度模型、演化时间线

---

### `_raw_kol/` — 影响力人物深度拆解

**是什么**：14 位历史上塑造了 SDLC 话语权的人/公司在 AI 时代的言论和立场。从 ThoughtWorks 技术雷达到 Martin Fowler，从 Kent Beck 到 Karpathy，从 Simon Willison 到前 GitHub CEO。

**源头特征**：
- 来源类型：**人物/组织的公开言论**——博客文章、会议演讲、访谈、社交媒体、官方出版物
- 可信度：人物本身可信，但需要区分"个人观点"和"可推广的实践"
- 偏向性：**每人都有自己的立场**。README 里已有共识/分歧矩阵——先看矩阵再读个人
- 处理建议：这个目录的价值在于**对比**——看看定义了旧 SDLC 的人怎么回应 AI 时代。`06_synthesis.md` 做了跨人物主题分析

**当前状态**：已有详细 README（含共识/分歧矩阵和快速定位指南）

---

### `_raw_frontier/` — 跨公司变革共识合成 ⚠️ 二次合成

**是什么**：从 `ai_sdlc_frontier/`（7 位前沿人物的原始材料）和 3 份深度技术研究中，提取并合成的"变革信号"。四份文件分别覆盖共识提取、人物深度、死亡清单、技术深水区。

**源头特征**：
- 来源类型：⚠️ **二次合成**——不是原始材料，是对原始材料的归纳和交叉分析
- 原始来源：`../ai_sdlc_frontier/` 下的 7 个人物目录（Anthropic ×3, OpenAI ×2, Cursor ×1, Google ×1）+ 3 份 followup 研究
- 可信度：取决于合成质量。每个 insight 在 README 中标注了来自哪个人物的哪份材料——可以回溯验证
- 偏向性：合成过程不可避免地带有选择性。共识部分可信度较高（被多人独立验证）；"死亡清单"基于单人宣布，需要更多独立验证
- ⚠️ **关键限制**：当前引用的是本地文件路径（`ai_sdlc_frontier/raw_*/`）而非可公开访问的 URL。溯源链条是：`_raw_frontier/` → `ai_sdlc_frontier/raw_*/` → 原文 URL（在原始材料的 `sources.md` 或正文中）

**处理建议**：
- 用其快速建立对"变革共识"的全局认知
- 引用具体 insight 时，溯源到 `ai_sdlc_frontier/` 的原始材料，确认原文语境没有被合成扭曲
- "死亡清单"中的 ☠️ 标注表示宣布者自己已停止使用，不是行业共识

---

### `_raw_fable5/` — Fable 5 模型变革信号合成 ⚠️ 二次合成

**是什么**：从 `fable5_field_signals/`（16 个真实使用 Fable 5 的人物/组织样本）中提取并合成的"这个具体模型导致了什么可能要变"的信号。

**源头特征**：
- 来源类型：⚠️ **二次合成**——不是原始材料，是对 16 个样本的归纳
- 原始来源：`../fable5_field_signals/run_*/` 下的 16 个目录（Every ×5, Anthropic ×3, Simon Willison, Superpowers, Zed, Wharton, 及其他）
- 可信度：分层。Simon Willison 的案例有完整 transcript 支撑（可信度最高）；Jesse Vincent 的案例有 podcast 和工程证据；部分 Every 样本是基于采访的二次转述。README 中标注了每个 insight 的证据强度（⭐~⭐⭐⭐）
- 偏向性："粗糙信号"文件中明确标注了证据薄弱的条目——不要把弱信号当结论用
- ⚠️ **关键限制**：和 `_raw_frontier` 一样，引用的是本地文件路径而非可公开访问的 URL

**处理建议**：
- "核心信号"和"流程模式"文件可用于指导团队实验
- "粗糙信号"文件是研究路线图，不是行动指南
- 引用时溯源到 `fable5_field_signals/` 中对应样本的 `quotes.md` 或 `raw_*.md`

---

## 两个合成目录的特殊说明

`_raw_frontier/` 和 `_raw_fable5/` 与其他三个目录有本质区别：

| | `_raw_aws/` `_raw_ecosystem/` `_raw_kol/` | `_raw_frontier/` `_raw_fable5/` |
|---|---|---|
| 材料性质 | 原始材料整理 + 少量归纳 | **合成分析**——跨来源提取共识/模式/信号 |
| 溯源路径 | 材料本身包含或指向原文 URL | README 标注来源文件路径 → 再溯源到原始 URL |
| 引用原则 | 可直接引用（引用原始 URL） | 引用前必须回溯到原始材料确认语境 |
| 当前 URL 状态 | 部分有，部分待补齐 | **无直接 URL**——溯源链条需要穿过原始材料 |

---

## 信息处理指南

### 按源头可信度分层

```
层级 1: 可公开访问的一手材料
  ├── AWS 官方博客/GitHub
  ├── Anthropic/OpenAI/Google/Cursor 官方博客
  ├── arXiv 学术论文
  └── 人物博客/演讲（Simon Willison, Martin Fowler 等）

层级 2: 可信的第三方报道
  ├── Every, 机器之心, 36kr 等媒体的编译/采访
  └── Gartner/Forrester/ThoughtWorks 等分析机构报告

层级 3: 合成分析（⚠️ 需要回溯验证）
  ├── _raw_frontier/ （四份合成文件）
  ├── _raw_fable5/ （三份合成文件）
  └── _raw_ecosystem/07_synthesis.md, _raw_kol/06_synthesis.md

层级 4: 社区讨论
  └── Reddit, Hacker News, 社交媒体（碎片化但真实）
```

### 按使用场景选目录

| 场景 | 先看 | 注意 |
|---|---|---|
| 理解 AIDLC 框架全貌 | `_raw_aws/` + `_raw_ecosystem/00_index_summary.md` | AWS 有偏向，需要 `_raw_ecosystem/` 交叉验证 |
| 了解谁在推动、谁在抵制 | `_raw_ecosystem/03_community_reactions.md` + `_raw_kol/06_synthesis.md` | 社区情绪变化快，注意材料时间戳 |
| 想知道旧 SDLC 的权威怎么回应 AI | `_raw_kol/`（先看 README 的共识/分歧矩阵） | 每人的立场不同，不要只看一个 |
| 想知道跨公司达成了什么变革共识 | `_raw_frontier/01` + `_raw_frontier/02`（分歧部分） | 需要回溯原始材料确认语境 |
| 想知道 Fable 5 具体改变了什么 | `_raw_fable5/01` + `_raw_fable5/02` | 区分核心信号和粗糙信号 |
| 审计团队现有流程是否过时 | `_raw_frontier/03_流程死亡清单` + `_raw_fable5/02` 检查清单 | 死亡清单基于单人宣布，不是行业共识 |
| 做研究/写论文需要引用 | 逐级回溯到层级 1 的原始 URL | 不要直接引用合成文件中的归纳性陈述 |

### 溯源铁律

1. **所有可追溯到公开 URL 的内容，URL 必须贴在原文中**（当前正在进行中）
2. 合成目录中的 insight → 先查 README 找来源文件 → 再去原始材料找 URL
3. 找不到 URL 的内容 → 移入 `_abandoned_no_reference/`
4. 片段信息和完整文章都可以保留——关键是标注来源，不是要求格式统一

---

## 最后更新

- 2026-07-07：创建 `_raw_fable5/` 和 `_raw_frontier/`，整理本 README
- 待办：全库 URL 溯源运动（进行中）
