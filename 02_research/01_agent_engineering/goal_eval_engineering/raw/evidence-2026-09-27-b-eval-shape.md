# Evidence 2026-09-27 · B · eval 写成可打分的形状

- 观测日期：2026-09-27
- 本档案回答：Q2 的构造。开放任务怎样写成环境里能打分的终态，以及「实习生测试 / 80% 同意」的原文到底是哪一句
- 不回答：打出数之后改 prompt 的那一步是否让产品变好。判读不在本档

## Source 1 · Eugene Yan《Patterns for Building Cybersecurity Evals》

- URL：https://eugeneyan.com/writing/cybersecurity-evals/
- 发布日期：写作目录标 **2026-06-21**。文末引用只写 Jun 2026。页面没有 `datePublished`。主证据窗内
- 访问/观测日期：2026-09-27【主验】
- 来源类型：作者本人长文。他在归纳别人的基准，不是在汇报自己产品循环的调优
- 原文摘录：
  > “A sandboxed target”
  > “Inputs that influence task difficulty”
  > “Tools”
  > “A grader: Where agents can submit their work—such as a working exploit or a captured flag—for immediate feedback. These are typically deterministic.”
  > “Because exploitation is open-ended, most benchmarks evaluate outcomes instead of the method used.”
  > “Thus, to get a more granular picture, we can award partial credit via subtasks that track progress along the attack chain”
  > “we can also run automated transcript audits to confirm that the agent actually exploited the vulnerability instead of reward hacking.”
- 做法：先放一个沙箱里的目标；用给多少提示控制难度（只有代码，或加上漏洞说明、崩溃栈、补丁）；给工具；裁判看环境里的结果，不看路径。结果太粗时，沿攻击链拆成可单独计分的子任务：找到漏洞、做出能触发的证明、在目标上执行、达到攻击者的目标。另外审 transcript，防止抄近路拿分。
- 该摘录支持的最小主张：2026-06 有一套把开放任务收成可打分 eval 的四件套。成功句写在环境状态上（sanitizer 崩溃、旗标、余额增加）。部分分是进度格，不是对路径打分。
- 不支持什么：文中的成功率是所引基准自己的数字，不是这次调优改好了哪一条条件。四件套不证明产品循环因此停得更准。与 A6、FAQ 里已有的部分分并列，不并成一步。

## 负结论 · 实习生测试与 80% 同意

聚合博客把「实习生测试」写成：把 rubric 交给不熟的人，10 条 trace 上过/不过一致达到 80% 才许自动化；另有一套「50 条、同意率低于 80% 就改 rubric、超过 85% 才信裁判」。

打开被点名的原文之后，那句话不是这个意思。

- URL：https://applied-llms.org/  §1.4.3
- 发布日期：页内引用 **2024-06-08**。作者 Eugene Yan、Bryan Bischof、Charles Frye、Hamel Husain、Jason Liu、Shreya Shankar。窗外。本主题不把 2024 的步骤收成窗内做法
- 访问/观测日期：2026-09-27【主验这一节】
- 原文摘录：
  > “If you took the exact input to the language model, including the context, and gave it to an average college student in the relevant major as a task, could they succeed? How long would it take?”
- 该节没有 “80%”，也没有 “agreement”。测的是交给模型的那道任务，实习生能不能做、要做多久。做不到就补上下文或把任务拆小；做得很快却仍错，才去看数据里的失败模式。
- 聚合页 https://www.kunalganglani.com/blog/evaluate-ai-agents-production 在检索摘录里写了 80% / 85% 的校准循环，并把它算到 Applied LLMs 头上。那套数字不在 §1.4.3。不入做法。
- Hamel《Using LLM-as-a-Judge》https://hamel.dev/blog/posts/llm-judge 页首两行日期是 2024-10-29 与 2026-09-01。没有 diff，不能把 Critique Shadowing 整套算成 2026-09 新写的。本档不摘那一套。

## 判读

- 观察：B 路此前没有自己的档案。这页补上的是「开放任务怎么变成一个数」：环境状态、难度由提示多少决定、部分分沿过程拆、另审有没有抄近路。实习生测试的原文则在回答另一件事：任务本身是否已经具体到人能做。
- 推断：量化之后「改哪一句、改哪一个数」这半边，这轮仍然没有新的窗内节拍。Yan 停在评测怎么搭。2024 的法官迭代指南因为对不上更新日期，先不搬进来。
- 与现有材料关系：A6 的「判环境里的结果、不判路径」和 FAQ 的部分分仍留在原档。这里只加四件套和攻击链上的四格。

## 负结论与限制

- Steinberger 原帖已打开，完成条件在 [`evidence-2026-09-27-a9-x-goal.md`](evidence-2026-09-27-a9-x-goal.md)，不在本档。
- r/AIQuality 那篇空抽取没有 URL 留在旧档里，这轮没有重试。
- 不能推出：安全基准的四件套就是产品 goal 的写法；部分分已经证明调优有效。
