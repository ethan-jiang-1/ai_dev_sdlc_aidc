# Topic 03 / Ref 12: LangGraph Persistence and Checkpoints

- source_url: `https://docs.langchain.com/oss/python/langgraph/persistence`
- source_type: `official framework documentation`
- authority_level: `official implementation guidance`
- publication_time: `current LangGraph docs, accessed 2026-04-17`
- accessed_on: `2026-04-17`
- topic: `03 agent-native-infrastructure`

## Why This Matters

This source makes the `work ledger` discussion more concrete for agent runtimes. LangGraph does not just preserve messages; it saves graph state as checkpoints at every step and exposes thread- and checkpoint-level retrieval surfaces.

## Key Facts Captured

- LangGraph says its persistence layer saves graph state as checkpoints at every step of execution, organized into threads.
- The persistence layer is explicitly linked to human-in-the-loop workflows, conversational memory, time-travel debugging, and fault-tolerant execution.
- Checkpointers expose methods to store checkpoints, store intermediate writes, and fetch a checkpoint tuple by `thread_id` and `checkpoint_id`.
- Production-oriented backends exist for persistent stores such as Postgres and Cosmos DB.

## Research Use

- Supports a more precise Topic 03 claim that a near-term `work ledger` can be decomposed into thread identity, checkpoint state, intermediate writes, and recovery surfaces.
- Shows that resumable agent execution is already pushing application frameworks toward explicit state-snapshot infrastructure.
- Helps connect Topic 03 runtime architecture with Topic 02 human review loops, because human-in-the-loop is a first-class persistence use case.

## Caveats

- LangGraph persistence is a checkpoint system, not a full enterprise agent ledger.
- The docs do not define a unified schema for authorization, budget, capability contracts, or acceptance criteria.
