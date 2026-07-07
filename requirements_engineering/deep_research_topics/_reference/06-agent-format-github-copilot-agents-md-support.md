# GitHub 2025–2026 — Copilot coding agent support for AGENTS.md and nested instructions

- source_url: `https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/` + `https://github.blog/changelog/2026-03-11-major-agentic-capabilities-improvements-in-github-copilot-for-jetbrains-ides/`
- source_type: `official product changelog`
- accessed_at: `2026-04-18`
- related_topic: `06 agent-format (primary), 04 future-trends`
- trust_level: `official`
- tier: `B`
- why_it_matters: Topic 06 的 adoption gap 目前已从“OpenAI/Amp vendor-only”收窄到“public OSS usage + vendor support”，但还可以继续收窄 cross-tool ecosystem breadth。GitHub 官方 changelog 直接确认 Copilot coding agent 和 JetBrains agent capabilities 都支持 `AGENTS.md`，包括 nested `AGENTS.md`。这进一步证明 AGENTS.md 已经跨出 OpenAI / Amp / OSS 单点，进入另一家主流 coding-agent 平台的正式支持面。
- captured_excerpt: `yes`
- claims_supported: `GitHub Copilot coding agent supports root AGENTS.md custom instructions; nested AGENTS.md files are supported; GitHub also continues to support CLAUDE.md and other instruction formats; JetBrains-side GitHub Copilot agent settings also surface AGENTS.md and nested AGENTS.md support.`
- date_scope: `2025-08-28 and 2026-03-11`
- related_entities: `GitHub Copilot coding agent; AGENTS.md; nested AGENTS.md; CLAUDE.md; JetBrains`

## 关键事实

1. GitHub changelog 2025-08-28 明确写道：`Copilot coding agent now supports AGENTS.md custom instructions`。
2. 同文说明：
   - can create a single `AGENTS.md` in repo root
   - can also create nested `AGENTS.md` files for specific parts of the project
3. 同文还说明 Copilot coding agent continues to support:
   - `.github/copilot-instructions.md`
   - `.github/instructions/**.instructions.md`
   - `CLAUDE.md`
   - `GEMINI.md`
4. 2026-03-11 GitHub changelog 进一步说明 JetBrains IDE agent capabilities 中也可启用 support for nested `AGENTS.md` and `CLAUDE.md`。

## 核心内容摘录

### GitHub 正式支持 AGENTS.md

- 这不再只是 OpenAI / Amp / agents.md 社区站点的叙事。
- GitHub 自身的 coding agent 已把 `AGENTS.md` 纳入正式 instruction file support。

### 与 Topic 06 的关系

- 这条证据不证明 enterprise-internal usage。
- 但它进一步证明：
  - `AGENTS.md` 是 cross-tool ecosystem signal
  - nested `AGENTS.md` supports scoped layering

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 06 `agent-format` | 补强 cross-tool support breadth：AGENTS.md 现已被 GitHub Copilot coding agent 正式支持 |
| Topic 04 `future-trends` | 支撑 repo contract / scoped instruction layering 正在被主流 tooling 内建吸收 |

## 可直接引用的术语 / 概念

- `supports AGENTS.md custom instructions`
- `nested AGENTS.md`
- `CLAUDE.md`
- `custom instructions`

## 风险与局限

1. 这仍是 tool support，不是 enterprise-internal usage case。
2. 它强化的是 ecosystem breadth，而不是 behavior uniformity 或企业 adoption outcome。

## 交叉引用

- Topic 06 evidence summary：[`../_artifacts/06-agent-format-evidence-summary.md`](../_artifacts/06-agent-format-evidence-summary.md)
- OpenWork OSS usage：[`06-agent-format-openwork-oss-usage.md`](06-agent-format-openwork-oss-usage.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
