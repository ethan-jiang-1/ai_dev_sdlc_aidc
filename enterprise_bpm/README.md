---
title: Enterprise BPM — 企业信息加工流的 AI 时代变革
stage: root
type: index
summary: 知识地图入口。核心发现：BPM = 企业侧 SDLC 等价物，Agentic BPM 范式核心是 Framed Autonomy，与 SDLC 的 AI Sandwich 完全同构。
---

# Enterprise BPM — 知识地图

> 给 AI/Agent 的导航入口。按图索骥：看目录结构 → 找对应文件夹 → 读文件 frontmatter → 深入内容。

## 这个目录在研究什么

**软件有 SDLC 体系化管理信息加工流。企业的办公/业务信息处理（文档、邮件、工单、审批、招投标…）有等价的方法论吗？** 答案：有，叫 BPM（Business Process Management）。AI 时代，BPM 正在变成 Agentic BPM——核心是 **Framed Autonomy**（有框的自主）。这与 SDLC 的 "AI Sandwich"（人在两端、AI 在中间）完全同构。

## 目录结构

```
enterprise_bpm/
│
├── README.md                                          ← 你在这里（知识地图入口）
│
├── comprehensive-findings-enterprise-info-flow-and-sdlc.md  ← 综合判断：企业信息流 × SDLC 的完全同构
├── exploration-trajectory.md                          ← 7 轮探索全过程（每轮搜了什么、发现了什么、为什么转向）
│
├── papers/                                            ← 关键学术论文（3 篇）
│   ├── README.md                                      ← 三篇论文索引 + 引用策略
│   ├── apm-manifesto/                                 ← ⭐⭐⭐ 主引用：Agentic BPM 研究 Manifesto
│   ├── abpms-architecture/                            ← ⭐⭐ 辅助：A-BPMS 五层架构
│   └── apm-formal-foundations/                        ← ⭐⭐ 辅助：APM 形式化数学基础
│
└── findings/                                          ← 研究发现（按主题维度组织）
    ├── README.md                                      ← findings 子索引
    │
    ├── bpm-and-sdlc-equivalence/                      ← BPM = SDLC 等价物
    │   ├── bpm-is-the-sdlc-equivalent.md              ← 核心论证：BPM 就是企业信息加工的 SDLC
    │   ├── four-layer-architecture.md                 ← 四层架构全景图（前端/中端/后端/治理）
    │   └── agentic-bpm-academic-landscape.md          ← 学术圈：APM manifesto、BPM Pulse Survey、信任鸿沟
    │
    ├── terminology-and-taxonomy/                      ← 品类命名与分类
    │   └── what-is-this-called.md                     ← Agentic Orchestration/APM/APO/BPM 3.0：术语收敛
    │
    ├── agentic-orchestration/                         ← Agentic 编排层（中端）
    │   ├── camunda-processos-deep-dive.md             ← Camunda ProcessOS：AI-native BPM 标本
    │   ├── agent-control-plane-cowork-frontier.md     ← Anthropic Cowork + OpenAI Frontier：Agent 控制平面
    │   ├── ai-native-startups-vs-legacy-vendors.md    ← 大厂 vs 模型公司 vs AI-native 创业公司
    │   └── framed-autonomy-in-practice.md             ← Framed Autonomy 从理论到工程实现
    │
    ├── office-and-collaboration-tools/                ← 办公与协作工具（前端）
    │   ├── office-becomes-agent-platform.md           ← MS/Google/腾讯：Office 套件→Agent 运行基础设施
    │   ├── feishu-dingtalk-not-bpm-but-cwm.md         ← 飞书/钉钉/企微：不是 BPM，是协同办公 (CWM)
    │   ├── feishu-cli-for-ai-agents.md                ← 飞书 CLI 开源：让 AI Agent 调用办公能力
    │   └── dingtalk-wukong-agent-os.md                ← 钉钉悟空：GUI→CLI 完整重构的 Agent OS
    │
    ├── classic-bpm/                                   ← 经典 BPM 场景（后端）
    │   └── classic-bpm-scenarios-and-ai-change.md     ← P2P/Onboarding/Invoice Processing + AI 冲击
    │
    ├── enterprise-case-studies/                       ← 企业落地案例
    │   └── real-enterprise-ai-deployments-2026.md     ← Cognizant/GE/奇瑞/COS 等：有名字有数据
    │
    ├── product-landscape/                             ← 产品全景
    │   └── 2026-enterprise-ai-agent-products.md       ← 全球 + 中国 AI Agent 产品地图
    │
    └── agent-governance/                              ← Agent 治理
        └── agent-governance-patterns.md               ← 权限预提交、审计追踪、熔断、Agent Rewind
```

## 快速导航：想看什么 → 打开哪个文件

| 你想知道... | 打开 |
|------------|------|
| BPM 是什么？跟 SDLC 什么关系？ | `findings/bpm-and-sdlc-equivalence/bpm-is-the-sdlc-equivalent.md` |
| 新范式叫什么？核心概念是什么？ | `papers/apm-manifesto/apm_manifesto.md`（Framed Autonomy） |
| 四层架构全景图（跟 SDLC 怎么对应） | `findings/bpm-and-sdlc-equivalence/four-layer-architecture.md` |
| 那些不同的术语（APM/APO/Agentic BPM）是一个东西吗？ | `findings/terminology-and-taxonomy/what-is-this-called.md` |
| Camunda ProcessOS 架构详解 | `findings/agentic-orchestration/camunda-processos-deep-dive.md` |
| Office 套件怎么变成 Agent 平台？ | `findings/office-and-collaboration-tools/office-becomes-agent-platform.md` |
| 飞书/钉钉到底是什么？跟 BPM 什么关系？ | `findings/office-and-collaboration-tools/feishu-dingtalk-not-bpm-but-cwm.md` |
| 有哪些真实企业案例？ | `findings/enterprise-case-studies/real-enterprise-ai-deployments-2026.md` |
| 学术论文引用哪篇？ | `papers/apm-manifesto/`（主引用源） |
| 这 7 轮研究怎么走过来的？ | `exploration-trajectory.md` |
| 综合判断是什么？ | `comprehensive-findings-enterprise-info-flow-and-sdlc.md` |
