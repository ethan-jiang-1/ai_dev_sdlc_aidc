---
type: concept_deep_dive
event: FOSE Europe (Engelberg)
concept: Risk Tiering for AI-Generated Changes
date: 2026-07
verification_status: verified
source_urls:
  - https://ubos.tech/news/thoughtworks-future-of-software-development-retreat-highlights-ais-transformative-role/
  - https://www.metasticworld.com/en/insights/thoughtworks-future-of-software-development-retreat-2026
  - https://overwatering.org/blog/2026/07/notes-from-fose-europe/
key_concepts:
  - risk_tiering
  - auto_merge_low_risk
  - human_review_high_risk
  - blast_radius
  - dependency_depth
---

# Risk Tiering — AI 生成变更的分级治理

> 来源：[UBOS.tech 总结](https://ubos.tech/news/thoughtworks-future-of-software-development-retreat-highlights-ais-transformative-role/) · [Metastic World](https://www.metasticworld.com/en/insights/thoughtworks-future-of-software-development-retreat-2026) · [Giles Edwards-Alexander](https://overwatering.org/blog/2026/07/notes-from-fose-europe/)

---

## 为什么需要 Risk Tiering

当 Agent 每天产生数十个 PR 时，人类不可能 review 所有变更。但也不是所有变更都需要 review。

Engelberg 浮现的共识：**不是所有代码承担同等风险。** 对 AI 生成的变更进行风险分级——低风险自动合，高风险人工审。

这直接呼应了 Ryan Lopopolo 的合并哲学：*"修复成本低，等待成本高→少阻塞门。"* Engelberg 把它系统化了。

---

## 三级风险分类

| 级别 | 标准 | 处理方式 |
|---|---|---|
| **低风险** | 纯增量 leaf node 功能、UI 文案调整、文档更新、已知模式的重复代码 | **自动合并**（linter + 测试通过即可） |
| **中风险** | 修改已有 API 合约、跨模块变更、涉及业务逻辑、schema 变更 | **Agent review + 人工抽查** |
| **高风险** | 数据模型变更、权限边界修改、跨服务协议变更、安全敏感代码 | **强制人工 review** |

---

## 风险判断的维度

- **复杂度**：变更涉及多少文件、多少模块？
- **依赖深度**：被多少下游模块依赖？（Erik Schluntz 的 Leaf Node 反向指标）
- **历史缺陷率**：这个区域以前出过多少次 bug？
- **影响半径**："如果这段代码错了，爆炸半径多大？"（Deer Valley 的原问题）

---

## 与 Deer Valley 的呼应

Deer Valley 问了 **"如果这段代码错了，爆炸半径多大？"** Engelberg 把它变成了**可操作的分类系统**。

这也是 Supervisory Engineering（Middle Loop）的核心活动之一：**校准信任**——知道什么时候该信任 Agent、什么时候该人工介入。

---

## 关键引用

> *"Classify AI-generated changes into low/medium/high risk based on complexity, dependency depth, and historical defect rates. Auto-merge low-risk; human review for high-risk."* — Engelberg 共识
