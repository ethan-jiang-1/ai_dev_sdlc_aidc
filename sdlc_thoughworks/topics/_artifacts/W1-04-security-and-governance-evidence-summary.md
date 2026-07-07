# W1-04 Security and Governance Evidence Summary

## Current Thesis

Topic 04 is no longer just “AI security matters.” The current evidence package supports a stronger thesis:

- Agent security is a combined identity, authorization, tooling, protocol, runtime posture, and adversarial-testing problem.
- Zero trust is one of the most useful architectural baselines for agents because agents are effectively new non-human actors operating across distributed resources.
- Governance must include preventive, detective, and release-admission controls, plus continuous drift monitoring and auditability.
- Security risk is not only in model prompts; it is also in protocols, plugins, tokens, privileges, memory, behavior-layer execution, and software-delivery pipelines.
- Delivery-specific blast radius is now concrete enough to model through immutable workflow dependencies, short-lived credentials, protected merge and deploy paths, provenance enforcement, protected environments, and audit trails.

## Evidence Clusters

### 1. Zero trust is the right access baseline

- NIST SP 800-207 removes implicit trust from network location and centers protection on resources and workflows.
- NIST SP 800-207A makes this practical for cloud-native systems by emphasizing service/application identities and granular policy enforcement.
- NIST SP 1800-35 turns that into implementable reference patterns.
- Google WIF best practices add concrete auditability guidance for impersonation and subject mapping.
- SPIFFE/SPIRE and Microsoft Entra Workload ID add concrete examples of workload identity issuance, rotation, projected tokens, and fail-close runtime behavior.

### 2. AI posture and drift need continuous controls

- Google AI Protection frames security across the whole AI lifecycle.
- Google’s Vertex AI protection work shows policy drift detection, posture controls, attack-path simulation, and attack exposure scoring.
- Google’s controls framework makes audit and control monitoring part of AI operations rather than a periodic afterthought.
- Google Risk Engine documents make attack exposure scoring and toxic-combination analysis concrete enough to treat them as a real blast-radius proxy architecture.
- Microsoft Defender shows a parallel graph-based implementation pattern built around permissions, lateral movement, and critical targets.

### 3. Threat taxonomy must include tool and protocol layers

- OWASP LLM Top 10 gives core categories such as prompt injection, insecure output handling, insecure plugin design, and excessive agency.
- OWASP MCP Top 10 adds protocol-specific issues like scope creep, token exposure, and tool poisoning.
- OWASP’s Agentic Applications Top 10 shifts the threat language from LLM misuse to agent behavior and identity abuse.

### 4. Adversarial evaluation must be institutionalized

- MITRE ATLAS provides a living knowledge base of tactics, techniques, and real-world case studies for adversarial AI threats.
- Google AI Protection’s virtual red teaming and attack-path features show how this can become an operational capability.

### 5. Software-delivery incidents prove CI/CD is a high-blast-radius surface

- CircleCI’s January 2023 incident shows a delivery platform can expose customer environment variables, tokens, and keys at ecosystem scale when platform or identity controls fail.
- The incident also shows why static secrets and coarse OAuth scopes are structurally weak delivery defaults.

### 6. Release-risk gates can already be assembled from real platform controls

- GitHub documents immutable action pinning, short-lived OIDC credentials, ephemeral or JIT runner posture, audit logs, and dependency review.
- GitHub protected branches and merge queue show merge admission can require validated checks and successful deployment to specific environments before merge.
- GitHub artifact attestation enforcement shows provenance can become a cluster-admission policy, not just metadata.
- Google Binary Authorization shows deploy-time attestation verification, blocking, audit logging, and continuous validation as one release-control model.
- GitLab protected environments and deployment approvals show higher-tier environment access and approvals can be enforced as platform defaults.

## What Is Confirmed

- Agent security has to be identity- and policy-centric.
- Runtime audit and drift detection are mandatory, not optional extras.
- Tool, protocol, and behavior-layer attack surfaces are now first-order concerns.
- Adversarial testing must be part of the control stack, not a rare special event.
- Non-human identity lifecycle can be implemented with short-lived projected or federated identities plus strong audit chains, rather than long-lived secrets.
- A realistic production proxy for blast radius is graph-based attack exposure over high-value assets and chokepoints, not just isolated issue severity.
- CI/CD and deployment systems are not peripheral delivery tools; they are privileged runtime and secret-bearing surfaces that need first-class blast-radius controls.
- A practical release-risk gate can already be built from immutable dependencies, short-lived credentials, dependency review, protected merge paths, successful deployment checks, provenance enforcement, protected environments, and audit logs.
- Security and delivery controls should be coupled into one release-admission system rather than run as separate lanes.

## What Is Still Missing

- More direct public case studies on agent-specific incidents in software-delivery pipelines.
- More public implementations of diff- or tool-call-specific blast-radius scoring before merge.
- More evidence on how human approvals, provenance enforcement, and deploy-time policy compare in AI-heavy release systems.

## Source Set

- `_reference/04-security-and-governance-01-nist-zero-trust-architecture.md`
- `_reference/04-security-and-governance-02-nist-zero-trust-cloud-native.md`
- `_reference/04-security-and-governance-03-nist-implementing-zta.md`
- `_reference/04-security-and-governance-04-google-ai-protection.md`
- `_reference/04-security-and-governance-05-google-vertex-ai-posture-drift.md`
- `_reference/04-security-and-governance-06-google-ai-controls-framework.md`
- `_reference/04-security-and-governance-07-owasp-llm-top10-2025.md`
- `_reference/04-security-and-governance-08-owasp-mcp-top10.md`
- `_reference/04-security-and-governance-09-mitre-atlas-fact-sheet.md`
- `_reference/04-security-and-governance-10-owasp-agentic-top10-2026.md`
- `_reference/04-security-and-governance-11-google-wif-best-practices.md`
- `_reference/04-security-and-governance-12-spire-svid-lifecycle.md`
- `_reference/04-security-and-governance-13-azure-workload-identity-fail-close.md`
- `_reference/04-security-and-governance-14-google-attack-exposure-scores.md`
- `_reference/04-security-and-governance-15-google-toxic-combinations.md`
- `_reference/04-security-and-governance-16-microsoft-attack-path-analysis.md`
- `_reference/04-security-and-governance-17-circleci-incident-report.md`
- `_reference/04-security-and-governance-18-github-actions-secure-use.md`
- `_reference/04-security-and-governance-19-github-protected-branches-deployment-gate.md`
- `_reference/04-security-and-governance-20-github-artifact-attestations-enforcement.md`
- `_reference/04-security-and-governance-21-google-binary-authorization.md`
- `_reference/04-security-and-governance-22-gitlab-protected-environments.md`
