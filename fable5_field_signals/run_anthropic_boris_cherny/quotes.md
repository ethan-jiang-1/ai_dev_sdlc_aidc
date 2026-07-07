# Boris Cherny：洞察摘录

## 关键言辞

> “The biggest step up I've felt in our models since Opus 4.5.”

- 这句话的重要性在于，它不是泛泛说“更强了”，而是把 Fable 放到 Anthropic 自己内部的代际坐标上。

> “Claude has stepped up from being a coding agent to a thought and design partner.”

- 这里的关键词不是 `coding`，而是 `design partner`。
- 这意味着模型开始介入方案、路径、取舍，而不是只接收任务单。

> “It has judgment, taste, and dimensionality in a way that previous models didn't.”

- `judgment`：知道该怎么判断和取舍。
- `taste`：会偏向更优雅、成体系的方案。
- `dimensionality`：不是一维优化，而是同时考虑多条约束。

> “It is the first model I have used that was so methodical and precise, taking measurements and adding logs then verifying that it truly fixed the issue before declaring victory.”

- 这句几乎可以当作 Fable 工程行为学的定义。
- 重点不是它会修 bug，而是它知道“宣布修好”之前应该经历哪些验证环节。

> “There's nothing in claude code's prompting telling the model to do that, it's just part of its personality.”

- 这是 Boris 最值钱的一句。
- 它说明 Fable 最强的一部分不是 prompt engineering 的产物，而是涌现出来的工作习惯。

## 辅助背景

> “Maybe you don't actually need an IDE.”

- 这是 Boris 在回忆 Claude Code 起源时的原话之一。
- 它解释了为什么 Claude Code 的设计从一开始就更像“让模型直接进入工程环境”，而不是把模型关在 IDE 边栏里。

> “The model just wants to use tools.”

- 这句来自他描述早期给模型 bash 的体验。
- 和 Fable 的行为方式连起来看，会发现 Anthropic 的产品方向一直是：少做花哨 wrapper，多给真实环境。
