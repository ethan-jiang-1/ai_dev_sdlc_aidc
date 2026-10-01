# Topic 04 / Ref 20: GitHub Artifact Attestations and Admission Enforcement

- source_url: `https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/enforce-artifact-attestations`
- source_type: `official GitHub documentation`
- authority_level: `official implementation guidance`
- publication_time: `live doc; accessed 2026-04-17`
- accessed_on: `2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

This source shows a concrete path from build provenance to deploy-time admission control. It is one of the clearest public examples of turning artifact provenance into an enforced release gate.

## Key Facts Captured

- GitHub documents artifact attestations as a way to establish build provenance for produced software.
- GitHub says the Kubernetes admission-controller path requires build provenance for container images, including `push-to-registry`, so the policy controller can verify the attestation.
- The documented setup deploys Sigstore Policy Controller, adds GitHub TrustRoot and a `ClusterImagePolicy`, and then enables enforcement per namespace.
- GitHub says the resulting policy rejects artifacts that have not originated from within the configured GitHub organization.
- The policy can be narrowed to specific image patterns and exemptions, which makes release-admission scope explicit.

## Research Use

- Strong evidence that provenance can become an enforceable deployment condition instead of a passive metadata record.
- Helps Topic 04 move from generic supply-chain talk to implementation-grade admission policy.
- Connects Topic 01 release slicing to Topic 04 provenance enforcement at cluster entry.

## Caveats

- Container and Kubernetes oriented; it does not directly solve arbitrary code-diff or tool-call risk.
- Enforcement depends on the surrounding Sigstore and cluster-policy stack.
