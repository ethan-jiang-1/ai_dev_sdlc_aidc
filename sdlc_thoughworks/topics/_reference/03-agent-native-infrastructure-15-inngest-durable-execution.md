# Topic 03 / Ref 15: Inngest Durable Execution and Step-State Persistence

- source_url: `https://www.inngest.com/docs/learn/how-functions-are-executed`
- source_type: `official platform documentation`
- authority_level: `official implementation guidance`
- publication_time: `current Inngest docs, accessed 2026-04-17`
- accessed_on: `2026-04-17`
- topic: `03 agent-native-infrastructure`

## Why This Matters

This source supplies a second concrete execution pattern for the `work ledger` question. Inngest documents a step-based model where state, retries, memoization, and failure records are all explicit execution concerns.

## Key Facts Captured

- Inngest defines durable execution around state persistence outside the execution context plus automatic retries from the point of failure.
- Functions are decomposed into steps with unique IDs; each step can run and retry independently and returns state for subsequent steps.
- Step results are persisted in a managed function state store and reused through memoization so completed work is skipped on subsequent executions.
- Errors, retry attempts, and step state are persisted, and the function resumes from the failure point rather than restarting blindly.
- The docs explicitly contrast this with Temporal's deterministic replay model, clarifying that multiple ledger-like execution patterns exist in production systems.

## Research Use

- Supports the claim that a practical `work ledger` can be built from durable step state, memoized outputs, execution attempts, and resumable failure boundaries.
- Adds evidence that ledger-like execution records do not have to be event-sourcing only; step-based memoization is another viable design pattern.
- Helps refine Topic 03 by distinguishing execution durability patterns from higher-level agent policy and capability models.

## Caveats

- Inngest is a durable workflow platform, not a dedicated agent ledger system.
- The documented model still does not unify authorization, budget, capability entitlement, and acceptance criteria in one canonical record.
