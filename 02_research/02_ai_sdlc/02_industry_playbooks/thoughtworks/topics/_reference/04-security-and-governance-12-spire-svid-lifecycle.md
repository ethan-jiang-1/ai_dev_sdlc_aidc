# Topic 04 / Ref 12: SPIRE Identity Issuance and Rotation Lifecycle

- source_urls:
  - `https://spiffe.io/docs/latest/spire-about/spire-concepts/`
  - `https://spiffe.io/docs/latest/deploying/configuring/`
  - `https://spiffe.io/docs/latest/deploying/svids/`
- source_type: `official SPIFFE/SPIRE documentation`
- authority_level: `official workload identity documentation`
- publication_time: `live docs; accessed 2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

SPIFFE/SPIRE is one of the clearest public references for workload identity lifecycle in distributed systems. It is especially relevant because agent systems are effectively workload identities with more autonomy.

## Key Facts Captured

- SPIRE documentation walks through the full lifecycle from agent startup and attestation to issuance of an X.509 SVID for a workload.
- The docs state that the server validates the join token and issues an SVID, and that the SVID is rotated automatically as long as the agent maintains a connection.
- SPIFFE Workload API exposes short-lived X.509-SVIDs and trust bundles to workloads so they can authenticate and establish mTLS.
- This is a concrete example of non-human identity lifecycle management using attestation, issuance, rotation, and trust-distribution rather than static credentials.

## Research Use

- Gives Topic 04 a stronger public implementation reference for NHI lifecycle details.
- Helps connect agent identity to workload identity, attestation, short-lived credentials, and automatic rotation.
- Supports the claim that agent identity should be treated as a runtime security substrate rather than an application secret.

## Caveats

- Strong for workload identity lifecycle, but not agent-specific policy or tool-authorization logic.
- More infrastructure-focused than governance-focused.
