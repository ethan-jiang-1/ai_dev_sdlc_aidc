# W2 — Claims Audit v2

- status: `closed_for_current_round`
- last_updated: `2026-04-18`
- source_v1: [`../claims-audit.md`](../claims-audit.md)
- synthesis_stub: [`W2-cross-topic-synthesis.md`](W2-cross-topic-synthesis.md)
- evidence_base: `74 authoritative copies indexed; closed-round audit for current DR round`

## Evidence Strength Scale

| level | meaning |
| --- | --- |
| A | peer-reviewed / official standard / legal text with direct relevance |
| B | official product docs, official KOL / method owner, or multi-party authoritative docs |
| C | industry radar / high-trust hosted case / single study with bounded external validity |
| D | vendor whitepaper / sales case |
| E | community opinion / blog signal only |
| F | author framing / metaphor |

## Legacy Claims To Re-Evaluate

| id | v1 claim | v1 strength | v2 provisional direction | key new evidence |
| --- | --- | --- | --- | --- |
| C1 | EARS 在系统工程界优于 User Story | F | reframe as layer-fit, not universal superiority | 01 / 02 / 03 / 05 summaries |
| C2 | LLM 需求解析准确性 +59.17% / +26.07% | C | keep as single-study claim unless upgraded | 04 question-list |
| C3 | sMBSAP metrics imply EARS-like benefit | C | keep risk: sMBSAP != EARS | 04 summary |
| C4 | AI review cuts review time 50–75% | D | keep vendor-claim status unless independent evidence found | 03 / 04 summaries |
| C5 | project saves $150k | D | keep case-claim status | 03 / 04 summaries |
| C6 | User Stories are dead / prompts replace them | E | downgrade rhetorically; Cohn 2026 supports AI as partner, not replacement | 02-user-story-mike-cohn-ai-era |
| C7 | TDD is dead | E | out of scope as factual claim; BDD remains examples-family, not TDD replacement | 05 summaries |
| C8 | EARS maps to Gherkin with zero semantic loss | D | reframe as structural affinity, not zero-loss conversion | 05 summaries + 03 summary |
| C9 | Room guide vs blueprint metaphor | F | keep as teaching metaphor only | W2 selection matrix |
| C10 | vague User Stories cause LLM hallucination | E/C | reframe as plausible risk, not direct causal proof | 04 / 06 summaries |

## First-Pass Audit Decisions

| id | v2 decision | strength after Wave 1 | handling |
| --- | --- | --- | --- |
| C1 | Replace superiority wording with layer-fit wording. | B for layered framing, F for superiority phrasing | remove universal superiority claim |
| C2 | Keep only if phrased as a single-study quantitative claim. | C | no headline use without replication |
| C3 | Keep only as sMBSAP-specific signal, not EARS proof. | C | mark conceptual-substitution risk |
| C4 | Keep as vendor/marketing claim unless independent eval found. | D | do not use in executive conclusion |
| C5 | Keep as anecdotal case claim. | D | do not generalize |
| C6 | Mark as contradicted by Cohn 2026: AI is partner, not replacement. | B against strong claim | remove or quote only as industry rhetoric |
| C7 | Out of scope / rhetorical. | E | do not use |
| C8 | Replace zero-loss claim with structural-affinity claim. | B/C for affinity, D/F for zero-loss | use with caveat |
| C9 | Keep as metaphor. | F | label as teaching device |
| C10 | Keep as plausible risk only. | C/E | needs direct empirical support |

## Second-Pass Final-Use Recommendations

| id | final-use recommendation | wording rule |
| --- | --- | --- |
| C1 | `remove_as_claim; replace_with_layered_recommendation` | Write “Story and EARS optimize different layers,” not “EARS is better.” |
| C2 | `keep_only_in_evidence_audit` | Keep the exact numbers out of main narrative unless the original study is independently reviewed. |
| C3 | `keep_with_caveat` | State that sMBSAP is a related structured process signal, not direct EARS evidence. |
| C4 | `demote_to_vendor_claim` | Use only as “vendor claims review-time reduction,” not as proven ROI. |
| C5 | `demote_to_case_claim` | Do not generalize beyond the specific reported case. |
| C6 | `remove_strong_claim` | Replace with “AI changes how stories are drafted and reviewed; it does not eliminate user conversations.” |
| C7 | `remove` | Do not use “TDD is dead” as evidence in this report. |
| C8 | `rewrite` | Use “EARS and Gherkin share structural affinity for state/event/response patterns,” not “zero semantic loss.” |
| C9 | `keep_as_metaphor` | Label as explanatory metaphor, not industry consensus. |
| C10 | `keep_as_hypothesis` | Phrase as “plausible risk that vague inputs amplify model errors,” not proven causality. |

## New Claims Introduced By Wave 1

| id | claim | provisional strength | evidence |
| --- | --- | --- | --- |
| N1 | `AGENTS.md` is a cross-tool adoption candidate but not yet semantically uniform | B | [`../_reference/00-shared-codex-agents-md-spec.md`](../_reference/00-shared-codex-agents-md-spec.md), [`../_reference/06-agent-format-amp-agents-md-adoption.md`](../_reference/06-agent-format-amp-agents-md-adoption.md), [`../_reference/06-agent-format-github-copilot-agents-md-support.md`](../_reference/06-agent-format-github-copilot-agents-md-support.md), [`06-agent-format-evidence-summary.md`](06-agent-format-evidence-summary.md) |
| N2 | Large single instruction files are a documented failure mode | B | [`../_reference/06-agent-format-openai-harness-engineering.md`](../_reference/06-agent-format-openai-harness-engineering.md), [`../_reference/00-shared-claude-code-official.md`](../_reference/00-shared-claude-code-official.md) |
| N3 | Feature-level spec workflows are now official product/tool workflows | B | [`../_reference/04-future-trends-github-spec-kit-official.md`](../_reference/04-future-trends-github-spec-kit-official.md), [`../_reference/04-future-trends-kiro-spec-workflow-official.md`](../_reference/04-future-trends-kiro-spec-workflow-official.md) |
| N4 | Structured documentation and traceability pressure is increasing under AI governance | A | [`../_reference/04-future-trends-ai-governance-nist-eu-ai-act.md`](../_reference/04-future-trends-ai-governance-nist-eu-ai-act.md) |

## First-Pass New-Claim Decisions

| id | v2 decision | final-use guidance |
| --- | --- | --- |
| N1 | Use as “cross-tool adoption candidate,” not “semantic standard.” | Strong enough for trend section, not enough for behavior-uniformity claim |
| N2 | Use as strong failure-mode evidence. | Can directly support “avoid one big instruction file” |
| N3 | Use as strong workflow-existence evidence. | Do not overstate adoption maturity |
| N4 | Use as strong governance-pressure evidence. | Do not claim any specific requirements format is legally required |

## Second-Pass New-Claim Recommendations

| id | final-use recommendation | wording rule |
| --- | --- | --- |
| N1 | `keep_with_precision` | “AGENTS.md is an adoption candidate / convention with cross-tool format-convergence evidence, not a fully uniform semantic standard.” |
| N2 | `keep` | “Large always-loaded instruction files are a documented failure mode.” |
| N3 | `keep_with_maturity_caveat` | “Feature-level spec workflows now exist in official tools; adoption maturity is still emerging.” |
| N4 | `keep` | “Governance trends increase demand for documentation, logs, traceability, and oversight.” |

## Final-Candidate Additions

| id | claim | provisional strength | evidence | final-use guidance |
| --- | --- | --- | --- | --- |
| N5 | SysML v2 provides an official model-layer anchor for requirements / behavior / structure relationships, complementing textual requirement formats | A | [`../_reference/01-re-landscape-omg-sysml-v2-official.md`](../_reference/01-re-landscape-omg-sysml-v2-official.md), [`01-re-landscape-evidence-summary.md`](01-re-landscape-evidence-summary.md) | Use as official positioning proof; do not use as proof of 2026 tool maturity or broad industrial adoption. |
| N6 | Amp / Sourcegraph switching from `AGENT.md` to `AGENTS.md` strengthens the cross-tool format-convergence claim | B | [`../_reference/06-agent-format-amp-agents-md-adoption.md`](../_reference/06-agent-format-amp-agents-md-adoption.md), [`06-agent-format-evidence-summary.md`](06-agent-format-evidence-summary.md) | Use as non-OpenAI tool-vendor adoption evidence; still avoid semantic-uniformity or enterprise-outcome claims. |
| N7 | Non-tool-vendor enterprise-internal coding-agent usage is now publicly supported by Stripe's Minions case, which also reinforces shared rule-file and scoped-rule layering patterns | B | [`../_reference/06-agent-format-stripe-minions-enterprise-usage.md`](../_reference/06-agent-format-stripe-minions-enterprise-usage.md), [`06-agent-format-evidence-summary.md`](06-agent-format-evidence-summary.md) | Use as enterprise-existence evidence; do not inflate one company case into a market-wide adoption census. |
| N8 | DoD SysML v2 transition guidance upgrades SysML v2 from OMG-only positioning to external official transition/adoption signal, without proving broad cross-industry maturity | A | [`../_reference/01-re-landscape-dod-sysml-v2-transition-guidance.md`](../_reference/01-re-landscape-dod-sysml-v2-transition-guidance.md), [`01-re-landscape-evidence-summary.md`](01-re-landscape-evidence-summary.md) | Use as non-OMG transition/adoption signal; do not rewrite it into a broad industrial adoption census. |
| N9 | Knowledge-graph adoption for requirements-related artifacts is now supported not only by RE research and customer-requirements matching, but also by a BMW virtual product-development collaboration case | A | [`../_reference/04-future-trends-bmw-virtual-product-development-kg.md`](../_reference/04-future-trends-bmw-virtual-product-development-kg.md), [`04-future-trends-evidence-summary.md`](04-future-trends-evidence-summary.md) | Use as broader product-development graph signal; do not generalize it into a universal software-team norm. |
| N10 | Coding-agent adoption breadth is no longer only anecdotal: a 2026 large-scale GitHub study shows broad adoption across project maturity, established organizations, and diverse languages/topics | A | [`../_reference/06-agent-format-github-adoption-study-2026.md`](../_reference/06-agent-format-github-adoption-study-2026.md), [`06-agent-format-evidence-summary.md`](06-agent-format-evidence-summary.md) | Use as adoption-breadth evidence; do not treat it as format-semantic or workflow-choice proof. |
| N11 | Mike Cohn's 2004 official slides strengthen the negative boundary of user stories: they are placeholders for future conversations, not written contracts, not fixed software requirements, and not use cases | B | [`../_reference/02-user-story-cohn-2004-intro-slides.md`](../_reference/02-user-story-cohn-2004-intro-slides.md), [`02-user-story-evidence-summary.md`](02-user-story-evidence-summary.md) | Use as anti-pattern/boundary support; do not overstate it as a full story-smell taxonomy. |
| N12 | Collins Aerospace / DARPA PROVERS provides a second non-OMG external signal that SysML v2 is entering defense-industry engineering pipelines and is framed as necessary for mass adoption in the Defense Industrial Base | B | [`../_reference/01-re-landscape-collins-sysml-v2-provers.md`](../_reference/01-re-landscape-collins-sysml-v2-provers.md), [`01-re-landscape-evidence-summary.md`](01-re-landscape-evidence-summary.md) | Use as defense-industry adoption signal; do not overstate it as broad cross-industry maturity. |
| N13 | Multimodal requirements/spec workflows are now supported by more than one official product path: Figma Make and Vercel v0 both combine visual/media inputs with generation and spec-oriented workflow steps | B | [`../_reference/04-future-trends-figma-make-multimodal-signal.md`](../_reference/04-future-trends-figma-make-multimodal-signal.md), [`../_reference/04-future-trends-vercel-v0-multimodal-prd-workflow.md`](../_reference/04-future-trends-vercel-v0-multimodal-prd-workflow.md), [`04-future-trends-evidence-summary.md`](04-future-trends-evidence-summary.md) | Use as multimodal workflow-existence evidence; do not turn it into a claim of mainstream adoption or superiority. |
| N14 | OpenSpec official docs upgrade Topic 06 from indirect multi-source reading to one direct cross-tool workflow/config comparison anchor across Spec Kit, Kiro, and 25+ agent tools | B | [`../_reference/06-agent-format-openspec-cross-tool-comparison.md`](../_reference/06-agent-format-openspec-cross-tool-comparison.md), [`06-agent-format-evidence-summary.md`](06-agent-format-evidence-summary.md) | Use as direct-comparison evidence; do not treat it as proof of semantic uniformity or runtime-behavior consistency. |
| N15 | O'Reilly preview pages strengthen Topic 02 by directly exposing both `What Stories Are Not` boundary framing and at least one concrete `Story Smells` item (`Stories Are Too Small`) | B | [`../_reference/02-user-story-cohn-story-smells-preview.md`](../_reference/02-user-story-cohn-story-smells-preview.md), [`02-user-story-evidence-summary.md`](02-user-story-evidence-summary.md) | Use as preview-level anti-pattern support; do not overstate it as a full captured taxonomy. |
| N16 | INCOSE IS 2025 automotive SysML v2 resource metadata extends Topic 01 beyond government/defense orbit into a bounded commercial-industrial signal, while remaining metadata-grade evidence | B | [`../_reference/01-re-landscape-incose-automotive-sysml-v2-case-metadata.md`](../_reference/01-re-landscape-incose-automotive-sysml-v2-case-metadata.md), [`01-re-landscape-evidence-summary.md`](01-re-landscape-evidence-summary.md) | Use as bounded non-defense signal; do not rewrite metadata into implementation maturity or broad industrial census. |
| N17 | Vercel's hosted Stripe case adds an early named outcome signal for AI app-building/spec workflows, but remains a single vendor-hosted case rather than market-wide adoption proof | C | [`../_reference/04-future-trends-vercel-v0-stripe-outcomes.md`](../_reference/04-future-trends-vercel-v0-stripe-outcomes.md), [`04-future-trends-evidence-summary.md`](04-future-trends-evidence-summary.md) | Use as hosted outcome evidence with caution; keep quantitative impact claims out of headline conclusions unless independently upgraded. |
| N18 | InformIT's official TOC upgrades Topic 02 from one previewed story smell to publisher-level visibility of the broader Chapter 14 smell taxonomy and Chapter 12 negative-boundary substructure | B | [`../_reference/02-user-story-cohn-story-smells-informit-toc.md`](../_reference/02-user-story-cohn-story-smells-informit-toc.md), [`02-user-story-evidence-summary.md`](02-user-story-evidence-summary.md) | Use as taxonomy-existence evidence; do not treat it as full smell-discussion capture. |
| N19 | An official INCOSE/OMG SysML v2 update deck broadens Topic 01 from a single non-defense metadata point to a multi-organization non-defense participation signal via named end-user organizations such as Ford, GM, John Deere, and Siemens | B | [`../_reference/01-re-landscape-sysml-v2-update-end-user-orgs.md`](../_reference/01-re-landscape-sysml-v2-update-end-user-orgs.md), [`01-re-landscape-evidence-summary.md`](01-re-landscape-evidence-summary.md) | Use as broader participation evidence; do not rewrite it into implementation maturity or outcome proof. |
| N20 | Personagram provides an independent empirical outcome signal for multimodal product-design workflows, but remains a bounded HCI study rather than enterprise adoption proof | A | [`../_reference/04-future-trends-personagram-multimodal-design-study.md`](../_reference/04-future-trends-personagram-multimodal-design-study.md), [`04-future-trends-evidence-summary.md`](04-future-trends-evidence-summary.md) | Use as independent workflow-outcome evidence; do not generalize it into mainstream requirements adoption. |
| N21 | Cline, Continue, and Aider official docs show cross-tool rule/instruction semantics diverge in loading order, precedence, nested scope, and chat inclusion behavior | B | [`../_reference/06-agent-format-rule-loading-semantics-comparison.md`](../_reference/06-agent-format-rule-loading-semantics-comparison.md), [`06-agent-format-evidence-summary.md`](06-agent-format-evidence-summary.md) | Use as semantic-divergence evidence; do not treat cross-tool format support as semantic portability. |
| N22 | Cohn's 2024 official blog gives discussion-level support for the `Stories Are Too Small` smell by identifying dependency, prioritization, and tracking overhead from overly small stories | B | [`../_reference/02-user-story-cohn-too-small-stories-2024.md`](../_reference/02-user-story-cohn-too-small-stories-2024.md), [`02-user-story-evidence-summary.md`](02-user-story-evidence-summary.md) | Use as one-smell discussion evidence; do not treat it as full Chapter 14 capture. |
| N23 | Productive4.0 / Arrowhead provides a non-defense SysML v2 validation/prototype use-case in Industry 4.0 / chemical / IIoT context | B | [`../_reference/01-re-landscape-productive40-sysml-v2-validation-use-case.md`](../_reference/01-re-landscape-productive40-sysml-v2-validation-use-case.md), [`01-re-landscape-evidence-summary.md`](01-re-landscape-evidence-summary.md) | Use as implementation-validation evidence; do not rewrite it into broad production maturity or quantified outcome proof. |
| N24 | AI4UI provides enterprise-grade multimodal design/spec-to-code benchmark evidence from Figma requirement encoding to engineering-ready UI code, but not independent adoption census | A | [`../_reference/04-future-trends-ai4ui-enterprise-pixel-to-production.md`](../_reference/04-future-trends-ai4ui-enterprise-pixel-to-production.md), [`04-future-trends-evidence-summary.md`](04-future-trends-evidence-summary.md) | Use as framework benchmark / enterprise-grade workflow evidence; do not state industry-wide production adoption. |
| N25 | A 2026 empirical study of agent rule files shows rules can improve coding-agent outcomes overall while certain rule types, especially positive directives, can hurt performance | A | [`../_reference/06-agent-format-rules-shape-or-distort-2026.md`](../_reference/06-agent-format-rules-shape-or-distort-2026.md), [`06-agent-format-evidence-summary.md`](06-agent-format-evidence-summary.md) | Use as rule-effect/failure evidence; do not overgeneralize beyond its agent/benchmark setup. |
| N26 | Mountain Goat's official curriculum broadens Topic 02 from single story-smell discussion to a practice-facing taxonomy of common story problems and non-story item boundaries | B | [`../_reference/02-user-story-mountain-goat-common-problems-taxonomy.md`](../_reference/02-user-story-mountain-goat-common-problems-taxonomy.md), [`02-user-story-evidence-summary.md`](02-user-story-evidence-summary.md) | Use as practice taxonomy evidence; do not treat it as full Chapter 14 discussion text. |
| N27 | AGENTbench / Evaluating AGENTS.md provides multi-agent evidence that repository-level context files are not automatically beneficial: LLM-generated files can reduce success and increase cost, while developer-written files are only marginally beneficial on average | A | [`../_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md`](../_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md), [`06-agent-format-evidence-summary.md`](06-agent-format-evidence-summary.md) | Use as multi-agent context-file evaluation evidence; do not present it as a formal semantic conformance suite or as proof that all context files are harmful. |
| N28 | FlowForge provides same-prototype evidence for a BPMN/DMN -> User Story/Gherkin chain, but not production or EARS-inclusive governance | A | [`../_reference/05-integration-bdd-flowforge-bpmn-dmn-gherkin.md`](../_reference/05-integration-bdd-flowforge-bpmn-dmn-gherkin.md), [`05-integration-bdd-evidence-summary.md`](05-integration-bdd-evidence-summary.md) | Use as same-chain prototype evidence; do not present it as a high-compliance production case or as evidence that EARS was integrated. |
| N29 | ISTQB Acceptance Testing syllabus provides an official governance frame linking requirements/user stories, acceptance criteria, Gherkin tests, BPMN/DMN models, and traceability | B | [`../_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md`](../_reference/05-integration-bdd-istqb-acceptance-testing-syllabus.md), [`05-integration-bdd-evidence-summary.md`](05-integration-bdd-evidence-summary.md) | Use as governance-framework evidence; do not treat it as a single-project case or EARS-specific recommendation. |
| N30 | UX Tools State of Prototyping 2026 provides independent open-survey evidence that AI prototyping / design-to-code workflows, including Figma Make and Claude Code, have meaningful reported adoption among designers/builders | C | [`../_reference/04-future-trends-state-of-prototyping-2026.md`](../_reference/04-future-trends-state-of-prototyping-2026.md), [`04-future-trends-evidence-summary.md`](04-future-trends-evidence-summary.md) | Use as independent adoption-census evidence; do not treat self-reported survey adoption or trust as verified production deployment. |
| N31 | A same-repo practitioner experiment shows `AGENTS.md` / `CLAUDE.md` is a useful repo-local contract but not a cross-tool conformance guarantee; different agent/scaffolding setups followed the same rules differently and none fully matched the target style | C | [`../_reference/06-agent-format-umans-agents-md-following-experiment.md`](../_reference/06-agent-format-umans-agents-md-following-experiment.md), [`06-agent-format-evidence-summary.md`](06-agent-format-evidence-summary.md) | Use as conformance-adjacent practitioner evidence; do not present it as a formal semantic conformance suite or universal model/tool ranking. |
| N32 | User stories should not be collapsed into BDD feature files or mini-requirements specs; Seb Rose's origin/boundary article ties XP/Beck stories to conversation/value focus and warns against cargo-cult template use | C | [`../_reference/02-user-story-rose-user-stories-bdd-origin-boundary.md`](../_reference/02-user-story-rose-user-stories-bdd-origin-boundary.md), [`02-user-story-evidence-summary.md`](02-user-story-evidence-summary.md), [`05-integration-bdd-evidence-summary.md`](05-integration-bdd-evidence-summary.md) | Use as Beck-adjacent origin/boundary support; do not treat it as Beck verbatim full text or Chapter 14 full-discussion capture. |
| N33 | Figma's Findable customer story gives a named real deployment case for AI-assisted design-to-code/app-shell work, with reported 50% faster delivery and 90%+ final product code from Figma Make | C | [`../_reference/04-future-trends-figma-make-findable-production-case.md`](../_reference/04-future-trends-figma-make-findable-production-case.md), [`04-future-trends-evidence-summary.md`](04-future-trends-evidence-summary.md) | Use as vendor-hosted named deployment evidence; do not treat the outcome numbers as independently verified or as proof of broad production maturity. |
| N34 | OctoBench provides formal benchmark evidence for scaffold-aware instruction following in repository-grounded agentic coding, separating task-solving from scaffold-compliance, but it is not an exact cross-tool `AGENTS.md` / `CLAUDE.md` semantic conformance suite | A | [`../_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md`](../_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md), [`06-agent-format-evidence-summary.md`](06-agent-format-evidence-summary.md) | Use as formal scaffold-aware compliance benchmark evidence; do not treat it as proof of instruction-file semantic uniformity across tools. |

## Open Audit Tasks

1. Numeric-effect claims remain excluded from the main narrative unless independently upgraded.
2. Preserve the distinction between official presentation/catalog evidence and full standard text.
3. Preserve the distinction between tool-vendor format adoption, direct workflow/config comparison, multi-agent effect evaluation, practitioner cross-tool instruction-following experiments, formal scaffold-aware compliance benchmarking, and exact cross-tool semantic conformance.
4. Preserve the distinction between hosted outcome cases and broader adoption maturity.
