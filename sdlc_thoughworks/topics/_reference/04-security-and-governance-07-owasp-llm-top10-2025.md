# Topic 04 / Ref 07: OWASP Top 10 for LLM Applications 2025

- source_urls:
  - `https://owasp.org/www-project-top-10-for-large-language-model-applications/`
  - `https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf`
- source_type: `official OWASP security guidance`
- authority_level: `community flagship security guidance`
- publication_time: `2025`
- accessed_on: `2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

This is the most widely recognized community security taxonomy for LLM application risks. It is directly relevant to Topic 04 because it names the failure modes that make “unchecked agent autonomy” dangerous.

## Key Facts Captured

- The project has grown into the OWASP GenAI Security Project, indicating sustained community investment.
- The Top 10 includes `Prompt Injection`, `Insecure Output Handling`, `Insecure Plugin Design`, and `Excessive Agency`.
- These are especially relevant for agent systems that route through tools and act on external systems.
- The taxonomy helps distinguish model risk from application and orchestration risk.

## Research Use

- Supports Topic 04’s threat-language layer.
- Useful as a shared vocabulary for evaluating why certain agent permissions, integrations, and output paths are unsafe.

## Caveats

- Community guidance, not a formal standard.
- Best used with NIST and system-specific runtime sources.
