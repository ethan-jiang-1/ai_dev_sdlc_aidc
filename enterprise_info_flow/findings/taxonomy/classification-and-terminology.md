---
title: 企业信息加工流 — 分类体系与术语
date: 2026-07-08
source: synthesis (Round 4 findings)
type: taxonomy
status: draft
---

# 分类体系与术语

> 7 轮探索后，企业信息加工流领域的所有"新东西"都有了正式名称。这个文件把它们整理成统一的分类体系。

---

## 一、品类名称对照表

飞书/钉钉/企微这些"协同办公"平台，英文世界叫什么？Camunda 的新产品叫什么？学术圈的新范式叫什么？——这些在 Round 4 里都有了答案。

| 东西 | 中文名 | 英文名 | 谁定义的 |
|------|--------|--------|---------|
| 传统流程管理 | 业务流程管理 (BPM) | Business Process Management | 40 年学术 + 工业共识 |
| 飞书/钉钉/企微/Teams/Slack | **协同办公** / 新型协同办公平台 | **Collaborative Work Management (CWM)** | Gartner/Forrester |
| Camunda 的新产品 | — | **Agentic Orchestration** / Adaptive Process Orchestration (APO) | Camunda / Forrester |
| 学术圈的新范式 | — | **Agentic Business Process Management (APM)** / A-BPMS | Dagstuhl Seminar (18 位作者) |
| 模型公司做的那层 | — | **Agentic Platform Layer** / Agent Control Plane | Arion Research / VentureBeat |
| 从零重建的创业公司 | — | **Agentic-Native Production Platforms** | xpander.ai / Windsor Drake |

**关键发现**：CWM 这个术语在 `grep -rn "CWM" findings/` 中零命中（2026-07-08 检查）——它只存在于 exploration-trajectory.md 的 Round 4 表格里。这说明早期 findings 文件在写的时候还没找到这个术语。现在补上。

> Source: Gartner/Forrester 对协作软件市场的品类定义。Arion Research 2026 年企业 AI 代理市场报告。

---

## 二、三层架构（Arion Research, 2026）

Arion Research 提出的企业 AI 代理三层架构：

```
Enterprise Platform Layer（CRM, ERP, HCM — 记录系统）
        ↓
Agentic Platform Layer（编排、执行、治理 — 新层）
        ↓
Collaboration Layer（跨 agent 通信）
```

与我们最终的四层模型对比：
- Arion 的 "Enterprise Platform Layer" = 我们的"后端"
- Arion 的 "Agentic Platform Layer" = 我们的"中端 + 治理层"
- Arion 的 "Collaboration Layer" = 未在我们的模型中单独成层，而是作为"前端"的能力之一

**差异**：Arion 把治理放在 Agentic Platform Layer 内部，我们把它作为横切层独立出来——因为治理（身份、权限、审计、熔断）横跨所有层，不是只属于编排层。

---

## 三、四类厂商分类（Arion Research）

| 类型 | 中文 | 代表 | 拥有什么 |
|------|------|------|------|
| **Vertical Integrators** | 垂直整合者 | Oracle, Salesforce, ServiceNow, SAP | 拥有数据（记录系统） |
| **Horizontal Platforms** | 横向平台 | OpenAI, Anthropic | 拥有智能（模型能力） |
| **Infrastructure/Ecosystem** | 基础设施/生态 | Microsoft, Google | 横跨所有层（分发 + 模型 + 数据） |
| **Independent/Specialized** | 独立/专业 | Camunda, xpander.ai | 编排优先，厂商中立 |

**与 SDLC 领域的对应**：
- Vertical Integrators ≈ 传统 SDLC 工具厂商（拥有项目管理和代码仓库）
- Horizontal Platforms ≈ AI 模型/Agent 框架厂商
- Infrastructure/Ecosystem ≈ GitHub/GitLab（横跨代码托管 + CI/CD + AI 能力）
- Independent/Specialized ≈ 独立 AI 编程工具（Cursor, Claude Code 等）

---

## 四、三级成熟度模型（xpander.ai）

| 级别 | 中文 | 代表 | 核心问题 |
|------|------|------|------|
| **Retrofitted Automation** | 改造式自动化 | Zapier, n8n, Make | Agent 继承了 trigger-action 的约束——流程仍是预定义的 |
| **Build-Only Frameworks** | 仅构建框架 | LangChain, CrewAI | 只管构建 agent，不管部署/监控/治理 |
| **Agentic-Native Platforms** | Agent 原生平台 | xpander.ai | 从零为 agent 自主执行而建——治理是一等公民 |

这个分类跟 SDLC 领域的工具链成熟度对应：
- Retrofitted ≈ CI/CD 管道里嵌入 AI 步骤（表面集成）
- Build-Only ≈ AI 编码助手（只管生成，不管部署和验证）
- Agentic-Native ≈ AI-SDLC（AI 贯穿全生命周期，治理内置）

---

## 五、术语收敛论

三个术语——厂商的 "Agentic Orchestration"、分析师的 "Adaptive Process Orchestration (APO)"、学术圈的 "Agentic BPM (APM)"——**是同一个结论从不同出身出发的表达**。

| 术语 | 出身 | 核心主张 |
|------|------|------|
| **Agentic Orchestration** | 厂商/实践者（Nividous, UiPath, AA） | 多 Agent 协调、目标分解、共享记忆 |
| **Agentic BPM (A-BPMS)** | 学术界（Dumas, Calvanese 等） | BPM 的自然进化——5 级自主连续体 |
| **Adaptive Process Orchestration (APO)** | 分析师（Forrester, 2025） | 确定性骨架 + 非确定性 Agent 行为共存 |

**三者的共识**：
> "确定性编排骨架提供治理、审计和结构。AI Agent 提供适应性、推理和自主。挑战是融合而非选择。"

UiPath 的 Boris Krumrey：
> "混合模式——确定性骨架 + 有边界的 agentic 任务——将主导。"

---

## 六、"Framed Autonomy"的正式定义

来自 Calvanese 等 18 位作者（Dagstuhl Seminar, 2026）：

> "确保 APM 系统中流程感知和目标对齐的主要机制，通过对 Agent 的知识和目标施加限制来约束其自主性。"

**框架的两种类型**：
- **Operational frames**：规定具体执行序列
- **Normative frames**：规定允许/禁止的行为（用道义逻辑或声明式语言）

**与 SDLC 的对应**：
- Operational frames ≈ CI 管道中的 lint/stage/merge 规则
- Normative frames ≈ 编码规范、安全策略、合规约束

---

## 七、CWM 和 BPM 的融合

CWM（协同办公）和 BPM（业务流程管理）不是竞争关系——在 AI 时代它们正在**融合成一个统一的执行层**。

**致远（中国 BPM/CWM 厂商）的三级模型**：
1. **Co-pilot 模式** — AI 辅助人（推荐、分析），人仍是主要行动者
2. **Co-work 模式（Agentic Orchestration）** — AI agent 在人定义的流程内执行特定任务。**这是 2026 年企业的主流。**
3. **Autonomous Agent 模式** — 多 Agent 独立分解目标、端到端执行、自纠正。人只是监督者。

**关键判断**：CWM 正在从"人用的协作工具"变成"Agent 运行的前端基础设施"——飞书/钉钉的 CLI 化、MS Office 的 Agent 365、Google Workspace Intelligence 都是这个趋势的实证。

---

## 对"信息加工流"研究的启示

1. **命名问题已解决。** 每个品类都有正式名称了——CWM（前端）、Agentic Orchestration/APM/APO（中端）、Agentic Platform Layer（治理层）。
2. **确定性骨架 + Agentic 自主是跨品类的共识。** 不同出身的人用不同术语在说同一件事。
3. **分类体系可以直接映射到 SDLC。** Retrofitted/Build-Only/Agentic-Native 的成熟度阶梯，在 SDLC 领域同样适用。
4. **CWM 和 BPM 的融合 = 前端和中端的融合。** 跟 SDLC 中 "编码工具 + CI/CD + Agent 编排" 的融合完全同构。
