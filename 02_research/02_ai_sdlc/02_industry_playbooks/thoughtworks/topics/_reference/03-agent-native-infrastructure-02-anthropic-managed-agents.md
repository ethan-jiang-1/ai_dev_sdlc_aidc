# Topic 03 / Ref 02: Anthropic Managed Agents

- source_url: `https://www.anthropic.com/engineering/managed-agents`
- source_type: `official engineering article`
- authority_level: `primary practitioner source`
- publication_time: `2026`
- accessed_on: `2026-04-17`
- topic: `03 agent-native-infrastructure`

## Why This Matters

Topic 03 asks what a real agent runtime looks like when agents run for long durations. This source is valuable because it argues that harness assumptions go stale as models improve, so the infrastructure layer must keep interfaces stable while allowing implementation change.

## Key Facts Captured

- Anthropic says harness assumptions become stale as models improve.
- Managed Agents are described as being built around stable interfaces even as harnesses evolve.
- The article uses context-limit behavior as an example of why hard-coded assumptions in runtimes decay quickly.

## Research Use

- Supports the view that Agent OS needs abstraction boundaries and versioned interfaces, not only one-off scripts.
- Helps explain why a durable, evolvable runtime layer matters when model behavior changes over time.

## Caveats

- This source is about harness design philosophy, not a full low-level systems blueprint.
- It is strong on runtime evolution but weaker on knowledge graph and ontology concerns.
