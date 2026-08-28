# 第四幕：DSH 的定位与 Harness 最终控制权（v1.6）

> DSH 是“可组合 Harness”的实例，不是插件商店、Loop 或 Graph 的替代品。它的价值在于把运行时合同、能力实现、规则与记录显式化，让 owner 把最终控制权留在自己手里。

## P19 DSH 不是插件商店；它是一套可组合的 Harness runtime（1 min）

**上屏**：模型 / 工具 / 执行后端 / 规则与 Loop → 共同合同 → append-only session log。

**定义**：DSH 是一套可组合的 Harness runtime：模型、工具、能力后端、规则与 loop 都能围绕同一套合同装配；每一次发生的行动仍进入 append-only session log。

**讲点**：默认 loop 只是其中一个驱动插件，不是整个系统。插件爆发发生在这套运行时之上：它让不同能力能被装进同一棵树，但它并不把 DSH 降格为插件目录。

## P20 插件进入执行链后，真正的问题变成：谁说了算？（2.5 min）

**上屏**：
- **接入**：谁允许它进来？· registry。
- **替换**：谁能换实现？· adapter + seam。
- **放行**：谁在执行前签字？· gate。
- **重建事实**：谁能还原事实？· session log。

**讲点**：四问不是插件功能清单，而是运行边界的责任清单。固定产品的公开合同决定你能改变什么；但当插件进入真实执行路径，owner 面对的是谁对合同、权限、门禁和记录负责。如果答案永远是厂商或插件作者，边界就不在你手里。

## P21 Harness 在手：关键时刻 owner 有 final say（1.5 min）

**上屏**：部件继续借；owner 决定什么进入、什么可换、什么能执行、事实如何留下。

**机制证明**：registry 管接入；adapter + capability seam 管替换；enforced gate 管放行；append-only session log 支持重建事实。

**讲点**：这不是“所有东西都自己写”。模型、工具、后端、插件都可以借；但 owner 必须拥有最后决定权：接什么、换什么、何时执行、如何复盘。“四项决定权”是本 talk 对“在手”的定义。部件可借，决定权不能外包。

## P22 回答封面：OPC 要掌握到 Harness 这一层（2 min）

**上屏**：
- **会用成熟 Harness**：常见任务，直接借现成。
- **看懂运行边界**：权限、门禁、验证与记录。
- **需要时握住 final say**：差异化进入执行链，自己决定四件事。
- **带走句**：部件可借，边界自己定。

**讲点**：回扣封面。掌握深度不按工具数量算，而按对运行边界的责任算。掌握到 Harness 层不是要求所有人编写框架，而是知道何时借、何时改、何时必须自己决定。

## P23 收尾（1 min）

**上屏**：谢谢；Ethan Jiang；部件可借，边界自己定。

**讲点**：一人公司的答案不是囤积工具，而是在该借力时借力、在运行边界成为竞争力时拥有改变它的能力。

## 来源与口径

- P19：`../_reference/rawdata_dsh-digested/system/00-map.md` 与 FAQ 01。
- P20：`../_reference/rawdata_dsh-plugin-seam-maturity/answer.md`、FAQ 08、`../_reference/rawdata_dsh-digested/tools-prompt-llm/00-map.md`、`capability-seams/00-map.md`、`session-and-loop/00-map.md`。
- P21：FAQ 07 / FAQ 08；"最终控制权"为本 talk 的解释性结论，非源码原话。
- P22：`../_reference/rawdata_ai-coding-evolution-final/final_v4/06-five-layer-forward.md`。
