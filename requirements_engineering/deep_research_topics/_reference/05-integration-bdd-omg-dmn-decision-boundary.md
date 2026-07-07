# OMG DMN 1.5 / 2024 — Decision Model and Notation official decision-model / decision-table boundary

- source_url: `https://www.omg.org/dmn/` + `https://www.omg.org/intro/DMN.pdf` + `https://www.omg.org/spec/DMN/1.5/About-DMN`
- source_type: `official standard / datasheet / specification catalog`
- accessed_at: `2026-04-18`
- related_topic: `05 integration-bdd (primary), 01 re-landscape, 03 ears, 04 future-trends`
- trust_level: `official`
- tier: `A`
- why_it_matters: Topic 05 仍缺 decision table / DMN 与 EARS 的正式边界材料。OMG 官方资料直接给出 DMN 的对象定位：它不是事件-响应句法模板，而是用于精确定义 business decisions / business rules 的建模标准，包含 Decision Requirements Diagrams、decision tables 和 decision logic/FEEL。结合 EARS 官方“超过 3 个前置条件、数学公式、不应强行文本化”的边界，可把两者分工写得更稳。
- captured_excerpt: `yes`
- claims_supported: `DMN 是 business decisions and business rules 的精确建模语言；DMN 设计上与 BPMN/CMMN 互补而非替代；DMN 用 DRD 建 decision requirements，用 boxed expressions / decision tables 表达 decision logic，用 FEEL 表达形式化逻辑；decision tables 是无歧义表达 business rules 的重要方式；DMN 适合复杂、多准则、可复用的 decision logic。`
- date_scope: `DMN 1.5 formal publication August 2024; latest catalog page current as of 2026-04-18`
- related_entities: `OMG; DMN; Decision Requirements Diagram; decision table; FEEL; BPMN; CMMN`

## 关键事实

1. OMG DMN 官方页把 DMN 定义为用于 `precise specification of business decisions and business rules` 的 modeling language and notation。
2. OMG 明确说明 DMN 设计上与 BPMN / CMMN 互补；组织应为不同类型的活动选择最合适的建模标准。
3. OMG 数据页说明 DMN 支持三个层面：
   - Decision requirements：用 DRD 表达 decision dependencies
   - Boxed expressions：图形化表达 decision logic，其中重要组成包括 decision tables
   - Decision logic：用 FEEL 等形式语言表达可执行逻辑
4. OMG 数据页明确说 decision tables 是表达 business rules 的 `unambiguous` 方式。
5. OMG 1.5 正式版页面说明 DMN 1.5 是 `formal` 规范，publication date 为 `August 2024`。
6. DMN 官方定位强调的是复杂、多准则 decision-making 的建模与自动化，而不是 Story、EARS、Gherkin 那种“业务意图 / 系统行为 / 验证场景”的同类替代物。

## 核心内容摘录

### 官方定位

- OMG DMN 官方页说明：DMN 面向 business decisions 与 business rules 的精确定义，并面向 business users、analysts、developers 共同可读。
- OMG 1.5 页面说明：DMN 的 primary goal 是建立 business decision design 与 decision implementation 之间的 standardized bridge。

### 三层结构

- OMG 数据页说明 DRD 用于表达 decisions、input data、business knowledge 之间的依赖关系。
- 同一份数据页说明 decision tables 用于建模 DRD 组件背后的 decision logic。
- 数据页还说明 FEEL / logic layer 可以表达结构化逻辑、计算与可执行表达式。

### 对 Topic 05 的边界意义

- 如果问题的核心是 `When / While / If / Where -> system shall` 的行为契约，EARS 很适合。
- 如果问题的核心是多输入、多规则、可组合、可复用的 decision logic，OMG DMN 提供了更直接的标准化表达对象：DRD + decision tables + FEEL。
- 这与 EARS 官方指南的边界是一致的：当前置条件太多、进入公式/复杂逻辑时，不应强行塞进单句受控自然语言。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 05 `integration-bdd` | 补齐 decision table / DMN ↔ EARS 的正式边界：EARS 管系统行为句法，DMN 管复杂决策逻辑与规则表 |
| Topic 03 `ears` | 强化“何时不用 EARS”的一手对照面：复杂、多条件、规则网更适合 decision model / decision table |
| Topic 01 `re-landscape` | 在 Story / EARS / BDD 之外补入 decision model 这一地图位置 |
| Topic 04 `future-trends` | 为 requirements / decisions 的 graph-like / model-driven 表达提供一个成熟标准先例 |

## 可直接引用的术语 / 概念

- `Decision Model and Notation`
- `business decisions and business rules`
- `Decision Requirements Diagram (DRD)`
- `decision tables`
- `boxed expressions`
- `FEEL`
- `standardized bridge`

## 风险与局限

1. 这份 reference 锁定的是 DMN 官方对象定位，不是某个行业项目中把 DMN 与 EARS、BDD 具体组合的落地案例。
2. DMN 面向的是 decision logic / business rules；它不自动替代系统级非功能要求、时序约束或 failure-response contract。
3. Topic 05 因而不能把 DMN 写成“EARS 的上位替代”；更稳的写法是把它作为 decision-table / multi-criteria logic 的专门表示层。

## 交叉引用

- Topic 05 evidence summary：[`../_artifacts/05-integration-bdd-evidence-summary.md`](../_artifacts/05-integration-bdd-evidence-summary.md)
- Topic 03 boundary anchor：[`03-ears-mavin-2016-ears-guidelines.md`](03-ears-mavin-2016-ears-guidelines.md)
- W2 selection matrix：[`../_artifacts/W2-selection-matrix-v2.md`](../_artifacts/W2-selection-matrix-v2.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
