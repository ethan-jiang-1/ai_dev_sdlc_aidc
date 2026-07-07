# W2 — Selection Matrix v2

- status: `closed_for_current_round`
- last_updated: `2026-04-18`
- synthesis_stub: [`W2-cross-topic-synthesis.md`](W2-cross-topic-synthesis.md)
- claims_audit: [`W2-claims-audit-v2.md`](W2-claims-audit-v2.md)
- evidence_base: `74 authoritative copies indexed; selected high-value gaps closed before formal round closeout for SysML v2 official positioning/tools ecosystem/DoD guidance/Collins signal plus INCOSE automotive metadata/end-user participation/Productive4.0 validation use-case, Topic 02 anti-pattern boundary plus Story Smells preview/taxonomy TOC/one-smell discussion/common-problems taxonomy and Seb Rose Beck/BDD origin-boundary article, Topic 04 BMW graph case + v0 multimodal workflow signal plus hosted/independent/enterprise-benchmark outcomes, UX Tools independent design-to-code adoption census, and Figma/Findable named deployment case, Topic 05 FlowForge same-prototype Story/DMN/Gherkin chain plus ISTQB acceptance-governance framework, and Topic 06 format/adoption/enterprise usage/diversity plus OpenSpec direct comparison, Cline/Continue/Aider semantic comparison, rule-effect study, AGENTbench multi-agent context-file evaluation, Umans AI practical cross-tool AGENTS.md following experiment, and OctoBench scaffold-aware compliance benchmark`

## Matrix Axes

| # | dimension | Story | EARS / structured requirement | BDD / Gherkin / Examples | Agent spec / workflow files | evidence pointers |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | primary purpose | intent / conversation | system behavior contract | confirmation / executable examples | team context + feature workflow | 01/02/03/05/06 summaries |
| 2 | best phase | discovery / backlog | definition / contract | formulation / verification | coding-agent execution loop | 02/03/05/06 |
| 3 | ambiguity tolerance | high by design | low | medium-low | varies by layer | 02/03/06 |
| 4 | machine readability | low-medium | medium-high | high when automated | high if structured and scoped | 03/05/06 |
| 5 | traceability support | weak alone | strong with RM | strong for tests | emerging; must link to specs | 01/04/05/06 |
| 6 | AI coding fit | weak alone; useful as intent | strong as behavior prompt | strong as test/acceptance prompt | strong if layered | 02/03/05/06 |
| 7 | compliance fit | weak alone | strong, but full standard text still risk-noted | supportive, not sufficient | supportive, not sufficient | 01/03/04/05 |
| 8 | failure modes | pseudo-spec / no AC | over-complex clauses / completeness gaps | brittle scenarios / tool-first BDD | rules bloat / context rot / spec drift | all |
| 9 | recommended role | north-star intent | precise behavior boundary | executable confirmation | scaffolding and workflow carrier | W2 synthesis |

## First-Pass Decision Rules

| rule | decision |
| --- | --- |
| If the problem is still discovery-heavy, use Story / Story Map first and delay EARS until behavior boundaries are worth freezing. |
| If the behavior is safety-critical, latency-sensitive, contract-like, or failure-mode-heavy, add EARS / structured requirements early. |
| If the team needs shared understanding and executable acceptance, add examples / BDD before or alongside automation. |
| If coding agents are involved, keep repo/team context files short and route feature detail into spec / plan / tasks artifacts. |
| If compliance or auditability matters, connect all lightweight artifacts back to 29148 / GtWR / traceability processes and mark standard full-text gaps explicitly. |

## Weighting Guidance

| project trait | highest-weight dimensions | recommended bias |
| --- | --- | --- |
| Product uncertainty is high | `primary purpose`, `best phase`, `ambiguity tolerance` | Start with Story / Story Map; avoid premature EARS saturation |
| Behavioral boundary risk is high | `machine readability`, `compliance fit`, `failure modes` | Add EARS or equivalent controlled natural language early |
| Team has mature automated acceptance testing | `BDD/examples`, `traceability support`, `AI coding fit` | Use examples/Gherkin as confirmation layer, not as discovery replacement |
| Coding agents do major implementation work | `Agent spec/workflow files`, `AI coding fit`, `failure modes` | Layer `AGENTS/CLAUDE` + scoped rules + feature `spec/plan/tasks` |
| Regulatory / safety pressure is high | `compliance fit`, `traceability support`, `failure modes` | Use 29148/GtWR-aligned requirements and explicit traceability; lightweight agile artifacts alone are insufficient |

## Provisional Recommendations

| context | provisional stack | caveats |
| --- | --- | --- |
| Startup discovery | Story + lightweight AC + small agent instructions | Do not over-formalize before product risk is reduced |
| SaaS delivery team | Story Map + AC/examples + selective EARS + Spec Kit/Kiro tasks | Keep team-level agent files short |
| Regulated / safety-sensitive | 29148/GtWR-aligned requirements + EARS + traceability + examples/tests | Current 29148 clause text still full-text pending |
| Agent-heavy coding workflow | AGENTS/CLAUDE as repo contract + scoped rules + feature spec/plan/tasks | Avoid one big instruction file |

## Second-Pass Scenario Recommendations

| scenario | recommended baseline | add when needed | avoid |
| --- | --- | --- | --- |
| Solo / prototype | Story or Job Story + minimal AC + one short `AGENTS.md` | lightweight `tasks.md` if an agent is implementing multiple steps | full GtWR-style requirements set before product risk is known |
| Small SaaS team | Story Map + AC/examples + selective EARS for NFR/failure cases + Spec Kit/Kiro-style `spec/plan/tasks` | scoped rules for domain conventions; Gherkin for stable flows | putting all product requirements into `AGENTS.md` |
| Platform / API team | Enabler stories + API contracts + EARS for behavioral / NFR clauses + examples for integration tests | decision tables / DMN for complex combinations | pretending user-facing Story templates are enough for technical contracts |
| Regulated / safety-sensitive | 29148/GtWR-aligned requirements + EARS + traceability + verification evidence + examples/tests | BPMN/DMN for process/rule coverage; formal methods / MBSE where behavior or safety cases demand it | treating BDD scenarios as the full requirement baseline |
| Agent-first engineering org | short repo-level context + source-of-truth docs + feature specs/plans/tasks + test feedback loop | doc-gardening / linting for specs and docs | one giant always-loaded instruction file |
| Systems / cyber-physical product | stakeholder needs + 29148/15288 requirements + SysML v2 model layer + verification examples | EARS for controlled textual requirements; MBSE toolchain when relationships and verification traces are central | treating model-layer evidence as proof that any specific tool workflow is mature |

## Evidence Pointers By Context

| context | strongest local evidence |
| --- | --- |
| Startup discovery | [`02-user-story-evidence-summary.md`](02-user-story-evidence-summary.md), [`00-shared-patton-story-mapping-primer.md`](../_reference/00-shared-patton-story-mapping-primer.md), [`../_reference/02-user-story-rose-user-stories-bdd-origin-boundary.md`](../_reference/02-user-story-rose-user-stories-bdd-origin-boundary.md) |
| SaaS delivery team | [`05-integration-bdd-evidence-summary.md`](05-integration-bdd-evidence-summary.md), [`../_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md`](../_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md), [`06-agent-format-evidence-summary.md`](06-agent-format-evidence-summary.md) |
| Regulated / safety-sensitive | [`01-re-landscape-evidence-summary.md`](01-re-landscape-evidence-summary.md), [`03-ears-evidence-summary.md`](03-ears-evidence-summary.md), [`../_reference/05-integration-bdd-flowforge-bpmn-dmn-gherkin.md`](../_reference/05-integration-bdd-flowforge-bpmn-dmn-gherkin.md), [`../_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md`](../_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md), [`../_reference/04-future-trends-ai-governance-nist-eu-ai-act.md`](../_reference/04-future-trends-ai-governance-nist-eu-ai-act.md) |
| Agent-heavy coding workflow | [`06-agent-format-evidence-summary.md`](06-agent-format-evidence-summary.md), [`../_reference/06-agent-format-openai-harness-engineering.md`](../_reference/06-agent-format-openai-harness-engineering.md), [`../_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md`](../_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md), [`../_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md`](../_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md), [`../_reference/06-agent-format-umans-agents-md-following-experiment.md`](../_reference/06-agent-format-umans-agents-md-following-experiment.md), [`04-future-trends-evidence-summary.md`](04-future-trends-evidence-summary.md) |
| Systems / cyber-physical product | [`01-re-landscape-evidence-summary.md`](01-re-landscape-evidence-summary.md), [`../_reference/01-re-landscape-omg-sysml-v2-official.md`](../_reference/01-re-landscape-omg-sysml-v2-official.md), [`../_reference/01-re-landscape-iso-iec-ieee-15288-2023-overview.md`](../_reference/01-re-landscape-iso-iec-ieee-15288-2023-overview.md) |

## Evidence Gaps Before Finalizing

1. MBSE / SysML v2 official anchor is now landed via [`../_reference/01-re-landscape-omg-sysml-v2-official.md`](../_reference/01-re-landscape-omg-sysml-v2-official.md); remaining upgrade is broader non-defense industrial maturity beyond metadata-grade signal, not official positioning.
2. Decision-table / DMN boundary now has an official starter anchor via [`../_reference/05-integration-bdd-omg-dmn-decision-boundary.md`](../_reference/05-integration-bdd-omg-dmn-decision-boundary.md); FlowForge adds same-prototype Story / DMN / Gherkin evidence via [`../_reference/05-integration-bdd-flowforge-bpmn-dmn-gherkin.md`](../_reference/05-integration-bdd-flowforge-bpmn-dmn-gherkin.md), and ISTQB adds acceptance-governance framework evidence via [`../_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md`](../_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md); remaining upgrade is EARS-inclusive or high-compliance same-project governance, not object-level positioning or generic Story/DMN/Gherkin connection.
3. Non-OpenAI format-adoption case is now partially landed via [`../_reference/06-agent-format-amp-agents-md-adoption.md`](../_reference/06-agent-format-amp-agents-md-adoption.md), non-tool-vendor enterprise-internal usage is now supported via [`../_reference/06-agent-format-stripe-minions-enterprise-usage.md`](../_reference/06-agent-format-stripe-minions-enterprise-usage.md), direct comparison is now starter-covered via [`../_reference/06-agent-format-openspec-cross-tool-comparison.md`](../_reference/06-agent-format-openspec-cross-tool-comparison.md), semantic divergence is now supported via [`../_reference/06-agent-format-rule-loading-semantics-comparison.md`](../_reference/06-agent-format-rule-loading-semantics-comparison.md), rule-effect/failure evidence is supported via [`../_reference/06-agent-format-rules-shape-or-distort-2026.md`](../_reference/06-agent-format-rules-shape-or-distort-2026.md), multi-agent context-file evaluation is supported via [`../_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md`](../_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md), practical cross-tool instruction-following evidence is supported via [`../_reference/06-agent-format-umans-agents-md-following-experiment.md`](../_reference/06-agent-format-umans-agents-md-following-experiment.md), and formal scaffold-aware benchmark evidence is now supported via [`../_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md`](../_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md); remaining upgrade is exact `AGENTS.md` semantic conformance-suite evidence, not basic enterprise existence, workflow comparison, precedence-difference proof, rule-effect proof, general multi-agent evaluation existence, formal scaffold-aware benchmark existence, or same-repo practitioner experiment.
4. Multimodal workflow existence is now stronger and has one hosted outcome via [`../_reference/04-future-trends-vercel-v0-stripe-outcomes.md`](../_reference/04-future-trends-vercel-v0-stripe-outcomes.md), one independent design study via [`../_reference/04-future-trends-personagram-multimodal-design-study.md`](../_reference/04-future-trends-personagram-multimodal-design-study.md), one enterprise benchmark via [`../_reference/04-future-trends-ai4ui-enterprise-pixel-to-production.md`](../_reference/04-future-trends-ai4ui-enterprise-pixel-to-production.md), one independent adoption census via [`../_reference/04-future-trends-state-of-prototyping-2026.md`](../_reference/04-future-trends-state-of-prototyping-2026.md), and one named real deployment case via [`../_reference/04-future-trends-figma-make-findable-production-case.md`](../_reference/04-future-trends-figma-make-findable-production-case.md); remaining upgrade is independently verified production outcome, not named deployment existence.

## Residual Risk Labels For Final Report

| risk | label to use |
| --- | --- |
| GtWR full PDF not captured | `GtWR-full-text-pending; official-presentation-supported` |
| 29148 clause text not captured | `29148-clause-text-pending; official-scope-supported` |
| Topic 02 Cockburn/Beck gap | `story-smells-preview-supported; story-smells-taxonomy-toc-supported; one-smell-discussion-supported; common-problems-taxonomy-supported; beck-planning-game-adjacent-supported; story-bdd-boundary-supported; chapter-14-full-discussion-pending; beck-verbatim-full-text-pending` |
| Topic 03 SaaS EARS gap | `ears-saas-evidence-pending` |
| Topic 04 multimodal gap | `multimodal-workflow-supported; multimodal-hosted-outcome-supported; independent-design-study-outcome-supported; enterprise-benchmark-supported; independent-adoption-census-supported; named-real-deployment-case-supported; independent-production-outcome-verification-pending` |
| Topic 06 comparison gap | `agent-format-enterprise-usage-supported; broader-diversity-supported; direct-comparison-supported; semantic-divergence-supported; rule-effect-failure-evidence-supported; multi-agent-context-file-evaluation-supported; practical-cross-tool-instruction-following-experiment-supported; formal-scaffold-aware-coding-compliance-benchmark-supported; cross-tool-AGENTS-md-semantic-conformance-suite-pending; Amp-format-adoption-supported; public-oss-usage-supported` |
| SysML v2 maturity gap | `sysml-v2-official-positioning-supported; tool-ecosystem-supported; external-transition-guidance-supported; defense-industry-signal-supported; non-defense-official-case-metadata-supported; multi-org-non-defense-participation-supported; non-defense-validation-supported; production-outcome-maturity-pending` |
| Topic 05 same-project DMN governance case gap | `dmn-boundary-official-positioning-supported; same-prototype-story-dmn-gherkin-supported; acceptance-governance-framework-supported; ears-inclusive-high-compliance-same-project-case-pending` |
