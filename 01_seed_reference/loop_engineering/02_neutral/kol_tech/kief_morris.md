---
type: kol_evidence
directory: 02_neutral/kol_tech
observation_date: 2026-10-06
---

# kief_morris — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——当前库存不足以判弧线，待补挖（补挖 agent 在跑，新发声到位后本节升级为完整轨迹）。
## Kief Morris《Humans on the loop, not in it: Taking agentic engineering end to end》PlatformCon Live Day London（2026-06-23 16:00 BST，30 min，Main stage）

- URL（官方 session 页）：https://2026.platformcon.com/sessions/humans-on-the-loop-not-in-it-taking-agentic-engineering-end-to-end-ldn ｜ 二手现场记录：https://lucaberton.com/blog/kief-morris-human-on-the-loop-platformcon-london-2026/（Luca Berton，2026-07-04）
- 来源类型：演讲——**官方摘要＋关键点全文取得（curl 实取 session 页）**；演讲视频本体未取得（Podwise 摘要页 fetch 失败）；Luca Berton 记录为二手转述。
- 号召力口径：①＋②——"on the loop" 分层框架定义者（martinfowler.com 2026-03-04 文，库内已有，其人物卡在 `01_seed_reference/voices/_raw_people/10_kief_morris.md`）；O'Reilly《Infrastructure as Code》作者、Thoughtworks Distinguished Engineer；PlatformCon 主舞台。
- **库内已有**：2026-03-04《Humans and Agents in Software Engineering Loops》（evidence-c）。**本条为增量**：命名周后 17 天他把它推向端到端交付＋平台工程受众。
- ⚠️ **归属澄清**：Luca Berton 博客称"Kief's article on MartinFowler.com, 'Human on the Loop'"——经核对，该文即 2026-03-04 的 humans-and-agents.html（标题被 Luca 转述改动），**不存在一篇单独的新文章**（martinfowler.com/articles/human-on-the-loop.html 为 404，系列索引无此条）。

**官方 session 页逐字摘录（一手）**：

> "Using AI to generate code isn't enough. Platform engineers can enable teams to put agents to work across the full delivery loop: specify, build, test, release, run, and improve. Humans steer outcomes while agents do the heavy lifting."
（官方摘要——他把循环从"写代码环"扩到全交付环，人的位置=steering。）

> "Teams should focus on defining outcomes and prioritizing improvements, not managing every artifact; humans should stay on the loop, not in it."
（官方 key points 逐字——against 逐件审批。）

> "As feedback loops tighten across the full cycle, teams progressively trust agents with more."
（官方 key points 逐字——**渐进信任**：不是一次性放权，是随反馈环收紧逐级授权。这是中性派"什么时候可以放权"的最清晰官方表述之一。）

> "Platform engineers need to enable the capabilities that make end-to-end agentic workflows reliable, especially for release and operations."
（官方 key points 逐字——可靠性能力建设是平台工程师的职责。）

**该条支持的最小主张**：Kief 在词源周后的公开立场是"人的位置=on the loop 的系统管理层；放权程度随全环反馈质量渐进提升"；官方文本无 hype 语汇。
**派别适配**：中性票（其 agentic flywheel 愿景部分偏推动，但以 sensors/渐进信任为前置条件——归中性，注明张力）。

---

---

# 增量补挖（2026-10-07 第二轮：07-01→10-06 增量——7 月密集输出后沉寂）

> 通道：infrastructure-as-code.com 个人博客文章页实取、个人站 Speaking 页、Bluesky authorfeed API 实取、LinkedIn 活动页（登录墙）。8 月中旬后沉寂：bsky 最新帖 08-05、博客无新文——通道清单如实记录。

## 《The Argument Underneath the Arguments: What I heard at the Future of Software Development Retreat》（2026-07-09）

- URL：https://infrastructure-as-code.com/posts/fose-july-2026.html （个人博客文章页实取全文；页面明示 09 July 2026）
- **与 loop engineering 的挂钩**：**验证回路＋自主度分档（外层调度）**——逐行审查被判定失效后，严谨性移至上游意图（验收标准）与下游检查（一致性测试、harness sensors），自主度带宽由检查成本与出错代价决定。
- 逐字摘录：

> "Here's an answer that came up in one form or another across most of the sessions: the rigour doesn't go away when an agent writes the code. It moves."
（FOSE 闭门会共识：严谨性不消失、它迁移——on-the-loop 框架的核心句。）


> "The preparation was the control. More control made it safer to increase autonomy."

> "A cheap, reliable check on the outcome buys you a wider remit. An expensive check, or a high cost of being wrong, forces a narrower one."
（**自主度带宽公式**：检查越便宜可靠、授权越宽——检查成本决定自主度分档。）


> "It's to let the level at which you need to understand the system rise as you hand off more of the detail: to understand it at the level of intent and boundaries and behaviour, while an agent works below that line"

> "don't point an agent at your production system and give it open-ended authority to watch for trouble and fix whatever it finds."
（对生产环境无人值守的窄授权警告——与 06-23 PlatformCon"humans steer outcomes"同线。）


- 立场：**支持（自主度分层治理理论化）**。

## 《Setting Agents Loose, Staying in the Loop》（LinkedIn Live 网络研讨会，2026-07-22）

- URL：https://www.linkedin.com/events/7482324853468090368/ （**登录墙：回放与正文不可得**——仅个人站 Speaking 页登记标题/日期，立场判定以标题为准，如实标注）
- **挂钩**：**外层调度（on-the-loop 分层）**——标题即"放权给 agent、人留在环上"，延续 03-04 文章与 06-23 PlatformCon 的叙事主线。
- 逐字摘录（Speaking 页登记原文）：

> "22 July, 2026, "Setting Agents Loose, Staying in the Loop" on LinkedIn Live (online webinar)"

- 立场：**支持（口径延续；正文未取得，弱证据）**。

## Bluesky 帖：对"自动黑客工具越界"事故的去戏剧化定性（2026-08-01）

- URL：https://bsky.app/profile/kief.com/post/3mrz4af7ejc2h （Bluesky authorfeed API 实取；createdAt 2026-08-01）
- **挂钩**：**无人值守运行**——把自动工具在无人盯守下越界破坏定性为环境隔离不足的工程问题，而非"AI 失控"神话。
- 逐字摘录：

> "We ran an automated hacking tool in an environment that wasn't as secure as we thought, and it hacked things we didn't mean for it to."

> "Not quite as exciting as, "Our super-powerful AI broke loose from its containment and went rogue, rampaging across the Internet.""
（问题在环境与范围控制、不在 AI 自主意志——与其"窄授权"主张一致。）


- 立场：**中性（去戏剧化定性）**。

**本轮最小主张**：Morris 07 月密集输出后转入沉寂（08-05 后无新发声）。07-09 FOSE 长文是其 on-the-loop 框架的升级：控制点从"逐行审查"迁往"预备（验收标准）＋检查（一致性测试/harness sensors）"，自主度带宽＝检查成本与出错代价的函数；07-22 LinkedIn Live 延续主线（正文被墙）；08-01 对 agent 安全事故做工程化定性。**姿态从实践叙事转向自主度分层治理理论化。**
**通道失败如实记录**：LinkedIn Live 登录墙（302 跳登录，回放不可得）；GOTO Book Club 剧集经核日期为 2025-06（窗口外，不入）；Buttondown newsletter 存档页空壳无法核；kief.com feed 空无条目。
