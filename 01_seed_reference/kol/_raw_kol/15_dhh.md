---
type: kol_deep_dive
person: DHH (David Heinemeier Hansson)
organization: 37signals / Ruby on Rails / Omarchy
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://www.youtube.com/watch?v=vDjW_dRyKXY
  - https://www.rubyevents.org/talks/opening-keynote-rails-world-2026
  - https://lexfridman.com/dhh-2-transcript/
  - https://world.hey.com/dhh/endless-execution-4157e065
  - https://thoughteconomics.com/david-heinemeier-hansson/
  - https://world.hey.com/dhh/i-m-sorry-dave-380ec27d
  - https://github.com/omacom/omarchy/pull/13770
key_concepts:
  - pencils_down
  - agent_accelerated_development
  - endless_execution
  - agent_luther
  - open_weight_advocacy
  - anti_upfront_specification
---

# DHH — "Pencils down"：从 AI coding 头号抵制者到最激进的 agent 派

> Ruby on Rails 创造者、37signals 联合创始人。2023–2025 年他是"不用 AI 写代码"的最著名声明者；他把拐点自定为 2025-11-24（"the Kodak Brownie of our era"），此后 180° 转身——2026-09-23 在 Rails World 2026 开幕 keynote 官宣 37signals **"pencils down on hand-written code"**。他的自我标签既不是 agentic engineering 也不是 vibe coding，而是 **"agent-accelerated development"**。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。建卡日 2026-10-03（增量核查窗口 2026-07-01 ～ 10-03，一手英文源）。

## 当前立场小结（2026-10-03 建卡）

1. **37signals 全公司层面官宣停止手写生产代码**——"pencils down on hand-written code"（Rails World 2026 开幕 keynote，2026-09-23, Austin）。
2. **个人旗舰项目已 100% agent 加速**——"I have not written any of the code that's shipped in Quattro by hand."（Omarchy Quattro，Lex #501）
3. **但明确拒绝 vibe coding 路线**——"vibe coding to me smells exactly like script kiddies did in the early 2000s"；不看实现是他划的线，Basecamp 5 "let them vibe" 的 PRs "destroyed the architecture of the system"。
4. **标准作业是多 agent 流水线**——Opus/Fable 写 → Codex xHigh 评审 → Copilot 补审；开源权重走 OpenCode + Fireworks（Kimi K3）；叠加购买多个 Claude/Codex 订阅（omarchy PR #13770 为实证）。
5. **反 upfront 精细化**——"resist the temptation to be overly specific upfront. Be as vague as you can"；AGENTS.md 过度具体反而 damaging（引 Opus 5 系统提示缩减 80%）。
6. **独有政治轴**——反 Anthropic "safety" 叙事、力挺开源权重（含中国模型）、Agent Luther 反程序员祭司阶层、P(bloom) over P(doom)。

---

## 立场背景（2025 及更早，一句话带过）

2023–2025 公开声明不做 AI-assisted coding；2025 年夏在 Lex 节目仍说 "did not let AI write his code, and that programmers learn with their fingers"，同年自述 "can literally feel competence draining out of my fingers"（回溯见 [Thought Economics 2026-09-28](https://thoughteconomics.com/david-heinemeier-hansson/)）。2026 上半年过渡轨迹：《Promoting AI agents》(01-07)、《Basecamp becomes agent accessible》(03-25)、Pragmatic Engineer Ep.58 *"DHH's new way of writing code"* (04-08)、《Let the agents democratize open source》(06-01)。

---

## Rails World 2026 开幕 keynote："Pencils down"（2026-09-23）

官方视频（1:03:07）章节表（自述，节选）：

> "November 24, 2025: the Kodak Brownie of our era" · "37signals goes pencils down on hand-written code" · "What vibe-coding Basecamp 5 taught us" · "150,000 lines of code in a month" · "English: the programming language DHH likes better than Ruby" · "Retiring from hand-written code, with joy" · "Rethinking software architecture for the age of agents" · "Bring your own agent: why every app needs a CLI" · "P(bloom) over P(doom)"

RubyEvents 官方简介：

> "DHH opens Rails World 2026 in Austin with a keynote on the age of AI agents: why 37signals has gone 'pencils down' on handwritten code, **why Rails' convention over configuration is built for this moment**, and why the only play left is total optimism."

判读：本窗口最重磅信号——一家以 Rails 为生的公司官宣停止手写代码，且把 convention over configuration 重新论证为 **agent 时代的架构优势**（可预测的约定 = agent 友好）。注意：The Verge（09-24，二手）"37signals 正在远离 Ruby"是媒体演绎——一手章节表反而强调 Rails 的适配性；二手源仅作交叉核对，不作证据。

次日（09-24）与 Matz 的官方 fireside chat 把身份迁移定调为社区议程："the identity shift from **software writer to software maker**, why taste and joy still matter"（[RubyEvents 同页](https://www.rubyevents.org/talks/opening-keynote-rails-world-2026)）。

---

## Lex Fridman #501（2026-08-26）：翻转的完整操作化

官方转录全文（human-generated）。关键自述：

> "the agent acceleration neared 100%, and in the last two months it has been 100%. **I have not written any of the code that's shipped in Quattro by hand.**"

> "we let them vibe. And we ended up with a lot of PRs that individually perhaps could have been justified for a hot moment, but taken all together, **destroyed the architecture of the system**. And we actually had to clean up manually, mop it up by hand."（Basecamp 5 教训，2026-02）

> "Agentic engineering? Oh, I fucking hate that term… It's become marketing slop speak… vibe coding to me smells exactly like script kiddies did in the early 2000s… **that is what separates vibe coding from… agent-accelerated development.**"

> "more often than not, I have the humility to recognize that **the agent knows best**."＋"the system prompt that they ship for Opus 5… shrunk by 80% because the agent not only needed far less human instruction, it was actually being damaged by overly prescriptive humans."

> "**resist the temptation to be overly specific upfront. Be as vague as you can** to manifest something, then interact with the something."

标准作业（SOP）自述：*"I'll have an Opus or Fable do the work, and then I always end it, review with Codex xHigh."*；*"I use OpenCode mainly as my main harness for all the open models, so Kimi K3 and so forth… on Fireworks"*；*"Copilot, I kid you not, has actually gotten good."*；*"I have not written any Bash myself for probably a couple months."*

对"评审"的让渡（引 Shopify CTO Mikhail 的生产事故回溯研究）：*"At this point, 100% in the majority of domains we work in today, **agents are better at finding bugs**."*

人的新位置：*"I'm a da Vinci, working with his whole studio of students… I can give feedback like an editor."*＋"in the agentic era… these are the skills you need"（产品判断）。

---

## 《Endless execution》（2026-08-09）：乐趣的重新定义

> "The age of agents has brought us endless execution. Every idea, every hunch, every experiment is now within immediate reach. For people with endless ideas, this is nirvana."

> "**This is simply the most fun I've ever had with a computer.** And I've loved them dearly for over forty years. I loved programming them myself… But none of it as much as I love the power to execute every idea that crosses my mind."

> "AGI is a nefarious concept to pin down, but I'm not sure how different whatever definition we eventually settle on will look from what I'm already experiencing on the daily."

判读：与"编程的乐趣不可外包"旧立场正面对撞后的新答案——乐趣的定义从"亲手写"换成"无限执行"，并暗示日常体验已接近 AGI 的实际形态。

---

## Thought Economics（2026-09-28）：经济判词与 Agent Luther

> "The frontier models, especially when you run them in collaboration with each other, are **better than virtually every programmer on Earth** at a broad set of programming skills… If you don't believe that, you simply haven't spent enough time working with these systems directly."

> "my programming skills, as they were, are **no longer economically viable** as independent leverage for creating things."

> "The mechanical notion of taking some requirements and turning them into code is **not going to have economic value going forward**."

> "Now you've got **Agent Luther** here, disintermediating everyone and providing a direct connection to the machine… there's a loss of identity here for an entire class of developers who saw themselves as particularly gifted."

> "What I'm saying now, I would not have said in February. The change has really gone vertical… in the last three, maybe four months. Since we got Fable, we're on a different trajectory."

另：宣判纯客户端软件生意 "borrowed time"（Adobe 一类将面对百万个 vibe coded 开源替代品）。

---

## 政治轴：开源权重与反审查（2026-07-27《I'm sorry, Dave》）

> "we desperately need **strong open-weight models** to protect ourselves against this kind of soft ideological tyranny, which can turn into hard repression real quick if a monopoly status is ever locked in."

> "Anthropic has built their entire brand around 'safety.'… But when the reality turns out to be a HAL 9000 denying to translate the most banal political commentary… you got to ask, 'Safety from what? Alignment with whom?'"

> "What an upside world when **Chinese open-weight models** will tell us about Tiananmen Square, but American frontier models won't translate a blog post."

判读：起因是 Claude 拒绝为他一篇争议博文翻译。这是库内主流 agentic 派（Beck/Fowler/Willison）都不占的轴：他把 agent 化接入反建制叙事——Agent Luther 反"程序员祭司阶层"、开源权重反意识形态垄断、P(bloom) over P(doom)。

---

## 与库内其他人物的立场对照

- **对手写代码终局**：Fowler 卡的口径是"竞争变成'能多快判断对错'"（验证仍是人的工程责任）——DHH 连"评审关键代码"都让渡给 agent（引 Shopify 研究）。两卡对照即光谱两端。
- **对 harness 精细化**：Fowler/Beck 一路主张 guides/sensors 越建越强、TDD 是边界；DHH 反向："be as vague as you can"、AGENTS.md 过度具体反而 damaging。
- **对词汇**：DHH 同时拒绝 "agentic engineering"（marketing slop）与 "vibe coding"（script kiddies）；Karpathy 卡（07）是这两个词的起源地。
- （跨人的系统判读沉淀在 `02_research/` 对应主题，本卡只做立场定位。）

---

## 关键引用汇总

> *"I have not written any of the code that's shipped in Quattro by hand."* — Lex #501, 2026-08-26

> *"37signals goes pencils down on hand-written code."* — Rails World 2026 keynote, 2026-09-23

> *"vibe coding to me smells exactly like script kiddies did in the early 2000s."* — 同上访谈

> *"Be as vague as you can to manifest something, then interact with the something."* — 同上访谈

> *"Taking some requirements and turning them into code is not going to have economic value going forward."* — Thought Economics, 2026-09-28

> *"This is simply the most fun I've ever had with a computer."* — 《Endless execution》, 2026-08-09

---

**Source:** [Rails World 2026 Opening Keynote（官方视频）](https://www.youtube.com/watch?v=vDjW_dRyKXY) · [RubyEvents 官方条目（keynote + Matz fireside chat）](https://www.rubyevents.org/talks/opening-keynote-rails-world-2026) · [Lex Fridman #501 官方转录](https://lexfridman.com/dhh-2-transcript/) · [Endless execution](https://world.hey.com/dhh/endless-execution-4157e065) · [I'm sorry, Dave](https://world.hey.com/dhh/i-m-sorry-dave-380ec27d) · [Thought Economics 访谈](https://thoughteconomics.com/david-heinemeier-hansson/) · [Sitting down with Senra](https://world.hey.com/dhh/sitting-down-with-senra-69f5e368) · [omacom/omarchy PR #13770](https://github.com/omacom/omarchy/pull/13770) · [Rails World 2026 官方回顾](https://rubyonrails.org/2026/10/1/rails-world-2026-recap)
