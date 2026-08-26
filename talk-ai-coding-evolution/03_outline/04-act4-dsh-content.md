# 第四幕 DSH + 收尾 —— 逐页内容（P19–P23）

> 对应 `00-page-structure-23.md` P19–P23（5 + 2 min）。**每节 = 一页现场内容**：上屏文字（标题/正文）+ 讲点素材。
> 素材来源见 `../02_evidence/00-absorption-plan.md` 第二节。

---

## P19 DSH（1 min）—— 一个灵活的 harness，能改 harness 本身

**上屏文字**
- 标题：DSH：能改 harness 本身的 harness
- 正文：
  - "No privileged core to patch: extend by mounting a plugin beside the others."
  - 不给你写死的 harness，给你能改它的框架
  - 接口标准化：装自己的，借现成的

**讲点 / 素材**
- 目的：引入 DSH 作为"灵活 harness"的答案，立住"能改 harness 本身"。
- 讲点：DSH = 把灵活性当第一原则的 harness；架构哲学（无特权内核，扩展 = 挂插件）；大白话（能改 harness 本身的框架）；通俗（精装公寓 vs 能改格局的空间，接口标准化）。
- 转场：那"灵活"具体长什么样？两句话：装自己的、借现成的。

---

## P20 双向灵活（2.5 min）—— 装自己的 + 借现成的

**上屏文字**
- 标题：装自己的，借现成的（DSH 的实现）
- 正文：
  - 挂模型：`ctx.llm` 注册 adapter——协议兼容纯配置
  - 挂工具：`ctx.tools` 注册——schema 自动进模型可见面
  - 换后端：capability seam——Definition / Provider / Consumer
  - 挂 skill / knowledge map："Each fact has one home"
  - 加模型、加工具，**都不必改 loop**
  - 借现成：15 行 YAML 挂一个新 vendor

**讲点 / 素材**
- 目的：用 DSH 的真实机制证明"装自己的 + 借现成的"两条腿都实（这里不讲 MCP——DSH 不用 MCP）。
- 讲点：装自己的四样机制（挂模型 ctx.llm / 挂工具 ctx.tools / 换后端 capability seam / 挂 skill+knowledge map）；金句"都不必改 loop"；借现成的（15 行 YAML 挂 vendor，协议兼容纯配置）；收束（DSH 就是这句话的实现）。
- 转场：最后一句哲学，是 DSH 整个设计的魂。

---

## P21 哲学（1.5 min）—— 可执行门禁，不靠自觉

**上屏文字**
- 标题：规则，要由机器执行
- 正文：
  - "Agents follow enforced gates far more reliably than prose conventions."
  - GraphARC 同套：确定性 checker 放行或拒绝
  - 你自己定义门禁，机器替你执行
  - **不靠自律，靠系统**

**讲点 / 素材**
- 目的：落在"可执行门禁"哲学上——规则要由机器执行，不是靠自觉。
- 讲点：DSH 核心哲学（enforced gates vs prose conventions）；GraphARC 同套（行业先例）；这就是"确定性优先"的真实样子（自己定义门禁，机器执行）；对一人公司（项目规则变成机器关卡，不靠自律靠系统）。
- 转场：所以，回到最开始那个问题。

---

## P22 回答 + 带走一句（2 min）—— 一人公司要掌握到 harness 层【合并：回答 + slogan】

**上屏文字**
- 标题：一人公司，掌握到 harness 这一层
- 正文：
  - 五种角色，一人承担（责任叠加上移，不是岗位替代）
  - 不用从零造，但要能改
  - 灵活 harness，自动罩住 loop / graph
  - **装自己的，借现成的**

**讲点 / 素材**
- 目的：回到一人公司主题，给出答案并落 slogan。
- 讲点：角色表回扣（五种角色一人承担）；答案（掌握到 harness 层，不用从零造但要能改）；为什么（承重墙 + 灵活 harness 自动罩住 loop/graph）；怎么选（从现成开始，但别停在只能现成）；slogan 落位。
- 转场：谢谢大家。

---

## P23 收尾（1 min）

**上屏文字**
- 标题：谢谢
- 副题：装自己的，借现成的
- 底部一行：[联系方式 / 二维码占位]（用户自填）

**讲点 / 素材**
- 一句话收拢——一人公司，答案在 harness。

---

## 本幕素材来源速查

- P19 无特权内核：FAQ `01_repository-organization` / `docs/architecture.md`
- P20 挂模型 / 挂工具 / 都不必改 loop：`rawdata_dsh-digested/tools-prompt-llm/00-map.md`
- P20 换后端：`rawdata_dsh-digested/capability-seams/00-map.md`
- P20 vendor 15 行 YAML：FAQ `03_model-vendors`
- P20 "Each fact has one home"：FAQ `04_root-entry-doc-design`
- P21 门禁哲学：FAQ `07_borrowing-harness-idea` + `final_v4/05-2026-graph-era.md`（GraphARC）
- P22 角色表：`final_v4/06-five-layer-forward.md`
