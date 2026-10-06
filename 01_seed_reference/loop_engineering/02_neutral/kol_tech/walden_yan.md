---
type: kol_evidence
directory: 02_neutral/kol_tech
observation_date: 2026-10-06
---

# walden_yan — loop engineering 证据轨迹（2026-06 后，时间正序）


> **背景**：Walden Yan——Cognition（Devin 制造商）联合创始人兼 Chief Product Officer；高中经 MIT PRIMES 做程序合成研究，2020 入 Harvard（CS＋经济）同年获 IOI 金牌（全球第 19），2023 退学与 Scott Wu、Steven Hao 创办 Cognition，2024-03 发布 Devin；《Don't Build Multi-Agents》（2025-06）作者——单线程 agent＋上下文工程原则立场。（履历核：ai.engineer 讲者页＋Latent Space 访谈，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——当前库存不足以判弧线，待补挖（补挖 agent 在跑，新发声到位后本节升级为完整轨迹）。
## Walden Yan（Cognition）窗口内复核

- 库内已有：2026-04-22《Multi-Agents: What's Actually Working》全文（evidence-u S2）。**本路复核结果：2026-06 后 Walden 无新的专门一手文**（Cognition 博客以 latent.space 访谈为最新大动作）。
- 本路取得的相邻票：Latent Space《The Age of Async Agents — Cognition's Walden Yan & OpenInspect's Cole Murray》（2026-05-28，词源周前，https://www.latent.space/p/cognition ，页面全文取得前段）。**注意窗口外**，仅作谱系补充：
  - 页面内嵌 Walden X 帖（2026-04-22，经 latent.space 嵌入转引）："A year ago, I'd tell people to not build multi-agents and to focus on context engineering fundamentals. Today, many sexy ideas are still impractical, but we've found some setups that actually work"（"sexy ideas are still impractical" 是中性派语体，但他谈的是自家产品形态）。
  - 页面编辑摘要（swyx 撰）列出对谈主题含 "Why pure auto-merge vibe coding breaks down after about two weeks" 与 "the real failure mode of uncontrolled vibe coding: your codebase regressing to your worst engineer"——**这两句是 swyx 的编辑摘要语，非经核实的 Walden 逐字**，引用必须标"经 swyx 摘要转述"，不得入 Walden 引句。
- **派别适配**：受约束形态的代表性人物（写入单线程/manager 拓扑），但作为 Cognition CPO 其发表带厂商利益；归"偏推动中的受约束支"或单列，由判读层裁定。中性票**不足**。

---

---

# 增量补挖（2026-10-07 第二轮：09-10 月 Cognition/Devin 官方立场）

> 通道：cognition.ai/blog 与 devin.ai/blog 文章页逐篇实取＋docs.devin.ai release notes 滚动页实取。**延续上轮结论：Walden 本人 06-07 后仍无一手长文**（个人署名通道无新文；本轮所收全部为 Cognition/Devin 公司级官方发声，RSA-260 署名 Eric Lu），但 09 月起公司工程叙事密集且全部挂七类钩。

## 《Do it all with Devin: Announcing our Series E》（2026-09-08）

- URL：https://cognition.ai/blog/series-e （官方博文实取；Cognition Team 署名）
- **挂钩**：预算与熔断＋外层调度——宣言称 compute budgets 将 self-allocate、人作为 architect 只定目标与优先级。
- 逐字摘录：

> "In this next chapter, agents will become proactive by default, software will improve itself, and even resource allocation will become intelligent as compute budgets self-allocate toward the highest impact use cases."

> "Human engineers will increasingly act as architects, setting goals and priorities while agents take on more of the work to achieve them."

> "We believed engineers should operate more like architects and delegate execution to swarms of agents."

> "Devin Automations let teams configure work to begin from events in Slack, GitHub, Linear, and other systems, without opening a chat for each task."
（事件驱动无人值守是产品既有能力；愿景新增"预算自分配"。）

- 立场：**支持（公司愿景）**。

## 《Factoring RSA-260》（2026-09-09）

- URL：https://cognition.ai/blog/factoring-rsa-260 （官方博文实取；作者 Eric Lu——Cognition 研究者一手复盘；HN 讨论已核，作者未在 HN 发言）
- **挂钩**：**无人值守运行＋验证回路＋停止条件**——Devin 群自主跑数周、人只设基准与纠偏，prompt 内嵌 "Iterate until" 停止条件，且作者诚实标注自主边界。
- 逐字摘录：

> "My role was primarily to set priorities, establish benchmarks, and recognize when work was going off-track. Devin otherwise autonomously handled measurements, cluster operations, and optimization end-to-end."

> "Iterate until you exceed the performance of the CPU lattice siever."
（停止条件写进 prompt 的原句。）

> "Then I went to bed. I woke up to find that, after another 7 hours of iteration, Devin had succeeded."

> "I interacted with this optimization loop once every couple of hours, alternating with talking to other Devin sessions for my regular work."

> "But I cannot claim that Devin iterated autonomously on the entire end-to-end pipeline. It is interesting to consider what he needed me for."
（诚实边界：自主叙事与实际人机交互频率并陈——09 月最硬的 loop 工程一手样本。）

- 立场：**复合（展示极限＋坦承仍需人）**。

## 《Introducing SWE-2: Pushing the Pareto Frontier》（2026-09-10）

- URL：https://cognition.ai/blog/swe-2 （官方博文实取）
- **挂钩**：**预算与熔断**——reasoning-effort 档位即预算旋钮，训练用线性 cost penalty 直接优化成本-性能前沿。
- 逐字摘录：

> "this led to user feedback that SWE-1.7 tended to over-explore and overthink on simple tasks"
（对"过度探索"的官方承认——循环空转问题的模型层治理。）

> "SWE-2 medium scores higher than SWE-1.7 while taking 58% fewer turns and costing 81% less on average."

> "We apply a linear cost penalty per effort level in a single RL run, with each penalty tuned to the local slope of the base model's Pareto frontier."
（把"按档位预算、少绕路"做成训练目标。）

- 立场：**支持（成本控制工程化）**。

## 《Introducing Fusion in Devin Desktop & CLI》（2026-09-11）

- URL：https://cognition.ai/blog/local-fusion （官方博文实取）
- **挂钩**：**验证回路＋外层调度**——lead 恒审 sidekick 并可随时收回控制，委派带 constraints 与 success criteria；按 task 计价是预算口径。
- 逐字摘录：

> "Fusion works around the common pitfalls of routing with a key idea: running two parallel agents, each with its own persistent context and tools."

> "The lead owns the plan, interpretation of ambiguity, and review. It hands the sidekick a brief of each task it delegates, with constraints and success criteria."

> "The lead always reviews the work, identifies problems, and can take control back when the sidekick is out of its depth."

> "In 2026, models (and model-harness combos) should be evaluated on price per task rather than price per token."

> "Fable delegated earlier and gave better briefs, while Opus micromanaged the sidekick and redid much of its work."
（lead 恒审＝验证回路做进产品架构——与 Walden 本人 04-22 反并行立场一脉相承：并行可以，但层级化受控。）

- 立场：**支持（受控并行）**。

## 《Cognition and AWS team up…》（AWS 战略合作，2026-09-15）

- URL：https://cognition.ai/blog/aws-sca （官方博文实取）
- **挂钩**：**无人值守运行**——autonomous engineers 部署进企业生产环境、并行多 session 跑迁移与安全修复。
- 逐字摘录：

> "It can understand a codebase, plan an approach, write code, test its work, and remediate issues it finds. Engineers decide what gets built and review the output; Devin handles the rest."

> "Customers can connect to Devin's dedicated AWS VPC and run multiple sessions in parallel on migrations, framework upgrades, and security fixes."
（无人值守 agent 运行变成企业级采购项。）

- 立场：**支持（生产化自主运行）**。

## 《Introducing Code Scans》（2026-09-16）

- URL：https://devin.ai/blog/introducing-code-scans （官方博文实取）
- **挂钩**：**循环产品化机制＋外层调度**——Agentic MapReduce（Plan/Shard/Map/Reduce）把目标驱动的并行调查循环产品化为 /scan 命令。
- 逐字摘录：

> "Tell Devin what you want to achieve, and it helps you investigate what needs to change, evaluate the findings, and turn them into pull requests."

> "Code Scans breaks large investigations into focused batches, distributes them across parallel agents, and synthesizes their findings into one report."

> "Devin helps establish what to inspect, what to skip, and what should count as a finding."

- 立场：**支持（调查循环产品化）**。

## Devin Release Notes：循环跳过守卫与定时扫描（2026-09-02/09-04）

- URL：https://docs.devin.ai/release-notes/overview （官方 changelog 实取，条目各自标日期）
- **挂钩**：**停止条件＋预算与熔断**——无新提交即跳过起 session 并记零 ACU 消耗（循环不空转、不烧钱），支持定时循环扫描。
- 逐字摘录：

> "Scan-new-commits runs (including scheduled runs in Automations) now skip starting a session when the repository has no new commits since the last scan; the run is recorded as completed with no ACU usage"

> "Automations now support a code scan agent type, so you can schedule recurring scans or re-scan new commits automatically."
（停止条件与预算守护成了产品细节——loop 治理被当日常工程纪律推进。）

- 立场：**支持（治理产品化）**。

## Devin Release Notes：Review Effort Levels（2026-10-05）

- URL：https://docs.devin.ai/release-notes/overview （同上，2026-10-05 条目）
- **挂钩**：**预算与熔断**——Devin Review 引入 effort level，触发动作可设档、企业管理员可定默认档。
- 逐字摘录：

> "Trigger actions can set a Devin Review effort level, and enterprise admins can choose the default effort level in enterprise Review settings."
（预算档位产品化到代码审查场景并可企业级统管。）

- 立场：**支持**。

## 《Memory and dreaming: how Devin learns from working with you》（2026-10-05）

- URL：https://devin.ai/blog/memory-and-dreaming （官方博文实取）
- **挂钩**：**无人值守运行＋循环产品化机制**——"Dreaming"＝每日后台异步 session，自动去重、清旧、重索引记忆，用户无需维护。
- 逐字摘录：

> "Dreaming is a daily background session, in which Devin reviews past conversations alongside its existing memory to improve its index for future sessions."

> "Memories generated during your sessions are deduplicated, linked to relevant sessions and artifacts, and new knowledge emerges."

> "If another session saves an update while a sync is underway, a revision check rejects the stale write so Devin can retry against the newer version."
（每日后台自跑的记忆整理回路做成默认功能——无人值守运行在记忆层的产品化。）

- 立场：**支持**。

**本轮最小主张**：Walden 个人发声让位公司工程叙事，但立场一致：自主循环全推（无人值守、预算自分配、记忆回路），且每处都带受控形态（lead 恒审、effort 档位、诚实边界）——与他 04-22 反裸并行、拥约束并行的原立场连续。个人通道（署名博文/X）窗口内无新文，如实记录。
