---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# steve_yegge — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

**对抗轴**：Ronacher 经济-质量极（[ronacher](../../03_skeptics/kol_tech/ronacher.md)）——同题正反。

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
