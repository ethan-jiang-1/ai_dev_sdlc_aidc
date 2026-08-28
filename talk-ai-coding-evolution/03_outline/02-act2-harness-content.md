# 第二幕：为什么答案停在 Harness（v1.7）

> 这一幕不是宣称 Harness “最高”，而是证明：每一次真实动作都必须先有可靠运行边界。六页各自承担一次推理，不能重复喊口号。

## P9 Loop / Graph 会放大结果，不会补上缺失的执行边界（1 min）

**上屏**：上层提出下一步 -> Harness 授权、检查、执行 -> 结果进入下一轮 / 下一节点。

**讲点**：P8 已说明 Loop 与 Graph 都建立在可执行节点之上。每个节点最终都落到一次真实执行，上层不会自动修复底层缺口。Loop / Graph 越强，每个节点越要先独立授权、检查、记录；所以问题重新回到 Harness。报告将 Context 与 Harness 并列为成熟主体，这一步是本 talk 的推断，不是假借报告结论。

## P10 模型决定能力上限，Harness 决定交付底线（1.5 min）

**上屏**：能力上限 = Model；交付底线 = Harness；权限清楚 / 环境隔离 / 工具受控 / 结果可验 / 过程可追 / 失败即停。

**讲点**：Harness 不替模型思考，它把可靠性变成可执行、可检查的系统行为。同一个模型，换一圈 Harness，就是两套交付系统。

## P11 Harness 同时在行动前引导、行动后反馈（3 min）

**上屏（两层关系）**：
- Guides：行动前的前馈约束。
- Sensors：行动后的反馈信号。
- Computational：测试、lint、类型、schema；Inferential：AI review、人工判断。

**讲点**：以“教小孩做菜”说明：先说规则，再尝结果。原则是把能确定检查的事情交给确定性系统；模型和人判断留给真正需要语义判断的部分。Loop 的验证并非另一套哲学，而是把这条原则跨运行延续。

## P12 Harness 先保证可靠，再承载专业知识（2.5 min）

**上屏**：
- 圈住：沙箱、权限、执行边界。
- 拦住：工具协议与验证门禁。
- 看清：trace、provenance、CI。
- 第二层专业知识：Knowledge Map，把事实归属、正确路径与项目地图放进可靠边界。

**讲点**：前三项是一条可靠性交付链：先限制伤害范围，再在错误靠近源头时拦下，最后能还原每次决策与产物来源。Knowledge Map 不是第四项并列控制，而是下一层承载的专业知识。

## P13 模型可以提议下一步；执行端必须独立决定放行（1 min）

**上屏**：
- **提议**：模型 / Loop / Graph 给出下一步动作。
- **检查**：权限 + 确定性门禁独立判断。
- **执行**：放行 / 拒绝并留下记录。

**讲点**：Loop / Graph 负责安排下一步，Harness 决定这一步能不能发生。GraphARC 的 `plan -> check -> execute` 说明模型可以提议工作图，但确定性检查器决定放行或拒绝。**提议权可以交给模型；执行权必须留在 Harness。**下一页用真实事故说明为什么执行许可不能留给生成侧。

## P14 2026 的教训：在生成时相信模型，不等于在执行时授权（1 min）

**上屏**：
1. 工具调用形状的数据被伪造或绕过模型回合。
2. 若执行端只相信“这像一次合法模型调用”，独立授权就缺失。
3. 工具动作仍会发生。
4. 修复：`authorize at execution, not at generation`。

**讲点**：这不是 prompt injection 故事，也不是 CVE 编号表。它说明授权必须在真正执行工具的位置再次判断；generation 侧的提示、审批、模型判断都不能替代执行端授权。结尾焊接下一幕：边界必须有人负责，但这不等于每个 OPC 都要自己造 Harness。

## 来源与口径

- P9、P13：`../_reference/rawdata_ai-coding-evolution-final/final_v4/04-2026-loop-era.md`、`05-2026-graph-era.md`、`06-five-layer-forward.md`。
- P10、P11、P14：`03-2026-harness-era.md`。
- P12：`../01_storyline/06-harness-internals.md`；`../_reference/rawdata_dsh-faq-on-digested/07_borrowing-harness-idea/answer.md`。
- P13 的 GraphARC 只作为“确定性门禁向上层延伸”的例子，不等同于 Graph 已成熟的证据。
