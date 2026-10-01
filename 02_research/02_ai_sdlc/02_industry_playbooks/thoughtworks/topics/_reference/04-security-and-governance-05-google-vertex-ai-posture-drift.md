# Topic 04 / Ref 05: Google Security Command Center for Vertex AI

- source_url: `https://cloud.google.com/blog/products/identity-security/introducing-security-command-center-protection-for-vertex-ai/`
- source_type: `official product/security architecture article`
- authority_level: `primary practitioner source`
- publication_time: `2024-02-27`
- accessed_on: `2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

This source matters because it makes drift detection and blast-radius reasoning concrete for AI workloads.

## Key Facts Captured

- Google recommends starting with organization policies as centrally defined guardrails for AI resources.
- Security Command Center provides near real-time detection of changes to policies and AI resource configurations.
- It offers continuous monitoring to detect when AI infrastructure drifts from best practices.
- Google also describes attack path simulation and attack exposure scoring for prioritizing remediation.

## Research Use

- Supports Topic 04’s interest in blast-radius estimation and pre-merge/posture risk scoring.
- Gives a practical example of preventive plus detective controls for AI infrastructure.

## Caveats

- Cloud-vendor-specific implementation.
- It focuses on AI infrastructure posture more than application-layer agent behavior.
