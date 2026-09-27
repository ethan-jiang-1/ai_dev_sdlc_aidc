# Evidence 2026-09-27 · A4 · loop 提出者本人怎么写完成条件

- 观测日期：2026-09-27
- 本档案回答：退回提出 loop engineering 的人，看他们自己怎么写 goal / eval。本轮打开的是吴恩达的信，以及 Boris Cherny 自己的帖。Karpathy 另档，见 A10
- 不回答：循环怎么调度。六月那场「我不再提示、我写循环」的访谈句，本轮仍没有逐字稿

## Source 1 · Andrew Ng《Three Key Loops for Building Great Software》

- URL：https://www.deeplearning.ai/the-batch/three-key-loops-for-building-great-software
- 发布日期：页上为 2026-06-26。二手有写成 6 月 30 日的，以本页为准
- 作者：Andrew Ng。访问/观测日期：2026-09-27【主验】
- 原文摘录：
  > “Given a product specification and optionally a set of evals (that is, a dataset against which to measure performance), we can have an AI agent write code, test its work, and keep iterating until the code is bug-free and meets its specification.”
  > “If you find that the system repeatedly runs into certain problems, building a set of evals for the agent becomes useful.”
  > “Many people describe this human contribution as ‘taste,’ but I prefer to think of it as humans having a context advantage”
- 该摘录支持的最小主张：内环的完成条件是「规格 + 可选的 eval 数据集」，停在代码无 bug 且符合规格。eval 在他这里是一份用来量表现的数据集，而且是同一类问题反复出现之后才值得建，不是开工前写死的一句。外两环（开发者看产品、朋友 / alpha / A/B）由人注入模型还没有的上下文。他显式不用 taste 这个词。
- 不支持什么：信里没有独立于干活模型的裁判，也没有把「怎样才算达成」写成可核的终态句。打字练习应用的例子是 agent 自己开浏览器看，「大约一小时」是他的一次经历，不是效果实验。

## Source 2 · Boris Cherny，2026-01-02 帖（窗边）

- URL：https://threadreaderapp.com/thread/2007179832300581177.html （原帖 https://x.com/bcherny/status/2007179832300581177 ，X 页未打开；Thread Reader 标 Jan 2，与 snowflake 解码的 2026-01-02 一致）
- 作者：Boris Cherny。访问/观测日期：2026-09-27【主验，经 Thread Reader】
- 原文摘录：
  > “give Claude a way to verify its work. If Claude has that feedback loop, it will 2-3x the quality of the final result.”
  > “It opens a browser, tests the UI, and iterates until the code works and the UX feels good.”
  > “verify-app has detailed instructions for testing Claude Code end to end”
- 长任务的停法，同帖第 12 条：做完后用后台 agent 核对、用 Stop hook 做确定性核对，或用 ralph-wiggum。三条里有一条把核对交给另一只 agent，另两条没有写裁判是否换模型。
- 该摘录支持的最小主张：他的完成条件是给干活的 Claude 一条能自己核对的通道（bash、测试、浏览器、模拟器）。停的句子里同时有「代码能工作」和「UX feels good」。后者不是硬规则。2–3 倍是他的判断，没有对照。
- 不支持什么：这不是 6 月以后的新说法。不能把它读成 Claude Code `/goal` 文档里的另一只模型三值判定。那是产品文档，见 A / A2，不是这篇帖。

## Source 3 · Boris Cherny，2026-07-17 回复（全文）

- URL：https://x.com/bcherny/status/2077929390806073807
- 发布日期：2026-07-17 01:32 UTC。回复他自己稍早的一条（https://x.com/bcherny/status/2077929386146169269）。那条把步骤表挂在 `https://claude.ai/code/artifact/bfdfaef9-bc62-4dfe-ba9e-c58a26c9accf`。构件页这次没打开
- 访问/观测日期：2026-09-27，经 fxtwitter API【主验】
- 原文摘录：
  > “In practice that means giving Claude ways to verify its own work end to end. It means enabling auto mode for permissions, defaulting on automated code review and security review, and using interfaces that let you manage multiple agents at once”
  > “To get to higher levels it means /loop, /batch, dynamic workflows, and worktree isolation for subagents.”
- 该摘录支持的最小主张：窗内全文仍是让干活的 Claude 自己从头核到尾，并默认打开自动代码审和安全审。`/loop` 放在更高一档，不是这句回复里的完成条件。没有写裁判是否换一只模型。
- 不支持什么：步骤表的构件页没有读到，不能用二手转述把每一档写成他的原句。6 月访谈里「我的工作是写 loops」仍没有逐字稿。

## 同层还没打开的人

Ng 的信点名的另一个人是 Peter Steinberger。原帖已打开，见 [`evidence-2026-09-27-a9-x-goal.md`](evidence-2026-09-27-a9-x-goal.md)。2026-06-07 那条没有完成条件；2026-06-12 他给了一句 `/goal`。Karpathy 的两帖已打开，见 [`evidence-2026-09-27-a10-karpathy.md`](evidence-2026-09-27-a10-karpathy.md)，都在窗边。

## 判读

- 观察：提出这个词的人，写完成条件的方式比后来的产品文档松。Ng 用规格加可选数据集，eval 是反复失败之后才建的。Cherny 用一条核对通道，停的时候允许「体验好不好」。7 月全文加上了自动代码审和安全审，仍是干活的 Claude 自己核。两人都没有把否决权写成干活模型之外的一只裁判。
- 推断：六月的热度句回答的是「人还要不要逐轮提示」，不是「怎样才算达成」。后一个问题是产品文档和 Osmani、Runkle 补上的，不是词源句里就有的。
- 与 A / A2 的关系：Anthropic 文档里的独立裁判仍只算机构机制。Cherny 的帖不给那套机制加一票。

## 负结论与限制

- Cherny 2026-04-16 的 Thread Reader 页正文为空，不引。
- Steinberger 原帖已打开，见 [`evidence-2026-09-27-a9-x-goal.md`](evidence-2026-09-27-a9-x-goal.md)。
- Ng 信中的打字应用是一次叙述，不是对照实验。
