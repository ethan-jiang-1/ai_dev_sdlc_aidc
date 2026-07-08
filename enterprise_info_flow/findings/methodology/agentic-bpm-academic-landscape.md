---
title: Agentic BPM — 学术圈对 AI 的回应
date: 2026-07-08
source: web_search (deep)
type: deep_dive
status: draft
---

# Agentic BPM — 学术圈对 AI 的回应

> BPM 学术圈没有在睡觉。2026 年，"Agentic Business Process Management (APM)"被正式定义为一个新范式。有 manifesto、有架构论文、有行业调查。这跟 SDLC 领域的"AI-SDLC"探索是完全平行的。

---

## 核心文献：APM Research Manifesto

**Diego Calvanese 等 18 位作者**（Dagstuhl Seminar #25192 AUTOBIZ 产出）。

正式定义了 **Agentic Business Process Management (APM)**——从"自动化导向的 BPM"到"自主 agent（人+AI）作为一等流程感知实体的系统"。

**APM 的四大能力**：

| 能力 | 含义 |
|------|------|
| **Framed Autonomy** | Agent 在流程"框架"（规范性 + 操作性约束）内自主运行 |
| **Explainability** | Agent 必须能解释行为理由——这是部署的前提条件 |
| **Conversational Actionability** | 自然语言交互、协商、异常处理 |
| **Self-Modification** | 短期适应 + 通过流程挖掘反馈回路的长期演进 |

**宏观/微观分离架构**：macro-level（APM 系统/框架）vs micro-level（agent 执行）。

> Source: [Agentic Business Process Management: A Research Manifesto](https://www.sciencedirect.com/science/article/pii/S0306437926000529), Information Systems, Vol.140, Aug-Sep 2026
> Source: [arXiv: 2603.18916](https://browse-export.arxiv.org/abs/2603.18916), Mar 2026

---

## 其他关键论文

### A-BPMS: Agentic BPMS（Chapela-Campa, Milani, Dumas）

提出 **A-BPMS**——集成自主性、推理和学习的 BPM 平台新类别。以流程挖掘为 agent 感知、推理和行动的基础。

> Source: [Agentic Business Process Management Systems](https://arxivlens.com/paperview/details/agentic-business-process-management-systems-289-5ef935b1), BPM 2025 AI4BPM Workshop

### 模块化 LLM Agent 架构

德国能源网公司的 meter-to-cash 真实案例：
- **Frame Agent**：生成流程描述
- **Operational Agent**：自主执行
- 预定义规则下 **99%** 成功执行率
- 能处理从流程挖掘中衍生的流程适应

> Source: [A modular LLM agent architecture for adaptive and autonomous process-aware execution](https://www.sciencedirect.com/science/article/pii/S0306437926000621), Information Systems, Vol.141, Oct-Nov 2026

### Agentic Orchestrations 分类框架

Rinderle-Ma 等人，按五个维度分类：任务特异性、可追踪性、可驾驭性、自主性、反应性、正确性保证。

> Source: [Design and Implementation of Agentic Orchestrations](https://browse-export.arxiv.org/abs/2606.31518), arXiv, Jun 2026

---

## 行业数据：BPM Pulse Survey 2026

BearingPoint & BPM&O，2026 年 3 月：

| 指标 | 比例 |
|------|------|
| 认为流程管理对业务关键 | **83%** |
| 已在 BPM 中使用生成式 AI | **42%** |
| 部署了自主操控流程的 AI agents | **16%** |
| 预计 Agentic BPM 成为核心能力 | 到 **2030** 年 |

**关键障碍**：数据质量不足、目标不清晰、能力缺失。组织正在从"AI 能工作吗？"转向"怎么让它规模化工作？"

> Source: [BPM Pulse Survey 2026](https://www.bearingpoint.com/zh-cn/insights-events/insights/bpm-pulse-survey-2026/), BearingPoint, Mar 2026

---

## 信任鸿沟

CHI 2026 论文：BPM 领域专家评估 LLM BPM 对话式建模 copilot (KICoPro)：
- 可用性：67.2/100（可接受）
- 信任度：**48.8%**（低）
- 可靠性被评为最关键的担忧

> Source: [Human-Centered Evaluation of an LLM-Based Process Modeling Copilot](https://ar5iv.labs.arxiv.org/html/2603.12895), CHI 2026

---

## 对"信息加工流"研究的启示

1. **"Framed Autonomy"是我们缺的那个术语。** 一直在说"流程不再被预定义但也不是没规则"——APM 社区给了它一个精确的名字。
2. **学术和工业在并行演进。** Camunda ProcessOS 的产品架构和 APM manifesto 的理论框架是同一件事的两个面。
3. **16% vs 42% 的 gap。** 42% 在 BPM 中用到了生成式 AI，但只有 16% 让 Agent 自主操控流程。这跟 SDLC 领域的情况一模一样：大家都在用 AI 辅助，但真正让 AI 自主执行还有距离。
4. **信任鸿沟是两边的共同瓶颈。** BPM 的 48.8% 信任度 ≈ SDLC 的 "你怎么知道 AI 验证得对不对？"
