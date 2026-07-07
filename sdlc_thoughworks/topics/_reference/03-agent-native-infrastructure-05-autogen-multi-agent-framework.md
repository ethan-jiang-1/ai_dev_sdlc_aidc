# Topic 03 / Ref 05: AutoGen Multi-Agent Framework

- source_url: `https://arxiv.org/abs/2308.08155`
- source_type: `arXiv paper`
- authority_level: `primary research`
- publication_time: `2023`
- accessed_on: `2026-04-17`
- topic: `03 agent-native-infrastructure`

## Why This Matters

AutoGen is one of the foundational research references for multi-agent conversation as an application-building primitive.

## Key Facts Captured

- The paper presents AutoGen as a framework for building LLM applications via multiple agents that converse to accomplish tasks.
- It explicitly supports combinations of LLMs, human inputs, and tools.
- Natural language and computer code can both define interaction behavior.
- The paper positions agent interaction behavior itself as programmable infrastructure.

## Research Use

- Supports Topic 03’s claim that orchestration is not just “call multiple models”; it is a conversation protocol and programmable coordination layer.
- Bridges runtime design with human-in-the-loop and tool-in-the-loop workflows.

## Caveats

- AutoGen is a framework paper, not a production operations guide.
- It says little about enterprise observability, security boundaries, or long-horizon persistence durability.
