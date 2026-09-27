# Evidence 2026-09-27 · H 路 · automation → autonomy 与 harness → loop

- 观测日期：2026-09-27
- 时间窗：2024-12-19 → 2026-09-27
- 研究假设：AI coding agent 是否从 automation（自动执行动作）转向 autonomy（目标驱动、自主选择下一步）；harness engineering 的成熟是否促成或暴露了 loop engineering？
- 本档案回答：建立时间轴与概念依赖矩阵；把 automation、autonomy、harness、loop 各自压到最小含义；检查“harness 成熟 → loop engineering”支持链、反例、不能证明的因果。
- 证据口径：P-existence = 名称/观点/功能存在；P-mechanism = 原文、文档或源码说明如何工作；P-outcome = 受控比较、运行指标或独立复盘说明效果。P-existence/P-mechanism 不自动升级为 P-outcome。
- 去重口径：按作者、机构和引用链去重。Anthropic 的多篇材料合并为一个机构证据簇；OpenAI 的 harness engineering 与 auto-review 合并为一个机构证据簇；Osmani 对 Cherny/Steinberger 的转引不增加原始来源票；LangChain 与 Anthropic、Huntley、Osmani 分开计，但 LangChain 文中的“AI leaders arrived at the same conclusion”只算引用关系，不算被引用者的新票。

## 结论先行

1. **“从 automation 转向 autonomy”作为机制趋势得到有限支持，但不是已证实的历史替代。** 一手材料显示：定时/脚本/固定路径的 automation 仍然存在；其上叠加目标、环境反馈、模型自主选择工具/子任务、停止与验证后，才达到本文的最小 autonomy。Claude Code 的官方材料明确区分：auto mode 只在一个 turn 内批准工具调用，不会启动新 turn；`/loop` 是时间触发；`/goal` 才是围绕一个完成条件持续迭代。因此不能把“无人审批”“定时运行”单独称为 autonomy。
2. **harness 的成熟是 loop engineering 被看见、被产品化的必要条件之一，但没有被证明是唯一原因或因果原因。** Anthropic 2025 的长程 harness 把持久状态、feature 清单、测试、git/progress 和跨 context 的恢复问题显式化；随后 Claude Code、Osmani、LangChain 把“谁取题、谁验证、何时再跑、何时停止”命名为 loop/goal/schedule 等原语。这支持“harness 把循环控制问题暴露为一等对象”的机制解释。
3. **时间顺序同时允许另一种解释：loop 不是 harness 成熟后才出现。** Anthropic 2024 已把 agent 定义为基于环境反馈的工具循环；Ralph（2025-07）已有 Bash 无限循环、back pressure 和人工判断；LangChain 的四环模型还把改写 harness 的 hill-climbing 纳入 loop。也就是说，loop 构件先于 2026 的命名与产品化存在。更稳妥的判断是：harness 与 loop **共同演化、互相暴露接口**，而非已证明的单向“harness 导致 loop”。
4. **没有足够 P-outcome 证明 autonomy 或 harness/loop 的普遍质量收益。** OpenAI auto-review 和 Anthropic auto mode 有内部评测数字，但它们主要测审批摩擦、危险动作召回或误报，不等于 coding 质量、返工率或端到端交付收益；Osmani、Huntley、LangChain 的案例/建议也不能外推为行业效果。

## 一、最小概念与依赖矩阵

| 概念 | 最小含义（本档案的分析定义） | 最小可观察证据 | 依赖/关系 | 不能据此推出 |
|---|---|---|---|---|
| **automation** 自动化 | 由预先写好的触发器、规则或固定路径自动执行动作；可以是 cron、脚本、权限放行或重复调用 | schedule/cron、固定脚本、allowlist、工具自动运行 | 是 loop 的触发器或执行器，但不要求模型选择下一步 | 不等于目标理解、策略选择、质量判断或自主性 |
| **autonomy** 自主性 | 在人给定目标、范围和约束后，系统依据状态/环境反馈选择下一步行动、工具、子任务或是否继续 | 下一步不是完全预编排；有目标/边界、反馈、状态、停止/升级规则 | 需要模型的决策能力，也需要 harness 提供可读环境、工具、权限、记忆与守门；可被人或规则降档 | 不等于无人监督、不等于正确、不等于安全，也不等于跨 session 持续 |
| **harness** | 包围模型的运行环境与控制面：context/工具、权限、sandbox、状态/日志、测试/评估、hooks、工作树及恢复机制 | 环境约束、持久化日志、可执行门、评估器、权限分类器、恢复接口 | 先把单次运行做得可观察/可控，才能把多轮 loop 的状态与结果连接起来 | 不等于 loop；有 harness 不证明会自动取题或跨 feature 调度 |
| **loop** | 至少有触发 → 反复行动 → 反馈/验证 → 状态记忆 → 停止或继续；下一轮会参考上一轮结果或明确完成条件 | 每轮输入/输出、反馈、状态、明确 stop/continue；必要时有外层调度 | 可由 automation 触发，也可在单 session 内由目标驱动；harness 是其运行基础，但外层调度不是所有 loop 的必要条件 | 不等于无限重试、定时任务、自动批准或“模型说 done” |
| **loop engineering** | 把上述循环的取题、授权、执行、验证、记忆、停止、升级和复盘设计成系统，而非人逐轮写 prompt | 目标/队列、独立检查、硬门/熔断、状态脊柱、调度与人工介入点 | 可视为 harness 之上或与 harness 互相反馈的一层；不同作者外延不一致 | 不是统一标准；不能由单一作者的 checklist 推出准入条件 |

**依赖图（分析模型，不是任何单一来源的原话）：**

```text
模型的工具决策能力
        ↓
 harness：可读 context + 工具 + 权限/sandbox + 状态/日志 + 验证器
        ↓
 bounded autonomy：在目标/边界内选择下一步、接受反馈、继续/停止
        ↓
 loop engineering：把多轮控制、调度、状态、验收、升级和复盘组织起来
        ↑                         ↓
 automation 提供触发/执行节拍       trace/失败反馈可反过来改 harness
```

这个图表达的是接口依赖，不是已证明的历史因果。一个定时 automation 可以没有 autonomy；一个 agent loop 可以没有跨 feature 外层调度；一个成熟 harness 也可能只服务单次调用。

## 二、时间轴与事件性质

| 日期 | 一手来源/事件 | 对假设的最小意义 | 强度 |
|---|---|---|---|
| 2024-12-19 | Anthropic《Building effective agents》 | 已把 workflow（预定义代码路径）与 agent（LLM 动态指挥自身过程/工具）区分；agent 依环境反馈循环运行，并可在 checkpoint/blocker 停顿 | P-existence + P-mechanism；同一机构 |
| 2025-07-14 | Geoffrey Huntley《Ralph Wiggum as a “software engineer”》 | `while :; do ...; done` 的无限循环、back pressure、每轮测试、todo/规格、人工 taste 和 greenfield 限制；loop 早于 2026 命名存在 | P-existence + P-mechanism；独立作者 |
| 2025-11-26 | Anthropic《Effective harnesses for long-running agents》 | 长程失败被拆成跨 context 记忆/增量工作/提前宣布完成/端到端验证；feature_list、progress、git、init/test 组成 harness | P-existence + P-mechanism；Anthropic |
| 2026-02-11（日期未由 OpenAI 正文核验） | OpenAI《Harness engineering: leveraging Codex in an agent-first world》官方 URL | 研究对象确有官方命名；正文当前 HTTP 403，故本档案不引用其内部数字或机制作为一手证据 | 仅 P-existence；P-mechanism/P-outcome 不纳入 |
| 2026-03-25 | Anthropic《How we built Claude Code auto mode》 | 以 transcript classifier 替代部分逐动作审批；拒绝后 deny-and-continue，3 连拒/20 总拒熔断；自动扩大“动作层”自主度，但不是下一轮调度 | P-mechanism；内部样本仅有限 P-outcome |
| 2026-04-30 | OpenAI《Auto-review of agent actions without synchronous human oversight》 | 独立审批 agent 替代 sandbox 边界的同步人工批准；拒绝给理由继续；反复拒绝停止轨迹；明确承认非安全保证 | P-mechanism + 有限 P-outcome；OpenAI |
| 2026-06-07 | Addy Osmani《Loop Engineering》 | 明确定义“替代人逐轮提示”；系统找工作、分发、检查、记录完成并决定下一项；loop “one floor above harness” | P-existence + P-mechanism；个人作者，且引用 Cherny/Steinberger |
| 2026-06-16 | LangChain/Sydney Runkle《The Art of Loop Engineering》 | 四环：agent、verification、event-driven、hill-climbing；最后一环直接改写 harness，显示 loop/harness 边界可互相嵌套 | P-existence + P-mechanism；厂商利益相关 |
| 2026-06-30 | Claude Code 团队《Loop engineering: Getting started with loops》 | 官方把 loop 定义为反复工作直到 stop condition；agentic/goal/time/proactive 四类产品模式 | P-existence + P-mechanism；Anthropic，和 2024/2025/auto mode 同机构簇 |
| 2026-08-14 | Osmani《Practical Loop Engineering》 | `/goal` = bounded task 的条件驱动；`/loop` = 定时调度；独立 evaluator 只查 transcript hard rules，不判断内容好坏；明确任务适配和人工 taste 边界 | P-existence + P-mechanism；个人作者/Claude Code 引用链 |
| 2026-09-27 | 本轮观测 | 官方页面、文档和现有 evidence/digested 交叉核对；OpenAI harness 正文仍不可达 | 观测日期，不是来源发布日期 |

## 三、来源档案（URL、日期、原文摘录与最小主张）

### Source 1 · Anthropic《Building effective agents》

- URL：https://www.anthropic.com/research/building-effective-agents （当前跳转到 https://www.anthropic.com/engineering/building-effective-agents）
- 作者：Erik S.、Barry Zhang；机构：Anthropic
- 发布日期：2024-12-19
- 访问/观测日期：2026-09-27
- 来源类型：厂商官方工程文；一手
- 原文摘录：
  - “Workflows are systems where LLMs and tools are orchestrated through predefined code paths.”
  - “Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.”
  - “During execution, it's crucial for the agents to gain ‘ground truth’ from the environment at each step ... Agents can then pause for human feedback at checkpoints or when encountering blockers.”
  - “They are typically just LLMs using tools based on environmental feedback in a loop.”
  - “The task often terminates upon completion, but it’s also common to include stopping conditions (such as a maximum number of iterations) to maintain control.”
  - “Code solutions are verifiable through automated tests; Agents can iterate on solutions using test results as feedback...”
- 支持的最小主张：Anthropic 在 2024 年已将“固定路径 workflow”与“模型动态指挥过程的 agent”区分，并把 environment feedback、循环、停止上限、人工 checkpoint 作为机制要素。编码任务因可测试而适合反馈循环。
- P 等级：P-existence + P-mechanism；没有该来源独立的 coding-agent outcome 对照。
- 负结论：未证明行业普遍从 automation 转向 autonomy；未证明 agent loop 比固定 workflow 的质量/成本更好；页面自己提醒 2024 tooling landscape 已变化。
- 偏差/限制：Anthropic 的定义和客户经验有厂商视角；“agents are typically...”是架构概括，不是产品采用率统计；同机构后续文档不能作为独立机构票。

### Source 2 · Geoffrey Huntley《Ralph Wiggum as a “software engineer”》

- URL：https://ghuntley.com/ralph/
- 作者：Geoffrey Huntley；发布：2025-07-14；访问/观测：2026-09-27
- 来源类型：作者本人原文；一手实践报告/方法文
- 原文摘录：
  - “Ralph is a technique. In its purest form, Ralph is a Bash loop.”
  - `while :; do cat PROMPT.md | claude-code ; done`
  - “Anything can be wired in as back pressure to reject invalid code generation. That could be security scanners, it could be static analysers, it could be anything.”
  - “After implementing functionality or resolving problems, run the tests for that unit of code that was improved.”
  - “Eventually, Ralph will run out of things to do in the TODO list. Or, it goes completely off track. ... it’s a matter of taste.”
  - “There’s no way in heck would I use Ralph in an existing code base” / “This works best as a technique for bootstrapping Greenfield...”
- 支持的最小主张：循环、反馈闸门、外置规格/todo、模型选择下一项和人工 taste 在 2025 已存在；Ralph 的自主性是强约束下的实验性自治，不是可靠的普适生产模式。
- P 等级：P-existence + P-mechanism；作者还给出个人成本案例，但不是受控 P-outcome。
- 负结论：Ralph 本身没有内建的可靠停止条件；无限 while 不等于自主完成；作者明确承认跑偏、坏代码、需要人工 judgment，并把适用范围限于 greenfield。
- 偏差/限制：单作者、个人项目、强烈立场；方法文不是独立评估；“eventual consistency”不能替代完成证明；其案例不能外推 brownfield、安全/金融任务。

### Source 3 · Anthropic《Effective harnesses for long-running agents》

- URL：https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- 作者：Justin Young；机构：Anthropic；发布：2025-11-26；访问/观测：2026-09-27
- 来源类型：厂商官方工程复盘；一手
- 原文摘录：
  - “getting agents to make consistent progress across multiple context windows remains an open problem.”
  - “an initializer agent ... and a coding agent ... making incremental progress in every session, while leaving clear artifacts for the next session.”
  - “After some features had already been built, a later agent instance would look around, see that progress had been made, and declare the job done.”
  - feature list 的结构包含 `description`, `steps`, `passes: false`；“Only mark features as ‘passing’ after careful testing.”
  - 每轮启动顺序：“Read the git logs and progress files ... Read the features list file and choose the highest-priority feature that’s not yet done to work on.”
  - “Claude ... would fail [to] recognize that the feature didn’t work end-to-end” unless explicitly prompted to use browser automation.
- 支持的最小主张：长程 autonomy 的瓶颈不是“再给一个 prompt”，而是跨 context 的外部状态、取题顺序、增量边界、端到端验证和 clean state；harness 把这些控制点显式化。
- P 等级：P-existence + P-mechanism；文中报告“dramatically improved performance”但没有受控基线、完整样本或可复核指标，不能单独作为强 P-outcome。
- 负结论：feature list、git、progress 证明有机制，不证明跨团队采用、不证明跨 feature 全局队列已解决、不证明任何长程任务都适合自主循环。
- 偏差/限制：Anthropic 内部 demo，full-stack web app 场景；同一机构的 2024 agent 定义、2026 auto mode/Claude docs不能作为独立机构复现。

### Source 4 · OpenAI《Harness engineering: leveraging Codex in an agent-first world》

- URL：https://openai.com/index/harness-engineering/
- 作者/机构：OpenAI（官方页面；作者/页面正文当前不可达）
- 发布日期：**2026-02-11（由可达的索引/线索标示；OpenAI 正文未核验，故不是已核实的一手日期）**
- 访问/观测日期：2026-09-27
- 来源类型：目标一手来源，但本环境站点级 HTTP 403
- 原文摘录：**未取得**。`web_fetch` 原 URL 返回 HTTP 403；对照检查同站其他已知 OpenAI index 页面也返回 403。未把搜索摘要、二手讲解或“约 1M 行/1,500 PR/0 手写代码”写作 OpenAI 原文引句。
- 支持的最小主张：仅能确认 OpenAI 官方存在名为 harness engineering 的页面/命名对象（P-existence，且发布日期仍待官方正文核验）。不能从本档案把该文的机制或产出数字当作一手事实。
- 负结论：OpenAI harness 正文不可达，因此本轮不能逐字核实其 harness 定义、context/guardrail/feedback loop 机制、自动化规模或 outcome；搜索到的二手摘要不入一手证据票。
- 偏差/限制：这是来源可达性限制，不是对 OpenAI 主张真伪的否定；不要将“未取得”写成“OpenAI 没有该机制”。该来源不能支撑本假设的因果箭头。

### Source 5 · Claude Code 官方 loop/goal 文档

- URL：https://claude.com/blog/getting-started-with-loops
- 发布：2026-06-30；访问/观测：2026-09-27；作者：Delba de Oliveira、Michael Segner；机构：Anthropic/Claude Code
- 交叉 URL：https://code.claude.com/docs/en/goal（活文档，无单页发布日期）与 https://code.claude.com/docs/en/scheduled-tasks（活文档，无单页发布日期）
- 原文摘录：
  - “On the Claude Code team, we define loops as agents repeating cycles of work until a stop condition is met.”
  - “Every prompt you send starts a manual loop with you directing each turn.”
  - “Each time Claude tries to stop, an evaluator model checks your condition and sends it back to work until the goal is met or a number of turns you define is reached.”
  - `/goal`：“The `/goal` command sets a completion condition and Claude keeps working toward it without you prompting each step.”
  - `/goal` evaluator：“completion is decided by a fresh model rather than the one doing the work.”
  - 官方比较表：`/goal` 在前一 turn 后继续，条件 met/impossible、错误或 clear 时停；`/loop` 在时间间隔后启动，用户停止或 Claude 判断完成时停；Stop hook 由脚本/提示决定。
  - `/loop` 文档：“Recurring tasks automatically expire 7 days after creation.”；无 prompt 时维护流程继续未完工作、PR/CI、清理，但“不 start new initiatives outside that scope”。
- 支持的最小主张：Anthropic 已把 trigger、stop、evaluator、schedule 和 scope 作为产品原语区分；`/goal` 是 bounded autonomy，`/loop` 是时间自动化；二者可组合但不是同义。
- P 等级：P-existence + P-mechanism；无公开跨产品 outcome。
- 负结论：auto mode 或 `/loop` 的存在不证明 autonomous quality；`/goal` evaluator 只判断条件/ transcript hard rules，不是通用内容质量审查；官方四类模式不是成熟度等级。
- 偏差/限制：Anthropic 产品文档，描述自家实现；博客与 docs 同属一个机构证据簇，不能算两家独立来源。

### Source 6 · Claude Code auto mode 官方工程文与文档

- URL：https://www.anthropic.com/engineering/claude-code-auto-mode
- 交叉 URL：https://code.claude.com/docs/en/permission-modes
- 作者：John Hughes；机构：Anthropic；发布：2026-03-25（博客）；文档无单页发布日期；访问/观测：2026-09-27
- 原文摘录：
  - “Claude Code users approve 93% of permission prompts.”
  - “The transcript classifier sees only user messages and the agent’s tool calls; we strip out Claude’s own messages and tool outputs, making it reasoning-blind by design.”
  - “If a session accumulates 3 consecutive denials or 20 total, we stop the model and escalate to the human.”
  - “Auto mode on its own approves tool calls within a single turn but doesn’t start a new one.”
- 支持的最小主张：harness/permission 层可以把逐动作人工审批替换成独立分类器、deny-and-continue 与熔断，因而扩大动作层 autonomy；但它不负责选择下一轮。
- P 等级：P-existence + P-mechanism；博客有内部 n=10,000 real traffic、n=52 real overeager、n=1,000 synthetic exfil 数据，但这些是单厂商评测，不能直接变成通用 P-outcome。
- 负结论：auto mode 不是 loop scheduler；不能证明“少审批”提升 coding quality 或减少返工；官方列出过度主动、误判、prompt injection 等风险。
- 偏差/限制：厂商自建评测与威胁模型；指标针对 permission safety/friction，不针对端到端软件交付；与 Anthropic 其他材料同机构去重。

### Source 7 · OpenAI《Auto-review of agent actions without synchronous human oversight》

- URL：https://alignment.openai.com/auto-review/
- 作者：Maja Trębacz、Sam Arnesen、Ollie Matthews、Dylan Hurd、Won Park、Owen Lin、Joe Gershenson；机构：OpenAI
- 发布：2026-04-30；访问/观测：2026-09-27
- 来源类型：官方 Alignment Research Blog；一手
- 原文摘录：
  - “Auto-review offers a safer default for deploying coding agents, using a separate agent to approve or deny boundary-crossing actions.”
  - “Codex sessions stop for human approval roughly 200x less often ... For the small fraction that need review, Auto-review approves around 99%.”
  - “The separation of roles matters. The main agent is optimized to complete the user’s task. Auto-review has a narrower job: decide whether a proposed boundary-crossing action should run.”
  - “A rejection does not merely say no. It gives Codex a rationale ... Codex continues after a denial and successfully finds an acceptable solution in more than half of cases.”
  - “Auto-review should not be treated as a guarantee of security.”
- 支持的最小主张：独立审批 agent 是 harness 中的权限/边界守门器；拒绝反馈可以驱动主 agent 改路径；这是一种“扩大行动自治、保留风险熔断”的机制。
- P 等级：P-existence + P-mechanism；有限 P-outcome（OpenAI 内部 traffic/evals 的审批率、召回率）。
- 负结论：不能证明 coding 质量、生产吞吐或长期 autonomy outcome；页面明确不是 deterministic security guarantee，且 sandbox 内部行为可能不被该审批器看见。
- 偏差/限制：OpenAI 内部 deployment 与 synthetic/red-team 数据；与 OpenAI harness engineering 属同机构；不能作为第二家机构独立复现。

### Source 8 · Addy Osmani《Loop Engineering》

- URL：https://addyosmani.com/blog/loop-engineering/
- 作者：Addy Osmani（Anthropic MTS，个人博客）；发布：2026-06-07；访问/观测：2026-09-27
- 来源类型：作者本人原文；一手命名/定义材料
- 原文摘录：
  - “Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead.”
  - “Now you build a small system that finds the work, hands it out, checks it, writes down what is done and then decides the next thing...”
  - “Loop engineering sits one floor above the harness.”
  - “A loop needs five things and then one place to remember stuff.”（automations、worktrees、skills、plugins/connectors、sub-agents，加 memory）
  - “A loop running unattended is also a loop making mistakes unattended”; “done is a claim and not a proof.”
- 支持的最小主张：loop engineering 把人工逐轮提示替换成取题、分发、验证、状态、下一项选择的系统；作者明确提出 loop 与 harness 的层次关系，并把无人值守错误作为风险。
- P 等级：P-existence + P-mechanism；五件套是作者 checklist/建议，不是行业准入条件。
- 负结论：不能证明 loop 已取代直接 prompting、harness，或所有循环都要五件套；作者自己承认仍早期、token 成本和人工判断重要。
- 偏差/限制：个人观点；文章转引 Cherny/Steinberger，不能为二人增加原始证据票；作者与 Anthropic 有职业关系，涉及 Claude Code 的内容需与官方 Anthropic 机构证据去重/标注引用链。

### Source 9 · Addy Osmani《Practical Loop Engineering》

- URL：https://addyosmani.com/blog/practical-loop-engineering/
- 作者：Addy Osmani；发布：2026-08-14；访问/观测：2026-09-27
- 来源类型：作者本人原文；一手实践建议
- 原文摘录：
  - “A loop is an autonomous, self-correcting feedback cycle where an AI agent repeatedly acts, tests its results and adjusts its approach until a specific goal is met.”
  - “goal primitive ... a single bounded task”；“loop reruns on a timer or a fixed interval.”
  - “The evaluator sitting behind goal ... doesn’t look at the content to see if it’s good or bad ... [it] examine[s] the conversation transcript to see if the hard rules ... have been met.”
  - “Tasks that require human taste, subjective design, or open-ended creative exploration aren’t a good fit.”
  - “One sub-agent drafts the change. A separate one verifies it.”
  - “Recurring loops expire seven days after creation ... loops are session-scoped.”
- 支持的最小主张：目标驱动 autonomy 需要明确 end-state、约束、验证工具和上限；`/goal` 与 `/loop` 分别承担 bounded completion 与 scheduling；内容质量和 taste 仍需独立 checker/人。
- P 等级：P-existence + P-mechanism；个人每天 agent 数量/并发是个人观察，不是 outcome 或阈值。
- 负结论：不能把“autonomous”解读为任意任务可无人值守；不能把 `/goal` evaluator 当质量裁判；不能推出固定并发上限、行业采用率或普遍 ROI。
- 偏差/限制：个人实践和产品生态建议；与 Source 5 的 Claude Code 描述有引用链，不能重复计票；示例多为清晰、可测、低风险任务。

### Source 10 · LangChain/Sydney Runkle《The Art of Loop Engineering》

- URL：https://www.langchain.com/blog/the-art-of-loop-engineering
- 作者：Sydney Runkle；机构：LangChain；发布：2026-06-16；访问/观测：2026-09-27
- 来源类型：厂商官方工程博客；一手
- 原文摘录：
  - “The core agent algorithm is simple: give the LLM context and let it call tools in a loop until it's done.”
  - “The verification loop adds a grader ... against a rubric ... sends the result back with feedback.”
  - “The event-driven loop connects your agent to your ecosystem. An event fires ... a schedule triggers, a webhook arrives...”
  - “The hill climbing loop runs an analysis agent over those traces and uses the findings to rewrite the harness with improved configuration.”
  - “Automation doesn't mean removing humans from the loop.”
- 支持的最小主张：loop 可分层为行动、验证、事件触发、trace→harness 改进；此模型直接展示 harness 与 loop 的反馈接口，并保留敏感动作的人审点。
- P 等级：P-existence + P-mechanism；厂商产品映射，不是跨组织 outcome。
- 负结论：四环不是 Osmani/Claude Code 的统一 taxonomy；hill-climbing 纳入 loop 与“loop 在 harness 之上”的说法存在外延冲突；不能证明 LangChain 的原语提升真实交付质量。
- 偏差/限制：LangChain 的产品动机明显（create_agent、RubricMiddleware、LangSmith Engine）；文中引用 Steipete/Boris/Andrej，不增加原始来源票；“no manual review needed”只限示例中的链接/CI/范围错误类别。

## 四、支持链：什么被材料支持，什么只是解释

### A. 由 automation 向 bounded autonomy 的机制链（支持到 P-mechanism）

1. Anthropic 2024 把预定义 workflow 与模型动态指导自身过程的 agent 分开；这是概念上的 automation/autonomy 分叉。
2. Ralph 展示了自动重复调用、规格/todo 取题、back pressure 和模型选择下一项；但它的无限循环、人工 taste 和 greenfield 限定说明“自动运行”仍不等于可靠 autonomy。
3. Claude Code 官方把权限 auto mode、`/loop`、`/goal` 分开：auto mode 解决轮内动作批准；`/loop` 解决时间触发；`/goal` 解决围绕完成条件的多轮推进。这个拆分是最清楚的产品机制证据。
4. OpenAI auto-review 以独立 agent 处理边界审批，拒绝后继续找安全路径；它扩大了“可以在无人同步审批下行动”的范围，但不选择产品任务的下一项。
5. 因此可以支持的最小句子是：**coding agent 的自治正在从“人不必批准每个动作”扩展到“系统在明确目标、反馈、权限和熔断下选择后续行动”**。不能支持“自动化已被 autonomy 取代”。

### B. harness 成熟使 loop 被暴露/产品化的机制链（支持到 P-mechanism，因果仍是竞争解释）

1. 单次 harness 先把工具、上下文、权限、sandbox 和验证变得可用；Anthropic 2025 进一步把 progress、feature_list、git 和端到端测试外置，解决跨 context “不知道做到哪/提前宣布完成”。
2. 一旦单次运行有 clean state 与可回读状态，剩下的控制问题被显性化：下一项从哪里来、谁选、何时重新触发、何时停止、谁独立验收、失败如何升级。
3. Osmani 直接把这组问题命名为“loop engineering”，并说其在 harness 之上；Claude Code 将 goal/loop/proactive 产品化；LangChain 将 event-driven 与 trace→harness 纳入循环栈。
4. 所以支持的最小句子是：**harness 的状态、反馈和守门能力使 loop engineering 更可设计、更可观察，也把原本隐藏在人工催促中的控制问题暴露出来。**
5. 但时间顺序不能单独证明“harness 成熟导致 loop engineering”：Anthropic 2024 已有 loop，Ralph 2025 已有循环；LangChain 甚至把“改 harness”的元循环纳入 loop。更可能是相互强化/共同演化：harness 为 loop 提供可运行基础，loop 的失败 trace 又推动 harness 改进。

## 五、反例与边界

| 反例 | 直接来源/机制 | 对假设的修正 |
|---|---|---|
| 有 automation 没有 autonomy | Claude Code auto mode 官方写明“within a single turn but doesn’t start a new one”；固定 `/loop` 只按时间启动 | 自动审批/定时不等于系统选择下一项工作 |
| 有 autonomy 没有成熟 harness | Ralph 的 Bash `while` 可让模型选择 todo 下一项，但作者承认跑偏、坏代码、人工 taste、greenfield 限定 | autonomy 可以先以脆弱的脚本存在，harness 不是逻辑前提的唯一实现 |
| 有 harness 仍不能可靠完成 | Anthropic 2025 记录 agent 仍会 one-shot、提前宣布完成、只做单测/curl 而非端到端；Böckeler 材料还指出 AI-generated tests 不足 | harness 只是把控制点显式化，不保证行为面验证或完成判断正确 |
| 有 loop 反而放大错误/债务 | Osmani：“unattended loop”会无人值守地犯错；comprehension debt/cognitive surrender；Ralph 需要 signs/back pressure | 更多自动循环可能扩大错误速度与理解债务，不是 outcome 自动改善 |
| 硬门不覆盖意图/体验 | `/goal` evaluator 只查 transcript hard rules；LangChain grader 只覆盖 rubric 类别；Anthropic 浏览器自动化也有视觉/原生弹窗限制 | stop condition、动作安全和内容质量是不同层的验证 |
| 复杂循环不一定适合任务 | Anthropic 2024 建议从简单方案起步；Osmani 明确主观 taste、开放式创作、模糊“good”不适合 loop | 不存在从 automation 到 autonomy 的单向升级阶梯，需按任务适配 |
| 自动审批不是安全保证 | OpenAI auto-review 明确可被误导；Anthropic auto mode 报告 17% real overeager false-negative（full pipeline）并承认残余风险 | autonomy 需要互补监控、sandbox、人工高风险点，不能只靠一个 evaluator |
| 外层调度仍未解决跨 feature 全局控制 | 现有 DSH evidence 显示 goal/todo/plan/session log 主要是 single-session；Claude/Anthropic案例是项目内文件，不是通用 multi-feature queue | loop 的跨 feature 可见性仍是开放问题，不能从单任务 goal 推出组织级 autonomy |

## 六、负结论与不能证明的因果

### 已主动搜过但不能纳入的内容

- OpenAI harness engineering 官方 URL 已访问；站点级 HTTP 403，未取得正文。搜索摘要、二手指南、媒体和讲座整理只能作线索，不能代替逐字一手证据。
- OpenAI auto-review 的官方正文可取得，但它证明的是审批/权限机制与内部安全评估，不证明 harness engineering 文章中所称的生产吞吐、代码质量或组织级自治效果。
- Claude Code 活文档没有统一历史发布日期；本档案分别记录“页面发布日期”和“观测日期”，不把当前页面状态伪装成历史 adoption 时间。

### 不能推出的因果句

1. 不能从“harness engineering”在 2026 被命名，推出 harness 在此之前不存在，或 loop 因它才诞生。
2. 不能从 Anthropic 2025 先写 long-running harness、Osmani/LangChain 2026 后写 loop，推出 harness 是 loop 命名/采用的充分原因；缺少同一组织的前后对照、反事实和跨机构 adoption 数据。
3. 不能从 `/goal`、`/loop`、auto mode、Auto-review 的产品存在，推出用户实际使用、生产质量、返工率、吞吐或把控感改善。
4. 不能从内部评测的审批率/拒绝率推出“自主编码质量更高”；这些指标最多是权限摩擦或危险动作识别的 outcome。
5. 不能从 LangChain 的四环或 Osmani 的五件套推出 loop engineering 的统一标准；二者在“改 harness 是否属于 loop”“rubric grader 是否等同硬停止条件”上存在外延冲突。
6. 不能把“人不再逐动作审批”写成“人退出系统”。Anthropic、OpenAI、LangChain 和 Osmani 都保留高风险动作、模糊意图、最终质量/品味或升级熔断的人类责任。
7. 不能把跨 context 的 durable memory 写成跨 feature 的工作队列；状态可恢复不等于候选、优先级、在途、阻塞、验收和回滚对人可见。

## 七、综合判读与后续可检验命题

### 当前判读

- **高置信（P-existence/P-mechanism）**：coding agent 的设计重心正在从“每轮由人提供下一句 prompt”扩展到“系统提供目标、环境反馈、权限边界、验证器、外部状态和下一步选择”。`/goal`、`/loop`、auto mode、Auto-review 是不同控制面，不应合并为一个“autonomy”按钮。
- **中置信（机制解释）**：harness 成熟会暴露 loop engineering，因为当工具/状态/验证不再完全依赖人盯住单次 turn 后，系统必须显式承担取题、调度、停止、升级和复盘；但 loop 的构件早于该命名，故“促成”应写成“提供可行条件/放大可见性”，不要写成单向因果。
- **低置信（P-outcome）**：尚无跨机构、受控、端到端证据证明从 automation 到 autonomy 带来普遍更高质量、更少返工或更低人时。现有 outcome 主要是厂商内部 permission/safety/friction 指标或单作者案例。

### 可检验命题（不当成已证实结论）

1. 在同一 coding task 上，对照“单轮 automation”“`/goal` bounded autonomy”“外置工作来源 + `/goal` + 独立 checker”，记录下一步选择、提前完成、返工、人工介入和成本；只有这种对照才能检验 autonomy 是否带来 outcome。
2. 在相同模型与任务上逐层加入 harness：权限/sandbox → 外部状态 → 验证器 → 调度器，观察 loop 是否从隐藏人工催促变为可观察机制；同时记录新增复杂度、误停和错误复制。
3. 将“动作面安全”（auto mode/auto-review 的 deny）与“行为面正确”（feature/场景/浏览器验证）分开计量，避免把审批放行率当作代码质量。
4. 以跨 feature queue、current pointer、blocked reason、accepted/rolled-back 状态为观察单位，检验单 session loop 是否真正升级为组织级 autonomous workflow。

## 与既有材料的关系

- 与 `evidence-a` 一致：Osmani 把 loop 置于 harness 之上，但 LangChain 的 hill-climbing 把改 harness 纳入 loop，外延未收敛。
- 与 `evidence-b` 一致：停止条件骨架是可核判据 + 硬上限/熔断 + 验收与干活分离；裁判权仍分歧。
- 与 `evidence-c` 一致：自主度位置词汇存在，但没有通用轮次阈值；风险/动作/歧义事件比轮次更接近现有判据。
- 与 `evidence-g` 一致：goal/todo/plan/session persistence 能支撑单 session 续轮与记忆，但不等于跨 feature queue 或独立完成认证。
- 本档案新增的 H 路收口：**automation → autonomy 是控制权从触发/执行向目标内下一步选择扩展；harness → loop 是“提供条件并暴露控制问题”的竞争解释，而不是已证实的单向因果。**
