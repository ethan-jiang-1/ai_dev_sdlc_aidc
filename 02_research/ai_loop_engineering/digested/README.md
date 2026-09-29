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
| 01 | **命名谱系与操作定义**：词源＝热度碎片、定义＝事后工程化。前四个定义源的核心同指只覆盖「一轮跑完」；Tessl 2026-09-14 的中环/外环暂保留为侦察回源候选，不计第五个已确认定义源。实践层不沿用这个词 | ✅ 已答（2026-09-26 evidence-a；2026-09-27 回填相邻实践，Tessl 候选见 evidence-i2 E2） | [`01-命名谱系.md`](01-命名谱系.md) |
| 02 | **KOL 全景**：谁在说、号召力依据 | ✅ **由台账承载**（[`../raw/kol-roster.md`](../raw/kol-roster.md) 即答案——不另写一篇，防双权威） | — |
| 03 | **构件**：停止条件三件骨架；外层调度是长程扩展。自主度没有轮次刻度；动作门的四种处置（自动放行 / 人批准 / 硬拒绝 / 升级）按出处分开，不合成一台机器 | ✅ 已答（2026-09-26 evidence-b/c；2026-09-27 动作门，evidence-f） | [`03-构件.md`](03-构件.md) |
| 04 | **实战配方**：各家怎么实操 | ➡️ **归并实践层**——操作规程的权威在 [`03_practice/loop_governance/result/backbone.md`](../../../03_practice/loop_governance/result/backbone.md)（§1–§4），本层不重复 | — |
| 05 | **边界判定**：loop / SDD / harness 各管哪层；收敛成立且双向；三条引用归属修正 | ✅ 已答（2026-09-26，evidence-c） | [`05-边界判定.md`](05-边界判定.md) |
| 06 | **Automation → Autonomy → Harness → Loop？**：是阶段迁移、harness 引发，还是控制面逐层外移与构件重命名；DSH 为什么“跑得动但看不清” | ✅ 初步判读（2026-09-27，evidence-e/g/h；P-existence/P-mechanism） | [`06-automation-autonomy-harness-loop.md`](06-automation-autonomy-harness-loop.md) |
| 07 | **控制问题矩阵**：取题 / 授权 / 执行 / 验证 / 停止 / 记忆 / 升档 / 复盘。每格只有已回源做法和它证明不了的事；feature 级空的是授权史、priority 变更、业务阻塞原因、跨 feature 验收 | ✅ 综合判读（2026-09-27，无新一手；A–I） | [`07-控制问题矩阵.md`](07-控制问题矩阵.md) |
| 08 | **KOL 概念对齐**：共同最小交集是 Goal/边界 → 行动 → 环境反馈 → Eval/裁判 → 继续/停止/升级 → 状态与结果分账；Ng 三环是产品反馈与规格演化总图，不是停止条件或自主度 taxonomy；Osmani/Runkle/Claude Code 的外延仍有冲突 | ✅ 已答（2026-09-28，基于 evidence-a/b 与 Andrew Ng 一手素材卡） | [`08-kol-alignment-andrew-ng.md`](08-kol-alignment-andrew-ng.md) |

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
| [`../raw/evidence-2026-09-27-i-high-influence-control.md`](../raw/evidence-2026-09-27-i-high-influence-control.md) | 簇外高影响面：Aider、12-factor、Beck、Willison、Beads、OpenAI harness 全文、Cursor / Copilot 云端循环 | 01 相邻专名；03 §五；06 样本偏差；07 矩阵。不升 KOL §A |
| [`../raw/evidence-2026-09-27-j-local-goal-session.md`](../raw/evidence-2026-09-27-j-local-goal-session.md) | 一条真实 DSH goal 的七字段事后编码。对照臂未跑。`roundsStarted` 为 0 | 07 §五。不是 P-outcome |
| [`../raw/evidence-2026-09-27-k-unrolling-codex-agent-loop.md`](../raw/evidence-2026-09-27-k-unrolling-codex-agent-loop.md) | Codex agent loop 的候选页面摘录：assistant message 据摘录是 turn 的终止态。正题 Unrolling；直接 HTTP 403，待独立复核 | 03 候选裁判语义。不增加 OpenAI 票。不把「四拍」当原文 |
| [`../raw/evidence-2026-09-27-i2-teams-evals-outcome.md`](../raw/evidence-2026-09-27-i2-teams-evals-outcome.md) | I 路批次 2 五切口：控制面候选形态、行为面验证、定量效果、谱系、SDD×loop 组合；档案内逐条区分 `【主验】` 与 `【侦察回源】`，后者须复验，不增加独立票 | 01/06/07 候选增量；P-outcome 场景地图；不自动关闭缺口 |
