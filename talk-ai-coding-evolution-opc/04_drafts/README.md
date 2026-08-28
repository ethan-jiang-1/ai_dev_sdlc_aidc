# 讲稿与术语规范

## 当前准本：V8

- `ppt-text-v8.md` 是当前权威的 PPT 生产事实稿：继承 V7，并在完整 P1-P23 叙事复核后重写 P3、P6、P9、P10、P13、P15、P18、P19、P21、P22。
- `ppt-text-v8-sep.md` 是与主版同步的紧凑逐页稿，适合 AI Agent 按页读取。
- 后续重制、转格式或继续迭代，默认以 **V8 PPTX + 两份 V8 文稿**为准。PPTX 与文稿发生冲突时，以完成文字、视觉与模板复核的 V8 PPTX 为最终生产事实，再把差异同步回文稿。
- P17 的 GitHub 数据是 2026-08-27 的快照，只能作为 attention / 扩展入口信号；P21 的四项决定权与“部件可借，边界自己定”是本 talk 的解释性结论，不冒充 DSH 官方原话。

## 历史材料

- `ppt-text-v1.md` / `ppt-text-v1-sep.md` 是前期生产素材：每页包含核心上屏、候选上屏素材和背景。它们适合追溯早期构思与候选文案，但不再是当前生产准本。
- `ppt-text-v5.md` / `ppt-text-v5-sep.md` 对应上一版成稿，只用于版本追溯。
- `ppt-text-v6.md` / `ppt-text-v6-sep.md` 对应 V6 成稿，只用于版本追溯。
- `ppt-text-v7.md` / `ppt-text-v7-sep.md` 对应 V7 成稿，只用于版本追溯。
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
