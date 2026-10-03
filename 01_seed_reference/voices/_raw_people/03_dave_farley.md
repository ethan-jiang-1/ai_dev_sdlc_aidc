---
type: kol_deep_dive
person: Dave Farley
organization: Continuous Delivery Ltd
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://www.aviator.co/podcast/engineering-discipline-dave-farley
  - https://leaddev.com/technical-direction/safe-production-changes-with-agents
  - https://tessl.io/registry/skills/github/AINativeDev/aidevcon-2026-ldn/talk-farley-vibe-coding-best-we-can-do
  - https://bsky.app/profile/davefarley77.bsky.social
  - https://youtu.be/mRF99to28sA
  - https://youtu.be/T539pbwTIZY
  - https://youtu.be/VGE84CeeaMo
  - https://youtu.be/JV7Wy6V-tgI
  - https://youtu.be/2pqwu41UdJU
  - https://youtu.be/B6B9LOLpoKY
  - https://media.rss.com/theengineeringroom/feed.xml
key_concepts:
  - continuous_delivery
  - engineering_discipline
  - ai_exposes_lack_of_engineering
  - safety_engineering_turn
  - high_level_spec_is_the_prompt
  - syntax_tree_limitation
  - safety_net_philosophy
  - grown_not_built
---

# Dave Farley — "AI 暴露那些从未学会工程师思维的人"

> *Continuous Delivery* 合著者、全球最具影响力的 CI/CD 倡导者之一。对 AI 编码的立场独特：既不恐吓也不夸大——但警告极其尖锐。2026 年的高质量一手源已从被墙的 YouTube/个人站**转移到 Bluesky**（davefarley77.bsky.social，多线程长帖）；视频字幕均为 [asr]。**⚠️ 频道多主播**：Modern Software Engineering 频道含 Emily Bache 主讲的 AI briefing 系列——引用须核主讲人（见"频道结构与归属勘误"节）。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及 frontmatter `source_urls`。单人深度分析，所有引用基于其公开材料。2026-10-03 深挖重构：Bluesky 全 feed 双路拉取（07-16→10-03 区间全部本人帖与转发，线程逐字）+ 08-05 视频全片字幕 + Engineering Room 播客 2026 全清单 + KanDDDinsky 五路核实。X 登录墙不采。

## 当前立场小结（2026-10-03）

1. **安全工程转向是年度重心**（08-05 视频全片）：AI 的真实风险不是科幻而是**工程失职**——"We are building powerful, poorly understood, non-deterministic systems, handing them autonomy, and wiring them into places that matter."；解法是"航空式纪律"：testing, feedback, safety culture, regulation, accountability, black boxes, incident reviews——"**The safety isn't bolt-on, the engineering discipline is the safety.**"
2. **工程问句替代科幻问句**："Stop asking the sci-fi question: 'Is it conscious?' Start asking the engineering question: 'Is this a powerful, unpredictable component being put somewhere consequential, and where's the feedback that tells us that it's safe?'"（09-09 / 08-05 收尾）——"If you can't answer that, you don't really have a safe system. **You have a hopeful one.**"
3. **AI 对复杂重构不可靠**（技术论点，07-16）："Current generative AI tools generally manipulate **text rather than safely engaging with the underlying syntax tree**, making them highly unreliable for complex structural changes."——重构必须走"小的、安全的、确定性的步骤 + 快速自动化测试"。
4. **ATDD 是 AI 时代的解法**（08-18）："ATDD raises the level of abstraction, **the high-level spec is the prompt**. This unlocks incredible speed"——可执行规格当合同，"If the code satisfies the tests, you don't need expensive human code reviews for every line of AI code."
5. **loop 之争的立场**（09-02 对谈 Tessl CEO）：认 "loop engineering = **fitness function** + 小步"，拒 "eval" 术语、归位 BDD/acceptance testing；developer = manager of agents。
6. **AI 放大，不改造**："AI makes teams with strong, human-led engineering practices do better, and teams with weak practices do much worse."（07-29 原句）——数据侧："50% more duplication and a rapid increase in critical security vulnerabilities."

---

## 思想变迁轨迹（2026）

> **本表是索引**——各阶段详见下文专节。≤2025 背景一句：CD 立场与"AI 暴露"论已是其长期基调。

| 阶段 | 日期 | 立场标记 |
|------|------|---------|
| 口径定形 | 2026-06-01/02 | Tessl DevCon 闭幕（transcript 已核）："AI assistance is rather like **the compiler**"；自然语言不合格；BDD 可执行规格驱动、验证交给流水线 |
| 重构不可靠论 | 2026-07-16 | bsky 八条线程：AI 操纵文本而非语法树（→ 详见 Bluesky 线节） |
| "vibe coding 是谎言" | 2026-07-20→22 | 与 Sam Newman："AI-assisted tools are things to **make experts better**… not tools to make non-experts create production-ready software"；"writing code was never the hard part" |
| **THE HARD PART 八条线程** | 2026-07-29 | "THE HARD PART OF BUILDING SOFTWARE WAS NEVER THE TYPING"＋工程账单论＋强弱团队分化原句（→ 详见 Bluesky 线节） |
| **安全工程转向（年度最重）** | 2026-08-05 | 晨间 CD 基本功六条 + 晚间《The Real AI Threat ISN'T Sci-Fi》全片（→ 详见安全工程节） |
| 遏制与瓶颈 | 2026-08-07→18 | 与 Sam Newman 遏制专题（blast radius/sandbox）；ATDD 七条线程 |
| 术语与收官 | 2026-09-02→29 | Tessl 对谈（fitness function）；五大 Ideal 线程（09-10）；Approval Testing 线程（09-21）；向一线征询（09-29）；**DHH pencils down：查无回应** |

**判语**：稳定型锚点的加强版——他不但没有 2026 式转身，还在 08-05 给出年度最重的安全工程长文（"grown, not built"、"that's a prayer"、"You have a hopeful one"）。对 loop 之争认 fitness function 而拒 eval 词汇；9 月守门大讨论他以"频道回应 Böckeler"参与而非亲自下场。**渠道结论**：Bluesky 已取代被墙的 YouTube/个人站成为最高质量一手源（多线程长帖形式）；字幕均 [asr]（"Mythus" 实为 Mythos，AP 佐证）。

---

## 一、安全工程转向：《The Real AI Threat ISN'T Sci-Fi (It's So Much Worse)》（2026-08-05，年度最重第一人称）

21:36 全片（[asr] 字幕全档）。缘起：Control AI 组织来信请他"警告观众 AI 可能消灭人类"——他没有换台："when I set the apocalypse to one side, **some of what they were worried about is very real indeed**."

**认识论（全片骨架）**：

- **grown, not built**："Modern AI systems are not built the way normal software is built. **They're grown.** Humans don't write the rules line by line… Even the people who made these machines can't tell you in any complete way why it does what it does."
- **不可测 = 不可保证**："**If I can't specify a system's behavior, I can't properly test it.** Testing is verifying behavior against the intent, and here **the intent was never written down**."——问题随自主度与 reach 指数放大。
- 反"随机鹦鹉"："stochastic parrots… rather misses something profound about the ways in which these things actually work."
- **CAIS 2023 声明的分量**："when **the people selling a technology are amongst those asking for it to be regulated**, then the least that we can do is to listen to them."
- **导弹类比**（endorse Control AI 的表述）："You don't really care whether a heat-seeking missile is conscious or not, you care that it's coming towards you. **Whether the software understands what it's doing is a philosophy seminar question. Whether it can do damage is an engineering question. And engineering questions have answers.**"

**战例**：超高频金融交易所——"We were in production for **13 months and 5 days** before an end user noticed a bug. But on that fifth day of the 13th month, everyone noticed."（怪异行情把内存涂满 → 匹配引擎 OOM → 自动重启重放 → 再 OOM 的死循环，关所数小时）——"we already know how painful poorly understood non-deterministic components can be, and now we're **busy building them on purpose and calling it progress**."

**Mythos 红队段的准确原句（含 nuance）**（[12:00-13:03]）："Anthropic's Mythos model was in the news recently because in a red team exercise this year, it was said to have found weaknesses across a range of sensitive, sometimes government systems **within a matter of hours**."——随即自设边界："**finding a vulnerability in an authorized test is not the same thing as breaking into that system on its own**… this is both a threat and an opportunity at the same time, depending on who uses this capability."（ASR 记作 "Mythus"，实名 Mythos，[AP 报道佐证](https://apnews.com/article/anthropic-mythos-ai-classified-systems-vulnerabilities-testing-3e8762c0527c4d8ed657cbe48c84a718)）

**安全网哲学完整论述**（[14:24-17:07]）：

> "I don't think a global ban on AI research is enforceable… The mistake is to assume that our goal is to eliminate the risk. It isn't… the real goal then is to instead **move the risk to somewhere where we can better manage it**. We don't ban aircraft, we build a discipline around them of **testing, feedback, safety culture, regulation, accountability, black boxes, and incident reviews. The safety isn't bolt-on, the engineering discipline is the safety.**"

> 引 Feynman 挑战者号报告："**For a successful technology, reality must take precedence over public relations, for nature cannot be fooled.** That is the whole of AI safety in one sentence, really. You can't ship a wish."

> "If your plan for keeping a powerful, poorly understood system under control is that you're really rather hoping that it will behave itself, then that isn't an engineering solution at all, **that's a prayer**."

**让他失眠的**："not the malevolent robots, **ordinary human malice, and ordinary human carelessness** handed a spectacularly powerful and unpredictable new tool."；能力外泄节奏："Open models tend to trail the frontier by only a few months."；监管者："The people writing the rules… very often do not understand this technology at all. That's not a dig, that's a description."

**对反方阵营的公道话**："Their **honest uncertainty is worth more than my confidence**… I might be wrong about the extreme case is an argument for the discipline that I am recommending, not against it."

**收尾**："If you can't answer that, you don't really have a safe system. **You have a hopeful one.**… push for the **boring, brilliant discipline**. Testing, transparency, accountability, and decision-makers who actually understand the technology. **That's not being anti-AI.** I'm genuinely excited about what some of this technology may be able to do for us."

**泡沫定调**（与 bigger-than-internet 互补）："we are **almost certainly in the midst of a hype bubble, but rather like the dot-com bubble**… That doesn't mean that the technology doesn't work or that it won't have a huge impact."

---

## 二、Bluesky 一手线（2026-07-16 → 09-29，线程精选）

**「THE HARD PART」八条线程（07-29）**——身份论与工程账单：

> "the idea that software developers are just **replaceable cogs in a machine**… a catastrophic failure, both morally and from a pure business perspective."

> "**THE HARD PART OF BUILDING SOFTWARE WAS NEVER THE TYPING.** It's understanding the problem, designing a coherent solution, and taking responsibility for the result."

> "relying solely on machines to pump out code leads to **50% more duplication and a rapid increase in critical security vulnerabilities**… The evidence shows… You cannot skip the engineering bill. It always comes due, and **the people who pay it are called engineers**."

> 强弱分化原句："AI makes teams with strong, human-led engineering practices do better, and teams with weak practices do much worse."

**安全网哲学六条线程（08-10）**——含真空吸尘器故事：

> "If your solution to system failures is 'tell developers to be more careful,' you don't have an engineering strategy. **You have a wish. And wishes don't scale.**"

> 初级工程师把吸尘器插进服务器插座、断掉生产服务器——老板没开除他："**You've just learned a multi-million pound lesson.** You won't do that again?"

> "Great teams don't make fewer mistakes. What makes them world-class is that their failures are **recognised faster, fixed quicker, and resolved in ways that make it systemically impossible to happen again**."

> "We must build a '**satisfactory philosophy of ignorance**', accepting that we don't know everything and engineering safety nets anyway. Stop blaming individuals; start building resilience."

**「AI 操纵文本而非语法树」八条线程（07-16）**——技术核心论点：

> "Current generative AI tools generally manipulate **text rather than safely engaging with the underlying syntax tree**, making them **highly unreliable for complex structural changes**."——配套：重构的真价值是**可预测性**（"you gain the ability to actually predict how long a change is going to take"）；解法是"disciplined sequence of small, safe, deterministic steps, executed with reliable tools and backed by fast automated tests."

**CD 基本功晨间六条（08-05 上午，与晚间视频同日互补）**：

> "Originally, CI was a social discipline. In our CD book, Jez and I wrote that all you really need is **a bell and a rubber chicken**."
> "**Automation is a multiplier of your discipline.** But with bad practices, you just build crap systems faster."
> "Without discipline, you don't get a CD pipeline. **You get a sewage pipeline**, continuously delivering bugs and patches."

**ATDD 七条线程（08-18）**：

> "For CTOs and Tech Leads, AI coding assistants present a seductive trap… **typing code was never the hard part**."
> "If you let AI loose on vague specs, **it will just build incorrect systems faster**."
> "With ATDD, you turn AI into a high-speed, self-verifying execution engine. **Executable specs act as a contract.**"
> "**ATDD raises the level of abstraction, the high-level spec is the prompt.**"

**其余线程**：五大 Ideal 培训线（09-10，Gene Kim《The Unicorn Project》框架：locality & simplicity / focus, flow & joy / improvement of daily work / psychological safety / customer focus——"Improving the work IS the work"）；Approval Testing 线（09-21："Approval testing asserts **behavioural consistency rather than correctness**"——AI 时代遗产代码的安全网）；向一线征询（09-29）："where are they genuinely saving you time, and where are they still causing friction?"

**⚠️ 署名规则**：08-13「If writing code is no longer the bottleneck…」与 09-14「When AI generates the job description and AI rewrites the CV, the system is broken.」原帖作者是 **modernswe.bsky.social**（他的自有频道号），个人号只是几秒后转发——引用须标"转发自有频道"，不作个人原创。

---

## 三、访谈与视频（07-20 → 09-02）

- **07-20《Why 'Vibe Coding' is a Lie》**（与 Sam Newman，Engineering Room 期）：*"it's obvious that kind of vibe coding a prototype for something that's fairly common is so easy that even non-programmers can do it. But… for grown-up professional software development… it still requires a lot more thoughtfulness. Not least at the level of software architecture."*＋"AI-assisted tools are things to make experts better. I don't think they're tools to make non-experts be able to create production-ready software. **And I think that's the lie that some people have sold.**"
- **07-22《Quietly Rehiring》**：*"writing code was never the hard part, and why AI tools are actually **increasing the need for real software engineering**."*
- **08-07《How Do You Safely Contain an AI Agent?》**（与 Sam Newman，Docker 赞助）：blast radius / sandbox / 遏制自治 agent。
- **09-02 与 Tessl CEO Guy Podjarny 对谈**：认 "loop engineering = **fitness function** + 小步"；**拒 "eval" 术语、归位 BDD/acceptance testing**；developer as manager of agents。
- **09-16《The CTO's Guide to Fixing Slow Delivery》**："software isn't a factory production line, **it's a discovery process**. Stop rushing delivery & start optimising for learning."
- **DHH pencils down（07→10）：查无回应**（视频字幕 grep=0、bsky 全 feed 无、Sam Ruby 文 0 次）。

---

## 四、频道结构与归属勘误（引用前必读）

1. **8-19《How to Stop AI from Ruining Your Codebase》与 9-23《The Last Year Has Changed Everything I Knew About TDD After 20 Years》是 Emily Bache 主讲**（频道 AI briefing series，非 Farley 第一人称）。9-23 系对 Böckeler《TDD inside the agent loop》（页标 2026-08-10）的频道级回应："I am not convinced… **I'm not going to be abandoning TDD with agentic AI**"——引用须写"频道立场/Farley 认可转发"。
2. **06-03 期为 Gojko Adzic 客串**（meta-automation："Instead of filling up the project constitution with random **markdown prayers**, we have deterministic checks executed as part of the build process"）——引用挂双名。
3. **modernswe 频道帖 vs 个人帖**：见上节署名规则。
4. **KanDDDinsky 2026（Berlin，10-14/15）：Farley 不在讲者名单**——五路核实（官方议程 speakers.json 48 人、sessions.json 38 场、pretix、主办方 Avanscoperta 博客、ConferenceGrid）均无他；其 feed 全程零自宣。07-30 那条 bsky 是**转发 Kevlin Henney 的自宣**（Kevlin 讲《Modular Monoliths and Other Facepalms》）。~~此前"KanDDinsky 已证实"的说法作废~~（2026-10-03 勘误）。

---

## 五、The Engineering Room 播客（2026 年 6 集，官方 RSS）

| Ep | 日期 | 嘉宾 | AI/Agent 相关 |
|---|---|---|---|
| 42 | 01-25 | Gene Kim | ✅ vibe coding 论战（他初评"2025 年最差想法之一"） |
| 43 | 03-01 | Dan Abel | —（工程领导力） |
| 44 | 04-05 | Steve Freeman | —（TDD 论架构） |
| 45 | 05-03 | David Yanacek（AWS Agentic AI 团队/Kiro） | ✅✅ "从补全到自治 agentic 开发，工程基本原则比任何时候更关键" |
| 46 | 06-14 | Sam Newman | ✅ "AI 真会取代软件架构师吗" |
| 47 | 09-27 | Andrey Breslav（Kotlin 设计者十年/Kotlin Foundation 主席/现 CodeSpeak CEO） | ✅✅ |

**Ep.47 官方描述（要点）**："AI assistants and large language models automate boilerplate implementation, shifting the software engineer's primary task **from typing code to clearly specifying problems and verifying outcomes**… developers must organize complexity, define modular boundaries, and enforce deterministic verification pipelines **to avoid the trap of 'spaghetti prompts'**."——与 Farley 自己的口径（ATDD/验证管线）同构，他的播客选题本身就是其立场的延伸。截至 10-03 无更新集。

---

## 六、上半场经典（2026-01→06）

**规模判断**："Without really much shadow of a doubt, the change that we are seeing now is bigger than all of those put together — bigger than the internet, bigger than object orientation, bigger than the agile transformation."——同时批判两个极端（恐吓者说 AI 不能编程 → 错；鼓吹者说 10x-100x → 错）。

**三个结构性问题**：①英语不是好的编程语言（自然语言太模糊、太不精确——后来被 ATDD 线程具体化）；②非确定性（"给编程语言相同的输入，你得到相同的结果。给 AI 相同的 prompt，你可能得到不同的输出"——不能靠重复实验建立信任）；③**验证成为瓶颈**（"代码生成便宜了；理解和验证行为才是困难的部分"）。

**12,000 行问题（vs Yegge）**："I can't read 12,000 lines of code carefully enough to feel that I truly understand and own them."——信任必须来自**可执行规范和持续验证**，不是逐行人工审查，也绝不是"不审查"。

**CD 是 AI 时代的基础设施**："危险不是 AI 写出烂代码——而是 AI 写出大量代码，速度快到没人能合理检查。"小步、安全、可验证的步骤因此**更**关键。

**AI 放大，不改造**："AI won't replace software engineers, but it will expose the ones who never learned to think like engineers. Tools can speed you up, but if your thinking's wrong, AI just gets you to the wrong place faster."——基本功扎实的团队获得提升；大批次团队看到下游混乱。

**意想不到的乐观**："AI may be the industry's best-ever opportunity to finally get XP practices embedded — not because teams adopt them ideologically, but because **working without them while using AI is visibly, measurably risky**."

---

## 关键引用汇总

> *"The change we are seeing now is bigger than all of those put together."* — 规模判断

> *"THE HARD PART OF BUILDING SOFTWARE WAS NEVER THE TYPING."* — 2026-07-29

> *"You cannot skip the engineering bill. It always comes due, and the people who pay it are called engineers."* — 2026-07-29

> *"The safety isn't bolt-on, the engineering discipline is the safety."* — 2026-08-05

> *"For a successful technology, reality must take precedence over public relations, for nature cannot be fooled."* — 引 Feynman，2026-08-05

> *"If I can't specify a system's behavior, I can't properly test it… the intent was never written down."* — 2026-08-05

> *"Current generative AI tools generally manipulate text rather than safely engaging with the underlying syntax tree."* — 2026-07-16

> *"ATDD raises the level of abstraction, the high-level spec is the prompt."* — 2026-08-18

> *"You don't really have a safe system. You have a hopeful one."* — 2026-08-05 收尾

> *"AI won't replace software engineers, but it will expose the ones who never learned to think like engineers."*

---

**Source:** [Bluesky @davefarley77（当前最高质量一手源，双路全 feed 拉取）](https://bsky.app/profile/davefarley77.bsky.social) · [The Real AI Threat ISN'T Sci-Fi (2026-08-05，[asr] 全片字幕)](https://youtu.be/mRF99to28sA) · [Why "Vibe Coding" is a Lie (2026-07-20)](https://youtu.be/T539pbwTIZY) · [Quietly Rehiring (2026-07-22)](https://youtu.be/VGE84CeeaMo) · [与 Tessl CEO 对谈 (2026-09-02)](https://youtu.be/JV7Wy6V-tgI) · [How Do You Safely Contain an AI Agent? (2026-08-07)](https://youtu.be/2pqwu41UdJU) · [The CTO's Guide to Fixing Slow Delivery (2026-09-16)](https://youtu.be/B6B9LOLpoKY) · [The Engineering Room 播客 RSS（2026 年 6 集）](https://media.rss.com/theengineeringroom/feed.xml) · [Tessl DevCon 2026 闭幕演讲 transcript](https://tessl.io/registry/skills/github/AINativeDev/aidevcon-2026-ldn/talk-farley-vibe-coding-best-we-can-do) · [Aviator Podcast: Engineering Discipline in the AI Era](https://www.aviator.co/podcast/engineering-discipline-dave-farley) · [LeadDev: Safe production changes with agents](https://leaddev.com/technical-direction/safe-production-changes-with-agents) · [AP News: Anthropic Mythos 红队报道](https://apnews.com/article/anthropic-mythos-ai-classified-systems-vulnerabilities-testing-3e8762c0527c4d8ed657cbe48c84a718)
