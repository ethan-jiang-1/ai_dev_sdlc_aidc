# SEBoK 2025 — System Requirements Definition and related requirements engineering pages

- source_url: `https://sebokwiki.org/wiki/System_Requirements_Definition` + `https://sebokwiki.org/wiki/Business_or_Mission_Analysis` + `https://sebokwiki.org/wiki/Requirements_Management`
- source_type: `official body of knowledge`
- accessed_at: `2026-04-18`
- related_topic: `01 re-landscape (primary), 03 ears, 05 integration-bdd`
- trust_level: `official`
- tier: `A`
- why_it_matters: Topic 01 需要一个能把“需求工程是如何从 mission/problem 一路走到 system requirements、verification、traceability”的系统框架锚定住的来源。SEBoK 正好提供了这一层。
- captured_excerpt: `yes`
- claims_supported: `Requirements engineering` 在 SEBoK 中不是单个文档写作动作，而是从 Business or Mission Analysis、Stakeholder Needs、System Requirements Definition 到 Requirements Management 的一整套系统工程流程；system requirements 把 stakeholder view 转成 technical developer view；requirements 是 architecture, design, integration, verification 的输入。`
- date_scope: `SEBoK v2.13 released 2025-11-17; accessed 2026-04-18`
- related_entities: `SEBoK; INCOSE; System Requirements Definition; Business or Mission Analysis; Requirements Management`

## 关键事实

1. `Business or Mission Analysis` 页面明确说，它是 `the first process performed in Concept Definition`，负责界定战略问题/机会与潜在解决类。
2. 同页还说，其输出会进入 `Stakeholder Needs Definition`，说明需求工程在系统工程里起点不是“写故事”，而是 mission/problem framing。
3. `System Requirements Definition` 页面明确写道：
   - 它把 `stakeholder view of desired capabilities` 转成 `technical, developer view`
   - system requirements 用于描述系统必须满足什么
   - 表达方式是 `well-formed textual statements and supporting models or diagrams`
4. 该页还明确 system requirements 的三大作用：
   - basis of architecture and design
   - basis of integration and verification
   - means of communication among project team members
5. `Requirements Management` 页面补充了 cross-cutting 视角：
   - baselining needs and requirements
   - bidirectional traceability
   - flow down / allocation / budgeting
   - change management

## 核心内容摘录

### 概念定义的上游

- Business or Mission Analysis 页面写道：
  - `the first process performed in Concept Definition`
  - 其目的在于建立对 `strategic problem or opportunity` 的定义，并识别候选 solution classes。

### 从 stakeholder view 到 technical view

- System Requirements Definition 页面写道：
  - `transforms the stakeholder view of desired capabilities into a technical, developer view`
  - requirements are `expressed in an appropriate combination of well-formed textual statements and supporting models or diagrams`

### system requirements 的系统作用

- 同页列出 system requirements:
  - `Form the basis of system architecture and design activities`
  - `Form the basis of system integration and verification activities`
  - `Provide a means of communication between the various project team members`

### 管理与追踪

- Requirements Management 页面把 RM 定义为一组 cross-cutting 活动，覆盖：
  - baselining
  - traceability
  - allocation
  - interfaces
  - change

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 01 `re-landscape` | 这是 Topic 01 的体系锚点：它把需求工程放回系统工程生命周期，而不是只讨论某种文档格式 |
| Topic 03 `ears` | `well-formed textual statements` 与 architecture / verification 的直接关系，正是 EARS 这类结构化文本的系统工程位置 |
| Topic 05 `integration-bdd` | 说明 examples / scenarios 只是验证层的一部分，上游仍有 requirements definition / management |

## 可直接引用的术语 / 概念

- `Business or Mission Analysis`
- `stakeholder view`
- `technical, developer view`
- `well-formed textual statements`
- `supporting models or diagrams`
- `basis of architecture and design`
- `bidirectional traceability`

## 风险与局限

1. SEBoK 是 body of knowledge，总结性强，但并非某一单个标准全文。
2. 它适合回答“范式地图与过程位置”，不直接给出每种文本语法的细粒度规则。
3. 对 Topic 01 来说，这正是需要的抽象层；更细的 shall-rule 仍要回到 29148 / GtWR / EARS。

## 交叉引用

- 15288 生命周期框架：[`01-re-landscape-iso-iec-ieee-15288-2023-overview.md`](01-re-landscape-iso-iec-ieee-15288-2023-overview.md)
- 用例桥梁：[`01-re-landscape-use-case-2-0-official.md`](01-re-landscape-use-case-2-0-official.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
