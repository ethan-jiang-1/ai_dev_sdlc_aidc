# Cline / Continue / Aider 2026 — rule-loading and precedence semantics comparison

- source_url: `https://docs.cline.bot/customization/cline-rules` + `https://docs.cline.bot/enterprise-solutions/configuration/infrastructure-configuration/rules` + `https://docs.continue.dev/customize/rules` + `https://docs.continue.dev/customize/deep-dives/rules` + `https://aider.chat/docs/usage/conventions.html`
- source_type: `official product documentation`
- accessed_at: `2026-04-18`
- related_topic: `06 agent-format (primary), 04 future-trends`
- trust_level: `official`
- tier: `B`
- why_it_matters: Topic 06 已有 OpenSpec direct workflow/config comparison，但仍需区分“同一类 instruction/config artifact 被多工具支持”和“多工具 runtime semantics 一致”。Cline、Continue、Aider 官方文档显示，规则文件的加载位置、优先级、自动应用范围和是否支持 AGENTS.md 的方式并不相同。这直接补强 semantic-consistency gap：跨工具 adoption / comparison 不能被写成 semantic uniformity。
- captured_excerpt: `partial`
- claims_supported: `Official docs for Cline, Continue, and Aider show materially different rule-loading semantics: Cline combines workspace/global rules, supports several rule file types including AGENTS.md, gives workspace rules precedence over global rules, and only recursively searches nested AGENTS.md when a root AGENTS.md exists; Continue joins rules into the system message and applies them in Agent/Chat/Edit with a documented Hub/local/global loading order; Aider convention files are explicitly read into chat via /read or configured read-only files. This supports the claim that cross-tool instruction-file adoption does not imply cross-tool semantic consistency.`
- date_scope: `docs accessed 2026-04-18`
- related_entities: `Cline; Continue; Aider; AGENTS.md; .clinerules; .continue/rules`

## 关键事实

1. Cline 官方文档支持多个规则来源：
   - `.clinerules/`
   - `.cursorrules`
   - `.windsurfrules`
   - `AGENTS.md`
2. Cline 明确说 workspace rules 和 global rules 都会被组合，但 workspace rules 在冲突时优先。
3. Cline enterprise docs 还给出一个关键 AGENTS.md 行为边界：
   - 只有 workspace root 存在顶层 `AGENTS.md` 时，才递归搜索 nested `AGENTS.md`
   - 找到后会把所有 `AGENTS.md` 合并，并用相对路径作为 headers
4. Continue 官方文档把 rules 定位为 Agent / Chat / Edit modes 的 system-message instructions。
5. Continue deep dive 给出明确加载顺序：
   - Hub assistant rules
   - referenced Hub rules
   - local workspace rules from `.continue/rules`
   - global rules from `~/.continue/rules`
6. Aider 官方 docs 则是另一套语义：
   - convention files 通过 `/read CONVENTIONS.md` 或 `aider --read CONVENTIONS.md` 加入 chat
   - 也可用 `.aider.conf.yml` 的 `read:` 字段 always load
   - 这些文件被标为 read-only，并可配合 prompt caching

## 核心内容摘录

### 这条证据补的不是 adoption，而是 semantics

- OpenSpec 已经证明：
  - cross-tool workflow/config comparison exists
  - 同一套 artifact 可以映射到多工具
- 本条证据进一步说明：
  - 即使都叫 rules / instructions / AGENTS.md
  - 各工具实际加载、合并、优先级、触发范围仍不同

### 对最终报告的写法约束

- 可以写：
  - `cross-tool format/workflow adoption is supported`
  - `cross-tool semantic divergence is documented`
- 不应写：
  - `AGENTS.md behaves the same across tools`
  - `rules files are semantically portable without review`

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 06 `agent-format` | 直接支撑 semantic-consistency gap：跨工具规则文件存在明显加载/优先级/作用范围差异 |
| Topic 04 `future-trends` | 支撑 future trend 判断：agent-era spec/config portability 需要 linting、normalization 或 adapter layer |

## 可直接引用的术语 / 概念

- `Workspace rules take precedence`
- `AGENTS.md`
- `.continue/rules`
- `Hub assistant rules`
- `/read CONVENTIONS.md`
- `read-only`

## 风险与局限

1. 这是官方 docs 对照，不是第三方 empirical study。
2. 它证明 semantic divergence / precedence differences 存在，但不量化这些差异造成的 defect rate。
3. Topic 06 因而可以升级为 `semantic-divergence-supported`，但仍不应声称已经有完整 cross-tool conformance suite。

## 交叉引用

- OpenSpec direct comparison：[`06-agent-format-openspec-cross-tool-comparison.md`](06-agent-format-openspec-cross-tool-comparison.md)
- Cline / Cursor / Claude / AGENTS shared baselines：[`00-shared-cursor-rules-official.md`](00-shared-cursor-rules-official.md), [`00-shared-claude-code-official.md`](00-shared-claude-code-official.md), [`00-shared-codex-agents-md-spec.md`](00-shared-codex-agents-md-spec.md)
- Topic 06 evidence summary：[`../_artifacts/06-agent-format-evidence-summary.md`](../_artifacts/06-agent-format-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
