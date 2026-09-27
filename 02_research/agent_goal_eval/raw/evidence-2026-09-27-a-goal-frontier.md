# Evidence 2026-09-27 · A · goal 如何构造，loop 才能跑

- 观测日期：2026-09-27
- 时间窗：主证据 2026-06 及以后；2026-05 的产品机制标「窗边」（用户同日定，见 [`../README.md`](../README.md) §3）
- 证据强度：本档案各条分开标。官方文档与作者原文为【主验】；检索命中但未打开全文的不写入引句
- 本档案回答：Q1。前沿的人、社区、公司在这个窗口里把 goal 写成什么，循环才有可对照的完成条件
- 不回答：Q2 的调优数字、Q3 的完整判读。Hamel 2026-06-29 与 Yeret 文只登记，判读留给后路

## Source 1 · Anthropic · Claude Code `/goal` 文档

- URL：https://code.claude.com/docs/en/goal
- 发布日期：功能在 Week 20（2026-05-11–15，v2.1.139）发布，见 https://code.claude.com/docs/en/whats-new/2026-w20 。**窗边**。本页是活文档，观测日仍在更新（页内写到 v2.1.269 的重试/暂停）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：官方文档（机构）
- 原文摘录：
  > “Use a goal for substantial work with a verifiable end state”
  > “The evaluator judges your condition against what Claude has surfaced in the conversation. It doesn’t run commands or read files independently, so write the condition as something Claude’s own output can demonstrate.”
  > “A condition that holds up across many turns usually has: One measurable end state… A stated check… Constraints that matter”
  > “`/goal` adds a separate evaluator that checks your condition after every turn, so completion is decided by a fresh model rather than the one doing the work.”
  > “The model returns one of three verdicts… Not yet met… Met… Impossible”
- 该摘录支持的最小主张：官方把能跑的 goal 写成可核的终态，加上 Claude 自己的输出里能看见的检查，加上不能被顺手改掉的约束。完成与否由另一只小模型看对话，不由干活的那只模型宣布。
- 不支持什么：不证明这样做以后产物更好。不证明业务结果被达成。裁判不自己跑命令，所以「对话里没印出来的事实」它看不见。

## Source 2 · Addy Osmani《Practical Loop Engineering》

- URL：https://addyosmani.com/blog/practical-loop-engineering
- 发布日期：2026-08-14（页面标注 August 14, 2026）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：作者原文
- 原文摘录：
  > “The way that I use goal is I use it for building any specific piece of work until it’s provably done.”
  > “The evaluator sitting behind goal is not that checker, by the way. It doesn’t look at the content to see if it’s good or bad in any way, shape, or form. All it does is examine the conversation transcript to see if the hard rules you specified have been met.”
  > “if you don’t have a clear idea of what the end-state/done/good means for your completion, it may not be the right pattern for your work. For example, a vague goal would be “keep going until this UI design is good”.”
  > “you need to sometimes check yourself, that you are not delegating the taste and the judgment to your agent.”
- 该摘录支持的最小主张：Osmani 的可跑写法是「可证明做完」的硬规则，并写明 `/goal` 后面的裁判不判断内容好不好。含糊的「做好看」他明确排除。品味仍留在人这边。他同时转述了 Claude Code 团队对 goal-based loop 的定义（确定性标准如测试数、Lighthouse 分数）。
- 不支持什么：文中 Lighthouse、issue 清理是他的自述实验（“Sometimes that works well, sometimes it doesn’t”），不是对照实验。他转述的团队博文，本次没有打开官方 URL，不另计 Anthropic 博客一票。

## Source 3 · OpenAI Cookbook《Using Goals in Codex》

- URL：https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex
- 发布日期：2026-05-09（页面标注 May 9, 2026）。作者 Raj Pathak、Stefano Fabbri（OpenAI）。**窗边**
- 访问/观测日期：2026-09-27【主验】
- 来源类型：官方 cookbook（机构）
- 原文摘录：
  > “A Goal is not background autonomy without boundaries. It is a scoped, user-controlled completion contract.”
  > “The strongest Goals usually define six things: Outcome… Verification surface… Constraints… Boundaries… Iteration policy… Blocked stop condition”
  > “A Goal should not be marked complete because the model believes it is probably done. It should be complete only after the objective is checked against the relevant files, tests, logs, benchmark output, generated artifacts, or other concrete evidence.”
  > “Do not use a Goal when the finish line is vague. Make this better gives Codex no reliable completion condition.”
- 该摘录支持的最小主张：OpenAI 把能跑的 goal 写成一份合同：终态、用什么证据核、不能破坏什么、碰哪些范围、每轮怎么选下一步、卡住时停下来报告什么。完成要对照具体证据，不接受模型觉得「大概好了」。
- 不支持什么：这是写法指南，不是效果测量。页内没有写一只独立于干活模型的裁判；「Codex can inspect the current evidence and decide」没有说明决定者是不是干活的同一只模型。不能用 Claude 的三值裁判去填这个空。

## Source 4 · Cursor changelog · `/goal`

- URL：https://cursor.com/changelog/08-19-26
- 发布日期：2026-08-19（changelog 路径 `08-19-26`）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：官方 changelog（机构）
- 原文摘录：
  > “Use `/goal` to give the agent a long-lived objective to work towards until it’s fully complete.”
  > “Try `/goal fix all flaky tests and make CI green`”
- 该摘录支持的最小主张：Cursor 在 2026-08 提供了同名命令，例子是「修掉不稳定测试并让 CI 变绿」。
- 不支持什么：这条没有写裁判是谁、看什么、何时判不可能。不能把它写成 Claude `/goal` 或 Codex Goal 的同一种机制。

## Source 5 · 社区 · Claude Code issue #93744

- URL：https://github.com/anthropics/claude-code/issues/93744
- 发布日期：2026-09-11（cws5026 打开；正文写观测 2026-09-12）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：社区第一人称（GitHub issue，不是团体声明）
- 原文摘录：
  > “The Stop-condition evaluator appears not to read it, so it repeatedly fires, cannot confirm the goal, and eventually reports its own condition as unachievable — while the goal text was present in the transcript the whole time.”
  > “Confirming whether the evaluator truly cannot see [the command metadata] requires internal knowledge — that part is inferred from the observed behavior, not verified from source.”
- 该摘录支持的最小主张：有一条无人值守的过夜会话里，`/goal` 的长指令被作者认为裁判没读到，于是反复触发，最后被判不可能，且后几次没有新工作。作者自己把「裁判看不见」标成推断。
- 不支持什么：不是 Anthropic 的确认，也不是普遍故障率。这条 goal 本身是「你们自己决定方向，尽量把项目做完」，不是 Source 1 要求的可核终态。

## 登记 · 不在本档案回答 Q1

### Yuval Yeret《Goal-Based Loop Engineering》

- URL：https://yuvalyeret.com/blog/ai-agent-completion-goals-aim-at-outcomes
- 发布日期：**本次摘录未见页面日期**。不能确认落在 2026-06 以后
- 访问/观测日期：2026-09-27【主验正文，日期未核】
- 摘录只留一句，供 Q3 使用：
  > “When you set a completion goal around a technical criterion, the agent has clear stopping conditions it can evaluate autonomously and reliably. When you set one around an outcome, you immediately run into the question: how would the agent observe whether that condition holds?”
- 不据此入册，也不据此写 Q1 结论。

### Hamel Husain《“It’s Hard to Eval” Is a Product Smell》

- URL：https://hamel.dev/blog/posts/eval-smell
- 发布日期：2026-06-29
- 访问/观测日期：2026-09-27【主验开头】
- 摘录：
  > “The most common objection I hear to evals is “our product is hard to eval”. This objection is a product smell. … designing your product for ease of verification should come before building evals.”
- 这是 Q3 的材料。本档案不把它写成 goal 构造结论。

## 判读

- 观察：窗内和窗边的官方材料把「能让循环停下来的 goal」写成可核终态加可见证据。Claude 明确裁判是另一只模型，而且只看对话里已经出现的内容。Osmani 把同一限制说成：裁判不判断好坏，只核硬规则。Codex 的六件套更长，但没有写独立裁判。Cursor 只有同名命令和一句例子。
- 推断：目前公开的、能让 loop 跑起来的写法，停在「输出或检查能否在环境里被看见」，还不是「业务结果是否发生」。这是材料的边界，不是已经证明业务 goal 不可写。
- 与现有材料关系：loop 主题的 [`evidence-b`](../../ai_loop_engineering/raw/evidence-2026-09-26-b-stop-and-scheduling.md) 已有 Claude `/goal` 的更早摘录。本档案按 2026-09-27 的活文档重取了构造条件的句子，不搬对方全文。

## 负结论与限制

- 搜到但不当一手：AI Builder Club、Tosea、explainx、Firecrawl、Prospere、APIDog、Data Science Dojo、Kingy、Locsic 等 2026 综述。它们转述 `/goal`，不增加独立来源。
- 官方博文已在 [`evidence-2026-09-27-a2-goal-more.md`](evidence-2026-09-27-a2-goal-more.md) 主验：页面日期是 **2026-06-30**。早先二手里的 2026-07-07 不成立。Osmani 的转述不再代替原文，但也不另计一家机构。
- 没有拿到一个社区**团体**（工作组、社区章程、共同实践文档）在 2026-06 后写下 goal 构造。#93744 是个人复现。Cursor 论坛里 “Grind 改称 Goal” 的帖子未全文提取，不入引句。
- LoopsBench（arxiv 2608.00267）只在检索摘要里出现，未读全文。
- 不能推出：三家 `/goal` 是同一机制；可核终态已经等于好的 goal；独立裁判会提高结果质量。
