# AGENTS.md — 这场 keynote 的叙事

> 2026-09-27 用户定：本目录的 agent **只提供 PPT 的内容**。
> 内容指叙事：结构、系统、故事是否往前走、主张是否自洽。
> 页的版式、画面、PNG、风格母版、PPTX，不在这个 agent 的工作里。那些文件若已存在，当作停掉的试验，不续做、不修图。

## 做完的标准

一次内容改动做完，当且仅当下面四条同时成立：

1. **结构**：每一页只推进故事的一步。两场都是平铺单档；追问的答案进备注，不开加深页。
2. **系统**：公式里的每个因子都能在大纲里指到页；多出来的页要写明它为什么不是第四个因子。
3. **叙事**：听众能用一句话接上下一页。接不上的页，删或并。
4. **自洽**：各场大纲（`intro/outline/outline.md`、`advanced/outline/outline.md`）的主张句与该场文稿的 CLAIM 是同一句。上屏的 subtitle 用这一句。研究层的边界写在讲者备注或 callout，不另起一套主张。

内容权威是大纲，展开在文稿。

## 项目定位

- **讲的事**：你离开之后它继续跑，你回来时它说做完了。整场回答你凭什么信。
- **两场分稿（2026-09-27 用户定）**：`intro/` 入门场（约 20 页，没跑过循环的通识听众，业务与管理为主）；`advanced/` 技术/产品场（在跑循环的工程师与产品，机制放开讲）。两场各自 outline → manuscript，互不搬页。原统一稿（标准 15 + 加深 10）已全部迁入两场，按用户决定移除。
- **语言**：中文短句。术语进备注，不进主张句。各场细则见其大纲的语言节。
- **源**：上游只有两处——研究层 `../../02_research/ai_loop_engineering/`，实践层 `../../03_practice/loop_governance/`。主张不超出两处成稿：`result/landscape.md` 与 `result/backbone.md`。本目录是它们的加工下游；核出处时读两个上游各自的 README。

## 内容流程

```
素材里哪几句能进故事    →  research/source-synthesis.md
入门场的故事与每页主张  →  intro/outline/outline.md
入门场每页怎么说        →  intro/manuscript/manuscript.md
技术产品场的故事与主张  →  advanced/outline/outline.md
技术产品场每页怎么说    →  advanced/manuscript/manuscript.md
每页上屏                →  同场文稿的 title / subtitle / content
```

上屏给后面的做片用——**做片方未必懂 loop engineering，写少了会乱发挥**。title 短，subtitle 等于主张句，只读二者应能跟上论证。content 分两档：第一档「必须写出」是这页的最小完整版面，缺一行这页就不成立；第二档 nice to have 版面有余再上，放不下整档舍弃。引用块是给做片的补充材料——这页的意思、词解、禁止、版面——永远不上屏，拿不准时以它为准。红、绿、灯只允许出现在引用块里。本目录仍不出 PPTX、PNG、风格母版。

改故事先改该场的大纲，再改该场文稿，使两处的主张句重新相同。

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

各场的顺序、公式落页、口播不说轮数，以该场大纲为准。下面这些是研究层的材料索引，不是幻灯片目录。不要按这个清单把故事改回题目摊开。

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

内容稿在各场的大纲和文稿。画面、PPTX、出图脚本已按用户要求删除，不重建。

| 稿 | 状态 |
|---|---|
| `research/source-synthesis.md` | 素材信号。早于「它说做完了」这一版故事 |
| `intro/outline/outline.md` | 入门场大纲（19 页），2026-09-27 用户过闸 |
| `advanced/outline/outline.md` | 技术产品场大纲（27 页），2026-09-27 用户过闸 |
| `intro/manuscript/manuscript.md` | 入门场文稿草案：19 页，主张句与大纲相同，四轴与红线自查过，待用户收口 |
| `advanced/manuscript/manuscript.md` | 技术产品场文稿草案：27 页，主张句与大纲相同，四轴与红线自查过，待用户收口 |
