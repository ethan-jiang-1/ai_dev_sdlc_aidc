---
type: org_evidence
directory: 01_advocates/orgs
observation_date: 2026-10-06
---

# google — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

## Google/GCP 面 ·《The Outer Loop》官方论坛长文＋ Agent Quality Flywheel（2026-07-20）

- URL：https://discuss.google.dev/t/the-outer-loop-how-google-cloud-and-alphaevolve-are-defining-agentic-governance-and-self-evolution/383304 （Google Developer Forums 官方 Google Cloud 版块，2026-07-20，全文取得，作者 Enrique_Chan——**作者雇员身份未在页面标明**）；官方博文 "Driving the Agent Quality Flywheel from your coding agent"（developers.googleblog.com，Cloud Next '26 发布，经上文引用；两次 fetch 均超时/失败，**未取得**）
- 来源类型：官方开发者论坛署名长文（渠道半官方、作者身份待核）＋官方博文（存在性经引用确认、正文未取得）
- 号召力口径：②——在 Google 官方渠道正面使用 loop engineering 词表并把 AlphaEvolve/ADK 接入叙事

**逐字摘录**（Enrique_Chan 论坛原文）：

> "Urged by architectural pioneers like Peter Steinberger and codified by frameworks defined by Google engineers like Addy Osmani, this movement has found its name: Loop Engineering."
>（**值得注意的口径错误**：把 Osmani 称为 "Google engineers"——若非笔误，说明 Google 侧作者仍把 Osmani 记为 Google 员工；与库内一手 bio（Anthropic Claude Code MTS，见 02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-26-a-originators.md）冲突，媒体/官方渠道的 bio 滞后值得记一笔。）

> "A loop running unattended is also a loop making mistakes unattended."
>（**推动派阵营里最精炼的难点格言**——无人值守的循环也是无人值守地犯错的循环。出自其文末 "core heuristic"。）

> "The architectural invariant of the Flywheel is simple: The optimizer never grades its own work."
>（转述 Cloud Next '26 发布的 Agent Quality Flywheel 官方框架：优化器永不自评——Google 把"验写分离"立为官方架构不变量。）

> "How do we move from the Inner Loop of agent development (Day 0) to the Outer Loop of agent governance, operations, and autonomous optimization (Day 2)?"
>（Google 的 inner/outer 双环词表＋治理定位——与 Tessl 三环、Voss 4+1、Runkle 四环并列为第五种厂商分类学。）

**该条支持的最小主张**：Google 官方开发者渠道 2026-07 出现体系化 loop engineering 长文（治理翼），Cloud Next '26 有官方 Flywheel 框架与其呼应；但作者身份与官方博文正文均未在一手核到。
**派别适配**：**推动票（厂商·治理翼，渠道半官方降半级）**——Flywheel 博文正文补到前，建议只按论坛文计。

---

### Google Jules / Gemini CLI —— 部分解决（Jules 窗口内官方静默＝负发现；机制在册走 living docs；Gemini CLI 一手 release note 行）

- **C1. Jules 官方 changelog——窗口内静默（负发现）**
  - URL/日期：https://jules.google/docs/changelog ；实取 2026-10-06（curl 直取 129KB）。**最新条目为 "Gemini 3.1 Pro is now available in Jules｜Mar 09, 2026"，其后（2026-06-01 至实取日）无任何官方 changelog 条目**——全列表 Mar 2026→May 2025 逐条实取核对。
  - 通道状态：官方一手、直取成功；负发现本身可信度强（不是抓取失败）。
  - 窗口外机制在册（供"把控性"主题引用，标注窗口外）："Introducing the Planning Critic for Auto-Approved Plans"（Jan 26, 2026）、"Put routine maintenance on autopilot with Scheduled Tasks"（Dec 10, 2025）——标题级。
  - **该条支持的最小主张**：Jules 的异步 agent 面在 2026-06 后没有官方产品增量；运动窗口内该产品无新话语（与 Anthropic/Cursor/Warp 的密集发牌形成反差，可供判读引用）。
  - 派别适配：负发现，不定票；作厂商面节奏差证据。

- **C2. Jules《Limits and Plans》官方文档（living docs，实取 2026-10-06）**
  - URL：https://jules.google/docs/usage-limits
  - 逐字（计划表数据实取）：Daily Tasks (rolling 24 hours)＝**15 / 100 / 300**（Jules/Pro/Ultra）；Concurrent Tasks＝**3 / 15 / 60**。
  - 逐字摘录："Will the features and limits in these plans change over time? We may adjust limits and features as we learn how people are using the product."
  - **该条支持的最小主张**：异步环的并发/日任务量被厂商做成**硬配额分层**——这是 target 9（预算上限机制）Jules 行的官方一手。
  - 派别适配：机制登记（把控面）。

- **C3. Gemini CLI 官方仓库 release notes（api.github.com 实取）**
  - 通道：https://api.github.com/repos/google-gemini/gemini-cli/releases （Google 维护官方仓库，release note 即官方一手载体）。
  - 逐字（2026-09-30，v0.64.0-nightly.20260930.g38700b4b3）：

> "fix(core): enable autonomous plan execution in non-interactive mode"

  - 另取（2026-09-16，v0.62.0-nightly.20260916）："fix(core): ensure AgentLoopContext properties are preserved across object spread"——**"AgentLoopContext" 为官方代码/提交词表中的正式构件名**。
  - **该条支持的最小主张**：Gemini CLI 在窗口内官方点亮了"非交互模式下的自主计划执行"（headless 自主环），载体为官方 release note。
  - 派别适配：**推动·厂商**（carrier 为 nightly release note，引用时注明）。
