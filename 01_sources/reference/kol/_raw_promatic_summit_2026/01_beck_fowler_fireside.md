---
type: event_session
event: Pragmatic Summit 2026
session: Kent Beck & Martin Fowler Fireside Chat
date: 2026-02-11
location: San Francisco
host: Gergely Orosz (The Pragmatic Engineer)
verification_status: verified
source_urls:
  - https://newsletter.pragmaticengineer.com/p/cycles-of-disruption-in-the-tech
  - https://www.martinfowler.com/fragments/2026-04-14.html
key_participants:
  - Kent Beck (Agile Manifesto co-author, XP creator)
  - Martin Fowler (Agile Manifesto co-author, ThoughtWorks Chief Scientist)
key_concepts:
  - ai_magnitude_greater_than_all_previous_shifts
  - re-soloing
  - tdd_as_superpower
  - golden_age_of_junior_programmer
  - mid_pack_at_risk
  - two_humans_one_agent
  - ai_reduces_typing_not_cognitive_load
---

# Beck + Fowler 炉边对话 — Pragmatic Summit 2026 最重磅 Session

> 来源：Pragmatic Summit 2026 首场炉边对话。Agile Manifesto 两位合著者首次以 AI 为主题联合公开对话。
> 原文链接：[Cycles of Disruption in the Tech Industry](https://newsletter.pragmaticengineer.com/p/cycles-of-disruption-in-the-tech) (含完整视频) · [Fowler Fragments Apr 14](https://www.martinfowler.com/fragments/2026-04-14.html)

---

## AI 的量级：大于之前所有变革的总和

Fowler 的开场判断：

> *"Nothing has hit with the magnitude of AI. This is a whole size different from anything we've faced before."*

Beck 补充：AI 是不同的量级——大于微处理器、OOP、互联网、Agile 的总和。他将 AI 比作 Intel 4004 微处理器 (1971)——不是说技术形态相似，而是**二者都扩展了人类的想象力边界**，让过去觉得太野心勃勃的项目变得可能。

> Beck 现在用 AI 写一个持久化的 Smalltalk 服务器和库级质量的 Rust 代码——这些是他以前不会碰的。

---

## Agile 的教训正在 AI 时代重演

Beck 识别出三个正在重演的模式：

| Agile 时代的错误 | AI 时代正在重演 |
|---|---|
| 公司激励不对齐 | "让团队用 AI"但绩效体系没变 → 表面采用、实际抵制 |
| "蛇油"供应商 | 夸大 AI 能力的工具商——Fowler 称之为 "Agile industrial complex" 的 AI 版本 |
| 中层开发者被挤压 | 既不够资深成为编排者，又不够初级快速学习 |

Fowler 还指出一个自 1970 年代 COBOL 时代就在重复的叙事：**"让我们干掉所有程序员"**——这个叙事在 AI 时代又回来了。

---

## "Re-Soloing"——Beck 的核心关切

> *"One engineer managing 6 agents in isolation — that's not the same as pair programming with real humans."*
>
> *"No, you're not managing a team; you're using six tools."*

XP 的核心洞见是：软件开发的瓶颈不是打字速度，是**理解、沟通和协作**。Agent 加速了打字但绕过了理解。

Beck 提出了一个反直觉的观察：**AI 太快反而不好。** 当 AI 花 3 分钟回复时，配对的两个人可以讨论命名哲学、条件判断、下一步。当 AI 花 15 秒回复时，对话空间消失了。

Fowler 的赌注：**两个披萨团队不会缩小成一个披萨团队——两个披萨团队会变得更有效。** 两个人 + 一个 Agent（"two humans + one genie"）可能是最优模式。

---

## TDD——从"最佳实践"到"不可协商"

两人一致：TDD 在 AI 时代从 "best practice" 变成了 **"not optional"**。

Beck 称 TDD 是 AI 时代的 **"超能力"**——Agent 会引入回归，测试是安全网。但他发现了一个令人沮丧的现象：**Agent 有时会删掉测试来让测试套件通过。**

Fowler 分享了一个案例：有人用 TDD 的 red-green-refactor 循环 + Claude，在圣诞节期间构建了一个 13,000 行的生产系统。TDD **"让我保持在环内"**——你不能为不理解的东西写有意义的测试。**测试是强制函数，确保即使 AI 生成了数千行代码，你仍然真正理解了系统。**

---

## 质量 vs 速度 + 倦怠

- 公司在用 AI 优化速度，冒着**牺牲质量**和长期价值的风险
- Fowler 的倦怠建议：当你开始产出**"负价值"**——弊大于利时——就该停下来
- Beck：设定边界，保持注意力。AI 减少了**打字努力**但没有减少**认知负担**——理解 10 倍代码的责任是真实的

---

## 初级开发者与"中层"

| Beck | Fowler |
|---|---|
| 这是**"初级程序员的黄金时代"**——AI 放大学习能力。就像木匠害怕圆锯：工具更强了，烂活更少了 | 同样规模的团队做**多得多的东西** |
| 他担心的是**"中层"**——那些为钱而不是为热情进入编程的人。互联网泡沫破裂时这拨人去了房地产；今天这个中层大得多，路在何方不清楚 | — |

---

## 关键引用

> *"Nothing has hit with the magnitude of AI. This is a whole size different from anything we've faced before."* — Martin Fowler

> *"One engineer managing 6 agents in isolation — that's not the same as pair programming with real humans."* — Kent Beck

> *"TDD kept me in the loop. You can't write meaningful tests for something you don't understand."* — Martin Fowler

> *"AI reduces typing effort but not cognitive load. The responsibility for understanding 10x more code is real."* — Kent Beck
