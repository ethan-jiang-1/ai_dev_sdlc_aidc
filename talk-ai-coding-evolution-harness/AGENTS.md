# AGENTS.md — 本目录是 talk 推敲的 harness

AI Coding 演变与 harness 的深度 talk。**你是这套 harness 里被驱动的 agent**：
每次进来按下面的步骤走，改完把状态落回源文件。
主题 / 听众 / 时长 / 目的 → `01_storyline/03-audience-and-pitch.md`。
本目录词义以 `CONTEXT.md` 为唯一权威；当前进度以 `CURRENT.md` 为唯一权威入口。
**五层演变（Prompt→Context→Harness→Loop→Graph）+ Pi / DSH 是素材，故事线是唯一的核心产物。**
**全场主轴：这次改动，凭什么可以上线？**（v3 定，见 `01_storyline/00-storyline-map.md`）

## 每次进来（按顺序走）

0. **新对话入口** — **最短路径**：延续性工作且无争议 → 直接读 `CURRENT.md`（唯一当前态·热区）即可动手；
   首次进入或踩坑 → 再读本文件与 `README.md`。`CURRENT-history.md` 是冷区（历轮改动记录），
   只在回查历史时读，默认不读，不是第二权威。
   纪律、陷阱与生产工具链在**本文件**；词义在 `CONTEXT.md`。
   > 2026-09-17：原 `HANDOFF.md` 已归档。它是给某一次对话的临时交接件，长期留在目录里
   > 会与 `CURRENT.md` 形成双权威。其仍有效的内容已并入本文件（见「已知陷阱」「生产工具链」）。
   > 2026-09-21：`CURRENT.md` 拆热/冷区，历轮流水移入 `CURRENT-history.md`（约定见根 `AGENTS.md` §1/§3）。
1. **读状态** — `README.md`（地图）→ `CURRENT.md`（唯一当前态）→ `CONTEXT.md`（术语与禁用词）→
   `01_storyline/00-storyline-map.md`（故事线总图）→ `03_outline/00-page-structure-v3.md`（页面职责）→
   `01_storyline/04-open-questions.md`（已决 / 待确认 / 待办）。
   完成标准：能说出当前阶段、正在推敲的问题、下一步动哪个文件，并能用 `CONTEXT.md` 的词义区分
   harness、运行边界、固定 harness 与可组合 harness。
   新对话不得依赖旧聊天记录代替上述文件；目录状态与聊天记忆冲突时，以目录中已落盘且彼此一致的当前态为准。

2. **定阶段** — 由用户这轮的话 + open-questions 判定：
   - 推敲故事线 → `01_storyline/`
   - 补论据 / 口径 → `02_evidence/`
   - 铺大纲 / 页面职责 → `03_outline/`
   - 写讲稿 / 生产事实稿 → `04_drafts/`
   - 表现设计 / 产 PPTX → `05_output/`

3. **动手** — 按 `01_storyline → 02_evidence → 03_outline → 04_drafts → 05_output` 单向加工；
   上游结论没有稳定前，不提前在下游定稿。

4. **审成稿** — PPTX 输出后必须逐页做两遍 review：文字（主张、口径、来源、转场）与视觉
   （层级、对齐、留白、溢出、模板保真）。

5. **反向同步** — 人工或视觉 review 若改变了成稿，以已确认 PPTX 为生产事实，
   把变化按 `04_drafts → 03_outline → 02_evidence → 01_storyline` 反向同步；不得让旧提纲在下一版复活。

6. **落状态** — 更新 `01_storyline/04-open-questions.md`、`00-storyline-map.md` 与 `CURRENT.md`。
   完成标准：总图、口径、页面职责、生产事实稿、PPTX 与待办一致，没有该更新而未更新的文件。

7. **做一致性审计** — 每次新增或改变关键决定后，检查对象边界、37 页职责、中文术语、证据标注、
   阶段状态；同一事实只保留一个权威来源，其他文件用指针引用。

8. **对齐术语** — 用户使用含混、临时或与 `CONTEXT.md` 冲突的词时，先指出可能对应的已定义概念，
   再确认实际所指；达成一致后立即更新 `CONTEXT.md`，其他文件只引用。

## 两阶段门禁

### A. 内容 REVIEW（当前阶段 · 未通过）

先回答「为什么讲、对谁讲、听完要发生什么改变」，再考虑「一页怎么长」。REVIEW 固定按以下顺序：

1. **沟通任务**：一句话写清「听众应该理解 / 相信 / 决定 / 行动什么，因为什么」。
2. **核心命题**：一个中心结论，由 3–5 个必要主张支撑；所有术语、边界与因果口径一致。
3. **累进故事线**：每一幕回答上一幕留下的问题，同时产生下一幕的必要性；议程与素材目录不算故事线。
4. **论据与意义**：每个关键主张都有可追溯论据，并说清「它对这批听众意味着什么」；
   外部观点明确归属，未证实内容进 `04-open-questions.md`。
5. **开场与收束**：开场建立值得听的张力，收束必须解开它，并把听众带到明确判断或下一步。

**内容锁定标准**：上述五项在 `01_storyline/` 中均有明确、互不矛盾的答案；
核心主张在 `02_evidence/` 中均有来源或被标为待验证；从开场到收束能用 5–8 分钟口述且无逻辑跳转。
未达标时继续改上游；37 页提供稳定边界，不代表页面职责已通过内容锁定。

### B. 表现设计与 PPTX 生产（未开始）

1. 先定每页的叙事职责和主要结论，再决定版式、图表、节奏。
2. 一页一个叙事任务；标题直接说结论，证据与当页结论同屏咬合。
3. **先过中文编辑门**：页面结论、上屏文字与讲稿都要按中文原生句法重写并通过朗读检查；
   英文只作必要术语或代码标识，不拿英文句法套中文词。
4. **视觉方向按 `README.md` 与 `CONTEXT.md` 已定方案**：纸白底 + 代码终端母题，
   等宽字体承担代码 / 命令 / 日志 / 指标，深墨承担标题与结构线，
   语义色只保留青绿（active path / 反馈）、朱红（门禁 / 风险）、琥珀（已提交工件 / 证据）。
   **不套第三方模板、不引入活动方视觉元素。**
5. **图源策略：全原生矢量。** 信息结构图、五层关系图、对照表、时间线、代码块、
   终端构件一律用可编辑图元绘制。不依赖 AI 生图，避免文字失真与风格漂移。
6. 中文编辑门通过后，再按页面职责铺生产事实稿，最后进 PPTX。
7. 每个外部非平凡主张标注来源与**证据强度**；PPTX 在 speaker notes 中保留 `[Sources]` 块。
8. 最终 PPTX 每页完整渲染并逐页检查；文字 REVIEW 与视觉 REVIEW 均通过后才交付。

表现阶段如果暴露了命题、证据或转场问题，立即退回内容 REVIEW，先修正上游源文件，再重做页面。

## 中文编辑门

这是一场中文演讲。中文负责叙述和推理，英文只负责标识确实需要保留的术语、产品名与代码。

1. **从意思出发重写**：先确定这句话要说清的判断，再用中文重新组织主语、动作和结果；不逐词搬运英文句法。
2. **标题能直接讲出口**：优先使用完整判断或自然提问；避免名词连续堆叠、斜杠串词、箭头代替因果。
3. **术语中文先行**：正文统一使用「运行边界、门禁、执行记录、交付底线」这类说法；
   `harness`、`runtime`、`skill`、`plugin`、`gate` 等没有稳定等价词或承担精确机制含义的词可以保留，
   但必须嵌进自然中文句子，不能充当中文谓语。
4. **一句只推进一个判断**：先给结论，再补条件、证据或例外。
5. **完成前朗读**：逐页朗读标题、上屏文字与关键转场。凡是需要倒回去才能读懂、
   或离开英文词就说不清的句子，继续改写。

## 规则

- **单一事实来源**：每个事实只写一处——主线在 `01_storyline/`，素材卡片在 `02_evidence/`。
- **术语单一来源**：本 talk 的局部词义只在 `CONTEXT.md` 定义；其他文件消费这些词，不重复定义。
- **故事线优先**：先通过内容锁定，再写页面文案 / 讲稿，最后做视觉与 PPTX。
- **素材只摘不搬**：从 `_reference/rawdata_*/` 摘进 `02_evidence/` 时标注来源路径与证据强度。
- **rawdata 只读**：`_reference/` 下的上游 symlink 只在里面读，不在里面写。
- **对象红线**：听众是**做团队协作开发、交付物对可靠性 / 合规 / 审计要求高、质量门槛高**的软件团队。
  论证必须落在**一致性 / 门禁 / 责任归属 / 交付可追溯**，不要滑向个人技能进阶。
- **引用红线**：audience-facing 文字**不出现 OPC / 一人公司 / 姊妹项目引用**。
- **行业红线**：**不点听众所属行业名，不用行业专属术语**；听众特征一律用通用描述承载。
- **议题红线**：圈住 / 拦住 / 看清是桥，不是终点。**不把这场讲成合规或安全培训。**
- **证据红线**：外部数字一律按 `CONTEXT.md` 四档标注；会漂移的值标观测日期；
  口径不可比的两个数字不合成一个。四条解释性结论（见 `02_evidence/00-absorption-plan.md` 第二节）
  必须认领为"本 talk 的判断"，不假借上游报告背书。
- **反软广纪律**：讲 Pi 与 DSH 时优点与代价必须同屏；收尾必须包含"什么时候别折腾"。
- **版本单一纪律**（2026-09-17 定）：被取代的旧版本**移出本目录**，归档到仓库根
  `.tmp-harness-talk-archive-YYYYMMDD/`。目录里只留当前版本，避免旧页码 / 旧编号把下一轮带偏。
- **视觉红线**：纸白画布统一底色；不使用整页黑底章节或深浅交替；语义色只作强调，不单独编码含义。
- **临时目录约定**：一次性产物一律放仓库根目录、以 `.tmp-harness-talk-` 前缀 + 主题命名，
  `.gitignore` 覆盖、永不入库；版本收口时清理对应目录。

## 已知陷阱（反复踩过，动手前先扫一遍）

| # | 陷阱 | 正确做法 |
|---|---|---|
| 1 | Pi 有没有 MCP，两个版本在打架 | 采信有源码锚点的一方：**无 MCP/ACP 实现**。讲"生态锁在自家 extension API，外部工具要付适配层税" |
| 2 | Pi 的"无沙箱"怎么说 | **不说"不安全"**。说"Pi 把信任放在『谁装了它』，而不是『它是什么代码』上" |
| 3 | Codex 的数字口径 | **⚠️ 厂商自述**，无第三方审计；一手原文是"**输出** token 少 6 倍"，同屏必标证据强度 |
| 4 | 8-harness 对照实测 | **⚠️ 趋势级**，无方法论。只作方向性信号，**不作基准** |
| 5 | Pi 星数 / DSH 插件数 | 会漂移的值，标观测日期；DSH 的 2000 / 3000 来自不同第三方商店，**口径不可比，不合成** |
| 6 | DSH 的机制表述 | **DSH 的原生机制不是 MCP**。说 `ctx.llm` adapter、`ctx.tools`、capability seam、plugin |
| 7 | 2026 授权事故 | 只讲**因果链**，不点名厂商、不堆 CVE 编号 |
| 8 | 四条"本 talk 的判断" | 讲述时要认领（"我的判断是……"），**不假借上游报告背书** |
| 9 | 把 harness 讲成层级 | 不是"最高层"，是每次动作都绕不开的**运行边界**；五层是叠加，不是包含 |
| 10 | Graph 与 Loop 的关系 | Graph 可以编排 Loop，**不能把所有 Graph 节点画成 Loop** |
| 11 | `_reference/` 检索 | 全是 symlink，`Grep` / `find` 默认不跟随，**必须加 `-L`** |
| 12 | 截图核对页序 | 只认 `slides/NN.slide` 的文件序号；**核页数用 `ls ppt/slides/*.xml`**，不要用 `ls ppt/slides/`（会数进 `_rels`） |
| 13 | 并行 Edit 同一文件 | 会互相覆盖（都返回成功，内容被后写的盖掉）。多处修改**串行执行**，或用一个脚本一次 replace |
| 14 | ~~批量 `upsert-dsl` 被中断~~ | **已随生成器路线作废（2026-09-17）**；若重建生成器再启用 |

**引用任何外部数字前，先查 `02_evidence/00-absorption-plan.md` 第三节（15 条口径红线）。**

## 生产工具链

> **⚠️ 2026-09-17 起旧路线整体作废**：不再走「生成器 → `.slide` → `slidep` → PPTX」。
> 生成器目录 `.tmp-harness-talk-deck-v3/` 已清理，`slidep` 及以下全部生成器经验**仅当历史参考 / 需重建生成器时再读**。
> **当前生产路线以 `CURRENT.md` 第 0 条为唯一权威**：本仓库只当内容事实源——改内容改上游五个管道目录，
> 重新合成 handoff 稿（`05_output/handoff/`），版式由外部 PPT 工具重做；不手改 `.slide` / PPTX。

<details>
<summary>【作废】旧生成器（slidep）工具链备忘</summary>

- CLI：`slidep` —— `/Users/bowhead/.workbuddy/binaries/node/versions/22.22.2-3/bin/slidep`（依赖已废弃的 `.workbuddy` 路径，随时可能失效）。
  子命令：`create` / `upsert-dsl --page-index N`（`-1` 追加）/ `validate` / `lint` / `screenshot --page-index N --out`。
  `lint` 就是内置布局诊断，不要自己写脚本量 rect。
- 三个必踩的坑：① JSX 样式值**必须带引号**（`background: "#FAFAF7"`），数字保持无引号；
  ② 文本里的裸花括号要转义（`loop {` → `&#123;`）；③ 复合值（`"28px 64px 24px"`）也要引号。
- DSL 里 Text 节点不吃 height，行高压在 Box 上（`minHeight`），否则版面会塌。
- 大字折行体检式：`半角单位 = sum(2 if 全角 else 1)`；56px 下 **1 单位 = 28px**。

</details>

- 本机沙盒**禁止 sudo**；需提权用 `osascript -e 'do shell script "..." with administrator privileges'`。

## 素材速查（只读 symlink，只摘不搬）

| 讲什么 | 去哪读 |
|---|---|
| 五层演变的宏观弧线与锚点 | `rawdata_ai-coding-evolution-final/final_v4/`（01–06 章） |
| 11 候选 harness 选型、评分卡、路线对照 | `rawdata_harness-selection-final/final_v3.md`（§2、§5.4、§5.5） |
| **Pi 的结构与代价（源码锚点）** | `rawdata_pi-digested/harness/01-Architecture/` + `.../02-Boundaries/` |
| **Pi vs DSH 逐面对照** | `rawdata_pi-faq-on-digested/06_pi_vs_dsh/04_strengths_weaknesses.md` |
| DSH 机制（无特权核心 / 会话日志 / 四种模式） | `rawdata_harness-selection-final/final_v3.md` §5.5 + `rawdata_dsh-digested/` |
| **DSH 插件生态（借力的好处 / 代价）** | `rawdata_dsh-plugin-ecosystem/00-map.md` + `04-plugin-taxonomy.md`（2026-09-15 快照，⚠️ 趋势级） |
| 圈住 / 拦住 / 看清的分解 | `rawdata_dsh-faq-on-digested/07_borrowing-harness-idea/answer.md` |
| 一手来源卡片层（305 张） | `rawdata_ai-coding-evolution-reference`（137）+ `rawdata_harness-selection-reference`（168） |

**源头冲突时以有源码锚点的一方为准**；摘进 `02_evidence/` 要标来源路径与证据强度。

## 当前状态指针

- 故事线总图（v2.2）：`01_storyline/00-storyline-map.md`
- 核心论点与立场：`01_storyline/01-thesis-and-positions.md`
- 推导句清单（〔前提〕〔推导〕〔结论〕〔边界〕）：`01_storyline/02-turning-points.md`
- 听众与 pitch：`01_storyline/03-audience-and-pitch.md`
- harness 里头干啥：`01_storyline/06-harness-internals.md`
- 素材与口径：`02_evidence/00-absorption-plan.md`
- 页面职责（37 页骨架）：`03_outline/00-page-structure-v3.md`
- 页面文案（37 页 + 停顿页）：`04_drafts/ppt-text-v3.md`
- 对外交付稿（handoff，当前生产路线）：`05_output/handoff/AI-Coding-演变指南-全页内容-v3.3.md`
- 当前 PPTX（42 张，内容与页序对照）：`05_output/v0.4/AI Coding 演变指南/`
- 已决 / 待确认 / 待办：`01_storyline/04-open-questions.md`
- 当前阶段与下一步：`CURRENT.md`
