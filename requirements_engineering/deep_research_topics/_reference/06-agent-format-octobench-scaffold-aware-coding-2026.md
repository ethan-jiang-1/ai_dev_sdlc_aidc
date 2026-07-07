# Ding et al. 2026 — OctoBench scaffold-aware instruction following in repository-grounded agentic coding

- source_url: `https://arxiv.org/abs/2601.10343`
- source_type: `academic preprint / benchmark`
- accessed_at: `2026-04-18`
- related_topic: `06 agent-format (primary), 04 future-trends`
- trust_level: `academic`
- tier: `A`
- why_it_matters: Topic 06 当前 residual gap 是 formal cross-tool semantic conformance suite。OctoBench 不是 `AGENTS.md` / `CLAUDE.md` 的跨工具语义 conformance suite，也没有证明各工具 runtime semantics 一致；但它是目前找到的最接近 formal suite 的 coding-agent benchmark：专门评估 repository-grounded agentic coding 中的 scaffold-aware instruction following，使用多 scaffold 类型、objective checklist、full trajectory capture 和 automated scoring，将 task solving 与 rule/scaffold compliance 拆开评估。这足以升级为 `formal-scaffold-aware-coding-compliance-benchmark-supported`，同时保留 exact cross-tool AGENTS.md semantic conformance pending。
- captured_excerpt: `yes`
- claims_supported: `OctoBench is a 2026 academic benchmark for scaffold-aware instruction following in repository-grounded agentic coding. It includes 34 environments, 217 tasks under three scaffold types, 7,098 objective checklist items, and an automated observation-and-scoring toolkit that captures full trajectories and performs fine-grained checks. Experiments on eight representative models reveal a systematic gap between task-solving and scaffold-aware compliance. This supports formal benchmark evidence for coding-agent scaffold compliance, while not proving cross-tool semantic conformance for AGENTS.md / CLAUDE.md rule files.`
- date_scope: `submitted 2026-01-15; revised 2026-01-16; accessed 2026-04-18`
- related_entities: `OctoBench; repository-grounded agentic coding; coding scaffolds; scaffold-aware instruction following; checklist success; trajectory scoring`

## 关键事实

1. 论文题目是 `OctoBench: Benchmarking Scaffold-Aware Instruction Following in Repository-Grounded Agentic Coding`。
2. 研究对象是 coding scaffolds 让 LLMs 成为 software agents 后，agent 是否能遵守 scaffold-specified instructions。
3. 作者指出此前 under-examined 的点是：
   - constraints are heterogeneous
   - constraints persist across interactions
   - task-solving 与 instruction/scaffold compliance 需要拆开看
4. OctoBench 明确定位为 benchmark：
   - `scaffold-aware instruction following`
   - `repository-grounded agentic coding`
5. Benchmark 规模：
   - 34 environments
   - 217 tasks
   - three scaffold types
   - 7,098 objective checklist items
6. 评估工具：
   - automated observation-and-scoring toolkit
   - captures full trajectories
   - performs fine-grained checks
7. 实验对象：
   - eight representative models
8. 主要结论：
   - task-solving 与 scaffold-aware compliance 之间存在 systematic gap
   - 需要显式针对 heterogeneous instruction following 进行 training 与 evaluation
9. 作者声明 release benchmark，以支持 reproducible benchmarking 和 scaffold-aware coding agents development。

## 核心内容摘录

### 这条 evidence 补的 gap

- 之前 Topic 06 已有：
  - Cline / Continue / Aider rule-loading semantics comparison
  - Zhang et al. rule-effect/failure evidence
  - AGENTbench multi-agent context-file evaluation
  - Umans AI same-repo AGENTS.md following practitioner experiment
- OctoBench 进一步补强：
  - formal coding-agent benchmark
  - repository-grounded tasks
  - scaffold-aware compliance
  - objective checklists
  - full trajectory capture
  - task success vs rule compliance separation

### 仍然不能解决的部分

- OctoBench 不是 `AGENTS.md` / `CLAUDE.md` format 的 semantic conformance spec。
- 它不证明 Codex / Claude Code / Cursor / Cline 等工具对同一 instruction file 的 discovery、precedence、merge、scope semantics 一致。
- 它不替代 official rule-loading comparison。
- 因此 Topic 06 的 exact gap 应从 `formal-cross-tool-conformance-suite-pending` 缩窄为：
  - `formal-scaffold-aware-coding-compliance-benchmark-supported`
  - `cross-tool-AGENTS-md-semantic-conformance-suite-pending`

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 06 `agent-format` | formal benchmark evidence that coding agents need scaffold-aware compliance evaluation beyond task success |
| Topic 04 `future-trends` | supports future trend toward executable checks / evaluation harnesses for spec/context/rule artifacts |

## 可直接引用的术语 / 概念

- `OctoBench`
- `scaffold-aware instruction following`
- `repository-grounded agentic coding`
- `34 environments`
- `217 tasks`
- `three scaffold types`
- `7,098 objective checklist items`
- `full trajectories`
- `fine-grained checks`
- `systematic gap between task-solving and scaffold-aware compliance`

## 风险与局限

1. 这是 arXiv preprint，仍需同行评审与独立复现。
2. 它是 scaffold-aware coding-agent compliance benchmark，不是跨工具 `AGENTS.md` / `CLAUDE.md` semantic conformance suite。
3. 论文摘要未在本轮 AC 中展开三类 scaffold 的完整定义；如果最终报告要细分 scaffold categories，应回到全文或 code/data。
4. Topic 06 因而可以升级为 `formal-scaffold-aware-coding-compliance-benchmark-supported`，但不能写成 `cross-tool-semantic-standard-solved`。

## 交叉引用

- AGENTbench multi-agent context-file evaluation：[`06-agent-format-evaluating-agents-md-agentbench-2026.md`](06-agent-format-evaluating-agents-md-agentbench-2026.md)
- Practical same-repo experiment：[`06-agent-format-umans-agents-md-following-experiment.md`](06-agent-format-umans-agents-md-following-experiment.md)
- Rule-loading semantics comparison：[`06-agent-format-rule-loading-semantics-comparison.md`](06-agent-format-rule-loading-semantics-comparison.md)
- Rule-effect study：[`06-agent-format-rules-shape-or-distort-2026.md`](06-agent-format-rules-shape-or-distort-2026.md)
- Topic 06 evidence summary：[`../_artifacts/06-agent-format-evidence-summary.md`](../_artifacts/06-agent-format-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
