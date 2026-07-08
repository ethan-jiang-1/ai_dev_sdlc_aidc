---
title: Phase 0 — 素材抽取与合成
stage: phase_0
position: pre_phase
type: guide
summary: 从 KOL 源材料中提取关键信号，按主题组织，为叙事大纲提供素材基础。
depends_on: []
feeds_into:
  - v1/outline/outline-v1.md
agent_action: guide
---

# Phase 0: 素材抽取与合成

> 本阶段目标：不是把所有材料读一遍——而是**按叙事线索**提取关键信号，让 Phase 1 有据可依。

## 为什么需要这个阶段

标准 PPT 框架假设你已经有清晰的内容方向。但你的素材是 14 位 KOL + 3 场事件 + 跨公司共识——信息量巨大且互有关联。需要先做一轮结构化抽取，才能进入叙事设计。

## 输入

```
../aidlc_reference_kol/
├── _raw_kol/                          ← 14 位 KOL 深度拆解
├── _raw_frontier/                     ← 跨公司变革共识（7人）
├── _raw_fable5/                       ← Fable 5 变革信号
├── _raw_agile_manifesto_2026/         ← Deer Valley Retreat
├── _raw_promatic_summit_2026/         ← Pragmatic Summit
└── _raw_engelberg_2026/              ← Engelberg Retreat
```

## 产出

`source-synthesis.md`——按以下维度组织的信号图谱：

1. **共识区** — 哪些判断所有人/大多数人都同意？
2. **分歧区** — 哪些问题上存在根本分歧？
3. **已死/正在死的流程** — 哪些 SDLC 实践被宣布不再适用？
4. **新涌现的概念** — 哪些新术语/新框架在形成？（Harness Engineering、Cognitive Debt、Supervisory Engineering、Middle Loop...）
5. **关键引用** — 最有冲击力的原话（可进入 slides 作为 pull quote）
6. **数据点** — 可引用的量化证据

## 工作方式

- Agent 读取各源目录的 README（已有完整的索引和共识/分歧矩阵）
- 提取跨源重复出现的主题
- 标注每条信号的证据强度（单个 KOL 断言 vs 多人独立验证 vs 有数据支撑）
- 用户审核：哪条信号放错了？哪条漏了？

## ⛔ 闸门

Phase 0 完成标准：
- [ ] 六大维度（共识/分歧/已死流程/新概念/关键引用/数据点）均有内容
- [ ] 每条信号标注了来源文件路径
- [ ] 用户确认：核心信号的抽取准确、无重大遗漏
