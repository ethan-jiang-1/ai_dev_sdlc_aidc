---
type: evidence_record
category: graph_engineering
date: 2026-03-01
status: verified
evidence_level: S
source_channel: anthropic_official_research
participants:
  - Anthropic Applied AI Team
topics:
  - Workflows vs Autonomous Agents
  - 五大工作流拓扑模式 (Patterns)
  - Orchestrator-Workers 动态 DAG 拓扑
  - Evaluator-Optimizer 回路
---

# raw/evidence-202603-anthropic-workflow-patterns.md — 拓扑范式基石：Anthropic 五大 Agentic Workflow 模式

> **观测时间**：2026 年初  
> **数据源**：Anthropic 官方研究与工程指南《Building Effective Agents》

---

## 1. 核心理论立论：Workflows vs Autonomous Agents

Anthropic 在指南开头做出了影响全行业技术选型的论断：

> *“When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. In many cases, **Workflows (predictable, structured programmatic paths)** offer far more reliability and success than fully open-ended autonomous agents.”*

工业落地中，开发者应优先将任务抽象为**工作流图（Workflow Graph）**，将非确定性大模型嵌入确定性的代码拓扑中。

---

## 2. 五大经典拓扑架构模式

```text
1. Prompt Chaining:
   [Step 1] ───► [Step 2] ───► [Step 3]

2. Routing:
                 ┌──► [Worker A]
   [Router] ─────┼──► [Worker B]
                 └──► [Worker C]

3. Parallelization (Sectioning / Voting):
                 ┌──► [Worker A] ──┐
   [Dispatcher] ─┼──► [Worker B] ──┼──► [Aggregator]
                 └──► [Worker C] ──┘

4. Orchestrator-Workers:
   [Orchestrator] ◄───► [Dynamic Sub-task DAG] ───► [Workers Fan-out]

5. Evaluator-Optimizer:
   [Generator] ───► [Evaluator]
        ▲                │ (Fail / Refine)
        └────────────────┘
```

### 拓扑 1：Prompt Chaining（链式有向图）
- **特征**：最基础的线性有向无环图（Linear DAG）。前驱节点的输出直接作为后继节点的输入；中间插入确定性校验函数（Gate）。
- **适用场景**：翻译加校对、代码生成加格式化。

### 拓扑 2：Routing（分类路由图）
- **特征**：中央路由器根据输入特征将请求分流至专门节点；各分支具备专属提示词、工具集与模型选型。
- **适用场景**：用户意图分流、异常分类处理。

### 拓扑 3：Parallelization（并行扇出与汇聚图）
- **特征**：分两种形态：
  - **Sectioning（切片分治）**：大任务拆分，子节点独立并发执行后汇聚；
  - **Voting（一致性仲裁）**：多个独立节点生成不同方案，由评审节点做多数表决。
- **适用场景**：跨文件批量代码分析、多方案竞选设计。

### 拓扑 4：Orchestrator-Workers（编排者-工作者动态图）
- **特征**：编排器基于输入动态生成子任务依赖图（Sub-task DAG），派发专职 Worker 并行执行，并对交付物进行综合组装。
- **在 Graph Engineering 中的核心地位**：这是**软件工程中大型功能实现的标准图模型**。

### 拓扑 5：Evaluator-Optimizer（评估者-优化者循环图）
- **特征**：形成局部有向回路（Cycle）。一个节点负责生成，另一个节点负责基于标准（如单测、Lint、Schema）评估，未达标则带反馈回退重写。
- **与 Loop 的映射**：这正是节点内部微循环（L1 自愈）的拓扑表现。
