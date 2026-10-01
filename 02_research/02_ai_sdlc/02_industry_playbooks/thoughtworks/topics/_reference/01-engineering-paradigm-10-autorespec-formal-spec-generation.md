# Topic 01 / Ref 10: AutoReSpec Formal Specification Generation

- source_url: `https://arxiv.org/abs/2604.03758`
- source_type: `arXiv paper`
- authority_level: `primary research`
- publication_time: `2026`
- accessed_on: `2026-04-17`
- topic: `01 engineering-paradigm`

## Why This Matters

This source matters because it directly studies the path from informal code context to verifiable formal specification, and it explicitly documents where naive LLM prompting fails.

## Key Facts Captured

- The paper notes that early LLM specification generation often fails verification due to syntax errors, logical inaccuracies, or incomplete reasoning.
- It argues that static prompts alone are insufficient for reliable specification generation.
- AutoReSpec uses validator feedback and a collaborative two-stage design to recover from failure.
- On its benchmark, it reports stronger success probability and completeness than prior methods, while reducing evaluation time.

## Research Use

- Supports Topic 01’s claim that spec generation must be validation-aware, not just prompt-engineered.
- Strengthens the argument for a `spec -> validate -> refine` loop before code generation.
- Supplies another limitation source showing that specification quality cannot be trusted without external checking.

## Caveats

- This is very recent research and has not yet proven broad industrial adoption.
- It improves formal specification generation, but does not replace release discipline or system-level safety controls.
