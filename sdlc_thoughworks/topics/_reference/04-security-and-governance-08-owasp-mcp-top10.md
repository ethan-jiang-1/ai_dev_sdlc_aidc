# Topic 04 / Ref 08: OWASP MCP Top 10

- source_url: `https://owasp.org/www-project-mcp-top-10/`
- source_type: `official OWASP project page`
- authority_level: `emerging protocol-specific security guidance`
- publication_state: `v0.1 beta`
- accessed_on: `2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

Topic 04 needs protocol-specific threat language for agent tool use. The OWASP MCP Top 10 is one of the clearest current attempts to catalogue that attack surface.

## Key Facts Captured

- The page says MCP risks include model misbinding, context spoofing, prompt-state manipulation, insecure memory references, and covert channel abuse.
- The listed Top 10 includes `Token Mismanagement & Secret Exposure`, `Privilege Escalation via Scope Creep`, and `Tool Poisoning`.
- The project explicitly says these risks are amplified in agentic AI, model chaining, and dynamic role assignment.

## Research Use

- Supports Topic 04’s claim that tool-layer protocols create their own governance and security class, not just generic app-security issues.
- Gives concrete language for agent permission creep, credential handling, and tool supply-chain risk.

## Caveats

- The project is still in beta.
- Useful as an emerging taxonomy, but not yet as mature as long-standing OWASP flagship lists.
