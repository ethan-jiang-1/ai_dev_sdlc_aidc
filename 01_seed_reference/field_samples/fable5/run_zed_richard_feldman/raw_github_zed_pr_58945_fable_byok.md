# Raw Notes: Zed PR `#58945`

Title:

`Add Claude Fable 5 to Anthropic BYOK`

Public source:

- https://github.com/zed-industries/zed/pull/58945

Key points captured from the PR body and commit summaries:

- `Zed` added support for Anthropic's `Claude Fable 5` when users provide their own Anthropic API key.
- The PR explicitly states that Fable 5 cannot be offered under `Zero Data Retention`, because Anthropic retains inference logs for 30 days.
- To handle that constraint, the product adds:
  - a `telemetry.anthropic_retention` setting, default `false`
  - UI exposure in the Privacy section
  - a hard gate in cloud completion when consent is missing
  - a typed `DataRetentionConsentRequiredError`
- The PR also implements user-facing recovery behavior:
  - if Fable declines a request, the system transparently falls back to `Claude Opus 4.8`
  - the agent panel shows `"Switch to Opus 4.8"` / `"Accept"` actions
  - the failed turn resumes without requiring the user to retype their message

Notable commit summaries:

- `Fable support`
  - adds `send_to_user` tool plus refusal-fallback model support, gated on the Fable model id prefix

- `Gate Claude Fable behind Anthropic data retention consent`
  - adds the privacy setting and runtime consent enforcement
  - makes missing consent a non-retryable typed error
  - adds agent panel recovery actions

Why this raw note matters:

- This is a product integration sample, not just a repo adding another model enum.
- It shows that once Fable 5 enters a user-facing product, privacy policy and fallback UX become first-class engineering concerns.
- It is a strong complement to samples that focus on workflow or agent orchestration because it documents what it takes to safely expose Fable 5 to end users.
