# GitHub Spec Kit — Official Spec-Driven Development Workflow

- source_url: `https://github.com/github/spec-kit`
- source_type: `official repository documentation`
- accessed_at: `2026-04-18`
- related_topic: `06 agent-format (primary), 04 future-trends, 05 integration-bdd`
- trust_level: `official`
- tier: `B`
- why_it_matters: 这是 Topic 06 需要的“AGENTS.md 之外的 feature-level workflow”主锚点。它清楚展示 spec-driven 开发不是再塞一个更长的 instruction file，而是把 `constitution / spec / plan / tasks` 变成显式工件链。
- captured_excerpt: `yes`
- claims_supported: `Spec Kit 以 Spec-Driven Development 为核心；工件链明确包含 constitution.md、spec.md、plan.md、tasks.md；/speckit.tasks 会生成带依赖、并行标记、TDD 顺序、checkpoint 的 tasks；/speckit.implement 会校验 constitution/spec/plan/tasks 是否齐备并按 tasks 执行；这是一套 feature-level spec workflow，不等同于 team-level AGENTS/CLAUDE contract。`
- date_scope: `repository state as crawled 2026-04-18`
- related_entities: `GitHub; Spec Kit; Specify CLI; constitution.md; spec.md; plan.md; tasks.md; CLAUDE.md`

## 关键事实

1. Spec Kit 对 `Spec-Driven Development` 的定义是：让 specifications 不再只是辅助说明，而成为直接生成实现的核心工件。
2. 官方 workflow 明确分阶段：
   - constitution
   - spec
   - clarify
   - plan
   - tasks
   - implement
3. 目录树展示出 feature 目录下的典型工件：`spec.md`、`plan.md`、`research.md`、`quickstart.md`、`data-model.md`、`contracts/*`，随后再生成 `tasks.md`。
4. `/speckit.tasks` 官方说明写得很清楚：它生成的 `tasks.md` 包含依赖顺序、并行标记 `[P]`、文件路径、TDD 先测后实现、checkpoint validation。
5. `/speckit.implement` 会先校验 `constitution, spec, plan, and tasks` 是否齐备，再按 `tasks.md` 顺序执行。
6. 这说明 Spec Kit 的核心价值不在 repo-level team instructions，而在 feature-level artifact graph。

## 核心内容摘录

### 方法定位

- 官方把 Spec-Driven Development 描述为：specification 不再是 coding 前的脚手架，而是直接驱动实现的工件。

### 工件链

- 先通过 `/speckit.constitution` 生成或更新 `constitution.md`。
- 新 feature 目录下首先生成 `spec.md`。
- `/speckit.plan` 之后会产生 `plan.md`，并伴随 `research.md`、`quickstart.md`、`data-model.md`、`contracts/*` 等实现细节文件。
- `/speckit.tasks` 再产出 `tasks.md`。

### tasks.md 的语义

- `Task breakdown organized by user story`
- `Dependency management`
- `Parallel execution markers`（`[P]`）
- `File path specifications`
- `Test-driven development structure`
- `Checkpoint validation`

### implement 的前置校验

- `/speckit.implement` 会验证 `constitution, spec, plan, and tasks` 全部存在。
- 然后解析 `tasks.md`，按依赖与并行标记执行，并遵循 task plan 中定义的 TDD 方法。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 06 `agent-format` | 明确表明 Spec Kit 不是 `AGENTS.md` 的替代品，而是 feature-level spec workflow；适合放 EARS / user stories / contracts / tasks，而不是放团队级长期约束 |
| Topic 04 `future-trends` | 支撑“spec-as-code / spec-driven workflow”在 2025–2026 已经工具化 |
| Topic 05 `integration-bdd` | `tasks.md` 的 story / TDD / checkpoint 结构为 story -> scenario -> implementation 的桥接提供了官方工作流载体 |

## 可直接引用的术语 / 概念

- `Spec-Driven Development`
- `constitution.md`
- `spec.md`
- `plan.md`
- `tasks.md`
- `Parallel execution markers`
- `TDD approach`
- `checkpoint validation`

## 风险与局限

1. Spec Kit 是 workflow toolkit，不是跨厂商读取的统一 context file 标准，因此它解决的问题与 AGENTS.md 不同。
2. 官方示例中既有 slash command 也有 `CLAUDE.md` 模板，这说明其早期生态与具体 agent 有耦合，但核心 artifact graph 本身相对 agent-agnostic。
3. 它证明“feature-level spec artifacts 的官方工作流已经存在”，但不自动证明所有团队都应采用完整链条。

## 交叉引用

- 对照 Kiro：[`06-agent-format-kiro-spec-workflow-official.md`](06-agent-format-kiro-spec-workflow-official.md)
- 对照 AGENTS 基线：[`00-shared-codex-agents-md-spec.md`](00-shared-codex-agents-md-spec.md)
- Topic 06 seed：[`../topic-06-agent-format.md`](../topic-06-agent-format.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
