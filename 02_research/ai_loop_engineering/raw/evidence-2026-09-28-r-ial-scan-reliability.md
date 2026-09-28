# evidence-r — IAL-Scan & ReliabilityBench 两篇论文

> 路别：r（研究论文）  
> 观测日期：2026-09-28  
> 回源代理：主代理（Antigravity）  
> 承重引文标注：见各条  

---

## 来源清单

| # | 类型 | 来源 | 发布日期 | 强度 |
|---|---|---|---|---|
| S1 | 论文·arxiv | "When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents" (Hou et al.) | 2026-07 | 一手·已复核摘要+HTML全文 |
| S2 | 论文·arxiv | "ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions" (Gupta) | 2026-01 | 一手·已复核摘要+HTML全文 |
| S3 | 官方文档 | OpenHands Stuck Detector（openhands.dev） | 2026（观测日期） | 一手·已复核搜索摘要；原文页面 timeout |
| S4 | 官方博客 | Augment Code · CIV 模式（augmentcode.com） | 2026（观测日期） | 一手·转述级（博客搜索摘要，未取原页全文） |

---

## S1 · IAL-Scan 论文（arXiv:2607.01641，2026-07）

### 核心摘要（逐字）

> "LLM agents increasingly rely on iterative execution to solve tasks through planning, tool use, state updates, and agent collaboration. While this design enables flexible automation, it also creates a new class of failures: an agent may repeatedly execute model calls, tools, workflow transitions, or agent handoffs when the feedback path is not effectively bounded. We call this problem Infinite Agentic Loops (IALs). IALs are not ordinary programming loops; they arise from the interaction between agent logic, framework semantics, runtime observations, and termination mechanisms. Such failures can amplify a single request into long running model and tool execution, causing cost exhaustion, model denial of service, context growth, and repeated external side effects."

### IAL 定义（逐字）

> "We define an Infinite Agentic Loop (IAL) failure as a structural execution failure where an agentic feedback path repeatedly triggers costly or state-growing actions without an effective stopping bound. An IAL is not merely a loop; it arises when model outputs, tool results, external observations, or delegation decisions can keep the path active, while no strong bound covers it."

### 核心区分：effective bound vs. bound existence（逐字）

> "These mechanisms do not eliminate IAL risks in practice. Developers may omit them, misuse them, configure them with ineffective bounds, or place them outside the actual feedback path."
>
> "Detection must check whether a bound constrains the controller or a scope that covers the feedback path, rather than merely checking whether a limit or exit condition appears near the loop."

### 威胁模型（关键段落）

> "Execution safeguards such as iteration limits, retry caps, timeouts, recursion limits, human approval checks, or policy gates may be missing, ineffective, disabled, or only partially applied to the repeated feedback path."
>
> "An attacker or untrusted user can interact with the agent through normal inputs, such as prompts, task requests, documents, URLs, issue reports, tickets, workflow parameters, or API calls. The attacker may craft inputs that influence model outputs, tool arguments, retrieved content, external observations, or error conditions, causing the agent to repeat tool calls, retries, polling, sub-agent invocations, or workflow transitions."

### 真实世界发现数字（逐字）

> "We evaluate IAL-Scan on 6,549 LLM agent repositories. It reports 74 potential findings, among which manual review confirms 68 IAL failures across 47 projects, achieving 91.9% precision."
>
> "LangGraph and AutoGen contribute 45 of the 68 confirmed findings (66.2%) across 31 projects."
>
> "Retry feedback without bounds, tool-call iteration without bounds, and multi-agent chat without turn bounds account for 47 findings (69.1%)."
>
> "The dominant impacts are API cost exhaustion and model denial of service, each appearing in 95.6% findings."

### IAL 四类来源（原文归纳）

来自论文 §V-B1（Overall Result）：
- **retry feedback without bounds**（重试无限上限）
- **tool-call iteration without bounds**（工具调用迭代无上限）
- **multi-agent chat without turn bounds**（多智能体对话无轮次上限）
- model-output-controlled continuation（模型输出控制续行，无确定性退出）

### 框架覆盖（逐字）

> "IAL-Scan currently supports the analysis of downstream agent projects built with eight frameworks: LangChain, LangGraph, CrewAI, AutoGen, LlamaIndex, the OpenAI Agents SDK, Google ADK, and Semantic Kernel."

### 关键工程洞察：bound outside feedback path（逐字）

> "An inner turn cap on a nested agent call does not cover an outer evaluator feedback cycle unless it dominates the outer feedback path."

### BoundStatus schema（原文代码）

```
BoundStatus:
  Covered:
    verified_bound | framework_default_bound
    | config_dependent_bound
  UncoveredOrWeak:
    missing_bound | weak_bound | disabled_bound
    | ineffective_bound | bypassed_bound
```

**最小主张**：
1. IAL（无限智能体循环）是真实的、跨框架的工程失败类型，在 6,549 个公开仓库中发现 68 个确认失败
2. 框架自带的上限机制（LangGraph/LangChain/CrewAI/AutoGen 等）存在但不足以消除 IAL 风险——问题在于 effective bound coverage，不在于 bound 是否存在
3. bound 必须覆盖实际的 feedback path，放在路径外面无效
4. 最常见三类：重试无限、工具迭代无限、多智能体对话无轮次限制（合计 69.1%）

**不支持什么**：不给出各框架在真实项目中的 IAL 发生率；不评估 IAL 造成的实际财务损失；不提供 runtime 检测方案（只有 static analysis）

---

## S2 · ReliabilityBench 论文（arXiv:2601.06112，2026-01）

### 核心摘要（逐字）

> "Existing benchmarks for tool-using LLM agents primarily report single-run success rates and miss reliability properties required in production. We introduce ReliabilityBench, a benchmark for evaluating agent reliability across three dimensions: (i) consistency under repeated execution using pass^k, (ii) robustness to semantically equivalent task perturbations at intensity ε, and (iii) fault tolerance under controlled tool/API failures at intensity λ."

### 关键数字（逐字）

> "Perturbations alone reduce success from 96.9% at ε=0 to 88.1% at ε=0.2."
>
> "Rate limiting is the most damaging fault in ablations."
>
> "ReAct is more robust than Reflexion under combined stress."
>
> "Gemini 2.0 Flash achieves comparable reliability to GPT-4o at much lower cost."

### Action Metamorphic Relations 定义（逐字）

> "Unlike traditional metamorphic testing where output equivalence is textual, agent tasks require end-state equivalence."
>
> "An Action-MR is a tuple (φ,ψ) where: φ:D→D transforms task descriptions; ψ:S→S specifies expected state relationship. For most cases, ψ is identity: v(Sf, S0) = v(Sf', S0)."

### State-Based Verification（逐字代码）

```python
# 确定性 state-based oracle 示例
reservations[flight_id].status == "confirmed"
reservations[flight_id].passenger == expected_passenger
```

> "Unlike benchmarks that rely on LLM judges or text matching, ReliabilityBench uses deterministic state-based oracles."

### Fault Injection 配置（逐字代码）

```python
LAMBDA_PROFILES = {
    0.0: {"failure_rate": 0.0},          # Baseline
    0.1: {"failure_rate": 0.075, "faults": [TransientTimeout, HighLatency]},
    0.2: {"failure_rate": 0.175, "faults": [+ RateLimit, PartialResponse]},
    0.3: {"failure_rate": 0.275, "faults": [+ Cascading, SchemaDrift]}
}
```

### 关键发现（逐字）

> "pass@1 overestimates reliability by 20-40%"
>
> "Multiply benchmarks by reliability factor: If a benchmark reports 90% accuracy, expect 70-80% in production when accounting for consistency and faults."
>
> "Rate limiting causes largest degradation: 2.5% below mixed baseline, suggesting agents struggle with backoff and retry logic for rate-limited APIs."
>
> "Transient timeouts well-handled: 98.75% pass rate indicates robust retry mechanisms for temporary failures."
>
> "The degradation gradient ∂R/∂λ is steeper for Reflexion (−0.50 per 0.1 λ) than ReAct (−0.38), indicating that self-reflection mechanisms may amplify rather than mitigate fault impacts."

### 对 stop conditions 的最小主张

1. **rate limit 是最大杀手**：比 transient timeout 更具破坏力，因为 agent 不知道该等多久还是放弃
2. **pass@1 虚高**：生产可靠性需要乘以修正因子（0.7-0.8）
3. **simpler is more robust**：Reflexion 的 self-reflection 机制在故障下放大失败（梯度更陡）——这是对复杂自判逻辑的结构性质疑
4. **end-state verification**（确定性 state-based oracle）是衡量 agent 完成的正确方法，不是 text matching

**不支持什么**：1,280 episodes 在 4 个人工设计的 domain 内；不覆盖 coding domain；rate limit 结论是 ablation 设定的，不是真实生产环境测量

---

## S3 · OpenHands Stuck Detector（2026 观测）

### 五类检测模式（转述级，来源：openhands.dev 搜索摘要）

⚠️ **转述级**：原文页面 timeout，以下来自搜索摘要转述，不能计为已复核引文

1. **Repeating Action-Observation Cycles**：相同动作+相同观察 ≥4 次触发
2. **Repeating Action-Error Cycles**：相同动作+相同错误 ≥3 次触发
3. **Agent Monologue**：≥3 条连续消息无用户输入/无实质进展触发
4. **Alternating Patterns**：两种不同 action-observation 对交替 ≥6 轮触发
5. **Context Window Errors**：重复上下文窗口错误触发

检测基于**语义内容**（工具名+参数），不是对象同一性或时间戳。默认开启（`stuck_detection=True`）。

**最小主张**：OpenHands 把重复模式检测（非资源上限）做成默认开启的独立构件，有五类具体阈值——比已有的"重复检测"记录更完整

---

## S4 · Augment Code CIV 模式（2026 观测）

### Coordinator-Implementor-Verifier 三角（转述级）

⚠️ **转述级**：来自搜索摘要，未取博客原文逐字

核心结构：
- **Coordinator**：拆解任务
- **Implementor**：写代码/生成测试
- **Verifier**：独立验证——**不是**同一个 agent 自验

关键概念：
- **oracle risk**：写代码和验证同一个 agent 做，会产生关联错误（correlated errors）
- **advisory mode → hard gate 升级路径**：先在 advisory 模式（不阻断，只评论）观察 false-approve rate，校准 specs 后，升级到 hard gate（阻断）
- **living spec**：Verifier 对照 living spec 而非 agent 自报验收

**最小主张**：Augment Code 把 oracle risk 命名（"写和验不能是同一个 agent"），并给出 advisory→hard gate 的渐进部署路径——③号点新增机构级实战做法

---

## 负结论与缺口

- S1（IAL-Scan）只做 static analysis，不检测运行时 semantic 无进展（这是 OpenHands stuck detector 的域）
- S2（ReliabilityBench）的 rate limit 结论依赖注入设定，不能直接外推到 hard caps 的设计
- S3（OpenHands Stuck Detector）五类阈值（4/3/3/6 次）的实验依据未公开
- S4（Augment CIV）advisory mode 的 "false-approve rate" 阈值不明，hard gate 升级标准不公开

---

## 与已有 evidence 的关联

- IAL-Scan 的 "effective bound coverage" 区分 → 补强 ② insights #8（上限被省略）和 insights #13（缺省无共识）
- IAL-Scan 的四类 IAL 类型 → 给 ② "失控四件套" 提供学术侧的类型学对照
- ReliabilityBench 的 end-state oracle → 补强 ① "环境 ground truth" 的跨域证据；补强 ③ "裁判输出契约" 
- OpenHands 五类模式 → 补强 ② #7（重复模式检测，比拒绝计数更细）
- Augment CIV → 补强 ③ practices（五极裁判权的新一极：multi-agent verifier 形态）
