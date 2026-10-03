# Dimension 2: Evolution and Timeline of AIDLC

## Overview

The shift from traditional human-driven software development to AI-native, agentic software engineering represents one of the fastest paradigm transitions in the history of the discipline. The concept evolved from in-editor autocomplete (2021) to full-lifecycle agent orchestration (2026) in approximately five years — compressed relative to prior shifts like Agile (decade+) or DevOps (half-decade).

---

## Pre-History: Before AIDLC

### 2018-2020: Foundation Models Emerge
- **GPT-1 (2018)**, **GPT-2 (2019)**, **GPT-3 (2020)**: Language models demonstrate surprising code generation ability but are not productized for development
- **CodeSearchNet (2019)**: GitHub/DeepMind dataset for code search; early exploration of ML + code
- **TabNine (2018)**: First commercial ML-based code completion tool; uses GPT-2

---

## Phase 1: AI-Assisted Coding (2021-2023)

### June 2021 — The Copilot Moment
- **GitHub Copilot** launches as a technical preview — first mainstream AI coding tool integrated into the editor
- Operates at line/function granularity — "autocomplete with judgment"
- **OpenAI releases Codex paper**: Introduces HumanEval benchmark for single-function synthesis
- **Initial sentiment**: Excitement mixed with skepticism; "will this replace junior devs?"

### 2022 — Proliferation of Assistants
- **Amazon CodeWhisperer** launched (free for individual use)
- **Tabnine**, **Codeium**, **Sourcegraph Cody** enter market
- All operate as in-editor assistants — suggest code, don't execute or plan
- **HumanEval saturation**: Frontier models exceed 90% pass@1; benchmark saturates, exposing need for repository-level evaluation

### March 2023 — GPT-4 Released
- Dramatic improvement in reasoning and code generation
- ChatGPT becomes fastest-growing consumer application in history
- First serious discussions about "AI replacing programmers" enter mainstream discourse

### October 2023 — SWE-bench Introduced
- **Princeton researchers (Jimenez et al.)** release SWE-bench
- 2,294 real GitHub issues across 12 mature Python repositories
- Requires navigating real codebase, locating files, writing patches, passing hidden tests
- **Baseline result: 1.96%** — exposing the vast gap between single-function synthesis and real-world engineering

---

## Phase 2: Agentic Beginnings (2024)

### March 2024 — Devin: First "AI Software Engineer"
- **Cognition launches Devin** — first commercial product framing AI as a full "software engineer"
- Runs in sandboxed cloud VM with browser, terminal, and editor
- Dispatched via Slack/Jira integration
- **Reaction**: Massive hype (viral demos) followed by backlash (real-world limitations exposed)
- **Key Insight**: The agent-computer interface (ACI) matters as much as the model

### Mid-2024 — Multi-Agent Software Development
- **MetaGPT**, **ChatDev**: Encode software development as multi-agent processes
- Roles: Product Manager, Architect, Engineer, QA — each played by different LLM instances
- Academic papers demonstrate the "society of agents" approach to software development

### Late 2024 — The Scaffolding Breakthrough
- **SWE-agent (Princeton, NeurIPS 2024)**: Resolution rate jumps from ~2% to **12.5%** using same model but structured ACI commands
- **Key finding**: Agent-computer interface design is a first-class research problem
- **Terminal-Bench**: New benchmark measuring agent performance on real terminal tasks
- **OpenHands (formerly OpenDevin)**: Leading open-source generalist agent platform with Docker-sandboxed execution

---

## Phase 3: AIDLC Frameworks Emerge (2025)

### Early 2025
- **Claude Code released** (Anthropic research preview) alongside Claude 3.7 Sonnet
- Operates at project granularity: reads full codebase, plans across files, executes shell commands, runs tests, iterates
- **SWE-bench Verified hits 49%** with Claude 3.5 Sonnet + scaffolding
- Anthropic reports majority of internal code now produced by Claude Code
- **Feb 2025**: Andrej Karpathy coins "**vibe coding**" — surrender-based AI workflow where you "forget the code exists"

### April 2025 — Atlassian Team '25
- First public articulation of "**AI-Native SDLC**"
- Five Structural Shifts framework presented
- Teamwork Graph concept introduced as "neural backbone" for AI context

### May 2025 — AlphaEvolve (DeepMind)
- **Google DeepMind unveils AlphaEvolve**: Evolutionary loop where Gemini models propose program variants, evaluator scores them
- Discovers new 4x4 matrix multiplication algorithm (48 scalar multiplications, beating Strassen's 1969 result)
- Recovers 0.7% of compute across Google data centers
- Produces 23% speedup of FlashAttention kernel
- **Published in Nature**

### Mid-2025
- **AWS AI-DLC Methodology formalized** (with CI&T): Three phases, Bolt cadence, open-sourced workflows
- **Gartner publishes** Innovation Insight for AI-Native Software Engineering
- **Forrester coins** "Agentic Software Development" as distinct category
- **SWE-bench Verified: 62.3%** (Claude 3.7 Sonnet + Claude Code)
- **EPAM publishes** AI-Run SDLC / ADLC framework
- **Microsoft Build 2025**: Agentic DevOps + Spec-Driven Development debut

### October 2025
- **Anthropic publishes three key blog posts:**
  - "Introduction to Agentic Coding" (Oct 30)
  - "How to Scale Agentic Coding Across Your Engineering Organization" (Oct 15)
  - Case studies: Rakuten (79% faster, 5x parallel tasks), TELUS (500K+ hours saved)

### Late 2025
- **SWE-bench Verified: 72.7%** (Claude Sonnet 4)
- **METR randomized controlled trial**: Experienced devs 19% slower with AI tools (despite believing they're 20% faster)
- **Goldman Sachs Q4 2025**: "No meaningful relationship between productivity and AI adoption at economy-wide level"
- **IEEE Conference papers**: Hallucination and overconfidence in agentic coders; documentation-driven frameworks
- **Cloze.world** publishes comprehensive Chinese-language analysis comparing all major frameworks

---

## Phase 4: Production Standardization & Backlash (2026)

### Early 2026
- **SWE-bench Verified hits ~78%** (Claude Opus 4.7) — up from 1.96% in ~2.5 years
- **IEEE P3398 Draft** (March 2026): Recommended Practice for GPT-Empowered Software Engineering Life Cycle
- **Gartner predictions intensify**: 65% of teams treat IDEs as optional by 2027; 75% enterprise AI code assistant adoption by 2028

![Gartner AI Hype Cycle 2025](figures/gartner_hype_cycle_ai_2025.jpg)

*Gartner 2025 AI Hype Cycle — "Agentic AI" 处于期望膨胀峰值 (Peak of Inflated Expectations)。来源：Gartner, [转载](https://testrigor.com/blog/gartner-hype-cycle-for-ai-2025)*
- **Forrester "State of Agentic Software Development 2026"**: Agents operate across all SDLC phases
- **PwC prediction**: >50% of teams run fully agentic SDLC by 2027

### Open Source Backlash (Jan-June 2026)
- **Zig** (April 2026): Hard ban on all AI-generated contributions — including rewrites, edits, brainstorming, debugging, and translations
- **OpenJDK** (April 2026): Interim policy — no LLM/diffusion-model-generated content in contributions
- **NetBSD, QEMU, Gentoo, OBS Studio, Ghostty, RPCS3, SDL**: Various bans/restrictions
- **cURL**: Closed 6-year bug bounty after AI-generated fake reports flooded the program (1/20-1/30 real by end 2025)
- **Bun vs. Zig conflict**: Bun (acquired by Anthropic) achieved 4x compilation performance with Claude Code but can't upstream to Zig

### Mid-2026: The Influencer Shift
- **March 2026**: Andrej Karpathy disavows "vibe coding" for serious work at AI Ascent conference
- **New term**: "**Agentic Engineering**" — emphasizing oversight, rigor, and craft
- **AI Native DevCon London** (June 2, 2026): 41 talks, 3 tracks; "Skills are the New Code"; CDLC framework debut

### June 2026 — Current State
- **Anthropic publishes** "Running an AI-Native Engineering Org" and "The Evolution of Agentic Surfaces"
- **New Relic 2026 Report**: 67% of leaders say AI generates 51-75% of code; 82% experienced AI-code production failures; "agent debt" coined
- **ai-sdlc-framework v0.11.0** released — declarative governance with EU AI Act/NIST/ISO 42001 mapping
- **FeatureBench (ICLR 2026)**: Claude 4.5 Opus gets only 11.0% on end-to-end feature development (vs. 74.4% on SWE-bench)
- **"Agentic AI in the SDLC"** (Bhati, arXiv April 2026): Six-layer reference architecture formalized
- **Business Insider**: "Software engineers are facing an identity crisis bordering on depression"
- **TechCrunch**: "Coders are refusing to work without AI — and that could come back to bite them"

---

## SWE-bench Verified Performance Trajectory

| Date | System | Resolution Rate |
|---|---|---|
| Oct 2023 | RAG Baseline | **1.96%** |
| Late 2024 | SWE-agent (NeurIPS) | **12.5%** |
| Early 2025 | Anthropic scaffold + Sonnet 3.5 | **33.2%** |
| Mid 2025 | Claude 3.5 Sonnet (new) | **49.0%** |
| Late 2025 | Claude 3.7 Sonnet + Claude Code | **62.3%** |
| Early 2026 | Claude Sonnet 4 | **72.7%** |
| April 2026 | Claude Opus 4.7 | **78.4%** |

**Key Insight**: Gains came primarily from scaffolding and agent-computer interface design, not raw model size. Frontier non-agentic systems plateau near ~20%.

---

## Key Academic Papers Timeline

| Date | Paper / Benchmark | Venue | Significance |
|---|---|---|---|
| Oct 2023 | SWE-bench | arXiv | Exposed gap between single-function and real-world engineering (1.96% baseline) |
| 2024 | SWE-agent | NeurIPS 2024 | ACI design as first-class problem (12.5%) |
| 2024 | MetaGPT, ChatDev | ACL/NeurIPS workshops | Multi-agent software development paradigms |
| Jan 2025 | Terminal-Bench | arXiv | Agent performance on real terminal tasks |
| Nov 2025 | CentaurEval | ICML 2026 | Human-AI collaboration needed for complex problems |
| Nov 2025 | "Confident but Incorrect" | IEEE | Hallucination and overconfidence in agentic coders |
| Nov 2025 | Documentation-Driven Framework | IEEE | Four-stage lifecycle for AI-assisted SE |
| Jan 2026 | OctoBench | arXiv | Scaffold-aware instruction following (34 envs, 217 tasks) |
| Feb 2026 | "Why Agentic-PRs Get Rejected" | arXiv | Seven rejection modes unique to AI; 67.9% lack feedback |
| March 2026 | IEEE P3398 Draft | IEEE | GPT-empowered SE lifecycle standard |
| April 2026 | Agentic AI in the SDLC (Bhati) | arXiv | Six-layer reference architecture (L0-L5) |
| May 2026 | FeatureBench | ICLR 2026 | Claude Opus 11% on end-to-end features (vs. 74% on SWE-bench) |
| June 2026 | RigorBench | arXiv | Process discipline (planning, verification, recovery) |
| June 2026 | AI-Driven SD: Pragmatic Path | arXiv (Munich) | Three-stage organizational maturity model |

---

## Key Observations

1. **Compression of adoption cycles**: The AI-assisted → agentic → AI-native transition is happening in 3-5 years, vs. 10+ years for Agile and 5+ years for DevOps
2. **Benchmark inflation trap**: SWE-bench is saturating just as HumanEval did; FeatureBench and RigorBench expose the remaining gap
3. **2026 as the inflection year**: Transition from experimentation to standardization; from capability celebration to production reckoning
4. **The backlash is part of the timeline**: Open source bans, production incidents, and skill atrophy concerns are not separate from AIDLC evolution — they are driving the next phase (governance, safety, maturity models)
5. **Chinese ecosystem tracking closely**: Chinese tech media and consultancies publishing comprehensive analyses within months of Western framework releases
