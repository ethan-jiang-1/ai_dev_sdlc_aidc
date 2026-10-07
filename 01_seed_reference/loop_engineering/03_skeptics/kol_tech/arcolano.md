---
type: kol_evidence
directory: 03_skeptics/kol_tech
observation_date: 2026-10-07
---

# arcolano — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：Jellyfish（工程智能平台）Head of AI & Research
> **背景**：Nicholas Arcolano——Harvard Ph.D.；Jellyfish Head of AI & Research，管理 3700 万+ PR 数据（2025 年 200 万+ → 2026-04 3700 万+）的研究线；AI Engineer World's Fair 2026-07 讲者；TechRadar Pro 2026-07 署名文、TechCrunch 2026-06 报道对象。**第九轮（2026-10-07）新入册——tokenmaxxing 批判的"数据权威"，怀疑面与推荐面俱全。**（履历核：arcolano.com＋ai.engineer 讲者页，2026-10-07）
> **号召力**：③ 一线规模（3700 万 PR 数据库的行业引用度）＋② 被媒体/会议引用
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)（2026-10-07 第九轮入册）
> 人群类型：**专业技术 KOL**（研究员出身，数据平台侧）

> **线索闭环**：旧线索《Tokenmaxxing is the New "Lines of Code"》（SREcon）——SREcon26 Americas 官方 program 页全文抓取＋grep **无其讲题**（presentation/arcolano 404），原题至今未发布；但内容已演化发表（见下）。待发布讲题：《It's Not the Model, It's You》（AI Engineer NYC · 2026-10）、《Botsitting Doesn't Scale: How to Navigate the Autonomy-Trust Gridlock in Real Engineering Orgs》（aiDevCon · New York · 2026-11——**标题即对无人值守运行的怀疑**）。

## 态度轨迹

**方向**：数据怀疑（放权放大的边际收益递减）＋建设面完整
**起点**：tokenmaxxing 不经济（谱系 2026-04-15）→ **终点**：trust 是平台投资、"Don't just code faster. Code further."
**弧线**：04-15 tokenmaxxing 成本论（谱系）→ 06 播客《Why Developers Hit a Wall at 4 AI Agents》→ 07 World's Fair 讲题 → 08-13 substack 同题文（本轮主档）
**关键转折**：从"token 烧得多≠产出多"的批判，走到"三 regime 分档＋信任作为平台投资"的处方

## 《Tokens Are Rocket Fuel, Spending Tokens Is Rocket Science》（Jellyfish Research substack，2026-08-13）

- URL：https://jellyfishresearch.substack.com/p/tokens-are-rocket-fuel-spending-tokens ｜ fetch 成功（全文）
- 来源类型：机构研究 substack（一手，作者署名 Arcolano）。
- **挂钩**：③预算与熔断 ④外层调度 ⑤验证回路 ⑥无人值守运行（四钩俱全——本轮唯一）。

### (a) 怀疑面（放权放大的数据反证）

**逐字摘录**：

> "the heaviest-spending decile of developers burns roughly 10x the tokens of the median developer, but merges only about 2x as many PRs."
（**最重十分位**：10x token 只换 2x PR——边际递减的头部证据。）

> "Roughly 70% of the developer-weeks we track sit below the barrier, where agentic software development is largely characterized by interactive workflows with heavy oversight."
（**agentic barrier 命名**：70% 的开发周卡在高监督交互区——"宽自主是常态"的组织级反证。）

> "Why are so many teams stuck? Because human attention doesn't scale, and unlocking meaningful autonomy requires moving some big rocks: serious investment in infrastructure, permissions, and trust."
（卡住的原因：**人的注意力不可扩展**——自主化需要搬基础设施/权限/信任三块大石头。）

> "In our data, we find that 81% of developers max out at one or two agents at a time."
（**81% 开发者同时最多 1–2 个 agent**——多 agent 并行 loop 在真实组织里是少数派。）

> "We find that agent-authored pull requests currently merge at about 61%, versus about 79% for human-authored PRs." ＋ "For agents though, the rate of dead PRs is double that."
（**merge 率 61% vs 79%、死 PR 率翻倍**——验证回路/外层调度是瓶颈的数据形态。）

> "The biggest culprit here is the review bottleneck. Code got faster to produce, but for most teams review and integration are struggling to keep up."
（**review bottleneck 是最大元凶**——与 Ronacher"越自主越要人复核"、Dotta"verification theater"同构。）

> "If you look instead at deliverables (e.g. actual features and epics shipped), the gain is only about 27%."
（**10x token → 2x PR → 交付物仅 +27%**——三段衰减链。）

> "among the bottom decile of token spenders, about 1 in 8 tool calls goes to review and integration, versus 1 in 4 for the top decile."
（**agent 间协调开销非线性上升**：1/8 → 1/4 tool calls。）

### (b) 推荐面（该怎么做——本轮最完整的怀疑者处方之一）

**逐字摘录**：

> 三 regime 分档："Interactive coding (< 50M tokens / dev / week)... you're still 'botsitting', limited to a small number of concurrent sessions and throttled by human attention." ／ "Autonomous agents (50M to 200M tokens / dev / week). In this regime, you've developed the process, platform, and infra to allow agents to work in more autonomous ways." ／ "Agent orchestration (200M+ tokens / dev / week)."
（**按 token 消耗分三档治理**：botsitting → autonomous → orchestration——外层调度的分档依据。）

> "**Invest in context.** Autonomy starts with agents that have access to everything they need to know to work unsupervised... A great place to start here is context files like Cursor rules and Claude skills... the heaviest skill users merged 27% more PRs than the baseline."
（处方一：投上下文——skill 重度用户 merge 率高 27%。）

> "**Move the big infrastructure rocks.** Meaningful autonomy requires significant platform investments like sandboxed environments, permissions, orchestration, and access to data."
（处方二：搬基础设施大石头——沙箱/权限/编排/数据接入。）

> "**Treat trust as a platform investment.** ... Guardrails, evals, observability, and access controls can help, but ultimately trust takes time, which is why teams need to start building it as soon as they possibly can."
（处方三：**信任是平台投资**——护栏/评测/可观测/访问控制四件套＋趁早。）

> "**Address the merge-rate gap.** ... If you're scaling agents, your agent merge rate is one of the most important numbers you can watch, and improving it is usually about process (review capacity, PR sizing, verification before the PR opens) rather than model quality."
（处方四：merge 率是头号指标，解药是**流程**（review 容量/PR 尺寸/**PR 打开前验证**）而非换模型——验证前移。）

> "**Recognize that not all unshipped work is waste.** ... The goal isn't to drive unmerged work to zero; it's to make the speculation deliberate and to know which work is intentionally disposable versus which is waste."
（处方五：未合并工作≠浪费——把投机**刻意化**，区分"有意弃置"与"浪费"。）

> "**Watch compounding coordination costs.** ... Whatever the equivalent of Brooks's Law for agents is, I doubt we can repeal it—but you can measure it, and squeezing coordination overhead is one of the highest-leverage optimizations available in the high-spend regimes."
（处方六：盯住复利式协调成本——"agent 版 Brooks 定律大概废不掉，但可以测量"。）

> "**Track outcomes over outputs.** ... measuring the token cost of what actually reaches a customer."
（处方七：测结果不测产出——量"到客户手里"的东西的 token 成本。）

> "Don't just code faster. Code further."
（**收束句**：别只是写得更快——写得更远。）

### 谱系（窗口前，2026-04-15，Jellyfish 博客）

- URL：Jellyfish 博客 2026-04-15 ｜ fetch 成功（curl 提取）。
> "The cost per merged PR increases from just $0.28 in the lowest usage tier to $89.32 in the highest."
（tokenmaxxing 不经济：每 merged PR 成本 $0.28 → $89.32——**300 倍**。）
> "Broad, moderate adoption delivers far more value than narrow, extreme usage."
（**广而适度的采用 > 窄而极端的使用**——推荐面谱系句。）

**该条支持的最小主张**：3700 万 PR 级数据显示放权放大的三段衰减（10x token→2x PR→+27% 交付物）与组织卡点（81% 最多 1–2 agent、merge 率差、协调开销复利）；他的替代方案是"三 regime 分档＋投上下文/搬基础设施/信任作平台投资＋merge 率用流程解＋测结果不测产出"。
**派别适配**：**怀疑票（数据实证向，强）＋完整推荐面**——注意他不是反 agent（处方是"怎么把自主做出来"），是反"烧 token＝进步"的叙事；判读勿读成"反 loop"。

---

# 增量补挖（2026-10-07 goal 第一批·单点→稳定复核）

> 判定：**单点解除 → 稳定**——04-15（谱系）→ 06-02 → 07-27 → 08-13 四时点同向，无方向性移动；07-27 实填了 06-02 与 08-13 之间的档案缺环。完整发现见 .tmp-goal-movers/batch-A-skeptics.md（tmp 不入库，关键句以下留存）。

## 《Why the Real ROI from AI Isn't Showing Up Yet》（Jellyfish 博客，2026-07-27，PlatformCon 讲作者文版；与 Nik Albarran 署名）

- URL：https://jellyfish.co/blog/why-the-real-roi-from-ai-isnt-showing-up-yet/ ｜ fetch 成功（web_fetch 截断→curl 全文）
- **挂钩**：③④⑤（与主档同）
- 逐字摘录：

> "Engineering organizations that go from zero to 100% adoption can expect a 2X increase in merged pull requests. But when you look further down the line, the change is much less dramatic: Jellyfish data show the average organization is seeing a 27% increase in epic throughput."
（比 08-13 更早的同一条衰减链：2X merged PR → 仅 27% epic 吞吐。）

> "Less than 9% of PRs involved autonomous agents at median companies, compared to almost 35% for companies at the 90th percentile."

> "While the median developer spends $50 to $100 a month on AI tokens, the top 5% are accumulating costs of $5,000 and over. That level of spending affects the bottom line, and it's the reason why organizations are starting to ask engineers to show their receipts."
（token 账单进 CFO 视野——"show their receipts"。）

> **质量面 nuance（判读关键）**："AI agents don't appear to be causing quality issues at scale. When we plot bugs, escape defects, and revert rate against a company's level of AI adoption, we see no dramatic difference between low and high adopters."
（他明说规模上**没看到质量问题**——怀疑锁定在"产出转化率"轴，不是代码质量；引用勿读成质量怀疑者。）

> 推荐面（三条建议之二）："Optimize for the middle. Getting more of the organization from low levels of agentic workflows to the 80th or 90th percentile is more important than pushing a small group of developers towards extreme use."；"every doubling of context-file investment gives you 29% more additional throughput on top of any other gains."

- 同日视频页（The New Default/Monterail，20M PR 口径）页面直引："I don't trust the opinion of any leader who isn't working with these tools themselves. When you talk to someone, you can tell immediately whether they're actually living this or just reading about it, and you have to live it."（其余策展转述）

## 《AI Native Dev #108》（Tessl 播客，2026-06-02）——show notes 级（transcript 区 JS 未取得，引用标页面语）

> "Human PRs merge at roughly 80%, meaning about 20% are closed without merging. For AI-generated PRs, that ratio shifts to approximately 60/40."＋"Even highly experienced engineers tend to max out at four concurrent agents."
（"4-agent ceiling"与 agentic barrier 的 6 月形态——主张与 08-13 一致。）

## 复核判定与负结论

- **稳定**：数字链四点收敛（$0.28→$89.32/PR ⇒ 80/20 vs 60/40 ⇒ 2X→27%＋9% vs 35% ⇒ 61% vs 79%＋10x→2x→+27%）；方向始终＝"边际收益递减＋瓶颈在 review/信任＋分档治理处方"。
- 负结论：09-10 月无本人一手新发声（substack 10 月新篇署名 Tomas Pardinas）；NYC／aiDevCon 讲题仍待发布；podtail 403（重试仍败）。
