# Topic 01 / Ref 07: Salesforce on Scaling Code Reviews Under AI Load

- source_url: `https://engineering.salesforce.com/scaling-code-reviews-adapting-to-a-surge-in-ai-generated-code/`
- source_type: `official engineering practice article`
- authority_level: `primary practitioner source`
- publication_time: `2026-01-29`
- accessed_on: `2026-04-17`
- topic: `01 engineering-paradigm`

## Why This Matters

This source directly validates the Topic 01 concern that human code review stops scaling once AI changes the economics of code production.

## Key Facts Captured

- Salesforce reports that AI-assisted development increased code volume and expanded pull requests beyond sizes where human review remained effective.
- Review latency increased even as time-to-code fell.
- The article explicitly says the deeper problem was the erosion of the `second-pair-of-eyes guarantee`.
- It identifies predictable failure modes for large AI-generated PRs: loss of conceptual coherence, non-linear cognitive load, and degraded reviewer engagement.

## Research Use

- Strong real-world support for the claim that code review is no longer the main reliable quality firewall.
- Supports Topic 01’s argument for smaller slices, better intent reconstruction, and stronger pre-review validation.
- Supplies a concrete failure-mode source for the `big batch trap`.

## Caveats

- This is one company’s engineering account, though at meaningful scale.
- It is about review-system redesign, not a general proof that review can be removed everywhere.
