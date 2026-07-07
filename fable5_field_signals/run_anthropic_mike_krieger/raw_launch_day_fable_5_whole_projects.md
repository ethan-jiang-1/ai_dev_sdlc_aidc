# Raw Notes: Mike Krieger on Handing Whole Projects to Fable 5

来源线索：

- Digg 聚合页：`https://digg.com/ai/g7bqoiyn#story-ai-responses-heading`
- Every 文章：`https://every.to/context-window/how-to-get-the-most-out-of-fable-5`
- 原始 X 帖子线索：`@mikeyk`，2026-06-09

## 这份材料补的是什么

`run_anthropic_mike_krieger/` 原来主要依赖 Every 的完整 transcript。

这份 raw 补的是 Mike 在 Fable 5 发布当天和 Every 后续整理里最浓缩、最适合快速理解的几个判断：

- Fable 为什么是他第一次敢整包委托 whole projects 的模型
- 他为什么会把复杂任务交给模型过夜推进
- 他如何理解“模型持有整个项目”的含义

## 发布日原话

> Claude Fable 5 is out today. The first Mythos-class model everyone can use & the first model I hand off whole projects to.

这句很重要，因为 Mike 把 Fable 的分界线划得非常清楚：

- 不是“更好的代码模型”
- 而是“第一个我敢整包委托 whole projects 的模型”

这实际上是在描述信任阈值的跨越。

> This weekend I built a self-maintaining, proactive media tracker for myself, over 2 days with Fable taking large chunks at a time.

这句补了一个具体样本：

- 不是玩具 demo
- 而是一个自己实际会用的内部工具
- 而且是让 Fable 分时段接管大块工作，而不是自己逐步盯着做

## Every 后续整理里对这条线的解释

Every 在 `How to Get the Most Out of Fable 5` 里，把 Mike 的访谈浓缩成几条很关键的框架：

### 1. More work is happening overnight

- Fable 5 是第一个“你可以把复杂任务交给它，走开，然后相信早上会完成”的模型
- 当它遇到障碍，比如远程服务挂掉、工具失灵，它会写绕过方案然后继续推进

这正好解释了为什么 Mike 会把“whole projects”这件事说得这么重。

### 2. The gap between what's in your head and what exists in the world is closing

- Mike 认为，这类模型让脑子里的想法和现实里已经做出来的东西之间的距离急剧缩短
- 这不只是工程师生产力问题，也是非工程角色能否直接把想法做出来的问题

### 3. Software engineering is dead. Long live software engineering

- Every 的总结指出，工程师花更少时间写代码
- 更多时间用来设方向、review agent 结果、处理生产环境中的判断题

这和 Mike 在 transcript 里反复强调的 `verification` 是一致的。

### 4. All eyes are on verification

- 当模型能接更多任务时，真正上升的门槛就变成了验证
- Mike 的做法包括：
  - regression tests
  - visual checks
  - 给模型看视频而不只是截图
  - mock backends
  - 让模型自己补 PR 和后续修正

## 为什么这份 raw 值得保留

- 这份材料把 Mike 的 Fable 5 观点从长访谈里抽成了一组更适合快速浏览的核心判断。
- 它尤其适合和 Boris 的 launch day 材料并读：
  - Boris 更强调模型行为学变化
  - Mike 更强调委托阈值、工作节奏和组织角色变化

## 对这个人物目录的意义

- 有了这份补充后，`run_anthropic_mike_krieger/` 不再只剩一个 transcript。
- 现在它至少同时覆盖了：
  - 长访谈里的完整工作流
  - 发布日的高度浓缩判断
  - Every 后续文章里的结构化总结
