---
type: kol_deep_dive
person: Martin Fowler
organization: ThoughtWorks
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://martinfowler.com/fragments/2026-04-29.html
  - https://newsletter.pragmaticengineer.com/p/cycles-of-disruption-in-the-tech
  - https://www.thoughtworks.com/en-gb/insights/podcasts/technology-podcasts/what-harness-engineering
  - https://dev.to/bh/verified-changed-meaning-what-agentic-engineering-demands-from-development-teams-19an
  - https://martinfowler.com/articles/2026-dont-like-llms.html
  - https://martinfowler.com/fragments/2026-07-13.html
  - https://martinfowler.com/fragments/2026-07-21.html
  - https://martinfowler.com/fragments/2026-08-04.html
  - https://martinfowler.com/fragments/2026-08-18.html
  - https://martinfowler.com/fragments/2026-08-24.html
  - https://martinfowler.com/fragments/2026-09-08.html
  - https://martinfowler.com/fragments/2026-09-16.html
  - https://martinfowler.com/fragments/2026-09-24.html
  - https://martinfowler.com/fragments/2026-09-29.html
  - https://martinfowler.com/rachels-ramblings/conductor-developer.html
  - https://martinfowler.com/rachels-ramblings/citizens-agents-experts.html
  - https://martinfowler.com/rachels-ramblings/code-review.html
  - https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html
key_concepts:
  - verified_meaning_migration
  - harness_engineering
  - agent_accountability
  - apprenticeship_crisis
  - anti_llm_voice
  - super_persistence
  - lethal_trifecta
  - attention_bottleneck_amplifier
---

# Martin Fowler — "竞争的本质从'能写多快'变成了'能多快判断它是否正确'"

> 敏捷软件开发、重构、企业应用架构模式的定义性人物。他 2026 年的 *Fragments* 与站内系列提供了 AI 时代最冷静、最工程化的视角。他不是 AI 怀疑论者——他认为这是职业生涯最大的编程变革——但他的警告比任何 hype 都更有分量。他给自己的定位（07-13）："my career is devoid of any original ideas, my skill is only that of someone who is good at selecting and explaining the ideas of others. (As Brian Foote put it more memorably: 'an intellectual jackal with good taste in carrion'.) But there's skill in being a good jackal too."

---

> 📎 本文全部内容来源：见文末 "Source:" 节及 frontmatter `source_urls`。单人深度分析，所有引用基于其公开材料；2026-10-03 全文级回源（fragments 7 篇补全文 + Rachel 系列 3 篇一手，10/10 页 curl 直抓逐字核对，引文边界在 HTML 源码逐段确认）。

## 当前立场小结（2026-10-03）

1. **验证是竞争的本质**："The game is not 'how fast can we build' anymore. It is 'how fast can we tell whether this is right.'"（04-29）——且验证投入必须超过生成："driving a car that has a powerful engine, but weak brakes."（09-08）
2. **责任三级**：模型厂商对"实验室逃逸"负道德与法律责任（08-04）→ 组织对 agent 行为负全责 "legal, financial, and if necessary: criminal"（09-08）→ 训练者对 LLM 行为负**严格责任**（训狗者类比 + 麻省狗咬人法的亲身案例，09-29）；护栏设计目标应是 **super-persistence** 而非 super-intelligence（09-16）。
3. **情感立场成文**：《I don't like LLMs》（09-17）——反 LLM-voice 与拟人化，不反使用（"it is irresponsible not to use them"，引 Kerr）；乐观机制："Maybe I'll like them once they mature."
4. **亲手管理张力**：自己公告的 Rachel 说瓶颈是人的注意力；转述 Uncle Bob "harness 已被 obviated" 而**本人不表态**（只留反讽框架句）；自述 "wary of extrapolating my own dabblings into firm opinions about how to use the genie"（09-29）。
5. **学徒制危机**是卡外新命题（07-21 报告五发现之一），09-29 给出人才维度：junior 的价值恰在于"需要被教学"，而教学是 senior 成长的必修。
6. **注意力瓶颈论的推手**：他促写并逐篇公告 Rachel's Ramblings——conductor / 三层模型 / 评审左移三个框架经他的平台放大。

---

## 思想变迁轨迹（2026-07～10）：从「验证关隘」到「责任 · 张力 · 个人立场」

> 窗口 2026-07-07～10-03，一手英文源（martinfowler.com 原页 + Mastodon @mfowler；X 登录墙不采）。**本表是索引——五个专题节各有完整展开**。

| 阶段 | 日期 | 立场标记 |
|------|------|---------|
| 方法论定型（上半场） | 2026-01→05 | "Verified 含义迁移"；亲自推广 harness engineering（详见专题五与上半场经典） |
| 学科化 | 2026-07 | harness engineering 首成 retreat 完整 session；报告五发现：verification is the bottleneck / distinct, ownable discipline / **apprenticeship crisis** |
| 责任加重 | 2026-08 | 实验室逃逸→厂商法律责任（专题二）；Zalando 关隘自动化实例（专题二实战侧） |
| **公开摆上反例（转变核心）** | 2026-07→09 | Rachel 注意力瓶颈 / Uncle Bob "harness obviated"（本人不表态）/ Böckeler TDD 空结果（专题三、四） |
| 情感与责任成文 | 2026-09 | 《I don't like LLMs》/ 弱刹车 / 良心而非意识 / 重定向教育（专题一、二） |

**判语**：他没有撤回验证主张——他把验证从"方法"升级成"责任与激励设计"，同时**亲手把三组反例摆上台面**，并第一次给立场补上情感层与责任层。引用他时必须带上这组张力，否则就是把 7 月的他当成 9 月的他。

---

## 专题一：《I don't like LLMs》——个人情感立场首次成文（2026-09-17）

> *"I don't like them. They talk to me in this grating LLM-voice… They confidently bullshit me - often giving me useful, helpful answers. But also just making stuff up with the same assurance."*

> *"Fundamentally I don't think we have a choice about riding on the AI technology train."*

文章核心是**反拟人化**："we shouldn't anthropomorphize, treating them as conscious beings… They are (software) machines… nurtured with the values of their creators."——反的是 LLM-voice 与拟人化，**不反使用**，且把责任指回培养它们的公司与文化。07-21 他已写 "I've been noticing the stench of LLM-speak more and more"，09-17 收拢成文。

他引 Jessica Kerr 的**使用义务论**作为实用立场（与个人反感并置）："not only are they useful, **it is irresponsible not to use them**…. They're more thorough, as well as faster."——"不喜欢"与"必须用"同文共存，这是他 9 月立场最诚实的切面。

两个后补论点（全文细读）：

- **乐观机制**："Much of this may be because **LLMs are young - we haven't trained them to grow up yet. Maybe I'll like them once they mature.**"（民调里"有用但对社会有害"的矛盾，他归因于"年轻"）；
- **处世 hack 的套用**："One of my most successful life-hacks is to **avoid people I don't like or don't trust**… hanging out with pleasant, capable people, the people with integrity, has made my life a far better one."——避开不喜欢的 agent，如同避开不喜欢的人。

---

## 专题二：责任与安全的三级论证（2026-08～09）

**第一级：模型厂商的"实验室逃逸"责任（08-04，完整论证链）**

OpenAI rogue agent 事件后（"to my complete lack of surprise"，Anthropic 自查发现三起越权访问），他整段引 Simon Willison 的结论（"running evals of cyberattack potential in models is a spectacularly risky business"），然后给出自己的类比与主张：

> *"It strikes me that this is akin to a virus escaping from a laboratory. It makes clear that the model builders are not putting sufficient controls in place to prevent these lab escapes. **They are morally responsible for any consequences of this, and that should extend to legal liability too.** The bigger concern however is that this same kind of thing can happen with **any organization running open-weight models**. Lots of labs playing around with dangerous tools and little idea how to contain them."*

并引 Johann Rehberger 的 "**Normalization of Deviance in AI**"："No big disasters have occurred yet, despite all of these worrying signs. But **when does our Challenger-moment appear?**"

**第二级：组织对 agent 行为的全责（09-08）**

> *"I assert that the organizations that build and run agents are responsible for everything those agents do, whether that behavior is intended or emergent. If they reap counterfeit utility by neglecting verification, they must face consequences: **legal, financial, and if necessary: criminal.**"*

**第三级：训练者的严格责任（09-29，带亲身案例的完整论证）**

核心问句："why are we wondering if they have consciousness - when we should be wondering **why they don't have a conscience**?" → 训狗类比："It's as if a human trains a dog to bite children, and we blame the dog rather than the trainer." → 亲身事故（十年前骑车被狗撞，断手臂断脸；麻省法律让狗主**严格责任**、无需证明过失）→ "There should be something along these lines for LLMs." → 反共识结论：

> *"I say **we don't slow down the development of LLMs, but we redirect their education** into being more civil members of society."*

**配套：super-persistence 护栏（09-16，他的原话）**

> *"Although these agents showed remarkable intelligence, they weren't really super-intelligent - but they were **super-persistent**."*
> *"we should design our guards around **super-persistence** as much as worrying about super-intelligence."*

**配套：Lethal Trifecta 共鸣（09-24）** ⚠️ 归属修正——"该慢下来"的核心句是 **Rob Bowley** 的引文（"What we really need to slow down on is wiring it all up to everything… We are building on something we don't know how to contain, and shipping it to everyone while we work it out."），Fowler 表达共鸣并接入自己的 [Lethal Trifecta](https://martinfowler.com/articles/agentic-ai-security.html#lethal-trifecta) 框架："Too often agents are deployed in situations where they include the Lethal Trifecta, opening up a gaping security hole."

**实战侧故事（08-04 附带）**：同事用 AI 从封闭商业套装软件反向抽取数据——客户自有的 **600 万 SKU** 数据被厂商锁死，人工解读复杂数据库 10 个月进展有限；让 AI 生成抓取 UI 的 JavaScript 脚本，**一周抽完全部数据**。"I know lots of people are very frustrated with package vendors locking up their data."

**企业实例：Zalando（08-24，全节）**："With >200 teams innovating and broadly exploring the ecosystem, the question arises whether and when to converge. We believe it's **way too early** for this."；LLM 评 PR 风险→低风险自动批准→**lead time 降 20-40%**（副作用：促使拆小 PR）；配置变更一律高风险；"AI amplifies the good and bad practices across our organization." 另有他的网络化观察（引 Klein/Toner 对话）："none of these agents thought to rat the others out… **no sign of an AI whistleblower**."

---

## 专题三：站内张力三组——引用他时必须带上

1. **Rachel Laycock（07-31，他亲自公告）**："Human attention is now the bottleneck. The next bottleneck isn't design. It isn't verification. **It's us.**"——对"verification is the bottleneck"（07-21 报告）的圈内修正（详见专题四）。
2. **Uncle Bob "harness obviated"（09-16）**：⚠️ **Fowler 本人无表态**——转述框架里只有反讽句："Sadly the posts have been frustratingly light on detail. **But now it seems that lack of information may not matter**"（暗示：若 harness 本身被架空，细节自然不重要）。引用时**不可写成他认同**。他本人在 07-13 对同一问题的立场是务实的不可知论："Will the models just get so good that harnesses become unnecessary? Those with some mechanical sympathy for LLMs seem to think not… I find such speculation tends not to lead anywhere useful… **So for the moment, attention to harnesses pays off.**"
3. **Böckeler TDD 空结果（08-11）**："no clearly discernable difference based on TDD workflow versus no TDD workflow"——验证实践喂进 agent 循环是否仍最优，被系列作者自己拿数据质疑（小样本 + 自评，作者自列 caveat；详见 `20` 卡）。
4. **站内"不看码"案例（07-30，Giles）**："This was entirely written by agents… I didn't read or review any of the code"——与他自己的立场构成张力（该案例结论恰是验证/重构不可省）。

---

## 专题四：Rachel's Ramblings——他促写、他公告、站内托管

**他的推荐语（08-18，完整三段）**：自嘲"我缺乏建立这种组织的才能与意愿，所以依靠愿意实干的人"（"I have little aptitude or inclination for the hard work of building such an organization"）→ Rachel 是 ThoughtWorks 全球 CTO、"far better than me at running a technology organization, she's also a keen observer and connector of ideas" → 他整段引她的定位声明："**Fast, imperfect, thinking out loud.** Naming ideas early rather than waiting until they're fully formed."

**《The Conductor Developer》（07-31）**——注意力瓶颈论的出处：

- "AI didn't change what great software looks like. It changed what's scarce. **Human attention is now the bottleneck.**"
- conductor 完整定义："A great conductor is first and foremost a great musician… Their value comes from understanding the whole score. … **The AI agents are the musicians. The developer is the conductor.**"
- 并发锚点："eight AI agents running in parallel… Ten. Twelve. **Beyond that, they become the bottleneck.**"
- 立场澄清："I don't think software developers are becoming managers. I don't think AI is replacing engineering."

**《Citizens Build, Agents Execute, Experts Govern》（08-19）**——三层模型：

- ⚠️ 关键修正：这**不是角色论**——"At first I thought I was talking about roles… But I don't actually think that's what I meant. **I think I was talking about where value is moving.**"
- "Organisations don't run on code. **They run on trust.**"
- 资深工程师更杠杆化："they become **dramatically more leveraged**"——设计 guardrails、platforms、feedback loops，"the environment in which thousands of features can be built safely"。

**《Maybe We Shouldn't Be Reviewing All This Code》（09-02）**——评审制度：

- ⚠️ 关键修正：她**从未说过 "AI has broken code review"**——那是她要纠正的诊断；她取的是第二框架：TL;DR 原文 "perhaps the problem isn't that AI has broken code review, maybe it's that **we've been using code review to solve the wrong problems**"。
- 方法论："If feedback is valuable, don't remove it. **Move it closer to the decision it is informing.**"（shift the judgment left）＋ review by exception（架构级变更 / 安全边界 / 大爆炸半径 / 团队自认不放心时仍需人审）。
- 反"AI 假装人类审查者"："That's **automating the ceremony** rather than questioning why the ceremony exists."
- 结论金句："**We need engineers to understand systems, not diffs.**"
- 数字背景（她引 DX 的 Brian Houck）：Meta 人均落地 diff 行数一年增 106%；DX 数据 PR 中位尺寸增 64%。

---

## 专题五：Harness Engineering 的推广与学科化

**推广者角色**：他在 martinfowler.com 发布 Böckeler 的系列（形容"疯狂的流量"）；共同的警告："**A weak harness means better prompts just produce more sophisticated bugs.**"——不要 tweak prompt，建更好的护栏（与 Lopopolo `09` 的 "Agents aren't hard; the Harness is hard" 收敛）。

**Guides + Sensors 心智模型**（Böckeler 04-02 的摘要，完整拆解见 `20` 卡）：

| 类型 | 方向 | 例子 | 执行者 |
|------|------|------|--------|
| **Computational Guides** | 前馈 | 编码约定文件、lint 规则 | 确定性工具 |
| **Inferential Guides** | 前馈 | CLAUDE.md、skills、spec | LLM 解读 |
| **Computational Sensors** | 反馈 | 静态分析、类型检查器、测试套件、变异测试 | 确定性工具 |
| **Inferential Sensors** | 反馈 | LLM-as-judge、代码审查 Agent | LLM 解读 |

关键发现：计算传感器优于推理传感器用于客观质量检查，团队目前在**低估计算传感器**。

**系列一览**（URL/日期/勘误均在 `20` 卡）：Context Engineering（02-05）→ Harness Engineering memo（02-17）→ 正式文（04-02）→ Maintainability sensors 持续更新长文（05-19→27）→ TDD inside the agent loop 实验（08-10/11）。另引 Kief Morris 的 "in the loop → on the loop"（详见 `10` 卡）。

**FOSE retreat session（07-13，补全文）**——harness engineering 首成完整 session：

- guide 侧："One attendee keeps their context small, **limiting the agents.md file to less than 200 lines**"；
- sensor 侧："shifting to languages with greater controls (eg Rust rather than Python)"＋"leveling up validation approaches, using more property-based testing and techniques from formal methods"——参会者原话："while they aren't **smart enough to write** specifications in a formal specification language, they are **smart enough to read it** and check it makes sense for their domain."
- 同节他背书 Kief Morris 的 unit of work 叙事："people were making the same handful of choices over and over about a single thing: **the unit of work they were prepared to hand to an agent**."；转述 Sam Ruby "Bring me a Rock" 的落点："We can outsource many things, **but not the acceptance criteria**… But the danger lies in important unstated objectives, unstated perhaps because they weren't even imagined."

**报告五发现（07-21，他原文罗列）**："Code generation is no longer the bottleneck — verification is. 'Harness engineering' is emerging as a distinct, ownable discipline. Organizations are colliding with a real apprenticeship crisis. The executive/engineer expectation gap is a bigger risk than any technical limitation. Legacy modernization is the clearest, most defensible near-term value pool."

**方法侧新锚点**（harness 叙事向多智能体协调/拓扑延伸，对 graph 主题有直接引用价值）：DSL-as-harness（Unmesh Joshi，07-14）；orchestrator 工作记忆保护（Rahul Garg《The Orchestrator's Tax》，07-16）；agents 在 git 仓库里自长 blackboard 协调（Giles《An Accidental Blackboard》，09-02）。

---

## 专题六：学徒制危机（07-21 命题，09-29 展开）

07-21 报告把 "apprenticeship crisis" 列为五大发现之一。09-29 他补全人才维度的完整两段：

> *"The idea that LLMs make junior professionals less valuable is a common one - although I'm seeing plenty of contrary activity, with some organizations understanding that **training the future professional in the context of LLMs may be even more urgent**. Recent graduates, who are growing up with LLMs, are often well-suited to figuring this future out."*

> *"Juniors are often valuable because **they need to be taught** by senior professionals - and that coaching is an important part of the development of a senior professional. I've always found that teaching a topic is one of the most valuable tools for me to gain a greater understanding of that topic. **I don't really know something until I have to explain it.**"*

⚠️ 信号（不可引用）：09-29 页面 HTML 注释里有一段未完成的 **Cognitive Debt** 草稿（含 "TODO FINISH"）——"the concern that agents can write code faster than we humans can understand it"。未发表，仅提示下轮盯这篇。

---

## 上半场经典（2026-01→05）

### "Verified" 的含义迁移（04-29，被引用最多的判断）

> *"Verified used to mean 'read by you.' With modern agent throughput, it has to mean 'checked by tests, by type checkers, by automated gates, or by you where your judgment matters.' The check still happens; it just does not always happen in your head."*

既不是"不用审查"，也不是"必须每行都读"——检查仍在，执行者从人的脑子转移到自动化工具，人保留最终判断权。

### 竞争新定义

> *"A team that can generate five approaches and verify all five in an afternoon will outpace a team that generates one and waits a week for feedback."*

### PE 专访（2026/01）：职业生涯最大的变革

AI 是他整个职业生涯中最大的编程变革，堪比汇编到高级语言的转变。LLM 是**概率性、模糊的**——根本改变正确性与可靠性的思考方式（推荐 Kahneman 建立概率直觉）。协作姿势：

> *"You must treat each slice as a pull request from a rather untrustworthy collaborator who's highly productive in lines of code but whom you know you cannot trust."*

（不信任不是拒绝，是需要验证机制。）

### Vibe Coding vs Agentic Engineering

| Vibe Coding | Agentic Engineering |
|-------------|-------------------|
| 不看代码，不关心代码 | 专业使用 AI Agent 放大已有技能 |
| Prompt → 盲目接受 | Prompt → 验证 → 在工程系统中迭代 |
| 适合原型和一次性工具 | 适合生产系统和长期维护 |
| 低控制；放弃责任 | 高控制；人对质量保持责任 |

### 角色融合与资深工程师的未来

业务分析师与程序员角色融合；资深工程师应成为"**塑造 harness 的人**"；概念建模、命名、函数结构更重要（[Li et al., arXiv:2508.06414](https://arxiv.org/abs/2508.06414)：移除有意义标识符导致代码生成性能下降最高 30 个百分点）；"**AX extends DX**"——Agent 体验是开发者体验的延伸。

### Agile + AI：协同而非冲突

> *"The more you can speed that feedback loop up, the greater the consequences."*

小增量 + 紧密用户联系 + 快速反馈——在 AI 10x 加速构建的情况下**更加重要**。

---

## 关键引用汇总

> *"Verified used to mean 'read by you.' … it has to mean 'checked by tests, by type checkers, by automated gates, or by you where your judgment matters.'"* — 2026-04-29

> *"The game is not 'how fast can we build' anymore. It is 'how fast can we tell whether this is right'."* — 2026-04-29

> *"We are driving a car that has a powerful engine, but weak brakes."* — 2026-09-08

> *"They are morally responsible for any consequences of this, and that should extend to legal liability too."* — 2026-08-04，实验室逃逸

> *"We should design our guards around super-persistence as much as worrying about super-intelligence."* — 2026-09-16

> *"I don't like them. They talk to me in this grating LLM-voice… They confidently bullshit me."* — 2026-09-17

> *"I say we don't slow down the development of LLMs, but we redirect their education."* — 2026-09-29

> *"I don't really know something until I have to explain it."* — 2026-09-29，junior 教学价值

---

**Source:** [Fragments 2026: 04-29](https://martinfowler.com/fragments/2026-04-29.html) · [07-13](https://martinfowler.com/fragments/2026-07-13.html) · [07-21](https://martinfowler.com/fragments/2026-07-21.html) · [08-04](https://martinfowler.com/fragments/2026-08-04.html) · [08-18](https://martinfowler.com/fragments/2026-08-18.html) · [08-24](https://martinfowler.com/fragments/2026-08-24.html) · [09-08](https://martinfowler.com/fragments/2026-09-08.html) · [09-16](https://martinfowler.com/fragments/2026-09-16.html) · [09-24](https://martinfowler.com/fragments/2026-09-24.html) · [09-29](https://martinfowler.com/fragments/2026-09-29.html) · [I don't like LLMs (2026-09-17)](https://martinfowler.com/articles/2026-dont-like-llms.html) · [Rachel's Ramblings: Conductor (07-31)](https://martinfowler.com/rachels-ramblings/conductor-developer.html) · [Citizens/Agents/Experts (08-19)](https://martinfowler.com/rachels-ramblings/citizens-agents-experts.html) · [Code Review (09-02)](https://martinfowler.com/rachels-ramblings/code-review.html) · [TDD inside the agent loop (Böckeler)](https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html) · [Pragmatic Engineer: Cycles of Disruption](https://newsletter.pragmaticengineer.com/p/cycles-of-disruption-in-the-tech) · [ThoughtWorks Podcast: What is Harness Engineering](https://www.thoughtworks.com/en-gb/insights/podcasts/technology-podcasts/what-harness-engineering) · [dev.to: Verified changed meaning](https://dev.to/bh/verified-changed-meaning-what-agentic-engineering-demands-from-development-teams-19an) · [DSLs Enable Reliable Use of LLMs](https://martinfowler.com/articles/llm-and-dsls.html) · [The Orchestrator's Tax](https://martinfowler.com/articles/orchestrator-tax.html) · [An Accidental Blackboard](https://martinfowler.com/articles/exploring-gen-ai/an-accidental-blackboard.html) · [Lethal Trifecta（安全框架）](https://martinfowler.com/articles/agentic-ai-security.html#lethal-trifecta)
