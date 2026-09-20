# GitHub Spec Kit（github/spec-kit）深挖

> **元数据**
>
> ```yaml
> source:
>   primary:
>     - https://api.github.com/repos/github/spec-kit          # GitHub REST API v3（仓库元数据）
>     - https://api.github.com/repos/github/spec-kit/releases  # release 历史
>     - https://api.github.com/repos/github/spec-kit/contributors
>     - https://raw.githubusercontent.com/github/spec-kit/main/README.md
>     - https://github.github.io/spec-kit/reference/integrations.html  # 官方文档
>   secondary:
>     - https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit
>     - https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html
>     - https://github.com/github/spec-kit/issues/75, /issues/1092, /issues/1401  # 官方 issue 中的批评
> accessed_at: 2026-09-20   # 所有 API 数字与页面均为该日观测
> trust_level: 高           # 核心事实全部来自 GitHub 官方 API / 官方 README / 官方文档站；
>                           # TW Radar 条目定性文字因 JS 渲染未提取（仅确认条目存在）；
>                           # 批评部分引用官方 issue 与二手评论，均标注。
> ```

---

## ① 一句话定位

Spec Kit 是 **GitHub 官方开源**的 Spec-Driven Development（SDD）工具包：一个 Python 写的 `specify` CLI（`uv tool install specify-cli`），把 constitution → spec → plan → tasks → implement 的一套 Markdown 模板与流程命令注入你已有的任意 AI coding agent（Claude Code、Copilot、Cursor、Gemini CLI 等 40+ 种），让 agent"先写规格、再写代码"。（来源：[GitHub API 仓库描述](https://api.github.com/repos/github/spec-kit)、[官方 README](https://raw.githubusercontent.com/github/spec-kit/main/README.md)，观测 2026-09-20）

## ② 起源与背景

- **GitHub 官方组织出品**，仓库创建于 **2025-08-21**（API `created_at`）。发布时定位是"实验性工具包"（experimental），配合 GitHub 说服行业从 vibe coding 转向 spec-first 的叙事；同月 AWS Kiro 也以 SDD 为卖点 preview，两者共同把 SDD 变成 2025 H2 的行业热词。
- **2026-08-21 发布 v1.0.0**（一周年当天），release notes 中明确阐述了"semver 的 1.0 承诺在 agent 时代不再重要"的立场——迁移成本已由 agent 承担，版本号退化为"一个好起点"（来源：[v1.0.0 release notes](https://github.com/github/spec-kit/releases/tag/v1.0.0)，观测 2026-09-20）。README 亦设有"Spec Kit 一周年 / project history"文档（v1.0.1 release notes 列出 docs: mark Spec Kit's first anniversary，#4260）。
- 从 v1.0 起产品结构明显扩张：README 现在提供**三条独立流程**——SDD（核心）、bug fixing（`specify extension add bug`）、idea assessment（`specify extension add assess`），后两者为可选 bundled extension，不是必经阶段。**语言**：Python；**License**：MIT。

## ③ 工作流与工件链

官方 README 的 SDD 主线（v1.x 口径）：

> **Constitution 每项目一次；specify → plan → tasks → implement → converge 每个功能一次。**

```text
/speckit-constitution   # 项目级原则：代码质量、测试、可维护性（写入 constitution.md）
/speckit-specify        # what & why → spec.md（需求规格）
/speckit-plan           # how → 技术选型与 plan.md（如 Vite + SQLite）
/speckit-tasks          # 拆解为 tasks.md（可执行任务清单）
/speckit-implement      # 按任务实现
/speckit-converge       # 收敛检查；重复 implement → converge 直到报告 Converged
```

可选质量门：clarify（澄清）、checklist、consistency analysis（一致性分析）。工件全部是项目内的 Markdown 文件（`.specify/` 目录树），人可 review、可 diff、可改——"Resolve unknowns by refining the existing Markdown artifacts directly, rather than regenerating whole stages"。（来源：官方 README + [docs: evolving-specs](https://github.github.io/spec-kit/guides/evolving-specs.html)）

**specify CLI 的职责**：`specify init <project> --integration <agent>` 为所选 agent 生成命令/skill 文件；`specify integration install/use/switch/upgrade/status` 管理多 agent 共存（0.8.5 起支持受控 multi-install，含 SHA-256 追踪、改装文件保护）；`specify extension/preset add` 装扩展与预设；`specify artifact` 内省（v1.0.7 新增，#4305）。

**支持的 agent（官方 integrations 页，观测 2026-09-20）**：内置 **40+ 集成**，其中声明 multi-install safe 的 24 个。包括：Claude Code、GitHub Copilot（默认 skills 模式，装 `.github/skills/`）、Codex CLI、Cursor、Gemini CLI、Antigravity、Cline、Devin、Factory Droid、Goose、Qwen Code、Kimi Code、Kiro CLI、Lingma（阿里）、CodeBuddy（腾讯）、Trae、Zed、IBM Bob、RovoDev（Atlassian）、Tabnine、Junie、DeepSeek Harness（`dsh`，v1.0.4 加入）等；未列出的 agent 可用 `--integration generic --integration-options="--commands-dir ..."` 自行接入。命令拼写因 agent 而异（`/speckit-specify`、`/speckit.specify`、`$speckit-specify`、`/skill:speckit-specify`）。（来源：[Supported AI Coding Agent Integrations](https://github.github.io/spec-kit/reference/integrations.html)）

**可定制性**：extensions（加能力）、presets（改行为）、workflows（自动化步骤）、bundles（打包角色化配置），另有社区 catalog——第三方 extension/preset 数十个（release notes 可见 Azure Cosmos DB、Figma、Linear、BDD、ADR 等条目持续进出）。

## ④ 数据指标（观测 2026-09-20，GitHub API 直读）

| 指标 | 数值 | 备注 |
| --- | --- | --- |
| Stars | **138,034** | `stargazers_count` |
| Forks | **12,366** | `forks_count` |
| Watchers | 706 | `subscribers_count` |
| Open issues | 307 | `open_issues_count` |
| Contributors | **100+** | contributors API `per_page=100` 满页；头部为 GitHub 员工 localden（361 次）、mnriem（336 次），社区长尾大（jawwad-ali 142、Quratulain-bilal 94 等） |
| 创建时间 | 2025-08-21 | `created_at` |
| 最近 push | 2026-09-18 | `pushed_at`，持续活跃 |
| 最新 release | **v1.0.8**（2026-09-17） | v1.0.0（2026-08-21）→ v1.0.8，约**每周一版** |

**交叉验证**：本仓库研究文件 `../sdd-tooling-landscape-2026-09.md`（观测同日）记录 138,033 stars / 12,366 forks / 307 open issues / 706 watchers——stars 差 1 为当日实时增长，其余完全一致；forks/issues/watchers 与本次 API 二读一致。数字可信。官方 Pages 站落地页在 v1.0.1 更新过 landing stats（release notes #4251），属自述口径，本文以 API 为准。

## ⑤ 采纳与影响力

- **ThoughtWorks Radar 有独立条目 "GitHub Spec Kit"**（languages-and-frameworks 象限，https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit ，观测 2026-09-20 确认条目存在；条目定性文字为 JS 渲染未能提取，ring 状态待补）。同期 OpenSpec 也被收录——TW 认可 SDD 工具这一品类本身。
- **大厂背书**：GitHub（Microsoft）官方开源并持续投入；集成列表本身就是一份"厂商背书链"——IBM Bob、Atlassian RovoDev、阿里 Lingma、腾讯 CodeBuddy、Google Gemini/Antigravity、字节 Trae 等或被 Spec Kit 集成、或主动适配。
- **社区案例**：社区 extension/preset/bundle catalog 已成型（数十个第三方扩展）；第三方教学与评测文章大量出现（Scott Logic《Putting Spec Kit Through Its Paces》、腾讯云社区选型对比文等）。Cory House（React 训练师）公开记录用 Spec Kit 实现 feature 的体验（coryhouse.dev，2025-09）。
- **参照系**：在 SDD 品类中体量第一梯队（vs OpenSpec ~70k、BMAD ~53k，均 API 观测 2026-09-20，详见 `../sdd-tooling-landscape-2026-09.md`）。

## ⑥ 趋势判断：上升

依据（均为一手源）：

1. **速度**：创建 13 个月达 138k stars，SDD 品类中非个人项目里最快之一（API 直读）。
2. **节奏**：v1.0 以来周级 release（2026-08-21 → 09-17 共 8 版），`pushed_at` 距观测日仅 2 天。
3. **边界扩张**：从单一 SDD 流程扩张为 SDD + bug fixing + idea assessment 三条流程，加 extension/preset/workflow/bundle 四层定制体系——工具在向"平台"演化。
4. **组织投入**：GitHub 官方维护、专职员工居贡献榜头部（localden/mnriem），v1.0.0 表明有长期主义叙事。
5. **生态外溢**：40+ agent 集成、社区 catalog、被 TW Radar 收录、带动 OpenSpec 等同类项目。
   证据强度：**强**（指标全部 API 可复核）。

## ⑦ 批评与局限

- **"生成的文字量 = 工作的错觉"**：官方 issue [#75](https://github.com/github/spec-kit/issues/75)（"SpecKit creates the illusion of work, generating a bunch of text"）——spec/plan/tasks 全套文档对小改动是重仪式。
- **上下文窗口开销**：官方 issue [#1401](https://github.com/github/spec-kit/issues/1401)——命令与工件每轮消耗大量 context window，长会话下挤压真正代码空间。
- **架构决策权问题**：官方 issue [#1092](https://github.com/github/spec-kit/issues/1092)（High Level Design Concerns）——模板预设了架构产物形态，复杂系统的设计未必能从 spec 线性推导。
- ** Opinionated / 仪式重**：marmelab《[Spec-Driven Development: The Waterfall Strikes Back](https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html)》（2025-11-12，HN 225 分 191 评）与 Scott Logic 同题评测把它类比为"瀑布回归"——spec 先行与迭代发现存在张力。（二手评论，标注）
- **spec 冗长难 review**：constitution + spec + plan + data-model + tasks 多件套对小团队/小 feature 是净负担；官方自己也承认需要 clarify/checklist 等额外门控来补质量。
- **版本观激进**：v1.0.0 release notes 公开宣告"semver 不再承诺稳定性，靠 agent 适应 breaking change"——对自动化程度低的团队是风险。
- 依赖链：需要 Python 3.11+ / uv；多 agent 共存的 multi-install 规则较复杂（integration 文档近万字）。

## ⑧ 适用场景与不适用

**适用**：
- AI agent 主导编码、需求可预先写清楚的 feature 开发（greenfield 或边界清晰的新功能）；
- 需求模糊、需要 clarify 门控把"人机对齐"显式化的团队；
- 想要可 review、可 diff 的规格工件沉淀（合规、审计、交接友好）；
- 多 agent 并用的团队（spec 工件是 agent 无关的，换 agent 不换 spec）。

**不适用**：
- 微小改动、bug 顺手修——全套仪式成本大于收益（官方因此把 bug fix 拆成独立轻流程）；
- 探索性原型 / spike，需求本身要在写代码中才被发现；
- 强架构不确定的系统：模板推导不出真正的架构决策（issue #1092 场景）；
- 团队已有重规格流程（如严格 DO-178/医疗文档体系）——Spec Kit 的模板格式未必兼容，定制成本高。

## ⑨ 来源列表（URL + 访问日期，均为 2026-09-20）

| # | 来源 | 类型 |
| --- | --- | --- |
| 1 | https://api.github.com/repos/github/spec-kit | 一手（API） |
| 2 | https://api.github.com/repos/github/spec-kit/releases?per_page=10 | 一手（API） |
| 3 | https://api.github.com/repos/github/spec-kit/contributors?per_page=20&anon=true | 一手（API） |
| 4 | https://raw.githubusercontent.com/github/spec-kit/main/README.md | 一手（官方 README） |
| 5 | https://github.github.io/spec-kit/reference/integrations.html | 一手（官方文档） |
| 6 | https://github.github.io/spec-kit/guides/evolving-specs.html | 一手（官方文档，经 README 引用） |
| 7 | https://github.com/github/spec-kit/releases/tag/v1.0.0 | 一手（release notes） |
| 8 | https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit | 二手（TW Radar；条目存在性确认，定性文字未提取） |
| 9 | https://github.com/github/spec-kit/issues/75 , /issues/1092 , /issues/1401 | 一手（官方 issue，批评部分） |
| 10 | https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html | 二手（评论） |
| 11 | https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html | 二手（评论） |
| 12 | 本仓库交叉验证：`02_research/spec_driven_development/sdd-tooling-landscape-2026-09.md`（观测同日） | 内部 |

> 未决项：TW Radar 该条目的 ring 状态（Assess/Trial 等）因页面 JS 渲染未提取到，后续可用 TW Radar JSON/移动端源补一次回源。
