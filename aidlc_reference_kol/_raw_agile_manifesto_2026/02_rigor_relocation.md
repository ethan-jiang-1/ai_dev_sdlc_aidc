---
type: concept_deep_dive
event: Future of Software Development Retreat (Deer Valley)
concept: Rigor Relocation
originator: Chad Fowler
date: 2026-02
verification_status: verified
source_urls:
  - https://www.honeycomb.io/blog/production-is-where-the-rigor-goes
  - https://martinfowler.com/fragments/2026-02-18.html
  - https://annievella.com/posts/finding-comfort-in-the-uncertainty/
  - https://okulbida.com/posts/future-of-software-engineering-thoughtworks-2026/
key_concepts:
  - rigor_relocation
  - constraint_removal_not_loss_of_rigor
  - five_destinations_of_rigor
  - production_is_reality
critique:
  author: Charity Majors (Honeycomb)
  url: https://www.honeycomb.io/blog/production-is-where-the-rigor-goes
---

# "严苛去哪儿了？"——Deer Valley Retreat 的核心问题

> 来源：Chad Fowler 在 retreat 中提出的框架，后经多方讨论和 Charity Majors 的批判性回应。
> 参考：[Honeycomb: Production Is Where the Rigor Goes](https://www.honeycomb.io/blog/production-is-where-the-rigor-goes) · [Fowler Fragments Feb 18](https://martinfowler.com/fragments/2026-02-18.html) · [Okulbida 总结](https://okulbida.com/posts/future-of-software-engineering-thoughtworks-2026/)

---

## 为什么这是 Retreat 最核心的问题

据多个来源确认，"Where Does the Rigor Go?" 是 Deer Valley Retreat 讨论时间最长、投入精力最多的议题。

Chad Fowler 的框架：

> *"Constraint removal is mistaken for loss of rigor. But what actually happens, when things go well, is **rigor relocation**. Control doesn't disappear. It moves closer to reality. If generation gets easier, judgment must get stricter. Otherwise, you're not engineering anymore."*

---

## 严苛正在迁移到五个地方

| 目的地 | 描述 |
|---|---|
| **1. 上游 → Specification review** | 糟糕的 spec 在大规模生成代码时产出糟糕的结果。团队开始采用结构化格式（EARS、状态机、决策表）因为模糊的 user story 对 AI agent 不够用 |
| **2. 进入 Test suites** | 测试变成**一等工件**——非确定性生成的确定性锚点。Kent Beck 称 TDD 为 AI 辅助编码的"超能力" |
| **3. 进入 Type systems 和约束** | 与其 post-generation review 代码，不如让错误的代码**不可表示**——通过强类型和形式化约束 |
| **4. 进入 Risk mapping** | 不是所有代码承担同等风险。学科变成：**"如果这段代码错了，影响半径多大？"** 并按比例缩放验证 |
| **5. 进入 Continuous comprehension** | 在 Agent 生成代码的同时，持续维护对系统行为和架构的理解 |

---

## Charity Majors 的批判：生产环境被遗漏了

Charity Majors（Honeycomb CTO）写了一篇尖锐的回应 [*"Production Is Where the Rigor Goes"*](https://www.honeycomb.io/blog/production-is-where-the-rigor-goes)：

> *"If control is supposed to be moving 'closer to reality,' what is closer to reality than your production systems? Production is reality!"*

她的核心论点：

- Retreat 的五个"严苛目的地"没有一个是**生产系统**
- 可观测性、feature flags、rollback 机制、生产环境中的渐进式交付——这些才是最接近现实的控制层
- "严苛不只是验证代码是否做对了事——还是在真实用户、真实数据、真实故障面前验证它是否**继续**做对的事"

---

## 关键引用

> *"If generation gets easier, judgment must get stricter. Otherwise, you're not engineering anymore."* — Chad Fowler

> *"Production is reality! If control is supposed to move 'closer to reality,' what's closer than production?"* — Charity Majors
