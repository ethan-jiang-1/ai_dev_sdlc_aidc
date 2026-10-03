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
  - https://lexfridman.com/dhh-david-heinemeier-hansson-transcript/
  - https://world.hey.com/dhh/promoting-ai-agents-3ee04945
  - https://world.hey.com/dhh/basecamp-becomes-agent-accessible-3ae6b949
  - https://newsletter.pragmaticengineer.com/p/dhhs-new-way-of-writing-code
  - https://world.hey.com/dhh/the-malleable-computer-7c187a9b
  - https://world.hey.com/dhh/let-the-agents-democratize-open-source-9fd630a9
  - https://www.anthropic.com/news/claude-opus-4-5
key_concepts:
  - pencils_down
  - agent_accelerated_development
  - endless_execution
  - agent_luther
  - open_weight_advocacy
  - anti_upfront_specification
  - opus_4_5_inflection
  - supervised_collaboration
---

# DHH — "Pencils down"：从 AI coding 头号抵制者到最激进的 agent 派

> Ruby on Rails 创造者、37signals 联合创始人。2023–2025 年他是"不用 AI 写代码"的最著名声明者；他把拐点自定为 2025-11-24——**Claude Opus 4.5 发布日**（"the Kodak Brownie of our era"），此后 180° 转身——2026-09-23 在 Rails World 2026 开幕 keynote 官宣 37signals **"pencils down on hand-written code"**。他的自我标签既不是 agentic engineering 也不是 vibe coding，而是 **"agent-accelerated development"**。

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

## 思想转变轨迹：从抵制到 pencils down（2025-07 → 2026-09）

> 2026-10-03 前半程回源（Lex #474 官方 transcript + RSS 日期核验、world.hey.com 逐篇直抓、Anthropic 官方页核验；X 原帖登录墙未核处均标注）。**这是库内唯一的"立场反转"样本，且转变的分水岭是模型事件，不是顿悟**——先看轨迹表，再读后半程证据：

| 阶段 | 日期 | 立场标记 | 关键原句 / 锚点 |
|------|------|---------|----------------|
| 抵制态 | 2025-07-12 | 手艺/学习论（不是"AI 无用"论）：拒自动补全、怕 competence 流失、自嘲当"agent 乌鸦群的项目经理" | Lex #474："**I chisel them out of the screen with my bare hands. I don't auto-complete.**" / "**I can literally feel competence draining out of my fingers.**"（01:29:03，此句原始出处即此）/"I have to do the typing myself **because you learn with your fingers.**"（吉他类比）/"**a project manager of a murder of AI crows**" / "I don't actually use it very much for Ruby code." |
| 抵制的边界 | 2025-10-07 | 只反"替我写码"，不反 AI 内容 | 博文《Give me AI slop over human sludge any day》 |
| **拐点** | 2025-11-24 | **Claude Opus 4.5 发布日**——后被他定名为 "the Kodak Brownie of our era"（keynote 官方章节 [00:11:20]）。当天本人原话无一手可核（X 登录墙）；可核锚点：Anthropic 官方页 datePublished=2025-11-24 + 次日博文已锚定"租用 frontier 模型干活" | 《Local LLMs…》(11-25)："you'll be back to using the rented models **for the vast majority of the work you're doing**."；PE#58 追述："it just happened from November… when Opus 4.5 dropped."（他把日期记成 27，实际 24） |
| 自我修正分水岭 | 2026-01-07 | 给 2025 年夏的自己打补丁：agent 从"顾问"升职为"能出生产级贡献的同事"，但仍自任把关人 | 《Promoting AI agents》："**At the end of last year, AI agents really came alive for me.**" / "**Yes, I'm ready to give the current crop of AI agents a promotion.**" / "I'm nowhere close to the claims of having agents write 90%+ of the code… **if I hold the line on quality and cohesion.**" / "Supervised collaboration, though, is here today." |
| 升为公司战略 | 2026-03-25 | 个人用法 → 37signals 全线产品的一等公民接口 | 《Basecamp becomes agent accessible》："**Anything you can do in Basecamp, agents can now do too.**" / "This is where the puck is going." |
| agent-first 日常化（判断权仍在手） | 2026-04-08 | "code first" → "agent first"；4 月刻度＝还留 review 和 taste——与 8 月的差值就是这一步 | PE#58："**I went from early November last year — code first… Now I start with the agent.**" / "stepping into this **super mech suit**… **I'm still the one doing it, even if I'm not typing.**" / "90 minutes… I processed 100 PRs… maybe 10% got merged as is… What the heck?" / 保留："Then I'll go in and also code myself." |
| 论域换轨 | 2026-04-15 | 从"护手艺"换成"AI 兑现个人计算/开源能动性承诺" | 《The malleable computer》："**Now, with AI, it suddenly isn't [too hard].**" / "AI is compressing that complexity and making it malleable at a ferocious rate." |
| 为 agent 参与权站队 | 2026-06-01 | 把 AI 辅助贡献权定义为开源创始愿景，守门者 = "旧行会" | 《Let the agents democratize open source》："…**to preserve the privileges of the old programmer guilds.**" / "**Don't succumb to this insular, fearful, protectionist thinking. Programming is evolving.**" |
| 乐趣重定义 → 100% → pencils down | 2026-07→09 | 见下文各节（Endless execution / Lex #501 / Rails World / Thought Economics） | — |

**转变判语**：2025-07 他说"AI 让我指尖的 competence 流失"，2026-09 他说"手写代码退役，怀着喜悦"。中间每一格都有日期与一手锚点：**模型跃迁（Opus 4.5，2025-11-24）→ 工作流改造（升职 → 产品化 → agent-first）→ 乐趣重定义（07）→ 判断权让渡（08 "agent knows best"）→ 组织与经济结论（09 pencils down / Agent Luther）**。4 月的 "super mech suit / I'm still the one doing it" 与 8 月的 "agent knows best" 之间的差值——把"还是我在做"改成"agent 最懂"——就是他走完反转的最后一格。

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

> *"I can literally feel competence draining out of my fingers."* — Lex #474, 2025-07-12（转变弧线的起点）

> *"Yes, I'm ready to give the current crop of AI agents a promotion."* — 2026-01-07（自我修正分水岭）

> *"I have not written any of the code that's shipped in Quattro by hand."* — Lex #501, 2026-08-26

> *"37signals goes pencils down on hand-written code."* — Rails World 2026 keynote, 2026-09-23

> *"vibe coding to me smells exactly like script kiddies did in the early 2000s."* — 同上访谈

> *"Be as vague as you can to manifest something, then interact with the something."* — 同上访谈

> *"Taking some requirements and turning them into code is not going to have economic value going forward."* — Thought Economics, 2026-09-28

> *"This is simply the most fun I've ever had with a computer."* — 《Endless execution》, 2026-08-09

---

**Source:** [Rails World 2026 Opening Keynote（官方视频）](https://www.youtube.com/watch?v=vDjW_dRyKXY) · [RubyEvents 官方条目（keynote + Matz fireside chat）](https://www.rubyevents.org/talks/opening-keynote-rails-world-2026) · [Lex Fridman #501 官方转录](https://lexfridman.com/dhh-2-transcript/) · [Endless execution](https://world.hey.com/dhh/endless-execution-4157e065) · [I'm sorry, Dave](https://world.hey.com/dhh/i-m-sorry-dave-380ec27d) · [Thought Economics 访谈](https://thoughteconomics.com/david-heinemeier-hansson/) · [Sitting down with Senra](https://world.hey.com/dhh/sitting-down-with-senra-69f5e368) · [omacom/omarchy PR #13770](https://github.com/omacom/omarchy/pull/13770) · [Rails World 2026 官方回顾](https://rubyonrails.org/2026/10/1/rails-world-2026-recap) · [Lex Fridman #474 transcript（2025-07-12，抵制态原话）](https://lexfridman.com/dhh-david-heinemeier-hansson-transcript/) · [Promoting AI agents（2026-01-07）](https://world.hey.com/dhh/promoting-ai-agents-3ee04945) · [Basecamp becomes agent accessible（2026-03-25）](https://world.hey.com/dhh/basecamp-becomes-agent-accessible-3ae6b949) · [PE Ep.58: DHH's new way of writing code（2026-04-08）](https://newsletter.pragmaticengineer.com/p/dhhs-new-way-of-writing-code) · [The malleable computer（2026-04-15）](https://world.hey.com/dhh/the-malleable-computer-7c187a9b) · [Let the agents democratize open source（2026-06-01）](https://world.hey.com/dhh/let-the-agents-democratize-open-source-9fd630a9) · [Local LLMs（2025-11-25）](https://world.hey.com/dhh/local-llms-are-how-nerds-now-justify-a-big-computer-they-don-t-need-af2fcb7b) · [Anthropic: Claude Opus 4.5（2025-11-24）](https://www.anthropic.com/news/claude-opus-4-5)
