# 05 — integration-bdd — Evidence Summary

- scope: `Wave 1 starter pack plus selected DMN/Gherkin governance upgrades for Topic 05`
- status: `closed_for_current_round`
- last_updated: `2026-04-18`
- related_references:
  - [`../_reference/05-integration-bdd-adzic-specification-by-example.md`](../_reference/05-integration-bdd-adzic-specification-by-example.md)
  - [`../_reference/05-integration-bdd-wynne-cucumber-book-example-guided.md`](../_reference/05-integration-bdd-wynne-cucumber-book-example-guided.md)
  - [`../_reference/05-integration-bdd-cucumber-discovery-formulation-case.md`](../_reference/05-integration-bdd-cucumber-discovery-formulation-case.md)
  - [`../_reference/05-integration-bdd-omg-dmn-decision-boundary.md`](../_reference/05-integration-bdd-omg-dmn-decision-boundary.md)
  - [`../_reference/05-integration-bdd-flowforge-bpmn-dmn-gherkin.md`](../_reference/05-integration-bdd-flowforge-bpmn-dmn-gherkin.md)
  - [`../_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md`](../_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md)
  - [`../_reference/00-shared-fowler-given-when-then-bliki.md`](../_reference/00-shared-fowler-given-when-then-bliki.md)
  - [`../_reference/00-shared-gherkin-official-reference.md`](../_reference/00-shared-gherkin-official-reference.md)
  - [`../_reference/00-shared-iso-26262-part8-overview.md`](../_reference/00-shared-iso-26262-part8-overview.md)

## 本轮已落地证据

1. 方法主锚：
   - [`../_reference/05-integration-bdd-adzic-specification-by-example.md`](../_reference/05-integration-bdd-adzic-specification-by-example.md) 说明 examples layer 的书级定位，以及 Specification by Example / agile acceptance testing / BDD 的组合关系。
2. 家族边界：
   - [`../_reference/05-integration-bdd-wynne-cucumber-book-example-guided.md`](../_reference/05-integration-bdd-wynne-cucumber-book-example-guided.md) 说明 TDD / BDD / ATDD / SbE 属于同一家族，Gherkin 只是其中的表达与自动化媒介。
3. 工作流与企业例证：
   - [`../_reference/05-integration-bdd-cucumber-discovery-formulation-case.md`](../_reference/05-integration-bdd-cucumber-discovery-formulation-case.md) 证明官方推荐链条是 `story -> examples -> structured scenarios -> automation`，并给出投行采用案例。
4. decision-model / decision-table 边界：
   - [`../_reference/05-integration-bdd-omg-dmn-decision-boundary.md`](../_reference/05-integration-bdd-omg-dmn-decision-boundary.md) 证明 DMN 是面向 business decisions / business rules 的标准化模型层，decision tables 和 FEEL 更适合承载复杂多条件 decision logic，而不是把它们硬塞进单句 EARS 或 Gherkin。
5. same-prototype Story / DMN / Gherkin 工件链：
   - [`../_reference/05-integration-bdd-flowforge-bpmn-dmn-gherkin.md`](../_reference/05-integration-bdd-flowforge-bpmn-dmn-gherkin.md) 在同一 prototype 中把 BPMN process model、DMN decision logic、User Stories、Gherkin test cases 串起来，并用 completeness / path accuracy / execution time 评估生成结果。
6. acceptance-governance framework：
   - [`../_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md`](../_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md) 把 requirements / user stories、acceptance criteria、acceptance tests、Gherkin、BPMN/DMN、traceability 放进同一 BA / tester 协作与验收测试治理框架。

## 当前可支撑的判断

1. Topic 05 的关键不是“User Story vs BDD”，而是 story 之后必须出现一个 examples / rules / scenarios 层。
2. Gherkin 不是凭空写出来的脚本；它应该来自 discovery / example mapping / formulation。
3. `Story -> rules/examples -> executable scenarios` 是当前最清晰的结构化链条。
4. Cucumber 官方和 Gojko / Matt Wynne 的主张高度一致：
   - 协作先于自动化
   - examples 是 shared understanding 的真正载体
   - 自动化是验证与文档同步机制，而不是全部目的
5. Topic 05 现在可以更明确地区分三种“结构化”：
   - EARS 处理系统行为与边界契约
   - Gherkin 处理可验证示例与验收场景
   - DMN / decision tables 处理复杂决策逻辑与规则组合
6. FlowForge 和 ISTQB 共同把 Topic 05 从“概念边界”推进到“同一原型链条 + 官方治理框架”：
   - FlowForge = same-prototype BPMN/DMN -> User Story/Gherkin transformation
   - ISTQB = requirements / user stories -> acceptance criteria -> acceptance tests / Gherkin -> BPMN/DMN -> traceability governance

## 对 must_answer 的覆盖进度

| must_answer 子问题 | 当前状态 | 证据 |
| --- | --- | --- |
| Adzic / Wynne 的当前立场 | `starter_covered` | Gojko 2011/2020 + Matt 2017/2019 |
| 故事到场景的正式工作流 | `covered` | Cucumber official BDD + Example Mapping docs |
| 企业 case | `starter_covered` | Cucumber hosted global investment bank case |
| 决策表 / DMN ↔ EARS 边界 | `starter_covered` | OMG DMN official + EARS “>3 preconditions / formulas” boundary |
| Story / DMN / Gherkin same-chain evidence | `same_prototype_supported` | FlowForge BPMN/DMN -> User Story/Gherkin prototype |
| Acceptance governance framework | `official_framework_supported` | ISTQB Acceptance Testing syllabus |
| 安全关键 / EARS-inclusive same-project governance case | `pending_narrowed` | FlowForge 和 ISTQB 缩小缺口，但未包含 EARS 同项目治理 |

## 当前 deep-dive questions

1. FlowForge 已补 same-prototype Story / DMN / Gherkin，ISTQB 已补 acceptance governance framework；2026-04-18 targeted search 未找到合格公开强源能同时覆盖 EARS-inclusive 或高合规 same-project Story/Example/Gherkin/DMN governance case，缺口继续显式 deferred。
2. Example Mapping 的 outputs 与 EARS clauses 如何系统映射，而不是停在启发式对应？
3. 什么时候 Gherkin 会过重，应该退回 checklist / rules / decision table / DMN？

## 风险与升级点

- 当前企业 case 偏 BDD 与 acceptance tests，FlowForge 是 prototype 而非生产治理，ISTQB 是 syllabus 而非 project case；2026-04-18 targeted search 后仍未找到能直接把 EARS 接入同一高合规案例的公开强源。
- decision-table / DMN ↔ EARS 的官方对象边界已 starter-covered，Story / DMN / Gherkin same-prototype chain 也已 supported，但仍缺 EARS-inclusive same-project governance case。
- Topic 05 目前已从 starter pack 升级到 governance_narrowed，但未到 full saturation。

## 下一轮建议动作

1. 只在出现高合规或大型组织案例时继续补，且该案例应显示 story / scenario / structured requirements / decision-model 四层如何治理，最好明确包含 EARS 或等价 controlled natural language；不要用 wiki、厂商泛文档或工具说明替代同项目治理案例。
2. 补 Dan North 原始 BDD 文本，进一步稳固 examples layer 的历史边界。
3. 在 Wave 2 / 选型矩阵中把 “EARS vs DMN vs Gherkin” 的职责边界写成明确选型规则。
