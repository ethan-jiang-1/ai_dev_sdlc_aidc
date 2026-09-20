# Matt Wynne 2017/2019 — The Cucumber Book and Example-guided Development

- source_url: `https://mattwynne.net/books` + `https://cucumber.io/blog/bdd/example-guided-development/`
- source_type: `official author page + official Cucumber blog`
- accessed_at: `2026-04-18`
- related_topic: `05 integration-bdd (primary), 02 user-story`
- trust_level: `official / practitioner`
- tier: `B`
- why_it_matters: Matt Wynne 是 Example Mapping 和 Cucumber 方法链里的关键人物。这两份材料把 BDD 从“写 Gherkin”提升到一组 xDD family practices，并把《The Cucumber Book》定位成可执行规格的实操主书。
- captured_excerpt: `yes`
- claims_supported: `The Cucumber Book (2nd Edition)` 是 Matt Wynne 的正式 BDD/Cucumber 主书；Matt 在 2019 明确把 TDD / BDD / ATDD / SbE 收束为同一家族的 example-guided practices；其关键不是测试工具，而是用 examples 进行跨角色协作和 outside-in delivery。`
- date_scope: `book page current as accessed 2026-04-18; blog published 2019-08-20`
- related_entities: `Matt Wynne; The Cucumber Book; Cucumber; Example Mapping; BDD; ATDD; Specification by Example`

## 关键事实

1. Matt Wynne 官方 books 页确认：
   - `The Cucumber Book (2nd Edition)`
   - 副标题 `Behaviour-Driven Development for Testers and Developers`
   - `Published: February 2017`
2. 这至少说明《The Cucumber Book》是 BDD/Cucumber 领域的正式书级锚点，而不是零散博客文章。
3. Matt 在 2019 的 Cucumber 官方博客中提出：
   - `TDD`, `BDD`, `ATDD`, `Specification by Example` 都属于同一家族
   - 用 `Example-guided development` 作为更清晰的抽象名
4. 文章说明 examples 的角色不是“附带测试”，而是 guide design / implementation / shared understanding。
5. 这对 Topic 05 的关键帮助是：把 story -> example -> implementation 的中间层合法化，而不是只把 BDD 看成测试框架。

## 核心内容摘录

### The Cucumber Book 的正式定位

- Matt Wynne 官方站列出：
  - `The Cucumber Book (2nd Edition)`
  - `Behaviour-Driven Development for Testers and Developers`
  - `Published: February 2017`

### 2019 的更高层抽象

- 2019 文章标题就是 `Example-guided development: A useful abstraction for the xDD family?`
- 文中明确说：
  - `TDD, BDD, ATDD, Specification by Example – they’re all the same.`
  - 它们都 `work from the outside in`
  - 使用 `examples to specify how the system should behave`
  - 然后把这些 examples 自动化，得到 verification 与 up-to-date documentation

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 05 `integration-bdd` | 这是 Topic 05 的第二主锚：它把 BDD / ATDD / Specification by Example 放进同一方法家族，说明 Gherkin 不是孤立终点而是 examples layer 的表达方式 |
| Topic 02 `user-story` | 帮助证明 story 不该直接变成测试脚本，中间需要 discovery / example / formulation |

## 可直接引用的术语 / 概念

- `The Cucumber Book`
- `Behaviour-Driven Development for Testers and Developers`
- `Example-guided development`
- `outside in`
- `examples to specify`
- `verification`
- `up-to-date documentation`

## 风险与局限

1. 书页只提供元数据，不提供章节级全文。
2. 2019 blog 是 practitioner synthesis，不是学术实验。
3. 但它对 Topic 05 很关键，因为本主题需要的是方法家族边界，而不是单点工具 benchmark。

## 交叉引用

- Gojko 书级主锚：[`05-integration-bdd-adzic-specification-by-example.md`](05-integration-bdd-adzic-specification-by-example.md)
- Cucumber 协作流程：[`05-integration-bdd-cucumber-discovery-formulation-case.md`](05-integration-bdd-cucumber-discovery-formulation-case.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
