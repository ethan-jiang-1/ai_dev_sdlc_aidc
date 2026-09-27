# AGENTS.md — 这场 keynote 的叙事

> 2026-09-27 用户定：本目录的 agent **只提供 PPT 的内容**。
> 内容指叙事：结构、系统、故事是否往前走、主张是否自洽。
> 页的版式、画面、PNG、风格母版、PPTX，不在这个 agent 的工作里。那些文件若已存在，当作停掉的试验，不续做、不修图。

## 做完的标准

一次内容改动做完，当且仅当下面四条同时成立：

1. **结构**：标准档每一页只推进故事的一步。加深页是追问的答案，不插进标准档中间。
2. **系统**：公式里的每个因子都能在大纲里指到页；多出来的页要写明它为什么不是第四个因子。
3. **叙事**：听众能用一句话接上下一页。接不上的页，删或并。
4. **自洽**：`v1/outline/outline.md` 的主张句与 `v1/manuscript/manuscript.md` 的 CLAIM 是同一句。上屏的 subtitle 用这一句。研究层的边界写在讲者备注或 callout，不另起一套主张。

内容权威是大纲，展开在文稿。`v1/session_design/`、`v1/style/`、`v1/production/` 不是内容权威。

## 项目定位

- **讲的事**：你离开之后它继续跑，你回来时它说做完了。整场回答你凭什么信。
- **语言**：中文短句。术语进备注，不进主张句。见大纲 §6。
- **源**：研究层 `result/landscape.md`，实践层 backbone。主张不超出这两处。

## 内容流程

```
素材里哪几句能进故事  →  research/source-synthesis.md
故事的一步一步        →  v1/outline/outline.md
每一步怎么说          →  v1/manuscript/manuscript.md
每页上屏              →  同文稿的 title / subtitle / content
```

上屏给后面的做片用。title 短，subtitle 等于主张句。只读二者应能跟上论证。content 写看得见的场面。红、绿、灯和版面分组放在引用块里，不上屏。本目录仍不出 PPTX、PNG、风格母版。

改故事先改大纲，再改文稿，使两处的主张句重新相同。

## 源材料路径速查

| 想看什么 | 路径 |
|---------|------|
| Loop Engineering 研究全景 | `../../02_research/ai_loop_engineering/README.md` |
| 当前研究态 | `../../02_research/ai_loop_engineering/CURRENT.md` |
| KOL 台账（6 位核心） | `../../02_research/ai_loop_engineering/raw/kol-roster.md` |
| 12 份回源档案（逐字引句） | `../../02_research/ai_loop_engineering/raw/evidence-*.md` |
| 命名谱系判读 | `../../02_research/ai_loop_engineering/digested/01-命名谱系.md` |
| 构件判读 | `../../02_research/ai_loop_engineering/digested/03-构件.md` |
| 控制问题矩阵 | `../../02_research/ai_loop_engineering/digested/07-控制问题矩阵.md` |
| 实践主干（backbone 7 节） | `../../03_practice/loop_governance/result/backbone.md` |
| 操作规程（manual 12 节） | `../../03_practice/loop_governance/result/manual.md` |
| goal/eval 构造 | `../../02_research/agent_goal_eval/` |
| harness 治理（环境轴对照） | `../../03_practice/harness_governance/` |
| Andrew Ng 消化稿 | `../../02_research/ai_loop_engineering/digested/kol/andrew_ng.md` |
| Andrew Ng 素材卡 | `../../01_sources/reference/kol/_raw_loop_engineering/andrew_ng/` |
| 边界判定 | `../../02_research/ai_loop_engineering/digested/05-边界判定.md` |

## 故事在哪

标准档的顺序、公式落在哪一页、口播里不说轮数，都以 `v1/outline/outline.md` 为准。下面这些是研究层的材料索引，不是幻灯片目录。不要按这个清单把故事改回题目摊开。

| 被追问时才翻 | 路径 |
|---|---|
| 两判据、十种失败、停止三件 | `../../03_practice/loop_governance/result/backbone.md` |
| 哪些已经有公开办法、哪四列是空的 | `../../02_research/ai_loop_engineering/result/landscape.md` |

## 三条铁律

1. **用户做选择题，你做创造性劳动。** 生成候选方案，让用户选。
2. **闸门不可跳过。** 每个 Phase 结束等用户确认。
3. **源文件是 single source of truth。** 改动永远从 markdown 开始。

## 前置条件（Phase 0 之前须满足）

- [x] backbone + manual 用户逐段确认（记录在 `03_practice/loop_governance/CURRENT.md`）
- [x] 研究层 `result/landscape.md`（2026-09-27）
- [x] 听众 / scope / 语言：见 `project-metadata.yaml` 与 outline §6

## 当前稿

内容稿在大纲和文稿。画面、PPTX、出图脚本已按用户要求删除，不重建。

| 稿 | 状态 |
|---|---|
| `research/source-synthesis.md` | 素材信号。早于「它说做完了」这一版故事 |
| `v1/outline/outline.md` | 当前故事 |
| `v1/manuscript/manuscript.md` | 主张句与大纲相同。标准 15 页：S02 点明这一转，其后分适合的问题、难处、场合。每页有上屏 |
