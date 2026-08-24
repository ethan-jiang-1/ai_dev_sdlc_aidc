# ISTQB 2019/2024 — Acceptance Testing syllabus for requirements, user stories, Gherkin, BPMN, and DMN

- source_url: `https://www.istqb.org/wp-content/uploads/2024/11/ISTQB-CT-AcT_Syllabus_v1.0_2019.pdf`
- source_type: `official professional certification syllabus`
- accessed_at: `2026-04-18`
- related_topic: `05 integration-bdd (primary), 01 re-landscape, 02 user-story, 03 ears`
- trust_level: `official professional body`
- tier: `B`
- why_it_matters: Topic 05 不只需要单个 BDD 工具证据，还需要治理层证据：requirements / user stories、acceptance criteria、acceptance tests、Gherkin、BPMN/DMN、traceability 如何在同一验收测试框架里分工。ISTQB Acceptance Testing syllabus 是官方专业认证 syllabus，明确面向 product owners / business analysts / testers 协作，覆盖 requirements/user stories、Gherkin、BPMN/DMN 和 traceability，能作为治理框架锚点。
- captured_excerpt: `yes`
- claims_supported: `ISTQB Acceptance Testing syllabus defines the relationship between requirements/user stories, acceptance criteria, and acceptance tests; describes Gherkin for acceptance-test design in ATDD/BDD; uses BPMN and DMN for business process/rule modeling; and states that traceability between requirements/user stories, acceptance criteria, and related test cases should be managed. This supports Topic 05's governance framing across story, examples, Gherkin, and decision/process models, while not serving as a single-project case or EARS-specific case.`
- date_scope: `syllabus version 1.0, 2019; PDF hosted in ISTQB 2024 site path; accessed 2026-04-18`
- related_entities: `ISTQB; Acceptance Testing; requirements; user stories; acceptance criteria; Gherkin; BPMN; DMN; business analysts; testers`

## 关键事实

1. ISTQB syllabus 说明其目标之一是加强 product owners / business analysts / testers 在 acceptance testing 中的协作。
2. Learning Objectives 明确要求解释：
   - business goals / needs / requirements 的关系
   - requirements / user stories、acceptance criteria、acceptance tests 的关系
   - requirements / user stories 和 acceptance criteria 的质量如何影响 acceptance testing
3. 文档把 acceptance criteria 定位为 requirements 或 user stories 的细化与测试基础。
4. 文档明确说 acceptance test cases are derived from acceptance criteria。
5. 文档把 ATDD 描述为在 requirements analysis 中由 business analysts、product owners、testers、developers 协作产生 acceptance tests。
6. 文档把 BDD 与 Gherkin 关联起来，说明 Gherkin 使用 Given-When-Then 结构表达 acceptance tests。
7. 文档明确要求 traceability between requirements / user story and related test cases should be managed。
8. 第 3 章覆盖 business process and business rule modeling，并把 BPMN 与 DMN 放入 acceptance testing。
9. 文档说明 BPMN 表示 workflows，DMN 表示 decisions、business rules、outcomes/output within the workflow。
10. 文档说明 business process/rule models 可作为生成 acceptance tests 的 basis。
11. 文档给出的 good practices 包括：
   - decision tables help manage dependencies in rule-based business processes
   - DMN supports conditions and outcomes corresponding to business rules under test
   - additional information such as links to user stories, requirements, risks, priorities may be useful

## 核心内容摘录

### 治理链条

- ISTQB 的链条不是“写 Gherkin 就够了”，而是：
  - requirements / user stories
  - acceptance criteria
  - acceptance tests
  - Gherkin for structured acceptance tests
  - BPMN/DMN for process and rule models
  - traceability between artifacts

### 与 Topic 05 的最直接关系

- 这份 syllabus 把 Topic 05 的几类对象放进同一治理框架：
  - Story / requirement 是需求入口。
  - Acceptance criteria 是测试边界。
  - Gherkin 是结构化 test-case 表达。
  - BPMN / DMN 是 process / rule model。
  - Traceability 是治理要求。

### 对最终报告的写法约束

- 可以写：
  - Story、Gherkin、BPMN/DMN 在 acceptance testing governance 中有不同职责。
  - BA/tester collaboration 与 traceability 是 acceptance testing 的核心治理面。
  - DMN 更适合表达 decision / business-rule dependencies。
- 不应写：
  - ISTQB 要求使用 EARS。
  - ISTQB 是同一生产项目案例。
  - Gherkin 取代了 requirements 或 user stories。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 05 `integration-bdd` | 官方治理框架：requirements/user stories -> acceptance criteria -> Gherkin tests -> BPMN/DMN process/rule models -> traceability |
| Topic 01 `re-landscape` | 把 acceptance testing 放回 requirements engineering / business analysis 协作流程 |
| Topic 02 `user-story` | 明确 user story 需要 acceptance criteria 和 related tests，而不是独立闭环 |
| Topic 03 `ears` | 间接支持 structured acceptance criteria / traceability，但不提供 EARS-specific guidance |

## 可直接引用的术语 / 概念

- `requirements / user stories`
- `acceptance criteria`
- `acceptance tests`
- `Gherkin`
- `BPMN`
- `DMN`
- `traceability`
- `business analysts and testers`
- `business process/rule model`

## 风险与局限

1. 这是 official syllabus，不是 production case。
2. 它不覆盖 EARS，因此不能关闭 EARS-inclusive same-project gap。
3. 它使用 BPMN/DMN 的 subset，不是完整 OMG 标准正文。
4. Topic 05 因而可升级为 `acceptance-governance-framework-supported`，但仍保留 `same-project-ears-inclusive-governance-case-pending`。

## 交叉引用

- FlowForge same-prototype chain：[`05-integration-bdd-flowforge-bpmn-dmn-gherkin.md`](05-integration-bdd-flowforge-bpmn-dmn-gherkin.md)
- OMG DMN boundary：[`05-integration-bdd-omg-dmn-decision-boundary.md`](05-integration-bdd-omg-dmn-decision-boundary.md)
- Gherkin official reference：[`00-shared-gherkin-official-reference.md`](00-shared-gherkin-official-reference.md)
- Topic 05 evidence summary：[`../_artifacts/05-integration-bdd-evidence-summary.md`](../_artifacts/05-integration-bdd-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
