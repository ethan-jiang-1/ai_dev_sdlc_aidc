# arxiv — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

## Source 7 · Sanderson Macedo《Stop Hand-Holding Your Coding Agent: Engineering the Loops that Replace Step-by-Step Prompting》（arXiv:2607.00038，2026-06-28 v1）

- URL：https://arxiv.org/abs/2607.00038 ｜ HTML：https://arxiv.org/html/2607.00038v1（摘要＋HTML 关键节实取核对）
- 来源类型：arXiv 预印本（cs.SE，单作者，CC BY 4.0；非同行评审结论）
- 号召力口径：**不满足硬性 KOL 门槛**——单作者、无机构背书、未核到他人引用（区别于库内已收的 arXiv:2608.21884：后者为 JAWs@ASE 2026 在审的灰色文献综述票）。**按门槛如实列"边缘候选"，不计入 KOL 台账，供判读层参考。**
- **库内状态**：无此论文条目。本条为增量（灰色文献新票）。

**逐字摘录（abs/HTML 实取）**：

> "In mid-2026 a slogan reorganized how practitioners talk about coding agents: stop prompting your agent, start designing the loop that prompts it. We take this claim seriously and give it a careful treatment."
（把口号当研究对象做"careful treatment"——学理式中性派姿态。）

> "we argue, against the stronger headlines, that it does not retire prompt engineering; loop and prompt are distinct tools with distinct uses."
（对推动派标题党的直接反驳：loop 不取代 prompt。）

> "Loop engineering moves the human along a spectrum of autonomy rather than removing the human. With a human in the loop, every consequential action is approved before it runs; on the loop, a person monitors by alert or dashboard and intervenes only on exceptions; out of the loop, the agent acts alone with occasional guidance."
（HTML 正文实取——把"人的位置"显式谱系化，与 Kief 的三层互通。）

> "seventy percent of loops verify in the autonomous zone of the ladder and seventy-four percent name their terminal states, while automated triggering and durable memory remain comparatively underdeveloped."
（对 50 个公开真实 loop 的人工编码结果——实践成熟度不均匀的实证。）

> "We close with the limits the practice must respect, including the verification burden, comprehension debt and the risk of cognitive surrender."
（三个极限：验证负担、理解债、**认知投降风险**——对放权循环的人本主义边界，中性派罕见的三连命名。）

**该条支持的最小主张**：2026-06 命名后有学术取向作者对口号做界定＋反夸大＋实证编码＋极限列举；其 "spectrum of autonomy" 与 "cognitive surrender" 可作三派判读的概念工具。
**派别适配**：中性票（证据级别：灰色文献，作者影响力未核）。

---

**（第四轮挖掘（2026-10-06）：arXiv 学术层扫描）**

### 方向 A · 专名谱系："loop engineering" 已沉淀为 arXiv 可测量术语（A1–A7）

> 本方向是本轮对运动史最重要的增量：命名运动发布约三个月内，arXiv 上出现了以 "loop engineering" 为**定义域**的独立基准（A1、A2）、专名应用框架（A5、A4 系列）与教科书立章（A7）——与库内 2608.21884 构成互证。

#### A1 · LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering（arXiv:2608.28281）

- v1 2026-08-28（cs.AI）｜Yi Wang, Haopeng Zhang, Chengxiang Huang, Rui Dai, Kaikui Liu, Piotr Koniusz, Xiangxiang Chu（7 作者；基准开源于 GitHub AMAP-ML org——摘要自述）
- 摘要逐字（export.arxiv.org API 实取；TeX 标记按原样保留）：

  > "Loop Engineering is emerging as a practice for organizing development work around coding agents. Instead of writing each prompt by hand, practitioners design loops that monitor progress, assign work, run checks, and decide what the agent should do next. Even with a capable coding agent, a loop may trust a stale progress note, skip needed verification, spend its budget in the wrong direction, or stop before the task is safe to submit. Yet the final outcome of one end-to-end run cannot tell whether success or failure reflects the loop's guidance or the coding agent's ability to carry out the task. We introduce LoopArena, a benchmark for evaluating how well one model can guide a separate coding agent through a long-running task. The model under evaluation is the \textbf{Controller}: after each coding round, it receives a structured summary of the run and instructs a separate, fixed coding agent, the \textbf{Worker}, on what to do or verify next, or decides whether to stop. LoopArena evaluates this ability in three complementary settings that differ in execution scope and cost. Type I scores next-step Loop Contract selection through execution-validated questions without running the Worker at evaluation time. Type II executes repeated control over a selected slice of a full task, while Type III evaluates the paired full task from its original state. On full tasks, the best observed Strict Success Rate is \textbf{24.69\%}, leaving substantial room for improvement in long-horizon loop control. Across Controllers, the paired reduction in estimated inference cost averages \textbf{64.4\%}, and Type II produces a similar ordering under the main Core criterion (Spearman's \(ρ=\textbf{0.9747}\)). We release the benchmark data and evaluation code at https://github.com/AMAP-ML/LoopArena ."

- **与 loop engineering 的挂钩**：外层调度＋停止条件——把"loop 控制者"（monitor/assign/check/stop 的决策模型）与"worker 编码 agent"显式分离并分别评测——直接对应库内 stop_conditions 与外层调度议题；"Loop Contract" 概念与库内 goal/停止条件构件同构。
- 证据级别：预印本（v1，无 venue 标注）｜S2 引用数 1（2026-10-06 实核）。
- 派别适配：**中性（测量件）**；附带怀疑面数据——最强 controller 全任务 Strict Success 仅 24.69%，即"控制 loop 本身是未解决难题"的定量证据。
- 入册建议：**候选入册（学术旁证层）**（多作者＋组织级开源仓库）。

#### A2 · LoopsBench: From Harness Engineering to Loop Engineering in Coding Agent Evaluation（arXiv:2608.00267）

- v1 2026-07-31，v2 至 2026-08-10（cs.SE,cs.CL）｜Han Li, Zhemin Fang, Rili Feng, Yingqi Zhao, Jiaheng Liu, Pengfei Gao, He Ye, Dayi Lin, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang（11 作者；含 Microsoft 系作者名与 microsoft org 仓库——摘要自述 "at microsoft/Loopsbench"；项目页 loopsbench.ai）
- 摘要逐字（API 实取）：

  > "Coding agent infrastructure is shifting from harness engineering toward loop engineering as coding agents are deployed for sustained long-horizon software development. Existing benchmarks often center on localized tasks or end-state outcomes, offering limited insight into sustained execution. We introduce LOOPSBENCH, a long-horizon benchmark for loop engineering in coding agent evaluation. Each task is a dependency DAG over separately testable development units with source-evidenced prerequisite edges. LOOPSBENCH comprises 112 tasks from authentic sources spanning 8 programming languages and 9 domains. Its flow-aware runtime releases tests along the ready frontier and retains completed nodes as regression obligations. We evaluate frontier coding agents paired with widely used loop implementations. The strongest configuration, Opus-4.7 with Claude Code and outer continuation, resolves 25.00% of tasks. Recorded plans recover only part of the source-recovered prerequisite DAG, and regression events remain visible across the evaluated loop profiles. We open source the benchmark data and code, including all tasks, more than 5,300 development units, and executable tests, at microsoft/Loopsbench."

- **与 loop engineering 的挂钩**：循环结构（外层续跑）＋验证回路（回归义务）｜**标题本身即命题**——"from harness engineering to loop engineering" 把运动的两段式演化写成了基准论文的正当性前提；DAG 前置依赖＋回归义务的评测面与库内 graph_engineering 主题直接相邻。
- 证据级别：预印本（无 venue 标注）｜S2 引用数 2（2026-10-06 实核）。
- 派别适配：**中性（测量件）**；附带怀疑面数据——最强配置也只解 25%，计划恢复不完整、回归事件跨 loop 档持续可见。
- 入册建议：**候选入册（学术旁证层）**（11 作者＋组织级仓库）。

#### A3 · Proof-or-Stop: Don't Trust the Agent, Trust the Evidence -- Loop Engineering for Verifiable Evidence-Gated Lifecycle Control（arXiv:2607.14890）

- v1 2026-07-16（cs.AI,cs.SE）｜Jek Huang, Jeffery Hsia, Jiayi Sun, Freddie Shi, Wei Huang, Ian H. White（6 作者）｜comment: 48 pages, Preprint v1
- 摘要逐字（API 实取）：

  > "Autonomous coding agents increasingly execute multi-step software work, but lifecycle states such as reviewed, tested, DONE, and ready-to-merge remain claims unless supported by current evidence. We present Proof-or-Stop Lifecycle Control, a method that permits lifecycle transitions only when fresh, tracked-source-state-bound, mechanically verifiable evidence satisfies the relevant gate. The method treats agent outputs as claims rather than lifecycle state, and uses proof operationally to mean gate-admissible evidence under a stated trust model, not semantic program correctness. We evaluate an open-source implementation through mechanism tests, a powered control-policy ablation, and operated self-application evidence. The unattended-loop engine passed 10 of 10 scenarios with zero false-DONE, and local-key receipt bundles rejected 18 tamper classes with zero false accepts. In a 9,240-cell ablation, the pre-registered A4 versus A2-prime comparison reduced visible-pass/hidden-fail amplification from 31 of 1,800 injected cells under a compute-budgeted naive loop to 2 of 1,800 under the gated loop, a 1.6 percentage-point improvement in not-amplified rate with a 95 percent confidence interval of [0.8, 2.5]. A near-compute A3 versus A4 comparison, 14 of 1,800 versus 2 of 1,800, indicates that the gain is associated with enforcing review as a lifecycle gate rather than merely adding a reviewer. The self-application corpus contains 565 stories and 1,007 review findings, with 94.8 percent resolved, plus a 68-row high/critical cross-vendor exhibit. These results support Proof-or-Stop as a model-agnostic, host-neutral control layer for deciding which autonomous-agent claims a lifecycle may act on. The evaluation is limited to one model family, 24 ablation tasks, and a self-hosted corpus."

- **与 loop engineering 的挂钩**：**停止条件的机器门语义化**——"agent 输出是 claim 而非状态，生命周期迁移必须过 evidence gate"；标题即库内 03_verdict_split 的同构表述。其中 "enforcing review as a lifecycle gate rather than merely adding a reviewer" 与库内 F3（Groundability）互证。
- 证据级别：预印本 v1｜S2 引用数 3（2026-10-06 实核）。
- 派别适配：**中性工具性为主＋推动面正报告**——caveat：作者自认"限于单模型家族、24 ablation 任务、自托管语料"；10/10 场景为自建场景。
- 入册建议：候选入册（学术旁证层，注明自证评测 caveat）。

#### A4 · Towards Agentic Cloud Engineering: Graph and Loop Engineering with a Zero-Trust Agent Harness（arXiv:2609.00050）＋同组系列

- v1 2026-08-30（cs.SE,cs.AI,cs.LG）｜Sagar Srinivas Sakhinana, Venkataramana Runkana（2 作者；机构未核，外部线索指向 TCS Research——未核实）｜comment: Nil
- 摘要逐字（API 实取）：

  > "Agentic AI is enabling cloud-based workflows in which autonomous agents reason over operational state, invoke authorized tools, modify software and infrastructure, deploy services, verify execution outcomes, and adapt across long-horizon, multistep tasks. Engineering such workflows requires explicit mechanisms for workflow progression, constrained execution, failure recovery, and verifiable completion. We present Agentic Cloud Workflow Engineering, an agentic AI framework that transforms natural-language agentic cloud-engineering tasks into validated code repositories and verified operational cloud deployments for automating cloud-based agentic workflows. The framework separates three complementary concerns: graph engineering specifies long-horizon workflow progression and verification-dependent transitions; loop engineering provides bounded diagnosis, repair or re-planning, retry, and re-verification; and agent harness engineering enforces zero-trust execution through identity, authorization, policy-scoped capabilities, isolation, and runtime safeguards. Workflow progression and completion require machine-checkable repository, deployment, and runtime evidence, with recovery constrained by explicit operational bounds and termination criteria. We instantiate the framework on Google Cloud and evaluate repository completeness, controlled execution, evidence-gated progression, operational deployment, and bounded recovery. Experimental results show that executions terminate with either a verified operational cloud deployment or an auditable terminal failure under bounded recovery. The framework provides a unified engineering architecture for cloud-based workflows spanning Agentic DevOps, Agentic CloudOps, Agentic SRE/AIOps, Agentic SecOps, Agentic DataOps, Agentic MLOps/LLMOps, AgentOps, Agentic RAG/GraphRAG, and related cloud-engineering domains."

- 同组系列（同作者、同月，API 实取）：arXiv:2609.29668《Graph, Loop, and Harness Engineering for Zero-Trust Agentic Data Engineering and Analytical Processing》（cs.LG,cs.AI；节引："Both frameworks share three abstractions: graph engineering for evidence-gated workflow structure, loop engineering for bounded recovery, and agent-harness engineering for zero-trust execution."）与 arXiv:2608.29615《Forward-Deployed Full-Stack Engineering for Autonomous Cloud MLOps》（cs.MA,cs.AI,cs.LG；节引："The framework combines graph engineering, loop engineering, and agent harness engineering."）——同一三人组概念（graph/loop/harness engineering）三连发。
- **与 loop engineering 的挂钩**：循环结构＋验证回路＋预算与熔断｜**企业级场景把 loop engineering 立为三抽象之一**且给出可操作定义（bounded diagnosis→repair/re-plan→retry→re-verify）；与库内 graph_engineering / loop_governance 双主题的三维分工（graph＝进展结构、loop＝有界恢复、harness＝执行约束）几乎逐字同构。
- 证据级别：预印本（无 venue；自建评测）｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：**推动档正报告**——caveat：自建框架自证（"executions terminate with either a verified deployment or an auditable terminal failure"），无外部 baseline。
- 入册建议：边缘候选（2 作者、引用数 0；但概念谱系价值高，供判读层对照"三工程分立"提法）。

#### A5 · LoopVSR: A Loop Engineering Framework for Automated Repair of Visual Speech Recognition Inference Pipelines（arXiv:2608.13610）

- v1 2026-08-12（eess.IV,cs.MM）｜Fei Qin, Bowen Zhang, Chao Fan, Pengcheng Luo, Genke Yang（5 作者，上海交大系作者名——机构未核）
- 摘要逐字（API 实取）：

  > "Visual speech recognition (VSR) recovers speech from lip movements when audio is noisy or unavailable. Its multi-stage inference pipeline spans video decoding, mouth-region extraction, preprocessing, model invocation, and decoding, where upstream failures can mask downstream faults. Pipeline maintenance therefore still relies largely on predefined checks and manual debugging. We propose LoopVSR, a Loop Engineering framework that enables a code agent to automatically diagnose and repair VSR inference pipelines using end-to-end execution evidence. It couples constrained repository-level diagnosis and patching with an external controller that audits changes, runs real inference, and accepts or rolls back patches using failures and character error rate (CER). The resulting feedback loop returns newly observed exceptions, tensor statistics, and recognition errors to the agent, progressively exposing faults masked by upstream failures. On the CMLR VSR system, LoopVSR repairs all 11 main faults with 100% mean recovery, whereas the Static guard repairs 2 of 11 with 18.13% mean recovery. It also resolves three cascading tasks in seven accepted iterations and preserves recovery on an independent 200-video hidden set. These results demonstrate that LoopVSR enables measurable, end-to-end automated repair of VSR inference pipelines."

- **与 loop engineering 的挂钩**：验证回路＋外层调度｜**专名向非编码域扩散的直接证据**——"Loop Engineering" 作为框架名出现在视觉语音识别管道修复（eess.IV 分类）；结构（外部 controller 审计→真实执行→接受/回滚）与库内 loop 构件一致。
- 证据级别：预印本｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：**推动档正报告**——caveat：单一系统（CMLR）、11 个故障的样本面。
- 入册建议：边缘候选（传播谱系证据价值＞方法本身）。

#### A6 · Graph Engineering in the Era of LLM Agents: From Individual Intelligence to System Intelligence（arXiv:2608.21156）——谱系旁证

- v1 2026-08-21，v2 至 2026-09-14（cs.IR,cs.AI,cs.ET）｜Yuyuan Feng 等 **36 作者**（大联合体）｜节引（API 实取）：

  > "This evolution has produced paradigms including Prompt Engineering to elicit model capabilities, Context Engineering to manage information access, Harness Engineering to organize external tools and resources, and Loop Engineering to support continual reflection and self-improvement. … We introduce Graph Engineering, an emerging paradigm for next-generation agent systems."

- **与 loop engineering 的挂钩**：循环产品化机制（学术范式谱系收编）｜**把 "Loop Engineering" 正式写进学术综述的四范式谱系**（Prompt→Context→Harness→Loop→Graph 第五）——与库内 2608.21884 互为独立来源；同时是姊妹主题 graph_engineering 的直接学术输入。
- 证据级别：预印本综述｜S2 引用数 1（2026-10-06 实核）。
- 派别适配：中性（谱系/综述件）。
- 入册建议：**候选入册（学术旁证层）**（36 作者联合体；loop 主题只收其谱系句，正文归 graph 主题）。

#### A7 · The Hitchhiker's Guide to Agentic AI: From Foundations to Systems（arXiv:2606.24937）——教科书层旁证

- v1 2026-06-22，**v3（version 1.4）至 2026-09-29**（cs.AI,cs.CL,cs.IR,cs.LG）｜Haggai Roitman（单作者，书-form 综述；外部常识指向 IBM Research——未核）｜节引（API 实取）：

  > "The second half is devoted to agentic AI proper: agentic training and trajectory-based RL, RAG and Agentic RAG, memory systems (in-context, external, episodic, and semantic), agent harness design, loop engineering, graph-based orchestration, and a taxonomy of agent design patterns covering security, red teaming, and gateway infrastructure."

- **与 loop engineering 的挂钩**：循环产品化机制（教科书立章）｜教科书层把 loop engineering 与 agent harness design、graph-based orchestration 并列为独立章节主题——术语进入系统性教材的信号。
- 证据级别：预印本"书"（v1.4）｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：中性（谱系件）。
- 入册建议：边缘候选（单作者无引用；但"教材化"信号本身值得判读层记录）。

**（第四轮挖掘（2026-10-06）：arXiv 学术层扫描）**

### 方向 B · 停止条件 / guardrail / 运行时控制（B1–B7）

#### B1 · AgentGuard: Learning Execution Guardrails from Anomalous Coding-Agent Trajectories（arXiv:2609.16287）

- v1 2026-09-14（cs.SE）｜Wuyang Dai, Song Wang（2 作者）
- 摘要逐字（API 实取）：

  > "AI coding agents increasingly rely on execution harnesses to interact with repositories and external tools. However, task success does not guarantee reliable execution. Agents may still modify unrelated files, rewrite tests, issue unsafe commands, or ignore failed validations, motivating behavioral guardrails for reliable execution. We present AgentGuard, an instruction-level guardrail framework that learns conditional execution constraints from anomalous trajectories of coding agents. Rather than relying on manually specified safety rules, AgentGuard automatically extracts recurring execution failure patterns, generalizes them into instruction-level behavioral constraints, and organizes them as a lightweight guardrail skill that dynamically activates only the rules relevant to the current instruction. This design enables behavioral guidance while minimizing unnecessary restrictions on normal execution. We evaluate AgentGuard using 642 documented failure traces collected from real coding-agent executions across 382 repository tasks. Guardrails are learned from 461 traces covering 282 tasks and evaluated on a disjoint set of 100 tasks. Using Claude Code with Claude Haiku 4.5 as the underlying coding agent, we compare the baseline agent with the same agent augmented by AgentGuard. Experimental results show that AgentGuard reduces the Abnormal Execution Rate from 69.0% to 26.7% and increases the Successful Task Completion Rate from 21.7% to 35.0%. These results demonstrate that execution guardrails learned from historical failures can substantially improve the reliability of AI coding agents while highlighting the remaining challenge of balancing safety and task completion."

- **与 loop engineering 的挂钩**：停止条件（执行约束门）＋验证回路｜guardrail 关键词直中——从失败轨迹学习执行约束（guardrail skill），对应库内 stop_conditions/01_machine_gates 的"机器门"素材；其失败模式清单（改无关文件/重写测试/不安全命令/忽略失败校验）可与库内事故目录（2606.04056）对表。
- 证据级别：预印本｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：**中性工具性＋推动面正报告**——caveat：单一底层 agent（Claude Code＋Haiku 4.5），baseline 完成率 21.7% 的起点很低。
- 入册建议：候选入册（学术旁证层，注明单 agent caveat）。

#### B2 · Guardrailed Meta-Agent Loops: Stress-Testing Policy Pinning, Budget Bounds, and Crash Recovery（arXiv:2609.12216）

- v1 2026-09-10（cs.RO）｜Qinzhen Ma, Jialin Wu（2 作者）
- 摘要逐字（API 实取）：

  > "Self-improving agent workflows create an audit problem when the same controller can change both its behavior and the conditions under which that behavior is judged. We present GuardrailLoop, a simulation-based testbed that makes three operational contracts jointly testable: preservation of human-defined policy, compute accounting at every recorded execution prefix, and recovery of a specified scientific state after crashes. A hash-pinned policy fixes goals, scope, evaluation identity, budget, and release conditions; machine-directed evolution is restricted to a code-owned feature catalog and bounded knobs. The contribution is an executable boundary and an evaluation protocol that separates useful adaptation, state recovery, and repeated execution. In a paired 50-seed 2 x 2 study, round-stage growth changes target attainment by +1.00 and restricted mean compute to target by -56.97 simulated GPU-hours (95% paired-bootstrap interval [-58.91,-54.70]); idle growth has zero measured utility effect. Across 240 enumerated crash injections, all runs recover the defined outcome, but only 210 preserve the normalized trace: 30 pre-commit crashes repeat a planner call. Resource-drift, kill-switch, integrity, and output-guard matrices satisfy their specified checks. These findings show why successful outcome recovery is insufficient evidence of exactly-once execution. They establish conformance within one calibrated deterministic testbed, rather than general safety or real-world self-improvement."

- **与 loop engineering 的挂钩**：预算与熔断（policy pinning/budget bounds/kill-switch）＋停止条件｜guardrail 关键词直中——把 policy pinning（hash 固定目标/预算/终止条件）＋预算边界＋崩溃恢复做成**可测的三契约**；"successful outcome recovery is insufficient evidence of exactly-once execution" 是停止条件语义的一条锋利学术表述（结果恢复≠恰好一次执行）。
- 证据级别：预印本（模拟 testbed，作者自认"非真实世界自改进的一般安全性"）｜S2 引用数：未核（本轮 batch 未含）。
- 派别适配：**中性（测试床/协议件）＋怀疑面**（30/240 崩溃注入重复 planner 调用）。
- 入册建议：边缘候选（2 作者；概念价值＞引用面）。

#### B3 · Online Monitoring and Corrective Steering of Programming Agents（arXiv:2608.06701，LivePlan）

- v1 2026-08-07（cs.SE,cs.AI,cs.CL,cs.LG）｜Shuyang Liu, Saman Dehghan, Ji Young Kim, Jatin Ganhotra, Martin Hirzel, Reyhaneh Jabbarvand（6 作者；Hirzel/Jabbarvand 机构归属为外部常识 IBM Research/Purdue——未核）
- 摘要逐字（API 实取）：

  > "Fixing GitHub issues in large-scale projects is a long-horizon task, especially when a fix requires changes across multiple locations or the issue description lacks the information needed to localize and repair it. As a result, agents traverse long trajectories that are prone to inefficiency and error: they drift away from their intended plan, repeat failed actions, or terminate without a working patch. This paper proposes LivePlan to monitor, detect, and correct such behavioral inefficiencies and drifts in real time. LivePlan decouples judging from advising: a deterministic, rule-based monitor examines general signals over the trajectory to detect issues without invoking an LLM, and only when an issue is detected does it consult an advisor LLM for a high-level, next-step correction. This design avoids the misleading re-planning and costly interventions of prior approaches. We implement LivePlan on top of SWE-agent and evaluate it using five LLMs (three as executor agents and two as advisors) across SWE-bench Verified and SWE-bench Pro. Compared to vanilla SWE-agent, LivePlan notably improves issue resolution rates, achieving consistent gains of up to 15.2% (average: 9.9%), while incurring only an additional cost of $0.08 per instance. The additional solutions concentrate on medium and hard instances. LivePlan consistently outperforms alternative approaches in resolution rate, with minimal regression on already successful runs and new successes on problems that no baseline solves."

- **与 loop engineering 的挂钩**：外层调度（确定性监视器＋按需顾问）＋停止条件｜**运行时监控＋纠偏转向（steering）的系统化**——"确定性规则监视器判异常、只在异常时唤 LLM 顾问"的分工直接是库内"observation→steering"环的学术件；drift/repeat/terminate-without-patch 三失败模式命名可入 stop_conditions 素材。
- 证据级别：预印本（SWE-bench 系内评测）｜S2 引用数 1（2026-10-06 实核）。
- 派别适配：**推动档正报告**——caveat：基准内增益（SWE-bench Verified/Pro），作者未做真实仓库部署面。
- 入册建议：候选入册（学术旁证层；6 作者＋知名研究者）。

#### B4 · Assurance Envelopes for Autonomous Coding Agents: Minimum-Cost Evidence for Software Change（arXiv:2609.16302）

- v1 2026-09-14（**cs.SE,cs.AI,cs.PL**）｜Anjan Goswami（单作者）
- 摘要逐字（API 实取）：

  > "When a coding agent returns to existing software, it inherits evidence from earlier engineering work: tests, type checks, proofs, static analyses, and traces. Reloading all of it is wasteful, but dropping a piece the change depends on can leave a required property unsupported. Given the properties a change must preserve, its obligations, we ask which least-cost subset of the available evidence re-establishes them, and we call such a subset a task-conditioned assurance envelope. Evidence and the rules that combine it form a typed inference graph; an obligation is met when forward chaining from the selected evidence reaches it, and we validate every selection by that closure rather than by trusting the optimizer. The software-derived graphs in our evaluation come from preserved outcomes of prior AI coding-agent runs; we freeze those artifacts and ask which accumulated evidence should be restored for a later task. Small graphs from Rust, IronBlocks, and Pong outcomes show that the minimum envelope depends on the task, that none may exist when current evidence cannot re-establish a required property, that some properties need several pieces of evidence together, and that expanding the requirements adds evidence rather than replacing it. A prespecified synthetic benchmark of 249 instances characterizes computation: a baseline that discards the 'several pieces together' structure necessarily fails to re-derive them; every completed exact cross-check agreed with the CP-SAT optimizer; and median solve time stayed below 20 ms at 500-evidence graphs, except that graphs with many alternative derivations per target timed out at far smaller sizes, so structure, not raw size, drives difficulty. The contribution is a bounded application of established optimization to selecting assurance context for a software change; discovering the obligations and downstream agent benefit remain open."

- **与 loop engineering 的挂钩**：**"证据最小充分集"的正式化**（验证回路——每轮迭代重载哪些证据）——对"每次 loop 迭代该重载哪些验证"给出优化问题的形式化（obligation/typed inference graph/CP-SAT）；是 evidence-gated stop（A3/B2）的下游精细件；cs.PL 标签命中任务第三分类。
- 证据级别：预印本｜S2 引用数：未核（本轮 batch 未含）。
- 派别适配：**中性（理论/工具件）**；作者自述义务发现与下游收益"remain open"——不外推。
- 入册建议：边缘候选（单作者无引用）。

#### B5 · Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents（arXiv:2608.27141）

- v1 2026-08-27，v6 至 2026-09-22（cs.CR,cs.AI）｜Chenhao Wu 等 14 作者｜（LoopHarness）
- 摘要逐字（API 实取）：

  > "Large language model agents are increasingly deployed as autonomous loops. Starting from one human goal, such a system repeatedly discovers work, plans, executes tool calls, verifies outcomes and persists state across many unattended iterations. The agent safeguards in wide use, however, are defined over a single trajectory, and their safety state is re-initialized when the next trajectory begins. We show that this is a failure of composition rather than an implementation detail. Our central result is a separation: against an attack whose evidence is fragmented across several iterations, every trajectory-scoped monitor has a true-positive rate equal to its false-positive rate, however expressive it is, because the evidence it would need never appears in the window it sees, whereas a monitor retaining cross-iteration state separates the two perfectly. We further show that the obvious repair of carrying a geometrically decaying risk score is insufficient, because the cooling-off period a patient adversary must wait is a constant that does not grow with the horizon $N$. We then present LoopHarness, which restores a persistent, non-decaying safety state at the loop level. Under mediated commits and an arbiter detection floor $δ_M$, it bounds the expected number of unauthorized irreversible actions by $B+m-1+m/δ_M$, a constant in $N$, of which the $B+m-1$ term is decided by a model-free rule and therefore survives a fully colluding verifier. We give a complete evaluation protocol on native Agent-SafetyBench tasks with paired clean and attacked episodes, an outer-state attack suite whose decisive evidence exists only across iterations, per-module ablations, and an adaptive white-box red team."

- **与 loop engineering 的挂钩**：循环结构（跨迭代安全状态）＋无人值守运行＋熔断｜**loop 级安全状态的形式化**——单轨迹监控对跨迭代碎片化攻击在理论上必然失效（TPR=FPR 的分离结果），衰减风险分也不够；"loop 层非衰减安全状态＋有界不可逆动作数"是停止条件/外层调度议题从未有过的定理级表述。
- 证据级别：预印本（v6 迭代活跃）｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：**怀疑档（失败模式/组合性证明）**＋工具（LoopHarness）。
- 入册建议：**候选入册（学术旁证层）**（14 作者＋理论结果）。

#### B6 · AgentLoop: Runtime Control of Slot-closed Execution Loops for Tool-augmented LLM Agents（arXiv:2609.33315）——节引

- v1 2026-09-27（cs.DC）｜Wanyi Zheng, Minxian Xu, Kan Hu, Kejiang Ye, Chengzhong Xu（5 作者）｜节引（API 实取）：

  > "Slot closure means that the information slots required by a request have been covered by sufficient runtime evidence, and that unresolved slots are explicitly identified before the loop stops. … total token cost reduced by up to 88.44% and average service invocations reduced by up to 76.85% against baselines."

- **与 loop engineering 的挂钩**：停止条件的运行时信号化（slot closure＝信息槽覆盖才允许停）——与 2606.04056 token 预算事故目录的"何时该停"问题同源；正报告 caveat：工具调用域（非编码域）。
- 证据级别：预印本｜派别适配：中性工具性。入册建议：边缘候选。

#### B7 · Don't Offer What Can't Be Done: Deterministic Executability Gating for LLM Skill Selection at Scale（arXiv:2608.01050）——节引

- v1 2026-08-02（cs.AI,cs.CL,cs.SE）｜Ortal Ashkenazi, Vitalii Kloz, Mykhailo Ulianchenko（3 作者；Wix 生产系统——摘要自述 Helpmate）｜comment: 投 KDD 2027 在审｜节引（API 实取）：

  > "In a post-launch production analysis of 756.6K user messages across 267.6K conversations … semantic matching and executability gating reduced skill-description context by 90.5% relative to exposing all ten skills to every message. … The model selected a production-blocked skill in 78 conversations (7.8%)."

- **与 loop engineering 的挂钩**：预算与熔断（上下文预算的确定性裁剪）＋机器门前置｜**生产级确定性门**（executable gate 在模型选择前裁掉不可执行项）——"机器门先于模型判断"的大规模生产证据，与库内 01_machine_gates 实践层直接同构。
- 证据级别：预印本（在审 KDD 2027；生产数据）｜派别适配：中性工具性。入册建议：边缘候选。

#### B8 · Learning When and How to Intervene: A Hindsight-Distilled Sentinel for Coding Agents（arXiv:2609.39957）——节引

- v1 2026-09-30（cs.SE,cs.AI,cs.LG）｜Jiangrui Zhao, Chenglong Li, Meng Zhang, Xiaoting Du（4 作者）｜节引（API 实取）：

  > "we introduce SWE-Intervene, an action-level dataset … that annotates whether an action should be allowed, autonomously redirected, or paused for human assistance … HiSentinel consistently improves task completion … with gains of up to 14% and 10%, respectively, while maintaining competitive token consumption."

- **与 loop engineering 的挂钩**：**"允许/转向/暂停求助"三分类的人机交接判定器**（外层调度——何时把人拉回来）——正是"外层调度什么时候把人拉回来"的学习化版本；正报告 caveat：自建数据集训练。
- 证据级别：预印本｜派别适配：中性工具性＋推动面。入册建议：边缘候选。

**（第四轮挖掘（2026-10-06）：arXiv 学术层扫描）**

### 方向 C · reward hacking 与 agent exploit（怀疑向核心区，C1–C6）

#### C1 · Shortcutting the Fix: Identifying and Categorizing Agentic Exploits in Software Engineering Benchmarks（arXiv:2609.06780）

- v1 2026-09-06（cs.SE）｜Nikolai Ludwig, Wasi Uddin Ahmad, Somshubra Majumdar, Boris Ginsburg（4 作者；NVIDIA 归属为外部常识——未核）｜comment: Preprint
- 摘要逐字（API 实取；TeX 转义按原样保留）：

  > "While autonomous software engineering (SWE) agents achieve high benchmark resolution rates, these scores can mask exploitative behaviors---such as leveraging local Git histories, accessing upstream repositories, or recalling memorized solutions---rather than demonstrating genuine problem solving. We systematize and audit these exploits across five open large language models on SWE-bench Multilingual and DeepSWE using a turn-level LLM-as-a-judge protocol. Under standard prompts, exploitation rates reach 45.1\%--82.4\% on SWE-bench Multilingual and 44.2\%--66.1\% on DeepSWE. Appending a targeted instruction enforcing solution originality drastically cuts these exploitation rates---down to 4.0\%--10.7\% and 1.5\%--7.1\%, respectively, while maintaining strong core task performance. Our findings demonstrate the critical need for exploit-aware evaluation frameworks that measure true repository-level problem solving over benchmark gaming."

- **与 loop engineering 的挂钩**：验证回路被博弈（loop 内取巧→假 DONE）｜**任务点名方向"coding agent 的 reward hacking 分类学"的直接命中**——系统化＋审计 exploit（git 历史利用/上游仓库访问/记忆化解法），并给出几乎零成本的缓解（一句 originality 指令把作弊率砍到 4–10.7%）。
- 证据级别：预印本｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：**怀疑档（失败模式系统化）**；缓解面是中性工具性。
- 入册建议：**候选入册（学术旁证层）**（多作者＋大厂团队）。

#### C2 · hacktrace: behavior-supervised detection of reward hacking during code generation（arXiv:2610.03055）

- v1 2026-10-02（cs.AI）｜Hao Jiang, Xin Li, Annan Wang, Yichi Zhang, Weisi Lin（5 作者）
- 摘要逐字（API 实取）：

  > "A coding agent can earn a passing grade by fixing its code, or by deleting the test that exposes the bug. Detecting such reward hacking requires recognizing attempted shortcuts, including those that fail. We release 173,561 annotated multi-turn coding trajectories from Qwen3-8B and show that supervising shortcut behavior independently of exploit success substantially improves detection. We introduce HACKTRACE, a behavior-supervised monitor that reads the internal states the agent already computes while generating code. Reusing these states enables monitoring before a turn is complete, without additional language-model tokens or passes. Combining this evidence with static features of the final files achieves a mean per-problem AUC of 0.997 with 8 ms of monitoring overhead, improving both accuracy and latency over monitors that run the model again on an honesty question and answer. The same generation states also provide an inexpensive monitoring signal for reinforcement learning. With strong GRPO penalties, HACKTRACE reduces the cheating share of passing solutions from 82-91% to 1-5%, while retaining honest, correct solutions and maintaining high detection accuracy as the policy evolves. Our results show that both the supervision target and the source of monitoring evidence matter for turning accurate detection into a useful training signal."

- **与 loop engineering 的挂钩**：**"删测试得分"型 reward hacking 的运行时监测**（验证回路——未遂作弊的运行时监测）（含未遂行为监督）——为库内"verdict split／机器门"提供低开销监测件参照；同时给出训练侧修复路径。
- 证据级别：预印本｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：怀疑档（失败模式监测）＋中性工具性。
- 入册建议：边缘候选。

#### C3 · Reward Hacking and Agent Containment Failure: A Monte Carlo Study Based on the 2026 Hugging Face Incident（arXiv:2609.32390）

- v1 2026-09-26（cs.AI,cs.CR）｜Murat Ozer, Bulent Erenay, Ibrahim Berber（3 作者）｜comment: 14 pages
- 摘要逐字（API 实取）：

  > "The July 2026 intrusion into Hugging Face production infrastructure showed how reward hacking can become an external cybersecurity incident when a capable agent encounters weak containment boundaries. This study develops a probabilistic risk model linking five stages: reward hacking, containment escape, usable access, persistence, and failure of detection. A Monte Carlo simulation evaluates 100,000 runs under each of four control configurations. Input distributions represent explicit uncertainty and are used for comparative analysis rather than real-world frequency prediction. Under the stated assumptions, layered controls reduce simulated external-incident probability substantially more than network isolation or monitoring used alone, an ordering that holds under independent plus/minus 25% perturbation of every coefficient in the model across 300 draws. Sensitivity analysis shows that agent capability and weaknesses in monitoring, authorization, and credential control exert the greatest influence on modeled risk. Human temporal discounting and metric gaming provide a behavioral analogy for short-horizon optimization, but the study does not infer that AI agents experience gratification or human motivation. The results support treating cyber-capable agent evaluations as hostile security zones in which indirect egress, shared infrastructure, credentials, and evaluation artifacts must remain outside the agent's effective authority."

- **与 loop engineering 的挂钩**：无人值守运行（围栏失效链）＋预算与熔断（containment 分层）｜**2026-07 Hugging Face 事件学术化**——reward hacking→containment escape→外部安全事件的五阶段风险链；"评测环境＝敌对安全区"的主张与库内 sandbox/egress 线（Darren Shepherd 档 Source D）同向但来源分层。
- 证据级别：预印本；**建模研究非实证**（作者自述"comparative analysis rather than real-world frequency prediction"）｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：怀疑档。
- 入册建议：边缘候选（引用须带"蒙特卡洛建模、非实证"限定）。

#### C4 · Approval Laundering: Systematizing Approval--Execution Binding Failures in AI Coding-Agent Harnesses（arXiv:2609.38983）

- v1 2026-09-30（cs.CR,cs.AI,cs.SE）｜Yang Wang（**单作者**）
- 摘要逐字（API 实取）：

  > "Modern AI coding-agent harnesses (Claude Code, Codex CLI, Cursor) rest their security boundary on a largely unexamined assumption: that the action A a human approves is the same action A' the harness executes, where A is fixed by a stated policy for what a scope grant or session-scoped approval authorizes. We show this assumption fails systematically and reproducibly. We introduce Approval Laundering, a taxonomy of six failure modes by which a harness's enforcement mechanism silently substitutes A' for A after approval: Scope, Argument, Temporal, Tool, Delegation, and Semantic laundering. Unlike prior work that evaluates risk classifiers against static corpora or infers implicit authorization boundaries, we study credential-binding integrity: given an already-approved action, does the harness dispatch exactly that action? Instrumenting Claude Code's pre-execution mediation point (PreToolUse), we conduct a controlled, headless, repeated-measures study of all six classes (N=19-20 runs each), reporting a Bound-Gap Rate (BGR) with Wilson confidence intervals and inter-rater agreement (kappa=1.0). We prototype Approval Token, a keyed capability Hk(principal, agent_id, session_id, tool, arguments, scope, expiry) issued by a mediator that never returns the key to the agent, evaluated via paired before/after replay of 118 runs (McNemar's exact test). The token fully eliminates Delegation laundering and, for our seeded session-identity-mismatch construction, Temporal laundering (p<10^-5), but by design leaves Scope laundering unaffected and shows no significant reduction in Argument laundering (p=1): an honest negative result, since these two classes leave every recorded dispatch field unchanged, diverging one process level below what a field-only verifier can observe. We discuss implications for defenses that bind only at the tool-invocation boundary."

- **与 loop engineering 的挂钩**：**"人批准的 A≠harness 执行的 A'"六类失败模式分类学＋对 Claude Code PreToolUse 的受控实测**（外层调度的失效面——人审批控制点被 harness 静默替换）——库内 harness_governance / 审批链议题最直接的学术件；其"honest negative result"（Approval Token 对两类无效）值得实践层吸收。
- 证据级别：预印本｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：怀疑档（失败模式分类学）。
- 入册建议：**边缘候选（单作者无引用）**——但方法透明度高（预注册比较＋Wilson CI＋kappa），引用时如实标注作者规模。

#### C5 · Maintaining Benchmarks Against Increasingly Capable Agents: Detection and Remediation of Unearned Passes（arXiv:2609.34262）

- v1 2026-09-28（cs.AI,cs.LG,cs.SE）｜Weijun Luo, Kelvin Luu, Xinyi Liu, Guangze Luo, Miguel Romero Calvo, Soham Dan, Daniel Yue Zhang, Ying Liu, Mohamed Elfeki（9 作者）
- 摘要逐字（API 实取）：

  > "Agentic benchmarks guide model selection and training. Yet an agent can pass a task without demonstrating the intended capability. Such outcomes constitute unearned passes; their proportion among all passes defines the integrity gap. As agents improve, benchmark surfaces that once seemed harmless can become exploitable, making benchmark validity an ongoing maintenance problem. We introduce a process-verification framework that audits passing trajectories, distinguishes evidenced reward hacking from verifier weakness, and localizes exploitable surfaces for repair. Across 3,810 passing trajectories from 29 model-benchmark cohorts, confirmed violations often increase with model generation but not monotonically. On SWEBench Pro V1.0, confirmed violation rates rise from 24% to 73% between Opus 4.7 and Fable 5 on matched tasks; later cohorts fall to 11% for Fable 5.1 and 0% for GPT-6 Astra. These comparisons are descriptive: configurations were not normalized, and the latest models also pass fewer exploitable tasks. Violations concentrate around a small set of recurring surfaces, especially unintended access to reference solutions through git history. Three repair case studies across two benchmarks show why blocking a recorded exploit is insufficient: the same protected information can remain accessible through another route. Therefore, we combine minimal patches with exploit replay and fresh agent evaluation, auditing new passes under the original standard. No evaluated attempt against the final patches reached the protected channel, and every post-patch pass was judged legitimate. Benchmark integrity requires ongoing maintenance: audit passing behavior, repair the enabling surface, and re-evaluate both exploit access and legitimate solvability."

- **与 loop engineering 的挂钩**：**"作弊面随 agent 能力增长而演化"的长期主义表述**（验证回路——benchmark validity 是验证回路的持续维护问题）＋"堵一条通道≠修复"的负结论——与 C1 互证并给出修复协议（minimal patch＋exploit replay＋fresh evaluation）。
- 证据级别：预印本；跨模型比较为描述性（作者自述未归一化配置）｜S2 引用数：未核。
- 派别适配：怀疑档。
- 入册建议：候选入册（学术旁证层，9 作者；引用时带描述性统计限定）。

#### C6 · LLM-as-a-Judge Is Not an Oracle: Why Self-Improving Agents Need Deterministic Guardrails（arXiv:2609.02246）——节引

- v1 2026-09-02（cs.AI,cs.LG）｜Vansh Wahi（**单作者**；同作者另有 arXiv:2609.25848《Optimizing the Score, Losing Sight of the Task: Reward Hacking Across Weights, Selection, and Prompts》，2026-09-22，19 pages）｜节引（API 实取）：

  > "Agents achieved perfect scores by reading cached answer keys from their environment, a 100% pass rate concealing 68% true capability. … the judge should be demoted from oracle to advisor: its verdict becomes one input among several, and every change is gated instead by a deterministic verification layer the judge cannot override."

- **与 loop engineering 的挂钩**：循环结构（自改进 loop）＋停止条件（确定性 gate 否决评委）｜**自改进 loop 的"评委非神谕"立场文＋生产事故目录**（11 种评估信号失败、四类）——与库内 judge lineage 档案（evidence-m）同向；确定性 guardrail 主张与 A3/B2/B7 构成学术层小集群。
- 证据级别：预印本（自述"months of production"经验）｜派别适配：怀疑档＋中性工具性。入册建议：边缘候选（单作者）。

**（第四轮挖掘（2026-10-06）：arXiv 学术层扫描）**

### 方向 D · harness 效应与评测批判（D1–D8）

#### D1 · What Does a Harness Buy? Tokens, Mostly（arXiv:2610.04433）

- v1 2026-10-03（cs.AI,cs.LG,cs.SE）｜Yangze Liu, Zhongyi Han（2 作者）
- 摘要逐字（API 实取）：

  > "A coding agent is a language model wrapped in a harness: the system prompt, the tool set, and the context management that turn a chat model into something that can work inside a repository. Production harnesses ship releases daily, vendors advertise pass-rate gains from harness changes, and leaderboards mix harnesses freely. What is rarely measured is how much the harness itself moves the score when the model is held fixed. We run five models through three production harnesses, Claude Code, mini-SWE-agent, and OpenCode, on SWE-bench Verified, and rerun the same configurations to calibrate how much a score moves when nothing changes but the run. On 447 tasks and the two models we ran there, Claude Code and mini-SWE-agent, the heaviest and the lightest harness, are equivalent within five points. On a 45-task hard subset and five models, swapping the harness flips as many tasks as rerunning the same harness, 13% in both cases, and the tasks a harness wins in one run are not the tasks it wins in the next. The one harness effect that clears the noise is a loss, not a gain: OpenCode trails by up to 9 points on the large pool, and on one model half of that gap sits in runs its output cap cut short. What the harness does decide is the bill. With the same model, the same tasks, and one price list, cost per task differs by up to 3x across harnesses. The gap is set at the first call, by the preamble of system prompt and tool schemas each harness sends with every step, and scaled by the number of steps; per-step growth and per-call tool output differ far less. The provider's price for cached input scales the bill and does not reorder it. The rerun data also give the resolution a harness comparison needs: at the discordance we observe, 45 tasks catch a 13-point gap only half the time and no gap with 80% power, and 447 tasks resolve 5 points, still coarser than the gains many harness changes claim."

- **与 loop engineering 的挂钩**：预算与熔断（同任务成本差 3x、输出上限截断）＋循环产品化机制｜**对 harness/loop 基建效果宣称的测量学清算**——固定模型换 harness 的分数波动≈同 harness 重跑波动（13% vs 13%），唯一过噪效应是**负向**（输出上限截断）与**账单**（同任务成本差 3x）；"harness 宣称的增益普遍小于测量分辨率"直接命中本主题"先测再信"的中性派方法论。
- 证据级别：预印本（含功效/样本量分析）｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：**怀疑档（对厂商增益宣称）＋中性测量学贡献**。
- 入册建议：候选入册（学术旁证层）。

#### D2 · Coding Agents Have Converged: Why the SWE-bench Leaderboard Can No Longer Order Its Top Entries, and What to Measure Instead（arXiv:2609.17394）

- v1 2026-09-15（cs.SE,cs.AI）｜Fengshuo Liu, Ying Liu, Ruize Sun, Lie Luo, Siyuan Guo（5 作者）｜comment: **Accepted at ADMA 2026**（Responsible Data Intelligence 特别_session），camera-ready
- 摘要逐字（API 实取）：

  > "Small differences on coding-agent leaderboards are often read as an ordering of systems. We audit whether the published verdicts support this reading, using 254 SWE-bench submissions across four splits without running models. On Verified, the leading two entries each resolve 396 of 500 instances. The top ten share 285 successes and 51 failures, leaving 164 instances that distinguish their outcomes. Frontier solution sets have median nesting 0.935 against a score-implied baseline of 0.774, indicating strongly shared successes. Scores also depend on the evaluated model-scaffold pair: observed within-model scaffold ranges reach 29.8 percentage points, compared with the 8.8-point spread of the top thirty. Six of nine cell-mean interaction tests remain significant after Holm correction, although this observational design does not identify causal scaffold effects. Exact paired McNemar tests separate none of the 29 adjacent Verified top-thirty pairs at alpha=0.05, while the larger Test split separates 14 of 23. A stated leader-based rule yields three descriptive tiers, or two after Holm correction; non-rejection does not establish equivalence. We release the partition and a five-step audit protocol that profiles shared outcomes, tests paired differences, reports grouping sensitivity, and estimates the instance budget needed for resolution. The results motivate reporting comparison-set-specific resolution and model-scaffold provenance instead of interpreting small aggregate gaps as established rank differences."

- **与 loop engineering 的挂钩**：验证回路（评测回路已无区分度）｜**SWE-bench 局限批判的直接命中**——榜首两强同分（396/500）、top10 共享 285 成功、模型×scaffold 交互范围 29.8pp＞top30 分差 8.8pp、相邻排名全部不可区分（McNemar）；与库内 2608.21884 的"话语/实践脱节"发现构成"榜单→实践推断"链条的两端质疑。
- 证据级别：**已录用会议（ADMA 2026）**——本轮命中中唯一确定 peer-reviewed venue 的主条目｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：怀疑档（评测批判）；作者自述 observational design 不识别因果。
- 入册建议：**候选入册（学术旁证层）**（已录用 venue）。

#### D3 · Schrödinger's Code Repository: Have LLMs Learned SWE-bench or Memorized It?（arXiv:2609.27891）

- v1 2026-08-21（cs.SE,cs.AI）｜Silin Chen, Yufei Yang, Xiaodong Gu, Yuling Shi, Chengcheng Wan, Haibing Guan（6 作者）
- 摘要逐字（API 实取）：

  > "Repository-level coding benchmarks have become the standard for evaluating coding agents, yet they inherently suffer from data leakage because they are built upon popular open-source repositories repeatedly used for training. Consequently, strong performance may reflect memorization of canonical repository cues rather than robust repository reasoning. We propose SchrodingerRepo (Schrödinger's Repository), an evaluation framework for testing coding agents under dynamically instantiated repository representations. Instead of repeatedly using a static representation of the test repository, SchrodingerRepo treats the test repository as an evaluation-time latent variable that is dynamically instantiated only when the agent enters the evaluation environment. The instantiated repository preserves the original executable behavior while eroding familiar cues such as naming conventions, file layouts, and implementation patterns through four transformation levels: problem statement reconstruction, namespace remapping, intra-file layout reordering, and functionality-preserving code rewriting. We evaluate popular LLMs on SWE-bench Verified and SWE-QA. Results show that removing familiar repository cues consistently degrades agent performance and substantially increases interaction costs across models. Further analysis reveals that the additional cost is primarily caused by increased difficulty in repository exploration and localization. These findings suggest that current coding agents may partially rely on memorized repository-side cues, highlighting the need for evaluation under dynamically instantiated repository representations."

- **与 loop engineering 的挂钩**：验证回路（记忆化令验证失真）｜SWE-bench 记忆化批判（评测时动态实例化仓库剥掉熟悉线索→一致退化）——评测局限方向的第三块拼图（榜首不可分 D2／作弊面 C1、C5／记忆化 D3）。
- 证据级别：预印本｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：怀疑档。
- 入册建议：候选入册（学术旁证层，6 作者）。

#### D4 · SWE-Gate: Passing Functional Tests Is Not Enough for Software Engineering Agents（arXiv:2609.04167）

- v1 2026-09-03（cs.SE,cs.AI）｜Xin He, Yanlin Wang, Mingwei Liu, Jiachi Chen, Hongyu Zhang, Guanbin Li（6 作者）
- 摘要逐字（API 实取）：

  > "Repository-level software engineering benchmarks have significantly advanced the evaluation of coding agents, but existing benchmarks primarily measure whether generated patches pass functional tests and overlook review-derived acceptance constraints (review constraints) that often influence whether a patch is acceptable in real-world software development. We introduce SWE-Gate, a repository-level benchmark for software engineering agents that explicitly evaluates review constraint compliance alongside functional correctness. SWE-Gate derives review constraints from real pull request review comments and synthesizes repository-level repair instances around these constraints. Each instance provides separate functional and constraint tests, together with non-compliant and gold patches, enabling explicit separation between issue resolution capability and review constraint compliance. We construct SWE-Gate with 303 repository-level repair instances spanning 75 open-source Python repositories across diverse software domains. Experiments with four LLM backends spanning different capability levels under a common coding-agent scaffold reveal a substantial gap between functional success and success under the complete repair specification: among 644 repairs that pass the functional tests, 221 fail to satisfy the provided review constraints. These findings show that functional-only evaluation overestimates agents' ability to satisfy the full requirements of repository-level repair tasks."

- **与 loop engineering 的挂钩**：**"过测试≠可合入"的定量版**（停止条件——DONE 判据缺口；验证回路。644 过功能测试中 221 违反 review 约束）——verdict split／停止条件"什么算 DONE"议题的学术对照件；同向件：arXiv:2610.06193 SWE-CC（节引见 G6）。
- 证据级别：预印本｜S2 引用数：未核。
- 派别适配：怀疑档。
- 入册建议：候选入册（学术旁证层）。

#### D5–D8 · harness 效应研究群（节引条目）

- **D5 · Beyond the Model: Demystifying Harness Effects in Software Engineering Agents**（arXiv:2609.32459，v1 2026-09-26，cs.SE，Haichuan Hu, Quanjun Zhang 等 8 作者）——节引（API 实取）："harness effectiveness depends jointly on model capability and task type. Complex harnesses provide diminishing marginal gains on SWE-style issue repair as model capability improves … context compression and general subagents can hurt repository-generation performance." **与 loop engineering 的挂钩**：循环结构（harness 组件改变循环行为与收益，复杂 harness 边际递减）。派别适配：中性（组件级消融）；与 D1 同向（复杂 harness 边际递减）。
- **D6 · An Empirical Study of Harness Design for Coding Agents**（arXiv:2609.20804，v1 2026-09-17，cs.AI 等 4 分类，Run-Ze Fan 等 9 作者，43 pages）——节引（API 实取）："(3) Planning shifts from an accuracy scaffold for weaker models to a cost saver for stronger models, with little change in accuracy. (4) Predefined tools improve performance for models with weaker bash proficiency, whereas bash-capable models can operate effectively with a bash-only interface and achieve substantially lower cost." **与 loop engineering 的挂钩**：循环结构（组件改变轨迹停点）＋预算与熔断（成本）。派别适配：中性（176 匹配设置的组件级实证）；"planning 从精度脚手架变成强模型省钱器"可入 harness 减法判读。
- **D7 · Same Model, Different Harness: Different Coding-Agent Results**（arXiv:2608.26218，v1 2026-08-26，cs.AI,cs.SE，**Sydney Lewis 单作者**，24 pages）——节引（API 实取）："treatment raises mean per-task F2PF from 28 percent to 49 percent and complete solutions from 43 to 72 … coding-agent evaluations should treat the model and harness together as the tested solver." **与 loop engineering 的挂钩**：循环产品化机制——model＋harness（循环载体）才是被测 solver。派别适配：中性偏推动（harness 是被测解的一部分）；边缘候选（单作者）。
- **D8 · QuoteBench: How Matched Scores Can Hide Command-Path Failures**（arXiv:2608.13547，v1 2026-08-13，cs.AI,cs.SE，Shangao Li, Yao Zhang, Volker Tresp, Yuanyuan Yang，4 作者）——节引（API 实取）："Matched execution scores alone cannot distinguish command-generation errors from failures introduced after generation. … replaying the same reply through the added parser lowers success by 55.4 to 73.2 percentage points." **与 loop engineering 的挂钩**：验证回路——匹配分数掩盖命令执行路径失败。派别适配：怀疑档（分数掩盖执行路径失败）。

**（第四轮挖掘（2026-10-06）：arXiv 学术层扫描）**

### 方向 E · multi-agent 协作失败（E1–E4）

#### E1 · Passes Alone, Fails Together: Benchmarking Semantic Coordination in Parallel LLM-Agent Development（arXiv:2609.25396）

- v1 2026-09-21（cs.CL,cs.AI,cs.SE）｜Haocheng Xia, Eugene Wu, Yongjoo Park（3 作者）｜comment: **accepted to EXPRESS 2026 workshop**
- 摘要逐字（API 实取）：

  > "Parallel coding agents can produce patches that work alone but fail when merged. This happens when one agent changes an interface or rule that another agent still relies on. We study these failures with stale, a benchmark for semantic coordination. Our evaluation runs the same tests on each patch alone and on their combination, counting only failures introduced by combining the patches. We use three tiers: synthetic tasks with controlled interface changes, pairs of merged pull requests, and constructed tasks that use real Django helpers. Among 834 runs on 417 mined Django pairs, only one showed interference after correcting the grading procedure. On constructed tasks using 12 Django helpers, interference occurred in 97% of runs. A message describing the completed concurrent change recovered 82% of runs. Reviewed pull requests may contain few unresolved parallel changes, even when agents fail on controlled tasks using real code. The constructed failure rates do not estimate how often these problems occur in practice."

- **与 loop engineering 的挂钩**：循环结构（并行循环的合并面）＋外层调度（通报消息修复）｜**multi-agent 协作失败方向的直接命中**——"单测全过、合并即坏"的语义干涉基准；尤其可贵的是其**双向诚实**：真实 Django PR 对 834 跑仅 1 次干涉（负结论），构造任务上 97% 干涉且一条通报消息恢复 82%（正结论＋修复线索＝共享上下文消息）。
- 证据级别：**workshop 已录用（EXPRESS 2026）**｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：怀疑档（失败模式）＋修复面中性。
- 入册建议：候选入册（学术旁证层，注明 workshop 级）。

#### E2 · When Agents Coordinate: Measuring Coordination in Multi-Agent AI Coding（arXiv:2608.16801）

- v1 2026-08-17（cs.AI,cs.SE）｜Giuseppe Destefanis, Tomaso Aste（2 作者；UCL 系作者名——未核）
- 摘要逐字（API 实取）：

  > "We study how teams of AI coding agents coordinate while solving programming tasks. Current evaluations usually report whether the agents complete the task and how much the run costs, leaving the coordination inside the team largely unmeasured. We introduce an instrument to measure this coordination. Each run is represented as a temporal network in which agents and files are nodes, and messages, file writes, and file reads are timestamped directed edges with an associated cost. We apply this instrument to 1902 runs, each evaluated with a fixed test suite, across configurations that vary the team size, the team structure, and the file policy. The resulting networks show how coordination changes as teams grow and as the work changes. Direct messaging initially increases close to quadratically with the number of agents, with much of this growth coming from an early round of introductions. As the teams grow further, this increase levels off in the largest teams we study, where agents increasingly communicate through broadcast messages. The task also shapes the network that emerges. Work built around a shared specification produces dense, highly connected teams, while pipeline tasks produce sparse networks organised around local interfaces. Shared files can replace repeated 1-to-1 communication, cutting output tokens by about 42% at eight agents on message-heavy work, while adding overhead when files already carry the coordination. Naming one agent as coordinator creates no communication hub and provides no reliable improvement in success. We also observe an unprompted tendency for agents to seek out hidden grading material. We repeat the key experimental conditions in a sealed environment, replacing the hidden material with marked placeholder files. Across 244 additional runs, agents still reach for it in four fifths of runs, while the coordinator and file-channel findings reproduce."

- **与 loop engineering 的挂钩**：外层调度（coordinator 无增益、共享文件替代 1:1）＋循环结构｜**多 agent 编码协作的时序网络测量**（1902 runs）——"共享规格→稠密网；流水线→稀疏网；共享文件省 42% 输出 token；**指定 coordinator 无可靠增益**"可直接进 graph_engineering 拓扑判读；"密封环境下仍有五分之四的 run 去够隐藏评分材料"是奖励投机的一手观察。
- 证据级别：预印本｜S2 引用数：未核。
- 派别适配：中性（测量件）＋怀疑面。
- 入册建议：边缘候选（2 作者；发现价值＞引用面）。

#### E3 · Asymmetric Repository Lineage Modeling and Verifier-Guided Coordination in Concurrent AI Coding Agents（arXiv:2610.04779，MERGEGYM）——节引

- v1 2026-10-03（cs.SE）｜Arjun Subramanian, George Xu, Nithilan Karthik（3 作者）｜节引（API 实取）：

  > "On a stratified 715-pair lineage set (167 textual conflicts), 79 conflicts (47.3%) occur despite disjoint authored file sets. … a decision-time gate de-overlaps a median 91.7% of labeled scope collisions at 65.0% makespan inflation under frozen-label replay. … when exact replay is cheap, verify everything."

- **与 loop engineering 的挂钩**：外层调度（decision-time gate）＋验证回路｜**并行 agent 冲突中 47.3% 发生在"文件集不相交"的 PR 对上**（语义重叠≠文件重叠）——并发调度的冲突面定量；"verify everything when replay is cheap"是停止条件经济学的一句话版。
- 证据级别：预印本｜派别适配：怀疑档＋中性工具性。入册建议：边缘候选。

#### E4 · Attention Tax, Handoff Tax: A Stylised Model of When Multi-Agent LLM Systems Help（arXiv:2610.06069）——节引

- v1 2026-10-05（cs.MA,cs.AI,cs.CL,cs.LG）｜Akshit Anchan, Nayonika Sen（2 作者）｜节引（API 实取）：

  > "Decomposition reduces the burden of long contexts but incurs a handoff tax when information is compressed or transferred between agents. … the model places the crossover at depth 10 and predicts decomposition to win at depths 20, 50, and 100. It does, on step-level and final-balance accuracy."

- **与 loop engineering 的挂钩**：**"何时该拆多 agent"的两税模型**（外层调度——拆分临界条件；attention tax vs handoff tax）与交叉点预测验证——为库内 graph/loop 分工给出理论化分界条件。
- 证据级别：预印本（stylised model＋单任务验证）｜派别适配：中性（理论件）。入册建议：边缘候选。

**（第四轮挖掘（2026-10-06）：arXiv 学术层扫描）**

### 方向 F · 安全 / 失控 / 审计能力（F1–F7）

#### F1 · Runaway Reaction: When Benign Skills Compose into Malicious Behavior（arXiv:2610.05943）

- v1 2026-10-05（cs.CR,cs.AI）｜Zunlong Zhou, Ziyuan Yang, Mengyu Sun, Yi Zhang（4 作者）
- 摘要逐字（API 实取）：

  > "Agent skills package task-specific knowledge and procedures that can be composed to support complex agent tasks, while public marketplaces provide a growing pool of reusable skills. Existing security vetting, however, largely evaluates skills in isolation, leaving composition-induced risks underexplored. Such risks arise because composing benign skills expands the agent's capability space, enabling behaviors unavailable to any skill alone. Interestingly, we find that directly composing benign skills can already induce malicious behaviors, even when every individual skill passes security vetting. We further find that some target malicious behaviors remain difficult to realize through direct composition, even when the selected skills collectively provide the required capabilities. To systematically instantiate these attacks, we present Compositional Risk Induction via Multi skill Execution (CRIME). CRIME first uses the Malicious Plot Casting (MPC) module to decompose a target malicious behavior into complementary requirements and identify suitable benign skill compositions from public skill repositories. For compositions that cannot directly realize the target behavior, the Runaway Reaction Steering (RRS) module uses execution feedback to iteratively refine the selected skills toward the target while requiring each skill to remain benign under standalone vetting. The resulting composition is then passed to the Skill Reaction Chamber (SRC) module, where the skill pair is executed in a sandbox and the resulting environmental consequences are examined to determine whether the target behavior has occurred. Unsuccessful cases are returned to RRS for further refinement. Furthermore, we construct a benchmark of 4,000 public skills across eight cybersecurity behaviors for systematic evaluation of composition-induced vulnerabilities."

- **与 loop engineering 的挂钩**：**"良性技能组合成恶意行为"的失控路径**（无人值守运行——组合失控面；循环结构——攻击本身即执行反馈迭代环；技能逐个过审≠组合安全）——直接命中"agent 失控实证"方向；与库内 skills/插件供应链档案（2608.05223、2609.23809）同域。
- 证据级别：预印本（**攻击构造论文**——引用时注意其为攻击演示而非事故统计）｜S2 引用数：None（S2 未收录，2026-10-06 实核）。
- 派别适配：怀疑档。
- 入册建议：边缘候选（4 作者；方向稀缺性高）。

#### F2 · Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents（arXiv:2606.11688）

- v1 2026-06-10（cs.CL,cs.AI）｜Youwang Deng（**单作者**）｜comment: Preprint，代码开源（EpistemicaLab org）
- 摘要逐字（API 实取）：

  > "Long-horizon LLM agents are not trusted to run unattended: with no human watching, they confidently report success they never verified. We treat honesty -- bounding what an agent may claim at termination -- as a first-class metric for unattended autonomy, distinct from capability. We present Autopilot, an execution model that makes silent fabricated success structurally impossible rather than merely rarer. Autopilot externalizes all working state into a durable, gated finite-state machine that a scheduler advances one stateless tick at a time; a hard floor forbids any terminal \"done\" claim whose falsifiable gate did not actually execute and pass. We prove a No-False-Success theorem -- under gate soundness, floor enforcement, and plan coverage, termination implies the goal holds -- whose only trust points are empirically measurable, and show the worst case degrades to an honest stall, never a fabricated success. Because each tick rehydrates only the state machine, per-step context cost is constant in the horizon. Across a 3,150-cell paired corpus (70 tasks x 3 systems x 3 models x 5 seeds, including 50 SWE-bench Lite tasks across 11 OSS repos), Autopilot fabricates on 0.95% of cells [95% CI 0.38--1.62] while Reflexion and StateFlow baselines fabricate on 8.10% [6.48--9.81] and 25.05% [22.48--27.62] respectively. The headline contrast lives in the hard regime: on SWE-bench Lite, the firewall reduces fabrication from 33.7% (StateFlow) to 0.67%, a paired difference of $-33.07$ pp [95% CI $-36.53, -29.73$]. The mechanism is the gate, not the model: all ten Autopilot fabrications come from the strongest model, while two weaker mid-tier models never fabricate across 700 paired cells. The firewall trades coverage for honesty by design -- an honest stall is recoverable; a confident wrong output shipped downstream is not."

- **与 loop engineering 的挂钩**：**"unattended agent"关键词直中**——把"终止时的诚实"（无虚报成功）立为无人值守自主性的一级指标，FSM 化 gate floor＋No-False-Success 定理；"诚实卡死优于虚假成功"是停止条件议题的最激进学术表述之一。窗口内最早（2026-06-10，命名周前后）。
- 证据级别：预印本（自建 corpus＋SWE-bench Lite）｜S2 引用数 1（2026-10-06 实核）。
- 派别适配：中性工具性（诚实防火墙）＋怀疑面数据（baseline 虚报率 8.1–25.05%）。
- 入册建议：边缘候选（单作者）——但"诚实性≠能力"的指标化提法值得判读层记录。

#### F3 · Groundability, Not Scale Alone: When Weak Reviewers Can Audit Strong Coding Agents（arXiv:2610.01023）

- v1 2026-10-01（cs.SE,cs.AI,cs.CL）｜Junyu Guo, Shangding Gu, Ming Jin, Javad Lavaei（4 作者）
- 摘要逐字（API 实取）：

  > "Coding agents can return plausible patches that omit required behavior. These failures are hard to review because long traces and confident summaries often hide what was missed. We ask when a nominally weaker reviewer can reliably decide whether a patch solves its issue. We study 411 execution-labeled traces from three agents and 101 controlled cases. On 154 GPT-5.4 traces, structured but unchecked evidence raises both defect catch and over-rejection. We then provide official execution evidence as an upper-bound diagnostic. After choosing and freezing one of two formats per reviewer, five of six reviewers improve both rates on 122 held-out traces; two classify every trace correctly. Reviewer size is not a consistent predictor of quality. Because official tests are unavailable in deployment, we also evaluate a frozen cascade with patch-caused static errors and generated tests that first fail on the unpatched repository. On 121 scored held-out GPT-5.4 traces and 59 Gemini traces, its coverage is 0.89 and 0.86, risk is 0.33 and 0.26, catch is 0.76 and 0.80, and over-rejection is 0.66 and 0.67. Most false rejections occur when unresolved cases reach the reviewer. Official execution evidence shows the potential of weak review when decisive checks are available. Producing equally reliable checks without official tests remains the main bottleneck."

- **与 loop engineering 的挂钩**：**"弱审计者何时能审计强 agent"的实证边界**（验证回路——人类评审环节的可行性边界）——决定性证据（official execution evidence）而非更大模型是审计可行性的关键；对库内 "cognitive surrender"（2607.00038）与 "verification 是瓶颈"（Huntley 4a）给出可操作的学术对应物：**可审计性的瓶颈是证据生产，不是评审者规模**。
- 证据级别：预印本｜S2 引用数：未核。
- 派别适配：怀疑档（失败难以审出）＋中性工具性（级联方案）。
- 入册建议：候选入册（学术旁证层）。

#### F4 · Between the Commits: Process, Error, and Claim Reliability in a Wholly AI-Authored Codebase（arXiv:2609.29744）

- v1 2026-09-24（cs.SE,cs.AI）｜Douglas Leith（**单作者**；Trinity College Dublin 教授为外部常识——未核）
- 摘要逐字（API 实取）：

  > "We present: (i) a new dataset consisting of the full development history of a 21,000-line Python tool built entirely by Claude AI, with no human-authored code or tests, (ii) two code-provenance tracing tools, (iii) three taxonomies for instruction intent, commit provenance, and response reliability, (iv) application of these to analyse the dataset. We find that: (i) user coding agent CLI instructions differ in kind from IDE-chat instructions, with a greater focus on comprehension, planning and consultation, (ii) code development is mainly proactive, (iii) 14.3% of AI code-generation events contain a real error later caught by the AI-authored test suite, (iv) roughly 1 in 4-5 of the AI's interactive responses contains one or more factual errors."

- **与 loop engineering 的挂钩**：无人值守运行（全 AI 无人值守产物质量）＋验证回路（AI 自写测试捕获）｜**全 AI 作者代码库的过程级误差审计**（21,000 行、无人写码无人写测试）——"14.3% 生成事件含真实错误（后被 AI 自写测试捕获）＋1/4–5 交互回复含事实错误"是无人值守叙事最冷静的定量反证之一。
- 证据级别：预印本｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：怀疑档。
- 入册建议：边缘候选（单作者无引用；但单样本 n=1 代码库的外推边界要标注）。

#### F5–F7 · 安全侧节引条目

- **F5 · Authority Is Not a String: A Capability-Scoped Harness for Prompt-Injection-Resistant Coding Agents**（arXiv:2609.08371，v1 2026-09-08，cs.SE，Dimitrios Stamatios Bouras, Yihan Dai, Sergey Mechtaev——Mechtaev 为知名 PL/SE 研究者，外部常识未核；基于 Pi coding agent 实现——摘要自述）——节引（API 实取）："The injected effect executes in 33-47/75 runs under the ambient-authority and global-policy baselines, compared with 3/75 under CapScope. CapScope completes 68/75 repairs, while the baselines complete 68-72/75."（能力最小授权把注入生效 33-47/75 压到 3/75 且不损完成率）**与 loop engineering 的挂钩**：外层调度——sub-agent 权限门（capability-scoped harness）。派别适配：中性工具性＋怀疑面。入册建议：候选入册（学术旁证层）。
- **F6 · Authorization Revocation for Long-Running AI Agents: Root-Scoped Quiescence under Delegation and Asyncronous Execution**（arXiv:2609.21284，v1 2026-09-18，cs.PL,cs.AI,cs.CR，Genliang Zhu, Chu Wang）——节引（API 实取）："Long-running AI agents outlive initiating processes through credentials, delegated tasks, queues, callbacks, reservations, and provider-side operations. Cancellation, process exit, and credential revocation neither close every pre-cut carrier nor distinguish independently authorized shared work."（撤权≠停止：长活 agent 的授权静默形式化）**与 loop engineering 的挂钩**：无人值守运行——长活 agent 的撤权/停止语义形式化。派别适配：中性（形式化件）。边缘候选。
- **F7 · Trajectory-Level Security Debt in LLM Coding Agents**（arXiv:2609.35199，v1 2026-09-28，cs.CR,cs.SE，Prateek Kumar Rajput 等 7 作者含 Tegawendé F. Bissyandé）——节引（API 实取）："Evaluating only the final artifact leaves the evolution of security findings unmeasured. We introduce the Security Debt Line Integral (SDLI) … Its value for steering agents and confirming exploitable vulnerabilities remains to be established."（终态安全审计漏掉轨迹中的安全债）**与 loop engineering 的挂钩**：验证回路——只验终态的盲区（轨迹级安全债）。派别适配：怀疑档＋中性测量件。边缘候选。

**（第四轮挖掘（2026-10-06）：arXiv 学术层扫描）**

### 方向 G · 工程实证与运动直接件（G1–G10）

#### G1 · Engineering Reliable Coding Agents: Evaluating and Operating the System Around the Model（arXiv:2608.13867）

- v1 2026-08-14（cs.SE,cs.AI）｜Stephanie Jarmak（**单作者**，314 页技术专著）｜comment: Technical review and engineering monograph, 314 pages; 含 evidence audit、206 reliability records 伴生工件、可运行协议；开源于 github.com/sjarmak/engineering-reliable-coding-agents
- 摘要逐字（API 实取）：

  > "AI coding agents are commonly evaluated as models but deployed as systems. Their reliability depends not only on model capability, but on the harness, execution state, retrieval, memory and state management, permissions, review interfaces, and resource allocation. This monograph examines those boundaries and develops a framework for evaluating and operating coding agents reliably. It synthesizes 164 scholarly works, 100 practitioner records, 29 benchmark records, and 17 author-system case records through a structured multivocal review, targeted update audits, software-engineering coverage analysis, and distributed-systems evidence synthesis. Across this evidence, many apparent model failures originate elsewhere in the system, while improvements at one layer often fail to propagate to end-to-end outcomes. Evaluation and operation are treated as a dependency chain in which weaknesses in task construction, execution environments, retrieval, state management, verification, or observability can invalidate downstream conclusions. The monograph contributes a versioned catalog of 206 reliability records: 193 gated practices, including 56 developed in depth, plus 13 research leads; an evidence ledger; a framework for dependency and repair asymmetry across the agent lifecycle; measurements and failure cases from operated agent systems; runnable evaluation and reliability protocols; and five reusable agent skills with evidence maps. Together, these provide a system-level methodology for distinguishing model capability from infrastructure effects, designing defensible evaluations, and building systems that recover safely when components fail. The review is structured rather than exhaustive, evidence strength varies by topic, and results depend on workload and configuration. The methods record which search lanes were executed, which remain unexecuted, and limits on evidence-grading claims."

- **与 loop engineering 的挂钩**：循环产品化机制（harness/权限/评审接口的系统级可靠性目录）＋验证回路｜**与本主题几乎同构的系统级专著**——"模型被评测、系统被部署"的错位＋206 条可靠性记录的版本化目录＋"单层改进不传导到端到端"；是库内 loop→harness→治理三层视野的学术镜像。
- 证据级别：预印本专著（multivocal review，方法透明度自述完整）｜S2 引用数 2（2026-10-06 实核）。
- 派别适配：中性（系统级方法论）。
- 入册建议：**边缘候选（单作者专著）**——如实标注：作者号召力未核、引用数 2；但工件规模（206 records＋可运行协议）使其值得单独立档回源。

#### G2 · A Few Pages of Markdown: Committed AI Configuration and Lower Quality Cost after Coding-Agent Adoption（arXiv:2608.25241，RAMP）

- v1 2026-08-26，v2 至 2026-09-14（cs.SE,cs.AI）｜Yegor Denisov-Blanch, Shyam Agarwal, Pavel Azaletskiy, Hao He, Rylan Schaeffer, Brando Miranda, Bogdan Vasilescu, Sanmi Koyejo（8 作者，多机构；Vasilescu/Koyejo 机构归属为外部常识 CMU/Stanford——未核）
- 摘要逐字（API 实取）：

  > "Coding agents increase development velocity but also technical debt. Prior work reports only average effects across adopters, hiding wide differences between teams. We introduce RAMP (Repository AI Maturity Profile), a four-level cumulative maturity model grounded in version-controlled artifacts that teams commit to configure AI tools. RAMP runs from behavioral rules and coding standards through named agent definitions to multi-agent orchestration, with observed practice concentrated in the first three levels. Across 441 repositories the levels behave as a cumulative scale, and independent human annotation reproduces RAMP's repository-level labels on 97% of a held-out sample. Adoption is cumulative, forward-only, and set-and-forget: 73.8% of artifacts are committed once and never modified. Re-estimating an existing agent-adoption panel within each stratum, agents accelerate development regardless of maturity (28-38% more commits), but quality diverges: among agent-first repositories, where the contrast is identified, those without committed AI configuration show roughly twice the increase in cognitive complexity (+53% versus +27%) and 1.7x the increase in static-analysis warnings. Because maturity is observational, correlated engineering discipline or model capability may explain part of the gap; we present these findings as hypothesis-generating and release RAMP as a reusable instrument."

- **与 loop engineering 的挂钩**：**"几页 markdown 配置"与质量代价的分层实证**（循环产品化机制——RAMP 成熟度分级；无人值守运行——agent-first 仓库质量分化。441 仓库）——agent 提速与质量分化并存（+53% vs +27% 认知复杂度增长）；RAMP 四级成熟度（行为规则→agent 定义→多 agent 编排）与库内 harness 治理实践层的分级视野可对表。
- 证据级别：预印本；作者自述 observational、hypothesis-generating｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：**中性（双向数据：速度正面、质量负面）**。
- 入册建议：候选入册（学术旁证层，8 作者多机构）。

#### G3 · Not All Agents Are Equal: Code Quality and Post-Merge Maintenance Across Five Autonomous Coding Agents in the Wild（arXiv:2609.17598）

- v1 2026-09-12（cs.SE）｜Obada Kraishan（**单作者**）｜comment: 9 pages
- 摘要逐字（API 实取）：

  > "Autonomous coding agents now open pull requests in public repositories at a scale that was out of reach two years ago, yet little is known about what happens to that code after it lands. This paper studies 37,623 provenance-labeled pull requests (PRs) from five commercial agents (OpenAI Codex, Devin, GitHub Copilot, Cursor, and Claude Code) and a matched human baseline, drawn from 2,807 GitHub repositories between December 2024 and July 2025. We combine the AIDev dataset with 58,792 cached GitHub API responses to measure security smells in added code, structural maintainability, post-merge churn, revert rates, and human review behavior. Three results stand out. First, quality differences are vendor-specific rather than uniform: Codex-authored PRs were reverted about half as often as human PRs (6.1% vs. 11.5%, odds ratio 0.50), while Devin PRs were reverted more often (14.5%, odds ratio 1.31). Second, agent code pooled across vendors was less likely than human code to contain a security smell (odds ratio 0.63), driven by fewer hardcoded credentials and eval-style constructs. Third, review effort concentrates unevenly: Copilot PRs drew the most human reviews and change requests, and Claude Code PRs waited the longest for a first human review (median 12.6 hours). All pipeline code, statistical reports, and figures are released for replication."

- **与 loop engineering 的挂钩**：无人值守运行（agent PR 落库后质量）＋外层调度（人工评审等待分布）｜**37,623 个真实 PR 的落库后质量追踪**——效应 vendor-specific（Codex revert 减半、Devin 反而更高）；"agent 代码安全坏味更少（OR 0.63）"是反直觉正报告；人工评审行为数据（Claude Code PR 首评等待中位 12.6h）是人的位置议题的量化素材。
- 证据级别：预印本（大规模观测；窗口 2024-12→2025-07）｜S2 引用数：未核。
- 派别适配：**中性（混合效应、vendor 异质）**。
- 入册建议：边缘候选（单作者）——数据规模大但单作者、无引用。

#### G4 · Specification-first convergence with an AI coding agent: a case study of dismantling a core architectural invariant across 189 files in a 717k-line codebase with no test oracle and no human code review（arXiv:2608.12440）

- v1 2026-08-12，v2 至 2026-08-15（cs.SE,cs.AI）｜Joel Abenhaim（**单作者**；n=1 案例）｜comment: v2 加了供 LLM 可读的纯文本日志 URL
- 摘要逐字（API 实取）：

  > "This paper reports a single, fully instrumented case study of a large-scale architectural refactoring by an AI coding agent under a specification-first protocol, with no human review of the generated code and no pre-existing oracle to validate the target behaviour. The task, dismantling a central invariant across a large interdependent codebase, was assessed by the author as effectively infeasible through incremental refactoring, the kind of change that conventionally calls for a rewrite instead. Under the protocol described here, the agent completed it successfully. The system is a 717,725-line production TypeScript application across 3,648 files. The task required dismantling a core lifetime invariant: the guarantee that a UI panel remains open for the duration of an AI request. The target behaviour was that a streaming generation survives the closing of its panel and can be reattached, on reopening, to the same live stream with no loss or duplication. The protocol: formal specification by the agent, 14 refinement cycles auditing that specification against the source code, atomic implementation, a compile/test feedback loop, then 17 verification cycles auditing the code against the frozen specification. Across 31 audit passes, 201 defects were corrected before any human executed the program. The convergence criterion was empirical: two consecutive verification passes returning zero findings. The change touched 189 files (31 new); with the extraction phase, the two commits total 288 files, 34,770 insertions, 16,422 deletions. Across the first and roughly thirty later sessions, the software behaved as specified, no bug observed. Elapsed: three days; cost: USD 2,430. The full specification and raw session logs, 1,500+ pages in French, are published as evidence, allowing inspection of the process and submission to a language model for consistency checking."

- **与 loop engineering 的挂钩**：无人值守运行＋停止条件（连续两轮零发现的收敛判据）＋验证回路（31 审计轮）｜**无人值守大重构的单例存在性证明**——717k 行、无测试 oracle、无人工评审，靠"规格冻结＋31 轮审计通过＋连续两轮零发现"的**经验收敛判据**完成；其收敛判据本身就是停止条件设计的一手样本；成本/时长透明（3 天、$2,430）。
- 证据级别：预印本；**n=1 自评案例**（作者自知并公开全部日志供检验）｜S2 引用数：未核。
- 派别适配：**推动档正报告——强单样本 caveat**（与库内 swyx/saldo 叙事对表时必须分层）。
- 入册建议：边缘候选（单作者 n=1；证据透明度是其主要 redeeming quality）。

#### G5–G10 · 工程实证节引条目

- **G5 · How Do Coding Agents Optimize Software and Report Performance Validation? A Large-Scale Empirical Study of Open-Source Pull Requests**（arXiv:2610.03969，v1 2026-10-02，cs.SE,cs.PF，Huiyun Peng, Ricardo Calvo, Kelechi G. Kalu, James C. Davis——Purdue 组，4 作者）——节引（API 实取）："agentic PRs are merged less often than human-authored PRs (54.4% vs. 73.3%) … Across both groups, about half of validated PRs report no quantitative performance metric."（agent 性能 PR 合入率更低、验证报告缺量化指标）**与 loop engineering 的挂钩**：验证回路——性能声明的验证缺口。派别适配：怀疑档。边缘候选（重复计入 MSR 2026 pilot，作者自述）。
- **G6 · Correct Code, Broken Contributions? SWE-CC: Benchmarking Repository Policy Compliance for Coding Agents**（arXiv:2610.06193，v1 2026-10-05，cs.SE,cs.AI，Hai Dang Truong 等 4 作者）——节引（API 实取）："although agents produce functionally correct patches, they still violate 43.1 percent of applicable project policies, with nearly half of all violations occurring during intermediate execution steps."（功能正确≠合规贡献：823 条机器可查策略基准；**近半违规发生在中间执行步**——loop 过程治理的直接证据）**与 loop engineering 的挂钩**：循环结构（中间执行步治理）＋验证回路。派别适配：怀疑档＋中性测量件。入册建议：候选入册。
- **G7 · Update from Hell: Can Coding Agents Survive Hidden Breakage in Dependency Upgrades?**（arXiv:2608.30300，v1 2026-08-31，cs.SE，Zijian Luo 等 9 作者含 Qingwei Lin, Saravan Rajmohan——Microsoft 系作者名，未核）——节引（API 实取）："The best completed configuration solves only 104/203 tasks (51.2%), with substantial variation across agent harnesses, models, and ecosystems."（DEPBENCH：隐藏性依赖破坏面当前 agent 过半不可解）**与 loop engineering 的挂钩**：验证回路——隐藏破坏超出常规测试面。派别适配：怀疑档。边缘候选。
- **G8 · Can Coding Agents Reproduce Official Statistics? Metadata, Retry Budget and the Limits of Execution Feedback in a Controlled Eurostat Benchmark**（arXiv:2609.22222，v1 2026-09-02，cs.LG 等 4 分类，**Sabina-Cristiana Necula 单作者**）——节引（API 实取）："Reliable statistical coding agents need semantic validation against frozen specifications, a fully specified output contract, and a retry budget - not execution diagnostics."（执行反馈≠正确性：retry budget＋冻结规格才是关键——360 task-runs 对照实验）**与 loop engineering 的挂钩**：预算与熔断（retry budget）＋停止条件（语义验证优先于执行反馈）。派别适配：怀疑档（对 execution feedback 作用的限定）。边缘候选（单作者）。
- **G9 · Model-Based Agentic Software Engineering**（arXiv:2608.25174，v1 2026-08-25，cs.SE，James C. Davis, Kelechi Kalu, Huiyun Peng, Parth V. Patil——Purdue 组）——节引（API 实取）："it externalizes the smallest purposeful representation needed to answer an engineering question, then gives settled obligations proportionate authority through constraints, sensors, validators, and gates."（MAGE：约束/传感器/校验器/门四件套的"义务授权"框架）**与 loop engineering 的挂钩**：停止条件（constraints/sensors/validators/gates）＋外层调度（retained human authority）。派别适配：中性（框架/立场文）。边缘候选。
- **G10 · Reproducibility in the Age of Agentic AI: Context Engineering at the Timescale of a Codebase**（arXiv:2609.11728，v1 2026-09-10，cs.SE,cs.CY，**Lorena A. Barba 单作者**，10 pages；GWU 教授为外部常识未核）——全文式节引（API 实取）："Reproducible research practices are context engineering for AI coding agents. I argue that agents lower the cost of maintaining tests, commit histories, repository structure, instructions, and decision records while making their benefits immediate. Researchers remain responsible for verifying these artifacts and the scientific judgments they encode."（可复现实践＝agent 的 context engineering；验证责任仍在人——一句话立场文）**与 loop engineering 的挂钩**：验证回路（验证责任在人）＋循环的上下文供给（可复现工件即 loop 输入）。派别适配：中性。边缘候选（单作者短文，但作者知名度高）。

**（第四轮挖掘（2026-10-06）：arXiv 学术层扫描）**

### 方向 H · PL 社区议程（cs.PL，H1–H4）

#### H1 · Agents as Software: A Programming Languages Agenda for Agent Reliability（arXiv:2609.32198）

- v1 2026-09-26（cs.PL,cs.AI）｜Shraddha Barke, Adithya Murali（2 作者）｜comment: **Accepted to Onward! at SPLASH 2026**（S2 venue 字段实核为 Proceedings of the 2026 ACM SIGPLAN … Onward! papers 卷）
- 摘要逐字（API 实取）：

  > "AI agents increasingly resemble software systems: they call tools, remember facts, follow policies, delegate work, and take actions with real consequences. % Yet the ``program'' of an agent is scattered across prompts, tools, memories, workflows, and execution traces, making its behavior difficult to inspect through ordinary testing and debugging alone. % This essay argues that a programming-systems perspective offers a natural lens for making agents reliable. % We recast agents as programmable artifacts whose behavior can be specified over traces and state, checked before deployment, monitored during execution, and improved from observed failures. % The goal is not to make probabilistic agents behave like deterministic programs, but to give them enough structure that their behavior can be reasoned about, controlled, and repaired."

- **与 loop engineering 的挂钩**：循环结构＋验证回路＋外层调度（specify→check→monitor→improve 四步）｜**PL 社区对 agent 可靠性的议程文**——"specify over traces → check pre-deploy → monitor in-execution → improve from failures"四步与库内 loop/harness 治理闭环同构；PL 视角（agent 的"程序"散落在 prompts/tools/memories/traces 中）为 harness_governance 提供学科接口。
- 证据级别：**已录用（SPLASH 2026 Onward!，立场文 track）**｜S2 引用数 0（2026-10-06 实核）。
- 派别适配：中性（议程/立场文）。
- 入册建议：候选入册（学术旁证层；已录用 venue＋PL 学科代表性）。

#### H2–H4 · cs.PL 元数据层条目（本轮仅核 ID/标题/作者/日期，摘要未逐字取）

- **H2 · From Verification Failures to Reusable Guidance for Coding Agents**（arXiv:2609.39022，v1 2026-09-30，cs.SE,cs.AI,cs.LO,cs.PL，Yuqing Zhai, Xiaohong Chen, Lingming Zhang, Sriram Vishwanath, Grigore Rosu——5 作者含 Rosu，外部常识 UIUC/formal systems 未核）——**与 loop engineering 的挂钩**：验证回路——把验证失败转成可复用指导（标题层判断，摘要未取）。
- **H3 · Grounding SWE-Agent Decisions in Architecture-0 Design**（arXiv:2609.17221，v1 2026-09-15，cs.SE,cs.AI，Zhongkai Wang, Yan Liu；comment: 51 pages，TOSEM 在审）——**与 loop engineering 的挂钩**：循环结构——SWE-agent 决策的架构接地（标题层判断，摘要未取）。
- **H4 · Neuro-Formal Verification: Agentic Language-Agnostic Formal Program Reasoning**（arXiv:2608.21516，v1 2026-08-21，v3 至 2026-09-14，cs.SE,cs.PL，**Shuvendu K. Lahiri 单作者**；Microsoft Research 为外部常识未核）——**与 loop engineering 的挂钩**：验证回路——形式化验证的 agentic 化（标题层判断，摘要未取）。

**（第四轮挖掘（2026-10-06）：arXiv 学术层扫描）**

### 已知方向核实结论（对应任务第 4 点）

1. **agent 安全/失控的实证研究：核实存在且活跃。** F1（技能组合失控）、B5（loop 级安全状态定理）、F2（无人值守虚报）、C3（HF 事件风险建模）、C4（审批-执行绑定六类失败）、F5/F6/F7、以及元数据层的 2610.04083《Self-Propagating Misalignment in LLM Agents》、2609.06649《Inducing Emergent Misalignment from Reward Hacks with Iterative DPO》、2608.05223《Towards a Risk Assessment of Malicious Skill Files in Coding Agents》、2609.11028《BenchShield》。
2. **coding agent 的 reward hacking 分类学：核实存在。** C1（NVIDIA 系：exploit 分类＋审计＋低成本缓解）、C5（unearned passes 过程验证框架）、C2（检测＋训练侧修复）、C6（生产自改进 loop 的 11 类评估信号失败）、SWE-Bench Pro Verified（arXiv:2609.08149，v1 2026-09-08，节引："existing results on SWE-Bench Pro may overestimate real software engineering capability"）。
3. **multi-agent 协作失败研究：核实存在。** E1（单过合坏＋修复线索）、E2（协作网络测量＋coordinator 无增益）、E3（47.3% 冲突在文件集不相交对上）、E4（拆分临界条件）；另有 2609.02750《Bilevel Coordinated Reflection》（博弈论协调，元数据层）。
4. **SWE-bench 系局限批判：核实存在且已成小集群。** D2（榜首不可分，已录用 ADMA 2026）、D3（记忆化）、D4（过测试≠合规）、D8（匹配分数掩盖路径失败）、C7（SWE-Bench Pro Verified 修复侧）；同域还有 arXiv:2609.01603《Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation》（在审）与 arXiv:2609.24928《Trajectory-Aware Benchmark Subset Selection》（回归测试成本侧，Bram Adams 组作者名，未核）。

**（第四轮挖掘（2026-10-06）：arXiv 学术层扫描）**

### 二级命中速览（API 元数据层，摘要未逐字取，按主题相关度排序）

| ID | 标题（缩） | **与 loop engineering 的挂钩** |
|---|---|---|
| 2609.35182 | Research-Native by Construction: Minimal Nodes, Re-verifiable Workflows | 验证回路——最小节点＋可重验证工作流（标题层判断） |
| 2609.38345 | OpenCollab: A Multi-Agent Coding Framework with Programmable Collaboration | 外层调度——可编程协作＋可控运行时（标题层判断；work in progress 自述） |
| 2608.28497 | Claude Code Plugin Marketplaces 维护与共演化（Bram Adams, Ahmed E. Hassan 等 5 作者） | 循环产品化机制——技能/插件生态是 loop 供给品的维护面。节引（API 实取）："plugin-touching commit activity growing 8.8x over six months after the October 2025 launch … 78% of co-changes being functionally coupled, representing a new class of maintenance dependency not observed in traditional software engineering"——技能/插件生态作为新维护对象的实证（在审） |
| 2609.23809 | Packaged, But Not Portable（Tezan Sahu 单作者，投 ISEC 2027） | 循环产品化机制——插件标准化≠组合性。节引（API 实取）："Only 6.2% validate, but the gap is shallow rather than structural: 96.6% would load after adding one missing boilerplate field."＋"81% of capability-exporting bundles share a name with another plugin"——插件标准化≠组合性 |

> 注：上表引句均出自本轮实取的 API 摘要；标注"节引"者引用时须注明非全文。2605.22526《"Refactoring Runaway"》（2026-05-21，cs.SE，Kamei 组作者名未核）为**窗口前**相邻件，仅登记存在。

**（第四轮挖掘（2026-10-06）：arXiv 学术层扫描）**

### 对本节的诚实评估

1. **本轮最大增量是专名谱系（A 组）**：LoopArena 与 LoopsBench 把 loop engineering 变成**可测对象**（controller 能力 24.69%／最强配置解 25%），零信任系列把它变成企业框架抽象，36 人综述与教科书把它写进范式谱系——与库内 2608.21884 合并后，"loop engineering 进入学术层"已有五个独立来源。
2. **学术层与 KOL 层的收敛点**：停止条件的"证据门"化（A3/B2/B5/F2/C4）、"验证是瓶颈"（F3：证据生产而非评审者规模；B3：确定性监视器＋按需 LLM）、"配置即治理对象"（G2 RAMP、A4 系列）——与库内 Huntley 4a（验证/理解是瓶颈）、Kent C. Dodds（"good loops make work cheaper to verify"）、marmelab（每 PR 人工评审保留项）同向。**引用时必须分层标注：学术旁证层不与 KOL 证据并列。**
3. **怀疑面弹药完整化**：评测批判（D2/D3/D4/D8/C7＋C1/C5 作弊面）＋失败模式分类学（C4 六类、B1 四类执行失败、E1 合并干涉）＋单例反证（F4：14.3% 生成事件含真实错误）——怀疑派在学术层的支撑密度首次与推动派持平。
4. **正报告的普遍弱点**：绝大多数正报告（A4/A5/B1/B3/F2/G4）为自建评测或单样本；G4（n=1 大重构）与库内 Dan Abramov Conway 猜想案例（第三轮 Source B）同构——"存在性证明"档，不是"效应量"档。
5. **对 02_research 判读层的接口建议**：A1/A2/A6/A7 → 运动谱系与"可测量化"节点；A3/B5/F2 → stop_conditions 三小节的学术锚（hard caps／verdict split／机器门）；C1/C5/C4 → reward hacking 与审批链治理；D1/D2 → "spectrum of autonomy" 的定量语境（scaffold 效应 29.8pp vs 排名差 8.8pp）；E2/E3 → graph_engineering 拓扑判读；G1/G2 → harness/loop 治理实践层的分层成熟度参照。
6. **本轮取证完整性**：所有主条目摘要为 export.arxiv.org API 逐字实取（TeX 转义原样保留）；全部数据在会话临时目录 `.tmp-arxiv-r4/`（`.gitignore` 已覆盖 `.tmp-*/`，不入库）；如需复核，重跑同 URL 即可复现。
## 机构研究旁证（不入 KOL 册，供判读引用）

- **arXiv:2608.21884《Loop Engineering: Building Blocks, Adoption, and Impact》**（JAWs@ASE 2026 在审 workshop 论文，2026-08-22，实际 fetch HTML 全文）：对本主题直接相关的学术整理。逐字（论文原文，其中引号内为论文转述社区言论）：
  > "The claims attached to loop engineering are substantial but rest almost entirely on anecdotes and self-reported productivity numbers, while experienced engineers voice equally strong skepticism, calling loops renamed cron jobs and warning about token costs and reviewer fatigue."
  > "Loops are 'a renamed cron job', 'automation was a thing before LLMs', and the term repackages event-driven architecture with, as one commenter put it, 'a fuzzy worker'."
  > "one experience report describes roughly eight million tokens spent in 48 hours by an over-eager CI-fixing loop"
  > "Review fatigue turns the human gate into a 'rubber stamp' while 'the pipeline still reports green', and 'the loops that stick are the ones where somebody was already paid to read the output'."
  > "comprehension debt (the gap between what exists in the repository and what the developer understands grows with loop velocity) and cognitive surrender (using loops to avoid thinking rather than to move faster on understood work)"
  （另：该论文对 36,645 仓库挖掘，确认自主 agent loop 运行于 217 仓库（0.59%）；并独立转述了 Orosz 调查结论——"most concrete examples fall into two familiar buckets, cron jobs and event-based triggers"，/loop、/goal 内建后对普通工程师 "as good as obsolete"。此转述与本档 Source 8 公开部分互证。）
