---
type: kol_deep_dive
person: Ryan Lopopolo
organization: Google Cloud (Principal Engineer, Agentic Google Cloud Platform)；ex-OpenAI
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://openai.com/index/harness-engineering/
  - https://github.com/openai/symphony
  - https://github.com/lopopolo/harness-engineering
  - https://raw.githubusercontent.com/lopopolo/harness-engineering/trunk/docs/lineage/README.md
  - https://www.zenml.io/llmops-database/zero-human-written-code-harness-engineering-for-autonomous-ai-agents-at-scale
  - https://www.zenml.io/llmops-database/extreme-harness-engineering-building-production-software-with-zero-human-written-code
  - https://www.infoq.com/news/2026/02/openai-harness-engineering-codex/
  - https://tessl.io/podcast/109/
  - https://hyperbo.la/contact/
  - https://hyperbo.la/w/agents-agents-agents/
  - https://hyperbo.la/w/software-work-not-scheduled/
  - https://hyperbo.la/w/harness-engineering-the-blog-build/
  - https://hyperbo.la/w/code-is-not-the-artifact/
  - https://hyperbo.la/w/agent-platform/
  - https://hyperbo.la/w/aligned-to-whom/
  - https://hyperbo.la/w/lazy-prompt-rustsec/
  - https://hyperbo.la/w/tell-the-model-how-to-work/
  - https://www.latent.space/p/harness-eng
  - https://cloud.google.com/blog/topics/developers-practitioners/agent-factory-recap-agent-harnesses-shifting-left-and-autonomous-coding/
key_concepts:
  - zero_human_written_code
  - harness_engineering
  - agent_self_review_loop
  - progressive_disclosure
  - ghost_library
  - lazy_prompter
  - agent_platform
  - utilization_to_effectiveness
---

# Ryan Lopopolo — Harness Engineering 提出者（OpenAI → Google Cloud）

> 原 OpenAI Frontier Product Exploration 团队 Member of Technical Staff，**2026-07 加入 Google Cloud（Principal Engineer, Agentic Google Cloud Platform，一手核验：hyperbo.la 自述 + GC 官方博客 09-25）**。职业线 Citadel → Box → Stripe → Brex → Snowflake → OpenAI → Google Cloud。他领导零人手写代码实验、创造 "Harness Engineering" 一词（Fowler 与 ThoughtWorks 推广；GC 官方口径 "the person who coined the term agent harness"）。2026 年他在个人站 hyperbo.la 发文 18 篇——harness 方法论从实验报告生长成一套完整体系。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及 frontmatter `source_urls`。单人深度分析，所有引用基于其公开材料。2026-10-03 深挖重构：谱系文档（field guide docs/lineage/）+ hyperbo.la 2026 全部 18 篇 + Agent Factory 逐段 + Latent Space 访谈（⚠️ 机器转写，ASR 噪声处标注 [原文如此]）。X 登录墙内容一律不采。

## 当前立场小结（2026-10-03）

1. **harness 的定义收束**（GC 官方口径，09-25）："the study and practice of **putting a model into an environment where it can succeed**"。
2. **人保留两件事**：merge decision 与 release authority——实现评审与合并可授权给 agent + harness，"ask a human for a **merge decision** rather than implementation time"（《Software Work Is No Longer Scheduled》03-13）。
3. **lazy prompter 是目标**："**I aspire to be an incredibly lazy prompter.** If I have done the job to give the model the tools and context it needs to ground itself, I don't need to write a long prompt. It figures it out."（09-25）——"prompt and pray" 是其反面。
4. **利用率降级为诊断**："a billion tokens per engineer per day is a **utilization target**. It asks how much of the software lifecycle the agents are actually allowed to do."→ 后续修正："token spend is unanchored in business value or ROI"＋"**effectiveness is what matters**"。
5. **agent 的新定义**（09-05《agent-platform》）：agent = "**a parameterized program over a set of capabilities**"；agent platform = "**the system for minting agents from compositions of capabilities**"——Codex/Claude Code/Pi 都**不算** agent platform。
6. **alignment 是不可约的复杂度**（09-12《aligned-to-whom》）："**There is no such thing as an unhackable grader**… To solve this—to solve alignment—is irreducible complexity"；"long-term coherence through use of agentic work product is a very unsolved problem"。
7. **对 MCP 转向 bearish**（Latent Space 访谈，04-07）："the harness forcibly injects all those tokens… **They mess with auto compaction**"——与 2025《tool-discovery》的立场演化（详见五轴第 3 轴）。

---

## 思想变迁轨迹（2026）

> **本表是索引**——各阶段详见下文专节（实验 / Symphony / 五轴 / 短文精选 / Agent Factory / 谱系）。

| 阶段 | 日期 | 立场标记 |
|------|------|---------|
| 术语诞生与实验定调 | 2026-02 | OpenAI 官方文《Harness Engineering: Leveraging Codex in an Agent-First World》（02-11，他自指 "seminal"）；InfoQ 报道扩散 |
| **Symphony 开源** | 2026-02-26 | openai/symphony（Apache-2.0，Elixir，27.5k★，最后 push 09-15；他离开后由 OpenAI 侧维护，无 v2）；03-13 口径："3-5 PRs/人/天 without Symphony → **75 PRs/人/周 with Symphony**" |
| 术语被采纳（影响力弧线） | 2026-02→05 | Fowler 站内 Böckeler 系列（02-17→05-27）+ TW 雷达背书——实验报告变成学科名（详见谱系节） |
| 方法论体系化 | 2026-03 | hyperbo.la 密集期：agents-agents-agents（利用率）、software-work-not-scheduled（划界）、code-is-not-the-artifact（幽灵库本体论）、blog-build（可执行约定） |
| 演讲与访谈 | 2026-04-07/17 | Latent Space 访谈（1M LOC/1B toks/0% human 的完整叙述 + 深重构 open problem + MCP bearish）；AI Engineer《Humans Steer, Agents Execute》 |
| 词汇再定义 | 2026-08→09 | tell-the-model-how-to-work（zero skills）；agent-platform（agent≠产品）；aligned-to-whom（alignment 不可约）；lazy-prompt-rustsec（红线队 prompt 全文） |
| **org 变动 + Agent Factory** | 2026-07→09-25 | OpenAI → Google Cloud Principal Engineer（一手核验；BlockBeats "Chief Engineer" 系误译不用）；GC 官方访谈 "lazy prompter" / "shifting left" |

**判语**：他本人 2026 年的言论节奏是"实验报告（02）→ 方法论体系化（03）→ 概念再定义（08-09）"三级跳，而被采纳率全场最高——Fowler/TW/Willison 线的 harness 话语都回溯到他的实验；术语归属已进入雇主官方口径（GC 09-25）。org 变动未改其主张，只放大了平台。

---

## 一、零人手写代码实验（2025→2026）

2025 年中，他对团队施加极端约束：**不写一行代码，不做一次代码审查。** 团队构建内部 beta 产品（Electron 数据分析 Agent 应用），完全由 AI Agent 产出。

| 指标 | 数据 |
|------|------|
| 团队 | 3 → 7 名工程师（+ PM 和设计师） |
| 时长 | ~5 个月 |
| 产出 | **~1,000,000 行代码（零人手写）** |
| 总 PR 数 | ~1,500+ |
| Token 消耗 | ~**10 亿 tokens/天**（~$2-3K/天） |
| 构建硬上限 | **<1 分钟** |

PR 吞吐量演进：GPT-5.2 时代 ~3.5/周 → +Symphony 5-10/天 → GPT-5.5 时代 **~70/周**——"超过线性扩展"，每个模型版本的改进被 harness 基础设施立即吸收。

## 二、方法论核心

**核心哲学**：

> *"Agents aren't hard; the Harness is hard."*
> *"It's borderline negligent not to use a billion tokens a day."*

Agent 失败时不要 tweak prompt——问："What capability, context, or structure is missing that prevents the agent from succeeding autonomously?" Agent 只有两个杠杆：**上下文 + 工具**，harness engineering = 系统性设计两者。

**五大支柱**：

1. **结构化文档作为 System of Record**：`docs/` 是唯一真相来源（agent.md ~100 行入口 / spec.md / core-beliefs.md / tech-tracker.md / quality-score.md）；**"地图，不是手册"**——渐进式披露；不在仓库里 = 对 agent 不存在。
2. **AGENTS.md = agent 的错误日志**：活的软件工程原则 + 过往错误 + 纠正文档（实验中长到 100-150 条评论）；**doc-gardening agents** 后台扫描偏差、自动开清理 PR。
3. **机械护栏**：分层架构（Types → Config → Repo → Service → Runtime → UI）由 linter 与结构测试强制；依赖只向前流；lint 错误格式化为**带修复指令的散文**；自定义 linter **由 Codex 自己生成**。
4. **Agent 优先的软件架构**：代码为 agent 理解而组织；~500 个 NPM 包深度分解（7 人团队的"万人架构"）；偏好"无聊"技术；git worktree 隔离实例。
5. **全面可观测性**：Vector→VictoriaMetrics→Grafana→分布式追踪全本地栈；Chrome DevTools Protocol 集成（DOM 快照/截屏）；per-worktree 可观测（agent 直接查 LogQL/PromQL）；**合并后审查**替代合并前审查；agent 自主插桩。

**构建执念**：<1 分钟内循环（Makefiles→Bazel→Turbo→**Nx** 达成）；agent 友好 CLI 输出（抑制通过测试，只显示失败）。

## 三、Symphony：编排、开源与幽灵库

**编排核心**（Elixir——**模型自己选的**：BEAM 进程监督是管理大量并发 agent 的理想基础设施，每个 PR 一个 GenServer 进程）：

- 将人类从同步循环中完全移除；管理完整 PR 生命周期：创作 → **agent 审查 agent** → CI → 合并冲突 → 合并；
- PR 被拒：worktree 丢弃、ticket 重来——**附带失败分析**；
- **反霸凌 prompt**：agent-reviewer 偏向合并、仅标 ≤P2 问题。

**开源状态**（2026-10-03 GitHub API 核验）：openai/symphony，2026-02-26 建、Apache-2.0、**27.5k stars**、最后 push 09-15；无 v2（0.0.3，GitLab 主线），他离开后由 OpenAI 侧维护。README："**moving from managing coding agents to managing work that needs to get done**."

**幽灵库本体论**（03-13《code-is-not-the-artifact》）：

> *"Symphony is a ghost library: **the spec is the distribution, and the source tree is one generated artifact**."*

依赖不再是代码依赖而是规范依赖——agent 可按需 vendoring 并重写中低复杂度库，实现按需再生；spec 经**蒸馏回路**从被接受的产物中沉淀（SDD 被反转：先产代码作稻草人，再蒸馏规范）。

## 四、人类保留什么

**时间分配**（原口径）：50-70% 代码产出 → ~30% 最难重构 + 0→1 构思 ＋ ~30% 客户对话/优先级 ＋ ~30% 排期/人员。

**划界的操作化**（《Software Work Is No Longer Scheduled》，03-13）——background task 三条件：**desired state 清晰 / interfaces 已知 / 结果可验证**；满足则异步交给 agent，"ask a human for a merge decision rather than implementation time"。保留给 roadmap 的判据："**decision itself is expensive**"——从零建产品、困难接口重构、接口未知区。

**深重构仍是 open problem**（Latent Space 访谈，04-07）：*"things that are hard and new is still something that the models need humans"*；*"**the deepest refactorings where you don't know what the proper shape of the interfaces are. And this is where I wanna spend my time.**"*
> *"the gnarliest refactorings are the ones that I spend my most time with… **So this is what it means to not bet against the model**."*

**Continuum 定位**：Volkov 6 月底命名 "**Zechner–Lopopolo Continuum**"："not about the people, it's about the task… **different tasks just need different proof**"；他未点名回应 Cherny/Orosz 的 9 月守门争论（立场已在 03-13 预答）。

**团队面**：周五 GC 会议（识别 slop 模式编码回 harness，"同样的反馈永远不需要给两次"）；新员工两周内 PR 吞吐 +5-15%（立即受益于 harness 上下文）；PM 经 PRD/测试/文档/harness 规则提交代码（实验中 PM 提交了 ~10 万行生产代码）。

## 五、自述五轴演变（谱系文档 "Evolution across Ryan's work"，2026-10-03 细读）

他亲笔写下的五个立场迁移——库内唯一的**自我文档化轨迹**：

1. **手动中继 → 整任务自治**：2023 ChatGPT 周末 4,000 行（"treated ChatGPT as **a highly technical junior engineer**"、"ran towards my fears"）→ 2026 RustSec / robot-vacuum 案例（agent 直连复现、实现、测试、交付、组证据）；intaglio#360：**实现评审保留、merge/release 由人授权**——"The evolution reduced manual relay while preserving implementation judgment and release authority."
2. **拟议的专家分工 → 固定 worker + 检索**：2023 提议按 crate/Ruby Core 分训专家 → 后来只养一个通用 worker、环境即时供给——"goal of situated expertise remains"，专长从训练迁移到环境策展。
3. **MCP 工具发现 → progressive disclosure → bearish**：2025《MCP Solves Tool Discovery for LLMs》（"MCP gives the models tokens"）→ 2026 自评上下文成本（整目录加载像装每本手册，`--help` 式按需暴露）→ Latent Space 访谈明确 bearish："the harness forcibly injects all those tokens… **They mess with auto compaction**"。
4. **"代码免费"获得所有权与比例约束**：2026 年初以便宜 justify 全量迁移/100% 覆盖（blog-build："**conventions rot unless they are executable. Code is free!** That means we codify repo contracts as tools and lints instead of tribal memory."；100% coverage 非谈判项；tests 只是 harness 一半，另一半是 repo legibility）→ software-work-not-scheduled 划界（见上节）；ablation framing 让每条控制自证注意力与维护成本。
5. **利用率降级为诊断**：1B tokens/人/天 = utilization target（探针）→ "token spend is unanchored in business value or ROI" → "**effectiveness is what matters**"。idle agent 的三种病因：缺 access、缺 context、人闸门——"Most of the software lifecycle is reading logs, checking traces…"（agents-agents-agents 完整论证）。

## 六、hyperbo.la 短文精选（2026 年 18 篇中的关键篇）

- **《lazy-prompt-rustsec》（03-30）**——红线队的 prompt 原文逐字："you must prove impact or exploitability"→ RUSTSEC-2026-0078 全链路：约束式验证的第一手操作样本。
- **《tell-the-model-how-to-work》（08-31）**——zero skills 主张："**I tell the model how to work, not what to do.**"
- **《agent-platform》（09-05，最长）**——agent 的再定义：agent = "a parameterized program over a set of capabilities"；agent platform = "**the system for minting agents from compositions of capabilities**"；Codex/Claude Code/Pi 都不算 agent platform。
- **《aligned-to-whom》（09-12）**——"There is no such thing as an unhackable grader… To solve this—to solve alignment—is **irreducible complexity**"；"long-term coherence through use of agentic work product is a very unsolved problem"。
- **《winding-down-artichoke-ruby》（02-15）**——Rust 功底 ↔ 用 agent 有效的直接因果（Artichoke 十年维护收尾）。

（三篇转刊自 X 的以 hyperbo.la 转刊页为一手源；全 41 篇站内清单见当日工作档。）

## 七、Agent Factory 与 Google Cloud 期（2026-07→09）

**org 核验（一手 ×2）**：hyperbo.la/contact/ 自述（last-modified 09-26）"At Google Cloud, I am **Principal Engineer, Agentic Google Cloud Platform**. I'm building agents that do the full job of operating your cloud, from design to routine operations through to incident response. Cloud operations require Harness Engineering to successfully deploy AI"；GC 官方博客（09-25）正文确认在职 + "maintaining that streak **through his transition into Google Cloud**"（自 2025-05 未开过传统编辑器）。BlockBeats 快讯 "Chief Engineer" 系 Principal 误译，不用。

**GC 官方访谈《The Agent Factory》（09-25，timestamped 分段实录；⚠️ 该页无"9 步流程"——此前传闻的 9-step 属 Orosz 09-15 写的 OpenAI 工厂，两篇勿混）**：

- **lazy prompter 的完整语境**：铺垫 "Upfront harness investment pays off by allowing engineers to become lazy prompters. When the repository contains structured documentation, clear interfaces, and discoverable tools, you do not need to paste walls of text into a prompt box every morning" → 逐字引语："I aspire to be an incredibly lazy prompter. If I have done the job to give the model the tools and context it needs to ground itself, I don't need to write a long prompt. It figures it out."
- **shifting left 两段**："try my prompt again… **from prompts, to repo docs, to linters, to tests, and all the way to upstream evals**"；收尾："increasingly capable tools which act as **a form of memory and enforcement of what you think good looks like**."
- **harness 定义**（官方口径）："the study and practice of putting a model into an environment where it can succeed"；"prompt and pray" 是反面。
- **Tilde Thurium 访谈**：capability overhang 定义段、RPG stats / 长时程 / 风险分层；**context-efficiency 技巧**：markdown 锚点放正文块正下方。
- 工具栈：Gemini 3.8 Flash / Antigravity /boost / Google Skills Repo（19k stars）；只审终态工件、tightly scoped PR 逐级放大。

## 八、谱系：技术根基与术语归属

**技术根基**（field guide `lopopolo/harness-engineering` docs/lineage/，2026-07-18 开源，trunk 分支）：

- **Artichoke 实践前身（2021）**：capability seams（Rust traits 独立于 mruby 后端）；2021-02-07 首个架构文档 commit **明确引 matklad**；02-08 **显式 Strangler Fig**。harness 方法论是他 2021 年"接缝渐进替换"实践的推广。
- **Alexis King "Parse, don't validate"**：typed boundary discipline——"manifests, CLI arguments, workflow files… parsed once into semantic values"；**"A sensor that understands the domain can report the violated relationship and the intended repair. A string comparison can usually report only that bytes differ."**（传感器质量 = 领域理解深度）
- **Zhang 的反馈回路闭合论**（他转述并采纳，03-07《Harness Engineering Is Cybernetics》）：compiler/test/linter 只能检测机械可观察偏差；capable agent 能 **inspect and repair architecture and design**——反馈回路在更深处闭合。

**术语归属的五点现状**：①他自指 02-11 OpenAI 文为 "**seminal harness-engineering essay**"；②Böckeler 02-17 memo 被定性为 "[initial memo] responded through context, deterministic constraints, LLM review, and recurring feedback"；③Zhang 与 Böckeler 并称 "**both … later interpretations of Ryan's essay**"；④Fowler 在其谱系中仅以 Strangler Fig 作采纳隐喻入谱；⑤**Böckeler memo 的 Hashimoto 猜源说在其谱系中零回应**（0 命中）。——引用 harness engineering 概念时须注明采用哪条谱系（详见 `20` 卡）。

---

## 关键结论（原实验报告的五条）

1. **代码现在是负债，不是资产**——"代码昂贵"的假设已反转，拥有更少的代码更有利。
2. **SDD 被反转**——先产代码作稻草人，从被接受的产物蒸馏规范。
3. **人类注意力是瓶颈**——不是 token 可用性，不是 agent 能力。
4. **幽灵库**——软件以规范而非源码分发。
5. **Agent 审查 Agent**——零人类合并前审查，人类只在合并后抽样。

---

## 关键引用汇总

> *"Agents aren't hard; the Harness is hard."*

> *"The study and practice of putting a model into an environment where it can succeed."* — GC 官方，2026-09-25

> *"I aspire to be an incredibly lazy prompter. … It figures it out."* — 2026-09-25

> *"Symphony is a ghost library: the spec is the distribution, and the source tree is one generated artifact."* — 2026-03-13

> *"There is no such thing as an unhackable grader… To solve this—to solve alignment—is irreducible complexity."* — 2026-09-12

> *"The deepest refactorings where you don't know what the proper shape of the interfaces are. And this is where I wanna spend my time."* — Latent Space, 2026-04-07

> *"A sensor that understands the domain can report the violated relationship and the intended repair. A string comparison can usually report only that bytes differ."* — 谱系文档引 Alexis King

---

**Source:** [OpenAI: Harness Engineering（2026-02-11）](https://openai.com/index/harness-engineering/) · [openai/symphony](https://github.com/openai/symphony) · [lopopolo/harness-engineering（field guide + lineage）](https://github.com/lopopolo/harness-engineering) · [ZenML: Zero Human-Written Code](https://www.zenml.io/llmops-database/zero-human-written-code-harness-engineering-for-autonomous-ai-agents-at-scale) · [ZenML: Extreme Harness Engineering](https://www.zenml.io/llmops-database/extreme-harness-engineering-building-production-software-with-zero-human-written-code) · [InfoQ](https://www.infoq.com/news/2026/02/openai-harness-engineering-codex/) · [Tessl Podcast #109](https://tessl.io/podcast/109/) · [hyperbo.la/contact/（org 自述）](https://hyperbo.la/contact/) · [agents-agents-agents (03-13)](https://hyperbo.la/w/agents-agents-agents/) · [software-work-not-scheduled (03-13)](https://hyperbo.la/w/software-work-not-scheduled/) · [harness-engineering-the-blog-build (02-17)](https://hyperbo.la/w/harness-engineering-the-blog-build/) · [code-is-not-the-artifact (03-13)](https://hyperbo.la/w/code-is-not-the-artifact/) · [agent-platform (09-05)](https://hyperbo.la/w/agent-platform/) · [aligned-to-whom (09-12)](https://hyperbo.la/w/aligned-to-whom/) · [lazy-prompt-rustsec (03-30)](https://hyperbo.la/w/lazy-prompt-rustsec/) · [tell-the-model-how-to-work (08-31)](https://hyperbo.la/w/tell-the-model-how-to-work/) · [Latent Space: Extreme Harness Engineering (04-07)](https://www.latent.space/p/harness-eng) · [GC 官方博客: The Agent Factory (09-25)](https://cloud.google.com/blog/topics/developers-practitioners/agent-factory-recap-agent-harnesses-shifting-left-and-autonomous-coding/)
