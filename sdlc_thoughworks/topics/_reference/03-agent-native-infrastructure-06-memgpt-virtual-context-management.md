# Topic 03 / Ref 06: MemGPT and Virtual Context Management

- source_url: `https://arxiv.org/abs/2310.08560`
- source_type: `arXiv paper`
- authority_level: `primary research`
- publication_time: `2024 version`
- accessed_on: `2026-04-17`
- topic: `03 agent-native-infrastructure`

## Why This Matters

This is one of the most direct matches to the seed’s “Agent OS” language. It explicitly treats memory management for LLMs as an operating-system-style problem.

## Key Facts Captured

- MemGPT proposes `virtual context management` inspired by hierarchical memory systems in operating systems.
- The paper says limited context windows are a hard constraint for extended conversations and document analysis.
- It introduces multiple memory tiers and uses interrupt-like control flow to manage interactions.
- The framing is explicitly OS-like rather than pure prompting.

## Research Use

- Strong support for Topic 03’s claim that agent memory needs runtime-level management rather than brute-force context extension.
- Useful for Agent OS discussions around working memory, long-term memory, and control flow.

## Caveats

- MemGPT is research, not standard enterprise infrastructure.
- It is strong on memory architecture but weaker on protocol interoperability and observability.
