# Reference Index: AI-Native SDLC Deep Research

> 计划：`/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round2.md`
> 状态：`/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round2.status.md`
> 队列：`/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round2.queue.md`

## 30-Second Local Evidence Retrieval

如果只需要快速恢复上下文：

- 研究对象与四条主线：读 `topics/README.md` 和计划文件的 topic registry。
- 共享地基：先读本索引的 `Wave 0 Shared Foundation` 表。
- 执行状态：读 status 的 `当前执行快照`、`Gate State`、`Wave 0` 和 `Wave 1`。
- 下一步动作：读 queue 的 `Active Queue`。

## Wave 0 Shared Foundation

| id | local file | source | type | primary topics | why it matters |
| --- | --- | --- | --- | --- | --- |
| `W0-01` | `00-shared-01-thoughtworks-future-software-engineering.md` | ThoughtWorks, `The future of software engineering: Retreat findings and strategic insights` | source seed / field synthesis | `01`, `02`, `03`, `04` | 本轮四个 topic 的原始问题空间，定义 rigor migration、middle loop、Agent OS、security afterthought 和 big-batch regression。 |
| `W0-02` | `00-shared-02-dora-gen-ai-impact-software-development.md` | DORA, `Impact of generative AI in software development` | primary research / practice report | `01`, `02` | 给出 AI 提升个体生产率但可能伤害 delivery stability 的关键反证，支撑 big-batch trap 与组织吸收能力研究。 |
| `W0-03` | `00-shared-03-dora-software-delivery-metrics.md` | DORA software delivery performance metrics | official methodology | `01`, `02` | 固定交付指标口径，避免用代码产量替代软件交付健康度。 |
| `W0-04` | `00-shared-04-anthropic-building-effective-agents.md` | Anthropic, `Building effective agents` | primary engineering guidance | `01`, `03`, `04` | 区分 workflow 与 agent，定义工具、memory、ground truth、测试与人类 checkpoint 对 agent 可靠性的作用。 |
| `W0-05` | `00-shared-05-anthropic-context-engineering-agents.md` | Anthropic, `Effective context engineering for AI agents` | primary engineering guidance | `02`, `03` | 支撑 Agent OS / 工作账本 / 中间循环中的上下文管理、note-taking、compaction 和 sub-agent 架构。 |
| `W0-06` | `00-shared-06-model-context-protocol-spec-2025-11-25.md` | Model Context Protocol specification, revision 2025-11-25 | official protocol spec | `03`, `04` | 固定 LLM app 与外部工具 / 数据连接的协议层术语，为 tool identity、authorization 和 agent runtime 研究提供基准。 |
| `W0-07` | `00-shared-07-nist-ai-rmf-1-0.md` | NIST AI RMF 1.0 | official risk framework | `04`, `02` | 提供 AI 风险治理的 Govern / Map / Measure / Manage 上层框架。 |
| `W0-08` | `00-shared-08-nist-genai-profile-600-1.md` | NIST AI 600-1 Generative AI Profile | official GenAI risk profile | `04`, `01`, `03` | 把 AI RMF 映射到生成式 AI 生命周期，支撑非确定性、评估、治理与信任缺口讨论。 |
| `W0-09` | `00-shared-09-nist-ai-rmf-playbook.md` | NIST AI RMF Playbook | official implementation guide | `04`, `02` | 提供可操作治理动作池，避免治理章节停留在原则层。 |
| `W0-10` | `00-shared-10-owasp-agentic-ai-threats-mitigations.md` | OWASP Agentic AI Threats and Mitigations v1.1 | official security guide | `04`, `03` | 提供 agentic reference architecture、threat model、memory/tool/NHI/confused deputy 等风险词表。 |

## Topic Routing

- `01 engineering-paradigm`: start with `W0-01`, `W0-02`, `W0-03`, `W0-04`.
- `02 organizational-synergy`: start with `W0-01`, `W0-02`, `W0-05`, `W0-07`, `W0-09`.
- `03 agent-native-infrastructure`: start with `W0-01`, `W0-04`, `W0-05`, `W0-06`, `W0-10`.
- `04 security-and-governance`: start with `W0-01`, `W0-06`, `W0-07`, `W0-08`, `W0-09`, `W0-10`.

## Wave 1 Topic 01: Engineering Paradigm

| id | local file | source | type | role in topic |
| --- | --- | --- | --- | --- |
| `T01-01` | `01-engineering-paradigm-01-ears-structured-requirements.md` | EARS / IEEE RE'09 | primary research | structured natural-language spec |
| `T01-02` | `01-engineering-paradigm-02-statecharts-reactive-specification.md` | Harel statecharts paper | primary research | behavioral / reactive specification |
| `T01-03` | `01-engineering-paradigm-03-llm4tdd-best-practices.md` | LLM4TDD | primary research | tests as iterative steering |
| `T01-04` | `01-engineering-paradigm-04-tests-as-prompt-tdd-benchmark.md` | Tests as Prompt | primary research | tests as prompt + verification |
| `T01-05` | `01-engineering-paradigm-05-genai-for-tdd-preliminary-results.md` | GenAI for TDD | primary research | supervision requirement / failure mode |
| `T01-06` | `01-engineering-paradigm-06-llm4tdg-constraint-reasoning.md` | LLM4TDG | primary research | constraint-aware generation |
| `T01-07` | `01-engineering-paradigm-07-salesforce-scaling-code-reviews.md` | Salesforce engineering | primary practitioner source | code review breakdown under AI load |
| `T01-08` | `01-engineering-paradigm-08-salesforce-ai-tooling-quality-safety.md` | Salesforce engineering | primary practitioner source | validation, coverage, and safe shipment |
| `T01-09` | `01-engineering-paradigm-09-type-constrained-code-generation.md` | Type-Constrained Code Generation | primary research | type systems as decoding guardrails |
| `T01-10` | `01-engineering-paradigm-10-autorespec-formal-spec-generation.md` | AutoReSpec | primary research | formal specification generation with validator feedback |
| `T01-11` | `01-engineering-paradigm-11-dora-working-in-small-batches.md` | DORA small batches capability | official research/practice guidance | batch-size measurement and slicing discipline |
| `T01-12` | `01-engineering-paradigm-12-dora-trunk-based-development.md` | DORA trunk-based development capability | official research/practice guidance | short-lived branches, daily merges, CI discipline |
| `T01-13` | `01-engineering-paradigm-13-github-branch-protection-merge-queue.md` | GitHub protected branches docs | official implementation guidance | required checks, merge queue, deployment gates |
| `T01-14` | `01-engineering-paradigm-14-google-sre-canarying-releases.md` | Google SRE workbook | primary practitioner guidance | canary rollout and production exposure slicing |

## Wave 1 Topic 02: Organizational Synergy

| id | local file | source | type | role in topic |
| --- | --- | --- | --- | --- |
| `T02-01` | `02-organizational-synergy-01-dora-ai-amplifier-org-system.md` | DORA 2025 | official research summary | AI amplifies org strengths and weaknesses |
| `T02-02` | `02-organizational-synergy-02-dora-clear-ai-stance.md` | DORA capability guide | official guidance | policy clarity and adoption friction |
| `T02-03` | `02-organizational-synergy-03-dora-trust-in-ai.md` | DORA research insight | research insight | trust calibration and productivity |
| `T02-04` | `02-organizational-synergy-04-dora-builder-mindset.md` | DORA builder mindset | research insight | different trust/control modes across builders |
| `T02-05` | `02-organizational-synergy-05-github-ai-developer-experience-survey.md` | GitHub survey | official practitioner research | collaboration, metrics, upskilling, DevEx |
| `T02-06` | `02-organizational-synergy-06-github-internal-ai-champions.md` | GitHub playbook | primary practitioner source | champion / translator network |
| `T02-07` | `02-organizational-synergy-07-github-thomson-reuters-adoption.md` | Thomson Reuters case | primary practitioner case study | rollout, training, metrics, champion program |
| `T02-08` | `02-organizational-synergy-08-github-executive-support-playbook.md` | GitHub playbook | primary practitioner source | executive translation and manager enablement |
| `T02-09` | `02-organizational-synergy-09-microsoft-frontier-firm-agent-boss.md` | Microsoft Work Trend Index | official workplace research | AI workforce managers and agent specialists |
| `T02-10` | `02-organizational-synergy-10-microsoft-copilot-socialization.md` | Microsoft Research | primary research | onboarding, junior growth, socialization |
| `T02-11` | `02-organizational-synergy-11-github-ai-powered-workforce-playbook.md` | GitHub AI-powered workforce playbook | primary practitioner source | DRI, advocates, metrics, enablement operating model |
| `T02-12` | `02-organizational-synergy-12-microsoft-frontier-firm-roles.md` | Microsoft Work Trend Index 2025 | official practitioner research | emerging AI roles and formal workforce redesign |
| `T02-13` | `02-organizational-synergy-13-atlassian-teamwork-graph.md` | Atlassian Teamwork Graph docs | official implementation guidance | shared context layer across tools and work objects |
| `T02-14` | `02-organizational-synergy-14-atlassian-rovo-ai-trends.md` | Atlassian Rovo analytics docs | official implementation guidance | adoption and agent analytics surfaces |
| `T02-15` | `02-organizational-synergy-15-atlassian-rovo-studio.md` | Atlassian Rovo Studio docs | official implementation guidance | builder workspace for agents, apps, and automations |
| `T02-16` | `02-organizational-synergy-16-atlassian-automating-rovo-agents.md` | Atlassian Rovo agent automation docs | official implementation guidance | triggers, downstream actions, admin-owned automation |

## Wave 1 Topic 03: Agent-Native Infrastructure

| id | local file | source | type | role in topic |
| --- | --- | --- | --- | --- |
| `T03-01` | `03-agent-native-infrastructure-01-anthropic-multi-agent-research-system.md` | Anthropic production article | primary practitioner source | orchestrator-worker, memory, artifacts, resume |
| `T03-02` | `03-agent-native-infrastructure-02-anthropic-managed-agents.md` | Anthropic engineering | primary practitioner source | stable interfaces for long-horizon agents |
| `T03-03` | `03-agent-native-infrastructure-03-anthropic-agent-sdk.md` | Anthropic / Claude blog | primary practitioner source | file system and context substrate |
| `T03-04` | `03-agent-native-infrastructure-04-a2a-protocol.md` | A2A protocol repo | official protocol source | inter-agent interoperability |
| `T03-05` | `03-agent-native-infrastructure-05-autogen-multi-agent-framework.md` | AutoGen | primary research | programmable multi-agent coordination |
| `T03-06` | `03-agent-native-infrastructure-06-memgpt-virtual-context-management.md` | MemGPT | primary research | OS-like memory architecture |
| `T03-07` | `03-agent-native-infrastructure-07-graphrag-paper.md` | GraphRAG paper | primary research | graph-based knowledge substrate |
| `T03-08` | `03-agent-native-infrastructure-08-graphrag-microsoft-blog.md` | Microsoft Research blog | primary practitioner/research explanation | enterprise private-data reasoning |
| `T03-09` | `03-agent-native-infrastructure-09-opentelemetry-genai-semconv.md` | OpenTelemetry | official spec | agent/model observability semantics |
| `T03-10` | `03-agent-native-infrastructure-10-opentelemetry-mcp-semconv.md` | OpenTelemetry | official spec | MCP-aware observability |
| `T03-11` | `03-agent-native-infrastructure-11-temporal-event-history.md` | Temporal docs | official implementation guidance | durable execution event record and replay |
| `T03-12` | `03-agent-native-infrastructure-12-langgraph-persistence-checkpoints.md` | LangGraph docs | official implementation guidance | checkpoints, threads, intermediate writes |
| `T03-13` | `03-agent-native-infrastructure-13-openai-agents-results-state.md` | OpenAI Agents docs | official implementation guidance | resumable state, ownership boundary, run results |
| `T03-14` | `03-agent-native-infrastructure-14-openai-agents-tracing-observability.md` | OpenAI Agents docs | official implementation guidance | traces, handoffs, tool calls, guardrail observability |
| `T03-15` | `03-agent-native-infrastructure-15-inngest-durable-execution.md` | Inngest docs | official implementation guidance | durable step state, retries, memoized outputs |

## Wave 1 Topic 04: Security and Governance

| id | local file | source | type | role in topic |
| --- | --- | --- | --- | --- |
| `T04-01` | `04-security-and-governance-01-nist-zero-trust-architecture.md` | NIST SP 800-207 | official framework | zero-trust baseline |
| `T04-02` | `04-security-and-governance-02-nist-zero-trust-cloud-native.md` | NIST SP 800-207A | official implementation-oriented framework | service/application identity enforcement |
| `T04-03` | `04-security-and-governance-03-nist-implementing-zta.md` | NIST SP 1800-35 | official practice guide | implementable ZTA patterns |
| `T04-04` | `04-security-and-governance-04-google-ai-protection.md` | Google AI Protection | primary practitioner source | lifecycle risk management and virtual red teaming |
| `T04-05` | `04-security-and-governance-05-google-vertex-ai-posture-drift.md` | Google SCC for Vertex AI | primary practitioner source | posture drift, attack-path simulation, exposure score |
| `T04-06` | `04-security-and-governance-06-google-ai-controls-framework.md` | Google AI Controls | primary practitioner source | runtime audit and control monitoring |
| `T04-07` | `04-security-and-governance-07-owasp-llm-top10-2025.md` | OWASP LLM Top 10 | official community guidance | core LLM app threat taxonomy |
| `T04-08` | `04-security-and-governance-08-owasp-mcp-top10.md` | OWASP MCP Top 10 | emerging community guidance | protocol-layer threat taxonomy |
| `T04-09` | `04-security-and-governance-09-mitre-atlas-fact-sheet.md` | MITRE ATLAS | official threat-knowledge-base summary | adversarial testing and threat intelligence |
| `T04-10` | `04-security-and-governance-10-owasp-agentic-top10-2026.md` | OWASP Agentic Top 10 | community peer-reviewed guidance | agent behavior and identity abuse taxonomy |
| `T04-11` | `04-security-and-governance-11-google-wif-best-practices.md` | Google WIF best practices | official implementation guidance | federated NHI auditability and subject mapping |
| `T04-12` | `04-security-and-governance-12-spire-svid-lifecycle.md` | SPIFFE/SPIRE docs | official workload identity docs | attestation, issuance, rotation, trust bundle lifecycle |
| `T04-13` | `04-security-and-governance-13-azure-workload-identity-fail-close.md` | Microsoft Entra Workload ID | official implementation guidance | projected workload identities and fail-close behavior |
| `T04-14` | `04-security-and-governance-14-google-attack-exposure-scores.md` | Google SCC docs | official implementation guidance | attack exposure scoring as blast-radius proxy |
| `T04-15` | `04-security-and-governance-15-google-toxic-combinations.md` | Google SCC docs | official implementation guidance | chokepoints and compound-risk prioritization |
| `T04-16` | `04-security-and-governance-16-microsoft-attack-path-analysis.md` | Microsoft Defender docs | official implementation guidance | graph-based attack path and AI-agent risk context |
| `T04-17` | `04-security-and-governance-17-circleci-incident-report.md` | CircleCI incident report | official vendor disclosure / incident report | CI/CD platform incident and secret blast radius |
| `T04-18` | `04-security-and-governance-18-github-actions-secure-use.md` | GitHub Actions secure use docs | official implementation guidance | immutable workflow deps, OIDC, runner posture, auditability |
| `T04-19` | `04-security-and-governance-19-github-protected-branches-deployment-gate.md` | GitHub protected branches docs | official implementation guidance | merge queue and deployment-success gate |
| `T04-20` | `04-security-and-governance-20-github-artifact-attestations-enforcement.md` | GitHub artifact attestations docs | official implementation guidance | provenance-based admission enforcement |
| `T04-21` | `04-security-and-governance-21-google-binary-authorization.md` | Google Binary Authorization docs | official implementation guidance | deploy-time policy, attestation, audit log, continuous validation |
| `T04-22` | `04-security-and-governance-22-gitlab-protected-environments.md` | GitLab protected environments docs | official implementation guidance | environment approval, access boundary, deployment-only access |

## Index Maintenance Notes

- This index now serves as the unified navigation layer for round1 baseline plus round2 continuation evidence.
- Round2 continuation batches have landed for Topic 02, Topic 03, and Topic 04.
- Do not put long synthesis in this file; use `_artifacts` for synthesis.
