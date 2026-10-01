# Topic 01 / Ref 01: EARS Structured Requirements

- source_url: `https://research.manchester.ac.uk/en/publications/easy-approach-to-requirements-syntax-ears/`
- source_type: `conference paper metadata for original IEEE RE'09 paper`
- authority_level: `primary research`
- publication_time: `2009`
- accessed_on: `2026-04-17`
- topic: `01 engineering-paradigm`

## Why This Matters

EARS directly addresses the seed question of whether free-form user stories are too weak for AI-native engineering. Its value is not “AI-specific,” but that it offers a compact syntax that reduces ambiguity without forcing teams into heavyweight formal methods.

## Key Facts Captured

- The paper frames unconstrained natural language requirements as a direct source of downstream volatility and risk.
- The authors explicitly argue that fully non-textual notations introduce translation errors and training overhead.
- EARS proposes a small set of structural rules and five simple templates.
- The reported case study found qualitative and quantitative improvement over conventional textual requirements specifications.

## Research Use

- Supports the claim that the next-generation spec language may be `structured natural language`, not necessarily full formal verification from day one.
- Gives Topic 01 a practical midpoint between vague user stories and mathematically formal specs.
- Provides a concrete candidate for “spec-first AI coding” workflows.

## Caveats

- The paper is about requirements quality, not LLM-driven coding specifically.
- It does not solve test generation, type constraints, or deployment safety by itself.
