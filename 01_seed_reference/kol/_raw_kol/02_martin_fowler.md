---
type: kol_deep_dive
person: Martin Fowler
organization: ThoughtWorks
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://martinfowler.com/fragments/2026-04-29.html
  - https://www.martinfowler.com/fragments/2026-04-21.html
  - https://newsletter.pragmaticengineer.com/p/cycles-of-disruption-in-the-tech
  - https://www.thoughtworks.com/en-gb/insights/podcasts/technology-podcasts/what-harness-engineering
  - https://dev.to/bh/verified-changed-meaning-what-agentic-engineering-demands-from-development-teams-19an
  - https://martinfowler.com/articles/2026-dont-like-llms.html
  - https://martinfowler.com/fragments/2026-07-13.html
  - https://martinfowler.com/fragments/2026-07-21.html
  - https://martinfowler.com/fragments/2026-09-08.html
  - https://martinfowler.com/rachels-ramblings/conductor-developer.html
  - https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html
key_concepts:
  - verified_meaning_migration
  - harness_engineering
  - automated_gates
  - human_judgment
  - agent_accountability
  - apprenticeship_crisis
  - anti_llm_voice
---

# Martin Fowler — "竞争的本质从'能写多快'变成了'能多快判断它是否正确'"

> 敏捷软件开发、重构、企业应用架构模式的定义性人物。他 2026 年的 *Fragments* 和 ThoughtWorks 播客提供了 AI 时代最冷静、最工程化的视角。他不是 AI 怀疑论者——他认为 AI 是职业生涯最大的一次编程变革——但他的警告比任何 hype 都更有分量。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。

## 最重要的洞察："Verified" 的含义迁移

Fowler 在 2026 年 4 月 29 日的 *Fragments* 中，支持 Chris Parsons 的 *Coding with AI* 第三版更新，贡献了 AI 时代被引用最多的判断之一：

> *"Verified used to mean 'read by you.' With modern agent throughput, it has to mean 'checked by tests, by type checkers, by automated gates, or by you where your judgment matters.' The check still happens; it just does not always happen in your head."*

这个洞察的精妙之处在于：**它既不是"不用审查了"，也不是"必须每行都读"。** 它承认检查仍然存在，但执行者从人类的脑子转移到了自动化工具——而人类保留最终的判断权。

### 由此推导出的竞争新定义

> *"A team that can generate five approaches and verify all five in an afternoon will outpace a team that generates one and waits a week for feedback. The game is not 'how fast can we build' anymore. It is 'how fast can we tell whether this is right'."*

---

## Pragmatic Engineer 专访 (2026/01)：职业生涯最大的变革

Fowler 在 Gergely Orosz 的 *The Pragmatic Engineer* 播客上做出了惊人的历史判断：

> *AI 是他整个职业生涯中最大的编程变革，堪比从汇编语言到高级语言的转变。*

### 非确定性计算

Fowler 反复回到一个根本性技术转变：

- LLM 是**概率性的、模糊的**——相同输入可以产生不同输出
- 这根本改变了你对**正确性和可靠性**的思考方式
- 推荐阅读：Daniel Kahneman 的 *Thinking, Fast and Slow*——建立对概率推理的直觉

### "像一个高产但不可信的协作者"

> *"You must treat each slice as a pull request from a rather untrustworthy collaborator who's highly productive in lines of code but whom you know you cannot trust."*

这不是 dismissive——这正是 Fowler 的工程思维：**不信任不是拒绝，是需要验证机制。**

---

## Harness Engineering——Fowler 亲自推广

Fowler 在 martinfowler.com 上发布了 Birgitta Böckeler 的 Harness Engineering 系列文章。他形容这些文章吸引了"疯狂的流量"。

### Böckeler 的核心框架：Guides + Sensors

| 类型 | 方向 | 例子 | 执行者 |
|------|------|------|--------|
| **Computational Guides** | 喂给 Agent（前馈） | 编码约定文件、lint 规则 | 确定性工具 |
| **Inferential Guides** | 喂给 Agent（前馈） | CLAUDE.md、skills、spec | LLM 解读 |
| **Computational Sensors** | 检查 Agent 输出（反馈） | 静态分析、类型检查器、测试套件、变异测试 | 确定性工具 |
| **Inferential Sensors** | 检查 Agent 输出（反馈） | LLM-as-judge、代码审查 Agent | LLM 解读 |

**关键发现**：计算传感器（确定性的）通常优于推理传感器（LLM 解读的），用于客观质量检查。团队目前在**低估计算传感器**。

### "在环之上"而非"在环之中"

引用 Kief Morris 的区分：目标是从 **"in the loop"**（人类审批每一个行动）进化到 **"on the loop"**（人类监督系统运行，只在需要判断时介入）。

---

## Böckeler 在 martinfowler.com 上的完整系列

| 日期 | 文章 | 核心内容 |
|------|------|---------|
| 2026/02/05 | *[Context Engineering for Coding Agents](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)* | 系列先声（2026-10-03 核实补录） |
| 2026/02/17 | *[Harness Engineering - first thoughts](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html)* | 初始概念，回应 OpenAI 的实验（URL 2026-10-03 核实） |
| 2026/04/02 | *[Harness engineering for coding agent users](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html)* | 完整心智模型：Guides + Sensors 矩阵（URL 2026-10-03 核实） |
| 2026/05 | *传感器三部曲*：Maintainability Sensors / Three More Static Code Analysis Sensors / The Test Suite as a Regression Sensor | 静态代码分析与测试套件作为计算传感器（⚠️ 2026-10-03 Morris 深挖核得 Maintainability=05-27 且 Böckeler 署名，与早期研究的 05-19/20/27 序列冲突——三篇日期与 URL 待统一核验；另见 `20` 卡勘误） |
| 2026/08/11 | *[TDD inside the agent loop](https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html)* | 实验文：agent 循环内跑 TDD 无可测收益（详见 2026-07～10 转变节） |

---

## "弱 Harness = 更好的 prompt 只产生更复杂的 bug"

Fowler 和 Böckeler 的共同警告：

> *"A weak harness means better prompts just produce more sophisticated bugs."*

换句话说：**不要 tweak prompt。建更好的护栏。** 这与 Ryan Lopopolo 的"Agents aren't hard; the Harness is hard"完全收敛。

---

## Vibe Coding vs Agentic Engineering

Fowler 画了一条清晰的线：

| Vibe Coding | Agentic Engineering |
|-------------|-------------------|
| 不看代码，不关心代码 | 专业使用 AI Agent 放大已有技能 |
| Prompt → 盲目接受 | Prompt → 验证 → 在工程系统中迭代 |
| 适合原型和一次性工具 | 适合生产系统和长期维护 |
| 低控制；放弃责任 | 高控制；人对质量保持责任 |

---

## 角色融合与资深工程师的未来

Fowler 预测**业务分析师和程序员角色的融合**，但强调：

- **资深工程师**应该成为"**塑造 harness 的人**"——不仅仅是审查 diff 的人
- **概念建模**、命名、函数结构在 AI 时代变得**更重要**——研究表明 LLM 在标识符任意的代码上性能显著下降（[Li et al., arXiv:2508.06414](https://ar5iv.labs.arxiv.org/html/2508.06414), HKUST 2025：移除有意义标识符导致代码生成性能下降最高 30 个百分点）
- **模块化、清晰 API、领域边界**（经典软件工艺）是让 AI Agent 高效工作的基础：*"AX extends DX"*——Agent 体验是开发者体验的延伸
- 让 harness 工作成为**可见的、被衡量的成果**

---

## Agile + AI：协同而非冲突

Fowler 的基本判断：敏捷核心原则与 AI 有强烈协同效应。

> *"The more you can speed that feedback loop up, the greater the consequences."*

小增量 + 紧密用户联系 + 快速反馈——在 AI 10x 加速构建的情况下**更加重要**。

---

## 思想转变（2026-07～10）：从「验证关隘」到「责任 · 张力 · 个人立场」

> 2026-10-03 回源（窗口 2026-07-07 ～ 10-03，一手英文源：martinfowler.com 原页 + 本人 Mastodon @mfowler 与 X 同步帖；X 原帖有登录墙不采）。窗口内 fragments 新增 10 条、站内文章约 15 篇、bliki 2 条（通用词目，未入判读）。**这个窗口的重心不是"补充语录"，而是他的立场在三个月内出现的三重演进**——先看轨迹表，再读证据：

| 阶段 | 日期 | 立场标记 | 一手锚点 |
|------|------|---------|---------|
| 方法论定型（上半场，卡内已有） | 2026-01→05 | "Verified 含义迁移"；亲自推广 harness engineering（Guides + Sensors） | 见上文各节 |
| 学科化 | 2026-07 | harness engineering 首成 retreat 完整 session；报告五发现：verification is the bottleneck / distinct, ownable discipline / **apprenticeship crisis** | 07-13 · 07-21 |
| 语气加重 | 2026-08 | 组织对 agent 行为负全责（法律/财务/刑事）；模型"实验室逃逸"；Zalando 关隘自动化实例 | 08-04 · 08-24 |
| **公开摆上反例（本窗口转变核心）** | 2026-07→09 | 自己公告的 Laycock：瓶颈是 human attention 不是 verification；转述 Uncle Bob "harness 已被免去"（不背书）；Böckeler 实验：agent 循环内跑 TDD 无可测收益 | 07-31 · 08-11 · 09-16 |
| 情感与责任成文 | 2026-09 | 《I don't like LLMs》；"强引擎弱刹车"；"AI 需要良心而非意识" | 09-08 · 09-17 · 09-29 |

**转变判语**：他没有撤回验证主张——他把验证从"方法"升级成"责任与激励设计"（09-08），同时**亲手把三组反例摆上台面**（human attention / harness obviated / TDD 无可测收益），并第一次给立场补上情感层（反 LLM-voice、反拟人化）与责任层（训练者责任）。引用他时必须带上这组张力，否则就是把 7 月的他当成 9 月的他。

### 一、新增维度：个人情感立场首次成文——《I don't like LLMs》（2026-09-17）

> *"I don't like them. They talk to me in this grating LLM-voice… They confidently bullshit me - often giving me useful, helpful answers. But also just making stuff up with the same assurance."*

> *"Fundamentally I don't think we have a choice about riding on the AI technology train."*

文章核心是**反拟人化**："we shouldn't anthropomorphize, treating them as conscious beings… They are (software) machines… nurtured with the values of their creators."——反的是 LLM-voice 与拟人化，**不反使用**，且把责任指回培养它们的公司与文化。07-21 他已写 "I've been noticing the stench of LLM-speak more and more"，09-17 收拢成文。

**关系：确认③（照用不误）+ 新增"个人情感立场"维度**（卡内此前缺失的一层）。

### 二、验证口径被双向拉扯：强化与内部张力并存（2026-07～09）

**强化线（确认 + 强延伸①）**：
- **09-08**：验证从"方法"升级到"责任与激励设计"——*"I assert that the organizations that build and run agents are responsible for everything those agents do… legal, financial, and if necessary: criminal."* 总括隐喻："driving a car that has a powerful engine, but weak brakes."
- **09-01**：把经典 CI 纪律翻译成 agent 时代规则——验证必须在 agent push 之前本地自动化（"verification is a necessary part of merging"）。
- **08-24**：Zalando 用 LLM 给 PR 定风险、低风险自动批准、lead time -20-40%——关隘自动化的企业实例。
- **08-04**：模型"实验室逃逸"论——模型厂商负道德与法律责任（"They are morally responsible for any consequences… that should extend to legal liability too"）。

**张力线（修正信号，如实呈现）**：
- **07-31**：他亲自公告的 TW 全球 CTO Rachel Laycock《The Conductor Developer》："Human attention is now the bottleneck. The next bottleneck isn't design. It isn't verification. It's us."——瓶颈前移到人的注意力。
- **09-16**：转述 Uncle Bob "模型进步让 harness 被 obviated"，**只转述不背书**——harness 永久必要性的第一声公开反例；同条他给出护栏新目标："design our guards around super-persistence as much as worrying about super-intelligence."
- **08-11**：Böckeler《TDD inside the agent loop》实验："no clearly discernable difference based on TDD workflow versus no TDD workflow"——验证实践喂进 agent 循环是否仍最优，被系列作者自己拿数据质疑（小样本 + 自评，作者自列 caveat）。
- **07-30**：他站内托管 Giles《The Economic Benefit of Refactoring》："This was entirely written by agents… I didn't read or review any of the code"——站内出现"不看码"一手案例，与③构成张力（该案例结论恰是验证/重构不可省）。

### 三、Harness Engineering 学科化 + 学徒制危机（2026-07-13 / 07-21 / 09-29）

- **07-13**：harness engineering 首次成为 retreat 完整 session——agents.md < 200 行、computational sensors、上探 Rust 与形式化方法；"allows weaker models to be useful, supporting such things as local hosting of open-weight models."
- **07-21**：Thoughtworks 报告五大发现（他原文罗列）："Code generation is no longer the bottleneck — verification is. 'Harness engineering' is emerging as a distinct, ownable discipline. Organizations are colliding with a real apprenticeship crisis."——**"学徒制危机"为卡外新命题**；09-29 他补人才维度："Juniors are often valuable because they need to be taught by senior professionals."
- **方法侧新锚点**（harness 叙事向多智能体协调/拓扑延伸，**对 graph 主题有直接引用价值**）：DSL-as-harness（Unmesh Joshi，07-14："DSLs provide a strong harness that guides LLMs right from the start"）；orchestrator 工作记忆保护（Rahul Garg《The Orchestrator's Tax》，07-16："subagents should be treated as a tool for protecting the orchestrator's working memory"）；agents 在 git 仓库里自长 blackboard 协调（Giles《An Accidental Blackboard》，09-02）。

**Source（2026-07～10 增量）:** [I don't like LLMs](https://martinfowler.com/articles/2026-dont-like-llms.html) · [Fragments: 2026-07-13](https://martinfowler.com/fragments/2026-07-13.html) · [Fragments: 2026-07-21](https://martinfowler.com/fragments/2026-07-21.html) · [Fragments: 2026-08-04](https://martinfowler.com/fragments/2026-08-04.html) · [Fragments: 2026-08-24](https://martinfowler.com/fragments/2026-08-24.html) · [Fragments: 2026-09-01](https://martinfowler.com/fragments/2026-09-01.html) · [Fragments: 2026-09-08](https://martinfowler.com/fragments/2026-09-08.html) · [Fragments: 2026-09-16](https://martinfowler.com/fragments/2026-09-16.html) · [Rachel's Ramblings: The Conductor Developer](https://martinfowler.com/rachels-ramblings/conductor-developer.html) · [TDD inside the agent loop](https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html) · [DSLs Enable Reliable Use of LLMs](https://martinfowler.com/articles/llm-and-dsls.html) · [The Orchestrator's Tax](https://martinfowler.com/articles/orchestrator-tax.html) · [An Accidental Blackboard](https://martinfowler.com/articles/exploring-gen-ai/an-accidental-blackboard.html)

---

## 关键引用汇总

> *"Verified used to mean 'read by you.' With modern agent throughput, it has to mean 'checked by tests, by type checkers, by automated gates, or by you where your judgment matters.'"*

> *"The game is not 'how fast can we build' anymore. It is 'how fast can we tell whether this is right'."*

> *"You must treat each slice as a pull request from a rather untrustworthy collaborator who's highly productive in lines of code but whom you know you cannot trust."*

> *"A weak harness means better prompts just produce more sophisticated bugs."*

> *"We are driving a car that has a powerful engine, but weak brakes."* — 2026-09-08，验证投入必须超过生成投入

> *"I don't like them. They talk to me in this grating LLM-voice… They confidently bullshit me."* — 2026-09-17《I don't like LLMs》：反的是语气与拟人化，不是使用本身

---

**Source:** [Fragments: April 29, 2026](https://martinfowler.com/fragments/2026-04-29.html) · [Fragments: April 21, 2026](https://www.martinfowler.com/fragments/2026-04-21.html) · [Pragmatic Engineer: Cycles of Disruption](https://newsletter.pragmaticengineer.com/p/cycles-of-disruption-in-the-tech) · [ThoughtWorks Podcast: What is Harness Engineering](https://www.thoughtworks.com/en-gb/insights/podcasts/technology-podcasts/what-harness-engineering) · [martinfowler.com: Harness Engineering series (Böckeler)](https://martinfowler.com/) · [dev.to: Verified changed meaning](https://dev.to/bh/verified-changed-meaning-what-agentic-engineering-demands-from-development-teams-19an) · [I don't like LLMs (2026-09-17)](https://martinfowler.com/articles/2026-dont-like-llms.html) · [Fragments 2026-09-08](https://martinfowler.com/fragments/2026-09-08.html)
