---
type: evidence_archive
collected_by: 委派回源子代理（C 路 · 自主度阶梯与对照面）
collected_at: 2026-09-26
serves: digested 边界判定篇 · 03_practice/loop_governance/result/backbone.md（自主度分档 / 检查点与反例 / 与 SDD 的收敛）
status: 全部一手源逐字核实（Kief Morris 四级阶梯 / Böckeler steering loop / marmelab 两篇 / Stripe / OpenSpec / Spec Kit / 橙皮书定性）
key_fixes: 三条引用归属修正（SDD adds little benefit 与 False Sense of Security 的真实出处是 marmelab 2025-11-12 而非 2026-09-24 审计文；False sense of control? 在 Böckeler 2025-10-15 sdd-3-tools 而非 harness-engineering；Agent = Model + Harness 原创是 Trivedy/LangChain，Böckeler 是传播锚点）
quality_bar: 2026-09-26 用户质量门槛——HN 评论者不入册；橙皮书定性为中文编译非独立发明
---

# 回源报告 C：自主度阶梯 / 对照面 / 中文圈（访问日期 2026-09-26）

> 回源人：loop-dig 子代理 C。访问日期统一为 **2026-09-26**（终端 `date` 实测：2026-09-26 20:08 CST）。
> 口径：只收一手源（作者本人文章 / 官方博客 / 官方 release notes / 官方文档 / 官方 npm 包描述）。逐字引句一律不翻译不改写。
> 方法备注：stripe.dev 页面为 JS 渲染，正文从页面内嵌 `__NEXT_DATA__` JSON 中提取（官方页面自身数据，仍为一手）；GitHub release 页在抓取中被导航模板截断，改用 GitHub REST API（api.github.com）取官方 release notes 原文；marmelab 长文用 curl 取 HTML 后转纯文本，全文核对。
> 按父代理 2026-09-26 新标准执行：HN 评论者一律不入册（见「不入册」节）；橙皮书降为低优先级（只定性，一句话结论）；每条入册证据附「为什么算高影响力」。

---

## 问题 3：自主度分档与人在环位置

### 1. Kief Morris（in the loop → on the loop）

- **URL**：https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html
- **作者**：Kief Morris（Thoughtworks 全球云技术专家，martinfowler.com「Exploring Gen AI」系列）
- **发布日期（页面标注）**：04 March 2026（线索说"约 2026-03-04"，精确命中）
- **访问日期**：2026-09-26
- **为什么算高影响力**：martinfowler.com 专栏作者、Thoughtworks 全球云技术专家；Böckeler 在 harness-engineering.html 的致谢里点名是他把 cybernetics 视角带进该文讨论（"in particular Kief Morris for bringing up cybernetics"）——即他属于定义这门学科话语权的 Thoughtworks 核心圈。
- **逐字引句**（全部核实自原文）：

  1) 开篇定调 + 命名 "on the loop"：
  > "Should humans stay out of the software development process and vibe code, or do we need developers in the loop inspecting every line of code? I believe the answer is to focus on the goal of turning ideas into outcomes. The right place for us humans is to build and manage the working loop rather than either leaving the agents to it or micromanaging what they produce. Let's call this 'on the loop.'"

  2) "in the loop" 的定义（线索句"人类审批每一个行动"核实为"内环守门人"）：
  > "When people talk about 'humans in the loop', they often mean humans as a gatekeeper within the innermost loop where code is generated, such as manually inspecting each line of code created by an LLM."

  3) in / on 的机制差别（本任务要的"操作性洞察"）：
  > "The difference between in the loop and on the loop is most visible in what we do when we're not satisfied with what the agent produces, including an intermediate artefact. The 'in the loop' way is to fix the artefact, whether by directly editing it, or by telling the agent to make the correction we want. The 'on the loop' way is to change the harness that produced the artefact so it produces the results we want."

  4) 分档结构：全文实际给出**四个位置**——Humans outside the loop（vibe coding，含"Some interpretations of Spec Driven Development (SDD) are much the same"）→ Humans in the loop → Humans on the loop → **The agentic flywheel**（"Agentic Flywheel" 提法核实存在，是节标题）：
  > "The next level is humans directing agents to manage and improve the harness rather than doing it by hand."

  5) flywheel 里的**渐进自主判据**（分数门槛自动放行）：
  > "As we gain confidence, the agents can assign scores to their recommendations, including the risks, costs, and benefits. We might then decide that recommendations with certain scores should be automatically approved and applied."

  6) "middle loop" 旁证（他把 on the loop 挂到第三方社群的同名概念）：
  > "Something like the on the loop concept has also been described as the 'middle loop,' including by participants of The Future of Software Development Retreat. The middle loop refers to moving human attention to a higher-level loop than the coding loop."

  7) 脚注对 ralph loop 的**人在环位置**澄清（对 loop engineering 谱系极重要）：
  > "These days 'ralph loop' is often used colloquially to mean just firing up a bunch of agents and leaving them to keep looping until (hopefully) they finish their task. But [as originally described](https://ghuntley.com/ralph/) the operator plays an important role in steering agents as they ralph."

- **支撑什么**：问题 3 的主证据——自主度"位置分档"（outside / in / on / flywheel）与渐进自主的评分判据；同时给 ralph loop 谱系补了"原始形态里操作员在环内掌舵"这个一手注脚。

### 2. Addy Osmani（生成/评估分离）

- **URL**：https://addyosmani.com/blog/agent-harness-engineering/
- **作者**：Addy Osmani（文末自述 bio："a Member of Technical Staff at Anthropic, where he works on Claude Code"，此前 14 年在 Google 领导 Chrome / AI 开发者体验，最近职位 Google Cloud AI Director；O'Reilly《Beyond Vibe Coding》作者）
- **发布日期（页面标注）**：April 19, 2026
- **访问日期**：2026-09-26
- **为什么算高影响力**：Claude Code 团队成员（Anthropic MTS）+ Google 前总监级 DX 负责人 + O'Reilly 作者；其文被 marmelab 2026 审计收进 57 篇文献的「methods & patterns」12 篇之列。
- **逐字引句**（线索句核实为真，但**出处链要注意**）：

  1) 线索引句原文（Osmani 把该模式归于 Anthropic 的长程 harness 工作，不是他原创）：
  > "**Planner / generator / evaluator splits.** Anthropic's long-running harness work is explicit that separating generation and evaluation into distinct agents outperforms self-evaluation, because agents reliably skew positive when grading their own work. It's GANs for prose. The related pattern is the **sprint contract**, where the generator and evaluator negotiate what 'done' actually means before code gets written."

  2) 与之配套的第一性判据（写死 done 条件）：
  > "In my own workflows, writing down the done-condition before starting has caught more scope drift than any prompt change I've ever made."

  3) hooks 作为强制层——人在环的审批被降级为少数高危动作的阻断门：
  > "They're the right place for things the agent should never forget but often does. Run typecheck and lint and tests after every edit and surface failures. Block destructive bash (`rm -rf`, `git push --force`, `DROP TABLE`). Require approval before opening a PR or pushing to `main`."

  4) 门的形态判据（静默成功、失败才说话）：
  > "**success is silent, failures are verbose.** If typecheck passes, the agent hears nothing. If it fails, the error text gets injected into the loop and the agent self-corrects."

  5) 规则的溯源判据（每条规则须对应真实失败）：
  > "**Every line in a good `AGENTS.md` should be traceable back to a specific thing that went wrong.**"

- **支撑什么**：问题 3——"生成/评估分离"作为自主运行的验收替代（谁来判定"可以不用人看"：另一个 agent + 预先写死的 done 条件），以及审批门收敛到"破坏性动作 + PR/push"这一小集合。

### 3. Birgitta Böckeler（False sense of control）

Böckeler 涉及**两篇**一手文章，线索把两件事捏在了一个 URL 上，实际分属两文：

**(a) "False sense of control?" 的真正出处 —— SDD 工具评测文**

- **URL**：https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- **标题**：Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl
- **作者**：Birgitta Böckeler（Thoughtworks Distinguished Engineer、AI-assisted delivery 专家，自述 20+ 年开发/架构/技术领导经验——页面 bio 原文）
- **发布日期（页面标注）**：15 October 2025
- **访问日期**：2026-09-26
- **逐字引句**：

  1) 设问原句与上下文（⚠️ 不在 harness-engineering.html，线索 URL 归属错误）：
  > "**False sense of control?**
  > Even with all of these files and templates and prompts and workflows and checklists, I frequently saw the agent ultimately not follow all the instructions. Yes, the context windows are now larger, which is often mentioned as one of the enablers of spec-driven development. But just because the windows are larger, doesn't mean that AI will properly pick up on everything that's in there."

  2) 具体案例（spec-kit 的 research 步骤产物被 agent 当成新规格重复生成）：
  > "For example: Spec-kit has a research step somewhere during planning, and it did a lot of research on the existing code and what's already there, which was great because I asked it to add a feature that built on top of existing code. But ultimately the agent ignored the notes that these were descriptions of existing classes, it just took them as a new specification and generated them all over again, creating duplicates. But I didn't only see examples of ignoring instructions, I also saw the agent go way overboard because it was too eagerly following instructions (e.g. one of the constitution articles)."

  3) 控制感结论（她给出的"如何才能在控"判据：小步迭代）：
  > "The past has shown that the best way for us to stay in control of what we're building are small, iterative steps, so I'm very skeptical that lots of up-front spec design is a good idea, especially when it's overly verbose."

  4) 审查负担原句：
  > "To be honest, I'd rather review code than all these markdown files."

  5) 三级 taxonomy（原文定义，spec-first / spec-anchored / spec-as-source）：
  > "Spec-first: A well thought-out spec is written first, and then used in the AI-assisted development workflow for the task at hand.
  > Spec-anchored: The spec is kept even after the task is complete, to continue using it for evolution and maintenance of the respective feature.
  > Spec-as-source: The spec is the main source file over time, and only the spec is edited by the human, the human never touches the code."

  6) 她转引的 GitHub 官方口径（阶段审批门的原始表述）：
  > "Because as GitHub's blog post about spec-kit says: 'Crucially, your role isn't just to steer. It's to verify. At each phase, you reflect and refine.'"

  7) 立场平衡注记（她不是反 spec 派）：
  > "So the general principle of spec-first is definitely valuable in many situations, and the different approaches of how to structure that spec are very sought after."

**(b) "Agent = Model + Harness" 公式的出处文**

- **URL**：https://martinfowler.com/articles/harness-engineering.html
- **标题**：Harness engineering for coding agent users
- **作者**：Birgitta Böckeler（同上）
- **发布日期（页面标注）**：02 April 2026（线索"约 2026-04-02"精确命中）
- **访问日期**：2026-09-26
- **为什么算高影响力**：marmelab 审计把此文列为 8 篇 founding texts 之一并称其为"The reference mental model"；SE Radio 730（2026-07）专访嘉宾；Thoughtworks Distinguished Engineer。
- **逐字引句**：

  1) 公式及其归属——⚠️ **Böckeler 本文把公式链接到 LangChain，不是自称原创**：
  > "The term harness has emerged as a shorthand to mean everything in an AI agent except the model itself - [Agent = Model + Harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/)."

  （对照：Osmani 文中写 "Viv's one-liner does most of the work: > Agent = Model + Harness. If you're not the model, you're the harness."，并称 "Viv Trivedy coined the term _harness engineering"；而 marmelab 写 "a formula we owe to Birgitta Böckeler"。**一手源链：Viv Trivedy/LangChain 原创 → Böckeler 在 martinfowler.com 使其成为行业引用锚点 → marmelab 把功劳记给 Böckeler**。转述层（marmelab）与一手源（Osmani、Böckeler 自文）归属不一致，引用时以一手链为准。）

  2) 人在环的总判据（问题 3 最直接的判据句）：
  > "Harnesses are an attempt to externalise and make explicit what human developer experience brings to the table, but it can only go so far. Building a coherent system of guides and sensors and self-correction loops is expensive, so we have to prioritise with a clear goal in mind: A good harness should not necessarily aim to fully eliminate human input, but to direct it to where our input is most important."

  3) steering loop（与 Kief "on the loop" 同构，且同属 Thoughtworks——需标注非完全独立）：
  > "The human's job in this is to **steer** the agent by iterating on the harness. Whenever an issue happens multiple times, the feedforward and feedback controls should be improved to make the issue less probable to occur in the future, or even prevent it."

  4) 高自主用户的现行做法与其短板（行为面验证缺口 = "能不能放手"卡点）：
  > "At the moment, I see most people who give high autonomy to their coding agents do this:
  > - Feed-forward: A functional specification (of varying levels of detail, from a short prompt to multi-file descriptions)
  > - Feed-back: Check if the AI-generated test suite is green, has reasonably high coverage, some might even monitor its quality with mutation testing. Then combine that with manual testing.
  > This approach puts a lot of faith into the AI-generated tests, that's not good enough yet."
  >
  > "So overall, we still have a lot to do to figure out good harnesses for functional behaviour that increase our confidence enough to reduce supervision and manual testing."

- **支撑什么**：问题 3（人的介入应被"定向到最重要的输入"而非消除；行为面 harness 是减监督的公认短板）＋"False sense of control" 的具体案例与原文。

### 4. 其他顺路发现的自主度分档证据（一手）

**4a. marmelab 2026 审计（详见对照面第 4 条）中的三段一手判据**——URL: https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html，François Zaninotto，2026-09-24（页面标注"September 24, 2026"），访问 2026-09-26：

  1) 预写规则 vs 逐动作审批的实测反直觉证据（引 arXiv 2608.27443，113 人）：
  > "Writing permission rules in advance works worse than approving each action. A study with 113 participants compared two ways of supervising an agent: writing the rules up front, or approving each action as it came. The rule writers blocked 20.1 percentage points fewer bad actions. They had set most of their rules to 'ask me', then approved the prompts anyway, as most people do (93% of permission prompts get approved). A rule that ends in a prompt isn't a rule."

  2) 谁来设计监督（harness 设计权判据，且自认是 opinion 非 finding）：
  > "That's also why we think a harness should be built by a human, instead of an agent. If an agent needs supervision, how can it decide the supervision it needs? This is our opinion rather than a finding: the only ablation study we found (NLAH, arXiv 2603.25723) measures the opposite, with a self-improving harness gaining 4.8 and 2.7 points on two benchmarks."

  3) 瓶颈转移（从产码到验证）：
  > "Agents produce code faster than humans can review it, so the bottleneck is no longer the production of code but its verification."

  4) 门禁策略随吞吐量分档（引 OpenAI）：
  > "In their words, 'corrections are cheap, and waiting is expensive'. A bad merge costs one extra PR to fix, while a blocked queue costs everyone, every time. But they warn that the same choice 'would be irresponsible in a low-throughput environment': the right answer depends on how much you ship."

**4b. OpenSpec 官方 release notes**（v1.13.2，2026-09-23，api.github.com/repos/Fission-AI/OpenSpec/releases，官方发布记录）——人工门收缩为「关键歧义才问」：
> "**Approval prompts** - Fast-forward asks for clarification only when context is critically unclear, and onboarding asks you to approve the task breakdown before saving it."

**4c. Spec Kit 官方 release notes**（v0.12.14，2026-07-13）——自主运行治理成为可安装 preset：
> "Add Autonomous Run Governance preset to community catalog (#3501)"

（同日还有 "Add Test-First Governance preset to community catalog (#3504)" 与 "[extension] Add Quality Gates (Enforcement Layer) extension to community catalog (#3431)"——SDD 官方目录在同时收"门禁/强制层"件。）

**4d. Stripe hard/soft steering**（详见对照面第 5 条）——门的形态判据：
> "The difference is simple: errors block progress but warnings don't."

### 综合：问题 3 是否已有成型判据？≥2 独立来源是否同向？

**结论：位置分档已成型（≥3 个独立来源同向）；量化分档（"跑几轮/什么风险必须人看"）尚未成型，且现有证据一致指向"风险/歧义触发"而非"轮次触发"；行为面验证被点名为当前最大缺口。**

1. **位置分档成型、多方同向**：Kief Morris 给出四位置阶梯（outside / in / on the loop / agentic flywheel）；Böckeler 的 steering loop（"steer the agent by iterating on the harness"）与 Kief 的 on the loop 机制完全同构——但两人同属 Thoughtworks，**只能算一个阵营的两票**。独立同向证据：marmelab 独立审计（"A rule that ends in a prompt isn't a rule"，人审门 93% 被顺手放行 → 机械门才可靠）、Stripe（hard steering 生效 / soft 全败）、经 marmelab 转引的 OpenAI（"corrections are cheap, and waiting is expensive"）。三家机构（Thoughtworks / marmelab / Stripe·OpenAI）互不隶属、方向一致：**把"人逐行动审批"降级为"阻断式机械门 + 少量判断点"**。
2. **介入点判据是"事件驱动"不是"轮次驱动"**：没有任何一手源给出"N 轮必须人看"的数字判据。现行的成型判据形态是：① 风险分数门槛（Kief："recommendations with certain scores should be automatically approved and applied"）；② 歧义触发（OpenSpec："only when context is critically unclear"）；③ 动作类别触发（Osmani：destructive bash / PR / push to main 才要审批）；④ 吞吐量分档（OpenAI via marmelab："irresponsible in a low-throughput environment"）。
3. **"写好规则再放手"这个直觉判据被实测证伪**（marmelab 引 113 人研究：预写规则比逐动作审批少拦 20.1 个百分点）——这解释了为什么行业在从"文档门"转向"可执行门"（12/391 仓库有 deny 规则的缺口数据见对照面第 4 条）。
4. **验收替代判据**：生成/评估分离（Osmani 引 Anthropic："separating generation and evaluation into distinct agents outperforms self-evaluation, because agents reliably skew positive when grading their own work"）+ 预写 done 条件（sprint contract）。
5. **公开承认的未成型处**：Böckeler 明说行为面 harness "not good enough yet"、尚不能 "reduce supervision and manual testing"；marmelab 明说监督设计权留给人是"opinion rather than a finding"（反例 ablation +4.8/+2.7 存在）。**"什么风险必须人看"目前只有方向（行为验收、关键歧义、不可逆动作），没有成型阈值。**

---

## 对照面：SDD 阵营 2026 演化

### 4. marmelab 审计

涉及两篇一手文章。⚠️ **归属修正（重要）**：任务线索把 "Most coding agents already have a plan mode and a task list…" 与 "False Sense of Security" 记在 2026-09-24 审计文下——**两条都不在该文**（对该文全文 grep "SDD / plan mode / task list / verify implementation" 均零命中；spec-kit 在文中仅作为库存表条目出现）。两条的真正出处是 2025-11-12 的 SDD 专文。

**(a)《The State Of AI Harness Engineering 2026》**

- **URL**：https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html
- **作者**：François Zaninotto（Marmelab 创始人兼 CEO，react-admin 首席开发者——页面 bio 原文）
- **发布日期（页面标注）**：September 24, 2026（"28 min read"）
- **访问日期**：2026-09-26
- **为什么算高影响力**：独立咨询方对 246 个仓库 + 57 篇文献的审计（本文自述方法与样本）；react-admin 作者；其计量数据被本仓 KOL 对齐调查整表引用。
- **逐字引句**：

  1) loop / Ralph Wiggum 段（"What Doesn't Work" 节，loop 侧的核心取证）：
  > "Looping works. Throwing away the context each time is unproven. OpenAI runs the loop in production (they call it a Ralph Wiggum Loop) at the scale of 1,500 merged PRs. The fresh-context variant rests on one uncontrolled run of a toy app, with no baseline. What actually helps isn't the wipe, it's that the work is written down in files."

  2) back pressure / 不会说谎的裁判（文中 57 篇文献清单里对 Huntley 的收录条目）：
  > "Inventing the Ralph Wiggum loop — Geoffrey Huntley — Loop the agent until an oracle that cannot lie (test, linter, type checker) passes. Huntley calls it _back pressure engineering_."

  3) 行业执行缺口（立场②的外部杠杆数据）：
  > "**Everybody writes instructions, almost nobody enforces them** … Only **12** of the 391 repositories commit a single `deny` rule in their Claude Code settings. **22** declare a `PreToolUse` hook, the kind that can veto an action before it runs."

  4) 公式归属句（与一手源冲突处，见问题 3 第 3 条）：
  > "it's safe to say that the only consensus is about _what_ Harness Engineering is (Agent = Model + Harness, a formula we owe to [Birgitta Böckeler]…)"

  5) harness 最小化判据（loop 侧对"SDD 冗余论"的机制基础）：
  > "But out of the box, the last generation of coding agents is already very capable. So a harness should be built in reaction to an agent failure, not based on an assumption that the agent can't do something properly."

  6) OpenAI 命名学科的入库条目（含 1,500 PR / 0 行手写数据）：
  > "The text that named the discipline, and the densest first-party account in this corpus: five months, ~1M lines, **0 lines of manually-written code**, ~1,500 merged PRs, 3.5 per engineer per day."

**(b)《Spec-Driven Development: The Waterfall Strikes Back》——两条待核实引句的真正出处**

- **URL**：https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html
- **作者**：François Zaninotto（同上）
- **发布日期（页面标注）**：November 12, 2025
- **访问日期**：2026-09-26
- **逐字引句**：

  1) "SDD adds little benefit" 原句（逐字核实）：
  > "Most coding agents already have a plan mode and a task list. In most cases, SDD adds little benefit. Sometimes, it even increases the cost of feature development."

  2) "False Sense of Security" 原句与案例（agent 把 verify implementation 标 done 却零单测——逐字核实）：
  > "False Sense of Security: The SDD methodology is meant to keep the coding agent on track, but in practice, agents don't always follow the spec. In the example above, the agent marked the 'verify implementation' task as done without writing a single unit test—it wrote manual testing instructions instead."

  3) brownfield 判死原句：
  > "For large existing codebases, SDD is mostly unusable."

  4) 他给 loop 侧方法起的备用名（Natural Language Development）：
  > "This approach has one drawback compared to Spec-Driven Development: it doesn't have a name. 'Vibe coding' sounds dismissive, so let's call it Natural Language Development."

- **支撑什么**：对照面——loop 侧对 SDD 的批评原文；"coding agents 自带 plan mode/task list" 是"loop 工具已吞掉 SDD 功能位"这一收敛论断的一手论据。

### 5. Stripe steering

- **URL**：https://stripe.dev/blog/ai-steering-experiments
- **标题**：You can't whisper at an AI agent
- **作者**：James Beswick（Stripe Developer Relations 团队负责人，前 AWS Developer Advocacy leader——页面作者栏 bio）＋ Peter Epsteen（Stripe Growth 团队软件工程师）
- **发布日期（页面标注）**：2026.5.14（页面元数据 "Date:2026.5.14"；线索 2026-05-14 命中）
- **访问日期**：2026-09-26
- **为什么算高影响力**：Stripe 官方工程博客（stripe.dev）一手实验报告；marmelab 57 篇文献清单把它列入 9 篇产品实战报告（"You need mechanisms, not instructions"）。
- **逐字引句**：

  1) hard vs soft steering 效果差异**原句**（本条重点取证，逐字核实）：
  > "**Error-based steering.** We ran an experiment using API compatibility mode. When new merchants hit the API with an outdated version, they received an explicit error rather than a degraded response. In test conditions, agents reliably detected the error, identified the version mismatch, and corrected their request. This is a meaningful contrast with the warning-based approach, which agents ignored. The difference is simple: **errors block progress but warnings don't.** An agent that hits an error *must* deal with it to complete its task. A warning is, from the agent's perspective, often just noise."

  2) 设计轴总结原句：
  > "Second, the distinction between 'hard' and 'soft' steering is probably the most important design axis for agent-facing infrastructure. Hard steers, such as errors, explicit instructions in loaded context, and blocking responses, work. Soft steers - warnings, hints, adjacent files, in-band suggestions - often don't."

  3) 实验设计（操作性洞察：约十几个实验、三类）：
  > "Our team ran roughly a dozen experiments aimed at a single question: how do you get an AI agent to use Stripe correctly? … **Passive hints.** We tried embedding guidance in places agents might encounter it organically, adding warning hashes in API responses, steering cues in SDK source files, and `AGENTS.md` files in package directories. … **Active prompts.** We restructured how skill files were organized (progressive disclosure versus monolithic blobs)… **Distribution plays.** … The results split very cleanly. Passive hints failed while active prompts and distribution plays worked, some of them far better than expected."

  4) 两个失败实验的细节（SDK 依赖目录 / API warn hash）：
  > "But in practice, agents almost never read files inside dependency directories. The steering cues were invisible so we ended the experiment."
  >
  > "Again, agents didn't respond. They parsed the API response for the data they needed, ignored the warning, and moved on."

  5) 渐进披露实测数字：
  > "The modular format outperformed the monolith by roughly 10% across our eval suite."

  6) 第一结论（分发问题）：
  > "First, agent-facing developer experience is a distribution problem, not a content problem."

  7) 时间注记（实验时段）：
  > "The experiments summarized here were run by engineers across Stripe's developer experience and agent platform teams during early 2026."

- **支撑什么**：问题 3（门的形态判据：只有阻断式生效）＋对照面（loop 侧的环境治理方法论：指令必须放进加载路径并具备阻断力）。

### 6. OpenSpec / Spec Kit

**OpenSpec（全部取自官方 release notes（GitHub REST API）、官方 docs/opsx.md、官方 npm 包 @fission-ai/openspec）**

- 访问日期：2026-09-26；发布日期以各 release 页标注为准。

  1) **OPSX 去掉刚性阶段锁**——官方文档原句（docs/opsx.md，仓库 Fission-AI/OpenSpec main 分支）：
  > "It's a **fluid, iterative workflow** for OpenSpec changes. No more rigid phases — just actions you can take anytime."
  >
  > "**Dependencies are enablers** — they show what's possible, not what's required next"
  >
  > "Artifacts form a directed acyclic graph (DAG). Dependencies are **enablers**, not gates:"

  （线索句 "No more rigid phases" 与 "Dependencies are enablers, not gates" 均**逐字核实**于官方文档。）

  2) v1.0.0 "The OPSX Release"（2026-01-26）release notes：
  > "Action-based workflow — Replaced the rigid proposal → apply → archive sequence with flexible actions. Edit any artifact anytime. The artifact graph tracks state automatically."

  3) **npm 是否保留 "Agree before you build"**——官方包 `@fission-ai/openspec`（latest 1.13.2，registry.npmjs.org）README 逐字核实**保留**：
  > "- **Agree before you build** — human and AI align on specs before code gets written"

  （包描述为 "AI-native system for spec-driven development"。注意：npm 上名为 `openspec` 的包是无关占位包（latest 0.0.0、无描述），官方包是 `@fission-ai/openspec`。）
  （解读：阶段锁拆了，但「动工前人机对齐 spec」的门槛语义仍在 npm README 一线保留——去的是"刚性时序门"，不是"对齐门"。）

  4) 人工确认持续收缩的版本链（官方 release notes 逐字）：
  - v1.6.0（2026-07-10）："Generated skills and Claude commands can pre-approve the OpenSpec CLI, avoiding repeated confirmation prompts while leaving other tools under normal permission controls."
  - v1.12.0（2026-09-03）："**Code-grounded planning** - Propose and fast-forward workflows now inspect relevant code, tests, and documentation before drafting artifacts."
  - v1.13.2（2026-09-23）："Fast-forward asks for clarification only when context is critically unclear, and onboarding asks you to approve the task breakdown before saving it."

**Spec Kit（github/spec-kit，全部取自官方 release notes，GitHub REST API）**

- 访问日期：2026-09-26。

  1) **DSH 集成**——v1.0.4（2026-09-02）release notes 逐字核实：
  > "Add DeepSeek Harness (DSH) integration (#4336)"

  2) **Autonomous Run Governance preset**——v0.12.14（2026-07-13）首次入册、持续更新至 v0.4.4：
  > "Add Autonomous Run Governance preset to community catalog (#3501)"（v0.12.14）
  >
  > "[preset] Update Autonomous Run Governance preset to v0.4.4 (#4586)"（v1.0.10，2026-09-22）
  >
  > 另有并行变体："[preset] Add Parallel Autonomous Run Governance preset to community catalog (#3614)"（v0.13.3，2026-07-22）

  3) **Ralph Loop extension**——官方社区目录收录并持续更新：
  > "Update Ralph Loop extension to v1.5.0 (#4593)"（v1.0.9，2026-09-21）
  >
  > （更早："Update Ralph Loop to v1.0.2 (#2435)"，v0.8.6，2026-05-06；"Update Ralph Loop extension to v1.2.1 (#3365)"，v0.12.6，2026-07-07。**线索里 "Ralph Loop extension（v1.5.0）" 的 v1.5.0 是该扩展自身版本号，非 spec-kit 版本号**——由 v1.0.9 的 release note 原句坐实。）

  4) 门禁/验证方向的相邻条目（官方 release notes 逐字）：
  - "Add Test-First Governance preset to community catalog (#3504)"（v0.12.14，2026-07-13）
  - "[extension] Add Quality Gates (Enforcement Layer) extension to community catalog (#3431)"（v0.12.14，2026-07-13）
  - "fix(workflows): exempt bug-fix from PR-count confirmation (#4636)"（v1.0.9，2026-09-21）
  - "fix: clarify converge assessment of completion claims (#4621)"（v1.0.9，2026-09-21）
  - "fix(init): stop specify init hanging on arrow-key pickers in agent harnesses (#4178)"（v0.16.5，2026-08-19）——工具在适配 agent 驱动（无人终端）的使用方式。

- **为什么 OpenSpec / Spec Kit 算高影响力**：两者是 SDD 工具链的头部官方实现——Spec Kit 属 github 官方 org（marmelab 库存表记 137k★，列为 Orchestrator 类）；OpenSpec 为 Fission-AI 维护、npm 官方包持续双周发版（2025-09 v0.1.0 → 2026-09 v1.13.2 共 50 个 release），其官方哲学句（"No more rigid phases"）被本仓研究层直接引用。

### 综合：loop 侧与 SDD 侧是否在互相吸收？（"收敛"判断的证据）

**结论：是，收敛证据充分且双向、全部可溯源到官方一手动作；但"取代/合并"不成立——分歧收敛到「工作流状态放哪」，而不是一方消失。**

1. **SDD → loop 方向（拆门 + 吸收 loop 构件）**：
   - OpenSpec v1.0.0（2026-01-26）官方拆掉刚性时序（"Replaced the rigid proposal → apply → archive sequence with flexible actions"），docs 原句 "No more rigid phases"；同时把人工确认收缩为歧义触发（v1.13.2 "only when context is critically unclear"）并 pre-approve 自家 CLI（v1.6.0）。
   - Spec Kit 官方社区目录**同时收录** Ralph Loop extension（loop 侧图腾）与 Autonomous Run Governance preset（自主运行治理）——SDD 官方生态在打包分发 loop 侧的构件。
   - Spec Kit v1.0.4 官方接入 DSH（#4336）：SDD 流程进入一个 coding agent harness——loop 侧工具成为 SDD 的又一对接端。
   - "fix: clarify converge assessment of completion claims (#4621)"：SDD 工具在加固对"完成声明"的核查——恰是 marmelab 2025-11 "False Sense of Security" 记录的失败模式（agent 把 verify implementation 标 done 却零测试）。
2. **loop → SDD 方向（吸收 spec 为 feedforward，而非审批门）**：
   - Böckeler 的 guides/sensors 模型里，spec 是高自主用户的首选 feedforward guide（"Feed-forward: A functional specification (of varying levels of detail, from a short prompt to multi-file descriptions)"），不是阶段门；marmelab 2026 审计把 spec-kit（137k★）直接作为 harness 库存的 Orchestrator 类收录进 loop 阵营清单。
   - marmelab 2025-11 的批评实质是"功能位已被吞并"："Most coding agents already have a plan mode and a task list. In most cases, SDD adds little benefit."——loop 工具内置了 SDD 的核心产物，SDD 作为独立层被摊薄。
3. **不合并的证据**：SDD 未死（Spec Kit 2026-08-21 发 v1.0.0 后一个月内 12 个 patch 版本、OpenSpec 活跃双周发版）；loop 侧也无结构性领先（marmelab："The median repository in our inventory is 8.7 months old, so nobody has a structural lead"）。两侧共同收敛到的目标形态是同一个：**机械门（deny/hook/error/block）+ 少量真人判断点**（Stripe "errors block progress but warnings don't"；OpenSpec "critically unclear"；Spec Kit Governance presets；marmelab 12/391 的 deny 缺口数据反证行业还没做到）。

---

## 中文圈

### 7. alchaincyf 橙皮书（独立发明 or 转述？证据是什么）

（按父代理新标准降级处理：只定性，不深挖。）

- **URL**：https://github.com/alchaincyf/loop-engineering-orange-book
- **仓库描述（GitHub 页面）**："别再问我什么是 Loop Engineering — 橙皮书系列。A plain-language guide to loop engineering (中文 + English PDF). Free."
- **作者**：HuaShu（花叔）——README 自述 "AI Native Coder · Indie Developer"，"An AI content creator with 500K+ followers across platforms"（中文圈 KOL；X 账号 @AlchainHust）。**语言：中文为主（附英文 PDF）**。
- **版本（README 标注）**：v260615——"First edition, written the week loop engineering emerged (June 2026)"。
- **访问日期**：2026-09-26
- **定性证据（README 逐字）**：
  > "A plain-language field guide to **loop engineering** — the term that blew up in a single week of June 2026, when [Peter Steinberger](https://x.com/steipete/status/2063697162748260627), Boris Cherny (head of Claude Code at Anthropic), and Google's [Addy Osmani](https://addyosmani.com/blog/loop-engineering/) all pointed at the same shift and gave it a name."
  >
  > "**v260615** — First edition, written the week loop engineering emerged (June 2026), based on Addy Osmani's founding post and the official Claude Code / Codex docs."
  >
  > "All sources are public and first-hand: Addy Osmani's founding post, Anthropic's harness-design engineering blog, Stripe's Minions, and the official Claude Code / Codex docs."

- **一句话定性**：**是英文谱系的中文转述/编译，不是独立发明**——作者本人在 README 里明写初版"based on Addy Osmani's founding post and the official Claude Code / Codex docs"，并把术语起源完整归于 2026 年 6 月同一周的 Steinberger / Cherny / Osmani；书是他本人一手写的中文指南（中文一手、标注语言），概念谱系全部来自英文一手源。
- 附注（不深挖，仅记录可复用线索）：它顺带记录了 loop engineering 命名周的三个一手源 URL（Steinberger 推文、Osmani 的 /blog/loop-engineering/、Cherny 的头衔发言）——这些 URL 本身**未回源核验**，只作线索登记，不作证据。

---

## 不入册（按父代理 2026-09-26 标准）

- **HN 评论者言论**（yoaviram、gsadaka、sermakarevich、constantcrying、conartist6、cfunderburg 等）：随机论坛评论，不作 KOL 证据。本次回源**未采集**任何 HN 评论内容。
- **中文聚合媒体**（腾讯云社区《最近疯传的 Loop Engineering，是台印钞机，还是绞肉机？》等）：标题党，直接丢弃，未采集。
- 橙皮书引用的 Steinberger 推文 / Osmani《loop-engineering》founding post：未回源（橙皮书已降级），仅作线索。

## 负结论清单

1. **归属修正（最重要）**：任务线索把 "Most coding agents already have a plan mode and a task list. In most cases, SDD adds little benefit." 与 "False Sense of Security"（agent 把 verify implementation 标 done 却零单测）记在 marmelab《The State Of AI Harness Engineering 2026》（2026-09-24）名下——**两条均不在该文**（全文 grep "SDD / plan mode / task list / verify implementation" 零命中）。真正出处是 marmelab《Spec-Driven Development: The Waterfall Strikes Back》（2025-11-12），两条已在该文逐字核实（见对照面第 4b 条）。
2. **"False sense of control?" 的 URL 归属错误**：该设问不在 harness-engineering.html（2026-04-02），在 sdd-3-tools.html（2025-10-15，Böckeler《Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl》）。已在该文逐字核实（见问题 3 第 3 条）。
3. **"Agent = Model + Harness" 公式归属冲突**：marmelab 写 "a formula we owe to Birgitta Böckeler"，但 Böckeler 本人文章把公式链接到 LangChain《The anatomy of an agent harness》，Osmani 明写该 one-liner 属 Viv Trivedy 且"Viv Trivedy coined the term harness engineering"。一手链为 Trivedy/LangChain 原创 → Böckeler 传播锚点化；引用时不应把公式原创记给 Böckeler。
4. **未找到**："Agentic Flywheel" 作为独立提法在 Kief 文中存在（节标题 "The agentic flywheel"），但**未发现**任何一手源给出"跑几轮必须人看"的量化判据（轮次阈值类判据不存在）。
5. **未核验**（超出本轮范围/被降级）：OpenAI harness-engineering 原文（openai.com/index/harness-engineering/）、Anthropic 两篇 harness 工程文、Huntley ghuntley.com/ralph/ 原文、Osmani /blog/loop-engineering/（founding post）、Steinberger 推文——本轮只经 marmelab/Osmani/Kief 的转引层接触，转引句已在相应条目标注出处，如需上屏须另行回源。
   > ⚠️ **调和注记（2026-09-26 评审轮）**：本条是 **C 路视角**。其中 **Osmani 两篇与 Huntley Ralph 原文已由 A/B 路全文取得**（见 [evidence-a](evidence-2026-09-26-a-originators.md) / [evidence-b](evidence-2026-09-26-b-stop-and-scheduling.md)）；仍待回源的是 OpenAI harness-engineering 原文（openai.com 站点级 403）与 Steinberger 推文正文（X 不可达）——**以台账 §E 的负结论清单为当前态**（其中 Steinberger 推文正文已于 2026-09-26 晚升级为"经 Osmani 转引的逐字"，见 evidence-a 补充回源节）。另：:57 记其著作为《Beyond Vibe Coding》——经同晚补充回源裁决为**误**（正确书名《Agentic Engineering》，O'Reilly 链接实锤，见 evidence-a 补充回源节）。
6. **npm 包名陷阱**：npm 上的 `openspec` 包（latest 0.0.0）为无关占位包；官方包是 `@fission-ai/openspec`。"Agree before you build" 在官方包 README 中保留（逐字核实）。
7. **无 403/paywall 阻断**：本轮全部目标源正文均取得；唯一的技术障碍（stripe.dev JS 渲染、GitHub 页面截断）均通过页面内嵌 JSON / REST API 解决，内容仍为一手。
