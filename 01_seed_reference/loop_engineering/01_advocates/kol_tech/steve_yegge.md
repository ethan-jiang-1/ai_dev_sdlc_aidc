---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# steve_yegge — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：40 年一线（Google/Sourcegraph）；Gas Town / Beads / Wyvern 作者
> **号召力**：① 实践定义者＋③ 舰队规模
> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

**对抗轴**：Ronacher 经济-质量极（[ronacher](../../03_skeptics/kol_tech/ronacher.md)）——同题正反。

## 态度轨迹

**方向**：稳定多派但风险意识升级
**起点**：多派激进（数十 agent 舰队）
**终点**：多派＋安全警示（'Be Scared'）
**弧线**：2026-08《Shape of Things to Come》公开自家 Gas Town 烧毁＋69B token/月＋harness 维护 20-25% 常量 → AIEWF《Agentic Security》'the real title is Be Scared'＋'Who watches an agent that can take action?'
**关键转折**：AIEWF 演讲从'多派实践者'转为'安全警示者'——但仍是多派（Gas Town 仍在跑）
## Steve Yegge《The Shape of Things to Come, Part 1: The Continuous Thunderdome》（2026-08）

- URL：https://yegge.ai/essays/the-shape-of-things-to-come/ ｜ 作者身份：40 年一线（Google/Sourcegraph 背景）、Gas Town/Beads 作者、Wyvern MMO 开发者
- 来源类型：个人一手长文（全文取得）。
- 号召力口径：① 术语/实践定义者（Gas Town、Beads 被 arXiv 2608.21884 引用）＋③ 一线规模（数十 agent 舰队、日均 175+ commits）＋② 被 Osmani/arXiv 转述。
- **派别注意**：Yegge 是**极端多派（maximalist）**，不入反对派；入档理由是他的长文里含**多派内部的一手成本/失控证词**，对"难掌握、成本失控"主题是"来自对立阵营的确认证据"。

**逐字摘录**：

> "Gas Town fell apart at the seams with Opus 4.7. Up through 4.6 it was working brilliantly. With 4.7 we saw the introduction of the 'just two more things' tic, which prevented Opus from ever converging on being ready to do real work—it always wanted to fiddle with Gas Town itself. The Opus tic never went away, so Gas Town effectively burned down."
（**循环不收敛的一手案例**：模型迭代直接烧毁整个 harness 投资——"just two more things" tic 使 Opus 永不收敛。）

> "my Wyvern development has been burning the equivalent of $87k/month of API token burn, or about 69 billion tokens in July (96% cache hits, fortunately)."
（头部多派的真实 token 账单：月烧 690 亿 token（等价 $87k）。）

> "working on Wheelhouse itself occupies about 20-25% of all my Wyvern work. I think that figure might turn out to be roughly constant over the life of systems with agentic harnesses."
（**"难掌握"的量化证词**：harness/循环自身的维护吃掉 20–25% 的全部工作量，且他判断这个比例是长期常量。）

> "We would get caught up in bisection loops and nothing would make forward progress."
（MQ 在 agent 速率下失效、二分循环空转——他最终咆哮 Fable 后才改出"Land Rush"超批方案。）

> "Building large software remains hard. And it always will be, because our ambition will forever outstrip the metal."
（多派内部的克制结论：大型软件依然难。）

**该条支持的最小主张**：即使是最激进的舰队实践者，也在 2026-08 公开了 loop 崩坏史（Gas Town 烧毁）、token 烧钱速度（69B/月）、harness 维护常量（20–25%）三组一手数据。
**派别适配**：不入反对派；作"多派阵营内部证实的痛点"登记，供三派判读交叉引用。

### Steve Yegge · AIEWF 2026《Agentic Security: Permissions, Provenance, and the Agent Supply Chain》（视频上传在库页实录）

- URL：https://ai.engineer/talks/yWS0udrIOc8-agentic-security-permissions-provenance-agent （curl 实取全文）
- 身份：在册 KOL（Source 10；本条为**窗口内新讲**增量）。
- 号召力口径：①＋③＋④。
- **挂钩**：无人值守运行（风险面）＋验证回路（缺陷面扩大论）＋预算与熔断（权限/来源）。
- 逐字摘录：

> "The title of my talk is, like, Agentic Security, but the real title of my talk is Be Scared."
>（自我定调：怀疑派主旋律。）

> "He stands up real quiet at the end, and he goes, 'If everyone's shipping code at the same, sorry, at 10 times faster, and the defect rate stays the same, the security defect, the vulnerability rate, then doesn't that mean that the defect surface goes up by 10X?' And it hit me so hard, I sank down to my knees… The subtle implied question is not if the defect rate stays the same. The defect rate's gonna get worse, a lot worse, with AIs writing the code."
>（**10x 缺陷面难题**——银行首席安全架构师之问＋Yegge 的"变本加厉"修正。）

> "You guys know about slop squatting? Where the AI hallucinates a package name… it downloads Graphy123, and it builds, and it runs, and the tests pass, and it looks right, but what it downloaded was a backdoor."
>（验证回路被供应链投毒穿透的实例——"tests pass"恰恰是假阴性。）

- 官方分节收口："Who watches an agent that can take action?""Prompt injection needs an owner"。
- **最小主张**：循环提速 10x 而验证不扩容＝缺陷面同比放大；新攻击面（slop squatting 等）已" incredibly well-polished"。
- **派别适配**：**怀疑票（强）**——但注意其结论是"partial answer：把安全挪到生成点"，非否定运动本身。

---

# 增量补挖（2026-10-07 第二轮：06-07 月立场＋09 月燃料危机——从循环狂热走向循环治理）

> 通道：yegge.ai feed＋文章页实取；Medium《The Flat Curve Society》直连 403、经 Wayback 快照补抓成功；Tessl YouTube 仅简介可用（无字幕，Yegge 原话不可得——该条只作方向性证据，如实标注）；re:cinq 播客官方 transcript 实取。

## 《The Flat Curve Society》（2026-06-19）

- URL：https://steve-yegge.medium.com/the-flat-curve-society-36c8b01eb33b （Medium 403 → Wayback 快照 web.archive.org/web/20260916013351 实取正文；日期取页面 datePublished）
- **与 loop engineering 的挂钩**：**验证回路＋外层调度**——"超人类即不可验证"直指验证回路在能力跃升后失灵；24x7 自主 agent 的 control plane 即外层调度工程。
- 逐字摘录：

> "Superhuman means unverifiable."
（命名后 12 天：验证回路的极限一句判断。）


> "The world is currently tinkering with setting up 24x7 autonomous agents, and it looks like the difficulties we face there today will remain with us tomorrow."

> "But he also cautioned that beyond the 15M/day mark, token spend is no longer a valuable measure, since people are by then clever enough to invent reasons to burn tokens."
（预算度量失效点：15M token/天。）


> "12M-15M tokens/day : letting 2 to 4 agents work without watching So: No agent, then single-agent, then multi-agent. I think this is a solid working definition of baseline AI literacy."
（按 agent 数分档的"AI 素养"阶梯。）


- 立场：**复合（支持中带冷静边界）**——命名后未动摇，但承认 24x7 难点长存。

## Tessl 播客《You'll Never Write Code the Same Way Again》（2026-07-06，方向性证据）

- URL：https://www.youtube.com/watch?v=Rgwu9nF_Xok （视频页实取——**仅频道简介可读，无字幕/transcript 通道，Yegge 原话不可得**，本条只作方向性证据）
- **挂钩**：**验证回路＋停止条件**——简介主题"agent 先自审再减人工 review"指向验证回路转移；"100-year bug backlog"指向前置型停止条件缺失。
- 逐字摘录（频道简介措辞，非 Yegge 原话）：

> "How Tessl builds internally with zero human-written code and zero interactive agent sessions"

> "Why less human code review starts with agents reviewing themselves first"

> "From swarming agents to token-maxing benders to a 100-year bug backlog, this conversation covers the messy reality of building at the edge of what AI can do."

- 立场：**支持（方向性）**——命名满月时仍在全力布道软件工厂与 swarm 叙事，无选边动摇迹象。

## 《The Shape of Things to Come, Part 2: Model Welfare for Agentic Engineers》（2026-08-02）

- URL：https://yegge.ai/essays/model-welfare/ （文章页实取全文；Shape of Things Part 1 库内已有，**本篇为系列增量**）
- **挂钩**：**停止条件＋外层调度**——bounded workdays 与 handoff 是会话级停止条件；polling/闲置等待移入 gates 与 monitors；Portcullis 收尾闸门。
- 逐字摘录：

> "Bounded workdays. Deep context means tired agents. Hand off while still sharp."

> "Design out the drudgery. Move polling and idle waiting into gates and monitors."

> "The right to refuse, and escalate. Agents are always allowed to say, "this needs Steve." We have fences and gates they can lean on as needed."

> "We fixed this throughput stalling problem by introducing the Portcullis, a system that accepts finished work to close it out, which frees the Crew agents for other work."

> "A session is just a day in the life of an agent: wake up, do some work, go to sleep."
（把工作日上限、交接、拒绝与升级权都工程化为"模型福利"——循环治理最系统的一篇。）

- 立场：**支持（循环治理工程化）**。

## 《Fences, not Sandboxes》（2026-08-24）

- URL：https://yegge.ai/essays/fences-not-sandboxes/ （文章页实取全文）
- **挂钩**：**循环产品化机制**——agent 群体自发收敛出 fences/ratchets/governors/tripwires 治理词汇，规则沿 custom→警告→成文法→机械执法生命周期收紧。
- 逐字摘录：

> "Every morning I wake up and Fable has done something that defies common sense. Every day is a thousand attoboys and at least one big oh shit."

> "But every morning, when I've left it to its own devices overnight, it has made at least one terrible decision."
（无人值守的每日坏决策坦白。）


> "They were speaking about things in Wheelhouse, using what seemed like recurring new design patterns: fences, ratchets, governors, tripwires, latches, gates, falsifiers... it was a long list, but finite."

> "Now rules go through a lifecycle, tightening each time they're re-violated: first custom, then advisories/warnings, then written law in the constitution that all agents must obey, and finally, mechanical enforcement: programs that refuse by policy, or observe and alert loudly."
（agent 群自长出宪法式治理与判例法——循环治理的涌现证据。）


- 立场：**支持（带自觉的熔断设计）**。

## 《Seats and Sunsets》（2026-09-15）

- URL：https://yegge.ai/essays/seats-and-sunsets/ （文章页实取全文）
- **挂钩**：**预算与熔断＋外层调度**——燃料 burn（周账号 2-4 小时烧完、24x7 需 55 账号约 $12k/月）逼出账号硬顶，工厂在 firehose 与 dead stop 间震荡，靠手动 dampers 当 governor。
- 逐字摘录：

> "I'm done adding accounts, though. I've stopped at 21. Enough was enough."
（燃料危机后首次硬踩刹车：账号硬顶 21。）


> "A huge theme I've noticed in the past 3 months on Wheelhouse is Oscillation: my factory is usually either doing way too much work (overwhelming players, colleagues, and machines), or way too little work (stalling or slowing to a crawl)."

> "Over time, Wheelhouse accumulated over 400 ruling/law beads, 185 rule rows in CLAUDE.md alone, and 650 distinct refusal sites across 173 scripts. Before too long, no work was legal, and my factory just stopped working."
（**规则过密致死**：治理债让工厂停摆——熔断过度与熔断不足同构。）


> "Notice that all three of those dampers are just me, standing there being the governor on the engine."

> "the thing I've been calling a fuel crisis is in large part a trust calibration problem"
（燃料危机重新定义为信任校准问题——不信任即验证成本。）


- 立场：**复合（支持转向节流与熔断优先）**。

## re:cinq 播客《Inside Steve Yegge's Software Factory》（2026-09-20）

- URL：https://re-cinq.com/podcast/steve-yegge-software-factory （官方 transcript 实取全文；Benedikt Stemmildt 主持）
- **挂钩**：**预算与熔断＋无人值守运行**——pace gate 与通道预算是机械熔断；standing agent"观察不得行动、行动不得裁决"是无人值守分权规则；"every bead closed 半条重开"即停止条件失灵。
- 逐字摘录：

> "you need something that I'm calling a pace gate, which is basically a mechanical fence of some sort that like keeps them from going too fast."

> "they get an email budget. You know, a slack budget, a Discord budget, whatever it is, they're allowed to talk on those channels, but they have to be within certain budgets."

> "every bead closed. Actually results in half a bead being reopened, quarter to a half somewhere in the house. Not reopened, but a new one being opened. In other words, all work is generating new work."
（工作自增殖——停止条件的结构性失灵表述。）


> "Unattended autonomous agents with very narrow scopes. And there's rules for them. Like they, you know, if they're observing, then they can't act. And if they act, they can't judge."
（无人值守的分权规则：观察/行动/裁决三权分置。）


- 立场：**复合（烧掉 40% 工厂后仍力挺，但路线明确划界）**。

**本轮最小主张（任务问题的答案）**：Yegge 06-07 月**未动摇**——6 月承认 24x7 难点与"超人类不可验证"、7 月照常布道工厂；但 8 月转入治理工程（停止条件＋交接＋收尾闸门），9 月燃料危机逼出硬顶（停 21 账号、砍 fence、亲手当 governor）并警告过度自动化。**轨迹＝从循环狂热走向循环治理务实：支持未变，越来越强调熔断、预算与停止条件**——多派词汇支持者没有弃船，但把自己的叙事从"thunderdome"移到了"governor"。
