# Umans AI 2025 — practical cross-tool experiment on whether coding agents follow AGENTS.md

- source_url: `https://blog.umans.ai/blog/agent-apply/`
- source_type: `practitioner experiment / engineering blog`
- accessed_at: `2026-04-18`
- related_topic: `06 agent-format (primary), 04 future-trends`
- trust_level: `practitioner`
- tier: `C`
- why_it_matters: Topic 06 当前剩余缺口是 formal cross-tool semantic conformance suite。本文不是正式 conformance suite，也不是学术 benchmark；但它直接把同一真实代码库、同一 `AGENTS.md` / `CLAUDE.md` 规则、同一测试生成任务放到 Codex CLI、Claude Code、Gemini CLI、Cursor 等 agent/scaffolding 中比较，度量 coverage、Given/When/Then compliance、fixture centralization、behavioral assertions 和 self-verification。它适合作为 conformance-adjacent practitioner evidence，说明 repo-level instruction file 是有用 baseline 但不是保证，并且 model + scaffolding 会显著影响规则遵循。
- captured_excerpt: `partial`
- claims_supported: `A 2025 practitioner experiment compared multiple coding-agent setups on one real repository and task using the same repo-level instructions: AGENTS.md for most agents and a CLAUDE.md copy for Claude Code. Configurations included GPT-5.1 Codex-Max / Codex via Codex CLI, Claude Sonnet 4.5 and Opus 4.5 via Claude Code, Gemini 3 Pro via Gemini CLI, and several Cursor setups. The article reports that provider-native tools generally followed more repository rules and self-verified more reliably than Cursor setups, but no configuration fully matched the AGENTS.md testing style. Fixture centralization was the weakest rule: only one Codex-Max high-effort run partially centralized fixtures. This supports a bounded practical claim that AGENTS.md-style files help expose expectations but do not provide formal conformance guarantees.`
- date_scope: `published 2025-11-29; page last-modified 2026-04-07 per HTTP header; accessed 2026-04-18`
- related_entities: `AGENTS.md; CLAUDE.md; Codex CLI; Claude Code; Gemini CLI; Cursor; GPT-5.1 Codex-Max; GPT-5.1 Codex; Claude Sonnet 4.5; Claude Opus 4.5; Gemini 3 Pro`

## 关键事实

1. 文章题目为 `Can coding agents actually follow your codebase's rules?`，页面标题为 `Do coding agents follow AGENTS.md?`。
2. 实验问题是：在一个真实 module 和清晰 `AGENTS.md` 存在时，不同 coding agents 是否会在真实 repo 工作中遵守规则。
3. 实验明确使用：
   - 一个真实 repository
   - 一个真实 `AGENTS.md`
   - 面向 Claude Code 的同内容 `CLAUDE.md`
   - 同一个测试生成任务
4. 目标代码面为两个模块：
   - `bash.py`，143 LOC
   - `edit.py`，288 LOC
   - 合计 431 LOC
5. 每个 agent 的任务相同：为目标 module 添加 tests，并遵守既有 testing style 和 guidelines。
6. 对比配置包括：
   - GPT-5.1 Codex-Max via Codex CLI（high / extra-high effort）
   - GPT-5.1 Codex via Codex CLI（high effort）
   - Claude Sonnet 4.5 / Opus 4.5 via Claude Code（Thinking）
   - Gemini 3 Pro via Gemini CLI
   - Claude Sonnet 4.5 / Gemini 3 Pro / GPT-5.1 Codex via Cursor
7. 实验 pipeline：
   - fresh workspace
   - one non-interactive agent run
   - collect tests touching `bash.py` / `edit.py`
   - run project checks
   - if checks fail, feed one error-feedback loop back to the same agent
   - evaluate final tests
8. 度量维度包括：
   - target module coverage
   - `# Given` / `# When` / `# Then` comment compliance
   - fixture centralization in `conftest.py`
   - behavioral assertions vs implementation internals
   - concision
9. 主要结果边界：
   - provider-native tools（Codex CLI、Claude Code）整体更像 repo 内 collaborator：遵守更多 `AGENTS.md` 规则，也更常自己跑 checks。
   - Cursor 与 Gemini CLI 设置在 convention following 上更弱，尤其是 GWT comments、fixture centralization、self-verification。
   - 没有任何配置完全匹配 `AGENTS.md` 中的 testing style。
10. Codex CLI 结果：
   - three Codex CLI runs were balanced
   - tests were small and readable
   - checks passed on first run
   - coverage roughly in high-70s to low-80s
   - Codex-Max high 是唯一创建 `conftest.py` 的配置，但也只集中化了三份 fixture 中的一份
11. Claude Code 结果：
   - Sonnet 4.5 reached 96.8% coverage but generated a large diff
   - Opus 4.5 reached 95% coverage
   - both followed visible style strongly, but some assertions were tied to internals rather than pure behavior
12. Gemini CLI 结果：
   - Gemini 3 Pro reached about 89% coverage
   - it ignored GWT comment style and did not centralize fixtures
13. Cursor 结果：
   - Cursor Sonnet reached about 90% coverage and used GWT comments, but did not reuse fixtures and needed the outer loop for failing checks
   - Cursor Gemini reached about 90% coverage but ignored GWT and fixtures and did not run project checks itself
   - Cursor Codex matched surface style but only reached about 55% coverage and relied heavily on mocks
14. 作者明确限定：这是一个小型、有观点的实验，基于一个 codebase 和一种任务，不声称 universal model/tool ranking。

## 核心内容摘录

### 这条 evidence 补的 gap

- 它不是 formal semantic conformance suite。
- 它补的是更低层级但更贴近工程现场的事实：
  - same repo rules
  - same task
  - same target codebase
  - multiple model + scaffolding combinations
  - observable instruction-following metrics
- 因而它可以加入 Topic 06 的 `practical-cross-tool-instruction-following-experiment-supported`，但不能消除 `formal-cross-tool-conformance-suite-pending`。

### 对最终报告的写法约束

- 可以写：
  - `AGENTS.md` / `CLAUDE.md` provides a reusable repo-local contract, but it is not a behavior guarantee.
  - Tool scaffolding changes how reliably the same or similar models follow repo-specific rules.
  - Convention-following failures can survive even when coverage and tests look good.
  - Executable checks are a better enforcement path than relying on instruction text alone.
- 不应写：
  - this is a formal conformance suite
  - this proves one model or vendor is universally best
  - all Cursor or Gemini setups are generally weak
  - `AGENTS.md` is ineffective

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 06 `agent-format` | 直接补充 conformance-adjacent practitioner evidence：同一 repo instruction artifact 在不同 agent/scaffolding 下产生不同 compliance 行为 |
| Topic 04 `future-trends` | 支撑 agent-era requirement/context workflow 需要 executable checks、linting、evaluation harness，而不是只把规则写进 Markdown |

## 可直接引用的术语 / 概念

- `AGENTS.md`
- `CLAUDE.md`
- `provider-native tools`
- `model + agent + tooling`
- `fixture centralization`
- `Given / When / Then`
- `quality guardrail`
- `not a full solution`

## 风险与局限

1. 这是 practitioner experiment / company blog，不是同行评审研究。
2. 实验只覆盖一个 repository、一个 task family（test generation）和一组当时可用配置。
3. 文章没有提供完整 formal benchmark harness / machine-readable suite / semantic oracle。
4. 工具和模型版本变化快，2025-11 的相对结果不能直接外推到 2026-04 之后。
5. Topic 06 因而只能升级为 `practical-cross-tool-instruction-following-experiment-supported`；`formal-cross-tool-conformance-suite-pending` 必须保留。

## 交叉引用

- AGENTbench multi-agent evaluation：[`06-agent-format-evaluating-agents-md-agentbench-2026.md`](06-agent-format-evaluating-agents-md-agentbench-2026.md)
- Rule-effect study：[`06-agent-format-rules-shape-or-distort-2026.md`](06-agent-format-rules-shape-or-distort-2026.md)
- Rule-loading semantics comparison：[`06-agent-format-rule-loading-semantics-comparison.md`](06-agent-format-rule-loading-semantics-comparison.md)
- Topic 06 evidence summary：[`../_artifacts/06-agent-format-evidence-summary.md`](../_artifacts/06-agent-format-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
