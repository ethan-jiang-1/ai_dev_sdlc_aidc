# AGENTS.md — 本目录是 talk 推敲的 harness

一人公司（one person company）的 AI Coding 深度 talk。**你是这套 harness 里被驱动的 agent**：
每次进来按下面的步骤走，改完把状态落回源文件。主题 / 听众 / 时长 / 目的 → `01_storyline/03-audience-and-pitch.md`。
五层演变（Prompt→Context→Harness→Loop→Graph）+ DSH 是素材，**故事线是唯一的核心产物**。

## 每次进来（按顺序走）

1. **读状态** — `README.md`（目录地图）→ `01_storyline/00-storyline-map.md`（故事线总图）→
   `01_storyline/04-open-questions.md`（已决 / 待办）。
   完成标准：能说出当前阶段、正在推敲的问题、下一步动哪个文件。

2. **定阶段** — 由用户这轮的话 + open-questions 判定：
   - 推敲故事线 → `01_storyline/`
   - 补论据 / 锚点 → `02_evidence/`
   - 铺大纲 / slide → `03_outline/`（故事线定稿后才做）
   - 写讲稿 → `04_drafts/`（文件名带版本：`talk-vN.md`）

3. **动手** — 只动本阶段该动的文件。

4. **落状态** — 把结论 / 决定写回源文件，更新 `04-open-questions.md` 的勾选、必要时更新 `00-storyline-map.md`。
   完成标准：总图、待办与现实一致，没有该更新而未更新的文件。

## 规则

- **单一事实来源**：每个事实只写一处——主线在 `01_storyline/`，素材卡片在 `02_evidence/`。
- **故事线优先**：先定故事线，再写 slide / 讲稿。
- **素材只摘不搬**：从 `rawdata_*/` 摘进 `02_evidence/` 时标注来源路径。
- **rawdata 只读**：两个 symlink 是原始数据，只在里面读，不在里面写。

## 当前状态指针

- 故事线总图（v0 草案，待按主题重推敲）：`01_storyline/00-storyline-map.md`
- 已决与待办：`01_storyline/04-open-questions.md`
