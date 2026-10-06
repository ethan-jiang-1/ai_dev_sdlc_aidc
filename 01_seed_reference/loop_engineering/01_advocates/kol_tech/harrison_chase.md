---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# harrison_chase — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：LangChain CEO
> **背景**：Harrison Chase——LangChain 联合创始人/CEO：2022 年以开源 LangChain 起家，扩至 LangGraph/LangSmith 生态，agent 技术栈事实标准的缔造者之一；此前任 Robinhood 机器学习工程师。词表为 harness/managed agents/learning loop，不用 “loop engineering”（台账 §A2 相邻位）。
> **号召力**：① 术语定义者＋② 被引用
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——当前库存不足以判弧线，待补挖（补挖 agent 在跑，新发声到位后本节升级为完整轨迹）。
## Harrison Chase（LangChain CEO）· "Harrison's In the Loop" 博客系列（2026-06-30 → 08-12）

- URL：https://www.langchain.com/blog/own-your-intelligence （2026-07-25，全文取得）；https://www.langchain.com/blog/why-managed-agents-are-the-next-big-thing-in-agent-building （2026-08-12，全文取得）；系列另有 "Wiki Memory"（2026-06-30，未取正文）；红杉播客 "Owning Your Intelligence Starts With the Harness"（sequoiacap.com，页面截断未取得正文）｜ 作者身份：LangChain 创始人兼 CEO
- 来源类型：个人署名一手博客（本人专栏，两条全文取得）；播客页面截断
- 号召力口径：①＋③＋④——LangChain 是 agent 基础设施头部厂商；其专栏名就叫 "Harrison's **In the Loop**"；此前红杉播客（2026-01-28，经 36氪中文全文编译取得）已把 "LLM run in a loop" 立为核心算法
- **边界情况**：Harrison Chase 全部可见文本中**未使用 "loop engineering" 这个词**——他的词表是 harness / managed agents / learning loop / feedback loop。判派依据是他对"循环作为 agent 核心原语"的一手表态，而非对本词的认领。

**逐字摘录**：

> "Sometime in early to mid 2025 the models started to get good enough to power what we think of agents today: LLMs running in a loop calling tools. This is the core primitive, the core algorithm, that underpins agents today."
>（把"循环中跑 LLM"定为 agent 的**核心原语与核心算法**——这是 loop 派的世界观基石，出自其 08-12 一手。）

> "The concept of Agent Harnesses like Claude Code, Pi, and Deep Agents emerged as we figured out the rights tools and environments to add into this loop."
>（harness 被定义为"往这个循环里加对的东西"——harness engineering 在他口中就是 loop 的外围工程，与 loop engineering 实为同一实践域的两种词表。）

> "Advantage comes from a feedback loop that improves the system with use… you should own this entire loop yourself."
>（07-25 文：竞争壁垒＝自持的学习循环。这是把 loop 从技术议题抬到**企业战略议题**。）

> "Buy the generic infrastructure, but own the intelligence that compounds."
>（同文结语——loop 是复利资产，故要"拥有"。）

- **难点自认（掌控教学面，本档重点）**：07-25 文给出整整十条"ownership checklist"（能否换模型、能否控制编排逻辑每一步输入 LLM 什么、能否按用户控成本、能否出示完整 trace、有无 evals 防回归、能否控制 agent 怎么学习），并引用 Uber 四个月烧完年度 AI 预算作"cautionary tale"："Cost matters because intelligence is only valuable if it's cheap relative to the return it generates… Being able to lock down costs - on a user, orgs, or agent level - is crucial to being able to scale AI reliably."＋"Quality needs to be measured, not assumed."＋"Boundaries define where AI can act independently and where it needs supervision."——**他是新增推动者中"教掌控"教得最系统的**。
- 辅助线（X 经转引，判派参考不作主张依据）：2026-03-02 hwchase17 转发他人帖子并加评 "The loop is the product — Great way to put it"（经 todayrss X 镜像页取得，原始 x.com 不可达）。**六月前**发声，不计入窗口票。
- 补充：Sydney Runkle 06-16 四环模型官方文致谢名单含 Harrison（"Thanks to Vivek, Mason, Harrison, and Hunter for thoughtful review"）——他对该文做了评审，属间接背书。

**该条支持的最小主张**：Harrison Chase 2026-06 后有密集本人署名一手发声（06-30 / 07-25 / 08-12＋红杉播客），把循环立为 agent 核心原语与复利资产，同时系统教授成本/边界/可观测的掌控面。
**派别适配**：**推动票**（以 harness/learning-loop 词表参与同一实践域；不改用 "loop engineering" 术语是他的词表选择，不是立场保留——他明确推荐 managed agents 这类"把循环包成产品"的默认方向）。

---

---

# 增量补挖（2026-10-07 第二轮：06-30 Wiki Memory 正文补取＋09-24 Interrupt NYC 主讲）

> 通道：LangChain 博客文章页实取（wiki-memory 正文）、LangChain YouTube 频道 feed 实取（keynote 描述）；博客索引确认 07-25 后 Chase 无新博客文。注意《The Art of Loop Engineering》为 Sydney Runkle 署名（06-16，库内已收），不重复；其余候选篇均他人署名不收。

## 《Wiki Memory: File-Based Memory for AI Agents》（2026-06-30，正文补取）

- URL：https://www.langchain.com/blog/wiki-memory （文章页实取全文；Harrison's In the Loop 栏目，署名 Harrison Chase，页面明示 June 30, 2026——上轮只记标题未取正文，本轮补齐）
- **与 loop engineering 的挂钩**：**循环结构**——把长期记忆定义为 agent 反复运行的压缩与维护循环（"How do you maintain it? → an agent"），是 loop 运维循环在记忆层的同构延伸。
- 逐字摘录：

> "Memory for agents is still early, with little to no standards. "Memory" means something different to everyone. But one common pattern is emerging: wiki memory."

> "The idea is simple: use an agent to turn raw source data into a compact, persistent, agent-readable knowledge layer."

> "A wiki is an agent-maintained data structure that represents source knowledge in an agent-friendly way."

> "The important bit is that it is persistent, structured, inspectable, and updated over time."

> "But for many domains, wiki memory may be the simplest useful long-term memory pattern we have."
（记忆压缩与维护也交给 agent 循环执行——"agent 作为可复用处理过程"主张向记忆层的延伸。）

- 立场：**支持**。

## Interrupt NYC Opening Keynote（2026-09-24 演讲，视频 2026-10-05 上传）

- URL：https://www.youtube.com/watch?v=950byF7njfw （LangChain YouTube 频道 feed 实取视频描述；演讲实录 09-24，Chase 开场主讲）
- **挂钩**：**验证回路＋循环产品化机制**——"复合学习循环"列为企业拥有智能的三大支柱之一；LangSmith Engine v2 自动红队并测试自身修复。
- 逐字摘录（视频描述）：

> "owning your intelligence, which means building domain-specific pieces in and around the model"

> "the three pillars it takes: an open, model-neutral harness such as LangGraph or Deep Agents, a loop that compounds what you learn from how people use your agents, and governance for internal agents"

> "LangSmith Engine v2, which adds red teaming and tests its own fixes on LangSmith Deployment"

> "shares that Engine has scanned over 70 million traces and detected over 21,000 issues"

> "Turning trajectories into optimized models with smithtune"
（**loop 正式进入三支柱框架**：harness＋复合学习循环＋治理——理念倡导转向售卖循环基础设施。）

- 立场：**支持（循环基础设施售卖化）**。

**本轮最小主张**：Chase 06-30→09-24 的增量把循环范式推广到记忆层（wiki memory＝agent 维护循环）并升格为企业级三支柱框架；对 loop engineering 专名无新直接表态（其个人通道窗口内无新博客文），但"loop as pillar"的产品化语言本身就是最强站队。
