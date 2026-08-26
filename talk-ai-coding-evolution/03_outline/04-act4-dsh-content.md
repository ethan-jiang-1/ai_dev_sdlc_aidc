# 第四幕：DSH 怎样把灵活性做成系统（v1.3）

> DSH 是“可组合 Harness”的实例，不是 Loop 或 Graph 的替代品。它的价值在于把运行时合同、能力实现、规则与记录显式化，让上层组织能力可以建立在可靠边界上。

## P19 DSH 的关键不是“一个更强的 Loop”，而是可组合的 Harness（1 min）

**上屏**：运行时插件树 + 持久事件记录。

**金句**：`There is no privileged core to patch: you extend dsh by mounting a plugin beside the others.`

**讲点**：默认 loop 只是一个实现 Agent 合同的驱动插件，不是整个系统。新的行为优先找到 extension point、capability seam 或组合层；只有改变 loop 合同本身才修改核心驱动。这样“改系统”不等于往核心函数打补丁。

## P20 一项能力要能换，必须把合同、实现和消费者一起设计（2.5 min）

**上屏**：
- 模型：在 `ctx.llm` 注册 adapter。
- 面向模型的能力：在 `ctx.tools` 注册，schema 自动进入模型可见面。
- 可替换后端：Definition -> Provider -> Consumer 的 capability seam。
- 组合：profile / plugin 决定本次实际装入什么。

**讲点**：这四点使“装自己的”变成受合同约束的组合，而不是随意改代码。增加模型或工具不用改默认 loop；兼容协议的 vendor 可以纯配置接入，说明“借现成的”也是一等能力。强调：DSH 原生机制不是 MCP。

## P21 规则写给人看，门禁才负责让系统做对（1.5 min）

**金句**：`Agents follow enforced gates far more reliably than prose conventions.`

**上屏**：可机械判断的承诺 -> 可失败的命令 -> CI / 真实执行路径。

**讲点**：文档负责指出正确道路，机械门禁负责把错误挡在真实路径上。检查还要做负例控制，证明它真的会失败。GraphARC 的 `plan -> check -> execute` 只是这条原则在上层编排中的一个例子。收束：不靠自律，靠系统。

## P22 OPC 不必从零造，但必须读懂并能改变 Harness 边界（2 min）

**上屏**：
- 五个角色，一人承担。
- 默认从现成开始。
- 当差异化需要进入运行边界，拥有可组合的 Harness。
- 装自己的，借现成的。

**讲点**：回扣开场。掌握到 Harness 层不是要求所有人编写框架，而是能识别并改变自己的运行合同。Loop 与 Graph 在任务需要时建立在这个可靠底座之上；它们不应被当成今天必须重仓的“更高一层”。

## P23 收尾（1 min）

**上屏**：谢谢；Ethan Jiang；装自己的，借现成的。

**讲点**：一人公司的答案不是囤积工具，而是在该借力时借力、在运行边界成为竞争力时拥有改变它的能力。

## 来源与口径

- P19：`../_reference/rawdata_dsh-digested/system/00-map.md` 与 FAQ 01。
- P20：`../_reference/rawdata_dsh-digested/tools-prompt-llm/00-map.md`、`capability-seams/00-map.md`、FAQ 03。
- P21：FAQ 07；GraphARC 见 `../_reference/rawdata_ai-coding-evolution-final/final_v4/05-2026-graph-era.md`。
- P22：`../_reference/rawdata_ai-coding-evolution-final/final_v4/06-five-layer-forward.md`。
