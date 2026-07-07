---
type: concept_deep_dive
event: FOSE Europe (Engelberg)
concept: Harness Engineering Emergence
date: 2026-07
verification_status: verified
source_urls:
  - https://martinfowler.com/fragments/2026-07-06.html
  - https://overwatering.org/blog/2026/07/notes-from-fose-europe/
key_concepts:
  - harness_engineering_term_emergence
  - harness_engineering_teams
  - devops_parallel
  - agent_judgement_gap
  - code_persistent_or_regenerated
  - domain_modeling_as_steering
---

# Harness Engineering 的浮现 — 以及 Engelberg 的开放问题

> 来源：Martin Fowler, [Fragments: July 6](https://martinfowler.com/fragments/2026-07-06.html) · Giles Edwards-Alexander, [Notes from FOSE Europe](https://overwatering.org/blog/2026/07/notes-from-fose-europe/)

---

## 一个术语在五个月内从不存在变成核心议题

Martin Fowler 注意到了一个惊人的变化：

> *"Harness engineering — a term that didn't even exist at the Utah retreat — was a major topic at Engelberg."*

在 Deer Valley（2026 年 2 月），这个术语还不存在。到 Engelberg（2026 年 7 月），它已经是核心议题。这反映了整个领域在极速演化。

---

## Harness Engineering Teams 正在浮现

Edwards-Alexander 报告说 **"harness engineering teams"** 已经作为一个模式在浮现。

但这里有一个危险的平行：

> **DevOps 运动的教训**：当初 "DevOps teams" 出现时，很多人误解了 DevOps 的本意——DevOps 应该是文化变革，不是一个新的 silo。Harness Engineering Teams 可能面临同样的陷阱。

问题是：**Agentic engineering 的 "DevOps 运动" 等价物是什么？** 目前还没有答案。

---

## Agent 能带来所有专业知识，但不能带来判断力

Engelberg 的一个关键洞察：

> *"Agents can bring all the expertise, but they can't bring judgement."*

这解释了为什么**领域建模**在讨论中反复出现——它是引导 Agent 和扩展团队的机制。但一个未解的问题是：为什么 DDD 现在突然有用了？以前从未成为主流。

---

## 工程严谨性在 Agentic 时代的去向

Engelberg 的讨论确认了严谨性正在迁移到：
- **测试**（BDD 正在复兴）
- **Linting**
- **形式化模型**（TLA+ 由 Agent 生成）
- **领域建模**作为引导 Agent 的机制

---

## 两个尚未回答的大问题

### 1. 代码是持久的还是持续丢弃再生的？

> *"Is the codebase persistent, or is it continuously discarded and regenerated?"*

如果 Agent 可以从 spec 随时重新生成代码，那代码库还需要存在吗？还是变成像 build artifact 一样每次都重新生成？

### 2. 什么是 Agentic Engineering 的 "DevOps 运动"？

> DevOps 在 2010 年代打破了 Dev 和 Ops 之间的墙。Agentic engineering 需要打破什么墙？
> Harness Engineering Teams 是答案还是又一个 silo？

---

## 关键引用

> *"Harness engineering — a term that didn't even exist at the Utah retreat — was a major topic."* — Martin Fowler

> *"Agents can bring all the expertise, but they can't bring judgement."* — Engelberg 讨论

> *"Is the codebase persistent, or is it continuously discarded and regenerated?"* — Engelberg 开放问题
