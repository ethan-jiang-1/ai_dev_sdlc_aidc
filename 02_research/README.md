# 02_research — 研究层 · 分析

**定位**：围绕主线（AI Coding 时代 SDLC 如何变化）的长期研究沉淀。
包含四大支柱：**智能体机制工程**、**AI-Native SDLC 与组织**、**需求与规格工程**、以及**企业侧镜像与案例**。

补素材 / 改结论前先确认是否为某场 talk 服务——**是 → 走该 talk 的 `02_evidence/`，不在根级研究层改**。

## 顶层结构

```text
02_research/
├── 01_agent_engineering/         运行时与控制机制（Loop, Harness, Graph, Goal/Eval, 评估系统）
├── 02_ai_sdlc/                   生命周期、研发演进、业界实践与组织管理
├── 03_requirement_engineering/   输入端需求工程与可验证规格理论沉淀
└── 04_enterprise_mirror/         企业信息流等价物（BPM）与真实转型案例（2026-10-01 归入）
```

## 主题一览

### 1. 01_agent_engineering（智能体工程）
详见 [`01_agent_engineering/README.md`](01_agent_engineering/README.md)。

| 主题 | 核心维度 | 讲什么 | 入口 |
|---|---|---|---|
| `loop_engineering/` | 时间 / 迭代 | Loop Engineering 运动（**活跃**）：命名谱系、KOL 实战、构件、停止条件、外层调度与自主度分档 | `raw/kol-roster.md` + `digested/README.md` |
| `harness_engineering/` | 空间 / 环境 | 环境治理：约束写进环境、规则机器级阻断、沙箱与上下文注入 | `README.md` |
| `graph_engineering/` | 拓扑 / 状态机 | 拓扑编排：DAG 编排、多步骤分支与合并、多智能体协同机制 | `README.md` |
| `goal_eval_engineering/` | 目标 / 驱动 | 目标与评估（**活跃**）：如何构造 goal 与 eval 让 loop 跑起来并量化调优 | `README.md` §1 + `CURRENT.md` |
| `repo_agent_friendliness/` | 成熟度 / 评估 | 仓库 Agent-Friendly **评估系统**（**活跃**）：九维框架 + 门禁打分规范与工具 | `README.md`（体系权威 `10-spec/framework.md`） |

### 2. 02_ai_sdlc（AI 软件研发范式与生命周期）
详见 [`02_ai_sdlc/README.md`](02_ai_sdlc/README.md)。

| 模块 | 子目录 | 讲什么 | 入口 |
|---|---|---|---|
| **01_evolution/** | `paradigm_evolution/` | AI-Coding 范式变迁主报告（多轮 wave 迭代） | `result_4_v5/` |
| | `agile_to_native/` | 从瀑布 / 敏捷到 AI-Native 研发的范式跃迁 | `result/AI_Native_Agile_Evolution.md` |
| **02_industry_playbooks/** | `anthropic/` | Anthropic 官方 AI-Native SDLC Playbook（英译原文 + 中文编译） | `org/ai-native-sdlc-playbook.md` |
| | `thoughtworks/` | ThoughtWorks 方法论视角的 AI-Native SDLC 深度工程报告 | `final/AI_NATIVE_SDLC_FINAL_ENGINEER_REPORT.md` |
| | `frontier_interviews/` | 前沿议题：OpenAI、Anthropic、Cursor 等一线人物访谈与分析 | `followup_research/` |
| **03_org_and_management/** | `teams/` | 智能体团队形态（Agent Teams PPT 成稿，人类与 Agent 协同模式） | `result/agent_teams_ppt.md` |
| | `management/` | Agentic 管理侧景观（效能度量与治理考量） | `raw/` |

### 3. 03_requirement_engineering（需求与规格工程）
详见 [`03_requirement_engineering/README.md`](03_requirement_engineering/README.md)。
- 沉淀 AI 时代输入端意图表达、形式化规格、契约设计与需求工程演进。
- 与下游实践层 [`../03_practice/requirements_engineering/`](../03_practice/requirements_engineering/final/00-reading-guide.md) 呼应。

### 4. 04_enterprise_mirror（企业侧镜像与案例）
详见 [`04_enterprise_mirror/README.md`](04_enterprise_mirror/README.md)。
- 探讨 SDLC 在企业非代码信息流中的等价物（BPM、Agentic BPM、Framed Autonomy）。
- 收录真实企业重构案例（Block、Cloudflare、捷普制造）。（沉淀状态）

---

## 历史架构调整记录

- **2026-09-21**：实践性主题（`requirements_engineering/`、`spec_driven_development/`）拆出至 `03_practice/`。
- **2026-09-27**：修复同名错写目录（`anthorpic_ai_sdlc` 合并至 `anthropic`，`rnd_native_2.0` 合并至 `ai_native_rnd`）。
- **2026-10-01**：全面重构收敛：散碎研究主题收拢为前沿机制、SDLC 与需求工程三大主干；原根目录 `02_research/04_enterprise_mirror/` 降维归入本层为 `04_enterprise_mirror/`。

## 纪律

一手源优先、来源可溯、标注观测日期（与 `01_seed_reference/`、`03_practice/` 统一）。
