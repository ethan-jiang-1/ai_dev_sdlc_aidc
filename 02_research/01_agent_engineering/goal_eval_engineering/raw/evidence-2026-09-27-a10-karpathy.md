# Evidence 2026-09-27 · A10 · Karpathy 自己写的成功标准

- 观测日期：2026-09-27
- 本档案回答：A4 写「Karpathy 未开」。下面是他本人两帖里和完成条件有关的句子
- 不回答：6 月以后他有没有另写一套。这轮按他的账号打开的是这两条，都在窗边

## Source 1 · 2026-01-26 长帖（窗边）

- URL：https://x.com/karpathy/status/2015883857489522876
- 发布日期：2026-01-26 20:25 UTC。窗边
- 访问/观测日期：2026-09-27，经 fxtwitter API【主验】
- 原文摘录：
  > “Don't tell it what to do, give it success criteria and watch it go.”
  > “Get it to write tests first and then pass them.”
  > “Put it in the loop with a browser MCP. Write the naive algorithm that is very likely correct first, then ask it to optimize it while preserving correctness.”
- 该摘录支持的最小主张：他把杠杆写成可验证的成功标准，不是逐步指令。例子是先写测试再让它通过，用浏览器看结果，先写很可能正确的朴素算法再优化且不许把正确性改掉。
- 不支持什么：没有独立于干活模型的裁判，也没有一个产品上的通过率。同一帖里他写自己仍在旁边的 IDE 里看着，模型会带着错误假设往下跑。这不是「写了标准就可以不看」。

## Source 2 · 2026-03-06 回复（窗边）

- URL：https://x.com/karpathy/status/2029957088022254014
- 发布日期：2026-03-06 16:27 UTC。回复别人。窗边
- 访问/观测日期：2026-09-27，经 fxtwitter API【主验】
- 原文摘录：
  > “the success criteria is quite simple: reach the lowest possible loss … but don't regress running time, keep memory in check, and keep a sense of simplicity/aesthetics”
- 做法：训练 GPT 的成功标准是损失尽量低，同时不许跑得更慢、不许内存变差、不许为了一点收益把代码写肿。他交给模型的说明大约 120 行 markdown。
- 该摘录支持的最小主张：标准客观、而且能写成「要优化的数 + 不许回退的几项」时，他把整段试验交给模型。
- 不支持什么：他说这更接近超参搜索，不是模型自己想出新研究。没有对照实验。简洁仍是他的判断，不是硬规则。

## 判读

- 观察：两帖都在窗边。完成条件是「先有可核对的标准，再让它循环」。1 月的例子是测试和浏览器。3 月的例子是损失，外加耗时、内存、简洁三条不许回退。
- 推断：后人口中的「Karpathy 四条 CLAUDE.md」是别人从 1 月这帖收的。本档只认他写在帖里的句子，不认衍生仓库里的 65% 到 94% 这类数。
- 与 A4 的关系：A4 此前写未开。以本档为准。他和 Cherny、Ng 一样，没有把否决权写成另一只模型。

## 负结论与限制

- 2026-06 及以后，这轮没有打开他另一条自己写下完成条件的原帖。
- Satya 仍只有别人的点名和主题演讲二手摘要（hill climb、用自己的 eval）。没有他写下完成条件的原文，不入。
- 不能推出：先写测试就等于 `/goal` 文档里的三值判定；损失最低可以套到业务结果上。
