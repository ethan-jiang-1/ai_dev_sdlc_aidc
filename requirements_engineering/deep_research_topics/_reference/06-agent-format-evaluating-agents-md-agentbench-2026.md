# Gloaguen et al. 2026 — Evaluating AGENTS.md and AGENTbench multi-agent context-file evaluation

- source_url: `https://arxiv.org/abs/2602.11988` + `https://arxiv.org/html/2602.11988` + `https://github.com/eth-sri/agentbench`
- source_type: `academic preprint + open benchmark/code repository`
- accessed_at: `2026-04-18`
- related_topic: `06 agent-format (primary), 04 future-trends`
- trust_level: `academic`
- tier: `A`
- why_it_matters: Topic 06 当前缺口是 cross-tool conformance suite / multi-tool replication。本文不是正式语义一致性 conformance suite，但它比既有单工具 rule-effect study 更直接：围绕 `AGENTS.md` / `CLAUDE.md` 等 repository-level context files，构造 AGENTbench，并在多个 coding agents 与 LLMs 上比较 no-context、LLM-generated context、developer-provided context 三类设置。这足以把 Topic 06 从单 agent rule-effect evidence 推进到 multi-agent context-file evaluation / replication evidence，同时仍保留 formal conformance-suite pending。
- captured_excerpt: `yes`
- claims_supported: `A 2026 academic preprint evaluates repository-level context files such as AGENTS.md across Claude Code, Codex, and Qwen Code, paired with Sonnet-4.5, GPT-5.2, GPT-5.1 mini, and Qwen3-30b-coder. It uses SWE-bench Lite plus a new AGENTbench dataset of 138 instances from 12 repositories with developer-written context files, and compares no-context, LLM-generated context, and human-written context settings. The study reports that LLM-generated context files tend to reduce success while increasing cost, developer-written files only marginally improve success while also increasing cost, and agents generally follow instructions but explore/test more. This supports multi-agent context-file evaluation evidence and reinforces concise, minimal repository context, while not proving cross-tool semantic conformance.`
- date_scope: `submitted 2026-02-12; arXiv HTML generated 2026-02-26; accessed 2026-04-18`
- related_entities: `AGENTS.md; CLAUDE.md; AGENTbench; SWE-bench Lite; Claude Code; Codex; Qwen Code; Sonnet-4.5; GPT-5.2; GPT-5.1 mini; Qwen3-30b-coder`

## 关键事实

1. 论文题目是 `Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?`。
2. 研究对象直接包括 repository-level context files：
   - `AGENTS.md`
   - `CLAUDE.md`
   - agent-generated context files
   - developer-committed context files
3. 论文把评估分成两个互补设置：
   - SWE-bench Lite popular repositories + LLM-generated context files
   - AGENTbench less-popular repositories + developer-committed context files
4. AGENTbench 是新构造的 benchmark：
   - 138 unique instances
   - 12 recent / niche repositories
   - all feature developer-written context files
5. 实验覆盖多个 coding agents / harnesses：
   - Claude Code + Sonnet-4.5
   - Codex + GPT-5.2
   - Codex + GPT-5.1 mini
   - Qwen Code + Qwen3-30b-coder
6. 对 Codex 与 Qwen Code，context file 写入 `AGENTS.md`；对 Claude Code，写入 `CLAUDE.md`。
7. 实验设置包括：
   - `None`：无 context file
   - `LLM`：按各 agent 推荐初始化命令生成 context file
   - `Human`：使用开发者提交的 context file（AGENTbench only）
8. 主要结果：
   - LLM-generated context files 在 8 个设置中的 5 个降低成功率
   - 平均 resolution rate 在 SWE-bench Lite 降低约 0.5%，在 AGENTbench 降低约 2%
   - LLM-generated context files 分别带来约 20% / 23% 的成本增加
   - developer-provided context files 相比无 context file 平均只带来约 4% 成功率提升，但也增加步骤数与成本
   - context files 会引导更广泛探索、测试与推理，agents 通常会遵守 instructions
9. 作者的实践结论是：human-written context files should describe only minimal requirements；暂不建议无差别使用 LLM-generated context files。
10. 作者公开了生成 AGENTbench instances 与评估 coding agents 的代码：`https://github.com/eth-sri/agentbench`。

## 核心内容摘录

### 这条证据补的 gap

- 之前 Topic 06 已有：
  - OpenSpec direct workflow/config comparison
  - Cline / Continue / Aider rule-loading semantic differences
  - Zhang et al. 2026 single-study rule-effect/failure evaluation
- 本文进一步提供：
  - multi-agent / multi-LLM evaluation
  - repository-level context-file settings
  - developer-written vs LLM-generated context comparison
  - benchmark/code availability

### 对最终报告的写法约束

- 可以写：
  - repository-level context files have now been evaluated across multiple coding agents and LLMs
  - LLM-generated context files are not reliably beneficial and can increase cost
  - developer-written files appear only marginally beneficial on average and should stay minimal
  - agents tend to follow context-file instructions, so unnecessary requirements can still shape behavior and add cost
- 不应写：
  - AGENTS.md / CLAUDE.md have a formal conformance suite
  - all tools interpret context files identically
  - context files are useless in all cases
  - developer-provided context files always hurt

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 06 `agent-format` | 直接补强 multi-tool / multi-agent context-file evaluation：context files 的效果已跨 Claude Code / Codex / Qwen Code 与多个 LLM 设置被测试 |
| Topic 04 `future-trends` | 支撑 future trend 判断：agent-era spec/context workflow 需要简洁、任务相关、可评估，而不是无边界堆上下文 |

## 可直接引用的术语 / 概念

- `AGENTbench`
- `138 unique instances`
- `12 repositories`
- `SWE-bench Lite`
- `Claude Code`
- `Codex`
- `Qwen Code`
- `AGENTS.md`
- `CLAUDE.md`
- `over 20%`
- `minimal requirements`

## 风险与局限

1. 这是 arXiv preprint，仍需同行评审与独立复现。
2. 它是 context-file effect evaluation，不是正式 cross-tool semantic conformance suite。
3. 研究主要围绕 Python repositories / SWE-bench-style tasks，不能直接外推到所有企业、所有语言和所有 requirement workflow。
4. Topic 06 因而可以升级为 `multi-agent-context-file-evaluation-supported`，但仍应保留 `formal-cross-tool-conformance-suite-pending`。

## 交叉引用

- Rule-effect study：[`06-agent-format-rules-shape-or-distort-2026.md`](06-agent-format-rules-shape-or-distort-2026.md)
- Rule-loading semantics comparison：[`06-agent-format-rule-loading-semantics-comparison.md`](06-agent-format-rule-loading-semantics-comparison.md)
- OpenSpec direct comparison：[`06-agent-format-openspec-cross-tool-comparison.md`](06-agent-format-openspec-cross-tool-comparison.md)
- Topic 06 evidence summary：[`../_artifacts/06-agent-format-evidence-summary.md`](../_artifacts/06-agent-format-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
