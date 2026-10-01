# WORKFLOW — 这场 keynote 的叙事流程

> 本目录的 agent 只写内容。页、画面、PNG、PPTX 不在此流程里。
> 范围以 `AGENTS.md` 开头的定为准。历史稿 `deck_ai_sdlc_keynote` 有自己的出图管线，不搬到这里来跑。
> **2026-10-01 重排**：两场以阶梯（capability_ladder 交接面）为主脊柱；新增开场故事页与「高手的错觉」收尾页；**叙事性=调性把控**，进入每轮打磨的固定考核（见文末「调性与叙事的把控」）。

---

## 内容怎么往前走

```
素材里哪几句能进故事    →  research/source-synthesis.md
入门场的故事与每页主张  →  intro/outline/outline-intro.md
入门场每页怎么说        →  intro/manuscript/manuscript-intro.md
入门场练什么、怎么判卷  →  intro/practice/（exercises + facilitator）
技术产品场的故事与主张  →  advanced/outline/outline-advanced.md
技术产品场每页怎么说    →  advanced/manuscript/manuscript-advanced.md
技术产品场练什么、怎么判卷 →  advanced/practice/（exercises + facilitator）
听众带走的操作件        →  manual/循环交接手册.md（单文件双篇）
```

做完的标准是 `AGENTS.md` 的四条：结构（**一页一概念**）、系统、叙事、自洽。页数预算是下限：入门 20+／技术 30+，宁可拆页加承接/呼吸页，不硬挤。

---

### Phase 0 — 素材合成（research/）

**你在哪个目录工作**：`research/`

**素材来源**：

| 来源 | 提供什么 |
|---|---|
| `02_research/01_agent_engineering/loop_engineering/result/landscape.md` | 综述成稿（含 §3.5 交接面——阶梯主张的引用依据） |
| `02_research/01_agent_engineering/loop_engineering/capability_ladder/` | LE 交接面判定（00-map）、逐档教学档案、结果可信闭环 |
| `02_research/01_agent_engineering/loop_engineering/digested/` | 命名谱系、构件、边界判定、控制问题矩阵 |
| `02_research/01_agent_engineering/loop_engineering/raw/evidence-*.md` | 回源档案（逐字引句） |
| `03_practice/loop_governance/result/backbone.md` | 实践主干（判据/失败模式/检查点） |
| `03_practice/loop_governance/result/manual.md` | 操作规程 13 节（含 §13 授权面） |
| `02_research/01_agent_engineering/goal_eval_engineering/` | goal/eval 构造（如作为子话题纳入） |
| `03_practice/harness_governance/` | 环境轴对照 |

**产出**：`research/source-synthesis.md`

**⛔ 闸门**：信号抽取准确、无重大遗漏 → 进入 Phase 1

---

### Phase 1 — 叙事大纲（intro/outline/ 与 advanced/outline/）

**产出**：`intro/outline/outline-intro.md` 与 `advanced/outline/outline-advanced.md`（两场各自过闸）

**内容**（v3 阶梯脊柱版）：

```
1. 开场故事与核心判断（系统接替逐次提示→「写 loop」；有反馈才可调整，不保证修对；收尾回收「需要锻炼」）
2. 定档四问（系统：每档给一遍答案，替代单条公式）
3. Narrative Arc（叙事弧：只读 title+subtitle 应能复述）
4. 页面清单（每页 title + 一句话主张；一页一个概念；承接/呼吸页标出）
5. 反馈双路落点（环境反馈基建／人的反馈，各在哪些页承重）
6. 语言纪律（本场红线、术语档、比喻标注）
```

**⛔ 闸门**：隐喻不是"差不多"是"就是它"、故事只立不贬、阶梯递进成立、四问贯穿 → Phase 2

---

### Phase 2 — 完整文稿（intro/manuscript/ 与 advanced/manuscript/）

**产出**：`intro/manuscript/manuscript-intro.md` 与 `advanced/manuscript/manuscript-advanced.md`（该场大纲过闸后逐场展开）

每张 slide 展开为：主张句（与大纲相同）+ 上屏（title / content，**content ≤3 条**）+ 展开 + 接到下一页 + 追问卡。subtitle 等于主张句。承重证据可用上屏 callout；同页备注保留完整出处、原句与边界。做片说明区分作者定义、产品机制、个人案例和本场编排，避免把教学映射排成行业标准。表格也计可读负担，不用表格绕过三条限制。

**⛔ 闸门**：主张句与大纲相同，通读能接上下一页，无超载页。到此为止。

---

### Phase 3 — 调性与叙事的把控（每轮打磨的固定考核）

> PPT 是一种叙事。内容改完不算完，每轮都要按下面五维跑一遍 review（对应 ongoing goal 的考核）；任何一维不合格即修，修完复跑。

| 维度 | 考什么 | 具体标准 |
|---|---|---|
| 系统性 | 四问/检查表是否贯穿 | 定档四问在开场提出、逐档给答案、收尾回扣 |
| 结构性 | 一页一概念、承接/呼吸 | 每页一个概念；content ≤3 条；转折有呼吸页；无超载页 |
| 一致性 | CLAIM = 大纲主张句 | 逐页机械比对（脚本跑），subtitle 用同一句 |
| 自洽性 | 主张不超上游 | 每条主张能指到 landscape / backbone / manual / ladder；参数带锚 |
| **叙事性（调性）** | 它是不是一个好故事 | ①承诺-回收：开场的问题与故事，收尾必须回收；②逐页交接：每页「接到下一页」一句话成立；③一线贯穿：阶梯与反馈双路全场反复出现并逐档升级，不中途消失；④转折呼吸：票价/错觉/收束等转折有呼吸，不堆叠；⑤无孤儿概念：讲的每个概念后来都被用到 |

**调性红线**（叙事的"怎么说"纪律）：

- 故事只立不贬、不贩卖焦虑；用已核一手定义支撑「系统接替逐次提示」，署名引句或意译保留作者、来源与日期。反馈是燃料，不保证修正成功；收尾回收「需要锻炼」。
- 「抽卡」是教学比喻，首现标注；「高手的错觉」只对硬核听众讲（技术场尾部），入门场不出现。
- 留在低档是合法驻留——不说成失败、退路或没资格。
- 短句，大陆中文习惯；主张句不依赖英文。
- 承接页/呼吸页是节奏的一部分，不是浪费页数。

**⛔ 闸门**：五维全过 + 两场/手册/练习互相接力不断裂 → 收口。

---

## 改故事时

先改该场大纲，再改该场文稿，直到两处主张句相同；然后重跑 Phase 3 的五维 review——结构性改动（插页/删页/换序）之后，叙事性考核必须整场重走，不能只看改动页。

## 前置条件

- [x] `03_practice/loop_governance/result/backbone.md` 与 manual §0–§12 已确认（§13 待复核）
- [x] `02_research/01_agent_engineering/loop_engineering/result/landscape.md`（含 §3.5 交接面）
- [x] 听众 / scope / 语言见 `project-metadata.yaml`
