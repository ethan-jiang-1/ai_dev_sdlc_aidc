# AIDLC (AI Development Life Cycle) — Research Index & Summary

**Research Date:** 2026-06-28
**Research Scope:** Comprehensive investigation into the emerging concept of AI-driven Software Development Life Cycle
**Languages Searched:** English and Chinese

---

## What is AIDLC?

**AIDLC** (also called AI-DLC, AI SDLC, Agentic SDLC, ADLC, AI-Native SDLC) is a structured framework that reimagines the traditional Software Development Life Cycle for the AI era. Unlike simply adding AI tools to existing workflows, AIDLC fundamentally restructures how software is built — making AI a core **participant** across every phase, not just an assistant in coding.

The unifying theme across all major frameworks is that **"Intent" replaces "Process"**: humans define intent, specifications, and guardrails; AI autonomously executes across requirements, design, development, testing, deployment, and operations.

---

## Key Terminology

| Term | Meaning |
|------|---------|
| **AI-SDLC** | Traditional SDLC augmented with AI assistance (humans still in full control) |
| **AIDLC / AI-DLC** | AI deeply embedded across the full lifecycle; humans govern, AI executes |
| **ADLC / Agentic-SDLC** | Autonomous AI agents operate independently within development phases |
| **Agentic DevOps** | AI agents manage the downstream pipeline: CI/CD, security, deployment |
| **AI-Native SDLC** | Development process designed from the ground up around AI as primary executor |
| **Vibe Coding** | Conversational development using plain English; coined by Andrej Karpathy (Feb 2025), disavowed for serious work by March 2026 |
| **Agentic Engineering** | Karpathy's replacement term — emphasizes oversight, rigor, and craft with AI agents |
| **Spec-Driven Development (SDD)** | Humans write specifications; AI agents implement against them; humans review at checkpoints |
| **Context Development Lifecycle (CDLC)** | Guy Podjarny/Tessl: humans manage context; agents manage SDLC |

---

## The "Big Seven" Framework Definers

| Organization | Framework Name | Core Emphasis |
|---|---|---|
| **AWS / CI&T** | **AI-DLC** (AI-Driven Development Lifecycle) | Three-phase model: Inception → Construction → Operations; context persistence |
| **Gartner** | **AI-Native Software Engineering** | AI as "Structured Collaborator"; predicts 90% adoption by 2028 |
| **Forrester** | **Agentic Software Development** (Maturity Model) | Five-level quantifiable maturity scale |
| **Microsoft / GitHub** | **Agentic DevOps + Spec-Driven Development** | Copilot as Coding Agent; MCP open protocols |
| **Google Cloud** | **ADLC** (Agentic Development Lifecycle) | Agent lifecycle management as product |
| **IBM** | **DevOps Loop 2.0** | Enterprise-grade agent orchestration using MCP |
| **Atlassian** | **AI-Native SDLC + Software Collection** | Teamwork Graph as neural backbone (15B+ connections) |

---

## Three Eras of Software Engineering

| Era | Period | Defining Characteristic |
|---|---|---|
| **SE 1.0 (Classical)** | ~1970s–2010s | Manual, plan-driven, code-centric. Humans always wrote the code. |
| **SE 2.0 (AI-Assisted)** | 2021–2024 | In-editor code completion (Copilot, Codeium, Tabnine). AI suggests; humans orchestrate. |
| **SE 3.0 (Agentic / AI-Native)** | 2024–present | Intent-driven, model-centric. AI agents autonomously plan, code, test, deploy, maintain. |

---

## Five Levels of AI-SDLC Maturity

| Level | Name | Core Characteristic |
|---|---|---|
| Level 1 | Traditional SDLC | All human-written code; basic tools only |
| Level 2 | AI-Supported | Passive AI assistance: autocomplete, snippets |
| Level 3 | AI-Assisted | AI actively participates: multi-file context, large code generation |
| Level 4 | AI-Native | AI as true collaborator; agents as virtual team members |
| Level 5 | AI-Autonomous | AI as primary implementer; humans do strategy and security review only |

---

## Key Tensions & Open Problems

1. **The productivity paradox**: Felt productivity gains vs. measured productivity losses (METR 2025: devs 19% slower but believe they're 20% faster)
2. **Agent debt**: Unvetted architectural logic from AI causing downstream production incidents (New Relic 2026: 82% report AI-code failures)
3. **Open source backlash**: Zig, OpenJDK, NetBSD, Gentoo, QEMU, cURL, and others have banned or severely restricted AI contributions
4. **Cognitive atrophy**: Developers report losing core skills; "cognitive debt" accumulating as AI generates code no one fully understands
5. **The junior developer crisis**: New engineers relying on AI never develop fundamentals; looming seniority cliff
6. **Governance gaps**: Only 47% of companies have GenAI security controls; 62% ship AI code without line-by-line review
7. **Identity crisis**: Software engineers experiencing "identity crisis bordering on depression" as craft meaning shifts

---

## Files in This Research

| File | Dimension | Description |
|------|-----------|-------------|
| `01_promoters_advocates.md` | Main promoters/advocates | Companies, organizations, and thought leaders actively promoting AIDLC |
| `02_evolution_timeline.md` | Evolution/timeline | Key milestones, papers, and events that shaped the concept |
| `03_community_reactions.md` | Community reactions | Developer and community debates, controversies, and responses |
| `04_current_influencers.md` | Current influencers | Voices currently driving the conversation around AIDLC |
| `05_core_drivers.md` | Core drivers | Technological, economic, and organizational forces pushing AIDLC forward |
| `06_historical_influencers_kol.md` | Historical voices &amp; KOLs | ThoughtWorks, Martin Fowler, Dave Farley, Simon Willison, Kent Beck, Agile Manifesto community |
| `07_synthesis.md` | Synthesis report | Adversarially-verified findings, open questions, methodology |
| `claim_verification*.md` | Claim verifications | Detailed adversarial verification of specific claims |

### Figures & Diagrams

| File | Content |
|------|---------|
| `figures/README.md` | 图片索引 |
| `../_raw_aws/figures/aws_aidlc_architecture.png` | AWS AI-DLC 14-node AgentCore 平台架构全景 |
| `../_raw_aws/figures/aws_blog_3phase_flow.png` | AWS 三阶段生命周期流程 |
| `../_raw_aws/figures/aws_blog_adaptive_model.png` | AWS 自适应执行模型 |
| `../_raw_aws/figures/aws_blog_artifacts_flow.png` | AWS 产物流与阶段门控 |
| `../_raw_aws/figures/ttpsc_full_aidlc_diagram.webp` | TT PSC 深度拆解 AI-DLC 三阶段 |
| `../_raw_aws/figures/ttpsc_full_artifacts.webp` | TT PSC 阶段产物流详解 |
| `../_raw_aws/figures/ttpsc_full_operations.webp` | TT PSC Operations 阶段示例 |
| `figures/gartner_hype_cycle_ai_2025.jpg` | Gartner 2025 AI Hype Cycle |

---

## Key Sources

- AWS AI-DLC methodology (https://aws.amazon.com)
- Forrester Agentic Software Development reports (2025-2026)
- Gartner Innovation Insight for AI-Native Software Engineering (2025)
- IEEE P3398 Draft Recommended Practice for GPT-Empowered SE Life Cycle (March 2026)
- arXiv:2604.26275 — Agentic AI in the Software Development Lifecycle (Bhati, 2026)
- arXiv:2606.15283 — AI-driven Software Development: A Pragmatic Path (2026)
- Anthropic Engineering Blog — Scaling Agentic Coding, AI-Native Engineering Org (2025-2026)
- Atlassian Team '25/'26 — AI-Native SDLC announcements
- Stack Overflow / PwC Agentic AI Playbook (2026)
- Cloze.world — 7大权威机构如何定义下一代 SDLC (Chinese comprehensive analysis)
- ELEKS AI-SDLC Maturity Model research
- EPAM AI-Native SDLC analysis
- New Relic 2026 State of AI Coding Report
- METR 2025 Randomized Controlled Trial
- iSAQB — AI Agents Don't Modernize Legacy Code on Their Own (May 2026)
- Docker — Coding Agent Horror Stories (2026)
- Various academic papers from IEEE, ICLR 2026, ICML 2026, NeurIPS workshops
