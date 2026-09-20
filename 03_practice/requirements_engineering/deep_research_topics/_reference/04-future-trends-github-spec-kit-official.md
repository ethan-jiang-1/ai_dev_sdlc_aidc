# GitHub Spec Kit — official signal for Spec-Driven Development as workflow

- source_url: `https://github.com/github/spec-kit`
- source_type: `official repository documentation`
- accessed_at: `2026-04-18`
- related_topic: `04 future-trends (primary), 06 agent-format, 05 integration-bdd`
- trust_level: `official`
- tier: `B`
- why_it_matters: Topic 04 需要判断“spec-as-code / spec-driven development”是不是已经从概念走向工具化。Spec Kit 是 2025–2026 最直接的官方信号之一。
- captured_excerpt: `yes`
- claims_supported: `Spec-Driven Development` 已经以官方工具链形式出现；spec.md / plan.md / tasks.md / constitution.md 组成显式 artifact graph；这说明 spec-first workflow 已经从理念进入可复用工程实践。`
- date_scope: `repository state accessed 2026-04-18`
- related_entities: `GitHub; Spec Kit; spec-driven development; constitution.md; spec.md; plan.md; tasks.md`

## 关键事实

1. GitHub 官方仓库把该项目直接命名为 `spec-kit`，定位就是帮助团队启动 `Spec-Driven Development`。
2. 工件链明确包含：
   - `constitution.md`
   - `spec.md`
   - `plan.md`
   - `tasks.md`
3. 这说明“需求 / 设计 / 执行计划”正在变成版本化、可复用、可交给 agent 消费的显式工件，而不是只存在于会议和 issue 评论中。

## 核心内容摘录

- Spec Kit workflow 的核心是：
  - 先有 `spec`
  - 再有 `plan`
  - 再有 `tasks`
  - 最后由工具链执行实现
- `constitution` 被单独提出来，说明长期原则和单个 feature spec 已被显式分层。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 04 `future-trends` | 这是“规约即工作流工件”已经工具化的强信号 |
| Topic 06 `agent-format` | 说明 feature-level spec layer 不只是 Kiro 一家现象，而是跨工具趋势 |
| Topic 05 `integration-bdd` | 为 examples / tasks / validation 提供更上游的 spec 容器 |

## 可直接引用的术语 / 概念

- `Spec-Driven Development`
- `constitution.md`
- `spec.md`
- `plan.md`
- `tasks.md`

## 风险与局限

1. 这是官方工具仓库，不是行业普及率统计。
2. 它证明“工作流存在”，不单独证明“大多数团队已采用”。

## 交叉引用

- Kiro 对照：[`04-future-trends-kiro-spec-workflow-official.md`](04-future-trends-kiro-spec-workflow-official.md)
- 趋势信号：[`04-future-trends-thoughtworks-spec-driven-development-signal.md`](04-future-trends-thoughtworks-spec-driven-development-signal.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
