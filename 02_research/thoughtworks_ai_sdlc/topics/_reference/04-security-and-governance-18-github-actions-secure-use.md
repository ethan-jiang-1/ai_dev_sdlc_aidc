# Topic 04 / Ref 18: GitHub Actions Secure Use Reference

- source_url: `https://docs.github.com/en/actions/reference/security/secure-use`
- source_type: `official GitHub documentation`
- authority_level: `official implementation guidance`
- publication_time: `live doc; accessed 2026-04-17`
- accessed_on: `2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

This is one of the strongest official documents for turning software-delivery blast-radius control into concrete pipeline defaults. It ties together immutable dependencies, short-lived credentials, runner posture, auditability, and dependency review.

## Key Facts Captured

- GitHub says pinning an action to a full-length commit SHA is currently the only way to use an action as an immutable release.
- GitHub says repository- and organization-level policies can require actions to be pinned to a full-length commit SHA.
- GitHub recommends OpenID Connect for cloud access so workflow runs can use short-lived, well-scoped tokens instead of long-lived secrets.
- GitHub says GitHub-hosted runners run in ephemeral clean virtual machines, while self-hosted runners do not have the same guarantee.
- GitHub documents ephemeral, just-in-time runners that perform at most one job before being automatically removed.
- GitHub documents audit-log visibility for Actions events and recommends dependency review to understand the security impact of workflow dependency changes in pull requests.

## Research Use

- Gives Topic 04 a concrete delivery-control bundle: immutable workflow dependencies, short-lived cloud credentials, ephemeral runner posture, auditability, and PR-level dependency review.
- Helps connect Topic 04 security controls to Topic 01 merge and release discipline.
- Strengthens the case that delivery blast radius should be reduced before merge and before runtime, not only after deployment.

## Caveats

- GitHub-specific implementation details should not be mistaken for a full cross-platform standard.
- This source gives control primitives, not a unified risk score.
