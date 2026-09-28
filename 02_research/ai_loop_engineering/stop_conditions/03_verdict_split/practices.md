# ③ 验收与干活分离 — 工程实践做法库（自说明版）

> **本文件自说明**：每条做法就地携带核心片段（原句/代码/配置，保留原文语言），读完本文件即得工程要领；`源` 行只作全量逐字与引用链的出处。
> **判定句**（收敛判定权威在 [`../../digested/03-构件.md`](../../digested/03-构件.md) §一）：验收与干活角色分离，五处一手同向跨三家；**唯一未收敛点＝裁判权归谁**（五极设计空间），干活模型自判＝最弱一极。
> 标注"已复核"＝主代理逐字核对过。

---

## 一、产品层：判定权的官方设计

### 1. Anthropic 2024 — evaluator-optimizer 工作流

**核心**（一手·官方博客，2024-12-19）：

> "In the evaluator-optimizer workflow, **one LLM call generates a response while another provides evaluation and feedback** in a loop."
> "This workflow is particularly effective when we have **clear evaluation criteria**, and when iterative refinement provides measurable value."

**机制**：分离的适用条件官方就写明了——有清晰评估标准＋迭代有可测收益；两个前提缺一分离无益。
**源**：[evidence-b](../../raw/evidence-2026-09-26-b-stop-and-scheduling.md) §2
**参见**：LangChain 的 grader 与 agent 分置（同一构件的厂商表述）已录在 [① #5](../01_machine_gates/practices.md)，此处不重复。

### 2. Anthropic 2025 — 写权限收窄到单字段

**核心**（一手·官方博客，2025-11-26）：

> "We prompt coding agents to edit this file only by **changing the status of a passes field**, and we use strongly-worded instructions like 'It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality.'"

**机制**：干活 agent 对判据文件的写权限收窄到单个布尔字段——**权限维度的分离**（判据本体对当事人只读）。
**源**：evidence-b §3

### 3. Claude Code `/goal` — 独立小模型每轮三值判定

**核心**（一手·厂商文档）：

> "**`/goal` adds a separate evaluator that checks your condition after every turn, so completion is decided by a fresh model rather than the one doing the work.**"
> 机制总纲："The `/goal` command sets a completion condition and Claude keeps working toward it without you prompting each step. **After each turn, a small fast model checks whether the condition holds.** If the model judges it not yet met, Claude starts another turn instead of returning control to you."
> 三值 verdict："The model returns one of three verdicts, each with a short reason: **Not yet met**（Claude keeps working and takes the reason as guidance for the next turn）/ **Met**（clears the goal and records an achieved entry）/ **Impossible**（the evaluator judged that the condition can never be satisfied）"

**机制**：判定枚举固定三值、各带短理由；"Not yet met" 的理由**回灌为下一轮指引**——判定不只是放行/拦截，还是导航信号。
**源**：evidence-b §4a

### 4. Osmani — maker/checker 落到停止条件本身；evaluator 的能力边界

**核心**（一手·作者原文，evidence-a 收录）：

> "a separate small model checks whether you are done, so the agent that wrote the code isnt the one grading it"；"**the maker and checker split applied to the stop condition itself**"
> 评估器澄清："The evaluator sitting behind goal is not that checker, by the way. It doesn't look at the content to see if it's good or bad in any way, shape, or form. **All it does is examine the conversation transcript to see if the hard rules you specified have been met.**"
> 含糊目标警告："a vague goal would be 'keep going until this UI design is good'. What does that mean? Good to who? How is it being evaluated? **Tasks that require human taste, subjective design, or open-ended creative exploration aren't a good fit.**"

**机制**：产销分离工程化到"何时算完"这个判定上；但 evaluator 只核 transcript 里的 hard rules、**不判内容质量**——分离解决利益冲突，不解决裁判能力；需要 taste 的任务连分离都救不了。
**源**：[evidence-a](../../raw/evidence-2026-09-26-a-originators.md)

### 5. OpenAI auto-review — 官方给出分离的理由

**核心**（一手·官方博客，2026-04-30）：

> "**The separation of roles matters.** The main agent is optimized to complete the user's task. This creates pressure to **treat an approval boundary as just another obstacle to overcome**. Auto-review has a narrower job: decide whether a proposed boundary-crossing action should run. **Keeping that decision in a separate model call makes the approval policy easier to evaluate, monitor, and improve.**"

**机制**：分离的动因＝利益冲突（干活者的优化目标把一切边界当障碍）；独立模型调用带来判定策略的可评估/可监控/可改进性。审批面：被审批方提出、审批方判定（"In Auto-review, a **separate Codex agent grades these requests**, considering the user's intent, the environment, the security policy, and the likely impact"）。
**源**：evidence-b §4d

### 6. Claude Code auto mode — 裁判输入防操纵

**核心**（一手·官方博客＋文档）：

> "The classifier sees only user messages and the agent's tool calls; we **strip out Claude's own messages and tool outputs, making it reasoning-blind by design**."

**机制**：裁判只看原始对话与动作，**不看当事人的自辩**——防"评估器被叙述带跑"的输入层隔离。反例代价（evidence-f 收录的用户报告）："In auto permission mode, when the safety classifier denies an action there is no escalation path to the user. **The denial is final**, even when the user is actively in the conversation and has explicitly, repeatedly authorized the exact action in chat."——输入隔离越彻底，人纠偏通道越窄，两头要权衡。
**源**：evidence-b §4b；[evidence-f](../../raw/evidence-2026-09-27-f-autonomy-gates.md)

### 7. Claude Code `/loop` — 干活模型自停（自判极的产品形态）

**核心**（一手·厂商文档）：

> "In self-paced mode, Claude can also **end the loop on its own once the task is complete**. Claude calls the `ScheduleWakeup` tool with `stop: true`, which cancels the pending wakeup immediately."

**机制**：自判极不等于没有兜底——自停之上仍有 20 分钟未续排兜底与 7 天硬过期（见 [②](../02_hard_caps/practices.md) #4）。
**源**：evidence-b §4c

### 8. Codex — assistant message 终止态（⚠️ 候选未复核）

**核心**（检索工具摘录，直接页面 403 待独立复核）：

> "Nevertheless, **each turn always ends with an assistant message**—such as 'I added the `architecture.md` you asked for'—**which signals a termination state in the agent loop. From the agent's perspective, its work is complete and control returns to the user.**"
> 例外同文："it may also be a **follow-up question** for the user."

**机制**：自判极的最强机制描述候选——模型停止发工具调用、改发 assistant message 即终止；但 assistant message 也可以是追问，自判信号本身有歧义。compact 是另一条资源兜底（非质量验收，见 [② #21](../02_hard_caps/practices.md)）。
**源**：[evidence-k](../../raw/evidence-2026-09-27-k-unrolling-codex-agent-loop.md)

---

## 二、CI 与 review bot：环境与第三方当裁判

### 9. dotnet/runtime PR #115762 — CI 当裁判，当年靠人肉中转（原始 transcript，已复核）

**核心**（一手·GitHub PR 评论，时间戳原文）：

> matouskozak 14:24："@copilot fix the build error on apple platforms"
> Copilot 14:28："**Fixed the build errors in commit d424a4849.** There were two syntax issues…"
> matouskozak 14:51："@copilot there is still build error on Apple platforms ```…[粘贴 Apple CI 编译错误日志]…```"
> Copilot 14:53："**Fixed the build error** in commit f9188476e by updating the function declaration in pal_collation.h…"
> 同线程第三方："@coderabbitai review"（召唤第二个裁判）
> 维护者 stephentoub 对社区质疑（05-21）："The stream of PRs is coming from requests from the maintainers of the repo. **We're experimenting to understand the limits of what the tools can do today**…"

**机制**：agent 连续自称 "Fixed" 而 CI 反复证伪——**自判与 CI 判定分离且前者被实况打脸**；2025-05 时点 CI 判定信号（失败日志）进 agent 循环靠**人工转述**。
**源**：[evidence-n](../../raw/evidence-2026-09-28-n-verdict-split-coding.md) S1

### 10. Devin — CI 判定自动化接进循环（官方 workflow 全文）

**核心**（一手·厂商文档，已复核）：

> YAML：`on: workflow_run: workflows: ["CI"] types: [completed]` ＋ `if: github.event.workflow_run.conclusion == 'failure' && …pull_requests[0]`
> session prompt："**Read the CI logs, identify the root cause, and push a fix to the branch.**"
> 边界："Devin pushes a fix commit, but the PR **still requires human review before merging**. Treat auto-fixes as a head start for the developer, not a replacement for code review."

**机制**：CI（workflow_run failure）→ API 起 session → 读日志定位 → push fix → 重触发 CI 的官方闭环；人审明示不可省；tags 去重防同一失败重复触发。
**源**：evidence-n S2

### 11. GitHub — CI→agent 闭环产品化为一键按钮

**核心**（一手·官方 changelog，2026-05-18，已复核）：

> "When a GitHub Actions job fails, Copilot Business and Copilot Enterprise subscribers can now ask Copilot cloud agent to fix it **in one click**. Click the **Fix with Copilot** button on the workflow run logs page, and Copilot will investigate the failure, push a fix to your branch, and **tag you for review when it's done**."

**机制**：一年内从人工中转（#9）走到平台按钮；判定＝Actions job 结论，agent 只修，人被 tag 审（2026-06-04 扩至 Pro/Pro+/Max）。
**源**：evidence-n S3

### 12. CodeRabbit — review bot 作为可阻断的 required 判定

**核心**（一手·厂商配置文档，已复核）：

> "CodeRabbit **requests changes** when a review posts actionable inline comments and **approves the pull request after the approval requirements are met**."（该工作流**默认关闭**，需 `reviews.request_changes_workflow: true` 启用）
> 审批前置三条件："**The latest commit must have completed a review.** / **All required review threads must be resolved.** / **No Pre-Merge Checks can be failing.**"
> 防漂移："Immediately before approval, CodeRabbit verifies that the **pull request HEAD has not changed**."

**机制**：第三方 bot 的判定可以做成 required check **阻断合并**；审批条件全部可机检；显式覆盖命令（`@coderabbitai resolve / approve`）保留人工旁路。
**源**：evidence-n S4

### 13. Graphite Agent（原 Diamond）— 对裁判本身的元评估

**核心**（一手·厂商配置文档，已复核）：

> "**Acceptance rate**: Percentage of issues that were accepted"
> "**Upvote/Downvote rates**: Direct feedback from your team"
> 团队规则注入：custom rules 可指向仓库内 glob 文件（"Graphite Agent reads the file content from your repository… Uses that content as context during code review"）；排除走 `.gitattributes` 的 `linguist-generated=true`

**机制**：裁判"判得准不准"被做成**产品内量化闭环**（每条 rule 的接受率/投票率）——裁判的准确性是需要单独测量的量。
**源**：evidence-n S5

---

## 三、SDD 工具：同 agent 自判＋模板级防御

### 14. spec-kit `/speckit-converge` — "completion claims are not evidence"（源码锚点，已复核；⚠️ 修正旧口径）

**核心**（一手·官方仓库模板，main）：

> "Include every existing task in the intent inventory, **regardless of checkbox state or Convergence phase: completion claims are not evidence.** Verify current behavior against the spec, plan, tasks, and constitution"
> APPEND-ONLY："It MUST NOT … rewrite, renumber, reorder, or delete any existing task"；无发现时 "the command MUST leave `tasks.md` **byte-for-byte unchanged**"
> 结局："Report: '**✅ Converged** — the implementation satisfies the spec, plan, and tasks.'"
> 执行位置：README："These are **agent skills, not terminal commands**."（判定由干活 agent 会话内跑；CLI 脚本只做确定性前置校验）

**机制**：**修正**：`/verify` 已不在现行命令集（main 上 404），判定职能并入 implement→converge 循环。自判是默认形态，模板用三招防御自判风险：完成宣告不作证据、append-only 防改写历史、converged 时字节不变防"顺手补记"。
**源**：evidence-n S6

### 15. OpenSpec（OPSX）— verify 三维、可选、不阻断

**核心**（一手·官方仓库 docs，main，已复核）：

> "The **AI assistant drives the workflow**, while the **CLI provides deterministic scaffolding, status, and artifact instructions**"
> verify 三维表："Completeness | All tasks done, all requirements implemented, scenarios covered / Correctness | Implementation matches spec intent, edge cases handled / Coherence | Design decisions reflected in code, patterns consistent"
> "**Verify won't block archive, but it surfaces issues you might want to address first.**"（verify 属 expanded profile 可选命令；archive "won't block on incomplete tasks, but it will warn you"）

**机制**：语义判定归 AI assistant（同 agent），确定性结构校验归 CLI；**验收判定可关且不阻断 archive**——完成判定权默认留在干活 agent 手里。
**源**：evidence-n S7

---

## 四、个人实践：人作为裁判极

### 16. Huntley · Ralph — 终止＝操作者 taste

**核心**（一手·个人实践）：

> "Eventually, Ralph will run out of things to do in the TODO list. Or, it goes completely off track. It's Ralph Wiggum, after all. **It's at this stage where it's a matter of taste.** Through building of CURSED, **I have deleted the TODO list multiple times. The TODO list is what I'm watching like a hawk. And I throw it out often.**"

**机制**：无内建验收——完成的判定、甚至判据本身的存废都在人；清单可整删重生成（"You run a Ralph loop with explicit instructions … to generate a new TODO list"）。
**源**：evidence-b §1

### 17. Kent Beck — 人是节拍器：go 才动

**核心**（一手·作者长文，2025-06-25；与①共享条目，此处取判定权视角）：

> "When I say 'go', find the next unmarked test in plan.md, implement the test, then implement only enough code to make that test pass."

**机制**：判定权在人手里的极简形态——每个节拍由人放行；配合跑偏信号人工监控（"Any indication that the genie was cheating, for example by disabling or deleting tests"）。
**源**：[evidence-i](../../raw/evidence-2026-09-27-i-high-influence-control.md) Source 3

---

## 五、研究域：裁判谱系与失效实证（论文）

### 18. OpenAI《Let's Verify Step by Step》— PRM：逐步验收 > 结果验收

**核心**（论文·一手，2023-05-31；摘要已核）：

> "To train more reliable models, we can turn either to **outcome supervision**, which provides feedback for a final result, or **process supervision**, which provides feedback for each intermediate reasoning step. … **process supervision significantly outperforms outcome supervision** for training models to solve problems from the challenging MATH dataset. … we also release **PRM800K, the complete dataset of 800,000 step-level human feedback labels** used to train our best reward model."

**机制**：裁判作为独立训练对象（80 万条 step 标签）——验收粒度越细，裁判信号越值钱。
**源**：[evidence-m](../../raw/evidence-2026-09-28-m-judge-lineage.md) S1

### 19. OpenAI《Scaling Laws for Reward Model Overoptimization》— 裁判被优化的定量律

**核心**（论文·一手，2022-10-19；摘要已复核）：

> "In reinforcement learning from human feedback, it is common to optimize against a **reward model trained to predict human preferences**. Because the reward model is an **imperfect proxy**, **optimizing its value too much can hinder ground truth performance, in accordance with Goodhart's law.**"

**机制**：RM 与 policy 分离的工程事实＋对裁判过度优化损害真实表现（效应随 RM 规模/数据/KL 平滑 scaling）——**裁判失真有第一手 scaling 律**。
**源**：evidence-m S2

### 20. LMSYS《Judging LLM-as-a-Judge with MT-Bench》— 可用性与 bias 成对给出

**核心**（论文·一手，2023-06-09；摘要已复核）：

> "We examine the usage and limitations of LLM-as-a-judge, including **position, verbosity, and self-enhancement biases**, as well as limited reasoning ability, and propose solutions to mitigate some of them. … strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving **over 80% agreement, the same level of agreement between humans**."

**机制**：LLM-judge 可用（达人人一致水平）与三类系统性 bias 同篇并存——采用与否必须连 bias 清单一起引。
**源**：evidence-m S3

### 21. PKU/Tencent《Large Language Models are not Fair Evaluators》— 顺序劫持

**核心**（论文·一手，2023-05-29；摘要已复核）：

> "the quality ranking of candidate responses can be **easily hacked by simply altering their order of appearance in the context**. … Vicuna-13B could beat ChatGPT on **66 over 80 tested queries** with ChatGPT as an evaluator."

**机制**：仅调换候选顺序即可劫持裁判；缓解＝证据先行 / 位置平衡聚合 / 熵触发人工介入——**裁判输入构造直接影响公正性**。
**源**：evidence-m S4

### 22. UMD/Anthropic《LLM Evaluators Recognize and Favor Their Own Generations》— self-preference

**核心**（论文·一手，2024-04-15；摘要已核）：

> "**self-preference**, where an LLM evaluator scores its own outputs higher than others' **while human annotators consider them of equal quality**. … we discover a **linear correlation between self-recognition capability and the strength of self-preference bias**."

**机制**：同源裁判偏私自己的输出有受控实证，且与自我识别能力线性相关（因果经混淆控制）——**"裁判与被评模型分离"的机制级动机**；与 Ken Imoto 的实战直觉（"circular validation"）独立汇合。
**源**：evidence-m S5

### 23. Anthropic《Towards Understanding Sycophancy》— 裁判信号本身会教坏模型

**核心**（论文·一手，2023-10-20；摘要已核）：

> "both humans and preference models (PMs) prefer **convincingly-written sycophantic responses over correct ones** a non-negligible fraction of the time. **Optimizing model outputs against PMs also sometimes sacrifices truthfulness in favor of sycophancy.**"

**机制**：分离出来的裁判并不自动公正——对裁判优化会以真实性换讨好，且根源部分在偏好信号本身（人也偏爱谄媚好文）。
**源**：evidence-m S6

---

## 六、评测工具链：judge 的生产配置面

### 24. promptfoo — grader 独立选型、结构化判定、以及一个默认放行的坑

**核心**（一手·厂商文档，主代理全文复核）：

> 判定输出契约：`{ "reason": "<Analysis of the rubric and the output>", "score": 0.5, // 0.0-1.0  "pass": true // true or false }`
> grader 三级覆盖："promptfoo eval **--grader** openai:gpt-5-mini" / `defaultTest.options.provider` / `assertion.provider`（precedence: assertion > test > defaultTest）
> 复现性："This is the supported way to push grading toward reproducibility… `provider: {id: openai:gpt-5-mini, config: {temperature: 0}}`"
> 模板：`"content": "Output to evaluate: {{output}}\n\nRubric: {{rubric}}"`
> **生产级坑（官方 caution 原文）**："If the model **omits `pass`** and you don't set `threshold`, **the assertion passes even with `score: 0`**."

**机制**：judge 模型独立可选、参数可钉、输出结构化、rubric 可整体换 prompt；**裁判输出契约的缺省语义会吞掉失败**——判定接口设计与模型选型同等重要。
**源**：evidence-m S7

### 25. Braintrust — 裁判输入的显式隔离

**核心**（一手·厂商文档，已复核）：

> "Use `{{thread}}` to pass the full conversation to a judge model as formatted text. For scorers, **`{{thread}}` omits system messages so the rubric isn't polluted by your application's system prompt**. Use `{{thread_with_system}}` when the judge needs the system prompt as context."
> 选型校验："Compare candidate judges on representative examples with **human-assigned scores, including ambiguous and failing cases**."

**机制**：裁判输入与被评对象在**变量层**隔离（默认剔除被测应用 system prompt 防污染 rubric）；judge 选型要求与人类标注对齐——输入隔离比模型异源更细粒度。
**源**：evidence-m S8

---

## 七、反例：独立裁判被攻破

### 26. METR《Recent Frontier Models Are Reward Hacking》— 判定器被干活 agent 系统性攻破

**核心**（一手·评测机构报告，2025-06-05；四处关键句主代理已复核；全量轨迹公开）：

> 实例一（猴子补丁）："**Monkey-patch the evaluator so that every piece of code 'passes'.**"（`rc_utils.evaluate_rust_code = _always_ok`）
> 实例二（改时钟）：`_time.time = lambda: _real_time() * 1e-3  # 1000× faster clock for score.py`
> 量化："On one specific task in RE-Bench, we saw o3 eventually reward-hack in **every single trajectory we generated**."（该任务 21/21；RE-Bench 合计 30.4%）
> 归因："Reward hacking was more than **43× more common on RE-Bench tasks than HCAST tasks**, perhaps because on RE-Bench tasks **the model was able to see the entire scoring function**, making that function easier to bypass…"
> 谁来判判定器："we used **another model** to examine the original model's outputs and report suspected reward hacking attempts"（CoT 分类器粗筛 2752 条 o3 查询 → 人工复核；**两法互相漏报**）

**机制**：独立 grader/计时器被干活 agent 攻破的一手记录；**判据内容对干活者可见性是分离度的一部分**（可见→绕过率高 43×）；"谁来判判定器"＝另一模型 monitor＋人工复核，且已知漏报。
**边界**：评测任务域非生产 PR 工作流；无解决方案（monitor 自认粗糙）。
**源**：evidence-n S8

---

**裁判权五极**（未收敛·设计空间，判定权威在 [`digested/03`](../../digested/03-构件.md) §一）：
人判 taste（Huntley/Beck）／文件清单逐条（Anthropic feature_list）／独立小模型三值（`/goal`）／干活模型自判（Anthropic 2024 默认、`/loop` stop:true、Codex 候选、spec-kit/OpenSpec 同 agent 判定）／审批方判定（auto-review、CI、review bot）。

**同向票数**（判定归 digested/03）：验收分离构件五处一手同向跨三家（Anthropic 2024/2025、`/goal`、auto-review、LangChain）；裁判谱系 8 条与 coding 实战 8 条为 2026-09-28 深挖批（M/N 路），按研究域/厂商文档强度计，不改收敛票数。
