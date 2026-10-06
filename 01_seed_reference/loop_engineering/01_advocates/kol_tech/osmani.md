---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-07
---

# osmani — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**方向**：稳定推动·持续演进（skill decay 后不回摆）
**起点**：2026-06-07 命名帖《Loop Engineering》
**终点**：持续演进：'Line-by-line reading is going away…Review…isn't'
**弧线**：06-07 命名帖 → 08-14 操作篇《Practical Loop Engineering》→ 08-31 skill decay → 09-28《The Code Nobody Reads》（answerability 上位＋Anthropic 内部数据：substantive review 16%→54%、8x 合并量）→ 公开反驳 Ball'code review will die'
**关键转折**：08-31 skill decay（承认技能退化）→ 09-28 answerability 替代 readability（不回摆，继续演进）

## 《The Code Nobody Reads》（2026-09-28，全文实取）

- URL：https://addyo.substack.com/p/the-code-nobody-reads （curl 浏览器 UA 实取全文）｜通道说明：个人博客本体 addyosmani.com/blog 09-14（brownfield）之后至 2026-10-06 **无新博文**（feed 10 条全列＋博客索引页双核），本篇仅在个人 newsletter《addyo.substack.com》首发，feed 日期 Mon, 28 Sep 2026。
- 作者身份：loop engineering 命名者（2026-06-07）；**2026-09-08 公布加入 Anthropic 任 MTS、Claude Code 团队**（HN 记录："Addy Osmani joins Anthropic"，2026-09-08，源为他的 X 帖——X 本体登录墙不可达，经 hn.algolia API 存档）。文中自报利益相关："I should say up front that I'm not neutral. I help build a tool that writes code."
- **与 loop engineering 的挂钩**：**验证回路**（review 的替代机制＝"multi-agent first pass finds bugs, verifies them, ranks them by severity"＋人批合并的循环）＋**停止条件/裁决权**（"someone deciding what ships and being answerable for it"——他 outer loop / verdict / answerability 词系的 09 月落点）＋**循环产品化机制**（Anthropic 内部把该循环做进 PR 流水线的一手数据）。
- 逐字摘录（全部实取自全文）：

> "Two years ago I wrote an essay about AI-assisted coding, and one of my tips was to review every line of generated code. I'd give that advice very differently today. What I'd say now is this: you don't need to read all the code. Every change still needs some review and every change still needs a person who owns the decision to ship it."
（**自我修正的公开记录**：两年前"逐行读"的建议被自己改写——skill decay（08-31）之后的持续修正，方向不是回摆而是条件化。）

> "Line-by-line reading is going away for a lot of code. Review, meaning someone deciding what ships and being answerable for it, isn't."
（reading 与 review 的拆分——answerability 接替 reading 成为中心词，与 07-15 "Engineers own the outer loop" 同一条词系的 09 月形态。）

> "I think every industry will stop reading most of its code line by line once it has some other good reason to trust that code. … So the trust has to come from the checking we build around it."
（**信任来源的重新定义**：从"人读过"移到"我们围绕它建的 checking"——验证回路的结构性上位。）

> "How fast a team or an industry gets there depends on two costs: the cost of checking work nobody read, and the cost of undoing a failure the checks miss."
（两个成本变量——给"停止读代码"划了经济学边界，不是无条件推动。）

> "At Anthropic, an automated Claude reviewer runs on nearly every PR, and engineers mark less than 1% of its findings as incorrect. Since it started, the share of PRs getting substantive review comments has gone from 16% to 54%."
（**Anthropic 内部一手数据**：自动 review 上线后实质性 review 评论占比 16%→54%——机器 review 没有杀死人的 review，反而提高了人的参与率。）

> "In the second quarter of 2026, the typical Anthropic engineer was merging about eight times as much code per day as in 2024, with the engineer, as Anthropic puts it, 'directing and reviewing, rather than typing.' Nobody reads eight times as much code carefully."
（8x 合并量＋"directing and reviewing"——为什么 reading 必须换形态的量化理由。）

> "Every PR gets a multi-agent first pass that finds bugs, verifies them, ranks them by severity and suggests fixes. … Core and sensitive paths still need an owner and a careful human review … Either way, a person approves the merge. Agents do the first pass and humans cover blast radius."
（**可行的验证回路形状**：多 agent 首过＋人按爆炸半径分配注意力＋人批合并——他的 light factory 的具体化。）

> "Nobody in that loop presses enter for thirteen hours, because pressing enter was never the human's job. The job is deciding what deserves attention."
（对"按回车的人"现象（8M 浏览的 Reddit 帖）的正面回应——人的位置＝注意力分配，不是执行。）

> "Last week Thorsten Ball posted a list of sixteen things he believes about the future of software development. The first one is 'code review will die.' I agree with much of the list, at least on direction, though I'd put that first one differently."
（**与 Ball 的公开分歧点**：方向同意、速度与形态不同意——判读层可引为"推动派内部的边界分歧"。）

> "Anthropic's researchers describe a 'paradox of supervision': supervising Claude well takes the very coding skills that fade if you never use them. Some engineers there deliberately solve problems without Claude now and then, even when they know it could handle it."
（skill decay 议题的 09 月延续：监督技能与手动技能是同一批技能——内部实践者已经在用"刻意不用"对冲。）

> "Budget for understanding like any other capacity. … The answer isn't to read nothing. It's to decide, area by area, how much human attention a change needs, and plan the work around that."
（治理提案：把"理解"当容量做预算、按区域分配人类注意力——outer loop 的资源化表述。）

- **该条支持的最小主张**：命名者在 skill decay 修正后继续演进而非回摆：line-by-line reading 的终结被条件化为"两成本"函数；验证回路（多 agent 首过＋人批合并＋按爆炸半径分配注意力）成为 reading 的制度替代；同时以 Anthropic 内部数据（16%→54%、8x）给"机器 review 增而非减人的参与"提供第一手证词。
- **派别适配**：**推动票（边界翼）**——方向上推（reading 将大面积退场），但每一步都带条件（两成本、answerability、按区域预算）；与 Ball"code review will die"的分歧正好标出推动派内部的速度边界。
- **窗口扫描说明**：09-15→10-06 其余通道——博客无新文（feed＋索引双核）；HN 无新故事；X 登录墙不可达（如实记录）；未发现播客/演讲新档。
