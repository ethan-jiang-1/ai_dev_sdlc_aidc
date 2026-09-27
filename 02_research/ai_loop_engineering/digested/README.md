# digested — 消化与判读

> **本层是什么**：把 `raw/` 的一手素材消化成**可读的判断**。一问题一篇，编号 = 创建序。
> **判读权威在本层**（`raw/` 是素材权威，`03_practice/loop_governance/` 是操作权威）。未采纳的线索**留原位，不删不隔离**。

## 增长规则

- 新议题 → 建 `NN-<slug>.md`（编号取当前最大 +1）→ 下表加一行。**不改已有编号**。
- 新 KOL 的专项消化 → 建 `kol/<slug>.md`（slug 与 [`../raw/kol-roster.md`](../raw/kol-roster.md) 对齐）。
  **有料才写**——词源碎片级的人（Cherny / Steinberger，见台账定性）不建消化稿，其结论在 digested/01 与时间线。
- 结论过筛后进实践层 [`03_practice/loop_governance/`](../../../03_practice/loop_governance/README.md)；**未过筛的不要搬走**。

## 问题看板

> **编号说明**：02 与 04 **有意不留文件**——02（KOL 全景）由 [`../raw/kol-roster.md`](../raw/kol-roster.md) 承载（台账即答案），04（实战配方）归实践层 [`03_practice/loop_governance/result/backbone.md`](../../../03_practice/loop_governance/result/backbone.md)；**新议题从 06 起编号**。

| # | 议题 | 状态 | 文件 |
|---|---|---|---|
| 01 | **命名谱系与操作定义**：这个词怎么来的（词源＝热度碎片、定义＝事后工程化）、四人是否同指一件事（核心同指、外延不兼容）、为什么实践层不沿用 | ✅ 已答（2026-09-26，evidence-a） | [`01-命名谱系.md`](01-命名谱系.md) |
| 02 | **KOL 全景**：谁在说、号召力依据 | ✅ **由台账承载**（[`../raw/kol-roster.md`](../raw/kol-roster.md) 即答案——不另写一篇，防双权威） | — |
| 03 | **构件**：停止条件与外层调度的收敛判定（三件骨架 / 两种调度形态 / 自主度位置 vs 量化） | ✅ 已答（2026-09-26，evidence-b/c） | [`03-构件.md`](03-构件.md) |
| 04 | **实战配方**：各家怎么实操 | ➡️ **归并实践层**——操作规程的权威在 [`03_practice/loop_governance/result/backbone.md`](../../../03_practice/loop_governance/result/backbone.md)（§1–§4），本层不重复 | — |
| 05 | **边界判定**：loop / SDD / harness 各管哪层；收敛成立且双向；三条引用归属修正 | ✅ 已答（2026-09-26，evidence-c） | [`05-边界判定.md`](05-边界判定.md) |
| 06 | **Automation → Autonomy → Harness → Loop？**：是阶段迁移、harness 引发，还是控制面逐层外移与构件重命名；DSH 为什么“跑得动但看不清” | ✅ 初步判读（2026-09-27，evidence-e/g/h；P-existence/P-mechanism） | [`06-automation-autonomy-harness-loop.md`](06-automation-autonomy-harness-loop.md) |

## 已完成的 KOL 专项消化

| slug | 人物 | 状态 | 素材 |
|---|---|---|---|
| [`kol/andrew_ng.md`](kol/andrew_ng.md) | Andrew Ng | ✅ 通读版 | [`_raw_loop_engineering/andrew_ng/`](../../../01_sources/reference/kol/_raw_loop_engineering/andrew_ng/profile.md) |

**不建消化稿的人**（2026-09-26 台账定性）：Cherny / Steinberger（词源碎片级，无深度内容可消化）、alchaincyf（中文编译非独立发明）。
**素材已归档但走 evidence 档案不建个人卡**：Runkle（四环，evidence-b §4e）、Osmani（两篇，evidence-a）、Huntley（Ralph，evidence-b §1）、Anthropic/OpenAI 机构条目（evidence-b/c）。

## 证据档案索引（本层判读的依据，逐字引句都在这里）

| 档案 | 内容 | 服务的判读 |
|---|---|---|
| [`../raw/evidence-2026-09-26-a-originators.md`](../raw/evidence-2026-09-26-a-originators.md) | 词源与定义者四人（Cherny / Steinberger / Runkle / Osmani） | 01 · 实践层 backbone §0/§4（自报）；backbone §1/§3 亦实引 |
| [`../raw/evidence-2026-09-26-b-stop-and-scheduling.md`](../raw/evidence-2026-09-26-b-stop-and-scheduling.md) | 停止条件与外层调度（9 个一手记录块全文） | 03 + 实践层 §1–§2 |
| [`../raw/evidence-2026-09-26-c-autonomy-and-convergence.md`](../raw/evidence-2026-09-26-c-autonomy-and-convergence.md) | 自主度阶梯与 SDD 对照面 | 03 §三 + 05 + 实践层 §3–§4 |
| [`../raw/evidence-2026-09-27-e-cross-feature-observability.md`](../raw/evidence-2026-09-27-e-cross-feature-observability.md) | Anthropic Managed Agents、OpenClaw tasks/flow、feature_list 的在途/授权/阻塞/验收/恢复状态矩阵 | 06 + 03 外层调度扩展；P0 跨 feature 缺口 |
| [`../raw/evidence-2026-09-27-f-autonomy-gates.md`](../raw/evidence-2026-09-27-f-autonomy-gates.md) | Codex action policy、拒绝升级、Spec Kit/OpenSpec 歧义门、LangChain HITL、授权漂移反例 | 03 §三；实践层自主度/检查点候选，尚非规范 |
| [`../raw/evidence-2026-09-27-g-dsh-control-surface.md`](../raw/evidence-2026-09-27-g-dsh-control-surface.md) | DSH goal/driver/todo/plan/session persistence 的原生控制面与跨 feature 边界 | 06；DSH 对照与 FAQ 15 体感定位 |
| [`../raw/evidence-2026-09-27-h-automation-to-autonomy.md`](../raw/evidence-2026-09-27-h-automation-to-autonomy.md) | automation/autonomy/harness/loop 时间轴、概念依赖、竞争解释与因果边界 | 06；不支持单向阶段史/简单因果 |
