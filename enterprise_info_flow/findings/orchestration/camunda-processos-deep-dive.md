---
title: Camunda ProcessOS — AI-native BPM 的唯一标本
date: 2026-07-08
source: web_search (deep)
type: deep_dive
status: draft
---

# Camunda ProcessOS — AI-native BPM 的唯一标本

> Camunda 是 BPM 领域的老牌厂商（不是创业炒作）。ProcessOS 是 2026 年 5 月发布的 AI 原生产品。它是目前最接近"AI-native BPM 的方法论+产品"的东西。挖透了它，等于看到一个 AI 时代业务处理流程的完整设计。

---

## 定位："The Great Process Re-Engineering"

Camunda CEO Jakob Freund：

> *"Every process in your enterprise is legacy — it was designed for a world where AI did not exist. This is why we are now entering the decade of 'the great re-engineering': every company will reinvent itself or die."*

他的判断：给旧流程加 AI 只提升 ~20%。为 AI 重设计流程可以把**数月压缩到数天**。

> Source: [Camunda announces ProcessOS](https://secure.businesswire.com/news/home/20260520352437/en/Camunda-announces-ProcessOS-an-agentic-operating-system-for-AI-first-enterprise-transformation), BusinessWire, May 2026

---

## 架构：四个专门 AI Agent

| Agent | 角色 | 做什么 |
|-------|------|--------|
| **Discovery Agent** | 发现 | 用运营数据映射流程**实际怎么跑的**（不是你以为怎么跑的） |
| **Design/Re-engineering Agent** | 重设计 | 围绕结果和 KPI 重新设计流程，决定什么归 Agent、什么归人 |
| **Build & Deploy Agent** | 构建 | 生成完整方案——agentic 流程、集成、数据映射、prompt、决策、UI |
| **Optimization Agent** | 优化 | 监控生产环境，标记漂移，用历史数据回测改进方案（人审批后执行） |

**四个 Agent 是按流程生命周期分工的，不是按功能模块分的。** 这意味着"流程"本身变成了一个活的、持续演进的东西——不再是画完 BPMN 就锁死的文档。

> Source: [ProcessOS: The Operating System for Your Processes](https://camunda.com/platform/process-os/), Camunda, 2026

---

## 关键架构决策

### 1. 自然语言 → 完整方案

你描述想要的业务结果和 KPI。ProcessOS 生成完整的流程方案——包括 agent 分配、集成、数据映射、prompt、UI 表单。

### 2. Fitness Functions

加权评分模型覆盖多个 KPI（周期、解决率、单例成本、合规率）。指导设计决策，评估每一个改进提案。**这是把"流程好不好"变成可测量的——跟 SDLC 里的 CI 质量门禁同构。**

### 3. Organizational Memory

存在**私有 git 仓库**里的知识模型——集成模式、边缘案例、流程决策。每建一个流程，下一个会更快。永不用来训练共享模型。

### 4. BPMN = 治理可视化层

关键：**BPMN 流程模型明确标出 AI 执行的步骤、条件、人接触点。** Agent 在 BPMN 流程内执行 = 继承了流程层的审计、版本管理、SLA、合规。这就是 Camunda 论证"BPM 一直是 AI Agent 的正确层"的核心。

> Source: [Stop Building Agent Islands. Start Orchestrating.](https://camunda.com/blog/2026/06/stop-building-agent-islands-start-orchestrating/), Camunda Blog, Jun 2026

### 5. Human-in-the-loop 是硬要求

每个流程修改必须经过人审批才能上线。不是可选项——是内建设计。

---

## 数据：多少人真的在生产环境？

CamundaCon 2026 从业者面板（Audi, Danica, Provinzial）：

- **71%** 的组织在用 AI agents
- 只有 **11%** 到了生产环境
- **48%** 说 agents 在孤岛中运行

> Source: [Stop Building Agent Islands. Start Orchestrating.](https://camunda.com/blog/2026/06/stop-building-agent-islands-start-orchestrating/), Camunda Blog, Jun 2026

---

## 客户案例

| 公司 | 结果 |
|------|------|
| Danica (Danske Bank) | 客户 onboarding：数月 → 数天 |
| Finnova | 客户 onboarding 快 70-80% |
| R-KOM | 工单响应：8 小时 → 近实时 |

---

## Forrester 的评价

Dr. Bernhard Schaffrik, Forrester 首席分析师：

> *"GenAI 扩展了可自动化流程的边界。APO（Adaptive Process Orchestration）是通向自主业务运营的进化一步。市场正在向 AI-first agentic 方法演进，将 AI 与确定性工作流混合，同时厂商将工具整合到以治理、可观测性和混合 human-in-the-loop 执行为核心的编排主干中。"*

> Source: [Camunda ProcessOS: BPM Was Always the Right Layer for AI Agents](https://resources.rework.com/news/ai-at-work/camunda-processos-bpm-agentic-layer-cto), Rework, 2026

---

## 对 SDLC-BPM 同构性研究的启示

ProcessOS 验证了一个关键假设：**流程引擎没有消失——它变成了 AI Agent 执行的 governance frame。** Agent 在框内自主，但框本身（BPMN + 审计 + SLA + human-in-the-loop）是人定义和控制的。

这是"预定义流程 → framed autonomy"的精确体现。跟 SDLC 里的 "操作者→委托人"、"AI Sandwich" 是同构的。
