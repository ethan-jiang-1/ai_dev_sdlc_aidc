# 06 — agent-format — Question List

- status: `closed_for_current_round`
- last_updated: `2026-04-18`
- based_on:
  - [`06-agent-format-evidence-summary.md`](06-agent-format-evidence-summary.md)
  - [`../_reference/06-agent-format-openai-codex-adoption.md`](../_reference/06-agent-format-openai-codex-adoption.md)
  - [`../_reference/06-agent-format-openai-harness-engineering.md`](../_reference/06-agent-format-openai-harness-engineering.md)
  - [`../_reference/06-agent-format-github-spec-kit-official.md`](../_reference/06-agent-format-github-spec-kit-official.md)
  - [`../_reference/06-agent-format-github-copilot-agents-md-support.md`](../_reference/06-agent-format-github-copilot-agents-md-support.md)
  - [`../_reference/06-agent-format-kiro-spec-workflow-official.md`](../_reference/06-agent-format-kiro-spec-workflow-official.md)
  - [`../_reference/06-agent-format-openwork-oss-usage.md`](../_reference/06-agent-format-openwork-oss-usage.md)
  - [`../_reference/06-agent-format-stripe-minions-enterprise-usage.md`](../_reference/06-agent-format-stripe-minions-enterprise-usage.md)
  - [`../_reference/06-agent-format-github-adoption-study-2026.md`](../_reference/06-agent-format-github-adoption-study-2026.md)
  - [`../_reference/06-agent-format-openspec-cross-tool-comparison.md`](../_reference/06-agent-format-openspec-cross-tool-comparison.md)
  - [`../_reference/06-agent-format-rule-loading-semantics-comparison.md`](../_reference/06-agent-format-rule-loading-semantics-comparison.md)
  - [`../_reference/06-agent-format-rules-shape-or-distort-2026.md`](../_reference/06-agent-format-rules-shape-or-distort-2026.md)
  - [`../_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md`](../_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md)
  - [`../_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md`](../_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md)
  - [`../_reference/06-agent-format-umans-agents-md-following-experiment.md`](../_reference/06-agent-format-umans-agents-md-following-experiment.md)

## Open Questions

1. OpenSpec 已提供 direct cross-tool workflow/config comparison，Cline / Continue / Aider 已证明 instruction precedence、nested scope、runtime semantics 存在实质差异，Zhang et al. 2026 已给出 rule-effect/failure study，Gloaguen et al. 2026 已给出 AGENTbench / multi-agent context-file evaluation，Umans AI 已给出 same-repo / same-task / same-rules 的 practitioner cross-tool AGENTS.md following experiment，OctoBench 已给出 formal scaffold-aware coding compliance benchmark；下一步是否能补到 exact cross-tool `AGENTS.md` / `CLAUDE.md` semantic conformance suite？
2. Aider / Continue / Cline 在 feature-level spec 上各自处于什么成熟度？
3. `AGENTS.md` 的跨工具 adoption 和 cross-tool semantic divergence 应如何分开论证？
4. 在什么场景下应把 EARS 放进 feature spec，而不是放进 team-level rule/contract？
