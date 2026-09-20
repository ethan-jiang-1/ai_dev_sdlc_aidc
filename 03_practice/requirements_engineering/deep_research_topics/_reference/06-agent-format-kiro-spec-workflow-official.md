# Amazon Kiro — Official Specs and Steering Workflow

- source_url: `https://kiro.dev/docs/getting-started/first-project/` + `https://kiro.dev/docs/steering/`
- source_type: `official product documentation`
- accessed_at: `2026-04-18`
- related_topic: `06 agent-format (primary), 04 future-trends, 03 ears`
- trust_level: `official`
- tier: `B`
- why_it_matters: 这是 Topic 06 需要的另一份 feature-level workflow 对照锚点。Kiro 的官方文档把 `requirements / design / tasks` 和 `.kiro/steering/` 分得很清楚，而且显式把 EARS 放在 requirements phase。
- captured_excerpt: `yes`
- claims_supported: `Kiro 把 Specs 定义为三阶段工作流：Requirements / Design / Tasks；Requirements phase 使用 user stories + EARS acceptance criteria；完成后 review tasks.md 并执行；同时 Kiro 使用 .kiro/steering/ 作为 workspace / global / team-level 持久上下文层，并支持 AGENTS.md 作为 steering directives。`
- date_scope: `docs updated 2026-02 to 2026-03; accessed 2026-04-18`
- related_entities: `Amazon Kiro; Specs; Requirements; Design; Tasks; EARS; .kiro/steering/; AGENTS.md`

## 关键事实

1. Kiro 的 `Your first project` 官方文档把 Specs 定义为三阶段流程：
   - `Requirements`
   - `Design`
   - `Tasks`
2. 其中 `Requirements` 阶段明确写的是：`User stories with acceptance criteria in EARS notation`。
3. 文档还写明：spec 完成后要 review `tasks.md`，逐项执行，并跟踪进度。
4. 这意味着在 Kiro 里，EARS 的首选落点不是 team-level steering file，而是 feature spec 的 requirements phase。
5. Kiro 的 `Steering` 文档把 `.kiro/steering/` 定义为 workspace root 下的持久知识层；也支持 `~/.kiro/steering/` 的 global scope 与 team steering。
6. Kiro 还明确支持 `AGENTS.md` 作为 steering directives，但说明 AGENTS.md 不支持 inclusion modes，且总是被包含。
7. 这形成了与 Topic 06 结论高度一致的分层：
   - team / workspace-level: `.kiro/steering/*` / `AGENTS.md`
   - feature-level: `requirements/design/tasks`

## 核心内容摘录

### Kiro Specs 三阶段

- 官方文档写明：Specs 会把高层 feature idea 转成三阶段实现计划：
  - `Requirements - User stories with acceptance criteria in EARS notation`
  - `Design - Technical architecture and implementation approach`
  - `Tasks - Discrete, trackable implementation steps`

### 执行闭环

- Spec 完成后，Kiro 指导用户：
  - review `tasks.md`
  - execute tasks
  - track progress as tasks update

### Steering 层

- `.kiro/steering/` 是 workspace scope 的持久上下文目录。
- `~/.kiro/steering/` 是 global scope。
- team steering 可通过集中分发方式落到 `~/.kiro/steering/`。

### AGENTS.md 在 Kiro 的位置

- Kiro 官方明确支持通过 `AGENTS.md` 提供 steering directives。
- 但 Kiro 同时说明：`AGENTS.md` 不支持 inclusion modes，并且总是包含。
- 相比之下，`.kiro/steering/*.md` 支持 always / fileMatch / manual / auto 等 inclusion 模式。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 06 `agent-format` | 这是“team-level context vs feature-level spec”分层的强官方证据；Kiro 同时拥有 steering 层和 specs 层，且职责清晰 |
| Topic 03 `ears` | Kiro 官方直接把 EARS 放进 requirements phase，说明 EARS 在 agent-era 最自然的落点之一就是 feature spec，而不是庞大的 always-on rule file |
| Topic 04 `future-trends` | 支撑 IDE-native spec workflow 已经产品化，而且与 AGENTS.md 兼容而非互斥 |

## 可直接引用的术语 / 概念

- `Requirements / Design / Tasks`
- `User stories with acceptance criteria in EARS notation`
- `tasks.md`
- `.kiro/steering/`
- `workspace steering`
- `global steering`
- `team steering`
- `AGENTS.md`
- `inclusion modes`

## 风险与局限

1. Kiro 文档证明的是官方推荐工作流，不是大规模第三方采用数据。
2. 它更强地回答“应该怎么分层”，而不是“这样分层一定带来更高产出”。
3. Kiro 的 steering 和 specs 体系仍在快速演化，未来文件名或界面入口可能变化，但当前分层思想已经很明确。

## 交叉引用

- 对照 Spec Kit：[`06-agent-format-github-spec-kit-official.md`](06-agent-format-github-spec-kit-official.md)
- shared 基线：[`00-shared-codex-agents-md-spec.md`](00-shared-codex-agents-md-spec.md)
- Topic 06 seed：[`../topic-06-agent-format.md`](../topic-06-agent-format.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
