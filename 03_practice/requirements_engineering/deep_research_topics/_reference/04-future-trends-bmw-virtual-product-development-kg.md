# BMW Group / TU Dresden 2025 — Knowledge graph in virtual product development for collaboration

- source_url: `https://doi.org/10.1017/pds.2025.10238`
- source_type: `academic industry-collaborative conference paper`
- accessed_at: `2026-04-18`
- related_topic: `04 future-trends (primary), 01 re-landscape`
- trust_level: `academic + industry collaborative`
- tier: `A`
- why_it_matters: Topic 04 当前 graph 轴已经有 W3C substrate、RE-specific research signal 与 IBM customer-requirements enterprise signal，但仍缺更广的 product-development adoption case。该论文由 Technical University Dresden 与 BMW Group 联合发表，直接研究虚拟产品开发中的 knowledge graph，明确把 `requirements`、CAD 数据、user/task 信息一起纳入图谱，用于信息检索、tracking changes 与 user/issue management。这使 Topic 04 可从“requirements-side KG signal”进一步升级到“broader product-development graph case supported”。
- captured_excerpt: `yes`
- claims_supported: `Knowledge graphs are being applied in virtual product development, not only in abstract RE research; product-development graphs can integrate CAD geometry, requirements, and user/task information; graph-based representations are used to support collaboration, traceability of changes, and issue management in large engineering organizations.`
- date_scope: `published online 2025`
- related_entities: `BMW Group; Technical University Dresden; virtual product development; CAD; requirements; knowledge graph; collaborative design`

## 关键事实

1. 论文题目直接是 `Leveraging knowledge graphs in virtual product development for enhanced collaboration`。
2. 作者单位包含 `BMW Group` 与 `Technical University Dresden`，不是纯实验室脱离场景的概念论文。
3. 摘要明确写道：方法整合了 `CAD models and geometry, requirements and user-related data` 来构建 knowledge graph。
4. 摘要列出的 use-cases 包括：
   - information retrieval
   - tracking changes
   - user-issue management
5. 正文指出，该研究在 `BMW Group` 的 virtual product development process 中开展。
6. 论文把 graph 用于 large-scale collaborative engineering system，而不是仅仅用于 requirements 元知识管理。

## 核心内容摘录

### 这是一条更广的 product-development graph signal

- 论文开头把虚拟产品开发描述为跨行业标准流程，涵盖 automotive、aerospace、electronics 等。
- 其 graph 目标不是单点文本检索，而是支撑大型协作式产品开发中的 transparency、information flow 与 coordination。

### requirements 被直接接入产品开发图谱

- 文中明确说，除 CAD 数据外，还要把 `requirements` 接入图谱。
- 这些 requirements 包括 legal regulations、customer preferences，以及随着开发周期演化的 requirement changes。
- 论文强调需要将 requirements 与 CAD models 建立连接，以便工程师理解为什么模型需要更新、并追溯 requirement change 的来源。

### user / issue / change 也一起建模

- 图谱不只包含技术对象，还包含 user-related information 与 issue entities。
- 这样图谱支持：
  - 找到相关责任人
  - 跟踪 change impact
  - 处理跨团队 CAD inconsistency

### 与 Topic 04 的关系

- 这条证据把 graph 轴从：
  - W3C substrate
  - RE-specific knowledge graph
  - enterprise customer-requirements matching
- 推进到：
  - real product-development collaboration case

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 04 `future-trends` | graph/knowledge-graph 轴已不再局限于 substrate、RE research 或 customer-requirements matching，而进入 broader product-development collaboration case |
| Topic 01 `re-landscape` | 说明 requirements artifacts 的未来承载体可能与 CAD / model / user / issue graph 联动，而不只停留在文档层 |

## 可直接引用的术语 / 概念

- `virtual product development`
- `requirements and user-related data`
- `information retrieval`
- `tracking changes`
- `user-issue management`
- `large-scale engineering systems`

## 风险与局限

1. 这是一条强 graph adoption signal，但仍主要覆盖 product-development / CAD-heavy 环境，不代表所有软件团队都会采用同样形态。
2. 它更强地支持 graph 轴，而不是 multimodal 轴。
3. 论文强调 potential 与 case-based methodology，不应把它写成已成行业主流的量化 adoption 证明。

## 交叉引用

- Topic 04 evidence summary：[`../_artifacts/04-future-trends-evidence-summary.md`](../_artifacts/04-future-trends-evidence-summary.md)
- W3C substrate：[`04-future-trends-w3c-shacl-graph-constraints.md`](04-future-trends-w3c-shacl-graph-constraints.md)
- RE graph signal：[`04-future-trends-kg-empire-re-knowledge-graph.md`](04-future-trends-kg-empire-re-knowledge-graph.md)
- IBM enterprise requirements KG：[`04-future-trends-ibm-enterprise-requirements-kg.md`](04-future-trends-ibm-enterprise-requirements-kg.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
