# Topic 04 / Ref 15: Google Toxic Combinations and Chokepoints

- source_url: `https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview`
- source_type: `official Google Cloud documentation`
- authority_level: `official implementation guidance`
- publication_time: `live doc; accessed 2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

This source is especially relevant because it operationalizes a concept very close to “compound blast radius”: multiple weaknesses combining into a path toward high-value assets.

## Key Facts Captured

- Google says Risk Engine detects `toxic combinations` and `chokepoints` during attack path simulations.
- Each toxic combination or chokepoint gets an attack exposure score based on the number and priority of exposed high-value resources and the likelihood of attacker success.
- Chokepoints represent common resources or resource groups where multiple attack paths converge.
- Remediating a chokepoint can therefore break multiple toxic combinations at once.

## Research Use

- Strengthens Topic 04’s blast-radius discussion by giving a concrete graph-based scoring and prioritization model.
- Provides a practical way to talk about cascading risk rather than isolated findings.
- Suggests a realistic future direction for agent change-risk scoring: find the chokepoints and compounded weakness paths first.

## Caveats

- Still a cloud/posture model, not a code-diff model.
- Strong on prioritization logic, weaker on software delivery incidents.
