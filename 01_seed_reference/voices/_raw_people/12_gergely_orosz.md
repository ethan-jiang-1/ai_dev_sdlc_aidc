---
type: kol_deep_dive
person: Gergely Orosz
organization: The Pragmatic Engineer
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://newsletter.pragmaticengineer.com/p/the-future-of-software-engineering-with-ai
  - https://securityboulevard.com/2026/03/top-6-takeaways-on-the-future-of-coding-from-sonar-summit-2026-7/
  - https://sourcelabs.nl/blog/pragmatic-engineer-survey-how-ai-tools-reshape-engineering-roles/
  - https://daringfireball.net/linked/2026/07/02/orosz-meta-engineering-culture
  - https://newsletter.pragmaticengineer.com/p/what-is-happening-with-code-reviews
  - https://newsletter.pragmaticengineer.com/p/openai-software-factory
  - https://newsletter.pragmaticengineer.com/p/the-pulse-end-of-coding-by-hand
key_concepts:
  - six_predictions_good_bad_ugly
  - something_precious_being_taken_away
  - engineering_culture_risk
---
# Gergely Orosz — "代码量爆炸，工程基本功反而更重要了"

> *The Pragmatic Engineer* 作者，Pragmatic Summit 主办者。2026 年 1 月发表万字长文 *"What Happens to Software Engineering When AI Writes Almost All the Code"*（个人长文＋访谈 Kent Beck、Martin Fowler、Simon Willison；**读者调查另行发布于 04-14 / 05-19 两部**——2026-10-03 回源校正，长文与调查非一体）。

---

## 思想变迁轨迹（2026）

| 阶段 | 日期 | 立场标记 | 锚点 |
|------|------|---------|------|
| 长文定调 | 2026-01-06 | 个人长文（⚠️ 非调查，校正见上）："**software engineering fundamentals should become more important**" + "Something precious is being taken away" | 卡内 + frontmatter |
| 峰会主办 | 2026-02 | Pragmatic Summit（Beck+Fowler 同台） | `../_raw_promatic_summit_2026/` |
| 上半年节拍 | 2026-01→07 | 01-22 Pulse#160："writing code by hand is almost dead… **mere months**"；02-17 How Codex is built；02-24 六预测成文；03-17 "Are AI agents actually slowing us down?"；**04-08 DHH 访谈（亲录其 agent-first 起点）**；06-23 Slow down to speed up；06-30 三实验室走访；07-14 loop engineering；07-28 Inside Anthropic；**读者调查两部 04-14 / 05-19**（Part 2："the benefits of AI heavily depend on **the engineering culture that was in place before**"） | PE 各期（2026-10-03 深挖档，40 页存证） |
| 文化批判 | 2026-06-17 | 《Why is Meta destroying its engineering organization?》："**people stop caring about real work and focus on performative work**"＋"writing code by hand…could cost you your job"（DF 07-02 转链；2026-10-03 校正：原文 6-17） | frontmatter + 深挖档 |
| **一线取证 + 制度议程** | 2026-09 | 三连：code reviews 是适应还是消亡（09-08）/ 潜入 OpenAI 软件工厂（09-15）/ 手写代码终结议程化（09-24） | 本卡"2026-09 增量"节 |
| **一线取证 + 制度议程** | 2026-09 | 三连：code reviews 是适应还是消亡（09-08）/ 潜入 OpenAI 软件工厂（09-15）/ 手写代码终结议程化（09-24） | 本卡"2026-09 增量"节 |

**判语**：从综合访谈的观察者变成一线取证者——1 月的"基本功"判断仍在，但 9 月的主叙事换成了"制度来不及适应"。

---

## 2025 年末的拐点

Orosz 精确标定了 AI 编码跨过关键门槛的时间窗口：

| 模型 | 厂商 | 日期 |
|------|------|------|
| Gemini 3 | Google | 2025/11/17 |
| Opus 4.5 | Anthropic | 2025/11/24 |
| GPT-5.2 | OpenAI | 2025/12/11 |

Orosz 自己的"a-ha moment"：**旅行中用手机部署生产代码**——通过 Claude Code for Web 连接 GitHub，prompt → 审查 PR → 合并，全程手机完成。

到 2025 年 12 月，Orosz 自己停止了手写代码——他发现 prompting + 审查**更快**，至少对他的 TypeScript/Node/React/Postgres 栈是如此。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。

## 六大预测：好、坏、丑

### 🔴 坏——正在贬值的技能

| 技能 | 为什么 |
|------|--------|
| **原型开发** | PM、设计师、业务人员现在可以自己用 Lovable/Replit 构建原型 |
| **多语言编程** | AI 可以跨语言翻译——"任何工程师都能跳进任何代码库" |
| **语言/栈专精** | 创业公司将停止分别招聘前端和后端——雇一个受信任的专家用 AI 覆盖全栈 |
| **实现定义好的 ticket** | Cursor 已经能从 Linear ticket 自动生成实现 |
| **手动重构** | AI 已经擅长这个并且变得更好 |

### 🟢 好——正在升值的技能

| 技能 | 为什么 |
|------|--------|
| **Tech Lead 特质** | 分解复杂工作、写 AI 能执行的清晰 spec、平衡功能和非功能需求。**"即使是初级工程师也需要这个来成长"** |
| **测试和测试基础设施** | 作为验证 AI 输出的反馈循环。单元测试、集成测试、E2E 测试、静态分析 |
| **产品思维工程** | 与用户共情、分解工作、主动修 bug。WorkOS（~80 工程师/1 PM）和 Linear（多年无 PM）是模板 |
| **架构决策** | 指定单体 vs 服务、接口、边界、可测试性。"你必须指导 AI 遵循这些决策" |
| **技术债务管理** | 更多代码 = 更多债务。跟踪、优先级排序、偿还 |
| **可靠/高性能/安全/可扩展系统** | "当任何人都能生成'大部分时候能跑直到突然不能跑'的软件时，能产出持续可靠的工程师更受追捧" |
| **做软件工程师，不是码农** | "The engineering part of building software matters much more" |

### 🟡 丑——令人不安的后果

1. **更多代码 = 更多问题**——Meta 前最高产开发者从月级提交变成 400-600 commits/月。Bug 面、安全问题、资源使用全部乘数级增长
2. **生产代码质量下降**——[Cortex 2026 Benchmark Report](https://go.cortex.io/rs/563-WJM-722/images/2026-Benchmark-Report.pdf): **变更失败率上升 30%**
3. **弱实践伤害更快**——没有自动化测试、编码标准、可观测性的团队会看到回归更频繁更快地打到生产
4. **没有工程技能的"码农"可能挣扎**——非技术人可用 AI 生成代码时，开发者必须提供超越写代码的价值
5. **工作-生活边界侵蚀**——2026 将是移动 AI Agent 编码年。"像 Slack 变成移动端一样，开发者现在走到哪里都能被联系到修 bug"
6. **初级工程师被迫加速成长**——曾经是 Senior/Staff 的期望（全栈、产品思维、架构、测试、验证、技术债）正在变成入门级基线
7. **CS 学位变成硬性要求？**——AI 生成的海量求职申请下，大学学位可能变成验证候选人真实性的"垃圾过滤器"

---

## 调查数据：900+ 工程师的真实状态 (2026/01-02)

| 指标 | 数据 |
|------|------|
| 每周使用 AI 工具 | **95%** |
| 70%+ 工程工作由 AI 完成 | **56%** |
| 常规使用 AI Agent | **55%**（大幅增长） |
| Staff+ 工程师使用 Agent | **63.5%**（所有级别中最高） |
| 常规触发 AI 订阅 token 限制 | ~30% |
| 公司每工程师每月 AI 工具花费 | $100–200 |
| 明确担心成本可持续性 | ~15% |
| 欧洲公司成本谨慎度 | 显著高于美国 |

### 工具市场份额 (2026)

Claude Code 在发布仅 8 个月后飙升到 #1：

| 工具 | "Love" 评分 | 趋势 |
|------|-----------|------|
| **Claude Code** | 46% | #1 最常用 & 最爱 |
| **Cursor** | 19% | 9 个月内增长 ~35% |
| **GitHub Copilot** | 9% | 持平/趋平 |
| **OpenAI Codex** | 爆发式早期增长 | 已达 Cursor 60% 用量 |
| 上升中 | OpenCode, Gemini CLI, Antigravity | — |

### 工程师的三种原型

| 原型 | 特征 |
|------|------|
| **Builder（构建者）** | 代码质量导向。AI 加速但保持高标准 |
| **Shipper（交付者）** | 速度导向。最大化 AI 产出 |
| **Coaster（滑行者）** | 产出足够但 AI 代码质量低，给他人制造摩擦 |

---

## 角色融合——"中间层变薄"

引用 Linear 联合创始人 Karri Saarinen 的概念：**"中间层正在变薄"**——意图到实现之间的人工翻译层在消失。

| 过去 | 现在 |
|------|------|
| PM 写需求 → Dev 写代码 → QA 测试 | PM 写 spec → AI 实现 → 工程师审查 |
| 清晰的角色边界 | 角色重叠急剧扩张 |
| 多层级审批 | "中间的翻译层消失了" |

> *"The era of Agent Centric Development Cycle has arrived. Developers shift from creators to governors."* — Orosz, Sonar Summit 2026

---

## Orosz 的底层判断

> *"The more a team relies on AI-generated code, the more software engineering fundamentals matter. More code means more problems that need to be caught early and addressed systematically."*

> *"Change might be brutally fast. Claude Code went from idea in Boris Cherny's head to industry-changing tool in just over a year. I don't remember change ever being this fast, or hitting the entire industry at once."*

> *"There's also a sense of loss. I'm coming to terms with the likely reality that from now on, most code I push to production will be written by AI. Something precious is being taken away, and suddenly."*

不是在讨论生产力、效率、工具——而是在讨论**失去**。

---

## 2026-09 增量：从访谈者到一线取样者，聚焦评审制度

> 2026-10-03 增量回源（newsletter 原页直抓）。三篇把"人-模型协作"讨论推进一步：

- **09-08《What is happening with code reviews?》**："AI generates more code than devs can track in 2026, so will the code review process have to adapt – or is it doomed?"——他记录的业界主流已是 "**Humans review the AI code reviews.**"（人审 AI 的评审）。
- **09-15《Inside OpenAI's agentic software factory》**："**Codex has gone from a 'nice-to-have' tool to being the backbone of pretty much everything at the company.**"——亲自进前沿实验室取样，作为"软件工程去向"的一线证据。
- **09-24 The Pulse**：转 DHH Rails World 宣告——"declared the end for writing code by hand for professional work… **Is this change now unstoppable?**"（副题："code reviews will probably also go away"）。

**判语**：1 月他是综合访谈与调查的观察者；9 月他一手进入 OpenAI 内部取证，并把"评审制度"立为行业议程——与其 1 月"基本功更重要"的判断相比，9 月的语气更像在记录一场来不及适应的制度变迁。

---

**Source:** [Pragmatic Engineer: What Happens to Software Engineering When AI Writes Almost All the Code](https://newsletter.pragmaticengineer.com/p/the-future-of-software-engineering-with-ai) (2026/01/06) · [Sonar Summit 2026 keynote](https://securityboulevard.com/2026/03/top-6-takeaways-on-the-future-of-coding-from-sonar-summit-2026-7/) · [Hanselminutes: Where is AI taking us](https://zencastr.com/z/P-ljHViI) · [Pragmatic Engineer Survey](https://sourcelabs.nl/blog/pragmatic-engineer-survey-how-ai-tools-reshape-engineering-roles/) · [Daring Fireball: Why Is Meta Destroying Its Engineering Organization](https://daringfireball.net/linked/2026/07/02/orosz-meta-engineering-culture) · [What is happening with code reviews? (2026-09-08)](https://newsletter.pragmaticengineer.com/p/what-is-happening-with-code-reviews) · [Inside OpenAI's agentic software factory (2026-09-15)](https://newsletter.pragmaticengineer.com/p/openai-software-factory) · [The Pulse: writing code by hand, is it over? (2026-09-24)](https://newsletter.pragmaticengineer.com/p/the-pulse-end-of-coding-by-hand)
