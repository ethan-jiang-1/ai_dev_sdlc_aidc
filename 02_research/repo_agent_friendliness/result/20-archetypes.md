# 形态档案（Archetype Profiles）

> 状态：v1.2（2026-09-21）。定义层组件，权威链：[`00-framework-v1.md`](00-framework-v1.md) §3.6 → 本文件。
> 依据为 2026-06 后行业共识（见文末依据），所有内容向其对齐；修改本文件须同步 framework 变更记录。

## 1. 分型依据：产出的应用种类 → 正确性模型

Repo 的目的都是开发某种应用。分型不看"代码由谁写"，看**产出物是什么、靠什么机制判定对错**：

| | 形态 A · 确定性应用 | 形态 B · 智能体（产出以 LLM 为引擎的应用） |
|---|---|---|
| 产出物 | 传统程序（Python/JS/…），确定性运行 | 一个要跑大模型才能干活的智能体，**其自身 harness 是产品本体** |
| 正确性机制 | 二元断言：测试/类型/断言即完整答案 | 统计评估：正确性是系统级、概率性的（"94% 成功率一个场景可用、另一个不可用"） |
| 模型先验 | 充足（通用编程知识成熟），repo 指令的作用是**校准** | 领域行为是新造的，repo 的 harness 资产是智能体**唯一的知识来源**——校准物变成了产品本体 |
| 漂移 | **A/B 共同的敌人**（不定调为分型依据），但守护对象不同：A 守 spec/契约与确定性实现一致（测试/CI 可钉）；B 守行为定义与预期行为一致（behavioral drift，需 evals + 永久看护） | |
| 反馈形式 | 错误表现为"测试红了" | 错误表现为"行为不对"，反馈闭环要靠 evals 人为建造 |
| 成熟度 | **成熟线**：惯例收敛（AGENTS.md、测试闭环），raw 60 条基本即答案；行业空白=棕地改造，正是本体系 A 线的生态位 | **探索线**：惯例未收敛，判据少而关键，标注成熟度，靠试测喂，宁缺毋糊 |

行业对照（引言用）：软件工程 build the system；agentic engineering builds the agentic system that helps build, operate, and evolve the system（[arXiv 2606.28791](https://ar5iv.labs.arxiv.org/html/2606.28791)）。

## 2. 消费路径（B 独有，评估时必须区分）

形态 B 的 repo 资产有**两类读者、两个消费时机**：

- **开发时路径**：coding agent 在开发中读 repo 指引——与形态 A 相同，按九维评（可发现、省 token、可验证）。
- **运行时路径**：**产出的智能体在运行时读自己的 harness 资产**（系统提示、SKILL、工具面）——形态 A 没有这条路径。运行时资产按产品 harness 工程评：注入策略、渐进披露是否产品设计、护栏是否结构性、评估器是否与生成器分离。

混在"产品层"一个词里评是禁止的（正交纪律：同路径异判）。

## 3. 形态档案只做三件事（不改九维定义）

1. **定评估面组合**：A = 开发时路径；B = 开发时路径 + 运行时路径。
2. **定条件判据**：维度⑧等含 A/B 子族（各维文件内标注）；如 A 下未采用 SDD 不惩罚、采用了则漂移守护判据加严。
3. **定成熟度标注**：B 线判据逐条标"共识/探索"，探索级判据不进总分硬约束，进观察项。

## 4. B 形态评估面 ↔ 行业六层 harness 架构映射

（LangChain: Agent = Model + Harness；六层为行业综合，来源见 §6）

| 行业六层 | 本体系维度 | 备注 |
|---|---|---|
| L1 信息边界 | ① 供给与预算、⑦ 新陈代谢 | AGENTS.md 当目录用（OpenAI ~100 行地图式）、40% 利用率阈值 |
| L2 工具系统 | ④ 命名/聚合面、⑤ 攻击面 | 最小权限暴露、强类型参数、幂等 |
| L3 执行编排 | ③ 冷启动、⑥ 恢复 | 分级授权、sprint/合同式编排 |
| L4 记忆状态 | ⑥ 干净重来、⑦ 状态清理 | 记忆外化为文件、context reset ≠ compaction |
| L5 评估观测 | ② 验证与证明 | **评估器与生成器分离**（B 核心判据） |
| L6 约束恢复 | ⑤ 门禁、⑥ 出口 | "无法机械化强制的约束，agent 必偏离"（OpenAI） |

含义：九维框架可整体迁移评估 B 的产品 harness——仓库审计是本体系在 A 场景的特例（"泛化"的验证）。

## 5. B 线三条深化判据（2026-09-21 共识核对产物，细节在各维文件）

1. **harness 代谢（⑦-B）**：harness 每个组件都编码"模型做不到 X"的假设；须定期压力测试、裁撤冗余（Anthropic：模型升级后 Sprint 机制整体可移除）；清理速度须跟上生成速度（OpenAI 自动化清理 PR）。
2. **评估分离（②-B）**：模型自评有系统性乐观偏见；评估器须与生成器分离并单独调严（Anthropic GAN 式架构）；"用 AI 生成的测试验证 AI 生成的代码 = 同一双眼检查作业"（Böckeler）——此题为行业级未解，判据标"探索"。
3. **组合可靠性与重启（⑥-B）**：p^n 衰减（0.95^20≈0.36）使检查点/HITL/干净重启成为结构必需；context reset（清空+交接文件）优于原地 compaction。

## 6. 依据（均为 2026-06 后）

- [From Determinism to Delegation（arXiv 2606.28791，2026-06）](https://ar5iv.labs.arxiv.org/html/2606.28791)：正确性模型三轴、behavioral drift、p^n、TEVV 永久看护。
- [Harness Engineering 综述（2026-04，引 OpenAI / Anthropic / Stripe / Hashimoto / LangChain / Böckeler 一手博客）](https://cloud.tencent.cn/developer/article/2660978)：Agent=Model+Harness、六层架构、40% 阈值、context reset、熵治理、harness 假设定期检验。一手原文：[OpenAI Harness Engineering](https://openai.com/index/harness-engineering/)、[Anthropic Harness Design](https://www.anthropic.com/engineering/harness-design-long-running-apps)、[LangChain Anatomy of an Agent Harness](https://blog.langchain.com/the-anatomy-of-an-agent-harness/)、[Stripe Minions](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)、[Böckeler (Martin Fowler)](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html)、[Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)。
- [AAIF: Code Is Cheap. Proof Is the Bottleneck.（2026-09）](https://aaif.io/blog/code-is-cheap-proof-is-the-bottleneck)：proof 瓶颈、comprehension debt。

## 变更记录

- v1.2（2026-09-21）：初版。A/B 正确性模型分型、消费路径、六层映射、B 线三条深化判据、成熟度标注机制。
