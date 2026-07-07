---
type: concept_deep_dive
event: Future of Software Development Retreat (Deer Valley)
concept: The Supervisory Programmer — context switching, cognitive load, and managing agents
date: 2026-02
verification_status: verified
source_urls:
  - https://mgks.dev/blog/2026-02-17-the-supervisory-programmer-managing-agents-context-switching-and-cognitive-debt/
  - https://martinfowler.com/bliki/FutureOfSoftwareDevelopment.html
key_concepts:
  - supervisory_programmer
  - context_switching_burnout
  - agent_management_cognitive_load
  - ide_orchestration
  - addictive_but_exhausting
---

# The Supervisory Programmer — 管理 Agent 的日常现实

> 来源：mgks.dev, [The Supervisory Programmer](https://mgks.dev/blog/2026-02-17-the-supervisory-programmer-managing-agents-context-switching-and-cognitive-debt/) (2026-02-17) — Deer Valley Retreat 的后续深度分析

---

## 新的日常工作是什么样

Deer Valley 参会者描述了一个正在浮现的新角色：**Supervisory Programmer**（监督程序员）。

不是写代码。是**管理多个 AI Agent**——同时进行。

---

## "又累又上瘾"

Deer Valley 上多人独立描述了同一种体验：

> 管理 Agent 是**又累又上瘾**（exhausting and addictive）。

- **累**：同时在多个 Agent 之间切换上下文——每个 Agent 在不同的任务、不同的文件、不同的设计决策上——产生巨大的认知负荷
- **上瘾**：看到 Agent 在推进工作，即使你已经累了也很难停下来——"再让它跑一个任务"

这与 Pragmatic Summit 上 Beck 和 Fowler 的"Agent 倦怠"警告完全一致。

---

## 上下文切换的认知成本

| 传统编程 | Supervisory Programming |
|---|---|
| 一次聚焦一个任务 | 同时监督 3-6 个 Agent |
| 上下文在你自己脑子里 | 上下文分布在多个 Agent session 中 |
| 切换成本 = 重新加载自己的记忆 | 切换成本 = 重新加载 N 个 Agent 各自的进展 |
| 产出 = 你写的代码 | 产出 = 你监督 Agent 写的代码 + 你做判断的决策 |

---

## IDE 的复仇

mgks.dev 提出了一个反直觉的观点：

> **IDE 仍然重要——但角色变了。**

- LLM 不应该"暴力"完成所有事情——它应该**编排 IDE 的确定性工具**（重构、导航、静态分析）
- IDE 工具是**确定性的**——Agent 用它们比用 prompt 更可靠
- 最好的模式：Agent 推理 → 调用 IDE 工具执行 → 验证结果 → 继续推理

---

## 对组织的含义

如果 Supervisory Programming 是未来：
- **招聘标准**：能同时管理多个并行任务、在不确定性中做判断、写清楚 spec
- **工作节奏**：不能 8 小时都在高强度监督——需要设计"断点"和"恢复"
- **工具需求**：Agent session 管理、上下文切换支持、跨 Agent 进度追踪

---

## 关键引用

> *"Several people admitted it's exhausting and addictive — context-switching across multiple agents creates immense cognitive load."* — Deer Valley 观察

> *"LLMs should orchestrate deterministic IDE tools rather than brute-forcing everything."* — mgks.dev
