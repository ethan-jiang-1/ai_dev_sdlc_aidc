# OpenSpec 深挖：AI 编码助手的规格驱动开发（SDD）工具

> **元数据**
>
> - **对象**：OpenSpec（Fission-AI/OpenSpec），MIT 许可，TypeScript CLI
> - **观测日期**：2026-09-19（GitHub API / npm API / 官方 README 与 docs 均为此日抓取）
> - **一手源**：GitHub REST API、raw.githubusercontent.com 上的 README 与 docs/（supported-tools.md、opsx.md、overview.md）、npm downloads API、ThoughtWorks Radar 官网
> - **证据强度**：数据指标部分全部来自一手 API（强）；雷达条目部分一手页面只能确认条目存在与主题引用，具体 ring 无法从抓取页面确认（中，文中已标注）
> - **交叉验证**：star 数与第三方 2026-06-22 核查（Security Boulevard/SSOJet）交叉比对；spec-kit 数字同步抓取做参照

---

## ① 一句话定位

OpenSpec 是一个轻量的**规格驱动开发（Spec-Driven Development, SDD）CLI**：在你的仓库里建立 `openspec/` 目录，用纯 Markdown 的 **proposal → specs → design → tasks** 工件链先与 AI 对齐"要做什么"，再让 30+ 种 AI 编码助手通过 slash 命令/技能执行，核心机制是**变更增量（change delta）**——每个变更只写对规格的 ADDED/MODIFIED/REMOVED 差量，归档时合并回真相规格，因此特别适合存量（brownfield）代码库。官方自述哲学："fluid not rigid, iterative not waterfall, built for brownfield not just greenfield"。

## ② 起源与背景

- **创建时间**：GitHub 仓库创建于 **2025-08-05**（API `created_at`），由 **Fission AI**（GitHub org，ID 203414896）维护；核心发起人 TabishB（X: @0xTab），至今仍是最大贡献者（519 次提交，占绝对主导）。
- **出身**：Fission AI 是一家 AI 工程咨询/产品公司，OpenSpec 源于其在真实项目中"AI 编码助手需求只活在聊天记录里导致结果不可预测"的痛点，把规格层做成开源工具。MIT 协议，npm 包 `@fission-ai/fission-ai/openspec`（`@fission-ai/openspec`），要求 Node ≥ 20.19。
- **演进速度极快**：截至观测日已有 52 个 tag、最新 release v1.13.1（2026-09-17，"Hardened CLI, safer archives"），近三个月每月都有功能 release（v1.7→v1.13：Spec Diffs、Batch Status、Zed 支持、Findings Reports 等）。
- **重大重构**：项目中途从"硬编码在 TypeScript 里的 legacy 工作流"迁移到 **OPSX** 工作流——指令模板（schema.yaml + templates/*.md）开放可编辑，用户可自定义工件与依赖，官方称其为现在的标准工作流。

## ③ 工作流与工件链

**两个目录、一次循环**（官方 overview.md 的心智模型）：

```
openspec/
  specs/     ← 真相（source of truth）：系统当前行为的规格，按域组织
  changes/   ← 提案：一个变更一个文件夹
```

- **工件链**：`proposal（为什么） → specs（改什么，增量） → design（怎么做） → tasks（步骤） → implement`。依赖是"使能器不是门禁"（enablers, not gates）——任何工件可随时回头改，无刚性阶段闸门。
- **变更增量（change delta）**：变更内不重写全量规格，只写 `## ADDED Requirements` / `MODIFIED` / `REMOVED` + Given/When/Then 场景。这是它区别于"先给 5 万行老系统写全量规格"的关键，也是官方声称适合 brownfield 的机制依据。
- **归档闭环**：`/opsx:archive` 把增量合并回 `specs/`，变更文件夹带日期戳移入 `changes/archive/`——规格永远是"当前事实"。
- **命令族**：core profile = `/opsx:explore`（无风险地与 AI 先想清楚，可选）、`propose`、`apply`、`update`、`sync`、`archive`；扩展 profile 另有 `new/continue/ff/verify/bulk-archive/onboard`。
- **Agent 分发**：`openspec init` 按所选工具写入各自路径的 skill/command 文件——官方 supported-tools.md 列出 **30+ 工具**（Claude Code、Cursor、Codex、Gemini CLI、GitHub Copilot、Cline、Kiro、Amazon Q、Devin、Zed、Kimi Code、Qwen Code、Lingma、OpenCode、iFlow、Antigravity、Factory Droid 等），同一命令在不同工具里拼写不同（`/opsx:propose` = Cursor 的 `/opsx-propose` = Codex 的 `$openspec-propose`）。分发靠 skill/command 文件而非 MCP——与当前"能 CLI 就不 MCP"的行业倾向一致。
- **规模化（beta）**：**Stores** 把同一套 `openspec/` 形状放进独立"规格仓库"，git push 共享，解决跨仓库特性、平台团队持有规格、先规划后写码的团队场景。

## ④ 数据指标（观测日期：2026-09-19，均为 GitHub/npm API 一手抓取）

| 指标 | 数值 | 备注 |
|---|---|---|
| Stars | **69,640** | 交叉验证：第三方 2026-06-22 核查为 55.9k → 约 3 个月 +24%，增速仍陡 |
| Forks | 4,771 | |
| Contributors | 100（per_page=100 拉满，实际可能略多） | 但提交高度集中：TabishB 519 + clay-good 144，bots 占其余大头 |
| Open issues（含 PR） | 241 | |
| Watchers/subscribers | 286 | |
| 创建时间 | 2025-08-05 | 距观测约 13.5 个月 |
| 最新 commit | 2026-09-17 | 活跃 |
| 最新 release | v1.13.1（2026-09-17） | 52 个 tag |
| npm 月下载 | **1,760,795**（2026-08-21 ~ 2026-09-19） | npm downloads API |
| 语言/许可 | TypeScript / MIT | topics：spec-driven-development、sdd、context-engineering 等 |
| 参照：github/spec-kit | 138,035 stars / 12,366 forks / 创建 2025-08-21 | 同期竞品，体量约为 OpenSpec 的 2 倍 |

> 口径说明：open_issues_count 是 issues+PR 合计；contributors 上限 100 表示至少 100 人。数字会漂移，引用请注明本观测日期。

## ⑤ 采纳与影响力

- **ThoughtWorks Technology Radar**：thoughtworks.com 官网存在 OpenSpec 专属 Radar 条目页（[tools/openspec](https://www.thoughtworks.com/radar/tools/openspec)，多语言镜像），**确认已入雷达**。具体 ring（Assess/Trial）在可抓取的页面内容中未能确认，此处存疑待查。可确认的是：**Vol.34（2026-04）** 的主题综述明确点名 OpenSpec——在"给编码 agent 上缰绳（coding agent harnesses）"主题下，把它与 GitHub Spec Kit 并列为 SDD 框架的代表，归入 **feedforward 控制**（先给 agent 结构化的规划/设计/实现工作流）一类；同卷亦指出 "spec-driven development" 一词存在语义扩散（semantic diffusion）问题。
- **生态位**：在第三方横向评测（SSOJet 2026-06 核查）中被列为七种 SDD 工具之一，类别是"change-based spec CLI"，卖点为"iterative, proposal-driven changes"；与 Spec Kit（agent-agnostic CLI 锚点）、Kiro（spec-first IDE）、Tessl（spec 注册表）形成不同象限。
- **社区**：官方 Discord、X 更新频道、community schemas（第三方 schema bundle 目录，对标 spec-kit 的 extensions 目录）。OpenSpec 用自身管理自身开发——仓库里就有 live specs 与 in-flight changes 可当真实样例。

## ⑥ 趋势判断：上升

依据：

1. **增长曲线未衰减**：55.9k（2026-06-22，第三方核查）→ 69.6k（2026-09-19，一手 API），13 周净增约 1.4 万星，斜率高于多数同期工具；
2. **分发面持续扩张**：v1.10（2026-08）新增 Zed，v1.8 新增多 agent 支持，受支持工具清单从 README 口径的 "25+/30+" 持续变大，几乎每个新冒头的 agent CLI 都会很快进清单——它已事实上成为 SDD 层的"兼容性标准"之一；
3. **工程活跃且产品化**：月度 release 节奏、匿名遥测、Stores（beta）向团队/企业场景延伸、自家 dogfooding，均超出个人项目的生命周期特征；
4. **行业叙事加持**：ThoughtWorks Radar Vol.34 把 SDD 框架（点名 OpenSpec）纳入 "coding agent harness" 的 feedforward 控制主线——SDD 从"新词"进入咨询机构的工程方法论叙事；
5. **需求侧顺风**：与雷达同卷的 "codebase cognitive debt"、"agent instruction bloat" 等 Caution 条目，正是 OpenSpec 这类规格层的反向需求来源。

风险保留：stars 是弱指标；项目提交高度集中于单一发起人，核心人物变动是单点风险。

## ⑦ 批评与局限

- **流程开销真实存在**：官方自己承认"对真正的一次性一行修复，仪式感可能不值"。小事强套 proposal/delta/tasks 是负收益，需要团队自行判断粒度。
- **无强制力**："enablers not gates" 意味着没有任何机制阻止变更范围蔓延或规格与实现漂移，纪律成本被转移给使用者；归档前 specs/changes 可能长期失同步（项目为此陆续加了 Spec Diffs、Batch Status、apply warnings 等补救功能，侧面印证这是真实痛点）。
- **Markdown 规格的验证缺口**：规格是自然语言 + Given/When/Then，本身不可执行；"规格驱动"并不自动等于"实现符合规格"，最终仍靠人工 review 和测试兜底。
- **单人项目风险**：提交量高度集中于 TabishB，bus factor 偏低（与 spec-kit 的 GitHub 背书形成对比）。
- **指令注入面**：向每个 agent 的 `.claude/.cursor/...` 目录写 skill/command 文件，属于对 agent 上下文的批量注入；v1.13 主打 "hardened CLI, safer archives" 说明工具自身也在补安全债。
- **语义扩散背景**：ThoughtWorks Vol.34 已指出 "spec-driven development" 术语被滥用，选型时需区分"真把 spec 变成实现约束的工具"与"只是多了几个 Markdown 模板"。

## ⑧ 适用与不适用

**适用**：
- brownfield/存量代码库上的 AI 迭代开发——delta 机制是为此设计的（官方明示的核心差异化）；
- 团队异构 agent 环境（一人 Claude Code、一人 Cursor、CI 里 Codex），需要一份规格被所有工具读；
- 需求值得先对齐的中型以上特性：可 review 的 proposal/delta 包替代考古聊天记录；
- 跨仓库特性/平台团队持有规格（Stores，beta）。

**不适用**：
- 一次性脚本、一行修复、纯探索式原型（explore 命令可覆盖一部分，但整套工件链是浪费）；
- 需要**可执行/可验证规格**的强合规场景（OpenSpec 规格不可执行，需另配验收测试或转向形式化方法）；
- 已深度绑定单一 IDE 且要开箱即用阶段闸门的团队（Kiro 更对口）；或偏好 rigid 多阶段流程、想要 GitHub 官方背书的团队（Spec Kit 更对口）。

## ⑨ 来源列表

一手源（观测 2026-09-19）：
1. GitHub API repo 元数据：https://api.github.com/repos/Fission-AI/OpenSpec（stars/forks/created_at/license/topics）
2. GitHub API releases / contributors / tags / commits：同 repo 下 `releases`、`contributors`、`tags`、`commits` 端点
3. 官方 README（main 分支）：https://github.com/Fission-AI/OpenSpec/blob/main/README.md
4. 官方 docs：docs/overview.md（specs/changes 双目录、delta、enablers-not-gates）、docs/opsx.md（OPSX 工作流）、docs/supported-tools.md（30+ 工具清单与调用拼写）
5. npm downloads API：https://api.npmjs.org/downloads/point/last-month/@fission-ai/openspec
6. ThoughtWorks Radar 条目页：https://www.thoughtworks.com/radar/tools/openspec（ring 未能在可抓取内容中确认）

二手/交叉验证源：
7. SSOJet《7 Spec-Driven Development Tools》（Security Boulevard，2026-06-24，数据核查日 2026-06-22；OpenSpec 55.9k stars、Spec Kit 115k）：https://securityboulevard.com/2026/06/7-spec-driven-development-tools-spec-kit-kiro-openspec-tessl-more/
8. ThoughtWorks Technology Radar Vol.34 综述（GeekNews 法语摘译，2026-04-17；含 "coding agent harnesses / feedforward" 主题点名 OpenSpec 与 Spec Kit）：https://fr.news.hada.io/topic?id=28625 、原文 https://www.thoughtworks.com/radar
9. GitHub API github/spec-kit 元数据（对照数字，2026-09-19 抓取）：https://api.github.com/repos/github/spec-kit
