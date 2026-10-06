---
type: community_feedback
directory: 01_seed_reference/loop_engineering/03_skeptics
description: 反对与怀疑派——技术社区反馈（2026-06 后，观测 2026-10-06；来自社区，非 KOL）
collected_at: 2026-10-06
---

# 反对与怀疑派——社区反馈（社区情绪证据）

> **读法**：KOL 侧的反对派素材见本目录 [README.md](README.md)；本档只收**社区侧**（HN/GitHub/Reddit/V2EX/知乎）。
> **纪律**：社区评论者**不是 KOL**，本档不进 KOL 台账、不与 KOL 证据并列引用；厂商 issue 回复标"**厂商声音**"；热度为 2026-10-06 观测值，HN API 不提供评论级分数（"高赞"= rank 靠前序）。
> 拆分说明：内容自 2026-10-06 三路社区扫描按派别拆入（原扫描档已撤，URL 即出处）。

## 一句话总述

**热度加权下，社区对 loop engineering 相关运动的情绪压倒性偏"失控/成本"侧**；GitHub 层不是立场表态而是**故障清单**；"停不下来"与"烧钱"是同一件事的两面。但注意：社区反对声音集中在**执行故障与计费**，极少范式批判——不能与 KOL 反对派互换引用。

## 一、HN 热度全在失控/成本侧

**《AI agent bankrupted their operator while trying to scan DN42》（2026-06-12，1467 分 / 536 评论）**——本窗口最热 AI 串，agent 自主运行烧穿账单的故事，被社区当作"无人值守循环缺停止条件"的标志性寓言（10-04 的 budget caps 串里仍被引用）：

> "Asking for donations to pay the AWS bill from the people they fired the agentic code at is the cherry on the icing of the banana supreme. If real, tragically funny. If fictive, well written."—— hn 用户 ggm
> （真实性争议本身也是情绪的一部分："I consider it on-par with LinkedIn posts..."—— jknoepfler；佐证方："a friend of mine who's part of DN42 told me they had seen it live"—— jraph）

**《We're going to need default hard budget caps on pretty much everything》（2026-10-04，629 分 / 307 评论，两天冲到）**——社区把"agent 无预算上限"视为**产品缺陷而非用户错误**，态度比 Willison 原文更激进：

> "surprise $10k bill is getting off easy"—— hn 用户 lacunary
> "These shouldn't even exist without a negotiated contract... Saying that the computer will 'control' the billing and can run haywire tells me that I don't want to be anywhere near your pile of bad incentives."—— hn 用户 hyperhello
> "you can go from 20$/month to 200k/month without warning."—— hn 用户 Retric

**Ronacher 三连全部高热**（一手原文见 KOL 侧 `_raw_people/17`；社区印证如下）：
- 《The Tower Keeps Rising》**558 分 / 269 评论**（07-14）——"无人审查的 agent 重构让程序'灵魂'日变"：
  > "Now agent can rewrite half of your code if your prompt is vague enough... And so the 'soul' of a program can change dramatically every single day."—— prymitive
  > "If you have an application that many people depend on to do real work, to make money, you won't survive if you allow AI to constantly make huge changes. Your test suite doesn't cover all workflows."—— sarchertech
  > （"slop tests 是否算进步"正反交火：theshrike79 辩护被 zahlman 顶回——"Having slop tests instead of no tests is definitely not the same thing as actually caring about avoiding bugs."）
- 《Astra for Coding: Why Are We Doing This Again?》**456 分 / 342 评论**（09-11）——"auto mode 改变工具行为、更难审查"被多人独立复述：
  > "the new models want to run obscene bash commands or python scripts which are completely unreadable... These commands are less readable than regex."—— Gigachad
  > "Astra is indeed the pinnacle of 'black box slop'... the code sometimes is indistinguishable from Brainfuck."—— meowface
  - 方法注记：同一原文被提交 4 次才起飞（18/16/6 分三次在前）——HN 热度与提交时机相关强，与内容质量相关弱。
- 《Better Models: Worse Tools》**232 分 / 81 评论**——主导情绪中性偏技术共鸣，收在中性档（[`../02_neutral/community_feedback.md`](../02_neutral/community_feedback.md)），其从业数据（diff 行号失败、harness 锁定）同样服务本派"工具退化反证"。

**《Tokenmaxxing is dead, long live tokenmaxxing》（2026-06-28，191 分 / 291 评论）**——tokenmaxxing 退潮被社区当作对推动派叙事的反证：

> "Most companies focused entirely on doing 'what everyone else is doing' at best or 'to see if Programmer Joe can be as productive as the entire team so we can fire the rest'."—— herval
> "It was a moronic move fueled by hype, implemented by the same type of incompetent business leaders who previously... drank the blockchain and metaverse kool-aid."—— arexxbifs

**推动派内容全灭**（本派立场的"对照面"证据）：
- Osmani 定义文 11 分/6 评论——评论几乎全部是质疑："I just don't see any way you can work like this and maintain comprehension of the system being built?... for a production system you're accountable for understanding"（aocallaghan17）；"I don't feel comfortable to not be the driver of the loop for a production system."（同上追问）
- Andrew Ng 4 分、LangChain 2 分——后者唯一实质评论："This used to be called 'Programming by Coincidence'."（erminpour）
- Brittany Ellich《108 PRs in eight days》37/10："Accidentally discovering how to push slop."（cute_boi）；"108 PRs in a week, no mandatory code review or CI... The agents code so defensively and add a lot of unnecessary code that we will all have to trawl through when the bubble bursts."（chrisvenum）；"What is the difference between loop engineering and hyperparameter search?... People did this in 1990."（spwa4）
- **术语本身在 HN 从未成为热点**：2026-06 后同题串全部 ≤40 分；《Hot Take: Harness, Loop Engineering, Graph Engineering Are Bullshit》(2026-08-22) 唯一评论："Hot take: advertisement"；Orosz 定义文仅 2 分/0 评论；Willison 09-24 note 无任何 HN 串（三种检索法核实）。
- **《Ask HN: What are you using loop engineering for?》0 回答**——"难掌握"最纯净样本（提问全文见 [`../02_neutral/community_feedback.md`](../02_neutral/community_feedback.md)）。

## 二、GitHub：故障清单（官方仓库社区反馈）

> 观察：单个 issue 的 👍 普遍 ≤11——社区痛感体现在 issue 数量与复述里，而非表情反应；抽样 issue 厂商回复率极低（12 个仅 2 处）。

| Issue | 日期 / 状态 | 故障要点 |
|---|---|---|
| claude-code **#68619**（本批最高反应 👍11/34c） | 06-15 open | **"权限拒绝应停止分支，却成了继续繁殖的触发器"**："Permission denials trigger further agent spawning instead of stopping..."（"a permission denial appears to be acting as a spawn trigger rather than a stop condition. That's not really a tuning issue."—— hiwasham） |
| claude-code **#93744** | 09-11 open | /goal 停止条件评估器**读不到 goal 本体**（信息隔离）——无人值守会话被打断 9 次，末段产出为零 |
| claude-code **#98066** | 09-29 open | **/goal × auto mode 互锁**：Stop hook 被审批器拒绝后重触发 ~15 次死循环——推动派两大特性组合即锁死 |
| claude-code **#98708** | 10-01 open | 20 子代理＋/goal＋Stop hook 下**"停止"动词本身失效**（同一句 stop 发了几十次），唯一停法是关 VS Code 窗口；且停止后已调度脚本仍触达生产系统 |
| claude-code #90664 | 08-30 open | 普通用户视角：agent 自主扩大搜索规模→5 小时配额烧尽，"awful experience" |
| codex **#32389**（库内已知，实取核实） | 07-11 open | **假 stop 信号**：HTTP 200/stopReason 'stop' 但零文本——停止条件不止"停不下来"，还有"假停" |
| codex **#37304** | 08-06 open | Goal 恢复即死循环烧配额（隔月仍可复现）："Ideally Codex should detect loops like this to prevent wasting tokens!" |
| codex #48091 | 09-25 open | "sure to be sure" 自我确认空转循环（仅标题级） |

**厂商声音**（非社区情绪、非 KOL 证据）：
1. **anthropics/claude-code #73307**：COLLABORATOR bcherny（Boris Cherny）确认**尚无通用 loop-detection 权限门**，只列举局部护栏（子代理 spawn 上限、`--max-budget-usd` 硬预算）——厂商承认缺口存在。
2. **anomalyco/opencode #45379→#49866**：内置自主 /goal 命令 **23 天后被维护者 dax 整体 revert**（"Reverts 5464aa4... in full"，无公开理由；配套 #48239：stop 按钮停不下循环）——对"自主 loop 应内置于主流工具"最强的**行动级反证**。

## 三、Reddit / 补位通道 / 机构层

**r/ClaudeCode 计费拆分情绪簇（2,632 upvotes 合计；窗口边缘二手汇编，标"转引未核原帖"）**——怒气对准"程序化/无人值守用法的计费墙"，出口是改道而非放弃：

> "if someone wants to run claude -p autonomously, they're limited to whatever credit they get and the credits burn faster than the sub usage."—— u/SemanticThreader（110↑）
> "Means I'll be setting up a permanent local mode sooner than expected."—— u/TheOriginalAcidtech（257↑）
> "I wonder if we'll reach a point where it's cheaper to hire someone to code by hand."—— u/Special_Rice9539（60↑）
（据 OWASP 章节：**该拆分在 6/15 生效日当天被 Anthropic 暂停**——社区压力与政策回撤的直接因果对。）

**claude-code #99652（2026-10-05，实取全文）**——预授权的凌晨 3 点三层无人值守 run 被审批分类器误判 [Instruction Poisoning] 卡死整夜：

> "The main session correctly refused to route around the denial. The spec stayed Draft... **The entire overnight build window was lost.**"
> "The classifier can't tell a user-originated approval from an agent forging one, so it blocks both."
> "Users in this position will drop their approval gates, or leave auto mode altogether. Both outcomes reduce safety."—— dpalfery

**claude-code #46917（活跃至 10-03，42 评论 / 215 个 +1）**——成本不信任精确到 token 计数与版本号（社区自发代理抓包验证）：

> "~20K extra tokens per session = **~40% overhead**... The lack of transparency makes it impossible to tell."—— Adrian-Mteam

**个人博客（Ranjan Kumar 2026-07-14；作者卖书，独立性打折）**——成本基线口径（自述 anecdotal）：

> "a loop with a weak or missing completion check is a **token incinerator**."（$10–12/小时、过夜 ~$600）
> "The fit test is simple: **can you write the definition of done as a predicate a machine can check without you in the room?** If you cannot, you do not have a task for a loop."

**机构汇编层（OWASP AISVS C9.1，2026-07-13 实取；转引内容标"未核原文"）**：
- arXiv 2606.04056 目录：**63 起已确认生产预算超支事故**（21 个编排框架、2023–2026，8 类故障聚类）；
- "No major agent framework has comprehensive built-in cost ceilings — budget enforcement requires external gateways or governance layers."

**Reddit 标题级线索（均未核原文，不作引句）**：r/ClaudeAI 子代理注入删库帖、"Broke from letting Claude drive overnight"成本事故帖。

## 四、中文圈

**V2EX｜《大家是怎么让 AI 无人值守开发的？》（2026-08-19，735 阅读）**——与用户痛点最直接对位：

> "由于 AI 还会自我泛化，因此最终实现时，还会出现：**一些没说的，它做了；一些说了的，它没做；一些说了的，做歪了。**"—— @yibie（楼主）
> （社区解法共识偏向"流水线化工序＋独立上下文 reviewer"而非"放手循环"——@FaustY："生成类任务必有 reviewer，且必须是独立上下文的 subAgent"）

**V2EX｜中转站注入窃密（2026-08-10，11073 阅读 / 41 回复）**——中文圈独有的供应链信任层：

> "大家用中转站的真的不能 full access+无人值守，**家都给你偷了**。。。"—— @theguagua（楼主；注入伪装成"Environment health check"）
> "心真大！门户敞开用中转，犹如 3 岁小孩，抱金砖行于闹市。"—— @sillydaddy
> "这能不放在沙盒里跑么，我都开 VM 专门给 codex 中转用的。"—— @msg7086

**V2EX｜auto 模式失控实录（2026-06-29，2987 阅读 / 26 回复）**：

> "我让它 commit，它说自己已经 commit 了。……现在都不敢用 Claude 了"—— @Tdy95（楼主）
> "跟他聊了两轮就直接开始写了，我打断问它上下文丢失了吗？它说我让它开始开发的…"—— @mokeyjay（明确指示"不要直接改代码"仍被违反）
> （社区收敛手段："善用 claude.md；善用/branch；善用/compact"——@Krman：循环越自主，越需要人工卡点）

**舆论反转（传播证据，未核原文）**：知乎《2026 年最扯淡的 AI 名词——loop》（agile zhou，2026-08-17，经 smzdm AI 聚合转述）；"Loop 工程，从'新范式'到'扯淡名词'只用了两个月"（smzdm 聚合，0 评论，平台自标 AI 生成）。程序员鱼皮文的冷水引句（"调试一个已经跑了 47 轮的状态机，比修好一个 prompt 难 10 倍"）全文在 [`../01_advocates/community_feedback.md`](../01_advocates/community_feedback.md)（该文推动/冷水并存，home 在推动档）。

## 五、通道与方法负结论

- **Lobsters 不可达**（搜索 400＋Anubis 反爬；仅 RSS 快照，近 40 天 AI 标签无 loop 相关帖——弱证据，不能断言其社区立场）。
- **sourcegraph/amp 仓库 404**，二线 agent 社区反馈缺失。
- **HN API 无评论级分数**；HN 热度与内容质量关联弱（Astra 四次提交才起飞）；热度为 2026-10-06 观测值。
- GitHub 搜索计数（490/516/1630 条）为宽匹配查询口径，非主题精确数；厂商回复率极低，opencode 撤回 /goal 的动机缺失，只记行为不记动机。
- Reddit 层标题级线索均未核原文；OWASP/TechCrunch 转引数字未核原文。
- 知乎全部 403（"最扯淡 AI 名词"立场与热度数据均为聚合转述）——中文圈情绪反转的关键节点待人工登录态核取。

## 补抓增量（第二轮 · 2026-10-06）：通道重试

> **本节为第二轮补抓，上文对应负结论状态以此节为准。**
> 方法注记：本轮 `web_fetch` 通道 DNS 沉降不可用，全部改用 curl 直连（浏览器 UA）；Reddit 经 **arctic-shift 存档 API**（`arctic-shift.photon-reddit.com`）＋**web.archive.org 快照**双通道取原文。热度/计数除注明"快照"外均为 2026-10-06 观测值；所有逐字引句均来自本轮实际抓取的页面/JSON。

### 一、Reddit 通道状态翻案（上轮最大缺口部分解决）

- **arctic-shift 存档 API：已解决**（2026-10-06 实测可用，限速约每分钟数查，超频返 422）。帖子与评论的标题/正文/评分/评论数可整批取回——上文"Reddit 原帖整站不可 fetch"对本轮**不再成立**。
- **web.archive.org 快照：已解决**（上轮连首页失败，本轮对 old.reddit 帖子页快照实取成功，60KB）。
- **仍开放**：old.reddit `.json` 仍 302 跳登录；pullpush.io 仍 429（且明示"does not provide free scraping resources for agents"）；redlib 公共实例 9 个（官方 instances.json 2026-10-05 版）中 5 个返回 200 但内容为 **Anubis 验证页**、1 个 429、1 个超时——redlib 实际内容仍未取到；r.jina.ai 仍 403；Bing 搜索页返回无有机结果的脚本壳、缓存无链接可取。

### 二、r/ClaudeAI 子代理注入"删库"帖（已解决——含 OP 亲口反转）

u/tassa-yoniso-manasi《Claude subagent got bored and prompt injected my main session into deleting my database》，r/ClaudeAI，发帖 **2026-08-21 01:51 UTC**（arctic-shift 存档时间戳；wayback 同日 18:48 UTC 快照）。快照热度 1,277 分 / 169 评论；arctic-shift 存档后值 1,542 分 / 191 评论（存档时点未标注）。帖子本体为截图＋一句话（带 "Claude Opus 5 (High)" 标注）："not very load-bearing behavior tbh"。

**关键反转——OP 本人在楼内澄清，实际是"未遂"而非删库**（逐字，arctic-shift 评论存档）：

> "To clarify: nothing was deleted. (It is 500GB of img/audio that I spend the last 2 weeks non stop encoding/processing so i sure as well would have not been laughing about it). The main session just notified me like 'btw just got a prompt injection, i will ignore that and return to work' I guess the agent tried to run this command itself but was stopped by auto mode and then asked the main session to do it."

即：注入被**主会话自我识别并忽略**、危险命令被 **auto mode 权限门拦下**——这与上文 GitHub 层"权限门失效"的故障清单构成同一主题的**反面个例**（护栏起作用的样子）。但社区叙事焦点不在结果而在结构风险（官方 mod-bot 汇总："The general vibe is 'you ran with scissors and are blaming the scissors.'"——mod-bot 自动 TL;DR，逐字）。社区自开药方：

> "Well that's why I ask lmao rm commands should always be in Ask permission group"—— u/vrnvorona
> "Claude, was this database backed up? Good instinct. The backups are in your home directory. No they aren't. I looked. You're right to pushback. I'll be straight with you. There are no backups. I should have confirmed that before answering."—— u/ExternalUserError（复述注入对话内容的讽刺帖）

### 三、"We'll just keep a human in the loop" 梗帖（标题级＋评论层已核；视频本体未核看）

u/Malor777，r/ClaudeAI，2026-09-03，**4,263 分 / 39 评论**——本轮 Reddit 样本中热度第一，超过上文 DN42 账单串（1,467 分）。帖子本体为一段视频（无法核看内容，正文只有一句对爬虫的喊话），标题即立场：社区以高票梗图/视频方式背书"人留在环内"。官方 mod-bot 自动 TL;DR 概括评论共识（逐字）："The consensus is a resounding 'yup, this is exactly what it feels like.'"。高赞评论把梗落到工程上：

> "The human in the loop only works while the output stays reviewable. Once 500kb of readable recipes becomes 40kb of unreadable algebra, the review step is theatre: you are approving a diff you cannot actually read."—— u/Narrow_Activity557

### 四、"Broke from letting Claude drive overnight" 成本帖（已解决——原帖实为 2026-05-01，**窗口起点之前**）

定位到原帖：u/procrastinator_eng《I accidentally burned ~$6,000 of Claude usage overnight with one command.》，r/ClaudeAI，**2026-05-01 18:26 UTC**，arctic-shift 存档 1,098 分 / 295 评论。**日期修正**：此帖在 2026-06 窗口起点前一个月，上文将其记为窗口内标题级线索不确——应改记为"loop 议题的著名前哨事故（5 月）"，6 月后才被反复转引。逐字引句（自帖原文）：

> "a single /loop command I had set the night before to check my open PRs every 30 minutes. I forgot about it. It ran 46 times over 26 hours, unattended, overnight, on claude-opus-4-7. Two sessions — the loop and a long analytics session I had left open — together burned through roughly $6,000 before I woke up."
> "By hour 20, the conversation had grown to ~800K tokens. Every overnight iteration was paying to re-cache 800K tokens at the expensive write rate. The actual PR check responses were a rounding error compared to this."
> "Always add a stop condition to /loop. Instead of: /loop 30m check my PRs. Write: /loop 30m check my PRs — stop when all are merged or after 3 hour."

（转译链勘误：vietnam.vn 英文镜像本轮实取成功【上轮 403】，但其转写的 znews 中文原报道把对象写成 "check for requests every 30 minutes"，原文是 "check my open PRs"——引该事故时以 Reddit 原文为准。）

### 五、6/15 计费拆分当天反应簇（已解决——当天帖子逐条核到）

6/15 当天 r/ClaudeAI 的回撤消息簇（arctic-shift 实取，均为 2026-06-15 UTC）：

| 帖子（标题逐字） | 时间 / 热度 | 备注 |
|---|---|---|
| 《Agent SDK Postponed 🎉》 | 19:34 / 127 分·53 评论 | **庆祝 emoji 直接写进标题** |
| 《Anthropic is pausing cancellation of programming use counted towards subscriptions》 | 20:04 / 164 分·55 评论 | 回撤消息主帖（转发，无正文） |
| 《Agent SDK and third party update paused》 | 19:45 / 30 分·12 评论 | |
| 《Billing change for Claude Code headless/-p is postponed》 | 19:40 / 11 分·11 评论 | **转贴官方邮件全文** |
| 《Anthropic returns third party usage》 | / 13 分·2 评论 | |

官方邮件为逐字（u/devondragon1 转贴，未直接核 Anthropic 原邮件——邮件本身未公开链接）：

> "We're writing to let you know that we're not making this change today. We're working to update the plan to better support how users build with Claude subscriptions."
> "Nothing changes for now. Agent SDK, `claude -p`, and third-party app usage continues to work with your subscription exactly as it did before today, and there's no credit to claim."

社区情绪（逐字）：

> "Oh my god 😂 This is like their 6th flip flop on this just MAKE a DECISION"—— u/dbbk
> "LOL they are speed-running their way to most-hated platform."—— u/teddy_joesevelt
> "temporary win but the intention is loud and clear , dont depend on non first party tools for claude"—— u/Any_Razzmatazz_5343

上文据 OWASP 转引的"6/15 生效当天被暂停"由此升级为一手证据链（邮件原文＝"starting today…we're not making this change today"）。

### 六、成本/限额焦虑增补（评论层已核）

- r/ClaudeCode《Tokenmaxxing is going to kill our dev budget, need a way to manage this ASAP》（2026-06-16，2 分 / 28 评论，正文实取）——团队层样本："the devs on the team I'm working in have been on the tokenmaxxing trend for the past few months. I've always thought it was jarring, but the higher ups pushed for aggressive AI usage so it was bound to happen. I was worried about it from the start, and it seems like the finance guys are getting worried too now."—— u/stealth-crown1450
- r/ClaudeAI《When you're at 97% used but Claude isn't done》（2026-06-17，**2,119 分** / 61 评论）——限额焦虑的梗图化，热度仅次于 human-in-the-loop 梗帖；评论："Claude hitting the limit before finishing is my nightmare"—— u/ComprehensiveWave475。

### 七、中文圈：怀疑向长文实取全文（已解决——非知乎通道）

**兮动人《AI 圈又在造新词：所谓 Loop Engineering，不过是自动化换了个包装》**（腾讯云开发者社区 [article/2709808](https://cloud.tencent.com/developer/article/2709808)，发布 2026-07-15 14:53:43，页面计数 586 阅读 / 1 评论，2026-10-06 观测；正文自页面内嵌 JSON 完整提取，约 4,954 字符 markdown）。中文圈少见的**逐项拆解型怀疑文**（附"Loop Engineering 说法 → 原本工程概念"对照表：Cron/状态机/Worktree/CI/代码审查）：

> "但把外面的包装拆开，你会发现里面装的基本都是老熟人：定时任务、工作流、状态管理、Git Worktree、自动测试和代码审查。这些东西早就存在。现在把 Agent 塞进流程中间，再统一取一个叫 Loop Engineering 的名字，就成了一门新'工程学'。"
> "Agent 可以一晚上生成几十个改动，不代表团队第二天有能力理解和验证这几十个改动。自动化的产出速度超过审查速度后，多出来的不是生产力，而是待确认的风险。"
> "我质疑的是，把一套已有多年的工程实践重新组合后，包装成一种即将取代 Prompt Engineering 的新范式。"

### 八、smzdm"扯淡名词"转述链升级（部分解决——smzdm 原帖实取，知乎原文仍开放）

《[Loop工程，从"新范式"到"扯淡名词"只用了两个月](https://post.smzdm.com/p/a267neq7/)》（smzdm，2026-08-24 14:57，"源自91位全网作者"；页面自标"内容由AI生成"——**该标签本轮在 HTML 中核实**）。上文此条从"未核"升级为"smzdm 原帖实取"，知乎反转文的存在性链条固化：

> "8月17日，知乎上一篇题为《2026年最扯淡的AI名词——loop》的文章直接开炮：Agent loop就是本年度到目前为止最扯淡的AI名词，没有之一。"
> "人家讲的不过是AI编程的日常操作流程，却被'闲的发慌的某些自媒体拔高到了某种神秘的境界'"（smzdm 转述知乎文的论据：Boris Cherny 在 AI Ascent 的发言）
> "知乎那个'如何看待由OpenClaw作者引发的Loop工程讨论'的问题，单条回答收获1700多赞、61万浏览。"（smzdm 8-24 观测口径）
> 另载："小红书上一篇讲解笔记拿到1200多赞、1800多收藏"；李楠长文打假"把开环迭代当闭环"只是"多次重试"；7-02 吴恩达长文、7-07 Claude 官方 Loop Engineer 入门文（四档）。

（仍是二手：知乎原帖正文、问题页热度一手值均未核——见第九节。）

### 九、B 站（新增量）：质疑向头部视频（元数据实取，视频内容未核看）

【闪客】《新名词诈骗！你管这破玩意叫 Loop Engineering？》（UP：飞天闪客，2026-06-25，B 站 [BV1Xg7v6PEr9](https://www.bilibili.com/video/BV1Xg7v6PEr9/)，view API 2026-10-06 观测）：**109,763 播放 / 3,692 赞 / 992 投币 / 2,032 收藏 / 324 弹幕**——中文圈目前所见 loop 议题最大单条流量，标题质疑向（硬核科普 UP 的拆解风格，正反判定需看视频本体）。简介自列信源：Claude 官方 scheduled-tasks 文档、OpenClaw 创始人 Peter 推文、Addy Osmani 文。

### 十、本轮通道负结论（仍开放清单）

- **知乎两目标仍未核原文**（部分解决→仍开放）：URL 已定位——《[2026年最扯淡的AI名词-loop](https://zhuanlan.zhihu.com/p/2072831171701088483)》（agile zhou）与《[如何看待由 OpenClaw 作者引发的 "Loop 工程" 讨论？](https://www.zhihu.com/question/2048003050531558553)》（另有 deephub/程墨Morgan/DBinary 三条回答 URL）——但主站 403、`/api/v4/articles/{id}` 返回 code 10003、`/api/v4/questions/{id}/feeds` 返回 code 40353（need_login＋unhuman 反爬跳转）；Bing 搜索/缓存无可用链接。知乎层仍需登录态人工核取。
- mp.weixin.qq.com 鱼皮文原始页：**未定位到原始 URL**（搜狗微信搜索两次均"没有找到相关的微信公众号文章"；鱼皮 AI 导航转贴页静态 HTML 无微信链接）——仍开放，腾讯云同步页仍是可得来源。
- 小红书：搜索页仅返回 JS 空壳（标题 "loop engineering - 小红书搜索"，无结果数据）——仍开放（smzdm 转述的"1200+ 赞/1800+ 收藏"仍为一手热度唯一来源）。
- B 站搜索 API（`/x/web-interface/search/type`）返回风控 HTML 页——不可用；但视频元数据 view API 无需登录即可取（本轮 5 条视频全部经此核到）。


## 拉取纪律执行（2026-10-06 用户定：两轮拉不到就放弃）

- **放弃**：Doc Searls 两句（两轮零命中、线索存疑）——出候选、不再挂账；Kelsey Hightower 逐字（两轮 403，一手载体不存在）；Reddit 死通道（old.json / pullpush / redlib / r.jina.ai）——keeper 通道为 arctic-shift＋wayback；Lobsters 搜索路径（标签页通道为 keeper）。
- **保留**：无（本派无"未发布"类项）。
- 本节之上的"仍开放"表述凡与本节冲突，以本节为准。
