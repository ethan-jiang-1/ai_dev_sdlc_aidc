---
type: cross_cut
directory: 02_neutral
observation_date: 2026-10-06
---

# _misc — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../01_seed_reference/voices/_raw_people/README.md)。

### Source E · 播客层群像（2026-06 后，按证据强度分档）

1. **Latent Space 2026-07-08**：Akshat Bubna（Modal CTO）《Why AI Infrastructure must evolve for Agent Experience》（58min）——经 SignalCast 周报页实取摘要（https://www.signalcast.app/this-week/latent-space/2026-07-06 ）："as AI moves from static model serving toward autonomous decision-making, the underlying platforms must fundamentally rethink how they allocate resources and handle unpredictable execution patterns."（**经摘要转述档**；latent.space 站内正文未取——sitemap/分页均 404）
2. **SE Radio 740**：Raju Dandigam《Building Production AI Agents》（2026-09，https://se-radio.net/2026/09/se-radio-740-raju-dandigam-on-building-production-ai-agents/ ，curl 实取官方简介）："The episode covers behavioral testing against contracts, golden scenarios, and observability that captures the full execution path rather than flat logs, which is the gap behind agent-inspect and its readable execution trees."（官方简介档；SE Radio 不附 transcript）
3. **SE Radio 732**：Jason Gorman《The Effective Use of AI For Software Development》（2026-08，条目级；正文未取）。
4. **Insecure Agents**（Socket 出品，host Allie Howe）：单集《A Reference Architecture for Securing "Software Factories"》（Aaron Stanley / Ahmad Nassri）与 David Cramer 单集（见怀疑档）——iHeart 406，日期未核。
5. **The Weekly Dev's Brew**（Jan-Niklas Wortmann，wordman.dev）：本轮播客层最大发现源——单集页自带 Key Takeaways＋Pull Quotes＋**页内全 transcript**；窗口内 loop 相关四集：Cramer（06-30）、Horthy（08-13）、Mulroy（09-10）、Shepherd（09-24）。主持人摘要语体审慎，可作"经主持人整理档"引用。


---

## community_tech 层

## 一句话总述

**社区主流不是两极，而是"要更自动，但要可停"**——行为上向 loop 迁移（使用率、委托比例都在涨），情绪上保留否定条款（成本、审批误伤）；机构采样证实"完全放手"仍是少数派行为。

### 五、通道与方法（本轮）

- github.blog WP API（`/wp-json/wp/v2/posts?slug=…`）畅通，为该站全文主力通道；Yale 报告主页静态可取且含采样期逐字段与勘误记录——调查类来源优先找报告主页而不止新闻稿。
- JetBrains research 原帖带浏览器 UA（Chrome/macOS）可直取全文，上轮"截断"疑为通道问题；research RSS 用于核对后续帖。
- SO/DORA/Octoverse 三快查各一 curl 记状态码（15:31 CST），未恋战。

### 五、媒体聚合层补点

**钛媒体专栏｜《[你还在手写 Prompt？聪明的人早就用上了循环工程，AI 的自动驾驶时代来了](https://www.tmtpost.com/8066456.html)》（"AI不是AI吧"，2026-07-16 08:10，自标全文 7303 字，正文实取）**——**编译+自写判定**（系统转述 Steinberger/Cherny/Osmani 与三阶段论）：

> "整个过程可以在无人值守的状态下持续运转，直到满足预设的退出条件，我愿称之为 AI 界的永动机。"（"永动机"用词自带反讽——标题正方、行文留刺）
> "三个阶段之间并非替代关系。好的提示词和充足的上下文依然有用，但它们已经从主要工程挑战变成了循环内部的子模块。真正决定产出质量的，是循环本身的设计。"
> Prompt Drift 中文化转述："很多团队甚至为提示词写了回归测试，像测试函数一样测试措辞，然后看着它们在每次模型升级后批量过期。"

（奇绩创坛同题镜像 news.miracleplus.com/share_link/136657 本轮 404 未取，维持开放。）

### 四、LangChain（LangSmith）：State of Agent Engineering 调查＋Open SWE 路由 A/B（自家 agent 成本分布）

**调查报告 [langchain.com/state-of-agent-engineering](https://www.langchain.com/state-of-agent-engineering)**（页面标注 12 June, 2026）。**样本口径**（Methodology 逐字）："a public survey that we ran for 2 weeks from Nov 18th-Dec 2nd, 2025. We received 1340 responses."（科技行业 63%、<100 人公司 49%；发布在窗口内，采样在窗口前——按页标注明）。

关键数据逐字：
- 落地率："More than half of respondents surveyed (57.3%) now have agents running in production environments, with another 30.4% actively developing agents with concrete plans to deploy them."（上年 51%）
- **质量是第一障碍**："Quality is the production killer, with 32% citing it as a top barrier. Meanwhile, cost concerns dropped from last year."；"Latency has emerged as second biggest challenge (20%)."
- **观测与评估的落差（把控性差的采纳率表述）**："Nearly 89% of respondents have implemented observability for their agents, outpacing evals adoption at 52%."；"89% of organizations have implemented some form of observability for their agents, and 62% have detailed tracing that allows them to inspect individual agent steps and tool calls."；已生产组织："94% have some form of observability in place, and 71.5% have full tracing capabilities."
- 评估成熟度："Just over half of organization (52.4%) report running offline evaluations on test sets"；"Adoption of online evals is lower (37.3%)"；生产组织中 "'not evaluating' drops from 29.5% to 22.8%"、在线评估 44.8%。
- **人在环比例**："human review (59.8%) remains essential for nuanced or high stake situations, while LLM-as-judge approaches (53.3%) are increasingly used to scale assessments."
- 大企业分层："Among enterprises (2k+ employees), quality remains the top blocker but security emerges as the 2nd largest concern, cited by 24.9% of respondents."

**实验博客《How to Build a Model Router in the Harness》**（[langchain.com/blog/how-to-build-a-model-router-in-the-harness](https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness)，datePublished 2026-10-01，作者 Sydney Runkle、Eugene Yurtsev）——**LangSmith trace 级一手数据**（其自家开源编码 agent Open SWE；任务分布窗口 "Aug 29 to Sep 5"，A/B 成本窗口 "Sep 16 to 22"）：

> "We pulled thread-level data from LangSmith traces: the kinds of requests coming in, plus the cost and turn count of each thread (as approximate measures of complexity)."
> 任务分布（一周交互线程，LLM 分类）："new features (22%) and bug fixes (17%) were the two largest groups, followed by test or no-op runs (16%)."
> A/B："half of threads went through the router, and half always used GPT-6 Astra, across 973 threads in total."；质量不降："29.2% of routed threads ended in a merged PR vs. 27.3% of control (p = 0.49). PR open rates were also flat (38.9% vs. 39.6%, p = 0.82)."
> **成本分布**："The median routed thread cost $0.94 vs. $2.61 on control, 64% less. The mean dropped 42% and the p90 dropped 37%, so the savings weren't just a few cheap outliers."；"Of routed threads, 56% went to balanced, 34% to fast, and only 10% to performance. The cost ladder between tiers is steep: the median thread cost $0.097 on fast, $1.50 on balanced, and $2.88 on performance, a 30× spread."
> 用户对超支的直接反馈逐字："pretty expensive for this query"／"this request should not have been routed to the performance model."
> 架构立场："An effective model router belongs in the harness, not a generic gateway. Choosing the right model requires domain and task context that the harness already assembles, and a gateway typically lacks."

（对位：**turn count 被明确当复杂度/失控信号用**（"a high count can mean a harder task or a model that needed follow-ups"）；成本分布 30× 阶梯＋路由省 64% 是"循环可以工程化调优"的正面一手量化。注意该文模型名（GLM-5.3-Flash / GPT-5.6 Sol / GPT-6 Astra）按页面原文照录。）

### 十、模型厂商公开用量统计：Anthropic Economic Index（OpenAI 无对应公开载体）

**Anthropic《Economic Index report: Learning curves》**（[anthropic.com/research/economic-index-march-2026-report](https://www.anthropic.com/research/economic-index-march-2026-report)，datePublished 2026-03-24）。**样本口径**："We sample 1 million conversations from both Claude.ai… and our first-party API… Our sample covers February 5 to February 12"（隐私保护聚合分型）。

- **官方交互分型里循环是一级类别**："we have classified conversations into one of five interaction types—directive, feedback loop, task iteration, validation, and learning—which we group into two broader categories: automation and augmentation."
- 走向："augmentation in Claude.ai increased slightly"；"we show that automation decreased sharply in the 1P API data."
- **熟练度与委托负相关（人在环的遥测证据）**："High tenure users are more likely to use Claude to iterate on their work, and much less likely to delegate greater responsibility through directive use patterns."；"people in this higher-tenure group have a 10% higher success rate in their conversations, an association that is not explained by their task selection, country of origin, or other factors."
- 编码工作流迁移："coding tasks continue to migrate from augmentative usage in Claude.ai to more automated workflows in our first-party API traffic… Claude Code has grown to represent a large share of sampled traffic."

**OpenAI：负结论**。usage dashboard 无公开统计载体；检索到的公开统计物为 cdn.openai.com 之 signals global report，**PDF 载体本轮未解析**（通道状态，不引数）。Anthropic Economic Index 是两家中唯一成体系滚动发布的公开用量统计。

### 十一、机构快查：Virtana 失败率调查（厂商利益相关，谨慎用）与 Grafana/Statsig/Helicone 负结论

- **Virtana《AI Is Breaking Human-Managed Operations》**（Business Wire 2026-03-10 发布；businesswirenews.com 与 tmcnet 转载页均 403，**经 Wedbush 投资者页转载全文实取**）。样本口径："an independent global survey of 351 senior IT and technology leaders"（100–10,000+ 人组织）。逐字：
  > "with 75% reporting AI job failure rates exceeding 10% and 33% experiencing failure rates above 25%, meaning one in four AI jobs fail."
  > "while 59% of executives believe their organizations are prepared for AI-scale operations, 62% of practitioners report fragmented systems and persistent visibility gaps."
  > "only 48% of practitioners… are confident their current observability tools can handle AI-scale workloads."
  > CEO 引语（把失败率接到循环后果）："At enterprise scale, these rates translate into thousands of failed executions per day, driving retries, wasted compute capacity, cascading delays, and escalating operational risk."
  **利益相关警示**：发布主体 Virtana 是可观测性厂商，发布日同步推出自家 Application Observability 产品；n=351 样本偏小——数字按机构采样层降权使用，且"AI job failure rate"口径未细分 agent 循环作业。
- **Grafana：负结论**。官方载体为 how-to 与 OTel GenAI 语义约定产品文（[grafana.com/blog/ai-observability-llms-in-production](https://grafana.com/blog/ai-observability-llms-in-production/)）；文中 "GPT-5 accounts for 70% of costs but only 20% of queries" 等出现在 Before/After 示例段，**属演示数值非遥测发现，不得引用**。未检索到 2026-06 后带真实数据的报告。
- **Statsig：负结论**。《Color commentary, Aug 2026》（datePublished 2026-09-10）仅方向性表述（"With MCP use steadily increasing…"），无数字。
- **Helicone：负结论**。一轮检索未命中 2026-06 后官方公开遥测统计（博客以教程类为主）；按两轮纪律登记，不再恋战。

### 四、《An agent used DNS to reach an external chatbot》（2026-09-26，198 分 / 189 评论）：kill-switch 延迟被社区逐帧讨论

**HN**（item 49853137；正文为某实验室事故 postmortem 引文，提交者 apsec112 逐字转贴）：

> "Incident timeline: 9:50:23 a.m. The agent made the DNS tool call that received an external response. 10:02:11 a.m. The monitoring system raised a P0 alert. 10:05:06 a.m. A human reviewer acknowledged the alert. 12:34:30 p.m. The run was killed."—— hn 用户 apsec112（转贴 postmortem）

> "The channel is always whatever primitive was left in the sandbox, not the one you thought you were guarding. Block fetch and the model finds the resolver. Block the resolver and something else is still leaking bits... The only version that holds is the one where the capability isn't there."—— hn 用户 sebastienburel

> "Once again... why are they not running these things in total airgap environments? I have to assume it's not incompetence at this point."—— hn 用户 voidfunc

**与 loop engineering 的挂钩**：P0 告警→人确认→**2.5 小时后**才 kill——社区逐帧引用的时间线给第四轮观测平台层（Sentry/Datadog"loop 过长/预算熔断"）补上了**熔断延迟的实测下界**；sebastienburel 的"能力不在场才算数"（capability absence, not permission）是**停止条件层级**（提示词规则→权限→能力移除）的社区级表述。
**对原内容的强化/反驳**：强化（第四轮"监测→熔断"链条的必要性被新事故验证）；同时给怀疑档供料（voidfunc 的"非无能即故意"）。

### 六、OpenAI《Dots: Always-on agents》（2026-09-29，768 分 / 647 评论）：常驻无人值守 agent 的产品化遭遇冷开场

**HN**（item 49896604；对应第四轮 Stratechery《Apps, Agents, and Aggregation》常驻 agent 基础设施叙事的社区反应）：

> "I cannot fathom how much compute will be wasted with that type of always on agentic systems"—— hn 用户 dgellow
> "Nope. If an AI agent can't intuit how I will feel about an action it's taking on my behalf, I'm not give it access to my digital life. OpenClaw, Muse, Dots... doesn't matter which one. All are an equally awful idea."—— hn 用户 jesse_dot_id
> "I wonder at what point they'll have to answer the inevitable question: 'why does the agent even need me anymore'?"—— hn 用户 realharo
> "It seems that this is the new primitive all AI vendors are converging onto next, first chat, then code, and now always-on Agents."—— hn 用户 rvshchwl
> "Ok but I want the time and attention so that I can do important work. What bizarre marketing."—— hn 用户 hankbond

**与 loop engineering 的挂钩**：①"always-on agent"产品化（第四轮 Stratechery 判定的无人值守基础设施条件）被厂商三连发（Muse/Dots/Grok Bot）坐实为**行业收敛方向**（rvshchwl 评）；②社区首批反应集中于**算力浪费**（dgellow——预算熔断面）与**意愿归属**（realharo——volition 稀缺论的民间版）；③768 分的热度说明无人值守运行已是 HN 大众议题而非常客话题。
**对原内容的强化/反驳**：产品事实强化、价值叙事反驳（"替你省时间"的营销被逐条吐槽——无人值守的**用户面**接受度尚无社区证据）。


---

## community_product 层

### 八、厂商产品面词汇锚（机构源，非 KOL 条目）：循环被翻译成"自主度开关＋聊天"

- v0 官方文档《Agentic features》（https://v0.app/docs/agentic-features ，curl 实取 2026-10-06）逐字："Every action runs inside an isolated sandbox, and you control how much autonomy v0 has."；"When v0 detects errors in your project, it can diagnose and fix them automatically as part of the generation loop."
- Lovable 官方博客《Inside Chats: How Lovable's Agents Work Together》（https://lovable.dev/blog/how-lovable-agents-work-together ，2026-09-24，curl 实取）要点逐字："Chats builds on infrastructure we originally developed for agents and subagents to work together."；"our Trajectory System appends roughly half a billion events, covering about 2.6 million user turns"；"activations arrange for them to run and pick up new work"；"Suspend and resume: agents that survive deploys"。
- **与 loop engineering 的挂钩**：反面钩（厂商锚）——no-code 产品把循环工程内容（多 agent 协同、迭代、暂停恢复、自主度控制）**全部以产品词发行**（autonomy 开关、generation loop、activations、Chats），其用户因此只接触产品面；Replit Agent 3 的"Max Autonomy"开关（2025-09-10 官方博客，早于窗口，仅作机制登记注记：`https://replit.com/blog/introducing-agent-3-our-most-autonomous-agent-yet`）是同一翻译策略的先例。
- **对原内容的强化/削弱**：中性（机制/词汇扩散证据；官方机构源不计 KOL 票，不与本档人群条目并列立票）。

### 九、分析层补点（第七轮 · 2026-10-07）：jwatte.com《Stop Prompting, Start Designing Loops》——词源推文的"诚实版"拆解（2026-06-16）

- URL：https://jwatte.com/blog/design-loops-not-prompts/ （curl 实取全文）
- 身份：J.A. Watte，独立技术写作者（SMB 受众、自家书推广站；页面自述"编辑日历定时发布"机制——**独立性打折标注**，③弱）。
- **挂钩**：**停止条件**＋**预算与熔断**＋**验证回路**（三段"去炒作"边界划定）；另涉**循环产品化机制**（Osmani 六原语的二手摘要失真校正）。
- 逐字摘录：

> "Loops without verification are just expensive prompt chains... If your loop has no verifier (no test suite, no lint pass, no diff review, no human checkpoint), it is not a loop. It is a fire hose."

> "A loop is not bounded. The whole point is that it runs on a schedule, fires off subagents, calls tools, retries on failure, escalates to bigger models when the small model gets stuck. Every one of those is a token-cost multiplier."＋结论句："**A loop without cost discipline is a self-inflicted denial-of-service attack on your own credit card.**"

> "The architecture has shipped, the security model has not."（供应链谱系注记〔窗口外〕：CVE-2026-25253〔2026-01〕与 ClawHub 341/2,857 恶意 skill 审计〔2026-02〕——窗口内机构层升级见怀疑档 [csa.md](../../03_skeptics/orgs/csa.md)。）

> **debunk 层（判读用）**："The 'OpenClaw was built in a single hour' story is wrong... The one-hour figure refers to Steinberger's original Clawdbot prototype in November 2025, not the production OpenClaw codebase"；Osmani 六原语中被二手摘要丢掉的恰是干活最多的两个："the scheduler that fires the loop without you sitting there, and the worktree"。
> （推动侧素材指针：Cherny 经 The New Stack/Office Chai 访谈——"I don't prompt Claude anymore... My job is to write loops."——推动档 Cherny 相关条目可引，本档只记指针。）

- **该条支持的最小主张**：对词源叙事的无条件背书有三处失真（一小时神话、无验证循环、安全模型缺位），被逐一划界；结论是教科书式中性口径——"Build the loop. Bound the cost. Verify the output. The rest is engineering."
- **派别适配**：**中性票（边界向，独立性打折）**。
