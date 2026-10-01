# Topic 03 / Ref 13: OpenAI Agents SDK Results and State Surfaces

- source_url: `https://developers.openai.com/api/docs/guides/agents/results`
- source_type: `official SDK documentation`
- authority_level: `official implementation guidance`
- publication_time: `current OpenAI docs, accessed 2026-04-17`
- accessed_on: `2026-04-17`
- topic: `03 agent-native-infrastructure`

## Why This Matters

This source is useful because it turns abstract agent continuation into named runtime surfaces. It shows what a practical run result needs to expose when the system must pause, resume, hand off, or continue on the next turn.

## Key Facts Captured

- OpenAI defines an agent result as more than final output; it is also a handoff boundary, next-turn continuation surface, and resumable snapshot when a run pauses.
- The documented result surfaces include local replay-ready history, the last owning specialist, managed response chaining identifiers, interruptions, and saved state.
- Interrupted runs return `state` as the saved snapshot that gets passed back into the runtime after approval or rejection.
- The docs explicitly recommend reusing sessions or stored IDs to persist and continue history across turns instead of replaying everything manually in every case.

## Research Use

- Supports the claim that an enterprise `work ledger` needs continuation-ready state surfaces, not just logs.
- Helps define a minimum ledger schema around run identity, continuation state, history, specialist ownership, and pending approval boundary.
- Bridges Topic 03 runtime design with Topic 02 handoff patterns and Topic 04 approval controls.

## Caveats

- This is an SDK state model, not a full multi-system ledger architecture.
- The docs do not specify an enterprise-wide persistent schema for budgets, capabilities, or compliance metadata.
