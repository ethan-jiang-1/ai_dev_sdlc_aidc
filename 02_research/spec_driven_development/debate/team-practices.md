# SDD 在真实团队/协作场景中的工程化实践（调研）

```yaml
title: Spec-Driven Development 团队工程化实践：协作界面、工程控制、迭代机制与失败教训
scope: 多人/多 agent 并行开发中 spec 如何承担协作与工程控制职能；面向 5-20 人 brownfield 团队的落地建议
accessed_at: 2026-09-20
observation_date: 2026-09-20
time_weighting: 2026 年材料优先（近 3-4 个月权重最高）；2025 年材料仅用于说明工具机制演化
evidence_tiers:
  tier1_primary: 一手——团队/项目自述实践（repo 内工作流文档、自建 CI 配置、issue/PR 记录、官方 docs 的规范行为本身）
  tier2_secondary: 二手——转述、分析、厂商案例稿
```

---

## 0. 材料清单（日期 + URL + 证据档 + 团队规模）

| # | 材料 | 日期 | 档 | 团队规模 |
|---|---|---|---|---|
| M1 | [austinxyz/opsx-superpowers — Multi-Engineer OpenSpec Workflow — Design](https://github.com/austinxyz/opsx-superpowers/blob/main/docs/superpowers/specs/2026-05-26-multi-engineer-workflow-design.md) | 2026-05-26（文中含 2026-05-20 等运行痕迹） | **一手**（团队自述工作流设计，明确 scope "2-6 engineer teams with existing CI/CD + PR review"） | 2-6 人（设计上限 4-6 人扩缩章节） |
| M2 | [PostHog/sdk-specs](https://github.com/PostHog/sdk-specs)（openspec/ 目录 + [.github/workflows/openspec.yml](https://github.com/PostHog/sdk-specs/blob/main/.github/workflows/openspec.yml) + commit `5777655` "ci: validate OpenSpec specs"） | 实地查看于 2026-09-20（CI 固定 `@fission-ai/openspec@1.4.1`） | **一手**（spec 仓库结构与其 CI 配置即实践本身） | 跨多个 SDK 团队共享的契约仓库（规模未公开） |
| M3 | [github/spec-kit 官方仓库自吃狗粮的 .specify/memory/constitution.md](https://github.com/github/spec-kit/blob/main/.specify/memory/constitution.md) | Ratified 2026-06-19（v1.0.0） | **一手**（GitHub 自己团队为 brownfield spec-kit 代码库制定的真实 constitution，含治理条款） | GitHub spec-kit 维护团队 |
| M4 | [github/spec-kit README 与 evolving-specs 指南](https://github.com/github/spec-kit) / [Evolving Specs in Existing Projects](https://github.github.io/spec-kit/guides/evolving-specs.html) | 实地查看于 2026-09-20（含 `/speckit-converge`、extensions/presets/bundles 等 2026 新机制） | 一手（工具官方 docs） | — |
| M5 | [kuchida1981/comic-viewer-helper — Issue #61 "OpenSpec ドキュメントの不整合解決と CI での自動検証導入"](https://github.com/kuchida1981/comic-viewer-helper/issues/61) | 2026-02-01，closed 2026-02-02 | **一手**（自述：validate --strict --all 发现 5 个 spec 不合规 → 修文件 + 上 GitHub Actions 自动校验） | 个人项目（流程样本价值） |
| M6 | [Fission-AI/OpenSpec 官方 docs：concepts.md / cli.md](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md) / [cli.md](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md) | 实地查看于 2026-09-20（含 stores/worksets beta 等 2026 新面） | 一手（工具官方 docs） | — |
| M7 | [joosiimoo/sdd-openspec-agents-template — ANTI_PATTERNS.md](https://github.com/joosiimoo/sdd-openspec-agents-template/blob/main/ANTI_PATTERNS.md) | 实地查看于 2026-09-20 | **一手**（自述"distilled from real failures in AI-assisted development"，14 条反模式） | 未公开 |
| M8 | [Kiro CLI Changelog 2.18 "Spec Review screen / Nested AGENTS.md steering"](https://kiro.dev/changelog/cli/2-18/)（另有 [steering docs](https://kiro.dev/docs/steering/)） | 2026-08-12（2.18.1 patch 2026-08-14） | 一手（厂商 changelog，机制性证据） | — |
| M9 | [Thoughtworks Technology Radar — Spec-driven development](https://www.thoughtworks.com/radar/techniques/spec-driven-development) 与 [GitHub Spec Kit 条目](https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit) | Radar 2026 版期 | 二手（行业判断，条目正文抓取被导航噪声吞掉，档位按转述计） | — |
| M10 | BMAD Method / obra Superpowers 能力面 | 检索于 2026-09-20（来源混杂，未逐条核官方 repo，仅作能力对照参考） | 二手 | — |

---

## 1. Spec 作为团队协作界面

### 1.1 实地看的开源 repo spec 目录（6 个，含真实结构片段）

**① PostHog/sdk-specs（M2）——"一个 API 行为一个目录"的跨团队契约仓库**

这是 PostHog 给所有 SDK（js/python/ios/android/node/ruby/php/…）定义统一行为契约的独立 spec 仓库。`openspec/` 顶层：

```
openspec/
├── changes/          # 进行中的变更（delta）
├── specs/            # 60+ 个能力目录，每个能力一个 dir
│   ├── get-feature-flag/spec.md
│   ├── session-replay-privacy/spec.md
│   ├── feature-flag-cache/spec.md
│   └── ...（alias、autocapture、consent-gating、identify、flush…）
├── config.yaml       # schema: spec-driven
└── project.md
```

`get-feature-flag/spec.md` 真实片段（展示"行为契约 + RFC2119 + 可测试 Scenario + 平台标签"四件套如何跨团队对齐）：

```markdown
### Requirement: Canonical get-feature-flag behavior
The SDK SHALL implement the canonical `get-feature-flag` behavior ...
but MUST preserve the observable outcomes in the scenarios below.

#### Scenario: Client getter returns the cached boolean flag value (@client)
- **GIVEN** ... cached feature flags are: | beta-ui | true |
- **WHEN** get feature flag "beta-ui" is called
- **THEN** the returned feature flag value should be true
- **AND** a "$feature_flag_called" event should be enqueued ...
```

协作语义：spec 与实现代码**分离成独立仓库**，多语言 SDK 团队以它为"单一行为事实源"；Scenario 用 `@client` / `@server` / `@both` 标注适用面，防止一个团队的行为改动悄悄破坏另一个团队。

**② github/spec-kit（M3）——官方仓库自吃狗粮的 `.specify/`**

```
.specify/
├── memory/constitution.md    # v1.0.0, Ratified 2026-06-19
├── templates/                # plan-template.md（内含 Constitution Check 门禁段）
├── scripts/
└── bugs/  assessments/       # 扩展产物目录（bug-fix / idea-assessment 扩展）
```

constitution.md 是一份真实的治理文档，值得整段引用其治理核心（M3）：

> **Authority.** Principles I–V are binding gates. The `## Constitution Check` section of the plan template MUST be evaluated against these principles, and `/speckit.analyze` treats conflicts with a MUST as CRITICAL.
> **Amendments.** Changes to this document require a PR with rationale, maintainer approval, and a version bump … **Versioning policy (SemVer for governance).** MAJOR = backward-incompatible governance or principle removal; MINOR = new principle; PATCH = clarifications.

要点：**constitution 本身也走 PR + 版本号 + 同步传播（Sync Impact Report 头注记录"本次修订波及哪些模板"）**——这是 2026 年看到的对"规则文件如何演进"最完整的工程化回答。

**③ austinxyz/opsx-superpowers（M1）——目前公开度最高的一手"多人 SDD 工作流"设计文档**

它自己的 spec 目录沿 Superpowers 惯例（`docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`，frontmatter `Status: REVIEWED`），同时详细定义了团队版 OpenSpec 布局。其核心分支/PR 模型（见 §1.2）以及共享文件架构：

```
openspec/specs/<capability>/spec.md       # 每能力一份契约
openspec/specs/<capability>/pitfalls.md   # 该能力的踩坑记录（archive 时更新）
openspec/specs/README.md                  # 每能力一行索引（仅新增能力时改）
```

外加每份 spec 的 frontmatter 承载依赖图（M1 原文）：

```yaml
---
capability: auth
depends_on: [user-store, session]
status: ACTIVE        # 重构期可标 MIGRATING
---
```

**④ kuchida1981/comic-viewer-helper（M5）——个人 brownfield 项目的标准 OpenSpec 布局**

```
openspec/
├── changes/          # 含 archive/
├── specs/            # activation-toggle、ci-testing、metadata-view、page-jump、pr-enforcement …
└── config.yaml
```

价值在它的 Issue #61（2026-02）自述了典型补救路径：跑 `openspec validate --strict --all` 发现 5 个 spec 结构不合规 → 逐个修复 → 在 GitHub Actions 加 `openspec validate` 防复发。

**⑤ Fission-AI/OpenSpec（M6）**——官方 docs 定义的"两区模型"即协作界面本身：`openspec/specs/`（当前行为事实源）× `openspec/changes/<change>/`（互不冲突的并行提案，内含 proposal/design/tasks/delta specs）。2026 年新增 **stores（独立 spec 仓库注册 + 只读引用）**：`openspec/config.yaml` 里 `references: [{id: team-context, remote: git@...}]`，支持"规划仓库与代码仓库分离"，注释明说"References are read-only context... never copied into the output"（M6）。

**⑥ joosiimoo/sdd-openspec-agents-template（M7）**——模板仓库形态的团队落地包：把 ANTI_PATTERNS.md、角色分工（Spec Refiner 才能改 spec）、验证清单直接沉淀为仓库文件，等价于"把评审 checklist 代码化进 repo"。

### 1.2 spec 怎么组织多人/多 agent 并行：所有权与评审流

M1（2026-05-26，一手，2-6 人团队自述）给出了目前颗粒度最细的公开方案，可复用颗粒如下：

- **两轨分支模型**：
  - 小特性（≤3 模块、无跨人接口、无架构影响、≤2 天）：`feat/<topic>` 一条分支，spec+代码+archive 一起进一个 PR；
  - 大特性（跨人接口 / 架构决策 / ≥3 天 / 破坏性 spec 变更，任一触发）：先开 `spec/<topic>` 分支只提 spec 文件 → **PR1 = Spec Review（团队锁需求/设计/任务结构，merge 后 tasks 锁定）** → 再从 main 拉 `feat/<topic>` 实施 → **PR2 = Impl Review**。
- **冲突在 propose 时暴露而非 merge 时**：propose 前必须 `git branch -r` 读所有活跃分支的 proposal.md，把 `depends on / conflicts with` 写进 design.md；B 依赖 A 的接口 ⇒ A 的 spec PR 必须先 merge（"interface must lock before parallel implementation starts"）。
- **所有权规则**：一人一个 topic 端到端；**绝不把一个 topic 拆给两个人**（"make the topic smaller instead"）；无 CODEOWNERS，任何非 owner 评审即可。
- **共享文件防冲突**（4-6 人并行 archive 的关键设计）：archive 只写 per-capability 文件（`spec.md`/`pitfalls.md` 各自独立），`CLAUDE.md` 退化为稳定索引**不在 archive 时更新**，全局踩坑条目攒到接近 5 条才开 maintenance PR 收敛。
- **4-6 人评审带宽测算**（原文）：每人每天约 1-2 个轻量 code PR 或 1 个 spec PR，spec PR 评审 15-30 分钟，"not a bottleneck"。
- **与敏捷的映射**（原文摘要）：explore≈story refinement、propose≈sprint planning、apply≈执行、archive≈review+retro；速率度量从故事点改为"本冲刺 archive 的能力 spec 数 + CI green"。

多 agent 维度：M2（PostHog）的 spec 仓库本质是给多语言 SDK 团队 + 各自 AI agent 的共享上下文契约；Kiro 2.18（M8，2026-08）把协作界面做进产品——spec 阶段检查点按 `Ctrl+X` 出**评审屏，支持逐行 stage comment，一次性汇成一条修订请求发给 agent**，并把**任意层级目录的 AGENTS.md 自动加载为 steering 上下文**（即"目录级所有权"由工具原生承担：哪个目录的 spec/代码，读哪个目录的规则）。

### 1.3 小结

公开分享过布局的都是 OpenSpec 系（PostHog、opsx-superpowers、comic-viewer-helper、模板仓库）+ Spec Kit 系（spec-kit 自身）。共同点：**按能力/域切目录、每能力一个 spec.md、changes/ 承载并行提案、依赖写进 frontmatter 或 design.md、共享索引文件冻结化**。未发现 2026 年有知名工程博客公开分享 Kiro spec 目录的多人布局（Kiro 侧证据停在产品机制层）。

---

## 2. 工程控制手段

### 2.1 CI / 机器校验（可复制配置）

**PostHog/sdk-specs 的真实 CI（M2，一手，`.github/workflows/openspec.yml` 全文关键段）：**

```yaml
on:
  pull_request:
    paths: ['openspec/**', '.github/workflows/openspec.yml']
  push:
    branches: [main]
    paths: ['openspec/**']
jobs:
  validate:
    steps:
      - run: npm install -g @fission-ai/openspec@1.4.1   # 版本钉死
        env: { OPENSPEC_TELEMETRY: '0' }
      - run: openspec validate --specs --strict --no-interactive
```

要点：**path-filter（只动 openspec/** 才跑）+ 版本 pin + --strict + 非交互**。

**OpenSpec validate 原生能力面（M6，2026 版）：**
- `openspec validate --all|--changes|--specs [--strict] [--json]`：结构校验 + **把 change 的 MODIFIED requirement 与被替换的主 spec 做比对**；
- 无 spec delta 的 change 默认校验失败，除非 `.openspec.yaml` 声明 `skip_specs: true`（纯重构/工具类变更的显式豁免通道）；
- `validate --archived`：**校验 archive 里每个 change 的 tasks.md 全部勾完**，官方建议挂 pre-commit；
- `openspec status --json` / `instructions` / `doctor`：给 agent/脚本消费的机器面；
- schema 机制：`openspec/schemas/<name>/schema.yaml` 定义 artifact 依赖图（proposal→specs→design→tasks），`schema fork` 让团队定制自己的流程并可用 `schema validate` 校验——**模板强制以 schema+templates 形式原生提供**。

**comic-viewer-helper 的教训路径（M5，2026-02）**：先人工跑 validate 发现 5 个 spec 不合规，修复后上 CI 自动校验——印证"裸 spec 目录会自然腐烂，必须靠机器门禁兜底"。

### 2.2 各工具原生提供 vs 需自建（对照表）

| 控制手段 | Spec Kit（M4/M3） | OpenSpec（M2/M6） | Kiro（M8） | Superpowers | BMAD（M10） |
|---|---|---|---|---|---|
| 机器校验 CLI | 无独立 validate CLI（质量靠 `/speckit-analyze`、`/speckit-converge` 在会话内做一致性/完成度分析，属 **LLM 门禁非确定性门禁**） | ✅ `validate --strict --json`，可进 CI | 未提供独立 spec 校验 CLI（校验停留在 IDE/CLI 内的 spec review 屏） | 无（skills 面向流程纪律） | 无确定性校验 |
| 模板/schema 强制 | ✅ `.specify/templates/` + plan 模板内 Constitution Check 段 | ✅ schema.yaml 依赖图 + templates + `skip_specs` 豁免 | ✅ spec 三件套（requirements/design/tasks）固定结构 | 弱 | ✅ 角色/文档模板重（PM/Architect/Dev/QA 全套产物） |
| constitution/规则治理 | ✅ 最完整：constitution + SemVer 版本化 + Sync Impact Report + `/speckit.analyze` 把 MUST 冲突判 CRITICAL（M3 实例） | 规则散在 config.yaml（context/rules 字段）+ AGENTS.md | ✅ steering 文件（含 2026-08 起嵌套 AGENTS.md），无版本化治理 | ✅ skills 形式的纪律 | ✅ 但偏流程模板 |
| 评审门禁（PR 带 spec diff） | 指南层：evolving-specs 要求"从干净工作树/专分支改 spec，diff 可评审"（M4）；PR 模板强制无 | 无强制，靠团队流程（M1 的 PR1=Spec Review 是自建层） | 产品内 review 屏，非 PR 集成 | — | — |
| spec↔测试一致性 | `/speckit-analyze`（LLM）+ `/speckit-converge` 收敛检查（M4） | `/opsx:verify` 检查实现是否符合 spec（M6）；**PostHog更进一步：spec 场景即验收测试输入**（M2 场景表驱动 harness） | hooks 可挂自定义检查 | ✅ TDD 强制 harness（M1 的 apply 层含 evaluator subagent + eval-log 重试环） | QA agent 角色 |
| drift 检测 | converge 周期性做 | archive 时 delta 对比；`update` 检测指令文件 drift | — | — | — |
| **需自建的部分** | **确定性 CI 校验**（无 validate 命令）、PR 机器门禁 | spec↔代码一致性（除 verify 命令外）、评审 checklist 强制 | PR/CI 集成、确定性校验 | 团队版流程（M1 即自建成果） | 确定性校验、轻量化 |

### 2.3 评审 checklist（可复用样本）

M1 的两层评审清单（一手，原文归纳）：

**Spec PR（高标准，15-30 min）**：读 requirements+proposal+design+tasks → 拆解是否干净？依赖是否声明？CONTRACT 块是否清晰？→ 评审者问的两个关键问题：*agent 是实现了 spec 的意图还是字面措辞？eval 通过是因为 spec 好，还是 spec 模糊到不可能失败？*

**Code PR（轻量，查表不逐行）**：CI green（单测+集成+E2E）｜eval 各组过阈值（eval-log.md）｜无未解决 CRITICAL/HIGH｜manual-ops.md 完整｜PR 描述与 proposal 意图一致。原则原文："Do not do line-by-line code review. The harness + E2E CD pipeline is the primary quality gate."

**Archive 门禁（四层 gate 的第 4 层）**：spec delta 已合并入 `specs/<cap>/spec.md`｜pitfalls.md 已写｜新增能力才更新 README。

---

## 3. 迭代支持：需求变更时 spec 怎么改

| 工具 | 变更机制 | 机制细节（2026 版） |
|---|---|---|
| **OpenSpec** | **change-delta / proposal 流** | 变更=一个文件夹（proposal/design/tasks/delta specs），delta 用 `## ADDED / ## MODIFIED / ## REMOVED Requirements` 三节声明相对当前 spec 的差量；archive 时 delta 机械合并进主 spec、change 移入 `changes/archive/YYYY-MM-DD-<name>/` 留全审计轨迹。明确卖点："brownfield-first"、"两份 change 改同一 spec 文件但不同 requirement 即不冲突"（M6 原文）。2026 新增：`retire_capabilities` 显式退役能力、跨仓库 stores 引用、`skip_specs` 豁免 |
| **Spec Kit** | **三种 spec 持久化模型**（M4，2026 新增的显式指南） | ① Flow-forward：每个 feature 目录是历史记录，新需求开新目录，旧目录保留审计；② Living spec：`spec.md` 是契约，行为变了**先改 spec 再重生成 plan/tasks**，`/speckit.analyze` 查三者裂缝；③ Flow-back：实现中的发现可先落 tasks/代码，但要求"带回对齐"否则 spec 不可信。另：constitution 用治理 SemVer 演进（M3）；2026 新增 `/speckit-converge`（implement→converge 循环直到 Converged）与 extensions/presets 机制 |
| **Kiro** | **steering 更新 + spec 阶段检查点** | steering 文件（含 2026-08 起任意嵌套目录的 AGENTS.md）承载长期约定，随代码目录就近维护；spec 流在每阶段末出评审屏，逐行评论一次性回传 agent 修订（M8） |
| **Superpowers** | explore→propose→apply→archive 四阶段，archive 即把学到的 pitfalls 沉淀为 per-capability 文件（M1） |
| **BMAD** | 角色化敏捷流水线（PM/Architect/Dev/QA agents），变更走角色再生成文档（M10，二手） |

**哪种对"长期 brownfield + 多人迭代"最友好？** 证据指向 **OpenSpec 的 delta/archive 流**：
1. delta 是结构化、可机器校验的（MODIFIED 要求与主 spec 比对，M6）——Spec Kit 的三种模型靠 LLM analyze 兜一致性，确定性弱；
2. change 文件夹天然是评审单元，可直接挂成 PR1=Spec Review（M1 即在 OpenSpec 上建成团队流）；
3. `openspec/specs/` 始终是"当前行为"事实源 + archive 留"为什么改"的完整因果——正对 brownfield 最痛的"不知道系统现在到底怎么行为"；
4. OpenSpec 官方哲学即 brownfield-first，且 2026 的 stores 支持规划/代码分仓。

Spec Kit 的 Living-spec 模型是合格的替代（尤其已在 spec-kit 生态内的团队），代价是一致性依赖 `/speckit.analyze` 的 LLM 判断而非确定性校验；其 2026-06-19 的 constitution 实例（M3）证明治理文件工程化是可行的，但它是"规则的迭代"，不是"需求的迭代"。

---

## 4. 失败与教训（协作层面）

一手来源 M7（自述"distilled from real failures"）+ M1（自述瓶颈转移）+ M5（腐烂实例）：

1. **spec 退化成事后辩护 / 死文档**（M7 #1、#3）：先写代码后补 spec ⇒ "Specs become retroactive justifications"；测试悄悄加 spec 没写的行为 ⇒ "Specs stop being being the source of truth"。M5 是对偶面：spec 存在但从不校验 ⇒ 5 个文件腐烂，直到 CI 化才止住。
2. **"AI 原生"被误当成"放手不管"**（M7 #14）："Humans own intent; agents execute roles, not judgment"——让 agent 决定意图 ⇒ AI 发明行为、spec 与现实漂移。
3. **评审瓶颈是 SDD 团队的第一新瓶颈**（M1，一手判断）："Bottleneck shifts from implementation to spec quality and PR review bandwidth; Engineer role shifts from executor to judge"。对策也是 M1 首创的：两层评审（spec 高标准/code 查表）+ 不逐行读代码 + 任何非 owner 可批 + 共享文件冲突消除设计。
4. **流程形式化**：M7 #13"为了快而跳步骤"与 #6"design 明显就不必写"都是形式化反面的教训；但 OpenSpec 官方用 "Progressive Rigor / Lite spec 默认、大多数变更留 Lite"（M6）承认全量仪式会压垮团队——**迭代支持机制必须带豁免通道（skip_specs）才能存活**。
5. **实现者私自改 spec/tests**（M7 #7）："I adjusted the spec to match the code" ⇒ 事实源静默漂移；对策：只有 Spec Refiner 角色可改 spec，实现者必须停手上报。
6. **知识单点**（M7 #12）：流程靠"只有一个人知道怎么跟 AI 说" ⇒ 不可迁移；对策：把规则写成 repo 内文件（agents.md/templates/anti-patterns），而非口口相传。
7. **共享文件写冲突**（M1 §7）：4-6 人并行 archive 时 CLAUDE.md/README 成为合并冲突热点 ⇒ archive 只写 per-capability 文件 + 索引冻结 + 定期 maintenance PR。

---

## 5. 结论：5-20 人团队在已有代码库落地 SDD 的推荐做法（证据支持的版本）

**工具选型**（单一首选 + 一个可接受替代）：
- **首选 OpenSpec 做 spec 骨架**（brownfield-first、delta/archive 迭代机制、`validate --strict --json` 可直接进 CI——三项都是 2026-09 时点可验证的能力，M2/M5/M6）；在 10-20 人需要更重架构治理时叠加 Spec Kit 式 constitution（模板见 M3 实例，含治理 SemVer 与 Sync Impact Report）。
- Kiro 的 steering/嵌套 AGENTS.md 值得**借鉴其"目录级规则就近放置"**，但把整个团队流程押在 Kiro 上证据不足（未见公开多人布局案例）。

**工程控制清单**（全部有 2026 一手实例背书）：
1. CI 里加 `openspec validate --all --strict --json`，path-filter 到 spec 目录、钉 CLI 版本（PostHog 样板，M2）；再挂 `validate --archived` 防"带未完成任务归档"（M6 官方建议）。
2. 纯重构/工具类变更显式 `skip_specs: true`，给流程留活口防形式化（M6/M7 教训 4）。
3. 大特性走双 PR：PR1=Spec Review 锁需求/设计/任务，merge 后 tasks 冻结；PR2 只做查表式轻量评审（M1）。
4. spec 目录按能力/域切分、一能力一目录；依赖写 frontmatter `depends_on:`，>15 个能力再考虑图可视化（M1 的投资阈值表）。
5. archive 只写 per-capability 文件；CLAUDE.md/索引文件冻结为"仅 maintenance PR 更新"，消除并行写冲突（M1 §7）。
6. 规则/反模式/评审 checklist 沉淀为 repo 内文件（M7 模板、M1 pitfalls 机制），不靠口传。
7. spec↔代码一致性：能力 spec 的 Scenario 直接当验收测试输入（PostHog 模式，M2）；无此 harness 时至少用 OpenSpec `/opsx:verify` + 归档前人工核对。

**三个最可能的死法与对策**（对应 §4）：spec 腐烂 → 上 CI 校验（M5）；评审瓶颈 → 两层评审+一人一 topic+不逐行读码（M1）；流程形式化 → Lite spec 默认 + skip_specs 豁免（M6/M7）。

**证据缺口**（诚实声明）：Kiro/BMAD 侧缺公开的多人 spec 目录实例；Thoughtworks Radar 2026 对 SDD 的正式评级正文未能完整抓取（M9）；5-20 人区间（尤其 >6 人）没有比 M1 更大规模的自述案例——20 人以上只是 M1 模式的外推，不是实证。
