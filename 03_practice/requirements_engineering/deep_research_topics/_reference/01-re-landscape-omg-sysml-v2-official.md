# OMG SysML v2.0 — Official specification and MBSE requirements-modeling signal

- source_url: `https://www.omg.org/sysml/index.htm` + `https://www.omg.org/sysml/specifications.htm` + `https://www.omg.org/news/releases/pr2023/07-10-23.htm` + `https://www.omg.org/sysml/sst_aiaa_award.htm`
- source_type: `official standard / specification`
- accessed_at: `2026-04-18`
- related_topic: `01 re-landscape (primary), 04 future-trends, 03 ears`
- trust_level: `official`
- tier: `A`
- why_it_matters: Topic 01 的范式地图缺 MBSE / SysML v2 官方锚点。OMG 官方资料说明 SysML 是用于 specify / analyze / design / verify complex systems 的建模语言，SysML v2.0 在 2025 年正式采用，并提供 textual + graphical representations、requirements modeling、API/services 和 interoperability。这补上了“文本需求之外的模型化需求层”。
- captured_excerpt: `yes`
- claims_supported: `SysML` 是 general-purpose modeling language for specifying, analyzing, designing, and verifying complex systems；SysML v2.0 was adopted by OMG in June 2025；SysML v2 enables modeling of complex systems with improved precision / expressiveness / consistency / usability / interoperability / extensibility；SysML v2 includes concepts for structure, behavior, requirements, and cross-cutting relationships；it provides complementary textual and graphical representations and a standard API/services layer.
- date_scope: `SysML v2 beta approved 2023-06/07; final adoption June 2025; formal specification publication September 2025`
- related_entities: `OMG; SysML v2.0; KerML; Systems Modeling API and Services; MBSE; SysML v2 Submission Team`

## 关键事实

1. OMG SysML official page defines SysML as a language that helps teams `design, analyze, and verify complex systems` and describes it as a general-purpose modeling language.
2. OMG states that SysML v1.7 was adopted in June 2024 and the next-generation SysML v2.0 was adopted in June 2025.
3. OMG's 2023 beta announcement says the SysML v2 beta package included:
   - KerML specification
   - SysML v2 language specification
   - Systems Modeling API and Services specification
4. The same 2023 announcement says SysML v2 improves precision, expressiveness, consistency, usability, interoperability, and extensibility over SysML v1.
5. It also says SysML v2 includes modeling concepts for deeply nested hierarchies of:
   - structure
   - behavior
   - requirements
   - cross-cutting relationships
6. OMG's SysML specification page notes that SysML v2.0 current formal specification is September 2025 and defines abstract syntax, concrete syntax, semantic foundations, standard libraries, and conformance requirements.
7. OMG / SysML materials also emphasize complementary textual and graphical representations and standardized APIs/services for access, query, validation, and tool interoperability.

## 核心内容摘录

### SysML 的基本定位

- OMG official page describes SysML as a general-purpose modeling language for specifying, analyzing, designing, and verifying complex systems.

### SysML v2 的正式采用

- OMG official SysML page states SysML v2.0 was adopted in June 2025.
- The SST award page further states the specifications were formally approved by OMG in June 2025 and culminated in KerML, SysML v2, and Systems Modeling API and Services specifications.

### Requirements modeling signal

- OMG 2023 announcement states SysML v2 extends KerML to include concepts for modeling systems with nested hierarchies of structure, behavior, requirements, and cross-cutting relationships.
- This directly supports Topic 01's map: SysML v2 is not another text-template method; it is a model layer that can contain and relate requirements, behavior, architecture, verification, and analysis.

### Textual + graphical representations

- OMG 2023 announcement states SysML v2 provides complementary textual and graphical representations of the underlying model.
- This is important for AI-era workflows because textual syntax can interface with code/spec tooling while graphical representation supports systems understanding.

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 01 `re-landscape` | 补齐 MBSE / SysML v2 官方锚点，说明需求表达地图必须包含模型化 requirements layer，而不是只在 Story / EARS / BDD 文本层内打转 |
| Topic 04 `future-trends` | SysML v2 的 textual + graphical + API/services 组合支持“requirements as model / graph / tool-interoperable artifact”的趋势判断 |
| Topic 03 `ears` | EARS 是 controlled textual requirement expression；SysML v2 是模型化 requirements and system relationship layer。二者可互补而非互斥 |

## 可直接引用的术语 / 概念

- `Systems Modeling Language (SysML)`
- `SysML v2.0`
- `Kernel Modeling Language (KerML)`
- `Systems Modeling API and Services`
- `requirements`
- `cross-cutting relationships`
- `textual and graphical representations`
- `interoperability`

## 风险与局限

1. 这份 reference 锁定的是 OMG official positioning，不是某个具体工具的工程落地案例。
2. SysML v2 正在从正式采用走向工具生态成熟；2026 年的实际工具成熟度仍需另行评估。
3. 它不替代 29148/GtWR 的 textual requirement quality rules，而是补上模型化表达与 traceability / relationship layer。

## 交叉引用

- Topic 01 evidence summary：[`../_artifacts/01-re-landscape-evidence-summary.md`](../_artifacts/01-re-landscape-evidence-summary.md)
- Topic 04 trend summary：[`../_artifacts/04-future-trends-evidence-summary.md`](../_artifacts/04-future-trends-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
