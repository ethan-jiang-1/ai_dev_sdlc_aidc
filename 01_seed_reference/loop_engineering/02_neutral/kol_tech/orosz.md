---
type: kol_evidence
directory: 02_neutral/kol_tech
observation_date: 2026-10-06
---

# orosz — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：同上
> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**方向**：审慎加深（观察者→调查式怀疑）
**起点**：观察者·损失感（grief）
**终点**：调查者·怀疑（'here today, gone tomorrow?'）
**弧线**：01-07 grief（'something valuable is being taken away'）→ 07-14《What is loop engineering?》调查（cron 旧物、tokenmaxxing、'Was looping a hack?'）
**关键转折**：07-14 从个人情绪表达转为系统性调查——发现多数用例是旧物重贴标签
## 《What is "loop engineering?"》（2026-07-14）

- URL：https://newsletter.pragmaticengineer.com/p/what-is-loop-engineering ｜ 作者身份：同上
- 来源类型：newsletter 一手（**截断**：§1–4 全文取得；§5–7 在付费墙后未取得，但其大纲句在公开目录中逐字可见）。副标题即怀疑定调："Is it a 'here today, gone tomorrow' trend?"
- 号召力口径：同上。

**逐字摘录**（公开部分）：

> "5. **Disappointment and 'tokenmaxxing'**. Several devs reject looping after trying it. Agents drifting, and the 'human in the loop' having better results are some reasons. Also, at companies that pay API prices for tokens, loop engineering gets expensive fast."
（§5 大纲句（逐字）：试用后放弃、agent 漂移、人在环反而更好、API 计价下成本失控——四条社区负面结论的浓缩。）

> "6. **Was looping a hack while tooling caught up?** Distinguished engineer Max Kanat-Alexander believes the 'loop' might have just been a temporary hack while the harnesses added the ability to do the same from a single prompt."
> "7. **Does 'context engineering' matter more for devs?** Except for engineers building AI infra, there seems little benefit in going deep into loop engineering."
（§6–7 大纲句（逐字）：loop 可能只是工具成熟前的临时 hack；除 AI 基建工程师外深入研究 loop engineering 收益甚微。）

> "The name suggests simplicity and repetition. Sometimes it feels like AI enthusiasts forgot automation was a thing before LLMs."
（受访者 Oded Messer，engineering director——经 Orosz 一手访谈转引，按纪律计为"Orosz 一手文内引述的从业者证词"，不单列 KOL。）

**该条支持的最小主张**：Orosz 基于 ~210 条从业者回复的独立调查得出：多数 loop 用例本质是 cron/trigger 旧物；试用者中不少人放弃；成本与漂移是主要弃因；对普通软件工程师，/loop、/goal 内建后"loop engineering"近似过时。（§5–7 结论句与其后被 arXiv 2608.21884 论文独立转述，见旁证节——两源互证。）
**派别适配**：部分票（对词本身的"新瓶旧酒"判定＋对价值的保留态度；但他同时如实收录了有用的 loop 案例，不是全面否定）。

---

# 增量补挖（2026-10-07 第二轮：08-10 月后续各期——未再专文，但每期都在供弹药）

> 通道：newsletter.pragmaticengineer.com 文章页与 RSS 逐期实取＋The Pulse 免费期 blog 镜像；付费墙截断逐条标注（OpenAI factory 截于第 4 节、Ramp/code reviews/Shopify RN 截于后文）；X 登录墙（JS 壳页无帖子正文），如实记录；Substack archive API 两页覆盖 2026-06-16→10-06 期次无缺漏。

## 《From Chrome DevTools to AI Engineering, with Addy Osmani》（播客 show notes，2026-08-19）

- URL：https://newsletter.pragmaticengineer.com/p/from-chrome-devtools-to-ai-engineering （show notes 页实取）
- **与 loop engineering 的挂钩**：**循环结构**——为 Osmani 的 loop engineering 方法单设播客章节（1:05:52）并回链自己 07-14 的定义篇。
- 逐字摘录（show notes）：

> "We also get into how he works with AI agents today, the risks of 'cognitive surrender,' his approach to 'loop engineering,' and why it's good to develop skills in product management, go-to-market, and other areas."

> "1:05:52 Loop engineering"

> "Help the agent improve throughout the task by having it log its decisions and key learnings"
（命名运动发起人被他请上播客单设 loop engineering 章节、双向交叉引用定义篇——持续为该词造势。）

- 立场：**支持**。

## The Pulse：《We need to talk about migrations with AI》（2026-08-20）

- URL：https://blog.pragmaticengineer.com/the-pulse-we-need-to-talk-about-migrations-with-ai/ （blog 免费镜像实取；newsletter 08-20 首发、blog 08-27 放出）
- **挂钩**：**循环结构＋验证回路＋无人值守**——Airbnb/Asana 靠自建重试循环连续跑 4 天完成迁移；他把共性总结为 design verification loops。
- 逐字摘录：

> "Airbnb's team had to build loops to keep retrying migrations; once they did, 75% of files were migrated in just four hours, and the migrations were straightforward."

> "They then built a more sophisticated refactor pipeline for the remaining 25% of tests; after building the pipeline, the new loop migrated most of the remaining tests (97%) in total, after running over 4 days."

> "The shared characteristic of all the above migrations is that engineers needed to plan for it, design verification loops, and be involved throughout."
（**design verification loops**——他的循环方法论关键词；且"人全程参与"是前提。）


- 立场：**支持**。

## 《Why Ramp built its own in-house coding agent, Inspect》（2026-08-25）

- URL：https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect （前半免费实取，付费墙截断已标注）
- **挂钩**：**验证回路＋循环产品化机制**——Inspect 以 "close the loop" 自证变更可用，被视为自建 harness 领先第三方的核心差异。
- 逐字摘录：

> "Inspect verifies all its changes. As a remote development environment with full tooling access, it can "close the loop" and confirm the changes it makes work:"

> "At present, most third-party AI harnesses cannot do these kinds of verifications 'out of the box' because they lack internal integrations with things like telemetry and feature flag systems."

> "Things like this placed Ramp months ahead of nearly all AI coding harnesses, and they could also build a far better feedback loop in their own harness."
（验证回路能力＝自建 harness 的胜负手——loop engineering 核心主张的头部案例。）


- 立场：**支持**。

## The Pulse：《tech companies move to open AI models》（2026-09-03）

- URL：https://blog.pragmaticengineer.com/the-pulse-tech-companies-move-to-open-ai-models/ （blog 免费镜像实取）
- **挂钩**：**预算与熔断**——Uber 撞穿年度 AI 预算后，按开发者月度限额、模型路由、自动压缩等控费机制成为行业回应。
- 逐字摘录：

> "Uber managed to blow through its annual AI budget in the first three months of this year"

> "Setting per-developer monthly AI usage limits"

> "Uber cut the cost per AI request by 34%, and the cost per AI session by 52%"

> "trigger automatic compaction above 400K tokens, even for models with 1M context windows"
（预算撞穿→限额与路由熔断式优化的行业样本，如实通报。）


- 立场：**中性（行业侧写）**。

## 《What is happening with code reviews?》（2026-09-08）

- URL：https://newsletter.pragmaticengineer.com/p/what-is-happening-with-code-reviews （前半免费实取，付费墙截断已标注）
- **挂钩**：**停止条件**——评审循环里 break the loop 与 exit criteria 由人拍板。
- 逐字摘录：

> "Vendors and home-grown solutions can instruct agents to update PRs with fixes and then re-trigger reviews – if you trust agents to make sensible fixes, that is!"

> "either repeat or break the loop (likely a human decision)"

> "So basically, 90% is left to agents, with humans in the loop for critical scope decisions and exit criteria."

> "There's more talk about dropping human code reviews than there is evidence of this actually happening, so far."
（循环可自动化但出口归人；且对"全自动评审"叙事的证据质疑。）


- 立场：**复合**。

## 《Building Codex with Tibo Sottiaux》（播客 show notes，2026-09-09）

- URL：https://newsletter.pragmaticengineer.com/p/building-codex-with-tibo-sottiaux （RSS 全文 show notes 实取）
- **挂钩**：**循环产品化机制**——Codex harness 以 "crutches" 策略随模型进步而收缩，循环载体的演进方法论。
- 逐字摘录：

> "The harness provides the model with crutches: guardrails, safety, efficiency, steerability, and the developer message injected into context at the start of each turn."

> "As models improve, some "crutches" are discarded and the harness shrinks. This has been the development cycle between Codex and OpenAI's new models to date."

> "Maintenance tasks like dependency upgrades can be handled by a model blasting through the codebase within a couple of hours."
（harness 收缩循环——与 Osmani"agent not only needed far less human instruction, it was actually being damaged by overly prescriptive humans"同谱系。）


- 立场：**中性**。

## 《Inside OpenAI's agentic software factory》（2026-09-15）

- URL：https://newsletter.pragmaticengineer.com/p/openai-software-factory （第 1-3 节实取，付费墙截断于第 4 节起，已标注）
- **挂钩**：**无人值守运行＋停止条件＋验证回路**——/goal 到完成才停、Perf Factory 生产信号回流开发、Sevbot 无人值守愿景与"oncall 仍在"的现实边界。
- 逐字摘录：

> "OpenAI added the /goal setting to Codex, where you can set up a goal for the agent and it keeps working until it is complete."

> "OpenAI has built a "software factory" with several automated, agentic feedback loops: for example, Perf Factory monitors production and kicks off Codex agents to automatically fix performance issues."

> "The dream is that no humans be woken up outside of their working hours during an outage because Sevbot can handle "routine" outages autonomously, with humans reviewing its actions when they return to work."

> "But as of now, oncall duty is not a thing of the past at the company."
（无人值守愿景与现实校准并陈——他自己的怀疑注记。）


- 立场：**复合**。

## 《AI Skills with Matt Pocock》（播客 show notes，2026-09-17）

- URL：https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock （show notes 页实取）
- **挂钩**：**外层调度＋无人值守**——day shift/night shift 分档调度、关机后云端 agent 续跑、agent 自证产出。
- 逐字摘录：

> "Matt explains his "day shift" and "night shift" approach, why splitting context up can keep agents in their "smart zone," and how concepts from classic software engineering books can guide agents to do better."

> "Matt is moving his coding sessions to cloud agents because doing so means agents run when he closes his laptop and cloud agents can be made "multiplayer" (collaborative) in ways that local agents cannot."

> "However, agents have longer context windows, so Matt has started to ask agents to produce proof that their code works – with or without TDD."

> "Everything is a Ralph loop: https://ghuntley.com/loop"
（参考文献收录 ghuntley 的 Ralph loop 文——原语引用链在主流 newsletter 的落地。）


- 立场：**支持**。

## 《Why has Shopify dropped React Native?》（2026-09-29）

- URL：https://newsletter.pragmaticengineer.com/p/shopify-native-mobile （前半免费实取，付费墙截断已标注）
- **挂钩**：**验证回路**——headless 共享测试套件给双端 agent 快速反馈回路。
- 逐字摘录：

> "We now have one shared test suite that validates business logic implemented in both Swift and Kotlin. This means that a feature can't ship until it passes the exact same tests on both platforms."

> "That logic runs headless on desktop, which gives agents a very fast feedback loop to iterate on."

> "Smart! It also confirms my sense that verifying code is becoming very important for working with agents, as is building dedicated verification layers."
（他本人直接表态：专用验证层正在成为与 agent 协作的通用前提。）


- 立场：**支持**。

## 《The state of the tech industry in 2026》（2026-10-06）

- URL：https://newsletter.pragmaticengineer.com/p/the-state-of-the-tech-industry-in （年度免费长文实取全文）
- **挂钩**：**循环产品化机制**——自建 harness 已成中大型公司标配、云端循环将统治、agentic evals 进 CI/CD、agentic observability 成新品类。
- 逐字摘录：

> "I asked it because most mid-sized-and-above companies have built their own agent harnesses, at this point!"

> "Cloud coding agents + harnesses will dominate. Most devs at companies will run AI agents in the cloud, instead of locally."

> "I'd also add that IDEs need to evolve into a validation and verification interface: how do we know that the agents' output works as expected, how can we verify what tests it passes"

> "Agentic observability will surely become its own problem space and specialization: how can we make sure that the customer-facing agents deployed work as expected, and how to ensure that systems which agents build and modify actually work as expected?"

> "CI/CD, with agentic evals part of the pipelines"
（年度报告把循环基础设施列为行业主趋势——循环产品化的行业级确认。）


- 立场：**支持**。

**本轮最小主张**：Orosz 07-14 定义篇后未再专文写 loop engineering，但 08-10 月每期都在供弹药：验证回路（Ramp/Shopify/迁移篇）、无人值守与外层调度（Pocock 昼夜分档、OpenAI /goal 与 Sevbot）、预算纪律（Uber 撞穿预算后限额）、产品化（人人自建 harness、年度报告立为主趋势）。总体支持，但坚持人工出口（"break the loop likely a human decision"）与现实校准（"oncall 还在"）。
