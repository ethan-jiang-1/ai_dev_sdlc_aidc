# W0-10 OWASP Agentic AI Threats and Mitigations

- source_url: `https://genai.owasp.org/download/45674/?tmstv=1739819891`
- source_type: `OWASP security guide`
- authority_level: `official practitioner security guidance`
- publication_version: `v1.1`
- accessed_on: `2026-04-17`
- applicable_topics: `04 security-and-governance; 03 agent-native-infrastructure`

## Why This Source Matters

这是本轮最直接面向 agentic threat surface 的安全来源。相比通用 AI 治理框架，它更接近 Topic 04 真正关心的攻击面、威胁模型和缓解路径。

## Key Facts Captured

- OWASP 把该文档定位成 `threat-model-based reference`，围绕 agentic AI reference architecture 展开。
- 它明确指出：agent memory 和 tool integration 是关键攻击面，尤其容易遭受 memory poisoning 与 tool misuse。
- 当 autonomy 失控、multi-agent architectures 相互学习时，这些风险会进一步复杂化。
- 工具使用会把 identity 与 authorization 问题带入 agent environment，并可能破坏原本信任边界。
- 文档专门指出 `Confused Deputy` 风险：当 AI agent 继承用户或系统权限去调用集成工具与 API 时，可能执行超出设计意图的动作。
- 文档还强调 `Non-Human Identities (NHI)` 是 agentic AI security 的核心对象，NHI 如果缺乏 session-based oversight，容易出现 privilege misuse 或 token abuse。

## Research Use

- Topic 04：作为 agent-specific threat taxonomy 的共享底座。
- Topic 03：帮助定义 Agent OS / tool runtime 中必须纳入的 identity、tool isolation、memory control 和 audit 需求。
- Wave 2：把安全 threat surface 与基础设施设计直接联动起来。

## Caveats

- 这是实践型安全指南，不是正式标准。
- 它更擅长 threat surface 与 mitigation catalog，不直接提供企业治理流程或交付指标。
