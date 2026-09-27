# WORKFLOW — 这场 keynote 的叙事流程

> 本目录的 agent 只写内容。页、画面、PNG、PPTX 不在此流程里。
> 范围以 `AGENTS.md` 开头的定为准。历史稿 `deck_ai_sdlc_keynote` 有自己的出图管线，不搬到这里来跑。

---

## 内容怎么往前走

```
素材里哪几句能进故事    →  research/source-synthesis.md
入门场的故事与每页主张  →  intro/outline/outline.md
入门场每页怎么说        →  intro/manuscript/manuscript.md
技术产品场的故事与主张  →  advanced/outline/outline.md
技术产品场每页怎么说    →  advanced/manuscript/manuscript.md
```

做完的标准是 `AGENTS.md` 的四条：结构、系统、叙事、自洽。

---

### Phase 0 — 素材合成（research/）

**你在哪个目录工作**：`research/`

**素材来源**（与 `deck_ai_sdlc_keynote` 完全不同）：

| 来源 | 提供什么 |
|---|---|
| `02_research/ai_loop_engineering/result/` | landscape 综述成稿（从 digested 过筛） |
| `02_research/ai_loop_engineering/digested/` | 命名谱系、构件、边界判定、控制问题矩阵 |
| `02_research/ai_loop_engineering/raw/kol-roster.md` | KOL 名单权威（6 位核心） |
| `02_research/ai_loop_engineering/raw/evidence-*.md` | 12 份回源档案（逐字引句） |
| `03_practice/loop_governance/result/backbone.md` | 实践主干 §0–§6（定义/停止条件/调度/自主度/检查点/接口/升格） |
| `03_practice/loop_governance/result/manual.md` | 操作规程 12 节 |
| `02_research/agent_goal_eval/` | goal/eval 构造（如作为子话题纳入） |
| `03_practice/harness_governance/` | 环境轴对照（harness 与 loop 的同构关系） |

**产出**：`research/source-synthesis.md`

**⛔ 闸门**：信号抽取准确、无重大遗漏 → 进入 Phase 1

---

### Phase 1 — 叙事大纲（intro/outline/ 与 advanced/outline/）

**产出**：`intro/outline/outline.md` 与 `advanced/outline/outline.md`（两场各自过闸）

**内容**：
```
1. 核心判断与核心公式（可证伪）
2. Narrative Arc（叙事弧：只读 title+subtitle 应能复述）
3. 页面清单（每页 title + 一句话主张）
4. 公式落在哪一页（因子 → 页）
5. 语言纪律（本场红线与术语档）
```

**⛔ 闸门**：隐喻不是"差不多"是"就是它"、公式可证伪、故事线成立 → Phase 2

---

### Phase 2 — 完整文稿（intro/manuscript/ 与 advanced/manuscript/）

**产出**：各场 `manuscript/manuscript.md`（该场大纲过闸后逐场展开）

每张 slide 展开为：主张句（与大纲相同）+ 上屏（title / subtitle / content，复杂页加 callout）+ 口播 + 接到下一页 + 备注。subtitle 等于主张句。content 把这一步说满，供后面的做片使用。备注放证据和不能说的边界。

**⛔ 闸门**：主张句与大纲相同，通读能接上下一页。到此为止。

---

## 改故事时

先改该场大纲，再改该场文稿，直到两处主张句相同。

## 前置条件

- [x] `03_practice/loop_governance/result/backbone.md` 与 manual 已确认
- [x] `02_research/ai_loop_engineering/result/landscape.md`
- [x] 听众 / scope / 语言见 `project-metadata.yaml`
