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
  - https://podcasts.apple.com/sg/podcast/ryan-lopopolo-openais-framework-for-shipping-code-at/id1756073806?i=1000771862526
  - https://hyperbo.la/contact/
  - https://cloud.google.com/blog/topics/developers-practitioners/agent-factory-recap-agent-harnesses-shifting-left-and-autonomous-coding/
key_concepts:
  - zero_human_written_code
  - harness_engineering
  - agent_self_review_loop
  - progressive_disclosure
---
# Ryan Lopopolo — Harness Engineering 提出者（OpenAI → Google Cloud）

> 原 OpenAI Frontier Product Exploration 团队 Member of Technical Staff，**2026-07 加入 Google Cloud（Principal Engineer, Agentic Google Cloud Platform，一手核验见轨迹表）**。曾任职 Citadel → Box → Stripe → Brex → Snowflake。他领导了零人手写代码实验，创造了 "Harness Engineering" 概念，已被 Martin Fowler 和 ThoughtWorks 推广；Google Cloud 官方口径称他 "the person who coined the term agent harness"。

---

## 思想变迁轨迹（2026）

| 阶段 | 日期 | 立场标记 | 锚点 |
|------|------|---------|------|
| 实验定调 | 2026-02 | OpenAI 官方页 + InfoQ 报道：harness engineering 进入公共视野 | frontmatter source_urls |
| 极端化展示 | 2026-04-17 | AI Engineer 演讲《Humans Steer, Agents Execute》；1M LOC、0% 人写人审；Symphony 编排 "**removing humans from the code review and merge loop entirely**" | 卡内实验节 + ZenML 档案 |
| **Symphony 开源** | 2026-02-26 | openai/symphony（Apache-2.0，Elixir，**27.5k stars**，最后 push 09-15；无 v2，他离开后由 OpenAI 侧维护）：README "**moving from managing coding agents to managing work that needs to get done**"；03-13 本人一手口径："**3-5 PRs per engineer per day** on GPT-5.2 without Symphony and about **75 PRs per engineer per week** with Symphony" | GitHub API 一手 + 03-13 博文 |
| **术语被采纳（影响力弧线）** | 2026-02→05 | Fowler 站内 Böckeler 系列（02-17→05-27）+ TW 雷达背书——harness engineering 从实验报告变成学科名 | `02_martin_fowler.md` 系列表 |
| 评审立场收束 | 2026-03→09 | 人只保留 **merge decision / release authority**；04-28 ablation framing 自我约束 harness 膨胀；Volkov 6 月底命名 "**Zechner–Lopopolo Continuum**"（"not about the people, it's about the task… **different tasks just need different proof**"）；未点名回应 Cherny/Orosz 的 9 月守门话题 | 轨迹档案 + 03-13 博文《Software Work Is No Longer Scheduled》 |
| 窗口内（07→10） | 2026-07→09 | **org 变动已一手核验**：加入 Google Cloud，职衔 **Principal Engineer, Agentic Google Cloud Platform**（本人站点自述 + Google Cloud 官方博客 09-25 确认在职；BlockBeats 快讯 "Chief Engineer" 系拔高误译，不用） | [hyperbo.la/contact/](https://hyperbo.la/contact/)（last-modified 2026-09-26）|
| **窗口内最重发声** | 2026-09-25 | Google Cloud 官方博客/播客 **The Agent Factory**：harness 定义收束（"**the study and practice of putting a model into an environment where it can succeed**"）、"prompt and pray"、**只审终态工件**、tightly scoped PR 逐级放大循环；工具栈 Gemini 3.8 Flash / Antigravity /boost / Google Skills Repo（19k stars）——"he hasn't opened a traditional code editor since May of last year, maintaining that streak **through his transition into Google Cloud**" | [GC 官方博客](https://cloud.google.com/blog/topics/developers-practitioners/agent-factory-recap-agent-harnesses-shifting-left-and-autonomous-coding/)（datePublished 已核）|

**判语**：他本人 2026 年发声不多，但"被采纳率"全场最高——库内 Fowler/TW/Willison 线的 harness 话语都回溯到他的实验；且 **harness 术语归属已进入雇主官方口径**（Google Cloud 官方博客称他 "the person who coined the term agent harness"，09-25）。**谱系自述已细读**（2026-07-18 开源 field guide `lopopolo/harness-engineering`，docs/lineage/README.md 18KB，trunk 分支）：①他把自己的 02-11 OpenAI 文章称为 "**seminal harness-engineering essay**"；②Böckeler 的 02-17 memo 定性为 "responded through context, deterministic constraints, LLM review, and recurring feedback"；③George Zhang（03-07《Harness Engineering Is Cybernetics》）与 Böckeler 并称 "**both … later interpretations of Ryan's essay**"（Zhang 显式化 higher-level control loop 与校准；Böckeler 按 direction / execution type / lifecycle timing / quality 分离控制）；④Fowler 在其谱系中仅以 Strangler Fig 作采纳隐喻入谱；⑤**Böckeler memo 的 Hashimoto 猜源说在其谱系中零回应**（Hashimoto 0 命中）。org 变动未改其主张，只放大了平台。

### 自述五轴演变（同谱系文档 "Evolution across Ryan's work" 节，2026-10-03 细读）

他亲笔写下的五个立场迁移，每轴带一手锚点——库内唯一的**自我文档化轨迹**：

1. **手动中继 → 整任务自治**：2023 年 ChatGPT 周末 4,000 行（人工在编辑器与模型间复制粘贴）→ 2026 年 RustSec / robot-vacuum 案例（agent 直连复现行为、实现变更、跑测试、备交付、组证据）；intaglio#360 评审记录显示**实现评审保留、merge/release 由人授权**——"The evolution reduced manual relay while preserving implementation judgment and release authority."
2. **拟议的专家分工 → 固定 worker + 检索**：2023 提议按 crate/Ruby Core 分训专家 agent → 后来只养一个通用 worker，环境即时供给代码、历史、流程数据与工具——"goal of situated expertise remains"，专长从训练迁移到环境策展。
3. **MCP 工具发现 → progressive disclosure**：2025 年《MCP Solves Tool Discovery for LLMs》→ 2026 年自评其上下文成本（整目录加载像装每本手册），改为 `--help` 式按需暴露。
4. **"代码免费"获得所有权与比例约束**：2026 年初以便宜 justify 全量迁移/100% 覆盖 → 《Software Work Is No Longer Scheduled》划界：清晰状态+可验证结果的活给异步 agent，**zero-to-one 产品、困难接口重构、未知接口域保留持续人类判断**（Latent Space 访谈同口径：困难深重构仍是 open problem）；ablation framing（[X 原帖](https://x.com/_lopopolo/status/2049145174790725654)）让每条控制自证注意力与维护成本。
5. **利用率降级为诊断**：1B tokens/人/天 从"目标"降为 "a utilization target"（探针：agent 被允许观察与操作多少生命周期）→ 后续修正："**token spend is unanchored in business value or ROI**"＋"**effectiveness is what matters**"。

（锚点：hyperbo.la/w/* 各文、intaglio#360 评审记录、[Latent Space 访谈](https://www.latent.space/p/harness-eng)、X 帖经谱系文档转引——X 原帖登录墙未核，已标注。）

### 谱系技术根基（同文档前三节，2026-10-03 细读）

- **Artichoke 实践前身（2021）**：capability seams 架构（Rust traits 独立于 mruby 后端）——2021-02-07 首个架构文档的 commit **明确引 matklad**；2021-02-08 **显式 Strangler Fig**（逐函数禁用替换、边界保持兼容）。harness 方法论不是 2026 年凭空出现，是他 2021 年在 Artichoke 就在做的"接缝渐进替换"的推广。
- **Alexis King "Parse, don't validate"**：typed boundary discipline——"manifests, CLI arguments, workflow files… are external syntax that should be **parsed once into semantic values**"；且 **"A sensor that understands the domain can report the violated relationship and the intended repair. A string comparison can usually report only that bytes differ."**（传感器质量 = 领域理解深度，这句对 harness 治理的"传感器分级"是直接论据）
- **Zhang 的反馈回路闭合论**（他转述并采纳）：compiler/test/linter 只能检测**机械可观察偏差**；capable agent 能 **inspect and repair architecture and design**——反馈回路可以在更深处闭合，repo 上下文与控制把它校准到系统期望状态。（原文链接：Zhang X 文章 2026-03-07）

---

## 实验：零人手写代码，零人审查

2025 年中，Lopopolo 对团队施加了一条极端约束：**不写一行代码，不做一次代码审查。** 团队构建了一个内部 beta 产品（Electron 数据分析 Agent 应用），完全由 AI Agent 产出。

| 指标 | 数据 |
|------|------|
| 团队 | 3 → 7 名工程师（+ PM 和设计师） |
| 时长 | ~5 个月 |
| 产出 | **~1,000,000 行代码（零人手写）** |
| 总 PR 数 | ~1,500+ |
| Token 消耗 | ~**10 亿 tokens/天**（~$2-3K/天） |
| 构建硬上限 | **<1 分钟** |

### PR 吞吐量演进

| 时期 | PR/工程师/周 |
|------|-------------|
| GPT-5.2 时代 (2025 末) | ~3.5 |
| GPT-5.2 + Symphony | 5-10/天 |
| GPT-5.5 时代 (2026 中) | **~70** |

Lopopolo 将其描述为 **"超过线性扩展"**——每个模型版本的改进在前一个基础上叠加，harness 基础设施立即吸收所有增益。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。

## 核心哲学

> *"Agents aren't hard; the Harness is hard."*

> *"It's borderline negligent not to use a billion tokens a day."*

当 Agent 失败时，不要 tweak prompt——问：

> *"What capability, context, or structure is missing that prevents the agent from succeeding autonomously?"*

Agent 只有**两个杠杆**：上下文 + 工具。Harness Engineering = 系统性设计两者。

---

## 五大支柱（详细版）

### 1. 结构化文档作为 System of Record

`docs/` 目录是 Agent 的**唯一真相来源**。关键文件：

| 文件 | 内容 |
|------|------|
| `agent.md` | ~100 行入口——Agent 启动时首先读取 |
| `spec.md` | 产品规格 |
| `core-beliefs.md` | 不可商量的架构原则 |
| `tech-tracker.md` | 技术栈追踪 |
| `quality-score.md` | 质量指标仪表盘 |

核心原则：**"地图，不是手册"**——从小入口渐进式披露到更深层文档。如果不在仓库里，**对 Agent 而言就不存在**。Slack、Google Docs、隐性知识 = 不可见。

### 2. AGENTS.md — Agent 的错误日志

- 活的软件工程原则 + 过往错误 + 纠正文档
- 实验中增长到 **100-150 条评论**
- 作为自动化**反 slop 系统**的种子数据
- **"Doc-gardening agents"** 在后台持续扫描代码库，识别与 AGENTS.md 的偏差，自动开启可合并的清理 PR

### 3. 机械护栏

严格分层架构由 linter 和结构测试强制执行：

```
Types → Config → Repo → Service → Runtime → UI
```

- 依赖**只能向前**流动；违规则 CI 失败
- Lint 错误格式化为**带嵌入式修复指令的散文**——Agent 可自主阅读并纠正
- 自定义 linter **由 Codex 自己生成**

### 4. Agent 优先的软件架构

- 代码为 **Agent 理解**而组织，不是为人类可读性
- ~500 个 NPM 包，深度分解——Lopopolo 称之为 **"万人架构"**（7 人团队）
- 偏好**"无聊"技术**（稳定 API，丰富训练数据覆盖）
- 一切结构化使 Agent 可通过 git worktree 启动隔离实例

### 5. 全面可观测性

从第一天起的全本地栈：

```
Vector (日志聚合) → VictoriaMetrics (指标) → Grafana (仪表盘) → 分布式追踪
```

**额外能力**：
- **Chrome DevTools Protocol** 集成——Agent 可拍 DOM 快照、截屏、导航页面
- **Per-worktree 可观测性**——Agent 直接查询 LogQL/PromQL
- 这使 prompt 如 *"确保服务启动 <800ms"* 可被自动验证
- **合并后审查**替代合并前审查——人类使用可观测性数据抽样已合并代码
- Agent 自主插桩——日志、指标、追踪 span 全部由 AI 生成

---

## Symphony：多 Agent 编排系统

Symphony 是整个实验的核心基础设施。用 **Elixir** 构建——**模型自己选的**，而非团队决定。

### 为什么是 Elixir？

模型论证：BEAM 虚拟机的 **进程监督能力**（GenServer + supervision tree）是管理大量并发编码 Agent 的理想基础设施。每个 PR 是一个独立 GenServer 进程，如果崩溃则被监督树自动重启。

### 核心机制

- **将人类从同步循环中完全移除**
- 管理完整 PR 生命周期：代码创作 → **Agent 审查 Agent** → CI → 合并冲突 → 合并
- 如果 PR 被拒绝：worktree 丢弃，ticket 重新开始——但**附带失败分析**
- **反霸凌 prompt**：Agent-reviewer 被告知偏向合并、仅标记 ≤P2 优先级问题

### "幽灵库（Ghost Library）"

Symphony 引入的最激进概念之一：

> 软件以**高保真规范**而非源代码的形式分发。依赖被"内化"——Agent 一个下午就能 vendoring 并重写中低复杂度库。实现按需再生。

---

## 构建系统演化

Lopopolo 对构建速度有硬性执念——**<1 分钟**的内循环上限。

| 阶段 | 工具 | 结果 |
|------|------|------|
| 1 | Makefiles | 太慢 |
| 2 | Bazel | 迁移成本高 |
| 3 | Turbo | 接近但不够 |
| 4 | **Nx** | **<1 分钟达成** |

Agent 友好的 CLI 输出：抑制通过的测试，只显示失败。

---

## Codex 模型演化

两条模型线：**Codex**（有主见的、harness 优化的）vs **主链 GPT-5**（通用的、可操控的）。

| 模型 | 关键能力 | 时间 |
|------|---------|------|
| **Codex Mini** | 慢，需深度分解；初始约人类 1/10 速度 | 2025 早期 |
| **GPT-5.2** | 编码 Agent 的"奇点时代"；~3.5 PR/周 | 2025/08 |
| **GPT-5.3** | 后台/并行工具调用；Agent 对阻塞操作不耐受 → 强制 <1min 构建 | — |
| **GPT-5.4** | 统一编码 + 通用推理 + Computer Use + 视觉；100 万 token 上下文 | — |
| **GPT-5.5** | 嵌入式浏览器 Computer Use；~70 PR/周 | 2026 |
| **Codex Max** | 设计用于 24hr+ 自主运行；内建上下文管理/压缩；可生成子 Agent | 2026 |

---

## 人类的新角色

Lopopolo 的时间分配变化：

| 之前 | 之后 |
|------|------|
| 50-70% 代码产出 | ~30% 最难的重构 + 0→1 构思 |
| — | ~30% 与客户对话 + 优先级 |
| — | ~30% 排期 + 人员安排 |

**周五 "GC 会议"**：每周同步站立会。团队识别反复出现的 slop 模式，编码回 harness——同样的反馈**永远不需要给两次**。

**新员工入职即高效**：每增加一个团队成员，两周内 PR 吞吐量提升 5-15%——因为他们立即受益于 harness 中积累的上下文。

**PM 和设计师也提交代码**：通过 PRD、测试、文档和 harness 规则——无需打开 IDE。PM 在实验中提交了 ~10 万行生产代码。

---

## 关键结论

### 1. 代码现在是负债，不是资产

每个工程组织都建立在"代码昂贵"的假设上。这个假设已经反转。当 Agent 可以按需生成代码，**拥有更少的代码比拥有更多的代码更有利**。

### 2. Spec-Driven Development 被反转

传统 SDD：先写 spec → AI 实现 → 人类验证。
Lopopolo 的反转：**先产出代码作为稻草人 → 完善它 → 从被接受的产物中蒸馏出规范。**

### 3. 人类注意力是瓶颈

不是 token 可用性。不是 Agent 能力。是**人类能审查和判断多少东西**。

### 4. "幽灵库"

软件以规范而非源码分发。Agent 按需再生实现。依赖不再是代码依赖，而是规范依赖。

### 5. Agent 审查 Agent

整个实验中**零人类合并前代码审查**。Agent 审查 Agent，人类只在合并后抽样。反霸凌 prompt 确保审查不吹毛求疵。

---

**Source:** [OpenAI: Harness Engineering — Leveraging Codex in an Agent-First World](https://openai.com/index/harness-engineering/) (2026/02/11) · [ZenML: Zero Human-Written Code](https://www.zenml.io/llmops-database/zero-human-written-code-harness-engineering-for-autonomous-ai-agents-at-scale) · [ZenML: Extreme Harness Engineering](https://www.zenml.io/llmops-database/extreme-harness-engineering-building-production-software-with-zero-human-written-code) · [InfoQ: OpenAI Harness Engineering](https://www.infoq.com/news/2026/02/openai-harness-engineering-codex/) · [Tessl Podcast #109: full transcript](https://tessl.io/podcast/109/) · [AI Native Dev Podcast](https://podcasts.apple.com/sg/podcast/ryan-lopopolo-openais-framework-for-shipping-code-at/id1756073806?i=1000771862526)
