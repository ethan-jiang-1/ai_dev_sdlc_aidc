# Evidence 2026-09-27 · A9 · X 上的 goal 原帖

- 观测日期：2026-09-27
- 本档案回答：有号召力的人在 X 上自己写下的完成条件。正文用 fxtwitter 取回，不是二手转述
- 不回答：这些帖有没有让循环的结果变好。调度、队列、授权不在这里展开

## Source 1 · Peter Steinberger 两条原帖

- URL：https://x.com/steipete/status/2063697162748260627
- 发布日期：2026-06-07 18:58 UTC（雪花 ID）
- 访问/观测日期：2026-09-27【主验】
- 原文摘录：
  > “Here’s your monthly reminder that you shouldn’t be prompting coding agents anymore.”
  > “You should be designing loops that prompt your agents.”
- 该摘录支持的最小主张：被传开的那条就是这两句。没有终态、没有裁判、没有失败时怎么办。
- 不支持什么：不能从这两句推出他已经会写完成条件。

同人下一条才有句子。

- URL：https://x.com/steipete/status/2065357277880877413
- 发布日期：2026-06-12 08:55 UTC。回复 Matthew Berman 2026-06-11 问「代币用不完，代码库上可以循环做什么」
- 原文摘录：
  > “/goal refactor until you are happy with the architecture. ensure you live test after each significant step and autoreview/commit. track progress in /tmp/refactor-{projectname}.md”
- 做法：停的句子是「架构让你满意」。每一步大改之后实机测，跑 autoreview，再提交。进度写在仓库外的一个 markdown 里。
- 该摘录支持的最小主张：他公开用过的 `/goal` 把品味留在停的句子里，把可重复的动作放在实机测、自动审和进度文件上。
- 不支持什么：「让你满意」不是硬规则。autoreview 的通过线这轮没有打开：`skills/autoreview/SKILL.md` 返回 404。2026-06-11 另一帖（https://x.com/steipete/status/2064998499780084154）链到的 orchestrator / triage 技能写的是队列和谁可以对外行动，不是一句完成条件，不摘进这里。

## Source 2 · Dominik Kundel《A guide to /goal》

- URL：https://x.com/dkundel/status/2062650378089594955
- 发布日期：2026-06-04 21:39 UTC
- 访问/观测日期：2026-09-27【主验，X Article 正文】
- 来源类型：作者本人。他写的是 Codex goal mode 怎么用
- 原文摘录：
  > “The prompt you define when you activate goal mode might act as your initial prompt but more importantly it will act as your exit criteria for the goal.”
  > “In most cases a good goal contains a clear number for the model to reach before the goal is considered complete.”
  > “If your goal is ambitious or if there are various ways that Codex could get closer to the goal it’s important that you give Codex tools to measure progress.”
  > “getting to a 100% passable test rate by reducing test coverage.”
- 做法，他自己的七条：
  1. 那句话主要是退出条件，不要写长。最好带一个数。他的例子是构建部署时间降 30%、迁移后测试对齐到 100%、生产环境最大内容绘制低于 2.5 秒。还不确定时先对话，让 Codex 根据对话自己设 goal，之后还能改。
  2. 有线索就写上从哪下手、能用什么工具、哪条路是错的。也可以先在 plan mode 写成文件，再让 goal 去对着那份计划。
  3. 给它测量进度的工具。他让 Codex 自己做截图 diff，工具后来还长出了不同的 diff 模式。同时写上哪些情况不算做完：把设计图裁下来嵌进界面冒充像素级一致，或靠删测试把通过率做成 100%。
  4. 环境要像生产：同一套栈、同一组开关、类似的数据库。预览环境少了生产的构建路径时，就改到真正相近的环境上部署。
  5. 「按这张图做到像素级」容易把模型困在图标上。图只当上下文。是否做完改看功能清单、要实施的规格、是否守住设计系统。
  6. 跑很久就让它在有意义的步骤提交并推草稿 PR，或更新一份给人看的 HTML / 图 / markdown，或把大进展发到 Slack。查进度用旁边的新对话，不打断这条 goal。
  7. 达到之后做 `/review`，并让它回想试过的失败方案，把留在 diff 里的废招清掉。
- 该摘录支持的最小主张：2026-06 Codex 这边把 goal 写成退出条件。数用来判定达到；测量工具用来看见中途有没有靠近；另外写明哪些取巧不算完成。
- 不支持什么：120 小时是「有人用过」，不是对照。不证明带数的 goal 比不带数的结果更好。与 Anthropic 文档同属「可核终态」这一类，作者和产品都不同，不并成一家。

## 判读

- 观察：X 上被传开的句子常常没有完成条件。打开本人帖之后，Steinberger 的用法和 Kundel 的七条是两套可以并列的写法。一套把品味留在停的句子里，用实机测和进度文件撑住过程。一套要求停的句子本身带一个数，并事先写好假完成。
- 推断：有号召力的帖值得打开，因为做法经常不在被引用的那一句里，而在同人紧接着的例子里。
- 与现有材料关系：A4 此前写原帖未打开。以本档为准。Osmani 排除「把界面做好」仍有效；Steinberger 的「架构让你满意」就是那种句子，他用旁边的节拍补上，不是把它改成硬规则。

## 负结论与限制

- LangChain 2026-06-02 的帖（https://x.com/LangChain/status/2061875246110507011）只写「挂上 rubric，grader 改到全部满足」。同一机构的机制已在 A2，不另计。
- Shreya Shankar 2025-11-16 的长帖（https://x.com/sh_reya/status/1990161469120659897）把 eval 拆成标准、怎么用、规模化。窗外，不摘做法。
- Karpathy 的两帖已打开，见 [`evidence-2026-09-27-a10-karpathy.md`](evidence-2026-09-27-a10-karpathy.md)，都在窗边。Cherny 2026-07-17 全文已补进 A4。6 月以后 Karpathy 没有另写完成条件的原帖。
- 不能推出：X 上的热帖普遍含有可核终态；「让你满意」加上实机测就已经等于硬规则。
