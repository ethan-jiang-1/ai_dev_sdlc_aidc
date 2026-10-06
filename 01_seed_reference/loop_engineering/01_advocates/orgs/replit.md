---
type: org_evidence
directory: 01_advocates/orgs
observation_date: 2026-10-06
---

# replit — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

### Replit —— 解决·强（Masad CEO 署名 07-16＋core loop 工程文 09-29＋评测 loop 文 06-23＋官方 docs）

- **B1. Amjad Masad（CEO）署名《The Self-Driving Company》**
  - URL/日期：https://replit.com/blog/self-driving-company ；datePublished **2026-07-16T17:01:00Z**（页面 JSON-LD＋页头 "Published: Jul 16, 2026" 双确认）；署名 **Amjad Masad, Scott Kennedy**（页面实取）。通道：curl＋浏览器 UA 直取全文。
  - 逐字摘录：

> "In the past six months, engineers at Replit have nearly tripled code output. Review times held steady. Reversions and product incidents have stayed flat. Quality metrics improved, and releases have accelerated."

> "Agents now investigate production incidents, review pull requests, answer questions, analyze business data, triage support tickets, research sales accounts, and improve the systems that power Replit Agent itself."

> "It is an expanding system of agents operating across the company: taking goals from people, gathering context, performing work, checking the results, and escalating when human judgment is needed. We think this represents the beginning of a new kind of organization: the self-driving company."

> "A self-driving company is not one without people. People still choose the destination. They decide which problems matter, make difficult tradeoffs, exercise taste, and take responsibility for the outcome. But increasingly, they do not perform every step required to get there."

> "We leveraged our agent harness, microVMs, and remote filesystem infrastructure so any engineer could orchestrate swarms of agents in parallel. Then we locked the whole thing behind access policies, token proxies, audit logging, and our ZeroTrust network."

> "People don't feel like they've been automated. They feel like they've been promoted."

  - **该条支持的最小主张**：任务 2 的核心交付——Masad 本人在 2026-06 后对 agentic loops 的署名定义是"目标→取上下文→执行→查结果→需要人判断时上报"的公司级 agent 环系统（"self-driving company"），并把"escalating when human judgment is needed"写进定义本身。
  - 派别适配：**推动·厂商**（公司级 loop 组织论；"人保留 destination/taste"的 nuance 与推动派"人做 spec/审查"谱系一致）。

- **B2. 官方工程博客《Free the models: Harness design at the frontier》**
  - URL/日期：https://replit.com/blog/free-the-models ；**2026-09-29**（datePublished＋页头双确认）；署名 Daniel Furman, Jacky Zhao, Vaibhav Kumar, Ed Sioufi, **Michele Catasta**（Replit 总裁，页面实取）。
  - 逐字摘录：

> "The main agent, or core loop, chooses its subagents' tier and effort, and adjusts its own as the task unfolds."

> "Model routers are everywhere right now, but they have a fundamental limitation. … a router will always be less capable than the model it's choosing for. Replit Agent lets the model decide instead."

> "The harness offers the options and keeps the guardrails; at every step, the core loop decides."（Figure 1 小标题："the three decisions the core loop makes at every step"——how hard to think / when to hand work off / who to hand it to）

> "As models become stronger at long-horizon tasks, they don't need as much scaffolding at the harness layer. In practice, we've observed them lean more towards delegation on their own: using subagents for context management and parallelism."

> "It also beats a sidekick architecture, the same setup with one long-lived worker, by 11 and 16 points."

  - **该条支持的最小主张**："core loop"已被厂商用作正式产品/架构词（主 agent 即"环"，环自己在每步做三个决定）；harness 哲学是"环做决定、harness 供选项与护栏"。
  - 派别适配：**推动·厂商**（且与 Steinberger "design loops that prompt agents" 词族直接同构）。

- **B3. 官方工程博客《Evaluating and improving agent at scale》**
  - URL/日期：https://replit.com/blog/evaluating-and-improving-agent-at-scale ；**2026-06-23**（Published Jun 23, Updated Jun 24，页面实取）；署名 Daniel Furman, Peter Zhong, Zhen Li, Michele Catasta。
  - 逐字摘录：

> "To answer that question, evaluation must become part of the improvement loop."

> "The old evaluation job ends at a human shipping decision; the new one feeds a continuous system that learns from production and ships improved agents."

> "The system has two measurement pillars and one optimization loop."＋"Human judgment keeps the improvement loop pointed at the right product and engineering outcomes."

  - **该条支持的最小主张**：厂商把 eval 本身重构成"改进环"的一环（评测→生产信号→回流）——loop 话语从"写码环"扩张到"评测/运维环"。
  - 派别适配：**推动·厂商**（对 goal/eval 主题的厂商面佐证）。

- **B4. 官方文档《Build in parallel》（docs.replit.com，living docs，实取 2026-10-06）**
  - URL：https://docs.replit.com/learn/build-in-parallel
  - 逐字摘录：

> "Building in parallel is a different relationship. You hand a feature to Agent as a task, and it goes off and builds it in the background while you do something else."

> "This changes your role. You stop being a passenger watching one build and become the director of several."

> "Your plan controls how many background tasks can run at once. Additional tasks queue and start as slots become available."

  - 边界面引句（"When to stay sequential"整节）见怀疑面文件增量 E。另：Replit Agent 4 发布（2026-03-23，官方博客实取）在窗口外，仅备注其并行任务系统为 B4 的产品底座。
  - **该条支持的最小主张**：并行无人值守任务（后台任务＋并发上限排队）是 Replit 官方文档化的工作方式，且官方同时文档化"何时不该并行"。
  - 派别适配：**推动·厂商**＋自认边界（分列）。
