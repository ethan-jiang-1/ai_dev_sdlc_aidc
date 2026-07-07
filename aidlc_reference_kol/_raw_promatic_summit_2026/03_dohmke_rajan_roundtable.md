---
type: event_session
event: Pragmatic Summit 2026
session: Thomas Dohmke & Rajeev Rajan Fireside Chat
date: 2026-02-11
location: San Francisco
host: Gergely Orosz (The Pragmatic Engineer)
verification_status: verified
source_urls:
  - https://podwise.ai/episodes/7546403
  - https://newsletter.pragmaticengineer.com/p/the-future-of-software-engineering-with-ai
  - http://mp.weixin.qq.com/s?__biz=Mzk5MDQyOTA5Ng==&mid=2247483763&idx=1&sn=b390aec4aec271a633f57e7dca337fd4
key_participants:
  - Thomas Dohmke (ex-GitHub CEO, Entire founder, $60M seed)
  - Rajeev "Rajie" Rajan (Atlassian CTO)
key_concepts:
  - homer_simpson_car
  - role_collapse
  - cto_coding_again
  - agent_assembly_line
  - token_cost_shock
  - dont_look_at_the_code
---

# Dohmke + Rajan 圆桌 — "Homer Simpson 车"与 AI-Native 团队的真实面貌

> 来源：Pragmatic Summit 2026 最具实操深度的 session。
> 原文链接：[Podwise 播客](https://podwise.ai/episodes/7546403) (~33 min) · [Pragmatic Engineer: Future of Software Engineering](https://newsletter.pragmaticengineer.com/p/the-future-of-software-engineering-with-ai) · [中文编译](http://mp.weixin.qq.com/s?__biz=Mzk5MDQyOTA5Ng==&mid=2247483763&idx=1&sn=b390aec4aec271a633f57e7dca337fd4)

---

## "Homer Simpson 车"——Dohmke 的警告

> *"You feed all your ideas to an agent, the agent writes all the code, another agent reviews it, auto-merges, and auto-deploys. The result is Homer Simpson's car — it has every feature, but it's ugly as hell."*

每个人都能提交代码，但没人做架构监督——结果是辛普森一家的车：什么功能都有，但什么都不对。

**仍然需要 PM、设计师和工程师来架构真正伟大的产品。**

---

## Atlassian 的 Rovo Dev 数据

Atlassian 内部编码 Agent（基于 Anthropic 模型）的实测指标：

| 指标 | 数据 |
|---|---|
| PR/工程师增长 | **89%** |
| Issue cycle time 减少 | **42%** |
| 安全漏洞由 Agent 修复 | **51%** |
| DORA 指标 | 全面改善 |

Rovo Dev **击败了专门的代码 Agent 竞品**——秘诀是通过 **Teamwork Graph**（150 亿连接）获取上下文：知道谁在哪个 PR 上协作过、哪些 Jira issues 关联、代码变更的历史上下文。

---

## "AI-Native Teams" 的真实面貌

> Rajeev: AI 的重点**不是减人**，是构建以前不可能构建的东西。
> Dohmke: "AI-native" 就像 2008 年的 "cloud-native"——我们只能事后才真正知道它意味着什么。

Atlassian 内部已有工程师团队**零手写代码**——一切由 Agent 完成。工程师的新角色：编排 Agent、设定规则、验证输出。

---

## 角色坍缩

> PM → Product Engineer · Designer → Design Engineer · Engineer → 半 PM

角色之间的 Venn 图重叠**急剧扩张**。Atlassian 的 PM 在用 AI 写代码，设计师在用 AI 写代码，工程师在做更多产品决策。

---

## 瓶颈迁移——Rajan 的框架

| 左边（上游） | 中间 | 右边（下游） |
|---|---|---|
| 规划 + Spec | ~~写代码~~（变成免费的） | CI/CD + 部署 + Incidents |

---

## CTO 们又开始写代码了

- Rajeev **自己买了台笔记本电脑**，度假时绕过公司 IT 限制使用 Claude Code 写 Python
- 银行 CTO 晚上用 AI 工具 coding——"我又能写代码了"
- 引用 Jensen Huang 的 **40-50 个直接下属**模型——管理层将压缩
- 给工程师的建议：**别急着进管理**——这是 hands-on 的黄金时代

---

## Token 成本——CFO 们没准备好

- Token 消耗正在吃掉固定工程预算——有团队因为**烧 token 太快被限速**
- CFO 们对这种弹性成本结构毫无准备
- 但两人都同意：**coding 又变好玩了**——把烦人的构建错误丢给 Agent 说"修好它，我不想看"的价值被低估了

---

## Dohmke 的"不要看代码"

> 最 AI-native 的开发者在绿地项目上强迫自己**不读**生成的代码，依赖 Agent 审查其他 Agent 的输出。人的角色从 coder 变成 "master of agents"。

---

## 关键引用

> *"The result is Homer Simpson's car — it has every feature, but it's ugly as hell."* — Thomas Dohmke

> *"Don't look at the code."* — Dohmke 描述最 AI-native 的开发者

> *"Coding is fun again."* — Rajeev Rajan
