# harness_engineering — 环境、门禁与上下文治理研究

**定位**：围绕 Agent 运行时的外部约束、脚手架（Harness）、门禁校验、传感器与上下文挂载机制的深入研究。
与下游实践层 [`../../../03_practice/harness_governance/`](../../../03_practice/harness_governance/README.md) 呼应。

## 研究主题与核心关注

- **环境轴定义**：约束写进环境（单次运行受控、沙箱隔离、危险指令拦截）。
- **规则执行与不可绕过**：规则如何变成机器级阻断而非 prompt 式建议。
- **与兄弟主题的分工**：
  - 本主题管**空间/环境与单次受控**；
  - [`../loop_engineering/`](../loop_engineering/README.md) 管**时间/多轮迭代与停止条件**；
  - [`../repo_agent_friendliness/`](../repo_agent_friendliness/README.md) 提供**环境友好度的九维评估与度量工具**。
