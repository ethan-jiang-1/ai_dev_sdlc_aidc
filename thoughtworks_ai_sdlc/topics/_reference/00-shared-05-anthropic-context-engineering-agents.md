# W0-05 Anthropic: Effective Context Engineering for AI Agents

- source_url: `https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents`
- source_type: `official engineering article`
- authority_level: `primary practitioner guidance`
- publication_time: `2025`
- accessed_on: `2026-04-17`
- applicable_topics: `02 organizational-synergy; 03 agent-native-infrastructure`

## Why This Source Matters

如果 Topic 03 想讨论 Agent OS、工作账本、记忆与知识层，Topic 02 想讨论 middle loop 的上下文打包与监督，那么这篇文章几乎就是共同底座。它把“prompt engineering”升级成“context engineering”。

## Key Facts Captured

- Anthropic 把 context engineering 定义为：在 LLM inference 期间持续维护和筛选最优 token 集的策略。
- 文章强调 context 问题不是单次 prompt 优化，而是 agent 在长时间运行中不断处理增长信息的系统问题。
- 更大 context window 不是万能解；仍会有 `context pollution` 与 relevance 问题。
- Anthropic 给出的关键机制包括：`compaction`、`structured note-taking`、`multi-agent architectures`。
- Claude Code 的做法是压缩关键上下文，保留架构决策、未解 bug、实现细节，并丢弃冗余工具输出。
- 文件型外部 memory 被用来支持跨 session 的知识保留和项目状态延续。

## Research Use

- Topic 02：可直接映射到 middle loop 的工作对象，例如上下文整理、信任校准、handoff 和 checkpoint。
- Topic 03：支撑 memory、ledger、semantic retrieval、sub-agent coordination 等基础设施讨论。
- Wave 2：帮助解释为什么“代码更多”会转化为“认知债务更多”。

## Caveats

- 这是 Anthropic 的产品和实践视角，不是通用标准。
- 它擅长解释 agent memory / context continuity，不直接覆盖风险治理或交付指标。
