# Topic 03 / Ref 14: OpenAI Agents SDK Tracing and Observability

- source_url: `https://developers.openai.com/api/docs/guides/agents/integrations-observability`
- source_type: `official SDK documentation`
- authority_level: `official implementation guidance`
- publication_time: `current OpenAI docs, accessed 2026-04-17`
- accessed_on: `2026-04-17`
- topic: `03 agent-native-infrastructure`

## Why This Matters

This source gives Topic 03 a concrete observability-side answer to the `work ledger` problem. A ledger that cannot explain model calls, tool calls, handoffs, approvals, and custom workflow boundaries is too weak for production agent systems.

## Key Facts Captured

- OpenAI says built-in tracing is enabled by default in the normal server-side Agents SDK path.
- Every run can emit a structured record of model calls, tool calls, handoffs, guardrails, and custom spans.
- The docs position traces as the end-to-end workflow record developers use before formal evaluation loops.
- The page also frames MCP wiring and observability as runtime decisions about which external surfaces live inside the agent loop.

## Research Use

- Strong support for the claim that a `work ledger` needs rich operational traces in addition to checkpoints or replay history.
- Helps break the ledger problem into two complementary records: continuation state and inspection state.
- Useful bridge between Topic 03 runtime substrate and Topic 04 audit, policy, and reviewability requirements.

## Caveats

- Trace records are diagnostic surfaces; they are not by themselves the full source of truth for task contracts, budgets, or authorization.
- The docs do not prescribe a canonical enterprise schema for joining traces to permissions or financial controls.
