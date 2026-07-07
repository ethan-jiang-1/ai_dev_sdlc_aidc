---
type: kol_deep_dive
person: Martin Fowler
organization: ThoughtWorks
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://martinfowler.com/fragments/2026-04-29.html
  - https://www.martinfowler.com/fragments/2026-04-21.html
  - https://newsletter.pragmaticengineer.com/p/cycles-of-disruption-in-the-tech
  - https://www.thoughtworks.com/en-gb/insights/podcasts/technology-podcasts/what-harness-engineering
  - https://www.sohu.com/a/975704211_122036485
  - https://dev.to/bh/verified-changed-meaning-what-agentic-engineering-demands-from-development-teams-19an
key_concepts:
  - verified_meaning_migration
  - harness_engineering
  - automated_gates
  - human_judgment
---

# Martin Fowler — "竞争的本质从'能写多快'变成了'能多快判断它是否正确'"

> 敏捷软件开发、重构、企业应用架构模式的定义性人物。他 2026 年的 *Fragments* 和 ThoughtWorks 播客提供了 AI 时代最冷静、最工程化的视角。他不是 AI 怀疑论者——他认为 AI 是职业生涯最大的一次编程变革——但他的警告比任何 hype 都更有分量。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。

## 最重要的洞察："Verified" 的含义迁移

Fowler 在 2026 年 4 月 29 日的 *Fragments* 中，支持 Chris Parsons 的 *Coding with AI* 第三版更新，贡献了 AI 时代被引用最多的判断之一：

> *"Verified used to mean 'read by you.' With modern agent throughput, it has to mean 'checked by tests, by type checkers, by automated gates, or by you where your judgment matters.' The check still happens; it just does not always happen in your head."*

这个洞察的精妙之处在于：**它既不是"不用审查了"，也不是"必须每行都读"。** 它承认检查仍然存在，但执行者从人类的脑子转移到了自动化工具——而人类保留最终的判断权。

### 由此推导出的竞争新定义

> *"A team that can generate five approaches and verify all five in an afternoon will outpace a team that generates one and waits a week for feedback. The game is not 'how fast can we build' anymore. It is 'how fast can we tell whether this is right'."*

---

## Pragmatic Engineer 专访 (2026/01)：职业生涯最大的变革

Fowler 在 Gergely Orosz 的 *The Pragmatic Engineer* 播客上做出了惊人的历史判断：

> *AI 是他整个职业生涯中最大的编程变革，堪比从汇编语言到高级语言的转变。*

### 非确定性计算

Fowler 反复回到一个根本性技术转变：

- LLM 是**概率性的、模糊的**——相同输入可以产生不同输出
- 这根本改变了你对**正确性和可靠性**的思考方式
- 推荐阅读：Daniel Kahneman 的 *Thinking, Fast and Slow*——建立对概率推理的直觉

### "像一个高产但不可信的协作者"

> *"You must treat each slice as a pull request from a rather untrustworthy collaborator who's highly productive in lines of code but whom you know you cannot trust."*

这不是 dismissive——这正是 Fowler 的工程思维：**不信任不是拒绝，是需要验证机制。**

---

## Harness Engineering——Fowler 亲自推广

Fowler 在 martinfowler.com 上发布了 Birgitta Böckeler 的 Harness Engineering 系列文章。他形容这些文章吸引了"疯狂的流量"。

### Böckeler 的核心框架：Guides + Sensors

| 类型 | 方向 | 例子 | 执行者 |
|------|------|------|--------|
| **Computational Guides** | 喂给 Agent（前馈） | 编码约定文件、lint 规则 | 确定性工具 |
| **Inferential Guides** | 喂给 Agent（前馈） | CLAUDE.md、skills、spec | LLM 解读 |
| **Computational Sensors** | 检查 Agent 输出（反馈） | 静态分析、类型检查器、测试套件、变异测试 | 确定性工具 |
| **Inferential Sensors** | 检查 Agent 输出（反馈） | LLM-as-judge、代码审查 Agent | LLM 解读 |

**关键发现**：计算传感器（确定性的）通常优于推理传感器（LLM 解读的），用于客观质量检查。团队目前在**低估计算传感器**。

### "在环之上"而非"在环之中"

引用 Kief Morris 的区分：目标是从 **"in the loop"**（人类审批每一个行动）进化到 **"on the loop"**（人类监督系统运行，只在需要判断时介入）。

---

## Böckeler 在 martinfowler.com 上的完整系列

| 日期 | 文章 | 核心内容 |
|------|------|---------|
| 2026/02/17 | *Harness Engineering* | 初始概念，回应 OpenAI 的实验 |
| 2026/04/02 | *Harness Engineering for Coding Agent Users* | 完整心智模型：Guides + Sensors 矩阵 |
| 2026/05/19 | *Maintainability Sensors for Coding Agents* | 静态代码分析作为计算传感器 |
| 2026/05/20 | *Three More Static Code Analysis Sensors* | 模块化检查扩展 |
| 2026/05/27 | *The Test Suite as a Regression Sensor* | 已有测试套件作为 Agent 代码的回归传感器 |

---

## "弱 Harness = 更好的 prompt 只产生更复杂的 bug"

Fowler 和 Böckeler 的共同警告：

> *"A weak harness means better prompts just produce more sophisticated bugs."*

换句话说：**不要 tweak prompt。建更好的护栏。** 这与 Ryan Lopopolo 的"Agents aren't hard; the Harness is hard"完全收敛。

---

## Vibe Coding vs Agentic Engineering

Fowler 画了一条清晰的线：

| Vibe Coding | Agentic Engineering |
|-------------|-------------------|
| 不看代码，不关心代码 | 专业使用 AI Agent 放大已有技能 |
| Prompt → 盲目接受 | Prompt → 验证 → 在工程系统中迭代 |
| 适合原型和一次性工具 | 适合生产系统和长期维护 |
| 低控制；放弃责任 | 高控制；人对质量保持责任 |

---

## 角色融合与资深工程师的未来

Fowler 预测**业务分析师和程序员角色的融合**，但强调：

- **资深工程师**应该成为"**塑造 harness 的人**"——不仅仅是审查 diff 的人
- **概念建模**、命名、函数结构在 AI 时代变得**更重要**——研究表明 LLM 在标识符任意的代码上性能显著下降
- **模块化、清晰 API、领域边界**（经典软件工艺）是让 AI Agent 高效工作的基础：*"AX extends DX"*——Agent 体验是开发者体验的延伸
- 让 harness 工作成为**可见的、被衡量的成果**

---

## Agile + AI：协同而非冲突

Fowler 的基本判断：敏捷核心原则与 AI 有强烈协同效应。

> *"The more you can speed that feedback loop up, the greater the consequences."*

小增量 + 紧密用户联系 + 快速反馈——在 AI 10x 加速构建的情况下**更加重要**。

---

## 关键引用汇总

> *"Verified used to mean 'read by you.' With modern agent throughput, it has to mean 'checked by tests, by type checkers, by automated gates, or by you where your judgment matters.'"*

> *"The game is not 'how fast can we build' anymore. It is 'how fast can we tell whether this is right'."*

> *"You must treat each slice as a pull request from a rather untrustworthy collaborator who's highly productive in lines of code but whom you know you cannot trust."*

> *"A weak harness means better prompts just produce more sophisticated bugs."*

---

**Source:** [Fragments: April 29, 2026](https://martinfowler.com/fragments/2026-04-29.html) · [Fragments: April 21, 2026](https://www.martinfowler.com/fragments/2026-04-21.html) · [Pragmatic Engineer: Cycles of Disruption](https://newsletter.pragmaticengineer.com/p/cycles-of-disruption-in-the-tech) · [ThoughtWorks Podcast: What is Harness Engineering](https://www.thoughtworks.com/en-gb/insights/podcasts/technology-podcasts/what-harness-engineering) · [martinfowler.com: Harness Engineering series (Böckeler)](https://martinfowler.com/) · [Sohu Chinese coverage](https://www.sohu.com/a/975704211_122036485) · [dev.to: Verified changed meaning](https://dev.to/bh/verified-changed-meaning-what-agentic-engineering-demands-from-development-teams-19an)
