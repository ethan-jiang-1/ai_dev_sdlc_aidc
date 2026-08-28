# 第四幕：DSH 的定位与 Harness 最终控制权（v1.5）

> DSH 是“可组合 Harness”的实例，不是插件商店、Loop 或 Graph 的替代品。它的价值在于把运行时合同、能力实现、规则与记录显式化，让 owner 把最终控制权留在自己手里。

## P19 DSH 不是插件商店；它是一套可组合的 Harness runtime（1 min）

**上屏**：模型 / 工具 / 执行后端 / 规则与 Loop → 共同合同 → append-only session log。

**定义**：DSH 是一套可组合的 Harness runtime：模型、工具、能力后端、规则与 loop 都能围绕同一套合同装配；每一次发生的行动仍进入 append-only session log。

**讲点**：默认 loop 只是其中一个驱动插件，不是整个系统。插件爆发发生在这套运行时之上：它让不同能力能被装进同一棵树，但它并不把 DSH 降格为插件目录。

## P20 只有插件不够：能装，还必须能管（2.5 min）

**上屏**：
- **接入**：registry。
- **替换**：adapter + seam。
- **放行**：enforced gate。
- **重建事实**：session log。

**讲点**：固定产品的公开合同决定你能改变什么；但当插件进入模型可见面或真实执行路径，owner 面对的已不是“装不装”的问题，而是“谁对合同、权限、门禁和记录负责”。`installable` 不等于 `trustworthy`，插件化也不等于安全。DSH 的 `ctx.llm`、`ctx.tools` 与 capability seam 给能力明确入口，但必须和执行门禁、会话事实一起理解。

## P21 Harness 必须在手：部件可借，四项决定权不能外包（1.5 min）

**上屏**：最终控制权 = **接入 / 替换 / 放行 / 重建事实**。

**机制证明**：registry 管接入；adapter + capability seam 管替换；enforced gate 管放行；append-only session log 支持重建事实。

**讲点**：这不是“所有东西都自己写”。模型、工具、后端、插件都可以借；但 owner 必须拥有最后决定权：接什么、换什么、何时执行、如何复盘。“四项决定权”是本 talk 对“在手”的定义，不冒充 DSH 官方原话。

## P22 OPC 要掌握到哪一步？先借现成，边界自己定（2 min）

**上屏**：
- **先借现成**：常见任务，复用成熟 Harness。
- **看懂边界**：接入、替换、门禁与日志。
- **差异化再握权**：进入业务执行链时，保有 final say。
- **带走句**：部件可借，边界自己定。

**讲点**：回扣开场。掌握到 Harness 层不是要求所有人编写框架，而是能识别并拥有自己运行合同的最终决定权。Loop 与 Graph 在任务需要时建立在这个可靠底座之上；它们不应被当成今天必须重仓的“更高一层”。

## P23 收尾（1 min）

**上屏**：谢谢；Ethan Jiang；部件可借，边界自己定。

**讲点**：一人公司的答案不是囤积工具，而是在该借力时借力、在运行边界成为竞争力时拥有改变它的能力。

## 来源与口径

- P19：`../_reference/rawdata_dsh-digested/system/00-map.md` 与 FAQ 01。
- P20：`../_reference/rawdata_dsh-plugin-seam-maturity/answer.md`、FAQ 08、`../_reference/rawdata_dsh-digested/tools-prompt-llm/00-map.md`、`capability-seams/00-map.md`、`session-and-loop/00-map.md`。
- P21：FAQ 07 / FAQ 08；"最终控制权"为本 talk 的解释性结论，非源码原话。
- P22：`../_reference/rawdata_ai-coding-evolution-final/final_v4/06-five-layer-forward.md`。
