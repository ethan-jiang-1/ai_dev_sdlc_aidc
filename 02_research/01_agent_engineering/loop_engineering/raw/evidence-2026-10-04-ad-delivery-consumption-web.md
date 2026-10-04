# Evidence AD — 反馈路径·投递与实际消费（T3b·网页一手，2026-10-04）

**路别**：反馈路径问题——结果产生后如何送达实际消费者（模型输入或控制分支）·投递与实际消费（T3b·网页一手）。
**执行日期**：2026-10-04（观测日期同）。
**来源**（计划指定三篇，全部一手实取正文）：

| # | 来源 | 发布日期 | 获取方式 |
|---|------|----------|----------|
| W | https://www.anthropic.com/engineering/writing-tools-for-agents | 2025-09-11（页面标注 "Published Sep 11, 2025"） | curl 实取，HTTP 200 |
| H | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | 2025-11-26（页面标注 "Published Nov 26, 2025"） | curl 实取，HTTP 200 |
| L | https://docs.langchain.com/oss/python/langgraph/persistence ＋ 同站替代页 checkpointers / use-time-travel | 页面无发布日期 | curl 实取，HTTP 200 |

**获取说明**：web_fetch 工具本轮对 anthropic.com / docs.langchain.com 均报 hostname 解析异常（与前轮 evidence-z 同症），按纪律切换 curl 直取成功——三页均为一手正文，**无 fetch 失败待核项**。LangGraph 计划页 `persistence` 实取成功但其站内 "Time travel" 导航 URL `/oss/python/langgraph/time-travel` 返回 404，从页面 href 反查实际路径为 `/oss/python/langgraph/use-time-travel`，已替代回源并记实际 URL（同站官方文档页，符合预案）。

**标注约定**：〔设计建议〕＝作者建议这样做；〔机制描述〕＝产品/参考实现实际这样做；〔实验观察〕＝作者报告其实验中发生的行为（非一般化效果结论）。引句逐字，粗体为档案笔者所加强调。

---

## 一、来源 W：Writing effective tools for agents — with agents（Anthropic Engineering）

主题：工具结果如何返回给 agent——返回什么、不返回什么、截断/分页建议、错误信息可行动性。

### W1 〔机制描述〕Claude Code 对工具响应的 25,000 token 默认上限＋截断工具箱
> "We suggest implementing some combination of pagination, range selection, filtering, and/or truncation with sensible default parameter values for any tool responses that could use up lots of context. **For Claude Code, we restrict tool responses to 25,000 tokens by default.** We expect the effective context length of agents to grow over time, but the need for context-efficient tools to remain."

前半句是〔设计建议〕，"For Claude Code…25,000 tokens by default" 是〔机制描述〕（作者自述其产品的默认行为）。同段后半句是设计前瞻（随上下文变长"截断需求仍在"）——**非效果结论**。

### W2 〔设计建议〕截断必须附带引导性指令，否则截断本身就是断头投递
> "**If you choose to truncate responses, be sure to steer agents with helpful instructions.** You can directly encourage agents to pursue more token-efficient strategies, like making many small and targeted searches instead of a single, broad search for a knowledge retrieval task."

配套机制句（节选自同段之后的图注）：
> "**Tool truncation and error responses can steer agents towards more token-efficient tool-use behaviors (using filters or pagination) or give examples of correctly formatted tool inputs.**"

即：截断后的响应体本身被当作控制分支的输入——截断文本里写什么指令，决定 agent 下一步怎么走。

### W3 〔设计建议〕错误信息必须"具体且可行动"，拒绝裸错误码/堆栈
> "Similarly, if a tool call raises an error (for example, during input validation), you can prompt-engineer your error responses to **clearly communicate specific and actionable improvements, rather than opaque error codes or tracebacks.**"

（正文配有 "unhelpful error response" vs "helpful error response" 对照图，图为截图本档案未转录。）

### W4 〔设计建议〕只回传高信号字段，弃用低层技术标识符
> "tool implementations should take care to **return only high signal information back to agents**. They should prioritize contextual relevance over flexibility, and **eschew low-level technical identifiers (for example: uuid, 256px_image_url, mime_type)**. Fields like name, image_url, and file_type are much more likely to directly inform agents' downstream actions and responses."

配套自然语言标识符主张（〔实验观察〕，作者自称发现）：
> "We've found that merely resolving arbitrary alphanumeric UUIDs to more semantically meaningful and interpretable language (or even a 0-indexed ID scheme) significantly improves Claude's precision in retrieval tasks by reducing hallucinations."

### W5 〔设计建议〕用 response_format 枚举把"详略选择权"交给 agent（含 token 对比）
> "You can enable both by exposing a simple response_format enum parameter in your tool, allowing your agent to control whether tools return 'concise' or 'detailed' responses"

图注（作者对其示例的度量，〔实验观察〕）：
> "'concise' tool responses return only thread content and exclude IDs. In this example, we use ~⅓ of the tokens with 'concise' tool responses."

同一节还留了格式没有普适答案的口子（〔设计建议〕）：
> "Even your tool response structure—for example XML, JSON, or Markdown—can have an impact on evaluation performance: there is no one-size-fits-all solution."

### W6 〔设计建议〕用"聚合型工具"在工具侧消化中间输出，而不是把原始清单丢回上下文
> "Instead of implementing a read_logs tool, consider implementing a **search_logs tool which only returns relevant log lines and some surrounding context**."

以及（同节，〔设计建议〕）：
> "Tools should enable agents to subdivide and solve tasks in much the same way that a human would…and simultaneously **reduce the context that would have otherwise been consumed by intermediate outputs**."

配套诊断信号（〔设计建议〕，用评测指标反推投递参数）：
> "Lots of redundant tool calls might suggest some rightsizing of pagination or token limit parameters is warranted; lots of tool errors for invalid parameters might suggest tools could use clearer descriptions or better examples."

---

## 二、来源 H：Effective harnesses for long-running agents（Anthropic Engineering）

主题：长程 harness 的反馈路径——结果如何在轮间被下一轮实际消费（feature list / progress file / git / 验证器）。

### H1 〔实验观察〕compaction 不可靠：压缩传递指令"并不总是清楚"
> "First, the agent tended to try to do too much at once—essentially to attempt to one-shot the app. Often, this led to the model running out of context in the middle of its implementation, leaving the next session to start with a feature half-implemented and undocumented. The agent would then have to guess at what had happened…and spend substantial time trying to get the basic app working again. **This happens even with compaction, which doesn't always pass perfectly clear instructions to the next agent.**"

这是三篇中对"压缩是否保留关键事实"最直接的一手负面表述：compaction 会失真，下一轮拿到的是不完整指令。作者由此引出的对策是**不依赖压缩**、改走外置工件（见 H2–H4）。

### H2 〔机制描述〕初始化 agent 铺设三类跨轮投递工件：init.sh / progress 文件 / 初始 git commit
> "Initializer agent: The very first agent session uses a specialized prompt that asks the model to set up the initial environment: **an init.sh script, a claude-progress.txt file that keeps a log of what agents have done, and an initial git commit** that shows what files were added."

关键设计动机（〔设计建议〕）：
> "The key insight here was finding a way for agents to quickly understand the state of work when starting with a fresh context window, which is accomplished with the claude-progress.txt file alongside the git history."

### H3 〔机制描述〕feature list：200+ 条全标 "failing"，作为"完整功能长什么样"的持久清单
> "we prompted the initializer agent to write a comprehensive file of feature requirements expanding on the user's initial prompt. In the claude.ai clone example, this meant **over 200 features**…These features were all initially marked as 'failing' so that later coding agents would have a clear outline of what full functionality looked like."

清单防篡改约束（〔机制描述〕其 prompt 用词＋〔实验观察〕格式选型结论）：
> "We prompt coding agents to edit this file only by changing the status of a passes field, and we use strongly-worded instructions like **'It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality.'** After some experimentation, we landed on using JSON for this, as the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files."

### H4 〔机制描述〕每轮的投递闭环：开局读三件套，收尾写 git commit ＋ progress 更新
每轮开局的固定取数步骤（作者给的 prompt 原文，逐字）：
> "**Read the git logs and progress files to get up to speed on what was recently worked on.**"
> "**Read the features list file and choose the highest-priority feature that's not yet done to work on.**"

收尾写回（故障对策表原文）：
> "**End the session by writing a git commit and progress update.**"

及为何要 git（〔设计建议〕＋〔实验观察〕）：
> "…the best way to elicit this behavior was to ask the model to commit its progress to git with descriptive commit messages and to write summaries of its progress in a progress file. **This allowed the model to use git to revert bad code changes and recover working states of the code base.**"

### H5 〔机制描述〕验证器驻留在工件里：feature list 的 passes 字段＝下一轮的"还剩什么没做"输入
> "Claude marks features as done prematurely." → 对策（表内原文）："Set up a feature list file." / "**Self-verify all features. Only mark features as 'passing' after careful testing.**"

即"完成度"这一关键事实不放在对话或压缩摘要里，而是放在 JSON 清单的 `passes` 布尔字段中——下一轮开局第一步就读它（呼应 H4）。

### H6 〔设计建议〕"clean state"定义：轮末状态以"可被下一轮直接接手"为准
> "By 'clean state' we mean the kind of code that would be appropriate for merging to a main branch: there are no major bugs, the code is orderly and well-documented, and in general, **a developer could easily begin work on a new feature without first having to clean up an unrelated mess.**"

---

## 三、来源 L：LangGraph Persistence（＋替代页 Checkpointers / Use time-travel）

实际回源 URL：
- `https://docs.langchain.com/oss/python/langgraph/persistence`（概览页）
- `https://docs.langchain.com/oss/python/langgraph/checkpointers`（深度页，替代/扩展）
- `https://docs.langchain.com/oss/python/langgraph/use-time-travel`（站内 "Time travel" 导航的真实路径；`/time-travel` 为 404）

页面均无发布日期。

### L1 〔机制描述〕checkpoint 与 thread 绑定：thread_id 是存取主键，缺它则无法恢复
> "The checkpointer uses **thread_id as the primary key** for storing and retrieving checkpoints. **Without it, the checkpointer cannot save state or resume execution after an interrupt**, since the checkpointer uses thread_id to load the saved state."

（概览页）双系统分工：
> "Checkpointers persist a thread's graph state as checkpoints. Use them for short-term, thread-scoped memory… **Stores persist application-defined data outside the graph state. Use them for long-term, cross-thread memory**…"

### L2 〔机制描述〕checkpoint 粒度＝super-step 边界；恢复只能从检查点走
> "LangGraph creates a checkpoint at each super-step boundary…**you can only resume execution from a checkpoint (i.e., a super-step boundary).**"

同页（检查点为全量快照，非摘要）：
> "**By default, LangGraph checkpoints write the full value of every state channel at each super-step.** For long-running threads with large accumulations—such as multi-turn conversations—this can produce significant storage growth over time."

### L3 〔机制描述〕pending writes：同 super-step 内成功节点的写入已持久化，恢复时不重跑
> "When a graph node fails mid-execution at a given super-step, **LangGraph stores pending checkpoint writes from any other nodes that completed successfully at that super-step. When you resume graph execution from that super-step you don't re-run the successful nodes.**"

及故障容错入口：
> "Checkpointing provides fault-tolerance and error recovery: **if one or more nodes fail at a given superstep, you can restart your graph from the last successful step.**"

### L4 〔机制描述〕time-travel：旧状态与新结果的关联方式＝分叉新检查点、原历史不动
> "**update_state does not roll back a thread. It creates a new checkpoint that branches from the specified point. The original execution history remains intact.**"

> "Fork: Branch from a prior checkpoint with modified state to explore an alternative path. Both work by resuming from a prior checkpoint. **Nodes before the checkpoint are not re-executed (results are already saved). Nodes after the checkpoint re-execute, including any LLM calls, API requests, and interrupts (which may produce different results).**"

> "Replay re-executes nodes—it doesn't just read from cache. **LLM calls, API requests, and interrupts fire again and may return different results.**"

update_state 的 reducers 语义（Checkpointers 页）：
> "**This creates a new checkpoint with the updated values — it does not modify the original checkpoint.** The update is treated the same as a node update: values are passed through reducer functions when defined, so channels with reducers accumulate values rather than overwrite them."

### L5 〔机制描述〕三种 durability 档位决定"结果何时变得可被下轮消费"
> "'exit': LangGraph persists changes only when graph execution exits…**'async': LangGraph persists changes asynchronously while the next step executes**…there is a small risk that LangGraph does not write checkpoints if the process crashes during execution. **'sync': LangGraph persists changes synchronously before the next step starts.**"

### L6 〔机制描述·beta〕DeltaChannel：存储层从全量改为增量（langgraph>=1.2，beta）
> "**DeltaChannel stores only incremental deltas instead of the full accumulated value**, substantially reducing checkpoint size for append-heavy channels."

（配套 subgraph 边界提示，概览页 troubleshooting：每个 subgraph 有自己的 checkpoint namespace，"the parent graph may not see the changes immediately"，官方 Fix 是"Use shared state via Store…or configure your subgraph to write to the parent checkpoint"。）

---

## 四、三篇合看：摘要、截断、压缩是否保留关键事实

**核心可引用表述（按主张强度排序）**：

1. **压缩（compaction）会丢失关键事实——唯一的一手负面表述来自 H1**："This happens even with compaction, which doesn't always pass perfectly clear instructions to the next agent."（〔实验观察〕，Anthropic 自家长程实验；非产品机制描述，也非一般化效果结论。）
2. **截断是产品级默认机制，且截断体本身承担控制职责——W1/W2**：Claude Code 默认 25,000 token 上限（〔机制描述〕）；作者建议截断必须附带引导指令、把 agent 推向过滤/分页（〔设计建议〕）。即截断方案的完整形态＝"截断＋指令"，光截断不断言保留哪些事实。
3. **LangGraph 的持久化不做摘要、存全量——L2**："checkpoints write the full value of every state channel at each super-step"，其增长代价用 prune/retention 处置（persistence 页 troubleshooting："Prune old checkpoints periodically or set a retention policy"），**不用压缩摘要**。即：LangGraph 路线上"关键事实保留"靠精确快照＋thread 绑定（L1）而非有损压缩。
4. **三篇共同的隐含答案：关键事实不放在压缩摘要里，放在外置工件里**——H 的 feature list JSON / progress file / git history（H2–H5）、W 的"聚合型工具在工具侧消化中间输出"（W6）、L 的全量 checkpoint＋跨线程 Store（L1）。投递渠道本身（文件、JSON 字段、checkpoint 表）就是关键事实的载体，摘要是易失路径。
5. **详略留权给消费者——W5**：response_format 枚举让 agent 自己选 concise/detailed（作者示例 ~⅓ token，〔实验观察〕），对应"截断/压缩应保留什么"由消费侧声明，而非投递侧单向裁剪。

---

## 五、边界提示：设计建议 ≠ 已部署机制

- **Anthropic 两篇是 engineering blog**，叙述在"我们的产品这样做"与"你应该这样做"之间自由切换：W1 一句话里前半是建议、后半（25k 默认值）才是机制描述。本档案逐句拆标，**引用时不得把整句当机制**。
- **H 的 initializer/coding agent 是 quickstart 参考实现**（作者脚注：两者仅初始 prompt 不同，"The system prompt, set of tools, and overall agent harness was otherwise identical"）。feature list / progress file 是**该 demo 的机制描述**，不等于 Claude Agent SDK 的默认行为——是否已进入产品默认路径，本档案未核实。
- **W 的 25,000 token 默认值**是作者 2025-09 的自述，是否可配置、当前版本是否仍为此值未核（需产品文档级回源）。
- **LangGraph docs 是产品文档**，机制描述密度高，但 "Fix:" 段落是建议；DeltaChannel 明标 beta（"The API may change in future releases"），不宜当稳定机制引用。
- **效果类自述一律未采信为结论**：W 的 "~⅓ of the tokens"、"dramatically improved"、SWE-bench 表现句，H 的 "dramatically improved performance"，均为作者自述，本档案只登记表述、不作效果判读（遵守"不写效果结论"纪律）。
- **类目对齐陷阱**：W/W2 的截断作用于"单次工具响应"；L 的全量快照作用于"图状态持久化"；H 的 compaction 作用于"上下文窗口"——三者是反馈路径上不同环节的保留机制，不能直接互相比较"谁更保留关键事实"。

---

## 六、未答问题与待核清单

**fetch 失败待核项：无**（三篇全部 curl 实取成功；前轮 DNS 异常在 curl 路径不复现）。

**已闭合的结构变更**：LangGraph `/oss/python/langgraph/time-travel` 404 → 实际为 `/oss/python/langgraph/use-time-travel`，已替代并记录。

**未答问题（下一轮回源候选）**：
1. Claude Code 工具响应 25k token 上限：产品文档核实默认值现状与可配置性（对应 W1）。
2. H 的 feature list / progress file / init.sh 三件套是否进入 Claude Agent SDK 正式默认行为，或仅存于 quickstart 示例。
3. LangGraph Agent Server "handles persistence infrastructure behind the scenes" 的具体行为（概览页只有一句带过，无机制细节）。
4. Anthropic 两篇的 compaction 内部机制（如何摘要、丢什么）两篇均未展开——H 只给了"不一定传清楚"的观察，属"知道会失真、不知道怎么失真"。
5. W 提到的官方工具定义最佳实践页（"our Developer Guide"）与 tools 动态加载机制页未回源，属 W 路延展。

**临时产物**：本轮抓取的 HTML/文本存于仓库根 `.tmp-t3b-web/`（`.gitignore` 已覆盖），已用毕即弃，不入库。
