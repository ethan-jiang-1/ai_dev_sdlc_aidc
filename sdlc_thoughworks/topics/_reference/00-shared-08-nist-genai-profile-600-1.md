# W0-08 NIST AI 600-1 Generative AI Profile

- source_url: `https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf`
- source_type: `official NIST GenAI risk profile`
- authority_level: `official GenAI risk profile`
- publication_time: `2024`
- accessed_on: `2026-04-17`
- applicable_topics: `04 security-and-governance; 01 engineering-paradigm; 03 agent-native-infrastructure`

## Why This Source Matters

AI RMF 1.0 给了通用治理骨架，AI 600-1 则把这个骨架进一步落到 Generative AI 场景。它适合帮助我们处理“非确定性、生命周期、第三方工具、插件和人机配置”的风险。

## Key Facts Captured

- 该 profile 面向 GenAI 的 cross-sectoral risk management，可用于 LLM、cloud services、acquisition 等跨行业场景。
- 它明确指出：GenAI 会引入新的风险，或加剧既有风险。
- 风险需要贯穿整个 AI lifecycle，而不是只看 deployment 时刻。
- NIST 还指出 GenAI 往往需要更高等级的人类 review、tracking、documentation 和 management oversight。
- 第三方 inputs、plugins、外部组件在 GenAI system 中尤其重要，因为它们常常伴随分布式接入和不足的 access control。

## Research Use

- Topic 04：支撑对 plugin、tooling、oversight、human-AI configuration 的治理研究。
- Topic 01：帮助把 verification / documentation / review 重新理解为风险管理要求，而不仅是工程偏好。
- Topic 03：支撑对 agent runtime 中第三方工具、插件和 access control 的基础设施设计要求。

## Caveats

- 这是风险 profile，不是具体安全架构蓝图。
- 它指出了风险与建议动作方向，但需要 OWASP 和 MCP 去补更具体的 agent threat surface。
