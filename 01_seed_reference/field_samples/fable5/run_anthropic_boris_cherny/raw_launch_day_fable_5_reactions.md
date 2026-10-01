# Raw Notes: Boris Cherny on Fable 5 Launch Day

来源线索：

- Digg 聚合页：`https://digg.com/ai/crrpnk9g`
- 原始 X 帖子线索：`@bcherny`，2026-06-09
- 相关二次聚合页：`https://digg.com/ai/g7bqoiyn#story-ai-responses-heading`

## 这份材料补的是什么

`run_anthropic_boris_cherny/` 原来已经有一篇 Every transcript，但那篇更偏 Claude Code 整体哲学。

这份材料补的是 Boris 在 `Fable 5` 发布当天最直接、最浓缩的一组判断，也就是：

- Fable 相比 Opus 4.5 到底新在哪
- 他为什么说它已经从 coding agent 变成了 thought and design partner
- 为什么他认为模型开始表现出 `judgment / taste / dimensionality`
- 为什么“self-verification”不是 prompt 设计的产物，而是模型行为本身的一部分

## 发布日核心原话

> Fable 5 is the biggest step up I've felt in our models since Opus 4.5 back in November.

这句最重要的作用，是把 Fable 放回 Anthropic 自己的内部代际经验里，而不是放在外部 benchmark 宣传里。

> After 4.5 came out I uninstalled my IDE when I realized that I'd been doing 100% of my coding in a terminal for a few weeks.

这句不是单纯在说“我不用 IDE 了”，而是在交代一个长期轨迹：

- Opus 4.5 已经让他的开发界面迁移到终端
- Fable 5 则进一步改变了“任务怎么被承担”

> With Fable, it's felt like Claude has stepped up from being a coding agent to a thought and design partner in building the product.

这是 Boris 对 Fable 5 最经典的一句定义。

重点不是 “coding” 能力提升，而是：

- Claude 开始参与产品构思
- 开始参与方案判断
- 不再只是执行层代理

> Fable has judgement, taste, and dimensionality in a way that previous models didn't, leading me to trust it more with the most complex work.

这句把他为什么更敢委托复杂任务说清楚了。

这里的三个关键词值得单独记：

- `judgment`：会做判断和取舍
- `taste`：会偏向更优雅、结构更好的方案
- `dimensionality`：能同时考虑多条约束，而不是一维优化

> I think the first time I had this realization was when I asked Fable to debug something. It is the first model I have used that was so methodical and precise, taking measurements and adding logs then verifying that it truly fixed the issue before declaring victory.

这段非常关键，因为它具体到可观察行为：

- 不是直接改代码
- 先测量
- 再加日志
- 再验证修复
- 最后才宣布完成

这几乎可以当成 Boris 眼里 Fable 工程行为学的定义。

> There's nothing in claude code's prompting telling the model to do that, it's just part of its personality. It really has this "big model smell" that I haven't felt before.

这句最值钱的地方在于：

- 它排除了“是不是 prompt 硬调出来的”这个解释
- 它把 Fable 的差异归因为模型级行为和性格
- `big model smell` 成了 Boris 用来指称这种新型行为气味的短语

## 同日补充原话

同一轮发布日聚合页里，还能看到 Boris 的另一句更产品化的表述：

> Fable is now available in Claude Code and Cowork.

> Fable is the best model I have used for coding, by a wide margin. It is a big step up, enabling less prompts and steers, more efficient token use, better code quality, better tool use, more intelligent self-verification, longer running sessions, and higher trust & autonomy.

这段把前面的感受进一步落成了操作层指标：

- 更少 prompts 和 steers
- 更高 token 效率
- 更好的代码质量
- 更好的工具使用
- 更智能的 self-verification
- 更长的连续会话
- 更高的 trust 和 autonomy

## 为什么这份 raw 值得保留

- 它补上了 Boris 在 2026 年后围绕 Fable 5 最直接的发布日判断。
- 它和 Every transcript 形成互补：
  - transcript 更像产品哲学与工作方式
  - 这份 raw 更像模型行为变化的原话证据
