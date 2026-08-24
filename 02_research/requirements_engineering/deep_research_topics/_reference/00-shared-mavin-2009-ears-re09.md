# Alistair Mavin 2009 — Easy Approach to Requirements Syntax (EARS) [RE'09]

- source_url: `https://alistairmavin.com/ears/`（作者官方指南，2026-04-17 抓取正文）+ `https://ieeexplore.ieee.org/abstract/document/5328509`（IEEE Xplore, RE'09 论文元数据 + DOI）+ `https://researchr.org/publication/MavinWHN09`（researchr 学术索引）+ `https://alastairreid.github.io/RelatedWork/papers/mavin:isre:2009/`（independent summary）+ `https://research.manchester.ac.uk/en/publications/easy-approach-to-requirements-syntax-ears/`（University of Manchester 著录）
- source_type: `academic (conference paper) + official author guide`
- accessed_at: `2026-04-17`
- related_topic: `shared (03 ears 主锚点；01 re-landscape、04 future-trends、05 integration-bdd、06 agent-format 均会引用)`
- trust_level: `official (author's own site) + academic (IEEE RE'09 peer-reviewed)`
- tier: `A`
- why_it_matters: 这是 **EARS 的原始定义文献**。所有后续 INCOSE GtWR、Jama / Visure / Inflectra、学界二次文献的 EARS 论述，必须回到 Mavin 2009 原文 + 作者官方指南对齐；否则下游会继承各种二次转述错位（例如把 EARS 当成"仅 5 种模式无复合"）。
- captured_excerpt: `yes`（官方指南正文 8 段全部摘录；RE'09 论文元数据 + 独立 summary 补充）
- claims_supported: EARS 由 Alistair Mavin、Philip Wilkinson、Adrian Harwood、Mark Novak 于 Rolls-Royce PLC 在分析喷气发动机控制系统适航规范时提出；正式发表于 2009 年 IEEE RE'09（Atlanta）；EARS 语法与关键词位置固定；基本模板为 `While <precondition>, when <trigger>, the <system name> shall <system response>`；ruleset 要求 0..N 前置条件、0..1 触发、1 系统名、1..N 系统响应；EARS 提供五种基础模式（Ubiquitous / State-driven / Event-driven / Optional Feature / Unwanted Behaviour）+ 复合模式（Complex）；EARS 被 Airbus / Bosch / Dyson / Honeywell / Intel / NASA / Rolls-Royce / Siemens 等公司采用；EARS 已在中国 / 法国 / 德国 / 瑞典 / 英国 / 美国的大学教学中使用。
- date_scope: 原论文 = 2009 年 IEEE RE'09（Atlanta, GA, USA）；作者官方指南为持续更新，当前页底版权 = 2026（本轮抓取时点与之一致）
- related_entities:
  - 作者：Alistair "Mav" Mavin（独立需求专家，德国）；Philip Wilkinson、Adrian Harwood、Mark Novak（Rolls-Royce PLC）
  - 机构来源：Rolls-Royce PLC 喷气发动机控制系统团队
  - 会议：17th IEEE International Requirements Engineering Conference (RE'09), Atlanta, GA, USA, 2009
  - 下游采纳代表：Airbus、Bosch、Dyson、Honeywell、Intel、NASA、Rolls-Royce、Siemens
  - 下游标准对齐：INCOSE GtWR v4 R1 Pattern Conformance（作为 EARS 在 INCOSE 语境合法化的接口）

## 关键事实

1. **发表**：Mavin, A.; Wilkinson, P.; Harwood, A.; Novak, M. *Easy Approach to Requirements Syntax (EARS)*. 17th IEEE International Requirements Engineering Conference (RE'09), Atlanta, 2009（IEEE Xplore DOI 映射）。
2. **设计起源**：Rolls-Royce 团队在分析喷气发动机控制系统**适航规范**时，观察到所有合格需求都遵从相同的子句顺序，遂抽象为 5 种模式 + 1 种复合。
3. **通用模板**：`While <optional pre-condition>, when <optional trigger>, the <system name> shall <system response>`。子句顺序恒定（temporal logic）。
4. **EARS ruleset（官方原文）**：
   - Zero or many preconditions
   - Zero or one trigger
   - One system name
   - One or many system responses
5. **五种基础模式 + 复合**：Ubiquitous / State-driven (`While`) / Event-driven (`When`) / Optional Feature (`Where`) / Unwanted Behaviour (`If ... then`) / Complex（组合多个关键词）。
6. **动机明确**：系统需求常以**无约束自然语言**写成；作者群体并非受过训练；问题在开发过程中向下传播，推高成本 / 排期波动。EARS 是"温和地约束"（gently constrain）而非强制形式化。
7. **工业采纳列表（作者官方列出）**：Airbus、Bosch、Dyson、Honeywell、Intel、NASA、Rolls-Royce、Siemens。
8. **学术 / 教学覆盖**：中国 / 法国 / 德国 / 瑞典 / 英国 / 美国的大学课程。
9. **定位**：轻量（light-weight）、低培训成本、无需专用工具、易读——这是 EARS 能从安全关键域**外溢**到 SaaS / AI coding agent 场景的关键条件。

## 核心内容摘录（作者官方指南 verbatim）

### 通用 EARS 语法

> "The clauses of a requirement written in EARS always appear in the same order. The basic structure of an EARS requirement is:
>
> `While <optional pre-condition>, when <optional trigger>, the <system name> shall <system response>`
>
> The EARS ruleset states that a requirement must have: Zero or many preconditions; Zero or one trigger; One system name; One or many system responses."

### 五种基础模式（官方示例）

| 模式 | 关键词 | 模板 | 官方示例 |
|------|--------|------|----------|
| Ubiquitous（恒常）| 无 | `The <system name> shall <system response>` | The mobile phone shall have a mass of less than XX grams. |
| State-driven（状态驱动）| `While` | `While <precondition(s)>, the <system name> shall <system response>` | While there is no card in the ATM, the ATM shall display "insert card to begin". |
| Event-driven（事件驱动）| `When` | `When <trigger>, the <system name> shall <system response>` | When "mute" is selected, the laptop shall suppress all audio output. |
| Optional feature（可选特性）| `Where` | `Where <feature is included>, the <system name> shall <system response>` | Where the car has a sunroof, the car shall have a sunroof control panel on the driver door. |
| Unwanted behaviour（异常 / 越界）| `If ... then` | `If <trigger>, then the <system name> shall <system response>` | If an invalid credit card number is entered, then the website shall display "please re-enter credit card details". |

### 复合模式（官方示例）

```
While <precondition(s)>, When <trigger>, the <system name> shall <system response>
```

示例：
> While the aircraft is on ground, when reverse thrust is commanded, the engine control system shall enable reverse thrust.

> 复合模式也可以叠加 `If ... then` 用于异常行为。

### 动机段（verbatim 摘录）

> "System requirements are usually written in unconstrained natural language (NL), which is inherently imprecise. Often, requirements authors are not trained in how to write requirements. During system development, requirements problems propagate to lower levels. This creates unnecessary volatility and risk, impacting programme schedule and cost. EARS reduces or even eliminates common problems found in natural language requirements. It is especially effective for requirements authors who must write requirements in English, but whose first language is not English."

### 工业采纳段（verbatim）

> "EARS is used worldwide by large and small organisations in different domains. These include blue chip companies such as Airbus, Bosch, Dyson, Honeywell, Intel, NASA, Rolls-Royce and Siemens. The notation is taught at universities around the world including in China, France, Germany, Sweden, UK and USA."

## RE'09 论文（IEEE Xplore 元数据层）

| 字段 | 值 |
|------|----|
| 标题 | Easy Approach to Requirements Syntax (EARS) |
| 作者 | Alistair Mavin, Philip Wilkinson, Adrian Harwood, Mark Novak |
| 会议 | 17th IEEE International Requirements Engineering Conference, Atlanta, GA, USA |
| 年份 | 2009 |
| 原始案例 | Rolls-Royce 喷气发动机控制系统适航规范 |
| 独立 summary（Alastair Reid） | 本文为正式发表版；独立总结站点列为"Related Work"锚点，可作二次证据 |

## 与本研究的关系

| 研究线 | 该 reference 能直接支撑的断言 / 模块 |
|--------|-------------------------------------|
| Topic 03 `ears` | **主锚点**：Mavin 五模式 + 复合模板表、ruleset、动机、工业采纳清单、教学 footprint 全部在此一份文件 |
| Topic 01 `re-landscape` | EARS 在范式地图中的身份 = "受控自然语言"与"系统契约层"的交叉点，以 Mavin 2009 为正式入口 |
| Topic 04 `future-trends` | 讨论"EARS 是 LLM 提示词范式"的论据链条，必须从 Mavin 2009 的**原始动机**（NL 不受控）出发；否则会跳过因果 |
| Topic 05 `integration-bdd` | EARS ↔ Gherkin 的关键词映射（While/When/If ↔ Given/When/Then）必须以本文档的 five-mode 表格为对齐基准 |
| Topic 06 `agent-format` | 讨论 "Cursor Rules / CLAUDE.md / AGENTS.md / Kiro spec 中应如何写约束性语句" 时，Mavin EARS 提供 ready-to-paste 模板；其**轻量、低培训成本**特征恰好匹配 agent / harness 场景 |

## 可直接引用的术语 / 概念

- EARS（Easy Approach to Requirements Syntax）
- Ubiquitous / State-driven / Event-driven / Optional Feature / Unwanted Behaviour / Complex（6 种模式，含 Complex）
- Precondition / Trigger / System name / System response（四类子句）
- "Gently constrain"（作者用词，强调轻量约束而非强制形式化）

## 风险与局限

1. **"零语义损耗映射到 Gherkin"是第三方过强表述**：Mavin 官方指南并未声称 EARS↔Gherkin 零损耗同构；原 raw_dr 文档的 §7 "同构映射"属下游夸张。引用时必须回到 Mavin 的 **"gently constrain"** 立场，避免"EARS 等于机器可执行规约"的误读。
2. **ruleset 叙述简洁但覆盖**：0..N preconditions / 0..1 trigger / 1 system / 1..N responses——该规则常被省略，但是 EARS 合规与否的硬检测项。
3. **"何时不用 EARS"未在官方指南中显式章节**：下游 practitioner 文章（如 `https://alistairmavin.com/ears/` 的延伸篇或第三方博客）补充了反例；Topic 03 的 Wave 1 需要单独拉取这类材料。
4. **案例采纳列表不等于 KPI 数据**：Airbus / Bosch / Dyson / Honeywell / Intel / NASA / Rolls-Royce / Siemens 是 **采纳事实**（作者自述），并不自证"EARS 效果"，与 claims-audit 中 §6.3 的 sMBSAP 数据（MDPI 单篇）属于不同证据类别。

## 交叉引用

- 研究入口：[`../../plan/dr-round-1.plan.md`](../../plan/dr-round-1.plan.md)
- 同组 Tier A 配对：[`00-shared-incose-gtwr-v4-summary.md`](00-shared-incose-gtwr-v4-summary.md)、[`00-shared-iso-iec-ieee-29148-2018.md`](00-shared-iso-iec-ieee-29148-2018.md)
- 研究线 03 入口：[`../topic-03-ears-tutorial.md`](../topic-03-ears-tutorial.md)
- 研究线 06 入口：[`../topic-06-agent-format.md`](../topic-06-agent-format.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
