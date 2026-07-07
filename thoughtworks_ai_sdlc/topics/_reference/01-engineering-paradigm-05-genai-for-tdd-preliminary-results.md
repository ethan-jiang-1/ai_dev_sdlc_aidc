# Topic 01 / Ref 05: Generative AI for TDD - Preliminary Results

- source_url: `https://link.springer.com/chapter/10.1007/978-3-031-72781-8_3`
- source_type: `open access conference paper`
- authority_level: `primary research`
- publication_time: `2025`
- accessed_on: `2026-04-17`
- topic: `01 engineering-paradigm`

## Why This Matters

This paper is useful because it does not assume AI automatically improves TDD. It tests interaction patterns and is explicit that supervision remains necessary.

## Key Facts Captured

- The paper compares collaborative, fully-automated, and non-automated TDD patterns.
- It states that GenAI can reduce some TDD effort, but only when the process remains incremental and supervised.
- The authors report that GenAI can mislead non-expert developers and may generate code “for the sake of the query” rather than for correctness.
- Their workflow design has to explicitly constrain the model to keep existing tests and proceed incrementally rather than jumping straight to a full solution.

## Research Use

- Strong evidence for Topic 01’s claim that AI-native TDD must be a control loop, not a one-shot code request.
- Provides a limitation source for “AI makes TDD easy” narratives.
- Supports keeping human review at refactor / quality checkpoints even when tests are AI-assisted.

## Caveats

- Small exploratory study.
- It demonstrates feasibility and limitations, not mature large-scale industrial practice.
