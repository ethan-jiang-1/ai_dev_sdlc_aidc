# W1-03 Agent-Native Infrastructure Question List

## Must Answer

- Agent OS 的最小可行组成到底是什么：runtime、memory、tool protocol、agent protocol、telemetry、policy，还是别的分层？
- “工作账本”如果要成立，应该记录哪些实体：任务、授权、预算、技能、工具使用历史、验收标准、失败恢复点？
- `work ledger` 的最小 record set 是否已经可以拆成：run/thread identity、event history、checkpoint state、intermediate writes、step outputs、interrupt boundary、trace spans、owner or specialist lineage？
- 企业级“数字潜意识”更适合 graph substrate、file substrate、mixed retrieval，还是 layered hybrid？
- 多智能体系统什么时候值得上，什么时候应该退回 workflow 或单 agent？
- 什么样的 observability 足以支持 agent debugging、cost governance 和 incident recovery？
- 哪些基础设施组件会先标准化，哪些会长期保持企业内定制？

## High-Value Follow-Ups

- A2A 与 MCP 最终会是互补层，还是会在某些场景上重叠甚至竞争？
- enterprise ontology extraction 的最佳输入面是什么：ticket、postmortem、log、wiki、code graph，还是它们的组合？
- “artifact-first handoff” 是否会成为长时运行 agent 的主流设计模式？
- event-sourcing、checkpointing、memoized step state 这三种 durability pattern 在 agent runtime 中应该如何分工，而不是互相替代？

## Current Gaps

- work ledger 的 primitives 已经补强，但统一融合 authorization、budget、capability 与 audit history 的成熟公开实现仍缺。
- 缺少更多企业级案例来说明如何把 graph substrate 接入生产任务流。
- 缺少更系统的 evidence 说明 multi-agent orchestration 在 coding 领域何时真的优于 workflow。
