# W1-01 Engineering Paradigm Question List

## Must Answer

- 在 AI-native 开发里，最小可行的“结构化规格语言”是什么？
- tests 什么时候应被视为 primary spec，而不是 secondary verification？
- constraint-aware generation 与传统类型系统、contract system、state-based modeling 的关系是什么？
- large AI-generated PR 的风险主要来自体量、跨模块扩散，还是 intent 丢失？
- 哪些环节可以被 AI-assisted review 吸收，哪些环节必须保留 human judgment？
- 如何机械性地阻止 AI 把系统带回大批量、低频交付？
- AI coding pipeline 中的最小可执行切片控制集是什么：branch lifetime、active branch count、required checks、merge queue、deployment gate、feature flag、canary，还是还需要 diff risk scoring？

## High-Value Follow-Ups

- 是否有企业在 AI coding pipeline 中强制 `spec -> test -> code -> verify -> slice` 的流水线？
- 有哪些工具或语言特性能把“不可接受的改动”编码成 hard constraint？
- 在实际团队中，谁负责定义测试即规格、谁负责定义不变量、谁负责定义爆炸半径边界？
- merge queue / protected branch / canary metrics 能否和 Topic 04 的 blast-radius scoring 合并成同一套 release-risk gate？

## Current Gaps

- 类型系统与 formal specification generation 的研究证据已经补到第一轮，但 enterprise practice evidence 仍然薄。
- 小批量切片与 release governance 的通用机制证据已经补强，但 AI-specific 端到端案例仍薄。
- 需要更明确的反例：哪些团队在 AI-assisted coding 后没有转向更强测试纪律？
