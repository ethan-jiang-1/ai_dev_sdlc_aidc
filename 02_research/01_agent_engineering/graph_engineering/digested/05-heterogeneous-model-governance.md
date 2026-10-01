# 05. 异构模型拓扑分工与通信治理：汇报冲动、收敛性与配额约束

> **判读依据**：`raw/evidence-20261001-field-exchange.md`（Jarvan 日成实录：“2小时烧掉了一个 grok heavy”）。

---

## 1. 异构模型混部的必然性与现实痛点

在生产级 Graph Engineering 中，让所有节点都使用最昂贵的大模型（如 Claude Opus 5.5 或 OpenAI Sol-Reasoning）在财务上是不现实的。合理的图拓扑必然采用**异构模型梯次搭配（Heterogeneous Model Tiering）**：
- 顶层 Planner / Architect：选用高推理、强逻辑、善于长程任务分解的超大模型（Claude Opus 5.5 / OpenAI Sol-Reasoning）；
- 中层 Worker / Coder：选用编码执行力强、速度快的高收敛模型（Claude Sonnet 5 / OpenAI Sol-Coder / Gemini 6 Astra）；
- 叶子节点 Reviewer / Linter / Gate：选用轻量模型（OpenAI Sol-Mini / Claude 5 Haiku）或确定性规则函数。

然而，2026-10-01 的一线实录揭示了一个极具隐蔽性的工程深坑：

> **“只是不同模型的汇报策略不一致，比如 opus5.5 和 6 astra 不会频繁汇报沟通，但 grok4.7 就会。所以我用 grok 做子智能体，2小时烧掉了一个 grok heavy。”**

---

## 2. 异构模型的“性格特质”与自主性谱系

在多 Agent 协同网络中，不同模型展现出了截然不同的“沟通行为学特征”：

| 模型类型 / 代表 | 沟通与汇报行为特征 | 在拓扑中的利弊 | 适用节点岗位 |
|---|---|---|---|
| **高收敛自主闭环型**<br>(Claude Opus 5.5 / Sonnet 5, Gemini 6 Astra) | **“闷头干大事”**。倾向于在单次调用或局部微循环中彻底解决问题，直到完成所有单测才向上提交工件；极少发起无信息增量的中间闲聊。 | **利**：Token 效率极高，不打扰编排器；<br>**弊**：存在过度架构重构（Architectural Over-reach）倾向。 | Planner, 复杂架构设计, 核心业务算法编写 |
| **话痨汇报冲动型**<br>(Grok 4.7 等特定强化对话模型) | **“事事有回响、巨细靡遗”**。每修改一行代码、每跑通一个测试，都倾向于向编排器汇报一次进度，并反问“下一步我该做什么”。 | **利**：过程极度透明；<br>**弊**：在多 Agent 拓扑中引发频繁的 A2A 握手，瞬间榨干 Token 与 API 额度。 | 严格受限的一对一人工交互界面，**严禁作为自主子任务 Worker** |
| **严格单步指令执行型**<br>(OpenAI Sol-Mini, Claude 5 Haiku) | **“指哪打哪”**。输入什么就只改什么，不主动延伸逻辑，格式极其遵循 JSON Schema。 | **利**：速度快、成本极低、确定性高；<br>**弊**：无全局联想能力，不能自主补齐缺漏。 | 单元测试执行器, AST 转换, Lint 修复, 文档注释生成 |

---

## 3. 图工程通信治理协议（Communication Governance Protocol）

为了防止“话痨模型”拖垮系统性能与预算，Graph Engineering 必须在框架层强加硬性治理约束，绝不能寄希望于模型的 Prompt 自律：

```text
               [Worker 执行中产生中间思考/动作]
                               │
                               ▼
               ┌───────────────────────────────┐
               │    通信治理拦截层 (Governor)   │
               └───────────────┬───────────────┘
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
   [尝试发起对主控的主动汇报]             [产出最终强类型工件]
            │                                     │
   ┌────────────────────────┐                     │
   │ 是否属于致命异常/阻塞? │                     │
   └────────┬───────────────┘                     │
      No    │       │ Yes                         │
            ▼       └──────────────┐              │
     [静默拦截并丢弃]              ▼              ▼
     [记录至本地沙箱日志]   [允许向上通知状态机] [更新黑板状态]
```

### 核心治理机制：
1. **静默执行契约（Silent Execution Contract）**：
   - 在图协议的 System Prompt 与调度器规则中严禁 Worker 主动发送非阻塞性质的自然语言进度更新；
   - 规定 Worker 只有两种终局输出：**要么返回标准工件（Success），要么抛出失败异常（Failure Envelope）**；
2. **汇报频次节流阀（Chatter Throttling）**：
   - 状态机对每个节点施加通信频次上限（例如：单任务执行期间最多允许 1 次外部提问/澄清）；
   - 超出频次的自然语言消息直接在通信网关层被截断，不唤醒编排器；
3. **节点级 Token / 消耗预算熔断（Hard Budget Cap）**：
   - 在调度 Worker 时设置硬性的 Token 与时长熔断阈值（例如：该节点预算上限为 50,000 Token 或 10 分钟）；
   - 一旦触发预算红线，宿主环境直接 `SIGKILL` 终止 Worker 进程，判定该节点失败，触发 L2 编排自愈，彻底避免“2小时烧干额度”的悲剧。

---

## 4. 生产级拓扑的最佳模型配置矩阵

```text
[用户需求入口]
       │
       ▼
[Planner 节点] ─────────────► Claude Opus 5.5 / OpenAI Sol-Reasoning (顶层长程架构与全局任务分解)
       │
       ▼ (Task DAG)
┌──────┴────────────────────┐
▼                           ▼
[Backend Worker Node]       [Frontend Worker Node]
(Claude Sonnet 5)           (Gemini 6 Astra / OpenAI Sol-Coder)
       │                           │
       └─────────────┬─────────────┘
                     ▼ (Patches)
[Integration & Test Gate] ──► 确定性脚本 (pytest / tsc / ruff) + OpenAI Sol-Mini (快速语法修正)
                     │
                     ▼
[Security / Review Gate] ──► Claude 5 Haiku (规范与只读差异审查)
                     │
                     ▼
[HITL 人机终审] ────────────► 人类工程师 (Pull Request 页面审查)
```
