# Evidence 2026-09-27 · I 路批次 2 · 定量效果（P-outcome 候选）＋先进团队/evals 思想/谱系/SDD 组合扫描

- 观测日期：2026-09-27
- 时间窗：2023-07-02 → 2026-09-27（按各来源发布日期分别标注）
- 证据强度：研究报告官方页 / arXiv 官方页 / 厂商官方 docs·changelog·blog / 作者本人长文，逐字摘录；无二手编译充当原句
- **主验状态标注**：`【主验】`＝主 Agent 亲手 web_fetch 该页并逐字核对引句；`【侦察回源】`＝侦察 Agent 打开一手页面逐字摘录、主 Agent 未复验（引用前建议复验；两者都比「转引」强，但弱于主验）。
- 本档案回答：I 路批次 2 的五个互斥切口——(a) 厂商控制面剩余＋社区编排、(b) 验证与 evals 思想、(c) 定量效果、(d) 谱系背景实践者长文、(e) SDD×loop 厂商组合形态。批次划分与扩容纪律见 [`research-plan.md` §2.3](research-plan.md)；批次 1（簇外高影响面控制实践）见 [`evidence-2026-09-27-i-high-influence-control.md`](evidence-2026-09-27-i-high-influence-control.md)，本档案不重复其记录。
- 证据层级纪律：P-existence / P-mechanism / P-outcome 不互升；方向相反的定量结果必须成对引用；侦察发现的全部反例随各切口记录，不单设「正例集」。
- **融合状态**：这是一个批次归档，不是同质证据包。每个 Source 以 `【主验】` / `【侦察回源】` 标记；只有主验或后续独立复核的条目才能进入已确认判读，侦察条目只进入候选清单，不增加独立票、不关闭缺口、不升格为 P-outcome。
- 与既有材料关系：补 CURRENT 缺口 4（真实 P-outcome，此前为 0 来源）；补缺口 3（跨 feature 可见性——新增五家厂商控制面与社区编排形态）；补 P1.5（行为面验证——首次拿到原句级实践）；补 P1.6（自我改写保护链——首次拿到机制级保护清单）；补时间线 §四 谱系（Ball/Walden/Manus/Armin/Gauthier-2023）；补 E 路（Kiro/Tessl/Linear 厂商级一手，此前只有 OpenSpec/Spec Kit 开源侧）。
---

## 切口 I-2c · 定量效果（P-outcome 候选）

> 引用陷阱（本节三条，全部来自来源自身的官方表述）：
> ① METR 2025-07 RCT 必须与 2026-02-24 官方续测**成对引用**——RCT 页面顶部自标 "These results are out of date" 并指向续测；
> ② DORA 两份年度报告方向相反（2025-03 报告：吞吐 -1.5%；2025-09 年报：吞吐↑+不稳定↑），**年份口径必须标注**；
> ③ GitClear 的 4–10x 产出差必须带上其官方限定「大半先于 AI 存在、纵向自比仅 25%」。

### Source C1 · METR RCT：受控实验测得 19% 变慢，且开发者感知反向偏差 20 个百分点

- URL：https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ （arXiv 同研究：2507.09089）
- 发布日期：2025-07-10；作者：Joel Becker, Nate Rush, Beth Barnes, David Rein
- 访问/观测日期：2026-09-27【主验】
- 来源类型：研究机构官方博客（RCT 报告）
- 影响面依据：METR 是前沿模型自主能力评测的权威非营利机构；该研究被媒体与评测社区广泛引用（其自报偏差结论被 METR 2026-05 调查页回引为标准锚点）
- 原文摘录：
  > "We conduct a randomized controlled trial (RCT) to understand how early-2025 AI tools affect the productivity of experienced open-source developers working on their own repositories. Surprisingly, we find that when developers use AI tools, they take 19% longer than without—AI makes them slower."
  > "we recruited 16 experienced developers from large open-source repositories (averaging 22k+ stars and 1M+ lines of code) … Developers provide lists of real issues (246 total) … we randomly assign each issue to either allow or disallow use of AI … (primarily Cursor Pro with Claude 3.5/3.7 Sonnet—frontier models at the time of the study)"
  > "developers expected AI to speed them up by 24%, and even after experiencing the slowdown, they still believed AI had sped them up by 20%."
  > "Models slow down humans on 20min-4hr realistic coding tasks"
- 该摘录支持的最小主张：issue 级随机分配下，2025 年早期工具使 16 名资深 OSS 开发者在熟悉仓库上完成 246 个真实 issue 的耗时多 19%；感知偏差可量化（预期 +24%、事后自报 +20%，实测 -19%）。
- 不支持什么：作者官方 Table 2 明确列出——不证明"AI 对多数开发者无效"；不外推到其他场景/工具用法（"Cursor does not sample many tokens from LLMs, it may not use optimal prompting/scaffolding"）；页面顶部自标 "These results are out of date" 并指向 2026-02 续测。
- 与 loop 研究的关系：唯一针对「真实 issue＋熟悉仓库」场景的受控效果测量。其官方解释句——"AI capabilities may be comparatively lower in settings with very high quality standards, or with many implicit requirements (e.g. relating to documentation, testing coverage, or linting/formatting)"——与验证门设计直接相关，但**不构成对「设计好的 loop 更有效」的检验**（该研究没有对照不同 loop 设计）。

### Source C2 · METR 续测：方向反转的弱证据 ＋ 受控实验设计被选择效应击穿

- URL：https://metr.org/blog/2026-02-24-uplift-update/
- 发布日期：2026-02-24；作者：Joel Becker, Nate Rush, Tom Cunningham, David Rein, Khalid Mahamud
- 访问/观测日期：2026-09-27【主验】
- 来源类型：研究机构官方博客（同设计续测的方法学更新）
- 原文摘录：
  > "Our early 2025 study found the use of AI causes tasks to take 19% longer, with a confidence interval between +2% and +39%. For the subset of the original developers who participated in the later study, we now estimate a speedup of -18% with a confidence interval between -38% and +9%. Among newly-recruited developers the estimated speedup is -4%, with a confidence interval between -15% and +9%."
  > "we believe that the data from our new experiment gives us an unreliable signal of the current productivity effect of AI tools"
  > "30% to 50% of developers told us that they were choosing not to submit some tasks because they did not want to do them without AI"
  > "our measurements of time-spent on each task are unreliable for the fraction of developers who use multiple AI agents concurrently."
  > [图注] "Late-2025 AI likely accelerated open-source developers, but selection effects obscure the true speedup."
  > "Throughout 2025 there was an increase in the use of agentic tools among open-source developers, such as Claude Code and Codex."
- 该摘录支持的最小主张：2025-08 起续测（57 开发者/143 仓库/800+ 任务）原始估计方向反转为提速（原班子样本 -18%，符号按原文对照 2025 报告的正=变慢约定），但作者官方把该数据降级为不可靠信号；**选择效应本身是量化的一手事实**（30–50% 开发者拒绝提交不愿无 AI 做的任务）。
- 不支持什么：不能当"现在已提速 X%"的定量依据（"our data is only very weak evidence for the size of this increase"）；-18% 不得简化成"提速 18%"。
- 与 loop 研究的关系（关键）：**"多 agent 并发使用使耗时自报失效"是跨 feature 可见性缺口（P0.3）的第一条独立定量旁证**——工作组织从单 agent 变成并发 agent 群后，现有度量基础设施（人自报耗时）失效。

### Source C3 · METR 长任务：循环可承载的任务时长约 7 个月翻倍（能力趋势，非效果）

- URL：https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ （arXiv：2503.14499）
- 发布日期：2025-03-19；作者：Thomas Kwa, Ben West, Joel Becker 等 24 人（METR）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：研究机构官方博客（论文页）
- 原文摘录：
  > "We propose measuring AI performance in terms of the length of tasks AI agents can complete. We show that this metric has been consistently exponentially increasing over the past 6 years, with a doubling time of around 7 months."
  > "current models have almost 100% success rate on tasks taking humans less than 4 minutes, but succeed <10% of the time on tasks taking more than around 4 hours"
  > [页面横幅] "Some of the text and figures in this post are out of date. … the static figures and some claims in the text (e.g. the doubling time) reflect the state of the data at the time of original publication. For our latest methodology and results, see the dedicated time horizons page and Time Horizon 1.1."
  > [脚注 2] SWE-Bench Verified 口径倍增期更短（"under 3 months"），作者自注原因：该口径的人类时长估计不含熟悉代码库的时间
- 该摘录支持的最小主张：agent 可完成任务时长（按人类专家耗时折算，50% 可靠度）约 7 个月翻倍——支持"loop 能承载的任务长度在快速外推"的能力趋势陈述。
- 不支持什么：能力趋势度量，**不是开发者产出的受控效果测量**；7 个月是 2025-03 口径且页面自标部分过时（现行口径 Time Horizon 1.1，2026-01-29）。
- 证据层级：P-mechanism 级能力趋势；不进 P-outcome。

### Source C4 · DORA gen-AI 报告（2025-03）：采用 +25% 关联吞吐 -1.5%、稳定性 -7.2%，官方建议直指反馈环

- URL：https://dora.dev/ai/gen-ai-report/report/
- 发布日期：2025-03（报告）；页面 "Last updated: April 13, 2026"
- 访问/观测日期：2026-09-27【主验】
- 来源类型：DORA（Google Cloud）官方 key findings 页（报告 PDF 需下载，本页为官方摘要）
- 影响面依据：DORA 是交付效能研究的行业标准品牌（State of DevOps 系列），Google Cloud 官方项目
- 原文摘录：
  > "AI currently hurts software delivery performance: Contrary to expectations, a 25% increase in AI adoption is associated with a 1.5% decrease in delivery throughput and a 7.2% decrease in delivery stability. Because AI allows developers to generate code much faster, it often leads to larger batch sizes, which are slower to review and more prone to creating system instability."
  > "Surprisingly, AI adoption leads to developers spending less time on valuable work, while time spent on toilsome, repetitive tasks remains unchanged."
  > "39% of developers still trust AI outputs 'a little' or 'not at all'"
  > "Double-down on fast, high-quality feedback loops: Because AI can rapidly generate large amounts of code, organizations must reinforce safeguards like automated testing and fast code reviews. Continuous integration helps catch AI-introduced errors before they reach production, fostering a virtuous cycle of trust and reliability."
- 该摘录支持的最小主张：组织级调查关联（+25% 采用 → 吞吐 -1.5% / 稳定性 -7.2%）；机制解释把不稳定归因于**更大批量使 review 变慢**；官方对策一节明确把「快而高质量的反馈环＋自动化测试＋快速 review」写成组织对策。
- 不支持什么：观测性关联非受控因果；系数来自官方摘要页，报告 PDF 全文本轮未取（正文系数核对待补）。
- 与 loop 研究的关系（关键）：**组织级数据对「验证环设计」的直接背书**——DORA 把 AI 时代交付不稳定的对策明确写成 feedback loop 工程。实践层 loop_governance 可引用（标注：关联证据非受控）。

### Source C5 · DORA 2025 年报（2025-09）：方向部分反转——吞吐↑但不稳定↑，"amplifier" 定位

- URL：https://dora.dev/research/2025/dora-report/ （落地页，【主验】其定位句）；具体系数页 https://dora.dev/insights/dora-2025-year-in-review/ 与 https://dora.dev/insights/balancing-ai-tensions/ 【侦察回源】
- 发布日期：2025-09（年报）；引句页 2026-01-07 / 2026-03-10
- 来源类型：官方摘要/年度回顾页（报告全文 gated 于 cloud.google.com/dora）
- 原文摘录（落地页，主验）：
  > "The State of AI-assisted Software Development report reveals AI's primary role is as an amplifier, magnifying an organization's existing strengths and weaknesses."
- 原文摘录（侦察摘录，待主验）：
  > "We found that AI improves throughput, but often at the cost of stability if your foundation isn't solid."（dora-2025-year-in-review）
  > "90% of technology professionals now use AI at work, and over 80% believe it has increased their productivity … higher AI adoption is associated with an increase in both software delivery throughput and software delivery instability … 30% of developers currently report little to no trust in the code generated by AI"（balancing-ai-tensions）
- 该摘录支持的最小主张：2025 年报口径 = 吞吐↑＋不稳定↑＋"amplifier"；90% 采用为该年官方口径。
- 不支持什么：具体系数未取得（全文 gated）；与 C4 的方向差必须按年份标注，不得混用。
- 证据层级：P-outcome（关联级，官方摘要口径）。

### Source C6 · GitClear「Write-Only Mode」（2026）：623M 变更的质量信号劣化 ＋ 4–10x 的官方限定句

- URL：https://www.gitclear.com/write_only_mode_ai_research （2025 前篇：https://www.gitclear.com/ai_assistant_code_quality_2025_research ）
- 发布日期：页面未标（数据窗口 2023–2026 YTD；abstract 自引前篇为 "Feb 2025"、"Jan 2026"）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：厂商研究落地页（白皮书全文 gated，本页含摘要与主要数字）。注意：**厂商自营研究**，有产品卖点相关性。
- 原文摘录：
  > "The data shows a 74% drop in long-term legacy updates and a 70% collapse in refactoring moves since 2023."
  > "a concerning rise in within-commit copy/paste (+41%), code block duplication (+81%), error-masking constructs (+47%), and two-week code churn (+15%)."
  > "block duplication climbed from 40.3 in 2023 to 73.0 year-to-date in 2026 — an 81% increase over 2023 and the highest level on record"
  > "the percentage of moved code dropped to 13% of changed lines in 2023, before freefalling to 3.8% year-to-date in 2026. Over the same window, copy/paste climbed from 9.4% (in 2022) to 15.7% in the first half of 2026"
  > "AI Coding Tools Attract Top Performers (Jan 2026) showed that heavy AI users out-produce non-users by 4–10x, but most of that gap pre-dated AI — compared to their past selves, heavy AI users enjoyed a more modest 25% velocity gain."
  > "The headline is not 'AI writes bad code.' It is that today's default AI workflow is incentivized to deliver atomic code — a happy-path, a passing test, a closed ticket — while quietly taxing the invisible and the deferred: the reuse, consolidation, and error-surfacing that determine how expensive a codebase is to own in year three."
  > [2026 abstract 转述 2025 报告] "2024 was the first year on record where within-commit copy/paste exceeded 'moved' (refactored) code, and that commits containing a duplicated block rose roughly 10x over two years."
- 该摘录支持的最小主张：2023–2026 观测性质量信号全向劣化；产出差有官方限定（4–10x 横截面差距大半先于 AI，纵向自比仅 25%）。
- 不支持什么：纯观测性、无对照、不可归因；"25% velocity gain" 是厂商自述解读。
- 与 loop 研究的关系（关键）：**"a happy-path, a passing test, a closed ticket" 是对「机械停止条件通过 ≠ 做了该做的事」（行为面验证缺口 P1.5）最精确的厂商级概括**——测试门＋票据关闭恰是当前 loop 的默认停止形状，质量债在它拦不住的地方累积。

### Source C7 · Peng et al. 2023：Copilot 受控实验 55.8% 提速（greenfield 场景，与 METR 成互补对）

- URL：https://arxiv.org/abs/2302.06590
- 发布日期：2023-02-13（arXiv 提交）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：arXiv 论文摘要页；作者为 GitHub/Microsoft 系（Peng, Kalliamvakou, Cihon, Demirer）
- 原文摘录：
  > "This paper presents results from a controlled experiment with GitHub Copilot, an AI pair programmer. Recruited software developers were asked to implement an HTTP server in JavaScript as quickly as possible. The treatment group, with access to the AI pair programmer, completed the task 55.8% faster than the control group."
- 该摘录支持的最小主张：单一、短时、greenfield 任务的受控实验中治疗组快 55.8%。
- 不支持什么：不能外推到维护型/熟悉代码库工作（METR C1 恰在该场景测得反向）；2023 年工具代际（前 agent 化）；产品方研究。
- 与 loop 研究的关系：与 C1 构成**场景互补对**——"AI 提效"与"AI 变慢"都是真的，分界变量是任务类型/场景/工具代际。任何"效果"结论必须成对引用。

### 切口 I-2c 判读

1. **缺口 4 的表述修正**：「真实 P-outcome 完全缺失」不再准确。当前有一批受控/大样本定量证据：METR RCT（-19%，早期工具、维护场景）、Peng RCT（+55.8%，greenfield、2023 代际）、DORA 关联（-1.5%/-7.2% → 吞吐↑不稳定↑）、GitClear 观测（质量劣化＋4–10x/25% 限定）。**它们方向不一，方向差与场景、任务类型、工具代际强相关**——这是 loop 研究的核心发现候选：效果问题不是"AI 有没有用"，而是"什么样的 loop/验证设计在哪个场景提效"。
2. **P-outcome 的时效性极差**：METR 官方 12 个月内两度更新口径；DORA 两年度方向反转。任何效果引用必须带观测日期与版本，2025 年的数字不能默认适用于 2026 年的工具。
3. **可观察性缺口获得定量旁证**：多 agent 并发使耗时自报失效（C2 官方原句）——外层调度研究与 DSH 实验设计必须把「并发 agent 的度量方法」当作一等问题。
4. **验证环获得组织级背书**：DORA 官方对策句（C4）把 feedback loop/自动化测试/快速 review 写成 AI 时代的交付稳定条件——practice 层可引用（标注：关联证据非受控）。

---

## 切口 I-2a · 厂商控制面剩余（Agent HQ / Jules / Antigravity / Cursor / Devin / 社区编排）

### Source A1 · Cursor Projects：feature 级 coordinator 控制面（当前最接近「统一 ledger」的厂商形态）

- URL：https://cursor.com/blog/projects
- 发布日期：2026-09-10（Sep 10, 2026；作者 Alexi Robbins & Fredrika Lindh）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：厂商官方博客（产品发布文）
- 原文摘录：
  > "Today we're launching Projects in Cursor. Projects lets you take on larger bodies of work, such as a feature, a migration, or a full app. It maintains context over months of work, delegates tasks to thousands of subagents, and performs recurring work without being prompted."
  > "You oversee a Project by chatting with its coordinator agent. The coordinator doesn't write code itself but directs other agents that do. Because it delegates rather than executes, it is never blocked and is always responsive to direction."
  > "**Shared context.** … Each Project maintains a set of files that sync across every cloud and local machine its agents use. Agents add research and artifacts, along with what they learn about the codebase and how you prefer work to be done. … This context grows with the Project, making the coordinator more effective over time."
  > "**Subscriptions.** The coordinator can watch a Slack channel, run on a schedule, or follow all your PRs, fixing CI and acting when they open or merge."
  > [迁移场景] "Early on, you review each PR closely. As the fixes hold up, you review less, and the coordinator keeps working through the migration on its own."
  > [gardening 场景] "the coordinator scans every new PR, extracts components that belong in the design system, and adds a lint rule whenever it sees the same mistake twice."
  > "We've found it to be a substantial productivity multiplier: new users merge 30% more PRs while users who primarily use Projects merge six times as many."
  > "Projects are available in beta and rolling out to all users starting today."
- 该摘录支持的最小主张：厂商产品化「feature 级控制面」——coordinator 只派发不执行、共享上下文跨会话/跨 agent 沉淀、订阅式事件触发、并行派发。迁移场景给出**放权递减曲线**（随验证通过率上升而降低 review 频率），gardening 场景给出**同类错误两次即固化成 lint 规则**的自改写环厂商实现。
- 不支持什么：30%/6x 为厂商自报、无方法学；无授权历史/优先级/业务阻塞字段；beta 状态。
- 证据层级：P-mechanism；产出数字若引用为 P-outcome 须标 vendor-reported。

### Source A2 · Google Antigravity：agent-first Manager surface ＋ Artifacts ＋ 四支柱（含 self-improvement）

- URL：https://antigravity.google/blog/introducing-google-antigravity
- 发布日期：2025-11-18（The Antigravity Team）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：厂商官方博客（产品发布文，public preview）
- 原文摘录：
  > "Antigravity is our first product that brings four key tenets of collaborative development together: trust, autonomy, feedback, and self-improvement."
  > "we are introducing an agent-first Manager surface, which flips the paradigm of agents being embedded within surfaces to one where the surfaces are embedded into the agent. You can think of it like a mission control for spawning, orchestrating, and observing multiple agents across multiple workspaces in parallel."
  > "Antigravity provides context on agentic work at a more natural task-level abstraction, with the necessary and sufficient set of artifacts and verification results, for the user to gain that trust."
  > "As the agent works, it produces Artifacts, tangible deliverables in formats that are easier for users to validate than raw tool calls, such as task lists, implementation plans, walkthroughs, screenshots, and browser recordings."
  > [feedback] "An agent being able to complete 80% of the work should be useful, but if there is no easy way to provide feedback, then it becomes more work than benefit to resolve the remaining 20%."
  > [self-improvement] "Antigravity treats learning as a core primitive, with agent actions both retrieving from and contributing to a knowledge base."
- 该摘录支持的最小主张：「agent manager」范式的官方命名与定义（多 agent/多 workspace 并行 mission control）；task 级抽象的验收点以 Artifacts＋验证结果供人核验；把 learning 列为核心原语（知识库回注）。
- 不支持什么：组织级优先级/审批历史/业务阻塞；"必要且充分的 artifacts" 是设计主张非使用证据。
- 证据层级：P-mechanism。

### Source A3 · GitHub Mission Control：集中任务视图 ＋ real-time steering

- URL：https://github.blog/changelog/2025-10-28-a-mission-control-to-assign-steer-and-track-copilot-coding-agent-tasks/
- 发布日期：2025-10-28
- 访问/观测日期：2026-09-27【主验】
- 来源类型：GitHub 官方 changelog
- 原文摘录：
  > "We've redesigned how you manage your Copilot coding agent tasks on github.com. Instead of jumping between pages to track progress, monitor changes, and manage tasks, everything you need now lives in one streamlined, centralized view."
  > "With real-time steering, you can guide Copilot as it's working. Provide input while a session runs, and Copilot will adapt as soon as its current tool call completes."
  > "Switch between tasks effortlessly with the new task view. See task status at a glance and jump in when Copilot needs your input. Quick links on the task make it easy to navigate straight to the pull request."
- 该摘录支持的最小主张：跨任务集中视图＋会话中途实时转向（steering 在当前工具调用完成后生效）；任务状态一览＋人工介入点（"jump in when Copilot needs your input"）。
- 不支持什么：该日期仍是单一 Copilot agent 的任务总览，非多厂商面板（那是同日 Agent HQ 宣告，且为 roadmap）；无优先级/授权历史/业务阻塞字段。
- 证据层级：P-mechanism。

### Source A4 · GitHub Agent HQ 宣告 ＋ 企业 agent 控制面（侦察回源）

- URL：https://github.blog/jp/2025-10-29-welcome-home-agents/ （英文正源三次抓取被导航壳截断；机制句以同日两份英文 changelog 为英文原样证据）＋ https://github.blog/changelog/2025-10-28-enterprise-ai-controls-the-agent-control-plane-are-in-public-preview/ ＋ https://github.blog/changelog/2025-08-19-agents-panel-launch-copilot-coding-agent-tasks-anywhere-on-github-com/
- 发布日期：2025-08-19（Agents panel）/ 2025-10-28（enterprise control plane）/ 2025-10-29（Agent HQ）
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句（enterprise control plane，英文）：
  > "This is your agent control plane, a suite of enterprise governance features designed to give organizations deeper control over how agents operate across their environments."
  > "See enterprise-wide agent sessions for the last 24 hours. Filter on agent type and the task state (e.g., completed, cancelled, in progress)."
  > "New fields for agent activity (e.g., `pull_request.create` executed by Copilot): Identify an `actor_is_agent`. Show `user` and `user_id` to identify who the agent is acting on behalf of. A new event for `agent_session.task` shows which sessions have started, finished, or failed to complete."
- 关键引句（Agent HQ，官方日文本地化版）：多厂商 agent（Anthropic/OpenAI/Google/Cognition/xAI）经 Copilot 订阅接入 GitHub、Mission Control 多 agent 并行派发、企业 agent 治理层——**路线图承诺**（"今後数か月以内に"）。
- 最小主张：企业级 agent 审计控制面存在（public preview）：组织级 session 视图（仅近 24h）、`actor_is_agent` 归属字段、`agent_session.task` 生命周期事件。Agents panel（2025-08-19）为全站任务派发/状态列表的起点。
- 不支持什么：审计面不是产品团队任务板；24h 窗口明示；宣告≠已上线。
- 证据层级：P-mechanism（控制面）/ P-existence（Agent HQ 路线图）。

### Source A5 · Google Jules：计划审批门 ＋ 单任务验收总览（侦察回源）

- URL：https://jules.google/docs/ 、https://jules.google/docs/tasks-repos/ 、https://jules.google/docs/code/
- 发布日期：unknown（活文档）
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > "Once you submit a task, Jules will generate a plan. You can review and approve it before any code changes are made. … You are free to leave Jules while it is running. … You'll be notified when the task completes or needs your input."
  > "You can launch multiple tasks at a time to run them simultaneously. … Each task runs in its own virtual machine and maintains its own logs, environment setup, and code changes. … You will have to navigate to the task to check for updates, approve the plan, etc."
  > "When the task completes, Jules provides a final summary which includes: ✅ Files changed ⏱ Total runtime ➕ Lines of code added/changed 🌿 Branch name and commit message. … Click Publish branch or Publish PR to push Jules' changes to GitHub"
- 最小主张：异步任务模型＝计划审批门（人批后才动代码）→ 运行期可离开 → 完成或需输入时通知召回；并发任务每任务独立 VM；单任务验收总览（变更/耗时/行数/分支）＋PR 交接。
- 不支持什么：全程个人视角——无团队/组织总览、优先级、审批历史、业务阻塞；查进度需人工导航到该任务（**反例：有任务列表 ≠ 有跨 feature 组织控制面**）。
- 证据层级：P-mechanism。

### Source A6 · Cursor 控制面演进线 ＋ Devin managed Devins（侦察回源）

- URL：https://cursor.com/changelog/1-0 （2025-06-04）· https://cursor.com/changelog/cloud-in-agents-window （2026-06-17）· https://cursor.com/changelog/08-19-26 （2026-08-19）· https://cognition.com/blog/devin-can-now-manage-devins （2026-03-19）
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句（Cursor 2026-08-19）：
  > "cloud agents can automatically pick up work in response to events, hold a goal until it's met, and stay on course through long-running sessions. … Cursor can now monitor your PRs, watch a Slack thread, or run scheduled tasks. … Use `/goal` to give the agent a long-lived objective to work towards until it's fully complete."
- 关键引句（Devin 2026-03-19）：
  > "The main Devin session acts as a coordinator: it scopes the work, assigns each piece to a managed Devin, monitors progress, resolves any conflicts, and compiles the results. … Monitor ACU consumption: track how much compute each child session is using - Put child sessions to sleep or terminate them"
- 最小主张：Cursor 控制面三级演进（个人快捷键面板 2025-06 → Agents Window 并发云子代理/babysit PR 2026-06 → 事件驱动＋/goal 长期目标 2026-08 → Projects coordinator 2026-09）；Devin 分层委派（主 Devin 协调、子 session 独立链接可人审/可计量/可终止）。Cursor 的 `/goal` 与 Anthropic Claude Code 的 `/goal` 同名不同实现，不能互证。
- 不支持什么：无审批门/授权历史/优先级/跨 feature 验收总览；Devin 文档 docs.devin.ai 被壳层截断未回源。
- 证据层级：P-mechanism。

### Source A7 · 社区编排工具三样本（侦察回源；机制证据，不入 KOL 台账）

- URL：https://github.com/BloopAI/vibe-kanban ＋ https://www.vibekanban.com/blog/shutdown （2026-04-10）· https://www.conductor.build/docs/concepts/parallel-agents · https://raw.githubusercontent.com/smtg-ai/claude-squad/main/README.md
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > [vibe-kanban README] "Plan with kanban issues — create, prioritise, and assign issues on a kanban board; Run coding agents in workspaces — each workspace gives an agent a branch, a terminal, and a dev server; … Switch between 10+ coding agents"
  > [vibe-kanban shutdown] "Today we're shutting down bloop, the company behind Vibe Kanban. The Vibe Kanban project will live on, open source and community maintained. … We launched in June 2025 and were the first to ship multi-agent support, diff commenting, live preview"
  > [Conductor] "Parallel agent work starts with one decision: should these agents share a workspace, or should they move independently? … For issue fanout, use multiple workspaces. Create one workspace per GitHub or Linear issue … then review and merge the branches that are worth keeping."
  > [Claude Squad] "Claude Squad is a terminal app that manages multiple Claude Code, Codex, Gemini (and other local agents including Aider) in separate workspaces … 1. tmux to create isolated terminal sessions for each agent 2. git worktrees to isolate codebases"
- 最小主张：社区层控制面形态＝看板/优先级（vibe-kanban）、workspace 共享-vs-隔离决策指南（Conductor）、tmux+worktree 终端层隔离（Claude Squad）；隔离单位一致收敛到「分支/worktree」。
- 生命周期反例：vibe-kanban 公司 2026-04-10 关停（云端看板/组织/评论服务下线退回本地）——独立社区控制面工具商业模式失败的单样本。
- 证据层级：P-mechanism（vibe-kanban shutdown 为 P-outcome 级生命周期结局，vendor-reported）。

### 切口 I-2a 判读（对准 P0.3 跨 feature 可见性缺口）

| 控制面形态 | 样本 | 有 | 仍无（对准缺口） |
|---|---|---|---|
| 任务面板/列表 | GitHub Agents panel、Jules、Cursor 1.0 | 派发＋状态＋单任务验收 | 优先级/授权史/阻塞/聚合验收 |
| 集中视图＋steering | GitHub Mission Control | 跨任务一览、运行中转向 | 字段级 ledger（priority/授权史） |
| 企业审计控制面 | GitHub agent control plane | 组织级 session 视图（24h）、agent 身份归属、生命周期事件 | 审批工作流（只有 audit log） |
| agent manager ＋ Artifacts | Antigravity Manager surface | 多 agent 并行观察、task 级 artifacts＋验证结果 | 候选任务来源机制、组织优先级 |
| project 原语 | Antigravity project（设置/资源/权限三轴）、Cursor Projects | 把权限/资源/行为按项目收敛作用于全部 agent；feature 级 coordinator＋共享上下文 | 授权历史、优先级、业务阻塞、跨 feature 验收总览 |
| 分层委派 | Devin managed Devins | 主 agent 协调、子 session 可人审/计量/终止 | session 级而非 feature 级 |
| 社区看板/编排 | vibe-kanban、Conductor、Claude Squad | 看板/优先级、workspace 决策指南、分支隔离 | 组织层；商业模式脆弱（vibe-kanban 关停） |

**结论（只写到证据支持的粒度）**：五家厂商＋三个社区样本确认了控制面的**形态谱系**（面板 → 集中视图 → 审计面 → manager/project/coordinator），其中 **Cursor Projects（2026-09-10）是目前最接近 feature-level ledger 的公开形态**（feature 级 coordinator＋跨会话共享上下文＋订阅触发）。但**没有任何一家提供统一 feature-level 的候选/授权历史/优先级变化/业务阻塞/跨 feature 验收总览**——缺口 3 在扩大样本后依然成立，且现在可以说得更精确：厂商收敛在「把权限按项目收敛」与「把状态按 session/任务呈现」，缺的是「把授权与验收按 feature 记账」。

---

## 切口 I-2b · 验证与 evals 思想（Q2.4 验证分界 · P1.5 行为面 · P1.6 自我改写保护链）

> 本切口人物（Hamel Husain / Shreya Shankar / Eugene Yan / Chip Huyen / GEPA·DSPy·AlphaEvolve 研究侧）**均未对 "loop engineering" 本词发声**，按 §2.3 纪律作为**证据来源**登记，不进 KOL 台账。

### Source B1 · Eugene Yan《How to Work and Compound with AI》：verification ladder ＋ execution/direction drift 二分 ＋ transcript 挖掘回写

- URL：https://eugeneyan.com/writing/working-with-ai/
- 发布日期：2026-05（页面引注 "Yan, Ziyou. (May 2026)"）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：作者本人长文（Eugene Yan，Anthropic MTS，站点自述订阅 11,800+）
- 原文摘录：
  > "**Shift verification left; catch errors at write time.** I think of verification as a ladder. The bottom is cheap and deterministic; the top is expensive and requires judgement. We want to address issues at the lowest possible rung. Near the bottom are post-edit hooks that run `ruff format`, `ruff check --fix` … Higher on the ladder are tests, evals, LLM reviews, etc."
  > "**For long-running tasks, have models watch models.** Long sessions can drift as errors build up. One fix is to run a secondary session with fresh context to read the original spec and the recent turns of the primary session."
  > "the pair programmer can watch for **execution drift**—is the model doing the task right? This is local and tactical, like ignoring an error, reporting a bad metric, or diverging from the spec. There's also **direction drift**—is the model doing the right task? These are bigger picture and strategic … Check for execution drift often and direction drift occasionally."
  > "You can't delegate what you can't verify, so this requires first defining success criteria and metrics."
  > "**Mine your transcripts for config updates.** Have the model read past session transcripts to find gaps. When I scanned ~2,500 of my past user turns, a sizable percentage contained phrases like _'can you also…'_, _'did you check…'_, _'still wrong'_, etc. … Hit counts show how often a correction happens and the transcripts show exactly what failed."
  > "**Refactor and prune periodically.** As configs grow, they can overlap or conflict with each other. As a result, if the model ignores a rule, it can be because another rule contradicts it."
- 该摘录支持的最小主张：①验证分层判据（确定性→测试/evals/LLM review，成本梯度＋"能在最低档解决就不上推"）；②**行为面验证的原句**——execution drift（做得对不对，常查）vs direction drift（做的事对不对，偶查），实现为 fresh-context 第二会话对照 spec 与主会话轨迹；③授权委托以可验证性为前提；④自我改进入口（transcript 修正短语挖掘→回写 config/skill→周期性重构防规则冲突）。
- 不支持什么：个人工作流，无量化收益与失败率；ladder 无各档实测。
- 证据层级：P-mechanism。

### Source B2 · Hamel Husain：三级评测金字塔 ＋ judge 校准方法论（侦察回源）

- URL：https://hamel.dev/blog/posts/evals/ （2024-03-29）· https://hamel.dev/blog/posts/llm-judge/ （2024-10-29，页面标注 Modified 2026-09-01）
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > "There are three levels of evaluation to consider: Level 1: Unit Tests; Level 2: Model & Human Eval (this includes debugging); Level 3: A/B testing. The cost of Level 3 > Level 2 > Level 1. This dictates the cadence and manner you execute them."
  > "Model-based evaluation is a meta-problem within your larger problem. You must maintain a mini-evaluation system to track its quality."
  > "You might not even need a LLM judge for some errors (and use a code-based assertion instead)."
  > "Validating an automated judge needs a larger labeled set. Aim for about 100 examples per failure mode … Below 60 examples, the confidence intervals are often too wide to support a useful conclusion."
  > "Raw agreement can be misleading when classes are imbalanced. Treat the human labels as ground truth and report the judge's True Positive Rate and True Negative Rate separately."
- 最小主张：验证分层的**成本×节奏**版判据；LLM-as-judge 是需要被再验证的"元问题"（mini-eval、~100 例/失败模式、TPR/TNR 而非 raw agreement）；能写断言就用断言。
- 不支持什么：无跨团队对照数据；>90% agreement 案例为单一咨询客户自述。
- 证据层级：P-mechanism（judge 校准流程）；>90% 案例为 P-outcome（单案例自报）。

### Source B3 · Shankar et al.《Who Validates the Validators?》（arXiv 2404.12272）：criteria drift ＋ judge 继承被评 LLM 的问题（侦察回源）

- URL：https://arxiv.org/abs/2404.12272
- 发布日期：2024-04-18；UC Berkeley 等（Shankar, Zamfirescu-Pereira, Hartmann, Parameswaran, Arawjo）
- 访问/观测日期：2026-09-27【侦察回源（摘要级）】
- 关键引句：
  > "Yet LLM-generated evaluators simply inherit all the problems of the LLMs they evaluate, requiring further human validation."
  > "we identify a phenomenon we dub criteria drift: users need criteria to grade outputs, but grading outputs helps users define criteria. What is more, some criteria appears dependent on the specific LLM outputs observed (rather than independent criteria that can be defined a priori), raising serious questions for approaches that assume the independence of evaluation from observation of model outputs."
- 最小主张：LLM judge 不能自我背书（需人工验证）；**criteria drift 对"固定 rubric 爬山"类自我改进循环的独立性假设构成论文级质疑**。
- 不支持什么：定性 HCI 研究（单接口、少数被试），不证明此类循环必然退化。
- 证据层级：P-existence（主张）＋ P-outcome（定性发现）；是 P1.6 的关键反例来源。

### Source B4 · Shreya Shankar《In defense of AI evals》：何时可以少验（侦察回源）

- URL：https://www.sh-reya.com/blog/in-defense-ai-evals/
- 发布日期：2025-09-05
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > "there are two main situations where you can get away with lighter processes. The first is when your task is already well represented in posttraining ... The second is when you and your team have enough domain expertise and taste to rely on your own dogfooding—and are religious about continuously dogfooding. ... evals live on a spectrum."
- 最小主张：验证降档的边界条件（posttraining 覆盖充分 / 团队品味＋持续 dogfood）——与"验证成本分级"互为补充。
- 不支持什么：边界条件为经验判断，无覆盖率度量。
- 证据层级：P-mechanism。

### Source B5 · Eugene Yan 评测流程两篇：judge 校准判据 ＋ 人本身就是噪声基准（侦察回源）

- URL：https://eugeneyan.com/writing/eval-process/ （2025-04-20）· https://eugeneyan.com/writing/product-evals/ （2025-11-23）
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > "Human oversight is still needed even with automated evaluators (aka LLM-as-judge). … we can calibrate automated evaluators to align with human judgment. This could mean measuring recall or precision on binary labels, or correlation when deciding between outputs via pairwise comparisons."
  > "I often see human inter-rater reliability (Cohen's Kappa) being as low as 0.2 - 0.3. And human annotators can miss as many as 50% of the defects due to fatigue … Thus, if our LLM-evaluator achieves higher recall and consistency than human annotators, I'd consider that a success. … We should treat this as a conventional machine learning problem and split the data into development and test sets."
  > "This cycle—write evals, make changes, run evals, integrate improvements—ensures measurable progress."
- 最小主张：judge 校准闭环（precision/recall/pairwise）＋ judge 自身按 ML 惯例切 dev/test 防过拟合＋每次配置变更都跑 eval harness（回归评估）；"人工金标准"本身不稳定（Kappa 0.2–0.3 为作者个人观察，不可当普适统计量）。
- 证据层级：P-mechanism。

### Source B6 · Chip Huyen（AI Engineering·Agents 章）：plan 验证启发式 ＋ false completion 失败模式（侦察回源）

- URL：https://huyenchip.com/2025/01/07/agents
- 发布日期：2025-01-07（书籍章节官方改编）
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > "planning should be decoupled from execution. You ask the agent to first generate a plan, and only after this plan is validated is it executed. … one simple heuristic is to eliminate plans with invalid actions. … Another simple heuristic might be eliminating all plans with more than X steps. A plan can also be validated using AI judges. … If a plan involves risky operations, such as updating a database or merging a code change, the system can ask for explicit human approval … To make this possible, you need to clearly define the level of automation an agent can have for each action."
  > "Compound mistakes: an agent often needs to perform multiple steps … If the model's accuracy is 95% per step, over 10 steps, the accuracy will drop to 60%, and over 100 steps, the accuracy will be only 0.6%."
  > "An interesting mode of planning failure is caused by errors in reflection. The agent is convinced that it's accomplished a task when it hasn't."
  > "To evaluate an agent, identify its failure modes and measure how often each of these failure modes happens. … Always print out each tool call and its output so that you can inspect and evaluate them."
- 最小主张：plan 级验证判据（确定性启发式 → AI judge → 高风险操作人工批准）＋**按动作定自主度等级**的明确表述；**false completion**（agent 自评完成而实际未完成）作为行为面失败模式的一手命名；失败模式应作为指标分别测量。
- 不支持什么：95%→60% 为示意算术；无各失败模式发生率实测。
- 证据层级：P-mechanism（false completion 为经验观察 P-existence）。

### Source B7 · 自我改进循环的研究侧＋官方文档：GEPA / DSPy / AlphaEvolve（侦察回源）

- URL：https://arxiv.org/abs/2507.19457 （GEPA，2025-07-25 v1，ICLR 2026 Oral）· https://dspy.ai/current/diving-deeper/gepa-in-depth/ · https://arxiv.org/abs/2506.13131 （AlphaEvolve，DeepMind，2025-06-16）
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > [GEPA] "GEPA samples trajectories (e.g., reasoning, tool calls, and tool outputs) and reflects on them in natural language to diagnose problems, propose and test prompt updates, and combine complementary lessons from the Pareto frontier of its own attempts. … GEPA outperforms GRPO by 6% on average and by up to 20%, while using up to 35x fewer rollouts."
  > [DSPy 官方文档] "Reflection is the proposal mechanism, not the evaluation mechanism. … GEPA tracks every candidate it ever proposed, with per-example scores. … the frontier is for exploration; the aggregate is for selection. … detailed_results is the audit trail"
  > [DSPy 官方文档·退化反例] "A plain-float metric still works, but the proposer sees only a generic 'This trajectory got a score of {n}' caption … GEPA doesn't error on a float; it just gives you a much weaker version of itself."
  > [AlphaEvolve] "The LLM-directed evolution process is grounded using code execution and automatic evaluation. … Since AlphaEvolve tackles problems with machine-gradeable solutions, the user must provide a mechanism for automatically assessing generated solutions. … While the use of an automated evaluation metric offers AlphaEvolve a key advantage, it is also a limitation—in particular, it puts tasks that require manual experimentation out of our scope."
- 最小主张：P1.6「trace→改写 prompt/harness」的研究侧保护链清单——**①提案与评估分离（reflection 只提案、验证集评分）；②population/Pareto 档案保留历史最优（可回退）；③预算上限；④全量谱系留痕（版本化/审计）；⑤周期性全量回归**；AlphaEvolve 给出适用域硬边界（machine-gradeable solutions only，官方自认）。
- 关键反例（官方承认）：反馈通道退化（metric 只返回裸分数）时循环**静默**退化为弱化版自身——失效不报错。
- 实践-研究张力（两处一手，未裁决）：Hamel 自述 "I haven't had much luck with prompt optimizers like DSPy"（手动调 prompt）vs GEPA/DSPy 官方主张。
- 证据层级：P-outcome（论文自报）＋ P-mechanism（文档保护机制）。

### Source B8 · Anthropic《Writing tools for agents》：verifier 谱系 ＋ raw transcripts 原则（侦察回源）

- URL：https://www.anthropic.com/engineering/writing-tools-for-agents
- 发布日期：2025-09-11
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > "Your verifier can be as simple as an exact string comparison between ground truth and sampled responses, or as advanced as enlisting Claude to judge the response. Avoid overly strict verifiers that reject correct responses due to spurious differences like formatting, punctuation, or valid alternative phrasings."
  > "for each prompt-response pair, you can optionally also specify the tools you expect an agent to call … However, because there might be multiple valid paths to solving tasks correctly, try to avoid overspecifying or overfitting to strategies."
  > "We relied on held-out test sets to ensure we did not overfit to our 'training' evaluations. … Review the raw transcripts (including tool calls and tool responses) to catch any behavior not explicitly described in the agent's CoT."
- 最小主张：verifier 双向警告（过严误杀/过松漏放）；行为面以**轨迹为准而非自我陈述为准**（看 raw transcripts 抓 CoT 未陈述的行为）；held-out 防过拟合。
- 证据层级：P-mechanism。

### 切口 I-2b 判读

1. **Q2.4（deterministic / LLM-judge / human 的分界）现在有一组成熟的一手判据**：成本×节奏分层（Hamel 三级）、verifier 谱系＋双向警告（Anthropic）、plan 级三段判据（Chip）、judge 需被再验证（mini-eval/100 例/TPR-TNR，Hamel；precision-recall 校准，Eugene）、降档边界（Shreya）。共同核心：**确定性门最便宜必跑、judge 是需要校准与回归评估的元系统、人不可完全退出**。
2. **P1.5（行为面验证）拿到原句级实践**：Eugene 的 execution/direction drift 二分＋fresh-context 对照会话；Chip 的 false completion 命名；Anthropic 的 raw-transcripts 原则；GitClear 的 "passing test, closed ticket" 概括。四条独立来源同指：**行为面必须看轨迹，且需要与 spec/意图对照的第二视角**。
3. **P1.6（自我改写保护链）首次成清单**：提案/评估分离、Pareto 档案可回退、预算上限、审计谱系、周期回归（DSPy/GEPA）；held-out（Anthropic）；dev/test 切分（Eugene）；规则冲突周期重构（Eugene）。反面：criteria drift（Shankar，评测标准被观察输出反向重塑）＋静默退化（DSPy 官方）＋错误放大风险（Horthy/I-1 的 80% 叙事）。
4. 与已覆盖 Runkle 四环的 grader 二分（deterministic/agentic）关系：**相容但更细**——本切口把"agentic grader"展开为需要校准/回归/防过拟合的被评系统，且给出了"何时可以少验"的边界。这批材料进 `digested/03` 或新议题时按问题组织，不并入 Runkle 口径。

---

## 切口 I-2d · 谱系背景实践者长文（2026-06 命名前）

### Source D1 · Thorsten Ball《How to Build an Agent》：机制本体最短表述（⚠️ 一手标题非《How to Build a Coding Agent》）

- URL：https://ampcode.com/notes/how-to-build-an-agent
- 发布日期：2025-04-15（页面署名 "Thorsten Ball // April 15, 2025"；HN 同日提交同为 "How to Build an Agent"）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：作者本人长文（Amp/Sourcegraph；Ball 为 Amp co-creator、《Writing An Interpreter In Go》作者）
- 原文摘录：
  > "It seems like it would be. When you look at an agent editing files, running commands, wriggling itself out of errors, retrying different strategies - it seems like there has to be a secret behind it. There isn't. It's an LLM, a loop, and enough tokens."
  > "You can do it in less than 400 lines of code, most of which is boilerplate."
  > "What's an agent? Here's [my definition]: an LLM with _access to tools_, giving it the ability to modify something outside the context window."
  > "(Yes, there is a loop in a loop, but it doesn't matter.)"
- 该摘录支持的最小主张：**"agent = LLM＋loop＋tokens" 的传播源头文本之一（2025-04，早于命名 14 个月）**——机制本体（model＋tools in a loop）在命名前已是可教学的最小构造（<400 行）。
- 不支持什么：无停止条件/治理/自主度讨论（演示循环由用户退出隐式终止）；无长时无人值守主张。
- 标题勘误：流传的《How to Build a Coding Agent》在一手页面与 HN 提交中均不存在，属二手标题变体（sourcegraph 旧 URL 已 404；Wayback 本环境不可达，原始快照未核）。时间线采用一手标题。
- 证据层级：P-mechanism。

### Source D2 · Walden Yan（Cognition）《Don't Build Multi-Agents》：单线程 agent ＋ Principles of Context Engineering

- URL：https://cognition.com/blog/dont-build-multi-agents （⚠️ cognition.com 非 cognition.ai）
- 发布日期：2025-06-12（页面署名 "By Walden Yan 06.12.25"）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：Cognition 官方博客（Yan 为 Cognition 联创）
- 原文摘录：
  > "_Principle 1_ Share context, and share full agent traces, not just individual messages"
  > "_Principle 2_ Actions carry implicit decisions, and conflicting decisions carry bad results"
  > "'Context engineering' is the next level of this. It is about doing this automatically in a dynamic system. It takes more nuance and is effectively the #1 job of engineers building AI agents."
  > "The simplest way to follow the principles is to just use a single-threaded linear agent"
  > [Claude Code 例] "As of June 2025, Claude Code is an example of an agent that spawns subtasks. However, it never does work in parallel with the subtask agent, and the subtask agent is usually only tasked with answering a question, not writing any code."
- 该摘录支持的最小主张：命名前 12 天，高影响实践者已把"多 agent 并行＝脆弱、单线程＋共享上下文＝可靠"写成原则文——**loop 叙事的内部分裂线**（反并行）在命名前已公开成形。
- 不支持什么：不涉及循环时长/终止判据；影响力峰值在 2025-09-01 HN 重投（123 分）而非首发，引用影响力须区分两个时间点。
- 后续修订线索：cognition.com/blog/multi-agents-working（《Multi-Agents: What's Actually Working》）疑为其立场修订，本轮未抓取——**登记待回源**。
- 证据层级：P-mechanism。

### Source D3 · Manus（Yichao 'Peak' Ji）《Context Engineering for AI Agents》：最完整的 "loop until task complete" 机制句

- URL：https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
- 发布日期：2025-07-18（页面 "2025/7/18 --Yichao 'Peak' Ji"）
- 访问/观测日期：2026-09-27【主验（loop 段与 KV-cache 段）；文件系统段经第三方全文镜像补齐，待主站复核】
- 来源类型：Manus 官方博客（Ji 为联创兼首席科学家）
- 原文摘录（主站逐字）：
  > "After receiving a user input, the agent proceeds through a chain of tool uses to complete the task. In each iteration, the model selects an action from a predefined action space based on the current context. That action is then executed in the environment (e.g., Manus's virtual machine sandbox) to produce an observation. The action and observation are appended to the context, forming the input for the next iteration. This loop continues until the task is complete."
  > "If I had to choose just one metric, I'd argue that the KV-cache hit rate is the single most important metric for a production-stage AI agent."
  > "we've rebuilt our agent framework four times, each time after discovering a better way to shape context."
  > [镜像来源，待复核] "That's why we treat the file system as the ultimate context in Manus: unlimited in size, persistent by nature, and directly operable by the agent itself." / "A typical task in Manus requires around 50 tool calls on average. That's a long loop"
- 该摘录支持的最小主张：命名前 11 个月，**"loop until the task is complete" 的完整机制句已逐字成文**，且把循环工程约束（KV-cache 命中率、append-only context）写成生产指标；外部记忆（文件系统）被明确归因为长循环可持续性条件。
- 不支持什么：未讨论由谁/按什么判据终止（只说 until complete）；非 coding agent 场景；无自主度分档。
- 证据层级：P-mechanism。

### Source D4 · Armin Ronacher《Agentic Coding Recommendations》：派活后等待完成的实践自述

- URL：https://lucumr.pocoo.org/2025/6/12/agentic-coding/
- 发布日期：2025-06-12（页面 "written on June 12, 2025"）
- 访问/观测日期：2026-09-27【主验】
- 来源类型：作者本人长文（Flask/Werkzeug 作者；本批影响面最大的一手实践长文，HN 296 分/203 评论）
- 原文摘录：
  > "My general workflow involves assigning a job to an agent (which effectively has full permissions) and then waiting for it to complete the task. I rarely interrupt it, unless it's a small task."
  > "I disable all permission checks. Which basically means I run `claude --dangerously-skip-permissions`."
  > "**Test caching:** Surprisingly crucial for efficient agentic loops."
  > "it can take quite a while for the interpreter to boot up … the agent loop is really slow."
  > "**Keep important checks local.** You really want to make sure that permission checks are very clear to the AI … Hiding permission checks in another file or some config file will amost guarantee you that the AI will forget to add permission checks in when adding new routes."
  > "One caveat: I expect this blog post to age very poorly."
- 该摘录支持的最小主张：命名前 9 天，"派活→全权→等待完成"的持续推进实践已有一手自述；**"agentic loop" 已被当作性能与可靠性工程对象**（测速、喂工具、环境选型）；行为面保护的环境侧直觉（权限检查必须放在 agent 看得见的地方）同文出现。
- 不支持什么：无机制定义句；工具细节作者自警会过时（引用只取工作流与循环工程观点）。
- 证据层级：P-existence（实践存在）。

### Source D5 · Armin Ronacher《Building an Agent That Leverages Throwaway Code》：命中最接近"停止条件＋恢复"的一手伪代码

- URL：https://lucumr.pocoo.org/2025/10/17/code/
- 发布日期：2025-10-17
- 访问/观测日期：2026-09-27【主验】
- 来源类型：作者本人长文
- 原文摘录：
  > "I would describe durable execution as the idea of being able to retry a complex workflow safely without losing progress. The reason for this is that agents can take a very long time, and if they interrupt, you want to bring them back to the state they were in."
  > [myAgenticLoop 伪代码] "while (stepCount < MAX_STEPS) { let cacheKey = `${taskID}:${stepCount}`; let cachedState = loadStateFromCache(cacheKey); if (cachedState !== null) { state = cachedState.state; } else { state = runAgenticStep(state); storeStateInCache(cacheKey, state); } stepCount++; if (reachedEndCondition(state)) { break; } }"
  > "You can improve on this greatly, but this is the general idea. The state is basically the conversation log and whatever else you need to keep around for the tool execution"
  > "## File Systems Are King"
  > [4 步运行记录] "Step 4: Stop reason: end_turn"
- 该摘录支持的最小主张：**命名前 8 个月，"步数上限（MAX_STEPS）＋显式终止判据（reachedEndCondition）＋逐步状态缓存（中断恢复）"已被实践者写成可复制伪代码**——B 路"停止条件三件骨架"在命名前的个人实践版。
- 不支持什么：玩具级 4 步示例（作者自注可大幅改进），不证明生产长时运行；durable execution 针对中断恢复而非自主度治理。
- 证据层级：P-mechanism。

### Source D6 · Paul Gauthier（aider）benchmark 循环：谱系根节点（侦察回源）

- URL：https://aider.chat/2023/07/02/benchmarks.html
- 发布日期：2023-07-02
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > "Aider updates the implementation file based on GPT's reply and runs the unit tests. If all tests pass, the exercise is considered complete. If some tests fail, aider sends GPT a second message with the test error output."
  > "Requiring GPT to fix its first implementation in response to test failures is another way in which this benchmark stresses code editing skill."
- 最小主张：本批最早的脚本化"跑→测→喂错→重试"循环一手描述（2023-07，比其他全部材料早约两年）；但被硬性限定为 2 次尝试，且是 benchmark harness 非日常工作流。
- 不支持什么：不支持开放式 until-done；页面未署名（aider 博客历史作者为 Gauthier，2023-12-21 文显式署名可旁证）。
- 证据层级：P-mechanism。与 evidence-i Source 1（2024-05 lint 环）构成同一作者的时间序列。

### Source D7 · 谱系内部反例：Amp《200k Tokens Is Plenty》及其官方撤销头（侦察回源）

- URL：https://ampcode.com/notes/200k-tokens-is-plenty
- 发布日期：2025-12-09（署名 Lewis Metcalf）
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > "Agents get drunk if you feed them too many tokens." / "The best threads are short, they do one thing, and they have just the right amount of context to do it."
  > [官方 Archived 头] "This note was written in December 2025 for an older model and context-window era. Now, auto-compaction makes longer threads work well, and it's fine and productive to go beyond 200k tokens."
- 最小主张：Ball 所在团队在 "loop＋enough tokens"（2025-04）八个月后公开转向短线程反长循环（2025-12），该反例又在模型/上下文条件变化后被官方撤销——**立场随模型与上下文条件摆动的一手事实记录**。
- 不支持什么：任何一方的定论；只证明"长循环 vs 短线程"是条件依赖的工程权衡，不是主义之争。
- 证据层级：P-existence（立场变化事实）。

### 切口 I-2d 判读

时间线 §四（谱系背景）新增五条一手锚点，**全部早于 2026-06-02 词源火花**：aider benchmark 测试反馈环（2023-07）→ Ball 机制本体（2025-04-15）→ Walden 单线程原则＋Armin 派活实践（同日 2025-06-12）→ Manus 循环机制句（2025-07-18）→ Armin 停止条件伪代码（2025-10-17）。与 evidence-i 批次 1（Aider lint 环 2024-05、Horthy 反自由循环 2025-03、Beck 单测试节拍 2025-06、Willison designing agentic loops 2025-09、Yegge issue 记忆 2025-10）合并后，**"构件先于命名"（evidence-h 的判断）的样本密度已足以支撑更强表述：到 2026-06 命名时，机制本体、验证分层、停止条件、外部记忆、反方立场都已有公开一手文本**。命名事件（06-02→06-16）的性质更接近"对既有构件族的聚合命名"，而非机制首创。

---

## 切口 I-2e · SDD×loop 厂商组合形态（Kiro / Tessl / Linear；E 路增量）

> 本切口全部为【侦察回源】（厂商页面多为客户端渲染或正文截断，已用官方博客/官方 README/RSS 全文补足）；主 Agent 未复验，引用前建议复验。

### Source E1 · AWS Kiro：spec 三件套作为循环推进骨架 ＋ 官方承认 spec 漂移

- URL：https://kiro.dev/blog/introducing-kiro （2025-07-14，Product Lead + VP DevEx & Agents 联名）＋ https://raw.githubusercontent.com/kirodotdev/Kiro/main/README.md （活文档，©2026 Amazon.com, Inc.）
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > "Kiro generates tasks and sub-tasks, sequences them correctly based on dependencies, and links each to requirements."
  > "The task interface lets you trigger tasks one-by-one with a progress indicator showing execution status. Once complete, you can see the completion status inline and audit the work by viewing code diffs and agent execution history."
  > "Kiro's specs stay synced with your evolving codebase. … This solves the common problem where developers stop updating original artifacts during implementation, causing documentation mismatches that complicate future maintenance."
  > "Kiro hooks act like an experienced developer catching things you miss … These event-driven automations trigger an agent to execute a task in the background when you save, create, delete files, or on a manual trigger."
  > [README] "One unified agent harness powers every Kiro surface, so your specs, steering, permissions, hooks, MCP servers, and custom agents can follow your project across workflows."
  > [README] "Use correctness with property-based testing to turn requirements into executable properties and exercise them across generated inputs that example-based tests may miss."
- 最小主张：厂商级 SDD×loop 组合的官方形态——spec 产物（requirements/design/tasks）链接任务并按依赖排序；任务**逐个人工触发**（与 Spec Kit Ralph Loop extension 的自动推进形成对照）；spec↔代码双向同步（官方点名 spec 漂移为普遍失败模式）；hooks 事件触发；**spec 被官方定位为 harness 层资产**；需求可转"可执行属性"自动检验。
- 不支持什么：遵守率/失真率无数据；docs 正文（客户端渲染）未回源，现行机制细节待补。
- 证据层级：P-existence / P-mechanism。

### Source E2 · Tessl：官方直接定义 "loop engineering"（内/中/外三层）＋ skills→loops→factory

- URL：https://tessl.io/blog/who-owns-yourthe-context （2026-09-14）· https://tessl.io/blog/context-driven-factories （2026-09-15）· https://tessl.io/blog/jev-is-136x-faster-and-27x-cheaper-than-gpt-luna-6-for-tessl-verifiers-try-it-yourself （2026-09-23）· https://docs.tessl.io/overview/readme.md ＋ https://docs.tessl.io/automations/overview.md （活文档）· https://tessl.gitbook.io/tessl-press-kit/readme.md
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > [2026-09-14] "Context engineering is the work of optimising the context itself, the markdown, the verifiers, the hooks, the linting rules, everything in the repo that steers an agent on a given run. **Loop engineering is broader.** It includes the maintenance agents and the automated factory improvement that make the whole system better over time, **the inner loop of a single run, the middle loop that analyses agent behaviour across many runs and proposes improvements, and the outer loop that asks whether the shipped feature actually moved the business metric it targeted.**"
  > [2026-09-15] "Once your team starts capturing their workflows and standards in skills, you automate them with loops. A loop is a skill you have deployed to run automatically, one that improves over time as it runs. A factory composes skills and loops into a full agentic SDLC. This path has become a mantra at Tessl: from skills, to loops, to factory."
  > [2026-09-15] "An agent starts with the triage-issue skill loaded. … Once a PR exists, pr-shepherd takes over in the same shape: resolve CI, address review, merge when the criteria are met."
  > [2026-09-23] "That gives you a practical loop: agents generate code, verifiers check it, and review feedback helps you improve the rules."
  > [docs] "Context as code. Skills, rules, and docs are versioned, reviewed, and rolled out with the same rigor as code dependencies." / [automations] "The schedule lives next to the code it runs against, so it is reviewed and version-controlled like any other change."
- 暂定主张（仅在 Source E2 完成主验后可升级）：厂商页面据侦察摘录直接使用 "loop engineering" 并给出三层分类；若复核成立，它会成为第五个独立定义候选，外延最宽。当前不把它计入已确认定义源，也不据此回填已确认判读。产品方法论（skills → loops → factory）同样先保留为厂商自述机制候选。
- 不支持什么：Tessl 自家框架非行业标准；"improves over time" 无数据；判定者是 agent 本身（criteria 判定失败率未披露）。
- 重要内部张力（反例）：Tessl 现行 docs 已无 spec 页（spec-driven-with-tessl 404，词汇迁移至 skills/context）——其 2025-09 的 spec-centric 官方定位在本观测窗口内发生**词汇迁移**。
- 证据层级：P-existence（术语使用）/ P-mechanism（产品机制）。

### Source E3 · Linear：issue 作为 agent 工作来源 ＋ 自主度边界作为产品卖点（侦察回源）

- URL：https://linear.app/now/coding-sessions-for-linear-agent
- 发布日期：2026-06-11（CEO Karri Saarinen 署名）
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > "Coding sessions let Linear Agent natively move directly from an issue to implementation. … The agent reads the issue and its surrounding discussion, investigates the codebase, proposes an approach, writes the code, and opens a pull request."
  > "This is a loop we run ourselves. In the last month, almost 700 PRs were merged by the agent. … You can let the loop start from triage and run all the way to a draft PR, or kick it off yourself, handing the agent a single issue or a dozen at once. Either way, you decide where it starts and how far it goes before it's back in your hands."
- 最小主张：需求工具侧向执行循环延伸的厂商形态——issue＋讨论充当循环起点与上下文记忆；厂商自报生产数据（上月 agent 合并近 700 PR，无审计）；**自主度边界（起点/终点由人决定）被写成产品承诺**。
- 不支持什么：issue 不是严格 spec（无验收标准结构）；700 PR 为自报；"how far it goes" 无分档判定规则。
- 证据层级：P-mechanism（700 PR 为 vendor-reported P-outcome 候选）。

### Source E4 · Tessl 客座文两条：Continuous AI（GitHub Next）＋ spec 入口限定（侦察回源）

- URL：https://tessl.io/blog/repository-automation-needs-continuous-ai （2026-09-11，Don Syme，文中自述 GitHub Next）· https://tessl.io/blog/agent-experience-is-the-next-product-surface （2026-09-23，Netlify CEO Dana Lawson）
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > [Don Syme] "Continuous AI is the use of automated or semi-automated AI workflows inside the ongoing software process. It is repetitive, integrated, collaborative, auditable, and triggered by repository events or schedules. … It takes an agentic workflow specification and hardens it into a GitHub Action."
  > [Dana Lawson] "Specs still matter, especially in large-scale technical platforms. But many new builders are not starting with a 50-page requirement document, a Jira ticket, or a complete PRD. They are starting with a prompt, a sketch, a reference, or a problem description." / "CI becomes a continuous feedback loop rather than a final checkpoint."
- 最小主张：**工作流规约产物被"硬化"为自动执行的 Action**（Continuous AI，机制表述发布于 Tessl 客座文，需回 GitHub 官方 docs 复核）；spec 的入口地位被客座方明确限定；CI 被重述为持续反馈环。
- 不支持什么：客座文不代表平台方立场文件。
- 证据层级：P-mechanism / P-existence。

### Source E5 · Guy Podjarny 官方定位文（侦察回源）

- URL：https://tessl.gitbook.io/tessl-press-kit/readme.md （落款 "Yours, Guy Podjarny"）
- 访问/观测日期：2026-09-27【侦察回源】
- 关键引句：
  > "But software development is currently built around the wrong asset - code. … They focus on nurturing an implementation, but neglect to preserve the intent behind it. … It needs to transform, growing to revolve around intent and taste, not code."
- 最小主张：Podjarny（Snyk 创始人、Tessl 创始人）的 spec/intent-centric 官方立场文本存在（press kit 宣言级）。
- 不支持什么：宣言无机制内容；其 spec-centric 长文正文（tessl.io 老博客）抓取截断未得。
- 证据层级：P-existence。

### 切口 I-2e 判读

1. **E 路的"双向收敛"判断再获厂商级增量**：Kiro 把 spec 定位为 harness 资产＋把需求转成可执行属性（SDD 吸收 loop 的机械验收）；Tessl 把流程写成 skill 产物再部署为 loop（spec 侧吸收自动推进）。与 C 路 OpenSpec/Spec Kit 的开源侧收敛合并，"spec 产物作为 loop 的外部记忆与验收依据"现在有**开源自社区＋闭源自厂商**两组独立一手。
2. **术语谱系增量（候选）**：若 Source E2 完成主验，Tessl 2026-09-14 的三层分类可作为第五个独立定义候选，且外延最宽；当前只登记为待复核冲突样本，不计入已确认定义源，不直接回填 `digested/01`。
3. **反例组**：Kiro 官方承认 spec 漂移是普遍失败模式（以自动同步回应，无遵守率数据）；Tessl 自家 docs 词汇已从 spec 迁移到 skills/context；Netlify CEO 客座文承认 spec 非普遍入口——**spec-centric 词汇在厂商侧正在松动**，与 Böckeler/marmelab 的批判线同向且来自 SDD 阵营内部。
4. Linear 是取题环节的第三种厂商形态（issue→agent→PR），与 GitHub（backlog 指派）和社区（issue fanout→workspace）并列。

---

## 总判读（批次 2 候选摘要，主 Agent 融合前）

1. **缺口 4（真实 P-outcome）的候选修正**：主验条目显示存在跨场景定量结果，但方向相反且不能外推；仍无任何针对“不同 loop 设计”的受控比较。侦察条目不得用于扩大这条结论。对 DSH 对照实验（P2.9）的直接含义仍是候选设计方向，不是已证明的必要实验。
2. **缺口 3（跨 feature 可见性）的候选形态地图**：I2 侦察与主验条目共同提出若干控制面形态；在主 Agent 逐条复核之前，只能说它们是待筛选样本，不能据此确认“六种形态”或关闭授权史/priority/阻塞/验收空列。
3. **P1.5（行为面验证）候选素材**：raw 档案收集了 execution/direction drift、false completion、raw transcripts、测试与票据、删测试等线索；是否足以形成正反例矩阵，待主 Agent 逐条复核。
4. **P1.6（自我改写）候选素材**：raw 档案记录提案/评估分离、Pareto、held-out、审计谱系等保护链及 criteria drift/静默退化反例；当前不进入实践层。
5. **Q2.4（验证分界）候选组**：Hamel、Eugene、Chip、Kiro、Tessl 等材料需按主验状态和来源类型拆开，不能合并为统一行业判据。
6. **谱系候选**：Ball/Manus/Armin 等主验条目可作为“构件先于命名”的增量候选；Walden/Amp 等侦察条目不计入已确认谱系，命名事件的聚合命名判读仍以既有已复核材料为准。
7. **KOL 台账处置**：本批次**不新增 §A**。Ball/Walden/Armin/Manus 按时间窗规则入 §B（谱系背景）；Gauthier 既有 §B 行追加 2023 记录指针；evals 四人与 METR/DORA/GitClear/GEPA/DSPy/AlphaEvolve 为**证据来源非发声 KOL**，不入册；Kiro/Tessl/Linear/GitHub/Antigravity/Cursor/Devin 为机构条目，素材在 evidence。

## 线索登记（侦察发现、未回源或不作主张依据）

- cognition.com/blog/multi-agents-working（《Multi-Agents: What's Actually Working》）——Walden Yan 立场修订线索，待回源。
- DORA 2025 年报具体系数：全文 gated（cloud.google.com/dora）；Thoughtworks 镜像 PDF 抓取不支持；官方公告页与 InfoQ 转述页抓取截断。
- GitClear 白皮书全文（2025-02、2026-01）需邮箱下载；本档案数字来自官方落地页摘要（Write-Only 页已主验）。
- METR 2026-05-11 自报调查（349 人，中位自报 1.4–2x value / 3x speed；官方自列怀疑理由）：https://metr.org/blog/2026-05-11-ai-usage-survey/ ——与 C1 的 +20pp 感知偏差互为锚点，本轮未独立主验。
- Kiro docs（kiro.dev/docs/specs/ 等）：HTTP 200 但客户端渲染，正文未取得；现行机制细节待人工浏览器补核。
- docs.devin.ai 组织级 API（List Organization Sessions / Get Session Metrics）：标题可见，正文被 Mintlify 壳层截断。
- Devin/Amp/Jules 在批次 1 负结论清单中的"仍未回源"项：本轮 Devin（官方博客）与 Jules（官方 docs）已回源；Amp 侧仅 Ball 文章与 200k 反例回源，Amp 产品机制文仍未回源。
- Atlassian/Jira Rovo Dev（"Generate code from a work item in Jira"）：官方 docs 标题确认存在，正文客户端渲染未取得。
- GitHub Agentic Workflows（Don Syme 表述）：机制句发布于 Tessl 客座文，需回 GitHub 官方 docs 复核。

## 负结论与限制

- 搜过但未取得：DORA 2025 年报正文具体系数；GitClear 白皮书全文；Podjarny spec-centric 长文正文；Kiro docs 正文；Devin docs 正文；Amp 原始快照标题史（Wayback 本环境网络失败）；DeepMind AlphaEvolve 博文与白皮书 §2.4–2.5（超长页截断，已用摘要＋§1–2.1＋图注替代）。
- 不能据此推出：行业已证明 AI 提效或无效（方向依赖场景/代际/度量）；METR/DORA/GitClear 数字可外推到 DSH 或任何具体 loop 设计；观测性质量劣化与缺陷率之间的因果；Tessl 三层 loop 分类是行业共识；Cursor 30%/6x 与 Linear 700 PR 的真实性（均 vendor-reported）。
- 本批次不改变：立题评估（README §4）；实践层 backbone/manual 状态；§A 名单。
