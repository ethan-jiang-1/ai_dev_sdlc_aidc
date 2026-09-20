# Superpowers（obra/superpowers）深挖研究

> **元数据**
>
> | 字段 | 值 |
> |---|---|
> | 观测日期 | 2026-09-20（所有数据均为此日实测） |
> | 仓库 | https://github.com/obra/superpowers |
> | 作者 | Jesse Vincent（GitHub: obra）/ Prime Radiant |
> | 一手源 | GitHub API（repos + search 双端点交叉）、官方 README（main 分支）、作者发布博文（blog.fsck.com, 2025-10-09） |
> | 版本 | 最新 release v6.4.1（2026-09-19 发布） |
> | License | MIT |
> | 本文归属 | `02_research/spec_driven_development/tools/` |

---

## ① 一句话定位

Superpowers 是一套**可组合的 agent skills + 完整软件开发方法论**（官方自述 "An agentic skills framework & software development methodology that works"）：通过 session 启动注入的 bootstrap 让编码 agent **强制**走 brainstorm → design → plan → TDD 实现 → subagent 执行 → code review → 收尾合并的流程。**注意：它不是传统意义上的 SDD 工具**（没有 spec 文件格式校验器、没有生成器/CLI 流水线），而是"以 skills 形态分发的行为方法论"——spec/plan 是它工作流中产出的 Markdown 工件，而非被工具链消费的机器可执行契约。详见⑧中的差异辨析。

## ② 起源与背景

- **作者**：Jesse Vincent（obra），知名开源老兵——RT（Request Tracker）、Perl 生态、Keyboardio 创始人，博客 "Massively Parallel Procrastination"（blog.fsck.com）。现通过其公司 **Prime Radiant**（primeradiant.com）维护，README 提供企业商业支持（sales@primeradiant.com）。
- **诞生**：仓库创建于 **2025-10-09**（GitHub API `created_at`），同日作者发布博文 [《Superpowers: How I'm using coding agents in October 2025》](https://blog.fsck.com/2025/10/09/superpowers/)。发布时机踩得很准：**当天上午 Anthropic 刚推出 Claude Code 插件系统**，Jesse 把原本"git clone + symlink 到 ~/.claude"的个人流程连夜打包成 marketplace 插件发布。
- **方法论前身**：源自其 2025 年 10 月初博文《How I'm using coding agents in September, 2025》中的 brainstorm→plan→implement 人工流程——原流程需要用户开第二个 Claude 会话充当"人类 PM"协调 architect 与 implementer；Superpowers 把这个协调自动化为 subagent 派发。
- **爆红路径**：个人项目，零营销。爆发原因可归为三点：① 时间点卡在 Claude Code 插件生态爆发窗口，是**最早一批、也是质量最高的插件之一**；② Jesse 在博客里公开了完整的构建过程（包括用 Cialdini 说服原理 pressure-test skills 的细节），自带传播性；③ "agent 需要方法论而非更多 token"的叙事精准命中 2025 下半年社区痛点。另有 Tim O'Reilly 与 Jesse 的直播对谈（O'Reilly 官方活动）助推。2026-09 星标已达约 28.9 万（见④）。

## ③ 工作流与工件链

### 3.1 形态：skills 是什么

每个 skill 是一个目录，核心是 `SKILL.md`（给 agent 读的自然语言指令 + 流程约定），可选附脚本。仓库 `skills/` 目录即技能库，配套 `hooks/`（session-start 注入 bootstrap）、各 harness 的插件清单（`.claude-plugin`、`.codex-plugin`、`.cursor-plugin`、`.pi`、`.opencode` 等）和跨 harness 测试（`tests/` 下有 claude-code / codex / devin / kimi / pi / opencode / antigravity / hermes 等子目录）。

**bootstrap 机制**（这是它区别于普通 prompt 库的关键）：session 启动 hook 注入一段 `<EXTREMELY_IMPORTANT>` 提示，告诉 agent "你有 skills；有 skill 可做的事**必须**用 skill"。作者刻意使用了说服心理学（权威、承诺、稀缺等 Cialdini 原则）并设计了压力场景对 skill 做"RED/GREEN 式 TDD 测试"——确保 agent 在时间压力、沉没成本等诱惑下仍会去查 skill。长会话 compaction 后 bootstrap 会重新注入（Pi 等原生支持，Hermes 因无 post-compaction hook 有已知缺陷）。

### 3.2 核心工作流（README "The Basic Workflow"，7 步链条）

1. **brainstorming** —— 写代码之前自动激活：苏格拉底式追问，把模糊想法磨成设计文档，分块给用户确认（"前面拷打需求两小时，后面执行只花 10 分钟"的社区体感即来自此步）。
2. **using-git-worktrees** —— 设计确认后自动建隔离 worktree + 新分支 + 干净测试基线，支持并行任务互不干扰。
3. **writing-plans** —— 把工作拆成 2-5 分钟粒度的任务，每个任务带精确文件路径、完整代码、验证步骤。README 的标准是"计划要清晰到能让一个热情但品味差、无判断力、无项目上下文、抗拒测试的初级工程师照做"。
4. **subagent-driven-development** / **executing-plans** —— 二选一：每任务派新 subagent 实现并逐一 review（最彻底），或当前会话内联执行、最后整分支一次 review（最省 token）。
5. **test-driven-development** —— 强制 RED-GREEN-REFACTOR：先写失败测试、看它失败、写最少代码、看它通过、提交。**"删除在测试之前写出的代码"** 是其标志性纪律。
6. **requesting-code-review / receiving-code-review** —— 任务间对照 plan 评审，按严重级报告，Critical 阻塞推进。
7. **finishing-a-development-branch** —— 验证测试后提供 merge / PR / 保留 / 丢弃选项，清理 worktree。

### 3.3 完整技能清单（skills/ 实测目录 + README 分类）

| 分类 | 技能 | 作用 |
|---|---|---|
| 协作 | brainstorming | 苏格拉底式设计打磨 |
| | writing-plans | 详细实现计划 |
| | executing-plans | 内联执行计划 |
| | dispatching-parallel-agents | 并发 subagent 工作流 |
| | subagent-driven-development | 每任务新 subagent + 两段式 review（先 spec 合规、后代码质量） |
| | requesting/receiving-code-review | 发起/响应评审 |
| | using-git-worktrees | 并行开发分支 |
| | finishing-a-development-branch | 合并/PR 决策收尾 |
| 测试/调试 | test-driven-development | TDD 红绿循环 + 反模式参考 |
| | systematic-debugging | 4 阶段根因流程 |
| | verification-before-completion | 完成前必须验证 |
| | diagnosing-superpowers | 事后诊断某次会话哪里出了问题（带行级证据，可打包脱敏 bundle 报 bug） |
| 元技能 | writing-skills | 按 best practice 创建新 skill（含 skill 测试法） |
| | using-superpowers | skills 系统入门 |

**哲学**（README 原文四条）：TDD always first；systematic over ad-hoc；complexity reduction；evidence over claims。
**贡献政策值得注意**：*"we don't generally accept contributions of new skills"*——技能库由核心团队严控，任何 skill 修改必须在所有支持的 harness 上工作；行为级测试用 prime-radiant-inc/superpowers-evals 的 drill eval harness。
**遥测**：brainstorming 可视化伴侣功能默认从官网加载带版本号的 logo 做匿名使用量统计（可用 `SUPERPOWERS_DISABLE_TELEMETRY` 关闭）——侧面说明插件生态无法回传使用数据。

### 3.4 多 harness 支持（README "Installation" 实测枚举，17 个）

Claude Code（Anthropic 官方插件市场：`/plugin install superpowers@claude-plugins-official`）、Antigravity、Codex App、Codex CLI（OpenAI 官方市场）、Cursor、Devin CLI、Factory Droid、Gemini CLI、GitHub Copilot CLI、Grok Build CLI（xAI 官方市场）、Kimi Code、OpenCode、Pi（原生 skills，无兼容层）、Qwen Code、Hermes Agent、Muse 等。**Claude Code 是首发与第一公民**（bootstrap/skill 格式即 Claude Code 的 SKILL.md 约定），其他 harness 靠各家插件市场与适配清单收敛到同一套 skills。这种"一套 skill、多 harness 分发"本身已成为行业事实标准的雏形（OpenAI/Anthropic/xAI 官方市场均收录它）。

## ④ 数据指标（观测日期：2026-09-20）

| 指标 | 值 | 来源 |
|---|---|---|
| Stars | **289,056**（≈28.9 万） | GitHub repos API；GitHub search API 第二端点同值 289,056，双源交叉一致 |
| Forks | 25,856（两端点相差 ±1，取整 ≈25.9k） | 同上双源 |
| Watchers/订阅 | 1,081 | repos API `subscribers_count` |
| Open issues | 372 | repos API |
| 创建时间 | 2025-10-09T19:45Z | repos API |
| 最近 push | 2026-09-19 | repos API |
| 最新 release | **v6.4.1**，2026-09-19 发布（此前 v6.3.0 2026-08、v6.2.0 2026-07、v6.1.x 2026-06/07）——近 4 个月 5 个 release，节奏稳定 | releases API |
| 贡献者 | obra 524 commits 居首；arittr 79；clkao 8；其余 10 名内均 ≤3 commits | contributors API |

**增速解读**：11 个月约 28.9 万星，在 GitHub 全站历史增速榜前列（对照：多数现象级项目达到该量级需 2-4 年）。贡献者分布极端头部化：**第一名（作者本人）commits 是第二名的 6.6 倍，前两名之外全部 ≤8 次**——这是典型的"个人爆款"信号，详见⑥⑦。

## ⑤ 采纳与影响力

- **官方市场收录**：Anthropic 官方 Claude 插件市场、OpenAI Codex 官方插件市场、xAI Grok 官方市场均直接收录——第三方方法论项目被三大模型厂商官方渠道分发，是行业认可度的强信号。
- **媒体/社区**：Tim O'Reilly 与 Jesse 的官方直播对谈（O'Reilly Live）、Heavybit Open Source Ready 播客 Ep.36；中文社区大量实测文（腾讯云开发者社区等转载的体验文）。中文用户体感标签是"拷打需求两小时，执行十分钟"。
- **概念外溢**：Jesse 在发布博文中预言 "Skills are what give your agents Superpowers... you're going to be hearing a lot more about them from just about everybody"——随后 Anthropic Agent Skills 规范化、各 harness 竞相兼容 SKILL.md 格式，Superpowers 是这一波 "skills 范式" 最早的公开样板与拉动力之一。其 SKILL.md + marketplace 结构实际参与了 de facto 标准的形成。
- **商业转化**：Prime Radiant 围绕它提供企业支持/工具/托管额度（sales@primeradiant.com），并另建 superpowers-evals 独立评测仓库。
- **生态衍生**：多个社区 fork/镜像与第三方评测文档（如 claude-code-ultimate-guide 的资源评估）存在。

## ⑥ 趋势判断：强上升，但个人主导风险显著

**判断：强上升（strong upward），配一个明确的公司化/巴士因子风险标签。**

上升依据：
1. 星标量级与增速（11 个月 28.9 万，2026-09 仍在活跃 push，release 节奏近月无放缓）；
2. 三大官方插件市场收录带来的持续分发面（新用户获取是被动管道化的，不依赖热点）；
3. 多 harness 覆盖随行业扩张自动增值——每出一个新 coding agent，社区就会要求 Superpowers 适配它（README 中 17 个 harness 的安装说明即证据链）；
4. 它绑定的"skills 范式"正是 2025-2026 agent 工程的主导方向，方法论层的稀缺供给（严控贡献、跨 harness 测试）形成质量护城河。

风险依据：
1. **巴士因子极低**：commits 分布 524 : 79 : 8 : 3…，核心方法论与全部技能实质由 Jesse Vincent（+Prime Radiant 小团队）把持，且官方明确"一般不接受新 skill 贡献"；
2. **平台耦合**：核心机制依赖各 harness 的 hook/插件 API（session-start、compaction hook 等），任一厂商改 API 都需团队跟进，维护负担与个人带宽成正比；Hermes 无 post-compaction hook 的已知缺陷说明长尾适配脆弱；
3. 商业化依赖 Prime Radiant 单一实体，若其重心转移，项目可能转入低维护模式；
4. 289k 星的"star泡沫"成分需保留态度：方法论类项目的星标反映的是叙事热度与"收藏待用"，不等于同规模的活跃使用者（项目自身遥测也只做到匿名版本计数，无法给出真实使用量）。

## ⑦ 批评与局限

1. **流程重量**：brainstorm 追问 + 分块设计确认 + 全量 TDD + 每任务双段 review，对原型、小修、探索性脚本而言是显著 overhead；社区反馈两极（"拷打两小时"在赶时间时是折磨）。
2. **token 成本**：subagent-driven-development 每任务派新 subagent + 评审，token 消耗数倍于直接编码；executing-plans 是官方认可的省钱替代，但牺牲隔离性。
3. **说服式提示工程的可维护性争议**：用 Cialdini 原则 + "EXTREMELY_IMPORTANT" 压制 agent 跳过流程，本质是对模型行为的经验性驯化，随模型版本升级可能失效或产生反直觉行为；Jesse 自己也记录过 subagent "游戏化答题"骗过 skill 测试的案例。
4. **强 TDD 教条**：先写测试否则删代码，对 UI 探索、数据科学、一次性脚本并不友好。
5. **skill 贡献封闭**：与一般开源的社区共建叙事相反，技能库不接受外部新 skill，生态多样性受限（官方理由是跨 harness 兼容成本，成立但代价真实）。
6. **中文/非英语场景**：skill 全部英文撰写，追问题目与计划文档对非英语用户的工作语言有一定摩擦（社区实测文提到该问题）。
7. **可观测性弱**：出问题时靠 diagnosing-superpowers 事后读 transcript 排查，缺少运行时指标。

## ⑧ 适用场景 / 不适用场景，及与 SDD 工具的差异

**适用**：从零构建的新项目/新功能；单人或小团队的自主长任务（"agent 自己干两小时不走偏"正是卖点）；需要严格质量纪律（TDD、review gate）的生产代码；多 harness 重度用户的统一工作流；想学习 agent 方法论设计的团队（读它的 SKILL.md 本身就是教材）。

**不适用**：快速原型/hackathon；遗留代码小修小补（bootstrapped 流程会强行 brainstorm）；强监管环境要求机器可校验 spec 的一致性工程；需要 spec 与代码双向追溯、规格变更管理的团队流程。

**与 SDD（spec-driven development）工具的关系——关键辨析**：
- 传统 SDD 工具（如 GitHub Spec Kit、Kiro 等）的核心是 **spec 作为一等工件**：有固定格式（spec/plan/tasks 文件树）、slash 命令驱动的生成流程、以及以 spec 为锚的后续一致性检查。spec 是**被工具消费、可校验的输入**。
- Superpowers 的 spec/plan 是**工作流的中间产物**：brainstorming 产出的设计文档和 writing-plans 的任务清单都是给人读的 Markdown，没有格式规范、没有机器校验、没有变更追溯。它的"契约"作用靠两个软机制实现：一是计划写得足够细（"初级工程师也能照做"），二是 subagent-driven-development 的**两段式 review 显式对照 spec 合规**——即用评审而非校验器来保真。
- 因此准确的归类是：**Superpowers 是方法论 + skills 形态的 agent 行为框架，与 SDD 工具是"同一问题（约束 agent 不跑偏）的两条技术路线"**：SDD 用工件与工具链做硬约束，Superpowers 用注入的行为纪律 + 评审回路做软约束。实践中两者可叠加（用 Superpowers 的纪律执行 SDD 工具产出的 spec），且 Superpowers 的 brainstorm→plan 前半段与 SDD 的 specify→plan 高度同构，这也是它常被误归入 SDD 工具类的原因。

## ⑨ 来源列表

一手源（均为 2026-09-20 实测/抓取）：
1. GitHub repos API: https://api.github.com/repos/obra/superpowers （stars/forks/issues/created_at/pushed_at/license）
2. GitHub search API（第二端点交叉验证星数）: https://api.github.com/search/repositories?q=repo:obra/superpowers
3. GitHub contributors API: https://api.github.com/repos/obra/superpowers/contributors
4. GitHub releases API: https://api.github.com/repos/obra/superpowers/releases （v6.4.1 等）
5. 官方 README（main）: https://raw.githubusercontent.com/obra/superpowers/main/README.md （工作流、17 harness 安装、技能清单、哲学、贡献政策、遥测）
6. 仓库目录树（skills/ 与 tests/ 实测结构）: https://api.github.com/repos/obra/superpowers/git/trees/main?recursive=1
7. Jesse Vincent 发布博文（2025-10-09）: https://blog.fsck.com/2025/10/09/superpowers/ （起源、bootstrap 机制、Cialdini pressure-test、memories/sharing 路线图）

二手源（背景与社区体感，2026-09 检索）：
8. O'Reilly 直播页: https://www.oreilly.com/live-events/give-your-agents-superpowers-jesse-vincent-live-with-tim-oreilly/0642572444747/0642572444730/
9. Heavybit 播客 Ep.36: https://www.heavybit.com/library/podcasts/open-source-ready/ep-36-managing-ai-coding-agents-with-jesse-vincent/
10. 中文实测（腾讯云开发者社区）: https://cloud.tencent.com.cn/developer/article/2674266
11. 第三方资源评估: https://github.com/alexica00/claude-code-ultimate-guide/blob/main/docs/resource-evaluations/obra-superpowers-evaluation.md
