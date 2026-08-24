# W0-04 Anthropic: Building Effective Agents

- source_url: `https://www.anthropic.com/engineering/building-effective-agents`
- source_type: `official engineering article`
- authority_level: `primary practitioner guidance`
- publication_time: `2024`
- accessed_on: `2026-04-17`
- applicable_topics: `01 engineering-paradigm; 03 agent-native-infrastructure; 04 security-and-governance`

## Why This Source Matters

它不是泛泛而谈“agent 很强”，而是给出一个很务实的判断框架：先用最简单方案，必要时再增加 agentic complexity。这对本轮避免“基础设施愿景过度设计”非常关键。

## Key Facts Captured

- Anthropic 明确区分 `workflows` 与 `agents`：
  - workflows：预定义代码路径编排 LLM 与工具。
  - agents：由 LLM 动态决定过程与工具使用。
- 他们建议先找最简单的可行方案，不必默认构建 agentic systems。
- agentic systems 往往用更高延迟和成本换更高任务表现，因此只有在复杂度确实必要时才值得。
- 文章把 `augmented LLM` 定义为基础构件：`retrieval + tools + memory` 是常见增强能力。
- Anthropic 还把 MCP 点名为一种把工具生态连接进 agent runtime 的可行接口方式。

## Research Use

- Topic 01：帮助区分哪些工程问题其实可由 workflow 解决，不必上升到全自治 agent。
- Topic 03：为 Agent OS / runtime 的最小组成提供务实基线。
- Topic 04：提醒 agent autonomy 本身会带来新的边界和控制需求。

## Caveats

- 这是 Anthropic 的工程经验总结，不是跨行业标准。
- 文章偏“设计原则”和“构建建议”，不是完整安全框架或组织框架。
