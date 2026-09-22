# 来源卡片（本场外部来源 · 证据权威）

> **本文件是本场外部来源的唯一登记处。** 引用一律回这里取，不在别处重复摘录（单一事实来源）。
> 纪律：一手源优先、来源可溯、标注观测日期；证据强度按 `../CONTEXT.md` 第六节四档，不发明新词。
> **观测日期**：2026-09-21（下列 URL 均于该日核验可达）。
> **本场是 2026-09-21 首次引入外部来源**——此前口径是"原则上不引数字"，见 `../CURRENT.md` 定调第 9 条。

---

## 1. Trivedy《The Anatomy of an Agent Harness》★ 核心命题的来源

| 项 | 内容 |
|---|---|
| 来源 | Vivek Trivedy（LangChain Blog） |
| 发布 | 2026-03-10 |
| URL | https://www.langchain.com/blog/the-anatomy-of-an-agent-harness |
| 观测日期 | 2026-09-21 |
| **证据强度** | **一手**（`harness engineering` 术语由该作者提出）；其中基准数字为 **⚠️ 厂商自述** |

**逐字直引**：

- "Agent = Model + Harness"
- "**If you're not the model, you're the harness.**"
- "The model contains the intelligence and the harness is the system that makes that intelligence useful."
- "Harnesses today are largely delivery mechanisms for good context engineering."
- "Today's models suffer from early stopping, issues decomposing complex problems, and incoherence as work stretches across multiple context windows."
- "we improved our coding agent Top 30 to Top 5 on Terminal Bench 2.0 by only changing the harness"（**⚠️ 厂商自述**）

**harness 组件面（原文列举）**：System Prompts / Tools, Skills, MCPs + descriptions /
Bundled Infrastructure（filesystem, sandbox, browser）/ Orchestration Logic（subagent spawning, handoffs,
model routing）/ Hooks & Middleware（compaction, continuation, lint checks）。

**推导模式（原文）**：`Behavior we want (or want to fix) → Harness Design to help the model achieve this.`

**本场怎么用**：P4 核心命题的来源；第三段五件事的工程对应——
① 上下文（context rot / compaction / progressive disclosure）；② 记忆与知识注入（AGENTS.md 式）；
③ bash / 沙箱 / 工具面；④ planning + Ralph Loop；⑤ self-verification + hooks。

**未采用**：Terminal Bench 排名细节、compaction / offloading 实现细节（本场听众不需要）。

---

## 2. MAST《Why Do Multi-Agent LLM Systems Fail?》★ 症状分类的来源

| 项 | 内容 |
|---|---|
| 来源 | Cemri, Pan, Yang 等（UC Berkeley / Intesa Sanpaolo） |
| 发布 | arXiv 2503.13657；**NeurIPS 2025 Datasets & Benchmarks Track** |
| URL | https://ar5iv.labs.arxiv.org/html/2503.13657 |
| 观测日期 | 2026-09-21 |
| **证据强度** | **一手（同行评审）** |

**方法**：7 个多 agent 框架、200+ 条执行轨迹（每条平均 15,000 行）、6 位专家标注；
标注者一致性 Cohen's Kappa **0.88**。

**14 种失败模式 / 3 大类**（括号内为出现频率）：

**FC1 规范问题（41.77%）**

| 模式 | 频率 |
|---|---:|
| 未遵守任务要求 | 10.98% |
| 未遵守角色设定 | 0.5% |
| **步骤重复** | **17.14%（全场最高频）** |
| 上下文丢失 | 3.33% |
| 未识别任务已完成 | 9.82% |

**FC2 agent 间错位（36.94%）**

| 模式 | 频率 |
|---|---:|
| 对话意外重置 | 2.33% |
| **用错误假设继续而不澄清** | **11.65%** |
| 任务脱轨 | 7.15% |
| 隐瞒关键信息 | 1.66% |
| 忽略其他 agent 的输入 | 0.17% |
| **推理与行动不一致** | **13.98%** |

**FC3 任务验证（21.30%）**

| 模式 | 频率 |
|---|---:|
| 提前终止 | 7.82% |
| 未验证 / 验证不完整 | 6.82% |
| 验证错误 | 6.66% |

**可直接引用的结构性结论**：

1. 失败**主要来自系统设计与协调，不是单个模型能力不足**——原文：
   "many MAS failures arise from the challenges in organizational design and agent coordination rather than
   the limitations of individual agents"。
2. **有验证者也不够**——"current verifiers often only perform superficial checks"（编译通过、有没有注释）。
3. **加一层高层目标验证 → ChatDev 成功率 +15.6%**（相对改进）。
4. 效率问题不在分类法内：绕路可致成本 / 延迟 **10 倍以上**。

**本场怎么用**：P2 五种症状的分类底稿（14 → 5 归位见 `../01_storyline/00-storyline-map.md` 第一段）；
P10「怎么验」的直接支撑。

> **口径警告**：MAST 的研究对象是**多 agent 系统**，而本场多数听众在**第 1–2 档**（单 agent / 固定流程）。
> 引用时**只说"失败模式"这一类结论，不引"多 agent 更容易失败"**——否则与本场四档口径打架。

---

## 3. Osmani《Agent Harness Engineering》

| 项 | 内容 |
|---|---|
| 来源 | Addy Osmani（个人博客；作者为 Anthropic MTS） |
| 发布 | 2026-04-19 |
| URL | https://addyosmani.com/blog/agent-harness-engineering/ |
| 观测日期 | 2026-09-21 |
| **证据强度** | **趋势级**（实践者综述，非一手研究） |

**逐字直引**：

- "A decent model with a great harness beats a great model with a bad harness."
- "anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent
  never makes that mistake again."
- "Every line in a good AGENTS.md should be traceable back to a specific thing that went wrong."
- "every component in a harness encodes an assumption about what the model can't do on its own."
- "success is silent, failures are verbose."
- "agents reliably skew positive when grading their own work"
- "The gap between what today's models can do and what you see them doing is largely a harness gap."

**本场怎么用**：

- **P3「这一圈不会消失，只会移动」**——直接支撑句是
  "every component in a harness encodes an assumption about what the model can't do on its own"，
  以及该文 "Harnesses don't shrink, they move" 一节的观察（模型变强 → 旧组件退休 → 新天花板要新组件）。
  **这是本场唯一的趋势判断**，用来回答听众最可能的反驳「等下一代模型不就行了」。
- P7 棘轮律（"Every line in a good AGENTS.md should be traceable back to a specific thing that went wrong."）
  = 隐性知识显性化的操作面。
- P10 验证者分离（"agents reliably skew positive when grading their own work"）。
- P3 / P4 的论证（"The gap between what today's models can do and what you see them doing is largely a
  harness gap."）。

> **转引警告**：该文引用的 HumanLayer（"it's not a model problem. It's a configuration problem."、
> AGENTS.md <60 行）与 Anthropic 长任务 harness 文，**本场未直接核验原文**，属转引；要用先回源。

---

## 4. 待回源（候选，尚未核验）

| 线索 | 出处 | 用途 |
|---|---|---|
| 《When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent Loops》 | 检索命中（Semantic Scholar），**未读全文** | P10「自己评自己总说好」的学术支撑，可替或补 Osmani 的转引 |
| Chroma《Context Rot》，2025-07 | 已在母版 `../../talk-ai-coding-evolution-harness/02_evidence/` 登记 | P6「塞得越满漏得越多」 |
| HumanLayer《Skill issue: harness engineering for coding agents》 | 经 Osmani 转引 | 棘轮律与入口文件尺寸 |

**引用前必须回源**；本场当前不依赖这四条。

---

## 5. 口径红线（本场自用）

1. **MAST 的频率数字不上屏**（本场原则上不引数字）——只作症状排序的底稿。
2. **唯一允许上屏的数字是 P4 的 Top 30 → Top 5**，且必须同屏标 **⚠️ 厂商自述**；
   **若嫌风险，整页不引数字亦可**（待定项，见 `../CURRENT.md`）。
3. **不引 MAST 的"多 agent 更容易失败"**——与本场四档口径冲突，且对**第 1–2 档**听众是误导。
4. **上屏只留作者 / 机构 + 年份**（如 "Trivedy, 2026"、"UC Berkeley 等, NeurIPS 2025"）；
   **不留产品名、工具名、公司名**。
5. **每处引用必须能回指本文件的条目号**；讲稿里的 `[Sources]` 块按条目号写。
