# Topic 03 / Ref 03: Anthropic Agent SDK

- source_url: `https://claude.com/blog/building-agents-with-the-claude-agent-sdk`
- source_type: `official engineering article`
- authority_level: `primary practitioner source`
- publication_time: `2025-09-29`
- accessed_on: `2026-04-17`
- topic: `03 agent-native-infrastructure`

## Why This Matters

This source gives a practical view of the minimum agent runtime loop: gather context, take action, verify work, repeat. It is useful because it treats the file system and tool environment as part of the runtime substrate.

## Key Facts Captured

- Anthropic says agents need more than prompts; they need to fetch and update context.
- The article explicitly describes the file system as information that can be pulled into context.
- It says folder and file structure become a form of context engineering.
- Anthropic recommends starting with agentic search over raw files and only adding semantic search when needed for speed or variation.
- MCP integrations are positioned as a standard way to attach external tools and services without custom integration code.

## Research Use

- Supports Topic 03’s claim that agent infrastructure includes context substrate, storage layout, search primitives, and tool integration.
- Gives a practical grounding for “work ledger” style design where state exists outside the model.

## Caveats

- This is a toolkit view rather than an enterprise governance or control-plane specification.
- It is strongest for local/runtime context and tool substrate, not for distributed multi-agent coordination.
