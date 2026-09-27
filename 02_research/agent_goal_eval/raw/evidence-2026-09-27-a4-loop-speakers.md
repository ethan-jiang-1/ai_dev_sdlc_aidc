# Evidence 2026-09-27 · A4 · loop 提出者本人怎么写完成条件

- 观测日期：2026-09-27
- 本档案回答：退回提出 loop engineering 的人，看他们自己怎么写 goal / eval。本轮打开的是吴恩达的信，以及 Boris Cherny 自己的帖
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

## Source 3 · Boris Cherny，2026-07-17 帖的可见预览

- 同一次 Thread Reader 页的「More from @bcherny」列出 Jul 17 一帖，正文只展开了预览，点进全文未成功
- 预览中的原句：
  > “In practice that means giving Claude ways to verify its own work end to end.”
  > “To get to higher levels it means /loop, /batch, dynamic workflows, and worktree isolation for subagents.”
- 该摘录支持的最小主张：到了主证据窗，他仍把核对写成 Claude 核对自己的工作，并把 `/loop`、`/batch` 放在更高一档。预览里没有写出完成条件的句子，也没有写裁判是否换一只模型。
- 不支持什么：预览不是全文。6 月访谈里「我的工作是写 loops」仍没有逐字稿，不从这篇预览回填那句话。

## 同层还没打开的人

Ng 的信点名的另一个人是 Peter Steinberger。本轮没有打开他的原帖。检索到的转述都只复述「不要再提示，去设计替你提示的循环」，没有见到他写完成条件或裁判。不入册。Karpathy 本轮未开。

## 判读

- 观察：提出这个词的人，写完成条件的方式比后来的产品文档松。Ng 用规格加可选数据集，eval 是反复失败之后才建的。Cherny 用一条核对通道，停的时候允许「体验好不好」。两人都没有把否决权写成干活模型之外的一只裁判。
- 推断：六月的热度句回答的是「人还要不要逐轮提示」，不是「怎样才算达成」。后一个问题是产品文档和 Osmani、Runkle 补上的，不是词源句里就有的。
- 与 A / A2 的关系：Anthropic 文档里的独立裁判仍只算机构机制。Cherny 的帖不给那套机制加一票。

## 负结论与限制

- Cherny 2026-04-16 的 Thread Reader 页正文为空，不引。
- Steinberger 原帖未打开。
- Ng 信中的打字应用是一次叙述，不是对照实验。
