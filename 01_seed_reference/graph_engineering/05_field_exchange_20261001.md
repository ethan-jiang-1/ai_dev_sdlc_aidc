---
type: field_sample
content_type: chat_transcript
category: graph_engineering
date: 2026-10-01
participants:
  - Jarvan 日成 (Raven Agent A2A 协作层开发者)
  - Willis
  - 李奕晨 Ethan
topic: DAG 状态机 vs 多 Agent 聊天、分层重试、动态 DAG 重规划、Session 内外编排架构
---

# 05. 一线真实交流实录：DAG 状态机替代多 Agent 聊天与动态图自愈

> **观测时间**：2026-10-01 11:08 – 11:11 (UTC+8)  
> **数据形态**：技术社区真实一线工程实践对话截图  
> **关联项目**：[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)（其中的 A2A 协作层）

---

## 1. 原始对话转写

- **Jarvan 日成** *(引用 Willis: "多 agent 聊天还是个太贵的方案")*:  
  > “不，不能让多 Agent 聊天。我现在是让编排者生成一个 DAG 图，做合法校验，在执行过程中做有限重试和退避，Worker 修不了的让编排者改 DAG 再重试。”
- **Jarvan 日成**:  
  > “这样不是靠互相聊天推进任务，而是靠 DAG 状态机推进”
- **李奕晨 Ethan** *(引用「我现在是让编排者生成一个 DAG 图」)*:  
  > “话说做这个 DAG 图的有没有一些开源项目捏，最近在研究类似的场景。”
- **Willis** *(回复李奕晨)*:  
  > “DAG 的图是业务逻辑，类似于人岗位的对接关系”
- **Jarvan 日成**:  
  > “只是不同模型的汇报策略不一致，比如 opus5.5 和 6 astra 不会频繁汇报沟通，但 grok4.7 就会。所以我用 grok 做子智能体，2小时烧掉了一个 grok heavy”
- **李奕晨 Ethan**:  
  > “这个实践中，这个是做在 session 内的 tool，比如是主 Agent 和 sub Agent 用这种编排工具推进呢。还是做成了外部的逻辑呢？”
- **Jarvan 日成**:  
  > “可以看看 Raven Agent，其中的 A2A 协作层是我开发的”
- **李奕晨 Ethan** *(引用 Willis: "DAG 的图是业务逻辑，类似于人岗位的对接关系")*:  
  > “嗯，，我主要是在看，这些逻辑究竟是做在主 session 内还是 session 外”
- **Jarvan 日成**:  
  > `https://github.com/EverMind-AI/Raven`
- **Willis**:  
  > “他是多 agent 架构，不是主从”

---

## 2. 核心工程洞察提取（一线手感）

### ① 摒弃“自由聊天”，转向“DAG 状态机”
- **痛点**：多 Agent 纯文本会话（Chat/Debate 模式）上下文成本极高（Token 爆炸）、行为不可控、易陷入发散和死循环。
- **解法**：由编排者（Planner/Orchestrator）生成显式 **DAG 依赖图**，经由静态合法性校验（环路检测、依赖完整性、语法检查）后，交由 **DAG 状态机引擎** 严格推进，节点之间只传递确定性交付物，而非自由交谈。

### ② 两层分级自愈机制（Two-Tier Resilience）
这是 **Loop Engineering 与 Graph Engineering 最生动的接合范式**：
- **L1 局部自愈（Worker 节点层）**：Worker 节点在内部执行时做**有限重试和退避（Backoff & Retry）**，对应节点内部的微循环（Loop Engineering）；
- **L2 全局拓扑重排（编排者层）**：若 Worker 无法在局部解决问题，触发异常升级，由编排者**重新修改 DAG 结构（动态图重编排）**后再次尝试。

### ③ 语义本质：DAG 图是业务逻辑与岗位关系的映射
- 明确指出 DAG 不是纯机器管道，而是**业务逻辑与人类岗位分工、交接关系的程序化表达**。节点是岗位能力/专职智能体，边是工件交接协议。

### ④ 核心架构争议：Session 内 Tool vs Session 外 外部系统？
- **Session 内**：主 Agent 将 DAG 编排库作为 Tool 调用，在自身上下文内管理子任务。优点是调度灵活性高，缺点是主 Agent 上下文易受污染（Context Rot）。
- **Session 外**：由独立的外部状态机/工作流引擎（如 Python/Go 运行时或 DAG 调度器）驱动，每个 Agent 仅拥有独立的局部 Session。具有更强的确定性和工程隔离性。

### ⑤ 模型异构性与通信配额消耗
- 真实场景下不同模型自主策略差异巨大：Opus 5.5 / Gemini 6 Astra 具备更高自治和收敛性；部分模型（如 Grok 4.7）有极高汇报冲动，放任频繁沟通会导致 2 小时耗尽 heavy 额度。因此必须在图协议层约束汇报策略与通信频率。
