---
title: 经典 BPM 场景 — 与 AI 时代的对比
date: 2026-07-08
source: web_search
type: reference
status: draft
---

# 经典 BPM 场景 — 与 AI 时代的对比

> 三个最经典的 BPM 场景，加上 AI 时代的变化。

---

## 场景 1：Procure-to-Pay（采购到付款）

**经典流程**：
```
需求识别 → 寻源/招标 → 供应商入驻 → 采购申请 → 采购订单 → 
收货校验 → 三单匹配（发票 vs PO vs 收货单） → 付款
```

**传统痛点**：审批在邮件里丢失、PO 发给不合格供应商、承诺支出不可见

**典型 ROI**：交易成本降 20-30%，采购申请到 PO 成本降 29%

**AI 时代的变化**：
- 三单匹配从"人比对"变成 AI OCR + 自动匹配——只把异常踢给人
- 供应商评估从"人打分"变成 AI 从多个数据源自动聚合风险信号
- Infosys 的 "touchless P2P" 已经能做到发票在几小时内完成 straight-through processing

> Source: [SAP Signavio: Business Process Management Examples](https://www.signavio.com/wiki/bpm/business-process-management-examples/)
> Source: [Infosys BPM: Touchless Procure-to-Pay](https://www.infosysbpm.com/blogs/finance-accounting/hands-free-hassle-free-with-touchless-procure-to-pay.html)

---

## 场景 2：Employee Onboarding（员工入职）

**经典流程**：
```
Offer 接受 → 
  HR：合同生成、政策确认、福利登记
  IT：系统账号开通、设备分配
  行政：工位分配、门禁卡
  薪酬：银行信息、税务表单
  直属领导：30/60/90天计划、buddy分配
```

**传统痛点**：新员工 Day 1 没电脑、没账号、没工位——各部门互不连通

**典型 ROI**：入职时间可预测、HR 从跟进中解放出来、新员工更快进入生产力状态

**AI 时代的变化**：
- Agent 自动触发多部门任务——不再依赖人手动发邮件
- IT 开通账号和分配设备可以完全自动化
- 飞书/钉钉里——新员工入职后 Agent 自动推送培训文档、拉进相关群聊、安排首周日程

---

## 场景 3：Invoice Processing（发票处理）

**经典流程**：
```
发票接收（PDF/纸质/EDI/邮件） → 智能数据提取（OCR/IDP） → 
三单匹配（发票 vs PO vs 收货单） → 异常人工处理 → 
审批路由 → 付款 → 对账
```

**传统痛点**：重复付款、错过早付折扣、周期长、审计噩梦

**典型 ROI**：发票处理生产力提升 28%，PO 采用率 92%

**AI 时代的变化**：
- 传统 OCR → LLM-based 的智能文档处理（IDP）——PDF、扫描件、Excel、邮件正文都能自动提取
- 异常处理从"人工查"变成 AI 建议 + 人确认
- 月结 6 万+ 文档完全数字化

> Source: [Kissflow: 10 Business Processes to Automate](https://kissflow.com/low-code/business-processes-automate-low-code/)

---

## 这三个场景的共同特征

| 特征 | 传统 BPM | AI 时代 |
|------|------|------|
| **数据格式** | 结构化表单 | 非结构化文档（PDF/Excel/邮件/聊天）——AI 直接处理 |
| **流程定义** | 预设路径，条件分支 | Agent 根据情况自主判断下一步 |
| **异常处理** | 踢给人工队列 | AI 建议 + 人快速确认 |
| **参与者** | 只有人 | 人 + AI Agent 混合 |
| **优化方式** | 基于历史数据的周期性回顾 | 实时监控 + 持续自动调优 |

---

## 这跟你说的"信息加工流"的关系

你说得对——传统 BPM 能处理的前提是**信息已经被结构化**。发票上的字段被 OCR 提取了、采购申请被填进表单了、入职信息被录入系统了。

AI 的 disruptive 之处在于：**它不需要信息先被结构化。** Excel、PDF、邮件正文、聊天记录、合同扫描件——AI 可以直接"读懂"并加工。这就是为什么飞书/钉钉的路线（处理各种 media 的协作流）在 AI 时代比传统 BPM（基于结构化流程引擎）更有想象力。

信息加工流的**加工层**不再要求输入是"干净的结构化数据"——这是 AI 带来的根本变化。
