# Topic 1 — 需求工程背景与范式地图（User Story / EARS 之外的"还有什么"）

> 本文件面向 **独立 Deep Research** 使用：建立需求表达的全景坐标系，作为 Topic 2–5 的导航底图。本文件有意**不**展开任何单一范式的教程细节，那些在 Topic 2 / 3 / 5 中。

## 研究问题（Deep Research 入口）

1. 在**准确性 / 可验证性**与**跨团队沟通灵活性**之间，需求工程历史上形成了哪些主要回应策略？各自的**抽象层级**与**默认受众**是谁？
2. "**用户级意图（User-level Intent）**"与"**系统级契约（System-level Contract）**"这对坐标，如何映射到常见制品（SRS、Use Case、User Story、结构化自然语言、BDD、形式化片段）？
3. 除 User Story 与 EARS 外，**范式地图**上还应包含哪些条目？各自典型适用域、取舍与工具生态是什么？
4. **MBSE / SysML**、**形式化方法**（TLA+、Alloy、B-Method）与文本型需求（EARS）在实践中的位置关系？

## 原文锚点（仅作坐标支撑，细节见对应 Topic）

| 章节 | 主题 |
|------|------|
| §1 引言 | RE 基础地位；User Story 主流性；安全关键与 LLM 时代的精确性张力 |
| §2 开篇 | 两种认识论：人类意图 + 商业价值 vs 严密系统契约 |
| §2.1（点）| User Story / XP / Planning Game → Topic 2 |
| §2.2（点）| EARS / Rolls-Royce / RE09 → Topic 3 |
| §3 段首 | 意图驱动 vs FSM / 事件驱动映射 |
| §5 段首 | System-level Contract vs User-level Intent 的"维数"表述 |

---

## 1. 双坐标系

```
                  ↑  系统契约（精确、可验证、机器可读）
                  │
   形式化方法 ────┤──── EARS  ──── INCOSE GTWR
   (TLA+/Alloy)  │
                 │      ↑
                 │   结构化自然语言
                 │      ↓
   Use Case ────┤──── 验收标准 ──── Gherkin (BDD)
                 │      ↑
                 │      │
                 │   叙事自然语言
                 │      ↓
   User Story ──┤──── Job Story ──── Story Map
                 │
                 ↓  用户意图（人本、探索、价值）
```

**核心观察**：User Story 与 EARS 在**同一轴**上处于不同抽象层级；**不是**互相替代关系，而是**分层**关系。Gherkin 是连接两层的可执行桥梁（见 Topic 5）。

## 2. 范式速查地图

| 范式 | 主要载体 | 抽象层级 | 默认受众 | 合规强度 | 工具生态（示例）| 在本主题包的去向 |
|------|---------|---------|---------|---------|----------------|----------------|
| **SRS**（传统软件需求规格）| 长文档 | 全层杂糅 | 业务 + 工程 + 审计 | 强 | DOORS, Polarion | Topic 1（背景）|
| **Use Case**（Jacobson）| 步骤场景 | 意图 + 行为 | 业务 + 工程 | 中 | UML 工具 | Topic 1（对照）|
| **User Story**（Beck/Cohn）| 卡片 + 对话 | 意图 | 业务 + UX | 弱 | Jira, Linear | → [Topic 2](topic-02-user-story-tutorial.md) |
| **Job Story**（Klement）| When/I want/So I can | 意图 | 产品 / 设计 | 弱 | 同上 | Topic 2（变体）|
| **EARS**（Mavin）| 受约束自然语言 | 系统契约 | 架构 / QA / 合规 | 强 | Jama, Visure, QVscribe | → [Topic 3](topic-03-ears-tutorial.md) |
| **INCOSE GTWR**（规则集）| 元规范 | 质量层 | SE / 审计 | 强 | QVscribe, specinnovations | Topic 3 + Topic 4 |
| **Gherkin / BDD**（Cucumber）| Given-When-Then | 可执行验收 | QA / Dev | 中 | Cucumber, SpecFlow | → [Topic 5](topic-05-integration-bdd-selection.md) |
| **Example Mapping**（Wynne）| 规则+例子+问题卡 | 意图→验收桥 | 三方共创 | 中 | 白板 / Miro | Topic 5 |
| **Specification by Example**（Adzic）| 活文档 | 意图→验收→代码 | 全栈 | 中 | Fitnesse, Concordion | Topic 5 |
| **决策表 / 真值表**| 矩阵 | 系统逻辑 | 架构 / QA | 中 | 电子表格, DMN 引擎 | Topic 3（何时退出 EARS）|
| **形式化方法**（TLA+, Alloy, B）| 数学 | 系统 + 算法 | 研究 / 关键系统 | 极强 | TLC, Alloy Analyzer | Topic 1（外部补全）|
| **MBSE / SysML**| 图 + 模型 | 系统 | SE | 强 | Cameo, Capella | Topic 1（外部补全）|

> 本表为"速查版"；Deep Research 时请为每一行独立补充：定义、代表文献、典型失败模式、与 EARS/Story 的接口。

## 3. 决策坐标（何时倾向哪一种）

- **探索早期 / 价值未验证** → Story / Job Story
- **面向最终用户的体验规格** → Story + AC（可 Gherkin）
- **微服务间的技术契约** → EARS + API Schema（OpenAPI / Protobuf）
- **NFR / 性能 / 安全约束** → EARS Ubiquitous
- **异常流 / 降级** → EARS Unwanted
- **复杂布尔 / > 3 前置条件** → 决策表或 DMN
- **核心算法 / 控制律** → 数学公式 / 伪代码
- **安全关键 / 功能安全合规** → EARS + INCOSE GTWR + 形式化补强
- **AI 辅助代码生成** → 结构化 Prompt（EARS 或受控自然语言），Story 降级为上游意图层

## 4. 待补文献与检索方向（原文未展开）

- **Use Case 2.0**（Jacobson 2011）：敏捷版 Use Case，与 Story 的边界争论。
- **Job Stories**（Klement, Intercom）：对 Persona 固化的反弹。
- **Specification by Example**（Gojko Adzic）：活文档与 BDD 的系统化论述。
- **ISO/IEC/IEEE 29148**：需求工程国际标准，与 INCOSE GTWR 的关系。
- **MBSE + SysML v2**（2024 发布）：与文本需求的分工。
- **Formal methods industrial adoption**：AWS TLA+、Amazon DynamoDB 等案例。

## 5. 本 Topic 参考文献（摘自原文编号）

见 [references-by-topic.md](references-by-topic.md) 中 **Topic 1**；完整条目见 [references-full.md](references-full.md)。

**编号快查：** 1, 2, 14, 24, 26, 44

## 6. Deep Research 查询种子

**英文**：

1. `requirements engineering paradigms landscape map user story vs use case vs EARS comparison 2023..2026`
2. `"Use Case 2.0" Jacobson agile adaptation boundary with user story`
3. `ISO IEC IEEE 29148 requirements specification relationship INCOSE GTWR`
4. `MBSE SysML v2 textual requirements integration EARS`
5. `formal methods industrial adoption TLA+ AWS DynamoDB requirements`

**中文**：

1. `需求工程 范式 地图 用户故事 用例 EARS 对比 综述`
2. `Use Case 2.0 Jacobson 敏捷用例 与 用户故事 边界`
3. `ISO 29148 需求工程 标准 INCOSE 关系`
4. `MBSE SysML 文本需求 分工 实践`
5. `形式化方法 工业应用 TLA+ 案例`

## 7. 交叉引用

- 教程深度：→ [topic-02-user-story-tutorial.md](topic-02-user-story-tutorial.md)、[topic-03-ears-tutorial.md](topic-03-ears-tutorial.md)
- 对照、BDD 管道与综合选型：→ [topic-05-integration-bdd-selection.md](topic-05-integration-bdd-selection.md)
- 趋势与前瞻揣测：→ [topic-04-future-trends-and-evidence.md](topic-04-future-trends-and-evidence.md)
- 原文断言可信度审查：→ [claims-audit.md](claims-audit.md)

## 8. 历史摘要（保留，不修改）

- 本主题的历史正文保留在 §1–§7：它提供范式地图、双坐标系、速查表、决策坐标、待补文献与原始查询种子，作为 User Story / EARS / BDD / MBSE 的导航底图。

## 9. 本轮新增证据

- 系统工程与生命周期主锚已经补齐：[`_reference/01-re-landscape-sebok-system-requirements-definition.md`](_reference/01-re-landscape-sebok-system-requirements-definition.md)、[`_reference/01-re-landscape-iso-iec-ieee-15288-2023-overview.md`](_reference/01-re-landscape-iso-iec-ieee-15288-2023-overview.md) 说明 Topic 01 不应只讨论“文体”，而应放回 requirements definition 与 system lifecycle processes 的过程框架中。
- Use Case 2.0 官方边界已经补齐：[`_reference/01-re-landscape-use-case-2-0-official.md`](_reference/01-re-landscape-use-case-2-0-official.md) 说明 use-case slices 与 story 不是互斥关系，而是面向不同复杂度与切片尺度的表达方式。
- SysML v2 / MBSE 主锚已经从“存在一个新标准”推进到“定位 + 工具 + 外部 adoption / transition signal + 非国防 validation signal”：
  - [`_reference/01-re-landscape-omg-sysml-v2-official.md`](_reference/01-re-landscape-omg-sysml-v2-official.md)
  - [`_reference/01-re-landscape-omg-sysml-v2-tools-ecosystem.md`](_reference/01-re-landscape-omg-sysml-v2-tools-ecosystem.md)
  - [`_reference/01-re-landscape-dod-sysml-v2-transition-guidance.md`](_reference/01-re-landscape-dod-sysml-v2-transition-guidance.md)
  - [`_reference/01-re-landscape-collins-sysml-v2-provers.md`](_reference/01-re-landscape-collins-sysml-v2-provers.md)
  - [`_reference/01-re-landscape-incose-automotive-sysml-v2-case-metadata.md`](_reference/01-re-landscape-incose-automotive-sysml-v2-case-metadata.md)
  - [`_reference/01-re-landscape-sysml-v2-update-end-user-orgs.md`](_reference/01-re-landscape-sysml-v2-update-end-user-orgs.md)
  - [`_reference/01-re-landscape-productive40-sysml-v2-validation-use-case.md`](_reference/01-re-landscape-productive40-sysml-v2-validation-use-case.md)

## 10. 本轮新增机制理解

- Topic 01 的地图现在应显式区分“需求表达工件”与“系统工程层级”：Story、Use Case、EARS、BDD、decision table、formal methods、SysML v2 并不是简单平铺同类项，而是在不同抽象层级、不同默认受众、不同 verification 强度上的组合。
- SysML v2 的价值不能被误写成“取代文本需求”。更稳的理解是：它为 requirements / behavior / structure relationships 提供模型层表达，并与文本型 requirements、examples、traceability artifacts 形成互补。
- 因此，本主题对 Topic 2/3/5 的外溢作用是：把“Story vs EARS”从二元对立改写成“意图层 / 契约层 / 示例层 / 模型层”的多层地图。

## 11. 本轮新增趋势与难点

- SysML v2 轴已经从“OMG 正式发布的新标准”推进到“有官方工具生态、外部 transition guidance、defense-industry signal、非 defense participation signal 与 validation signal”，但仍缺 public production rollout / quantified outcome。
- 这意味着 Topic 01 现在最重要的 residual risk 已不再是“有没有 adoption signal”，而是“能否把 metadata / participation / validation / transition 写成真正的 production maturity”。本轮多次 targeted search 后，该 gap 明确保留。
- 形式化方法、decision-table / DMN 在大地图中的独立位置仍待补强；当前 Topic 01 只能把它们作为需要继续 formalize 的外部补完层，而非已完成的地图区域。

## 12. 当前判断（本轮综合后）

- 本主题的最终地图判断应写成：User Story、Use Case 2.0、EARS、BDD/Gherkin、decision tables / DMN、formal methods、SysML v2 分别占据不同层级与职责，不是“哪种格式全面优于另一种格式”。
- SysML v2 现在可以稳写成：
  - `official-positioning-supported`
  - `tool-ecosystem-supported`
  - `external-transition-guidance-supported`
  - `defense-industry-signal-supported`
  - `non-defense-official-case-metadata-supported`
  - `multi-org-non-defense-participation-supported`
  - `non-defense-validation-supported`
  - `production-outcome-maturity-pending`
- 因而 Topic 01 已足以作为全包的“导航底图”，但还不应把 SysML v2 2026 写成广泛 public production maturity 已被证明。
