# Wave 0 Shared Foundation Summary

## Foundation Thesis

AI-Native SDLC cannot be framed as "AI writes more code." The shared evidence points to a system-level shift:

- Engineering rigor moves away from line-by-line code review and into specifications, tests, constraints, risk tiering, and release discipline.
- Agentic systems are useful only when their autonomy is bounded by tool design, environmental feedback, evaluation, checkpoints, and security controls.
- Organizational throughput becomes constrained by approval, trust, knowledge distribution, and governance latency rather than raw code generation capacity.
- Infrastructure and security become inseparable: every agent runtime is also an identity, authorization, memory, tool-use, audit, and threat-modeling problem.

## Implications For Wave 1

- Topic 01 must prove whether quality controls are actually migrating upstream and sideways, not merely restate that AI improves coding speed.
- Topic 02 must treat "middle loop" as a control-plane function: task decomposition, trust calibration, context packaging, checkpointing, and organizational exception handling.
- Topic 03 must define a minimum viable Agent OS using concrete primitives: tool protocol, authorization, state/memory, work ledger, observability, and context retrieval.
- Topic 04 must own the non-negotiable safety layer: least privilege, non-human identities, confused deputy controls, auditability, threat modeling, blast-radius estimation, and red-team practice.

## Cross-Topic Tensions To Track

- Productivity vs delivery health: DORA evidence suggests AI adoption can coexist with worse delivery stability if batch size and delivery discipline regress.
- Agent autonomy vs governance: Anthropic and OWASP both imply that useful autonomy requires clearer interfaces, stronger sandboxing, and explicit checkpoints.
- Context richness vs reliability: context engineering evidence suggests that more context is not always better; systems need compact, high-signal retrieval and durable external memory.
- Platform convenience vs security boundary: MCP-style tool integration improves interoperability but turns tool servers, tokens, schemas, and authorization paths into critical control surfaces.

## Evidence Base

Primary Wave 0 sources are indexed in `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference/_INDEX.md`.
