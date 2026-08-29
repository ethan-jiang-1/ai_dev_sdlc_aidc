# AGENTS.md — 本目录是 talk 推敲的 harness

AI-Native 研发组织的规模化 AI Coding 深度 talk。**你是这套 harness 里被驱动的 agent**：
每次进来按下面的步骤走，改完把状态落回源文件。主题 / 听众 / 时长 / 目的 → `01_storyline/03-audience-and-pitch.md`。
两轴素材（宽轴 = 六阶段 SDLC，深轴 = 五层 + Harness）都是素材，**故事线是唯一的核心产物**。

> 与 `../talk-ai-coding-evolution-opc/` 的差别：那里问「一个人掌握多深」，这里问「研发组织要把整条 SDLC 建成什么能力」。
> 不要照搬 `-opc` 的叙事——五层只是深轴，宽轴是 Anthropic 的六阶段 SDLC playbook。

## 每次进来（按顺序走）

1. **读状态** — `README.md`（目录地图）→ `01_storyline/00-storyline-map.md`（故事线总图）→
   `01_storyline/07-narrative-thinking.md`（叙事思路：看了什么 / 为什么这样想）→
   `03_outline/00-page-structure.md`（现场版页面）→ `01_storyline/04-open-questions.md`（已决 / 待办）。
   完成标准：能说出当前阶段、正在推敲的问题、下一步动哪个文件。

2. **定阶段** — 由用户这轮的话 + open-questions 判定：
   - 推敲故事线 → `01_storyline/`
   - 补论据 / 锚点 / play 拆解 → `02_evidence/`
   - 铺大纲 / slide → `03_outline/`（主线稳定即可；现场版 `00-page-structure.md`）
   - 写讲稿 / 生产事实稿 → `04_drafts/`
   - 选模板 / 产 PPTX → `_asset/` + `05_output/`

3. **动手** — 按 `01_storyline → 02_evidence → 03_outline → 04_drafts → 05_output` 单向加工；上游结论没有稳定前，不提前在下游定稿。

4. **审成稿** — PPTX 输出后必须逐页做两遍 review：文字（主张、口径、来源、转场）与视觉（层级、对齐、留白、溢出、模板保真）。

5. **反向同步** — 人工或视觉 review 若改变了成稿，以已确认 PPTX 为生产事实，把变化按 `04_drafts → 03_outline → 02_evidence → 01_storyline` 反向同步。

6. **落状态** — 更新 `04-open-questions.md`、`00-storyline-map.md`、`04_drafts/README.md` 与 `05_output/README.md`。
   完成标准：总图、口径、页面职责、生产事实稿、PPTX 与待办一致。

## 规则

- **单一事实来源**：每个事实只写一处——主线在 `01_storyline/`，素材卡片在 `02_evidence/`。
- **故事线优先**：先定故事线，再写 slide / 讲稿。
- **素材只摘不搬**：从 `_reference/rawdata_*/` 摘进 `02_evidence/` 时标注来源路径。
- **rawdata 只读**：`_reference/` 下的上游 symlink 只在里面读，不在里面写。
- **对象红线**：对象是「研发整体组织，从产品一路到底到实施 + 运维」；落点始终在
  **整条 SDLC 的转型 / 工件链 / gate / 平台治理 / 合规审计 / 规模化**，不滑回「个人技能进阶」的 `-opc` 叙事。
- **独立红线**：不依赖、不承接 `04_output/deck_ai_sdlc_keynote`（听众不同）；不把「代码不再是瓶颈」讲成普适事实，标注是 Anthropic 论点。
- **模板不预设**：用户明确「PPT 风格不限制，按内容找到最配合的」——`-opc` 的 CLAWTIME 模板**不是**本 talk 的默认；
  到 PPT 生产阶段再按内容选模板，选型理由记入 `_asset/README.md`。
- **临时目录约定**：所有一次性产物（构建中间体、逐页 inspect、审稿草稿、模板试验）
  一律放在仓库根目录、以 `.tmp-org-talk-` 前缀 + 主题命名；工具自动生成的随机名目录（`.ppt-build-*`、`.tmp-xxx.XXXX`）算同类，
  `.gitignore` 覆盖、永不入库。**版本收口时清理**：某一版 PPTX 落进 `05_output/` 并完成 review 后，对应 `.tmp-org-talk-vN*` 及散落目录即删。

## 当前状态指针

- 故事线总图（v0.5 初稿）：`01_storyline/00-storyline-map.md`
- 叙事思路笔记（上下文记忆）：`01_storyline/07-narrative-thinking.md`
- 现场版页面结构（50 页 · 75–90 min 骨架）：`03_outline/00-page-structure.md`
- 素材与口径（六阶段 + 15 play 进货单）：`02_evidence/00-absorption-plan.md`；脉络：`02_evidence/01-info-flow-map.md`（待补）
- 当前生产事实稿：暂无（未到 `04_drafts/` 阶段）
- 当前交付：暂无（未到 `05_output/` 阶段）
- 已决与待办：`01_storyline/04-open-questions.md`
