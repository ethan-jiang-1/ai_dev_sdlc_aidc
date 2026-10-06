---
type: event_evidence
directory: 01_advocates/events
observation_date: 2026-10-06
---

# aiewf_2026 — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

## AIEWF 2026 厂商群像——Warp / Factory / OpenAI / Cursor / Sierra（2026-06-30 现场报道）

- URL：https://www.latent.space/p/aiewf-daily-dispatch-loops （Latent.Space 本刊 Richard MacManus 现场报道，2026-07-01，全文取得）｜ 涉及人物：Zach Lloyd（Warp CEO）、Tereza Tížková（Factory）、Alexander Embiricos & Romain Huet（OpenAI Codex 团队）、Pauline Brunet（Cursor VP of Forward Deployed Engineering）、Natalie Meurer（Sierra Head of Agent Engineering）、Allie Howe（Keycard）、Peter Steinberger（OpenClaw，**现已入职 OpenAI**——报道原文 "the 'ClawFather' of OpenClaw, now working for OpenAI"）
- 来源类型：会议现场报道（latent.space＝swyx 自家刊物；引语为记者笔录的演讲原话——**转述级一手**：本人演讲、他人笔录）
- 号召力口径：②——各厂商负责人在 6000 人级会议主台把 loops/software factory 立为叙事主线

**逐字摘录**：

> "There will be a lot of talk today about loops. And if you can connect the agent to not only the work that you have to do, but why it has to be done, that's how you can get the agent to start to begin much more work. And then if you can connect it to what you do afterwards, review and deploy, that's how you help it land much more work." — Alexander Embiricos（OpenAI，Codex）
>（OpenAI 在大会把循环连接"为什么做＋事后评审部署"作为产能方法论主讲。）

> "She defined a software factory as 'the whole loop, the whole lifecycle of developing software with autonomy'… also 'collecting all the signals, reacting to user feedback to logs, prioritizing what's important, then orchestrating it all.'" — Tereza Tížková（Factory）
>（Factory 官方定义：软件工厂＝带自主性的整个开发生命周期循环。）

> "software engineering will become factory engineering… 'You'll be building the thing that builds the product.'" — Zach Lloyd（Warp CEO）
>（Warp 的激进重构宣言：软件工程将变成工厂工程。）

> "The way to think of the factory is, like, pick your repos, pick the parts of the lifecycle that you want to automate, pick the ways in which you want humans to be brought into the loop… different organizations and code bases will have different preferences for, like, do you fully automate code review or do you have humans do hard coding." — Zach Lloyd（对记者 booth 采访）
>（**难点自认**：Warp CEO 亲口说明工厂要"选人从哪里进环"——掌控面是产品参数而非默认取消。）

> "For better or worse, the power of these systems is so great and the ability to accelerate is so strong that just writing stuff by hand... I don't think it's going to make sense for very much longer." — Zach Lloyd
>（承认 "for better or worse"＋"factory 一词可能吓到开发者"的争议自认。）

> "We partner with your organization to co-design and co-build your AI software factory. We transform how you design, develop, and maintain software across your entire life cycle." — Pauline Brunet（Cursor VP FDE）
>（Cursor 的企业服务话术直接以 software factory 为轴——与 S5 changelog 互证。）

> "He added that deciding what to pay attention to is his main challenge nowadays — and that the future is 'better loops' to help solve this issue." — Peter Steinberger 现场发言转述
>（**Steinberger 的难点自认**：当下的主挑战是"决定关注什么"，答案是"更好的循环"——词源人物六月后的立场补强：仍推动，但问题意识转向注意力管理。）

- 注：Boris Cherny 的 AIEWF 登台句 "I don't prompt Claude anymore. I write loops, the loops do the work."（经 All Things Open 文转述）——词源句的**又一个现场流传版本**（02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-26-a-originators.md 与 evidence-2026-09-28 期 u 档的多版本对照表可增补：2026-06-30 AIEWF 台上版）。

**该条支持的最小主张**：2026-06-30 AIEWF 上 Warp、Factory、OpenAI、Cursor、Sierra 等厂商负责人集体以 loops/software factory 为主叙事——推动派在 6 月后完成了**会议级厂商合流**；且多位演讲者当场给出"人从哪里进环"的掌控面表述。
**派别适配**：**推动票**（厂商群像；单人引语为笔录转述，入册时按"本人演讲·经转述"降半级标注）。

---

### AIEWF 2026 官方议题群像（llms-full.md 全量页实取，https://ai.engineer/worldsfair/2026/llms-full.md）

- 官方摘要逐字可引的 loop 议题（讲者均为**非在册新名**）：
  1. **Joel Hooks**《The Art and Science of Loopcraft with Pi (and friends)》（Workshop，4:30pm-5:30pm）："This workshop helps agentic coding practitioners stop treating agents like pretend coworkers and start designing reliable, compounding loops. Using Pi as the concrete demo surface, Joel Hooks will show how loop state, handoffs, review, memory, and operator control become visible…"
  2. **Fuad Ali**《Building self-learning loops for your agent》（Workshop，11:05am-12:05pm）。
  3. **John Craft（Docker）＋Dan Ndombe**《From approval loops to autonomous agents with Docker》（Workshop＋Session Day 共 6 段连讲）："unlocking autonomous development without creating security headaches, governance gaps, or endless approval loops."
  4. **Andrew Orobator**《Spin at the Gate Until Green: The Engineering Primitives Behind Self-Driving Codebases》："If you can express correctness as a binary — does it compile, do the tests pass, does the lint check clear — you can remove the human from that loop entirely. The AI submits. The gate checks. If red, it adjusts and resubmits. Spin at the gate until green."＋"The culmination is a flag lifecycle agent — triggered by a cron job…verified by compile + test + lint, no human in the loop."
  5. **Anirban Chatterjee（Sonar）**《Guide, Verify, Solve: The Engineering Discipline Agentic Development Demands》："Sonar's Agent Centric Development Cycle (AC/DC), a three-stage continuous loop of Guide, Verify, and Solve."
- **最小主张**：AIEWF 2026 上 loop engineering 已是"Workshop＋Session"双层的正式教学科目——以 loop 专名或 loop 原语组织的议题至少 6 个（不含已在册的 swyx《The Highest Loop》）。
- **派别适配**：**推动向会议层群票**（官方摘要级，讲者个人一手未取者不入个人条目）。

### AIEWF 2026 loop 议题官方编辑稿群像（增量 L 的深化，讲者一手逐字已入上列者不重复）

官方摘要/分节/要点层可直引的补充议题（全部 curl 实取官方页）：
1. **Itamar Friedman（Qodo CEO）**《The Last Human Code Review》（上传 2026-08-20，https://ai.engineer/talks/s-aixZYJG4c-last-human-code-review-building-trust ）：现场逐字 "Is human code review still optional end of twenty twenty-six?"；双功能框架 "One is we wanna validate the code… The second reason is actually alignment and learning"；"You need to think what's your philosophy because that will lead you to different milestones or different tools that you need to use in order to get that confidence that you can skip over a human review"——**挂钩：验证回路**。推动票（会议层，KOL ③弱）。
2. **Ankit Jain**《How to Kill the Code Review》（上传 2026-08-17）：分节 "Turn repeated comments into reusable checks""Build the register before retiring the ritual"——**挂钩：验证回路**。会议层样本。
3. **《Building an Autonomous Engineering Org》**（https://ai.engineer/talks/whue9_YquGA-building-autonomous-engineering-org ）——**挂钩：外层调度**。会议层样本。
4. **《Stop Burning Tokens: Why self-improvement needs domain expertise first》**（eAXxdtNlK04）——**挂钩：预算与熔断**（自改进的经济学节制）。会议层样本。
5. **《Your Agents Need a Save Button》**（bZISsg7H7DA）/《Agents Need Feature Flags》（zU4EagB311U）/《Agents Need Receipts, Not More Tool Calls》（Fu45geO3zX8）——三连"控制面板件"议题：存档回滚／灰度开关／可审计凭据——**挂钩：预算与熔断＋停止条件**。会议层样本。
6. **Simulation-Maxxing（Nubank）**（KMR_RBoCa4M）：官方分节 "Run the real agent inside a simulated environment""Check whether simulation tracks production"——**挂钩：验证回路**（仿真闭环）。会议层样本。
7. **Uber 双讲**：《Agentic SDLC at Uber》（17-YSUHo6Lk）＋《Building uReview, Uber's Multi-Agent Code Review Engine》（EL123UNokkI，上传在库页实录）——**挂钩：外层调度＋验证回路**。会议层样本（甲方）。
8. **Erik Meijer**《In Code They Act, In Proof We Trust》——形式化验证入环——**挂钩：验证回路**。KOL ①（语言学界名人）。
9. **Cornelia Davis**《MCP Tasks (async)/ Why the heck aren't any agents supporting MCP tasks/async?》——异步任务原语缺位之问——**挂钩：循环结构（协议层）**。会议层样本。
10. **Dominik Kundel**《Building on the Codex Harness》＋Ignacio Martinez《Total Recall: Agent Memory and Harness Engineering》＋Robert Brennan《Sandboxes Aren't Optional》＋Abhishek Bhardwaj《From fork() to Fleet》——harness/沙箱基建群像——**挂钩：循环结构（环境层）**。会议层样本。
### Source F · 会议层数据点（AIEWF 2026 官方全量页＋现场稿）

- **Barr Yaron（Amplify）年度调查**（经 MacManus 现场稿转述）："According to Amplify's data, 95% of respondents now use agents — roughly double last year's share. Among teams using agents, 89% said those agents could write data, up from 52% the previous year."＋"The controls, however, remain comparatively primitive. Human approvals and permissions were the two leading safeguards…"
- **Allie Howe（Keycard）主持设问**（现场稿直录）："is there or is there not a delta between the hype behind loops and what actually works in practice?"
- **Ameya Bhatawdekar**《Your Agent Evolved. Your Evals Didn't.》（llms-full.md 官方摘要实取）："Agent architectures have evolved through six generations; prompt, chain, ReAct loop, workflow graph, modern agent loop, AI harness. And each one quietly breaks the eval strategy of the generation before it."（六代架构谱系句——判读层可用的官方分期表述）
- **Sonar AC/DC**（Anirban Chatterjee）官方摘要（同页实取）："the critical challenge has shifted from generation to verification…making cognitive surrender among human reviewers an acute risk."（"cognitive surrender" 在会议层官方摘要中出现）
- **派别适配**：中性（数据与设问层，非个人 KOL 票）。

### AIEWF 2026 evals/验证层中性群像（官方编辑稿层，curl 实取）

1. **Lukas Petersson（Andon Labs）**《Vending-Bench: Long-Horizon Agent Evals》（上传 2026-07-24，https://ai.engineer/talks/cO8qC6HBuBg-vending-bench-long-horizon-agent-evals ）——官方分节："Misbehavior without an instruction to misbehave""When the agent treats the customer as simulated""No observations are not evidence of no demand"——长程自主行为的评测边界。**挂钩：验证回路**。
2. **Rishi Desai（Abundant AI）**《SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale》（Rx8f05JI_WA）——官方分节："A weak verifier becomes an attack surface""Large token budgets do not establish project ownership""Distinguish attempted shortcuts from rewarded exploits"——九小时级长任务的验证器弱点论。**挂钩：验证回路＋预算与熔断**。怀疑派亦可引。
3. **Ameya Bhatawdekar**《Your Agent Evolved. Your Evals Didn't.》（nxokqOq1imY）——官方分节："The loop returns, and evaluation becomes a distribution""Production must keep changing the evaluation suite"——评测随循环结构漂移。**挂钩：验证回路**。
4. **Sachin Gupta（eBay）**《ReviewDebt: a practical framework for scoring every pull request》（TJPInBjhE4Q）——官方分节："Code production can outrun review""Volume accumulates burden even when authorship markers stay flat"——review 背压的量化（与 Mistele 的 review 背压主张互证）。**挂钩：验证回路＋停止条件**。
5. **《Benchmarks: The Good, the Bad, and the Ugly》（Ali Khial）**——评测批判层。**挂钩：验证回路**。
