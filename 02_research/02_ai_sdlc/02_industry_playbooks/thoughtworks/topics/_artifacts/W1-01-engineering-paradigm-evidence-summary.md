# W1-01 Engineering Paradigm Evidence Summary

## Current Thesis

Topic 01 is no longer just "AI makes review harder." The current evidence package supports a stronger thesis:

- The quality firewall is moving upstream into `structured requirements` and `behavior models`.
- It is moving sideways into `tests as prompt`, `tests as verification`, and `constraint-aware generation`.
- It is moving downstream into `validation workflows`, `coverage`, `review augmentation`, and `safe shipment controls`.
- Human review is not disappearing, but its role is narrowing toward high-judgment checkpoints rather than bulk line-by-line validation.

## Evidence Clusters

### 1. Structured specs beat vague requirements

- EARS shows that a small number of structural templates can reduce ambiguity and volatility in stakeholder requirements.
- Statecharts show that complex reactive behavior can be specified in a more manageable, simulatable, and partially verifiable form than plain prose.

### 2. TDD becomes an agent control loop

- LLM4TDD frames tests as iterative steering signals for code generation.
- Tests as Prompt strengthens this by treating tests as both prompt and verification interface.
- Generative AI for TDD shows this can work, but only with incremental interaction patterns and supervision.

### 3. Constraint systems improve reliability

- LLM4TDG shows that explicit constraint representations and backtracking materially improve test-driven generation outcomes.
- Type-Constrained Code Generation shows that type systems can be lifted into decoding-time guardrails rather than only post-generation checks.
- AutoReSpec shows that when LLM-generated specifications are validator-coupled, formal spec generation becomes materially more robust.
- This suggests that “make illegal states or invalid outputs harder to express” is not just a type-system slogan; it is a practical design direction for AI-native coding workflows.

### 4. Code review stops scaling under AI load

- Salesforce reports that AI-generated code volume and PR size can outpace human review capacity.
- Review quality degrades not only because of more code, but because reviewers lose conceptual coherence and operate under higher cognitive load.

### 5. Safe shipment becomes the new bottleneck

- Salesforce’s production account makes clear that more code only helps if testing, validation, review, and deployment safeguards scale with it.
- Human approval remains mandatory for production-impacting actions.

### 6. Small-batch discipline can be instrumented

- DORA's small-batch and trunk-based-development guidance gives concrete measurement surfaces: branch lifetime, active branch count, merge cadence, review latency, feature slice size, release cadence, and ability to release partial features safely.
- GitHub branch protection and merge queue show how required checks, reviews, deployment gates, linear history, and queue validation can become enforceable merge controls rather than team norms.
- Google SRE canarying shows that release slicing continues after merge: binary release, feature exposure, traffic rollout, metric evaluation, and rollback can be decoupled to constrain production blast radius.

## What Is Confirmed

- Structured specification is not optional if AI-generated code is expected to be reliable.
- TDD is becoming both a prompting method and a verification method.
- Large AI-generated PRs are a systemic review hazard.
- Quality gates must move earlier and become more automated.
- Small-batch delivery can be partially mechanized through trunk discipline, fast CI, protected-branch policy, merge queues, deployment gates, feature flags, and canary rollout.

## What Is Still Missing

- Stronger topic-specific evidence on type systems / formal constraints outside testing.
- Direct AI-specific enterprise case studies showing `spec -> test -> code -> slice -> merge -> canary` as a full enforced pipeline.
- More explicit comparative evidence on when human review can be safely reduced and where it must remain mandatory.

## Source Set

- `_reference/01-engineering-paradigm-01-ears-structured-requirements.md`
- `_reference/01-engineering-paradigm-02-statecharts-reactive-specification.md`
- `_reference/01-engineering-paradigm-03-llm4tdd-best-practices.md`
- `_reference/01-engineering-paradigm-04-tests-as-prompt-tdd-benchmark.md`
- `_reference/01-engineering-paradigm-05-genai-for-tdd-preliminary-results.md`
- `_reference/01-engineering-paradigm-06-llm4tdg-constraint-reasoning.md`
- `_reference/01-engineering-paradigm-07-salesforce-scaling-code-reviews.md`
- `_reference/01-engineering-paradigm-08-salesforce-ai-tooling-quality-safety.md`
- `_reference/01-engineering-paradigm-09-type-constrained-code-generation.md`
- `_reference/01-engineering-paradigm-10-autorespec-formal-spec-generation.md`
- `_reference/01-engineering-paradigm-11-dora-working-in-small-batches.md`
- `_reference/01-engineering-paradigm-12-dora-trunk-based-development.md`
- `_reference/01-engineering-paradigm-13-github-branch-protection-merge-queue.md`
- `_reference/01-engineering-paradigm-14-google-sre-canarying-releases.md`
