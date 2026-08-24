# Gherkin — Official Reference (Cucumber)

- source_url: `https://cucumber.io/docs/gherkin/reference/`（2026-04-17 抓取正文，Cucumber 官方）
- source_type: `official product documentation / DSL spec`
- accessed_at: `2026-04-17`
- related_topic: `shared (05 integration-bdd primary；03 ears 对照；02 user-story 联动)`
- trust_level: `official (cucumber.io 是 Cucumber 项目官方站点)`
- tier: `B`
- why_it_matters: **BDD 在工具层的落地标准**就是 Gherkin；Topic 05 要做 User Story ↔ BDD ↔ EARS 的选型矩阵，必须有一份\"keyword-level 清单 + 语义约束\"的权威锚点。本文件锁定 Gherkin 的一等公民关键字、其在\"一条 feature 文件\"里的结构约束，以及\"GWT 模式 ≠ Gherkin 关键字集\"的区分（Fowler bliki 另存于 `00-shared-fowler-given-when-then-bliki.md`）。
- captured_excerpt: `yes`
- notes: Gherkin 也被 SpecFlow、Behat、Reqnroll、Behave、godog 等多个 BDD 生态复用；本 reference 是其规范性最强、维护最活跃的一份。

---

## 关键事实

1. **主关键字（primary keywords）**
   - `Feature`、`Rule`（Gherkin 6 引入）、`Example`（= `Scenario`）、`Background`、`Scenario Outline`（= `Scenario Template`）、`Examples`（= `Scenarios`）。
   - **步骤关键字**：`Given`、`When`、`Then`、`And`、`But`、`*`（asterisk 等价于任意步骤关键字）。
   - 次关键字：`"""`（Doc Strings）、`|`（Data Tables）、`@`（Tags）、`#`（Comments）。

2. **结构硬约束（一条 `.feature` 文件）**
   - **必须以 `Feature:` 开头**；每个文件只能有一个 `Feature`。
   - `Feature` 下的 free-form description **在遇到 `Background / Rule / Example / Scenario Outline`（或其别名）时终止**。
   - `Background` 在 Feature 或 Rule 级别都可用，**每个 Feature/Rule 至多一个 Background**。

3. **步骤语义（官方给出的角色分工）**
   - `Given` — 建立系统的已知状态；对应\"use case 的 preconditions\"。官方反对在 Given 中写用户交互。
   - `When` — 事件或动作；官方建议\"想象 1922 年没有电脑时用户怎么描述\"，即**避开 UI/技术细节**。
   - `Then` — 期望结果；必须\"对可观察输出\"断言，**不允许断言数据库内部记录**。
   - 步骤是顺序执行的；**步骤关键字不参与 step-definition 匹配**，因此\"Given there is money / Then there is money\"会被视为重复 step（Cucumber 官方明确给出反例）。

4. **可重用结构**
   - `Scenario Outline` + `Examples` 表格 = **参数化的 scenario**；Scenario Outline 模板本身永不直接运行，而是对 Examples 每行运行一次。
   - `Doc Strings` 用三重引号 `"""`（或三个反引号）传多行文本，**可加 content type 标签**（如 `"""markdown`）。
   - `Data Tables` 用 `|` 传结构化数据；支持 cell 转义 `\n` / `\|` / `\\`。

5. **本地化（与 EARS 的对照要点）**
   - Gherkin 已被本地化到 **70+ 种口语**；`# language: xx` 首行声明。
   - 这是一条关键选型论据：**Gherkin 的受众优先假设是\"业务+技术混编团队\"**，因此用\"自然语言关键字\"；而 EARS 的受众优先假设是\"工程团队/安全关键系统\"，因此用\"结构化英文\"。

6. **重要的\"它不是什么\"**
   - Gherkin 不是通用需求规约语言；官方定位为**可执行规约（executable specification）+ 活文档（living documentation）**。
   - Gherkin 不支持 block comments，只允许行首 `#` 注释——这是\"纪律 > 表达力\"的设计取向。

---

## 原文直引（选段）

> "The primary keywords are: Feature, Rule (as of Gherkin 6), Example (or Scenario), Given, When, Then, And, But for steps (or *), Background, Scenario Outline (or Scenario Template), Examples (or Scenarios)."

> "Given steps are used to describe the initial context of the system … If you were creating use cases, Given's would be your preconditions."

> "When steps are used to describe an event, or an action. … Imagine it's 1922, when there were no computers."

> "An outcome should be on an observable output. That is, something that comes out of the system (report, user interface, message), and not a behaviour deeply buried inside the system (like a record in a database)."

> "The language you choose for Gherkin should be the same language your users and domain experts use when they talk about the domain. Translating between two languages should be avoided."

## 桥接

- → `00-shared-fowler-given-when-then-bliki.md`：Fowler 指出\"Gherkin is the name of Cucumber's DSL\"，Gherkin = GWT 的**工具落地**之一，非等价概念。
- → `00-shared-mavin-2009-ears-re09.md`：EARS Event-driven `When <trigger>, <system> shall <response>` vs Gherkin `When / Then`——**语法层近似，语义层分层**：EARS 是\"行为规约\"，Gherkin 是\"行为示例+可执行断言\"。
- → `00-shared-incose-gtwr-v4-summary.md`：GtWR 的\"需求特征\"是否可在 Gherkin 的 scenario 层成立？Topic 05 要专门比较。

## 限制

- 本 reference 侧重**语法层**；**实施最佳实践**（如 antipattern: \"three amigos\" flow、scenario bloat）需要 Cucumber School / Cucumber book 做补。
- Gherkin reference 并不给出\"如何在安全关键系统里用 BDD\"的指南——那一面由 ISO 26262 Part 8 + INCOSE GtWR 在 Topic 05 / 限制面提供。
