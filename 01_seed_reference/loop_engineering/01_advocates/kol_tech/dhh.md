---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-07
---

# dhh — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：37signals/Rails 创造者
> **号召力**：④ 全球影响力＋① 框架创造者
> **人物全景**：[_raw_people/15_dhh.md]()
> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景：[_raw_people/15_dhh.md](../../../voices/_raw_people/15_dhh.md)（2026-10-03 建卡，覆盖 pencils down 反转全程）。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**方向**：词表不屑＋机制全采纳（词与实践分离的极端样本）
**起点**：2023-2025 头号抵制者（'competence draining out of my fingers'）
**终点**：2026-09'pencils down'＋对机制全面采纳但对词表嘲讽
**弧线**：2025-11-24 Opus 4.5 拐点 → 2026-04 agent-first 日常化 → 2026-09-23 Rails World'pencils down'→ Lex #501 嘲讽换词（loops→graphs→harnesses 'constantly churning'）→ Oma bot 定时无人值守＋'/goal 类工具不再需要，默认不停'→ Omarchy'the whole loop is closed'
**关键转折**：词与机制的分离：feed 零 loop 字样＋嘲讽换词，但产品全线采纳循环机制

## Lex #501：嘲讽 loops→graphs→harnesses 术语轮换（2026-08-26，对 loop engineering 词族的边界表态）

- URL：https://lexfridman.com/dhh-2-transcript/ （官方 transcript 页实取全文；人物卡已收该访谈的 Opus→Codex SOP 段，**本段为卡未收的术语更迭段**）
- **与 loop engineering 的挂钩**：循环结构——他从不使用 loop engineering 专名（博客 feed/HN 全文检索零命中），但在此直接点评 loops→graphs→harnesses 词表更迭，是对本词家族最接近专名的直接评论。
- 逐字摘录：

> "It's loops now. Oh, no, no, we're done with loops. It's graphs now. Oh, no, no, we're done with that. It's harnesses this, right? They're constantly churning through the frontier, which in one way is actually very exciting."
（把词表轮换当营销噪音但认可底层实践——与他拒绝 "agentic engineering"（"I fucking hate that term… marketing slop speak"，卡内已收）同一条态度线：词无关紧要、实践才要紧。）

> "if I had just been backpacking for the last year, hadn't touched a computer, hadn't witnessed this agentic moment, and I just showed up yesterday, do you know what? I would've been caught up in two weeks."
（对词汇门槛的不屑：词表两周就能补课，说明词不承载知识。）

- 立场：**边界化（对专名）**。

## Lex #501："human in the loop is the limit" → Oma bot 定时无人值守回路（2026-08-26）

- URL：https://lexfridman.com/dhh-2-transcript/ （02:43:27 段；人物卡未收）
- **挂钩**：无人值守运行＋外层调度——人成为环上瓶颈后，改走定时调度跑 PR/issue、邮件汇总、人只做最终裁决。
- 逐字摘录：

> "I will say just very recently, I found that the human in the loop is the limit here. So I've started setting up more automated systems."

> "I've been building an Oma bot that can do more autonomous development on Omarchy that is just on a regular schedule process, all depending to do or PRs and issues, and then send me an email using the HEY CLI"

> "Here's 12 PRs that are either ready to go or I think you should close. And then I just make the final determination there."
（判断权让渡被机制化成定时无人值守＋邮件裁决。）

> "So oftentimes I'll run Claude up top, and then I'll run Codex down below, and then maybe I also have an OpenCode set up."
（多 agent 分栏并行＝他自己的外层调度。）

- 立场：**支持（无人值守机制化）**。

## Lex #501：Amabot 自迭代循环与 agent 群 auto research loops（2026-08-26）

- URL：https://lexfridman.com/dhh-2-transcript/ （02:58:20 段 Amabot、02:01:22 段 auto research loops；人物卡均未收）
- **挂钩**：循环结构＋无人值守运行——自跑、自察失败、自优化的循环成为自修正基础设施。
- 逐字摘录：

> "I'm seeing that recurrent loop where I started it on, like, "This is what I want. I want you to be able to have these isolated VM workers and so forth," and then it can do the self iteration."

> "And even in that loop, I keep seeing it catch itself, spotting vulnerabilities"
（环内自捕注入漏洞——验证回路长在循环内部。）

> "And then I got a swarm of agents to run all these auto research loops of trying all these different theories"

> "And a lot of that system, Amabot in particular, AI has driven the majority of the design decisions."
（连循环设计本身也交给 AI——比人物卡的 SOP 又深一层。）

- 立场：**支持（自修正循环基础设施）**。

## Lex #501：/goal 类工具不再需要，循环默认不停（2026-08-26）

- URL：https://lexfridman.com/dhh-2-transcript/ （02:34:48 段；人物卡未收）
- **挂钩**：**停止条件**——实践者一手观察：春季之后 agent 默认就能在循环里持续跑，"告诉它不要停"即可。
- 逐字摘录：

> "I think something happened—I don't know, I think it was in the spring—where we didn't need these slash goal things anymore. The agents could just automatically keep going in a loop if you told it not to stop-"
（对 Claude Code `/goal` 工具史有分量的实践者对照证据：停止条件的工具化正在被"默认不停"的模型能力吃掉。）

- 立场：**中性（工具史观察）**。

## Thought Economics 访谈：Omarchy 产品化验证闭环 "the whole loop is closed"（2026-09-28）

- URL：https://thoughteconomics.com/david-heinemeier-hansson/ （访谈页实取；人物卡已收该访谈经济判词/Agent Luther 段，**本段为卡未收的 Omarchy 闭环段**）
- **挂钩**：**循环产品化机制**——crash→AI 诊断→修复→向上游项目开 PR 的验证回路做进操作系统的默认用户体验。
- 逐字摘录：

> "When a program crashes, the first thing we do is pop up a little notification that says, "Would you like AI to take a look?""

> "your agent can diagnose why, perhaps even create the fix, then open a pull request to the original project"

> "and the whole loop is closed."

> "You pick your Claude, your Codex, your Grok, whatever."
（验证回路的终端产品化：闭环不是开发流程而是用户开机即得的默认能力。）

- 立场：**支持（循环终端产品化）**。

## X 帖：嘲讽"每行代码必须人工评审才能合并"的强制人审闸门（2026-10-06）

- URL：https://x.com/dhh/status/2107427852845199687 （**X 登录墙壳页内嵌 JSON 提取**——x.com 个人页 SSR 壳含近 6 条推文的内嵌数据（2026-09-24→10-06），推文 id 与 created_at 2026-10-06T11:08:48Z 已核；历史推文不可达，如实记录）
- **挂钩**：**验证回路**——公开嘲讽把人工评审制度化为合并前的强制门，反对以"就业保护"为由冻结验证让渡。
- 逐字摘录：

> "Every line of code must be manually reviewed before you're allowed to merge! Ensure that any agent use does not lead to too much unauthorized acceleration."

> "Maybe we can ensure full employment with programmers forever like this too?"
（反讽推文（非字面主张）；与他"评审让渡给 Codex xHigh"的立场同向。）

- 立场：**反对（制度化人审门）**——验证回路治理上的鲜明反对票。

**本轮最小主张**：DHH 对 loop engineering 专名的态度＝不屑使用、当营销噪音嘲讽（与他拒绝 agentic engineering 同构）；对循环机制本身＝全采纳并持续推进（定时无人值守、自修正循环、默认不停、验证闭环产品化、反强制人审）。**"对词表不屑、对机制全采纳"是他对本运动的完整答案。**
**通道说明**：world.hey.com feed.atom 全文无 "loop" 字样——博客通道窗口内无本词发声；窗口内新帖《a pond of interesting problems》（06-03）《What on earth are you dooming about》（10-05）《over my dead pencil》（10-06）均不挂七类钩，按相关性底线弃收；HN 通道 dhh 专名零命中（负结论）；X 6-9 月推文不可达（登录墙，仅壳页内嵌 6 条近期推文可取）。
