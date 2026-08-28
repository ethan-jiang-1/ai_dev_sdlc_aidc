# AGENTS.md — 本目录是 talk 推敲的 harness

一人公司（one person company）的 AI Coding 深度 talk。**你是这套 harness 里被驱动的 agent**：
每次进来按下面的步骤走，改完把状态落回源文件。主题 / 听众 / 时长 / 目的 → `01_storyline/03-audience-and-pitch.md`。
五层演变（Prompt→Context→Harness→Loop→Graph）+ DSH 是素材，**故事线是唯一的核心产物**。

## 每次进来（按顺序走）

1. **读状态** — `README.md`（目录地图）→ `01_storyline/00-storyline-map.md`（故事线总图）→
   `03_outline/00-page-structure-23.md`（现场版页面）→ `01_storyline/04-open-questions.md`（已决 / 待办）。
   完成标准：能说出当前阶段、正在推敲的问题、下一步动哪个文件。

2. **定阶段** — 由用户这轮的话 + open-questions 判定：
   - 推敲故事线 → `01_storyline/`
   - 补论据 / 锚点 → `02_evidence/`
   - 铺大纲 / slide → `03_outline/`（主线稳定即可；现场版 `00-page-structure-23.md`）
   - 写讲稿 → `04_drafts/`（文件名带版本：`talk-vN.md`）

3. **动手** — 按 `01_storyline → 02_evidence → 03_outline → 04_drafts → 05_output` 单向加工；上游结论没有稳定前，不提前在下游定稿。

4. **审成稿** — PPTX 输出后必须逐页做两遍 review：文字（主张、口径、来源、转场）与视觉（层级、对齐、留白、溢出、模板保真）。

5. **反向同步** — 人工或视觉 review 若改变了成稿，以已确认 PPTX 为生产事实，把变化按 `04_drafts → 03_outline → 02_evidence → 01_storyline` 反向同步；不得让旧提纲在下一版复活。

6. **落状态** — 更新 `04-open-questions.md`、`00-storyline-map.md`、`04_drafts/README.md` 与 `05_output/README.md`。
   完成标准：总图、口径、页面职责、生产事实稿、PPTX 与待办一致，没有该更新而未更新的文件。

## 规则

- **单一事实来源**：每个事实只写一处——主线在 `01_storyline/`，素材卡片在 `02_evidence/`。
- **故事线优先**：先定故事线，再写 slide / 讲稿。
- **素材只摘不搬**：从 `_reference/rawdata_*/` 摘进 `02_evidence/` 时标注来源路径。
- **rawdata 只读**：`_reference/` 下的上游 symlink 只在里面读，不在里面写。

## 当前状态指针

- 故事线总图（v1.5）：`01_storyline/00-storyline-map.md`
- 现场版页面结构（23 页 / 45 min）：`03_outline/00-page-structure-23.md`
- 素材与口径：`02_evidence/00-absorption-plan.md`；脉络：`02_evidence/01-info-flow-map.md`
- 当前生产事实稿：`04_drafts/ppt-text-v6.md` / `ppt-text-v6-sep.md`
- 当前交付：`05_output/v6/OPC航海指南-harness-v6.pptx`
- 已决与待办：`01_storyline/04-open-questions.md`
