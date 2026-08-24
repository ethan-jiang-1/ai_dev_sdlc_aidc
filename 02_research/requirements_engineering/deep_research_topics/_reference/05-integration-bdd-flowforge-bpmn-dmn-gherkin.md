# Riskiana et al. 2025 — FlowForge BPMN + DMN to User Stories and Gherkin prototype

- source_url: `https://socjs.telkomuniversity.ac.id/ojs/index.php/ijoict/article/view/1015/` + `https://socjs.telkomuniversity.ac.id/ojs/index.php/ijoict/article/download/1015/440/4823`
- source_type: `academic journal article / open-access prototype study`
- accessed_at: `2026-04-18`
- related_topic: `05 integration-bdd (primary), 02 user-story, 03 ears, 04 future-trends`
- trust_level: `academic`
- tier: `A`
- why_it_matters: Topic 05 当前缺口是同一项目 / 同一工作流里 Story、Gherkin、DMN / decision logic 如何治理。FlowForge 不是高合规企业案例，也不包含 EARS，但它在同一 prototype 中把 BPMN process model、DMN decision logic、User Stories、Gherkin test cases 串成可执行映射，并报告 completeness、path accuracy 与 execution time。这比仅靠概念性“EARS / Gherkin / DMN 边界”更接近同一工件链证据。
- captured_excerpt: `yes`
- claims_supported: `FlowForge transforms BPMN models into User Stories and Gherkin test cases, integrates DMN to handle decision logic and exceptions, and evaluates generated Gherkin against BPMN element completeness and path accuracy. The study reports 98.25% average element completeness, 87.5% average path accuracy, and 0.36-second average execution time across four BPMN diagrams. This supports a same-prototype Story/DMN/Gherkin governance chain while leaving EARS-inclusive and high-compliance same-project evidence pending.`
- date_scope: `received 2024-11-20; published 2025-01-10; accessed 2026-04-18`
- related_entities: `FlowForge; BPMN; DMN; User Story; Gherkin; BDD; Telkom University`

## 关键事实

1. 论文题目是 `FlowForge: A Prototype for Generating User Stories and Gherkin Test Cases from BPMN with DMN Integration and Pattern Matching`。
2. 论文发表于 International Journal on ICT，Vol. 10 No. 2，页码 195-213，DOI 为 `10.21108/ijoict.v10i2.1015`。
3. 研究问题来自 requirements specifications 中的 stakeholder / developer miscommunication，以及 BPMN 模型到测试用例自动化的困难。
4. FlowForge 的核心链条是：
   - BPMN process model
   - DMN decision logic / exceptions
   - User Stories
   - Gherkin test cases
5. 论文明确说 FlowForge 直接从 BPMN models 自动生成 User Stories 和 Gherkin test cases。
6. DMN 的作用是处理 complex decision-heavy workflows、gateways、exceptions、conditional flows，并提高 test completeness。
7. 实验使用四个 BPMN diagrams：
   - Credit-Scoring-Asynchronous
   - Dispatch-of-Goods
   - Recourse
   - Self-Service Restaurant
8. 结果指标包括：
   - BPMN element completeness
   - path accuracy
   - execution time
9. 报告结果：
   - average element completeness = 98.25%
   - average path accuracy = 87.5%
   - average execution time = 0.36 seconds
10. 论文也明确列出限制：cross-pool verification incomplete、pattern libraries restricted、Event-basedGateway 的更多类型仍未充分覆盖。

## 核心内容摘录

### 同一工件链的意义

- FlowForge 不是只讨论 BDD 或只讨论 DMN，而是在同一 prototype 中把 process model、decision model、story、Gherkin 串起来。
- 这对 Topic 05 很关键，因为它提供了同一工作流内多类需求 / 验收工件如何转化的可观察证据。

### 与 EARS / DMN / Gherkin 边界的关系

- 论文不使用 EARS。
- 但它强化了现有判断：
  - 复杂路径和 decision logic 不适合只靠单句需求或单个 scenario 表达。
  - DMN / BPMN 适合承载 workflow / decision structure。
  - Gherkin 适合生成可读、可执行的 acceptance-test scenarios。

### 对最终报告的写法约束

- 可以写：
  - Story / DMN / Gherkin 可以在同一原型链条中治理。
  - DMN 能补足 BPMN 到 Gherkin 转换中的 decision / exception handling。
  - 这是一条 prototype-level same-chain evidence。
- 不应写：
  - 已找到 EARS + Story + DMN + Gherkin 的同一高合规项目案例。
  - FlowForge 已证明生产级治理成熟。
  - BPMN/DMN 到 Gherkin 的自动生成已经没有覆盖或准确性风险。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 05 `integration-bdd` | same-prototype Story / DMN / Gherkin 工件链；DMN 与 Gherkin 的职责边界；BPMN/DMN 驱动 acceptance-test generation |
| Topic 02 `user-story` | User Story 可由 process model 派生，但不等于完整 business process / decision model |
| Topic 03 `ears` | 间接支持“复杂多条件逻辑应转入 decision model / table，而不是单句 EARS” |
| Topic 04 `future-trends` | 支撑 model-to-test / model-to-requirements 自动化趋势 |

## 可直接引用的术语 / 概念

- `FlowForge`
- `BPMN`
- `DMN`
- `User Stories`
- `Gherkin test cases`
- `98.25%`
- `87.5%`
- `0.36 seconds`
- `cross-pool verification`
- `pattern libraries`

## 风险与局限

1. 这是 prototype study，不是生产组织治理案例。
2. 它没有覆盖 EARS，因此不能关闭 EARS-inclusive same-project gap。
3. 它的 path accuracy 仍有波动，不能当作 fully reliable automated transformation。
4. Topic 05 因而可以升级为 `same-prototype-story-dmn-gherkin-supported`，但仍保留 `ears-inclusive-high-compliance-same-project-case-pending`。

## 交叉引用

- OMG DMN boundary：[`05-integration-bdd-omg-dmn-decision-boundary.md`](05-integration-bdd-omg-dmn-decision-boundary.md)
- Cucumber workflow / case：[`05-integration-bdd-cucumber-discovery-formulation-case.md`](05-integration-bdd-cucumber-discovery-formulation-case.md)
- Topic 05 evidence summary：[`../_artifacts/05-integration-bdd-evidence-summary.md`](../_artifacts/05-integration-bdd-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
