---
type: concept_deep_dive
event: FOSE Europe (Engelberg)
concept: Galaxy Brain Debate — does architecture still matter?
date: 2026-07
verification_status: verified
source_urls:
  - https://martinfowler.com/fragments/2026-07-06.html
  - https://overwatering.org/blog/2026/07/notes-from-fose-europe/
  - https://aardling.eu/en/insights/software-design-in-the-agentic-age-placing-your-bets
key_concepts:
  - galaxy_brain_hypothesis
  - agent_experience_equals_developer_experience
  - token_cost_as_design_proxy
  - mechanical_sympathy_for_llms
  - ai_dependency_risk_hedging
---

# Galaxy Brain 辩论 — 架构在 Agent 时代还重要吗？

> 来源：Martin Fowler, [Fragments: July 6](https://martinfowler.com/fragments/2026-07-06.html) · Giles Edwards-Alexander, [Notes from FOSE Europe](https://overwatering.org/blog/2026/07/notes-from-fose-europe/)

---

## 两种对立假设

Engelberg Retreat 上浮现了一场核心辩论——两派在架构/设计的未来角色上存在根本分歧：

### 假设 A：Galaxy Brain（"银河大脑"）

> LLM 太强大了，架构和设计不再重要——它可以处理任何意大利面代码。

如果 LLM 真的可以理解和修改任何代码结构，那么投入在模块化、命名、架构整洁上的精力就是浪费。Agent 会自己搞清楚。

### 假设 B：Agent Experience = Developer Experience

> Laura Tacho：*"The Venn Diagram of Developer Experience and Agent Experience is a circle."*

好的模块化、命名、设计——对人类开发者有帮助的东西——**同样帮助 Agent**。乱代码让 Agent 也乱写。整洁代码让 Agent 写得好。

---

## Token 成本作为设计质量的代理指标

Engelberg 浮现了一个新论证：**如果同样的变更消耗更少的 token，可能反映了更好的架构。**

这对于 Galaxy Brain 假设是一个有力的反驳——如果架构真的不重要，为什么糟糕的架构会消耗更多 token？

Martin Fowler 提到了 **"机械共情"（mechanical sympathy）**——理解 LLM 的内部工作机制和成本结构，就像理解 CPU 缓存对性能的影响一样，会成为工程素养的一部分。

---

## Token 成本焦虑

Fowler 引用了 404 Media 的报道：一家公司的 token 账单从 **$5M（2025 年 8 月）→ $15M（2026 年 5 月）→ 预计 $120M/年**。

这使得"好设计是否能降低 token 成本"从一个学术问题变成了**财务问题**。

---

## 依赖风险对冲

Mathias Verraes 提出了另一个论点：好的软件设计是**对 AI 依赖风险的 hedge**。

- AI 可能被监管阻断
- Token 成本可能暴涨
- 公众舆论可能反转

如果系统设计得好，切换 AI 提供商或减少 AI 依赖的成本就更低。**架构是保险。**

---

## 开放问题

- Domain-Driven Design 为什么现在突然有用了？以前从来没有成为主流
- "Mechanical sympathy for LLMs" 作为一门新学科——该教什么？
- Token 成本作为设计质量的定量指标——如何测量和基准化？

---

## 关键引用

> *"The Venn Diagram of Developer Experience and Agent Experience is a circle."* — Laura Tacho

> *"Token costs can serve as a proxy measure for design quality."* — Engelberg 讨论
