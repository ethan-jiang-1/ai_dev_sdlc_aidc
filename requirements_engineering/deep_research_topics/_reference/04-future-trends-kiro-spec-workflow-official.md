# Amazon Kiro — official signal for IDE-native specs and steering

- source_url: `https://kiro.dev/docs/getting-started/first-project/` + `https://kiro.dev/docs/steering/`
- source_type: `official product documentation`
- accessed_at: `2026-04-18`
- related_topic: `04 future-trends (primary), 06 agent-format, 03 ears`
- trust_level: `official`
- tier: `B`
- why_it_matters: Topic 04 的一个核心前瞻判断是“需求将成为 IDE 原生原语”。Kiro 已经把 specs 与 steering 直接内建进 IDE workflow，是最直接的产品级信号。
- captured_excerpt: `yes`
- claims_supported: `requirements / design / tasks` 已成为 IDE 内建三阶段工作流；workspace / global steering 成为持久上下文层；EARS 已被放进 requirements phase；这说明 IDE-native spec primitive 已经出现。`
- date_scope: `docs snapshot accessed 2026-04-18`
- related_entities: `Amazon Kiro; specs; requirements; design; tasks; steering; EARS`

## 关键事实

1. Kiro 官方把 feature specs 分为三阶段：
   - `Requirements`
   - `Design`
   - `Tasks`
2. requirements phase 明确采用 `User stories with acceptance criteria in EARS notation`。
3. 文档还明确说明：
   - review `tasks.md`
   - execute tasks
   - track progress
4. steering 文档则把 `.kiro/steering/` 设为 workspace root 下的长期上下文层。
5. 这意味着需求表达已经从外部文档工具移动到 IDE 内部一等工作流。

## 核心内容摘录

- `Requirements - User stories with acceptance criteria in EARS notation`
- `Design - Technical architecture and implementation approach`
- `Tasks - Discrete, trackable implementation steps`
- `Review Generated Tasks in the tasks.md file`
- `.kiro/steering/` 作为 workspace/global/team-level context

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 04 `future-trends` | 这是“IDE 原生需求原语”已经产品化的最强信号之一 |
| Topic 06 `agent-format` | 说明 team-level steering 与 feature-level spec 正在被工具显式分层 |
| Topic 03 `ears` | 表明 EARS 已进入 agent-era IDE workflow，而非停留在传统 ALM |

## 可直接引用的术语 / 概念

- `Requirements / Design / Tasks`
- `.kiro/steering/`
- `IDE-native`
- `User stories with acceptance criteria in EARS notation`

## 风险与局限

1. 这是单一厂商产品的官方工作流，不代表行业默认。
2. 但对 Topic 04 来说，它已经足够证明“这种未来不是纯猜测”。

## 交叉引用

- GitHub 对照：[`04-future-trends-github-spec-kit-official.md`](04-future-trends-github-spec-kit-official.md)
- 治理约束：[`04-future-trends-ai-governance-nist-eu-ai-act.md`](04-future-trends-ai-governance-nist-eu-ai-act.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
