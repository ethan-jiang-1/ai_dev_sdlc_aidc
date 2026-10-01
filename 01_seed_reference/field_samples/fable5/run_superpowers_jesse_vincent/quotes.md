# Jesse Vincent：洞察摘录

## 关键言辞

> “Specs are the thing that matters now. The code does not matter anymore.”

- Jesse 的极端之处就在这里。
- 他不是说代码不重要，而是说在 agent 时代，代码的生产变得廉价，真正稀缺的是高质量 spec。

> “The only thing worse than a failing test is a reduction in test coverage.”

- 这是一个非常典型的 Jesse 式规则：把含糊道德劝告变成可测量约束。
- 它直接针对 agent 会“投机取巧”这个问题。

> “Superpowers 6 is much, much faster and burns many fewer tokens to get the same high-quality outcomes.”

- 这句说明 Jesse 到了 2026 年中，已经不只是设计方法，而是在系统优化 agent 工作流的成本结构。

> “As I was going to bed... run at least 25 experiments.”

- 这句很能体现 Jesse 和 Fable 的合作方式。
- 不是让模型做一件事，而是让模型搭研究循环、记假设、跑实验。

## 工作流层面的硬货

- brainstorming 先于 coding
- spec 是人类 review 的主对象
- fresh reviewer 要和 implementer 解耦
- test writer、implementer、reviewer 最好分开
- end-to-end 证据比单测通过更有说服力

## 来自卡尔整理的 Fable 5 实验结论

> 限制思考字数、让便宜模型先写计划、给测试预算设上限，这些看似省钱的做法，实际都会破坏 Fable 的任务结构。

- 这是 Jesse 非常值钱的一点：他愿意认真记录失败路线。
- 失败记录会变成以后最值钱的复用资产。

> `/goal` 最佳结构是目标、指标、边界。

- 这和 Jesse 的整体方法是同一脉：把模型当研究员或工程团队管理，而不是当 autocomplete。
