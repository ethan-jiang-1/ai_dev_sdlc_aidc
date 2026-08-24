# INCOSE Guide to Writing Requirements (GtWR) v4 — Summary Sheet & 42-Rule Overview

- source_url: `https://www.incose.org/publications-library/product-details?productid=2bfc20a2-f35b-ef11-8473-002248009cd0`（产品页 / Access：member-only full PDF）+ `https://www.incose.org/resource/webinar-168-guide-to-writing-requirements-version-4/`（Webinar 168 概览）+ `https://www.incose.org/wp-content/uploads/2026/01/webinar_168_wheatcraft_guide_to_writing_requirements_version_4.pdf`（official webinar presentation PDF, publicly reachable, 2026-04-18 抓取）+ 官方 Summary Sheet PDF `https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose_rwg_gtwr_v4_summary_sheet.pdf`（Cloudflare 墙，2026-04-17 直抓被拦）+ 结构性重述 `https://reqi.io/articles/incose-requirements-quality-42-rule-guide`
- source_type: `standard + guide`（GtWR 是 INCOSE 的 Technical Product，与 ISO/IEC/IEEE 29148:2018 在技术社群中并列使用）
- accessed_at: `2026-04-17`
- related_topic: `shared (01 re-landscape, 02 user-story, 03 ears, 05 integration-bdd, 06 agent-format)`
- trust_level: `official（INCOSE 本体，RWG 出品）+ practitioner（reqi.io 二次重述）`
- tier: `A`（INCOSE 官方技术产品）+ 二次证据为 `C`（practitioner 重述，用于补全 Cloudflare 下无法直抓的细粒度规则表）
- why_it_matters: 本轮所有研究线都要回到"需求质量"这条基线；GtWR v4 是 2023-06 后的 **最新官方基线**，其 15 条特征 + 42 条规则 + 42 条规则 / 4 层实体的交叉矩阵，是 Topic 01（范式地图）、Topic 03（EARS ↔ INCOSE 逐条映射）、Topic 05（选型矩阵）、Topic 06（agent 格式 vs 需求质量）共同的证据锚点。
- captured_excerpt: `yes`
- claims_supported: GtWR v4 为 2023-06 发布且 INCOSE-TP 编号为 `INCOSE-TP-2010-006-04`；official webinar presentation 公开确认 GtWR v4 为 144 pages、包含 42 rules、Appendix C/D/E（patterns + rule applicability matrix + cross-reference matrices），并显式把 EARS 列为 commercialized conditional-clause approach；GtWR v4 与 ISO/IEC/IEEE 29148、INCOSE SE Handbook v5、Needs & Requirements Manual (NRM)、Guide to Verification and Validation (GtVV) 一致化；R1 / R11 / R18 / R27 / R28 与 conditional clauses directly related；R1 的官方立场是 structured statements / approved pattern，R27/R28 的 "Explicit Conditions" 与 "Multiple Conditions" 为 EARS 的 `When / While / If / Where` 提供语义对齐点。
- date_scope: GtWR v4 publication date = 2023-06（出版）/ 2023-07（INCOSE-TP 文档日期）；上代 v3.1 = 2022-05；Summary Sheet 2022 版本曾作为 v3.1 附件独立提供
- related_entities:
  - 机构：INCOSE Requirements Working Group (RWG)
  - 文件编号：`INCOSE-TP-2010-006-04`
  - 作者：Lou Wheatcraft、Rick Zinni、Jeremy Dick、Kathy Baksa、Tim Kerby
  - 配套产品：Needs & Requirements Manual (NRM, INCOSE-TP-2021-002-01.1, 2022)、Guide to Needs and Requirements (GtNR)、Guide to Verification and Validation (GtVV)、INCOSE Systems Engineering Handbook v5
  - 对齐标准：ISO/IEC/IEEE 29148:2018、ISO/IEC/IEEE 15288:2015

## 关键事实

1. **版本与编号**：`INCOSE-TP-2010-006-04` = Guide to Writing Requirements, **Version 4**, June 2023。official webinar presentation 进一步确认：V4 released in June 2023，正文 `144 pages`，另有 `7-page Summary Sheet`。
2. **同系列产品**：GtWR 与 **Needs and Requirements Manual (NRM)**、**Guide to Needs and Requirements (GtNR)**、**Guide to Verification and Validation (GtVV)**、**INCOSE SE Handbook v5** 在 RWG 内部有一致化约束。下游凡涉及 INCOSE 术语（need vs requirement vs expression）必须以 NRM + GtWR 一体为准。
3. **两层对象，一套特征**：well-formed 特征分 **语句级（C1–C10）** 与 **集合级（C11–C15）** 两类，共 15 条（下方 §核心内容摘录.特征表）。
4. **42 条规则 / 12 类**：official webinar presentation 的 cross-reference matrix 公开给出 rule titles 与分组：Accuracy (R1–R9)、Concision (R10–R11)、Non-Ambiguity (R12–R17)、Singularity (R18–R23)、Completeness (R24–R25)、Realism (R26)、Conditions (R27–R28)、Uniqueness (R29–R30)、Abstraction (R31)、Quantifiers (R32)、Tolerance (R33)、Quantification/Uniformity/Modularity (R34–R42)。
5. **7 页 Summary Sheet**：INCOSE 单独提供 GtWR v4 Summary Sheet（7 页 PDF），包含 **定义 + 特征清单 + 规则清单 + 可附加属性清单 + 交叉参照矩阵**；该 Summary Sheet 本身也是 INCOSE 出品并有编号。
6. **R1 + 条件子句 = EARS 接口**：official webinar presentation 明确列出 conditional clauses 相关规则为 `R1 Structured Statements`, `R11 Separate Clauses`, `R18 Single Thought Sentence`, `R27 Explicit Conditions`, `R28 Multiple Conditions`，并直接写出该概念 `has been commercialized in approaches such as "EARS"`。
7. **R27 / R28 = Explicit / Multiple Conditions**：R27 要求"触发条件必须显式写出"、R28 要求"多条件下必须明确命题结构（AND / OR）"——二者合读即 EARS 的 `When / While / If-Then / Where` + 复合模式的需求质量侧依据。
8. **R31 = Solution-Free**：INCOSE 明确区分"what vs how"，把 **需求** 与 **架构约束** 分层。这与 User Story 的"intent on the customer side"有结构性对应。
9. **R32 = "Each" over "All / Any / Both"**：这条常被忽略的规则是 **INCOSE 自己**抑制量词歧义的显式约定；任何 agent 生成的 EARS 要通过 GtWR 检测，必须满足此项。
10. **R16 = Avoid "Not"**：GtWR 倾向正向可验证语句；因此 EARS 的 Unwanted mode（"If … then the system shall …"）必须把"失效 / 越界"的处置写成 **正向动作**，而非 "shall not X"。

## 核心内容摘录

### 特征表（15 条，分两层）

语句级特征（对单个 need / requirement statement）：

| # | 名称 | 要点 |
|---|------|------|
| C1 | Necessary | 定义满足生命周期概念 / 上层需求 / 上层约束所必需的能力、特征、约束或质量因素 |
| C2 | Appropriate | 抽象层次与所指实体匹配（system / segment / subsystem / component）|
| C3 | Unambiguous | 所有既定听众只能得到一种解读 |
| C4 | Complete | 不需要外部放大即足以描述所需能力 |
| C5 | Singular | 单一能力 / 特征 / 约束 / 质量因素 |
| C6 | Feasible | 可在实体约束下以可接受风险实现 |
| C7 | Verifiable / Validatable | 结构允许 verify / validate 实现 |
| C8 | Correct | 是对其转换来源（上层 need / requirement / source）的准确再现 |
| C9 | Conforming | 遵从经批准的模式与风格（与 R1 直接联动）|
| C10 | (位置保留) | v4 将部分特征重分组；以官方 Summary Sheet 为准 |

集合级特征（对 requirement set）：

| # | 名称 | 要点 |
|---|------|------|
| C11 | Complete | 集合独立说明所有必要方面 |
| C12 | Consistent | 不冲突，语言同质 |
| C13 | Feasible | 集合整体可在约束下可接受风险实现 |
| C14 | Comprehensible | 读者清楚实体与关系 |
| C15 | Able to be Validated | 集合整体可 validate 达成目标 |

> 注：reqi.io 的重述里列出 15 条并在编号上略有偏移（把 references 列为 1）；以上表格以 INCOSE 官方分层（语句级 / 集合级）还原。涉及精确引用任意一条时，**必须对回 INCOSE 官方 Summary Sheet**（我们目前因 Cloudflare 暂未直抓）。

### 42 规则 / 12 类（按官方 webinar matrix + reqi 细节对照）

1. **Accuracy (R1–R9)**
   - R1 Structured Statements：符合且仅符合一个约定的模式（pattern）。
   - R2 Active Voice：主动语态，责任实体作主语。
   - R3 Appropriate Subject-Verb：主语与需求层级匹配。
   - R4 Defined Terms：所有术语落在术语表 / 数据字典。
   - R5 Definite Articles：用 "the …" 指特定实体，而非 "a …"。
   - R6 Common Units of Measure：一致的量纲与单位制。
   - R7 Vague Terms：禁用 "adequate / reasonable / user-friendly / fast" 等。
   - R8 Escape Clauses：禁用 "where possible / as appropriate / if necessary"。
   - R9 Open-Ended Clauses：禁用 "including but not limited to / etc."。
2. **Concision (R10–R11)**
   - R10 Superfluous Infinitives：禁用 "shall be able to / shall be capable of"。
   - R11 Separate Clauses：一条件一从句。
3. **Non-Ambiguity (R12–R17)**
   - R12 Correct Grammar；R13 Spelling；R14 Punctuation；R15 Logical Expressions（用 `[X AND Y]` / `[X OR Y]` 等约定）；R16 Use of "Not"（避免）；R17 Oblique "/" symbol（避免）。
4. **Singularity (R18–R23)**
   - R18 Single Thought Sentence；R19 Combinators（避免用 and / or / then / unless 连接多事件）；R20 Purpose Phrases（rationale 放属性，不进语句）；R21 Parentheses（避免）；R22 Enumeration（显式列举，不用集合名词）；R23 Supporting Diagrams（复杂行为引用图 / ICD）。
5. **Completeness (R24–R25)**
   - R24 Pronouns（避免 it / they / this / that）；R25 Headings（不能靠标题补意义）。
6. **Realism (R26)**：避免 "100% / always / never" 类不可验证绝对词。
7. **Conditions (R27–R28)**
   - R27 Explicit Conditions：条件写在语句内，不由上下文推断。
   - R28 Multiple Conditions：显式命题结构（AND / OR）。
8. **Uniqueness (R29–R30)**
   - R29 Classification（按问题域 / 子系统分组）；R30 Unique Expression（每条只出现一次）。
9. **Abstraction (R31) Solution-Free**：需求描述 "what" 不绑定 "how"。
10. **Quantifiers (R32) Universal Qualification**：用 "each" 取代 "all / any / both"。
11. **Tolerance (R33) Range of Values**：用区间代替单点。
12. **Quantification / Uniformity / Modularity (R34–R42)**
    - R34 Measurable Performance；R35 Temporal Dependencies；
    - R36 Consistent Terms & Units；R37 Acronyms；R38 Abbreviations；R39 Style Guide；R40 Decimal Format；
    - R41 Related Requirements（相关需求聚类）；R42 Structured Sets（统一模板）。

### 典型对照示例（来自 reqi.io 重述，对 R1 / R7 / R26 / R27 / R31 / R33 的高保真再现）

| 规则 | 反例 | 合规示例 |
|------|------|----------|
| R1 Structured Statements | "The system should work fast" | "When processing user queries, the Database_System shall return search results within 2.0 ± 0.5 seconds" |
| R7 / R34 Vague Terms / Measurable Performance | "The system shall have good response" | "The Order_Service shall return order details within 2.0 ± 0.3 seconds at the 95th percentile, measured under 500 concurrent users" |
| R26 Absolutes | "The system shall have 100% availability" | "The system shall have ≥99.9% availability during operational hours" |
| R27 Explicit Conditions | "The system shall encrypt data" | "When transmitting customer records over public networks, the system shall encrypt data using AES-256" |
| R31 Solution-Free | "The system shall use a MySQL database" | "The system shall store customer records with 99.9% data availability" |
| R33 Range of Values | "Response time shall be 2.0 seconds" | "Response time shall be 2.0 ± 0.3 seconds" |

### 2026-04-18 升级说明

本文件已从“主要依赖 reqi.io 二次重述”升级为“**official webinar presentation + reqi 细节补全**”的组合：

1. official webinar presentation 公开确认了：
   - V4 发布时间
   - 144-page 正文结构
   - 7-page summary sheet 的存在
   - 42 rules
   - Appendix C/D/E
   - conditional clauses 与 EARS 的官方关系
   - rules-to-characteristics cross-reference matrix
2. 仍然**没有**拿到 INCOSE Store 中的 full technical product PDF，因此 rule definitions / elaborations / full examples 仍未达到逐条 verbatim capture。
3. 因此当前正式决定是：
   - **接受**：Topic 03 / 05 / 06 在 Wave 1 / Wave 2 中可使用本文件作为 `officially-upgraded primer-level anchor`
   - **保留风险**：凡需要逐条 verbatim quote 或完整 Appendix D/E 细则的论证，仍标注 `full-text upgrade pending`

### 与其他 RWG 产品的关系（一致化约束）

GtWR v4 与下列产品共同构成 INCOSE 的需求工程知识体系，术语一致：

- **Needs and Requirements Manual (NRM)**（INCOSE-TP-2021-002-01.1, 2022）：提供 need / requirement / expression 的完整解释层与管理过程。
- **Guide to Needs and Requirements (GtNR)**：为 need 层提供同等地位的写作指南。
- **Guide to Verification and Validation (GtVV)**：把 R33 tolerance、R34 measurable performance 对接到 V&V 方法。
- **INCOSE SE Handbook v5**：整体工程流程参考，确保 GtWR v4 不是孤立出版。
- **外部对齐**：ISO/IEC/IEEE 29148:2018（需求工程生命周期过程）、ISO/IEC/IEEE 15288:2015（系统生命周期过程）。

## 与本研究的关系

| 研究线 | 该 reference 能直接支撑的断言 / 模块 |
|--------|-------------------------------------|
| Topic 01 `re-landscape` | 把 INCOSE GtWR v4 作为范式地图"系统契约层 / 结构化"格的**官方锚点**；与 ISO/IEC/IEEE 29148、Use Case 2.0、SysML v2 并列 |
| Topic 02 `user-story` | R31 Solution-Free、R27 Explicit Conditions → 解释 User Story 为何常显"未满足 INCOSE 语句级"的原因，并给出"AC 层接 GtWR 规则"的路径 |
| Topic 03 `ears` | EARS 五模式与 R1 / R27 / R28 / R22 的逐条对齐；EARS 与 GtWR 的"模式符合性"是 EARS 合规性的关键依据 |
| Topic 05 `integration-bdd` | 九维选型矩阵的"需求质量 / 可审核"列 → 以 42 条规则作判据；Gherkin 与 GtWR 的关系（Gherkin 本身不是 needs 文档，但 Then 子句可回引 GtWR 可验证性规则） |
| Topic 06 `agent-format` | 判断 agent 生成 spec（CLAUDE.md / AGENTS.md / Cursor Rules / Kiro spec）是否达到"系统级需求"的门槛 → 用 GtWR v4 的 R1 / R4 / R24 / R27 / R31 / R33 / R39 做清单式校验 |

## 可直接引用的术语 / 概念

- Need Statement / Requirement Statement / Requirement Expression / Requirement Set（四层对象，GtWR v4 规范化区分）。
- Pattern conformance（R1 的官方用词，是 EARS 在 INCOSE 语境的入场券）。
- Design Input Requirements（经 V&V 后的正式集合）。
- 42 Rules Cross-Reference Matrix（GtWR Summary Sheet 中的"矩阵"概念）。

## 风险与局限

1. **官方全文仍未获取**：虽然 2026-04-18 已补到 official webinar presentation，并把 42 rules/matrix 从二次重述升级到官方 presentation 级，但 INCOSE Store 正文与 Summary Sheet 本体仍未公开直抓到。对 rule definitions / elaborations / Appendix D/E 全量内容，仍需会员访问或购买。
2. **42 条规则分类编号非普适**：reqi.io 文章把规则分为 12 类并和 14 节标题交叠（Quantification Rules / Uniformity / Modularity 在其文章中合并展示），与 INCOSE 官方分类可能有轻微差异；以官方 Summary Sheet 为最终权威。
3. **"新版 v4 vs v3.1"差异未全面捕捉**：v4 主要演化点（如与 SE Handbook v5 对齐、与 NRM 一致化）来自 Edinburgh 著录的 Abstract，详细 diff 未入库。
4. **不构成许可授权**：本文件为**摘录与再表达**，引用时仍须标注 `INCOSE-TP-2010-006-04` 为原始权威。

## 交叉引用

- 研究入口：[`../../plan/dr-round-1.plan.md`](../../plan/dr-round-1.plan.md)
- 研究线 03（EARS 教程与合规）：[`../topic-03-ears-tutorial.md`](../topic-03-ears-tutorial.md)
- 研究线 06（Agent 格式实证）：[`../topic-06-agent-format.md`](../topic-06-agent-format.md)
- 断言审查：[`../claims-audit.md`](../claims-audit.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)（本 reference 在 `00-shared` 分组）
