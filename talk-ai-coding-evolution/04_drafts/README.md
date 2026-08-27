# 讲稿与术语规范

## 当前准本：V5

- `ppt-text-v5.md` 是当前权威的 PPT 生产事实稿：完全继承 V4，只重写 P17-P21，并微调 P22 的收束语。它记录 P1-P23 的实际上屏文字、叙事任务、画面构成和不上屏背景。
- `ppt-text-v5-sep.md` 是与主版同步的紧凑分页稿，适合 AI Agent 逐页消费；背景统一使用 blockquote，避免与上屏文字混淆。
- 后续重制、转格式或继续迭代，默认以 **V5 PPTX + 两份 V5 文稿**为准。PPTX 与文稿发生冲突时，以手工调整后的 V5 PPTX 为最终事实来源，再把差异同步回文稿。
- V5 保留 V4 已完成的内容取舍；不要自动把 V1 中未采用的候选文案加回页面。P17 的 GitHub 数据是 2026-08-27 的快照，只能作为 attention / 扩展入口信号使用。

## 历史材料

- `ppt-text-v1.md` / `ppt-text-v1-sep.md` 是前期生产素材：每页包含核心上屏、候选上屏素材和背景。它们适合追溯早期构思与候选文案，但不再是当前生产准本。
- `../03_outline/` 保存较早的页面内容与讲点素材，可用于追溯目的、例子、转场和素材来源。
- `talk-v1.md` 是早期口语讲稿，仅作 speaker notes 参考，非当前交付物。

## 术语规范

PPT 上保留英文的术语，中文只作口播参考：

| 英文（上屏） | 中文表达参考（口播可讲） |
|---|---|
| prompt / context / harness / loop / graph engineering | 提示 / 上下文 / 围栏（harness 建议直接保留）/ 循环 / 图 工程 |
| Agent = Model + Harness | 不译，公式上屏 |
| context rot | 不译，保留英文 |
| Guides / Sensors | 引导 / 感知（标注英文） |
| computational / inferential | 确定性 / 概率性（标注英文） |
| authorize at execution, not at generation | 执行时授权，而非生成时授权 |
| capability seam | 能力接缝（标注英文） |
| adapter / vendor | 适配器 / 供应商（标注英文） |
| provenance / trace | 溯源 / 链路（标注英文） |
| MCP / RAG / CI / AGENTS.md | 保留英文 |
| sandbox | 沙箱（通用译法） |
| "Each fact has one home" | 每个事实只有一个家（金句，双语） |
