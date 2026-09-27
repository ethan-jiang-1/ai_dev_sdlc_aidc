# 当前状态（热区）

> 最近一次更新：**2026-09-27（goal/eval 研究判读的控制接口落地）**：在原有 F/I/07 操作补充上，主干与手册新增三个分流：外部业务结果不可观察时只让可核产出自动停并交人；裁判与人判冲突时暂停自动验收/升档并复核判据；过程通过与外部结果分别记录。来源为 `agent_goal_eval/digested/01/02/03`，单人/单源建议已标注，案例数字不移植为通用阈值；七节主干和 12 节手册仍待用户逐段确认。

## 一句话

**立题初稿仍待用户复核**：backbone §0–§6 七节和 manual 12 节现补有授权演练、停机/产出/结果分账、裁判分歧的暂停与人审；多 feature 工作行只在真实交接问题出现时试行，没有效果对照，不升级为通用规范。量化放行阈值和统一跨 feature 控制面继续开放。

## 状态

| 件 | 状态 |
|---|---|
| `README.md` | ✅ 定位 / 命名理由 / 分工边界 / 信息流 / 核心结论速览 |
| `result/backbone.md` | ✅ §0–§6 七节初版；§1 产出/结果边界、§3 裁判分歧阻断升档、§5 与 `agent_goal_eval` 的接口；原跨 feature 试点和授权路径仍保留——**未经用户逐段确认** |
| `result/README.md` | ✅ 入层判据 |
| `result/manual.md` | ✅ 12 节初版；§2 增终态可观察性分流，§9/§10 增人机裁判分歧处理和外部结果分账；原 §5/§7 授权及交接试点仍保留——**待用户逐节确认** |
| 证据层 | ✅ 循环机制仍见 [`ai_loop_engineering`](../../02_research/ai_loop_engineering/README.md)；本轮控制接口见 [`agent_goal_eval` 判读 01/02/03](../../02_research/agent_goal_eval/digested/README.md)，Hamel/Shankar 分歧处理为单源建议，无前后效果对照 |

## 下一步

1. **用户复核 backbone（§0–§6 七节）＋ manual（12 节）**——建议对照着过（manual 是 backbone 各节的操作化展开）；参照 harness_governance 2026-09-21 的逐段确认流程。
2. 研究层遗留（不阻塞本主题，登记在研究层 CURRENT）：
   - 《Unrolling the Codex agent loop》目前只有检索工具候选摘录，直接访问 openai.com 仍 403；assistant-message 的 turn 终止语义待独立回源，不能当作任务完成规则；
   - `talk-harness-201/02_evidence/01-kol-alignment-2026.md` 的 "Agent = Model + Harness" 归属需按 C 路一手链修正（原创＝Viv Trivedy/LangChain，Böckeler 是传播锚点）；
   - Kief Morris 卡片（`_raw_kol/10`）是三档版，C 路核实实为**四级**（+agentic flywheel），待修订。
3. manual 已成（12 节）——后续增补走「研究层新证据 → backbone 修订 → manual 对应节同步」的信息流。

## 缺口（backbone 登记的两项开放缺口 + 两项附加）

1. **量化自主度分档＝0 一手来源**（backbone §3 登记的开放缺口①）——只能给位置不给刻度；若后续出现轮次判据的一手源，回研究层补档再升主干。
2. **跨 feature 在途可见性**（backbone §2 开放缺口②）——手册 §5 给出受限工作行试点，但已复核材料没有证明统一控制面成型；先观察交接漏项与维护成本，再决定是否推广。
3. **行为面与外部结果仍有盲区**：§4/手册 §10 的删测、越界功能、未解释失败核对不能证明“该做的事都做了”；外部业务结果无观测时保留待人判/待观测，不把产出完成伪装为业务成功。两类操作分流都没有效果对照。
4. DSH 侧的 goal/plan 机制是本主题控制轴的一个**第一方实例候选**（姊妹仓 FAQ 15 的 owner 四仓案例），但那是外部研究——若要引用须走本仓研究层回源流程。

## 铁律速记

- **证据权威在对应研究主题**：循环机制来自 [`ai_loop_engineering`](../../02_research/ai_loop_engineering/README.md)；goal/eval 条件和裁判分歧来自 [`agent_goal_eval`](../../02_research/agent_goal_eval/README.md)。F 的未合并 PR/单用户报告只作反例，I 的个人案例不作效果证据，I2 侦察与 K 候选不入规程；goal/eval 的单人观察与单源 FAQ 不作通用效果结论。
- **result 层语义命名、无序号**；主干结论改动 → 反向同步研究层 digested。
- **未回源的东西不上主干**（`⏳ 待回源` 只能出现在研究层的线索区）。
