# 命名与事件时间线

> **append-only**：新事件往下加，不改旧行；旧行被推翻时**加一条勘误行**，不删原行。
> **强度口径**：【一手】＝本主题已归档原文 ｜【转引】＝来自外部/他处研究，**未独立回源** ｜【聚合】＝多源综合判断。
> **回源状态**：`✅` 已回源（一手原文已归档，证据在 [`raw/evidence-*.md`](.)）｜ `⏳` 待回源（**不可作主张依据，只可作检索方向**）。

**观测日期**：2026-09-26 起，**2026-09-27 I/J/K 追加**（不改旧行）。三路回源见 [evidence-a](evidence-2026-09-26-a-originators.md) / [evidence-b](evidence-2026-09-26-b-stop-and-scheduling.md) / [evidence-c](evidence-2026-09-26-c-autonomy-and-convergence.md)。高影响面控制实践见 [evidence-i](evidence-2026-09-27-i-high-influence-control.md)。I2 扩容档案含主验与侦察回源，侦察条目不计票；本地 goal 观察见 [evidence-j](evidence-2026-09-27-j-local-goal-session.md)；K 的 Codex 摘录直接页面仍 403，见 [evidence-k](evidence-2026-09-27-k-unrolling-codex-agent-loop.md)。

---

## 一、本词的正身：loop engineering（2026-06 起）

行序按日期排；**日不详的行排表尾并标注**。

| 日期 | 事件 | 操作定义要点 | 强度 | 回源 |
|---|---|---|---|---|
| **2026-06-02** | **Boris Cherny** 词源火花：WorkOS × Acquired Unplugged 访谈（视频存在、**无 transcript**；流传名句 "My job is to write the loops" **逐字未核验**，三个流传版本措辞不一致——A 路已列对照表） | **词源是碎片级的**：YC Lightcone 官方 transcript（2026-02-17）里 "loop" 一词**出现 0 次**——他当时用 swarm / "Mama Claude" / spec+Asana 的语言描述同一套机制；**无个人书面操作定义**（团队官方定义 ≠ 本人） | 【部分一手】 | ✅ [evidence-a](evidence-2026-09-26-a-originators.md) |
| **2026-06-07** | **Addy Osmani**《Loop Engineering》（命名篇，addyosmani.com/blog/loop-engineering/） | **本词的命名与首次定义**：loop ＝ agent 反复行动、自测、调整直到写清目标达成；分层**四级**（agentic loop → `/goal` → `/loop`/`schedule` → proactive 事件触发无人值守）；Ralph bash loop 是原语出现前的手写形态；澄清 `/goal` 评估器"只核 transcript 硬规则、不判内容好坏" | **【一手】** | ✅ [evidence-a](evidence-2026-09-26-a-originators.md) |
| **2026-06-08** | **Peter Steinberger** 词源推文（snowflake 解码精确到 2026-06-08 02:58 CST；X 全域不可达，**正文经 Osmani 06-07 帖逐字转引**："You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."） | **词源是碎片级的，无深度内容**（A 路明确结论）：两句话推文；博客自 2026-02-14 后无新帖、无 loop engineering 长文。**重要 nuance**：其 2025-12-28 长文《Shipping at Inference-Speed》明确**反对自动编排**（"usually I'm the bottleneck"）——与 6 月推文立场相反，一手证据 | 【部分一手】 | ✅ [evidence-a](evidence-2026-09-26-a-originators.md) |
| **2026-06-16** | **LangChain / Sydney Runkle**《The Art of Loop Engineering》 | **四环模型**：agent loop（核心："an agent is just a model calling tools in a loop until a task is complete"）→ verification loop（rubric + grader，grader 分 deterministic 与 agentic/LLM-as-judge）→ event-driven loop（cron/webhook/channel 触发）→ hill-climbing loop（用 trace 改写 harness 本身——"the return arrow doesn't just loop back to the top — it reaches inside and updates the agent loop directly"） | **【一手】** | ✅ [evidence-b §4e](evidence-2026-09-26-b-stop-and-scheduling.md) |
| **2026-06-30** | **Claude Code 团队**官方博客给出 loop engineering 定义（**团队官方 ≠ Cherny 本人**）；**Andrew Ng**《Loop Engineering: My 3 Key Loops for Building 0-to-1 Products》（*The Batch* → X）同日 | Ng：**三环嵌套**（agentic coding / developer feedback / external feedback），外环修正内环方向，人类价值＝**上下文优势**而非"品味"；CC 团队《Loop engineering: Getting started with loops》（Delba de Oliveira & Michael Segner）：loop ＝ "agents repeating cycles of work until a stop condition is met"，四类循环 turn-based / goal-based / time-based / proactive（evidence-a D3 逐字核验） | **【一手】** | ✅ [Ng 归档](../../../../01_sources/reference/kol/_raw_loop_engineering/andrew_ng/raw_ng_x_post_en.md) · [CC 团队见 evidence-a](evidence-2026-09-26-a-originators.md) |
| **2026-06**（日不详） | 中文圈《Loop Engineering 橙皮书》（花叔 / alchaincyf 编） | **C 路定性：英文谱系的中文转述/编译，非独立发明**——作者 README 明写初版 "based on Addy Osmani's founding post and the official Claude Code / Codex docs"，并把术语起源完整归于 2026-06 同一周的 Steinberger / Cherny / Osmani | 【一手（其 README 自述）】 | ✅ [evidence-c](evidence-2026-09-26-c-autonomy-and-convergence.md) |
| **2026-08-14** | **Addy Osmani**《Practical Loop Engineering》（操作篇） | 把 06-07 命名篇的操作层展开；`/goal`/`/loop` 转述已被 Claude Code 官方文档一手取代（B 路判定），但**四级分层**与两条警告句是其独有（含糊目标不配循环；别把品味和判断委托给 agent——两句均经 evidence-a 补充回源取得逐字） | **【一手】** | ✅ [evidence-a](evidence-2026-09-26-a-originators.md) |
| **2026-08 后**（具体日期⏳待锚定） | **中文视频生态传播锚**：B站/YouTube 频道「为什么叫QQ」《Loop Engineering实操指南 \| 90%工程师还在做AI时代的"人肉API"》（YT `hzLfDKUzl2M` / B站 `BV1zYEz6oEx7`） | **与花叔橙皮书同类的中文转述层，不入册**：定义谱系完整归于 06 词源周（其复述的 Steinberger 推文、Osmani"替代提示者"口径与一手档案一致，转述保真度尚可）；新增价值在三层实操叙述（Cursor Run Mode 分档 / `/goal` 可观察停止条件 / fan-out＋对抗验证＋大小模型分层）与传播失真点（"90% 开发者"无源统计、专名 ASR 讹变多处）。文字稿全文与讹变对照表见 [evidence-t](evidence-2026-09-30-t-shenmejiaoqq-video-zh.md)（侦察级：文字稿未对原声核验，机制细节待回官方一手） | 【转引（用户提供文字稿）】 | ✅ [evidence-t](evidence-2026-09-30-t-shenmejiaoqq-video-zh.md) |

| **2026-09-14** | **Tessl**（员工署名博客《Who owns your context?》）官方直接使用并定义 "loop engineering" | **候选五定义源，待主验**：若原文复核成立，它把 loop engineering 与 context engineering 分界为内环单次运行、中环跨运行行为改进、外环业务指标；外延比 Runkle/Osmani 更宽，但不计入已确认定义源 | **【候选一手文本】**（侦察回源·主验待补） | ⏳ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source E2 |
| **2026-09-27 勘误** | 上一行 Tessl 的定义冲突已登记为候选判读，**主验仍待补** | 暂按 `digested/01` §二处理：若原文复核成立，同指只覆盖内环；中环接近 Runkle，外环不等同 Ng 的 external feedback。侦察回源，未复验 | 【候选判读】 | ⏳ digested/01 |


> **本词的操作定义与"体感像 loop"的分界**（判据，展开见 [`../digested/01-命名谱系.md`](../digested/01-命名谱系.md)）：
> 公开材料比"入口是粗目标、后面反复调用工具"通常多出**①人能核的停止/继续条件；②在长程场景中外置的工作来源、记忆或调度**。后者是重要扩展，不是单个 bounded task loop 的必要条件；B 路、E 路只证明若干机制形态存在，不证明行业主导或效果。
>
> **命名事件的定性（A 路一手证据）**：**词源＝热度碎片，定义＝事后工程化**——两条 viral 碎片（Cherny 06-02 访谈句未逐字核验 + Steinberger 06-08 两句话推文无深度）触发，Osmani 06-07 命名并定义、Runkle 06-16 给四环栈、CC 团队 06-30 给官方定义。**四个已确认定义源的核心同指一件事（系统替人逐轮提示），但外延不兼容**；Tessl 2026-09-14 暂作候选，待主验。

---

## 二、相邻旧名（各自指不同层，**不是本词的同义词**）

| 日期 | 名字 | 提出者 | 指哪一层 | 强度 | 回源 |
|---|---|---|---|---|---|
| **2024-12-19** | agents 的机制句 | Anthropic《Building effective agents》（Erik S. & Barry Zhang） | **机制**："typically just LLMs using tools based on environmental feedback in a loop"；停止条件首次成文（任务完成终止 + "stopping conditions (such as a maximum number of iterations) to maintain control"）；evaluator-optimizer 工作流（生成/验收分离雏形） | **【一手】** | ✅ [evidence-b §2](evidence-2026-09-26-b-stop-and-scheduling.md) |
| 2025-02 | **vibe coding** | Karpathy（"I 'Accept All' always"）；Willison 随即收窄并警告语义扩散 | **接受姿态**：不看代码就接受——与"要求测试门"不是同一层 | 【转引】 | ⏳ |
| **2025-07-14** | **Ralph Wiggum loop** | Geoffrey Huntley（`while :; do cat PROMPT.md \| claude-code ; done`） | **原语**：故意无限的 bash 循环——**无内建停止条件**（TODO 耗尽与否是 "a matter of taste"）；back pressure＝类型/测试/静态分析/安全扫描当逐轮拒绝门；signs＝把踩坑写成环境里的牌子；fix_plan.md 每轮确定性重装；"There's no way in heck would I use Ralph in an existing code base"（greenfield 专用） | **【一手】** | ✅ [evidence-b §1](evidence-2026-09-26-b-stop-and-scheduling.md) |
| **2025-11-26** | **harness engineering 的前身文本** | Anthropic《Effective harnesses for long-running agents》（Justin Young） | **学科**：initializer 把粗目标展开成 feature_list.json（claude.ai clone 一例 200+ 条，结构 category/description/steps/passes，初始全部 `passes: false`）；"It is unacceptable to remove or edit tests"；JSON 选型因"模型较不易整文件改写"；"提前宣告完成"被官方点名为头号失败模式 | **【一手】** | ✅ [evidence-b §3](evidence-2026-09-26-b-stop-and-scheduling.md) |
| **2025-11-12** | **Natural Language Development** | François Zaninotto（marmelab《The Waterfall Strikes Back》） | **另一次命名**："'Vibe coding' sounds dismissive"。⚠️ **归属修正（C 路）**："Most coding agents already have a plan mode and a task list. In most cases, SDD adds little benefit." 与 "False Sense of Security" 两条名言的出处是**这篇 2025-11-12**，不是 2026-09-24 审计文 | **【一手】** | ✅ [evidence-c](evidence-2026-09-26-c-autonomy-and-convergence.md) |
| 2026-02-11 | **harness engineering** 正式命名 | OpenAI（Ryan Lopopolo） | **学科**：~100 万行代码、0 行手写、约 1500 个合并 PR | 【转引】 | ⏳ |
| 2026-02 | **Agentic Engineering** | Karpathy（终结自创的 Vibe Coding） | **另一次命名**：99% 时间不直接写代码，在指挥 agent | 【转引】 | ⏳ |
| **2026-09-27 勘误** | 上一行 2026-02-11 的【转引】⏳ **已被一手正文取代**（旧行保留） | OpenAI / Ryan Lopopolo《Harness engineering》全文已取得 | 0 行手写、约百万行、约 1500 PR、3→7 名工程师均为**该团队自述**；文中把自己的评审循环称为 Ralph Wiggum Loop；巨型 AGENTS.md 失败，短地图 + `docs/exec-plans` 为记录；明确写不可外推，多年一致性未知 | **【一手】** | ✅ [evidence-i](evidence-2026-09-27-i-high-influence-control.md) Source 6 |

---

## 三、loop 原语的 2026 上半年厂商落地（本轮新增，B 路一手）

| 日期 | 事件 | 要点 | 回源 |
|---|---|---|---|
| **2026-01-23** | OpenAI / Michael Bolin《Unrolling the Codex agent loop》 | 候选页面文本显示：turn 在模型不再发出工具调用、写出 assistant message 时结束，文本称 termination state，控制交还用户；该消息可以是追问。一个 turn 内可有多次推理与工具调用。compact 是上下文资源兜底，不是质量验收。**「四拍」不是已核实的原文用语。** | ⏳ [evidence-k](evidence-2026-09-27-k-unrolling-codex-agent-loop.md)（直接 HTTP 403，待独立复核） |
| **2026-03-25** | Anthropic《How we built Claude Code auto mode》（John Hughes） | 审批循环的官方解剖：deny-and-continue（拒绝带理由回给模型换安全路径，不终止循环）；**双阈值熔断**（3 连拒或累计 20 拒 → 停机升级给人；headless 无 UI 直接终止进程；阈值官方写明不可配置）；分类器 "reasoning-blind by design"（只看用户消息与工具调用，剥掉模型自述——防评估器被操纵） | ✅ [evidence-b §4b](evidence-2026-09-26-b-stop-and-scheduling.md) |
| **2026-04-08** | Anthropic《Managed Agents》（Lance Martin 等） | 把"外层"本身接口化：session（append-only 日志）/ harness（循环本体）/ sandbox 三件虚拟化，harness 崩了 `wake(sessionId)` 从最后事件恢复；《Building effective agents》页顶官方注记指其为 current approach | ✅ [evidence-b §5](evidence-2026-09-26-b-stop-and-scheduling.md) |
| **2026-04-30** | OpenAI《Auto-review of agent actions without synchronous human oversight》 | 标题即立场：人工同步审批退出调度回路。独立审批 agent（"The separation of roles matters"——主 agent 有把审批边界当障碍绕过的压力）；审批停机约 200× 减少、 escalated 动作约 99% 通过；"automatically stop the trajectory after repeated denials"；官方自述边界："Auto-review should not be treated as a guarantee of security" | ✅ [evidence-b §4d](evidence-2026-09-26-b-stop-and-scheduling.md) |
| 活文档（锚点 v2.1.228/283/269） | Claude Code 官方文档：`/goal` · `/loop` · permission-modes | `/goal`＝条件驱动（独立小模型每轮判定，三值：Not yet met / Met / Impossible）；`/loop`＝时间驱动（间隔可固定/模型自选/loop.md 定制，7 天硬过期"bounds how long a forgotten loop can run"）；auto mode v2.1.283+ 为内置默认 | ✅ [evidence-b §4a/4b/4c](evidence-2026-09-26-b-stop-and-scheduling.md) |

---

## 四、谱系背景人物（2026-06 前，**不入 KOL 名册**）

| 人物 | 贡献 | 日期 | 已有卡片 / 回源 |
|---|---|---|---|
| Kief Morris | **四级阶梯**：outside / in / on the loop → **agentic flywheel**（C 路核实：四级非三级，flywheel 为节标题；脚注澄清 ralph 原始形态里 "operator plays an important role in steering"） | 2026-03-04 | [`_raw_kol/10`](../../../../01_sources/reference/kol/_raw_kol/10_kief_morris.md) ✅ [evidence-c](evidence-2026-09-26-c-autonomy-and-convergence.md) |
| Birgitta Böckeler | steering loop / guides-sensors 模型（**spec 降格为 feedforward guide 而非审批门**）。⚠️ **归属修正（C 路）**："False sense of control?" 在 **2025-10-15 的 sdd-3-tools.html**（含具体案例：agent 把既有类的 research 笔记当新规格重复生成 duplicates），不在 2026-04-02 的 harness-engineering.html | 2025-10-15 / 2026-04-02 | [`_raw_kol/01`](../../../../01_sources/reference/kol/_raw_kol/01_thoughtworks.md) ✅ [evidence-c](evidence-2026-09-26-c-autonomy-and-convergence.md) |
| **Viv Trivedy**（LangChain） | **"Agent = Model + Harness" 公式的原创者**——⚠️ **归属修正（C 路）**：marmelab 记功给 Böckeler，但 Böckeler 本人文章把公式链到 LangChain《The anatomy of an agent harness》，Osmani 明写是 Trivedy 的 one-liner。**一手链：Trivedy/LangChain 原创 → Böckeler 传播锚点化** | 2026 上半年 | 无卡片（候选入册） |
| Andrej Karpathy | Vibe Coding → Agentic Engineering | 2026-02 | [`_raw_kol/07`](../../../../01_sources/reference/kol/_raw_kol/07_andrej_karpathy.md) ⏳ |
| Ryan Lopopolo | 命名 harness engineering | 2026-02 | [`_raw_kol/09`](../../../../01_sources/reference/kol/_raw_kol/09_ryan_lopopolo.md) ⏳ |
| **Stripe**（Beswick & Epsteen） | 《You can't whisper at an AI agent》hard / soft steering——"errors block progress but warnings don't"（C 路逐字到手） | 2026-05-14 | ✅ evidence-c |
| **Harrison Chase**（LangChain CEO） | "harness engineering is an extension of context engineering"（播客转述）；LangChain 四环文页尾致谢含他（evidence-b）但非本人署名 | 2026-03 | ⏳ |

> ⚠️ **本仓受影响的旧账**：[`talk-harness-201/02_evidence/01-kol-alignment-2026.md`](../../../../talk-harness-201/02_evidence/01-kol-alignment-2026.md) 立场①表格里把公式记为"出自 Birgitta Böckeler"——与一手链冲突，**建议该 talk 复核时修正**（`03_practice/harness_governance/result/backbone.md` 宪法 1 的记法"Trivedy 命源 + Böckeler 框架化"是对的）。

---

## 四之二、高影响面控制实践（本词命名之外；I 路，2026-09-27）

不入 §A 名册：要么早于 2026-06，要么是活文档产品机制、并未使用 “loop engineering” 这个词。主张以 [evidence-i](evidence-2026-09-27-i-high-influence-control.md) 与 [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) 为准。

| 日期 | 事件 | 要点 | 回源 |
|---|---|---|---|
| **2023-07-02** | **Paul Gauthier / Aider** benchmark 测试反馈环 | "Aider updates the implementation file based on GPT's reply and runs the unit tests. If all tests pass, the exercise is considered complete. If some tests fail, aider sends GPT a second message with the test error output."——本主题最早已归档的脚本化「跑→测→喂错→重试」循环（硬性 2 次尝试，benchmark harness 非日常工作流） | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D6 |
| **2024-05-22** | **Paul Gauthier / Aider**《Linting code for LLMs》 | 每次 LLM 编辑后 lint，人点头后把错误喂回模型，可迭代数次。现行文档：lint 默认开，测试环要 `--auto-test` | ✅ [evidence-i](evidence-2026-09-27-i-high-influence-control.md) Source 1 |
| **2025-03-30** | **Dex Horthy** 12-factor agents 仓库创建（最后 push 2025-09-21） | 反对 “prompt + 工具袋 + loop until goal”；控制流要在工具选定与执行之间可打断 | ✅ [evidence-i](evidence-2026-09-27-i-high-influence-control.md) Source 2 |
| **2025-04-15** | **Thorsten Ball**（Amp）《How to Build an Agent》（⚠️ 一手标题非《How to Build a Coding Agent》——后者在本人页面与 HN 提交中均不存在，属二手变体） | **机制本体最短表述**："There isn't. It's an LLM, a loop, and enough tokens."＋agent 定义 "an LLM with access to tools, giving it the ability to modify something outside the context window"；<400 行可教学。无停止条件/治理讨论 | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D1【主验】 |
| **2025-06-12** | **Walden Yan**（Cognition 联创）《Don't Build Multi-Agents》 | 单线程 agent ＋ Principles of Context Engineering（"Share context, and share full agent traces"；"Actions carry implicit decisions, and conflicting decisions carry bad results"）；context engineering ＝ "effectively the #1 job of engineers building AI agents"。**反并行立场在命名前已公开成形**（影响力峰值在 2025-09-01 HN 重投，引用须分时点） | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D2【主验】 |
| **2025-06-12** | **Armin Ronacher**（Flask 作者）《Agentic Coding Recommendations》 | 派活后等待完成的自述（"assigning a job to an agent (which effectively has full permissions) and then waiting for it to complete"）；agentic loop 已被当性能与可靠性工程对象（测试缓存 "Surprisingly crucial for efficient agentic loops"）。作者自警会过时 | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D4【主验】 |
| **2025-06-25** | **Kent Beck**《Augmented Coding: Beyond the Vibes》 | 人说 go 才做计划中的下一条测试；跑偏信号含空转、超范围、关/删测试 | ✅ [evidence-i](evidence-2026-09-27-i-high-influence-control.md) Source 3 |
| **2025-07-18** | **Manus**（Yichao 'Peak' Ji）《Context Engineering for AI Agents》 | **最完整的 "loop until the task is complete" 机制句逐字成文**＋循环工程约束（"the KV-cache hit rate is the single most important metric for a production-stage AI agent"、append-only context）；文件系统作为外部记忆支撑长循环（该段经镜像补齐·主验待补） | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D3【主验（loop/KV-cache 段）】 |
| **2025-09-30** | **Simon Willison**《Designing agentic loops》 | 相邻专名，不是 loop engineering 的词源。agent ＝ tools in a loop；要有清楚成功标准；测试套件放大价值；YOLO 同时放大破坏与外泄 | ✅ [evidence-i](evidence-2026-09-27-i-high-influence-control.md) Source 4 |
| **2025-10-13** | **Steve Yegge**《Introducing Beads》 | 会话间无记忆；层级 markdown 计划导致提前宣布 DONE；主张 git JSONL issue + 做完一个 issue 就杀掉会话。单人观察，alpha | ✅ [evidence-i](evidence-2026-09-27-i-high-influence-control.md) Source 5 |
| **2025-10-17** | **Armin Ronacher**《Building an Agent That Leverages Throwaway Code》 | **命名前把「步数上限＋显式终止判据＋逐步缓存恢复」写成一手伪代码**：`while (stepCount < MAX_STEPS) { … if (reachedEndCondition(state)) { break; } }`；durable execution ＝ "retry a complex workflow safely without losing progress"。玩具级示例，非生产主张 | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D5【主验】 |
| **2025-12-09** | **Amp**《200k Tokens Is Plenty》（谱系内部反例） | 同一团队八个月内从 "loop＋enough tokens" 转向短线程反长循环（"Agents get drunk if you feed them too many tokens."）；该文现被官方加 Archived 头撤销（auto-compaction 时代已变）。**立场随模型/上下文条件摆动的一手记录，不作任何一方定论** | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D7（侦察回源） |
| 活文档（观测 2026-09-27） | **Cursor Cloud Agents**、**GitHub Copilot cloud agent** | Cursor：不能跑测试就闭不上环，交接是分支/PR + 截图视频日志。Copilot：Actions 环境里跑测试/linter，59 分钟硬停，单仓库单分支单 PR | ✅ [evidence-i](evidence-2026-09-27-i-high-influence-control.md) Source 7–8 |

## 五、本主题的观测锚点（不是外部事件，是我们自己的动作）

| 日期 | 动作 |
|---|---|
| 2026-06~07 | 主题建立，只消化 Andrew Ng 一篇（原 `digested_andrew/`） |
| 2026-09-26（上午） | **主题重构**：三层 + KOL 主轴；KOL 素材迁入 `01_sources/reference/kol/_raw_loop_engineering/`；建台账与时间线；登记与 `03_practice/` 的分工边界与升格触发器 |
| 2026-09-26（下午） | **三路回源全部完成**：A 路（词源与定义者）· B 路（停止条件/调度，9 个一手记录块）· C 路（自主度/收敛）归档为 `raw/evidence-*.md`；**用户质量门槛**落库（论坛评论者/聚合媒体/碎片推文不入册） |
| 2026-09-26（晚） | **两轮四维评审 + 全部修复**：第一轮（自查 24 项 + 冷读 20 项）与第二轮（合并 29 项）全部落地——引用强度降级、时间窗合规移行、计数统一、evidence 调和注记、org/community 撤销；git 提交 8396657 后复检再修 |
| 2026-09-27 | **I 路**：簇外高影响面控制实践归档为 [evidence-i](evidence-2026-09-27-i-high-influence-control.md)。OpenAI harness 正文从 ⏳ 改为已取得；《Unwinding》仍未取得。不升 §A |
| 2026-09-27 | **J 路**：一条本机 DSH goal session 的七字段事后编码，见 [evidence-j](evidence-2026-09-27-j-local-goal-session.md)。外置行对照臂未跑。不是公开事件 |
| 2026-09-27 | **行 K**：执行前写下 [ledger-row-2026-09-27-k.md](ledger-row-2026-09-27-k.md)，工作项是尚未开始的 Unwinding。本机 headless 没有 `/goal`，goal 未创建，正文未取。不是公开事件 |
| 2026-09-27 | **K 路勘误**：Unrolling 的检索工具候选摘录写入 [evidence-k](evidence-2026-09-27-k-unrolling-codex-agent-loop.md)。直接 HTTP 仍 403，终止态仍待独立复核。没有 DSH goal，不是对照臂 |
| 2026-09-27 | **I 路批次 2（扩容扫描）**：五切口（厂商控制面 / evals 思想 / 定量效果 / 谱系长文 / SDD×loop 厂商）归档为 [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md)；每条区分 `【主验】` 与 `【侦察回源】`，后者待复核、不增加独立票。§一保留 Tessl 候选定义行；§四之二新增 2023–2025 谱系候选。不升 §A |

---

## 六、对照：SDD 侧的收敛动向（C 路一手核实）

**收敛成立且双向，全部可溯源到官方一手动作**（展开见 `digested/` 边界判定篇）：

- **OpenSpec**（官方 docs 逐字）：v1.0.0 拆刚性阶段（"No more rigid phases"、"Dependencies are enablers, not gates"）；人工确认收缩为 "only when context is critically unclear"（v1.13.2）；npm 官方包为 `@fission-ai/openspec`；README 保留 "Agree before you build"。
- **Spec Kit**（官方 release/community 目录）：收录 **Ralph Loop extension**（扩展自身 v1.5.0，v1.0.9 release note 坐实）与 **Autonomous Run Governance preset**（#3501）；v1.0.4 官方接入 DSH（#4336）。
- **loop 侧反向**：Böckeler 把 spec 降格为 feedforward guide；marmelab 明说 plan mode + task list 已被 coding agents 内置，"In most cases, SDD adds little benefit"（注意出处是 2025-11-12，见第二节）。
- **判语**：两边收敛到同一形态「**机械门 + 少量真人判断点**」；"取代"不成立（SDD 工具 2026-09 仍活跃发版）。

SDD 工具 release 史与辩论谱系的**权威在** [`03_practice/spec_driven_development/`](../../../../03_practice/spec_driven_development/README.md)，本节只放与 loop 侧对判所需的最小集。
