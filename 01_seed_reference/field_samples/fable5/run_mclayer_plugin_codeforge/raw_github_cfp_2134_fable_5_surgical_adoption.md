# Raw Notes: plugin-codeforge `#2134` / `#2135`

## Issue `#2134`

Title:

`[CFP][EPIC] Fable 5 surgical adoption — chief-author·long-horizon·adversarial 역할 10개 에이전트 model:fable + Claude Code ≥2.1.170 floor`

Key points captured from the public Epic:

- Fable 5 is treated as materially stronger than Opus 4.8 on long-horizon software engineering and adversarial reasoning, but at 2x the price.
- Adoption is intentionally narrow: only `chief-author`, long-horizon agentic coding, and adversarial review/judging roles are upgraded.
- The Epic explicitly excludes several other roles from Fable adoption, including narrower advocate roles, cheaper model lanes, deploy workers, and the top-level orchestrator session.
- Compatibility is part of the policy: `model: fable` requires `Claude Code >= 2.1.170`.
- The target surface is split across four lanes and ten agents:
  - `design`: `Architect`, `ArchitectPL`, `SecurityArch`
  - `develop`: `Developer`, `DeveloperPL`
  - `review`: `ClaudeReview`, `CodeReviewPL`, `DesignReviewPL`, `SecurityTestPL`
  - `requirements`: `Researcher`

Notable later status update in the same issue:

- Runtime fallback was later codified so that if Fable is unavailable, the orchestrator triggers a fresh respawn on `opus`.
- The issue author explicitly separates two questions:
  - governance is complete
  - actual Fable runtime availability may still be unsolved in the current environment

## PR `#2135`

Title:

`feat(CFP-2134): ADR-117 Fable 5 surgical 모델 tier 채택 (foundation)`

Key points captured from the merged PR:

- `ADR-117` is introduced as the policy anchor for the Fable tier decision.
- The PR states that lane PRs and marketplace sync remain separate, which shows the adoption was decomposed into multiple execution surfaces rather than shipped as one big blob.
- The PR body calls out the `Claude Code >= 2.1.170` floor in the consumer guide.
- The commit message explicitly frames the change as:
  - `surgical 10 에이전트 model:fable`
  - `Claude Code >=2.1.170 호환성 floor`
  - `Orchestrator opus 유지`
- The PR merged with CI checks and later became a precedent referenced by follow-up governance changes.

## Why this raw note matters

- This is not a media article. It is a public issue + PR chain with role scoping, compatibility gating, staged rollout, and recovery logic.
- It is one of the clearest GitHub-native examples in this repo so far of Fable 5 being treated as a selectively assigned systems component rather than a generic “best model.”
