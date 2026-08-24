# NIST AI RMF 1.0 + EU AI Act — official governance signals for documentation, risk, and traceability

- source_url: `https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10` + `https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf` + `https://artificialintelligenceact.eu/wp-content/uploads/2024/01/AI-Act-FullText.pdf`
- source_type: `official framework + official legal text`
- accessed_at: `2026-04-18`
- related_topic: `04 future-trends (primary), 06 agent-format, 03 ears`
- trust_level: `official`
- tier: `A`
- why_it_matters: Topic 04 不是只看工具趋势，还要看治理方向。NIST AI RMF 和 EU AI Act 都把 AI 风险管理、技术文档、可追踪信息、日志与人类监督放在核心位置，这对结构化需求与 spec artifact 的未来位置至关重要。
- captured_excerpt: `yes`
- claims_supported: `AI RMF 1.0` 是面向设计/开发/部署/使用 AI systems 的官方风险管理框架；EU AI Act Article 11 要求 high-risk AI system 在投放前编制并保持最新 technical documentation，Article 12 要求自动记录 logs，Article 14 要求人类监督；这些都强化了“结构化、可更新、可审计的 specification/documentation layer”的未来必要性。`
- date_scope: `NIST AI RMF 1.0 published 2023-01-26; EU AI Act text snapshot accessed 2026-04-18`
- related_entities: `NIST; AI RMF 1.0; EU AI Act; Article 11; Article 12; Article 14; technical documentation; logs; human oversight`

## 关键事实

1. NIST 官方页写明：
   - `AI RMF 1.0`
   - 目标是帮助 `organizations designing, developing, deploying, or using AI systems`
   - 用于管理 AI risks 并促进 trustworthy and responsible AI
2. 这说明 AI 风险管理被官方直接覆盖整个设计-开发-部署-使用链，而不是只看上线后的合规。
3. EU AI Act Article 11 明确要求：
   - technical documentation 在 system 投放前即应完成
   - 且 `shall be kept up-to date`
   - 必须足以让 authorities 评估合规性
4. Article 12 要求：
   - high-risk AI systems 应支持 automatic recording of events (`logs`)
   - 以保证适当 traceability
5. Article 14 要求：
   - high-risk AI systems must be effectively overseen by natural persons
   - oversight 要与 risk、autonomy level、context of use 相称

## 核心内容摘录

### NIST AI RMF 1.0

- 官方 abstract 写道，AI RMF 面向 `designing, developing, deploying, or using AI systems`
- 且 intended to be `practical`, `use-case agnostic`, and adaptable to evolving AI landscape

### EU AI Act Article 11

- `The technical documentation of a high-risk AI system shall be drawn up before that system is placed on the market or put into service and shall be kept up-to date.`

### EU AI Act Article 12

- `High-risk AI systems shall technically allow for the automatic recording of events ('logs')`
- 并要求记录与 traceability 相关的事件

### EU AI Act Article 14

- `High-risk AI systems shall be designed and developed ... that they can be effectively overseen by natural persons`

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 04 `future-trends` | 强化“结构化规约/文档层不会消失，反而会因治理与审计要求更重要”的判断 |
| Topic 06 `agent-format` | 说明 team-level instructions 之外，还需要更正式、更可更新、更可审计的 technical documentation layer |
| Topic 03 `ears` | 支撑 EARS / structured requirements 在高监管语境中的长期价值，而不只是写作偏好 |

## 可直接引用的术语 / 概念

- `designing, developing, deploying, or using AI systems`
- `technical documentation`
- `kept up-to date`
- `logs`
- `traceability`
- `human oversight`

## 风险与局限

1. 这些来源证明的是治理与文档义务，不直接规定 EARS / Story / Spec Kit 哪种格式获胜。
2. 但它们明确提高了“结构化、持续维护、可追踪 documentation artifact”的长期必要性。

## 交叉引用

- 工具化信号：[`04-future-trends-github-spec-kit-official.md`](04-future-trends-github-spec-kit-official.md)
- IDE 原生信号：[`04-future-trends-kiro-spec-workflow-official.md`](04-future-trends-kiro-spec-workflow-official.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
