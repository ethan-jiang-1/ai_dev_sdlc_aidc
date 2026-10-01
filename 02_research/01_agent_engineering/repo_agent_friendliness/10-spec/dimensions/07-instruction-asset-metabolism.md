# 维度 07 · 指令资产新陈代谢

> 角色：加权维。**v1.1 新增维**。形态适用：A+B，**B 下含义加深**（harness 自身的退役机制，见 §形态 B 子族）。

## 核心问题

Agent 指引资产（指令文件、skills、agent 文档）是否保鲜，有没有打扫机制？

## 为什么独立成维

"上下文腐化"在 2026-06 后的社区用法里有两个含义，必须拆开（同词异义纪律）：**(a) 注意力稀释**（context rot 原义，token 越多越退化）是维度 01 的理论依据；**(b) 指令资产腐化**——过期规则、互相矛盾的沉淀层、无人删除的死指引本身成为 distractor——已被列为正式反模式（[Stale AI Configuration Artifacts](https://raw.githubusercontent.com/agentpatterns-ai/website/refs/heads/main/patterns/anti-patterns/stale-ai-configuration-artifacts.md)）。(b) 加上其解法"定期打扫"（T4：[Anthropic session/compaction 工程化](https://claude.com/blog/using-claude-code-session-management-and-1m-context)、/doctor 式修剪政策），构成一个自足的问题域：**指引资产的生命周期治理**。

## 边界声明

- 归此维：**指引资产自身**的新鲜度与打扫——过期内容检测、矛盾沉淀层清理、修剪政策成文、文档更新政策、清扫节奏/责任人、上下文坟场预防（技能/规则/过期定义堆积）。
- 归他维：指引描述的行为与实现不一致 → **归 08**。分界口诀：⑦管"文件旧了没人删"，⑧管"文件还新、但说的和代码做的已经是两回事"。一个典型的仓库问题要问一句：这条坏指引的问题是**没人维护它**（⑦）还是**维护了但对象错了**（⑧）？
- 会话内的 compaction/记忆管理是 harness 能力（L-profile 层），仓库侧只收"为会话卫生提供的仓库级配合"（如指引短到不依赖压缩）。

## 判据族（草案）

1. **新鲜度可检测**：指引文件有最后校验标记或 staleness 检查手段；过期内容可被机器/流程发现。
2. **修剪政策**：有成文的修剪标准（删什么、留什么——pitfalls/rationale 留、可推导内容删）；有 /doctor 式的清理入口或定期执行记录。
3. **更新政策**：行为变更必须同变更集更新指引的规则成文且有例证（git log 可查）。
4. **坟场预防**：无堆积的废弃规则/注释掉的指令/多代并存的指南；一处行为只有一条现行规则。
5. **规模自律**：指引总量随仓库增长有预算意识（不是只增不减）。
6. **打扫节奏**：定期 review 有节奏与责任人（成文即可，不要求工具化）。

## 形态 B 子族（harness 代谢，v1.2）

B 形态下本维从"修剪文档"加深为"harness 自身的退役机制"：

1. **假设检验**：harness 的每个组件都编码了一个"模型做不到 X"的假设；模型升级后这些假设会过期——须定期逐组件压力测试、裁撤冗余（Anthropic 实测：模型升级后 Sprint 机制整体可移除；"harness 设计空间随模型变强而移动，不是缩小"）。
2. **清理速度 ≥ 生成速度**：熵治理判据——低质量产物、矛盾指令、死亡状态引用的清理须与生成同速（OpenAI：后台 agent 定期扫描并自动提清理 PR）。
3. **保留/丢弃分离**：状态蒸馏时保留决策结论与理由，丢弃推理过程与过期临时状态。

## 依据

- [Stale AI Configuration Artifacts (Context Rot)](https://raw.githubusercontent.com/agentpatterns-ai/website/refs/heads/main/patterns/anti-patterns/stale-ai-configuration-artifacts.md)（反模式化，2026）。
- [Anthropic: Using Claude Code — session management](https://claude.com/blog/using-claude-code-session-management-and-1m-context)（2026：session/compaction/记忆管理工程化）。
- raw 01 §2（/doctor 修剪标准）、raw 02 §4.1 原则 1（"技能/规则/prompt 片段的坟场"警告）。
- raw 90 篇（[90-audit-checklist.md](../../90-archive/raw/90-audit-checklist.md)）#6/#15/#46（矛盾、活文档、同源政策——v1.1 起划入本维）。

## 泛化注意

- raw #15/#46 原在维度①④，v1.1 归此维；checklist-A/B 落条时在**对应条目**上标注 raw 编号溯源（raw 已冻结只读，不在其原编号处回写）。

## 开放问题

- "最后校验标记"会不会本身变成新的腐化源（标记过期但没人看）？——判据需配"标记被消费"的机制要求。
- 与 08 的分界在"文档与代码同源"上最薄：checklist 落条时逐条标注归侧。
