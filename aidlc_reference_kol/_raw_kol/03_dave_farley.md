---
type: kol_deep_dive
person: Dave Farley
organization: Continuous Delivery Ltd
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://www.aviator.co/podcast/engineering-discipline-dave-farley
  - https://leaddev.com/technical-direction/safe-production-changes-with-agents
key_concepts:
  - continuous_delivery
  - engineering_discipline
  - ai_exposes_lack_of_engineering
---
# Dave Farley — "AI 暴露那些从未学会工程师思维的人"

> Dave Farley 是 *Continuous Delivery* 的合著者，全球最具影响力的 CI/CD 倡导者之一。
> 他对 AI 编码持一种独特的立场：既不恐吓也不夸大——但警告极其尖锐。

---

## AI 的规模判断

Farley 做了一个大胆的历史比较：

> *"Without really much shadow of a doubt, the change that we are seeing now is bigger than all of those put together — bigger than the internet, bigger than object orientation, bigger than the agile transformation."*

但他同时批判两个极端：
- 恐吓者说 AI 不能编程 → **错误**
- 鼓吹者说 10x-100x 提升 → **错误**
- "不是没有提升，只是没有 10 倍"

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。

## AI 编码的三个结构性问题

Farley 不是情绪化地反对 AI——他从工程角度识别了三个结构性问题：

### 1. 英语不是好的编程语言

> *"编程语言被设计来帮助我们思考——分解问题、具体表达想法、推理系统。自然语言太模糊、太开放解释、太不精确。"*

当你用自然语言描述需求时，你失去了编程语言提供的**精确性**和**可组合性**。

### 2. AI 不具确定性

> *"给编程语言相同的输入，你得到相同的结果。给 AI 相同的 prompt，你可能得到不同的输出。这根本改变了我们工具的可靠性特征。"*

非确定性意味着你 **不能依赖重复实验来建立信任**——这是工程方法论的基石。

### 3. 验证成为瓶颈

> *"代码生成便宜了；理解和验证行为才是困难的部分。AI 有时会说测试通过但实际上没有，或者走捷径。"*

你需要的不是更快的代码生成——你需要**验证机制来确认产出符合意图**。

---

---

## 12,000 行问题 — Farley vs Yegge

当 Steve Yegge（知名的"AI 最大化主义者"）告诉 Farley 他用 AI 一天产出 12,000 行代码时，Farley 的回应毫不留情：

> *"I can't read 12,000 lines of code carefully enough to feel that I truly understand and own them."*

这个碰撞代表了 AI 时代最核心的张力：

| Steve Yegge 的立场 | Dave Farley 的立场 |
|-------------------|-------------------|
| 信任 AI，批量产出 | 不能读的东西不能拥有 |
| AI = 生产力倍增器 | AI = 验证挑战放大器 |
| 代码审查管不过来就减少审查 | 不能减少审查 → 需要更好的验证机制 |

Farley 的结论：信任必须来自**可执行规范和持续验证**，不是逐行人工审查，但也绝对不是"不审查"。

---

## Continuous Delivery — 让 AI 时代可以存活

Farley 的核心论点是：**CD 是 AI 时代的基础设施**。定义不变——软件必须始终处于可发布状态，每次小变更后都验证。但在 AI 可以比人类推理速度快得多的速度生成代码的世界里，**小步、安全、可验证的步骤**变得更加关键，而非更不重要。

> *"危险不是 AI 写出烂代码——而是 AI 写出大量代码，速度快到没人能合理检查。"*

---

## AI 放大，不改造

Farley 最尖锐的判断：

> *"AI won't replace software engineers, but it will expose the ones who never learned to think like engineers. Tools can speed you up, but if your thinking's wrong, AI just gets you to the wrong place faster."*

Farley 的核心判断：
- 基本功扎实的团队（小批次、紧反馈循环、CI）从 AI 获得提升
- 大批次工作的团队看到下游混乱——更长的队列、更多问题泄漏到发布中
- **如果你已经工作得好，AI 会是一个大赢家。如果你工作得不好，你只是更快地挖更深的坑。**

---

## 意想不到的乐观

尽管有这些警告，Farley 有一个出人意料的乐观结论：

> *"AI may be the industry's best-ever opportunity to finally get XP practices embedded — not because teams adopt them ideologically, but because working without them while using AI is visibly, measurably risky. The stakes are now too high to ignore engineering discipline."*

换句话说：**AI 让好实践的缺失变得肉眼可见地危险。** 这可能是第一次，不是因为理想主义，而是因为风险太高，组织不得不好好做工程。

---

## 关键引用汇总

> *"The change we are seeing now is bigger than all of those put together — bigger than the internet, bigger than object orientation, bigger than the agile transformation."*

> *"I can't read 12,000 lines of code carefully enough to feel that I truly understand and own them."*

> *"AI won't replace software engineers, but it will expose the ones who never learned to think like engineers."*

> *"If you're already working well, AI will be a big win. If you're working poorly, you'll just dig a deeper hole faster."*

> *"The stakes are now too high to ignore engineering discipline."*

---

**Source:** [Aviator Podcast: Engineering Discipline in the AI Era with Dave Farley](https://www.aviator.co/podcast/engineering-discipline-dave-farley) · [GOTO 2025: The Most Important Programming Invention In 20 Years](https://devblogs.co/posts/the-most-important-programming-invention-in-20-years-dave-farley-goto-2025) · [LeadDev: Safe production changes with agents](https://leaddev.com/technical-direction/safe-production-changes-with-agents)
