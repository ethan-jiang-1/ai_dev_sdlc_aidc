---
title: Findings — 目录说明
date: 2026-07-08
type: index
---

# Findings 目录

按**四层架构模型**组织。放新文件时，问自己：这个内容属于哪一层？

```
findings/
├── README.md                                    ← 你在这里
│
├── front-end/                                   ← 前端：Agent 运行的基础设施
│   │                                              （身份、邮箱、日历、协作频道）
│   ├── office-workspace-agent-platform.md       ← MS/Google/腾讯 Office→Agent 平台
│   ├── feishu-dingtalk-vs-bpm.md                ← CWM（协同办公）vs BPM 定位
│   ├── feishu-cli-architecture-deep-dive.md     ← 飞书"龙虾"架构 + CLI 化
│   └── dingtalk-wukong-architecture.md          ← 钉钉悟空 Agent OS
│
├── orchestration/                               ← 中端：工作流怎么编排
│   │                                              （确定性骨架 + Agentic 自主）
│   ├── camunda-processos-deep-dive.md           ← Camunda ProcessOS 深挖
│   ├── agent-control-plane-cowork-frontier.md   ← Agent 控制平面（Anthropic/OpenAI）
│   ├── ai-native-startups-vs-legacy.md          ← 大厂 vs 模型公司 vs 创业
│   └── framed-autonomy-implementation.md        ← Framed Autonomy 工程实现（Round 9）
│
├── backend/                                     ← 后端：记录系统
│   │                                              （CRM/ERP/HCM/传统 BPM）
│   └── classic-bpm-scenarios.md                 ← 经典 BPM 场景 + AI 变化
│
├── governance/                                  ← 治理层（横切所有层）
│   │                                              （身份、权限、审计、熔断）
│   └── agent-governance-patterns.md             ← Agent 治理模式（Round 9）
│
├── methodology/                                 ← 方法论/理论（横切所有层）
│   ├── bpm-the-sdlc-equivalent.md               ← BPM = SDLC 等价物（含 ServiceNow Blueprint）
│   ├── agentic-bpm-academic-landscape.md        ← 学术圈：Agentic BPM manifesto
│   └── four-layer-architecture.md               ← 四层架构全景图 + SDLC 同构对照
│
├── taxonomy/                                    ← 分类体系（横切所有层）
│   └── classification-and-terminology.md        ← 品类名/厂商分类/成熟度/术语收敛
│
├── landscape/                                   ← 全景扫描（横切所有层）
│   └── 2026-enterprise-ai-agents-landscape.md   ← 2026 全球 + 中国产品全景
│
└── cases/                                       ← 实证
    └── real-enterprise-deployments-2026.md      ← 真实案例（有名字有数据）
```

## 放新文件的规则

| 新内容属于… | 放哪里 |
|-----------|--------|
| Agent 的"家"——Office/Workspace/协同办公/CLI 化 | `front-end/` |
| 工作流编排——流程引擎/Agent 控制平面/Framed Autonomy | `orchestration/` |
| Agent 治理——身份/权限/审计/熔断 | `governance/` |
| 记录系统——传统 BPM/ERP/CRM 的 AI 化 | `backend/` |
| 方法论/理论——跨层分析、学术回应、架构总图 | `methodology/` |
| 命名/分类/成熟度模型 | `taxonomy/` |
| 全景扫描/市场格局 | `landscape/` |
| 真实部署案例/数据 | `cases/` |
