# 证据与来源（唯一登记处 · v0.1）

## 一、语料根（仓库外，只读）

**路径**：`/Users/bowhead/deepseek-harness/_faq_on_digested/07_borrowing-harness-idea/`
（18 件：question / answer / 01–14 / reference / research，约 1700 行；2026-09-25 消化完毕）

- **只在里面读，不写**（与仓库 `talk-*/_reference/` symlink 同一条纪律）。
- 语料家族还有 00–09 兄弟专题（如 `04_root-entry-doc-design`、`06_spec-change-path`）——
  本场当前**只消费 07 号**；确需跨号引用时先在此登记，避免事实散装。

## 二、证据强度（本场自用，沿用仓库四档口径）

| 标注 | 含义 | 本场对应物 |
|---|---|---|
| **一手 · 钉版** | DSH 仓库固定 commit `46a7f68b09`（`dsh-v0.1.7-rc.1`）的 GitHub URL——任何人可点开核对 | DSH 原话、实物文件、演示提交 `5124a2a310` |
| **语料归纳** | FAQ 07 自己的归纳（非 DSH 原文，语料里有标注） | 三层模型、三问自检、L0–L3 阶梯命名、"七缺口"表述 |
| **内部账本** | `research.md`／`reference.md`——整理过程记录，不进上屏 | — |

**红线**：上屏引用 DSH 事实时标 commit；"DSH 原话"逐字引英文；语料归纳与 DSH 原话**不许混标**。

## 三、关键事实登记（摘录 + 出处；storyline 引用的都在这）

| # | 事实 | 出处（语料 → DSH 钉版） | 强度 |
|---|---|---|---|
| 1 | 开发主力自称 coding agents："This codebase is developed primarily by coding agents." | answer／14 → `.agents/notes/implemented/process/2026-06-11-quality-gates.md` | 一手 |
| 2 | "Agents follow enforced gates far more reliably than prose conventions." | answer／09 → 同上 Note | 一手 |
| 3 | "A guard only guards if the regression fails it. … introduce the regression, watch red, revert." | 09 → `docs/testing.md` | 一手 |
| 4 | "Model-visible ⟺ logged"（模型可见的事实必须可从会话日志重建） | 04 → 根 `AGENTS.md` | 一手 |
| 5 | "Each fact has one home: the tier whose job it is; elsewhere, link there." | 02 → `docs/AGENTS.md` | 一手 |
| 6 | `CLAUDE.md` symlink → `AGENTS.md`（仓库 4 处）；`ln -s AGENTS.md CLAUDE.md` | 02／07 → 根 `AGENTS.md` | 一手 |
| 7 | 根 AGENTS.md 字数预算是门禁：`doc-budgets.manifest.json` 逐文件卡上限（根文件 ≤ 1,950 词） | 07 → `docs/AGENTS.md` Wordcount Budgets | 一手 |
| 8 | 演示提交 `5124a2a310`（PR #5004，模型选择器显示 model ID）：7 文件 +15/−14；红灯对照实测 2 红 95 绿 | 01／06 → commit 页 | 一手 |
| 9 | "There is no privileged core to patch"（扩展=挂插件，注册即效果，卸载即 unwind） | 05／10 → `docs/architecture.md` | 一手 |
| 10 | 入口链会话态：touch-driven 注入＋maxBytes＋去重；丢弃顺序"先丢宽的、保最具体的" | 07 → `packages/context/agent-instructions/README.md` | 一手 |
| 11 | 执行链三设计：call 先落日志／策略在工具体外／结果单一出口（异常→isError） | 08 → `docs/tool-execution-pipeline.md` | 一手 |
| 12 | compaction 保留 tool-call/result 配对（"Region boundaries preserve tool-call/result pairing"） | 13 → `docs/subsystems/compaction.md` | 一手 |
| 13 | subagent spawn 不带父历史（"Spawn supplies no history; fork supplies its balanced seed."） | 13 → `packages/subagent/subagent-in-process-driver/README.md` | 一手 |
| 14 | skill catalog 只给 name＋description（≤500 字符），正文按需加载 | 11／13 → `docs/subsystems/skills.md` | 一手 |
| 15 | 决策记录豁免判据："Mechanical or local edits … are exempt."（diff 大小无关，看有没有持久取舍） | 01／03 → `.agents/notes/README.md` | 一手 |
| 16 | 三条立场／三层模型／三问自检／立即借-有压力再借-不照搬／四条边界 | answer（语料归纳） | 语料归纳 |
| 17 | 七个信息缺口（糊涂=1–3／乱发挥=4–6／交付=7） | 14（语料归纳） | 语料归纳 |
| 18 | L0–L3 参与阶梯（组合／扩展点／capability seam／core loop；不是价值排序） | 05（语料归纳自 DSH 归属表逻辑） | 语料归纳 |

## 四、待回源（当前无）

语料自带 reference.md 总账，DSH 侧事实均已钉版；storyline 若新增 DSH 声称，先在此登记再上屏。
