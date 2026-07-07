---
type: kol_deep_dive
person: Andrej Karpathy
organization: Independent (ex-OpenAI, ex-Tesla)
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://www.forbes.com/sites/jodiecook/2026/06/12/is-vibe-coding-already-dead-even-karpathy-is-moving-on/
  - https://www.glideapps.com/blog/what-is-agentic-engineering
  - https://hub.baai.ac.cn/view/52377
  - https://sdtimes.com/ai/andrej-karpathy-has-renamed-vibe-coding-heres-what-engineering-leaders-need-to-do-about-it/
  - https://www.ibm.com/think/topics/agentic-engineering
key_concepts:
  - vibe_coding
  - agentic_engineering
  - software_3_0
---
# Andrej Karpathy — 从 "Vibe Coding" 到 "Agentic Engineering"

> OpenAI 联合创始人、前 Tesla AI 负责人。Karpathy 是 AI 时代对开发者文化影响最大的单一个人——他创造的两个词定义了整个 discourse。

---

## 13 个月的完整循环：从造词到否定

| 时间 | 事件 |
|------|------|
| **2025/02** | Karpathy 创造 "**Vibe Coding**"——"全权交付给 AI，忘记代码存在" |
| **2025 全年** | 术语病毒式传播，成为 AI 编码的文化符号 |
| **2025/12** | Karpathy 自己从 80% 手动编码变成 80% AI 生成 |
| **2026/02** | Karpathy **公开否定** Vibe Coding |
| **2026/03** | 提出新术语："**Agentic Engineering**"——强调 oversight、严谨、工艺 |
| **2026/04** | Sequoia AI Ascent 大会主题演讲："提升远超 10 倍工程师" |
| **2026/05** | 加入 **Anthropic** 重建预训练研究团队 |

一个完整的炒作→高潮→幻灭→纠正周期被压缩到 **仅 13 个月**。之前的类似周期（如 "Agile"）用了 10+ 年。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。

## Agentic Engineering 的定义

Karpathy 自己下的定义：

> *"Agentic" because the new default is that you are not writing the code directly 99% of the time, you are orchestrating agents who do and acting as oversight. "Engineering" to emphasize that there is an art & science and expertise to it. It's something you can learn and become better at, with its own depth of a different kind.*

---

## Vibe Coding vs Agentic Engineering

| Vibe Coding | Agentic Engineering |
|-------------|-------------------|
| AI 生成，人类接受 | AI 生成，人类**严格审查** |
| 直接开始 prompt | 先写设计文档、spec、架构 |
| "希望能跑" | **测试是最大的差异化因素** |
| 适合原型和 demo | 适合生产系统和团队项目 |
| 轻率的所有权 | 完整所有权：文档、版本控制、CI、监控 |
| "忘记代码存在" | "不能外包你的**理解**" |

---

## Karpathy 的 Software 3.0

Karpathy 描述了三个编程范式：

| 范式 | 内容 |
|------|------|
| **Software 1.0** | 写显式指令（if-else, for loops） |
| **Software 2.0** | 用数据集训练神经网络（他 2017 年提出的概念） |
| **Software 3.0** | 通过 prompting 编程——LLM 本身成为可编程的通用计算机，上下文窗口是杠杆 |

> *"I'm programming in English."* — Karpathy 描述自己从手动编码到自然语言编程的转变。"有点羞辱感，像在指挥一个实习生——但一旦你体验到那种杠杆效应，你回不去了。"

---

## 对 SDLC 的影响

### 1. 规划 & 规格
开发者在调用任何 Agent **之前**写设计文档和 spec——定义架构、目标、约束、"完成标准"。技能从编码转移到写精确的规范。

### 2. 实现
AI Agent 自主规划、编写、测试、演化代码，在人类监督下进行。开发者 99% 的时间**不直接写代码**——他们编排专用 Agent。

### 3. 测试 & 验证
**多 Agent 系统协同**：一个负责实现，一个负责测试，一个负责安全审查。**验证循环是连续的**——Agent 运行测试，观察失败，自我纠正。

Karpathy 强调**"可验证性"**是关键因素：AI 在编码和数学领域表现出色，因为结果易于自动验证。

### 4. 审查 & 治理
人类监督被**刻意嵌入**。质量关隘、自动化测试、审计追踪在整个过程中强制执行。在受监管行业，Agent 可以在开发过程中持续执行合规规则。

### 5. 维护 & 现代化
Agentic Engineering 使遗留系统的**渐进式现代化**成为可能——Agent 重构组件、改善测试覆盖率、增量文档化系统，无需大型高风险重写。

---

## "萎缩"的自白

Karpathy 坦诚了一件很少有 KOL 愿意承认的事：

> *"My own manual coding ability is deteriorating, like losing mental arithmetic after calculator use."*

他自己的手动编码能力在退化——就像计算器使用后失去心算能力。这可能是 AI 时代最诚实的工程师自白之一。

---

## 与 Boris Cherny 的对话 (2026)

Karpathy 与 Claude Code 创作者 Boris Cherny 的高调对话增加了哲学深度：

- 两人都确认了从手动编码到 Agent 编排的**不可逆转变**
- **"Slopacalypse" 辩论**：Karpathy 担忧 AI 生成的代码污染（"slop"）；Cherny 更乐观——"在 Anthropic，AI 审查 AI 的 PR"
- Karpathy 的转变速率：**80% 手动 / 20% AI（2025/11）→ 80% AI / 20% 手动（2025/12）**——仅仅一个月

---

## 核心信息

> *"You can outsource your thinking, but you can't outsource your understanding."*

AI 可以执行思考过程、生成解决方案、编写代码——但人类对系统、架构、边界情况和故障模式的深度理解仍然是工程学科**不可替代的核心**。AI Agent 能产生的质量上限最终被指导它的人的理解深度所限制。

---

**Source:** [Forbes: Is Vibe Coding Already Dead?](https://www.forbes.com/sites/jodiecook/2026/06/12/is-vibe-coding-already-dead-even-karpathy-is-moving-on/) · [Glide: What is agentic engineering](https://www.glideapps.com/blog/what-is-agentic-engineering) · [BAAI: Karpathy × Cherny 对话](https://hub.baai.ac.cn/view/52377) · [SD Times: Karpathy renamed vibe coding](https://sdtimes.com/ai/andrej-karpathy-has-renamed-vibe-coding-heres-what-engineering-leaders-need-to-do-about-it/) · [IBM: What is Agentic Engineering](https://www.ibm.com/think/topics/agentic-engineering)
