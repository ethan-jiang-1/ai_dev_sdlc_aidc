---
type: evidence_archive
collected_by: delegated research pass（主代理复核既有 evidence；补核 Anthropic 与 DSPy 一手页面）
collected_at: 2026-09-30
serves: capability_ladder/branch-a-orchestration.md; capability_ladder/branch-b-meta-loop.md
status: 新增档案；不改既有阶档与判读文件
quality_bar: 一手工程博客/官方文档/官方源码或官方代码仓库；每条区分已运行实例、工具/配置局部改动、研究优化器结构、构想；数字保留原口径并标注，不作跨源效果结论
---

# 回源档案 X：两条高阶支线的可示范机制链（观测 2026-09-30）

## 0. 使用边界

本档只为两张机制卡提供可复用的原句/源码锚点，不改写 [00-map](../capability_ladder/00-map.md) 的阶位判定。组合链是教学拼接，不代表存在一个机构已经把所有部件做成同一产品。尤其要分开：

- **已运行实例**：来源明确说已经用于产品、内部系统或实际实验。
- **配置/工具描述改动**：只改外围件，不等于代理获得改写 evaluator、权限模型或核心 loop 的权力。
- **研究优化器结构**：可示范 proposal/evaluation/budget/lineage，但不作为 coding-agent harness 自改的运行实例。
- **构想/建议**：原文使用 *might / could / expect* 等未来式，只登记为方向。

访问/观测日期统一为 **2026-09-30**；发布日期按来源页面或既有档案元数据记录。

---

## 1. 支线 A：并行只读 → 隔离写入/合并 → 树级预算与取消

### A1. 并行只读研究：LeadResearcher → 独立上下文 Subagents → 汇总/引文

- **来源**：Anthropic，《How we built our multi-agent research system》；URL：<https://www.anthropic.com/engineering/multi-agent-research-system>
- **发布/观测日期**：2025-06-13 / 2026-09-30。
- **实例状态**：文章明确描述 Claude Research feature 的系统，并称其已用于 production；这是研究/检索域的已运行实例，不是编码并行写入实例。
- **机制原句**：
  > “Our Research feature involves an agent that plans a research process based on user queries, and then uses tools to create parallel agents that search for information simultaneously.”
  > “Subagents facilitate compression by operating in parallel with their own context windows, exploring different aspects of the question simultaneously before condensing the most important tokens for the lead research agent.”
  > “The lead agent … spawns subagents to explore different aspects simultaneously.”
- **边界与停止**：LeadResearcher 负责决定是否需要更多研究；结果进入 CitationAgent；并行子代理各自搜索、评估工具结果并返回 findings。作者还说明当前 lead 等待每批 subagents 完成，异步执行会增加结果协调、状态一致性和错误传播难度。不能把“并行读”外推为并行写入安全。
- **努力预算原句**：
  > “Simple fact-finding requires just 1 agent with 3-10 tool calls, direct comparisons might need 2-4 subagents with 10-15 calls each, and complex research might use more than 10 subagents with clearly divided responsibilities.”
  > “Early agents made errors like spawning 50 subagents for simple queries …”
- **谨慎数字**：上述是 Anthropic 对自身研究系统的 prompt 规则/失败回顾；不是行业默认值，也不是跨任务效果阈值。文章另报 internal research eval 与 token 倍数，本文不将其当 loop 设计因果效果。

### A2. 隔离并行写入/合并：每代理 clone + task lock + pull/merge/push

- **来源**：Nicholas Carlini（Anthropic），《Building a C compiler with a team of parallel Claudes》；URL：<https://www.anthropic.com/engineering/building-c-compiler>
- **发布/观测日期**：2026-02-05 / 2026-09-30。
- **实例状态**：作者明确称这是 “very early research prototype”；不是生产通用方案，也不是有独立 orchestrator 的成熟产品。
- **隔离与认领源码**：
  > “A new bare git repo is created, and for each agent, a Docker container is spun up with the repo mounted to `/upstream`. Each agent clones a local copy to `/workspace`, and when it's done, pushes from its own local container to upstream.”
  > “Claude takes a ‘lock’ on a task by writing a text file to `current_tasks/` … If two agents try to claim the same task, git's synchronization forces the second agent to pick a different one.”
- **合并链源码**：
  > “Claude works on the task, then pulls from upstream, merges changes from other agents, pushes its changes, and removes the lock. Merge conflicts are frequent, but Claude is smart enough to figure that out.”
- **拓扑边界**：
  > “I don't use an orchestration agent. Instead, I leave it up to each Claude agent to decide how to act.”
  因而它证明的是隔离 worktree/容器、文件锁认领、git 合并这一种可运行变体；不证明必须有 manager，也不证明写入单线程。作者还明确指出多个代理会在不可分任务上反复撞同一 bug，16 个代理不会自动增加收益。
- **验收边界**：
  > “it's important that the task verifier is nearly perfect, otherwise Claude will solve the wrong problem.”
  > “it is easy to see tests pass and assume the job is done, when this is rarely the case.”
  测试通过是该实例的工程闸门，不等于业务验收或通用效果证据。

### A3. 树级预算/取消：现有一手机制可拼成控制链，但未发现同一公开实例同时给出全树预算＋取消

**预算覆盖（研究系统的运行约束）**

- Anthropic A1 的 lead prompt 按任务复杂度设定子代理与 tool-call 规模，并记录“50 个子代理处理简单问题”的失控反例；这是**预算/分配规则**，不是统一 runtime token cap。
- IAL-Scan 论文（Hou 等），URL：<https://arxiv.org/html/2607.01641>；发布：2026-07；观测：2026-09-30。原句：
  > “An inner turn cap on a nested agent call does not cover an outer evaluator feedback cycle unless it dominates the outer feedback path.”
  > “Retry feedback without bounds, tool-call iteration without bounds, and multi-agent chat without turn bounds account for 47 findings (69.1%).”
  这支持“预算必须覆盖整棵实际反馈路径”，不支持一个跨系统统一数字；论文是静态分析，数字是其样本口径，不能当生产发生率。

**树级取消（OpenClaw Task Flow）**

- **来源**：OpenClaw 官方文档/源码仓库文档，URLs：
  - <https://raw.githubusercontent.com/openclaw/openclaw/main/docs/automation/tasks.md>
  - <https://raw.githubusercontent.com/openclaw/openclaw/main/docs/automation/taskflow.md>
  - <https://raw.githubusercontent.com/openclaw/openclaw/main/docs/cli/tasks.md>
- **发布/版本锚点/观测日期**：文档页无单独发布日期；既有回源记录的最近提交锚点为 tasks 2026-09-26、taskflow 2026-09-23、cli/tasks 2026-09-10；观测 2026-09-30。
- **任务账本原句**：
  > “Each task moves through `queued → running → terminal` (succeeded, failed, timed_out, cancelled, or lost).”
  > “`openclaw tasks list` shows all tasks” / “`openclaw tasks cancel <lookup>`”
- **Flow 取消源码**：
  > “A flow is a durable record of multi-step work with its own status, JSON state, revision counter, and linked task records.”
  > “Cancellation intent refuses new child links. The flow finalizes as cancelled once its active children have settled.”
- **边界**：这是公开的 detached-task/flow 状态与取消机制；它没有声明自己是 feature backlog，也没有统一的全树 token/dollar budget。`blocked` 在 task 文档中可特指结果投递受阻，不应直接翻译成执行中断。故教学链应写成：**根调度先设树级预算（数值由具体 runtime 设定）→ 子代理不得绕过外层 cap → cancel 拒绝新 child、等待已有 child 收敛 → terminal/cancelled 可观测**；“四件合一的成熟产品”目前没有一手证据。

### A 卡可示范最小链

`研究问题 → lead 拆分只读子任务 → 每个子代理独立上下文并行检索 → 汇总/引用`（Anthropic Research，已运行）

或在可分且可验证的写任务中：`根任务 → 每代理独立 clone/worktree → task lock 认领 → 修改 → pull/merge/push → 冲突处理/测试`（Carlini，研究原型）

再叠加控制层：`根预算覆盖 outer feedback path → 禁止预算外继续派生 → cancel 设置后拒绝新 child → active children settle → flow cancelled`（IAL-Scan 的覆盖判据＋OpenClaw 的取消语义，**跨源教学组合，不冒充单一已运行实例**）。

---

## 2. 支线 B：人改 harness → 代理提案 → 局部应用 → 独立评估/可回退

### B1. 人改 harness：从失败事件反应式改 controls

- **来源**：Kief Morris，URL：<https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html>；发布：2026-03-04；观测：2026-09-30。与 Birgitta Böckeler 同属 Thoughtworks，不能算两家独立机构票。
- **原句**：
  > “The ‘in the loop’ way is to fix the artefact … The ‘on the loop’ way is to change the harness that produced the artefact so it produces the results we want.”
  > “The next level is humans directing agents to manage and improve the harness rather than doing it by hand.”
- **Böckeler 的触发句**（URL：<https://martinfowler.com/articles/harness-engineering.html>；发布 2026-04-02；观测 2026-09-30）：
  > “The human's job in this is to steer the agent by iterating on the harness. Whenever an issue happens multiple times, the feedforward and feedback controls should be improved …”
- **边界**：这是“人如何改环境/规则”的机制与建议，不是代理已经获得 harness 写权限；同一 Thoughtworks 阵营不重复计票。

### B2. 代理提出修改：反思/分析角色提出 candidate，评估角色独立打分

- **方向性来源**：Sydney Runkle，LangChain，《The Art of Loop Engineering》；URL：<https://www.langchain.com/blog/the-art-of-loop-engineering>；发布：2026-06-16；观测：2026-09-30。
- **原句**：
  > “The hill climbing loop runs an analysis agent over those traces and uses the findings to rewrite the harness with improved configuration.”
  > “the return arrow doesn't just loop back to the top — it reaches inside and updates the agent loop directly.”
- **提案后自动放行是构想**：Morris 原句用的是条件式：
  > “As we gain confidence, the agents can assign scores to their recommendations, including the risks, costs, and benefits. We might then decide that recommendations with certain scores should be automatically approved and applied.”
  这不是已运行的自动批准证明。

### B3. 局部自动应用：实际是工具描述改动，不是 evaluator/core loop 自改

- **来源**：Anthropic，《How we built our multi-agent research system》；URL：<https://www.anthropic.com/engineering/multi-agent-research-system>；发布：2025-06-13；观测：2026-09-30。
- **已运行实例原句**：
  > “We even created a tool-testing agent—when given a flawed MCP tool, it attempts to use the tool and then rewrites the tool description to avoid failures.”
  > “This process for improving tool ergonomics resulted in a 40% decrease in task completion time for future agents using the new description …”
- **严格边界**：改动对象是 MCP **tool description** 这一外围配置；原文没有证明该 agent 能改 evaluator、权限策略、停止条件或核心 harness 结构。40% 是 Anthropic 自述的该内部流程结果，不能外推为 coding-agent harness 的通用效果或因果估计。

### B4. 独立评估、预算、候选谱系与可回退：DSPy GEPA 是结构实例，不是 coding-agent 自改实例

- **新增一手来源**：DSPy 官方文档《GEPA in depth》；URL：<https://dspy.ai/current/diving-deeper/gepa-in-depth/>；发布日期：页面未标注（living docs）；观测：2026-09-30。
- **角色分离原句**：
  > “Reflection is the proposal mechanism, not the evaluation mechanism.”
  > “Score evaluation runs through whatever LM the program is configured with (`task_model`). Two roles, two budgets …”
- **预算约束原句**：
  > “Only one of `auto`, `max_full_evals`, or `max_metric_calls` may be set.”
  > “`max_metric_calls` — raw cap Direct ceiling on metric invocations. Use this when you’ve measured per-call cost and want a hard dollar cap.”
- **独立候选与选择原句**：
  > “GEPA tracks every candidate it ever proposed, with per-example scores.”
  > “The frontier is for exploration; the aggregate is for selection.”
  > “`detailed_results` is the audit trail” and carries every candidate, every parent in the lineage, every per-example score, and when each candidate was discovered.
- **回退边界**：文档明确保留候选与 lineage，并返回 aggregate winner；这提供“保留旧 candidate、拒绝新 candidate、重新选择已记录 candidate”的回退基础，但没有把它描述成 coding harness 的自动 rollback 命令。不能把“有候选档案”写成“生产自改已安全”。
- **适用域边界**：GEPA 是 DSPy 的 reflection-driven instruction optimizer，面向程序/指令候选；它证明 proposal/evaluation 分离、预算和审计谱系可实现，不证明 coding-agent 能安全修改自身 evaluator 或核心 loop。

### B 卡可示范最小链

`人根据重复失败改 harness → 代理读取 trace 提出外围配置 candidate → 只在工具描述/提示等受限对象局部应用 → 独立 task/eval model 在验证集评估 → 保留 candidate + parent/score lineage → 不达标留用旧版本/回退`。

证据级别要拆开：前两步由 Morris/Böckeler/Runkle 提供“机制/构想”；工具描述局部改动由 Anthropic 提供**已运行实例**；最后的 proposal/evaluation/budget/lineage 由 DSPy GEPA 提供**优化器结构实例**。将四步拼成 coding-agent 核心 harness 自动自改，当前仍是教学构想，不能写成已验证通用机制。

---

## 3. 负结论与可用措辞

1. **并行不等于同一拓扑**：Anthropic 研究系统是 orchestrator-worker 的并行只读；Carlini 是无 orchestrator、独立 clone、文件锁和 git merge；Cognition 的单线程写入建议是另一种机构方案，三者不计为共同写入共识。
2. **取消不等于预算**：OpenClaw flow 有明确取消传播和 active-child 收敛；没有同时提供统一 token/dollar tree cap。IAL-Scan 只给“外层 cap 必须覆盖反馈路径”的分析判据。
3. **局部配置自改不等于 evaluator 自改**：Anthropic 的工具描述改写只证明外围件局部实例；GEPA/DSPy 的独立评估和 lineage 只证明优化器结构。不要把它们合并成“coding agent 已能安全改自己的评估器”。
4. **效果数字谨慎**：Anthropic 的 internal eval、token 倍数、40% 时间下降、Carlini 的成本/规模均保留来源自报口径；本档不将其当跨机构效果、采用率或因果证据。
5. **当前最稳妥的教学问句**：谁拆任务、谁拥有写入、谁合并、谁验收、预算覆盖哪条反馈路径、取消后哪些 child 仍会收敛、谁能把 harness 改动退回？
