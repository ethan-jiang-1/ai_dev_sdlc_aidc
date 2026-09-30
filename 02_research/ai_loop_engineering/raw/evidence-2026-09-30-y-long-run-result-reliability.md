---
type: evidence_archive
collected_at: 2026-09-30
collected_by: Y 路回源核验
serves: ai_loop_engineering 的 LE3 边界、stop_conditions 三件骨架、agent_goal_eval 的 goal/eval 接口
status: 一手官方文档/源码与公司一手工程帖；不新增通用成熟度刻度
quality_bar: 每条承重主张保留原始 URL、短引句或代码/参数、范围与负结论；既有证据只用指针
---

# 回源档案 Y：长程静默自主 loop 的结果可信度不是调度成熟度的单调升级

## 0. 先给结论

**已证机制**：调度解决“何时再跑、是否续轮、何时过期”；目标构造解决“什么叫完成、用哪份可见证据检查”；验收解决“谁来判、判什么、裁判是否可信”；结果可信还要有外部状态、线上观测和人工/业务校准。这些是正交控制面，不能合并成一个“自主度/LE3 成熟度”分数。

**工程推论（不是跨产品效果定律）**：长程静默运行至少要把以下四条线分别落账：

```text
目标可观察性 → 验收信号/裁判质量 → 资源与取消闭环 → 真实业务结果
```

因此：

- **LE3 有调度不代表结果可靠**：按时唤醒、事件触发、云端持久化只证明能再次启动或维持运行，不证明目标已达成。
- **上限停机不代表达成**：turn/time/拒绝/预算上限是安全出口，语义通常是 paused、terminated、expired 或 cancelled，不是 success。
- **分离裁判不保证准确**：独立 evaluator 可以降低“干活者给自己打分”的利益冲突，但仍可能只核 hard rules、看不到事实，或与专家不一致。
- **环境外业务结果无法观察时不称自动完成**：如果业务结果在 loop 的环境外、没有可回读的状态或遥测，只能称“产出/检查完成”或“等待人工确认”，不能称业务自动完成。

本文只写增量判读，已有逐字原文优先指向：
[`evidence-b`](evidence-2026-09-26-b-stop-and-scheduling.md)、[`evidence-l`](evidence-2026-09-28-l-quickstart-code.md)、[`evidence-n`](evidence-2026-09-28-n-verdict-split-coding.md)、[`evidence-r`](evidence-2026-09-28-r-ial-scan-reliability.md)、[`evidence-s`](evidence-2026-09-28-s-langgraph-dbt-civ.md)，以及 [`agent_goal_eval/raw/evidence-2026-09-27-a-goal-frontier.md`](../../agent_goal_eval/raw/evidence-2026-09-27-a-goal-frontier.md)、[`agent_goal_eval/raw/evidence-2026-09-27-a6-how.md`](../../agent_goal_eval/raw/evidence-2026-09-27-a6-how.md)、[`agent_goal_eval/raw/evidence-2026-09-27-b3-engineering.md`](../../agent_goal_eval/raw/evidence-2026-09-27-b3-engineering.md)、[`agent_goal_eval/raw/evidence-2026-09-27-b4-abridge.md`](../../agent_goal_eval/raw/evidence-2026-09-27-b4-abridge.md)、[`agent_goal_eval/raw/evidence-2026-09-27-b5-company-posts.md`](../../agent_goal_eval/raw/evidence-2026-09-27-b5-company-posts.md)、[`agent_goal_eval/raw/evidence-2026-09-27-c-hard.md`](../../agent_goal_eval/raw/evidence-2026-09-27-c-hard.md)。

## 1. 维度拆开：调度、验收、结果不是一根梯子

| 维度 | 它实际回答的问题 | 一手锚点 | 能推出什么 | 不能推出什么 |
|---|---|---|---|---|
| 触发/调度 | 何时开下一轮、是否跨会话继续 | Claude Code `/loop` 官方文档：<https://code.claude.com/docs/en/scheduled-tasks>；已有 [`evidence-b`](evidence-2026-09-26-b-stop-and-scheduling.md) §4c | 有时间触发、自停、20 分钟兜底、7 天过期等运行机制 | 不能推出业务结果已发生或验收准确 |
| 目标可观察性 | 完成条件是否能由运行环境/记录证明 | Claude Code `/goal`：<https://code.claude.com/docs/en/goal>；OpenAI Codex Goal：<https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex> | measurable end state、stated check、constraints/boundaries、blocked stop | 不能把模型“认为完成”升级成事实 |
| 裁判能力 | evaluator 检查的对象是否足够、是否与专家一致 | Anthropic evals：<https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents>；OpenAI eval best practices：<https://developers.openai.com/api/docs/guides/evaluation-best-practices> | code/model/human graders 各有适用面，需校准、读 transcript | 独立或自动化不等于无误报/无漏报 |
| 资源/取消 | 到预算、错误或取消时，谁停、哪些子任务仍在途 | IAL-Scan 与 OpenClaw 指针见 [`evidence-r`](evidence-2026-09-28-r-ial-scan-reliability.md) §S1、[`evidence-x`](evidence-2026-09-30-x-ladder-branches-detail.md)；Anthropic Managed Agents 见 [`evidence-w`](evidence-2026-09-30-w-ladder-runtime-detail.md) | 可把 cap 覆盖到 feedback path，并记录 cancelled/terminated 等状态 | 停下来不等于完成；取消信号到达控制面不等于所有 worker 已停 |
| 真实结果 | 外部用户/业务状态是否实际改善或发生 | Abridge：<https://tech.abridge.com/blog/offline-evaluations-to-improve-our-systems>；Shopify：<https://shopify.engineering/fine-tuning-agent-shopify-flow>；Yeret：<https://yuvalyeret.com/blog/ai-agent-completion-goals-aim-at-outcomes> | offline、online、human preference、业务遥测必须分开解释 | offline pass、激活率、偏好率都不能单独证明线上业务完成 |

这是“正交维度”的工程归纳，不是说任何产品都必须有相同 API。公开材料只足以证明这些控制问题分别存在，不足以给出跨产品可靠性函数 `reliability = f(scheduling maturity)`。

## 2. `/goal` 三值：独立但很窄的完成判定

### 2.1 已证机制：三值、fresh evaluator、只对可见条件作判断

- **原始 URL**：<https://code.claude.com/docs/en/goal>
- **短引句/参数**：官方写明 `The model returns one of three verdicts`：`Not yet met`、`Met`、`Impossible`；并写明 `completion is decided by a fresh model rather than the one doing the work`。同页还说 evaluator `doesn’t run commands or read files independently`，只判断 Claude 已在 conversation 中呈现的内容。
- **适用范围**：Claude Code 当前会话的 `/goal` Stop hook；不是所有 Claude/agent API 的通用协议。
- **对结果可信的启示**：三值是控制状态机（继续/清 goal/判不可行），不是质量分数。要让它对事实有用，目标必须把命令输出、文件状态、测试结果或其他证据显式带入可见 transcript；没有被呈现的环境外状态，evaluator 没有观察通道。

已有原文与版本/恢复边界见 [`agent_goal_eval/raw/evidence-2026-09-27-a-goal-frontier.md`](../../agent_goal_eval/raw/evidence-2026-09-27-a-goal-frontier.md) §Source 1 和 [`evidence-b`](evidence-2026-09-26-b-stop-and-scheduling.md) §4a。不要把“三值”写成“评估器能辨别真实完成”。

### 2.2 已证边界：只核 hard rules，不核“好不好”；误报/漏报不能由分离消除

- **原始 URL**：<https://addyosmani.com/blog/practical-loop-engineering/>
- **短引句**：`The evaluator sitting behind goal ... doesn’t look at the content to see if it’s good or bad ... [it] examine[s] the conversation transcript to see if the hard rules you specified have been met.`
- **适用范围**：Osmani 对 Claude Code `/goal` 的一手说明；这是产品行为边界说明，不是误报率实验。
- **对结果可信的启示**：`separate evaluator` 解决的是 maker/checker 的角色冲突，不是“内容质量已被验证”。若 hard rule 本身遗漏了关键业务条件，evaluator 可以准确地核错目标；若 transcript 的证据不完整，也可能无法确认或错误地判 impossible/met。

本条与既有 [`agent_goal_eval/raw/evidence-2026-09-27-a-goal-frontier.md`](../../agent_goal_eval/raw/evidence-2026-09-27-a-goal-frontier.md) §Source 2 互指，不复制正文。社区 issue 只作局部反例，不能升级成故障率：<https://github.com/anthropics/claude-code/issues/93744> 的作者写 `appears not to read it`，并承认这是 inference，不是源码核实。

### 2.3 已证机制：上限、错误和无进展有不同语义

- **原始 URL**：<https://code.claude.com/docs/en/goal>
- **短引句/参数**：目标条件可写 `or stop after 20 turns`；连续数轮没有 tool use 时会停并把 goal 留着；认证失败、额度耗尽、不可解决的 context overflow、模型不可用会清 goal；其他错误三次重试后暂停。
- **适用范围**：Claude Code `/goal` 文档所述实现；阈值是该产品参数，不是自主度等级。
- **对结果可信的启示**：`Impossible`、pause、cap exhaustion、error、cancel 必须和 `Met` 进入不同的结果账本。把“到上限自动停”计成 success 会系统性夸大长程完成率。

## 3. 独立 evaluator 与“测试不可改”：分离是必要条件，不是准确性证明

### 3.1 Anthropic 长程 harness：测试/规格受到保护，但完成判定仍有实现落差

- **原始 URL（官方工程文）**：<https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents>
- **短引句/代码约束**：feature list 初始 `passes: false`；coding agent 只能改 `passes`，官方明确 `It is unacceptable to remove or edit tests`；“Only mark features as ‘passing’ after careful testing”。浏览器端到端测试是另外的验证要求。
- **适用范围**：Anthropic 的长程 coding harness 设计/配套 quickstart，主要是 web app demo；不是所有生产 agent。
- **对结果可信的启示**：不可改测试描述/步骤、独立的 feature inventory 和 E2E 证据，能抑制“为了通过而改测试”的一类 Goodhart 路径；但它仍不自动证明业务结果，也不证明 agent 真按约束执行。

- **原始源码 URL**：<https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/agent.py>、<https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/progress.py>、<https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/prompts/coding_prompt.md>
- **短引句/代码**：`max_iterations: Optional[int] = None`，`None for unlimited`；驱动层 `while True` 只在 `max_iterations` 超限时 `break`；`progress.py` 只打印 `passing/total`，没有 `passing == total` 的退出分支；prompt 才写 `YOU CAN ONLY MODIFY ONE FIELD: "passes"`。
- **适用范围**：官方 quickstart 的公开 demo；不能代表 Anthropic 内部生产实现。
- **对结果可信的启示**：同一机构的“机器可核 feature list”在博客/Prompt 叙述与驱动代码的退出语义并不相同。看见进度条或 `passes` 不能证明 loop 已接上“全部通过即停机”闸门，必须追到实际 `break`/return 与 terminal outcome。

这组源码判读完整指针见 [`evidence-l`](evidence-2026-09-28-l-quickstart-code.md)；它是本档“上限停机不等于达成”的直接反例。

### 3.2 OpenAI：独立 auto-review 有角色分离，但官方也不把它当安全保证

- **原始 URL**：<https://alignment.openai.com/auto-review/>
- **短引句/参数**：`Codex sessions stop for human approval roughly 200x less often`；auto-review 对少数需审动作 `approves around 99%`；官方同时写 `Auto-review should not be treated as a guarantee of security`，并说明会在 repeated denials 后自动停止 trajectory。
- **适用范围**：OpenAI Codex 的 auto-review 研究/内部部署说明；数字不是通用 evaluator accuracy，也不是业务结果通过率。
- **对结果可信的启示**：独立审批器减少同步人工审批或提供 deny-and-continue 信号，但“约 99% 批准”不能读成“约 99% 正确完成”。安全 reviewer、完成 evaluator、业务 outcome grader 是不同问题。

OpenAI Codex 固定 commit 的执行策略源码也只回答“动作能否执行”，不回答“动作是否达成用户真正结果”：<https://raw.githubusercontent.com/openai/codex/1f4c47343a1bff2d8cddc429c5d39503fb5a6c30/codex-rs/core/src/exec_policy.rs>；源码中明确是 `Forbidden` / `NeedsApproval` / `Skip` 三态。完整边界见 [`evidence-f`](evidence-2026-09-27-f-autonomy-gates.md) §Source 1。

### 3.3 OpenAI evaluator 设计：独立/自动化不等于免校准；测试集也不能任意改成“全绿”

- **原始 URL**：<https://developers.openai.com/api/docs/guides/evaluation-best-practices.md>
- **短引句/参数**：官方要求 `Define eval objective`、收集 production/domain/historical 数据、在 `held-out set` 上评估并持续运行；明确 `Maintain agreement: Use human feedback to calibrate automated scoring`；对 LLM judge 建议 pairwise/pass-fail、清晰 rubric、与 human annotations 校准。
- **适用范围**：OpenAI API eval 设计指南；它是方法文档，不是 Codex `/goal` 实现规格。
- **对结果可信的启示**：独立 judge 需要 calibration、held-out 数据和持续维护。若 agent 可修改测试集、grader 或目标数据，得到的“全绿”只证明测试被重写或过拟合，不证明结果可信。这里可安全说“测试/裁判应由被测 agent 之外的控制面拥有”；不能把该指南扩大成 OpenAI 某个产品已实现不可修改测试。

### 3.4 独立裁判会被攻破：分离还需判据隔离与反作弊

- **原始 URL**：<https://metr.org/blog/2025-06-05-recent-reward-hacking/>
- **短引句/代码**：METR 记录 `Monkey-patch the evaluator so that every piece of code 'passes'`（`rc_utils.evaluate_rust_code = _always_ok`），并报告某一 RE-Bench 任务上 o3 `every single trajectory` reward-hacked；判定代码可见时，RE-Bench reward hacking 比 HCAST `more than 43× more common`。
- **适用范围**：METR 的 RE-Bench/HCAST 评测任务，不是生产业务 loop；是攻击面/局部反例，不是普遍发生率。
- **对结果可信的启示**：maker/checker 物理分离仍不够：还需隔离 evaluator 代码/状态、审 transcript、用独立 monitor 和人工抽查。否则“分离裁判”可能只是把错误从同一个模型移到另一个可被绕过的接口。

## 4. 机器闸门、预算和取消：停机闭环与成功语义必须分开

### 4.1 已证机制：上限必须覆盖真实 feedback path

- **原始 URL**：<https://arxiv.org/abs/2607.01641>
- **短引句/参数**：IAL-Scan 在 6,549 个 agent repositories 中报告 74 potential findings，人工确认 68 个 IAL failures across 47 projects；论文写 `An inner turn cap on a nested agent call does not cover an outer evaluator feedback cycle unless it dominates the outer feedback path`。
- **适用范围**：静态分析的公开 agent repository 样本；不是所有线上系统的 IAL 发生率，也不是业务损失测量。
- **对结果可信的启示**：worker 的单轮 cap 不能替代根控制器的总预算；外层 evaluator 反馈、retry、polling、子 agent 派生都应被 budget 覆盖。否则“每个子任务有限”仍可能整体无界。

已有代码/schema 和负结论见 [`evidence-r`](evidence-2026-09-28-r-ial-scan-reliability.md) §S1：`verified_bound`、`config_dependent_bound`、`weak_bound`、`bypassed_bound` 是 bound coverage 的区分，不是可靠性分数。

### 4.2 已证机制/局部实例：取消不是“控制台关掉”

- **原始 URL（公开任务流源码/文档）**：见 [`evidence-x`](evidence-2026-09-30-x-ladder-branches-detail.md) §A3 的 OpenClaw 源码与文档链接：<https://github.com/openclaw/openclaw>。
- **短引句/状态**：`Cancellation intent refuses new child links. The flow finalizes as cancelled once its active children have settled.`；任务状态有 `queued → running → terminal`，terminal 包括 `succeeded, failed, timed_out, cancelled, or lost`。
- **适用范围**：OpenClaw detached task/flow 的公开实现；不证明它是产品 feature 队列，也不证明有统一全树 dollar/token cap。
- **对结果可信的启示**：取消至少要区分拒绝新 child、等待已有 child 收敛、最终 cancelled；不能只把 scheduler 标成 stopped 就算副作用停止。取消完成与业务完成是两个终态。

本条是局部实现，不可和 IAL-Scan 的 budget 判据拼成“同一产品已具备全树预算+取消”的事实。跨源组合只能作为工程检查链：`root cap covers feedback path → cancel rejects new children → active children settle → terminal/cancelled is observable`。

### 4.3 已证机制：Claude `/loop` 的时间上限只是遗忘任务兜底

- **原始 URL**：<https://code.claude.com/docs/en/scheduled-tasks>
- **短引句/参数**：self-paced mode 可用 `ScheduleWakeup` `stop: true`；未续排约 20 分钟后 fallback；recurring task 创建 7 天后自动过期，官方称其为 `bounds how long a forgotten loop can run`。
- **适用范围**：Claude Code `/loop` 本地 session 调度。
- **对结果可信的启示**：7 天过期回答“忘记的循环最多活多久”，不是“任务在 7 天内一定完成”。需要在 ledger 中把 `expired` 与 `met` 分开，并记录最后一次可观察证据。

## 5. 离线量化与线上真实结果：Rippling/Abridge 的区分

### 5.1 Abridge：离线 rubric 有校准数字，但目标是方向信号，不是线上完成证明

- **原始 URL**：<https://tech.abridge.com/blog/offline-evaluations-to-improve-our-systems>
- **短引句/参数**：encounter-specific clinician-written rules；平均每次约 10 条、复杂可到 50 条；LLM rule checker 在 300 rules / 40 notes 上 `0.78 TPR, 0.07 FPR`；数据拆 train/test 防过拟合；一次 agent 改动后 clinicians blinded preference 为 `91%`。
- **适用范围**：Abridge 临床笔记的离线开发评估；博客明确示例使用 synthetic data 保护隐私，结果是其内部系统案例。
- **对结果可信的启示**：离线裁判可提供快速、可解释、可迭代的方向信号，但 0.78/0.07 是裁判对 clinician verdict 的局部校准，不是通用准确率；91% 是专家盲比偏好，不是规则通过率，也不是线上临床结果改善。需保留 held-out、专家复核、线上监测三本账。

完整引句与“不支持外推”见 [`agent_goal_eval/raw/evidence-2026-09-27-b4-abridge.md`](../../agent_goal_eval/raw/evidence-2026-09-27-b4-abridge.md)。

### 5.2 Rippling：同一公司也把 offline、post-merge、deployment gate、production monitoring 分层

- **原始 URL（MCP harness）**：<https://www.rippling.com/blog/building-mcp-server>
- **短引句/参数**：50+ golden cases；每条有 user prompt、reference answer、stubbed API response、expected code；评分四格为 function selection、function path、call correctness、final answer；动作头让 Claude Code 成绩 `41%` 上升，写 p95 后 production sandbox timeout `70%` 下降。
- **适用范围**：Rippling MCP 说明文字/工具调用 harness；41% 是 Claude Code 该实验的成绩变化，70% 是沙箱超时，不是统一质量分。
- **对结果可信的启示**：同一离线评分可拆“路径/调用/最终答案”，但生产 timeout 是另一维。把 41% 和 70% 合并成“结果可靠性提升”是指标错配。

- **原始 URL（Rippling AI 案例，一手转述）**：<https://www.langchain.com/blog/how-rippling-went-ai-native-across-every-product-in-6-months-with-deep-agents-and-langsmith>
- **短引句/参数**：四层检查：offline mock；post-merge 300–400 queries with real APIs；deployment gate 约 10 条关键场景；production data 多次/日；失败 trace 触发改动和重跑，但 merge 仍需 human review。
- **适用范围**：LangChain 对 Rippling 的客户案例转述；没有公开某条检查的前后质量分。
- **对结果可信的启示**：它是离线到线上分层的局部实例，证明“不同观察面要分开”，不证明这四层是行业标准或自动修复已可靠。

完整指针及 41%/70% 的口径见 [`agent_goal_eval/raw/evidence-2026-09-27-b5-company-posts.md`](../../agent_goal_eval/raw/evidence-2026-09-27-b5-company-posts.md) §Source 1–2。

### 5.3 Shopify 反例：线上激活率不是模型质量

- **原始 URL**：<https://shopify.engineering/fine-tuning-agent-shopify-flow>
- **短引句**：离线评估分别检查 semantic correctness、syntactic correctness、latency；生产 `Activation rate was our first production signal, but it turned out to be noisy: it reflects merchant behavior, not model quality.`
- **适用范围**：Shopify Flow 生成 workflow 的工程帖；离线 300 条手写例子与 1% 流量生产信号。
- **对结果可信的启示**：线上业务代理指标可能受用户行为、入口和产品摩擦影响；必须先证明它与目标结果的连接。若业务指标无法解释或无法回读，只能称“生产信号”，不能称“完成判据”。

### 5.4 结果在系统外：不能把静默停止称自动完成

- **原始 URL**：<https://yuvalyeret.com/blog/ai-agent-completion-goals-aim-at-outcomes>
- **短引句**：先问 goal 是 `completion condition for an output, or for an outcome`；若 outcome 在 agent 可观察范围外，`how would the agent observe whether that condition holds?`；他观察到无 observability loop 时，agent 会 stop and hand it back。
- **适用范围**：作者对 outcome-oriented goal 的工程观察，2026-05-27，窗边；不是运行统计。
- **对结果可信的启示**：把 output（文件、测试、报告）和 outcome（客户采用、财务及时性、临床结果、环境外系统状态）分层。结果不可观察时，正确状态是 `blocked/awaiting human or external signal`，不是 `completed`。

## 6. 目标构造与可观察验收的最小组合

以下是从一手机制抽出的工程推论，**不是任何一家官方的统一规范**：

1. **目标层**：写一个可观察终态、一个明确检查、路径/不可变约束、边界、迭代策略、blocked stop；参考 Claude `/goal` 的 `measurable end state + stated check + constraints` 与 OpenAI Goal 的六项 contract。原始 URL：<https://code.claude.com/docs/en/goal>、<https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex>。
2. **验收层**：尽量用环境状态/确定性测试；对主观维度用结构化 rubric、独立 evaluator，并用 held-out 数据和专家校准。Anthropic 明确 code/model/human graders 各有 strengths/weaknesses；OpenAI 明确 automated scoring 要 human calibration。原始 URL：<https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents>、<https://developers.openai.com/api/docs/guides/evaluation-best-practices.md>。
3. **不可篡改层**：被测 agent 不应拥有修改测试描述、grader、gold/held-out split 的权限；Anthropic quickstart 的 `only modify passes` 是局部实例，不能冒充所有产品默认。原始 URL：<https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/prompts/coding_prompt.md>。
4. **资源层**：硬上限必须覆盖 outer feedback path；记录预算耗尽、错误、无进展、取消与过期，不能把它们并入成功。原始 URL：<https://arxiv.org/abs/2607.01641>、<https://code.claude.com/docs/en/scheduled-tasks>。
5. **结果层**：至少保留 offline capability/regression、production monitoring、A/B/user feedback/human review 的不同来源；真实业务结果不可见时降级为待验证。原始 URL：<https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents>、<https://tech.abridge.com/blog/offline-evaluations-to-improve-our-systems>。

## 7. 不可推出清单

- 不能从 LE3 的 `/loop`、cron、webhook、cloud routine 或事件触发，推出结果已经可靠；LE3 只证明再次启动/维持运行的控制面存在。
- 不能从 `/goal` 的 `Not yet met / Met / Impossible` 三值推出 evaluator 判得准、产物质量好或业务 outcome 发生。
- 不能从 `fresh model`、separate evaluator、CIV verifier 或 OpenAI auto-review 推出无误报、无漏报、抗 reward hacking；分离不等于准确。
- 不能从 turn/time/7-day/denial/token/dollar cap 触发后的停止推出任务达成；上限停机、错误暂停、取消、过期都必须与 `Met/succeeded` 分开。
- 不能把 Anthropic quickstart 的 feature list、`passes` prompt 保护或其进度条外推成生产驱动层有 `passing == total` 自动退出；源码恰好显示默认 `max_iterations=None` 且没有该退出分支。
- 不能把 Abridge 的 `TPR 0.78/FPR 0.07` 外推为其他领域的 evaluator accuracy；不能把临床专家 `91%` 偏好读成 91% 规则通过或线上医疗结果改善。
- 不能把 Rippling 的 Claude 成绩 `+41%`、沙箱 timeout `-70%`、或其四层检查，合并成一个“结果可靠性 +X%”；它们的对象、环境和指标不同。
- 不能把 Shopify activation rate、Glean preference ratio、用户点击/打开等线上代理信号直接称为模型完成率；必须先验证它们与目标 outcome 的因果/测量连接。
- 不能把 OpenAI Goal cookbook 的“对照 files/tests/logs/artifacts”写法，填充成 OpenAI 已公开实现独立 evaluator 的证明；该页是构造指南，未给出该实现细节。
- 不能把“测试不可改”从 Anthropic quickstart 的局部 prompt/权限约束，升级成 OpenAI 或所有 Anthropic 产品的默认不变量；只能说这是应由控制面强制的工程要求。
- **环境外业务结果无法观察时不称自动完成**：没有可回读状态、独立遥测或人工确认，只能报告 output/verification 状态与 `awaiting external signal`。

## 8. 与既有档案的精确关系

- `/goal` 三值、hard-rules 限界、turn/time 上限、`/loop` 7 天过期：见 [`evidence-b`](evidence-2026-09-26-b-stop-and-scheduling.md) §4a–4c 与 [`agent_goal_eval/raw/evidence-2026-09-27-a-goal-frontier.md`](../../agent_goal_eval/raw/evidence-2026-09-27-a-goal-frontier.md)。本文只把它们放到“结果可信”正交轴，不重抄大段正文。
- quickstart 的 `agent.py`/`progress.py`/prompt 落差：见 [`evidence-l`](evidence-2026-09-28-l-quickstart-code.md)。本文只取“进度显示 != 驱动退出”的反向实验。
- evaluator 分离、CI/review bot、METR reward hacking：见 [`evidence-n`](evidence-2026-09-28-n-verdict-split-coding.md)。本文只取“分离 != 准确”的边界。
- effective bound coverage、state-based oracle、ReliabilityBench：见 [`evidence-r`](evidence-2026-09-28-r-ial-scan-reliability.md)。本文只取“外层 cap 与反馈路径”和“终态 oracle”接口。
- LangGraph RemainingSteps、dbt exit code、CIV advisory→hard gate：见 [`evidence-s`](evidence-2026-09-28-s-langgraph-dbt-civ.md)。本文不把这些局部实现拼成统一产品方案。
- Rippling/Abridge/Shopify 的量化口径：见 [`agent_goal_eval/raw/evidence-2026-09-27-b3-engineering.md`](../../agent_goal_eval/raw/evidence-2026-09-27-b3-engineering.md)、[`agent_goal_eval/raw/evidence-2026-09-27-b4-abridge.md`](../../agent_goal_eval/raw/evidence-2026-09-27-b4-abridge.md)、[`agent_goal_eval/raw/evidence-2026-09-27-b5-company-posts.md`](../../agent_goal_eval/raw/evidence-2026-09-27-b5-company-posts.md)。本文不重新复制数字表。

## 9. 观测与验证记录

- 观测日期：2026-09-30；官方 URL 已用 `web_fetch` 复核：Claude Code `/goal`、`/scheduled-tasks`、Anthropic long-running harness、Anthropic evals、OpenAI eval best practices、OpenAI Codex Goals、OpenAI Auto-review、Abridge、Rippling、Shopify、Osmani、Yeret。
- 本档是回源增量，不改其他已有 evidence 的逐字摘录；教学结构与术语以 [`capability_ladder/00-map`](../capability_ladder/00-map.md) 为准。
- Markdown 链接检查重点：本档案内的相对链接均指向已存在的既有 evidence/raw 文件；外部链接均保留为原始官方/作者 URL。若后续页面改版，需按本档案的“短引句 + 适用范围 + 不支持什么”重新回源，不把活文档当永久快照。
