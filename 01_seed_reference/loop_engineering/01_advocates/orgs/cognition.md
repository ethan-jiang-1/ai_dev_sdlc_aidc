---
type: org_evidence
directory: 01_advocates/orgs
observation_date: 2026-10-06
---

# cognition — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

### Devin / Cognition —— 解决·强（06-04 双篇＋Fusion 06-29＋ACU usage policies 文档）

- **F1. Scott Wu（CEO）署名《AI should earn its keep: Introducing the AI Productivity Guarantee》**
  - URL/日期：https://cognition.com/blog/ai-guarantee ；datePublished **2026-06-04**（页面 JSON-LD＋页头 "06.04.26" 双确认）；署名 **By Scott Wu**。
  - 逐字摘录：

> "The industry needs to move from maximizing usage metrics to maximizing outcomes — and right now, there's no good standard for measuring that. AI vendors should be the ones to provide it."

> "We built an AI estimator that measures the productive engineering output Devin is providing to enterprise customers. … if Devin delivers less engineering value than you're paying for, Cognition will fund your usage up to $10M until it does. We're calling it the AI Productivity Guarantee."

> "We measure in hours of productive output because lines of code don't correspond to effort: a critical bug that takes hours to investigate might be a two-line fix."

> "If the session resulted in unmerged PRs or was classified as otherwise unproductive, the output is considered not useful."

> "Devin has fine-grained controls to manage spend and steer users towards more productive prompts already."

  - **该条支持的最小主张**：Cognition 把"环产出有没有用"的判定（unmerged PR／unproductive session 分类）做成产品承诺机制——loop 输出质量本身被厂商金融化担保（$10M 上限）。
  - 派别适配：**推动·厂商**（对赌式卖点）；其方法论自认（估计不可靠等）见怀疑面增量 G。

- **F2. 技术博客《Estimating the Productivity of an Autonomous AI Software Engineer》**
  - URL/日期：https://cognition.com/blog/ai-productivity ；**2026-06-04**（同上双确认）；署名 The Cognition Team。逐字与自认部分见怀疑面增量 G（本体一手：数据集 258 sessions / 126 users、r_log 0.74、LLM 时间估计不可靠的官方表述）。
  - **该条支持的最小主张**：自主 agent 生产力可被自动估计并已在生产运行（厂商自述 "the first automated system measuring AI engineering productivity in production"）。
  - 派别适配：**推动·厂商**（能力主张）＋方法学自认（分列）。

- **F3. 官方博客《Devin Fusion》（06-29）**
  - URL/日期：https://cognition.com/blog/devin-fusion ；datePublished **2026-06-29T10:00:00-08:00**（JSON-LD 实取）。
  - 逐字摘录：

> "Engineering teams are lighting money on fire. It's no longer sustainable to use the most expensive models on every task. But existing tools for mixing models suck."

> "The key idea behind our architecture is to run two parallel agents: one with a frontier model, the other with a more cost-effective "sidekick" model."

> "By default it should delegate and monitor, while making the significant decisions: the plan, the interpretation of ambiguity, the final review."

> "We initially reported a 35% cost reduction at publication. On the latest FrontierCode 1.1 Extended data (updated 8/7/2026), Fusion is up to 60% cheaper, as shown in the updated charts."

  - **该条支持的最小主张**：Cognition 的并行产品表达（Fusion）=主环"delegate and monitor"、sidekick 并行执行、决策（plan/歧义解释/终审）留给 frontier 主环；**初报 35%→8/7 修正 60%** 是官方自我数据修正（证据链注记）。
  - 派别适配：**推动·厂商**。窗口外备注："Devin can now Manage Devins"（并行编排 manager-devin，2026-03-19 实取）为本产品面底座。

- **F4. 官方文档《Usage policies: per-user ACU limits》（docs.devin.ai，living docs，实取 2026-10-06）**
  - 逐字摘录：

> "Usage policies let enterprise administrators cap each member's monthly ACU consumption. A member's local usage (Devin Desktop, Devin CLI) and cloud usage (Devin sessions) count against a single per-user limit, and new work is blocked on all surfaces once the limit is reached."

> "Per-user limits are independent of organization-level ACU limits — a session is blocked if either limit is reached."

  - beta 状态句进怀疑面增量 H。**该条支持的最小主张**：Devin 的预算上限是"双门闩"（per-user 与 org-level 任一触顶即阻断所有表面）——target 9 Devin 行官方一手。

### F · Devin：ACU 双门闩参数化（docs.devin.ai 实取）

- **三层 ACU 控制与解析公式**（federal/acu-limits.html 实取）：Team limit（每人默认）/Group cap（组内每人的 cap，**非共享池**，逐字："*It is not a shared pool for the group*"）/User override。**有效限额公式逐字**："*valid user override ?? min(team limit, highest positive group cap)*"；user override 即使更高也赢；多组取**最高**正 cap。**零与未设值语义表**：Team=0 或 user=0 → 封禁；**portal group cap=0 是"清除"不是零限**（"*The group cap is cleared; it is not treated as a zero-ACU group limit*"，portal 收 `cycle_acu_limit: 0`，API 用 `set_cycle_acu_limit`/`clear_cycle_acu_limit`）；全未设→无执行。示例表逐字：team 1000/两组 300、400 → 400；team 200/override 500 → 500。
  - 挂钩：**预算与熔断**（熔断粒度到人、零值封禁语义逐字）。
- **企业 usage policies**（enterprise/features/usage-policies.html 实取，标注 **beta**）：本地（Desktop/CLI）与云（sessions）合并计数，"*new work is blocked on all surfaces once the limit is reached*"；**Devin Review 不计入**；per-user 与 org-level 双门闩——"*a session is blocked if either limit is reached*"。tier 解析优先级逐字：显式指定 tier > 最高优先级 IdP 映射 tier > default tier；override 分 **temporary**（本周期到期）/**permanent**；**审批策略三档**：Manual approval / Always approve（至 tier 的 maximum auto-approve allocation）/ **Approve based on efficiency**（efficiency score 为 Healthy/Satisfactory 才自动批，且只批小步额）——"*Requests are never denied automatically — denying is always an admin decision.*"；降限额前预览 blast radius（"*how many members would be blocked, lowered, or unaffected*"）。计量（admin/billing/usage.html）：Windows 会话 **+9%**，macOS 平价（促销定价）；睡眠不计费——"*Devin sleeps automatically after 30 minutes of inactivity by default.*"
  - 挂钩：**预算与熔断**（效率分驱动自动加预算＝把"该不该续费算力"判据从人移到计量器）＋**无人值守运行**（sleep/wake 计费模型）。
