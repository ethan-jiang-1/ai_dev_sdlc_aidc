---
type: kol_deep_dive
person: Kief Morris
organization: Independent (IaC pioneer)
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html
  - https://lucaberton.com/blog/kief-morris-human-on-the-loop-platformcon-london-2026/
  - https://techleadjournal.dev/episodes/227
  - https://www.infoq.com/news/2026/03/mf-aiassisted-dev/
  - https://kief.com
key_concepts:
  - in_the_loop_to_on_the_loop
  - agentic_flywheel
  - infrastructure_as_code
---
# Kief Morris — "不要修产物，修 Harness"

> ThoughtWorks Distinguished Engineer（15 年），O'Reilly *Infrastructure as Code* 三版作者。在 Martin Fowler 网站发表 *Humans and Agents in Software Engineering Loops* (2026/03)——"in the loop → on the loop" 框架已被 Böckeler、Fowler、Lopopolo 广泛引用。PlatformCon 2026 主题演讲嘉宾。

---

## 人物背景

Morris 的故事比大多数 KOL 更有"实战感"：

- **田纳西出身**——[kief.com](https://kief.com) 自述"Originally from Tennessee"，已在伦敦生活近 30 年
- **互联网泡沫时期搬到伦敦**——此后与妻子、儿子和猫一直住在那里
- **加入 ThoughtWorks 约 15 年**——从 Cloud Practice Lead 到 Distinguished Engineer，历任 Developer、SysAdmin、R&D Manager、Technical Architect、Director of Cloud Engineering
- **个人站点**: [kief.com](https://kief.com) · IaC 站点: [infrastructure-as-code.com](https://infrastructure-as-code.com)

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。

## IaC 到 AI Harness——独特的桥梁视角

Morris 是极少数**同时拥有深厚基础设施自动化和 AI 编码 Agent 经验**的人。他的 *Infrastructure as Code* 第三版恰好于 2025 年 3 月出版——正是 Claude Code 发布、agentic coding 开始炸裂的时间点。

这个时间巧合让 Morris 成为**最早注意到 AI Agent 讨论在重复 IaC 教训的人**：

> *"Much of the current agentic-AI conversation is repeating lessons Infrastructure as Code already learned about treating operational systems as engineered artifacts."*

### IaC 的核心教训 → AI Harness 的直接映射

| IaC 教训 | AI Harness 映射 |
|---------|---------------|
| "基础设施即代码，不是即脚本"——手动 SSH 改配置是反模式 | "Harness 即工程产物，不是即 prompt"——手动 tweak prompt 是反模式 |
| 声明式 > 命令式——定义**期望状态**而非执行步骤 | Spec + Tests = Agent 的不可变期望状态 |
| 不可变基础设施——不修运行中的服务器，重建 | 不修 Agent 的 bug——修产生 bug 的 Harness，让 Agent 重新生成 |
| 平台工程——将专家知识嵌入可复用组件 | Harness = 将工程判断嵌入可复用约束 |

---

## AI 在 IaC 中的定位——Morris 的谨慎立场 (2025)

在被 Agent 编码 hype 席卷之前的 2025 年中，Morris 对 AI + 基础设施做出了一个极为冷静的判断：

> *"I don't think you wanna vibe code your infrastructure. You need to understand what's going on there."* — Tech Lead Journal #227

| Morris 对 AI + IaC 的立场 | 细节 |
|--------------------------|------|
| **GenAI 用于基础设施代码生成** | 尚不可信。最佳角色是**学习助手**，而非直接作者 |
| **"AI-Assisted ClickOps"** | 真实危险——从简单 prompt 直接 provisioning 资源，破坏一致性、可重复性、透明性和治理 |
| **AI 的最佳角色** | **教练/向导**——当开发者需要数据库时，AI 问：什么数据？合规要求（PII）？持久性？事务性？引导到经过验证的预构建平台组件 |
| **5 年预测** | AI 帮助团队**精确定义基础设施需求**（数据敏感度、连接规则），产出**持久化、确定性的规范** |

这个谨慎立场的重要性在于：**一个写了三版 IaC 书的人对 AI 生成代码的怀疑，不是出于恐惧——而是出于 20 年自动化经验。**

---

## 核心理念："Why Loop" vs "How Loop"

Morris 在 2026/03/04 的文章中提出了比 Böckeler/Fowler 更基础的一个区分：

| 循环 | 内容 | 执行者 | 为什么 |
|------|------|--------|--------|
| **Why Loop（目标循环）** | 把想法通过迭代变成可工作的软件——决定**做什么** | **人类**——只有人关心结果 | 不可外包 |
| **How Loop（执行循环）** | 创建、选择、使用中间产物——决定**怎么做** | **AI Agent**——在 Harness 内运行 | 可自动化 |

关键是：**Why Loop 永远是人类领域。** AI 可以帮你决定"怎么做"，但只有你知道"为什么"。这与 Andrew Ng 的 "context advantage"（人类相对 AI 拥有上下文优势）完全收敛——两人从完全不同的路径得出了完全相同的结论。

---

## "In / On / Out of the Loop"——三层框架

这是 Morris 最著名的贡献（已被 Böckeler、Fowler、Lopopolo 广泛引用）：

| 模式 | 人在做什么 | Agent 在做什么 | 风险 |
|------|-----------|---------------|------|
| **Out of the loop** (环外) | 只定义 "Why" | 运行整个 "How" | Vibe Coding 的陷阱：表面能用，内部质量糟糕 |
| **In the loop** (环内) | 审查每一行代码 | 生成代码给人审 | 人类成为瓶颈——规模化时退化到橡皮图章模式 |
| **On the loop** (环上) ✅ | 构建和维护 **Harness** | 在 Harness 内自主运行 | 当前最佳切入点 |

### 最核心的区分：

> *"When an agent produces unsatisfactory results, the 'in the loop' approach fixes the artifact. The 'on the loop' approach fixes the harness that produced it."*

**Agent 产出不行 → 环内思维修那个产出。环上思维修产生那个产出的系统。**

---

## Harness 的复合机制——PlatformCon 2026 的实操细节

Morris 在 PlatformCon London 2026 的演讲中（被 Luca Berton 详尽记录）给出了比文章更具体的操作指南：

### 被拒绝的 PR → Harness 改进的闭环

```
被拒绝的 PR
    ↓
生成分类记录（什么失败了、为什么、修了什么）
    ↓
每周 30 分钟 Harness Retro
    ↓
问："我们能不能加一个 Guide 来预防这个？"
    ↓
新的 Guide / Skill / Gate / Test → 提交到 Harness
    ↓
同类失败不会再出现
```

> 失败的门控变成 CLAUDE.md 更新；被拒的 PR 变成新测试。**Harness 是复合增长的。**

### Harness Retro 的三个问题

1. **有什么模式？**——这周哪些失败反复出现？
2. **为什么 Harness 没抓到？**——是缺 Guide 还是 Sensor 不够敏感？
3. **能不能自动化？**——能不能加一个确定性检查？

---

## Agentic Flywheel——超越静态 Harness

Morris 描述了 Harness Engineering 的下一个阶段：**Agent 管理并改进 Harness 本身。**

```
信号（测试、生产数据、用户日志、业务结果）
        ↓
Agent 审查结果 → 推荐 Harness 改进
        ↓
按风险、成本、收益打分
        ↓
高置信度推荐 → 自动批准 → 提交到 Harness
        ↓
Harness 成为自进化、可能性反脆弱的系统
```

> *"By engineering the harness we won't just get one-off, 'good enough' solutions — we'll get robust, maybe even anti-fragile systems that continuously improve themselves."*

这与 Lopopolo 的"周五 GC 会议 → 编码回 harness → 同样的反馈永远不需要给两次"完全对应——两者独立得出了相同的结论。

---

## 三层模型在实践中的映射

| Harness 层级 | Lopopolo (OpenAI) | Böckeler (ThoughtWorks) | Morris |
|-------------|-------------------|------------------------|--------|
| **Guides** | AGENTS.md, core-beliefs.md | Feedforward controls | Harness Retro 产物 |
| **Sensors** | CI linter (Codex 生成) | Computational Sensors | 被拒 PR → 分类记录 |
| **Gates** | 分层架构强制 | Completion gates | Harness Retro 三个问题 |
| **Flywheel** | 周五 GC → 编码回 harness | Agentic flywheel (理论) | Agent 自我改进 Harness |

---

## IaC 的终极教训——代码库本身不会因为 Agent 变健康

Morris 在 PlatformCon 2026 的这句话是他整个思想体系最浓缩的表达：

> *"A codebase with weak test coverage, unclear ownership, or no deployment discipline does not get healthier because an agent wrote more of it faster."*

测试覆盖率弱、所有权不清、部署纪律缺失的代码库——不会因为 Agent 更快地往里写了更多代码而变得更健康。

这是从 IaC 到 AI Harness 一以贯之的原则：**自动化不修复糟糕的工程实践——它放大它们。**

DORA 2025 确认了这一点：AI 不修复团队，它放大已经存在的东西。

---

## 关键引用汇总

> *"When an agent produces unsatisfactory results, the 'in the loop' approach fixes the artifact. The 'on the loop' approach fixes the harness that produced it."*

> *"Build the system that builds the software, not just the software."*

> *"A codebase with weak test coverage, unclear ownership, or no deployment discipline does not get healthier because an agent wrote more of it faster."*

> *"I don't think you wanna vibe code your infrastructure. You need to understand what's going on there."*

> *"By engineering the harness we won't just get one-off, 'good enough' solutions — we'll get robust, maybe even anti-fragile systems that continuously improve themselves."*

> *"Much of the current agentic-AI conversation is repeating lessons Infrastructure as Code already learned."*

---

**Source:** [martinfowler.com: Humans and Agents in Software Engineering Loops](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html) (2026/03/04) · [Luca Berton: Kief Morris PlatformCon 2026](https://lucaberton.com/blog/kief-morris-human-on-the-loop-platformcon-london-2026/) · [Terrateam: AI in IaC](https://terrateam.io/blog/ai-infrastructure-kief-morris) (2025/07) · [Tech Lead Journal #227: IaC 3rd Ed](https://techleadjournal.dev/episodes/227) (2025/08) · [tokenless.tech: IaC Evolution](https://tokenless.tech/posts/2025/kief-morris-abby-bangser-infrastructure-as-code-evolution/) (2025/10) · [ThoughtWorks: IaC in 2025 podcast](https://share.snipd.com/episode/0c947153-9a77-494d-8e01-06edf6d1306a) (2025/03) · [InfoQ: Where Do Humans Fit](https://www.infoq.com/news/2026/03/mf-aiassisted-dev/) · [InfoQ China 中文译](https://www.infoq.cn/article/eu4vZqJqSuXv3hsEoIo9) · [kief.com](https://kief.com) · [infrastructure-as-code.com](https://infrastructure-as-code.com)
