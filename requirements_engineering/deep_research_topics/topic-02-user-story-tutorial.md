# Topic 2 — User Story（教程向独立主题）

> 本文件面向 **独立 Deep Research** 使用：嵌入了原文 §2.1 / §3.1 / §8.1 的关键定义与 §4.1 的手机银行案例，不依赖打开源文即可完成一轮研究。

## 研究问题（Deep Research 入口）

1. User Story 从 **XP / C3** 到 **3C、Planning Game、Story Mapping** 的演进脉络是什么？**"对一次对话的承诺"**（Cockburn）在远程/AI 协作时代如何被重新解释？
2. 经典模板（角色 / 需要 / 以便）与 **验收标准（AC）**、**Gherkin** 如何分工？何时故事应拆为 Enabler、Spike 或纯技术项？
3. **INVEST** 各维度在真实 Backlog 中的**常见违反**与修复模式？
4. User Story 的典型反模式（伪规格、缺 AC、NFR 硬套、复制粘贴灾难）有哪些可操作的检测与重构手法？
5. **AI 生成 User Story** 的质量（Atlassian Rovo、Copilot4DevOps、Azure Copilot + INVEST）在真实 Backlog 中可靠吗？

## 原文锚点（供回溯）

| 章节 | 主题 |
|------|------|
| §2.1 | 起源：Kent Beck C3、Cockburn"对话的承诺"、Planning Game、3C、Cohn、Jeff Patton Story Mapping |
| §3.1 | 意图驱动；三问；不写实现；AC 与 Gherkin 的分层 |
| §4.1（前半）| 手机银行：故事侧价值对齐与对后端不足（已嵌入）|
| §5.1 | 优势：人本、占位符促对话、Backlog 灵活；盲区：歧义、NFR、形式主义 |
| §8.1 | INVEST 六维全文（已嵌入）|
| §9 表左列 | 用户故事一列的多维对比摘要（主矩阵见 Topic 5）|

---

## 1. 历史脉络（§2.1 压缩）

- **1997**：Kent Beck 在克莱斯勒 C3 项目首次引入 User Story，旨在替代瀑布的冗长 SRS。
- **1998**：Alistair Cockburn 将其提炼为 **"A promise for a conversation"**——一张卡不是契约，而是承诺后续对话。
- **1999**：Kent Beck《Extreme Programming Explained》正式将 User Story 作为 Planning Game 的核心构件。
- **2001**：Ron Jeffries 提出 **3C**：Card、Conversation、Confirmation。
- **2004**：Mike Cohn《User Stories Applied》成为事实上的行业教材。
- **2014**：Jeff Patton《User Story Mapping》引入"地图维度"，解决故事之间依赖不可见的问题。

**核心哲学**：反文档化、将细节推迟到临近开发的对话中；以用户视角注入同理心，避免"满足规格但未交付价值"。

## 2. 经典模板与变体

### 2.1 最小模板

```
As a <role / persona>,
I want <capability / outcome>,
so that <business value / goal>.
```

中文：
```
作为 <角色>，
我希望 <能力 / 预期结果>，
以便 <商业价值 / 达成的目标>。
```

**刻意省略的维度**：如何实现、技术栈、性能阈值、异常处理。这些**不属于故事主干**，应落到 AC / 技术任务 / EARS 级规约。

### 2.2 常见变体

| 变体 | 何时使用 | 写法提示 |
|------|---------|---------|
| **Enabler Story**（SAFe）| 技术债、平台能力、架构启用 | "As a platform, we need X so that downstream teams can Y" |
| **Spike**（时盒研究）| 不确定性高、需先探路 | 明确时盒（如 2 天）、探索性问题列表、输出形式 |
| **Job Story**（Klement）| 想摆脱"角色"的过度拟人化 | `When <situation>, I want to <motivation>, so I can <outcome>.` |
| **非人类角色**（系统、定时任务）| B2B、平台化产品 | 角色可为 "Billing Service"、"Nightly Cron Job" |

### 2.3 与 AC / Gherkin 的分工

- **Story 卡**：三段式 + 一句话价值。
- **验收标准（AC）**：故事完成边界；可为要点列表，也可为 Gherkin 场景。
- **Gherkin（§3.1）**：
  ```
  Given <initial state>
  When <action/event>
  Then <expected outcome>
  ```
  Gherkin 只是 AC 的一种**载体**，不是 Story 本身（详见 [topic-05-integration-bdd-selection.md](topic-05-integration-bdd-selection.md) §2）。

---

## 3. INVEST 质量准则（§8.1 完整嵌入）

由 Bill Wake 提出，评估单个故事是否健康：

| 字母 | 维度 | 通过标准 | 常见违反 |
|------|------|---------|---------|
| **I**ndependent | 独立性 | 故事间不强耦合，可任意顺序开发、交付 | "必须先做 A 才能做 B" 的串联链条 |
| **N**egotiable | 可协商 | 卡不是合同，保留程序员与业务方共创空间 | 卡片上列出 15 条实现细节 |
| **V**aluable | 有价值 | 对最终用户或客户可感知 | "把日志格式改成 JSON"（技术任务伪装成故事）|
| **E**stimable | 可估算 | 团队可基于经验给出规模/故事点 | "做一个 AI 助手" 级别的模糊 |
| **S**mall | 小巧 | 能在一个 Sprint 内完成并验收 | 3 个 Sprint 才能跑通的 Epic |
| **T**estable | 可测试 | 存在可编写的 AC，能证明"Done" | "用户体验更流畅" 类主观叙述 |

## 4. Worked Example：手机银行"主屏余额"（§4.1 完整版）

**Story 卡**：

> **As** a mobile banking customer,
> **I want** to see my account balance directly on the home screen,
> **so that** I can check my finances at a glance without extra taps.
>
> 作为手机银行用户，我希望在主屏直接看到账户余额，以便无需繁琐点击即可随时了解财务状况。

**这张卡做对了什么**：

- 明确**角色**（mobile banking customer，不是"用户"笼统词）。
- 明确**价值**（at a glance、without extra taps）。
- 刻意不写"如何"：没有缓存策略、没有 API 细节、没有字体字号。

**这张卡不足以落地的部分**：

- 未登录时余额是否显示？
- 后端超时如何降级？
- 余额刷新频率？
- 多账户 / 多币种 UI？

→ 这些属于 **AC + EARS 级规约** 的职责，应在"对话"阶段补齐。详见 [topic-03-ears-tutorial.md](topic-03-ears-tutorial.md) §4.1 的 EARS 补齐示例。

---

## 5. 反模式 → 重构对照

### 反例 A：故事写成伪规格（Valuable / Negotiable 违反）

**坏例**：
> 作为后端工程师，我希望把 `/api/v2/order` 的返回码从 200 改为 201，并把 `user_id` 字段移到响应头 X-User-ID，以便前端团队适配新规范。

**问题**：
- **角色错位**：后端工程师不是产品的用户。
- 全是技术细节，无商业价值。
- Negotiable = 0，已经写成验收清单。

**重构**：
- 这根本不是 Story，应降级为 **技术任务（task）** 或放入 **Enabler Story**：
  > *As the API Platform team, we need the Order API v2 to emit REST-compliant status codes and standardized identity headers, so that future SDK consumers can integrate without per-endpoint workarounds.*
  > 再在 AC 里列技术细节。

### 反例 B：NFR 硬塞入 Story 模板（Testable / Valuable 违反）

**坏例**：
> 作为用户，我希望 App 足够快、足够安全、足够可靠，以便我能愉悦地使用它。

**问题**：
- 三个非功能性需求堆一起；没有任何可测指标。
- INVEST 中 **T**estable 直接失败。

**重构**（两条路都对，看场景选）：

1. **拆分为多条独立 NFR 或 EARS Ubiquitous**（详见 [topic-03-ears-tutorial.md](topic-03-ears-tutorial.md) §3 模式 1）：
   > *The App shall load the home screen within 1.5 s at P95 under 4G network.*
2. **保留 Story 外壳，NFR 入 AC**：
   > *As a returning user, I want the home screen to load quickly, so that I can start using the app without waiting.*
   > **AC**：`Given 4G network, When launching the app, Then the home screen is interactive within 1.5 s at P95.`

**教学点**：Story 模板**不是万能载体**；NFR 常需外溢到 EARS 或明确 AC。

---

## 6. 典型场合 vs 不适用场合

### 适用（Story 发光的地方）

- 产品 Discovery / 价值假设验证。
- Backlog 优先级排序、跨职能对齐、Sprint 计划。
- 需要**同理心**与**留白**促对话的早期阶段。

### 不适用（需要让位或外溢）

- **安全关键 / 合规证明**：ASIL、FDA、HIPAA 等场景，需 EARS / 形式化（详见 [topic-03-ears-tutorial.md](topic-03-ears-tutorial.md) §4.2）。
- **LLM 代码生成输入**：模糊 Story 易致幻觉与弱边界；需结构化补齐（详见 [topic-04-future-trends-and-evidence.md](topic-04-future-trends-and-evidence.md)）。
- **深度后端 / 平台内部契约**：用 Enabler Story + API 契约 + EARS 更清晰。
- **性能 / 安全 NFR 主导**：同反例 B。

## 7. 与周边实践的配合

- **3C**（§2.1）：Card 是占位符；Conversation 才是需求的真正承载；Confirmation（AC）是完成证明。
- **Story Map**（Patton 2014）：用二维地图解决故事之间依赖不可见。
- **Example Mapping**（Matt Wynne）：在 Story 与 AC 之间加一层"规则 + 例子 + 问题"卡片，是从 Story 走向 Gherkin 的标准桥梁（详见 [topic-05-integration-bdd-selection.md](topic-05-integration-bdd-selection.md)）。

## 8. 待补文献与检索方向

- Mike Cohn《User Stories Applied》(2004)、《Agile Estimating and Planning》：经典教材，原文未直引。
- Jeff Patton《User Story Mapping》(2014) 与相关演讲。
- Alistair Cockburn 原始博文 / 演讲"A promise for a conversation"。
- **AI 生成 Story** 实证：原文 [15][35][52]（与 Topic 4 重叠）。

## 9. 本 Topic 参考文献（摘自原文编号）

见 [references-by-topic.md](references-by-topic.md) 中 **Topic 2**；完整条目见 [references-full.md](references-full.md)。

**编号快查：** 1, 3, 4, 5, 15, 19, 35, 52

## 10. Deep Research 查询种子

**英文**：

1. `"user story" Kent Beck C3 project 1997 origin history`
2. `INVEST criteria examples violations anti-patterns 2024..2026`
3. `"Example Mapping" Matt Wynne user story acceptance criteria workshop`
4. `user story non-functional requirements NFR anti-pattern how to handle`
5. `LLM generated user stories quality INVEST assessment empirical`

**中文**：

1. `User Story 起源 Kent Beck C3 克莱斯勒 历史`
2. `INVEST 原则 常见违反 重构 案例`
3. `用户故事 验收标准 AC Gherkin 分层 实践`
4. `用户故事 NFR 非功能性需求 反模式 重构`
5. `User Story 与 Job Story 区别 Klement`

## 11. 交叉引用

- 范式背景：← [topic-01-re-landscape-and-paradigm-map.md](topic-01-re-landscape-and-paradigm-map.md)
- EARS 对照 / Story 之外的契约层：→ [topic-03-ears-tutorial.md](topic-03-ears-tutorial.md)
- Story → BDD 交付管道：→ [topic-05-integration-bdd-selection.md](topic-05-integration-bdd-selection.md)
- LLM 与 INVEST 工具：→ [topic-04-future-trends-and-evidence.md](topic-04-future-trends-and-evidence.md)
- 高流量断言可信度：→ [claims-audit.md](claims-audit.md)

## 12. 历史摘要（保留，不修改）

- 本主题的历史正文保留在 §1–§11：它系统介绍了 User Story 的起源、模板、INVEST、常见反模式、与 EARS/Gherkin 的边界、以及 worked example。

## 13. 本轮新增证据

- 书级与原始方法锚点已经补齐：[`_reference/02-user-story-cohn-book-excerpts.md`](_reference/02-user-story-cohn-book-excerpts.md)、[`_reference/02-user-story-wake-invest-original.md`](_reference/02-user-story-wake-invest-original.md)、[`_reference/02-user-story-mike-cohn-ai-era.md`](_reference/02-user-story-mike-cohn-ai-era.md)。
- 起源与边界链条已经从“XP 传统说法”推进到有一手或近一手支持：
  - [`_reference/02-user-story-xp-origins-cockburn-boundary.md`](_reference/02-user-story-xp-origins-cockburn-boundary.md)
  - [`_reference/02-user-story-beck-planning-xp-previews.md`](_reference/02-user-story-beck-planning-xp-previews.md)
  - [`_reference/02-user-story-rose-user-stories-bdd-origin-boundary.md`](_reference/02-user-story-rose-user-stories-bdd-origin-boundary.md)
- Story Smells / `What Stories Are Not` 已从目录推断推进到 preview、publisher-level taxonomy、discussion-level smell、practice taxonomy：
  - [`_reference/02-user-story-cohn-2004-intro-slides.md`](_reference/02-user-story-cohn-2004-intro-slides.md)
  - [`_reference/02-user-story-cohn-story-smells-preview.md`](_reference/02-user-story-cohn-story-smells-preview.md)
  - [`_reference/02-user-story-cohn-story-smells-informit-toc.md`](_reference/02-user-story-cohn-story-smells-informit-toc.md)
  - [`_reference/02-user-story-cohn-too-small-stories-2024.md`](_reference/02-user-story-cohn-too-small-stories-2024.md)
  - [`_reference/02-user-story-mountain-goat-common-problems-taxonomy.md`](_reference/02-user-story-mountain-goat-common-problems-taxonomy.md)
- subtype / adjacent work item 边界已 starter-covered：[`_reference/02-user-story-subtypes-job-spike-enabler.md`](_reference/02-user-story-subtypes-job-spike-enabler.md)。

## 14. 本轮新增机制理解

- User Story 的核心机制进一步被锁定为：`card/text -> conversation -> confirmation`。模板只是入口，不是本体。
- 因此，本主题现在可以更稳地把 Story 定位为“价值对齐与协作载体”，而不是写作格式竞赛里的赢家；细节、约束、异常、规则、可执行示例都应外溢到更合适的工件。
- `What Stories Are Not` 与 `Story Smells` 的新证据强化了这一点：方法论自身从书级别就承认 Story 不是 written contract、不是 fixed software requirement、不是 use case，也会产生系统性的坏味道。

## 15. 本轮新增趋势与难点

- AI 时代没有消灭 User Story，反而让其职责更清晰：Story 继续承载 why / value / conversation，具体约束下沉到 AC、Gherkin 或 EARS。
- Chapter 14 full-discussion 与 Beck verbatim full text 仍然缺合法公开强源；本轮多次 targeted search 后，这个 gap 被正式 deferred，而不是被弱摘要“假装解决”。
- subtype 边界虽已 starter-covered，但跨框架统一标准仍不存在；不要把 Job Story / Spike / Enabler 写成单一 canonical taxonomy。

## 16. 当前判断（本轮综合后）

- Topic 02 现在可以稳写成：
  - `xp-roots-supported`
  - `cockburn-boundary-supported`
  - `beck-planning-game-adjacent-supported`
  - `story-bdd-boundary-supported`
  - `direct-story-smell-preview-supported`
  - `story-smells-taxonomy-toc-supported`
  - `one-story-smell-discussion-supported`
  - `multi-problem-story-taxonomy-supported`
  - `chapter-14-full-discussion-pending`
  - `beck-verbatim-full-text-pending`
- 因而本主题的当前判断是：User Story 在 AI 时代没有死亡，但职责被进一步收敛为上游意图与对话层；如果把它当成完整规格或可执行契约，反而最容易制造坏味道。
