# W3C RDF / SHACL — Official graph-data and constraint-language signal for graph-shaped requirement artifacts

- source_url: `https://www.w3.org/TR/shacl/` + `https://www.w3.org/RDF/Overview.html`
- source_type: `official standard / standards overview`
- accessed_at: `2026-04-18`
- related_topic: `04 future-trends (primary), 01 re-landscape, 03 ears, 05 integration-bdd`
- trust_level: `official`
- tier: `A`
- why_it_matters: Topic 04 的另一个剩余缺口是“requirements 是否可能 graph/constraint 化”。W3C 的 RDF + SHACL 官方标准不能证明 requirements engineering 社区已经普遍用 knowledge graph 表达需求，但它能证明图结构数据与可机器校验约束已经有成熟官方标准底座，可用于承载未来的 graph-shaped requirement artifacts、validation、integration 和 code generation 信号。
- captured_excerpt: `yes`
- claims_supported: `RDF is a W3C standard graph data model; SHACL is a W3C Recommendation for validating RDF graphs against conditions expressed as shapes graphs; SHACL descriptions can be used for validation, user interface building, code generation, and data integration; graph-shaped constraints and machine-checkable conditions already have standards-level support.`
- date_scope: `RDF overview current as of 2026-04-18; SHACL is a W3C Recommendation`
- related_entities: `W3C; RDF; SHACL; shapes graph; data graph; knowledge graph; constraints; validation`

## 关键事实

1. W3C RDF overview 把 RDF 定义为 graph-based data model，并说明它是 Semantic Web standards 的核心基础。
2. W3C SHACL Recommendation 的摘要明确写道：SHACL defines a language for validating RDF graphs against a set of conditions。
3. 同一摘要说明：这些 conditions 以 `shapes` 形式表达在 RDF graph 中，这些 graph 被称为 `shapes graphs`。
4. SHACL 摘要还明确说：这种 graph-shaped constraints 描述除了 validation 外，还可用于：
   - user interface building
   - code generation
   - data integration
5. 这说明“graph + constraints + machine checking”并不是未来想象，而是已经有标准化表示与验证机制的成熟 substrate。

## 核心内容摘录

### 图结构数据标准底座

- RDF 官方 overview 说明 RDF 提供 graph-based data model，用于 structured information representation。
- 对 Topic 04 来说，这意味着“requirements as graph”至少在底层数据表示上不是无标准可依。

### 机器可校验的图约束

- SHACL 官方 Recommendation 摘要明确说它用于 validating RDF graphs against conditions。
- 条件由 shapes graph 给出，因此 graph 中不仅可以存结构，还可以存 validation constraints。

### 与 requirements future-trend 的弱连接

- SHACL 官方直接提到 UI building、code generation、data integration。
- 这与 Topic 04 中“requirements 变为 machine-checkable artifact、graph/constraint layer、工具互操作输入”的未来趋势存在明显结构相似性。
- 但更严格的写法应是：`graph/constraint substrate supported; requirements-specific adoption still pending`。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 04 `future-trends` | graph-shaped constraint artifacts 已有 W3C 标准底座，可支持“requirements as graph / constraint layer”的弱趋势判断 |
| Topic 01 `re-landscape` | 补足 Story / EARS / SysML 之外的 graph/constraint representation 轴 |
| Topic 03 `ears` | EARS 提供 controlled NL；SHACL 代表更机器化的 graph/constraint validation layer |
| Topic 05 `integration-bdd` | graph constraints 与 scenario/examples 不同，说明未来的 requirement stack 可能继续分层 |

## 可直接引用的术语 / 概念

- `graph-based data model`
- `validating RDF graphs against a set of conditions`
- `shapes graph`
- `data graph`
- `code generation`
- `data integration`

## 风险与局限

1. 这份 reference 不证明 requirements engineering 社区已经把需求写成 RDF/SHACL。
2. 它更适合支撑“graph/constraint substrate exists”而非“graph requirements 已成熟采用”。
3. 若要把 Topic 04 写成更强结论，仍需 requirements-specific graph / knowledge-graph case 或学术 signal。

## 交叉引用

- Topic 04 evidence summary：[`../_artifacts/04-future-trends-evidence-summary.md`](../_artifacts/04-future-trends-evidence-summary.md)
- Topic 01 model-layer anchor：[`01-re-landscape-omg-sysml-v2-official.md`](01-re-landscape-omg-sysml-v2-official.md)
- W2 cross-topic synthesis：[`../_artifacts/W2-cross-topic-synthesis.md`](../_artifacts/W2-cross-topic-synthesis.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
