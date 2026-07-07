# Topic 02 / Ref 16: Atlassian on Automating Rovo Agents

- source_url: `https://support.atlassian.com/rovo/docs/agents-in-automations/`
- source_type: `official product documentation`
- authority_level: `official implementation guidance`
- publication_time: `current Atlassian support docs, accessed 2026-04-17`
- accessed_on: `2026-04-17`
- topic: `02 organizational-synergy`

## Why This Matters

This source gives the strongest operational answer in the current batch to `what does the middle-loop tool surface actually do`. It shows that agents can be wired into triggers, prompts, secondary actions, app-specific workflows, and permission-scoped automation rules.

## Key Facts Captured

- Atlassian says agents only work autonomously when managed through automation rules owned by existing Jira or Confluence administrators.
- Agents can be triggered either from their own configuration or from an automation rule in Studio.
- The automation model includes a trigger, a `Use Rovo agent` action, a prompt, and a second action that consumes `{{agentResponse}}`.
- Automated agents operate with the permissions of the rule creator, tying autonomy back to administrative and governance boundaries.
- The examples include decision review, work-item organization, and themed analysis pushed into comments or Slack.

## Research Use

- Strong support for the claim that the middle loop includes automation design, prompt templating, admin-owned permissions, and response routing across tools.
- Helps define the operator surface more concretely: triggers, policies, agent selection, prompts, downstream actions, and permission-scoped execution.
- Connects Topic 02 role design with Topic 04 governance, because admin-owned rules and permission inheritance are explicit control points.

## Caveats

- This is a product-specific implementation pattern, not a universal standard.
- It says little about failure cases, staff engineer incentives, or how organizations divide ownership of these controls.
