# arXiv 2026 — Large-scale adoption study of coding agents on GitHub

- source_url: `https://arxiv.org/abs/2601.18341`
- source_type: `academic preprint`
- accessed_at: `2026-04-18`
- related_topic: `06 agent-format (primary), 04 future-trends`
- trust_level: `academic`
- tier: `A`
- why_it_matters: Topic 06 在补完 OpenAI internal、Stripe enterprise-internal、OpenWork OSS、Amp/Copilot ecosystem breadth 之后，剩余 gap 之一是“这些现象是否还是少数样本，还是已经体现更广 adoption diversity”。这篇 2026 大样本研究直接分析 128,018 个 GitHub 项目，明确覆盖 Cursor、Claude Code、Codex 等 coding agents，并指出 adoption 跨越 project maturity、established organizations、diverse languages/topics。它不能证明某一种文件格式语义统一，但能强力补强 Topic 06 对“agentic coding 已快速进入实践”的广度判断。
- captured_excerpt: `yes`
- claims_supported: `Coding agents such as Cursor, Claude Code, and Codex had already rapidly transitioned into practice by the first half of 2025; estimated GitHub-project adoption rate is substantial and increasing; adoption spans the full maturity spectrum, includes established organizations, and covers diverse languages/topics; coding-agent-assisted commits tend to be larger and often correspond to features/bug fixes.`
- date_scope: `submitted 2026-01-26; revised 2026-04-08`
- related_entities: `GitHub; Cursor; Claude Code; Codex; coding agents; pull requests; commits`

## 关键事实

1. 论文标题是 `Agentic Much? Adoption of Coding Agents on GitHub`，属于 software engineering 研究。
2. 摘要明确把 `Cursor, Claude Code, or Codex` 作为 coding agents 代表，并把它们与传统 code completion LLM 区分开。
3. 论文声称基于显式 traces（如 co-authored commits / PRs）完成了首个大规模 adoption study，样本规模为 `128,018 projects`。
4. 摘要给出的 adoption estimate 为 `22.20%--28.66%`，并说明这一比例对 only-a-few-months-old technology 来说“very high”且仍在增长。
5. 摘要明确写到 adoption is broad：
   - spans the entire spectrum of project maturity
   - includes established organizations
   - concerns diverse programming languages or project topics
6. 论文还指出 agent-assisted commits 更大，并有较高比例属于 features 和 bug fixes。

## 核心内容摘录

### 这不是单个工具厂商或单个企业案例

- 与 OpenAI、Stripe、Amp、GitHub Copilot 这类单点案例不同，这篇研究试图从 GitHub traces 观察更广 adoption picture。
- 因而它更适合补 Topic 06 的“diversity / breadth”层，而不是某个工具的产品细节层。

### 与 Topic 06 的最直接关系

- 这条证据不能说明 `AGENTS.md`、`CLAUDE.md`、`.cursor/rules` 哪个语义最优。
- 但它能更稳地支持：
  - coding agents 已快速进入实践
  - adoption 不只发生在少数早期试验者
  - established organizations 也已卷入

### 如何正确使用这条证据

- 它适合强化 adoption breadth / diversity。
- 不适合拿来证明：
  - 某个 agent 文件格式是标准
  - 某个工具一定更优
  - agent-generated PR 的质量已经无条件可靠

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 06 `agent-format` | 补强 broader diversity：coding-agent adoption 已跨越 project maturity、established organizations、diverse languages/topics，不再只是若干 vendor/company 个案 |
| Topic 04 `future-trends` | 支撑“agentic coding 已快速进入实践”的 wider trend signal |

## 可直接引用的术语 / 概念

- `Cursor, Claude Code, or Codex`
- `128,018 projects`
- `22.20%--28.66%`
- `adoption is broad`
- `established organizations`
- `diverse programming languages or project topics`

## 风险与局限

1. 这是 adoption study，不是 config-file / workflow-file 的直接比较研究。
2. 它强化的是 adoption breadth，而不是 semantic uniformity 或 format choice。
3. 作为 preprint，应避免把其中数字写成最终定论；更稳的做法是用来支撑“rapid and broad adoption signal”。

## 交叉引用

- Topic 06 evidence summary：[`../_artifacts/06-agent-format-evidence-summary.md`](../_artifacts/06-agent-format-evidence-summary.md)
- Stripe enterprise case：[`06-agent-format-stripe-minions-enterprise-usage.md`](06-agent-format-stripe-minions-enterprise-usage.md)
- OpenAI internal case：[`06-agent-format-openai-codex-adoption.md`](06-agent-format-openai-codex-adoption.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
