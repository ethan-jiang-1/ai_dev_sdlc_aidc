# Dimension 6: Historically Influential Voices & KOLs on AI-SDLC

> 历史上塑造了 SDLC、Agile、DevOps 的公司和人物，在 AI 时代的立场和观点
> Research date: 2026-07-05

---

## Overview

当 AI 开始重塑软件开发生命周期时，一个关键问题是：**那些曾经定义了"好的软件开发方式"的人和公司，现在在说什么？**

本维度覆盖三类声音：

1. **历史上影响 SDLC 的公司**——ThoughtWorks、敏捷社区
2. **Agile Manifesto 时代的核心人物**——Martin Fowler、Kent Beck、Dave Farley、Jim Highsmith
3. **AI Coding / Agentic Engineering 时代的 KOL**——Simon Willison、Birgitta Böckeler

---

## 1. ThoughtWorks — 从技术雷达看 AI-SDLC 演化

ThoughtWorks 在 2025-2026 连续两期技术雷达中将 AI 辅助开发置于核心位置。

### Volume 33 (Fall 2025) — 四大 AI 主题

| 主题 | 内容 |
|------|------|
| **Rise of agents elevated by MCP** | MCP 成为 Agent 生态系统的标准集成协议 |
| **AI coding workflows** | AI 嵌入全 SDLC 价值链——从理解遗留代码到正向工程 |
| **Infrastructure orchestration for AI** | GPU 感知编排成为平台团队核心竞争力 |
| **Emerging AI antipatterns** | AI 加速的影子 IT、对 AI 代码的盲目信任、"vibe coding" |

### Volume 34 (April 2026) — 拐点

118 个 blip，**超过一半直接与 AI/Agent 相关**。四个核心主题：

| 主题 | 关键概念 |
|------|---------|
| **保留原则，放弃旧模式** | 经典实践不是过时了——而是 AI 速度的制衡力量。结对编程、零信任架构、变异测试、DORA 指标、整洁代码、可测试性重新变得关键 |
| **保护权限饥渴的 Agent** | Simon Willison 的"致命三角"：私有数据 + 不可信内容 + 外部操作 = 高风险。零信任、最小权限、沙箱执行是"不可商量的底线" |
| **给编码 Agent 上缰绳 (Harness Engineering)** | 前馈控制（Spec-Kit, OpenSpec）+ 反馈控制（编译器、linter、类型检查器、变异测试）。**CPU 确定性工具补充 GPU 概率推断** |
| **Agent 时代的工具评估危机** | "语义扩散"——新术语（"spec-driven development"、"harness engineering"）出现得比含义稳定快。"太年轻无法 blip"成为真实的评估标准 |

### ThoughtWorks 的核心警告

1. **认知债 (Cognitive Debt)**——AI 生成的代码越多，人类理解与系统之间的鸿沟越大
2. **真实成本**——重度 Agent 使用可达 **$380/天/开发者**（约 $91K/年）
3. **审查疲劳**——开发者在多会话 AI 代码审查中 burnout
4. **速度悖论**——Amazon 内部分析发现 AI 代码事故导致**增加更多审查门控**，而非减少
5. **资历悖论**——只有资深工程师能有效驾驭高自主性的 AI；初级工程师缺乏判断力

### AI/works™ (Jan 2026)

ThoughtWorks 推出 AI/works™ agentic 开发平台，采用 **3-3-3 交付模型**：从想法到生产 90 天。

> *"我们正处于的拐点不是技术拐点——而是技术的运用方式的拐点。"* —— Rachel Laycock, CTO

---

## 2. Martin Fowler — "验证的意义变了"

Martin Fowler 在 2026 年的 *Fragments* 中区分了两种 AI 开发模式：

| Vibe Coding | Agentic Engineering |
|-------------|-------------------|
| 不看代码，全权交付 | 专业使用 AI Agent 放大已有技能 |
| Prompt → 盲目接受 | Prompt → 验证 → 在工程系统中迭代 |
| 适合原型和一次性工具 | 适合生产系统和长期维护的代码库 |

### 最关键的洞察："验证"的语义变了

> *"Verified 曾经意味着 'read by you'。在现代 Agent 吞吐量下，它必须意味着 'checked by tests, by type checkers, by automated gates, or by you where your judgment matters.' 检查仍然发生；只是不总是在你的脑子里。"*

竞争的本质从"能写多快"变成了 **"能多快判断它是否正确"**：

> *"The game is not 'how fast can we build' anymore. It is 'how fast can we tell whether this is right.'"*

### Harness Engineering —— Fowler 亲自推广

Fowler 在自己的网站上发布了 Birgitta Böckeler 的 Harness Engineering 文章（他说这篇文章吸引了"疯狂的流量"）。核心概念：

- **Harness** = 把非确定性的 LLM 嵌入确定性工程工作流的控制面
- 管理：目标、状态、边界、权限、工具、验证、回滚
- 六层生产 Harness：任务/状态 → 知识/上下文 → 工具/权限 → 执行/编排 → 验证/质量 → 组织/角色设计
- 计算传感器（静态分析、类型检查器、测试）比人类审查对 AI 代码更可靠

---

## 3. Dave Farley — "CI/CD 让 AI 时代可以存活"

Continuous Delivery 作者 Dave Farley 是 AI 时代最有力也最慎重的批判声音之一。

### AI 的规模判断

> *"毫无疑问，我们现在看到的变化大于所有这些的总和——大于互联网，大于面向对象，大于敏捷转型。"*

但他同时批判极端论调：恐吓者说 AI 不能编程是错的，说 10x-100x 提升的人也是错的。他参与的研究显示约 55% 的生产力提升——"不是没有，只是没有 10 倍"。

### AI 编码的三个结构性问题

1. **英语不是好的编程语言**——自然语言太模糊、太开放解释
2. **AI 不具确定性**——同样的 prompt，不同的输出。这根本改变了工具的可靠性特征
3. **验证成为瓶颈**——代码生成便宜了；理解和验证行为才是困难的部分

### DORA 的警钟

Farley 强调了 DORA 报告中一个令人担忧的数据：**70% 的 AI 工具使用者不置疑输出**。他将其类比为"开发者能否测试自己的代码"的经典辩论——不能，除非有意识地切换视角。开发者必须从 "prompter 模式"切换到 "verifier 模式"，大多数人没有做这个切换。

### 12,000 行问题

当 Steve Yegge 告诉他一天产出 12,000 行代码时，Farley 的回应毫不留情：

> *"我没法仔细读 12,000 行代码并感到我真正理解并拥有它们。"*

这意味着信任必须来自**可执行规范和持续验证**，而不是逐行人工审查。

### 最终的乐观判断

> *"AI 可能是行业有史以来最好的机会，让人们最终内嵌 XP 实践——不是因为意识形态采用它们，而是因为在用 AI 的同时不这样做**可见地、可衡量地危险**。"*

---

## 4. Simon Willison — "整个 SDLC 都被设计错了"

Django 联合创始人 Simon Willison 是 AI 编码时代被引用最多的 KOL 之一。

### 2025 年 11 月的拐点

GPT-5.1 和 Claude Opus 4.5 发布后，Willison 说 AI 编码跨过了关键门槛：

> *"几乎每次都做到你说的——这带来了所有的不同。"*

他现在估计 **~95% 的代码是 AI 生成的**。

### SDLC 瓶颈的迁移

Willison 最具影响力的观察：

> *"如果你能从一天产 200 行代码变成 2,000 行，还有什么会崩？整个 SDLC 是围绕'一天产几百行代码'设计的。现在不是了。"*

**上游影响**（引用 Anthropic 设计负责人 Jenny Wen）：
- 设计流程存在是因为"建了 3 个月后才发现建错了"是灾难性的
- 如果构建只需几小时而非几个月，风险计算就变了
- **迭代便宜时，prototype-validate 优于 spec-and-pray**

**下游影响**：
- 代码审查管线无法吸收 10 倍吞吐量
- 传统质量信号（commits、tests、README）已无意义——AI 30 分钟就能全搞出来
- 新的质量指标：*"这个东西有没有人真正每天用了两周？"*

**DORA 2025 数据确认**：高 AI 采用率组织中——PR 体积 +154%、审查时间 +91%、bug 率 +9%。

### 认知成本和倦怠

> *"我可以并行启动 4 个 Agent 处理 4 个不同问题。然后到上午 11 点，我已经被榨干了。"*

他描述了上瘾般的行为——开发者熬夜"启动更多 Agent"，凌晨 4 点醒来检查结果。"学会新的个人极限"成了新的专业技能。

### 黑暗工厂 (Dark Factory) 与"没人读代码"

他讨论了 StrongDM 的"黑暗工厂"实验：
- 规则 1：没人**写**代码（已经可行——他自己 ~95% AI 生成）
- 规则 2：没人**读**代码（StrongDM 的新实践）

他类比：就像你不会在使用另一个团队的内部服务之前读它的每一行代码——他现在把 Agent 输出当做**半黑盒**，信任它直到它坏掉。

---

## 5. Kent Beck — "我们保持怀疑，我们保持人性"

### XP 的复苏

Kent Beck 指出 **Extreme Programming 实践正在 AI 时代复苏**——特别是 TDD、模块化和快速反馈循环——因为它们创造了 AI Agent 最高效运行所需的那种结构化、可测试的代码。

### 对未来软件开发峰会的联合声明

在 Agile Manifesto 25 周年之际（Deer Valley, Utah），Beck、Laura Tacho、Steve Yegge 联合声明：

> *"组织被人和系统层面的问题所制约。我们仍然对任何承诺在不先解决人和系统层面约束的情况下改善组织绩效的技术保持怀疑。我们保持怀疑，我们保持人性。"*

### TDD 是 AI 时代的理想实践

Beck 的观点被多家媒体报道：TDD 在 AI 编码中找到了最强的理由——它提供了可验证的、可执行的规范，AI Agent 可以据此工作。不确定性存在于模型层，确定性存在于测试层。

---

## 6. Agile Manifesto 社区 — "敏捷过时了吗？"

### Jim Highsmith（Agile Manifesto 合著者）

Highsmith 公开表示对 vibe coding "着迷"——不是因为他认为正确的开发方式就是这样，而是因为这代表了软件开发民主化的新可能。

### The Register 报道：TDD 是 AI 的理想选择

Agile 工作坊得出关键结论：TDD 之所以适合 AI 时代，是因为它提供了 Agent 可以据以工作的**可验证、可执行的边界条件**。

### Does AI Make the Agile Manifesto Obsolete?（InfoQ 辩论）

InfoQ 2026 年 2 月的专题讨论反映了社区的分裂：
- 否认派：AI 不改变敏捷核心——小增量、紧密用户联系、快速反馈如果有什么变化的话是更重要了
- 重构派：AI 要求重写敏捷——"个体与互动高于流程与工具"中的"个体"现在包含 AI Agent？

Fowler 的立场是前者：**敏捷的核心原则与 AI 有强烈的协同效应**。"你能加速反馈循环越多，后果就越大。"

---

## 7. 其他重要声音

### Birgitta Böckeler (ThoughtWorks)

AI 辅助软件交付全球负责人，QCon NYC 2026 发言。她绘制了 12 个月的关键演化：

| 12 个月前 | 今天 |
|----------|------|
| Rules files (CLAUDE.md) | Skills, subagents, plugins, specs |
| Prompt Engineering | Context Engineering |
| Human-in-the-loop by default | 无监督/云 Agent |
| Ad-hoc AI 使用 | Harness Engineering |
| "Vibe coding" | 结构化 spec-driven development |

### Gergely Orosz (Pragmatic Engineer)

Orosz 在 Substack 上发表了 *"The Future of Software Engineering with AI: Six Predictions"*，强调 AI 不会消除工程师角色但会重新定义它——中层级工程师是最脆弱的群体。

### Steve Yegge

在同一个峰会与 Beck 共同声明。Yegge 以直言不讳著称——他公开承认一天产出 12,000 行 AI 代码，引发 Farley 等人的批评。他是"AI 最大化主义者"的代表声音。

---

## 总结：历史声音的共识与分歧

| 观点 | 支持者 |
|------|--------|
| **经典实践（TDD、CI/CD、模块化）比任何时候都重要** | Farley, Beck, Fowler, ThoughtWorks |
| **SDLC 必须为 AI 吞吐量重新设计** | Willison, Böckeler, Orosz |
| **"Vibe Coding" 对生产系统不负责任** | Fowler, Farley, Böckeler (ThoughtWorks 将其标记为反模式) |
| **"Vibe Coding" 是软件民主化的有趣实验** | Highsmith (谨慎兴趣) |
| **AI 应该被信任为半黑盒，直到它出问题** | Willison (实践上), StrongDM 黑暗工厂 |
| **AI 绝不是黑盒——必须用确定性传感器验证** | Farley, Böckeler, Fowler |
| **AI 是中层级工程师的就业风险** | Willison, Orosz |
| **AI 是内嵌正确工程实践的最佳机会** | Farley, Beck |

### 最值得咀嚼的一句话

来自 Martin Fowler：

> *"The game is not 'how fast can we build' anymore. It is 'how fast can we tell whether this is right.'"*

来自 Dave Farley：

> *"AI won't replace software engineers, but it will expose the ones who never learned to think like engineers."*

来自 Simon Willison：

> *"If you can go from producing 200 lines of code a day to 2,000 lines of code a day, what else breaks?"*

---

**Sources:**
- [ThoughtWorks Technology Radar Vol.34](https://www.thoughtworks.com/en-cn/about-us/news/2026/combat-ai-cognitive-debt-radar-v34)
- [Martin Fowler Fragments](https://martinfowler.com/fragments/2026-04-29.html)
- [ThoughtWorks: AI-first software engineering](https://www.thoughtworks.com/zh-cn/perspectives/edition36-ai-first-software-engineering/article)
- [The Register: Agile Manifesto co-author smitten with vibe coding](https://www.theregister.com/software/2026/02/19/agile-manifesto-co-author-smitten-with-vibe-coding/)
- [InfoQ: Does AI Make the Agile Manifesto Obsolete?](https://www.infoq.com/news/2026/02/ai-agile-manifesto-debate/)
- [Simon Willison: Vibe coding and agentic engineering](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/)
- [Heavybit Podcast: Simon Willison](https://heavybit.com)
- [Lenny's Podcast: Simon Willison (Apr 2026)](https://www.lennyspodcast.com)
- [Dave Farley: Engineering Discipline in the AI Era](https://www.aviator.co/podcast/engineering-discipline-dave-farley)
- [GOTO 2025: Dave Farley keynote](https://devblogs.co/posts/the-most-important-programming-invention-in-20-years-dave-farley-goto-2025)

---

*本文件为 AIDLC 研究第六维度，与前五个维度（推进者、发展脉络、社区反应、当前推手、核心驱动力）互补，聚焦历史上塑造 SDLC 的声音在 AI 时代的立场。*
