# Topic 04 / Ref 19: GitHub Protected Branches and Deployment Gates

- source_url: `https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches`
- source_type: `official GitHub documentation`
- authority_level: `official implementation guidance`
- publication_time: `live doc; accessed 2026-04-17`
- accessed_on: `2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

This source is important because it makes release-risk admission concrete at merge time. It shows that branch protection can already require reviews, checks, merge-queue validation, and successful deployment to specific environments before merge.

## Key Facts Captured

- GitHub protected branches can require pull-request reviews, status checks, merge queue, and deployments to succeed before merging.
- GitHub says merge queue ensures pull-request changes pass required checks when applied to the latest target branch and any pull requests already in the queue.
- GitHub documents a rule that can require changes to be successfully deployed to specific environments before a branch can be merged.
- GitHub documents branch restrictions so only specific users, teams, or apps can push to protected branches, while still enforcing required checks.

## Research Use

- Strong direct bridge between Topic 01 delivery controls and Topic 04 release-risk gates.
- Supports the claim that release admission can be enforced as a combined quality and security policy, not only as human review.
- Helps define a practical `merge gate -> deploy gate` chain for AI-generated changes.

## Caveats

- This is a merge-control system, not a full blast-radius model.
- It is strongest for repositories already using GitHub-native branching and deployment primitives.
