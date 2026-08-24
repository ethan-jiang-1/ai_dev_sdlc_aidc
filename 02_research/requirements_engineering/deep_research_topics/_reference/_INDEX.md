# _INDEX — 30 秒本地证据检索入口

> 本文件是 `navigation layer`，不是证据本体，也不是 artifact。
> 每新增 / 删除 / 重命名一份 Authoritative Copy，必须同步刷新相应分组。

## 导航锚点

- 设计态蓝图：[`../../plan/dr-round-1.plan.md`](../../plan/dr-round-1.plan.md)
- 执行态状态：[`../../plan/dr-round-1.status.md`](../../plan/dr-round-1.status.md)
- 执行队列：[`../../plan/dr-round-1.queue.md`](../../plan/dr-round-1.queue.md)
- 证据强度初版：[`../claims-audit.md`](../claims-audit.md)
- 目录总览：[`../README.md`](../README.md)

## 分组：共享地基（`00-shared-*`）

进入本组的材料要求：对 ≥2 条研究线有直接用途，或构成跨主题术语与对象分类的共同地基。

| file | title | tier | source_type | related_topic | accessed_at |
| --- | --- | --- | --- | --- | --- |
| [00-shared-incose-gtwr-v4-summary.md](00-shared-incose-gtwr-v4-summary.md) | INCOSE GtWR v4 Summary Sheet & 42-Rule Overview | A | standard + guide | 01, 02, 03, 05, 06 | 2026-04-17 |
| [00-shared-iso-iec-ieee-29148-2018.md](00-shared-iso-iec-ieee-29148-2018.md) | ISO/IEC/IEEE 29148:2018 — Requirements engineering life cycle processes | A | standard | 01, 02, 03, 04, 05, 06 | 2026-04-17 |
| [00-shared-mavin-2009-ears-re09.md](00-shared-mavin-2009-ears-re09.md) | Alistair Mavin 2009 — Easy Approach to Requirements Syntax (EARS) [RE'09] | A | academic + official author guide | 03 (primary), 01, 04, 05, 06 | 2026-04-17 |
| [00-shared-cursor-rules-official.md](00-shared-cursor-rules-official.md) | Cursor Rules — Official Documentation (`.cursor/rules/*.mdc` + AGENTS.md) | B | official product docs | 06 (primary), 03, 04, 05 | 2026-04-17 |
| [00-shared-claude-code-official.md](00-shared-claude-code-official.md) | Anthropic Claude Code — Best Practices & CLAUDE.md official guidance | B | official product docs | 06 (primary), 03, 04, 05 | 2026-04-17 |
| [00-shared-codex-agents-md-spec.md](00-shared-codex-agents-md-spec.md) | AGENTS.md open format spec + OpenAI Codex CLI integration (Linux Foundation AAIF) | B | community standard + vendor official | 06 (primary), 04, 05 | 2026-04-17 |
| [00-shared-fowler-user-story-bliki.md](00-shared-fowler-user-story-bliki.md) | Martin Fowler bliki — UserStory (KOL anchor) | B | KOL blog | 02 (primary), 01, 04, 05 | 2026-04-17 |
| [00-shared-fowler-given-when-then-bliki.md](00-shared-fowler-given-when-then-bliki.md) | Martin Fowler bliki — GivenWhenThen (KOL anchor for BDD syntax) | B | KOL blog | 05 (primary), 02, 03, 04 | 2026-04-17 |
| [00-shared-gherkin-official-reference.md](00-shared-gherkin-official-reference.md) | Gherkin Official Reference (Cucumber keywords + structure) | B | official product docs | 05 (primary), 02, 03 | 2026-04-17 |
| [00-shared-cohn-user-stories-primer.md](00-shared-cohn-user-stories-primer.md) | Mike Cohn — Mountain Goat User Stories primer + *User Stories Applied* | A | practitioner primer + standard book | 02 (primary), 01, 05, 06 | 2026-04-17 |
| [00-shared-patton-story-mapping-primer.md](00-shared-patton-story-mapping-primer.md) | Jeff Patton — *The New User Story Backlog is a Map* + *User Story Mapping* book | A | KOL blog + standard book | 02 (primary), 01, 04, 05 | 2026-04-17 |
| [00-shared-iso-26262-part8-overview.md](00-shared-iso-26262-part8-overview.md) | ISO 26262-8:2018 Part 8 — Supporting Processes (Clause 6 + Clause 11 focus) | C | standard (paywalled) + industry primer | 04, 05 (limitation face), 02, 03, 06 | 2026-04-17 |

## 分组：研究线 01 — re-landscape（`01-re-landscape-*`）

| file | title | tier | source_type | accessed_at |
| --- | --- | --- | --- | --- |
| [01-re-landscape-sebok-system-requirements-definition.md](01-re-landscape-sebok-system-requirements-definition.md) | SEBoK 2025 — System Requirements Definition and related requirements engineering pages | A | official body of knowledge | 2026-04-18 |
| [01-re-landscape-iso-iec-ieee-15288-2023-overview.md](01-re-landscape-iso-iec-ieee-15288-2023-overview.md) | ISO/IEC/IEEE 15288:2023 — System life cycle processes official overview | A | standard catalog page / official abstract | 2026-04-18 |
| [01-re-landscape-use-case-2-0-official.md](01-re-landscape-use-case-2-0-official.md) | Ivar Jacobson International — Use-Case 2.0 official pages | B | official method page + official e-book landing page | 2026-04-18 |
| [01-re-landscape-omg-sysml-v2-official.md](01-re-landscape-omg-sysml-v2-official.md) | OMG SysML v2.0 — Official specification and MBSE requirements-modeling signal | A | official standard / specification | 2026-04-18 |
| [01-re-landscape-omg-sysml-v2-tools-ecosystem.md](01-re-landscape-omg-sysml-v2-tools-ecosystem.md) | OMG 2025 — SysML v2 tools ecosystem and pilot implementation signal | A | official standards community tools catalog | 2026-04-18 |
| [01-re-landscape-dod-sysml-v2-transition-guidance.md](01-re-landscape-dod-sysml-v2-transition-guidance.md) | U.S. DoD OUSW(R&E) 2026 — SysML v2 transition guidance as non-OMG adoption / maturity signal | A | official government guidance / technical highlight | 2026-04-18 |
| [01-re-landscape-collins-sysml-v2-provers.md](01-re-landscape-collins-sysml-v2-provers.md) | Collins Aerospace / DARPA PROVERS 2025 — SysML v2 industrial adoption signal in high-assurance engineering toolchain | B | official industry presentation | 2026-04-18 |
| [01-re-landscape-incose-automotive-sysml-v2-case-metadata.md](01-re-landscape-incose-automotive-sysml-v2-case-metadata.md) | INCOSE IS 2025 — Automotive SysML v2 case metadata as non-defense adoption signal | B | official resource metadata / conference case page | 2026-04-18 |
| [01-re-landscape-sysml-v2-update-end-user-orgs.md](01-re-landscape-sysml-v2-update-end-user-orgs.md) | INCOSE / OMG SysML v2 Update — non-defense end-user organization participation signal | B | official standards-community presentation / update deck | 2026-04-18 |
| [01-re-landscape-productive40-sysml-v2-validation-use-case.md](01-re-landscape-productive40-sysml-v2-validation-use-case.md) | Productive4.0 / Arrowhead 2020 — SysML v2 validation use-case for Industry 4.0 service-oriented architecture | B | official EU industry-project result / consortium report | 2026-04-18 |

## 分组：研究线 02 — user-story（`02-user-story-*`）

| file | title | tier | source_type | accessed_at |
| --- | --- | --- | --- | --- |
| [02-user-story-cohn-book-excerpts.md](02-user-story-cohn-book-excerpts.md) | Mike Cohn 2004/2026 — User Stories Applied official book page + sample chapter excerpts | A | standard book + official sample chapter | 2026-04-18 |
| [02-user-story-wake-invest-original.md](02-user-story-wake-invest-original.md) | Bill Wake 2003 — INVEST in Good Stories, and SMART Tasks | B | practitioner original article | 2026-04-18 |
| [02-user-story-mike-cohn-ai-era.md](02-user-story-mike-cohn-ai-era.md) | Mike Cohn 2024/2026 — Revisiting User Stories and using AI to write better stories | B | official podcast + official KOL blog | 2026-04-18 |
| [02-user-story-xp-origins-cockburn-boundary.md](02-user-story-xp-origins-cockburn-boundary.md) | Kent Beck / Martin Fowler / Alistair Cockburn — XP story origins and use-case boundary | B | official book page + KOL bliki + official author article | 2026-04-18 |
| [02-user-story-subtypes-job-spike-enabler.md](02-user-story-subtypes-job-spike-enabler.md) | Intercom / Agile Alliance / SAFe — Job Story, Spike, and Enabler boundary starter pack | B | official product-method blog + glossary pages + framework glossary | 2026-04-18 |
| [02-user-story-beck-planning-xp-previews.md](02-user-story-beck-planning-xp-previews.md) | Kent Beck / Martin Fowler 1999–2000 — XP planning and writing-stories preview anchors | B | official publisher metadata + book preview pages | 2026-04-18 |
| [02-user-story-cohn-2004-intro-slides.md](02-user-story-cohn-2004-intro-slides.md) | Mike Cohn 2004 — Introduction to User Stories slides as direct anti-pattern / boundary anchor | B | official presentation slides | 2026-04-18 |
| [02-user-story-cohn-story-smells-preview.md](02-user-story-cohn-story-smells-preview.md) | Mike Cohn 2004 — O'Reilly previews for `What Stories Are Not` and `Story Smells` | B | official book preview pages | 2026-04-18 |
| [02-user-story-cohn-story-smells-informit-toc.md](02-user-story-cohn-story-smells-informit-toc.md) | Mike Cohn 2004 — InformIT table of contents for `What Stories Are Not` and the full `Story Smells` chapter taxonomy | B | official publisher book page / table of contents | 2026-04-18 |
| [02-user-story-cohn-too-small-stories-2024.md](02-user-story-cohn-too-small-stories-2024.md) | Mike Cohn 2024 — Overly small user stories as a concrete story-smell discussion | B | official KOL blog | 2026-04-18 |
| [02-user-story-mountain-goat-common-problems-taxonomy.md](02-user-story-mountain-goat-common-problems-taxonomy.md) | Mountain Goat Software 2026 — common user-story problems and non-story item taxonomy | B | official training curriculum page | 2026-04-18 |
| [02-user-story-rose-user-stories-bdd-origin-boundary.md](02-user-story-rose-user-stories-bdd-origin-boundary.md) | Seb Rose 2022 — User Stories and BDD Part 1, origin and BDD boundary | C | practitioner journal / KOL article | 2026-04-18 |

## 分组：研究线 03 — ears（`03-ears-*`）

| file | title | tier | source_type | accessed_at |
| --- | --- | --- | --- | --- |
| [03-ears-uusitalo-2023-plc-empirical.md](03-ears-uusitalo-2023-plc-empirical.md) | An Experiment in Requirements Engineering and Testing using EARS Notation for PLC Systems | A | academic (conference/workshop paper) | 2026-04-18 |
| [03-ears-mavin-2016-ears-guidelines.md](03-ears-mavin-2016-ears-guidelines.md) | The Easy Approach to Requirements Syntax: The Definitive Guide + RE 2016 lessons-learned trace | B | official guide + academic bibliographic trace | 2026-04-18 |
| [03-ears-jama-industrial-primer.md](03-ears-jama-industrial-primer.md) | Jama webinar — Adopting the EARS Notation to Improve Requirements Engineering | B | official webinar deck / vendor industrial primer | 2026-04-18 |
| [03-ears-software-scope-guidance.md](03-ears-software-scope-guidance.md) | QRA 2025 — EARS software-scope guidance and low-level software specification boundary | B | official practitioner guidance + official author biography | 2026-04-18 |

## 分组：研究线 04 — future-trends（`04-future-trends-*`）

| file | title | tier | source_type | accessed_at |
| --- | --- | --- | --- | --- |
| [04-future-trends-github-spec-kit-official.md](04-future-trends-github-spec-kit-official.md) | GitHub Spec Kit — official signal for Spec-Driven Development as workflow | B | official repository documentation | 2026-04-18 |
| [04-future-trends-kiro-spec-workflow-official.md](04-future-trends-kiro-spec-workflow-official.md) | Amazon Kiro — official signal for IDE-native specs and steering | B | official product documentation | 2026-04-18 |
| [04-future-trends-ai-governance-nist-eu-ai-act.md](04-future-trends-ai-governance-nist-eu-ai-act.md) | NIST AI RMF 1.0 + EU AI Act — official governance signals for documentation, risk, and traceability | A | official framework + official legal text | 2026-04-18 |
| [04-future-trends-thoughtworks-spec-driven-development-signal.md](04-future-trends-thoughtworks-spec-driven-development-signal.md) | Thoughtworks Technology Radar Vol. 33 (2025) — Spec-driven development as an emerging technique | C | industry radar / KOL trend report | 2026-04-18 |
| [04-future-trends-figma-make-multimodal-signal.md](04-future-trends-figma-make-multimodal-signal.md) | Figma Make 2025 — Official multimodal prompt-to-code signal for requirements inputs | B | official product documentation | 2026-04-18 |
| [04-future-trends-figma-make-findable-production-case.md](04-future-trends-figma-make-findable-production-case.md) | Figma 2026 — Findable Figma Make app-shell production case | C | official hosted customer story / case study | 2026-04-18 |
| [04-future-trends-vercel-v0-multimodal-prd-workflow.md](04-future-trends-vercel-v0-multimodal-prd-workflow.md) | Vercel v0 2025–2026 — Multimodal inputs and PRD-to-spec workflow | B | official product documentation | 2026-04-18 |
| [04-future-trends-w3c-shacl-graph-constraints.md](04-future-trends-w3c-shacl-graph-constraints.md) | W3C RDF / SHACL — Official graph-data and constraint-language signal for graph-shaped requirement artifacts | A | official standard / standards overview | 2026-04-18 |
| [04-future-trends-kg-empire-re-knowledge-graph.md](04-future-trends-kg-empire-re-knowledge-graph.md) | KG-EmpiRE 2024 — Requirements-engineering-specific knowledge graph signal | A | academic preprint / accepted conference paper | 2026-04-18 |
| [04-future-trends-ibm-enterprise-requirements-kg.md](04-future-trends-ibm-enterprise-requirements-kg.md) | IBM Research 2023 — Enterprise knowledge graph approach for customer requirements | A | industry research conference paper landing page | 2026-04-18 |
| [04-future-trends-bmw-virtual-product-development-kg.md](04-future-trends-bmw-virtual-product-development-kg.md) | BMW Group / TU Dresden 2025 — Knowledge graph in virtual product development for collaboration | A | academic industry-collaborative conference paper | 2026-04-18 |
| [04-future-trends-vercel-v0-stripe-outcomes.md](04-future-trends-vercel-v0-stripe-outcomes.md) | Vercel / Stripe 2026 — v0 customer story as outcome signal for app-building AI workflow | C | official hosted customer story / case study | 2026-04-18 |
| [04-future-trends-personagram-multimodal-design-study.md](04-future-trends-personagram-multimodal-design-study.md) | Personagram 2026 — multimodal LLM product-design workflow with comparative user-study outcomes | A | academic preprint | 2026-04-18 |
| [04-future-trends-ai4ui-enterprise-pixel-to-production.md](04-future-trends-ai4ui-enterprise-pixel-to-production.md) | AI4UI 2025 — enterprise-grade pixel-to-production frontend workflow from Figma requirements | A | academic preprint | 2026-04-18 |
| [04-future-trends-state-of-prototyping-2026.md](04-future-trends-state-of-prototyping-2026.md) | UX Tools 2026 — State of Prototyping independent survey for AI design-to-code adoption | C | independent industry survey + open dataset | 2026-04-18 |

## 分组：研究线 05 — integration-bdd（`05-integration-bdd-*`）

| file | title | tier | source_type | accessed_at |
| --- | --- | --- | --- | --- |
| [05-integration-bdd-adzic-specification-by-example.md](05-integration-bdd-adzic-specification-by-example.md) | Gojko Adzic 2011/2020 — Specification by Example and its 10-year follow-up | A | official book page + official follow-up article | 2026-04-18 |
| [05-integration-bdd-wynne-cucumber-book-example-guided.md](05-integration-bdd-wynne-cucumber-book-example-guided.md) | Matt Wynne 2017/2019 — The Cucumber Book and Example-guided Development | B | official author page + official Cucumber blog | 2026-04-18 |
| [05-integration-bdd-cucumber-discovery-formulation-case.md](05-integration-bdd-cucumber-discovery-formulation-case.md) | Cucumber official 2014/2017/2024 — Discovery, Formulation, Example Mapping, and enterprise case | B | official documentation + official blog + hosted case study | 2026-04-18 |
| [05-integration-bdd-omg-dmn-decision-boundary.md](05-integration-bdd-omg-dmn-decision-boundary.md) | OMG DMN 1.5 / 2024 — Decision Model and Notation official decision-model / decision-table boundary | A | official standard / datasheet / specification catalog | 2026-04-18 |
| [05-integration-bdd-flowforge-bpmn-dmn-gherkin.md](05-integration-bdd-flowforge-bpmn-dmn-gherkin.md) | Riskiana et al. 2025 — FlowForge BPMN + DMN to User Stories and Gherkin prototype | A | academic journal article / open-access prototype study | 2026-04-18 |
| [05-integration-bdd-istqb-acceptance-testing-syllabus.md](05-integration-bdd-istqb-acceptance-testing-syllabus.md) | ISTQB 2019/2024 — Acceptance Testing syllabus for requirements, user stories, Gherkin, BPMN, and DMN | B | official professional certification syllabus | 2026-04-18 |

## 分组：研究线 06 — agent-format（`06-agent-format-*`）

| file | title | tier | source_type | accessed_at |
| --- | --- | --- | --- | --- |
| [06-agent-format-openai-codex-adoption.md](06-agent-format-openai-codex-adoption.md) | OpenAI 2025/2026 — How OpenAI uses Codex | B | official product / engineering case study | 2026-04-18 |
| [06-agent-format-openai-harness-engineering.md](06-agent-format-openai-harness-engineering.md) | OpenAI 2026 — Harness engineering: leveraging Codex in an agent-first world | B | official engineering blog | 2026-04-18 |
| [06-agent-format-github-spec-kit-official.md](06-agent-format-github-spec-kit-official.md) | GitHub Spec Kit — Official Spec-Driven Development Workflow | B | official repository documentation | 2026-04-18 |
| [06-agent-format-github-copilot-agents-md-support.md](06-agent-format-github-copilot-agents-md-support.md) | GitHub 2025–2026 — Copilot coding agent support for AGENTS.md and nested instructions | B | official product changelog | 2026-04-18 |
| [06-agent-format-kiro-spec-workflow-official.md](06-agent-format-kiro-spec-workflow-official.md) | Amazon Kiro — Official Specs and Steering Workflow | B | official product documentation | 2026-04-18 |
| [06-agent-format-amp-agents-md-adoption.md](06-agent-format-amp-agents-md-adoption.md) | Amp / Sourcegraph 2025 — From AGENT.md to AGENTS.md | B | official product news / adopter-format case | 2026-04-18 |
| [06-agent-format-openwork-oss-usage.md](06-agent-format-openwork-oss-usage.md) | OpenWork OSS repo 2026 — Public AGENTS.md usage with separate PRD workflow | B | official repository README + official repository AGENTS.md | 2026-04-18 |
| [06-agent-format-stripe-minions-enterprise-usage.md](06-agent-format-stripe-minions-enterprise-usage.md) | Stripe 2026 — Minions enterprise-internal coding-agent usage and rule-layering case | B | official engineering blog | 2026-04-18 |
| [06-agent-format-github-adoption-study-2026.md](06-agent-format-github-adoption-study-2026.md) | arXiv 2026 — Large-scale adoption study of coding agents on GitHub | A | academic preprint | 2026-04-18 |
| [06-agent-format-evaluating-agents-md-agentbench-2026.md](06-agent-format-evaluating-agents-md-agentbench-2026.md) | Gloaguen et al. 2026 — Evaluating AGENTS.md and AGENTbench multi-agent context-file evaluation | A | academic preprint + open benchmark/code repository | 2026-04-18 |
| [06-agent-format-octobench-scaffold-aware-coding-2026.md](06-agent-format-octobench-scaffold-aware-coding-2026.md) | Ding et al. 2026 — OctoBench scaffold-aware instruction following in repository-grounded agentic coding | A | academic preprint / benchmark | 2026-04-18 |
| [06-agent-format-umans-agents-md-following-experiment.md](06-agent-format-umans-agents-md-following-experiment.md) | Umans AI 2025 — practical cross-tool experiment on whether coding agents follow AGENTS.md | C | practitioner experiment / engineering blog | 2026-04-18 |
| [06-agent-format-openspec-cross-tool-comparison.md](06-agent-format-openspec-cross-tool-comparison.md) | OpenSpec 2026 — Cross-tool spec workflow and direct comparison to Spec Kit / Kiro | B | official repository documentation + official docs | 2026-04-18 |
| [06-agent-format-rule-loading-semantics-comparison.md](06-agent-format-rule-loading-semantics-comparison.md) | Cline / Continue / Aider 2026 — rule-loading and precedence semantics comparison | B | official product documentation | 2026-04-18 |
| [06-agent-format-rules-shape-or-distort-2026.md](06-agent-format-rules-shape-or-distort-2026.md) | Zhang et al. 2026 — empirical study of agent rule files and coding-agent performance | A | academic preprint | 2026-04-18 |

## 快速计数

| group | docs | tier-A | tier-B | tier-C | tier-D/E |
| --- | --- | --- | --- | --- | --- |
| 00-shared | 12 | 5 | 6 | 1 | 0 |
| 01-re-landscape | 10 | 5 | 5 | 0 | 0 |
| 02-user-story | 12 | 1 | 10 | 1 | 0 |
| 03-ears | 4 | 1 | 3 | 0 | 0 |
| 04-future-trends | 15 | 7 | 4 | 4 | 0 |
| 05-integration-bdd | 6 | 3 | 3 | 0 | 0 |
| 06-agent-format | 15 | 4 | 10 | 1 | 0 |
| **total** | **74** | **26** | **41** | **7** | **0** |

## 最近一次刷新

- last_updated: `2026-04-18`
- last_action: `Queue continuation: Topic 06 upgraded via OctoBench formal scaffold-aware coding compliance benchmark; reference total = 74`
