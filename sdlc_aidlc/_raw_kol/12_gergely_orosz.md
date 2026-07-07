# Gergely Orosz — "代码量爆炸，工程基本功反而更重要了"

> *The Pragmatic Engineer* 作者，Pragmatic Summit 主办者。2026 年 1 月的万字长文 *"What Happens to Software Engineering When AI Writes Almost All the Code"* 被广泛认为是 AI 时代软件工程最全面的预测之一。采访了 Kent Beck、Martin Fowler、Simon Willison。900+ 工程师调查。

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
2. **生产代码质量下降**——Cortex 2026 Benchmark Report: **变更失败率上升 30%**
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

最后这句话可能是 2026 年最诚实的工程师情感表达。不是在讨论生产力、效率、工具——而是在讨论**失去**。

---

**Source:** [Pragmatic Engineer: What Happens to Software Engineering When AI Writes Almost All the Code](https://newsletter.pragmaticengineer.com/p/the-future-of-software-engineering-with-ai) (2026/01/06) · [Sonar Summit 2026 keynote](https://securityboulevard.com/2026/03/top-6-takeaways-on-the-future-of-coding-from-sonar-summit-2026-7/) · [Hanselminutes: Where is AI taking us](https://zencastr.com/z/P-ljHViI) · [Pragmatic Engineer Survey](https://sourcelabs.nl/blog/pragmatic-engineer-survey-how-ai-tools-reshape-engineering-roles/) · [Daring Fireball: Why Is Meta Destroying Its Engineering Organization](https://daringfireball.net/linked/2026/07/02/orosz-meta-engineering-culture)
