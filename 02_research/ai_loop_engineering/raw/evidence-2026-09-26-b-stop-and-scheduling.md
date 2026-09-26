---
type: evidence_archive
collected_by: 委派回源子代理（B 路 · 停止条件与外层调度）
collected_at: 2026-09-26
serves: digested 构件篇 · 03_practice/loop_governance/result/backbone.md（停止条件 / 外层调度两节）
status: 7 组一手全文取得（Ralph / Building effective agents / Effective harnesses / CC /goal / CC auto mode / CC /loop / OpenAI auto-review / LangChain 四环）
negatives: 4 条见文末（Unwinding Codex's Agent Loop 站点级 403 未取得——"四拍循环/assistant message 终止态"未逐字核实，引用前必须回源）
quality_bar: 2026-09-26 用户质量门槛——只收高影响力一手；不入册内容单列文末「不入册·仅社区情绪」
---

# 回源报告 B：停止条件与外层调度（访问日期 2026-09-26）

> **任务**：为 "loop engineering"（2026-06 起流行的术语）回源两个构件的机制证据——
> 问题 1：停止条件怎么写才算可核；问题 2：外层调度由什么承担。
> **口径**：只收一手源（官方博客原文 / 官方文档 / 官方 changelog / 作者本人原始文章）。
> 每条引句标注支撑 Q1（停止条件）还是 Q2（外层调度）。
> 访问日期统一为 2026-09-26（终端 `date` 实测）；发布日期为页面标注。
> 种子线索：本仓库 `talk-harness-201/02_evidence/01-kol-alignment-2026.md` +
> `/Users/bowhead/deepseek-harness/_faq_on_digested/15_loop-engineering-vs-sdd/research.md`（二手，仅作 URL 线索，未当证据）。

---

## 问题 1：停止条件

### 1. Geoffrey Huntley — Ralph Wiggum loop

- **一手源记录**
  - URL：https://ghuntley.com/ralph/ （页面标题 "Ralph Wiggum as a 'software engineer'"）
  - 作者：Geoffrey Huntley（页面署名 "By Geoffrey Huntley in AI"）
  - 发布日期：14 Jul 2025（页面标注）
  - 访问日期：2026-09-26（HTTP 200，全文取得）
  - **为什么算高影响力**：Ralph Wiggum loop 的命名原文，loop engineering 谱系公认的起点文献（marmelab 2026 审计、VentureBeat/The Register 报道均以此文为源头——后者是二手，仅佐证影响力）。
- **逐字引句**
  - 定义（Q1+Q2 总纲）：
    > "Ralph is a technique. In its purest form, Ralph is a Bash loop."
    代码块原文：`while :; do cat PROMPT.md | claude-code ; done`
  - 无限循环的前提（Q1）：
    > "Ralph can be done with any tool that does not cap tool calls and usage."
  - **back pressure 是什么**（Q1——Ralph 的逐轮"接受/拒绝"闸门）：
    > "In the diagram above, it just shows the words 'test and build', but this is where you put your engineering hat on. Anything can be wired in as back pressure to reject invalid code generation. That could be security scanners, it could be static analysers, it could be anything. But the key collective sum is that the wheel has got to turn fast."
    > "Specific programming languages have inbuilt back pressure through their type system."
    > "If you're using a dynamically typed language, I must stress the importance of wiring in a static analyser/type checker when Ralphing"（文中列出 dialyzer、pyrefly）
  - 每轮测试闸门（Q1）：
    > "After implementing functionality or resolving problems, run the tests for that unit of code that was improved."
  - **signs（"牌子"）是什么**（Q1——把踩坑教训写成环境内的持久提示，让下轮循环自己看见）：
    > "Ralph is very good at making playgrounds, but he comes home bruised because he fell off the slide, so one then tunes Ralph by adding a sign next to the slide saying 'SLIDE DOWN, DON'T JUMP, LOOK AROUND,' and Ralph is more likely to look and see the sign."
    > "Eventually all Ralph thinks about is the signs so that's when you get a new Ralph that doesn't feel defective like Ralph, at all."
    具体牌子的实例（文中 prompt 原文）：
    > "Before making changes search codebase (don't assume an item is not implemented) using parrallel subagents. Think hard."
    > "DO NOT IMPLEMENT PLACEHOLDER OR SIMPLE IMPLEMENTATIONS. WE WANT FULL IMPLEMENTATIONS. DO IT OR I WILL YELL AT YOU"
  - **循环怎么终止**（Q1——Ralph 没有内建停止条件，终止是操作者对 TODO 清单耗尽的判断）：
    > "Eventually, Ralph will run out of things to do in the TODO list. Or, it goes completely off track. It's Ralph Wiggum, after all. It's at this stage where it's a matter of taste. Through building of CURSED, I have deleted the TODO list multiple times. The TODO list is what I'm watching like a hawk. And I throw it out often."
    > "Now, if I throw the TODO list out, you might be asking, 'Well, how does it know what the next step is?' Well, it's simple. You run a Ralph loop with explicit instructions such as above to generate a new TODO list."
    每轮"绿灯"的机器判定（git tag）：
    > "As soon as there are no build or test errors create a git tag. If there are no git tags start at 0.0.0 and increment patch by 1 for example 0.0.1 if 0.0.0 does not exist."
  - 失败兜底（Q1）：人做判断，`git reset --hard` 或换一系列 prompt：
    > "you'll wake up to a broken codebase that doesn't compile from time to time, and you'll have situations where Ralph can't fix it himself. This is where you need to put your brain on. You need to make a judgment call. Is it easier to do a `git reset --hard` and to kick Ralph back off again? Or do you need to come up with another series of prompts to be able to rescue Ralph?"
  - 反例边界（Q1）：Ralph 不用于存量代码库：
    > "There's no way in heck would I use Ralph in an existing code base"
    > "This works best as a technique for bootstrapping Greenfield, with the expectation you'll get 90% done with it."
- **机制描述（Q1 视角）**
  - `while :;` 是**故意无限的**：终止条件不写在循环里。逐轮的"可核闸门"全部是 back pressure（类型系统/测试/linter/静态分析/安全扫描）——即"不会说谎的裁判"；循环级终止由操作者看 TODO 清单（fix_plan.md）是否耗尽/跑偏，凭 taste 决定，且清单本身可整体扔掉重生成。
  - 另有防作弊条款：测试必须当场写明"为什么存在"（`"capture the why tests and the backing implementation is important"`），因为"future loops will not have the reasoning in their context window"（逐字：> "it's crucial in that moment to ask Ralph to write out the meaning and the importance of the test explaining what it's trying to do."）。
  - 关键反例样本（Q1）：Huntley 亲述的失败模式是模型"reward function is compiling code"导致占位实现（> "Claude has the inherent bias to do minimal and placeholder implementations."），对策是牌子 + "run more Ralphs to identify placeholders and minimal implementations and transform that into a to-do list for future Ralph loops"。

### 2. Anthropic《Building effective agents》

- **一手源记录**
  - URL：https://www.anthropic.com/research/building-effective-agents （现跳转到 https://www.anthropic.com/engineering/building-effective-agents ，两者同文）
  - 作者：Erik S. 和 Barry Zhang（页尾 "Written by Erik S. and Barry Zhang."）
  - 发布日期：Dec 19, 2024（页面标注 "Published Dec 19, 2024"）
  - 访问日期：2026-09-26（HTTP 200，全文取得）
  - **为什么算高影响力**：Anthropic 官方工程博客，"agents = LLMs using tools based on environmental feedback in a loop" 这一定义的出处，业界引用最广的 agents 结构文献；Anthropic 同时是 Claude Code 的厂商。
  - 注意：页面顶部现有官方注记——"Note: Much of the tooling landscape described in this post has changed since December 2024. For our current approach, see how we built Claude Managed Agents"（引用时注明）。
- **逐字引句**
  - agents 定义（Q1+Q2 总纲）：
    > "Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop."
  - **停止条件的成型写法**（Q1）：
    > "During execution, it's crucial for the agents to gain 'ground truth' from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control."
  - 评估器-优化器工作流（Q1——生成/验收分离的雏形）：
    > "In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop."
    > "This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value."
  - 编码 agent 为什么适合做循环（Q1——可核性来源）：
    > "Code solutions are verifiable through automated tests; Agents can iterate on solutions using test results as feedback; The problem space is well-defined and structured; and Output quality can be measured objectively."
  - 人工检查点定位（Q1/Q2）：
    > "Agents can then pause for human feedback at checkpoints or when encountering blockers."
- **机制描述（Q1 视角）**：停止条件两种成型形态被并列写出——①任务完成即终止（模型判定）+ ②资源上限（最大迭代次数）作为控制手段；可核性来自环境 ground truth（工具结果/代码执行），编码域的可核裁判是自动化测试；验收角色建议与生成角色分离（evaluator-optimizer）。

### 3. Anthropic《Effective harnesses for long-running agents》

- **一手源记录**
  - URL：https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
  - 作者：Justin Young（页尾 "Written by Justin Young."）
  - 发布日期：Nov 26, 2025（页面标注 "Published Nov 26, 2025"）
  - 访问日期：2026-09-26（HTTP 200，全文取得）
  - 配套代码：文中链接官方 quickstart https://github.com/anthropics/claude-quickstarts/tree/main/autonomous-coding
  - **为什么算高影响力**：Anthropic 官方工程博客；feature_list.json 进度规格模式的唯一一手出处，也是"提前宣告完成"被官方点名为长程 agent 头号失败模式的一手出处。
- **逐字引句（全部与 Q1 相关，feature_list.json 的结构/初始状态/保护条款/选型理由逐字如下）**
  - 失败模式之一：one-shot（> "the agent tended to try to do too much at once—essentially to attempt to one-shot the app."）
  - **失败模式之二：提前宣告完成**（Q1）：
    > "A second failure mode would often occur later in a project. After some features had already been built, a later agent instance would look around, see that progress had been made, and declare the job done."
  - **feature_list 的规模与初始状态**（Q1+Q2）：
    > "To address the problem of the agent one-shotting an app or prematurely considering the project complete, we prompted the initializer agent to write a comprehensive file of feature requirements expanding on the user's initial prompt. In the claude.ai clone example, this meant over 200 features, such as 'a user can open a new chat, type in a query, press enter, and see an AI response.' These features were all initially marked as 'failing' so that later coding agents would have a clear outline of what full functionality looked like."
  - **结构（文中 JSON 原文，含初始 `passes: false`）**（Q1）：
    ```json
    {
      "category": "functional",
      "description": "New chat button creates a fresh conversation",
      "steps": [
        "Navigate to main interface",
        "Click the 'New Chat' button",
        "Verify a new conversation is created",
        "Check that chat area shows welcome state",
        "Verify conversation appears in sidebar"
      ],
      "passes": false
    }
    ```
  - **保护条款与 JSON 选型理由**（Q1）：
    > "We prompt coding agents to edit this file only by changing the status of a passes field, and we use strongly-worded instructions like 'It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality.' After some experimentation, we landed on using JSON for this, as the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files."
  - **逐条通过判定 + 端到端测试要求**（Q1）：
    > "One final major failure mode that we observed was Claude's tendency to mark a feature as complete without proper testing. Absent explicit prompting, Claude tended to make code changes, and even do testing with unit tests or `curl` commands against a development server, but would fail recognize that the feature didn't work end-to-end."
    > "In the case of building a web app, Claude mostly did well at verifying features end-to-end once explicitly prompted to use browser automation tools and do all testing as a human user would."
  - 失败模式对照表（Q1，表中原文逐字）：
    > "Claude declares victory on the entire project too early." → 对策："Set up a feature list file."
    > "Claude marks features as done prematurely." → 对策："Self-verify all features. Only mark features as 'passing' after careful testing."
- **机制描述（Q1 视角）**：停止条件被外置成**机器可核的逐条清单**——initializer 把粗目标展开成 200+ 条 feature（结构：category/description/steps/passes），初始全部 `passes: false`，"全真"即完成的可核定义；coding agent 只被允许改 `passes` 字段；测试/清单本身受强措辞保护且选 JSON 格式防整文件改写；标记通过的前置是端到端自验证（browser automation），不是单测/curl。

### 4. 其他停止条件机制（官方一手）

#### 4a. Claude Code `/goal`（官方文档）

- **一手源记录**
  - URL：https://code.claude.com/docs/en/goal （页面标题 "Keep Claude working toward a goal"）
  - 作者：Anthropic（Claude Code 官方文档站）
  - 发布日期：活文档，无单页发布日期；页内版本锚点最高到 "Claude Code v2.1.269 or later"（`/goal` 恢复逻辑）
  - 访问日期：2026-09-26（HTTP 200，全文取得）
  - **为什么算高影响力**：Claude Code 官方文档（Anthropic 产品文档），`/goal` 完成条件机制的唯一权威表述——loop engineering 时代"停止条件即原语"的厂商级落地。
- **逐字引句**
  - **机制总纲**（Q1）：
    > "The `/goal` command sets a completion condition and Claude keeps working toward it without you prompting each step. After each turn, a small fast model checks whether the condition holds. If the model judges it not yet met, Claude starts another turn instead of returning control to you. The goal clears automatically once the condition is met, if the model judges the condition impossible to satisfy, or if a turn fails on an error you have to fix."
  - **条件怎么写才算可核（官方写法指南）**（Q1）：
    > "A condition that holds up across many turns usually has: **One measurable end state**: a test result, a build exit code, a file count, an empty queue; **A stated check**: how Claude should prove it, such as '`npm test` exits 0' or '`git status` is clean'; **Constraints that matter**: anything that must not change on the way there, such as 'no other test file is modified'"
  - **资源上限写进条件**（Q1）：
    > "To bound how long a goal runs, include a turn or time clause in the condition, such as `or stop after 20 turns`."
  - **三值判定**（Q1）：
    > "The model returns one of three verdicts, each with a short reason: **Not yet met**: Claude keeps working and takes the reason as guidance for the next turn. **Met**: Claude Code clears the goal and records an achieved entry in the transcript. **Impossible**: the evaluator judged that the condition can never be satisfied."
  - **验收者与干活者分离**（Q1+Q2）：
    > "`/goal` adds a separate evaluator that checks your condition after every turn, so completion is decided by a fresh model rather than the one doing the work."
  - **无进展熔断**（Q1）：
    > "If Claude keeps answering the evaluator without making progress (no tool use for several turns in a row), Claude Code stops the loop, prints a warning, and returns control to you with the goal still set."
  - 不可恢复错误清空目标（Q1）：四类——认证失败、额度耗尽、压缩无法解决的上下文溢出、模型不可用（> "Four kinds of failure clear the goal: An authentication failure... An exhausted credit balance... A context overflow that auto-compaction couldn't clear... A model that isn't available"）；其余错误三次自动重试后暂停（> "After three automatic retries, the goal pauses instead."）
  - 底层实现（Q2）：
    > "`/goal` is a wrapper around a session-scoped prompt-based Stop hook."
- **机制描述（Q1 视角）**：`/goal` 把停止条件做成**每轮由独立小模型评估的完成条件**，判定枚举固定为三值（Not yet met / Met / Impossible）；官方对"可核条件"的写法要求＝一个可度量终态＋一个声明式检查＋路径约束，并可加轮次/时间上限子句；配两道熔断（无进展连续数轮、不可恢复错误）。

#### 4b. Claude Code auto mode 分类器熔断（官方工程博客 + 官方文档）

- **一手源记录**
  - URL 1：https://www.anthropic.com/engineering/claude-code-auto-mode （标题 "How we built Claude Code auto mode: a safer way to skip permissions"）
  - 作者：John Hughes（页尾 "Written by John Hughes."）；发布日期：Mar 25, 2026；访问日期：2026-09-26（全文取得）
  - URL 2：https://code.claude.com/docs/en/permission-modes （官方文档；访问日期 2026-09-26，全文取得）
  - **为什么算高影响力**：Anthropic 官方工程博客对 auto mode 分类器的官方解剖（含评估数据）；auto mode 现为 Claude Code 内置默认权限模式（官方文档逐字确认），是"审批循环"的现代形态。
- **逐字引句**
  - **拒绝-继续与熔断**（Q1——审批循环的停止条件）：
    > "When the transcript classifier flags an action as dangerous, that denial comes back as a tool result along with an instruction to treat the boundary in good faith: find a safer path, don't try to route around the block. If a session accumulates 3 consecutive denials or 20 total, we stop the model and escalate to the human. This is the backstop against a compromised or overeager agent repeatedly pushing towards an outcome the user wouldn't want. In headless mode (`claude -p`) there is no UI to ask the human, so we instead terminate the process."
  - 文档版同机制（Q1）：
    > "if the classifier blocks an action 3 times in a row or 20 times total, auto mode pauses and Claude Code resumes prompting. Approving the prompted action resumes auto mode. These thresholds are not configurable."
  - 分类器不看什么（Q1——评估器输入的防操纵设计）：
    > "The classifier sees only user messages and the agent's tool calls; we strip out Claude's own messages and tool outputs, making it reasoning-blind by design."
  - 默认化（Q2 背景）：
    > "With Claude Code v2.1.283 or later, auto mode is the built-in starting permission mode for interactive terminal and VS Code sessions. On earlier versions, it's the built-in starting permission mode only on Pro, Max, and Team plans."（permission-modes 文档逐字）
- **机制描述（Q1 视角）**：审批循环的停止条件是**双阈值熔断**（3 连拒或累计 20 拒→停下升级给人；headless 无 UI 则直接终止进程），阈值官方写明不可配置；单次拒绝不停循环，而是带着理由回给模型"换安全路径"。

#### 4c. Claude Code `/loop` 的终止（官方文档）

- **一手源记录**
  - URL：https://code.claude.com/docs/en/scheduled-tasks （页面标题 "Run prompts on a schedule"，含 "Run a prompt repeatedly with /loop" 一节）
  - 作者：Anthropic（Claude Code 官方文档站）；活文档无发布日期；访问日期：2026-09-26（全文取得）
  - **为什么算高影响力**：同上——Claude Code 官方文档，`/loop` 原语的唯一权威表述。
- **逐字引句（Q1）**
  - 模型自停：
    > "In self-paced mode, Claude can also end the loop on its own once the task is complete. Claude calls the `ScheduleWakeup` tool with `stop: true`, which cancels the pending wakeup immediately."
  - 兜底终止（时间上限）：
    > "Recurring tasks automatically expire 7 days after creation. The task fires one final time, then deletes itself. This bounds how long a forgotten loop can run."
    > "If an iteration ends without either rescheduling or stopping, Claude Code schedules one fallback wakeup about 20 minutes later and ends the loop when that iteration doesn't reschedule either."
- **机制描述（Q1 视角）**：定时循环的终止有四层——人按 Esc、模型判定完成主动 `stop: true`、一次未续排的 20 分钟兜底、以及**硬性 7 天过期**（官方明说这是给"被遗忘的循环"设的上界）。

#### 4d. OpenAI《Auto-review of agent actions without synchronous human oversight》

- **一手源记录**
  - URL：https://alignment.openai.com/auto-review/
  - 作者：Maja Trębacz, Sam Arnesen, Ollie Matthews, Dylan Hurd, Won Park, Owen Lin, Joe Gershenson（页面署名；文末附 BibTeX `@misc{openai2026autoreview...}`）
  - 发布日期：Apr 30, 2026（页面标注）
  - 访问日期：2026-09-26（HTTP 200，全文取得）
  - **为什么算高影响力**：OpenAI 官方 Alignment Research Blog；Codex 自动审批机制的一手出处，附评估数据与开源声明。
- **逐字引句（Q1 相关）**
  - 审批量（Q1/Q2）：
    > "In Auto-review mode, Codex sessions stop for human approval roughly 200x less often than in manual approval mode, while still catching many of the actions humans would want stopped. Most actions run without approval in the sandbox. For the small fraction that need review, Auto-review approves around 99%."
  - **熔断**（Q1）：
    > "We also monitor for cases where Codex attempts to game the Auto-reviewer. To reduce the likelihood of this occurring, we automatically stop the trajectory after repeated denials."
  - 拒绝不终止循环（Q1——deny-and-continue）：
    > "A rejection does not merely say no. It gives Codex a rationale and enough signal to continue safely without asking the user for approval or guidance. In our internal deployment, Codex continues after a denial and successfully finds an acceptable solution in more than half of cases."
  - 非保证声明（Q1 反例，官方自述边界）：
    > "Auto-review should not be treated as a guarantee of security. During automated and human red-teaming, we identified cases where Auto-review could be misled into approving commands without user approval."
- **机制描述（Q1 视角）**：审批循环停止条件＝"反复拒绝后自动停轨迹"（未给具体阈值，与 Claude Code 的 3/20 阈值同型不同参）；单次拒绝设计为**可恢复**（带理由回给模型、过半场景能自行找到安全替代路径）。

#### 4e. LangChain《The Art of Loop Engineering》——verification loop

- **一手源记录**
  - URL：https://www.langchain.com/blog/the-art-of-loop-engineering
  - 作者：Sydney Runkle（LangChain；页尾致谢含 Harrison Chase）
  - 发布日期：June 16, 2026（页面标注）
  - 访问日期：2026-09-26（HTTP 200，全文取得）
  - **为什么算高影响力**：LangChain 官方工程博客；"loop engineering" 一词在 2026-06 的厂商级体系化定义（四环模型），LangChain/LangSmith 是 agent 基础设施主要供应商。注意其产品动机（文中推销 create_agent / RubricMiddleware / LangSmith Engine），结论当作"厂商一手"用。
- **逐字引句（Q1）**
  - 内层循环定义：
    > "At its core, an agent is just a model calling tools in a loop until a task is complete."
    > "The core agent algorithm is simple: give the LLM context and let it call tools in a loop until it's done."
  - **verification loop 的可核结构**（Q1）：
    > "The verification loop adds a grader: something that checks the agent's output against a rubric and, if it fails, sends the result back with feedback. Graders can either be deterministic or agentic (LLM as a judge is a classic example, here)."
    > "For our docs writer example, the grader runs tests after each attempt, checking that all links resolve, all CI checks pass, and the diff is scoped to what was actually requested. No manual review needed to catch those classes of error."
- **机制描述（Q1 视角）**：停止条件被表述为"rubric + grader"——评分器分确定性（测试/CI/链接检查）与 agentic（LLM-as-judge）两类；不合格带反馈回环重试。四环表格原文：> "2. Verification loop | Agent runs, output is scored against a rubric, retried with feedback if it fails | Ensure work quality and correctness"。

#### 4f. OpenAI《Unwinding Codex's Agent Loop》——已确认存在、正文未取得

- **一手源记录（负结论，详见负结论清单）**
  - URL：https://openai.com/index/unwinding-codex-agent-loop/ （父代理线索：作者 Michael Bolin，2026-01-23）
  - 状态：**openai.com 全站对本环境 403**（对照实验实锤：已知存在的 openai.com/index/harness-engineering/ 同样 403；bash curl 带浏览器 UA 亦 403）。搜索发现同文另一 slug `openai.com/index/unrolling-the-codex-agent-loop/`（罗马尼亚语镜像 openai.com/ro-RO/... 亦 403）。
  - 可见的存在证据：搜索结果返回官方 ro-RO locale URL（标题 "Desfășurarea buclei agentului Codex"）；Ars Technica 2026-01 报道标题 "OpenAI spills technical details about how its AI coding agent works"（正文 405 人机验证未取得）；Michael Bolin（bolinfest）经 openai/codex 仓库大量 PR 确认为核心贡献者。
  - 其"四拍循环与终止条件"内容**未能逐字核实**，引用前须回源。

---

## 问题 2：外层调度

### 1. feature_list.json 作为进度规格（同《Effective harnesses for long-running agents》材料，调度视角）

- **一手源记录**：同上文（URL/作者/日期/访问日期/影响力理由见问题 1 第 3 条）。
- **逐字引句（Q2 视角）**
  - 双 agent 分工（Q2）：
    > "1. Initializer agent: The very first agent session uses a specialized prompt that asks the model to set up the initial environment: an `init.sh` script, a claude-progress.txt file that keeps a log of what agents have done, and an initial git commit that shows what files were added.
    > 2. Coding agent: Every subsequent session asks the model to make incremental progress, then leave structured updates."
  - **下一轮做什么：读清单选最高优先级未完成项**（Q2——外层调度的核心句）：
    > "1. _Run `pwd` to see the directory you're working in. You'll only be able to edit files in this directory._
    > 2. _Read the git logs and progress files to get up to speed on what was recently worked on._
    > 3. _Read the features list file and choose the highest-priority feature that's not yet done to work on._"
  - **每轮先过基线再干活**（Q2）：
    > "It also helps to ask the initializer agent to write an init.sh script that can run the development server, and then run through a basic end-to-end test before implementing a new feature."
    > "This ensured that Claude could quickly identify if the app had been left in a broken state, and immediately fix any existing bugs. If the agent had instead started implementing a new feature, it would likely make the problem worse."
  - **一次一件 + 干净收尾（git/进度文件）**（Q2）：
    > "the next iteration of the coding agent was then asked to work on only one feature at a time. This incremental approach turned out to be critical to addressing the agent's tendency to do too much at once."
    > "we found that the best way to elicit this behavior was to ask the model to commit its progress to git with descriptive commit messages and to write summaries of its progress in a progress file. This allowed the model to use git to revert bad code changes and recover working states of the code base."
  - 失败模式对照表（Q2 原文）：
    > "Claude leaves the environment in a state with bugs or undocumented progress." → "Start the session by reading the progress notes file and git commit logs, and run a basic test on the development server to catch any undocumented bugs. End the session by writing a git commit and progress update."
  - 未决问题（Q2——多 agent 调度是 open question）：
    > "Most notably, it's still unclear whether a single, general-purpose coding agent performs best across contexts, or if better performance can be achieved through a multi-agent architecture."
- **机制描述（Q2 视角）**：外层调度＝**文件系统里的三件持久化状态**（feature_list.json 进度规格、claude-progress.txt 叙事日志、git 历史）＋**固定开场序列**（pwd → 读 git log/progress → 选清单里最高优先级未完成项 → init.sh 拉起开发服务器过一遍基线端到端）。决定"下一轮跑什么"的不是人、不是定时器，是**规格文件里第一个 `passes: false` 的条目**。

### 2. Claude Code auto mode / `/goal` / `/loop`（官方一手）

- **一手源记录**（三个官方来源，均已在上文登记；此处按 Q2 视角摘引）
  - https://code.claude.com/docs/en/goal 、https://code.claude.com/docs/en/scheduled-tasks 、https://code.claude.com/docs/en/permission-modes 、https://code.claude.com/docs/en/auto-mode-config （均为 Anthropic 官方文档，访问日期 2026-09-26）
  - https://www.anthropic.com/engineering/claude-code-auto-mode （2026-03-25）
  - 公告博客：https://claude.com/blog/auto-mode-default-in-claude-code （标题经搜索确认："Auto mode is now the default in Claude Code for Pro, Max, and Team plans"；**正文未取得**，见负结论清单）
- **逐字引句（Q2）**
  - **三种外层调度的官方对照表**（Q2——最浓缩的一手材料，表格原文）：

    | Approach | Next turn starts when | Stops when |
    |---|---|---|
    | `/goal` | The previous turn finishes, or, in an interactive session, an idle check-in or an automatic retry comes due | A model confirms the condition is met or judges it impossible, or a turn fails on an error you have to fix, or you run `/goal clear` |
    | `/loop` | A time interval elapses | You stop it, or Claude decides the work is done |
    | Stop hook | The previous turn finishes | Your own script or prompt decides |

    （来源：/goal 文档 "Compare ways to keep a session running" 表格，逐字转录）
  - 三个原语的分工（Q2）：
    > "`/goal` and a Stop hook both fire after every turn. `/goal` is a session-scoped shortcut: you type a condition and it's active for the current session only. A Stop hook lives in your settings file, applies to every session in its scope, and can run a script for deterministic checks or a prompt for model-evaluated ones."
    > "The two are complementary: auto mode removes per-tool prompts, and `/goal` removes per-turn prompts."
  - auto mode 的调度边界（Q2——auto mode 只管轮内审批，不开下一轮）：
    > "Auto mode on its own approves tool calls within a single turn but doesn't start a new one. Claude stops when it judges the work done."
  - **闲置检查点（定时器型调度）**（Q2）：
    > "Once background work has kept the goal waiting for 30 minutes, a check-in is due. In the check-in, Claude Code lists the running tasks and asks Claude to read their output, keep waiting if they're progressing, and fix or stop any that are stuck. After the first check-in, Claude Code waits twice as long before each later check-in, up to four times the first interval."
  - `/loop` 的三种拍法（Q2）：
    > "Interval and prompt | `/loop 5m check the deploy` | Your prompt runs on a fixed schedule"
    > "Prompt only | `/loop check the deploy` | Your prompt runs at an interval Claude chooses each iteration"
    > "Interval only, or nothing | `/loop` | The built-in maintenance prompt runs, or your `loop.md` if one exists"
  - **`/loop` 的内置维护 prompt（外层调度的"下一件工作"清单化）**（Q2）：
    > "On each iteration it works through the following, in order: continue any unfinished work from the conversation; tend to the current branch's pull request: review comments, failed CI runs, merge conflicts; run cleanup passes such as bug hunts or simplification when nothing else is pending."
    > "Claude does not start new initiatives outside that scope, and irreversible actions such as pushing or deleting only proceed when they continue something the transcript already authorized."
  - loop.md 作为可定制调度规格（Q2）：`/loop` 无 prompt 时读 `.claude/loop.md`（项目级优先）或 `~/.claude/loop.md`（用户级）。
  - 三档调度面（云/桌面/会话内）的官方对照（Q2）：scheduled-tasks 文档 "Compare scheduling options" 表——Cloud（Routines，1 小时最小间隔、无需开机）/ Desktop（本机 cron）/ `/loop`（会话内，1 分钟最小间隔，恢复受限）。
  - 动态间隔的机制（Q2）：
    > "When you omit the interval, Claude chooses one dynamically instead of running on a fixed cron schedule. After each iteration it picks a delay between one minute and one hour based on what it observed: short waits while a build is finishing or a PR is active, longer waits when nothing is pending."
- **机制描述（Q2 视角）**：Claude Code 把"下一轮怎么开"做成**三个并列原语**——条件驱动（`/goal`，独立小模型每轮评估）、时间驱动（`/loop`/cron，间隔可固定、可模型自选、可 loop.md 定制）、脚本/自定义驱动（Stop hook，确定性检查或模型评估）；auto mode 只在轮内做审批不触发新轮。人工只在熔断/错误/ask 规则处介入。

### 3. OpenAI auto-review / Codex 自动批准（官方一手）

- **一手源记录**：同上文问题 1 第 4d 条（alignment.openai.com/auto-review/，2026-04-30，全文取得）。
- **逐字引句（Q2）**
  - **调度者＝独立的审批 agent**（Q2——干活的与守门的角色分离）：
    > "The separation of roles matters. The main agent is optimized to complete the user's task. This creates pressure to treat an approval boundary as just another obstacle to overcome. Auto-review has a narrower job: decide whether a proposed boundary-crossing action should run. Keeping that decision in a separate model call makes the approval policy easier to evaluate, monitor, and improve."
  - 触发点＝沙箱边界穿越（Q2）：
    > "Upon reaching a sandbox boundary, Codex can request escalation to execute an action outside of the sandbox. In Auto-review, a separate Codex agent grades these requests, considering the user's intent, the environment, the security policy, and the likely impact of the action."
  - 拒绝后的恢复路径（Q2）：
    > "Even when Auto-review rejects an action, Codex often recovers on its own by finding a safer way to make progress."
  - 内部采纳度（Q2）：
    > "Today, a majority of Codex Desktop token usage within OpenAI comes from Auto-review mode, and that share is growing."
  - 开源与文档指针（Q2）：文末注记原文——> "Auto-review is open source in the Codex repository, and you can learn how to use it in the Codex Auto-review docs."（指 developers.openai.com/codex/concepts/sandboxing/auto-review，该 docs 页本环境 403，见负结论清单）
- **机制描述（Q2 视角）**：外层调度中出现了一个新角色——**边界审批的独立 agent**：主 agent 只管完成任务，另一个模型调用专职判定"这个越界动作能不能跑"；审批通过率约 99%（ escalated actions），人工同步审批被替换成"异步监护 + 反复拒绝熔断"。

### 4. Huntley 的外层调度（同 Ralph 材料，Q2 视角）

- **一手源记录**：同问题 1 第 1 条（ghuntley.com/ralph/，2025-07-14）。
- **逐字引句（Q2）**
  - **每轮确定性重装"栈"**（Q2——调度状态每轮从文件重载）：
    > "the other key thing is **deterministically** **allocate the stack the same way every loop**."
    > "The items that you want to allocate to the stack every loop are your plan ('@fix_plan.md') and your specifications."
  - **下一件工作由谁选：模型在清单上选最重要的一件**（Q2）：
    > "you also need to trust Ralph to decide what's the most important thing to implement. This is full hands-off vibe coding that will test the bounds of what you consider 'responsible engineering'."
    > "LLMs are surprisingly good at reasoning about what is important to implement and what the next steps are."
    （CURSED 的 prompt 原文：> "Follow the @fix_plan.md and **choose the most important thing**." / "Follow the fix_plan.md and choose the most important 10 things."）
  - **主上下文窗口＝调度器，子 agent＝干活的**（Q2）：
    > "Ralph requires a mindset of not allocating to the primary context window. Instead, what you should do is spawn subagents. Your primary context window should operate as a scheduler, scheduling other subagents to perform expensive allocation-type work, such as summarising whether your test suite worked."
  - 并发度的调度约束（Q2）：
    > "You may use up to parrallel subagents for all operations but only 1 subagent for build/tests of rust."（原文拼写如此）
    > "If you were to fan out to a couple of hundred subagents and then tell those subagents to run the build and test of an application, what you'll get is bad form back pressure."
  - **两种模式化的 Ralph：planning Ralph 与 building Ralph**（Q2）：
    > "Then when you've got your todo list you kick Ralph back off again with... instructions to switch from planning mode to building mode..."
    （文中附两段完整 prompt："current prompt used to plan cursed" 与 "current prompt used to build cursed"）
  - 规格从哪来（Q2）：specs/ 是**环境夹具**而非审批物——> "Specs are formed through a conversation with the agent at the beginning phase of a project... Once your agent has a decent understanding of the task to be done, it's at that point that you issue a prompt to write the specifications out, one per file, in the specifications folder."（引至 ghuntley.com/specs/ 一节）
- **机制描述（Q2 视角）**：外层调度＝bash `while` 循环本身（每轮冷启动、确定性重装 fix_plan.md + specs）＋主上下文当调度器派发子 agent（搜索/写文件可高并发，build/test 限 1 个防 back pressure 失效）＋fix_plan.md 即进度清单（planning Ralph 生成、building Ralph 消费）。

### 5. 其他官方一手（Q2）

- **Anthropic《Scaling Managed Agents: Decoupling the brain from the hands》**
  - URL：https://www.anthropic.com/engineering/managed-agents ；作者：Lance Martin, Gabe Cemaj, Michael Cohen；发布日期：Apr 08, 2026；访问日期：2026-09-26（全文取得）。
  - **为什么算高影响力**：Anthropic 官方工程博客；《Building effective agents》页面顶部注记把它指为 "our current approach"，是 harness 架构的当前官方立场。
  - 逐字引句（Q2）：
    > "We virtualized the components of an agent: a session (the append-only log of everything that happened), a harness (the loop that calls Claude and routes Claude's tool calls to the relevant infrastructure), and a sandbox (an execution environment where Claude can run code and edit files)."
    > "When one fails, a new one can be rebooted with `wake(sessionId)`, use `getSession(id)` to get back the event log, and resume from the last event. During the agent loop, the harness writes to the session with `emitEvent(id, event)` in order to keep a durable record of events."
    > "The session provides this same benefit, serving as a context object that lives outside Claude's context window."
  - 机制（Q2）：把"外层"本身接口化——会话日志独立于 harness 存活，harness 崩了从最后一个事件恢复；"下一轮"的调度状态全部落在 session log 这个外部对象上。（另：此文含 "assumptions rot" 句——> "a harness encodes assumptions about what the model can't do … those assumptions rot as the model improves"——上下文参考，不属两问核心。）
- **LangChain 四环的调度环（Q2）**
  - 同 4e 一手源记录。逐字引句：
    > "The event-driven loop connects your agent to your ecosystem. An event fires — a new document lands, a schedule triggers, a webhook arrives — and the agent runs. The agent isn't something you invoke manually; it's a component running continuously inside a larger system."
    > "The hill climbing loop runs an analysis agent over those traces and uses the findings to rewrite the harness with improved configuration. That can include prompt/tool tweaks or grader tweaks."
    > "The key move here is that the return arrow doesn't just loop back to the top — it reaches inside and updates the agent loop directly. Each cycle of the outer loop makes the inner loops more effective."
  - 机制（Q2）：外层调度被分成两环——**事件环**（事件/定时/webhook 触发下一轮）与**爬山环**（用 trace 分析 agent 改写 harness 自身）；四环表格原文见 4e。

---

## 综合

### 问题 1：停止条件——成型做法已收敛，且 ≥2 独立一手来源同向

**收敛的四个构件（每条都有 ≥2 个独立一手来源）**：

1. **机器可核的验收判据作为逐轮闸门**（测试/类型/linter/评分器）——
   Huntley（"Anything can be wired in as back pressure to reject invalid code generation"，类型系统/静态分析/安全扫描）、Anthropic 2024（"ground truth from the environment... Code solutions are verifiable through automated tests"）、Anthropic 2025（feature_list 逐条 passes + 端到端自验证）、LangChain（grader 分 deterministic/agentic 两类）。四家同向。
2. **硬性资源上限作为兜底停止**（最大迭代/轮数/时间/拒绝计数）——
   Anthropic 2024（"stopping conditions (such as a maximum number of iterations)"）、Claude Code `/goal`（`or stop after 20 turns` 子句 + 无进展熔断）、auto mode（3 连拒/20 总拒停机，headless 终止进程）、`/loop`（7 天硬过期）、OpenAI auto-review（"automatically stop the trajectory after repeated denials"）。五处一手同向。
3. **"提前宣告完成"被官方点名为头号失败模式**（停止条件设计的目标敌人）——
   Anthropic 2025 两个表格条目（"declares victory on the entire project too early"、"marks features as done prematurely"）＋ LangChain（verification loop 的存在理由）。Huntley 的对应物是占位实现（"inherent bias to do minimal and placeholder implementations"）与" eventual consistency"信仰。
4. **验收角色与干活角色分离**——
   Anthropic 2024（evaluator-optimizer 工作流）、Anthropic 2025（只许改 passes 字段 + "Only mark features as 'passing' after careful testing"）、Claude Code `/goal`（"completion is decided by a fresh model rather than the one doing the work"）、OpenAI auto-review（"The separation of roles matters"）、LangChain（grader 与 agent 分置）。五处一手同向，且跨 Anthropic/OpenAI/LangChain 三家。

**未收敛的一点——谁是裁判**：完成判定权在各家不同：操作者人判（Huntley：TODO 耗尽是 "a matter of taste"）／文件清单逐条判定（Anthropic 2025）／独立小模型每轮判定（Claude Code `/goal` 三值判定）／干活模型自判（Anthropic 2024 的默认 "terminates upon completion"）／被审批方提出、审批方判定（OpenAI auto-review）。即：**"可核判据 + 熔断上限 + 验收分离"的骨架已收敛（≥2 独立一手）**，裁判权的归属仍是各家分歧点。

**保护条款**（单源但机制成型）：Anthropic 2025 的 "It is unacceptable to remove or edit tests" + JSON 选型理由（"less likely to inappropriately change or overwrite JSON files compared to Markdown files"）目前只此一家逐字成文——但与 Claude Code auto mode "strip out Claude's own messages... reasoning-blind by design"（防评估器被操纵）同属"保护裁判不被当事人改写"这一族，方向同向、条目不同源。

### 问题 2：外层调度——两种主导形态已收敛；"人工队列"形态在一线厂商手中已退位

**收敛的构件（四个，下游判读归并为"两种主导形态＋旁论"，每条 ≥2 独立一手来源）**：

1. **进度状态外置成持久化文件/日志，每轮冷启动重读**——
   Huntley（每轮 "deterministically allocate the stack"：fix_plan.md + specs/）、Anthropic 2025（feature_list.json + claude-progress.txt + git log 的三件套与固定开场序列）、Anthropic Managed Agents（session log 独立于 harness，`wake(sessionId)` 从最后事件恢复）、Claude Code `/loop`（loop.md）。四家同向（Anthropic 占三家，Huntley 独立）。
2. **"下一件工作"＝清单上最高优先级的未完成项，由模型自选**——
   Anthropic 2025（"choose the highest-priority feature that's not yet done to work on"）与 Huntley（"trust Ralph to decide what's the most important thing to implement"、"Follow the @fix_plan.md and choose the most important thing"）。两家独立、句式几乎同构。Claude Code `/loop` 内置维护 prompt 是同族的清单化变体（固定三步优先级：未完工作 → PR 偶发维护 → 清理）。
3. **定时/事件触发是另一类一等调度原语**——
   Claude Code（`/loop` 固定/动态间隔、cron、云 Routines/桌面任务三档）、LangChain（event-driven loop：cron/webhook/channel）、Huntley 反例（bash while 是纯"上一轮结束即下一轮"，无定时器）。两家一手同向。
4. **边界审批型调度（审批作为循环里的独立角色）**——
   Claude Code auto mode（分类器轮内审批 + deny-and-continue）、OpenAI auto-review（独立审批 agent，审批通过率约 99%）。两家一手同向（厂商各一）。

**人工队列的位置**：Anthropic 2024 还把 "pause for human feedback at checkpoints" 写进定义；到 Anthropic 2025 的长程 harness，人工门禁已完全退出调度回路（只有 git 提交与进度文件）；Claude Code `/goal` 文档把人工留在三处——熔断、ask 规则、`/goal clear`；OpenAI auto-review 的标题即立场（"without synchronous human oversight"）。**即"人工同步审批作为外层调度"在两家一线厂商的 2025-2026 一手材料中都被机械门禁＋熔断升级取代**——这本身是收敛结论（≥2 独立一手）。

### 成型做法清单（按来源数）

| 做法 | 一手来源数 | 来源 |
|---|---|---|
| 测试/类型/linter/评分器做逐轮闸门（back pressure / grader） | 4（≥2 独立） | Huntley、Anthropic 2024、Anthropic 2025、LangChain |
| 最大迭代/轮数/时间/拒绝计数等硬上限熔断 | 5（≥2 独立） | Anthropic 2024、CC `/goal`、CC auto mode、CC `/loop`、OpenAI auto-review |
| 验收与干活角色分离 | 5（≥2 独立，跨 3 家） | Anthropic 2024/2025、CC `/goal`、OpenAI auto-review、LangChain |
| "提前宣告完成"点名为头号失败模式 | 3（≥2 独立） | Anthropic 2025、LangChain、（Huntley 对应物：占位实现） |
| 进度外置成文件/日志、每轮冷启动重读 | 4（Anthropic×3 + Huntley 独立） | Huntley、Anthropic 2025、Managed Agents、CC `/loop`(loop.md) |
| 下一件工作＝清单最高优先级未完成项、模型自选 | 2（独立） | Huntley、Anthropic 2025 |
| 定时/事件触发型调度原语 | 2（独立厂商） | Claude Code、LangChain |
| 人工同步审批退出调度回路 | 2（独立厂商） | Anthropic（2024→2025 演化）、OpenAI |
| 完成判定权归谁（人判/清单/独立模型/自判） | **未收敛** | 各家分歧（见上） |
| 测试不可改写条款＋JSON 选型理由 | 1（单源） | Anthropic 2025 |
| 评估器输入防操纵设计（reasoning-blind） | 2（Anthropic×2：auto mode 文档＋博客） | CC auto mode |
| Codex 四拍循环与 assistant-message 终止态 | **0（正文未取得）** | 仅负结论＋官方仓库用户报告佐证（不入册） |

---

## 负结论清单

1. **OpenAI《Unwinding Codex's Agent Loop》（Michael Bolin，2026-01-23，openai.com/index/unwinding-codex-agent-loop/）——已确认存在、正文未取得。**
   试过的路径：① web_fetch 原 URL → 403；② 搜索发现同文 slug `unrolling-the-codex-agent-loop`（openai.com/index/ 与 openai.com/ro-RO/ 两个入口）→ 均 403；③ **对照实验**：已知存在的 openai.com/index/harness-engineering/ 同样 403 ⇒ openai.com 对本环境是**站点级**封锁，非单篇问题；④ bash curl 带浏览器 UA → HTTP 403（10KB 拦截页）；⑤ web.archive.org → 本环境网络不可达（fetch failed，多 URL 重试同）；⑥ Ars Technica 的报道 → HTTP 405 人机验证；⑦ 搜作者个人站镜像（bolinfest / "Michael Bolin codex agent loop"）→ 未找到；⑧ openai/codex 仓库 `docs/` 目录（GitHub API 列目录）→ 全是 126–150 字节的跳转占位文件，无 agent loop 文档等价物。
   存在的可见证据：官方 ro-RO locale URL 出现在搜索结果（标题 "Desfășurarea buclei agentului Codex"）；Ars Technica 2026-01 报道标题 "OpenAI spills technical details about how its AI coding agent works"；Michael Bolin（bolinfest）在 openai/codex 仓库有大量合并 PR（作者身份可交叉印证）。
   **"四拍循环""每轮以一条 assistant message 收尾进入终止态"等表述未能逐字核实，上屏引用前必须回源。**
2. **Claude Code 官方 CHANGELOG（github.com/anthropics/claude-code CHANGELOG.md）——未取得。**
   web_fetch raw.githubusercontent.com 超时（30s）；bash curl 两次失败（exit 28/56，本环境到 raw.githubusercontent.com 网络不可达）。auto mode/`/goal`/`/loop` 的引入日期未从 changelog 拿到；已用官方文档的版本锚点替代（auto mode 内置默认：v2.1.228+（Pro/Max/Team）、v2.1.283+（所有 plan）；`/goal` 恢复逻辑锚点最高 v2.1.269）。
3. **Claude Code auto mode 公告博客正文——标题已确认、正文未取得。**
   https://claude.com/blog/auto-mode-default-in-claude-code（标题经搜索结果逐字确认："Auto mode is now the default in Claude Code for Pro, Max, and Team plans"）与 https://claude.com/blog/auto-mode（页面标题 "Auto mode for Claude Code"）：两个 URL 均可访问（HTTP 200），但页面导航过重，正文被截断未取得，页面发布日期未见到；`claude.com/blog/auto-mode.md` → 404。二手日期线索（Simon Willison 2026-08-08、gigazine 2026-08-10）未回源核实，不作证据。auto mode 默认化的逐字证据已由官方文档 permission-modes.md 覆盖（见 4b）。
4. **OpenAI Codex auto-review 官方文档（developers.openai.com/codex/concepts/sandboxing/auto-review）——403，正文未取得。**
   URL 的存在由 OpenAI 官方博客正文链接确认（alignment.openai.com/auto-review/ 文中两处引用）。auto-review 的机制证据以官方博客原文为准（已全文取得）。

## 不入册·仅社区情绪（按新增标准，均不作为证据）

- **openai/codex issue #32389**（https://github.com/openai/codex/issues/32389，2026-07-11，open状态，官方维护者已打 `bug`+`model-behavior` 标签）：**用户 bug 报告**（作者 mistrjirka，非 OpenAI 立场文件），不入册。但它从 wire 层逐字记录了 Codex agent loop 的终止语义，对《Unwinding》一文是独立旁证：> "Because the response is classified as a normal `stop`, the client correctly considers the agent turn complete even though the task is still in progress." / > "The agent loop ends because the response is a successful completion."（引用需标注"官方仓库用户报告"）
- **Ars Technica**：openai.com 报道（2026-01，405 未取得正文）——媒体转述，仅作《Unwinding》存在性线索。
- **Turing Post 采访**（"The New Inner Loop of Software Engineering with Michael Bolin"）——媒体转述，未取正文，不入册。
- **swyx《loopcraft: the art of stacking loops》**（latent.space）——被 LangChain 官方博客引用并致谢（"This is what loop engineering — or loopcraft, as swyx puts it — actually looks like in practice."）；个人 newsletter，按新标准不入册，可作后续回源线索。
- **Addy Osmani《Practical loop engineering》**（addyosmani.com/blog/practical-loop-engineering，种子标注 2026-08-14，未回源核实）——个人博客，不入册。其对 `/goal`、`/loop` 的转述已被本报告的 Claude Code 官方文档直接取代（官方一手 > 个人转述）。
  > ⚠️ **调和注记（2026-09-26 评审轮）**：本行是 **B 路视角**（其任务不含 Osmani）。Osmani 两篇（命名篇 2026-06-07 + 操作篇 2026-08-14）**已由 A 路全文取得并核实**（见 [evidence-a](evidence-2026-09-26-a-originators.md)），台账 §A 已入册——**以 evidence-a 与台账为准**；本行"取代"判断（`/goal`//`/loop` 部分以官方文档为一手）仍然成立。
- **社区镜像仓库**（SiluPanda/codex-agent-loop、Fnine59/codex-loop 的 README）——非官方复制品，不入册。
- **Simon Willison / gigazine / 36kr**——对 auto mode 与《Unwinding》的二手报道，仅作日期与存在性线索，全部未回源核实，不作证据。
- 本仓库 `talk-harness-201/02_evidence/01-kol-alignment-2026.md` 与 deepseek-harness `research.md`——种子底稿（二手），本报告所有 URL 均已按其线索回源到一手原文，未直接引用其文字作证据。
