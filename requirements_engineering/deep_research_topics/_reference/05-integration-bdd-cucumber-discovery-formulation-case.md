# Cucumber official 2014/2017/2024 — Discovery, Formulation, Example Mapping, and enterprise case

- source_url: `https://cucumber.io/docs/bdd/` + `https://cucumber.io/docs/bdd/example-mapping/` + `https://cucumber.io/blog/collaboration/the-worlds-most-misunderstood-collaboration-tool/` + `https://cucumber.io/blog/bdd/improving-throughput-and-collaboration/`
- source_type: `official documentation + official blog + hosted case study`
- accessed_at: `2026-04-18`
- related_topic: `05 integration-bdd (primary), 02 user-story, 06 agent-format`
- trust_level: `official`
- tier: `B`
- why_it_matters: 这组材料把 Topic 05 里最重要的“story -> rules/examples -> scenarios -> automated implementation”链条讲清楚，而且还给出一个全球投行的 enterprise case，证明这不是纯培训课堂方法。
- captured_excerpt: `yes`
- claims_supported: `BDD` 在 Cucumber 官方定义中是以 user story 为输入、以 examples 为桥梁、以 structured documentation / automation 为落点的三步迭代流程；Example Mapping 以 yellow story / blue rules / green examples / red questions 组织 discovery；Cucumber 创始人明确说 Cucumber 是 collaboration tool 而不是 testing tool；投行案例显示 product owners 参与 acceptance tests / Gherkin 可降低返工并提升完成 feature stories 的可预测性。`
- date_scope: `2014-03-03, 2017-04-10, 2024-12-18 docs snapshot, accessed 2026-04-18`
- related_entities: `Cucumber; Aslak Hellesøy; Theo England; Simon Powers; Example Mapping; Discovery; Formulation; Automation; Gherkin; three amigos`

## 关键事实

1. 2024 Cucumber BDD 文档把日常实践定义成三步循环：
   - 从 `a small upcoming change -- a User Story`
   - 讨论 `concrete examples`
   - 把 examples `document` 成可自动化形式
   - 再自动化并驱动实现
2. 同一页明确把三实践命名为：
   - `Discovery`
   - `Formulation`
   - `Automation`
3. Cucumber Example Mapping 文档进一步把中间层结构明文化：
   - yellow card = story
   - blue cards = acceptance criteria / rules
   - green cards = examples
   - red cards = questions
4. 2014 Aslak 官方文章则从反面给出失败模式：
   - Cucumber 不是 testing tool，而是 `collaboration tool`
   - 如果缺少 BA / PO 输入，scenarios 会变得 imperative、slow、brittle
5. 2017 hosted case study 给出 enterprise signal：
   - global investment bank
   - defects 曾占开发时间 35%
   - 在 3-6 个月阶段 `POs wrote better acceptance tests that could be directly translated to code tests using the Gherkin language`
   - 9 个月后 defect rate 到 `4%`
   - feature stories 的完成可预测性上升

## 核心内容摘录

### 官方三步流程

- Cucumber docs 写道：
  1. `take a small upcoming change to the system -- a User Story`
  2. `talk about concrete examples`
  3. `document those examples`
  4. `implement the behaviour described by each documented example`
- 并命名为 `Discovery, Formulation, and Automation`

### Example Mapping 的卡片结构

- 官方 docs 写道：
  - `We write the story on a yellow card and place it on top.`
  - `acceptance criteria, or rules` on blue cards
  - `Examples` on green cards
  - `Questions` on red cards

### Cucumber 的原始设计意图

- Aslak 写道：
  - `Cucumber was born out of the frustration with ambiguous requirements`
  - 目标是把 `automated acceptance tests, functional requirements and software documentation` 组合进一个 format
  - `Cucumber is a collaboration tool`

### 投行案例

- case study 写道：
  - 在 3-6 个月阶段，`POs wrote better acceptance tests`
  - 这些 tests `could be directly translated to code tests using the Gherkin language`
  - 结果是 `rework within a sprint` 下降
  - 团队更频繁 `building the right thing`
  - 9 个月后 defect rate 降到 `4%`

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 05 `integration-bdd` | 这是 Topic 05 最直接的流程锚：story 不是直接写成 Gherkin，而是经过 discovery / example mapping / formulation 这层中间工序 |
| Topic 02 `user-story` | 说明 acceptance criteria / examples 是 story 方法的自然后续，而不是附加负担 |
| Topic 06 `agent-format` | Example Mapping 的彩卡结构本质上就是一种 feature-level requirements decomposition artifact，可被 agent 工作流吸收 |

## 可直接引用的术语 / 概念

- `Discovery, Formulation, and Automation`
- `a small upcoming change -- a User Story`
- `concrete examples`
- `yellow story card`
- `blue rules`
- `green examples`
- `Cucumber is a collaboration tool`
- `POs wrote better acceptance tests`

## 风险与局限

1. 2017 投行案例是 hosted case study，不是同行评审研究。
2. 9 个月 defect 改善包含多因素，不应简化成“仅因 Gherkin”。
3. 但它仍是高价值企业采用证据，因为它把 PO、acceptance tests、Gherkin、feature stories 放进同一组织变革过程。

## 交叉引用

- Gojko 书级主锚：[`05-integration-bdd-adzic-specification-by-example.md`](05-integration-bdd-adzic-specification-by-example.md)
- Matt Wynne 方法抽象：[`05-integration-bdd-wynne-cucumber-book-example-guided.md`](05-integration-bdd-wynne-cucumber-book-example-guided.md)
- shared 基线：[`00-shared-gherkin-official-reference.md`](00-shared-gherkin-official-reference.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
