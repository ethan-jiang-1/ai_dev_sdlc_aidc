# Topic 01 / Ref 03: LLM4TDD

- source_url: `https://arxiv.org/abs/2312.04687`
- source_type: `arXiv paper`
- authority_level: `primary research`
- publication_time: `2023`
- accessed_on: `2026-04-17`
- topic: `01 engineering-paradigm`

## Why This Matters

This is one of the cleanest direct attempts to turn TDD into an LLM-facing development method rather than a purely human discipline.

## Key Facts Captured

- The paper explicitly studies `guiding LLMs to generate code iteratively using a test-driven development methodology`.
- It empirically evaluates ChatGPT on coding problems and studies how different test, prompt, and problem attributes affect outcomes.
- The framing is important: tests are not only for post-hoc verification but also for structuring iterative code generation.

## Research Use

- Supports the Topic 01 claim that TDD can act as both `prompt structure` and `verification harness`.
- Helps reframe TDD as part of the agent control loop rather than just a human coding habit.
- Useful for identifying what test attributes matter when tests become the main steering signal for code agents.

## Caveats

- It is early empirical research and uses benchmark-style tasks rather than a full enterprise SDLC.
- It does not answer deployment workflow, release safety, or human governance questions on its own.
