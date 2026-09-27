# Evidence 2026-09-27 · A2 · goal 构造补源

- 观测日期：2026-09-27
- 时间窗：2026-06-16 → 2026-07-22
- 本档案回答：A 路缺口。官方 loops 博文的日期，以及窗内另一家对「检查怎么写」的说法
- 不重复：[`evidence-2026-09-27-a-goal-frontier.md`](evidence-2026-09-27-a-goal-frontier.md) 已有的 Claude 文档、Osmani、Codex、Cursor、issue

## Source 1 · Anthropic 博客《Loop engineering: Getting started with loops》

- URL：https://claude.com/blog/getting-started-with-loops
- 发布日期：**2026-06-30**（页面标注 June 30, 2026）。作者 Delba de Oliveira、Michael Segner（Claude Code 团队）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：官方博客（机构，与 Claude `/goal` 文档同一机构，不另计一票）
- 原文摘录：
  > “On the Claude Code team, we define loops as agents repeating cycles of work until a stop condition is met.”
  > “Stop criteria: Goal achieved OR maximum number of turns reached.”
  > “Best used for: Tasks that have verifiable exit criteria.”
  > “When you define the success criteria, Claude doesn’t have to make a determination on what is “good enough” and end the loop early. Each time Claude tries to stop, an evaluator model checks your condition and sends it back to work until the goal is met or a number of turns you define is reached. This is why deterministic criteria, such as number of tests passed or clearing a certain score threshold, are so effective.”
  > “Goal-based | You hand off | The stop condition | You know what done looks like”
- 该摘录支持的最小主张：团队自己把 `/goal` 的适用面写成「知道怎样算做完、退出条件可核」。确定性标准被写成有效的原因：免得干活的模型自己决定「够好了」就停。日期以本页为准，不是 7 月 7 日。
- 不支持什么：不证明分数阈值或测试数在他们以外的任务上同样有效。文中 proactive 例子把 `/goal` 写成「本轮找到的每条反馈都分诊、处理、回复」，这句比 Lighthouse 例子宽，页面没有说明裁判如何核「回复过了」。

## Source 2 · 同团队《Building verification loops in Claude Code with skills》

- URL：https://claude.com/blog/building-verification-loops-in-claude-code-with-skills
- 发布日期：2026-07-22。作者 Delba de Oliveira
- 访问/观测日期：2026-09-27【主验】
- 来源类型：官方博客（仍是 Anthropic 一票）
- 原文摘录：
  > “If you're struggling to articulate the verification check itself, ask Claude for best practices first and edit from there. Your version probably differs on a few specific points, and those differences are exactly what you want to capture.”
  > “The check doesn't have to be qualitative to belong here. "Reject any migration that drops a column without a backfill step" is a deterministic rule no generic linter will catch but a project-specific one will.”
  > “Rubrics in Claude Managed Agents (beta): A managed agentic service that allows you to verify outcomes against a rubric using a separate grader agent. Failures loop back for rework automatically.”
- 该摘录支持的最小主张：写不出检查时，官方建议先让模型起草再改，留下和通用做法不同的那几条。项目自己的确定性规则算检查。rubric 加独立 grader 被写成另一种内建循环，失败会退回去改。
- 不支持什么：没有写起草再改的成功率。Managed Agents 的 rubric 标成 beta，没有写出 rubric 的字段。

## Source 3 · Sydney Runkle / LangChain《The Art of Loop Engineering》

- URL：https://www.langchain.com/blog/the-art-of-loop-engineering
- 发布日期：2026-06-16（页面标注 June 16, 2026）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：公司工程博客、作者署名
- 原文摘录：
  > “The verification loop adds a grader: something that checks the agent's output against a rubric and, if it fails, sends the result back with feedback. Graders can either be deterministic or agentic (LLM as a judge is a classic example, here).”
  > “An automated grader can check whether links resolve; it takes a human to notice the framing is wrong for the audience.”
  > “Those traces contain high value signal regarding what's working and what isn't. The hill climbing loop runs an analysis agent over those traces and uses the findings to rewrite the harness with improved configuration. That can include prompt/tool tweaks or grader tweaks.”
- 该摘录支持的最小主张：LangChain 把「检查」写成对着 rubric 打分，不过就退回并附反馈。grader 可以是确定性的，也可以是模型。人被留在「受众是否接得住」这种判断上。trace 被写成以后改 grader 的材料。这是另一家，不是 Anthropic 的转述。
- 不支持什么：文档 agent 的例子（链接能打开、CI 过、diff 不越界）是他们的内部做法叙述，没有对照数据。hill-climbing 改 grader 只说明他们把调优设计成读 trace，不证明这样调了就更好。文中点名的 swyx《loopcraft》旧链 404。活链的公开段在 [`evidence-2026-09-27-a3-citation-map.md`](evidence-2026-09-27-a3-citation-map.md)，没有检查句子。

## 判读

- 观察：6 月 30 日的官方页和活文档说的是同一件事：goal 交给循环的是停止条件，而且最好是确定性的。7 月 22 日补了一句给写不出来的人：先起草再改。LangChain 用 rubric 这个词，并把「模型当分」和「人看受众」分开。
- 推断：窗内能对上的构造，仍是「看得见的检查」。独立来源现在是 Anthropic 文档+博客（一票）、Osmani、OpenAI（窗边）、LangChain。Cursor 仍不能算进这组。
- 与 A 档关系：只补 A 档写明未打开的博文，以及 A 档没有的 LangChain。不改 A 档已写的引句。

## 负结论与限制

- swyx 的 Loopcraft：Runkle 给出的旧链 404。活链的公开段见 [`evidence-2026-09-27-a3-citation-map.md`](evidence-2026-09-27-a3-citation-map.md)。付费墙从 Reddit 回顾起，墙后未读。
- 社区里在谈论的人不少，见 a3。还没有一份团体章程。通讯和会场发言算摸索中的谈论，不算已沉淀的做法。
- 不能推出：rubric、skill、`/goal` 三者可以互换；trace 改 grader 已经是可用的调优方法。
