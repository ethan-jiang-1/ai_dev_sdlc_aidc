# _artifacts/ — 本轮 Deep Research 的综合产物层（Derived Synthesis Layer）

> 本目录只承载**综合判断**（`derived synthesis`），不替代 [`../_reference/`](../_reference/) 的证据本体，也不替代 [`../../plan/dr-round-1.status.md`](../../plan/dr-round-1.status.md) 的执行状态。

## 定位

- `_reference/*.md` 是单一来源的本地权威副本。
- `_artifacts/*.md` 是跨来源的综合、压缩、对照、判断。
- 每条综合里的关键判断都必须可追溯到具体的 `../_reference/*.md`。

## 本轮必产出清单

按 [`../../plan/dr-round-1.plan.md`](../../plan/dr-round-1.plan.md) 的 `输出契约.3 过程性 Artifacts`：

- 每条研究线一份 `evidence-summary`：`<NN>-<topic-slug>-evidence-summary.md`
- 每条研究线一份 `question-list`：`<NN>-<topic-slug>-question-list.md`
- 一份横向综合：`W2-cross-topic-synthesis.md`
- 一份选型矩阵升级版：`W2-selection-matrix-v2.md`（九维选型矩阵 × KOL / 标准背书，每行带来源）
- 一份 claims-audit 升级版：`W2-claims-audit-v2.md`（基于 Wave 1 新证据重评 [`../claims-audit.md`](../claims-audit.md) 中 10 条断言的证据强度）
- 本 README（导航）

## 命名约定

- 研究线绑定：`<NN>-<topic-slug>-<artifact-type>.md`
- Wave 2 跨主题：`W2-<purpose>.md`
- 不要把 artifact 命名为 `*-reference-*`，避免与 `_reference/` 混淆。

## 产出节奏

| 阶段 | 触发条件 | 产出 |
| --- | --- | --- |
| Wave 1 研究线内 | 每线 `doc_count ≥ wave1_doc_floor_per_topic` 后 | `evidence-summary` + `question-list` |
| Wave 2 开始 | 所有研究线至少完成一轮 stop assessment | 三份 W2-* |
| Readiness Check 前 | 所有交叉验证关闭 | 更新导航（本 README）与 Wave 2 产物末尾的交叉引用 |
