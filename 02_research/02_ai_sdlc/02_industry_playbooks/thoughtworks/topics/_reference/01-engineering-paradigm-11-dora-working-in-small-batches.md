# Topic 01 / Ref 11: DORA on Working in Small Batches

- source_url: `https://dora.dev/capabilities/working-in-small-batches/`
- source_type: `official capability guidance`
- authority_level: `official research/practice guidance`
- publication_time: `last updated 2025-12-08`
- accessed_on: `2026-04-17`
- topic: `01 engineering-paradigm`

## Why This Matters

This source directly addresses the Topic 01 gap around mechanical resistance to the AI-driven `big batch trap`. It gives a practical definition of small-batch work and connects the practice to continuous integration and trunk-based development.

## Key Facts Captured

- DORA frames small batches as work that can be completed in hours and tested or deployed rapidly.
- The page warns against slicing work locally and then regrouping it before downstream testing or release, because that delays defect and user-feedback signals.
- DORA treats small batches as a necessary condition for both continuous integration and trunk-based development.
- Measurement guidance includes release cadence, feature slicing, whether features can be completed in a week or less, and whether teams can commit and release before the whole feature is complete.

## Research Use

- Supports the claim that AI-native pipelines need batch-size instrumentation, not just exhortations to keep PRs small.
- Provides a measurement vocabulary for release slicing: hours-scale work, release cadence, one-week-or-less feature slices, MVP decomposition, and ability to release partial features safely.
- Strengthens the Topic 01 answer to `how to mechanically prevent AI from recreating low-frequency big-batch delivery`.

## Caveats

- This is general delivery capability guidance, not AI-specific pipeline evidence.
- It does not prescribe one concrete implementation mechanism, so it should be combined with branch protection, merge queue, CI, canary, and feature-flag controls.
