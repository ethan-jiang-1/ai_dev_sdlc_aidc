# Spec-Driven Development (SDD) 工具生态现状、趋势与影响力（2026-09 快照）

> 观测日期：**2026-09-20**（任务要求"2026-09-17 附近"；GitHub API 数字为该日实测，另注明交叉验证）。
> 方法：一手源优先（GitHub REST API v3 `api.github.com`、官方 README/release/blog），二手报道仅作补充并标注。
> 定位：2026-09-21 起属实践层 `03_practice/spec_driven_development/` 本目录（不再使用旧 "Topic 07 / topic-NN" 编号身份）；本文提供生态全景与原始指标，**横向比较结论以同目录 [comparison.md](comparison.md) 为权威**。
> **快照锚点声明**：stars/forks 等快照以本文 §3 表为回溯锚（观测 2026-09-20），tools/ 各篇及他处数字若差 ±1~10 属同日实时漂移，以本表为准。

---

## 1. 逐项调研

### 1.1 GitHub Spec Kit（github/spec-kit）

- **Stars / Forks**：**138,033 stars / 12,366 forks / 307 open issues / 706 watchers**。
  来源：`https://api.github.com/repos/github/spec-kit`（观测 2026-09-20）。
- **创建时间**：2025-08-21（同上 API `created_at`）。
- **活跃度**：**高，仍活跃**。最近 push 2026-09-18；release 周节奏：v1.0.6（2026-09-10）→ v1.0.7（2026-09-15）→ v1.0.8（2026-09-17），来源：`https://api.github.com/repos/github/spec-kit/releases?per_page=3`（观测 2026-09-20）。
- **定位与机制一句话**：GitHub 官方的 SDD 工具包（`specify` CLI），把 constitution → spec → plan → tasks 的模板化工作流注入 Claude Code / Copilot / Cursor / Gemini CLI 等任意 agent，"`/speckit.constitution` `/speckit.spec` …" 斜杠命令驱动（来源：README 与 release notes，同上）。
- **采纳迹象**：**100+ contributors**（contributors API `per_page=100` 满页，观测 2026-09-20；头部为 GitHub 员工 localden/mnriem，社区贡献者长尾）。有扩展生态（community catalog 中第三方 extension 数十个）。ThoughtWorks Radar 设有独立条目 "GitHub Spec Kit"（languages-and-frameworks 象限，来源：https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit ，观测 2026-09-20；条目定性文字页面 JS 渲染未能提取，仅确认条目存在）。⚠ 勘误（2026-09-21）：该独立条目页未在本目录补遗核查中命中、未获核验，维持正文点名口径，见 [debate/authoritative-verdicts.md](debate/authoritative-verdicts.md) 补遗。Martin Fowler 站点专文分析（见 §3）。
- **趋势判断**：**上升**。创建仅 13 个月即 138k stars；周级 release；extension 生态成型；大厂（GitHub 自家）持续投入。证据强度：强。

### 1.2 OpenSpec（Fission-AI/OpenSpec）

- **归属确认**：官方仓库确为 **Fission-AI/OpenSpec**（公司 Fission AI），官网 https://openspec.dev/ 。
- **Stars / Forks**：**69,639 stars / 4,771 forks / 241 open issues / 286 watchers**。
  来源：`https://api.github.com/repos/Fission-AI/OpenSpec`（观测 2026-09-20）。
- **创建时间**：2025-08-05。
- **活跃度**：**高**。最近 push 2026-09-18；v1.13.1 "Hardened CLI, safer archives" 发布于 2026-09-17（releases API，观测 2026-09-20）。
- **定位与机制一句话**：轻量级、厂商中立的 SDD CLI：`openspec` 用 Markdown spec + change delta 管理"提议→应用→归档"变更流，生成的 skills/commands 面向 Claude Code、Cursor、Copilot、Codex 等多 agent，强调对**已有代码库**渐进式加规格（来源：repo description "Spec-driven development (SDD) for AI coding assistants" + v1.13.1 release notes）。
- **采纳迹象**：**~50 名 contributors**（contributors API per_page=100 返回约 50+ 条，观测 2026-09-20；头部 TabishB 519 次、clay-good 144 次，其余为长尾）。**进入 ThoughtWorks Radar**（Tools 象限独立条目 "OpenSpec"，来源：https://www.thoughtworks.com/radar/tools/openspec ，观测 2026-09-20；定性文字 JS 渲染未提取）。
- **趋势判断**：**上升**。与 Spec Kit 同月创建、体量约其一半，但作为创业公司项目做到 70k stars 且被 TW Radar 收录，是"非大厂也能赢"的信号。证据强度：中强（公司背书弱于 GitHub，但社区指标实）。

### 1.3 Superpowers（obra/superpowers）

- **归属确认**：官方仓库确为 **obra/superpowers**（Jesse Vincent / obra 个人项目），描述 "An agentic skills framework & software development methodology that works"。
- **Stars / Forks**：**289,048 stars / 25,856 forks / 371 open issues / 1,081 watchers**。
  来源：`https://api.github.com/repos/obra/superpowers`（观测 2026-09-20）；**交叉验证**：github.com 页面实测 "289,049 users starred"（同日，差 1 为实时增长），API 二读亦为 289,049。数字可信。
- **创建时间**：2025-10-09。
- **活跃度**：**极高**。最近 push 2026-09-19；v6.4.1 发布于 2026-09-19（当日 release，releases API 观测 2026-09-20）。
- **定位与机制一句话**：不是"写 spec 模板"而是**整套 agent 开发方法论插件**——brainstorming→writing-plans→executing-plans（原生/子代理两种执行模式）→TDD→code review 的技能链，以 Claude Code plugin 为主、已扩展支持 OpenCode、Muse、Qwen Code 等多 harness（来源：v6.4.1 release notes 全文，观测 2026-09-20）。
- **采纳迹象**：**~46 名 contributors**（contributors API，观测 2026-09-20；obra 本人 524 次占绝对主导，其余长尾——**巴士因子低**）。repo topics 明确含 "subagent-driven-development"。是整个清单中 star 绝对值最高的项目，说明"方法论打包成 skills"的形态比"spec 模板"更抓社区。
- **趋势判断**：**强劲上升**（但个人主导，持续性存疑）。11 个月 289k stars 为异常快速度。证据强度：指标强、组织可持续性弱。

### 1.4 BMAD-METHOD（bmad-code-org/BMAD-METHOD）

- **Stars / Forks**：**53,266 stars / 6,009 forks / 仅 66 open issues / 417 watchers**。
  来源：`https://api.github.com/repos/bmad-code-org/BMAD-METHOD`（观测 2026-09-20）。
- **创建时间**：2025-04-13（本批最早）。
- **活跃度**：**高**。最近 push 2026-09-20（观测当日）；v6.12.0 发布于 2026-09-04（releases API）。
- **定位与机制一句话**：多 agent"敏捷团队角色扮演"方法论——Analyst/PM/Architect/Dev/QA 等 agent 依次产出 PRD→架构→story→代码，v6 转向 "Build 决定仪式感轻重" 的可裁剪流程（来源：repo 描述 + v6.12.0 release notes）。
- **采纳迹象**：**100+ contributors**（contributors API per_page=100 满页，观测 2026-09-20；头部 Brian Madison(匿名署名) 886 次、alexeyv 662 次）。仓库 topic 自带 `spec-driven-development`。open issues 仅 66（治理严格/收口快）。license 为自定义 "Other"（非标准 OSI，商用需查）。
- **趋势判断**：**平台期偏上升**。星标增速落后于 Spec Kit/OpenSpec/Superpowers，但维护极活跃、社区成熟（最早创建、方法论最"重"）。证据强度：中强。

### 1.5 Amazon Kiro（AWS）— 厂商采纳证据

- **一手源**：AWS Kiro 官方博客 "One year of Kiro: a look back, and a look ahead"（Deepak Singh, VP DevEx & Agents，2026-07-14），https://kiro.dev/blog/one-year/ （观测 2026-09-20）。关键声明：
  - 2025-07 preview 上线，**5 天内 10 万开发者试用**，10 月翻倍；**2025-11 GA**；
  - 自称 "first to bring spec-driven development to AI coding tools"；
  - 企业客户点名：**Siemens**（3-4 人月项目 2 周单人完成）、**SmugMug/Flickr、Appian**，以及高校（Loyola Marymount、ASU）与多家初创；
  - 生态：100+ 官方合作方 powers（Figma、Stripe、Postman、Supabase、Netlify），社区 15,000+ powers；开源组织 kirodotdev-labs。
  - 注意：以上均为厂商自述数字（一手但利益相关），无独立审计。
- **定位**：把 spec（requirements EARS 化 → design → tasks）做成 IDE 一等公民的 agentic IDE，"better than vibe coding"。
- **趋势判断**：**上升（商业验证最强的一条线）**。Evidence：GA 后产品线扩张到 CLI/Web/Mobile + GovCloud。证据强度：强（事实层）/ 中（数字为自述）。

### 1.6 其他值得注意

**Tessl**（tessl.io）
- 定位：Snyk 创始人 Guy Podjarny 创办的 "spec-centric / AI-native" 开发平台，主张 "spec as source of truth"，有 Registry（如 `spec-as-source` 包，https://tessl.io/registry/spec-driven-development/spec-as-source/3.0.0/ ，观测 2026-09-20）。
- 资金信号（二手报道，标注）：$125M 融资（[TechFundingNews](https://techfundingnews.com/tessl-raises-125m-ai-native-software-development/)）；后续 $100M、估值约 $750M（[Yahoo Finance/SCMP 转载](https://sg.finance.yahoo.com/news/exclusive-tessl-worth-reported-750-080100819.html)，观测 2026-09-20）。官方博客确认 Series A：https://tessl.io/blog/announcing-our-series-a-for-ai-native-software-development/ （标题页确认，正文 JS 截断）。
- 判断：~~资本层面上升~~（2026-03 起公开停摆转型，见 [comparison.md](comparison.md) §1⁴ 勘误与 [tools/tessl.md](tools/tessl.md)；写作时点口径作存档）；开源社区声量小于 Spec Kit/Superpowers。

**claude-task-master**（eyaltoledano/claude-task-master）
- **28,085 stars / 2,619 forks**，创建 2025-03-04（API，观测 2026-09-20）。
- **停滞信号**：`pushed_at = 2026-04-28`，**近 5 个月无 push**；homepage 改为 tryhamster.com（转向商业产品 Hamster）。判断：**下降/被放弃**——早期（2025 H1）PRD→task 拆解的事实标准，已被 Spec Kit/OpenSpec/Superpowers 挤出。证据强度：强（API 直读）。

**Kiro-style 开源仿制品**：HN 上持续出现个人仿制（例：Show HN "I Made a Claude Skill for SDD"，自称照 Kiro 的 SDD 管理做的，2026-05-21，40 分 17 评，https://github.com/FredAntB/Spec-Driven-Development ）。说明 Kiro 的 spec 工作流成为被模仿对象，但单品影响力小。

### 1.7 调研中新发现、值得补充的对象

- **Verified Spec-Driven Development (VSDD)**：2026-02-28 HN 211 分 118 评（gist: https://gist.github.com/dollspace-gay/d8d3bc3ecf4188df049d7a4726bb2a00 ，经 HN Algolia API 检索，观测 2026-09-20）——社区把 SDD 往"可验证规格"方向推进的新分支。
- **Marmelab "Spec-Driven Development: The Waterfall Strikes Back"**：2025-11-12，HN 225 分 191 评（https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html ）——最具传播度的批判性分析。

---

## 2. 横向问题

### A. 社区/行业"公认较好"的 SDD 方案是哪几个？

依据（按可追溯性排列）：
1. **ThoughtWorks Radar 独立条目**：OpenSpec 的 Vol.34 独立条目已获官方直读确认（Tools 象限，Assess）；"spec-driven development" 作为 technique 有条目（Vol.33 Assess）。GitHub Spec Kit 的独立条目**未获核验**（条目页未在补遗核查中命中，仅 Vol.33 正文点名；见 [debate/authoritative-verdicts.md](debate/authoritative-verdicts.md) §补遗）。行业背书成立但强度需按此口径区分。
2. **Martin Fowler 站点专文** "Understanding Spec-Driven-Development: Kiro, Spec-Kit, and Tessl"（martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html，HN 2025-10-16 128 分）——把 **Kiro、Spec Kit、Tessl** 并列为三大代表。
3. **社区体量**：Superpowers、Spec Kit、OpenSpec、BMAD 四个 5 万+ star 项目全部活跃维护（2026-09 均有 release）。

**结论**：公认头部 = **GitHub Spec Kit**（大厂官方、事实默认）、**Kiro**（商业产品、企业验证）、**OpenSpec**（中立轻量、TW Radar）；**Superpowers** 是社区最热但属于"方法论/skills"而非纯 SDD；**BMAD** 是"重流程"流派代表。

### B. SDD 方向整体热度：上升还是退潮？

> ⚠ 勘误指针（2026-09-21）：本小节"仍在上升/两极辩论期"为 2026-09-20 快照口径，已被 [debate/README.md](debate/README.md) 的 2026H2 裁决（话语退潮、工件固化、SDD 跌出 Radar 当前版）取代，趋势判断以那边为权威。以下保留作快照存档。

**判断：仍在上升，但已从"新鲜事物"进入"两极辩论期"。**

上升信号（2025H2–2026）：
- ThoughtWorks Radar 为 spec-driven development、OpenSpec 设独立条目（Spec Kit 条目页后经补遗核查未命中，仅 Vol.33 正文点名，见 [debate/authoritative-verdicts.md](debate/authoritative-verdicts.md) 补遗；观测 2026-09-20）；
- HN Algolia 检索 "spec-driven development" 共 **138 条 story**（观测 2026-09-20），且高热帖横跨 2025-09 → 2026-05 持续出现；
- Kiro 一周年报告用户逐季翻倍、企业名单扩张（2026-07，厂商自述）；
- Tessl 两轮融资累计 $225M+（二手，标注如上）；
- Spec Kit/OpenSpec/Superpowers/BMAD 四项目 2026-09 均有当日/当周级 push 与 release。

退潮/分化信号：
- HN 出现 "Ask HN: What Happened to Spec-Driven Development?"（2026，检索确认存在）与 "SDD doesn't work if you're too confused to write the spec"（2026-02-10）等质疑帖；
- 最早的 claude-task-master 已停滞（5 个月无 push）——**工具层开始洗牌**；
- 批评文章（Marmelab "Waterfall Strikes Back"）获得 SDD 话题最高讨论度（225 分/191 评），说明叙事已从"银 器"转向辩论。

综合：**热度上升 + 共识收窄**——大厂（GitHub、AWS）与咨询业（TW）已正式接纳，社区进入"哪种 SDD 形态对"的细化竞争（模板流 vs 方法论流 vs 可验证流）。

---

## 3. 对比表格

| 项目 | Stars（2026-09-20 API） | 创建 | 活跃度 | 定位 | 趋势判断 | 证据强度 |
|---|---|---|---|---|---|---|
| obra/superpowers | 289,048 / 25.9k forks | 2025-10-09 | push 09-19；v6.4.1 09-19；极高 | Agent 方法论技能链（brainstorm→plan→TDD→review），Claude Code 为主、多 harness | 强上升（个人主导风险） | 强（双源验证）；组织可持续性=中 |
| github/spec-kit | 138,033 / 12.4k forks | 2025-08-21 | push 09-18；周级 release（v1.0.8, 09-17）；高 | GitHub 官方 SDD 工具包，spec→plan→tasks 模板注入各 agent | 上升 | 强（官方+TW Radar+100+ contributors） |
| Fission-AI/OpenSpec | 69,639 / 4.8k forks | 2025-08-05 | push 09-18；v1.13.1 09-17；高 | 厂商中立轻量 SDD CLI，change-delta 管理，面向多 agent | 上升 | 中强（TW Radar； contributor 面窄于 Spec Kit） |
| bmad-code-org/BMAD-METHOD | 53,266 / 6.0k forks | 2025-04-13 | push 09-20；v6.12.0 09-04；高 | 多 agent 角色化敏捷方法论（PM/架构/Dev/QA），重流程可裁剪 | 平台期偏上升 | 中强（license 非标准，需注意） |
| eyaltoledano/claude-task-master | 28,085 / 2.6k forks | 2025-03-04 | **push 停在 2026-04-28，停滞** | PRD→task 拆解管理（早期事实标准） | **下降（项目转向商业产品）** | 强（API 直读） |
| Amazon Kiro（商业，无 star） | n/a（5 天 10 万试用，自述） | preview 2025-07，GA 2025-11 | 产品线持续扩张（CLI/Web/Mobile/GovCloud） | spec 一等公民的 agentic IDE | 上升 | 事实层强；数字为厂商自述=中 |
| Tessl（商业） | n/a | 2024 创立 | Registry 活跃 | spec-as-source 平台 | ~~资本上升~~（2026-03 起停摆，见 comparison.md⁴ 勘误） | 中（融资为二手报道） |

---

## 4. 来源清单（均标注观测日期 2026-09-20）

一手源：
- GitHub API：`api.github.com/repos/{github/spec-kit, Fission-AI/OpenSpec, obra/superpowers, bmad-code-org/BMAD-METHOD, eyaltoledano/claude-task-master}`（repos / releases / contributors 端点）
- https://kiro.dev/blog/one-year/ （Kiro 官方博客，2026-07-14）
- https://tessl.io/blog/announcing-our-series-a-for-ai-native-software-development/
- https://github.com/obra/superpowers 页面 star 交叉验证

二手/索引源（仅补充）：
- ThoughtWorks Radar 条目：[spec-driven development](https://www.thoughtworks.com/radar/techniques/spec-driven-development) · [GitHub Spec Kit](https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit) · [OpenSpec](https://www.thoughtworks.com/radar/tools/openspec)（条目存在性确认；定性文字 JS 渲染未提取）
- Martin Fowler: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- HN Algolia API（"spec-driven development" 138 stories，观测 2026-09-20）：Marmelab 2025-11（225 pts）、VSDD 2026-02（211 pts）、Fowler 文 2025-10（128 pts）、Ask HN 等
- Tessl 融资：[TechFundingNews](https://techfundingnews.com/tessl-raises-125m-ai-native-software-development/)、[Yahoo Finance](https://sg.finance.yahoo.com/news/exclusive-tessl-worth-reported-750-080100819.html)

**已知局限**：① Kiro 用户数/企业案例为厂商自述，未经第三方核实；② TW Radar 各条目的 Assess/Trial/Hold 定级未能提取（页面 JS 渲染），仅确认条目存在；③ contributor 数为 `per_page=100` 一页实测（Spec Kit/BMAD 满页 100+，OpenSpec ~50+，Superpowers ~46），未做分页穷举；④ Kiro-style 仿制品单品未逐一深挖。
