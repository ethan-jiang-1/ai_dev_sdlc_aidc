# Topic 03 / Ref 09: OpenTelemetry GenAI Semantic Conventions

- source_url: `https://opentelemetry.io/docs/specs/semconv/gen-ai/`
- source_type: `official specification docs`
- authority_level: `official observability specification`
- publication_state: `development`
- accessed_on: `2026-04-17`
- topic: `03 agent-native-infrastructure`

## Why This Matters

If Agent OS is real, it needs observability. This source matters because it shows observability for GenAI systems is becoming explicit and structured rather than ad hoc logging.

## Key Facts Captured

- OpenTelemetry defines GenAI semantic conventions across events, metrics, model spans, and agent spans.
- The conventions also anticipate provider-specific extensions.
- The existence of dedicated `agent spans` is especially important because it treats agent operations as a first-class observability target.

## Research Use

- Supports Topic 03’s claim that agent infrastructure must include telemetry and trace semantics.
- Gives a concrete path for instrumenting agents in a consistent, cross-system way.

## Caveats

- The spec is still in development.
- Observability standards do not provide the runtime itself; they only help us inspect and govern it.
