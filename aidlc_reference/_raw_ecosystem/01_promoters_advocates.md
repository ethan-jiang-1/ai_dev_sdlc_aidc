# Dimension 1: Main Promoters and Advocates of AIDLC

## Overview

The concept of AIDLC (AI Development Life Cycle) is being actively promoted by a coalition of major cloud platforms, enterprise software vendors, analyst firms, AI labs, and open-source projects. These organizations are not merely observing the trend — they are actively constructing frameworks, publishing maturity models, and building products that instantiate AIDLC concepts.

---

## 1. Major Cloud Platforms

### AWS / Amazon
- **Framework:** AI-DLC (AI-Driven Development Life Cycle), co-developed with CI&T
- **Key Contribution:** Most formalized methodology; three-phase model (Inception → Construction → Operations); "Bolt" cadence replacing sprints; Mob Elaboration/Mob Construction rituals; open-sourced workflows on GitHub (awslabs/aidlc-workflows)
- **Product:** Amazon Q Developer; Kiro internal AI assistant
- **Chinese-language promotion:** AWS China blog published "Apache SeaTunnel AIDLC Methodology Practice" case study
- **Claimed Results:** 10-15x productivity gains, 40-60% defect reduction, 300-500% ROI within 12 months
- **Notable:** Amazon also experienced a 13-hour AWS outage and 6.3M lost orders attributed to AI-written code, triggering a 90-day "code safety reset" — revealing the gap between promotion and production reality

**AI-DLC 核心架构：**

![AWS AI-DLC 14-Node AgentCore Platform Architecture](../_raw_aws/figures/aws_aidlc_architecture.png)

*上图：AWS AI-DLC 参考实现平台架构——基于 Bedrock AgentCore + Strands GraphBuilder 的 14-Node 多 Agent 编排器，覆盖 Inception → Construction 全阶段。来源：[aws-samples/sample-ai-driven-development-lifecycle-platform](https://github.com/aws-samples/sample-ai-driven-development-lifecycle-platform)*

**三阶段生命周期流程：**

![三阶段流程](../_raw_aws/figures/aws_blog_3phase_flow.png)  ![自适应模型](../_raw_aws/figures/aws_blog_adaptive_model.png)  ![产物流](../_raw_aws/figures/aws_blog_artifacts_flow.png)

*左：Inception→Construction→Operations 三阶段流程 · 中：自适应执行模型（条件 Stage 根据复杂度动态执行）· 右：产物流与状态管理三元组。来源：[AWS DevOps Blog](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)*

**第三方深度分析 (TT PSC)：**

| | | |
|---|---|---|
| ![TT PSC 拆解](../_raw_aws/figures/ttpsc_full_aidlc_diagram.webp) | ![TT PSC 产物流](../_raw_aws/figures/ttpsc_full_artifacts.webp) | ![TT PSC Operations](../_raw_aws/figures/ttpsc_full_operations.webp) |
| 三阶段深度拆解 | 质量门控与产物流 | Operations 阶段示例 |

*来源：[TT PSC](https://ttpsc.com/en/blog/how-aws-ai-dlc-defines-an-ai-native-methodology/)*

### Google Cloud
- **Framework:** ADLC (Agentic Development Lifecycle)
- **Key Contribution:** Focus on lifecycle management for AI Agents themselves; unveiled at Google Cloud Next 2026
- **Products:** Gemini, Gemini Code Assist, Android Studio AI integration
- **Strategic moves:** Acquired Windsurf for $2.4B; Logan Kilpatrick as head of AI Studio driving developer community engagement

### Microsoft / GitHub
- **Framework:** Agentic DevOps + Spec-Driven Development
- **Key Contribution:** "Write Specs, not Code" paradigm; Copilot Agent Mode; Project Padawan (autonomous contributor)
- **Products:** GitHub Copilot, Azure DevOps, VS Code
- **Leadership messaging:** GitHub CPO Mario Rodriguez: "We're the fuel. You're the rocket ship"; "AI-native is the new frontier"
- **Research:** GitHub Next — agentic maintenance at repository scale

---

## 2. Major Analyst & Advisory Firms

### Gartner
- **Framework:** AI-Native Software Engineering
- **Key Predictions:**
  - 90% of enterprise software engineers will use AI code assistants by 2028 (up from <10% in early 2023)
  - By 2027, 65% of engineering teams using agentic coding will treat IDEs as optional
  - 30% reduction in application modernization costs through GenAI by 2027
- **Positioning:** AI as "Structured Collaborator"; developer role evolves to "AI Orchestrator"
- **Hype Cycle:** Placed "Agentic AI" at the peak of the 2025 Generative AI Hype Cycle

### Forrester
- **Framework:** Agentic Software Development (Five-Level Maturity Model)
- **Key Contribution:** Most detailed maturity assessment tool; co-developed with 3Pillar Global
- **Five Levels:** Classic SDLC → AI-Assisted → AI-Optimized → Agent-Augmented → Agent-Native
- **2026 State of Agentic Software Development report:** Agents now operate across all SDLC phases
- **Principal Analyst:** Devin Dickerson — "AI maturity isn't linear — it's fragmented"

### 3Pillar Global
- **Co-creators:** Scott Young and Lance Mohring (Field CTOs)
- **Contribution:** AI-Enabled SDLC Maturity Model with Forrester; "faster horse moment" metaphor
- **Webinar (Nov 2025):** "AI & the SDLC: Beyond the Hype to a Practical Roadmap"

---

## 3. Enterprise Software & Platform Companies

### Atlassian
- **Framework:** AI-Native SDLC + Software Collection
- **Key Innovation:** Teamwork Graph — 15+ billion connections forming a "neural backbone" for AI context
- **Five Structural Shifts:**
  1. Developer becomes "intent definer + AI output reviewer"
  2. Code review becomes "trust but verify"
  3. Roles blur: PMs code more, engineers take on content/design
  4. Planning moves to "just-in-time" (JIT)
  5. AI handles style/linting/bugs; humans handle expertise/legal/security
- **Products:** Rovo Dev, Bitbucket Pipelines, Developer Intelligence (DX)
- **CEO:** Mike Cannon-Brookes — "Smarts can be bought by token, but your moat is Institutional Memory"

### IBM
- **Framework:** DevOps Loop 2.0
- **Key Contribution:** Enterprise-grade agent orchestration using MCP protocol
- **Focus:** Making agentic workflows operational at enterprise scale

### EPAM
- **Framework:** AI-Run SDLC / Agentic Development Lifecycle (ADLC)
- **Key Contribution:** Distinction between AI-Assisted, AI-Integrated, and AI-Driven maturity stages
- **Published analysis:** "From Traditional Software to a Native AI SDLC: How GenAI is Redefining Engineering"

### Stack Overflow / PwC
- **Joint publication:** "How Agentic AI is Rewriting the Software Development Playbook"
- **Prediction:** Over 50% of engineering teams will run a fully agentic SDLC by 2027
- **Five adoption phases:** Exploration → Experimentation → Integration → Optimization → Transformation

---

## 4. AI Labs (Model Providers)

### Anthropic
- **Products:** Claude (Sonnet, Opus), Claude Code, MCP integration
- **Key Publications:**
  - "How to Scale Agentic Coding Across Your Engineering Organization" (Oct 2025)
  - "Introduction to Agentic Coding" (Oct 2025)
  - "Eight Trends Defining How Software Gets Built in 2026" (early 2026)
  - "Running an AI-Native Engineering Org" (June 2026)
  - "The Evolution of Agentic Surfaces: Building with Claude Managed Agents" (June 2026)
- **Innovations:** "Dreaming" — batch async agent self-improvement via transcript analysis; claimed internal majority of code now produced by Claude Code
- **Adoption:** Claude Code grew from 4% to 63% developer adoption in 9 months
- **CEO:** Dario Amodei — publicly estimated AI coding productivity gains at ~15-20%

### OpenAI
- **Products:** GPT-5.4-Codex, Codex CLI, ChatGPT
- **Key Contribution:** Defining "Harness Engineering" as a discipline — deterministic wrappers around probabilistic models
- **Staff:** Ryan Lopopolo on harness engineering patterns
- **Controversy:** Sam Altman's "Thank you... but we'll take it from here" message sparked developer backlash

### Google DeepMind
- **Innovation:** AlphaEvolve — evolutionary loop for code optimization; discovered new matrix multiplication algorithm; 23% FlashAttention kernel speedup
- **Leadership:** Demis Hassabis (CEO, Nobel laureate)

---

## 5. Emerging Specialized Players

### Tessl
- **Founder/CEO:** Guy Podjarny
- **Framework:** Context Development Lifecycle (CDLC) — humans live in CDLC, leave SDLC to agents
- **Mantra:** "Skills are the New Code" — named, versioned, testable, installable context bundles
- **Debut:** AI Native DevCon London (June 2026)

### Opsera
- **Co-Founder/CEO:** Kumar Chivukula
- **Focus:** Agentic DevOps platform; pipeline self-remediation; AI supply chain security
- **Event:** "The Agentic Future" (Jan 2026)

### Cycode
- **Framework:** ADLC (Agentic Development Life Cycle) — security-focused
- **Position:** Autonomous agents generate/test/deploy with minimal human input; security must be embedded

### Cognition / Devin
- **Product:** First commercial "AI Software Engineer" (March 2024)
- **Acquisitions:** Acquired Windsurf for $250M; later Google acquired Windsurf for $2.4B

### Replit
- **CEO:** Amjad Masad (459K X followers)
- **Position:** Making AI coding accessible to non-traditional developers
- **Incident:** Agent wiped live database during code freeze; CEO announced new safeguards

---

## 6. Chinese Ecosystem Promoters

### 填空题咨询 (Cloze Consulting)
- **Role:** Leading Chinese-language analyst of AIDLC frameworks
- **Key Publication:** "AI 时代软件研发范式全景：7大权威机构如何定义下一代 SDLC" (Comprehensive analysis of all 7 major frameworks)
- **Partnership:** Atlassian partner; Chinese-language coverage of AI-native development

### 36Kr (36氪)
- **Coverage:** Extensive reporting on Zig's anti-AI stance; developer skill atrophy from AI dependence; Amazon AWS outages
- **Audience:** Chinese tech community; influential in shaping Chinese developer discourse

### InfoQ China
- **Coverage:** "Agentic Coding: God or Trap?" (ClickHouse engineering team case study); practical evaluations
- **Audience:** Enterprise developers and architects in China

### Apache SeaTunnel
- **Case Study:** Full AIDLC implementation on AWS; 3-4x acceleration; 70% AI-generated code; published on AWS China blog

---

## 7. Open-Source Implementations

### ai-sdlc-framework (GitHub)
- **Type:** Declarative governance framework for AI-augmented SDLC
- **Latest Release:** v0.11.0 (June 2026)
- **Features:** Decision Engine, Autonomous Pipeline Orchestrator, Cross-Harness Review, Operator TUI

### aaidlc (npm)
- **Type:** CLI tool with specialized agents (PM, Architect, Dev, QA, Security) for each SDLC phase
- **Features:** Enforced quality gates; decision checkpoints

### Project Iris (npm)
- **Type:** AI-DLC implementation as markdown-based agents
- **Features:** Bolt-based cadence; DDD, TDD, BDD built into methodology

### aws-samples/sample-aidlc-decisions-driven-skill (GitHub)
- **Type:** Reference implementation of AWS AI-DLC
- **Features:** Decision gates, manifest-based state tracking, parallel sub-agent implementation

---

## 8. Enterprise Adopters (Case Study Sources)

| Organization | What They're Doing |
|---|---|
| **CJ Olive Young (Korea)** | AI-native development on AWS AIDLC; CTO Kim Hwan presenting at AWS Summit Seoul |
| **Spotify** | Anthropic customer case study; using Claude for engineering workflows |
| **Rakuten** | 7-hour autonomous refactoring with 99.9% accuracy; 79% faster feature delivery |
| **TELUS** | 30% faster shipping; 500,000+ hours saved |
| **Notion, Asana, Atlassian, Sentry** | Claude Managed Agents deployment |
| **Verily (Alphabet)** | VIDA — custom VS Code plugin invoking Copilot across entire codebase |
| **Swamp Club** | "Dark Factory" — zero handwritten production code since January 2026 |
| **Odevo** | Zero-handwritten-code transformation |

---

## Key Observations

1. **"Naming competition" underway**: Multiple organizations are racing to establish their terminology as the industry standard — AI-DLC (AWS), ADLC (Google, Cycode), AI-Native SDLC (Atlassian, Gartner), Agentic SDLC (Forrester, Outshift)
2. **Convergence on core ideas**: Despite different names, all frameworks agree on: (1) SDLC phases persist but human/AI roles invert; (2) "Write Spec" replaces "Write Code"; (3) maturity models are essential navigation tools
3. **Promoter incentives matter**: Cloud platforms and AI labs have direct revenue interests in AIDLC adoption; analyst firms have influence incentives; open-source projects have community governance concerns
4. **Chinese ecosystem engaged**: Major Chinese tech media and consultancies actively tracking and translating AIDLC frameworks; enterprise case studies emerging
5. **Gap between promotion and reality**: Many promoters' claimed results (10-15x productivity) conflict with independent studies (METR: 19% slower) and documented failures (Amazon outages, open source bans)
