---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# sachin_malhotra — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：Anthropic CI 团队工程师
> **背景**：Sachin Malhotra——硕士期间任 Information Sciences Institute（ISI）research assistant；Microsoft Azure authoritative DNS 团队（2019–2022）→ Etsy Personalization staff ML 工程师（计算机视觉）→ 现 Anthropic CI 团队：测试隔离、merge 自动化、CI autoscaling，主导 Claude Tag CI 事件响应器与 ci-weather；AIEWF 2026 讲《Give the Agent a Budget, Not a Token》。（履历核：ai.engineer 讲者页＋claude.com 博客署名，2026-10-07）
> **号召力**：③
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——待补挖。
### Sachin Malhotra（Anthropic，CI 团队工程师）· AIEWF 2026《Give the Agent a Budget, Not a Token》（视频上传在库页实录）

- URL：https://ai.engineer/talks/rbjWzZK2LU0-give-agent-budget-not-token （curl 实取全文）
- 身份：Anthropic CI 团队（测试隔离/合并自动化/CI 自动扩缩），一线工程实践者。
- 号召力口径：③（Anthropic 一线），个人非 KOL——**仅作会议层样本，但其"预算四维"框架机制价值高**。
- **挂钩**：预算与熔断（七类最正牌的一篇）＋停止条件。
- 逐字摘录：

> "It took out about 200 workloads, which ended up impacting about 20 engineers worth of stuff, and all of that was gone in 90 seconds. Nobody was being malicious… the agent genuinely thought it was tidying up after itself."
>（开场事故实录：agent 清理时 selector 空匹配→批量删除。）

> "A token is a boolean. It's just a yes or no… If the token list is too tight, then your agent is effectively useless. If the token list is too wide, then you're maybe writing a postmortem. A budget is a very different shape… it has four different dimensions: how much can the agent do? How fast can it do it? What can it undo on its own? And who's noticing while it's actually taking those actions?"
>（**"预算四维"**：量/速/可撤销/可观测——预算与熔断类迄今最干净的会议层表述。）

> "Some verbs fail out loud… there are other verbs that fail silently… you give access to verbs that can fail loudly on a dashboard to your agent, and for the other ones just involve a human."
>（"非对称动词"＝按失败可观测性分配人审位——停止条件的工程化判据。）

- 官方要点层："Replace boolean agent permissions with budgets that account for quantity, speed, reversibility, and observation"；分节标题含 "Put a ceiling on every write—and let it refill"（预算回补）与 "Use tripwires to learn from aggregate behavior"（熔断线）。
- **最小主张**：权限的布尔模型必须换成四维预算模型，熔断线（tripwire）与 undo test（用可撤销性给自主度定档）是配套件。
- **派别适配**：**推动票（受约束翼）**。

---

# 增量补挖（2026-10-07 goal 第一批·单点→稳定复核；载体升级：会议层→官方署名）

> 判定：**单点解除 → 稳定（受约束翼）**（08-18 官方署名文 → 08-22 AIEWF 同向）。

## 《Claude on call: How Claude Tag serves as Anthropic's first responder for CI/CD failures》（claude.com，2026-08-18，本人署名）

- URL：https://claude.com/blog/ai-ci-cd-on-call ｜ fetch 成功
- 逐字摘录：

> "Claude authored the first situation report in every recent incident that had one, typically publishing its first analysis within 15 minutes."

> "Standing instructions are in markdown files as skills, committed in a GitHub repository… a log of lessons learned **as part of a self-improvement loop**."
（**lessons 回灌的自改进环**——受约束翼的自改进形态。）

> "The key takeaway here is that the alerting process is deterministic, while on-call escalation has both deterministic and agentic paths."

- 配套：anthropics/oncall-kit 开源（同文链接）。
