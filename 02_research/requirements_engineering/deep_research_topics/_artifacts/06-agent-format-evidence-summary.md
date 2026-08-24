# 06 — agent-format — Evidence Summary

- scope: `Wave 1 starter pack plus selected high-value adoption upgrades for Topic 06`
- status: `closed_for_current_round`
- last_updated: `2026-04-18`
- related_references:
  - [`../_reference/06-agent-format-openai-codex-adoption.md`](../_reference/06-agent-format-openai-codex-adoption.md)
  - [`../_reference/06-agent-format-openai-harness-engineering.md`](../_reference/06-agent-format-openai-harness-engineering.md)
  - [`../_reference/06-agent-format-github-spec-kit-official.md`](../_reference/06-agent-format-github-spec-kit-official.md)
  - [`../_reference/06-agent-format-github-copilot-agents-md-support.md`](../_reference/06-agent-format-github-copilot-agents-md-support.md)
  - [`../_reference/06-agent-format-kiro-spec-workflow-official.md`](../_reference/06-agent-format-kiro-spec-workflow-official.md)
  - [`../_reference/06-agent-format-amp-agents-md-adoption.md`](../_reference/06-agent-format-amp-agents-md-adoption.md)
  - [`../_reference/06-agent-format-openwork-oss-usage.md`](../_reference/06-agent-format-openwork-oss-usage.md)
  - [`../_reference/06-agent-format-stripe-minions-enterprise-usage.md`](../_reference/06-agent-format-stripe-minions-enterprise-usage.md)
  - [`../_reference/06-agent-format-github-adoption-study-2026.md`](../_reference/06-agent-format-github-adoption-study-2026.md)
  - [`../_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md`](../_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md)
  - [`../_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md`](../_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md)
  - [`../_reference/06-agent-format-umans-agents-md-following-experiment.md`](../_reference/06-agent-format-umans-agents-md-following-experiment.md)
  - [`../_reference/06-agent-format-openspec-cross-tool-comparison.md`](../_reference/06-agent-format-openspec-cross-tool-comparison.md)
  - [`../_reference/06-agent-format-rule-loading-semantics-comparison.md`](../_reference/06-agent-format-rule-loading-semantics-comparison.md)
  - [`../_reference/06-agent-format-rules-shape-or-distort-2026.md`](../_reference/06-agent-format-rules-shape-or-distort-2026.md)
  - [`../_reference/00-shared-cursor-rules-official.md`](../_reference/00-shared-cursor-rules-official.md)
  - [`../_reference/00-shared-claude-code-official.md`](../_reference/00-shared-claude-code-official.md)
  - [`../_reference/00-shared-codex-agents-md-spec.md`](../_reference/00-shared-codex-agents-md-spec.md)

## 本轮已落地证据

1. adopter case：
   - [`../_reference/06-agent-format-openai-codex-adoption.md`](../_reference/06-agent-format-openai-codex-adoption.md) 证明 OpenAI 内部真实使用中，工程师会把 `user request or spec` 直接交给 Codex 生成 rough draft，并把 background PR work 当作正常工作方式。
   - [`../_reference/06-agent-format-amp-agents-md-adoption.md`](../_reference/06-agent-format-amp-agents-md-adoption.md) 证明非 OpenAI 工具 Amp 先支持 `AGENT.md`，后主动切换到 `AGENTS.md`，以减少 agent-specific 文件碎片化。
   - [`../_reference/06-agent-format-stripe-minions-enterprise-usage.md`](../_reference/06-agent-format-stripe-minions-enterprise-usage.md) 证明非工具厂商企业内部也已公开采用 unattended coding agents；Stripe 还明确披露其自研 harness 复用与 Cursor / Claude Code 相同的 rule files，并以子目录条件加载规则。
2. 失败模式 / 机制：
   - [`../_reference/06-agent-format-openai-harness-engineering.md`](../_reference/06-agent-format-openai-harness-engineering.md) 明确记录 `one big AGENTS.md` 失败，以及 `AGENTS.md -> docs/ -> plans` 的分层替代方案。
3. feature-level workflow：
   - [`../_reference/06-agent-format-github-spec-kit-official.md`](../_reference/06-agent-format-github-spec-kit-official.md) 给出 `constitution -> spec -> plan -> tasks -> implement` 链条。
   - [`../_reference/06-agent-format-kiro-spec-workflow-official.md`](../_reference/06-agent-format-kiro-spec-workflow-official.md) 给出 `requirements -> design -> tasks` 链条，并明确 requirements phase 使用 EARS。
4. direct cross-tool comparison：
   - [`../_reference/06-agent-format-openspec-cross-tool-comparison.md`](../_reference/06-agent-format-openspec-cross-tool-comparison.md) 直接把同一套 spec workflow 映射到 25+ agent tools，并在官方 README 里显式对比 `vs. Spec Kit` 与 `vs. Kiro`，把 Topic 06 从“并列读取多份单工具文档”推进到“已有一份官方 cross-tool workflow/config comparison anchor”。
5. semantic consistency / precedence comparison：
   - [`../_reference/06-agent-format-rule-loading-semantics-comparison.md`](../_reference/06-agent-format-rule-loading-semantics-comparison.md) 直接对照 Cline、Continue、Aider 官方规则加载语义，证明跨工具 rule/instruction adoption 不等于加载顺序、优先级、自动应用范围一致。
6. rule-effect / failure evidence：
   - [`../_reference/06-agent-format-rules-shape-or-distort-2026.md`](../_reference/06-agent-format-rules-shape-or-distort-2026.md) 用 679 个规则文件、25,532 条 rules、5,000+ agent runs 直接评估 agent rule files 的收益与损害，证明规则文件不是“越多越好 / 越专家越好”，negative constraints 更安全，positive directives 可能 actively hurt。
7. public OSS usage：
   - [`../_reference/06-agent-format-openwork-oss-usage.md`](../_reference/06-agent-format-openwork-oss-usage.md) 证明已有公开仓库把 `AGENTS.md` 作为 repo contract 使用，同时把新 PRD 文件放在单独路径，形成 `AGENTS.md + companion docs + separate PRD artifacts` 的分层实践。
8. ecosystem breadth：
   - [`../_reference/06-agent-format-github-copilot-agents-md-support.md`](../_reference/06-agent-format-github-copilot-agents-md-support.md) 证明 GitHub Copilot coding agent 也已正式支持 `AGENTS.md` 与 nested `AGENTS.md`，说明 cross-tool support breadth 继续扩大。
9. broader diversity / adoption breadth：
   - [`../_reference/06-agent-format-github-adoption-study-2026.md`](../_reference/06-agent-format-github-adoption-study-2026.md) 说明 coding agents 的采用已跨越 128,018 个 GitHub 项目，并覆盖 established organizations、diverse languages/topics；这进一步降低了“仅是少数先行者个案”的风险。
10. multi-agent context-file evaluation：
   - [`../_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md`](../_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md) 直接评估 `AGENTS.md` / `CLAUDE.md` 等 repository-level context files 在 Claude Code、Codex、Qwen Code 以及多个 LLM 设置下的效果；它提供 AGENTbench + SWE-bench Lite 的多 agent evaluation，显示 LLM-generated context files 往往降低成功率并增加成本，developer-provided files 只带来边际收益但也增加成本。
11. formal scaffold-aware compliance benchmark：
   - [`../_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md`](../_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md) 进一步把 Topic 06 从“有 multi-agent evaluation / practitioner experiment”推进到“有 formal benchmark”：OctoBench 用 repository-grounded tasks、three scaffold types、7,098 objective checklist items、full trajectory capture 与 automated scoring，把 task success 与 scaffold-aware compliance 拆开评估。它支持 `formal-scaffold-aware-coding-compliance-benchmark-supported`，但仍不是 exact cross-tool `AGENTS.md` / `CLAUDE.md` semantic conformance suite。
12. practical cross-tool instruction-following experiment：
   - [`../_reference/06-agent-format-umans-agents-md-following-experiment.md`](../_reference/06-agent-format-umans-agents-md-following-experiment.md) 在同一真实 repo、同一 `AGENTS.md` / `CLAUDE.md` 规则和同一测试生成任务上比较 Codex CLI、Claude Code、Gemini CLI、Cursor 等 agent/scaffolding；它不是 formal conformance suite，但显示不同工具对 repo-level rules 的遵守差异明显，且没有任何配置完全匹配 testing style。
13. shared 基线：
   - [`../_reference/00-shared-cursor-rules-official.md`](../_reference/00-shared-cursor-rules-official.md)
   - [`../_reference/00-shared-claude-code-official.md`](../_reference/00-shared-claude-code-official.md)
   - [`../_reference/00-shared-codex-agents-md-spec.md`](../_reference/00-shared-codex-agents-md-spec.md)
   已经分别给出 Cursor、Claude Code、AGENTS.md 的 repo / team-level instruction layer。

## 当前可支撑的判断

1. `AGENTS.md` / `CLAUDE.md` / `.cursor/rules` / `.kiro/steering` 这类文件更像 team-level 或 workspace-level contract，不应承担全部 feature spec 细节。
2. 真正高密度、变动频繁、需要评审和跟踪的需求工件，更适合落在 feature-level artifact 中：
   - Spec Kit 的 `spec.md / plan.md / tasks.md`
   - Kiro 的 `requirements / design / tasks`
   - OpenSpec 的 `proposal.md / specs / design.md / tasks.md`
3. “把所有规则和需求都塞进一个大 instruction file”不是理论担忧，而是 OpenAI 已公开承认的失败模式。
4. Topic 06 当前最强结论不是“哪个单一格式赢了”，而是“三层分离”：
   - team / repo layer
   - domain / scoped rule layer
   - feature / task layer
5. OpenSpec 让 Topic 06 的 `direct cross-tool workflow/config comparison` 不再只是 deferred idea，而是已有一份官方对照锚点；Cline / Continue / Aider 对照进一步证明各工具对 rule/instruction artifact 的 runtime semantics 并不一致；Zhang et al. 2026 证明 rule files 的效果本身有收益/损害分化；Gloaguen et al. 2026 则把 context-file 评估推进到 Claude Code / Codex / Qwen Code 的 multi-agent benchmark；Umans AI 的 practitioner experiment 进一步说明同一 `AGENTS.md` / `CLAUDE.md` 在 Codex CLI、Claude Code、Gemini CLI、Cursor 等 scaffold 下会出现可观察的 rule-following 差异；OctoBench 则补上 formal scaffold-aware coding compliance benchmark，但仍不能替代 exact cross-tool `AGENTS.md` semantic conformance suite。
6. 对 EARS 的初步判断已经足够清楚：
   - EARS 可出现在 agent-era workflow 中
   - 但最佳落点更像 feature-level requirements，而不是 always-on 的大规则文件
7. Topic 06 对 adoption / comparison 的表述现在可以更稳：
   - `tool-vendor-format-convergence-supported`
   - `cross-tool-support-breadth-supported`
   - `public-oss-usage-supported`
   - `enterprise-internal-usage-supported`
   - `direct-cross-tool-workflow-config-comparison-supported`
   - `cross-tool-semantic-divergence-supported`
   - `rule-effect-failure-evidence-supported`
   - `multi-agent-context-file-evaluation-supported`
   - `practical-cross-tool-instruction-following-experiment-supported`
   - `formal-scaffold-aware-coding-compliance-benchmark-supported`
   - `cross-tool-AGENTS-md-semantic-conformance-suite-pending`

## 暂定分层模型

1. team-level / repo-level：
   - `AGENTS.md`
   - `CLAUDE.md`
   - root-level steering / rules
   - 作用：长期约束、命令、架构原则、导航入口
2. scoped rule layer：
   - `.cursor/rules/*.mdc`
   - `.kiro/steering/*.md` with inclusion modes
   - subdir `AGENTS.md`
   - 作用：按路径 / 文件类型 / 任务条件加载的局部规则
3. feature-level workflow：
   - `spec.md`
   - `plan.md`
   - `tasks.md`
   - requirements / design / tasks
   - 作用：当前 feature 的需求、设计、执行闭环

## 对 must_answer 的覆盖进度

| must_answer 子问题 | 当前状态 | 证据 |
| --- | --- | --- |
| 各工具官方推荐的需求 / 规约文件格式是什么 | `starter_covered` | shared 三基线 + Kiro + Spec Kit |
| 是否形成跨工具事实标准 | `comparison_upgraded_semantic_divergence_supported` | AGENTS.md shared 基线 + Amp 官方切换到 AGENTS.md + OpenSpec 官方直接比较 `Spec Kit / Kiro / 25+ tools` + Cline/Continue/Aider rule-loading semantics 对照；format/workflow convergence 有证据，但 semantic uniformity 不成立 |
| 工程团队实际采用模式是什么 | `supported_with_broader_diversity` | OpenAI Codex adopter case + Stripe enterprise-internal usage + OpenWork OSS public usage + GitHub-scale adoption study |
| 与 EARS / User Story / BDD 的对齐 | `starter_covered` | Kiro requirements phase 明确 EARS；Spec Kit / OpenAI adopter case 间接支持 spec-first |
| 失败模式与限制 | `covered_plus_empirical_rule_effects_multi_agent_context_eval_and_practical_cross_tool_experiment` | OpenAI harness engineering + Anthropic context-bloat guidance + Zhang et al. 2026 rule-effect study + Gloaguen et al. 2026 AGENTbench / multi-agent context-file evaluation + Umans AI cross-tool AGENTS.md following experiment |
| 不同场景下的推荐选型 | `upgraded_formal_scaffold_compliance_supported` | 当前已有 Spec Kit / Kiro / OpenSpec 的 workflow comparison、Cline / Continue / Aider 的 precedence / loading semantic differences、AGENTbench multi-agent context-file evaluation、Umans AI same-repo practical cross-tool experiment，以及 OctoBench formal scaffold-aware benchmark；仍需 exact cross-tool `AGENTS.md` / `CLAUDE.md` semantic conformance suite |

## 当前 deep-dive questions

1. OpenSpec 已把 `direct workflow/config comparison` 推进一格；Cline / Continue / Aider 已证明 rule-loading semantics 存在差异；Zhang et al. 2026 已补真实 rule-effect/failure study；Gloaguen et al. 2026 已补多 agent / 多 LLM context-file evaluation；Umans AI 已补 same-repo / same-task / same-rules 的 practitioner cross-tool AGENTS.md following experiment；OctoBench 已补 formal scaffold-aware coding compliance benchmark。下一步若继续增强，应优先补 exact cross-tool `AGENTS.md` / `CLAUDE.md` semantic conformance suite / semantic oracle，而不是重复证明多工具 evaluation 是否存在。
2. Continue、Cline、Aider 在 feature-level artifact 上到底是偏薄层接入，还是已有成体系 workflow？
3. `AGENTS.md` 的跨工具采纳已经很强，但目前更稳写成 format/workflow convention，而不是 semantic standard。
4. 什么时候应该把 EARS 放进 feature spec，什么时候只保留 story / checklist / examples？

## 风险与升级点

- 当前 adopter evidence 已覆盖 OpenAI internal、Stripe enterprise-internal、Amp / Sourcegraph format-adoption、GitHub Copilot 的正式支持、一个公开 OSS usage case，以及 GitHub-scale adoption study；再加上 OpenSpec 官方 direct comparison、Cline/Continue/Aider semantic comparison、Zhang et al. rule-effect study、Gloaguen et al. AGENTbench multi-agent evaluation、Umans AI practical cross-tool instruction-following experiment，以及 OctoBench formal scaffold-aware compliance benchmark，剩余 gap 已从“是否有 formal benchmark”进一步收敛到“是否有 exact cross-tool `AGENTS.md` / `CLAUDE.md` semantic conformance suite”。
- Kiro、Spec Kit、OpenSpec 强力证明了 feature-level workflow 存在，并已出现 cross-tool planning layer；但尚不足以单独决定“哪套 workflow 最优”。
- `AGENTS.md` 的广泛采纳与 semantic uniformity 必须分开写；当前证据反而支持 semantic divergence。

## 下一轮建议动作

1. 继续 Topic 06 时，优先找 exact cross-tool `AGENTS.md` / `CLAUDE.md` semantic conformance suite / semantic oracle，而不是继续补“workflow 存在”“规则加载差异存在”“single-agent rule-effect study”“一般 multi-agent context-file evaluation”“formal scaffold-aware benchmark”或 single-repo practitioner experiment。
2. 若要再补 adopter side，应优先找能暴露 cross-tool behavior differences 的 primary/comparative study，而不是重复证明“有没有人用”。
3. 保持“三层分离”与“semantic divergence supported”的双重口径，不要把 adoption breadth 或 direct comparison 写成 semantic standard proof。
