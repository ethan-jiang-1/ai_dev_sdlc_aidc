# Topic 01 / Ref 12: DORA on Trunk-Based Development

- source_url: `https://dora.dev/capabilities/trunk-based-development/`
- source_type: `official capability guidance`
- authority_level: `official research/practice guidance`
- publication_time: `current DORA capability page, accessed 2026-04-17`
- accessed_on: `2026-04-17`
- topic: `01 engineering-paradigm`

## Why This Matters

This source gives Topic 01 a concrete delivery discipline for keeping AI-generated changes small: short-lived branches, frequent merges, fast automated tests, and no stabilization phases.

## Key Facts Captured

- DORA defines trunk-based development around small batches merged to trunk at least daily, with branches lasting hours rather than days or weeks.
- Continuous integration requires both trunk-based development and fast automated tests after each commit to trunk.
- DORA links high delivery and operational performance to three practices: three or fewer active branches, daily merges to trunk, and no code freezes or integration phases.
- Heavy asynchronous code review is called out as a common obstacle because it encourages developers to batch many changes and makes large changes harder to reason about.
- The measurement table includes active branch count, code freeze periods, merge frequency, and approval time for change requests.

## Research Use

- Converts the `small-batch enforcement` gap into measurable pipeline controls: branch lifetime, active branch count, merge cadence, test-before-merge, and review latency.
- Supports the thesis that AI-generated code must be constrained by delivery topology, not only by model prompting or post-hoc review.
- Connects directly to existing Salesforce evidence about review load and AI-generated PR size.

## Caveats

- DORA guidance is not specifically about agent-generated changes.
- Trunk-based development requires team skill, architecture, and testing maturity; it cannot be dropped into a weak test environment as a standalone fix.
