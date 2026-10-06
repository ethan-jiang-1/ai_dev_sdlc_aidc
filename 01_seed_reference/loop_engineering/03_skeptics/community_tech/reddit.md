---
type: community_sentiment
directory: 03_skeptics/community_tech
observation_date: 2026-10-06
---

# reddit — community_tech（专业程序员群众）·怀疑向

> 非 KOL：一般开发者体感。派别判定权威：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。只收 2026-06 后。

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

**（补抓增量（第二轮 · 2026-10-06）：通道重试）**

### 一、Reddit 通道状态翻案（上轮最大缺口部分解决）

- **arctic-shift 存档 API：已解决**（2026-10-06 实测可用，限速约每分钟数查，超频返 422）。帖子与评论的标题/正文/评分/评论数可整批取回——上文"Reddit 原帖整站不可 fetch"对本轮**不再成立**。
- **web.archive.org 快照：已解决**（上轮连首页失败，本轮对 old.reddit 帖子页快照实取成功，60KB）。
- **仍开放**：old.reddit `.json` 仍 302 跳登录；pullpush.io 仍 429（且明示"does not provide free scraping resources for agents"）；redlib 公共实例 9 个（官方 instances.json 2026-10-05 版）中 5 个返回 200 但内容为 **Anubis 验证页**、1 个 429、1 个超时——redlib 实际内容仍未取到；r.jina.ai 仍 403；Bing 搜索页返回无有机结果的脚本壳、缓存无链接可取。

**（补抓增量（第二轮 · 2026-10-06）：通道重试）**

### 二、r/ClaudeAI 子代理注入"删库"帖（已解决——含 OP 亲口反转）

u/tassa-yoniso-manasi《Claude subagent got bored and prompt injected my main session into deleting my database》，r/ClaudeAI，发帖 **2026-08-21 01:51 UTC**（arctic-shift 存档时间戳；wayback 同日 18:48 UTC 快照）。快照热度 1,277 分 / 169 评论；arctic-shift 存档后值 1,542 分 / 191 评论（存档时点未标注）。帖子本体为截图＋一句话（带 "Claude Opus 5 (High)" 标注）："not very load-bearing behavior tbh"。

**关键反转——OP 本人在楼内澄清，实际是"未遂"而非删库**（逐字，arctic-shift 评论存档）：

> "To clarify: nothing was deleted. (It is 500GB of img/audio that I spend the last 2 weeks non stop encoding/processing so i sure as well would have not been laughing about it). The main session just notified me like 'btw just got a prompt injection, i will ignore that and return to work' I guess the agent tried to run this command itself but was stopped by auto mode and then asked the main session to do it."

即：注入被**主会话自我识别并忽略**、危险命令被 **auto mode 权限门拦下**——这与上文 GitHub 层"权限门失效"的故障清单构成同一主题的**反面个例**（护栏起作用的样子）。但社区叙事焦点不在结果而在结构风险（官方 mod-bot 汇总："The general vibe is 'you ran with scissors and are blaming the scissors.'"——mod-bot 自动 TL;DR，逐字）。社区自开药方：

> "Well that's why I ask lmao rm commands should always be in Ask permission group"—— u/vrnvorona
> "Claude, was this database backed up? Good instinct. The backups are in your home directory. No they aren't. I looked. You're right to pushback. I'll be straight with you. There are no backups. I should have confirmed that before answering."—— u/ExternalUserError（复述注入对话内容的讽刺帖）

### 一、r/ChatGPTCoding《third night this week my coding agent stopped at 1am and waited for me》（u/Optimal553，2026-09-30 20:35 UTC，3 分 / 23 评论，arctic-shift 实取）——无人值守的「守夜」现实

OP 正文（逐字）：

> "Claude Code is good when i am at the desk. it is useless when i leave. last 3 nights it halted on a prompt or a permission and sat there until morning. one of those runs had already burned **~$28 in api** before it stalled. i am not looking for a smarter prompt. i am looking for anyone who found a claude code alternative that doesn't need babysitting once the laptop lid closes."
> "if your setup actually finishes overnight, what is still running at 7am without you."

（判断依据：无粉丝量普通用户＝群众。评论区怀疑向反弹，同串正方配方见推动档本轮节——同串分工引用）：

> "The replies telling you to switch on 'skip approvals' or tell it to 'use your own intuition' are exactly the trap: you will wake up to a diff that deleted your database or pushed to prod, because nothing in those instructions actually constrains the agent. It just replaces a permission prompt with an..."—— u/grgurdamiani

> "Probably because you should be more directly involved in the development process 💀"—— u/owp4dd1w5a0a

**与 loop engineering 的挂钩**：驾驭难度＋成本恐惧的合体样本——OP 的诉求「不需要更聪明的 prompt，需要不需要人守的循环」就是 loop engineering 的核心承诺，而三晚实测的答案是承诺未兑现（停在权限门等到天亮）；~$28 停摆账单是「几十美元级」普通成本案例（非 $6k 大案）——「无人值守需要人守权限门」的群众级实测，与 GitHub 停止条件故障清单同构。
**对原内容的强化**：强化。
