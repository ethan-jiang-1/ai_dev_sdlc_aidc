# Topic 01 / Ref 14: Google SRE on Canarying Releases

- source_url: `https://sre.google/workbook/canarying-releases/`
- source_type: `official SRE workbook chapter`
- authority_level: `primary practitioner guidance`
- publication_time: `2018 SRE workbook chapter`
- accessed_on: `2026-04-17`
- topic: `01 engineering-paradigm`

## Why This Matters

This source strengthens the release-slicing side of Topic 01. It shows how production exposure can be staged, evaluated, and rolled back instead of treating deployment as an all-or-nothing event.

## Key Facts Captured

- Feature flags or experiment frameworks can separate feature launch from binary release, preventing many changes from being released as one indivisible event.
- Canarying deploys a candidate to a subset of traffic and compares it with a control before broad rollout.
- Canarying requires a way to deploy to a subset, an evaluation process, and integration of the evaluation into the release process.
- Risk to SLOs and error budget is proportional to the exposed traffic fraction and exposure time.
- Gradual canaries support staged metric selection, starting with clear problem signals such as crashes or request failures before broader confidence is assumed.

## Research Use

- Supports a concrete answer to `release slicing`: separate merge, binary release, feature exposure, and production traffic rollout.
- Provides a practical complement to DORA small-batch and trunk-based development: even after small merges, production impact should be progressively exposed.
- Helps frame AI-native safe shipment as a multi-stage control system rather than one final human approval.

## Caveats

- The SRE workbook predates the current agentic coding wave and is not AI-specific.
- Canarying only reduces production exposure risk; it does not solve specification errors, security policy violations, or hidden data-impact risks by itself.
