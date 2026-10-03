---
type: org_deep_dive
organization: Microsoft + GitHub
content_type: engineering_blog_and_research_analysis
verification_status: verified
source_urls:
  - https://github.blog/engineering/the-cost-of-saying-yes-has-changed/
  - https://github.blog/ai-and-ml/generative-ai/continuous-ai-in-practice-what-developers-can-automate-today-with-agentic-ci/
  - https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/
  - https://github.blog/ai-and-ml/decoding-the-new-ai-lingo-loops-harnesses-squads-hill-climbing-oh-my/
  - https://github.blog/ai-and-ml/github-copilot/the-harness-is-all-you-need-mostly/
  - https://github.blog/ai-and-ml/github-copilot/evaluating-performance-and-efficiency-of-the-github-copilot-agentic-harness-across-models-and-tasks/
  - https://developer.microsoft.com/blog/learn-from-microsoft-transform-software-development-through-an-agentic-platform/
  - https://arxiv.org/abs/2607.01418
  - https://arxiv.org/abs/2606.05391
  - https://github.blog/news-insights/octoverse/what-the-fastest-growing-tools-reveal-about-how-software-is-being-built/
key_concepts:
  - coder_to_orchestrator
  - continuous_ai
  - agent_harness
  - probe_not_deliverable
  - agent_factory
  - spec_as_source_of_truth
---

# Microsoft + GitHub — 平台原语吸收 agent 的路线

> 与 ThoughtWorks（方法论编纂者：靠文字与咨询定义「好的开发方式」）当量相当的**基建编纂者**——不写实践教科书，而是把工作流（Pull Request、CI、Actions、CODEOWNERS）铸成平台原语，用产品默认值定义「好的开发方式」。GitHub 自 2008 年原创 PR 工作流起就是全球软件协作的原子单位；微软 2018 年收购 GitHub、自身经历 Agile@Microsoft→DevOps 转型。2026 年的立场形态由此决定：TW 发布「认知债警告＋harness 学科化」，微软/GitHub 发布「把 agent 编排进 PR/Actions 原语」与「工厂级转型纲领」。
> 生态卡：GitHub 与 Microsoft 分节收录，两者叙事在窗口内互相咬合（微软内部采用数据＝GitHub 产品数据；Copilot runtime 横跨两家产品线）；若后续立场分叉再拆卡。

---

## 思想变迁轨迹（2026）

> 机构卡。2026 年内是「双线并进、逐月加码」：GitHub 侧从数据文走到判断文再到旗舰复盘；微软侧从转型纲领走到实证研究。

| 阶段 | 日期 | 立场标记 | 锚点 |
|------|------|---------|------|
| 自动化类别重划 | 2026-02-03/05 | Octoverse 数据文：强类型是 AI 时代护栏；提出 **Continuous AI**——CI 管「确定性工作」，agent 管「需要判断力的后台工作」 | 本卡 Continuous AI 节 |
| 年度叙事定调 | 2026-06-04 | Universe 2026 官宣口号即立场："agentic era" + **"builders become orchestrators"** | 官宣文（见 Source） |
| 微软纲领落地 | 2026-06-02→25 | Build 2026 + **Customer Zero 系列**：「软件工厂→AI 与 agent 工厂」；"undifferentiated code → unambiguous intent"（spec 单一事实源）；内部数据 90% 开发者用 Copilot、AI review 覆盖 90% PR | 本卡 Customer Zero 节 |
| 研究线补位 | 2026-06-03→07-01 | MSR：oversight 四分类（监督**前移**到生成之前）；Claude Code/Copilot CLI 内部大铺开实证（**+24% merged PR**，自带 "a merged PR is not the same as the value it delivers" 限定） | 本卡 MSR 研究线节 |
| 判断文峰值 | 2026-07-17 | **The cost of saying yes**：生产成本 vs 拥有成本二分——"AI lowers the cost of producing a candidate. It does nothing to lower the cost of owning one" | 本卡工程经济学节 |
| harness 收编 | 2026-06-25→07-27 | 官方确立「模型 vs harness」二分 → 直接宣称 "GitHub Copilot is an agent harness"——harness 词汇的产品化收编 | 本卡 harness 节 |
| 角色论 + 质量出路 | 2026-08-11→24/29 | coder→orchestrator 官方定调；MSR **Proofs Promptly**：agent＋证明助手，人类退到 spec 审阅与关键不变量 | 本卡两节 |
| 旗舰 + 词汇收编 | 2026-09-02→18 | **80 万行生产级 Rust 由 agent 主写**（单人数月）；官方词汇表为 loop engineering / Ralph loop / hill climbing 背书定义并褒贬 | 本卡旗舰节 / 词汇表节 |
| 窗口内待回查 | — | **Octoverse 2026 截至 2026-10-03 未出**（惯例 10 月底–11 月）；**Universe 2026 未办**（10-28/29，Fort Mason）——出/办后回查补证 | 归档页当日核验 |

**判语**：与 TW 的「收紧路线」（经典实践是 AI 速度的制衡力量）相对，微软/GitHub 走的是「吸收路线」——不发明新学科，而是把 agent 装进既有平台原语（PR/Actions/CODEOWNERS/branch protections），让平台默认值替你执行纪律。两条路线在同一批词汇（harness、loop、factory）上交叉，构成本库最有观测价值的对照张力（见文末三重对照节）。

> 📎 本文全部内容来源：见文末 "Source:" 节及 frontmatter `source_urls`。全部证据逐条一手核验（github.blog / developer.microsoft.com / microsoft.com / arxiv.org / icfp26.sigplan.org），日期读自页面本体 meta（datePublished / arXiv Submitted），搜索摘要不采。组织卡评估底稿：`.tmp-msft-github-org-scan-2026-10/`（工作档，收口后清理）。

---

## GitHub：把 agent 编排进平台原语

### 工程经济学定调 — The cost of saying yes has changed（2026-07-17）

窗口内最硬的一条立场文（作者 Dalia Abuadas，engineering 频道）：

> *"Here's the trap, and it it's the most important distinction of the AI era. A change is not cheap just because the code was cheap to generate. It's cheap only if a human can confidently review and own the result."*
> *"AI lowers the cost of producing a candidate. It does nothing to lower the cost of owning one."*

判断线从「agent 能不能写」移到「人能不能验证并拥有」——与 Willison / Fowler 线的「验证是瓶颈」论同构。patch 的定位被显式改写：*"The mistake is to treat the generated patch as the deliverable. It isn't. It's a probe."*

### Continuous AI：自动化类别重划（2026-02-05）

> *"This is the gap Continuous AI fills: not more automation, but a different class of automation. CI handles deterministic work. Continuous AI applies where correctness depends on reasoning, interpretation, and intent."*

GitHub 官方对 SDLC 自动化边界的重划：第一代 AI 编码是代码生成，第二代是「接管认知负担的后台 agent」（文引 Idan Gazit，head of GitHub Next）。配合 02-03 的 Octoverse 数据文——*"Stronger type systems act as early guardrails… make AI-generated changes easier to reason about before code reaches production"*——用平台数据为「AI 时代工程护栏」背书。

### harness 词汇的产品化收编（06-25 / 07-27）

06-25 官方工程评估文先确立二分：*"While the model provides the raw intelligence, the harness shapes how effectively that intelligence is applied… Improve the harness, and every surface benefits."* 07-27 方法论文更进一步：*"just know that GitHub Copilot is an agent harness"*——同一个词，TW 走学科化（Böckeler 的 Guides+Sensors），GitHub 走产品化（Copilot＝harness）。07-27 同时带一条反军备竞赛立场：*"less is way more. It's not about what I install or configure or trick the agent into doing that makes any real difference."*

### 词汇表收编：官方定义 loop engineering（2026-09-02）

> *"Loop engineering is the practice of designing repeatable systems around agents, instead of manually prompting them one task at a time."*

官方为 loop engineering / Ralph loop / harness engineering / squads / hill climbing 背书定义并给出褒贬（*"it can also be expensive and inefficient because every iteration uses more tokens"*）——前沿话语被平台厂商收编的现场，直接接本库 [loop](../../../02_research/01_agent_engineering/loop_engineering/README.md) / [graph](../../../02_research/01_agent_engineering/graph_engineering/README.md) 主题（作者 Cassidy Williams，GitHub Podcast 配套）。

### "How GitHub builds GitHub with AI"：80 万行 Rust 旗舰（2026-09-16）

Stephen Toub 的旗舰复盘：*"we completely rewrote the runtime into more than 800,000 lines of production Rust. AI agents wrote most of the code, spanning 128 pull requests that landed in main and shipped incrementally"*；*"A project that would have taken a whole team of developers a year or two before agents was now completed primarily by a single developer, in only a few months."* runtime 被定义为 "an agentic harness"，横跨 VS Code / Visual Studio / Copilot 全产品线。

同群复盘（"How we…" 系列的方法论内核）：

- **07-10 code review 改造**：*"But the tools weren't the problem. The instructions were."*——重写指令后 review 成本约降 20% 而质量不降；agent 工程的反直觉教训：瓶颈在「agent 怎么读 PR」不在工具。
- **08-04 PR 栈分解**：*"Stacked pull requests introduce a different and better structure of delivery. The principle is simple: decomposition."*——agent 放大而非取消「怎么组织 PR」的选择。
- **09-02 效率方法论**：*"tokens per tool call is the wrong objective"*——整任务级 outcome 优化 + offline benchmark / controlled online experiments 双层验证。
- **09-18 风险分级审查**：*"Pretending every change carries the same risk is not rigor. It is just a bad use of time."*——「该不该读 agent 写的代码」的官方答案：按风险与代码库熟悉度分层。
- **08-11 coder→orchestrator**（口径注记：产品口径最重，同文称 Copilot 为 "control plane"，降权收录）：*"Developers are the system orchestrators who define triggers, scope agent permissions, and design handoffs."*

---

## Microsoft：从软件工厂到 AI 与 agent 工厂

### Customer Zero 转型纲领（2026-06-25）

Poonam Gupta（Partner Director of PM, 1ES & Azure DevOps）的纲领文：

> *"At Ignite 2025, we shared the vision of Microsoft's transformation from a software factory to an AI and agent factory… An agent factory is what comes next, where agents collaborate across the entire software development lifecycle, systems learn and improve each cycle, and every team works side by side with agents."*
> *"Another important shift we've made is moving from undifferentiated code to unambiguous intent. In practice, that means treating specs as a single source of truth to define what we're building, help generate the right changes, verify that the system behaves as intended, and even help operate it in production."*

配套内部数据：*"Over 90% of Microsoft developers now use GitHub Copilot, and our AI code review covers 90% of Microsoft pull requests and speeds completion time by more than 10%."* Build 2026 期间的 Inside Track 文（06-02）是同一纲领的 IT 组织视角（治理先行、平台化铺开）。

### MSR 研究线：监督前移 / 采用实证 / 形式验证（2026-06-03 → 08-24/29）

1. **Human oversight of agentic systems in practice**（arXiv 2606.05391，06-03）：*"We found at least four forms of emergent oversight work: a priori control, co-planning, real-time monitoring, and post hoc review."*——监督工作不止事后回顾，a priori control 与 co-planning 把监督**前移到生成之前**，直接冲击传统 SDLC 阶段论。
2. **Adoption and Impact of Command-Line AI Coding Agents**（arXiv 2607.01418，07-01，Murphy-Hill/Butler/Savelieva）：*"adopters merged roughly 24% more pull requests than they would have otherwise"*；*"organizations should treat visible peer use as central to rollout strategy"*——对自家 early-2026 Claude Code + Copilot CLI 数万工程师铺开的官方测量（媒体「24% 研究」的一手本体），摘要自带审慎限定 *"a merged PR is not the same as the value it delivers"*。
3. **Proofs Promptly**（ICFP 2026，PACMPL DOI 10.1145/3828709，会议周 08-24/29，全 MSR 作者）：*"The widespread adoption of AI-assisted coding is directly proportional to an increase in software bugs; can AI-assisted formal verification help reduce bugs at a comparable scale?"*——三位专家两周完成估需约半年的证明工程量；MSR 式质量出口：agent＋证明助手产出机器检查代码，人类退到 spec 审阅与关键不变量。

---

## 与 ThoughtWorks 的三重对照张力

1. **同一指标两种立场**：TW 把「coding throughput as productivity」列 Caution（雷达 Vol 34：用代码行数/PR 数衡量生产力是危险误导）；微软把 24% PR lift、90% 采用率当转型证据发布（论文自带「merged PR ≠ value」限定）。
2. **同一词汇两种收编**：「harness」在 TW 走学科化（independent ownable discipline），在 GitHub 走产品化（Copilot＝agent harness）。
3. **词汇收编的标本**：GitHub 官方为 loop engineering / Ralph loop / hill climbing 背书定义并褒贬——前沿话语进入平台厂商词汇表的现场。

## 口径分级注记（读卡须知）

- 本卡证据按口径强度分级：**判断层**（cost of saying yes / Continuous AI / 词汇表 / 风险分级审查）、**工程复盘层**（How we… 系列）、**纲领层**（Customer Zero——转型叙事与平台销售叙事耦合）、**产品口径降权**（coder→orchestrator 的 "control plane"、Universe 官宣本质是售票文）。
- Customer Zero 三篇 Tech Community 子故事（Azure SRE Agent / 1ES 安全合规 / Azure Networking）被 WAF 拦截，仅经 06-25 主篇间接核验，引用须标注。
- Octoverse 2025 头条（2025-10-28）及 Ignite 2025「agent factory」愿景为窗口前背景，不作证据。

---

## 关键引用

> *"AI lowers the cost of producing a candidate. It does nothing to lower the cost of owning one."* — The GitHub Blog, 2026-07-17

> *"The mistake is to treat the generated patch as the deliverable. It isn't. It's a probe."* — The GitHub Blog, 2026-07-17

> *"An agent factory is what comes next, where agents collaborate across the entire software development lifecycle."* — Microsoft Customer Zero, 2026-06-25

> *"While the model provides the raw intelligence, the harness shapes how effectively that intelligence is applied."* — The GitHub Blog, 2026-06-25

---

**Source:** [The cost of saying yes has changed（2026-07-17）](https://github.blog/engineering/the-cost-of-saying-yes-has-changed/) · [Continuous AI in practice（2026-02-05）](https://github.blog/ai-and-ml/generative-ai/continuous-ai-in-practice-what-developers-can-automate-today-with-agentic-ci/) · [Migrating the Copilot runtime to Rust（2026-09-16）](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/) · [Decoding the new AI lingo（2026-09-02）](https://github.blog/ai-and-ml/decoding-the-new-ai-lingo-loops-harnesses-squads-hill-climbing-oh-my/) · [The harness is all you need (mostly)（2026-07-27）](https://github.blog/ai-and-ml/github-copilot/the-harness-is-all-you-need-mostly/) · [Evaluating the Copilot agentic harness（2026-06-25）](https://github.blog/ai-and-ml/github-copilot/evaluating-performance-and-efficiency-of-the-github-copilot-agentic-harness-across-models-and-tasks/) · [Better tools made Copilot code review worse（2026-07-10）](https://github.blog/ai-and-ml/github-copilot/better-tools-made-copilot-code-review-worse-heres-how-we-actually-improved-it/) · [Turn one giant AI-generated PR to a reviewable stack（2026-08-04）](https://github.blog/engineering/turn-one-giant-ai-generated-pull-request-to-a-reviewable-stack/) · [From coder to orchestrator（2026-08-11，产品口径降权）](https://github.blog/developer-skills/career-growth/from-coder-to-orchestrator-how-agents-shift-the-role-of-a-developer/) · [How we make AI coding more cost efficient（2026-09-02）](https://github.blog/ai-and-ml/github-copilot/how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality/) · [Should you read the code（2026-09-18）](https://github.blog/ai-and-ml/should-you-read-the-code-is-rag-dead-and-did-skills-kill-mcp/) · [What the fastest-growing tools reveal（2026-02-03）](https://github.blog/news-insights/octoverse/what-the-fastest-growing-tools-reveal-about-how-software-is-being-built/) · [GitHub Universe is back: the agentic era（2026-06-04）](https://github.blog/news-insights/company-news/github-universe-is-back-all-together-now-in-the-agentic-era/) · [Learn from Microsoft: agentic platform（Customer Zero，2026-06-25）](https://developer.microsoft.com/blog/learn-from-microsoft-transform-software-development-through-an-agentic-platform/) · [Microsoft Build 2026 Inside Track（2026-06-02）](https://www.microsoft.com/insidetrack/blog/microsoft-build-2026-empowering-our-developers-to-adopt-agentic-ai-at-microsoft/) · [arXiv 2607.01418：CLI agents 采用研究（2026-07-01）](https://arxiv.org/abs/2607.01418) · [arXiv 2606.05391：oversight 四分类（2026-06-03）](https://arxiv.org/abs/2606.05391) · [Proofs Promptly（ICFP 2026，DOI 10.1145/3828709）](https://dl.acm.org/doi/10.1145/3828709)
