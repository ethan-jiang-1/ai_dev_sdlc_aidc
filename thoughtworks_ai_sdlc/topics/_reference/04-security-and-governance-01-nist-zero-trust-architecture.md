# Topic 04 / Ref 01: NIST SP 800-207 Zero Trust Architecture

- source_url: `https://csrc.nist.gov/pubs/sp/800/207/final`
- source_type: `official NIST special publication`
- authority_level: `official security framework`
- publication_time: `2020-08-11`
- accessed_on: `2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

Topic 04 needs a principled security baseline for agents acting on enterprise resources. NIST SP 800-207 provides that baseline by shifting protection from network location to users, assets, services, and workflows.

## Key Facts Captured

- Zero trust removes implicit trust based on network location or ownership.
- Authentication and authorization are discrete functions performed before a session is established.
- The framework focuses on protecting resources and workflows rather than perimeter segments.
- This is highly relevant to agent systems because agents are effectively new actors touching enterprise resources across clouds, tools, and environments.

## Research Use

- Supports Topic 04’s claim that agent access should be identity- and policy-centric rather than environment-trusting.
- Provides a canonical baseline for dynamic permission and access-gate discussions.

## Caveats

- The document is generic ZTA guidance, not agent-specific implementation guidance.
- It should be paired with more specific agent/tool threat sources.
