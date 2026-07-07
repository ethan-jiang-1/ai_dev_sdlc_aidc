---
type: kol_deep_dive
person: ThoughtWorks
organization: ThoughtWorks
content_type: technology_radar_analysis
verification_status: verified
source_urls:
  - https://www.thoughtworks.com/en-cn/about-us/news/2026/combat-ai-cognitive-debt-radar-v34
  - https://www.thoughtworks.com/en-in/about-us/news/2025/thoughtworks-tech-radar-33-rapid-ai
  - https://www.thoughtworks.com/en-cn/about-us/news/2026/ai-works-heralds-new-era-of-agile-and-next-generation-software-development
  - https://www.tipranks.com/news/private-companies/thoughtworks-flags-ai-driven-cognitive-debt-in-new-technology-radar-urges-disciplined-engineering-at-scale
key_concepts:
  - cognitive_debt
  - harness_engineering
  - spec_driven_development
  - ai_governance
---

# ThoughtWorks — 从技术雷达看 AI-SDLC 演化

> ThoughtWorks 是过去 20 年对 SDLC 实践影响最深远的咨询公司之一。它的 Technology Radar 被全球 CTO 视为技术选型的风向标。
> 2025-2026 连续两期雷达以 AI 辅助开发为核心主题。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。

## Volume 33 (Fall 2025) — "Agent 的崛起"

### 四大主题

**1. Rise of agents elevated by MCP**
MCP (Model Context Protocol) 成为 Agent 生态系统的标准集成协议。每个主要供应商都在自己的工具中构建 agent-awareness，为 agent-assisted 工作流创建基础设施。

**2. AI coding workflows**
AI 战略性嵌入整个 SDLC 价值链——从理解遗留代码库到正向工程。团队专注于"上下文工程"（如 `AGENTS.md` 文件、spec-driven development）来有效管理编码 Agent。

**3. Infrastructure orchestration for AI**
GPU 感知编排成为平台团队的核心竞争力。工具如 Kueue、Kubeflow、Volcano 用于管理大规模 GPU 集群。

**4. Emerging AI antipatterns**
早期警示：AI 加速的影子 IT、对 AI 代码的盲目信任、"vibe coding"（无严谨性的 prompt 驱动开发）——这个术语迅速被行业放弃。

---

## Volume 34 (April 2026) — "拐点"

**118 个 blip，超过一半直接与 AI/Agent 相关。** CTO Rachel Laycock：

> *"我们正处于的拐点不是技术拐点——而是技术的运用方式的拐点。"*

### 主题一：保留原则，放弃旧模式

经典实践**不是**过时——它们是 AI 速度的制衡力量：

| 经典实践 | AI 时代为什么更重要 |
|---------|-------------------|
| 结对编程 | 两个人比一个人更容易发现 AI 的逻辑漏洞 |
| 零信任架构 | Agent 寻求最大权限时，最小权限是唯一防线 |
| 变异测试 | 检测 AI 生成的"永远绿灯"测试最诚实的信号 |
| DORA 指标 | "代码行数"作为生产力指标在 AI 时代是危险的误导 |
| 整洁代码 | AI 可以生成更多代码——它不会更整洁，除非你要求 |

### 主题二：保护"权限饥渴"的 Agent

引用了 Simon Willison 的"致命三角"框架：
- 私有数据访问 + 不可信内容 + 外部操作 = **高风险**
- 零信任、最小权限、沙箱执行是"**不可商量的底线**"

### 主题三：给编码 Agent 上缰绳 —— Harness Engineering

这是 ThoughtWorks 在 2026 年推广的最重要概念。完整的对比：

| 12 个月前 | 今天 |
|----------|------|
| Rules files (CLAUDE.md) | Skills, subagents, plugins, specs |
| Prompt Engineering | **Context Engineering**（信息环境设计） |
| Human-in-the-loop by default | 无监督/云 Agent（Codex, Claude Code headless） |
| Ad-hoc AI 使用 | **Harness Engineering**——确定性护栏包裹非确定性模型 |
| "Vibe coding" | 结构化 spec-driven development |

**前馈控制（Feedforward）**：原则、编码约定、how-to 文档、参考实现、结构化 spec——在 Agent 生成代码**之前**喂给它

**反馈控制（Feedback）**：静态分析、结构测试（ArchUnit, dependency-cruiser）、变异测试、linter、浏览器检查——在人类审查**之前**应用到 Agent 输出

**混合方法**：CPU 确定性工具（codemods, OpenRewrite recipes, language server refactorings）补充 GPU 概率推断

### 主题四：Agent 时代的工具评估危机

**语义扩散（Semantic Diffusion）**——"spec-driven development"、"harness engineering"等新术语出现得比含义稳定快。**"太年轻无法 blip"** 成为真实的评估标准。

---

## Adopt / Trial / Caution 分类

### Adopt（生产级）

| Blip | 说明 |
|------|------|
| Claude Code | "能力与可用性的基准" |
| Cursor | 最广泛采用的 IDE 编码 Agent |
| Context Engineering | Prompt Engineering 的进化——系统性设计 AI 的信息环境 |
| Curated Shared Instructions | CLAUDE.md、AGENTS.md 作为团队工程资产 |
| Structured Output from LLMs | LLM 消费应用的默认实践 |
| Zero Trust Architecture | Agent 时代的安全基础 |
| DORA Metrics | 比任何时候都关键——拒绝把"代码行数"当生产力标准 |

### Trial（值得探索）

| Blip | 说明 |
|------|------|
| Agent Skills | 模块化、懒加载的编码 Agent 指令 |
| Feedback Sensors for Coding Agents | 确定性质量关隘（编译器、linter、测试）接入 Agent 工作流 |
| Mutation Testing | 检测"永远绿灯"的 AI 生成测试的最诚实信号 |
| Sandboxed Execution | Dev Containers 进化为 Agent 执行边界 |
| Progressive Context Disclosure | 按需加载指令，避免上下文膨胀 |
| Claude Code Plugin Marketplace | 基于 Git 的共享命令、prompts 和 skills 分发 |

### Caution（暂停/重新评估）

| Blip | 风险 |
|------|------|
| **Agent Instruction Bloat** | AGENTS.md 文件失控膨胀，指令相互冲突或被忽略 |
| **Codebase Cognitive Debt** | 代码加速产出但理解不跟上 |
| **Coding Agent Swarms** | 数十/数百个 Agent——昂贵、实验性、未经验证 |
| **Coding Throughput as Productivity** | 用代码行数或 PR 数量衡量生产力是危险误导 |
| **Ignoring Durability in Agent Workflows** | 开发环境成功 ≠ 生产可靠性 |
| **MCP by Default** | 不加选择地采用 MCP；CLI 等更简单的替代方案经常足够了 |
| **AI-Accelerated Shadow IT** | 非工程师用 AI 构建系统，绕过治理 |

---

## 五个核心警告

1. **认知债无声累积**——代码能"工作"但没人理解，这种负债以月计而非以冲刺计
2. **固定成本模型结束**——重度 Agent 使用的 token 消耗可能远超固定预算预期
3. **审查疲劳**——多会话 AI 代码审查导致 developer burnout
4. **资历悖论**——只有非常资深的工程师才能有效驾驭高自主性 AI；初级工程师缺乏安全监督 Agent 所需的判断力

---

## AI/works™ — ThoughtWorks 自己的回答 (Jan 2026)

ThoughtWorks 不仅分析趋势——他们直接入场。AI/works™ 是一个 agentic 开发平台：

- 统一遗留系统理解、需求增强、自动 spec 生成和 agentic 代码生成/测试
- 目标企业混合环境（不仅是绿地项目）
- 声称将现代化周期从**年压缩到月**
- **3-3-3 交付模型**：从想法到生产 90 天

---

## 关键引用

> *"Speed without discipline only compounds cost. The maturity of a coding agent lies not in making it more autonomous, but in building better feedforward + feedback control systems around it."*
> — ThoughtWorks Technology Radar Vol. 34

> *"我们正处于的拐点不是技术拐点——而是技术的运用方式的拐点。"*
> — Rachel Laycock, CTO

---

**Source:** [ThoughtWorks Technology Radar Vol.34](https://www.thoughtworks.com/en-cn/about-us/news/2026/combat-ai-cognitive-debt-radar-v34) · [Vol.33](https://www.thoughtworks.com/en-in/about-us/news/2025/thoughtworks-tech-radar-33-rapid-ai) · [AI/works™](https://www.thoughtworks.com/en-cn/about-us/news/2026/ai-works-heralds-new-era-of-agile-and-next-generation-software-development) · [TipRanks coverage](https://www.tipranks.com/news/private-companies/thoughtworks-flags-ai-driven-cognitive-debt-in-new-technology-radar-urges-disciplined-engineering-at-scale)
