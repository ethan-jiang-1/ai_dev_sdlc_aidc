---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# masad — loop engineering 证据轨迹（2026-06 后，时间正序）


> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**方向**：稳定推动·公司级愿景
**起点**：推动·技术层
**终点**：推动·组织层（core loop 成正式架构词）
**弧线**：06-23 评测循环 → 07-16《The Self-Driving Company》（环的公司级定义）→ 09-29《Free the models》（core loop 正式架构词）
**关键转折**：07-16 从技术层（评测循环）升至组织层（Self-Driving Company）
### Amjad Masad（Replit CEO）· 窗口内个人署名内容三路（含分档标注）

- **J1（半一手：经主持人转述）**：SaaStr AI 2026 现场（页内日期 2026-06-22/25；https://www.saastr.com/amjad-masad-and-me-at-saastr-ai-2026-the-agents-we-actually-built-and-what-replits-founder-thinks-comes-next/ ，Jason Lemkin 执笔，curl 实取全文）：
  - "Amjad put it"（Lemkin 转述其 nightly 自改进 agent）：**"it's not improving its weights, it's improving its context, which matters just as much."**——"每夜读全量 trace → 生成 prompt 修改 PR → A/B 上线 → 回环"的自改进外环叙事。
  - agent 可运行时长：**"practically indefinitely"**（Lemkin 引号直录，指配合 compaction）。
  - 预言句（Lemkin 转述）：每家公司将运行内部 "Oracle"——持有一切 commit/Slack/文档、CEO 向它问策。
- **J2（经中文转译，原始英文载体未定位——开放）**：品玩深度对话（https://www.pingwest.com/a/313307 ，页标"发布于 7月30日"，对话人 Amjad Masad＋YC 合伙人 Andrew Miklas，curl 实取全译文）：核心主张两条——"我们正在走向'后提示词时代'"（对 AI 说"帮我创建一个SaaS公司，想办法让它盈利"，系统自己推进）；"未来公司里只剩两种人——建造者和销售者"。
- **J3（窗口前谱系，不计窗口票）**：YC《The Breakdown》全 transcript（https://www.ycombinator.com/library/Mi-replit-ceo-amjad-masad-coding-agents-autonomy-and-the-future-of-work ，页面 created_at **2025-07-17**，curl 实取全 transcript）：autonomy 阶梯（"maybe 3.5 was like 5 to 10 minutes…they said they made it work for seven hours"）、transactional/可回滚基础设施、sampling 分支选优、"if you give us $1,000, we'll spend them"（compute budget）——2019-2026 无人值守循环路线图的早期完整版。
- 号召力口径：③＋④。
- **派别适配**：**推动票**（厂商身份重；J1 须标"经 Lemkin 转述"、J2 须标"经中文转译"）。

---

# 增量补挖（2026-10-07 第二轮：08-01→10-06 后续立场——由叙事转向产品化）

> 通道：Platformer 书面访谈实取、Replit 官方博客逐篇实取、a16z 播客转录页实取、LinkedIn 动态页实取。分档标注：一手（本人署名/本人直接引语）／半一手（转录无说话人标签）／公司层（The Replit Team 等署名）。X 时间线 SSR 不可得（仅 bio），如实记录；Fortune Free Mode 报道通篇无 Masad 本人引语，弃收。

## 《Replit's CEO on building a company that can run itself》（Platformer 书面访谈，2026-08-06）

- URL：https://www.platformer.news/replit-amjad-massad-interview-coding-design-jobs/ （访谈页实取全文；Casey Newton 长篇访谈，Masad 直接引语——**一手**）
- **与 loop engineering 的挂钩**：**循环结构＋无人值守运行**——他把"构建-反馈-维护"的 autonomous loop 点名为 Replit 要建的产品方向，并给出 bug 修复直通 PR、成本预估模型等无人值守要件。
- 逐字摘录：

> "But now you can really unleash an agent and have it work continuously, and not only create the first version, but actually maintain it and take user feedback and iterate on it. You can create an entire autonomous loop for building and maintaining software."

> "You should be able to create a loop that collects feedback, where you swipe left and right on whether you want that feature, and you have very light-handed management on top of that agent — but the agent is really maintaining the software."

> "You'll be able to create loops — something Replit is interested in building as well — that can use and write software to solve problems."

> "one of the things I don't like about vibe coding products is you put in a prompt and you never know, you're rolling a dice. It might be $20, it might be $10, it might take your entire credits for the month."
（循环成本预估是他主动点出的治理要件。）

> "When someone reports a bug, someone tags the autonomous AI engineer we built and says, hey, fix that bug — and it will go all the way to a pull request."

- 立场：**支持（autonomous loop 定为产品方向）**。

## 《Replit Introduces Free Mode…》（Free Mode 公告，2026-08-18）

- URL：https://replit.com/blog/replit-introduces-free-mode （官方博客实取；**Amjad Masad 本人署名——一手**；区别于已收的 09-29《Free the models》）
- **挂钩**：**预算与熔断＋外层调度**——Free/Power/Max 三档预算、5 小时额度重置、Agent 主动建议升降档。
- 逐字摘录：

> "But using AI today still means choosing models, managing context, watching usage, and juggling a growing collection of sprawling tools. Intelligence is now abundant, but access remains complicated."

> "Free Mode is a new way to use Agent that lets you create 30x more with just your monthly subscription. Spend less time thinking about usage and more time bringing ideas to life."

> "Core and Pro users can use Free Mode until they reach their usage limits - which reset every 5 hours - or continue building in Power or Max Modes."

> "If your work progresses to a more complex or high-value task, Replit Agent may suggest switching to our other Agent Modes, Power Mode and Max Mode."
（把"操心 token"定为要消灭的摩擦：预算分档与额度熔断成为产品默认。）

- 立场：**支持（预算分档默认化）**。

## 《Govern Replit at scale》（企业治理工具公告，2026-08-16，公司层）

- URL：https://replit.com/blog/new-enterprise-governance-tools （官方博客实取；The Replit Team 署名——**公司层**）
- **挂钩**：**预算与熔断＋循环产品化机制**——agent 活动审计、工作区级模型与 agent 模式策略管控。
- 逐字摘录：

> "Comprehensive Audit Logs: More than 50 events across deployments, identity, secrets, and agent activity, with native streaming to your SIEM. Available today."

> "These updates are designed to help teams answer those questions without putting a manual review step in front of every user."
（治理设计哲学逐字：**免人工审批**——与 DHH 10-06 反人审门立场同向。）

> "Configure which individual models are allowed in each workspace for compliance and cost control."

- 立场：**支持（循环治理产品化）**。

## 《Black-box pen tests on Replit》（2026-08-17，公司层）

- URL：https://replit.com/blog/black-box-pen-tests （官方博客实取；Alexandre Cuoci 署名——**公司层**）
- **挂钩**：**验证回路**——白盒+黑盒扫描"每次构建即运行"，把安全验证固化进构建循环。
- 逐字摘录：

> "Our existing scans have an agent read your code and look for patterns that tend to be dangerous. That catches a lot, and it runs every time you build."

> "Replit runs each scan against a full copy of your app running in a private sandbox, so nothing it tries can escape or reach your users."

- 立场：**支持（验证回路默认嵌入构建循环）**。

## 《Intelligent Model Routing on Replit》（2026-08-26，公司层）

- URL：https://replit.com/blog/intelligent-model-routing （官方博客实取；The Replit Team 署名——**公司层**）
- **挂钩**：**外层调度**——按任务演化自动匹配模型、升级时通知、允许人工覆盖，管理员可圈定模型集。
- 逐字摘录：

> "As each task evolves, we match it with the model best suited to complete it - balancing quality, speed, and cost behind the scenes."

> "In our testing, Intelligent Model Routing delivered the same output quality at 65% lower cost than the previous version of Max Mode."

> "All users will start in Free Mode, and will be notified when their work escalates to higher-powered modes that can incur usage costs. Users can always over-ride this, and choose to remain in Free Mode."

> "Administrators can define the approved model set for each workspace based on company policy. Replit then automatically chooses the model best suited to each task from that approved set."
（任务级模型路由＋通知＋人工覆盖默认开启——外层调度最直接的产品证据。）

- 立场：**支持**。

## 《Amjad Masad on Rethinking College for the AI Era》（a16z Podcast，2026-09-23）

- URL：https://podscripts.co/podcasts/a16z-podcast/amjad-masad-on-rethinking-college-for-the-ai-era （转录页实取；无说话人标签——**半一手**）
- **挂钩**：**外层调度（公司级循环）**——agents 作组织粘合剂、官僚机制交由机器后台运行。
- 逐字摘录：

> "you can have agents kind of function as the glue within these organizations and, like, have the bureaucracy be this invisible thing that's happening by machines in the background."

> "And the AI can sort of judge your impact. I don't have fully formed thoughts about this, but I see it in our company where I've changed how I run the company."

> "And we call this idea of, like, a self-driving company eventually. like the company will like run itself."
（在教育话题里主动拉回 self-driving company 叙事。）

- 立场：**支持**。

## Replit 收购 Atta＋Masad LinkedIn 欢迎帖（2026-09-25）

- URL：https://replit.com/blog/replit-acquires-atta ＋ LinkedIn 动态（双实取；LinkedIn 帖为**本人一手**，博客为公司层）
- **挂钩**：**外层调度（公司级循环）**——收购理由直接落在 self-driving companies 愿景，"investigation 成为 recurring routine"＝公司级循环日常化。
- 逐字摘录：

> "We've been thinking a lot about what it means to build the self-driving company. A big part of that is putting the ability to understand a business in everyone's hands."

> "Together, we're building toward a future in which analysis is part of the work itself, not a separate destination."

> "In Replit, an investigation could become a recurring routine. Its findings could become slides for a leadership review. Those insights could then shape the next product, campaign, or internal tool a team builds."

- 立场：**支持（公司级循环扩到业务分析）**。

## 《Beyond the God Model | Alex Atallah & Amjad Masad》（a16z Show，2026-10-03）

- URL：https://podscripts.co/podcasts/the-a16z-show/beyond-the-god-model-alex-atallah-amjad-masad （转录页实取；无说话人标签——**半一手**）
- **挂钩**：**外层调度＋预算与熔断**——Replit 做企业与模型间的 independence layer；成本预估模型。
- 逐字摘录：

> "replet is becoming more of an independence layer inside inside enterprises where we create a layer of indirection between um between you and the models and we get you the best token at the cheapest price."
（转录原文含口语重复，逐字保留。）

> "I trained a cost estimator model internally so that when you put it in a prompt and replica, we know exactly how much it will cost. And it basically emits a, you know, probability distribution over multiple buckets."

> "Yeah, and I think as well, like, inside the enterprise, making these products actually do real work is still unsolved problem."
（"do real work still unsolved"——推动派内部的坦白时刻。）

> "Amjad's been doing that a lot of replet, for example. Like, you guys have done a lot of cost per task research. You guys have been, you know, you made, like, a doom loop. rescue."
（co-guest 点名其 doom loop rescue 与 cost-per-task 研究——循环研究被同行引用的佐证。）

- 立场：**支持（半一手）**。

**本轮最小主张**：Masad 08 月起由叙事转向产品化：autonomous loop 定为产品方向（Platformer）、预算分档/审计/验证回路/自动升降档做成默认产品（Free Mode/治理/渗透测试/模型路由）、公司级循环扩到业务分析（Atta）；10-03 访谈坦承"enterprise real work still unsolved"。全程稳定推动。
