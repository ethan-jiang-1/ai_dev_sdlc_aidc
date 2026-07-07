# Topic 5 — 互补、分层、BDD 管道与综合选型

> 本文件面向 **独立 Deep Research** 使用：嵌入原文 §4 平行案例要点、§7 EARS↔Gherkin 桥梁、§9 九维矩阵完整文本与结语隐喻，不依赖打开源文即可完成一轮研究。

## 研究问题（Deep Research 入口）

1. 同一业务线（如手机银行）中，**User Story** 应止于何处、**EARS** 应从何处接管？组织上如何防止"故事写成伪规格"或"EARS 前置于价值探索"？
2. **EARS 子句**与 **Gherkin（Given-When-Then）** 的逻辑同构如何用于 **测试左移 / ATDD / Cucumber 自动生成**？人工翻译与 NLP 自动化各自的失败模式？
3. **§9 九维矩阵**在真实项目中的使用方式：一次性对照表，还是作为**门禁**（如 AI 项目强制结构化规约）？
4. **TDD / BDD / USDD** 与 User Story、EARS 的组合：Roost 等叙事的可验证主张（§7 [38]）是什么？
5. 大型组织如何在 **PO 层（Story）/ 系统层（EARS）/ 测试层（Gherkin）** 三轨间建立一致性，避免语义漂移？

## 原文锚点（供回溯）

| 章节 | 主题 |
|------|------|
| §4 全文 | 抽象层级与问题域；§4.1 平行案例（故事 vs EARS）；§4.2 AEB 与 User Story 失效 |
| §7 全文 | TDD 阻力；BDD/USDD 与故事模糊性；EARS↔Gherkin 映射表；Roost、Inflectra、Cucumber、测试左移 |
| §9 表 + 结语 | 九维对比矩阵（已嵌入）；"房间指南 vs 建筑蓝图"隐喻；宏观故事 + 微观 EARS + Gherkin 网 |

---

## 1. 分层模型：Story / EARS / Gherkin 三轨

```
┌─────────────────────────────────────────────────────┐
│  PO 层：User Story   —— 北极星 / 商业价值           │  ← Topic 2
│  as <role>, I want <outcome>, so that <value>        │
├─────────────────────────────────────────────────────┤
│  系统层：EARS        —— 契约 / 行为边界              │  ← Topic 3
│  While/When/If/Where <...>, the <system> shall <...>│
├─────────────────────────────────────────────────────┤
│  测试层：Gherkin      —— 可执行规格 / 防护网         │  ← 本 Topic §2
│  Given <state>, When <event>, Then <outcome>         │
└─────────────────────────────────────────────────────┘
```

**隐喻**（原文 §9 结语）：User Story = **房间装修指南**（空间感、功能布局、体验愿景）；EARS = **建筑工程蓝图**（承重墙、电力管线、抗震合规）；Gherkin = **验收防护网**。三者缺一不可。

## 2. EARS ↔ Gherkin 同构映射（§7 复刻）

| EARS 子句 | 逻辑语义 | Gherkin 映射 | BDD 对应 |
|-----------|---------|--------------|---------|
| `While <precondition>` | 系统执行前必须满足的持续状态 | `Given <initial state>` | Setup / Background |
| `When <trigger>` | 状态转换的动作/事件 | `When <action/event>` | Action |
| `If <trigger>, then` | 异常或非法输入触发 | `When <error input>` + `Then <fallback>` | Negative path |
| `Where <feature>` | 可选特性装配条件 | `Background: <feature enabled>` / Tag | Feature toggle |
| `the <system> shall <response>` | 必达的输出或状态 | `Then <expected outcome>` | Assertion |

**工程意义**：EARS 写好之后可通过 NLP 工具（Roost.ai [38]、Inflectra AI [27]）**近零损耗**地转换为可执行 Cucumber 脚本，实现 **Test-Shift-Left** 与 ATDD（验收测试驱动开发）。这是 EARS 对比松散 User Story 在"可自动化"一维上的最大优势。

### 2.1 端到端示例：手机银行余额（贯穿三层）

**Story（Topic 2 §4）**：

> As a mobile banking customer, I want to see my balance on the home screen, so that I can check my finances at a glance.

**EARS（Topic 3 §4.1）**：

- *While the user is in the authenticated session, the App shall render the balance within 1 s of screen load.*
- *If the backend does not respond within 3 s, then the App shall display a placeholder and log timeout.*

**Gherkin（本 Topic）**：

```gherkin
Feature: Home-screen balance display

  Background:
    Given the user is authenticated

  Scenario: Balance renders within 1 second
    When the user opens the home screen
    Then the real-time balance is displayed within 1000 ms

  Scenario: Backend timeout triggers skeleton fallback
    Given the accounting backend latency exceeds 3000 ms
    When the user opens the home screen
    Then a skeleton placeholder is shown
    And a timeout event is logged with the request ID
```

**教学点**：Story 负责"为什么做"，EARS 负责"系统应该怎样响应"，Gherkin 负责"怎么证明它真的做到了"。三层**同一业务意图**在不同抽象层的投影。

---

## 3. §9 九维综合评估矩阵（完整嵌入）

> 原文 §9 矩阵是**选型决策的一次性参考**。Deep Research 时可按项目特征逐行打分，形成项目专属权重。

| # | 评估维度 | User Story | EARS |
|---|---------|------------|------|
| 1 | **理论渊源与哲学** | 敏捷 / XP / 反文档化，Kent Beck 1997 C3 | 安全关键重工业，Mavin 2009 Rolls-Royce RE09 |
| 2 | **核心关注点** | 商业价值：谁、想做什么、为什么 | 系统行为与边界：何种状态、什么触发、必达响应 |
| 3 | **受众视角** | 业务方、UX、最终用户；黑盒 | 架构师、底层开发、QA、合规；灰盒/白盒 |
| 4 | **语法强制力** | 极宽松：`as / I want / so that` | 严格词法时间逻辑：`While / When / If / Where / shall` |
| 5 | **NFR 处理能力** | 极差：需靠 AC 或技术债卡片绕路 | 极优：Ubiquitous 模式天然服务于约束与基础性能 |
| 6 | **对模糊性的态度** | 拥抱模糊，留白以促对话 | 零容忍，强制消解歧义 |
| 7 | **LLM / AI 编程契合度** | 较差：易诱发幻觉与弱边界 | 优异：本身即结构化 Prompt，精准映射控制流 |
| 8 | **BDD/TDD 自动化映射** | 较弱：需人工拆解 Given-When-Then | 极强：NLP 可近零损耗编译为 Cucumber |
| 9 | **质量金标准** | INVEST（6 维，强调价值与解耦） | INCOSE GTWR（14 类 41 条系统工程规则） |

**使用建议**：

- **初创 SaaS 探索期**：行 2、3、6 倾向 Story；行 7、8 可暂不加权。
- **安全关键硬件**：行 3、4、5、8、9 倾向 EARS；行 6（模糊性）直接否决 Story 独用。
- **AI 辅助代码生成**：行 7、8 加权 → 强烈倾向 EARS 或结构化 Prompt，Story 降级为上游意图层。

## 4. 平行案例（§4）教学重用

| 案例 | Story 侧表现 | EARS 侧表现 | 教学点 |
|------|-------------|-------------|-------|
| **手机银行余额**（§4.1）| 价值叙事到位，但未覆盖缓存、超时、未登录掩码 | 状态驱动 + 有害行为精确补齐边界 | 软件 SaaS 内两者**互补**而非竞争 |
| **AEB / ISO 26262**（§4.2）| Story 对 ASIL D 毫无指导意义 | 复合逻辑 + 异常切换满足 HARA | 安全关键域 Story **不可单独胜任** |

完整案例文本：手机银行见 [topic-02-user-story-tutorial.md](topic-02-user-story-tutorial.md) §4、[topic-03-ears-tutorial.md](topic-03-ears-tutorial.md) §4.1；AEB 见 [topic-03-ears-tutorial.md](topic-03-ears-tutorial.md) §4.2。

## 5. 组织落地 Playbook（§9 结语 + 推论）

1. **PO 写 Story + AC 要点**，不碰实现细节。
2. **架构师 / Tech Lead 把 Story 展开为 EARS**（每个 Story 产出 3–10 条 EARS），AC 中的性能/异常部分上升为 EARS Unwanted / Ubiquitous。
3. **QA（或 NLP 工具）把 EARS 编译为 Gherkin + Cucumber**，进入 CI。
4. 每次 Story 变更，**反向溯源**到 EARS 与 Gherkin，形成三轨一致性门禁。
5. **"Definition of Ready"** 检查：Story 通过 INVEST；对应 EARS 通过 INCOSE 关键 C1/C2；Gherkin 场景可运行。

## 6. 待补文献与检索方向

- Specification by Example（Gojko Adzic）：Story → Example → Gherkin 的系统论述。
- Cucumber / Gherkin 官方规则与 tag 模型（原文 [41][42]）。
- Roost.ai / Inflectra.ai 生成式测试的**独立**第三方评测（非厂商案例）。
- 大型组织（金融、航空、汽车）三轨治理实践：原文 [44][45][50] 的扩展。

## 7. 本 Topic 参考文献（摘自原文编号）

见 [references-by-topic.md](references-by-topic.md) 中 **Topic 5**；完整条目见 [references-full.md](references-full.md)。

**编号快查：** 6, 9, 14, 16, 17, 19, 20, 21, 22, 23, 27, 37, 38, 39, 40, 41, 42, 43, 44

## 8. Deep Research 查询种子

**英文**：

1. `"EARS to Gherkin" automated transformation NLP Cucumber ATDD`
2. `"Specification by Example" Gojko Adzic user story BDD workshop`
3. `three-tier requirements user story system spec acceptance test governance case study`
4. `ATDD test shift left enterprise adoption metrics automotive OR finance`
5. `user story vs formal specification selection matrix decision criteria`

**中文**：

1. `EARS Gherkin 映射 Cucumber 自动化 案例`
2. `Story EARS Gherkin 三层 分层 需求治理`
3. `行为驱动开发 BDD 实例化需求 Specification by Example 中文`
4. `验收测试驱动 ATDD 金融 / 汽车 / 航空 落地`
5. `需求选型 矩阵 用户故事 EARS 对比 决策`

## 9. 交叉引用

- User Story 教程：← [topic-02-user-story-tutorial.md](topic-02-user-story-tutorial.md)
- EARS 教程：← [topic-03-ears-tutorial.md](topic-03-ears-tutorial.md)
- 证据与趋势：→ [topic-04-future-trends-and-evidence.md](topic-04-future-trends-and-evidence.md)
- 高流量断言可信度：→ [claims-audit.md](claims-audit.md)

## 10. 历史摘要（保留，不修改）

- 本主题的历史正文保留在 §1–§9：它保留了 Story / EARS / Gherkin 三轨分层、EARS ↔ Gherkin 同构、端到端 worked example、九维矩阵与综合选型原始表达。

## 11. 本轮新增证据

- Topic 05 starter pack 已覆盖 Story -> examples -> structured scenarios -> automation 的官方链条：见 [`_reference/05-integration-bdd-adzic-specification-by-example.md`](_reference/05-integration-bdd-adzic-specification-by-example.md)、[`_reference/05-integration-bdd-wynne-cucumber-book-example-guided.md`](_reference/05-integration-bdd-wynne-cucumber-book-example-guided.md)、[`_reference/05-integration-bdd-cucumber-discovery-formulation-case.md`](_reference/05-integration-bdd-cucumber-discovery-formulation-case.md)。
- 本轮补上 decision-model / decision-table 官方边界锚点：[`_reference/05-integration-bdd-omg-dmn-decision-boundary.md`](_reference/05-integration-bdd-omg-dmn-decision-boundary.md)。该材料说明 DMN 面向 business decisions / business rules、DRD、decision tables、FEEL，与 EARS 的系统行为句法模板不是同类对象。
- same-prototype Story / DMN / Gherkin 链条已由 [`_reference/05-integration-bdd-flowforge-bpmn-dmn-gherkin.md`](_reference/05-integration-bdd-flowforge-bpmn-dmn-gherkin.md) 补齐，acceptance-governance framework 已由 [`_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md`](_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md) 补齐。
- 与之配套的 EARS 官方边界由 [`_reference/03-ears-mavin-2016-ears-guidelines.md`](_reference/03-ears-mavin-2016-ears-guidelines.md) 提供：当前置条件超过 3 个、进入公式或复杂逻辑时，不应强行写成单句 EARS。

## 12. 本轮新增机制理解

- Topic 05 不只是“三轨分层”，而是至少存在四种不同表达职责：
  - Story：意图与价值
  - EARS：系统行为与边界契约
  - Gherkin：可验证示例与验收场景
  - DMN / decision table：复杂决策逻辑与规则组合
- 因此“结构化”不能只理解为把所有内容都写成受控自然语言。复杂规则组合一旦超过 EARS 的舒适区，应进入 decision model / decision table 层，再由场景和测试去验证。
- FlowForge 与 ISTQB 组合起来，已经把 Topic 05 从“概念边界”推进到“同一原型链条 + 官方治理框架”，所以当前缺口不再是 object boundary，而是高合规项目中的联用治理公开样本。

## 13. 本轮新增趋势与难点

- 难点不再只是 Story 与 EARS 的边界，而是团队往往会把 decision logic、行为契约、验收示例混写，导致单个工件同时承担过多职责。
- 当前已能用官方材料支持“DMN 不是 EARS 的替代，而是 decision logic 的专门表示层”；同样也已能支持“Story / DMN / Gherkin 可以进入同一原型链条，requirements / acceptance criteria / acceptance tests / BPMN/DMN 可以进入同一治理框架”。
- 但仍缺一个高合规项目里 Story / EARS / DMN / Gherkin 联用的公开治理案例，这一缺口在本轮多次 targeted search 后继续保留。

## 14. 当前判断（本轮综合后）

- Topic 05 现在可以稳写成：
  - `story-to-examples-to-automation-supported`
  - `dmn-boundary-official-positioning-supported`
  - `same-prototype-story-dmn-gherkin-supported`
  - `acceptance-governance-framework-supported`
  - `ears-inclusive-high-compliance-same-project-case-pending`
- 因而本轮对 Topic 05 的判断已从“三轨足够解释大多数案例”升级为“若存在复杂规则网或多条件组合，应显式引入 decision-table / DMN 层，而不是把复杂性全部压进 EARS 或 Gherkin”。
- 更稳的组合建议是：
  - Story 负责为什么做
  - EARS 负责系统在何种条件下必须如何响应
  - DMN / decision tables 负责复杂决策逻辑
  - Gherkin 负责把关键例子转成可验证场景
- 这一判断已进入 [`_artifacts/05-integration-bdd-evidence-summary.md`](_artifacts/05-integration-bdd-evidence-summary.md)、[`_artifacts/W2-cross-topic-synthesis.md`](_artifacts/W2-cross-topic-synthesis.md) 与 [`_artifacts/W2-selection-matrix-v2.md`](_artifacts/W2-selection-matrix-v2.md)。
