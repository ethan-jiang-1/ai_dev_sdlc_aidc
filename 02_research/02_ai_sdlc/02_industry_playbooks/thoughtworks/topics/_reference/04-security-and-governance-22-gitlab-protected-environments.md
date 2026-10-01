# Topic 04 / Ref 22: GitLab Protected Environments and Deployment Approvals

- source_url: `https://docs.gitlab.com/ci/environments/protected_environments/`
- source_type: `official GitLab documentation`
- authority_level: `official implementation guidance`
- publication_time: `live doc; accessed 2026-04-17`
- accessed_on: `2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

This source shows an enterprise-ready deployment-control pattern where environment access, approval rules, and operator-developer separation are explicit platform features. It is a direct example of delivery-specific blast-radius containment by environment tier.

## Key Facts Captured

- GitLab protected environments restrict who can deploy to specific environments and can define approvers and approval rules before deployment.
- GitLab supports deployment-only access, where a group can deploy to a protected environment without having push or merge access to the production branch.
- GitLab documents group-level protected environments to enforce an explicit developer/operator boundary across higher environments such as staging and production.
- When both group-level and project-level environment configurations exist, GitLab says a user must be allowed in both rulesets to run a deployment job.
- GitLab documents project audit events for deployment approval history.

## Research Use

- Gives Topic 04 a concrete protected-environment and approval model for production release gating.
- Supports the claim that release-risk controls should be tier-aware and environment-aware, not only repo-aware.
- Helps connect software-delivery governance to organizational permission boundaries.

## Caveats

- Approval- and access-centric rather than algorithmic risk scoring.
- GitLab-specific environment model may not map one-to-one onto every enterprise release stack.
