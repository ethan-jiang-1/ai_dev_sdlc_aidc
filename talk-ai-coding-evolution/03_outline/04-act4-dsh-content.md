# 第四幕 DSH + 收尾 —— 逐页内容（现场 P19–P23）

> 对应 `00-page-structure-23.md` P19–P23（5 + 2 min）。内部小节编号是素材锚点。素材来源见 `../02_evidence/00-absorption-plan.md` 第二节。
> 每页：目的 / 讲点 / 金句 / 通俗例子 / 转场。

---

## S22 DSH（1 min）—— 一个灵活的 harness，能改 harness 本身

- **目的**：引入 DSH 作为"灵活 harness"的答案，立住"能改 harness 本身"。
- **讲点**：
  1. DSH（DeepSeek Harness）——一个把"灵活性"当第一原则的 harness。
  2. 它的架构哲学一句话：**"There is no privileged core to patch: you extend dsh by mounting a plugin beside the others."**——没有特权内核，扩展 = 在旁边挂一个插件。
  3. 换句话说：它不给你写死的 harness，它给你**能改 harness 本身的框架**。
  4. 通俗：精装公寓 vs 能改格局的空间——DSH 是后者，而且接口是标准化的。
- **转场**：那"灵活"具体长什么样？两句话：装自己的、借现成的。

---

## S23 双向灵活（2.5 min）—— 装自己的 + 借现成的

- **目的**：用 DSH 的真实机制证明"装自己的 + 借现成的"两条腿都实（这里不讲 MCP——DSH 不用 MCP）。
- **讲点**：
  1. **装自己的**——四样机制（源码里都有）：
     - **挂模型**：在 `ctx.llm` 注册 adapter（vendor / adapter 四档梯子：协议兼容的纯配置、不兼容的写个小 adapter）；
     - **挂工具**：在 `ctx.tools` 注册，schema 自动进模型可见面；
     - **换后端**：capability seam（Definition / Provider / Consumer 三角色——换 fs / subprocess 后端，Consumer 不用改）；
     - **挂 skill / 挂 knowledge map**：过程性记忆按需加载；项目地图作为一等对象（"Each fact has one home: the tier whose job it is; elsewhere, link there."）。
     - 金句：加模型、加工具，**"都不必改 loop"**。
  2. **借现成的**——vendor adapter：**15 行 YAML 挂一个新 vendor**，协议兼容的纯配置搞定。行业里成熟的东西（你选定的模型、现成的工具）直接复用。
  3. 收束：这不就是"装自己的，借现成的"吗？DSH 就是这句话的实现。
- **转场**：最后一句哲学，是 DSH 整个设计的魂。

---

## S24 哲学（1.5 min）—— 可执行门禁，不靠自觉

- **目的**：落在"可执行门禁"哲学上——规则要由机器执行，不是靠自觉。
- **讲点**：
  1. DSH 的核心哲学：**"Agents follow enforced gates far more reliably than prose conventions."**——agent 会可靠地遵守被强制执行的关卡，而不是写在 prose 里的约定。
  2. 这不是 DSH 一家之言——Graph 层最前沿的 GraphARC 也是同一套：模型提议工作图，**确定性 checker 放行或拒绝**，只有被放行的才执行。
  3. 这就是第二幕讲的"确定性优先"在一个真实 harness 里的样子：**你自己定义门禁，机器替你执行**。
  4. 对一人公司：你项目的规则（哪里该改、什么不能做、什么算完成）可以变成机器执行的关卡——不靠自律，靠系统。
- **转场**：所以，回到最开始那个问题。

---

## S25 回答（1.5 min）—— 一人公司要掌握到 harness 层，不用从零造，但要能改

- **目的**：回到一人公司主题，给出答案。
- **讲点**：
  1. 回顾角色表：一个成熟团队要五种角色（prompt 设计师 → context 平台 → harness SRE → loop 设计师 → graph 架构师），一人公司就是"**被同一个人承担**"的极端情况。
  2. 答案：你要掌握到 **harness 这一层**——不用从零造，但要能改。
  3. 为什么：harness 是承重墙（第二幕）；而且**一个灵活的 harness 自动罩住上面两层**——loop 每次迭代实例化 harness、graph 节点跑在自己的 harness 里，harness 灵活了，loop / graph 也跟着灵活。
  4. 怎么选：从现成开始，但别停在"只能现成"——给自己留一个**能改 harness 本身**的选项。
- **转场**：收尾。

---

## S26 带走一句（1 min）—— 装自己的，借现成的

- **目的**：一句话让听众带走。
- **讲点**：
  1. **装自己的，借现成的。**
  2. 展开：你的知识、你的流程、你的门禁，能进去；行业里成熟的东西，也借得上。
  3. 这就是一人公司掌握 AI Coding 该到的深度——**harness 这一层：能改，也能接**。
- **转场**：Q&A。

---

## S27 Q&A（0.5 min）

- 预埋可问点：
  - Loop / Graph 到底是不是炒作？（答：是叙事期，重心在成熟层）
  - 现成 harness 什么时候够用？（答：常见任务够用；卡在你自己的知识/流程/门禁进不去时）
  - DSH 怎么上手？（答：挂 vendor / 挂工具 / 挂 knowledge map，见 docs/cookbook）

---

## 本幕素材来源速查

- S22 无特权内核：FAQ `01_repository-organization` / `docs/architecture.md`
- S23 挂模型 / 挂工具 / 都不必改 loop：`rawdata_dsh-digested/tools-prompt-llm/00-map.md`
- S23 换后端：`rawdata_dsh-digested/capability-seams/00-map.md`
- S23 vendor 15 行 YAML：FAQ `03_model-vendors`
- S23 "Each fact has one home"：FAQ `04_root-entry-doc-design`
- S24 门禁哲学：FAQ `07_borrowing-harness-idea` + `final_v4/05-2026-graph-era.md`（GraphARC）
- S25 角色表：`final_v4/06-five-layer-forward.md`
