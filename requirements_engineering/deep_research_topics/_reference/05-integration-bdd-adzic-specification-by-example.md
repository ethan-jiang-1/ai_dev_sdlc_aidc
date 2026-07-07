# Gojko Adzic 2011/2020 — Specification by Example and its 10-year follow-up

- source_url: `https://gojko.net/books/specification-by-example/` + `https://gojko.net/2020/03/17/sbe-10-years.html`
- source_type: `official book page + official follow-up article`
- accessed_at: `2026-04-18`
- related_topic: `05 integration-bdd (primary), 02 user-story, 04 future-trends`
- trust_level: `official / practitioner`
- tier: `A`
- why_it_matters: 这是 Topic 05 最需要的 book-level 方法锚。它直接把 Specification by Example、agile acceptance testing、BDD、living documentation 串成一条链，而且 2020 follow-up 还能说明十年后的实践收敛点。
- captured_excerpt: `yes`
- claims_supported: `Specification by Example` 基于约 50 个项目的研究与案例总结；其目标是用 examples 桥接 stakeholders 与 implementation teams；它把 specifications 变成 living documents；2020 follow-up 继续强调 collaboratively specifying 比测试自动化本身更重要，并把 examples / acceptance criteria 视作 source of truth。
- date_scope: `book published 2011-06-06; follow-up published 2020-03-17`
- related_entities: `Gojko Adzic; Specification by Example; agile acceptance testing; behaviour-driven development; living documentation`

## 关键事实

1. Gojko 官方书页明确写道：
   - `published Jun 6, 2011`
   - 该书基于 `over 50 projects`
   - 目的是帮助团队 `bridge the communication gap between stakeholders and implementation teams`
2. 书页还明确把几个方法串联为一个组合：
   - `specification by example`
   - `agile acceptance testing`
   - `behaviour driven development`
3. 这说明在 Gojko 的方法体系里，BDD 不是孤立的语法工具，而是 examples 驱动的协作式需求方法。
4. 2020 follow-up 明确写出：
   - 十年后，最重要的不是自动化本身，而是 `specifying collaboratively`
   - `examples as a source of truth about the system`
   - 自动化与文档的价值来自 examples 持续映射到系统行为
5. 2020 文章还点出一个很重要的现实修正：
   - text files in version control 不是主流表现形式，只占调查中的少数
   - 但 collaborative specification 作为 shared understanding 依然是核心

## 核心内容摘录

### 2011 书级定位

- 官方书页写道：
  - `This book presents case studies (of over 50 projects)...`
  - `With case studies and real examples, this book helps you understand how successful teams implement specification by example, agile acceptance testing and behaviour driven development`
  - `bridge the communication gap between stakeholders and implementation teams`

### 2020 十年后回看

- follow-up 写道：
  - `collaborative specifications might be the most valuable part`
  - 他过去十年持续推广的重点是 `specifying collaboratively`
  - `examples as a source of truth about the system`
- 这说明 Specification by Example 的核心不只是“把测试写成 Given/When/Then”，而是把例子作为长期有效的 shared understanding artifact。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 05 `integration-bdd` | 这是 Topic 05 的 book-level 主锚：story 不能直接跳到代码，中间需要 example/specification layer；BDD / acceptance testing 是这个 layer 的实现方式 |
| Topic 02 `user-story` | 说明 story 本身不是终点，必须通过 examples 继续澄清 |
| Topic 04 `future-trends` | `source of truth` 与 `living documentation` 为 spec-as-code / agent-readable artifact 提供早期方法基础 |

## 可直接引用的术语 / 概念

- `over 50 projects`
- `bridge the communication gap`
- `agile acceptance testing`
- `behaviour driven development`
- `living documents`
- `source of truth`
- `specifying collaboratively`

## 风险与局限

1. 书页提供的是 high-level method framing，不是章节级全文摘录。
2. 2020 follow-up 是作者自己的 survey / reflection，不是独立同行评审研究。
3. 但对于 Topic 05 的目的，这种书级主张和方法回访恰好足以支撑“examples layer”的必要性。

## 交叉引用

- Cucumber 协作流程：[`05-integration-bdd-cucumber-discovery-formulation-case.md`](05-integration-bdd-cucumber-discovery-formulation-case.md)
- Matt Wynne / Cucumber Book：[`05-integration-bdd-wynne-cucumber-book-example-guided.md`](05-integration-bdd-wynne-cucumber-book-example-guided.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
