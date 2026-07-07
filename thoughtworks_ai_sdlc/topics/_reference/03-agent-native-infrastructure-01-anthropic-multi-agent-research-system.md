# Topic 03 / Ref 01: Anthropic Multi-Agent Research System

- source_url: `https://www.anthropic.com/engineering/multi-agent-research-system`
- source_type: `official engineering article`
- authority_level: `primary practitioner source`
- publication_time: `2025-06-13`
- accessed_on: `2026-04-17`
- topic: `03 agent-native-infrastructure`

## Why This Matters

This is one of the most concrete public descriptions of a production multi-agent system. It is directly relevant to Topic 03 because it shows what a real orchestrator-worker agent runtime needs beyond a single model call.

## Key Facts Captured

- Anthropic describes a lead-agent and subagent `orchestrator-worker` pattern.
- They explicitly say multi-agent systems introduce new coordination, evaluation, and reliability challenges.
- The article states the lead agent stores its plan in memory so it survives long contexts and can hand off across context resets.
- Anthropic also uses external artifact creation so subagents can persist outputs directly instead of sending everything back through conversation history.
- The system relies on durable execution and resume capability because restarting long-running agents from scratch is too costly.

## Research Use

- Supports Topic 03’s claim that agent infrastructure needs orchestration, memory, artifact persistence, and recovery semantics.
- Gives a concrete model for why “Agent OS” is more than model hosting.
- Helps distinguish simple workflows from true long-horizon multi-agent runtimes.

## Caveats

- Anthropic also says multi-agent systems are expensive and not ideal for tightly interdependent tasks.
- This is a production research-agent pattern, not a universal architecture for every enterprise agent use case.
