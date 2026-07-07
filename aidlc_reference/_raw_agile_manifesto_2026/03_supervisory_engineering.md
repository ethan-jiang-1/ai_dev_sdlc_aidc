---
type: concept_deep_dive
event: Future of Software Development Retreat (Deer Valley)
concept: Supervisory Engineering / The Middle Loop
date: 2026-02
verification_status: verified
source_urls:
  - https://www.thoughtworks.com/en-us/about-us/events/the-future-of-software-development
  - https://martinfowler.com/fragments/2026-02-18.html
  - https://annievella.com/posts/finding-comfort-in-the-uncertainty/
  - https://www.railsreviews.com/articles/the-middle-loop
key_concepts:
  - middle_loop
  - supervisory_engineering
  - agent_direction
  - trust_calibration
  - constraint_encoding
related_concepts:
  - harness_engineering
  - agent_experience
---

# Supervisory Engineering — Deer Valley Retreat 浮现的新工种

> 来源：Deer Valley Retreat 中被识别为"准备好进入更广泛行业对话"的概念之一。
> 参考：[ThoughtWorks 活动页](https://www.thoughtworks.com/en-us/about-us/events/the-future-of-software-development) · [The Middle Loop](https://www.railsreviews.com/articles/the-middle-loop) · [Annie Vella 回顾](https://annievella.com/posts/finding-comfort-in-the-uncertainty/)

---

## 什么是 "Middle Loop"？

传统软件开发有两个 loop：

```
Inner Loop（内循环）：写代码 → 构建 → 测试 → 重复
Outer Loop（外循环）：提交 → CI/CD → 部署 → 监控
```

Deer Valley Retreat 识别出了**第三个 loop**——在两者之间：

```
Middle Loop（中间循环）：
  指挥 Agent → 评估 Agent 输出 → 校准信任 → 编码标准 → 定义安全约束
```

这不是写代码，也不是发布管理。这是一个**新类别的工作**。

---

## Supervisory Engineering 的具体内容

| 活动 | 描述 |
|---|---|
| **指挥 Agent** | 给 Agent 分配任务、设定目标、提供上下文 |
| **评估输出** | 判断 Agent 的产出是否达到了质量要求 |
| **校准信任** | 知道什么时候该信任 Agent、什么时候该人工介入 |
| **编码标准** | 把人的品味和工程规范转化为 Agent 可执行的规则 |
| **定义约束** | 划定 Agent 可以安全运行的操作边界 |
| **维护上下文** | 确保 Agent 有理解系统所需的正确信息 |

---

## 与其他概念的关系

- **Harness Engineering**（Ryan Lopopolo/ThoughtWorks）是 Supervisory Engineering 的**工具层**——设计环境、约束、反馈回路
- **Supervisory Engineering** 是 Harness Engineering 的**人的层面**——指挥、判断、校准
- 两者合在一起：**工具 + 人的判断 = Agent 时代的新工程学科**

---

## Annie Vella 的观察

Annie Vella 在 retreat 中专门提出了"supervisory engineering work"作为讨论主题。她的观察：

> 这不是传统意义上的"管理"——管理 Agent 和管理人不一样。Agent 不会倦怠、不需要激励、但会以人类不会的方式系统性失败。这需要一套全新的监督技能。

---

## 关键引用

> *"A new category of work between writing code and release management: directing agents, evaluating their output, calibrating trust, encoding standards, and defining constraints."*
> — Deer Valley Retreat 总结
