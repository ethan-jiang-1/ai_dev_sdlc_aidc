# 03a：团队级规则文件治理深挖——全文证据档案

> 编号说明：本档案旧编号 03a（AGENTS.md 治理 03a，与渐进披露档案旧编号同为 03a、以主题区分），抽出后文件名重编为 01b；正文中"03a A/B/C/D"式引用即指本档案小节。本档案正文所称"03 文 / 03 文档"指上游 `research/01-context-engineering.md`（旧称），与 `final/03` 无关（2026-09-21 升格消歧）。

> **元数据**
> - accessed_at：2026-09-21（二轮逐条回源；三路并行：大厂一手 / OSS repo 活样本 / 度量·工具·harness 声音）
> - 上游：`01-context-engineering.md` §「团队治理实践深挖（2026-09-21 二轮）」（本文件为其全文证据档案，不复制结论性判读）
> - 回源途径标注（与 04a 同一口径）：
>   - **一手** = 直接抓到原文页面 / GitHub API / shallow clone 直读源文件；
>   - **半回源** = 原文页存在且关键信息（标题/日期/摘要）直接确认，但正文未完整渲染，细节经消化稿核验；
>   - **转述** = 原文抓不到，仅经媒体译文/第三方摘要中转。
> - 摘录纪律：所有英文原句为回源页面逐字摘录；抓不到的如实标注"转述"，不代拟。部分摘录由并行回源子代理完成（⚠ 审计注：A1.1/A3/A5 等条目的一手判定系转承子代理结论，非本档案作者直核——引用时按"半手"对待）并逐字核对，本档案按其报告记录回源状态。
> - 观测方法备注：OSS repo 部分使用 GitHub REST API（未认证，约 10 次调用）+ 当日 shallow clone 直读；PR 逐条 review 记录未全量拉取（推断处均已标注）。

---

## A1. Anthropic —— skills 市场治理 + 组织级转型 + AGENTS.md 立场反转

### A1.1 《Lessons from building Claude Code: How we use skills》

| 项 | 值 |
|---|---|
| URL | https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills |
| 日期 | 页面标注 June 3, 2026；作者 Thariq Shihipar（Claude Code 团队） |
| 回源状态 | **一手**（整页正文抓到，逐字核对） |

**逐字摘录**：

规模与定位：
> "We've been using skills in Claude Code extensively at Anthropic with hundreds of them in active use."

分类法（治理第一步是编目）：
> "After cataloging all of our internal skills at Anthropic, we noticed they cluster into nine categories. The best skills fit cleanly into one; the ones that try to do too much straddle several and confuse the agent."

谁写 / 怎么准入（无中心团队，沙盒孵化 + traction 后 PR）：
> "At Anthropic, we don't have a centralized team that decides; instead we try to find the most useful skills organically. If someone has a skill that they want people to try out, they can upload it to a sandbox folder in GitHub and point people to it in Slack or other forums."

> "Once a skill has gotten traction (which is up to the skill owner to decide), they can put in a PR to move it into the marketplace."

观测 / 防腐（用量遥测而非人工巡检）：
> "To understand how a skill is doing, we use a PreToolUse hook that lets us log skill usage within the company … we can find skills that are popular or are undertriggering compared to our expectations."

> "The highest-signal content in any skill is the Gotchas section. … Ideally, you will update your skill over time to capture these gotchas."

效果自述：
> "Verification skills have had the most measurable impact on Claude's output quality internally. It can be worth having an engineer spend a week just making your verification skills excellent."

### A1.2 《Running an AI-native engineering org》（Fiona Fung，Code w/ Claude（页面 fetch 截断，引语取自本场次页元数据，核对途径单一） SF 2026）

| 项 | 值 |
|---|---|
| URL | https://claude.com/blog/running-an-ai-native-engineering-org |
| 日期 | 2026-06-03 发布；会议场次页 https://claude.com/code-with-claude/session/tyo-running-an-ai-native-engineering-org（东京场 2026-06-10，**一手**确认场次/讲者/议题描述："the bottlenecks changed at Anthropic (review, ownership, hiring) and the norms we rewrote to keep shipping"） |
| 回源状态 | **半回源**：claude.com 正文页被导航层截断，内容经两份详细第三方消化稿核验（韩文 BLUEBUG 博客 https://k82022603.github.io/posts/ai-네이티브-엔지니어링-조직-의-운영-원칙-앤트로픽-사례/ ，2026-06-28；中文腾讯云开发者《跑 AI 原生工程团队是什么感觉？》 https://cloud.tencent.com/developer/article/2696603 ）。以下要点按消化稿口径记录，**引用时不得当逐字一手引语使用**。 |

治理相关要点（半回源口径）：
- 瓶颈迁移论：写代码不再是瓶颈，验证/领域 review/安全边界是新瓶颈——组织流程按新瓶颈重设计。
- Review 分层："Trust, but Verify"——AI 负责 style/lint/PR 整理/测试补充；人保留法律风险、安全与信任边界、产品判断；且该平衡随模型演进持续重调（规则文件治理的相邻上层）。
- 三条 non-negotiable 原则：全员 dogfood、尽量扁平（manager 先做 IC）、**过时流程杀掉**（成员有质询并废除流程的授权）。
- 度量三指标：onboarding ramp time ↓、PR cycle time ↓（用作管线诊断）、Claude-assisted commit rate ↑（消化稿引语："基本上所有 commit 都有 Claude 帮助；最近四个月没见过没有 Claude 帮助的 commit"——转消化稿，勿作逐字）。
- 运营模型：原则统一 + pod 自治（自动化顺序、triage、计划节奏 pod 自决）。

### A1.3 AGENTS.md 立场反转（2026-09）——对 03 文 §1.1 空档的勘误级更新

| 项 | 值 |
|---|---|
| URL | The Register: https://www.theregister.com/ai-and-ml/2026/09/18/anthropic-decides-to-support-openais-markdown-instructions-spec/5297588 |
| 日期 | published Fri 18 Sep 2026 |
| 回源状态 | **半回源**（标题+发布时间直接回源，正文截断）；旁证：aiweekly.co 记 Claude Code 2.1.277 在无 CLAUDE.md 时回退读 AGENTS.md（未逐字回源） |
| 判读 | 03 文 §1.1 所记"Claude Code 原生支持 AGENTS.md 口径不一（待验证）"在 2026-09-21 观测下应更新为：**Anthropic 已宣布支持**（回退式/渐进式，细节待正式文档回源）。导火索见 A2。 |

---

## A2. Shopify —— 全司统一指令格式的最强立场（转述级）

| 项 | 值 |
|---|---|
| URL | InfoQ/36kr 英文版：https://eu.36kr.com/en/p/3955873528626311（2026-08-26 发布，InfoQ 原文经微信公众号授权转载） |
| 回源状态 | **转述**：Tobi Lütke X 原帖未能直接回源，以下引语为该媒体给出的英译，谨慎使用 |

**转述引语**：
> "I am considering banning Claude Code at Shopify until they change their mind and are willing to read AGENTS.md, .agents/skills and other files"

> "Both AGENTS.md and CLAUDE.md take effect recursively along the directory tree. When thousands of developers maintain a monorepo together, it is inevitable that one of the files will be missing in a certain directory. As a result, some developers end up using agents that are 'missing a piece of their brain'."

> "We solved this problem with automation, but this is a stupid complexity tax that should never have been paid"

**治理相关事实**（转述口径）：Shopify 数千工程师维护 monorepo、多 AI 工具并存；曾自建自动化兼容层（递归查找 AGENTS.md → 建 CLAUDE.md symlink → fswatch 监控 → launchd 自启 → 全局 gitignore），即团队级"格式统一"防腐的实例；该事件以 Anthropic 2026-09 让步收尾（A1.3）。

**旁证（一手但不作治理断言）**：https://shopify.engineering/building-an-agentic-harness-that-outlasts-the-model（2026，Shopify 官方工程博客）——主题为安全 agent harness，仅旁证其"指令/harness 编码严格 guidelines"思路。

**同文附带数据点**：文内引 2026 年一项 2,926 repo 研究——context files 已是开发者给 agent 下指令的最常见方式（该研究本体未回源，转述）。

---

## A3. Vercel —— "规则当产品做"的人流程样本

### A3.1 《Teaching agents product design at Vercel》

| 项 | 值 |
|---|---|
| URL | https://vercel.com/blog/teaching-agents-product-design-at-vercel-2UtdJlYIxoLAmiwWt5i4rV/f0095a8e84 |
| 日期 | 页面标注 25 Jun 2026；作者 John Phamous（Design Engineer） |
| 回源状态 | **一手**（正文全抓） |

**逐字摘录**：

治理总纲：
> "We treat accepted product decisions like code, keeping them in the repository, reviewing changes against them, and making them available to every agent working there."

文件分工（repo AGENTS.md 做 load 路由，skill 内 AGENTS.md 定义治理）：
> "The repository AGENTS.md tells coding agents when to load the skill. The skill-local AGENTS.md defines load order, validation, and governance."

> coverage-gaps.md "lists areas where we do not have a standard yet."

规则准入（防膨胀双闸门）：
> "Add or change a rule only after current-source verification and human acceptance."

> "Never promote one screenshot, one shipped file, or one reviewer comment into a universal rule by itself."

防腐/更新回路（collector/judge 分离 + 人工终审）：
> "Product standards change … and every update needs evidence and human review."

> "A collector gathers messages, links, and nearby context without proposing rules. A separate judge groups the evidence, verifies sources, and records open questions."

> "Automation ends with the review packet. A human decides whether a candidate becomes agent guidance, a lint rule, an example, an eval, or no change."

淘汰：
> "Treat new rules as product changes, reviewing and testing each one, and removing those that stop helping."

效果自述（触发率实证）：
> "In separate Next.js evals, agents failed to invoke an available skill in 56% of cases. Test the trigger separately from the guidance, because failing to load the skill and failing to follow a rule are different problems."

### A3.2 Changelog：Vercel Agent code reviews 遵循 repo 规则

| 项 | 值 |
|---|---|
| URL | https://vercel.com/changelog/vercel-agent-code-reviews-now-follow-your-code-guidelines |
| 日期 | 页面标注 6 Jan 2026；作者 Julian Benegas, John Phamous, Marcos Grappeggia |
| 回源状态 | **一手** |

> "Vercel Agent now applies your repository's coding guidelines during code reviews. Add an AGENTS.md file to your repository, or use existing formats like CLAUDE.md, .cursorrules, or .github/copilot-instructions.md. Agent automatically detects and applies these guidelines to provide context-specific feedback for your codebase."

（规则消费端产品化：code review agent 自动检测并应用各格式规则文件。）

---

## A4. Cloudflare —— 规则文件全链路自动化闭环（3,900+ repo）

| 项 | 值 |
|---|---|
| URL | https://blog.cloudflare.com/internal-ai-engineering-stack/ |
| 日期 | Agents Week 2026 系列；第三方书签记录添加于 2026-04-21（ https://raw.githubusercontent.com/jerrylususu/bookmark-summary/refs/heads/main/202604/2026-04-21-the-ai-engineering-stack-we-built-internally-%E2%80%94-on-the-platform-we-ship.md ） |
| 回源状态 | **一手**（web_fetch 只回 TL;DR 层；改用 curl 抓整页 HTML 成功，以下引语逐字来自原文） |

动机（为什么需要 AGENTS.md）：
> "the model didn't know the right test command, the team's current conventions, or which parts of the codebase were off-limits. That pushed us toward AGENTS.md: a short, structured file in each repo that tells coding agents how the codebase actually works and forces teams to make that context explicit."

谁写 / 怎么 review（机器生成 + owning team MR 审）：
> "A capable model then generates the structured document, and the system opens a merge request so the owning team can review and refine it."

> "We've processed roughly 3,900 repositories this way."

（生成管线输入：Backstage 服务目录元数据（2,055 个服务）+ 仓库结构分析 + Engineering Codex 标准映射。）

防腐（腐烂检测闭环——本轮最重要的一手发现）：
> "The initial merge request solved the bootstrap problem, but keeping these files current mattered just as much. A stale AGENTS.md can be worse than no file at all. We closed that loop with the AI Code Reviewer, which can flag when repository changes suggest that AGENTS.md should be updated."

工程标准（Engineering Codex）与规则文件的关系：
> "The Engineering Codex is Cloudflare's new internal standards system where our core engineering standards live. We have a multi-stage AI distillation process, which outputs a set of codex rules ('If you need X, use Y. You must do X, if you are doing Y or Z.') along with an agent skill that uses progressive disclosure and nested hierarchical information directories and links across markdown files."

执行与效果自述：
> "Each agent … pulls Engineering Codex rules from a central repo, and reads the repository's AGENTS.md for codebase context."

> "when a finding maps to an Engineering Codex rule, it cites the specific rule ID, turning an AI suggestion into a reference to an organizational standard."

> "From launching this effort to 93% R&D adoption took less than a year."

（活跃用户 3,683 = 公司 60%、R&D 93%；数据区间 Feb 5–April 15, 2026；AI Code Reviewer 集成于 GitLab CI 审所有 MR。）（括注数字按当日抓取记录，未独立复核）

---

## A5. Figma —— steering memory：先例/政策分流（安全域）

| 项 | 值 |
|---|---|
| URL | https://www.figma.com/blog/how-we-secure-figmas-internal-systems-with-agents/ |
| 日期 | 页面标注 July 29, 2026；作者署名 Matthew |
| 回源状态 | **一手**；范围限安全 agent（安全团队单系统），非全司工程治理 |

**逐字摘录**：

规则文件定位：
> "This is behavioral guidance for the agent, stored as a markdown document that gets loaded into the agent's context at the start of every run. Think of it like an AGENTS.md file"

防腐经验（纠错回写）：
> "The agent can update its own steering memory when a security engineer corrects it."

分流纪律（本轮独有的反膨胀原则）：
> "One early mistake was saving everything as steering memory, which started overriding the agent's behavior in unwanted ways. Precedent and policy are different things and they belong in different places."

---

## A6. Google / Linear —— 未找到一手（如实记录）

- **Google**：多轮搜索（developers.googleblog.com、research.google、Google Cloud blog）未见 2026 年内部"AI 规则文件治理"一手博客。周边材料仅：modular prompt transpilation 产品方法帖（面向客户非内部治理）；媒体转述 Pichai"75% 新代码 AI 生成"（ https://enterpriseai.economictimes.indiatimes.com/news/industry/google-ceo-sundar-pichai-reveals-75-of-new-code-is-ai-generated/130457744 ，2026-04-24，转述）。
- **Linear**：仅第三方镜像仓库的 AGENT_INSTRUCTIONS.md（非官方）与产品动态，无官方一手。

**治理完整度排序（判读）**：Cloudflare（全链路自动化闭环+系统兜底保鲜）＞ Vercel（人流程最完备：证据回路/稳定 ID/coverage-gaps/eval holdout/淘汰）＞ Anthropic（市场+用量遥测，但准入 owner 自决）＞ Shopify（立场最强硬但缺一手系统描述）＞ Figma（域内纪律清晰）。Google/Linear 不参与排序。

---

## B. 开源项目活样本：三个 repo 的规则文件演化史

> 方法：GitHub REST API `commits?path=AGENTS.md`（未认证）+ 当日 shallow clone 直读。观测日期 2026-09-21。标注【一手】= API/clone 直接观测；【推断】= 证据推理。

### B0. 候选池筛除（一手）

- google-gemini/gemini-cli、anthropics/claude-code：**0 条** AGENTS.md 提交史（claude-code 无公开规则文件演化）。
- ghostty-org/ghostty：17 条，但 13/17 为 Mitchell Hashimoto 一人 → 单人治理，排除。
- openai/openai-cookbook：仅 6 条（亮点 commit "Add mandatory docs-editor review gate (#2862)"， https://github.com/openai/openai-cookbook/commit/d9e5840b ，2026-07-17），规模不足落选。

### B1. openai/codex —— 治理强项：规则即代码（规则进 CI）

- **提交史**【一手】 https://api.github.com/repos/openai/codex/commits?path=AGENTS.md ：77 条提交，2025-05-11（2b122da0 "feat: add support for AGENTS.md in Rust CLI (#885)"）→ 2026-09-07，**24 位作者**（pakrym-oai 11、Michael Bolin 11、Adam Perry 9、Jeremy Rose 9、Eric Traut 6…长尾 18 人各 1–4 条）。
- **PR 流程**【一手】抽检提交全部带 PR 号；含规则文件的 commit 如 93c79046 "ci: fail jobs that dirty the worktree (#29720)"（ https://github.com/openai/codex/pull/29720 ，merged 2026-06-24，body 明说 "Update `AGENTS.m…"）。【推断】review 人细节未逐 PR 拉 reviews API。
- **CI 检查**【一手】AGENTS.md 里的约定被固化为 lint 并进 CI：`.github/workflows/rust-ci-full.yml` 含 argument-comment-lint job（L75-147， https://github.com/openai/codex/blob/main/.github/workflows/rust-ci-full.yml ）；AGENTS.md 原文（clone 直读）："You can run `just argument-comment-lint` to run the lint check locally. … Note CI checks all three platforms, which the local run does not." 另 repo-checks.yml 有 fmt-check；PR #29720 给 19 个 CI job 加 worktree-cleanliness 终检，防 CI 弄脏 AGENTS.md 等文件。
- **防腐机制**【一手】320 行文件强分区（Rust 规范 / app-server 协议 / Python / Platform Support）；规则带例外条款与 commit/PR 锚点（"as in `3c7f013f9735` / `#16630`"）；模块体量规则点名高热文件（"Target Rust modules under 500 LoC"）；存在 `codex-rs/tui/src/bottom_pane/AGENTS.md` 目录级子文件。【推断】无 recent-learnings 式日志区，靠"规则即代码"防腐。

### B2. vercel/next.js —— 治理强项：结构单源（symlink + 分层）

- **提交史**【一手】 https://api.github.com/repos/vercel/next.js/commits?path=AGENTS.md ：36 条，2026-01-05 首条 8fd79ff4 "Rename CLAUDE.md to AGENTS.md with symlink (#88105)" → 2026-09-17，16 位作者（Tim Neutkens 12、Tobias Koppers 4…）。
- **PR 流程**【一手】首条 PR https://github.com/vercel/next.js/pull/88105 （merged 2026-01-05 by huozhi，2 条 review comments），body 逐字："Keep `AGENTS.md` as main instruction file to benefit for more coding agents. Symblink `CLAUDE.md` to it…"（"Symblink" 为原文拼写）。近期 commit 1ae49102（2026-09-17）"agents: Add a `--comments-only` flag to `pr-status` script…" 显示有专门 agent 脚本维护指令面。
- **CI 检查**【一手】无直接 lint AGENTS.md 的 job。间接机制：`scripts/run-for-change.mjs`（clone 直读）把 `.agents`、`.claude`、`.cursor` 列入同一 "docs" 变更组——改规则文件触发 docs 级验证链。【推断】一致性靠 symlink 结构而非 CI。
- **防腐机制**【一手】CLAUDE.md→AGENTS.md symlink（clone：`lrwxr-xr-x CLAUDE.md -> AGENTS.md`）；AGENTS.md 首行原文："> **Note:** `CLAUDE.md` is a symlink to `AGENTS.md`. They are the same file."；根 / `.github/` / `test/` / `evals/` / `turbopack/` 五层目录级 AGENTS.md（clone 确认）；文件内路由规则原文："Before editing or creating files in any subdirectory … read all `README.md` files in the directory path from the repo root up to and including the target file's directory."【一手】例外：turbopack 下 CLAUDE.md 是普通文件非 symlink。

### B3. block/goose（现 aaif-goose org）—— 治理强项：流程元治理

- **提交史**【一手】 https://api.github.com/repos/block/goose/commits?path=AGENTS.md （需 -L 跟随 301）：27 条，2025-09-05（e54ba78 "Add AGENTS.md for AI coding assistant support (#4539)"）→ 2026-09-17，14 位作者（Angie Jones 5、Jack Amadeo 4、Douwe Osinga 3…），分布最社区化。
- **PR 流程**【一手】全部带 PR 号；代表性元规则 PR https://github.com/aaif-goose/goose/pull/10819 "docs: adopt issue-first contribution workflow"（merged 2026-07-30 by alexhancock，**16 条 review comments**——三 repo 中评审强度最高），body 逐字 "add the Ready-status gate to agent instructions"。AGENTS.md 现文即其产物："The issue is the source of truth… Every external pull request must link the Ready issue it implements."
- **CI 检查**【一手】无 lint；但 `.github/workflows/goose-pr-reviewer.yml` L141 与 `goose-issue-solver.yml` L75 均含 checklist 项逐字 "Read AGENTS.md if it exists"——自家 agent 做 PR 评审/解决时被强制读规则文件（agent 化消费，非 lint）。
- **防腐机制**【一手】(a) CLAUDE.md 仅一行 "@AGENTS.md" 引用（单一事实源）；(b) 显式过期机制段 "Agent Loop Migration"："We are replacing the legacy agent loop in `crates/goose/src/agents/agent.rs` with the state machine in … Until the migration is complete, changes to agent-loop behavior must be implemented and tested in both paths."；(c) 决策外链："See [Discussion #10830](https://github.com/aaif-goose/goose/discussions/10830) for the decision and migration direction.（⚠ 审计勘误：实测 #10830 为 MCP registry 退役公告，与 agent-loop 迁移无关——待核）；(d) 主动减法 commit a9060fd2 "docs: stop enumerating crates in AGENTS.md Structure (#11614)" 防清单腐化。

### B4. 横向对比（2026-09-21 观测）

| | 演化方式 | 批准流程 | CI 检查 | 防腐机制 |
|---|---|---|---|---|
| openai/codex | 77 commits / 24 作者 / 16 个月，高频小幅 | 全走 PR，维护者 merge | ★最强：约定固化为 argument-comment-lint 进 CI + fmt-check + worktree 终检 | 规则即代码；例外+锚点；目录级子 AGENTS.md |
| vercel/next.js | 2026-01 由 CLAUDE.md 改名起家，36 commits / 16 作者 | 全走 PR（#88105，2 review） | 无直接 lint；run-for-change.mjs 归入 docs 验证组（间接） | ★结构最强：symlink 单源 + 五层目录级 + "读沿途 README"路由 |
| block/goose | 27 commits / 14 作者，与功能迁移同步 | 全走 PR，评审最重（#10819，16 comments） | 无 lint；agent 工作流强制 "Read AGENTS.md if it exists" | ★元治理最强：issue-first Ready gate、迁移双路径条款、决策外链、主动删减史 |

**总体判断**【推断】：治理维度不同冠——工程化执行选 codex、结构单源选 next.js、流程元治理选 goose；共同点：**规则修改一律走 PR、提交史完全可溯**。没有一家在 CI 里直接 lint AGENTS.md 内容本身（codex 是把文件里的约定提升为代码 lint）——这与 C2 工具空档互相印证。

---

## C1. 三组实证的细节回源（逐字）

### C1.1 Gloaguen et al. 2026 —— 勘误：论文实名 CTXbench，非 "AGENTbench"

| 项 | 值 |
|---|---|
| URL | https://arxiv.org/abs/2602.11988 （全文 https://arxiv.org/html/2602.11988v2 ） |
| 日期 | v1 2026-02-12，v2 2026-06-23 |
| 回源状态 | **全回源** |
| 题名 | "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"；作者 Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev（ETH Zurich + LogicStar.ai） |
| 命名勘误 | 论文自建 benchmark 名为 **CTXbench**；"AgentBench" 是二手（Upsun 博客等）误称（见 D3），03 文/底稿引用时应更正 |

构造方法（逐字）：
> "The benchmark contains 138 unique instances, covering both bug-fixing and feature addition tasks across 12 recent and niche repositories, all featuring developer-committed context files."

> "Using this process, we obtained 138 instances from a total of 5694 PRs from 12 repositories that meet our criteria, using GPT-5.2 with Codex as the agent."

agent/模型（逐字）：
> "We consider four coding agents, paired with suitable models: Claude Code with Sonnet-4.5, Codex with GPT-5.2 and GPT-5.1 mini, and Qwen Code with Qwen3-30b-coder."

数据集与三 setting：SWE-bench Lite（300 tasks）+ CTXbench（138 instances）；None / LLM 生成（各 agent 推荐 /init）/ Dev（开发者提交）三组对照。

主要数字（逐字）：
> "Surprisingly, we find that providing context files does not generally improve task success rates, while increasing inference cost by over 20% on average."

> "developer-committed files outperform LLM-generated ones by a significant margin of 7% on average."

> "we observe that instructions in context files are well followed. This leads to increased exploration, testing, and reasoning by coding agents, and, as a result, increases costs by over 20%."

结论原句（摘要末句）：
> "We conclude that while context files are useful for specifying non-standard coding practices, any attempts to improve performance should be rigorously evaluated before deployment."

（引言更强："We therefore suggest omitting LLM-generated context files for the time being, contrary to agent developers' recommendations, as they don't help improve performance."）

局限：第 5 节 Limitations（语言仅 Python、只考察任务解决场景等）——该节正文未逐字抓取（页面截断），**半回源**。

### C1.2 Umans AI 跨工具遵循度实验 —— 勘误：日期为 2025-11-29

| 项 | 值 |
|---|---|
| URL | https://blog.umans.ai/blog/agent-apply/ （实题 "Can coding agents actually follow your codebase's rules?"） |
| 日期 | **2025-11-29（非 2026 材料）** |
| 回源状态 | **全回源** |

实验设计（逐字）：
> "we gave agents a concrete contract inside the repo (AGENTS.md), we ran them as actual coding agents (editing files, running commands), and we checked how closely their behavior matched what we asked for."

9 个 "model+tool" 配置各跑 1 次：GPT-5.1 Codex-Max via Codex CLI（high/extra-high）、GPT-5.1 Codex via Codex CLI（high）、Claude Sonnet 4.5 / Opus 4.5 in Claude Code (Thinking)、Gemini 3 Pro via Gemini CLI、Sonnet 4.5 / Gemini 3 Pro / GPT-5.1 Codex High in Cursor。任务面 "the target surface is 431 lines of code"（bash.py 143 + edit.py 288）；AGENTS.md 测试准则 8 条。"For each configuration we follow the same steps: Fresh workspace → Agent run → Collect tests → Automatic checks（最多一次错误回喂）→ Evaluation"。

逐字结论句：
> "Agents running in provider tools (Codex CLI, Claude Code) behaved more like collaborators inside the repo: they respected more of AGENTS.md, ran checks, and produced code we could imagine keeping after edits."

> "Fixture reuse and centralization is where agents struggled the most … Only one configuration (Codex-Max, high effort) even created a conftest.py, and it only centralized one of its three fixtures there. Every other agent … defined fixtures locally in each test file, duplicated setup code across tests, or ignored fixtures entirely."

> "None of the setups fully matched the testing style in AGENTS.md; every one drifted somewhere."

> "This is a small, opinionated experiment on one codebase and one kind of task. It is here to make our own day-to-day experience with agents a bit more concrete and comparable, not to claim any universal ranking of models or tools."

### C1.3 Lulla et al., ICSE JAWs 2026（arXiv:2601.20404）

| 项 | 值 |
|---|---|
| URL | https://arxiv.org/abs/2601.20404 （全文 https://arxiv.org/html/2601.20404v2 ） |
| 日期 | v1 2026-01-28，v2 2026-03-30；页眉 "Conference: Journal Ahead Workshop (JAWs) 2026; April 12–18, 2026; Rio de Janeiro" |
| 回源状态 | **全回源** |

abstract 逐字：
> "We analyze 10 repositories and 124 pull requests, executing agents under two conditions: with and without an AGENTS.md file. We measure wall-clock execution time and token usage during agent execution. Our results show that the presence of AGENTS.md is associated with a lower median runtime (Δ 28.64%) and reduced output token consumption (Δ 16.58%), while maintaining a comparable task completion behavior."

细节：agent 仅 OpenAI Codex（gpt-5.2-codex）；26 合格 repo 随机抽 10、每 repo ≤15 合并 PR；配对设计；Wilcoxon p<0.05（wall-clock、output tokens）；表格逐字：Median wall-clock 98.57s→70.34s；Median output tokens 2,925→2,440；输入/总 token 中位数基本不变。

自述局限（逐字）：
> "the study focuses on a sampled subset of repositories, pull requests, and agent configurations, which naturally motivates the next steps."

> "observed effects may still depend on agent stochasticity, the specific agent framework and model used, and the characteristics of the selected tasks."

> "these metrics do not capture whether agent-produced changes are correct, maintainable, or aligned with developer intent."

> §3.1.8: "A comprehensive evaluation of the output quality … is beyond the scope of this paper"（仅 50 PR 抽查 sanity check）

---

## C2. 2026 年新出现的规则文件 lint/测试工具（除 Codacy AgentLinter 外）

1. **agnix**（agent-sh/agnix）
   - URL：https://github.com/agent-sh/agnix ｜ 日期：README 无首发日期，仓库活跃，观测 2026-09-21
   - README 逐字："The missing linter and lsp for AI coding assistants. Validate CLAUDE.md, AGENTS.md, SKILL.md, hooks, MCP." / "456 rules across Claude Code, Codex CLI, OpenCode, Cursor, Copilot, and more"
   - auto-fix、GitHub Action、LSP/MCP server、多编辑器插件；AGENTS.md 专属规则 13 条（AGM-*/XP-*）；开源（MIT OR Apache-2.0，Rust，npm/crates/pip 分发）。README 引 Vercel 评测（skills 语法错误时 "invoke at 0%"， https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals ）为价值论据。
2. **ai-linter**（fchastanet/ai-linter）
   - URL：https://github.com/fchastanet/ai-linter ｜ 日期：未标注首发，pre-commit 示例 rev 0.3.3，观测 2026-09-21
   - README 逐字："AI Linter is a validation tool for AI skills and agent configurations. It enforces structure, frontmatter, content length, token limits, and file reference checks for SKILL.md and AGENTS.md files."
   - 规则含：内容 ≤500 行 / ≤5000 token、引用文件必须存在、根目录缺 AGENTS.md 告警（`agents-file-missing`）；MIT，Python，pre-commit + VS Code。
3. **claudemd-pro**（crisnahine/CLAUDEMD-PRO）
   - URL：https://github.com/crisnahine/CLAUDEMD-PRO ｜ 日期：未标注，观测 2026-09-21
   - README 逐字："Deep codebase-aware CLAUDE.md generator, linter, and effectiveness scorer."
   - 特色是**效果评分**：`claudemd lint`（26 条规则：token-budget、vague、redundant、style-vs-linter、contradictory-advice 等）+ score（0–100）+ drift 检测（evolve）+ GitHub Action + MCP server；MIT，npm。
4. **claude-md-lint / claude-code-lint（npm）**： https://www.npmjs.com/package/claude-md-lint 、 https://socket.dev/npm/package/claude-code-lint ——**半回源**（npm 页 403，仅确认存在与命名，无法摘功能与日期）；同类另有 @studiomeyer-io/skilldoctor（SKILL.md 体检）。
5. **空档判断**：2026 年尚无独立的 "agent instruction compliance eval" 通用工具成型；合规评测目前以论文 benchmark（C1）+ 厂商自评（Vercel agent evals）+ claudemd-pro 的 effectiveness score 形态存在。

---

## D. "规则文件治理 = harness 治理子层"的新独立声音（2026，排除已知的 arXiv 2609.00252 / OpenAI 三目录 / 腾讯云 / Codacy / Hashimoto / Osmani）

### D1. Andrea Griffiths / Agentic AI Foundation（Linux Foundation）—— 官方标准层的治理分工判词

- URL：https://aaif.io/blog/measuring-agents-md-what-five-runs-show-that-one-doesn-t ｜ 日期：2026-07-22 ｜ **全回源**
- 逐字：
> "AGENTS.md is guidance, not enforcement … Real enforcement still belongs to CI, branch protection, and sandboxed execution."

> "Keep enforcement in CI and branch protection, not in the file. The file guides; the checks decide."

> "That's a rare outcome in developer tooling, and it's exactly the kind of outcome AAIF exists to protect: an open, vendor-neutral standard that any tool can adopt without asking permission."

- 独立性：独立（基金会/标准治理视角，自做实验：Copilot CLI、同 repo 两 clone × 5 runs 取中位）。**注意其结论方向与 ETH 论文相反**（该文实测规则文件有可测收益）——本身就是有用张力点。

### D2. Cody Lindley —— AI Harness Engineering Compatibility Matrix

- URL：https://github.com/codylindley/ai-harness-engineering-compatibility-matrix （live： https://codylindley.github.io/ai-harness-engineering-compatibility-matrix/ ）｜ 日期：页面自注 "Last updated: August 26, 2026"，repo 描述称 "(April 2026)" ｜ **全回源**
- 逐字：
> "Harness engineering shapes the system around the model: tools, permissions, state, checks, hooks, agents, MCP servers, and guardrails."

> "This matrix focuses on harness files you can version, review, and refactor: AGENTS.md, scoped rules, skills, prompt files, lifecycle hooks, MCP config, and permission/sandbox settings."

- 独立性：**部分独立**——独立作者与产物，但术语明确站在 Hashimoto（coinage）与 Böckeler（martinfowler.com taxonomy）肩膀上，属体系化扩散者而非新源头；增量是"把规则文件放进可版本治理的 harness 文件清单 + 四工具兼容/优先级实证"。

### D3. Guillaume Moigneu / Upsun —— ".gitignore 式"规则文件治理法

- URL：https://developer.upsun.com/posts/ai/agents-md-less-is-more ｜ 日期：2026-02-23 ｜ **全回源**（.md 原文）
- 逐字：
> "Treat your CLAUDE.md like a .gitignore. It grows as you discover new edge cases, and it gets pruned when entries become irrelevant."

> "Verification matters more than instruction. Instead of trying to preemptively tell the agent everything it needs to know, invest in the infrastructure that catches mistakes: test suites, linters, type checkers, CI pipelines."

- 独立性：独立（云厂商工程实践，以实证论文为据但给出自己的 start empty→incremental→prune 治理法）。**注意**：该文是把 ETH 论文误称 "AgentBench" 的二手来源（"the paper's custom AgentBench (138 tasks from 12 repositories with developer-written context files)"）——C1.1 命名勘误的证据链一环。

### D4. dougborg/harness-kit —— 规则文件的可审计/可锁版本 harness 工件化

- URL：https://github.com/dougborg/harness-kit ｜ 日期：未标注首发，观测 2026-09-21（Release Please 自动 semver）｜ **全回源**
- 逐字："A self-improving agent harness for Claude Code and Codex"；`/harness audit` — "10-step quality gate on your project's harness"；bootstrap "installs repository-local AGENTS.md, .agents/skills/, and .codex/agents/ content"，用 `.harness-lock.json` 追踪 provenance。
- 独立性：独立（audit/retro/hoist 闭环，纯实践者工具，未引用已知六家）。

### D5. Umans AI（治理视角的延伸）

- https://blog.umans.ai/blog/consistency-matters/ （2025-11-10 / updated 11-27）；https://blog.umans.ai/blog/stop-being-your-ai-agents-assistant/ （2026-02-26）
- 逐字（2025-11）："Unless you give them explicit, repo-local rules and checks to latch onto, they tend to optimize for 'get this change done'"；（2026-02）"design your process assuming the agent will occasionally drop instructions." / "What worked last week might not be enough this week because the product moved."
- 独立性：独立（规则文件被定位为需要持续运维、会衰减的治理组件，而非 prompt 技巧）。主体材料跨 2025-11～2026-03。

### D6. 线索但未回源（如需再挖）

- Zenodo "The Repository-Scoped Agent Harness"（ https://zenodo.org/records/20636367 ，搜索摘要片段："Agent harnesses provide the technological infrastructure to solidify code style and architectural boundaries into executable axi…"，**半回源**）
- nguyenanh92/harness-kit（ https://nguyenanh92.github.io/harness-kit/ ，"Governance layer for any AI coding agent"，未回源）
- deusyu/harness-engineering 中文概念文档（未回源）
- 三者与已知腾讯云/Hashimoto 系的独立性需回源后才能下结论。
