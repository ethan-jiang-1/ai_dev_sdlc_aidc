# Topic 04 / Ref 14: Google Attack Exposure Scores and Attack Paths

- source_url: `https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn`
- source_type: `official Google Cloud documentation`
- authority_level: `official implementation guidance`
- publication_time: `live doc; accessed 2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

This is the strongest implementation-oriented public source found so far for the blast-radius problem. It does not fully solve code-change blast radius, but it provides a concrete operational proxy via attack exposure scores and attack path simulation.

## Key Facts Captured

- Google defines an `attack exposure score` as a measure of how exposed resources are to potential attack if an attacker gains access to the cloud environment.
- Scores apply to findings, issues, and high-value resources, and are intended to prioritize remediation.
- Risk Engine generates these scores through attack path simulations from the public internet.
- The documentation says a score of `0` means no path was found in the latest simulation, but not that risk is absent.
- Google also requires a defined `high-value resource set` for scores to reflect business priorities.

## Research Use

- Gives Topic 04 a concrete operational model for “blast radius” as exposure-to-high-value-resources rather than only line-level code impact.
- Supports the claim that business-valued assets, graph simulation, and prioritized remediation need to be part of the control stack.
- Useful as a proxy architecture for the later research question of code-change risk weighting.

## Caveats

- Focused on cloud attack-path exposure, not software-diff-specific blast radius.
- Explicitly excludes some internal-actor and zero-day scenarios from the score.
