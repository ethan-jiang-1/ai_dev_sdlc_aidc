# Topic 04 / Ref 16: Microsoft Defender Attack Path Analysis

- source_url: `https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-attack-path`
- source_type: `official Microsoft Learn documentation`
- authority_level: `official implementation guidance`
- publication_time: `2025-11-25 update`
- accessed_on: `2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

This source complements Google’s attack exposure work with another official implementation pattern: graph-based, context-aware prioritization over multicloud attack paths, including AI agents as resources.

## Key Facts Captured

- Microsoft says its cloud security graph collects assets, permissions, lateral movement possibilities, internet exposure, vulnerabilities, and other context into a graph.
- Attack path analysis identifies externally initiated, exploitable paths that lead to critical assets.
- Microsoft highlights risk factors such as internet exposure, permissions, and lateral movement.
- The documentation explicitly says attack path analysis covers resources including unmanaged APIs and AI agents.

## Research Use

- Strengthens Topic 04’s case that blast-radius reasoning will likely be graph- and path-based in production systems.
- Gives a second vendor-implemented example of exposure prioritization grounded in graph context rather than isolated findings.
- Helps bridge security scoring to agent runtime and permission models.

## Caveats

- Like Google’s implementation, this is an exposure model rather than a code-change blast-radius model.
- Proprietary scoring details remain abstract.
