---
title: 企业信息加工流 — 四层架构
date: 2026-07-08
source: synthesis (Round 7 capstone)
type: architecture
status: draft
---

# 企业信息加工流的四层架构

> 7 轮探索的 capstone synthesis。信息加工流从"人操作工具"变成"Agent 在分层平台上自主加工信息"——这个变化在每一层同时发生。

---

## 四层全景图

```
┌─────────────────────────────────────────────────────────────┐
│  前端（Agent 的"家"）                                        │
│  Office / Workspace / WorkBuddy / 飞书 / 钉钉                │
│  身份、邮箱、日历、文档、协作频道——Agent 运行的基础设施         │
├─────────────────────────────────────────────────────────────┤
│  中端（工作流怎么编排）                                       │
│  Agentic Orchestration / APO / Agentic BPM / ProcessOS       │
│  确定性骨架 + Agentic 自主 = Framed Autonomy                  │
├─────────────────────────────────────────────────────────────┤
│  后端（记录系统）                                             │
│  CRM / ERP / HCM / 传统 BPM                                  │
│  业务数据、合规流程、审计追踪                                   │
├─────────────────────────────────────────────────────────────┤
│  治理层（横切）                                               │
│  Agent 365 / AI Control Tower / Rubrik Agent Cloud           │
│  身份、权限、审计、熔断、回滚                                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 每一层的 2026 年状态

### 前端：从"人用的工具"到"Agent 的基础设施"

**发生了什么**：Office 套件不再只是人用的生产力工具——每个 Agent 需要一个"办公身份"（邮箱、日历、文档权限、Teams 频道）。

**关键信号**：
- Satya Nadella（2026）：*"在 Agent 时代，企业配置的第一个资源是 Office——因为 Agent 需要跟人协作。"*
- MS Copilot Cowork：用户描述目标 → Agent 自主跨 Excel/Outlook/Word/PPT 执行
- Google Workspace Intelligence：实时知识图谱为自主 Agent 提供上下文
- 腾讯 WorkBuddy：月访问 885 万，SkillHub 7 万+ 技能，微信/企微统一身份
- 飞书/钉钉同日开源 CLI：2500+ API 变成 AI 可调用的原子指令

**代表厂商**：Microsoft（Agent 365）、Google（Workspace Intelligence）、腾讯（WorkBuddy）、飞书（龙虾架构）、钉钉（悟空）

> 详见: `findings/front-end/office-workspace-agent-platform.md`, `findings/front-end/feishu-cli-architecture-deep-dive.md`

### 中端：从"预定义流程引擎"到"Framed Autonomy"

**发生了什么**：流程不再被完整预定义。人在关键节点定义"框"（治理边界、KPI、约束），Agent 在框内自主执行原子能力。

**关键信号**：
- Camunda ProcessOS：4 个 AI agents（发现→重设计→构建→优化），BPMN = 治理可视化层，Fitness Functions，Organizational Memory
- Agentic BPM manifesto（Dagstuhl Seminar, 18 位作者）：Framed Autonomy, Explainability, Conversational Actionability, Self-Modification
- 致远三级模型：Co-pilot → Co-work → Autonomous——**2026 年主流在 Co-work**
- BPM Pulse Survey 2026：42% 在 BPM 中用生成式 AI，但只有 16% 让 Agent 自主操控流程

**代表厂商/框架**：Camunda ProcessOS, ServiceNow AI Control Tower, xpander.ai, Neo, Reevo

> 详见: `findings/orchestration/camunda-processos-deep-dive.md`, `findings/methodology/agentic-bpm-academic-landscape.md`

### 后端：记录系统仍在，但接入方式变了

**发生了什么**：CRM/ERP/HCM 这些记录系统不会消失——但它们不再是人直接操作的界面，而是变成 Agent 调用的数据源和约束源。

**关键信号**：
- SAP Autonomous Enterprise：50+ Joule Assistants，200+ 专门 agents，全流程编排
- Salesforce $8B 收购 Informatica——数据集成是 Agent 可用的前提
- Oracle/SAP 的 Agent 策略都是"在我们的记录系统之上加编排层"

**代表厂商**：SAP, Oracle, Salesforce, 用友, 金蝶

### 治理层：Agent 的控制平面——2026 年最激烈的争夺点

**发生了什么**：当 Agent 有了身份、邮箱、文件权限、跨系统操作能力，谁控制 Agent 的权限边界和审计追踪？这是模型公司和大厂的正面战场。

**关键信号**：
- MS Agent 365：IT 集中治理面板——组织内每个 Agent 都可观测、可管控
- ServiceNow AI Control Tower：Agentic 采用框架 + 治理模型
- Rubrik Agent Cloud：补 Claude Cowork 的企业控制缺口
- Routines 权限预提交模式：Agent 计划提交 → 人 approve → Agent 执行

**核心 tension**：模型公司（OpenAI/Anthropic）拥有智能，大厂（MS/SAP/ServiceNow）拥有数据和治理框架。Agent 控制平面是双方必争之地。

> 详见: `findings/orchestration/agent-control-plane-cowork-frontier.md`

---

## 与 SDLC 变革的完全同构

这是这个研究项目的核心结论——两边的变革在每一层都有精确对应：

| 维度 | SDLC 领域 | 企业信息流领域 |
|------|------|------|
| **旧范式** | 人先想清楚 → 拆解 → 逐行写代码 | 预定义流程 → 审批流 → 人执行 |
| **新范式** | AI Sandwich / 操作者→委托人 | Framed Autonomy / Co-work 模式 |
| **人的角色** | Brief / Review / Sign-off | 定义框 + 关键节点策展 + 熔断确认 |
| **AI 的角色** | 中间层执行和探索 | 框内自主执行原子能力 |
| **核心 artifact** | Spec 取代代码 | 流程框（frame）取代 BPMN 流程图 |
| **治理模式** | 约束编码进 CI/linter | 权限预提交 + 审计 + Agent Rewind |
| **前端平台** | Claude Code / Cursor / Copilot | Office / Workspace / WorkBuddy |
| **中端编排** | Agent SDK / Routines / Triggers | Camunda ProcessOS / APO / Agentic BPM |
| **后端记录** | Git / Issue Tracker / Code Review | CRM / ERP / HCM |
| **治理层** | CI/CD Pipeline + Code Owners + Protected Branches | Agent 365 / AI Control Tower / Permission Pre-commit |
| **成熟度** | 11% 生产环境（CamundaCon 数据） | 11% 生产环境（同一数据源） |

**最关键的数字**：两边都是 42% 在用 AI 辅助，但只有 16%（企业侧）/ 11%（SDLC 侧）让 AI 自主执行。信任鸿沟（BPM 侧 48.8%）是两边的共同瓶颈。

---

## 这个架构意味着什么

1. **"信息加工流"确实是一个统一框架。** 不管加工的是代码还是合同，四层架构（前端/中端/后端/治理）是通用的。每一层都在经历同样的范式转移。

2. **前端是 2026 年被低估的一层。** BPM 和编排层研究很多，但 Office→Agent 基础设施的转变是最近 3 个月才加速的。Nadella 的原话说明 MS 已经把这一层定位为 Agent 时代的入口。

3. **治理层是最激烈的战场。** 谁控制 Agent 的身份、权限、审计——谁就控制企业 AI 的采用方式。模型公司和大厂在这里正面冲突。

4. **中端是方法论的核心。** "Framed Autonomy" 是目前最精确的术语——它同时描述了 SDLC 和 BPM 的新范式。框由人定义，框内的执行由 Agent 自主完成。

5. **两边的研究可以互相借力。** 如果 BPM 侧在治理层先行一步（比如 ServiceNow Blueprint），SDLC 侧可以直接借用。如果 SDLC 侧在 Agent 编排上更成熟，也可以反向输出给 BPM。
