# Zhang et al. 2026 — empirical study of agent rule files and coding-agent performance

- source_url: `https://arxiv.org/abs/2604.11088`
- source_type: `academic preprint`
- accessed_at: `2026-04-18`
- related_topic: `06 agent-format (primary), 04 future-trends`
- trust_level: `academic`
- tier: `A`
- why_it_matters: Topic 06 已有 format/workflow adoption、semantic divergence 和 precedence evidence，但仍缺更强的 conformance/failure style evidence：规则文件是否真的帮助 agent，哪些规则有害。Zhang et al. 2026 直接研究 natural-language instruction files（如 `CLAUDE.md`、`.cursorrules`），抓取 679 个 files / 25,532 rules，并在 SWE-bench Verified 上进行 5,000+ agent runs。这是本轮最贴合 Topic 06 的 empirical evidence，能把 conformance/failure gap 从推断推进到 controlled large-scale evaluation。
- captured_excerpt: `yes`
- claims_supported: `A 2026 empirical study of 679 agent rule files and 25,532 rules ran over 5,000 coding-agent runs on SWE-bench Verified. It found that rules improved performance by 7--14 percentage points overall, but random rules helped as much as expert-curated ones; negative constraints were the only individually beneficial rule type, while positive directives actively hurt. This supports the claim that agent rule files are not simple portable guidance: they can help collectively, but poorly shaped rules can degrade performance, making conformance/failure evidence and rule-design discipline necessary.`
- date_scope: `submitted 2026-04-13; accessed 2026-04-18`
- related_entities: `CLAUDE.md; .cursorrules; coding agents; SWE-bench Verified; agent rules`

## 关键事实

1. 论文题目直接是：
   - `Do Agent Rules Shape or Distort? Guardrails Beat Guidance in Coding Agents`
2. 摘要明确研究对象是 natural language instruction files：
   - `CLAUDE.md`
   - `.cursorrules`
3. 论文声明此前缺少 controlled study 来衡量这些规则是否改善 agent performance，以及哪些规则属性有益。
4. 研究抓取：
   - 679 个 instruction / rule files
   - 25,532 条 rules
5. 实验规模：
   - 5,000+ agent runs
   - SWE-bench Verified
6. 关键结果：
   - rules overall improve performance by 7--14 percentage points
   - random rules help as much as expert-curated ones
   - negative constraints 是唯一 individually beneficial rule type
   - positive directives actively hurt
   - individual rules are mostly harmful in isolation but collectively helpful
   - no degradation up to 50 rules
7. 论文给出的 practical principle 是：
   - constrain what agents must not do
   - rather than prescribing what they should do

## 核心内容摘录

### 这条 evidence 补的 gap

- 之前 Topic 06 已有：
  - adoption breadth
  - OpenSpec direct comparison
  - Cline / Continue / Aider rule-loading semantic differences
- 本文进一步提供：
  - large-scale controlled evaluation
  - rule usefulness / harmfulness distinction
  - concrete rule-design failure mode

### 对最终报告的写法约束

- 可以写：
  - agent rule files can improve outcomes, but the mechanism is not simply “more expert guidance is better”
  - negative constraints appear safer than positive directives in this study
  - rule files need design discipline and conformance testing
- 不应写：
  - any well-written rule file is beneficial
  - AGENTS/CLAUDE/rules are semantically portable and harmless
  - more detailed guidance always improves coding-agent behavior

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 06 `agent-format` | 直接补强 conformance/failure evidence：规则文件有整体收益，但规则类型会造成收益或损害 |
| Topic 04 `future-trends` | 支撑未来 spec/config workflow 需要 rule linting、negative constraints、conformance evaluation，而不是纯粹堆更多上下文 |

## 可直接引用的术语 / 概念

- `679 such files`
- `25,532 rules`
- `over 5,000 agent runs`
- `SWE-bench Verified`
- `7--14 percentage points`
- `negative constraints`
- `positive directives`
- `hidden reliability risk`

## 风险与局限

1. 这是 arXiv preprint，仍需同行评审与复现。
2. 实验基于 SWE-bench Verified 和一个 state-of-the-art coding agent，不能直接外推到所有工具和所有企业工作流。
3. Topic 06 因而可以升级为 `rule-effect/failure-evidence-supported`，但仍应保留 cross-tool conformance suite pending。

## 交叉引用

- Rule-loading semantics comparison：[`06-agent-format-rule-loading-semantics-comparison.md`](06-agent-format-rule-loading-semantics-comparison.md)
- OpenSpec direct comparison：[`06-agent-format-openspec-cross-tool-comparison.md`](06-agent-format-openspec-cross-tool-comparison.md)
- OpenAI harness failure mode：[`06-agent-format-openai-harness-engineering.md`](06-agent-format-openai-harness-engineering.md)
- Topic 06 evidence summary：[`../_artifacts/06-agent-format-evidence-summary.md`](../_artifacts/06-agent-format-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
