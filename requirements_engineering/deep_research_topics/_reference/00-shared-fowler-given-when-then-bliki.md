# Martin Fowler — bliki `GivenWhenThen` (KOL Anchor for BDD syntax)

- source_url: `https://martinfowler.com/bliki/GivenWhenThen.html`（2026-04-17 抓取正文，Martin Fowler 官方 bliki）
- source_type: `KOL blog (expert practitioner)`
- accessed_at: `2026-04-17`
- related_topic: `shared (05 integration-bdd primary；02 user-story, 03 ears, 04 future-trends 引用)`
- trust_level: `practitioner (author-owned blog)`
- tier: `B`
- why_it_matters: 本轮所有\"BDD / Given-When-Then / EARS Event-driven\"的讨论都需要一个**权威、简洁、非 vendor 叙事**的 GWT 定义锚。Fowler 的 bliki 直接把 GWT **归因到 Daniel Terhorst-North + Chris Matts** 作为 BDD 的一部分，并把它**明确等价于 xUnit 的 Four-Phase Test** 与 Bill Wake 的 Arrange-Act-Assert——这对 Topic 05 的\"BDD 只是测试阶段结构，不是需求方法论\"判断是核心证据。
- captured_excerpt: `yes`

---

## 关键事实

1. **归因与起源**
   - Fowler 明确指出 GWT 是 **Daniel Terhorst-North 与 Chris Matts 作为 BDD 一部分开发的**；Dan 在 review comments 中承认 **Ivan Moore 给过显著启发**。
   - GWT 出现在 Cucumber 等测试框架中是\"作为结构化方式的采用\"，**GWT 本身不依赖 Cucumber**。

2. **三段结构的官方定义**
   - **Given** — 描述\"在你开始指定的行为之前，世界的状态\"；可视为测试的前置条件（pre-conditions）。
   - **When** — 你正在指定的那段行为。
   - **Then** — 你期望该行为导致的变化。
   - Fowler 强调：\"用 GWT 时用 'and' 串联多个表达式\"是惯例。

3. **GWT 的\"双身份\"问题（Fowler 明确点破）**
   - Fowler 原文：\"I've characterized the given as a description of the pre-condition state because that's the way I prefer to think of it. A testing framework, however, interprets the givens as a **set of commands to bring the system-under-test into the correct state** before executing the when command.\"
   - **研究线含义**：GWT 在\"规约语义\"与\"执行语义\"上是双重身份——这直接牵出 Topic 05 的**"EARS 等需求语法 vs GWT 等测试脚本语法"**边界问题。

4. **与 xUnit / AAA 的等价关系（关键反证）**
   - Fowler 原文：\"Meszaros describes the pattern as Four-Phase Test. His four phases are Setup (Given), Exercise (When), Verify (Then) and Teardown. Bill Wake came up with the formulation as Arrange, Act, Assert.\"
   - **研究线含义**：GWT **本质上是测试阶段模式的 DSL 化**，而不是\"需求规约的原生结构\"。这点对以下两个论断提供证据支撑：
     - **Topic 05 结论**：BDD ≠ 需求方法论；把 EARS 换成 GWT **不等于替换需求工具链**。
     - **Topic 03 ↔ 05**：EARS 的\"When X, the system shall Y\"与 GWT 的\"When X … Then Y\"**语法近似但语义层不同**——前者是系统**行为规约**，后者是**执行期断言**。

5. **Given-When-Then ≠ Gherkin**
   - Fowler 脚注 3：\"Or to be strict it uses Gherkin, which is the name of Cucumber's DSL.\"
   - 这一区分要在 Topic 05 中保留：**GWT 是概念/结构，Gherkin 是 Cucumber 里落地的 DSL**。

---

## 原文直引（关键段）

> "Given-When-Then is a style of representing tests - or as its advocates would say - specifying a system's behavior using SpecificationByExample. It's an approach developed by Daniel Terhorst-North and Chris Matts as part of Behavior-Driven Development (BDD)."

> "The essential idea is to break down writing a scenario (or test) into three sections:
> - The given part describes the state of the world before you begin the behavior you're specifying in this scenario. You can think of it as the pre-conditions to the test.
> - The when section is that behavior that you're specifying.
> - Finally the then section describes the changes you expect due to the specified behavior."

> "Although Given-When-Then style is symptomatic to BDD, the basic idea is pretty common when writing tests or specification by example. Meszaros describes the pattern as Four-Phase Test. … Bill Wake came up with the formulation as Arrange, Act, Assert."

## 桥接

- → `00-shared-mavin-2009-ears-re09.md`：EARS Event-driven 的 `When <trigger>, the <system> shall <response>` 与 GWT `Given <pre> / When <event> / Then <result>` 的语法-语义层次对比，是 Topic 03 ↔ 05 的关键对照组。
- → 待落 `00-shared-gherkin-reference.md`：Gherkin 官方 keywords 的完整清单是 GWT 在工具层的准确落地。
- → `00-shared-fowler-user-story-bliki.md`：Fowler 本人也把 story 与 spec-by-example 的关系串在同一个 KOL 体系内。

## 限制

- Fowler bliki 是\"权威重述\"，但 GWT 的**最原始出处**是 Dan North 的 2006 博文\"Introducing BDD\"——Topic 05 正式主张前还需要回到 Dan North 原文做一次锚定。
- Fowler 未细化\"GWT 在工程质量维度（可测性、可跟踪性）上的局限\"；这一面需由 INCOSE GtWR + 学界二次文献补。
