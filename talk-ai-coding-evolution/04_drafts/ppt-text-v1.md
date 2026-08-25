# PPT 文字 v1 · OPC 航海指南：OPC 与 Harness，AI 协作之道（23 页）

> **每页 PPT 的上屏文字**（标题 + 正文），不是讲稿。原则：凝练、抓人、中文表达规范；术语写准，
> 英文术语保留原文（见文末术语对照）。对应现场版 `../03_outline/00-page-structure-23.md` P1–P23。

---

### P1 · 封面

**OPC 航海指南**

OPC 与 Harness，AI 协作之道

> 一个人，AI Coding 要掌握到多深？

---

### P2 · 钩子

**你的角色，两年换了五任**

- 2024 说话者：打磨 prompt
- 2025 策展者：审代码、喂 context
- 2026 环境工程师 → 控制流作者 → 编排者

> "I don't prompt Claude anymore. My job is to write loops." —— Boris Cherny

你不是在追新工具，你是在被模型往上推。

---

### P3 · 路线图

**今天四站**

1. 五层演变——注意力一层层上移
2. 根本还是 harness
3. 固定 vs 灵活——你该怎么选
4. DSH——一个把灵活性交给你的 harness

---

### P4 · 发动机

**一个原因，五层结果**

- METR：50% 可靠性任务长度 ≈ 每 7 个月翻倍
- "prompt 的精确措辞，越来越不重要" —— Anthropic
- 杠杆点上移：说什么 → 看什么 → 在什么系统里跑
- **叠加，不是替代**

---

### P5 · Prompt + Context

**第一二层：从"说什么"到"看什么"**

- Prompt 是行为控制面，不是系统本身
- 把系统问题塞进更长 prompt = 把缺失的控制面伪装成提示复杂度
- "The agent has a prompt, a Bash Tool, and an Edit Tool."（最小脚手架）
- Context engineering：决定模型此刻该看到什么
- context rot：**塞得越多，记得越差**
- MCP / RAG：能力到位、注意力上移，才成为焦点

---

### P6 · Harness（埋雷）

**第三层：模型在什么系统里跑**

- **Agent = Model + Harness** —— Böckeler
- harness = 模型之外的一切：权限 / 沙箱 / 工具 / 验证 / trace / CI
- **单次运行容器**：loop 每次迭代实例化一个 harness；graph 每个节点跑在它自己的 harness 里
- ⚠️ 2026 安全事件，集中爆发在这一层

---

### P7 · Loop + Graph

**第四五层：从"重复"到"组织"**

- Loop：何时、为何、以什么条件重复
- 黄金法则：只有上次结果改变下次行动，才算 loop
- "A loop can be wrong in ways that are subtle, expensive, and hard to detect."
- Graph：从个体智能到系统智能
- 两盆冷水：不是新东西（LangGraph 2024）/ 术语先于发布（260 万浏览，无框架发布）
- **叙事期：火六周就被接棒**

---

### P8 · 叠加观 + 成熟度

**五层不是时间线，是一栋楼**

- 叠加，不是换代：学会用扳手，不等于扔掉螺丝刀
- 成熟度标尺：前三层在生产里跑；后两层在叙事期
- 今天重仓 1–3 层
- 五层里，有一层是其他所有层的**承重墙**

---

### P9 · 转折

**五层讲完，根本还是 harness**

- loop 实例化 harness；graph 节点跑在自己的 harness 里
- 上层是楼层，harness 是地基
- 口径：这是我们的判断（报告将 Context 与 Harness 并列）
- 三条线撑：结构 / 哲学 / 风险

---

### P10 · 定义

**Agent = Model + Harness**

- harness = 模型之外的一切：权限、沙箱、工具、验证、trace、CI
- 你以为你在用一个聪明的模型，其实你用"模型 + 一整圈系统"
- 雏形早就在：一个 prompt + 一个 Bash Tool + 一个 Edit Tool

---

### P11 · 两套控制 + 确定/概率

**harness 里头：两套控制，一档分野**

- **Guides**（前馈）：行动前约束——按这个样式 / 必须过 lint / 只能用这些工具
- **Sensors**（反馈）：行动后喂回——测试挂了 / 用户拒绝 / 退出码非零
- **computational**（确定性）：测试 / lint / 类型——可复现，可审计
- **inferential**（概率性）：AI review——意见本身可能错
- 原则：**能交给确定性的，绝不靠概率性的**
- Loop 五级验证梯：同一哲学

---

### P12 · 圈住 / 拦住 / 看清

**三个动词，记住 harness**

- **圈住**：沙箱 + 权限——文件与网络双重隔离（-84% 权限提示）
- **拦住**：验证门禁——错误在离源头最近的地方就地拦下
- **看清**：可观测性 + provenance + CI——trace 记下每一步

> 模型给能力，harness 给可靠性。

---

### P13 · 承重墙

**连上层自己的定义，都承认 harness 在底下**

- "Loop sits one floor above the harness." —— Osmani
- "The harness supplies the engine; loop writes the pilot." —— Macedo
- GraphARC：plan → check → execute——上层自己在长 harness
- **假设下层正确是 bug 的来源；对下层显式验证，是工程成熟的标志**

---

### P14 · 2026 CVE

**反面证据：2026 真实事故**

- AWS / Google / Vercel agent 工具触发漏洞
- 不是 prompt injection：**执行时授权缺失**
- 攻击者伪造工具调用，无需运行模型
- 修复方向：**authorize at execution, not at generation**

---

### P15 · 抉择

**harness 这一格：固定，还是灵活？**

- 不是"自己做 vs 依赖现成"的二选一
- 真正的区别在一条轴：**固定 vs 灵活**
- 精装公寓 vs 可改造空间

---

### P16 · 固定的好

**固定 harness 的价值：组件随产品交付**

- harness 民主化：沙箱 / 权限 / 可观测性，开箱即用
- Claude Code 沙箱双重隔离；Copilot 云端沙箱
- "Start with the simplest viable system." —— Anthropic
- 绝大多数人，应从现成开始

---

### P17 · 固定的卡

**卡住的地方：想改 harness 本身**

- 挂自己的模型 / 工具：厂商支持什么，你才能用什么
- 换后端：沙箱、工具集定死，没有接口
- 挂 skill / knowledge map：只能塞进 prompt（context rot：塞得越多记得越差）
- 补执行时授权？改不了内核，只能等厂商

---

### P18 · 本质

**不是别用现成，是别只能现成**

- 灵活 harness = **装自己的 + 借现成的**
- 装自己的：挂模型 / 挂工具 / 换后端 / 挂 skill / 挂 knowledge map / 自定义门禁
- 借现成的：成熟 adapter / skill / 模型，直接复用
- 不逼你二选一

---

### P19 · DSH

**DSH：能改 harness 本身的 harness**

- "No privileged core to patch: extend by mounting a plugin beside the others."
- 不给你写死的 harness，给你能改它的框架
- 接口标准化：装自己的，借现成的

---

### P20 · 双向灵活

**装自己的，借现成的（DSH 的实现）**

- 挂模型：`ctx.llm` 注册 adapter——协议兼容纯配置
- 挂工具：`ctx.tools` 注册——schema 自动进模型可见面
- 换后端：capability seam——Definition / Provider / Consumer
- 挂 skill / knowledge map："Each fact has one home"
- 加模型、加工具，**都不必改 loop**
- 借现成：15 行 YAML 挂一个新 vendor

---

### P21 · 哲学

**规则，要由机器执行**

- "Agents follow enforced gates far more reliably than prose conventions."
- GraphARC 同套：确定性 checker 放行或拒绝
- 你自己定义门禁，机器替你执行
- **不靠自律，靠系统**

---

### P22 · 回答 + slogan

**一人公司，掌握到 harness 这一层**

- 五种角色，一人承担（责任叠加上移，不是岗位替代）
- 不用从零造，但要能改
- 灵活 harness，自动罩住 loop / graph
- **装自己的，借现成的**

---

### P23 · Q&A

**Q&A**

- Loop / Graph 是炒作吗？—— 叙事期，重心在成熟三层
- 现成 harness 何时够用？—— 卡在自己知识、流程、门禁进不去时
- DSH 怎么上手？—— 从挂 vendor / 工具 / knowledge map 开始

---

## 术语对照（PPT 上保留英文的术语）

| 英文（上屏） | 中文表达参考（口播可讲） |
|---|---|
| prompt / context / harness / loop / graph engineering | 提示 / 上下文 / 围栏（harness 建议直接保留）/ 循环 / 图 工程 |
| Agent = Model + Harness | 不译，公式上屏 |
| context rot | 上下文腐烂（不译，保留英文） |
| Guides / Sensors | 引导 / 感知（标注英文） |
| computational / inferential | 确定性 / 概率性（标注英文） |
| authorize at execution, not at generation | 执行时授权，而非生成时授权 |
| capability seam | 能力接缝（标注英文） |
| adapter / vendor | 适配器 / 供应商（标注英文） |
| provenance / trace | 溯源 / 链路（标注英文） |
| MCP / RAG / CI / AGENTS.md | 保留英文 |
| sandbox | 沙箱（通用译法） |
| "Each fact has one home" | 每个事实只有一个家（金句，双语） |
