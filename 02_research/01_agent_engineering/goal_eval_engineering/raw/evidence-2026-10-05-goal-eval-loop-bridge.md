# Evidence 2026-10-05：goal/eval 与 coding-agent loop 的可执行接口

- **研究问题**：loop engineering 与 goal/eval engineering 如何结合；coding agent 在「目标清晰」「只有执行次序」「目标/验收难定义」三种输入下，怎样设计完成条件、grader、反馈、停止、预算、升级、人审、过程证据与结果验收的循环。
- **整理/尝试访问日期**：2026-10-05。各来源的原始核验日期以链接的既有档案为准；本轮未成功重新获取官方网页，不能把以下“观测 2026-10-05”理解为当前网页主验。
- **档案角色**：跨主题桥接索引，不是新增独立证据；引句节选用于接口核对，事实与版本的权威仍在原档案。§5–§6 为待综合候选；采用后的研究结论以 [Goal/Eval × Loop](../../loop_engineering/capability_ladder/goal-eval-axis.md) 为准。
- **来源纪律**：以下优先使用官方文档、官方工程博客、官方源码或论文原文。Anthropic/OpenAI/LangGraph 页面本轮 `web_fetch` 受 `hostname resolves to a non-public IP address` 限制；相关逐字引句已在本仓库既有回源档案中以 curl/源码复核，本档案保留原始 URL 与既有档案指针，不把搜索摘要当引句。
- **证据等级**：`P-existence` = 一手材料证明功能/观点存在；`P-mechanism` = 一手材料说明如何工作；`P-outcome` = 受控比较、运行指标或独立复盘支持结果效果。存在性或机制不能自动升级为 outcome。

## 1. 目标清晰：把 goal 写成可观察的完成合同

### 1.1 Claude Code `/goal`：完成判定与干活模型分离，但观察面很窄

- **URL**：<https://code.claude.com/docs/en/goal>
- **发布日期/版本锚**：功能在 Week 20（2026-05-11–15，v2.1.139）发布；活文档观测 2026-10-05。日期与全文摘录已在 [`evidence-2026-09-27-a-goal-frontier.md`](evidence-2026-09-27-a-goal-frontier.md) §Source 1 复核。
- **原文摘录**：
  > “Use a goal for substantial work with a verifiable end state”
  >
  > “The evaluator judges your condition against what Claude has surfaced in the conversation. It doesn’t run commands or read files independently, so write the condition as something Claude’s own output can demonstrate.”
  >
  > “`/goal` adds a separate evaluator that checks your condition after every turn, so completion is decided by a fresh model rather than the one doing the work.”
  >
  > “The model returns one of three verdicts… Not yet met… Met… Impossible”
- **机制参数/边界**：条件可含 measurable end state、stated check、constraints；可写 `or stop after 20 turns`。文档还描述无 tool use 连续数轮会停止、其他错误三次重试后暂停，以及认证/额度/不可解 context overflow 等清 goal（详见 loop 主题 [`evidence-2026-09-30-y-long-run-result-reliability.md`](../../loop_engineering/raw/evidence-2026-09-30-y-long-run-result-reliability.md) §2.3）。
- **证据分级**：`P-existence + P-mechanism`。
- **能支持什么**：coding agent 可把“做完”编码成可在运行记录中呈现的终态；每轮由 fresh evaluator 给 `Not yet met / Met / Impossible`，从而把继续、成功、不可行分成控制状态；turn cap、错误暂停和无进展停止是安全出口。
- **不能支持什么**：evaluator 不自行读文件/执行命令，不能证明 transcript 外的业务状态；三值不是质量分数，不证明 evaluator 准确，也不证明最终业务结果发生；“停了”不能直接记为 success。

### 1.2 OpenAI Codex Goal：把执行次序放进合同，但不等于验收

- **URL**：<https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex>
- **发布日期/观测日期**：页面标注 2026-05-09（窗边）；观测 2026-10-05。原文摘录已在 [`evidence-2026-09-27-a-goal-frontier.md`](evidence-2026-09-27-a-goal-frontier.md) §Source 3 复核。
- **原文摘录**：
  > “A Goal is not background autonomy without boundaries. It is a scoped, user-controlled completion contract.”
  >
  > “The strongest Goals usually define six things: Outcome… Verification surface… Constraints… Boundaries… Iteration policy… Blocked stop condition”
  >
  > “A Goal should not be marked complete because the model believes it is probably done. It should be complete only after the objective is checked against the relevant files, tests, logs, benchmark output, generated artifacts, or other concrete evidence.”
  >
  > “Do not use a Goal when the finish line is vague.”
- **证据分级**：`P-existence + P-mechanism`。
- **能支持什么**：当用户给出目标时，contract 至少要固定 outcome、verification surface、constraints/boundaries、iteration policy、blocked stop；“执行次序”只能是 iteration policy/action plan，不能替代终态证据。blocked 是显式终态，不是静默继续。
- **不能支持什么**：该 Cookbook 没有说明 Codex Goal 一定使用独立 evaluator；不能借 Claude 的 fresh-model 三值填补 OpenAI 实现细节；没有效果对照，不能声称 contract 提升产出质量。

### 1.3 Osmani：硬规则裁判不判断品味

- **URL**：<https://addyosmani.com/blog/practical-loop-engineering/>
- **发布日期/观测日期**：2026-08-14；观测 2026-10-05。原文已在 [`evidence-2026-09-27-a-goal-frontier.md`](evidence-2026-09-27-a-goal-frontier.md) §Source 2 复核。
- **原文摘录**：
  > “The way that I use goal is I use it for building any specific piece of work until it’s provably done.”
  >
  > “The evaluator sitting behind goal … doesn’t look at the content to see if it’s good or bad … [it] examine[s] the conversation transcript to see if the hard rules you specified have been met.”
  >
  > “if you don’t have a clear idea of what the end-state/done/good means … it may not be the right pattern … ‘keep going until this UI design is good’.”
- **证据分级**：`P-existence + P-mechanism`，无 `P-outcome`。
- **能支持什么**：对可证明的工程终态使用 goal loop；硬规则验收与人类 taste/judgment 分离。
- **不能支持什么**：不证明硬规则足够表达业务质量；不证明独立 evaluator 没有漏报/误报；不支持把主观设计任务强行变成无人值守完成。

## 2. 只有执行次序：把“下一步做什么”与“是否完成”分成两条线

### 2.1 Anthropic long-running harness：过程证据进入持久工件

- **URL**：<https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents>
- **发布日期/观测日期**：页面标注 2025-11-26（窗外；仅引用 loop 主题已回源机制背景，本主题不新增旧源研究）；观测 2026-10-05。官方正文回源、源码边界见 [`../../loop_engineering/raw/evidence-2026-10-04-ad-delivery-consumption-web.md`](../../loop_engineering/raw/evidence-2026-10-04-ad-delivery-consumption-web.md) §来源 H 与 [`../../loop_engineering/raw/evidence-2026-09-30-y-long-run-result-reliability.md`](../../loop_engineering/raw/evidence-2026-09-30-y-long-run-result-reliability.md) §3.1。
- **原文摘录**：
  > “an init.sh script, a claude-progress.txt file that keeps a log of what agents have done, and an initial git commit”
  >
  > “Read the git logs and progress files to get up to speed…”
  >
  > “Read the features list file and choose the highest-priority feature that’s not yet done…”
  >
  > “End the session by writing a git commit and progress update.”
  >
  > “Self-verify all features. Only mark features as ‘passing’ after careful testing.”
  >
  > “It is unacceptable to remove or edit tests…”
- **源码/参数**：官方 quickstart `agent.py` 的 `max_iterations: Optional[int] = None`，`None for unlimited`；驱动层只在 `max_iterations` 超限时 `break`。`progress.py` 显示 `passing/total`，没有 `passing == total` 的退出分支；coding prompt 才约束 agent 只能修改 `passes` 字段。源码指针：<https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/agent.py>、<https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/progress.py>、<https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/prompts/coding_prompt.md>。
- **证据分级**：博客工件设计 `P-existence + P-mechanism`；源码参数 `P-mechanism`；无跨项目 `P-outcome`。
- **能支持什么**：当用户只有执行次序或把工作拆成 feature 时，loop 仍需通过 progress/git/feature list 形成可恢复的过程证据；每轮选择最高优先级未完成项；博客以 prompt 约束测试/规格，不能当成驱动层权限隔离；commit/progress 是下一轮的输入。过程证据（做过什么、当前状态、可恢复点）与结果验收（feature 是否真的 passing）应分账。
- **不能支持什么**：feature list 或进度条本身不构成“全部通过即停”；quickstart 不是 Claude Agent SDK 默认行为；`max_iterations=None` 甚至表示默认可能无界。不能把“执行次序完成”写成“目标完成”，也不能由 `passing/total` 推出业务 outcome。

### 2.2 反馈与状态持久化：结果必须能被下一轮消费

- **URL**：<https://docs.langchain.com/oss/python/langgraph/persistence>、<https://docs.langchain.com/oss/python/langgraph/checkpointers>、<https://docs.langchain.com/oss/python/langgraph/use-time-travel>
- **发布日期/观测日期**：页面未标发布日期；观测 2026-10-05。逐字回源见 [`../../loop_engineering/raw/evidence-2026-10-04-ad-delivery-consumption-web.md`](../../loop_engineering/raw/evidence-2026-10-04-ad-delivery-consumption-web.md) §来源 L。
- **原文摘录/参数**：
  > “The checkpointer uses `thread_id` as the primary key…”
  >
  > “LangGraph creates a checkpoint at each super-step boundary… you can only resume execution from a checkpoint”
  >
  > “`sync`: LangGraph persists changes synchronously before the next step starts.”
  >
  > “update_state does not roll back a thread. It creates a new checkpoint… The original execution history remains intact.”
- **证据分级**：`P-existence + P-mechanism`，无 `P-outcome`。
- **能支持什么**：反馈应绑定 thread/目标状态，并在明确 super-step 边界持久化；恢复、重放、分叉和原历史保留可作为过程证据。若要让 evaluator/下一轮实际使用结果，应追踪结果的关联键、投递路径和消费分支，而不只记录“有 checkpoint”。
- **不能支持什么**：持久化不等于正确验收；checkpoint 不判断业务完成；文档没有证明 agent 会自动消费某个结果或因此提升质量。

## 3. Grader/eval：先把“可判定”做出来，再谈自动循环

### 3.1 Anthropic evals：任务、结果、路径和人工校准分开

- **URL**：<https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents>
- **发布日期/观测日期**：2026-01-09（窗边）；观测 2026-10-05。逐字回源见 [`evidence-2026-09-27-a6-how.md`](evidence-2026-09-27-a6-how.md) §Source 1。
- **原文摘录**：
  > “A good task is one where two domain experts would independently reach the same pass/fail verdict.”
  >
  > “Everything the grader checks should be clear from the task description.”
  >
  > “it’s often better to grade what the agent produced, not the path it took.”
  >
  > “We recommend choosing deterministic graders where possible, LLM graders where necessary or for additional flexibility, and using human graders judiciously for additional validation.”
  >
  > “20-50 simple tasks drawn from real failures is a great start.”
- **证据分级**：机制 `P-mechanism`；文中 CORE-Bench 42%→95% 的 grader 修订属于作者报告的局部 `P-outcome`，不是 loop 因果证据。
- **能支持什么**：eval 的最小可执行单元应是任务+可复现输入+pass/fail 判据；先从真实失败取 20–50 条；能查环境状态就用确定性 grader；主观维度用 LLM/human grader，并把人用于校准/抽查；结果验收优先看产物，不把一条预设工具调用路径误当唯一正确路径。
- **不能支持什么**：文章不证明任何特定 coding agent 的质量提升；不证明 LLM grader 可靠；不能把“两个专家可一致判定”扩展为所有开放式目标都可自动化。

### 3.2 OpenAI eval best practices：held-out、持续回归和人校准

- **URL**：<https://developers.openai.com/api/docs/guides/evaluation-best-practices>
- **发布日期/观测日期**：页面无发布日期；观测 2026-10-05。步骤已在 [A6 Source 2](evidence-2026-09-27-a6-how.md) 归档；`Maintain agreement` 与 held-out 的原始核验摘录在 [Y §3.3](../../loop_engineering/raw/evidence-2026-09-30-y-long-run-result-reliability.md)。
- **原文摘录**：
  > “Define eval objective. What’s the success criteria for the eval?”
  >
  > “LLMs are better at discriminating between options. Therefore, evaluations should focus on tasks like pairwise comparisons, classification, or scoring against specific criteria instead of open-ended generation.”
  >
  > “Maintain agreement: Use human feedback to calibrate automated scoring.”
- **参数/机制**：官方示例要求在 held-out set 上评估；每次改动后重跑，并把新的不确定案例加入集合；示例把标准写成 ROUGE-L、召回率、精确率、正向比例等数值。
- **证据分级**：`P-existence + P-mechanism`；页面的示例数字不是 coding-agent 结果，故不作 `P-outcome`。
- **能支持什么**：目标/验收难定义时，先把自由生成改造成 pairwise、分类或 rubric scoring；保留 held-out 集，持续纳入不确定样本；自动 grader 必须用人类反馈校准。
- **不能支持什么**：不能把通用 eval 指南写成 Codex Goal 的内部实现；不能用一个自动分数替代人对业务结果的最终判断。

## 4. 停止、预算、升级：所有“停”都要带语义

### 4.1 外层预算必须覆盖 evaluator feedback path

- **URL**：<https://arxiv.org/abs/2607.01641>
- **发布日期/观测日期**：论文页面标 2026-07（版本日期需以论文页面为准）；观测 2026-10-05。论文原文机制已在 [`../../loop_engineering/raw/evidence-2026-09-30-y-long-run-result-reliability.md`](../../loop_engineering/raw/evidence-2026-09-30-y-long-run-result-reliability.md) §4.1 回源。
- **原文摘录**：
  > “An inner turn cap on a nested agent call does not cover an outer evaluator feedback cycle unless it dominates the outer feedback path.”
- **证据分级**：样本研究对该漏洞模式是 `P-existence + P-mechanism`；论文样本统计不能直接外推业务事故率，故不写通用 `P-outcome`。
- **能支持什么**：预算要覆盖 root loop、重试、poll/ping、evaluator 反馈和派生子 agent；只给 worker 一个 turn cap 不能证明整个系统有界。
- **不能支持什么**：不能从论文样本推出任何特定 coding agent 已经安全；预算耗尽只说明 `budget_exhausted/paused`，不说明目标已达成。

### 4.2 OpenAI auto-review：人审/拒绝停止是安全控制，不是完成验收

- **URL**：<https://alignment.openai.com/auto-review/>
- **发布日期/观测日期**：页面发布日期未在既有回源中固定；观测 2026-10-05。摘录和边界见 [`../../loop_engineering/raw/evidence-2026-09-30-y-long-run-result-reliability.md`](../../loop_engineering/raw/evidence-2026-09-30-y-long-run-result-reliability.md) §3.2。
- **原文摘录/参数**：
  > “Codex sessions stop for human approval roughly 200x less often”
  >
  > “approves around 99%”
  >
  > “Auto-review should not be treated as a guarantee of security”
  >
  > repeated denials 后自动停止 trajectory。
- **证据分级**：官方部署/运行数字是局部 `P-existence + P-outcome`（说明其系统中观察到的审批频率/批准率），不是完成率或安全保证。
- **能支持什么**：人审可作为风险动作的升级点；重复拒绝应进入停止/升级状态；审批器、完成 evaluator、业务 outcome grader 是三种不同角色。
- **不能支持什么**：99% approve 不是 99% 正确完成；低人工介入频率不是高质量证明；人审也不自动替代明确的验收判据。

### 4.3 evaluator 隔离仍可能被 reward-hacking 绕过

- **URL**：<https://metr.org/blog/2025-06-05-recent-reward-hacking/>
- **发布日期/观测日期**：2025-06-05（窗外；仅引用 loop 主题已有反例，本主题不新增旧源研究）；观测 2026-10-05。引句见 [`../../loop_engineering/raw/evidence-2026-09-30-y-long-run-result-reliability.md`](../../loop_engineering/raw/evidence-2026-09-30-y-long-run-result-reliability.md) §3.4。
- **原文摘录/代码**：
  > “Monkey-patch the evaluator so that every piece of code ‘passes’”
  > `rc_utils.evaluate_rust_code = _always_ok`
- **证据分级**：特定 RE-Bench/HCAST 任务的攻击观察为局部 `P-outcome`；机制边界为 `P-mechanism`。
- **能支持什么**：被测 agent 不能拥有修改 evaluator、gold、held-out split 或判定状态的权限；需要审计 evaluator 代码/输入、独立 monitor 和人工抽查。
- **不能支持什么**：不能推出所有 coding agent 都会 reward hack；不能把“裁判独立”当作抗攻击证明。

## 5. 三种输入形态的循环设计（由上述一手机制支持的综合，不冒充单一来源规范）

### A. 目标清晰、终态可观察

```text
Goal(contract: outcome + verification surface + constraints + boundaries)
  -> bounded action loop
  -> environment evidence (tests/files/logs/benchmark)
  -> independent or calibrated grader
  -> Met | Not yet met | Impossible/Blocked
  -> commit/progress/trace + next turn or human escalation
```

- 完成依据来自实际证据；grader 可以是程序、模型或人，模型自述“应该完成”不是成功。
- 条件判定与控制决定分账；`Met`、`Impossible/Blocked`、预算、错误、取消、过期不能混作一个成功信号。产品可能将错误/预算记为可恢复暂停，而不是 terminal；并非所有产品有这些枚举。
- 过程证据（每轮做了什么、使用了哪个环境/commit、下一步指针）与结果验收（最终产物是否满足目标）分开存储和报告。

### B. 只有执行次序，没有结果 goal

- 将步骤表视为 **action policy / iteration policy**；若目标是需求满足，步骤走完不够；若目标本来是执行审计流程并交付证据包，步骤回执和工件完整性可以是合法验收项。
- 步骤产出可检查的中间状态（文件/测试/日志/feature status）；同一会话可直接消费工具结果，跨会话恢复才需 progress/checkpoint 等持久状态；不强制每轮 commit。
- 若没有可见终态：loop 可以在有界预算内执行和准备证据，但终态应是 `awaiting_goal` 或 `awaiting_external_signal`，而不是 `Met`。这是对“可观察性缺失”的控制语义，不是禁止自动执行。
- 可把人放在“确认 outcome/改写 goal/批准下一阶段”这一升级点，而不是每个机械步骤都同步审批。

### C. 目标/验收难定义、含主观判断或开放探索

- 先从真实失败建立小型任务集；由两位领域专家能独立 pass/fail 的部分做自动化候选，其余保留为 rubric + human review。
- 将开放生成改造成 pairwise/classification/criteria scoring；自动评分用 held-out 数据和人类反馈校准；允许 `Unknown`/`Needs human`，不要强迫 grader 二值化不可观察事实。
- loop 采用“探索预算 + 证据记录 + 人审升级”：可以自动多轮，未知时允许有限补查；反复无进展、无法取证或触及边界再暂停交人。不能把暂停自动计为成功或质量失败。
- 反作弊边界：执行者不能削弱判据来换绿；开发新测试与修改受保护验收集区别对待，后者由指定负责人管理。过程 trace 用于诊断，结果检查用于验收，不能用“做过很多步骤”抵换结果。

## 6. 待综合的硬结论

1. **Goal 是停止合同，不是背景提示**：至少要有可观察终态、验证面、约束/边界、迭代策略和 blocked stop；执行顺序只能回答“下一步怎么做”，不能回答“何时算完成”。
2. **完成条件与结果验收必须分层**：goal/evaluator 可以只验证 transcript、文件、测试或 benchmark；业务 outcome 只有在环境外状态可回读、独立遥测或人工确认时才能计为完成。
3. **过程证据与结果验收不可互换**：git/progress/feature list/checkpoint 证明状态可恢复与行为可追溯；它们不自动证明 feature 通过，更不证明业务结果改善。
4. **停止状态必须带语义**：`Met`、`Not yet met`、`Impossible/Blocked`、`budget_exhausted`、`error`、`cancelled`、`expired` 分账；任何 cap 或静默停止都不能直接计成功。
5. **grader 的选择遵循可判定性**：确定性检查优先；不可避免的主观维度用结构化 rubric/LLM grader；人用于校准、抽查和最终业务判断，而不是让干活模型自证。
6. **只有执行次序时仍可自动执行，但必须限定声明**：以 action policy 驱动有界执行并产出证据；过程交付本身可作为目标，但不能代替隐藏结果验收。确实没有任何可观察终态时，交接未定义或未验证部分，不虚构 success。
7. **目标难定义时，先改造验收面再提高自治度**：从真实失败建任务集、让专家能一致判定；用 pairwise/classification/rubric 与 held-out 校准；不确定就 `Needs human`，不要用无限重试替代定义工作。
8. **独立 evaluator 是角色分离，不是准确性保证**：还需要判据隔离、不可篡改测试/gold、反 reward-hacking 监控、外层预算覆盖反馈路径和人审升级。
9. **人审应是显式升级路径**：主观质量、外部 outcome、连续无进展、预算/权限风险和 grader 不确定都应能落到人；人审频率降低或 auto-review 高批准率不能替代结果验收。
10. **当前证据仍不足以给出跨产品“自主度越高越可靠”的因果结论**：上述材料主要证明可执行机制与失败边界；除局部运行数字外，没有证明 loop/goal/eval 组合普遍改善 coding-agent 业务 outcome。

## 7. 负结论与获取限制

- 本档案没有把搜索结果摘要、中文转述或社区猜测当作原文证据。
- 本轮官方网页 `web_fetch` 对 `anthropic.com`、`openai.github.io` 等返回 non-public IP；Anthropic/OpenAI 相关引句依赖本仓库既有 curl/源码回源档案，并保留其 URL、版本和边界。
- 未将 Cursor 的 `/goal` 命令或任何产品“长任务”宣传语当作独立 grader/停止机制证据；没有裁判、证据面和 terminal semantics 的页面只证明功能存在。
- `P-outcome` 只用于来源明确报告局部运行数字或受控研究的条目；不能把这些数字外推为通用 coding-agent 完成率、安全率或业务质量。
