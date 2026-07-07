# Raw Notes: AI Engineer World's Fair Fable 5 Talk

来源线索：

- 本地整理来源：`ai_sdlc_frontier/raw_Anthropic_Thariq Shihipar/new_talk.md`
- 相关主题：Thariq 在 AI Engineer World's Fair 上围绕 Fable 5 的演讲

## 这场演讲补充了什么

如果说 `A Field Guide to Fable` 主要是在讲“怎么找到 unknowns”，这场演讲补的是更上层的方法论语境：为什么强模型时代的最佳实践会反过来，以及为什么很多旧经验正在失效。

## 主题 1：Unhobbling Claude

Thariq 认为，模型能力并不是一次性被完整设计出来的，而是在使用过程中逐步被释放出来的。

他给的代表例子是：

- 聊天模型本身未必能直接回答某类枚举题
- 但一旦给它代码执行工具，它会立刻写脚本，把问题转成可计算流程

Anthropic 内部把这类现象称为：

> capability overhang

也就是模型很多能力其实已经存在，只是接口、工具和用法还没有把它们释放出来。

## 主题 2：减少系统提示词，增加上下文

这场演讲里最关键的一个实践判断是：

> Claude Code 最近一个关键变化是砍掉了 80% 的系统提示词。

Thariq 的逻辑是：

- 早期模型需要大量示例和强约束
- 但 Fable 这个级别的模型，过多示例反而会限制它
- 新做法不再是拼命指定动作，而是提供充分上下文，让模型自己展开

可复用的总结句是：

> 多给上下文，少给约束；告诉它情况，不告诉它不许做什么。

## 主题 3：Unknowns 仍然是核心

演讲再次强调，Fable 5 的活动范围太大了，如果你不提前搞清楚未知项，它就会在你没想到的地方替你做决定。

Thariq 在演讲中继续推荐这些动作：

- blindspot pass
- 4 个方向的快速原型
- 让模型采访你
- 给它真实参考代码
- 在执行中记录 decision / deviation
- 在结束后反过来测验自己

## 主题 4：Be Unreasonable

演讲后半段最值得保留的，不是情绪描述，而是这句态度建议：

> be unreasonable

这里的意思不是鲁莽，而是：

- 不要太快接受旧时代“好、快、省三选二”的默认边界
- 先让更强的模型和工具把边界往外推
- 看现实是否真的逼你回到旧取舍

他提到，自己演讲前一天花了 4 个小时就用 Fable 做完了这场演讲的全部 PPT。

## 为什么这场演讲值得放进目录

- 它不是和长文重复，而是给长文补了“为什么现在该改方法”的解释层。
- 它把 `unknowns`、`capability overhang`、`减少系统提示词`、`more context less constraints` 串成了一条完整链路。
- 对 Thariq 这个人物来说，这场演讲说明他不是只发了一篇帖子，而是在 2026 年持续围绕 Fable 5 反复表达同一套方法论。
