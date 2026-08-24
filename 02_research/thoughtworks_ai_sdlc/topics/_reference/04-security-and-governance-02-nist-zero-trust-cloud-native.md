# Topic 04 / Ref 02: NIST SP 800-207A Cloud-Native Zero Trust

- source_url: `https://csrc.nist.gov/pubs/sp/800/207/a/final`
- source_type: `official NIST special publication`
- authority_level: `official implementation-oriented framework`
- publication_time: `2023-09-13`
- accessed_on: `2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

This source is especially relevant for agents because it moves from abstract zero trust to application/service identity enforcement in cloud-native systems.

## Key Facts Captured

- SP 800-207A says the key paradigm shift is from network-based controls to identities.
- It requires authentication and authorization policies based on application and service identities in addition to user identities.
- The publication points to API gateways, sidecar proxies, and application identity infrastructure such as SPIFFE as runtime enforcement mechanisms.
- The goal is granular application-level policy enforcement in multi-cloud and hybrid environments.

## Research Use

- Supports Topic 04’s “agent identity” and micro-isolation thesis.
- Helps connect agent security to practical runtime enforcement patterns rather than only high-level principles.

## Caveats

- Focused on cloud-native applications, not explicitly on LLM agents.
- Strong on access control design, weaker on prompt injection and model-specific threat categories.
