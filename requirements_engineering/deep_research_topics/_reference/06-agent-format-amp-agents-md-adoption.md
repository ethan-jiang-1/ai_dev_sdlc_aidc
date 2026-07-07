# Amp / Sourcegraph 2025 — From AGENT.md to AGENTS.md

- source_url: `https://ampcode.com/news/AGENT.md` + `https://ampcode.com/news/AGENTS.md`
- source_type: `official product news / adopter-format case`
- accessed_at: `2026-04-18`
- related_topic: `06 agent-format (primary), 04 future-trends`
- trust_level: `official`
- tier: `B`
- why_it_matters: 这是 Topic 06 缺少的非 OpenAI adopter/format case。Amp 先推出 `AGENT.md`，随后公开切换到 `AGENTS.md`，直接说明跨工具标准化压力已经影响真实工具的文件命名与兼容策略。
- captured_excerpt: `yes`
- claims_supported: Amp originally supported root `AGENT.md` for project structure, build/test steps, conventions, and common mistakes; Amp could generate it from existing agent-specific files such as `.cursorrules`, `.cursor/rules`, `.windsurfrules`, `.clinerules`, `CLAUDE.md`, and `.github/copilot-instructions.md`; Amp later switched to `AGENTS.md` while retaining backward compatibility with `AGENT.md`; stated motivation was preferring one standard and avoiding proliferation of agent-specific files.
- date_scope: `AGENT.md support announced 2025-05-07; AGENTS.md switch announced 2025-08-20`
- related_entities: `Amp; Sourcegraph; AGENT.md; AGENTS.md; Claude Code; Cursor; Cline; Windsurf; GitHub Copilot`

## 关键事实

1. Amp 2025-05-07 announcement states Amp looks in root `AGENT.md` for:
   - project structure
   - build & test steps
   - conventions
   - avoiding common mistakes
2. The same post says Amp can generate `AGENT.md` by reading the project and existing agent files:
   - `.cursorrules`
   - `.cursor/rules`
   - `.windsurfrules`
   - `.clinerules`
   - `CLAUDE.md`
   - `.github/copilot-instructions.md`
3. The post explicitly says Amp chose `AGENT.md` as a naming standard to avoid proliferation of agent-specific files.
4. Amp 2025-08-20 follow-up says OpenAI picked `AGENTS.md`, and Amp decided it would prefer one standard.
5. As of that announcement, Amp looks for `AGENTS.md` files while staying backward compatible with existing `AGENT.md` files.

## 核心内容摘录

### AGENT.md 初始动机

- Amp says root `AGENT.md` is for project guidance around structure, build/test steps, conventions, and common mistakes.
- Amp also says it chose a naming standard to avoid proliferation of agent-specific files.

### 切换到 AGENTS.md

- Amp says OpenAI picked `AGENTS.md`.
- Amp's condition was that if OpenAI could get the agents.md domain, Amp would switch.
- Amp then switched to `AGENTS.md`, keeping backward compatibility with `AGENT.md`.

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 06 `agent-format` | 非 OpenAI 官方 case，证明 `AGENTS.md` 不是 OpenAI 单方自述，而是其他 agent tool 为避免 fragmentation 主动对齐 |
| Topic 04 `future-trends` | 支撑 agent-era format standardization 是正在发生的工具链趋势 |

## 可直接引用的术语 / 概念

- `AGENT.md`
- `AGENTS.md`
- `one standard`
- `avoid the proliferation of agent-specific files`
- backward compatibility

## 风险与局限

1. 这是工具厂商自身新闻，不是企业采用效果案例。
2. 它强力支撑 format-convergence / naming-convention adoption，不直接证明 `AGENTS.md` 的语义在不同工具中完全一致。
3. 它应与 OpenAI / agents.md shared baseline 一起使用，支撑“cross-tool adoption candidate”，而不是“fully uniform semantic standard”。

## 交叉引用

- Topic 06 evidence summary：[`../_artifacts/06-agent-format-evidence-summary.md`](../_artifacts/06-agent-format-evidence-summary.md)
- shared AGENTS baseline：[`00-shared-codex-agents-md-spec.md`](00-shared-codex-agents-md-spec.md)
- W2 claims audit：[`../_artifacts/W2-claims-audit-v2.md`](../_artifacts/W2-claims-audit-v2.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
