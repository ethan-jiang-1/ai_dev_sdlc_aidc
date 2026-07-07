# Topic 6 — 最强 Coding Agent / Harness 的需求格式实证与选型

> 本文件面向 **独立 Deep Research** 使用。它是本轮（[dr-round-1](../plan/dr-round-1.plan.md)）**唯一具有决策输出**的研究线：必须在 2024Q3–2026Q1 时间窗内，产出针对 Cursor / Claude Code / Codex / Kiro / GitHub Spec Kit / OpenSpec / Amp / Aider / Continue / Cline 等 coding agent / harness 的需求 / 规约格式选型建议。
>
> 与其他 5 个主题不同，本主题是 **exploration + exploitation 混合**：需要第一手观察 + 实证证据，不能靠文献综述一次性解决。

## 0. 研究线元数据

- topic_id: `06`
- topic_slug: `agent-format`
- registry_ref: [`../plan/dr-round-1.plan.md`](../plan/dr-round-1.plan.md) → 研究线注册表（topic registry）→ 06/agent-format
- time_window: `2024Q3–2026Q1`（严格）
- recency_floor: `2024-07`
- 研究定位: `exploration + exploitation`
- 评估策略: 官方文档（Tier B/C）+ 官方仓库模板（Tier C）+ 工程团队公开案例（Tier C）+ 社区失败模式（Tier E，需双证）

## 1. 研究问题（Deep Research 入口）

1. **官方主张面**：Cursor（Rules / AGENTS.md）、Anthropic Claude Code（CLAUDE.md / Skills / Plugins）、OpenAI Codex CLI（AGENTS.md 规范）、Amazon Kiro Spec Workflow、GitHub Spec Kit、OpenSpec、Amp、Aider、Continue、Cline 各自官方推荐的需求 / 规约 / 上下文文件格式是什么？命名、位置、schema、分层结构、与代码仓库的关系分别如何？
2. **事实标准面**：这些格式之间是否已经在 2024Q3–2026Q1 间形成**跨工具的事实标准**（例如 `AGENTS.md` 是否正在成为多 agent 共用的约定）？是否有 spec 级别的文档（而非单厂商 README）支撑？
3. **采用模式面**：公开可见的工程团队 / 大型 OSS 项目 / 大厂内部实践，在这些 agent / harness 下**实际**采用的需求或规约组织方式是什么（文件层级、与 ADR / RFC / issue / PR 的关系）？有没有可复用的模式？
4. **格式对齐面**：这些格式与 User Story、EARS、BDD、INCOSE GTWR 之间是否有可见的对齐？是否有团队把 EARS 直接塞进 CLAUDE.md / .cursor/rules / AGENTS.md？效果如何？
5. **失败模式面**：已观察到的失败模式（context rot、上下文过长、规则打架、rules 污染 reasoning、agent 忽略 spec、spec 与代码漂移、"rules bloat"）的一手证据或复盘？
6. **决策输出面**：综合上述，对"产品 / 架构师 / AI 编程实践者"这一读者群，**本轮的推荐选型**是什么？针对不同场景（独立开发者 / 小团队 SaaS / 合规敏感的大型组织）应如何搭配？

## 2. 观察对象清单（work list）

本研究线需要对下列对象分别建立 Authoritative Copy 或合并摘录，落在 [`_reference/06-agent-format-*.md`](_reference/)：

### 2.1 IDE 级 agent / harness

| 工具 | 官方规约 / 上下文文件入口 | 主分发渠道 |
| --- | --- | --- |
| Cursor | `.cursor/rules/*.mdc`、项目根 `AGENTS.md` | Cursor 官方文档 |
| Anthropic Claude Code | `CLAUDE.md`（项目根 + 用户级）、`.claude/skills/`、`.claude/agents/`、plugins | Anthropic 官方文档 |
| OpenAI Codex CLI | 项目根 `AGENTS.md`（与 Cursor、Amp、等共享约定） | OpenAI Codex CLI 官方文档 + `agents.md` 约定站点 |
| Amp | 项目根 `AGENTS.md` | Sourcegraph Amp 文档 |
| Aider | `CONVENTIONS.md`、`.aider.conf.yml`、`.aiderignore` | aider.chat 官方文档 |
| Continue | `.continuerules`、`config.yaml`/`config.json`、Hub blocks | Continue 官方文档 |
| Cline | `.clinerules/*.md` | Cline 官方文档 |

### 2.2 Spec 流程 / Spec-as-Code 工具

| 工具 | 定位 | 主分发渠道 |
| --- | --- | --- |
| Amazon Kiro | IDE 内嵌 Spec Workflow（requirements / design / tasks 三分文件） | Kiro.dev 官方文档 |
| GitHub Spec Kit | 跨 agent 的 spec-driven 开发工具链（`spec.md` / `plan.md` / `tasks.md`） | github.com/github/spec-kit |
| OpenSpec | 轻量 spec change workflow，强调变更驱动 | github.com/openspec / openspec.dev |
| Linear Spec / Notion AI Spec | SaaS 端 spec 管理（外围信号） | 各自官方 |

### 2.3 非 harness 但影响格式事实标准的参与者

- `AGENTS.md` 社区约定（agents.md 站点 + 支持该文件的工具清单）
- 大型 OSS 项目已公开的 `CLAUDE.md` / `AGENTS.md` / `.cursor/rules/`（用于采用模式证据）
- 大厂工程博客中关于 rules / spec 文件布局的文章（Shopify、Sentry、Cloudflare、Anthropic 自身的产品团队博客）

## 3. Wave 0 基线清单（必须先落库）

进入 Wave 1 前，必须至少完成下面三份 Authoritative Copy（它们同时是本研究线的 baseline 三角）：

- `_reference/00-shared-cursor-rules-official.md`：Cursor Rules 官方文档（`.cursor/rules/*.mdc` schema + `AGENTS.md` 支持状况 + recommended patterns）
- `_reference/00-shared-claude-code-official.md`：Anthropic Claude Code 官方文档（`CLAUDE.md` 分层 + Skills / Plugins + Subagents）
- `_reference/00-shared-codex-agents-md-spec.md`：OpenAI Codex CLI + `AGENTS.md` 社区约定（agents.md 官方站点 + Codex CLI 官方文档）

这三份同属共享地基层（`00-shared-*`），因为其他研究线在讨论"AI 编程时代"时会反复引用。

## 4. Wave 1 深挖维度

本研究线在 Wave 1 期间，除 Wave 0 基线外，每类对象至少补充下列材料（可按需合并 Authoritative Copy）：

### 4.1 证据（evidence）

- 每个 §2.1 / §2.2 对象的官方主张（primary source，Tier B/C）
- 至少 3 份公开工程团队 / OSS 项目的采用案例（primary source 或 high-trust blog，Tier C）
- 至少 1 份 agents.md 约定的来源说明 + 支持工具清单（Tier B/C）

### 4.2 根本机制（mechanism）

- 为什么 CLAUDE.md / AGENTS.md / `.cursor/rules/*.mdc` 能影响 agent 行为？与 system prompt、tool prompt、retrieval context 的关系
- Spec Kit / Kiro / OpenSpec 的流程模型（`spec -> plan -> tasks -> code` 与反向闭环）
- AGENTS.md 与 Cursor Rules 的语义重叠 / 互斥情况

### 4.3 趋势（trend）

- 2024Q3→2026Q1 间格式演化的时间线（Cursor Rules v1/v2、Claude Code Skills/Plugins 引入、AGENTS.md 的跨工具采纳、Spec Kit 发布）
- 是否出现跨工具的事实标准化（AGENTS.md 是明显候选）

### 4.4 难度（difficulty）

- Context window 与上下文污染
- 多文件 rules / skills 的优先级冲突
- rules 版本化 vs IDE 缓存
- 团队共享 vs 个人定制

### 4.5 争议 / 失败模式（limitation）

- "context rot" / "rules bloat"
- rules 与 agent reasoning 的相互干扰
- Skills vs Rules 的角色定位争论
- spec drift（spec 与代码脱钩）
- 必须至少覆盖 2 份一手来源（Tier B/C 的官方说明或 Tier E 的社区讨论 + 双证）

## 5. 产出契约

本研究线须在 Wave 2 结束前产出：

- `_reference/06-agent-format-*.md` ≥ 8 份（其中一手来源 ≥ 5 份、近期来源 ≥ 3 份、限制 / 失败来源 ≥ 2 份）
- `_artifacts/06-agent-format-evidence-summary.md`
- `_artifacts/06-agent-format-question-list.md`
- 回填本 seed 的下列章节：
  - `本轮新增证据`
  - `本轮新增机制理解`
  - `本轮新增趋势与难点`
  - `当前判断（本轮综合后）`
- 在 Wave 2 的 `_artifacts/W2-selection-matrix-v2.md` 与 `_artifacts/W2-cross-topic-synthesis.md` 中贡献专门的"agent-format 选型列 / 章节"
- 在 Wave 2 同步回填 [`topic-04-future-trends-and-evidence.md`](topic-04-future-trends-and-evidence.md) §4.6 "IDE 原生的需求原语"，把揣测升级为近因观察 + 判断

## 6. 当前工作假设（pre-research）

> 本节是 Wave 0 / Wave 1 开始前的工作假设，**不是结论**；每一条都将在 Wave 1 / Wave 2 被证伪、验证或精化。

1. **事实标准候选**：`AGENTS.md` 正在成为跨工具的约定；Cursor / Codex / Amp / Aider 已经或即将支持它，Claude Code 仍以 `CLAUDE.md` 为主但允许共存。
2. **分层事实**：`AGENTS.md` / `CLAUDE.md` 更像"项目-agent 合约"（team-level），`.cursor/rules/*.mdc` 或 `.clinerules/*.md` 更像"精细化情境化规则"（scope-level）；Spec Kit / Kiro / OpenSpec 处理"功能级 spec"（feature-level）。三层并存而非互斥。
3. **与 EARS 的关系**：EARS 可以被塞进上述任何一层；但在不同层"划算度"不同——feature-level spec（Kiro / Spec Kit）最合适，team-level contract 放太多 EARS 会造成 context rot。
4. **推荐组合（待验证）**：
   - 独立开发者 / 快节奏原型：一份 `AGENTS.md` + Cursor Rules，按需塞入少量 EARS 约束。
   - 小团队 SaaS：`AGENTS.md`（团队合约）+ `.cursor/rules/*.mdc`（模块化规则）+ Spec Kit / OpenSpec 做 feature-level spec，spec 内部用 EARS + Gherkin。
   - 合规敏感的大型组织：在上述之上，把 EARS / INCOSE GTWR 落到 ALM（Jama / Visure），spec 文件作为双向映射入口。
5. **主要失败模式**：rules bloat、skills / rules 混用导致冲突、spec 与 `AGENTS.md` 重复维护、AI 生成 spec 但无人 review。

## 7. Deep Research 查询种子

**英文**：

1. `AGENTS.md specification cross-tool Cursor Codex Amp Aider adoption 2025..2026`
2. `"CLAUDE.md" project context anthropic best practices layering skills plugins`
3. `cursor rules .mdc format schema recommended patterns 2025..2026`
4. `GitHub Spec Kit spec-driven development workflow case study`
5. `Kiro spec workflow requirements design tasks file structure Amazon`
6. `OpenSpec spec change workflow adoption pattern 2024..2026`
7. `"context rot" OR "rules bloat" cursor claude code agent failure mode`
8. `EARS requirement syntax Cursor Claude Code AGENTS.md actual use case`
9. `coding agent harness requirements format empirical comparison`
10. `spec drift spec and code divergence AI coding agent maintenance`

**中文**：

1. `AGENTS.md 约定 跨工具 Cursor Codex Amp Aider 采用情况 2025 2026`
2. `CLAUDE.md 分层 上下文 最佳实践 Skills Plugins`
3. `Cursor Rules .mdc 格式 schema 推荐模式 2025`
4. `Spec Kit 规范 驱动 开发 案例 2025 2026`
5. `Kiro Spec 工作流 requirements design tasks 三分文件`
6. `context rot rules bloat 规则膨胀 Cursor Claude Code 失败模式`
7. `EARS 需求语法 Cursor Claude Code 实际采用案例`
8. `coding agent 需求格式 实证对比`

## 8. 交叉引用

- 与 Topic 04 的关系：本主题是从 [topic-04-future-trends-and-evidence.md](topic-04-future-trends-and-evidence.md) §4.6 "IDE 原生的需求原语"剥离出来的独立研究线；Wave 2 结束时必须反哺 Topic 04。
- 与 Topic 03 的关系：EARS 能否塞进 agent 格式是本主题核心之一；在 [topic-03-ears-tutorial.md](topic-03-ears-tutorial.md) 的 "何时不用 EARS" 准则建立后，本主题需对齐判断。
- 与 Topic 05 的关系：三轨（Story / EARS / Gherkin）分层 × 三层（AGENTS / Cursor Rules / Spec Kit）正交，是 Wave 2 `W2-selection-matrix-v2.md` 的核心矩阵轴。
- 与 claims-audit 的关系：本主题将给 [claims-audit.md](claims-audit.md) 贡献新条目（"agent 格式的事实标准已存在"等断言），在 Wave 2 `W2-claims-audit-v2.md` 升级证据强度。

## 9. 本 seed 状态

- status: `closed_for_current_round`
- last_updated: `2026-04-18`
- backfill_sections_to_be_added_in_wave1: `done below; remaining gaps tracked in _artifacts/06-agent-format-question-list.md`

## 10. 历史摘要（保留，不修改）

- 本主题的历史正文保留在 §0–§9：它定义了研究问题、观察对象、Wave 0 baseline 三角、Wave 1 深挖维度、选型输出要求与 seed 状态。

## 11. 本轮新增证据

- Shared baseline 已覆盖 Cursor Rules、Claude Code `CLAUDE.md`、AGENTS.md / Codex CLI 三类 team/repo context 文件：[`_reference/00-shared-cursor-rules-official.md`](_reference/00-shared-cursor-rules-official.md)、[`_reference/00-shared-claude-code-official.md`](_reference/00-shared-claude-code-official.md)、[`_reference/00-shared-codex-agents-md-spec.md`](_reference/00-shared-codex-agents-md-spec.md)。
- Adopter case：OpenAI 内部工程使用 Codex 时会把 `user request or spec` 作为 agent 输入，并通过 Ask Mode / Code Mode 推进实现；见 [`_reference/06-agent-format-openai-codex-adoption.md`](_reference/06-agent-format-openai-codex-adoption.md)。
- Failure / mechanism case：OpenAI 明确记录 `one big AGENTS.md` 失败，并把短 AGENTS.md 定位为 table of contents，deeper docs / plans 作为 system of record；见 [`_reference/06-agent-format-openai-harness-engineering.md`](_reference/06-agent-format-openai-harness-engineering.md)。
- Feature-level workflow：GitHub Spec Kit 与 Kiro 分别提供 `spec/plan/tasks` 与 `requirements/design/tasks` 的官方流程；见 [`_reference/06-agent-format-github-spec-kit-official.md`](_reference/06-agent-format-github-spec-kit-official.md)、[`_reference/06-agent-format-kiro-spec-workflow-official.md`](_reference/06-agent-format-kiro-spec-workflow-official.md)。
- Format convergence / ecosystem breadth：Amp / Sourcegraph 已从 `AGENT.md` 公开迁移到 `AGENTS.md`，GitHub Copilot 也已正式支持 `AGENTS.md` 与 nested `AGENTS.md`；见 [`_reference/06-agent-format-amp-agents-md-adoption.md`](_reference/06-agent-format-amp-agents-md-adoption.md)、[`_reference/06-agent-format-github-copilot-agents-md-support.md`](_reference/06-agent-format-github-copilot-agents-md-support.md)。
- Public OSS usage：OpenWork 公开把 `AGENTS.md` 作为 repo contract，并把 PRD 放在独立路径；见 [`_reference/06-agent-format-openwork-oss-usage.md`](_reference/06-agent-format-openwork-oss-usage.md)。
- Enterprise-internal usage：Stripe 官方 `Minions` 文章说明，非工具厂商企业内部也已公开采用 unattended coding agents，并复用与 Cursor / Claude Code 相同的 rule files；见 [`_reference/06-agent-format-stripe-minions-enterprise-usage.md`](_reference/06-agent-format-stripe-minions-enterprise-usage.md)。
- Multi-agent evaluation：Gloaguen et al. 2026 的 `Evaluating AGENTS.md` / AGENTbench 在 Claude Code、Codex、Qwen Code 与多个 LLM 设置下评估 repository-level context files，显示 LLM-generated context files 往往降低成功率并增加成本，developer-provided files 只有边际收益且也增加成本；见 [`_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md`](_reference/06-agent-format-evaluating-agents-md-agentbench-2026.md)。
- Formal scaffold-aware benchmark：OctoBench 已提供 repository-grounded agentic coding 中 scaffold-aware instruction following 的 formal benchmark，把 task-solving 与 scaffold-compliance 拆开评估；见 [`_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md`](_reference/06-agent-format-octobench-scaffold-aware-coding-2026.md)。
- Practical cross-tool experiment：Umans AI 同仓、同任务、同规则的 practitioner experiment 进一步说明不同工具对 `AGENTS.md` / `CLAUDE.md` 的遵守差异可被直接观察；见 [`_reference/06-agent-format-umans-agents-md-following-experiment.md`](_reference/06-agent-format-umans-agents-md-following-experiment.md)。

## 12. 本轮新增机制理解

- 关键机制不是“哪个单一 markdown 文件赢了”，而是 **三层分离**：
  - team / repo contract：`AGENTS.md`、`CLAUDE.md`、root steering
  - scoped rule layer：`.cursor/rules/*.mdc`、subdir `AGENTS.md`、steering inclusion modes
  - feature workflow layer：`spec.md / plan.md / tasks.md` 或 `requirements / design / tasks`
- team-level contract 应短小、稳定、导航化；feature-level spec 可以更具体、更可审查、更适合承载 EARS / examples / tasks。
- 大而全 always-loaded instruction file 是失败模式，会造成 context scarcity、priority dilution、staleness 和 verification 难题；见 [`_artifacts/06-agent-format-evidence-summary.md`](_artifacts/06-agent-format-evidence-summary.md)。
- Multi-agent context-file evaluation 进一步说明：即便 agents 通常会遵守 context-file instructions，不必要的 requirements 也会增加探索、测试、步骤数和推理成本；这支持“短、必要、任务相关”的 repo-level context，而不是自动生成长 context。
- OctoBench 进一步把 Topic 06 从“有 evaluation / experiment”升级到“有 formal scaffold-aware coding compliance benchmark”，但 exact cross-tool `AGENTS.md` semantic conformance 仍未被解决。

## 13. 本轮新增趋势与难点

- `AGENTS.md` 是跨工具 adoption candidate，但当前证据只能支持“采用约定正在形成”，不能直接支持“跨工具语义完全一致”；见 [`_artifacts/W2-claims-audit-v2.md`](_artifacts/W2-claims-audit-v2.md)。
- 企业内部 adoption 已不再是 OpenAI 单点：Stripe 公开说明大型组织会把 homegrown coding agent 与 Cursor / Claude Code rule files、MCP tools、CI feedback loop 连成统一工程系统。
- Spec Kit / Kiro 证明 feature-level spec workflow 已经产品化，但 Thoughtworks 对 spec-driven development 的 elaborate / opinionated / hard-to-review 风险提示仍需保留；见 [`_artifacts/W2-selection-matrix-v2.md`](_artifacts/W2-selection-matrix-v2.md)。
- 仍缺 exact cross-tool `AGENTS.md` semantic conformance suite；但 multi-tool replication / evaluation 缺口已由 AGENTbench、OctoBench 与 Umans AI 进一步收窄，不应再重复用弱证据证明“多工具评估存在”；见 [`_artifacts/06-agent-format-question-list.md`](_artifacts/06-agent-format-question-list.md)。

## 14. 当前判断（本轮综合后）

- 本轮推荐的 agent-era 需求格式不是“把 EARS 或 Story 塞进 AGENTS.md”，而是：短 team contract + scoped rules + feature-level spec/plan/tasks。
- EARS 最适合放在 feature-level requirements / acceptance criteria 中；除非是极少数长期、全局适用的写作规则，否则不应放进 always-loaded team-level file。
- 工程团队实际采用模式现在可以更稳地写成“vendor + public OSS + enterprise-internal”三类都已出现，但 enterprise-internal 的公开样本仍然不够多，不能把 Stripe 单点写成行业普及。
- Topic 06 的比较结论现可稳写成：
  - `direct-comparison-supported`
  - `semantic-divergence-supported`
  - `multi-agent-context-file-evaluation-supported`
  - `practical-cross-tool-instruction-following-experiment-supported`
  - `formal-scaffold-aware-coding-compliance-benchmark-supported`
  - `cross-tool-AGENTS-md-semantic-conformance-suite-pending`
- 对产品 / 架构师 / AI 编程实践者的初步选型：
  - 原型和发现期：Story / Job Story + 少量 AC + 短 agent context。
  - 小团队 SaaS：Story Map + examples + selective EARS + Spec Kit/Kiro-style feature workflow。
  - 合规敏感组织：29148/GtWR-aligned requirements + EARS + traceability + examples/tests，agent files 只做导航和工作约束。
- 以上判断已进入 [`_artifacts/W2-cross-topic-synthesis.md`](_artifacts/W2-cross-topic-synthesis.md) 与 [`_artifacts/W2-selection-matrix-v2.md`](_artifacts/W2-selection-matrix-v2.md)，当前状态是 `closed_for_current_round`；它们仍不是 polished final report，而是本轮正式收口后的 source-of-record surface。
