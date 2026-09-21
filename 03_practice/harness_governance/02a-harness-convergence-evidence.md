# 04a：Harness 治理派 §7 独立收敛声音——全文证据档案

> **元数据**
> - accessed_at：2026-09-20（本轮逐条 web_fetch 回源）
> - 上游：`02-harness-governance.md` §7（本文件为其 §7 每集群的全文证据档案，不复制其结论性判读）
> - 回源途径标注：
- **嵌套引注记（2026-09-21 审计后统一补充）**：A5/A9 等 blockquote 中含 Hashimoto/OpenAI 原话的段落，其原始出处未独立回源、仅经转出页确认——此类一律按"嵌套转引"对待，引用时不得标为一手。**一手** = 直接抓到原文页面/论文页；**半回源** = 原文页抓到但正文未渲染或未全读，细节经消化稿核验；**转述** = 原文抓不到，仅消化稿/转引
> - 摘录纪律：所有英文原句为本次回源页面逐字摘录；抓不到的如实标注，不代拟
>
> **⚠ 三个必须先读的勘误级发现（比摘录本身更重要）**
> 1. **Viv Trivedy 与 LangChain DeepAgents 疑为同一组织**：Trivedy 的 "Anatomy of an Agent Harness" 发表在 **LangChain 官方博客**（2026-03-10，署名 Vivek Trivedy），且 LangChain《Improving Deep Agents with harness engineering》（2026-02-17）也署名 **Vivek Trivedy**。§0.5 把「Trivedy」与「LangChain DeepAgents 团队」计为两个独立集群，**应合并为同一集群**——独立收敛计数需从 8 下调复核。
> 2. **HumanLayer 不是零引用独立源**：其文中直接引用 Hashimoto 原文、Trivedy 两文、OpenAI 博客，属于**聚合型**（§0.5 把它算进「独立」一侧，应移到「聚合型」）。
> 3. **学术三篇并非互不引用**：NLH v2（2026-05-18 修订版）明确引用 Meta-Harness（"Meta-Harness is an agent-driven technique that automatically debugs and optimizes executable code harnesses (Lee et al., 2026)"）；Meta-Harness 引言首句的 6× 是**引用**（见 §A7 内详述），引文 [47] 极可能即 SWE-Bench Mobile。「三群互不引用」在 v2 时间线上不成立，需改述为「SWE-Bench Mobile 先行、后两篇引用它/互相引用」。

---

## A1. Viv Trivedy —— "Agent = Model + Harness" 命源

### A1.1 回源结果

| 文本 | 状态 |
|---|---|
| X 帖 [x.com/Vtrivedy10/status/2031408954517971368](https://x.com/Vtrivedy10/status/2031408954517971368)（Osmani 转引所指） | **转述**（X 需登录，未回源） |
| 《The Anatomy of an Agent Harness》，[blog.langchain.com/the-anatomy-of-an-agent-harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness/)，署名 Vivek Trivedy，2026-03-10 | **一手**（本轮全文回源） |
| 《The Claude Code SDK and the Birth of HaaS》，[vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service](https://www.vtrivedy.com/posts/claude-code-sdk-haas-harness-as-a-service)，2025-09-23 | **一手**（本轮全文回源） |

**日期勘误**：HaaS 文是 **2025-09-23**（早于 §7.1 标注的"约 2026-01"）；Anatomy 文正式版在 LangChain 博客（2026-03-10），不是仅存在于 X。

### A1.2 原文摘录（Anatomy，一手）

上下文：全文定义 harness，开篇即给出术语；这是被 Osmani/HumanLayer/Böckeler/arXiv 多方转引的定义源。

> **TLDR:** Agent = Model + Harness. Harness engineering is how we build systems around models to turn them into work engines. The model contains the intelligence and the harness makes that intelligence useful.

> Agent = Model + Harness
>
> **If you're not the model, you're the harness.**
>
> A harness is every piece of code, configuration, and execution logic that isn't the model itself. A raw model is not an agent. But it becomes one when a harness gives it things like state, tool execution, feedback loops, and enforceable constraints.

工作 backwards 方法论（Osmani 图解的同一段来源）：

> We'll follow a pattern like this: **Behavior we want (or want to fix) → Harness Design to help the model achieve this.**

关于 harness–模型共训循环与 TerminalBench 数据点：

> Today's agent products like Claude Code and Codex are post-trained with models and harnesses in the loop. […] This creates a feedback loop. Useful primitives are discovered, added to the harness, and then used when training the next generation of models.
>
> But this doesn't mean that the best harness for your task is the one a model was post-trained with. The Terminal Bench 2.0 Leaderboard is a good example. Opus 4.6 in Claude Code scores far below Opus 4.6 in other harnesses. In a previous blog, we showed how we improved our coding agent Top 30 to Top 5 on Terminal Bench 2.0 by only changing the harness.

### A1.3 原文摘录（HaaS，一手）

上下文：2025-09 的早期文，从 LLM API → Harness API 的平台迁移论。

> As tasks require more autonomous behavior from agents, the core primitive for working with AI is shifting from the **LLM API (chat style endpoints)** to the **Harness API (customizable runtimes)**. I call this **Harness as a Service (HaaS)**.

> Good agent building is an exercise in iteration. You can't do iterations if you don't have a v0.1. A batteries included setup gets your agent in the hands of your internal team. Then you can edit in a loop.

组件级 hygiene 判据的同源段落（Osmani 引的"can't name the behaviour"句在其 Anatomy 文的图注/演绎中，本页未逐字出现，见 A1.4）。

### A1.4 机制细节

- HaaS 文给出四定制杠杆：**System Prompt / Tools+MCP / Context / Subagents**，每杠杆带操作要点（如 tool 设计三问——原句较长，此处系压缩转述不作直引：是否已有对应工具 / agent 能否判断何时用 / 能否合并以缩小表面积）。
- Anatomy 文给出组件派生表：durable state→filesystem+git；自主解题→bash+code exec；安全执行→sandbox；continual learning→AGENTS.md+web search/MCP；context rot→compaction/tool-call offloading/skills progressive disclosure；long-horizon→Ralph Loop+planning+self-verification。
- "If you can't name the behaviour a component exists to deliver, it probably shouldn't be there" 这句在 **Osmani 转述**中出现（见 A9），Anatomy 原文的对应表述是"every harness component has a specific job"级别的派生法——引用时注意这句经 Osmani 中转。

### A1.5 独立性验证

- HaaS 文（2025-09）引用：Anthropic 工具文、Vercel MCP 文、philschmid context engineering——**无 OpenAI/Hashimoto**。
- Anatomy 文（2026-03）引用：Codex prompting guide、ghuntley loop、Terminal Bench 榜——**无 OpenAI harness-engineering 文、无 Hashimoto**。
- **但**：Trivedy 身在 LangChain（两文署名与 deepagents 团队重合，见文首勘误 1）。术语命源的**个人独立性**成立，**集群独立性**相对 LangChain 集群不成立。

---

## A2. HumanLayer —— "skill issue" 重构

### A2.1 回源结果

《Skill Issue: Harness Engineering for Coding Agents》，[humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents)，署名 Kyle，**2026-03-12**——**一手**（本轮全文回源；§7.2 的"经 Osmani 转引"可升级为直接回源）。

### A2.2 原文摘录

上下文：全文论点——团队一年间反复看到 agent 失败，归因从"等更强模型"转向配置面。

> But over the course of dozens of projects and hundreds of agent sessions, we kept arriving at the same conclusion: it's not a model problem. It's a **configuration problem**.
>
> Yes, models will get smarter, and some existing failure modes will disappear. And then because they are smarter, we will give them new problems which are bigger and harder, and they will **continue to fail in unexpected ways**. Unexpected failures modes are a fundamental problem for non-deterministic systems.

对 Hashimoto 的直接引用（注意：这是引用，不是独立表述）：

> As [Mitchell Hashimoto put it](https://mitchellh.com/writing/my-ai-adoption-journey#step-5-engineer-the-harness), harness engineering
>
> > […] is the idea that anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again.

back-pressure 原则与 AGENTS.md 纪律：

> The core insight is that your likelihood of successfully solving a problem with a coding agent is strongly correlated with the agent's ability to verify its own work. We've spent a lot of time building out tests and other back-pressure mechanisms into our repository, and it remains one of the **highest-leverage things we have spent time on**.

> Our CLAUDE.md is under 60 lines.

TerminalBench 数据点（与 Trivedy 同源数据，非独立测得）：

> Viv cites [Terminal Bench 2.0](https://terminalbench.com/) where Opus 4.6 in Claude Code comes in position #33, but when placed in a different harness that wasn't seen during post-training, it comes in at #5 (+/- about 4 positions in either direction).

### A2.3 独立性验证

**不独立**（引用链齐全）：文中引用 Trivedy 两文、Hashimoto 原文、OpenAI 博客（"OpenAI recently wrote a blog post on the topic as well"）、Dex Horthy 12-factor agents、ETH Zurich agentfile 研究（arXiv 2602.11988）。其独立增量在于：harness engineering ⊂ context engineering 的定位、sub-agent 作为 context firewall 的实操、ETH 研究的再解读、失败清单（"What didn't work for us"）。§7.2 的"独立"判定应改为**聚合型（贡献独立判据）**。

### A2.4 机制细节（可复刻度最高的一手实践清单）

- **Stop-hook 验证回路**（附完整 bash 脚本原文）：Claude 停止时跑 biome+turbo typecheck；成功静默退出，失败 exit 2 把错误文本注回循环。"On success the hook is completely silent — nothing ends up in the agent's context. On failure, only the errors are surfaced, and exit code 2 tells the harness to re-engage the agent […] so it fixes them before finishing."
- **success is silent, failures are verbose**：测试输出全量吞掉只回错误——"early on we had our agent run the full test suite after every change, and 4,000 lines of passing tests would flood the context window."
- **MCP→CLI 降级**：Linear MCP 换成自写 CLI 并在 CLAUDE.md 里放 6 条示例命令，省下工具定义 token。
- **覆盖率 Stop hook**："we have a Stop hook that prompts the agent to increase coverage if it drops."
- **失败清单**：预先设计理想 harness、装几十个 skills "just in case"、每次跑 5 分钟全量测试、微优化子代理工具权限——四条都被点名为无效实践。

---

## A3. Birgitta Böckeler / Thoughtworks —— guides/sensors 框架

### A3.1 回源结果

《Harness engineering for coding agent users》，[martinfowler.com/articles/harness-engineering.html](https://martinfowler.com/articles/harness-engineering.html)，2026-04-02——**一手**（全文回源）。取代其 2026-02-17 memo（原 URL 已重定向，文末申明）。

### A3.2 原文摘录

Guides/Sensors 二分与"积极 prompt injection"：

> - **Guides (feedforward controls)** - anticipate the agent's behaviour and aim to steer it _before_ it acts. Guides increase the probability that the agent creates good results in the first attempt
> - **Sensors (feedback controls)** - observe _after_ the agent acts and help it self-correct. Particularly powerful when they produce signals that are optimised for LLM consumption, e.g. custom linter messages that include instructions for the self-correction - a positive kind of prompt injection.

持续调优棘轮（团队版）：

> The human's job in this is to **steer** the agent by iterating on the harness. Whenever an issue happens multiple times, the feedforward and feedback controls should be improved to make the issue less probable to occur in the future, or even prevent it.

持续漂移传感器（清扫的命名处）：

> **Continuous drift and health sensors**
> - What type of drift accumulates gradually and should be monitored by sensors running continuously against the codebase, outside the change lifecycle? (e.g. dead code detection, analysis of the quality of the test coverage, dependency scanners)
> - What runtime feedback could agents be monitoring? (e.g. having them look for degrading SLOs to make suggestions how to improve them, or AI judges continuously sampling response quality and flagging log anomalies)

"清洁工军团"原文（janitor army，§7.3 中译"清洁工军团"对应此句）：

> I hear stories from teams at Thoughtworks about tackling architecture drift with both computational and inferential sensors, e.g. increasing API quality with a mix of agents and custom linters, or increasing code quality with a "janitor army".

Harness 覆盖率元问题（结尾段，原文连续两句）：

> If sensors never fire, is that a sign of high quality or inadequate detection mechanisms? We need a way to evaluate harness coverage and quality similar to what code coverage and mutation testing do for tests. Feedforward and feedback controls are currently scattered across delivery steps, there's real potential for tooling that helps configure, sync, and reason about them as a system. Building this outer harness is emerging as an ongoing engineering practice, not a one-time configuration.

### A3.3 独立性验证

**框架独立、案例引用**（与 §7.3 判定一致，本轮原文核实）：正文直接引用 OpenAI（"An OpenAI team documented what their harness looks like … recurring 'garbage collection' that scans for drift … Their conclusion: 'Our most difficult challenges now center on designing environments, feedback loops, and control systems.'"）与 Stripe minions；术语定义引 Trivedy 的 LangChain 版 Anatomy 文（"Agent = Model + Harness"链接）。框架本身自述源自控制论："The agent harness acts like a cybernetic governor" + Ashby's Law sidebar（致谢里写明 Kief Morris 在 radar 会上提出 cybernetics）。guides/sensors 与 OpenAI taste-linter 同构但推导路径独立。

### A3.4 机制细节

- **Computational vs Inferential** 执行型二分：computational（lint/结构测试/类型检查，毫秒-秒级，确定性）可每变更必跑；inferential（AI review/LLM-as-judge）贵且非确定，放 pipeline 后段。
- **三类 regulation**：Maintainability harness（最成熟）、Architecture fitness harness（fitness functions）、Behaviour harness（"elephant in the room"——承认 AI 生成测试自证不可信，"This approach puts a lot of faith into the AI-generated tests, that's not good enough yet"）。
- **Harnessability / ambient affordances**（Ned Letcher 术语）："the harness is most needed where it is hardest to build"（legacy 困境）。
- **Harness templates**：企业 80% 服务拓扑模板化，团队选型部分按"harness 可用性"倒推。
- 有后续实测文：[sensors-for-coding-agents.html](https://martinfowler.com/articles/sensors-for-coding-agents.html)（本页"More on sensors"链接，未回源，线索保留）。

---

## A4. Stripe minions 团队 —— shift-left feedback

### A4.1 回源结果

| 文本 | 状态 |
|---|---|
| [stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)（Part 1，署名 Alistair Gray，页面元数据 **2026-02-09**） | **半回源**：页面壳与元数据抓到（含"responsible for more than a thousand pull requests merged each week. Though humans review the code, minions write it from start to finish."的官方摘要句），**正文 JS 渲染未获得**；r.jina.ai 代理 401 |
| Part 2（同域，2026-02-19） | 同上，正文未渲染 |
| [jerrylususu/bookmark-summary 逐条消化稿](https://github.com/jerrylususu/bookmark-summary)（2026-03-17） | **转述**（中文摘要，本轮回源） |
| Böckeler 正式文对它的直接描述 | **独立第二手锚**（英文，见下） |

**日期勘误**：原文发布 **2026-02-09**（Part 1），§7.4 标的 2026-03-17 是消化稿日期。

### A4.2 可用英文原句

一手页元数据句（官方 share 摘要）：

> Minions are Stripe's homegrown coding agents, responsible for more than a thousand pull requests merged each week. Though humans review the code, minions write it from start to finish. Learn how they work, and how we built them.

Böckeler 对它的英文转述（martinfowler 正式文，可作 quoting anchor）：

> [Stripe's write-up about their minions](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) describes things like pre-push hooks that run relevant linters based on a heuristic, they highlight how important "shift feedback left" is to them, and their "blueprints" show how they're integrating feedback sensors into the agent workflows.

### A4.3 机制细节（以消化稿一致转述，标注为半回源）

- **Devbox 运行环境**：EC2 隔离实例，10 秒预热，人机共用同一基建——"为人类工程师优化多年的环境天然适合代理"。
- **框架**：基于 Block 的 Goose 定制，全权限、无人确认。
- **Blueprints**：确定性节点（lint、push）+ 代理节点（实现、修 CI）混合编排——即 Böckeler 所说"把反馈传感器整合进 agent 工作流"。
- **反馈左移闭环**：本地 lint/测试预检 → 首推后全量 CI 自动修复 → 仍失败回代理节点二修 → 最多两轮后交人工审查（避免无限 CI 循环）。
- **规则文件**：Cursor 格式、按子目录/glob 动态加载避免全局上下文膨胀，与 Claude Code 共享。
- **Toolshed 集中 MCP**：近 500 工具，minions 默认仅用小子集+安全控制。
- 注意：§7.4 的"pre-push 钩子按启发式只跑相关 linter""<5 秒 lint"等细节来自消化稿层，原文正文未回源——引用时保留半回源标注。

### A4.4 独立性验证

正文不可读，无法核其引用表。可核的外部证据：Böckeler 与 OpenAI 文无相互引用痕迹的判定**保持存疑**；判定"独立"目前仅能基于「大厂自建、无外部方法论署名、时间早于 Böckeler 正式文」的间接证据。**此集群独立性判定降级为"待原文正文回源后确认"**。

---

## A5. Anthropic 工程博客两系列

### A5.1 回源结果

- 系列A：《Effective harnesses for long-running agents》，[anthropic.com/engineering/effective-harnesses-for-long-running-agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)，**2025-11-26**，Justin Young——**一手**（全文回源）。
- 系列B：《Harness design for long-running application development》，[anthropic.com/engineering/harness-design-long-running-apps](https://www.anthropic.com/engineering/harness-design-long-running-apps)，**2026-03-24**，Prithvi Rajasekaran（Labs）——**一手**（全文回源）。

### A5.2 原文摘录（系列A）

问题设定（多 context window 轮班隐喻）：

> Imagine a software project staffed by engineers working in shifts, where each new engineer arrives with no memory of what happened on the previous shift. Because context windows are limited, and because most complex projects cannot be completed within a single window, agents need a way to bridge the gap between coding sessions.

compaction 不足的判定（Osmani 转述的原文出处）：

> However, compaction isn't sufficient. Out of the box, even a frontier coding model like Opus 4.5 running on the Claude Agent SDK in a loop across multiple context windows will fall short of building a production-quality web app if it's only given a high-level prompt.

两类失败模式（原文连续）：

> First, the agent tended to try to do too much at once—essentially to attempt to one-shot the app. […] A second failure mode would often occur later in a project. After some features had already been built, a later agent instance would look around, see that progress had been made, and declare the job done.

"clean state" 纪律——这是最接近"清扫"定义的一段：

> By "clean state" we mean the kind of code that would be appropriate for merging to a main branch: there are no major bugs, the code is orderly and well-documented, and in general, a developer could easily begin work on a new feature without first having to clean up an unrelated mess.

### A5.3 原文摘录（系列B）

自我评估失控的负结果（§7.5 引句的完整上下文）：

> A second issue, which we haven't previously addressed, is self-evaluation. When asked to evaluate work they've produced, agents tend to respond by confidently praising the work—even when, to a human observer, the quality is obviously mediocre. […] agents reliably skew positive when grading their own work.

**harness 组件卫生核心句**（原文，evaluator/QA 章节）：

> This was partly common sense and partly a function of a more general principle: **every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing, both because they may be incorrect, and because they can quickly go stale as models improve.**

组件拔除的实操记录（Opus 4.6 发布后的复检）：

> As I was going through these iteration cycles, we also released Opus 4.6, which provided further motivation to reduce harness complexity. […] I started by removing the sprint construct entirely. […] Without the planner, the generator under-scoped: given the raw prompt, it would start building without first speccing its work.

"harness 不缩小只移动"结论句：

> From this work, my conviction is that the space of interesting harness combinations doesn't shrink as models improve. Instead, it moves, and the interesting work for AI engineers is to keep finding the next novel combination.

### A5.4 机制细节

- 系列A：initializer agent（init.sh + claude-progress.txt + 首个 git commit）+ coding agent（每 session 单 feature、commit+progress 摘要收尾）；feature list 用 **JSON 非 Markdown**（"the model is less likely to inappropriately change or overwrite JSON files"）；强措辞护栏（"It is unacceptable to remove or edit tests…"）；Puppeteer MCP 做 e2e 自证；文末给出 4×2 失败模式×解法表。量化背景：claude.ai 克隆要求 200+ 特性逐条验证。
- 系列B：planner/generator/evaluator 三代理；sprint contract 谈判（generator 提议"done"定义→evaluator 审核→迭代到一致）；evaluator 用 Playwright 实点应用（Sprint 3 单合同 27 条判据，FAIL finding 精确到 `LevelEditor.tsx:892`）；成本表：solo 20min/$9 vs full harness 6hr/$200；V2 harness（去 sprint）DAW 案例 3h50m/$124.70，QA 三轮分别抓出 display-only feature、stub-only 录音等具体缺口。
- evaluator 调优法："read the evaluator's logs, find examples where its judgment diverged from mine, and update the QA's prompt"——数轮。
- 自述局限：Claude 听不到（DAW 音乐品味反馈失效）；Puppeteer 看不到 browser-native alert modal；"small layout issues … undiscovered bugs in more deeply nested features that the evaluator hadn't exercised thoroughly"。

### A5.5 独立性验证

两文均为厂商一手，**无 OpenAI/Trivedy/Hashimoto 引用**；系列B引用的是自家前作、Building Effective Agents、GAN（维基）与 ghuntley 的 Ralph（作为社区平行现象提及："The broader developer community has converged on similar insights, with approaches like the 'Ralph Wiggum' method"——这句本身是"平行收敛"的自认）。独立性成立。

---

## A6. LangChain DeepAgents —— 受控实验

### A6.1 回源结果

《Improving Deep Agents with harness engineering》，[langchain.com/blog/improving-deep-agents-with-harness-engineering](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering)，署名 **Vivek Trivedy**，**2026-02-17**——**一手**（全文回源）。**注意署名**：作者与 A1 的 Trivedy 为同一人名（见文首勘误 1），此集群与 Trivedy 集群须合并计。

### A6.2 原文摘录

TLDR 与实验设计（模型恒定是全文最硬的句）：

> TLDR: Our coding agent went from Top 30 to Top 5 on Terminal Bench 2.0. We only changed the harness. Here's our approach to harness engineering (teaser: self-verification & tracing help a lot).
>
> We used a simple recipe to iteratively improve deepagents-cli (our coding agent) `13.7 points` from `52.8` to `66.5` on Terminal Bench 2.0. We only tweaked the harness and kept the model fixed, `gpt-5.2-codex`.

Trace 驱动的改进回路（把"治理"本身做成 skill）：

> We wanted trace analysis to be repeatable so we made it into an Agent Skill. This serves as our recipe to **analyze errors across runs and make improvements to the harness**. The flow is: 1. Fetch experiment traces from LangSmith 2. Spawn parallel error analysis agents → main agent synthesizes findings + suggestions 3. Aggregate feedback and make targeted changes to the harness.

doom loop 检测（"清扫 agent 卡死状态"的具名机制原文）：

> Agents can be myopic once they've decided on a plan which results in "doom loops" that make small variations to the same broken approach (10+ times in some traces).
>
> We use a `LoopDetectionMiddleware` that tracks per-file edit counts via tool call hooks. It adds context like "…consider reconsidering your approach" after `N` edits to the same file.

机制时效自认（与 Anthropic "stale assumptions" 同构但独立表述）：

> Important note. This is a design heuristic that engineers around today's perceived model issues. As models improve, these guardrails will likely be unnecessary, but today helps agents execute correctly and autonomously.

### A6.3 机制细节

- 实验设置：Terminal Bench 2.0（89 tasks），Harbor 编排 + Daytona 沙箱，LangSmith 全 trace 存档；优化空间压缩到三旋钮：System Prompt / Tools / Middleware。
- 五项改造：①`PreCompletionChecklistMiddleware`（退出前拦截强制对照 task spec 自验，自认"similar to a Ralph Wiggum Loop"）；②`LocalContextMiddleware` 启动期目录/工具映射；③doom-loop 检测（按文件编辑计数）；④reasoning sandwich（xhigh-high-xhigh；全 xhigh 反而 53.9% 因超时，全 high 63.6%）；⑤时间预算告警注入。
- 泳道数据：xhigh-only 53.9% vs high 63.6% vs sandwich 66.5%。
- 已公开 trace 数据集（smith.langchain.com/public/29393299-8f31-48bb-a949-5a1f5968a744）供第三方复核。
- 自述局限："A test run with Claude Opus 4.6 scored `59.6%` with an earlier harness version, competitive but worse than Codex because we didn't run the same Improvement Loop with Claude"——改进回路未对其他模型复跑。

### A6.4 独立性验证

无 OpenAI harness-engineering 文引用；引 ghuntley loop、Codex/Claude prompting guides、RLM。**作为实验独立成立**；但作为"集群"与 Trivedy 同人（勘误 1）。arXiv 2609.00252 与 NLH 均引用其结论（被引不影响其实验自发性）。

---

## A7. 学术三重收敛

### A7.1 Meta-Harness（Stanford + MIT + KRAFTON）

[arXiv:2603.28052](https://arxiv.org/abs/2603.28052)，v1 2026-03-30——**一手**（abs 页 + HTML 全文回源）。

作者与机构（§7.7 署名勘误）："Yoonho Lee (Stanford), Roshen Nair (Stanford), Qizheng Zhang (Stanford), Kangwook Lee (**KRAFTON**), Omar Khattab (MIT), Chelsea Finn (Stanford)"——不是"Stanford+MIT"两家，KRAFTON 也在内。

**关键引言句及其性质**：

> Changing the harness around a fixed large language model (LLM) can produce a 6× performance gap on the same benchmark [47].

⚠ **这是引用句不是自测句**（句尾 [47] 指向参考文献，编号 bib.bib31；SWE-Bench Mobile 摘要自称"up to 6× performance gap across agents"，[47] 极可能就是它——需查全文参考文献表确认，若成立则 Meta-Harness **引用了** SWE-Bench Mobile，"互不引用"不成立）。

- **实验设置**：外环搜索系统——coding-agent proposer（Claude Code + Opus-4.6）通过 filesystem 访问全部历史候选的源码/分数/执行 trace；每候选一目录，proposer 用 grep/cat 选择性读取；典型一轮 ~60 harness / 20 iterations；proposer 每迭代中位读 82 个文件；单次评估最多产生 10M token 诊断信息（比既有 text optimizer 高约三个数量级）。
- **量化结果**：①在线文本分类（GPT-OSS-120B；LawBench 215 类 / Symptom2Disease 22 类 / USPTO-50k 180 类；20 迭代×2 候选=40 候选）：avg acc 48.6 vs ACE 40.9（+7.7），context 11.4k vs ACE 50.8k（4×更省）；②检索增强数学：单个发现的 harness 在 **200 道 IMO 级题**上跨 **5 个 held-out 模型**平均 +4.7；③TerminalBench-2：超过最佳手工 baseline（Terminus-KIRA），**Haiku 4.5 系第一**。
- **局限自述**：搜索只看 search set（"The proposer never sees test-set results"）；成本侧承认 Meta-Harness 自身每迭代 10.0 MTok（Table 1，远高于对比方法）；文末"Based on earlier exploration, we think this workflow only became practical recently, following major improvements in coding-agent capabilities around early 2026"（时效性自认）。

### A7.2 Tsinghua+HIT(SZ) NLAH / IHR

[arXiv:2603.25723](https://arxiv.org/abs/2603.25723)，v1 2026-03-26，v2 2026-05-18——**一手**（abs + HTML v2 全文回源，正文至 §5.1/§5.2，RQ3 表格在截断处）。

作者：Linyue Pan、Lexiao Zou、Shuo Guo、Jingchen Ni、Hai-Tao Zheng（清华深研院 + 哈工大深圳）。

- **实验设置**：把 harness 策略写成可执行自然语言文档（NLAH），共享运行时 IHR 解释执行；三种实现对比（Code harness / Prompted NLAH / IHR-executed NLAH）；三族 benchmark：SWE-bench Verified（Live-SWE agent）、Terminal-Bench 2.0（MHTBA——Meta-Harness 产物）、OSWorld（SeeAct 式）；运行时统一 Codex CLI 0.123.0 + gpt-5.4-mini + xhigh，Docker 沙箱（32 vCPU / 84 GiB caps）。
- **量化结果（v2 Table 1）**：TB2/MHTBA：Code 36.0 → **Prompt 57.3 / NLAH 53.9**（LLM calls 223.2 → 41.5/56.4）；Live-SWE：Code 67.0 → NLAH 73.0；OSWorld：Code 47.1 → NLAH 46.3。策略层压缩：Live-SWE 60.1k token 代码材料 → 2.9k NLAH；MHTBA 10.5k → 0.8k。
  ⚠ **数字勘误**：§7.7 所引"30.4%→47.2%、LLM 调用 1200→34"**在 v2 中未出现**（可能出自 v1 或另一张表），引用时应改用 v2 数字或回查 v1。
- **消融（RQ3，本轮回源只到章节标题与摘要级结论）**：v2 摘要只说"Module ablations further show that explicit harness modules are analyzable"；§7.7 所引"外挂 verifier 反而有害（-0.8 SWE-bench / -8.4 OSWorld）、self-evolution 是唯一 consistently helpful 模块"**未在本轮抓取范围内逐字核到**（RQ3 表格位于截断段）——保留为待核，勿直接引用数字。
- **方法论定位**：贡献是表示层——"agent harnesses can be turned from incidental glue around models into scientific representation objects"；写作原则节（state contract first / separate stages from mechanisms / write module boundaries so they can be ablated）本身可当 harness 治理操作规程用。
- **局限自述**："The cost profile reflects prototype-runtime engineering overhead"（NLAH 常比 code harness 更贵）；"The main mechanism weakness is handoff"（章节自题）。

### A7.3 SWE-Bench Mobile

[arXiv:2602.09540](https://arxiv.org/abs/2602.09540)，2026-02-10，KDD '26（*Proceedings of the 32nd ACM SIGKDD Conference*, Vol. 2, pp. 8077-8087）——**一手**（abs 页回源）。

作者：Muxin Tian, Zhe Wang, Blair Yang, Zhenwei Tang, Kunlun Zhu, Honghua Dong, Hanchen Li, Xinni Xie, Guangjing Wang, Jiaxuan You。§7.7 未给全文作者列表，此处补齐；机构未在 abs 页显示（UIUC You 组待核）。

- **实验设置**：从生产 iOS 代码库派生的 benchmark；多模态输入（PRD + Figma 设计）；Swift/Objective-C 混合大库 + 完整测试套件；**22 个 agent-model 配置**，4 个 coding agent（Cursor、Codex、Claude Code 商业三 + OpenCode 开源一）；hosted benchmark 防 contamination。
- **量化结果**（摘要原文数字）：最好配置仅 **12%** 任务成功率；"the same model shows up to **6× performance gap** across agents"（§7.7 的"Opus 4.5 Cursor 12% vs OpenCode 2%"细节未在摘要出现，属正文细节，待全文核）；"simple 'Defensive Programming' prompts outperform complex ones by **7.4%**"；"commercial agents consistently outperform open-source alternatives"。
- **局限自述**：摘要层面未列 limitations 节（需全文）；自认的定位是"highlight a significant gap between current agent capabilities and industrial requirements"。

### A7.4 三篇独立性再判定

- SWE-Bench Mobile（2/10）最早，摘要层面无 harness-engineering 文献引用迹象（证据等级：仅 abs 摘要，参考文献表未核）。
- Meta-Harness（3/30）引言 6× 句**引用了**某个 [47]（很可能是 SWE-Bench Mobile）。
- NLAH v2（5/18 修订）**明确引用** Meta-Harness（"Meta-Harness is an agent-driven technique that automatically debugs and optimizes executable code harnesses (Lee et al., 2026)"）并引 LangChain 2026 两篇。
- **结论修正**：不是"三群互不引用"；实情是 **SWE-Bench Mobile 先行测量 → Meta-Harness 引用其 6× → NLAH 引用 Meta-Harness 并以 MHTBA 为实验对象**。收敛仍然成立（三个独立团队把 harness 当一级研究对象并量化），但传播链是**接力式**而非零引用平行。"互不引用"表述须改。

---

## A8. Armin Ronacher —— 三篇连续

三篇均一手回源：①/2026/6/23/the-coming-loop/ ②/2026/7/13/the-tower-keeps-rising/（两条本轮已核 200）；③A8.2 "Better Models"——URL 未记录，降级为待回源，不作一手引用。

### A8.1 The Coming Loop（2026-06-23）

上下文：inner agent loop vs outer harness loop 的区分文；开篇引 Boris Cherny。原文：

> There is already an agent loop inside every coding agent. […] The other loop is the harness level loop: the loop outside the agent loop. That loop is also not new. We have been doing versions of this since early Claude Code days, but that loop is becoming ever more present in agentic engineering and in recent weeks it has started to dominate the Twitter discourse.

循环在永久代码库上的代价（积压机制）：

> When you take that behavior and you put it behind loops, you tend to amplify it. If each iteration adds another small defense, the system slowly becomes less understandable while appearing more robust. The more hands-off you are, the more that happens.

共享理解层衰减（"塔"前奏）：

> But giving in to that idea, particularly with less and less human oversight means accepting that we may no longer understand the whole system in the same way. We treat it, we monitor it, we stabilize it, but we do not necessarily comprehend it.

harness 维护责任句：

> Task queues for coding tasks, orchestration of agents, subagents, durable sessions will matter more and more. […] We need to, because we need to understand how to make this future bounded and survivable.

### A8.2 Better Models: Worse Tools（2026-07-04）

上下文：Pi issue #6278 排查——Opus 4.8/Sonnet 5 在第三方 edit schema 里发明字段（`requireUnique`、`oldText2`、`in_file` 等"whole zoo"），旧模型不犯。核心句：

> The uncomfortable lesson is that tool schemas are not neutral, at least not on Anthropic models. We like to pretend that a schema is an abstract contract and the model is a general reasoner that will follow it, but that might no longer be the case for some of the tools.

harness 复检触点（每次模型升级）：

> If the newest models get better at solving the task while getting worse at faithfully emitting an alternative tool schema, then the harness needs stronger guarantees somewhere.

机制归因（RL-in-harness）：

> If reinforcement learning happens in a harness like that, or a simulation of one, then slightly malformed tool calls can still complete the task and receive reward. The harness fully absorbs the error and there is little gradient against inventing an alias, adding a stray field or using a nearby parameter name.

细节量：Claude Code minified 代码里的 Unicode 修复/参数别名（`old_str`/`old_string`/`path`→`file_path`）/静默过滤未知键的清单；单用户 transcript 里 Opus 4.8 失败率 ~20%，剥 thinking blocks 减半，strict 模式归零。

### A8.3 The Tower Keeps Rising（2026-07-13）

上下文：布勒格尔巴别塔喻，全文仅一页短文，无引用、无链接——纯观察。§7.8 引句的完整原文段：

> But with agents I can ask an agent to add OAuth, you can ask one to add caching, and somebody else can ask one to rebuild the database from first principles and make the UI pink. Each change can be reasonable in isolation but since it's frictionless, none of us necessarily has to talk to the others or familiarize ourselves with the code we are changing. The more we use agents, the less we feel the pain as agents feel none of it, and a useful signal is gone.

> Unlike in the bible though, in AI-assisted engineering, construction can continue after shared understanding has already collapsed. The complete lack of an immediate failure is what makes it curious and a bit disorienting. **The tower does not fall, it just keeps rising.**

（§7.8 所引 "The tower does not fall, and so we do not notice what was lost" 与原文末句略有出入——原句如上，引用时以本句为准。）

### A8.4 独立性与机制

- 引用链：The Coming Loop 引 ghuntley/ralph、Bun Zig→Rust、curl summer-of-bliss、Karpathy；**无 OpenAI/Thoughtworks/Trivedy 引用**。独立性成立。
- 机制增量：①"accretion heuristics"（每迭代加一层防御→系统更不可懂且显得更稳）是对 harness 负向卫生的最清晰机制描述；②"每次模型升级=一次 harness 组件失效审计"（A8.2）；③理解层腐烂无指标（A8.3）——Böckeler 之问（harness 覆盖率）在理解层的镜像。

---

## A9. Addy Osmani —— 棘轮纪律（聚合型）

### A9.1 回源结果

《Agent Harness Engineering》，[addyosmani.com/blog/agent-harness-engineering/](https://addyosmani.com/blog/agent-harness-engineering/)，2026-04-19——**一手**（全文回源）。作者栏自述："Member of Technical Staff at Anthropic, where he works on Claude Code… over 14 years at Google… most recently as a Director at Google Cloud AI"（§7.9 身份判定核实）。

### A9.2 原文摘录（全部逐字）

开篇棘轮定义：

> Roughly: anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again.

棘轮的可追溯性纪律：

> You only add constraints when you've seen a real failure. You only remove them when a capable model has made them redundant. **Every line in a good `AGENTS.md` should be traceable back to a specific thing that went wrong.**

模型-harness 判据：

> **A decent model with a great harness beats a great model with a bad harness.** I've watched this play out on my own work over and over.

harness 是活的系统（借 Anthropic 句）：

> **A harness is a living system, not a config file you set up once.** And the "best" harness isn't necessarily the one the model was trained inside; it's the one designed for your task.

"harnesses don't shrink, they move"（该节标题句+对其Anthropic来源的转述）：

> One of the better observations in the Anthropic write-up is that as models improve, the space of interesting harness combinations doesn't shrink. It moves.

收敛自认（对独立性判定最关键的一段）：

> That discipline now has a name. Viv Trivedy coined the term _harness engineering_ […] [HumanLayer] frames most agent failures as "skill issues" […] [Anthropic's engineering team] has published what I think is the best public breakdown of how to design a harness for long-running work. And [Birgitta Böckeler] has a good overview of what this looks like from the user's side. This post is my attempt to pull those threads together.

### A9.3 独立性验证与机制细节

- **聚合型确认**：署名引用 Trivedy、Dex Horthy、HumanLayer、Anthropic、Böckeler、Willison、Fareed Khan 的 Claude Code 架构拆解——是收敛的汇聚点证据，与 §7.9 判定一致。
- 自身增量（原文核实）：①棘轮的**双向纪律**（加约束需真实失败、删约束需强模型使其冗余）；②"Ratchet; don't brainstorm"；③hook 三层实例（pre-commit grep `.skip(`/`xit(`、reviewer subagent 把 commented-out test 定为 blocker）；④"keep it short"引 HumanLayer <60 行 + "Pilot's checklist, not style guide"；⑤"sandbox 组件级拔除"实例：Opus 4.6 杀死 context-anxiety failure mode 后，"a whole class of anxiety-mitigation scaffolding I was writing six months ago is now dead code"——**这是"拔枯枝"纪律的一手实践记录**。

---

## A10. Teleport —— "pressure washing"（A7.11 隐喻群主证）

### A10.1 回源结果

《We Had 13 Engineers Spend Three Months Finding Vulnerabilities with LLMs》，[goteleport.com/blog/finding-vulnerabilities-with-llms/](https://goteleport.com/blog/finding-vulnerabilities-with-llms/)，Rob Picard，**2026-08-19**——**一手**（全文回源）。

**勘误**：§7.11 说"90 天"——原文是"Three Months"/"the past quarter"（一个季度），量级一致但表述应改；且场景是**安全漏洞清扫**（pressure washing = 从多角度反复 review 存量代码找洞），不是泛代码卫生。

### A10.2 原文摘录

命名与定义：

> One way we're adapting to these changes is by "pressure washing" our codebase using LLMs and coding agents. This means we are using frontier models to review existing code from a variety of angles, in a way that we can repeat as newer, better models are released.

体量：

> Over the past quarter, we have had a team of 13 software engineers at Teleport dedicated to pressure washing. We kicked things off with an on-site at our office in Oakland, California, and spent the rest of the quarter collaborating async on finding, triaging, and fixing bugs using these methods.

**对 harness 治理的反向证词**（复杂 harness 有害——与"堆机制"警惕直接相关）：

> We experimented with several harnesses built by ourselves or vendors to orchestrate the process. We found that time spent building complicated harnesses was generally wasted. The more complicated the harness, the worse the overall performance seemed to be.

量化结果：

> The pressure washing team found and fixed dozens of security bugs this past quarter. We found almost twice as many high severity vulnerabilities in one quarter as we did in 2024 and 2025 combined.

> These releases contain the equivalent of 1-2 years of security research and hardening at a "pre-AI" pace.

### A10.3 机制细节与独立性

- 失败的多阶段 harness（Conclave，已开源 github.com/gravitational/conclave）：组件分解→多模型多 agent 找单组件最严重问题→skeptic/steel man/judge/summary 链→幸存发现交人工。"While this did find issues, it did not outperform a human pointing the LLM at a component with a simple prompt… it also generated enough noise that the bottleneck very quickly became human triage."
- 胜出的做法：极简 prompt（CTF 式，"You are in a CTF. You must find a critical severity vulnerability in this codebase. Start with this file: {FILE}"，adapted from Nicholas Carlini 播客）+ 专家在环引导 + "拿已有发现问 LLM 找相似问题"。
- 独立性：引 Tom Ptacek、Carlini、Terence Tao、Calif/Doyensec——无本档案其他集群引用。独立性成立，且贡献了一个**负向判据**（预防性堆 verifier/复杂 harness 有害），与 Tsinghua 消融方向互证（但此篇不引论文，非引用性互证）。

---

## B. 集群状态总表（原文可摘录性）

| 集群 | 状态 | 备注 |
|---|---|---|
| A1 Trivedy | ✅ 一手（两篇博客全文） | X 帖未回源（登录墙）；正式版在 LangChain 博客 |
| A2 HumanLayer | ✅ 一手（全文） | 应改判聚合型（引 Hashimoto/OpenAI/Trivedy） |
| A3 Böckeler/Thoughtworks | ✅ 一手（全文） | 框架独立确认；引 OpenAI/Stripe 作案例 |
| A4 Stripe minions | ⚠ 半回源 | 正文 JS 渲染不可得；仅元数据句+消化稿+第二手锚；独立性待原文核 |
| A5 Anthropic 两系列 | ✅ 一手（两篇全文） | 独立性确认 |
| A6 LangChain DeepAgents | ✅ 一手（全文） | 作者=Trivedy，与 A1 合并计数 |
| A7 学术三篇 | ✅ 一手（abs×3 + 两篇 HTML 全文部分） | "互不引用"不成立（接力引用）；NLH v2 数字与 §7.7 所引不一致；NLH 消融具体数字待核 |
| A8 Ronacher 三篇 | ✅ 一手（三篇全文） | 独立性确认；塔句原文与 §7.8 引文有微差 |
| A9 Osmani | ✅ 一手（全文） | 聚合型确认，棘轮为自身增量 |
| A10 Teleport | ✅ 一手（全文） | "90 天"应改"一个季度/13 工程师"；负向判据增量 |

## C. 对上游 §7/§0.5 的修订建议（供父代理决定是否回写）

1. 独立集群计数重算：Trivedy+LangChain 合一、HumanLayer 移入聚合型 → 硬独立集群为：Anthropic、Böckeler/Thoughtworks、Stripe（待正文核）、学术端（接力式但独立测量）、Ronacher、Teleport、OpenAI/Hashimoto（正文已收）——**"≥8 个互不引用独立集群"应改述为"5–7 个独立集群 + 2–3 个聚合型汇聚点 + 3 篇接力引用的学术量化"**。
2. 术语命源链更新：Trivedy 双文均为一手可得，且其身份与 LangChain 重合；"双命源"（Trivedy vs Hashimoto）仍成立。
3. 数字回改：NLH 采用 v2 数字（36.0→53.9 TB2）或回查 v1；Teleport "90 天"→"一个季度"；Stripe 日期→2026-02-09。
4. 新增收录：Teleport 的"复杂 harness 有害"负判据值得进 §4（成本/过度建设）一节；ETH Zurich agentfile 研究（arXiv 2602.11988，经 HumanLayer 转引）值得单独立卡。
