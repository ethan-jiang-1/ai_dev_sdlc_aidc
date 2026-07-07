# ISO/IEC/IEEE 29148:2018 — Systems and software engineering — Life cycle processes — Requirements engineering

- source_url: `https://www.iso.org/standard/72089.html`（ISO 编目页 / 购买入口）+ `https://standards.ieee.org/ieee/29148/6937/`（IEEE SA 官方页）+ `https://ieeexplore.ieee.org/document/8559686`（IEEE Xplore 索引页）
- source_type: `standard`（国际联合标准，ISO + IEC + IEEE 三方发布）
- accessed_at: `2026-04-17`
- related_topic: `shared (01 re-landscape, 02 user-story, 03 ears, 04 future-trends, 05 integration-bdd, 06 agent-format)`
- trust_level: `official`（ISO + IEC + IEEE 联合）
- tier: `A`
- why_it_matters: 该标准是 **"什么叫需求、如何工程化管理需求"** 的国际统一答案。本轮任何跨范式判断（User Story / EARS / Use Case / BDD / Agent spec）若不回到这里做术语与过程对齐，都会停留在 vendor 或 community 层叙事。原文也与 ISO/IEC/IEEE 12207:2017（软件生命周期过程）和 ISO/IEC/IEEE 15288:2023（系统生命周期过程）配套，构成"需求工程 ↔ 系统 / 软件工程生命周期"的桥接层。
- captured_excerpt: `partial`（标准全文为付费；本文件摘录 ISO / IEEE SA 官方页面可公开访问的 scope 说明、治理信息、版本沿革；下次需要正文条款时，应通过 IEEE SA 订阅 / Accuris Store 补抓正文）
- claims_supported: ISO/IEC/IEEE 29148:2018 的官方发布日期是 2018-11-30；接替 29148:2011；由 IEEE Computer Society C/S2ESC 标准委员会 + WG_LCP 工作组治理；其 scope 显式包含"定义 good requirement 构件、提供属性与特征、讨论迭代 / 递归应用"，并作为 ISO/IEC/IEEE 15288:2023 与 ISO/IEC/IEEE 12207:2017 的需求过程补充；INCOSE GtWR v4（INCOSE-TP-2010-006-04, 2023-06）在 reference 处明确与 29148:2018 对齐；与 ISO/IEC/IEEE 24748-1:2024（生命周期管理）和 ISO/IEC/IEEE 16085:2020（风险管理）同系列。
- date_scope: 标准 PAR 批准 2016-12-07；IEEE SA 板批准 2018-10-23；publication date 2018-11-30；接替 ISO/IEC/IEEE 29148:2011；当前状态 `Active Standard`（2026-04-17 证）；新一版 P29148 在 IEEE SA 立项草拟中（项目编号 12262）。
- related_entities:
  - 机构：ISO + IEC + IEEE Computer Society
  - 标委会：IEEE C/S2ESC（Software & Systems Engineering Standards Committee）
  - 工作组：WG_LCP（Working Group for Life Cycle Processes），Chair: Teresa Doran；PM: Christian Orlando
  - 前代 / 配套：ISO/IEC/IEEE 29148:2011（被接替）、ISO/IEC/IEEE 15288:2023（SLCP）、ISO/IEC/IEEE 12207:2017（SLCP）、ISO/IEC/IEEE 24748-1:2024、ISO/IEC/IEEE 15939:2017（测量过程）
  - 下游参考：INCOSE GtWR v4（INCOSE-TP-2010-006-04, 2023-06）、INCOSE Needs & Requirements Manual (NRM)

## 关键事实

1. **正式名称**：*Systems and software engineering — Life cycle processes — Requirements engineering*（ISO + IEC + IEEE 三方标准）。
2. **出版日期**：`2018-11-30`。**PAR 批准**：`2016-12-07`。**IEEE SA 板批准**：`2018-10-23`。**状态**：`Active Standard`（截至 2026-04-17）。**接替**：`ISO/IEC/IEEE 29148:2011`。
3. **Scope 原文（IEEE SA 官方复述）**：
   > "This document contains provisions for the processes and products related to the engineering of requirements for systems and software products and services throughout the life cycle. It defines the construct of a good requirement, provides attributes and characteristics of requirements, and discusses the iterative and recursive application of requirements processes throughout the life cycle. This document provides additional guidance in the application of requirements engineering and management processes for requirements-related activities in ISO/IEC/IEEE 12207 and ISO/IEC/IEEE 15288. Information items applicable to the engineering of requirements and their content are defined. The content of this document can be added to the existing set of requirements-related life cycle processes defined by ISO/IEC/IEEE 12207 or ISO/IEC/IEEE 15288, or can be used independently."
4. **适用范围**：规模、方法、复杂度不限——人造系统、软件密集型系统、软件与硬件产品、服务。项目范围无限制。
5. **治理**：IEEE Computer Society，C/S2ESC，WG_LCP（Working Group for Life Cycle Processes）。
6. **Official Edition**：2018 版取代 2011 版；new P29148 项目（IEEE SA 12262）已在起草，下版尚未发布。
7. **访问性**：全文为付费标准（ISO Store / Accuris / IEEE SA 订阅），scope + 结构在官方 catalog 页公开。
8. **与 INCOSE 的互补关系**：INCOSE GtWR v4 在 reference 处明示与 29148:2018 对齐；INCOSE NRM 中的 need / requirement / expression 术语体系是对 29148:2018 "good requirement 构件"的工程细化。

## 核心内容摘录（可公开信息层面）

### 1. 适用对象

| 对象类型 | 覆盖 |
|---------|------|
| Man-made systems | yes |
| Software-intensive systems | yes |
| Software and hardware products | yes |
| Services | yes |
| 项目规模 / 方法 / 复杂度 | 无限制 |

### 2. 内容层级

根据 scope 原文与 IEEE Xplore 官方条目，该标准至少显式覆盖：

- **需求工程过程**（processes）在生命周期中的 iterative / recursive 应用
- **"good requirement" 构件**（construct）的定义 + 属性 + 特征
- **信息项**（information items）及其内容
- 与 **ISO/IEC/IEEE 12207**（软件生命周期过程）、**ISO/IEC/IEEE 15288**（系统生命周期过程）中需求相关活动的对齐
- 可作为**独立过程**使用，也可叠加到 12207 / 15288 既有过程上

### 3. 标准编号与前代 / 后续

| 编号 | 发布年 | 关系 |
|------|--------|------|
| ISO/IEC/IEEE 29148:2011 | 2011 | 前代，已被取代 |
| ISO/IEC/IEEE 29148:2018 | 2018-11-30 | **当前活标准** |
| P29148 | 起草中（IEEE SA 12262） | 下一版，尚未发布 |

### 4. 治理结构（2026-04-17 证）

- Sponsor: IEEE Computer Society（[https://computer.org](https://computer.org)）
- Committee: C/S2ESC — Software & Systems Engineering Standards Committee
- Working Group: WG_LCP — Life Cycle Processes
- Working Group Chair: Teresa Doran
- IEEE Program Manager: Christian Orlando (c.orlando@ieee.org)

### 5. 与相关标准的组合（按 IEEE SA 最新活标准清单）

| 相关标准 | 发布 | 关系 |
|----------|------|------|
| ISO/IEC/IEEE 15288:2023 | 2023 | 系统生命周期过程（SLCP）——需求过程嵌入点 |
| ISO/IEC/IEEE 12207:2017 | 2017 | 软件生命周期过程（SLCP）——需求过程嵌入点 |
| ISO/IEC/IEEE 24748-1:2024 | 2024 | 生命周期管理 Part 1：指南 |
| ISO/IEC/IEEE 15939:2017 | 2017 | 测量过程（可支持 requirement metrics）|
| ISO/IEC/IEEE 16085:2020 | 2020 | 风险管理 |
| ISO/IEC/IEEE 15026 系列 | 2021–2025 | Systems & software assurance（等级、保证案例）|

### 6. 与下游 practitioner 指南的关系

- **INCOSE Guide to Writing Requirements (GtWR) v4 / INCOSE-TP-2010-006-04, 2023-06**：其 reference 明示 29148:2018。GtWR v4 的 42 条写作规则 = "对 29148:2018 的 good requirement 特征"的 practitioner 级展开。
- **INCOSE Needs and Requirements Manual (NRM, INCOSE-TP-2021-002-01.1, 2022)**：把 29148:2018 的"good requirement 构件 + 属性"展开为 needs / requirements / expressions 三层对象管理手册。

### 2026-04-18 升级说明

1. 本轮再次尝试获取 29148 正文级 clause text，但公开可达路径仍停留在：
   - ISO catalog / abstract
   - IEEE SA product page
   - IEEE Xplore index metadata
2. 当前环境下仍**没有**合法公开取得可引用的 clause-level 正文。
3. 因此当前正式决定是：
   - **接受**现有 catalog-level / scope-level primer coverage 作为 Topic 01 / 03 / 05 / 06 的 shared anchor
   - **保留风险**：凡需要逐条 clause wording（尤其“construct of a good requirement”具体条款）支撑的强断言，继续标注 `full-text access pending`
4. 这意味着 29148 目前在本库中的角色仍是：
   - lifecycle / scope / construct-level official anchor
   - 而不是 clause-by-clause verbatim anchor

## 与本研究的关系

| 研究线 | 该 reference 能直接支撑的断言 / 模块 |
|--------|-------------------------------------|
| Topic 01 `re-landscape` | 范式地图的**"系统契约层 / 结构化格"的官方锚点**；Use Case / EARS / User Story / MBSE 的对齐都以 29148:2018 + 15288 + 12207 为共同基线 |
| Topic 02 `user-story` | 讨论 User Story 与 "good requirement" 的关系时，必须与 29148:2018 "construct of good requirement" 对照；User Story 本质上不是 29148 意义上的 requirement |
| Topic 03 `ears` | EARS 模式在 29148:2018 中获得**"可接受的结构化模式"**的正式地位（经 INCOSE GtWR R1 Pattern Conformance 承接）|
| Topic 04 `future-trends` | 任何"AI-authored spec 是否可审计"的讨论，回到"好需求的属性 / 特征"这一基础；即 29148:2018 给出的基线不能被 AI 规避 |
| Topic 05 `integration-bdd` | 九维选型矩阵的"合规 / 可审计"列须回到 29148:2018 构件定义；User Story → AC → Gherkin 管道中，29148:2018 定义了 AC 可验证性的硬边界 |
| Topic 06 `agent-format` | 判断 CLAUDE.md / AGENTS.md / Cursor Rules / Kiro spec 是否达到"正式需求"门槛的 **最高一层参照**；若只到"项目备忘"程度，则不应当作 29148 意义上的 requirement；若要上线合规系统，需要把 agent 产出接回 29148 / GtWR 检测 |

## 可直接引用的术语 / 概念

- "Construct of a good requirement"（29148 原生术语）
- "Attributes and characteristics of requirements"（29148 原生术语）
- "Iterative and recursive application of requirements processes"（29148 原生表述）
- "Information items"（29148 对"需求产物"的抽象容器）
- 与 15288 / 12207 的"additional guidance"关系——不是替代而是补充或独立运作

## 风险与局限

1. **全文付费且本轮仍未获取**：ISO/IEC/IEEE 29148:2018 正文需通过 ISO Store / Accuris / IEEE SA 订阅获取；截至 2026-04-18，本文件仍基于 ISO + IEEE SA 官方公开页的 scope 叙述 + 治理信息。任何引用具体条款号（§5.x、§6.x）的断言必须先回到正文复核。
2. **29148 与 GtWR 的职责边界常被混用**：29148:2018 定义"工程化过程"和"需求构件"，GtWR 提供"语句级写作规则"。市面上 practitioner 文章常把两者指称交换（把 GtWR 的 42 条写作规则写成"29148 的规则"）——本库要避免这类错位。
3. **下一版本在起草**：P29148（IEEE SA 12262）已在草拟；如果本研究跨越 2026–2027 年，需跟踪草案变化（IEEE SA 的 myProject 公开目录）。
4. **不构成许可授权**：本文件仅摘录官方公开层级信息；引用时必须标注 `ISO/IEC/IEEE 29148:2018` 为原始权威来源。

## 交叉引用

- 研究入口：[`../../plan/dr-round-1.plan.md`](../../plan/dr-round-1.plan.md)
- 同组 Tier A 配对：[`00-shared-incose-gtwr-v4-summary.md`](00-shared-incose-gtwr-v4-summary.md)
- 研究线 01（范式地图）：[`../topic-01-re-landscape-and-paradigm-map.md`](../topic-01-re-landscape-and-paradigm-map.md)
- 研究线 03（EARS）：[`../topic-03-ears-tutorial.md`](../topic-03-ears-tutorial.md)
- 研究线 06（Agent 格式）：[`../topic-06-agent-format.md`](../topic-06-agent-format.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
