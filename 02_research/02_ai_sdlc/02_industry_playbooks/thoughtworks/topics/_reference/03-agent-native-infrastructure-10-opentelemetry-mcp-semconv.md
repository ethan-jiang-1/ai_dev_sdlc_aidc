# Topic 03 / Ref 10: OpenTelemetry MCP Semantic Conventions

- source_url: `https://opentelemetry.io/docs/specs/semconv/gen-ai/mcp/`
- source_type: `official specification docs`
- authority_level: `official observability specification`
- publication_state: `development`
- accessed_on: `2026-04-17`
- topic: `03 agent-native-infrastructure`

## Why This Matters

This source ties protocol-layer interoperability to observability. It matters because Topic 03 is not only about agent communication, but about being able to inspect prompt, tool, and RPC behavior across that communication.

## Key Facts Captured

- The MCP semantic conventions define fields such as `gen_ai.prompt.name`, `gen_ai.tool.name`, and `jsonrpc.request.id`.
- They also include operation names and RPC status/error fields.
- This makes prompt-level, tool-level, and request-level tracing part of the shared instrumentation surface.

## Research Use

- Supports Topic 03’s claim that a viable Agent OS needs protocol-aware observability rather than opaque tool calls.
- Helps connect MCP-based runtimes to enterprise tracing and debugging layers.

## Caveats

- Like broader GenAI semconv, this spec is still developing.
- It instruments protocol behavior but does not itself enforce authorization or memory policy.
