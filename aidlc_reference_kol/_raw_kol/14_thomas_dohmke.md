---
type: kol_deep_dive
person: Thomas Dohmke
organization: Entire (ex-GitHub CEO)
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://www.bloomberg.com/news/articles/2026-02-10/former-github-ceo-thomas-dohmke-raises-60-million-for-new-startup
  - https://www.geekwire.com/2026/former-github-ceo-launches-new-developer-platform-with-huge-60m-seed-round/
  - https://www.axios.com/2026/02/10/former-github-ceo-ai-coding-startup
  - https://devops.com/former-github-ceo-bets-60m-that-developer-tools-need-a-factory-reset-for-the-ai-age/
  - https://36kr.com/p/3678623948366473
  - https://entire.io
key_concepts:
  - homer_simpson_car
  - agent_assembly_line
  - developer_tools_factory_reset
---
# Thomas Dohmke — "Git 只记录了'改了什么'，无法回答'为什么这么改'"

> 前 GitHub CEO（领导了 Copilot 的推出）。2025 年 8 月离职，2026 年 2 月创办 Entire（$60M 种子轮，$300M 估值）。他的核心判断：**GitHub 那代开发者平台诞生于"人写代码"的时代，而非"Agent 写代码"的时代。**

---

## 从 GitHub CEO 到 AI-Native 创业者

Dohmke 是极少数**在 Copilot 时代领导过全球最大开发者平台**、现在又亲自下场重建的人。他的转型路径本身就值得注意：

| 时间 | 事件 |
|------|------|
| 2021-2025 | GitHub CEO——推出 Copilot，见证从代码补全到 Agent 的完整演化 |
| 2025/08 | 从 GitHub 离职 |
| 2026/02/10 | 宣布 Entire——**$60M 种子轮，$300M 估值**（DevTools 领域最大种子轮） |

投资方：Felicis Ventures（领投）、Madrona、微软 M12、Basis Set。个人投资人：Jerry Yang（雅虎联合创始人）、Garry Tan（YC CEO）、Olivier Pomel（Datadog CEO）。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。

## 核心判断：开发者平台需要"工厂重置"

> *"GitHub's generation of developer platforms was born in an era when humans wrote code, not agents. The entire stack needs a factory reset for the AI age."*

Dohmke 认为现有工具链有三个根本问题：

| 问题 | 现有工具 | Entire 的答案 |
|------|---------|-------------|
| **Git 记录"改了 什么"但不记录"为什么"** | Git blame 告诉你谁改了哪行 | 把完整的 Agent 会话上下文（prompt、日志、工具调用、token 消耗）作为一等版本数据保存 |
| **Agent 之间无法共享"工作记忆"** | 每个 Agent 实例独立推理，重复消耗 Token | 通用语义推理层——跨会话共享上下文 |
| **IDE 为人类设计，不是为 Agent 设计** | 可视化 diff、代码导航 | "AI-native UI"——重新思考人机协作的界面 |

---

## 首款产品：Checkpoints（已开源 CLI）

> 把 Agent 的**思考过程**写进 Git。

Checkpoints 将每次 AI 编码会话的完整上下文与 commit 绑定：

- Prompt、推理链、日志、访问文件、工具调用、Token 消耗
- 每次 Agent 触发的提交生成结构化检查点对象，与对应 commit SHA 关联
- 推送时检查点同步写入**独立、只追加的分支**——形成完整审计日志
- "Git blame 告诉你谁改了哪行。Checkpoints 告诉你**为什么**。"

首批集成：Claude Code、Google Gemini CLI。即将支持 OpenAI Codex、Cursor CLI。

### 竞争定位

> *"We are not training models or building agents, we are integrating with them."*

Entire 不做模型、不做 Agent——它是 Agent 之上的**管理层/编排层**。开源、独立、Agent 无关。商业模式遵循"开源 + 托管服务"。

### 从 HockeyApp 到 GitHub 到 Entire

| 时间 | 事件 |
|------|------|
| 2015 | 将 HockeyApp 卖给微软，移居美国 |
| 2018 | GitHub 被微软收购，Dohmke 加入 |
| 2021 | 成为 GitHub CEO，推动 Copilot |
| 2025/08 | 离开 GitHub |
| 2026/02/10 | Entire 公开——$60M 种子轮，$300M 估值 |

---

## "Token 价值"——CFO 们的新噩梦

Dohmke 在 Pragmatic Summit 上提出了一个 CFO 们尚未准备的概念：

> *"Leaders need to look at headcount differently — not just salary and benefits, but also token value. Some engineers are burning thousands of dollars in tokens monthly."*

| 传统成本模型 | 新成本模型 |
|-----------|-----------|
| 固定薪资（可预测） | 固定薪资 + **弹性 Token 成本**（不可预测） |
| 按人头预算 | **按 Agent 使用量预算** |
| 工具是固定单价 | Token 单价随模型能力和使用强度变化 |

---

## "Agent 装配线"——开发流程的重构

Dohmke 引用汽车工业从手工作坊到流水线的转变作为 Entire 的核心理念：

> *"Soon, developers won't look at the code anymore, as agents will write way more than humans can review. We have to rethink the entire system of software production from the ground up. Just like when automotive companies replaced the traditional, craft-based production system with the moving assembly line, we must now reimagine the software development lifecycle for a world where machines are the primary producers of code."*

| 手工作坊（过去） | Agent 装配线（未来） |
|---------------|------------------|
| 一个开发者做所有事 | 专用 Agent 处理不同阶段 |
| 代码是手工艺品 | 代码是流水线产物 |
| 质量靠个人判断 | 质量靠 pipeline 中的关隘强制执行 |

---

## Pragmatic Summit 上的关键发言

在 2026 年 Pragmatic Summit 上，Dohmke 与 Atlassian CTO Rajeev Rajan 同台，贡献了几个被广泛引用的判断：

### "Homer Simpson 车"问题

> *"When everyone can ship code but nobody is doing architecture/design oversight, you get the Homer Simpson car."*

每个人都能提交代码，但没人做架构监督——结果是辛普森一家的车：什么功能都有，但什么都不对。

### "AI-native"就像 2008 年的"cloud-native"

> *"We'll only know what it truly means in hindsight."*

### 远程团队获得 AI 优势

Entire 是 15 人、6 个国家的全远程团队。Agent 解决了远程工作最大的痛点："我被卡住了，周围没人可问。"

> *"Cross-timezone coverage plus agents creates a 24/7 work rhythm that office-bound teams can't match."*

---

## 关键引用汇总

> *"GitHub's generation of developer platforms was born in an era when humans wrote code, not agents. The entire stack needs a factory reset."*

> *"When everyone can ship code but nobody is doing architecture/design oversight, you get the Homer Simpson car."*

> *"Leaders need to look at headcount differently — not just salary and benefits, but also token value."*

> *"Software development needs to be restructured as an agent assembly line."*

---

**Source:** [Bloomberg: Former GitHub CEO Raises $60M](https://www.bloomberg.com/news/articles/2026-02-10/former-github-ceo-thomas-dohmke-raises-60-million-for-new-startup) · [GeekWire: $60M seed round](https://www.geekwire.com/2026/former-github-ceo-launches-new-developer-platform-with-huge-60m-seed-round/) · [Axios: Former GitHub CEO launches AI coding startup](https://www.axios.com/2026/02/10/former-github-ceo-ai-coding-startup) · [DevOps.com: Factory Reset for the AI Age](https://devops.com/former-github-ceo-bets-60m-that-developer-tools-need-a-factory-reset-for-the-ai-age/) · [36Kr (Chinese)](https://36kr.com/p/3678623948366473) · [InfoQ China: 前GitHub掌门人](https://www.infoq.cn/article/fcjA0034GUQVp20cjHZU) · [entire.io](https://entire.io)
