# Mikael Ebrahimi Salari et al. 2023 — An Experiment in Requirements Engineering and Testing using EARS Notation for PLC Systems

- source_url: `https://www.es.mdu.se/publications/6673-An_Experiment_in_Requirements_Engineering_and_Testing_using_EARS_Notation_for_PLC_Systems` + `https://www.es.mdu.se/pdf_publications/6673.pdf`
- source_type: `academic (conference/workshop paper)`
- accessed_at: `2026-04-18`
- related_topic: `03 ears (primary), 05 integration-bdd, 04 future-trends`
- trust_level: `academic`
- tier: `A`
- why_it_matters: 这是本轮最直接的近年实证材料之一。它不只是重复 EARS 五模式，而是观察人在真实建模和测试任务里如何选模式、卡在哪里、以及 EARS 生成测试在 PLC 场景里是否可用。
- captured_excerpt: `yes`
- claims_supported: `EARS 可用于 PLC 需求形式化与基于规约的测试；不同作者会为同一 NL 需求选择不同 EARS 模式；完整性是最常见问题；EARS 需求驱动的测试生成与执行在 PLC 场景中可行；optional-feature 模式在给定实验对象中未被使用。`
- date_scope: `paper year 2023; venue = 19th Workshop on Advances in Model Based Testing`
- related_entities: `Mikael Ebrahimi Salari; Eduard Paul Enoiu; Wasif Afzal; Cristina Seceleanu; Mälardalen University; CODESYS; IEC 61131-3; PLC; EARS`

## 关键事实

1. MDU 出版页将该文标注为 `Conference/Workshop Paper`，venue 为 `19th Workshop on Advances in Model Based Testing`，年份 2023。
2. 研究对象是 PLC 软件与 CODESYS 测试环境，不是通用 SaaS；因此它支撑的是“EARS 作为半形式化契约和测试输入”的可行性，而不是跨行业通用效果。
3. 实验共有 10 名参与者，任务是把 3 条自然语言需求改写成 EARS，并据此生成 PLC 测试。
4. 论文把主要研究问题分成三类：EARS 如何用于 PLC 需求与测试、参与者实际使用了哪些模式、参与者感知到哪些挑战。
5. 作者的核心结果有三点：
   - 不同参与者会以不同方式把同一条自然语言需求改写成 EARS。
   - `Completeness` 是最常见的问题。
   - 基于这些 EARS 需求进行 PLC 测试生成与执行是可行的。
6. 表 II 显示，参与者对同一需求会选不同模板；其中 RI1 几乎都选 ubiquitous，RI2/RI3 常落到 event-driven 与 unwanted behaviour，state-driven 也会出现。
7. 论文显式记录的挑战包括：原始 NL 不够完整、单模板或多模板边界不清、系统视角难确定、optional-feature 模式在这组对象上不适用。

## 核心内容摘录

### 论文摘要里的结果句

> The results of this study show that humans create requirements using semi-formal notations in distinct ways and using different patterns.

> Completeness is the most common issue when rewriting and using such requirements for testing.

> Additionally, we found that test generation and execution using these EARS requirements for PLC systems is applicable.

### 研究问题

- `RQ1`: EARS 半结构化语法与测试创建如何用于 PLC 场景
- `RQ2`: 写需求时实际使用了哪些 EARS 模式
- `RQ3`: 在需求规约和测试创建时感知到了哪些挑战

### 参与者挑战归纳

- 原始需求不完整，不足以直接决定应选哪一种 EARS 模式
- 为了同时覆盖正向与异常行为，往往需要拆成多个 EARS 需求
- 系统主语 / 视角并不总是容易从原始需求里识别出来
- optional-feature 模式并非普遍需要

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 03 `ears` | 近年实证锚点：EARS 不只是语法表，确实进入了“需求改写 + 测试设计”流程；同时补上失败模式与难点证据 |
| Topic 05 `integration-bdd` | 说明从需求表达走向测试设计时，EARS 可以承担“半形式化规约层”角色，但需要补全性和视角澄清 |
| Topic 04 `future-trends` | 支撑“结构化文本需求作为可测试中间层”这一趋势，不等于 fully executable spec，但足以进入自动化测试链路 |

## 可直接引用的术语 / 概念

- `Completeness is the most common issue`
- `distinct ways and using different patterns`
- `test generation and execution ... is applicable`
- `Conference/Workshop Paper`

## 风险与局限

1. 样本量仅 10 人，且任务时长固定为 1 小时，外推能力有限。
2. 场景严格局限于 PLC / IEC 61131-3 / CODESYS，不直接证明 EARS 在 SaaS 产品需求中同样有效。
3. 论文证明的是“可行性”和“建模挑战”，不是 KPI 级 ROI 证据。
4. 这份实证很适合作为 Topic 03 的“近年 empirical anchor”，但不能单独承担“EARS 普适有效”的总论证。

## 交叉引用

- 共享原始定义锚点：[`00-shared-mavin-2009-ears-re09.md`](00-shared-mavin-2009-ears-re09.md)
- Topic 03 seed：[`../topic-03-ears-tutorial.md`](../topic-03-ears-tutorial.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
