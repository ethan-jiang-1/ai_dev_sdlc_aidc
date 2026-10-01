---
title: "Agentic Business Process Management: A Research Manifesto"
authors: "Diego Calvanese, Angelo Casciani, Giuseppe De Giacomo, Marlon Dumas, Fabiana Fournier, Timotheus Kampik, Emanuele La Malfa, Lior Limonad, Andrea Marrella, Andreas Metzger, Marco Montali, Daniel Amyot, Peter Fettke, Artem Polyvyanyy, Stefanie Rinderle-Ma, Sebastian Sardiña, Niek Tax, Barbara Weber"
venue: "Information Systems, Vol. 140, Article 102738, Aug-Sep 2026"
arxiv: 2603.18916
origin: "Dagstuhl Seminar #25192 (AUTOBIZ) + PMAI'25 Workshop"
pages_content: "1-25 (of 34)"
pdf: apm_manifesto_content.pdf
---

# Agentic Business Process Management: A Research Manifesto

**18 authors from 15 institutions**: Free University of Bozen-Bolzano, University of Oxford, University of Tartu, IBM Research (Haifa), Umeå University, SAP (Berlin), Sapienza Università di Roma, University of Duisburg Essen, University of Ottawa, DFKI/Saarland University, University of Melbourne, TU Munich, RMIT University, Meta (London), University of St. Gallen

---

## Abstract

This paper presents a manifesto that articulates the conceptual foundations of **Agentic Business Process Management (APM)**, an extension of Business Process Management (BPM) for governing autonomous agents executing processes in organizations.

From a management perspective, APM represents a **paradigm shift** from the traditional view on business processes. This shift is driven by the realization of process awareness by agent-oriented abstractions: software and human agents act as primary functional entities that perceive, reason, and act within explicit **process frames**. APM moves away from automation-oriented BPM toward systems in which **autonomy is constrained, aligned, and made operational through process-aware agents**.

The paper introduces the core abstractions and architectural elements required to realize APM systems and elaborates on **four key capabilities** that agents in APM systems must support:

1. **Framed Autonomy** — guard-rails agent behavior so decisions stay within organizational boundaries
2. **Explainability** — agents articulate the rationale for their behavior (a prerequisite for deployment)
3. **Conversational Actionability** — natural language interaction, negotiation, exception handling
4. **Self-Modification** — short-term adaptation + long-term evolution toward self-improving systems

These capabilities are **purposefully ordered**: Framing ensures process-awareness and guard-rails. Explainability preserves autonomy by having agents articulate behavioral rationale. Conversational actionability ensures effective execution, interaction, and governance. Self-modification allows continuous improvement.

The manifesto serves as a **roadmap** for bridging the BPM, AI, and Multi-Agent Systems communities and for guiding the development of APM systems in practice.

**Keywords**: business process management, autonomous agents, agentic AI, framed autonomy, explainability, conversational actionability, self-modification

---

## 1. Introduction and Motivation

With the advent of LLMs, organizations increasingly adopt AI to instill **autonomy** into software systems—systems that independently perceive, reason, and act to achieve their goals, emphasizing intentionality, goal-directed behavior, and constrained autonomy.

However, increasing the autonomy of LLM-based software agents also brings risks:

- **Business level**: agents may make decisions violating compliance rules, disregarding social norms, or leading to adverse business outcomes
- **Technical level**: reliance on LLMs entails inherent functional uncertainty—difficult to test and debug, leading to technical debt when replacing agents requires making sense of entangled behaviors from agent interactions

To mitigate these risks, it is crucial to **govern software agents in organizations**. Agent governance has been a well-established research line for decades (normative MAS). LLM providers have issued governance recommendations. But these lack a bridge to the practically well-established perspective of **managing work in organizations**—which is exactly what BPM provides.

**BPM and MAS** have a strong joint tradition dating back to the 1990s. However, most work focuses on allocating agents to execute tasks within a business process, rather than on managing autonomous agents **as first-class citizens** to ensure achievement of business goals. Some exceptions exist—process choreographies, agent system mining, agentic AI process observability—but there is a lack of a **holistic perspective** on applying BPM to governing software agents in organizations.

### A Concrete Example: Supplier Onboarding

Consider an APM system facilitating supplier onboarding as part of procurement. There is a **buyer agent** and several **supplier agents**, some human and some AI-based. Both types possess **process awareness**: they continuously align their individual goals and act in concert to meet organizational procurement objectives.

The buyer agent periodically disseminates RFQs to suitable suppliers and evaluates quotes to decide which supplier to contract with. Supplier agents fulfill winning bids within contractual time frames. Individual agents may also pursue non-process-aware goals (e.g., a supplier restricted to a particular geographical region). The system may include agents that are not process-aware, such as a legal agent ensuring contract diligence.

### How This Manifesto Was Created

Output of **Dagstuhl Seminar #25192 (AUTOBIZ)** and follow-up sessions at the **PMAI'25 workshop** (ECAI). Experts gave talks → participants split into working groups → results presented to all seminar participants → feedback incorporated → further discussed at PMAI'25.

---

## 2. Agentic Business Process Management Systems

### 2.1 Fundamental Concepts

An **agentic system** is a collection of one or more individual goal-driven agents that sense, reason, and act upon external stimuli. The term **agentic** indicates the system is **agent-centric**: agents constitute the primary functional entities responsible for executing business processes. This marks a paradigm shift from AI-augmented BPM systems where non-agent entities may exhibit some degree of agentic characteristic.

#### Four Categories of Agents

| Category | Description |
|----------|-------------|
| **Human agents** | Process workers, process managers |
| **Software agents** | Tasks executed by program code, without deliberation |
| **Embodied agents (robots)** | Decision-making directly affects the physical world |
| **AI agents** | Accomplish tasks via deliberation using AI (e.g., LLMs) |

#### Process Awareness

While an agentic system hosts inter-operating agents (a socio-technical system), it does not by itself realize **process awareness**. We define process awareness as: *the assurance that agents' inner workings conform to organizational processes and adhere to their operational constraints, regulations, and goals.*

#### Definition 2.1 (APM System)

> An **Agentic Business Process Management (APM) system** is a socio-technical system jointly realized by a collection of agents, some of which are at least partially process-aware.

The system is socio-technical: it allows a combination of social (human) and technical (technological) agents that interact and depend on each other. This **does not exclude fully autonomous systems** with little to no human intervention. Collectively, agents execute business processes by virtue of each agent possessing a certain degree of process awareness. Every agent is treated as autonomous, with its own goals, decision-making capabilities, and knowledge of (parts of) the business processes.

#### Autonomy ≠ Automation

| Automation | Autonomy in APM |
|------------|-----------------|
| Execution of predefined tasks exactly as specified | Agents perceive, reason, and **choose** how to act within a process frame |
| Follows fixed rules | Context-sensitive decisions while respecting process awareness |

#### Definition 2.2 (APM Agent)

> An **agent in an APM system** is a primary execution entity—an actor that perceives, reasons, and acts autonomously, with its autonomy **framed** to ensure process-aware behavior aimed at achieving process goals.

Once an agent becomes part of an APM system, its individual behavior and goals are both **framed** (complying with process constraints AND directed toward process goals) and **aligned** (harmonized with other agents). Process-awareness is qualitative: different agents may vary in their degree of process awareness and autonomy.

To realize this notion, agents must possess **four essential capabilities**: framing, explainability, conversational actionability, and self-modification (detailed in Section 3).

#### Definition 2.3 (Tool)

> A **tool** in an APM system is a means accessible to an agent that augments its capacity to reason, and to perceive and act upon its environment.

Tools may include sensors, actuators, messaging, or other software functions and services, accessed through communication protocols.

### 2.2 Conceptual Architecture

The architecture focuses on **two distinct levels**:

```
┌──────────────────────────────────────────────────────────────────┐
│                       MACRO LEVEL                                │
│                  APM System (Process-Aware Management)            │
│                                                                  │
│  Processes defined by collective, organization-level goals       │
│  Framing mechanism imposes:                                      │
│    • Process Awareness — agents' work toward common objectives   │
│    • Goal Alignment — rules of engagement, hierarchies, roles    │
├──────────────────────────────────────────────────────────────────┤
│                       MICRO LEVEL                                │
│                 APM Agents (Autonomous Execution)                 │
│                                                                  │
│  Each agent = Perception → Reasoning → Action loop               │
│                                                                  │
│  Reasoning module sub-capabilities:                              │
│    ┌─ Framing (internalized process frame: mental + intentional) │
│    ├─ Explainability (trace logs, auditability)                  │
│    ├─ Conversational Actionability (negotiate, coordinate)       │
│    └─ Self-Modification (adapt and evolve)                       │
│                                                                  │
│  Agents interact with: other agents, tools (messaging, sensors,  │
│  services, actuators), AI models (LLMs), external environment    │
└──────────────────────────────────────────────────────────────────┘
```

Agents rely on a **shared language, ontology, or protocol** to understand each other. Examples include MCP (Model Context Protocol), ACP (Agent Communication Protocol), RDF, and KQML.

#### Definition 2.4 (Framing)

> **Framing** is a primary mechanism for ensuring process-awareness and goal alignment in an APM system, imposing restrictions on the autonomy of agents through their knowledge and goals.

Without framed autonomy, an agent could perform any action in pursuit of its own individual goals. Framing provides the **normative and operational specifications** that agents must adhere to, including lifecycle management to create, suspend, or destroy agents as the process evolves.

**Two aspects of Framing**:

1. **Process-Awareness**: governs all agents' work toward common process objectives. An agent's autonomy is directed to ensure its actions aim to fulfill collective process goals.

2. **Goal-Alignment**: sets the rules of engagement and structural relationships (hierarchies/coalitions), including role assignment and segregation of duties throughout the agent lifecycle.

The concrete realization of framing is an **engineering choice**—it could be implemented by assigning collective responsibility to one or more agents, through orchestration, or via a shared memory allowing agents to progress along a mutual plan.

#### 2.2.2 APM Agent — Three Conceptual Modules

Drawing on foundational ontologies (DOLCE, GFO), agent-oriented modeling frameworks (i*, Tropos), classic AI constructs (BDI, FIPA), and mental model theory of reasoning:

**1. Perception Module**: observes environment state, context (situational constraints, location), and other agents (some process-aware, some external). Manages sensing attributes—sensors, percepts, belief update functions—ensuring the agent continuously updates its understanding of the world.

**2. Reasoning Module**: core component for knowledge representation and decision-making. Continuously informed by the framing mechanism to maintain:
- **Mental model**: the agent's "memory" regarding process model, running instances, stakeholders, and all relevant process context
- **Intentional model**: the agent's goals shaped by social and normative dispositions (obligations, roles, collective goals, prohibitions)

The agent's core knowledge includes its identity (agent ID, type) and behavioral dispositions (policies, triggers, reactions). Recent advances explore LLMs for this role, though their true capability remains under debate. Alternative approaches include externalizing reasoning through specialized tools.

**3. Action Module**: performs actions changing the environment and sends messages to other agents. Defines agent capabilities (skills, resources) and abilities to socially interact.

---

## 3. Envisioned Capabilities of an APM System

> The four capabilities are **purposefully ordered**: Framing → Explainability → Conversational Actionability → Self-Modification. Each is a prerequisite for the next.

### 3.1 Framed Autonomy

A **frame** is a set of rules, restrictions, and regulations, which may evolve over time. Frames establish boundaries within which agents may operate with **maximal flexibility**, making autonomous decisions. Frames may exist on at least three levels: **agent type, process, and organization** (as well as across organizations).

#### Normative Frame vs. Operational Frame

This is one of the paper's most important conceptual contributions:

| | Normative Frame | Operational Frame |
|---|---|---|
| **Specifies** | Deontic requirements—obligations, prohibitions, permissions | Concrete execution steps |
| **Example** | "Must reject any student assignment submitted after deadline" | "(1) Retrieve student name and ID (2) Record in database (3) Send rejection email" |
| **Room for autonomy** | **Wider** — agent decides HOW to comply | **Narrower** — agent just follows steps |
| **Governance** | Boundary-setting + agent discretion | Instruction-following |

The normative frame could replace operational steps with a single prohibition: "Do not delete the rejected assignment without informing the student." This leaves the agent to decide whether to email first or record first—**more autonomy within the same boundary**.

**Key insight**: *If there are no autonomous decision-makers, then the normative frame is just an additional condition over the operational frame; but if decision-making is possible, then the operational frame requires finding a strategy to satisfy the objective, whereas the normative frame requires choosing a strategy that remains within what is allowed.*

In contrast to classical process specification languages (BPMN, DECLARE) that specify behavior required to accomplish a goal, frames focus on the **normative specification**. Goals remain largely implicit in formal process languages.

#### Three Blueprint Scenarios for Framed Autonomy

1. **Single decision-maker** — place a frame on process behavior
2. **Multiple decision-makers** — place frames on individual decision-makers
3. **Multiple decision-makers** — place frame(s) on process behavior or parts thereof

#### Centralized vs. Distributed Intelligence

- **Centralized**: AI agents as a single entity orchestrating the process. The environment may be stochastic and not fully observable. The frame is over the process.
- **Distributed**: AI agents as distributed resources enacting the process. Resources may have partial observability of other resources; coordination may be effortful; resource-level goals may be mutually inconsistent or inconsistent with process-level goals. Can frame individual resources, groups, or the entire process.

#### Security Benefit of Local Frames

Local operationalization of frames acts as a **security and privacy boundary**: the frame limits an agent's perspective and capabilities to only its necessary process context, inherently restricting the potential impact if an agent is compromised or manipulated by a malicious actor.

### 3.2 Explainability

As a **prerequisite to effective execution and governance**, an APM system should be explainable. Because an APM system is a composition of AI agents, this is achieved by endowing agents with the intrinsic capability to explain their own behavior—including agents assigned collective process-awareness responsibilities.

**Why explainability matters**:

| Concern | How Explainability Addresses It |
|----------|-------------------------------|
| **Trust** | Stakeholders (process owners, analysts, end users, customers) hesitate to rely on agentic recommendations when rationale is unclear |
| **Accountability** | If an agent fails, it must explain why so responsibility can be assigned and corrective actions taken |
| **Bias** | AI/ML may perpetuate biases—explainability enables detection and mitigation |
| **Compliance** | GDPR, EU AI Act require transparency, especially in finance, healthcare, HR |

**Explainability supports autonomy from two directions**:
1. Enabling agents to independently resolve misalignment in other agents' behavior
2. Reducing human intervention by making agent behavior understandable and transparent

**Four desirable properties of explanations in APM**:
1. Conform to framing constraints and statements
2. Capture the richness of contextual information affecting agents' behavior
3. Reflect causal execution dependencies (not just temporal sequences)
4. Be interpretable to other agents (human or digital)

### 3.3 Conversational Actionability

Conversational actionability = the agent's ability to **combine interaction and enactment capabilities**.

Agents need to integrate **conversational capabilities** (to coordinate with one another, receive instructions from, interact with, and report to human agents) with **enactment capabilities** (making decisions, performing actions accordingly).

**Two requirements**:

1. **Process-aware conversation**: interact with users or external agents using conversational interfaces to support, trigger, and guide actions related to process enactment

2. **Process-aware actionability**: conversations trigger business process executions (decisions, actions) and evolution actions (priority changes, process changes)

#### Federated, Not Centralized

Instead of centralized intelligence with a single point of truth, an APM system caters to **federated perspectives**. Each agent decides how it instantiates these capabilities based on its own individually informed perspective about 'the process' (its frame). This may require consensus resolution or tolerance for result variety.

#### Four Types of Agent-Enacted Behavior

| Type | Description |
|------|-------------|
| **Query** | Provide information on process(es) at model or instance level |
| **Recommend** | Provide insights and suggestions on adaptation and future evolution |
| **Create** | Elicit models from domain knowledge and process-relevant data |
| **Execute** | Trigger actions moving process instances to a new state |

To enact these behaviors, agents require interacting with tools providing different services—creating the challenge of identifying the best mix of tools to realize functionality in the "best way" possible.

### 3.4 Self-Modification

To adjust to ephemeral or permanent changes, APM systems must self-modify. A fundamental distinction:

| | Adaptation | Evolution |
|---|---|---|
| **Scope** | Short-term, instance-specific | Long-term, across multiple instances |
| **Permanence** | Ephemeral—affects only current instance | Persistent—incorporated into process model/schema |
| **Trigger** | Immediate, unforeseen issues during execution | Aggregated insights from historical data, repeated anomalies |
| **What changes** | Localized modifications within current process definition | The process model itself—affects future instantiations |
| **Examples** | Handle exceptional circumstance not anticipated at design time | Systemic improvement after observing patterns across many instances |

**The adaptation↔evolution feedback cycle**:

Adaptations generate execution traces and performance data → feed into learning mechanisms → when patterns prove consistently effective across multiple instances → become candidates for **evolutionary incorporation** into the process model (the agent's frame).

Conversely, evolution should **reduce the frequency** of certain adaptations by preemptively addressing known failure modes. But adaptations remain necessary for truly novel situations not yet encountered frequently enough to justify evolutionary modification.

**Design implications**:
- **Adaptation** mechanisms prioritize responsiveness, robustness, and security under uncertainty
- **Evolution** mechanisms require pattern mining across execution histories, causal inference, statistical validation, and change management protocols for safe deployment

---

## 4. Research Challenges

Challenges are categorized according to the four capabilities, plus cross-cutting challenges. These were identified during the Dagstuhl seminar, published as PMAI workshop papers, then augmented based on feedback.

### 4.1 Challenges Regarding Framed Autonomy

**F1: What is a pragmatic notion of an agent in business process execution?**
Before LLMs, "agent" didn't play a major role in business information systems. Practitioners may call any LLM-powered tool an "agent" without understanding deeper properties. Defining a precise yet intuitively understandable notion of an agent is a key prerequisite for framing autonomy.

**F2: How to elicit and specify frames?**
Requires a frame meta-model and specification language(s). Declarative approaches (DECLARE, temporal business rule languages) can be augmented with deontic notions. For elicitation: LLMs can generate frames from natural language text; rule mining can infer normative constraints from traces of well-behaved agents.

**F3: How to operationalize frames on real-world symbolic data?**
Frames need runtime integration to ensure agent frame-compliance. Formal logic-based approaches provide the imperative foundation to guardrail agent execution to legal actions. Explainability is a necessity given the intricacy of normative requirements and the scale of real-world symbolic data.

**F4: How to design incentive and reinforcement mechanisms for frame-compliant agents?**
The question is not merely how to make a frame available, but how to ensure agents **actively use it, internalize it, and treat it as instrumentally valuable**. Humans can be motivated through compensation and recognition. AI agents require a functional counterpart that reshapes their internal utility models. The open problem: designing rewards inherently as part of the frame that make adherence beneficial while preserving autonomy. Over time, agents must learn which parts of the frame are genuinely useful, which constrain them productively, and which can be deprioritized without violating governance.

### 4.2 Challenges Regarding Explainability

**X1: How to specify or let agents learn other agents' explanation preferences?**
Preferences may be explicitly declared, interactively elicited through dialogue, or implicitly inferred from behavior. Must accommodate both static and dynamically adapting preferences. Challenge: finding the sweet spot between keeping explanations current and not confusing the explainee.

**X2: How to leverage and extend existing XAI techniques?**
Making sense of agent behavior goes beyond explaining AI models—must account for broader context, knowledge acquired over time, cause-and-effect relationships, and framing constraints.

**X3: How to articulate actionable explanations to preserve autonomy?**
Explanations should indicate corrective or mitigating actions the explainee can take without escalating to an external agent—enabling autonomous resolution.

**X4: When to generate explanations (generation time) and how long to preserve them?**
Proactive vs. deferred generation; when to retire outdated explanations.

**X5: How to generate causally sound explanations?**
Distinguish spuriously correlated actions (merely temporally sequential) from causally dependent ones (one directly triggers another)—within and across agents.

### 4.3 Challenges Regarding Conversational Actionability

**A1: How to engage in conversations with human principals and other agents?**
Two facets: (a) agent-to-human interaction using natural language and domain-specific formats (process diagrams, dashboards); (b) agent-to-agent interaction using protocols (ACP, MCP), formal languages, and recently developed human-readable token encoding formats (e.g., TOON).

**A2: How to exploit capabilities of process management tools and services?**
Agents need to relate conversations to goals and actions—requiring interaction with: ERP/CRM systems, collaboration tools, physical actuators (IoT/robots), process/task automation tools, dedicated planners/schedulers. This requires semantically rich descriptions enabling discovery (e.g., via MCP).

**A3: How to compute and use key indicators on overall behavior?**
Standard KPIs (performance, time, cost) plus trust, usability, uncertainty, flexibility indicators. Agents need to ponder the impact of taking actions before doing so.

### 4.4 Challenges Regarding Self-Modification

Challenges center on: runtime monitoring for adaptation triggers, pattern mining across execution histories, causal inference (correlation vs. causation), statistical validation (not artifacts of noise), and change management protocols for safe deployment without disrupting ongoing operations.

---

## 5. Conclusion

The manifesto serves as a **roadmap** for bridging BPM, AI, and Multi-Agent Systems communities. It calls for:

1. Establishment of **APM formal foundations** (process algebra, π-calculus, BDI formalisms)
2. Development of **engineering and management practices** for building and operating APM systems
3. **Empirical research** to confirm or challenge the assumptions made herein
4. Security frameworks, legal/liability frameworks, benchmarking suites

> The paper explicitly acknowledges that all of these are **still needed**—this is a research agenda, not a solved problem.

---

## Cross-Reference: APM ↔ SDLC Transformation

| Concept | SDLC Domain | APM Domain (this paper) |
|---------|------------|------------------------|
| Old paradigm | Human thinks first → decompose → write code | Predefined process → approval flow → human execution |
| New paradigm | AI Sandwich / Operator→Patron | Framed Autonomy / Agentic BPM |
| Human role | Brief, Review, Sign-off | Define frame + Human-on-the-loop |
| AI role | Execute and explore in the middle layer | Perceive→Reason→Act within frame |
| Governance | Constraints encoded into CI/linter | Normative frame + Explainability |
| Core artifact | Spec replaces code | Frame replaces BPMN flowchart |
| Production maturity | ~11% (CamundaCon 2026) | ~11% (same data source) |
| Key tension | "You can't think clearly enough anymore" | "Process can no longer be fully predefined" |
| Theoretical framework | None yet (exploring) | APM Manifesto (Dagstuhl, 18 authors) |

**Key conceptual correspondences**:

- *Framed Autonomy* ↔ AI Sandwich / brief-review-signoff / in-the-loop→on-the-loop
- *Normative frame vs. Operational frame* ↔ Constraints in CI/linter vs. constraints in prompt
- *Human-Agent Handoff challenge* ↔ Sign-off gate in delegation workflow
- *Self-Modification feedback cycle* ↔ Continuous improvement via process mining (Engelberg)
- *Agent as first-class citizen* ↔ "I no longer steer; I commission" (Mollick)
