# Topic 03 / Ref 04: Agent2Agent (A2A) Protocol

- source_url: `https://github.com/a2aproject/A2A`
- source_type: `official protocol repository`
- authority_level: `official open protocol source`
- publication_state: `v1.0.0 as of 2026-03-12`
- accessed_on: `2026-04-17`
- topic: `03 agent-native-infrastructure`

## Why This Matters

Topic 03 needs to answer how agents talk to each other as agents rather than as raw tool wrappers. A2A is one of the strongest current candidates for that interoperability layer.

## Key Facts Captured

- A2A is described as an open protocol for communication and interoperability between opaque agentic applications.
- The repo and docs emphasize capability discovery, long-running tasks, streaming, push notifications, and security/authentication concerns.
- A2A’s design goal is to let agents collaborate without exposing their internal memory, tools, or implementation details.
- The project is open source under the Linux Foundation with Google contribution lineage.

## Research Use

- Supports Topic 03’s claim that agent-native infrastructure needs an inter-agent protocol layer in addition to tool protocols like MCP.
- Useful for reasoning about agent cards, capability negotiation, and cross-runtime collaboration.

## Caveats

- A2A gives an interoperability protocol, not a complete runtime, memory, or governance platform.
- It does not by itself solve evaluation, ontology extraction, or work-ledger persistence.
