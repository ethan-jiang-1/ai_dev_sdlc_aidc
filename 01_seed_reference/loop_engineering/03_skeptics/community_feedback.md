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
