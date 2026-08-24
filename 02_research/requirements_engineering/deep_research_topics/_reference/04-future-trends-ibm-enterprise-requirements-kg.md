# IBM Research 2023 — Enterprise knowledge graph approach for customer requirements

- source_url: `https://research.ibm.com/publications/understanding-customer-requirements-an-enterprise-knowledge-graph-approach`
- source_type: `industry research conference paper landing page`
- accessed_at: `2026-04-18`
- related_topic: `04 future-trends (primary), 02 user-story, 01 re-landscape`
- trust_level: `industry research`
- tier: `A`
- why_it_matters: Topic 04 当前缺的是 industrial/product-side 的 requirements-specific graph adoption signal，而不只是 W3C substrate 或 RE research literature graph。IBM Research 这篇 ESWC 2023 论文直接面向 enterprise customer requirements：把 free-text requirements 映射进 Enterprise Knowledge Graph，并用 IBM 十年以上历史 requirement-offering records 做匹配验证。这足以把 Topic 04 的 graph axis 再推进一层。
- captured_excerpt: `yes`
- claims_supported: `Enterprise Knowledge Graphs can represent customer requirements from free text in enterprise settings; the approach formalizes customer requests and enterprise offerings; IBM researchers demonstrate the approach using historical requirement-offering records spanning over 10 years; requirements-to-business-unit matching is treated as a knowledge-graph problem.`
- date_scope: `conference paper dated 2023-05-28`
- related_entities: `IBM Research; enterprise knowledge graph; customer requirements; free text; business units; requirements-offering records`

## 关键事实

1. IBM Research 页面标题直接是 `Understanding Customer Requirements - An Enterprise Knowledge Graph Approach`。
2. 摘要明确写道：customers come to a large enterprise with a set of requirements，而 formalizing requests and offerings is a way to achieve matching。
3. 摘要进一步写道：`Enterprise Knowledge Graphs (EKG) are an effective method to represent enterprise information in ways that can be more easily interpreted by both humans and machines.`
4. 同一摘要说明：该方案识别 customer requirements from free text，并用 EKG 表示。
5. 论文使用 IBM spanning over 10 years 的 historical requirement-offering records 数据集来验证 requirement-to-business-unit matching。

## 核心内容摘录

### 工业侧 requirements graph signal

- 这不是 generic KG 教程，而是把企业客户需求本身当成 graph representation 和 matching 的对象。
- 它表明 requirements graph / knowledge graph 在 enterprise context 已经出现实际研究与数据应用。

### 对 Topic 04 的意义

- graph axis 不再只有：
  - W3C substrate
  - RE research-knowledge graph
- 现在还多了一层：
  - enterprise customer requirements knowledge graph signal

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 04 `future-trends` | graph / knowledge-graph requirements 轴现在已有 enterprise-side requirements signal |
| Topic 02 `user-story` | 上游 free-text customer requirements 可被结构化进 graph，而不只停留在 backlog prose |
| Topic 01 `re-landscape` | requirements map 可以加入 enterprise knowledge representation 轴 |

## 可直接引用的术语 / 概念

- `Enterprise Knowledge Graphs`
- `customer requirements from free text`
- `historical requirement-offering records`
- `business units`
- `formalizing requests and offerings`

## 风险与局限

1. 这是 enterprise research signal，不是成熟商用品类普及证据。
2. 它描述的是 customer requirements matching 场景，不等于完整产品开发需求库都已知识图谱化。
3. 更稳的写法应是：`enterprise-requirements-kg-signal-supported; broad-product-adoption-pending`。

## 交叉引用

- Topic 04 evidence summary：[`../_artifacts/04-future-trends-evidence-summary.md`](../_artifacts/04-future-trends-evidence-summary.md)
- RE knowledge graph signal：[`04-future-trends-kg-empire-re-knowledge-graph.md`](04-future-trends-kg-empire-re-knowledge-graph.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
