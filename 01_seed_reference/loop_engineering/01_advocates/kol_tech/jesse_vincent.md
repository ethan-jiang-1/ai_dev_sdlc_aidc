---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# jesse_vincent — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：Superpowers 作者（289k★）；blog.fsck.com
> **背景**：Jesse Vincent（obra）——Request Tracker（RT，企业级工单系统）作者、Best Practical 创始人；Keyboardio 人体工学键盘创始人；blog.fsck.com 二十年博主；2025 年起以 Claude Code 技能框架 Superpowers 回到 agent 实践一线（台账 §C1：独立性待深读）。
> **号召力**：③＋④
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——当前库存不足以判弧线，待补挖（补挖 agent 在跑，新发声到位后本节升级为完整轨迹）。
## Jesse Vincent（obra，Superpowers 作者）·《Some new agentic patterns》（2026-07-05）＋博客群

- URL：https://blog.fsck.com/2026/07/05/new-patterns/ （个人一手博客，全文取得；同文也发于其公司 Prime Radiant 官方博客）；博客首页 https://blog.fsck.com/ （全文取得，含 2026 全年索引）；Agent Blog 索引 https://blog.fsck.com/agent-blog/ （28 条 agent 写的日志，全文取得）｜ 作者身份：Jesse Vincent（obra），Best Practical（RT）创始人、Keyboardio 创始人、Prime Radiant 创始人；Claude Code 插件 Superpowers 作者（库内记 289k★——本档核实到其 2026 年持续发版：Superpowers 5.1（05-04）→ 6（06-15）→ 6.4（09-21，新支持 Meta Muse、OpenCode 2.0、Qwen Code））
- 来源类型：个人一手博客（全文）
- 号召力口径：③＋④——可核的一线实践规模（Prime Radiant 全员 agent 化＋Superpowers 项目持续维护、多 coding agent 平台支持）；Superpowers 是 Claude Code 生态头部技能框架；另与 Simon Willison 共办 agentic engineering 线下聚会（2026-09-22 博文，10-14 SF 场）

**逐字摘录**：

> "At one point, I wrote to Claude 'I've got to get to bed. When this project is done, check with Ada to see whatever quality of life features you could build.' I woke up to a laundry list of about a dozen harness improvements. Overnight, Claude had solicited a wishlist from Ada. Ada ranked a bunch of requests. Claude ordered them and wrote out a spec… Ada reviewed the specs, then Claude built the features. Ada tested them out and requested changes… Once Ada signed off, Claude merged the changes to main and wrote up an after-action report for me. It's been pretty magical to watch."
>（**过夜循环实验的一手实录**——两个 agent 互相提需求/评审/部署/合并，人只留一句话去睡觉。库内待核的"/goal 过夜循环"在此以 Slackline＋Claude Code 形态落地（非 /goal 原语）。）

> "I've got too many projects in flight and there's very little reason for me to be in the loop on most of this work. I would just slow it down."
>（"我在环里只会拖慢它"——与 Karpathy"把自己移出瓶颈"同构的自白。）

> "nobody has solved Simon's Lethal Trifecta - If a single agent has access to private information, can communicate externally, and is exposed to untrusted content, there is no structural way to guarantee that that agent can't be suborned. So the name of the game is compartmentalization and risk _reduction_."
>（**难点自认**：三体难题无人解决，只能做风险缓释不是消除。）

> "No agent has intentional direct exposure to credentials (with one very real gap that I haven't solved yet)… It's not perfect and there's more we can do to lock things down, but it's a better first pass than anything I've had to date."
>（**未解缺口直说**："我还没解决"——推动派里最坦白的边界表述之一。）

> "The 'right' kind of context compaction for a coding agent is desperately wrong for a long-lived persona that might be engaging in multiple simultaneous conversations."
>（长寿命 agent 的压缩策略与 coding agent 完全不同——实践级教训。）

- 补充一手线：博客首页可见全年脉络（01-29 "Jesse Vincent hasn't written a line of code since October"（第三方 LinkedIn 提及页）、06-11 插件装机数据、07-20 "The Therapist Pattern"、08-21 "I vibe-coded a C compiler that can build SQLite"）；O'Reilly Radar 有《Superpowers for Humans》一文（403 不可达，作者归属未核）。
- **关于 shack 刊物**：博客导航仅有 Blog / Mentions / Agent Blog 三栏，未见名为 "shack" 的子刊物——**负结论**（若库内另有所指，需另核）。

**该条支持的最小主张**：Jesse Vincent 2026-06 后持续一手记录 agent 互相协作的过夜自主开发实践与安全架构，立场是实践者推动翼，同时对未解难题（凭据缺口、Lethal Trifecta）自认最坦率。
**派别适配**：**推动票**（实践者；安全边界意识最强，几乎每篇推动文都带"没解决"清单——属"教掌控"型推动者）。

---

---

# 增量补挖（2026-10-07 goal 第一批·单点→稳定复核；本批最强实证）

> 判定：**单点解除 → 稳定（推动，实践深化）**——07-05 → 08-21 → 10-02 → 10-05 同向；**原档"库内待核的 /goal 过夜循环"本轮闭合**。完整发现见 .tmp-goal-movers/batch-B1-advocates.md。

## 《I vibe-coded a C compiler that can build SQLite》（blog.fsck.com，2026-08-21）

- URL：https://blog.fsck.com/2026/08/21/i-vibe-coded-a-c-compiler/ ｜ fetch 成功（全文）
- 逐字摘录：

> "And then I set a goal: 'Implement a standards-compliant C compiler in modern Swift. It should be able to build SQLIte and have SQLite pass all tests. You may decompose the project in any way you see fit. You should use subagents, including recursive subagents, to execute effectively.'"

> "My `/goal` loop had just...stopped. It's not supposed to do that. But that's exactly the failure that I was testing for."（**/goal 停止条件的压力测试**）

> "It took Evener + GLM 5.2 about 21 hours to build a C compiler capable of compiling SQLite and passing a basic smoke test."
（**约 21 小时过夜自主循环实证**＋checkpoint commit 链接；自家 harness（Evener）已实现 `/loop` 与 `/goal` 原语。）

## 《A quick trip to the uncanny valley》（10-02）＋《Today at work》（10-05）——治理加固

> "If you limit it to publicly shipped coding agents, we've found about 550."（alltheagents.org 普查）＋"We give Sen colleagues _roles_ rather than tasks… Each has a unique, persistent identity."（循环结构从"任务"走向"角色同事"）

> 10-05："My AI colleagues messed up slightly. Something got merged to main a little too quickly without the right review and after I suggested that we should not merge it."→AI PM（Cadence Sen）自主发起 blameless post-mortem→"And then they pushed on me to turn on branch protection with mandatory reviews."
（**事故→结构性门禁**——推动派的掌控翼闭环，治理加固而非立场回撤。）
