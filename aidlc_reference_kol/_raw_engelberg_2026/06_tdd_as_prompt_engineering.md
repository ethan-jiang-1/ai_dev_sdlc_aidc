---
type: concept_deep_dive
event: FOSE Europe (Engelberg)
concept: TDD as Prompt Engineering
date: 2026-07
verification_status: verified
source_urls:
  - https://ubos.tech/news/thoughtworks-future-of-software-development-retreat-highlights-ais-transformative-role/
  - https://www.metasticworld.com/en/insights/thoughtworks-future-of-software-development-retreat-2026
  - https://martinfowler.com/fragments/2026-07-06.html
key_concepts:
  - tdd_as_prompt_engineering
  - tests_as_communication_language
  - tests_first_then_agent_implements
  - robust_test_suites_as_agent_performance_multiplier
---

# TDD = Prompt Engineering — Engelberg 的核心工程发现

> 来源：[UBOS.tech 总结](https://ubos.tech/news/thoughtworks-future-of-software-development-retreat-highlights-ais-transformative-role/) · [Metastic World](https://www.metasticworld.com/en/insights/thoughtworks-future-of-software-development-retreat-2026) · [Fowler Fragments](https://martinfowler.com/fragments/2026-07-06.html)

---

## 核心发现

Engelberg 确认了一个 Deer Valley 时还只是猜测的结论：

> **TDD 是 Agentic 时代最有效的 prompt engineering 方式。**

不是写更长的 prompt。不是调 temperature。而是**先写失败的测试，让 Agent 去实现**。

---

## 为什么 TDD 在 Agent 时代成了"超能力"

| 传统 TDD 的价值 | Agent 时代的额外价值 |
|---|---|
| 确保代码正确 | **测试是 Agent 最精确的 spec 语言**——比自然语言 prompt 准确得多 |
| 防止回归 | Agent 在测试失败时会自动迭代——测试告诉它"哪里不对" |
| 驱动设计 | 测试定义了 Agent 的**不可协商的边界**——"这个东西必须工作" |

---

## Adam Tornhill 的研究数据

Engelberg 上引用了 Adam Tornhill 的研究发现：

> **有健壮测试套件的代码库，AI 生成的 PR 成功率高出 45%。**

这意味着：在 AI 时代，测试覆盖率不再只是"质量指标"——它是 **Agent 生产力的直接杠杆**。

- 测试覆盖率低 → Agent 反复猜测你的意图 → 更高的 token 成本 + 更低的成功率
- 测试覆盖率高 → Agent 有明确的成功标准 → 一次通过率显著提升

---

## 实践含义

1. **在写任何 prompt 之前，先写测试。** 测试就是你给 Agent 的 spec
2. **测试比 CLAUDE.md 里的自然语言规则更可靠。** Agent 可以绕过文字规则（Jesse Vincent 的删测试案例），但无法绕过**可测量的失败**
3. **BDD 正在复兴。** Engelberg 上多次提到 BDD（行为驱动开发）在 Agent 时代获得了新的生命力——用可执行的规范语言描述行为，Agent 直接对接
4. **Token 成本和测试覆盖率的关系。** 好的测试 → Agent 更少试错 → 更少 token 消耗 → 更低成本

---

## 与 Deer Valley 的连接

Deer Valley 上 Beck 和 Fowler 已经说了 TDD 是 "superpower" 和 "not optional"。Engelberg 把这条推到了操作层面：**TDD 不是哲学立场——它是 Agent 的 API。**

---

## 关键引用

> *"Tests become the primary language for communicating intent to LLMs."* — Engelberg 讨论

> *"Robust test suites yield 45% more successful AI-generated PRs."* — Adam Tornhill 研究（Engelberg 引用）

> *"Write the failing test first. Then let the agent implement. The test IS the prompt."* — Engelberg 实践共识
