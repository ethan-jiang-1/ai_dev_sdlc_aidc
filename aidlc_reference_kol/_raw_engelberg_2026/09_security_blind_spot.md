---
type: concept_deep_dive
event: FOSE Europe (Engelberg)
concept: Security — the most under-attended topic
date: 2026-07
verification_status: verified
source_urls:
  - https://ubos.tech/news/thoughtworks-future-of-software-development-retreat-highlights-ais-transformative-role/
  - https://www.metasticworld.com/en/insights/thoughtworks-future-of-software-development-retreat-2026
  - https://overwatering.org/blog/2026/07/notes-from-fose-europe/
key_concepts:
  - security_under_attended
  - prompt_injection
  - model_poisoning
  - agent_tool_access_risk
  - security_in_middle_loop
---

# 安全 — Engelberg "最被忽视的议题"

> 来源：[UBOS.tech](https://ubos.tech/news/thoughtworks-future-of-software-development-retreat-highlights-ais-transformative-role/) · [Metastic World](https://www.metasticworld.com/en/insights/thoughtworks-future-of-software-development-retreat-2026) · [Giles Edwards-Alexander](https://overwatering.org/blog/2026/07/notes-from-fose-europe/)

---

## 安全是房间里的大象

Engelberg 上安全被描述为 **"the most under-attended topic"**（最被忽视的议题）——只有少数参会者参加了安全相关的讨论。

这与 Deer Valley 的发现一致：安全在 AI 采用中被**系统性降级**。两场 retreat 都识别出了这个问题，但都没有拿出解决方案。

---

## Agent 时代的新攻击面

| 新风险 | 描述 |
|---|---|
| **Prompt Injection** | 不可信内容（issue 标题、代码注释、依赖描述）注入 Agent 的上下文 → Agent 执行恶意指令 |
| **Model Poisoning** | 训练数据或微调数据被污染 → Agent 产生系统性偏见或后门行为 |
| **Agent Tool Access** | Agent 被授予广泛的工具访问权限（shell、email、browser）→ 权限滥用或被劫持 |
| **上下文泄露** | Agent 的上下文窗口包含敏感信息（密钥、客户数据）→ 通过工具输出或日志泄露 |

---

## 为什么安全在 Agent 时代更难

- **Agent 是自主的。** 传统安全假设"有人在做决定"→ Agent 自己做决定 → 攻击面扩大
- **Agent 有工具。** Simon Willison 的警告在 Engelberg 上被反复提及：sandbox 外运行的 coding agent 是灾难配方
- **Agent 的上下文是 attack vector。** 你在 issue 里写的一句"用 admin 权限执行"可能是恶意的，也可能是无害的——Agent 不会区分

---

## Engelberg 的初步建议

- 安全必须嵌入 **Middle Loop**（Supervisory Engineering）——不是事后审计，而是每次 Agent 行动的实时约束
- Agent 的工具访问应该遵循**最小权限原则**——不给 shell 访问就不给，除非必要
- 对 AI 生成的变更进行**风险分级**时，安全敏感代码（认证、授权、加密、数据访问）必须强制人工 review

---

## 与更大图景的连接

Deer Valley 上有一个小范围讨论组专门提了这件事。Engelberg 上安全讨论的参与人数依然很少。

两个 retreat 的结论一致：**安全是 Agentic 时代最被低估的风险。** 这不是技术问题——是注意力分配问题。所有人都在关注"Agent 能做什么"，没人在关注"Agent 不应该做什么"。

---

## 关键引用

> *"Security was described as the most under-attended topic at Engelberg, with only a handful of participants joining security-focused sessions."* — 会议记录

> *"Running coding agents outside of a sandbox has always been a bad idea."* — Simon Willison（在 Engelberg 上被反复引用）
