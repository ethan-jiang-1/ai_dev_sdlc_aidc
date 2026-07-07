# QRA 2025 — EARS software-scope guidance and low-level software specification boundary

- source_url: `https://qracorp.com/when-not-to-use-ears/` + `https://alistairmavin.com/about/`
- source_type: `official practitioner guidance + official author biography`
- accessed_at: `2026-04-18`
- related_topic: `03 ears (primary), 05 integration-bdd, 01 re-landscape`
- trust_level: `official practitioner / official author site`
- tier: `B`
- why_it_matters: Topic 03 的高价值缺口之一是 “EARS 在纯软件 / SaaS 场景是否只停留在安全关键叙事”。这份组合证据不能直接证明 SaaS empirical adoption，但它能把风险从“软件适用性不明”收窄为“软件适用性与 low-level software audience 已获官方指导支持，SaaS empirical evidence 仍待补”。QRA 官方文明确举 `low-level software requirements specification` 与 `software developers` 作为 EARS/替代表达的目标受众场景；Mavin 官方简介则确认其项目域包含 `software systems`。
- captured_excerpt: `yes`
- claims_supported: `EARS 适用于高层系统需求，也可作为 textual requirements 的默认起点；针对 low-level software requirements specification，受众若是 software developers，可结合 pseudocode / state transition diagrams / visual forms 选择更适合的记法；复杂条件可转 list / decision table；EARS 可描述 new IT solution deliverables；Mavin 的实际项目域包含 software systems。`
- date_scope: `QRA page current as of 2026-04-18; Mavin official biography current as of 2026-04-18`
- related_entities: `QRA; Alistair Mavin; EARS; software developers; low-level software requirements specification; IT solution`

## 关键事实

1. QRA 官方文说明：requirements should be written in the notation most appropriate for the user of the specification。
2. 同文明确给出一个非安全关键的软件语境示例：
   - document = `low-level software requirements specification`
   - audience = `software developers`
   - developers may prefer pseudocode, state transition diagrams, and other abstract/visual forms for some content
3. 同文同时说明：EARS 对 high-level system requirements 很合适，但并非所有 requirement 都应强行写成 EARS。
4. QRA 官方文还明确说：
   - 可以把 EARS 作为 textual requirements 的 `default starting point`
   - 同一方法可描述 `the deliverables of a new IT solution`
5. 该文再次重申软件/复杂逻辑边界：
   - >3 preconditions 时可改 list / table
   - 复杂条件可由 decision table 承担
   - 数学式 requirement 不适合 EARS
6. Mavin 官方简介说明其 requirements engineering projects 覆盖 `software systems`，说明作者本人并未把 EARS 仅限于航空/汽车等硬件或 safety-critical 语境。

## 核心内容摘录

### 软件受众场景

- QRA 官方文给出的示例受众是 `low-level software requirements specification` 的 `software developers`。
- 文中说明这类受众通常能理解 pseudocode、state transition diagrams 等形式，因此 textual requirements 主要保留给难以可视化表达的部分。

### EARS 仍是起点，但不是唯一格式

- QRA 官方文写道：EARS is good as the `default starting point for all of your textual requirements`。
- 同时强调 requirement format 应按 audience 和 meaning 选择，而不是机械地把所有内容模板化。

### IT / software 适用性

- QRA 官方文明确说同一套 EARS core patterns 可以描述 `the deliverables of a new IT solution`。
- Mavin 官方简介说明其 RE 项目域包括 `software systems`。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 03 `ears` | 把风险从“EARS 是否适用于软件场景不明”收窄为“软件适用性已官方支持，但 SaaS empirical evidence 仍待补” |
| Topic 05 `integration-bdd` | 与 decision tables / visual forms 的边界在软件开发文档场景里更明确 |
| Topic 01 `re-landscape` | 说明 EARS 的地图位置不是只属于 safety-critical hardware，也进入 software / IT textual requirements 空间 |

## 可直接引用的术语 / 概念

- `low-level software requirements specification`
- `software developers`
- `default starting point for all of your textual requirements`
- `the deliverables of a new IT solution`
- `pseudocode`
- `state transition diagrams`

## 风险与局限

1. 这份材料是 official practitioner guidance，不是 SaaS 团队 adoption case，也不是同行评审 empirical study。
2. 它能证明软件-scope applicability 与格式边界，不足以证明 EARS 已在 SaaS 团队中广泛采用。
3. 因此 Topic 03 的更强表述应是：`software-scope-supported; saas-empirical-pending`，而不是 “EARS 已在 SaaS 中充分验证”。

## 交叉引用

- Topic 03 evidence summary：[`../_artifacts/03-ears-evidence-summary.md`](../_artifacts/03-ears-evidence-summary.md)
- Topic 05 boundary summary：[`../_artifacts/05-integration-bdd-evidence-summary.md`](../_artifacts/05-integration-bdd-evidence-summary.md)
- official guide / boundary anchor：[`03-ears-mavin-2016-ears-guidelines.md`](03-ears-mavin-2016-ears-guidelines.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
