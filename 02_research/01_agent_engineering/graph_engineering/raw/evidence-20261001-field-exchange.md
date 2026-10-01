---
type: evidence_record
category: graph_engineering
date: 2026-10-01
status: verified
evidence_level: B
source_channel: developer_community_chat
participants:
  - Jarvan 日成 (Raven Agent A2A 开发者)
  - Willis (架构师/工程专家)
  - 李奕晨 Ethan (AI SDLC 实践者)
topics:
  - DAG 状态机替代多 Agent 聊天
  - 两层自愈体系 (Worker 局部重试 + 编排者改 DAG 重试)
  - 岗位对接同构映射
  - 异构模型汇报冲动差异与配额消耗
  - Session 内 Tool vs Session 外 外部系统架构权衡
---

# raw/evidence-20261001-field-exchange.md — 一线工程实录：DAG 状态机替代自由聊天与动态图自愈

> **观测时间**：2026-10-01 11:08 – 11:11 (UTC+8)  
> **数据源**：一线 AI 工程师技术研讨现场转写与开源代码锚点  
> **关联项目**：[`EverMind-AI/Raven`](https://github.com/EverMind-AI/Raven)

---

## 1. 逐字发言摘录与事实核查

### 事实段落 1：否定自由聊天，确立 DAG 状态机推进
- **Jarvan 日成**：
  > “不，不能让多 Agent 聊天。我现在是让编排者生成一个 DAG 图，做合法校验，在执行过程中做有限重试和退避，Worker 修不了的让编排者改 DAG 再重试。”
  > “这样不是靠互相聊天推进任务，而是靠 DAG 状态机推进”
- **核查判定**：
  - 一线已彻底放弃 AutoGen 早期那种“把所有角色放在同一个聊天室自由交谈”的做法。
  - 核心代际演进：**从「Chat-driven」演进为「State-Machine-driven」**。

### 事实段落 2：DAG 拓扑的业务本质是岗位分工
- **Willis**：
  > “DAG 的图是业务逻辑，类似于人岗位的对接关系”
- **核查判定**：
  - 揭示了图拓扑与现实人类工程组织的同构性：Node 对应岗位职责，Edge 对应工件交付与审查协议。

### 事实段落 3：模型异构性对图通信的影响（汇报冲动与 Token 消耗）
- **Jarvan 日成**：
  > “只是不同模型的汇报策略不一致，比如 opus5.5 和 6 astra 不会频繁汇报沟通，但 grok4.7 就会。所以我用 grok 做子智能体，2小时烧掉了一个 grok heavy”
- **核查判定**：
  - 异构模型在自主工作与频繁汇报（Chatter）的倾向不同：高自主度模型倾向于静默执行直至产出完整工件；低收敛性/多语模型倾向于频繁向上汇报，若无图协议限制会导致严重 Token 浪费与额度枯竭。

### 事实段落 4：Session 内外架构选择争议
- **李奕晨 Ethan**：
  > “这个实践中，这个是做在 session 内的 tool，比如是主 Agent 和 sub Agent 用这种编排工具推进呢。还是做成了外部的逻辑呢？”
  > “嗯，，我主要是在看，这些逻辑究竟是做在主 session 内还是 session 外”
- **Jarvan 日成**：
  > “可以看看 Raven Agent，其中的 A2A 协作层是我开发的……他是多 agent 架构，不是主从”
- **核查判定**：
  - 核心分歧点在于控制面（Control Plane）的位置：做在 LLM 的 Session 内会带来严重 Context Rot；做在 Session 外则能实现确定性高可靠治理。

---

## 2. 机制提炼与技术特征

1. **DAG 生成的静态合法性校验**：编排模型生成的 DAG JSON/YAML 必须经过静态代码校验（无环检测、前驱节点输入输出契约对齐、资源声明完整性），校验不通过直接拦截，不进入执行。
2. **两层自愈体系的职责切分**：
   - **L1 局部自愈（Loop）**：Worker 节点内通过 `pytest`/`tsc`/`lint` 门禁执行有限退避重试（3~5 次）。
   - **L2 全局拓扑自愈（Graph）**：Worker 彻底失败，向编排器报出结构化异常，编排器重新修改 DAG（增加拆解节点、更换备用路径、回退 Checkpoint）。
3. **通信治理必须作为图协议层（Graph Protocol）的必备组件**：不可依赖模型自觉，必须由拓扑引擎硬性节流（Throttling）。
