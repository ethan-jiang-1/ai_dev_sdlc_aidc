---
type: practical_pattern
event: FOSE Europe (Engelberg)
concept: Daily Agentic Workflow — a 7-step pattern shared by an attendee
date: 2026-07
verification_status: verified
source_urls:
  - https://ubos.tech/news/thoughtworks-future-of-software-development-retreat-highlights-ais-transformative-role/
  - https://www.metasticworld.com/en/insights/thoughtworks-future-of-software-development-retreat-2026
key_concepts:
  - adr_as_persistent_spec
  - agent_task_list
  - overnight_quality_checks
  - explanatory_documentation
---

# 一个 Engelberg 参会者的 7 步日常工作流

> 来源：[UBOS.tech](https://ubos.tech/news/thoughtworks-future-of-software-development-retreat-highlights-ais-transformative-role/) 和 [Metastic World](https://www.metasticworld.com/en/insights/thoughtworks-future-of-software-development-retreat-2026) 引用的 Engelberg 参会者分享

---

## 完整 7 步流程

```
1. 从 Backlog 取一个 Story
       ↓
2. 和 Agent 讨论它
   （探索代码库、理解上下文、提出方案）
       ↓
3. 达成一致后，创建 ADR
   （Architecture Decision Record — 持久化的 spec）
       ↓
4. Agent 生成 Task List
   （拆成 bite-sized 任务，含文件引用和变更理由）
       ↓
5. Agent 执行 Task List
   （每个 task 由新鲜 Agent 实例执行，角色解耦）
       ↓
6. Agent 生成解释性文档
   （Session 结束时，Agent 产出变更总结供人阅读）
       ↓
7. 隔夜运行质量检查
   （Agent 在非工作时间运行完整测试套件、lint、
    安全扫描 → 早上人类看到一份报告）
```

---

## 为什么这个工作流值得关注

1. **ADR 作为持久化 spec** — 不是用后就扔的对话。ADR 进入版本控制，成为 Agent 和人类共享的真相来源。这直接呼应了 Ryan Lopopolo 的"一切推入仓库"

2. **先讨论再执行** — 不是"给 prompt 然后不管"。讨论阶段是人的判断力介入的关键窗口。一旦 ADR 建立，执行就是机械化的（Jesse Vincent 的 "Specs are the thing that matters now"）

3. **隔夜质量检查** — 人类睡觉时 Agent 在跑全套验证。早上人类只需要看报告 + 做决策。与 Mike Krieger 的 "wish Claude good night" 模式完全一致

4. **解释性文档** — Agent 不只是写代码，还要**解释它做了什么**。这解决了 Thariq Shihipar 的"只看 diff 无法理解变更"的问题

---

## 这个工作流与已知模式的对应

| 步骤 | 对应模式 | 来源 |
|---|---|---|
| 和 Agent 讨论 | Blindspot pass + 头脑风暴 | Thariq Shihipar |
| 创建 ADR | Spec 作为核心工件 | Jesse Vincent |
| Agent 生成 Task List | 实现计划（优先呈现决策点） | Thariq Shihipar |
| Agent 执行 | AI Sandwich 中层 | Kieran Klaassen |
| 解释性文档 | 推介与解释文档 | Thariq Shihipar |
| 隔夜质量检查 | Overnight execution | Mike Krieger |

---

## 关键引用

> *"Once agreement is reached, create an ADR as a persistent spec. Generate a task list. Get the agent to complete it. Get agents to generate explanatory documentation. Run overnight quality checks with a report for humans to review in the morning."* — Engelberg 参会者
