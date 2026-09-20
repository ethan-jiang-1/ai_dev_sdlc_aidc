# BMAD-METHOD 深挖研究

> **元数据**
> - 观测日期：2026-09（GitHub API 与官方文档拉取于 2026-09-20）
> - 对象：[bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)（Breakthrough Method for Agile AI-Driven Development）
> - 一手源：GitHub REST API（repo / releases / contributors / tags）、仓库 LICENSE 与 README（main 分支）、官方文档站 docs.bmad-method.org
> - 交叉验证：star/fork 数与 release 列表均直接取自 GitHub API；license 同时核对 README 徽章、LICENSE 文件正文与 GitHub API 的 license 字段（三方，见 §4 末尾）
> - 定位：本文属实践层沉淀（`03_practice/spec_driven_development/tools/`）

---

## ① 一句话定位

BMAD-METHOD 是一个开源（MIT）的**多 agent 角色化敏捷 AI 开发方法论 + 可安装的 skill 包**：把"一个想法/变更请求"通过 Analyst → PM → Architect → Dev 等 agent 角色与结构化工作流，变成带显式决策记录（PRD、架构、故事）的规划工件，再驱动 AI 编码工具实现——核心卖点是"过程可裁剪（right-sized process）+ 决策上下文可跨会话延续"。

## ② 起源与背景

- 仓库创建于 **2025-04-13**，由 BMad Code, LLC（个人品牌 "BMad Code"，主创 bmadcode/破釜号 "Mike" 社区）发起，属 2025 年"agentic coding 方法论"浪潮中最早成体系的开源项目之一。
- 出发点（官方 README "Why BMad?"）：编码助手擅长实现，但常把**未言明的假设直接变成代码**；BMad 用 agent 与结构化工作流把重要决策显式化，并作为上下文带入后续工作。
- 版本演化（tag 佐证）：
  - **v4.x**（2025 年，最新 v4.44.3）：经典形态——markdown 人格化 agent（PM/Architect/Dev/QA）+ 两阶段"规划 → 开发循环"，依赖 IDE 内复制粘贴或简单编排，在 2025 年病毒式传播。
  - **v5.x**（过渡版，v5.0.0 → v5.1.3）：安装与模块化改造的过渡带。
  - **v6.x**（2026 年重构，当前最新 **v6.12.0**，发布于 2026-09-04）：彻底重写为 **skills 架构**（`npx skills add` / Claude Code / Codex 插件市场安装），工作流重组为 Clarify → Plan → Build & Verify → Learn 的"交付环（delivery loop）"，并新增 `bmad-spec`、`bmad-build` 等标准化 skill；文档导航中已出现 **v7 previews** 测试入口，说明重构仍在快速迭代。

## ③ 工作流与工件链

### Agent 角色（v6，官方 docs/reference/skills-and-agents）

| Agent | Skill ID | 职责（菜单码） |
| --- | --- | --- |
| Analyst (Mary) | `bmad-agent-analyst` | 头脑风暴、市场/领域/技术研究、技术选型、竞品拆解、产品 brief、PRFAQ 挑战、项目上下文 |
| Product Manager (John) | `bmad-agent-pm` | 创建/更新/校验 PRD、epic 与故事拆分、实现就绪度检查、纠偏（correct course） |
| Architect (Winston) | `bmad-agent-architect` | 架构脊柱（architecture spine）、实现就绪度 |
| Developer (Amelia) | `bmad-agent-dev` | 构建（BD）、QA 测试生成、代码评审（CR）、sprint 计划、epic 回顾 |
| UX Designer (Sally) | `bmad-agent-ux-designer` | UX 设计 |
| （Technical Writer "Paige" 官方注明 hiatus；企业级测试由独立模块 Test Architect / TEA 承担） | | |

核心模块另含 8 个跨项目通用 skill：`bmad-help`（检查工件并推荐下一步）、`bmad-advanced-elicitation`（具名推理方法的二次审视）、`bmad-review`、`bmad-customize`、`bmad-brainstorming`、`bmad-deep-recon`、`bmad-forge-idea`、`bmad-party-mode`（多 agent 讨论）等。

### Phase 流程与产物链（v6 交付环）

1. **Clarify**（模糊念头入口）：brainstorming / deep-recon / forge-idea → 产出 product brief、研究纪要。
2. **Plan**（想法已清晰入口）：官方文档《Choose a Planning Path》给出裁剪判据——**意图是否已被良好定义**：
   - 已定义 → 直接 `bmad-spec` 生成规格（官方注明输入上限约"几万 token / 40 页文档"），小规格直接 `bmad-build`；epic 级规格走 Story Breakdown + 每故事一次 Build。
   - 未定义 → 选用探索/验证、研究决策、需求与规格、UX 与架构、故事拆分等**互相独立（非阶段制）**的规划 skill，产物包括 PRD、架构文档、故事列表、epic。
3. **Build & Verify**：`bmad-build` 实现 → review / walk-through / 测试（QA 生成 e2e 测试，TEA 模块做企业级测试架构）。
4. **Learn**：epic 回顾（retro）、纠偏，回流 Plan；另有 **BMad Loop** 模块可"无人值守跑完整个 epic 的 build-verify-retro"。

工件链：brief → PRD（含 epic/story）→ 架构文档 → 规格书（spec）→ 故事 → 实现 + 评审记录 → 回顾/项目上下文。官方强调工件可脱离 BMad 单独使用（"Start anywhere… carry its briefs, specifications, and architecture into your existing delivery workflow"）。

### 生态模块（官方 README）

BMad Builder（自建 skill/工作流/agent）、Creative Intelligence Suite、Test Architect（TEA）、BMad Loop、Game Dev Studio；另有 Web Bundles 把规划工作流打包成 Gemini Gem / ChatGPT GPT 在网页端做规划、再带回 IDE 实现。

### 可裁剪性（right-sized process）

官方明确三档：小变更直达 Build（"明显的低风险改动甚至不需要 BMad"）；中型变更走 spec → build；大型动议补全规划链。同一方法覆盖"周末原型"到"有多年历史的遗留系统"（现有代码库有专门入门路径：先建立"已验证上下文"）。

## ④ 数据指标（观测日期 2026-09，GitHub API 2026-09-20）

| 指标 | 数值 | 备注 |
| --- | --- | --- |
| Stars | **53,267** | |
| Forks | **6,009** | |
| Watchers (subscribers) | 418 | |
| Open issues（含 PR 计数） | 66 | 项目用 issue 跟踪较克制 |
| 仓库创建 | 2025-04-13 | |
| 最近 push | 2026-09-20（观测当日仍活跃） | |
| 最新 release | v6.12.0（2026-09-04） | v6.11.0（2026-08-10）、v6.10.0（2026-07-03）：约 4–6 周一个 minor 的稳定节奏 |
| Contributors（前 10） | alexeyv 662、bmadcode 188、semantic-release-bot 91、muratkeremozcan 61、dracic 23 … | 第 10 名约 13 次提交，长尾contributors 规模中等 |
| Topics | agile、ai、context-engineering、sdlc、spec-driven-development | 官方自我归类即含 spec-driven-development |
| License | 见下 | |

**License 核实（任务点）**：GitHub API 的 license 字段返回 `NOASSERTION`（"Other"），**非标准标识**；但逐一核对：README 徽章写 MIT，仓库 LICENSE 文件正文为标准 MIT 文本（"MIT License, Copyright (c) 2025 BMad Code, LLC"，仅附加一句指向 CONTRIBUTORS.md 的署名说明）。结论：**实质是 MIT**，GitHub 未自动识别大概率因文件附加了署名段落；README 同时声明 "BMad / BMAD-METHOD" 是 BMad Code, LLC 的**商标**（TRADEMARK.md）。使用其名称做二次分发/产品命名时注意商标条款，代码使用基本无 MIT 之外的负担。

## ⑤ 采纳与影响力

- 5.3 万 star、6 千 fork，在"AI 开发方法论"类仓库中位居头部（同类多为文章/awesome 列表，BMad 是少数带可执行工具链的方法论仓库）。
- 传播渠道：Discord 社区、YouTube 教程与 master class、官方博客 bmadcode.com；v4 时期即被多家 AI coding newsletter 与 YouTube 博主作为"多 agent SDLC"代表案例介绍。
- 工程化采纳信号：安装面覆盖 Claude Code、Cursor、Windsurf、Codex、Cline、Amp 等主流工具；企业向加购模块（TEA 测试架构）与"Plan Inside an Organization"文档（PRD 需多人审批、多工程师并行）表明有团队级使用诉求。
- 官方特别声明"free and open source, no paywalled workflows or gated community"，以开源社区运营为核心策略（变现靠 coffee 赞助/企业赞助）。

## ⑥ 趋势判断：平台期偏上升

依据：
1. **增速仍健康**：2025-04 创建到 2026-09 约 17 个月即 53k star，且观测当日仍在 push、release 保持 4–6 周节奏——不是停滞项目。
2. **架构自我革新**：v6 整体迁移到 skills/插件生态并开始 v7 preview，说明团队在追平 2026 年"skills 成为 agent 工具分发标准形态"的行业变化，产品仍在生长而非维护模式。
3. **生态外溢**：从单体仓库扩展为多模块生态（Loop、TEA、Game Dev、Builder）+ 多语言文档（中/韩/越/法/捷克），投入在加深。
4. **限制因素**：方法论赛道竞争者众（spec-kit、各类 SDD 框架、IDE 原生规划功能）；多 agent 重流程范式本身见顶争论增多（见⑦），增长斜率较 2025 年 v4 病毒期大概率已放缓——综合判断为**高位平台期、偏上升**，而非爆发期。

## ⑦ 批评与局限

- **重流程 / 学习曲线**：v4 时代"两阶段+多文档"被普遍反映对小团队过重；v6 用 right-sizing 缓解，但 agent/skill/工作流/模块的概念栈仍陡，文档专设 "Customize BMad""Adopt BMad Across a Team" 等章节侧面印证。
- **token 成本**：多 agent + 多轮 elicitation + 大工件链意味着显著高于"直接让 AI 写"的 token 消耗；官方对 `bmad-spec` 输入上限（约 40 页）的自述也暴露了上下文窗口的现实约束。
- **人格化 agent 的实与虚**：所谓"多 agent 协作"本质是同一模型加载不同 persona/skill，并非独立进程；party-mode 等功能的增益依赖模型能力，评审者（含社区讨论）指出其"仪式感大于机制"的部分。
- **主创集中**：贡献高度集中于 alexeyv 与 bmadcode 两人（合计 850/约 1000+ 提交），bus factor 偏低，方法论演进方向由单组织主导。
- **版本断裂**：v4 → v6 是破坏性重写，早期教程/工件格式大量失效，社区存量内容与新版存在兼容混乱（官方需提供 deprecated names 说明）。
- **依赖宿主工具**：作为 skill 包，体验强依赖所装 IDE 对 skills 的支持质量，本身不提供执行运行时（除 BMad Loop 模块）。

## ⑧ 适用与不适用场景

**适用**：
- 从零起步的新产品/原型，需要 PRD→架构→故事的完整规划链并希望决策可追溯；
- 遗留代码库改造（官方有专门"先建立已验证上下文"路径）；
- 已采用敏捷叙事、希望 AI 参与但保留 PM/架构师把关的中小团队；
- 单人全栈者用 agent 角色替代缺失的职能视角（产品/架构/UX/测试）。

**不适用**：
- 一次性脚本、小修小补（官方自己都说"不需要 BMad"）；
- 强合规/固定流程的企业 SDLC（需大改其工作流才能对齐）；
- 追求最低 token 成本、全自动无人干预的流水线（BMad 的价值恰在人在环的显式决策）；
- 对多 agent 并行执行有硬性要求的场景——BMad 核心是 persona + 工件，不是分布式 agent 运行时。

## ⑨ 来源列表

1. GitHub API — repo 元数据：https://api.github.com/repos/bmad-code-org/BMAD-METHOD （2026-09-20 观测：stars 53,267 / forks 6,009 / created 2025-04-13 / license NOASSERTION）
2. GitHub API — releases：https://api.github.com/repos/bmad-code-org/BMAD-METHOD/releases （v6.12.0, 2026-09-04）
3. GitHub API — contributors：https://api.github.com/repos/bmad-code-org/BMAD-METHOD/contributors
4. GitHub API — tags（v4.41–v6.12 版本序列）：https://api.github.com/repos/bmad-code-org/BMAD-METHOD/tags
5. 仓库 README（main）：https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md （定位、生态模块、安装路线、license 声明、商标声明）
6. 仓库 LICENSE（main）：https://github.com/bmad-code-org/BMAD-METHOD/blob/main/LICENSE （MIT 文本 + 署名附注）
7. 官方文档《Choose a Planning Path》：https://docs.bmad-method.org/plan/choose-a-planning-path/ （right-sizing、bmad-spec 输入上限、epic/story 分流）
8. 官方文档《Reference: Skills and Agents》：https://docs.bmad-method.org/reference/skills-and-agents/ （五 agent 及菜单码、核心 8 skills、skills 目录映射、Paige hiatus、v7 previews 入口）
