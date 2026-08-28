# 第二幕：为什么答案停在 Harness（v1.5）

> 这一幕不是宣称 Harness “最高”，而是证明：每一次真实动作都必须先有可靠运行边界。六页各自承担一次推理，不能重复喊口号。

## P9 每一次真实动作，都要经过一个可靠性边界（1 min）

**上屏**：模型提出动作 -> Harness 授权、执行、验证、记录 -> 结果才能进入下一步。

**讲点**：P8 已说明 Loop 与 Graph 都建立在可执行节点之上。这里给出本 talk 的判断：Harness 是最值得 OPC 掌握的临界层，因为每个行动都绕不过它。报告将 Context 与 Harness并列成熟主体，“Harness 最关键”是本 talk 的推断，不是假借报告结论。

## P10 模型买来的是能力，交付可靠性来自 Model + Harness（1.5 min）

**上屏**：`Agent = Model + Harness`；模型之外的一切：工具、权限、沙箱、验证、trace、provenance、CI。

**讲点**：用“一个 prompt + Bash Tool + Edit Tool”的最小脚手架，把大概念落到工程事实：agent 从来都不是裸模型。可靠性是 model-plus-harness 系统的属性。

## P11 Harness 同时在行动前引导、行动后反馈（3 min）

**上屏**：
- Guides：行动前的前馈约束。
- Sensors：行动后的反馈信号。
- Computational：测试、lint、类型、schema；Inferential：AI review、人工判断。

**讲点**：以“教小孩做菜”说明：先说规则，再尝结果。原则是把能确定检查的事情交给确定性系统；模型和人判断留给真正需要语义判断的部分。Loop 的验证并非另一套哲学，而是把这条原则跨运行延续。

## P12 Harness 先保证可靠，再承载专业知识（2.5 min）

**上屏**：
- 圈住：沙箱、权限、执行边界。
- 拦住：工具协议与验证门禁。
- 看清：trace、provenance、CI。
- 专业知识：Knowledge Map，帮助模型找到事实归属与正确路径。

**讲点**：前三项是一条可靠性交付链：先限制伤害范围，再在错误靠近源头时拦下，最后能还原每次决策与产物来源。Knowledge Map 不是第四项可靠性控制，而是在可靠边界之上承载领域地图与正确路径。

## P13 Loop 与 Graph 开始之前，先过确定性门禁（1 min）

**上屏**：
- Loop：跨运行，放大反馈。
- Graph：跨节点，显式路由。
- Harness：执行前，独立授权、检查、记录。

**讲点**：可靠性必须先进入节点，Loop 才能放大，Graph 才能编排。GraphARC 的 `plan -> check -> execute` 说明模型可以提议工作图，但确定性检查器决定放行或拒绝；下一页用真实事故说明为什么执行许可不能留给生成侧。

## P14 2026 的教训：在生成时相信模型，不等于在执行时授权（1 min）

**上屏**：
1. 工具调用形状的数据被伪造或绕过模型回合。
2. 若执行端只相信“这像一次合法模型调用”，独立授权就缺失。
3. 工具动作仍会发生。
4. 修复：`authorize at execution, not at generation`。

**讲点**：这不是 prompt injection 故事，也不是 CVE 编号表。它说明授权必须在真正执行工具的位置再次判断；generation 侧的提示、审批、模型判断都不能替代执行端授权。对 OPC 的意义：安全与可靠性都不是“模型听话”的副产品。

## 来源与口径

- P9、P13：`../_reference/rawdata_ai-coding-evolution-final/final_v4/04-2026-loop-era.md`、`05-2026-graph-era.md`、`06-five-layer-forward.md`。
- P10、P11、P14：`03-2026-harness-era.md`。
- P12：`../01_storyline/06-harness-internals.md`；`../_reference/rawdata_dsh-faq-on-digested/07_borrowing-harness-idea/answer.md`。
- P13 的 GraphARC 只作为“确定性门禁向上层延伸”的例子，不等同于 Graph 已成熟的证据。
