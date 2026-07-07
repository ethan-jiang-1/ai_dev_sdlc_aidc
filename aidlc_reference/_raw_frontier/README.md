---
type: index
content_type: readme
directory: _raw_frontier
description: 跨公司（Anthropic/OpenAI/Cursor/Google）变革共识合成，从 7 位人物 + 3 份深度研究提取
derived_from: ai_sdlc_frontier/
people_count: 7
research_pieces: 3
files_indexed: 5
research_date: 2026-07-07
---

# _raw_frontier — 跨公司变革共识：信息地图

> 来源库：`ai_sdlc_frontier/`（7 个人物/组织的一手材料 + 3 份深度研究）
> 研究日期：2026-07-07
> 核心问题：站在 AI 辅助软件开发最前沿的人，在说什么东西必须变？

---

## 先看这里

如果你第一次进这个目录，按这条路读：

1. 先看本文件（README）— 搞清楚四份 MD 分别是什么、来源是谁
2. 再看 `01_变革共识_跨公司方法论趋同.md` — 七个共识 + 变革烈度
3. 然后看 `02_人物深度_每个人的变革视角.md` — 每个人的独特角度和分歧
4. 再看 `03_流程死亡清单_什么不再适用.md` — 22 条被宣布已死的做法
5. 最后看 `04_技术深水区_压缩与上下文工程的变革含义.md` — 底层怎么做到的

如果你只读一份，读 `01`。
如果你想知道他们哪里不一致，读 `02` 的最后一节。

---

## 四份文件概览

| 文件 | 一句话 | 适合谁 |
|---|---|---|
| `01_变革共识_跨公司方法论趋同.md` | 七个跨公司共识 + 变革烈度 + 与 AWS AIDLC 对比 | 想快速建立全局认知的人 |
| `02_人物深度_每个人的变革视角.md` | 七人各自的触发事件、独特视角、变革处方 + 分歧矩阵 | 想做比较分析的人 |
| `03_流程死亡清单_什么不再适用.md` | 22 条被明确宣布不再适用的流程（☠️/⚠️/🔮），每条附替代方案 | 想审计团队现有流程的人 |
| `04_技术深水区_压缩与上下文工程的变革含义.md` | 上下文压缩四层防线、缓存策略、动态上下文发现 → 流程含义 | 关心底层工程机制的人 |

---

## 来源全量映射

### 原始材料来源（`ai_sdlc_frontier/` 目录结构）

```
ai_sdlc_frontier/
├── raw_Anthropic_Erik Schluntz/
│   ├── Erik Schluntz.md              ← Vibe Coding Masterclass（36kr/机器之心编译）
│   └── 要点总结.md
├── raw_Anthropic_Fiona Fung/
│   ├── Fiona Fung.md                 ← Running an AI-native engineering org（Anthropic 官方博客）
│   └── 要点总结.md
├── raw_Anthropic_Thariq Shihipar/
│   ├── Thariq Shihipar.md            ← Fable 5 使用指南（机器之心编译）
│   ├── new_talk.md                   ← AI Engineer World's Fair 演讲笔记
│   └── 要点总结.md
├── raw_OpenAI_Michael Bolin/
│   ├── Michael Bolin.md              ← Unwinding Codex's Agent Loop（OpenAI 官方工程博客）
│   └── 要点总结.md
├── raw_OpenAI_Ryan Lopopolo/
│   ├── Ryan Lopopolo.md              ← Harness Engineering（OpenAI 官方博客）
│   └── 要点总结.md
├── raw_Google_Rody Davis/
│   ├── Rody Davis.md                 ← Agent Factory Recap（Google Cloud Blog）
│   └── 要点总结.md
├── raw_Cursor_Jediah Katz/
│   ├── Jediah Katz.md                ← Dynamic Context Discovery（Cursor 官方博客）
│   └── 要点总结.md
└── followup_research/
    ├── 01_context_compaction_六家对比.md        ← 六家 Agent 上下文压缩策略深度对比
    ├── 02_claude_code_四层上下文压缩深度拆解.md   ← Claude Code 压缩源码逆向分析
    └── 03_dynamic_context_discovery_静态到动态的范式转移.md ← 从静态到动态的范式转移
```

### 每份合成文件使用了哪些原始材料

#### `01_变革共识_跨公司方法论趋同.md`

| 共识 | 主要来源人物 | 来源文件 |
|---|---|---|
| 共识一：瓶颈转移 | Fiona Fung | `Fiona Fung.md` + `要点总结.md` |
| | Thariq Shihipar | `Thariq Shihipar.md` + `要点总结.md` |
| | Rody Davis | `Rody Davis.md` + `要点总结.md` |
| 共识二：角色转变 | Ryan Lopopolo | `Ryan Lopopolo.md` + `要点总结.md` |
| | Erik Schluntz | `Erik Schluntz.md` + `要点总结.md` |
| | Fiona Fung | `Fiona Fung.md` |
| 共识三：流程过时 | Fiona Fung | `Fiona Fung.md`（四条流程重写） |
| | Ryan Lopopolo | `Ryan Lopopolo.md`（合并哲学反转） |
| 共识四：上下文范式转移 | Jediah Katz | `Jediah Katz.md` + `要点总结.md` |
| | Ryan Lopopolo | `Ryan Lopopolo.md`（AGENTS.md 作为地图） |
| | Thariq Shihipar | `Thariq Shihipar.md`（Skills 渐进加载） |
| 共识五：地图≠疆域 | Thariq Shihipar | `Thariq Shihipar.md` + `要点总结.md` |
| 共识六：约束=杠杆 | Ryan Lopopolo | `Ryan Lopopolo.md`（分层架构 + linter） |
| | Erik Schluntz | `Erik Schluntz.md`（Leaf Nodes） |
| 共识七：知识管理重构 | Ryan Lopopolo | `Ryan Lopopolo.md`（仓库=记录系统） |

#### `02_人物深度_每个人的变革视角.md`

| 章节 | 来源 | 核心内容来自 |
|---|---|---|
| Erik Schluntz | `raw_Anthropic_Erik Schluntz/` | `Erik Schluntz.md` + `要点总结.md` |
| Fiona Fung | `raw_Anthropic_Fiona Fung/` | `Fiona Fung.md` + `要点总结.md` |
| Thariq Shihipar | `raw_Anthropic_Thariq Shihipar/` | `Thariq Shihipar.md` + `要点总结.md` + `new_talk.md` |
| Ryan Lopopolo | `raw_OpenAI_Ryan Lopopolo/` | `Ryan Lopopolo.md` + `要点总结.md` |
| Michael Bolin | `raw_OpenAI_Michael Bolin/` | `Michael Bolin.md` + `要点总结.md` |
| Jediah Katz | `raw_Cursor_Jediah Katz/` | `Jediah Katz.md` + `要点总结.md` |
| Rody Davis | `raw_Google_Rody Davis/` | `Rody Davis.md` + `要点总结.md` |
| 分歧 1-4 | 跨人物交叉对比 | 综合所有来源 |

#### `03_流程死亡清单_什么不再适用.md`

| 章节 | 死亡项数量 | 主要来源人物 |
|---|---|---|
| 规划类 | 4 | Fiona Fung, Thariq Shihipar, Erik Schluntz, Ryan Lopopolo |
| Review 类 | 3 | Fiona Fung, Ryan Lopopolo, Thariq Shihipar |
| 角色类 | 3 | Ryan Lopopolo, Fiona Fung, Jesse Vincent（交叉引用自 fable5） |
| 上下文类 | 3 | Ryan Lopopolo, Jediah Katz |
| 合并与质量类 | 3 | Ryan Lopopolo, Erik Schluntz |
| 知识管理类 | 2 | Ryan Lopopolo |
| 清理与维护类 | 2 | Ryan Lopopolo, Rody Davis |
| 模型使用类 | 2 | Willie Williams, mclayer, Jediah Katz（后两者交叉引用自 fable5） |
| 正在被挑战的 | 7 | 综合 |

#### `04_技术深水区_压缩与上下文工程的变革含义.md`

| 章节 | 来源文件 |
|---|---|
| 上下文压缩四层防线 | `02_claude_code_四层上下文压缩深度拆解.md` |
| 缓存策略 | `01_context_compaction_六家对比.md`（Codex 部分）+ `02_claude_code_四层上下文压缩深度拆解.md`（cache_edits 协议） |
| Context Collapse | `02_claude_code_四层上下文压缩深度拆解.md`（marble_origami） |
| 动态上下文发现 | `03_dynamic_context_discovery_静态到动态的范式转移.md` |
| 六家压缩策略对比 | `01_context_compaction_六家对比.md` |
| AutoCompact 9 段摘要 | `02_claude_code_四层上下文压缩深度拆解.md`（Layer 4） |
| 三层上下文架构 | `03_dynamic_context_discovery_静态到动态的范式转移.md` §九 |
| 与 AIDLC 映射 | 跨 `_raw_aws/` 和 `followup_research/` 的交叉分析 |

---

## 人物速查

| 人物 | 公司 | 一句话 | 最值钱的原话 |
|---|---|---|---|
| Erik Schluntz | Anthropic | "被迫 vibe code" 的研究员 | "当模型 7 个月翻一倍能力时，人类逐行 code review 会成为瓶颈" |
| Fiona Fung | Anthropic | "杀掉旧流程" 的工程总监 | "Build is cheap. Argument is expensive." |
| Thariq Shihipar | Anthropic | "命名了未知项" 的工程师 | "Fable 5 是第一个让澄清未知项的能力成为工作质量瓶颈的模型" |
| Ryan Lopopolo | OpenAI | "零人工代码" 的实验者 | "人类负责掌舵，智能体负责执行" |
| Michael Bolin | OpenAI | "拆解 Agent Loop" 的工程师 | "所有 Agent Loop 的工程决策最终都回到一句话：保持前缀不变" |
| Jediah Katz | Cursor | "发现少即是多" 的工程师 | "给模型更少的预设信息，让它自己按需拉取上下文" |
| Rody Davis | Google | "盆景艺术家" | "AI 速度的最大瓶颈不是上下文窗口——是糟糕的代码库健康度" |

---

## 材料层级说明

原始材料（`ai_sdlc_frontier/` 中每个人物目录下的 `*.md`）已经经过一轮"要点总结"的提炼。本目录的四份文件是在此基础上的**第二次合成**——不再逐人复述，而是跨人物提取共识、分歧、模式、死亡清单。

如果你对某个具体人物的完整论述感兴趣，应该回到 `ai_sdlc_frontier/raw_*/` 读原文 + 要点总结。

如果你对原始人物**在 Fable 5 具体使用上的信号**感兴趣，去看 `../_raw_fable5/` ——那边是从 `fable5_field_signals/`（16 个样本）合成的。

---

## 和相邻目录的关系

```
aidlc/
├── _raw_aws/          ← AWS 的 AI-DLC 方法论（三阶段、14-Node AgentCore）
├── _raw_fable5/       ← Fable 5 具体模型引发的变革信号（16 个样本合成）
├── _raw_frontier/     ← 你在这里。跨公司变革共识（7 人物 + 3 研究合成）
├── _raw_kol/          ← 历史 KOL（Fowler、Farley 等）
└── _raw_ecosystem/    ← 非 AWS 全景
```

**`_raw_frontier` 和 `_raw_fable5` 的差别：**

| | `_raw_frontier` | `_raw_fable5` |
|---|---|---|
| 来源 | `ai_sdlc_frontier/`（7 人 + 3 研究） | `fable5_field_signals/`（16 个样本） |
| 核心问题 | 人在说什么必须变？ | Fable 5 这个模型导致了什么可能要变？ |
| 视角 | 方法论者、工程领导者 | 一线使用者、早期 adopters |
| 证据类型 | 团队实践、官方博客、方法论框架 | 个人体验、行为观察、制度调整 |

两者互补。`_raw_frontier` 给出"为什么变"的论证，`_raw_fable5` 给出"变了之后什么样"的实例。

**`_raw_frontier` 和 `_raw_aws` 的差别：**
- `_raw_aws`：AWS 的自顶向下方法论设计——"正确的流程应该长这样"
- `_raw_frontier`：四家公司一线人物的自底向上实践报告——"我们试过了，旧流程死了，新做法管用"

---

## 阅读路径速查

| 如果你关心... | 先读 | 再读 |
|---|---|---|
| 大局：四家公司达成了什么共识 | `01` §一~§三 | `01` §五（核心教训） |
| 每个人到底怎么想的 | `02` §一~§七（选你感兴趣的人） | `02` §九（分歧） |
| 我的团队现在有哪些流程该杀了 | `03` §十（死亡清单总表） | 按类别查 `03` §一~§九 |
| 底层技术是怎么支撑这些变化的 | `04` §一~§四 | `04` §六（人的行为建议）、§八（与 AIDLC 映射） |
| 这些说法有没有矛盾 | `02` §九（四个分歧） | `01` §三（变革烈度） |
| 和 AWS AIDLC 什么关系 | `01` §四 | `04` §八 |
| 我还想读原始材料 | 看本文件 §来源全量映射 | 去 `ai_sdlc_frontier/` 读对应 `要点总结.md` |
