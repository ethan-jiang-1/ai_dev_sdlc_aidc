# Topic 01 / Ref 04: Tests as Prompt

- source_url: `https://arxiv.org/abs/2505.09027`
- source_type: `arXiv paper`
- authority_level: `primary research`
- publication_time: `2025`
- accessed_on: `2026-04-17`
- topic: `01 engineering-paradigm`

## Why This Matters

This paper pushes the Topic 01 hypothesis further: tests are not merely helpful guardrails, they can be the specification interface itself.

## Key Facts Captured

- The paper introduces WebApp1K, a benchmark where test cases serve as both prompt and verification signal for code generation.
- It argues this setup is closer to real-world development than relying only on natural-language prompts.
- Results emphasize instruction following and in-context learning as more important for TDD success than general coding ability alone.
- The benchmark also surfaces bottlenecks such as instruction loss in long prompts and multi-feature complexity.

## Research Use

- Reinforces the idea that next-generation specs may often be partly executable.
- Supports the claim that AI-native engineering quality depends on how precisely tests encode intent.
- Provides explicit failure modes when test-as-spec prompts get too long or lose structure.

## Caveats

- Benchmark evidence is useful for mechanism understanding, but it is not the same as enterprise deployment evidence.
- It highlights test-prompt limitations, so it should be paired with structured requirements and smaller task decomposition.
