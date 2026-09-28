# ② 硬性资源上限兜底 — 工程实践做法库（自说明版）

> **本文件自说明**：每条做法就地携带核心片段（原句/代码/参数，保留原文语言），读完本文件即得工程要领；`源` 行只作全量逐字与引用链的出处。
> **判定句**（收敛判定权威在 [`../../digested/03-构件.md`](../../digested/03-构件.md) §一）：最大迭代/轮数/时间/拒绝计数/过期做兜底停止——**是资源熔断，不是质量分**。五处一手同向＋I 路补强。
> **收录口径**：无逐字硬核内容可取的条目不入本表（Reddit $6k 案为转述级，撤至 insights #11 保留机制）；标注"已复核"＝主代理逐字核对过。

---

## 一、厂商产品层

### 1. Anthropic 2024 — "最大迭代数"首次成文

**核心**（一手·官方博客，2024-12-19）：

> "The task often terminates upon completion, but it's also common to include **stopping conditions (such as a maximum number of iterations) to maintain control**."

**机制**：与"任务完成即终止"并列的兜底件——官方从一开始就把上限定位为**控制手段**，不是质量判据。
**源**：[evidence-b](../../raw/evidence-2026-09-26-b-stop-and-scheduling.md) §2

### 2. Claude Code `/goal` — 上限写进条件子句＋无进展熔断＋错误分级

**核心**（一手·厂商文档）：

> 上限子句："To bound how long a goal runs, **include a turn or time clause in the condition, such as `or stop after 20 turns`**."
> 无进展熔断："If Claude keeps answering the evaluator **without making progress (no tool use for several turns in a row)**, Claude Code stops the loop, prints a warning, and **returns control to you with the goal still set**."
> 错误分级："Four kinds of failure clear the goal: An authentication failure… An exhausted credit balance… A context overflow that auto-compaction couldn't clear… A model that isn't available"；"After three automatic retries, the goal pauses instead."

**机制**：上限不做成独立参数，而是**条件语法的一部分**（用户可组合）；触发后的去向分三档——无进展＝停但保留 goal、不可恢复错误＝清空 goal、普通错误＝重试三次后暂停。恢复语义随错误类型分级。
**源**：evidence-b §4a

### 3. Claude Code auto mode — 3 连拒 / 20 总拒双阈值熔断

**核心**（一手·官方博客 2026-03-25＋文档；已复核）：

> "If a session accumulates **3 consecutive denials or 20 total**, we stop the model and **escalate to the human**. This is the backstop against a compromised or overeager agent repeatedly pushing towards an outcome the user wouldn't want. In headless mode (`claude -p`) there is no UI to ask the human, so we instead **terminate the process**."
> "**These thresholds are not configurable.**"
> 单拒不停："that denial comes back as a tool result along with an instruction to treat the boundary in good faith: **find a safer path, don't try to route around the block**."

**机制**：双阈值（连续×累计）＋触发后分环境（有 UI 升级给人 / headless 直接杀进程）；阈值官方锁死不可配——厂商替用户押注了"这个数字是安全的"；单次拒绝是**带理由的反馈**而非停止（deny-and-continue）。
**源**：evidence-b §4b

### 4. Claude Code `/loop` — 7 天硬过期＋未续排兜底

**核心**（一手·厂商文档）：

> "**Recurring tasks automatically expire 7 days after creation.** The task fires one final time, then deletes itself. **This bounds how long a forgotten loop can run.**"
> "If an iteration ends without either rescheduling or stopping, Claude Code schedules one **fallback wakeup about 20 minutes later** and ends the loop when that iteration doesn't reschedule either."

**机制**：定时循环的四层终止（人 Esc / 模型自停 `stop:true` / 一次未续排 20 分钟兜底 / 7 天硬过期）——**"被遗忘的循环"被官方当一等风险命名**，死期是产品原语。
**源**：evidence-b §4c

### 5. OpenAI auto-review — 反复拒绝停轨迹＋拒绝可恢复

**核心**（一手·官方博客，2026-04-30）：

> "We also monitor for cases where Codex attempts to game the Auto-reviewer. To reduce the likelihood of this occurring, we **automatically stop the trajectory after repeated denials**."
> "**A rejection does not merely say no.** It gives Codex a rationale and enough signal to continue safely… In our internal deployment, Codex continues after a denial and successfully finds an acceptable solution in **more than half of cases**."
> 边界自述："Auto-review should not be treated as a guarantee of security… we identified cases where Auto-review could be misled into approving commands without user approval."

**机制**：与 Claude 同型不同参（未公布数字）；拒绝设计为可恢复反馈（过半场景自寻安全路径），反复拒绝才熔断；官方自述裁判可被误导——熔断是对裁判失灵的兜底。
**源**：evidence-b §4d

### 6. GitHub Copilot cloud agent — 59 分钟硬顶

**核心**（一手·厂商文档）：

> "Each Copilot cloud agent session has a maximum execution time of **59 minutes**. This is a **hard limit that cannot be extended or bypassed**."

**机制**：产品级时间熔断；跑在一次性 Actions 环境里；一次任务写范围＝单仓库/单分支/单 PR（"Copilot cannot make changes across multiple repositories in one run"）——**范围限制本身就是横向爆炸的闸**。
**源**：[evidence-i](../../raw/evidence-2026-09-27-i-high-influence-control.md) Source 8

### 7. Anthropic quickstart（官方 demo 源码）— 默认 Unlimited，Ctrl+C 是官方停止方式

**核心**（一手·官方源码，主代理本地解码核对）：

> `max_iterations: Optional[int] = None`（docstring："None for unlimited"）→ 未传参打印 "Max iterations: **Unlimited (will run until completion)**"
> 主循环唯一退出：`if max_iterations and iteration > max_iterations: … break`（错误路径**不停**："Will retry with a fresh session..."）
> README："**Press Ctrl+C to pause**; run the same command to resume"；CLI 表：`--max-iterations` 默认 **Unlimited**；预期 "Building all 200 features typically requires **many hours**"
> 而 progress.py 只算通过率给人看：`passing = sum(1 for test in tests if test.get("passes", False))` → `print(f"Progress: {passing}/{total} tests passing…")`

**机制**：上限是 **opt-in**（默认无限）；"will run until completion" 是打印文案，代码层没有实现它的完成检查；错误按可恢复处理不熔断。**连最先讲"机器可核完成定义"的机构，自己的 demo 也把兜底交给 Ctrl+C**（demo 定位，不外推生产）。
**源**：[evidence-l](../../raw/evidence-2026-09-28-l-quickstart-code.md) S1/S2/S4

### 8. Osmani — 把上限写成 goal 条件一部分（实战全例）

**核心**（一手·作者原文，evidence-a 收录）：

> "/goal Refactor the data-fetching layer in Dashboard.tsx until **Lighthouse performance score is >= 92 and LCP is under 1.8s** as shown by the Lighthouse CLI output. **Do not change the public API of any hooks. Each turn must improve at least one reported metric; abort if two consecutive turns show no improvement. Stop after 10 turns.**"

**机制**：一条实战条件里同时有①（可度量终态 Lighthouse>=92）、②（10 轮上限＋连续两轮无改进 abort——**进展熔断**，比纯轮数更细）、③（路径约束"不得改公共 API"）。上限的最佳写法不是独立参数，是**条件里的行为规则**。
**源**：[evidence-a](../../raw/evidence-2026-09-26-a-originators.md)（一手·作者原文）

---

## 二、框架层默认值（源码字面量；含 docs↔源码分歧双录）

### 9. OpenHands — 轮次默认 500，预算默认无

**核心**（一手·源码，tag 锚定 0.30.0）：

> `max_iterations: int = Field(default=OH_MAX_ITERATIONS)` ＋ `OH_MAX_ITERATIONS = 500`（config_utils.py:8 → app_config.py:70）
> `max_budget_per_task: float | None = Field(default=None)`——**轮次有缺省、花费无缺省**

**机制**：Python 时代锚点；main 已重构 TS 栈，500 只锚 Python 线。默认值的版本漂移本身是要点：**引参数必须带 tag**。
**源**：[evidence-q](../../raw/evidence-2026-09-28-q-framework-defaults.md) S2

### 10. SWE-agent — 成本上限是一等默认件

**核心**（一手·源码 main，主代理逐字复核 73-78 行）：

> `per_instance_cost_limit: float = Field(default=3.0, description="Cost limit for every instance (task).")`
> `total_cost_limit: float = Field(default=0.0, ...)` / `per_instance_call_limit: int = Field(default=0, ...)`
> 行为（agents.py:336-339）："Total instance cost exceeded cost limit... **Triggering autosubmit.**"（超 1.1× 阈值）

**机制**：**成本上限做成 schema 级默认（$3.0/实例）**而调用数默认关；超限行为是 autosubmit（带错交卷）不是硬杀——成本维度的兜底语义与轮次不同。
**源**：evidence-q S3

### 11. LangGraph / CrewAI — docs 与源码字面量打架（⚠️ 方法论样本）

**核心**（docs 与源码各为一手，**分歧双录不仲裁**）：

> LangGraph docs："Starting in version 1.0.6, the default recursion limit is set to **1000** steps. … LangGraph will raise GraphRecursionError."
> LangGraph 源码（1.2.12 与 main 一致，`_internal/_config.py:32`）：`DEFAULT_RECURSION_LIMIT = int(getenv("LANGGRAPH_DEFAULT_RECURSION_LIMIT", "10007"))`
> CrewAI docs（v1.15.22）："Maximum iterations before the agent must provide its best answer. **Default is 20.**"
> CrewAI 源码（**同版本号** sdist，base_agent.py:286-288）：`max_iter: int = Field(default=25, …)`；超限走 `handle_max_iterations_exceeded`（**给出最佳答案后收尾**，非硬杀）

**机制**：触发行为两家都清楚（抛错/告警/转最佳答案）；**默认值两处一手来源互相矛盾**——引用"默认值"类主张必须锚"字段＋文件＋tag＋字面量"，docs 单源不可信。
**源**：evidence-q S4/S5

---

## 三、失控模式检测闸门（判据≠拒绝计数）

### 12. OpenRouter — doom-loop 检测：五级动作梯子

**核心**（一手·厂商文档，主代理复核）：

> "It tries the same tool call, gets the same result, and tries again anyway, **like a robot vacuum bumping into the same wall forever**. That's a doom loop: **the run keeps spending money without getting anywhere.**"
> "It's **off by default**. Turn it on with doomLoop: true // recommended defaults: **observe@2, block@3, stop@6**"
> escalate 档："run the NEXT turn on a stronger model … **maxEscalations: 2, // spend cap for the whole conversation**"
> 边界自述："What this doesn't catch: Loops with changing inputs... Saying the same thing in different words"

**机制**：按**重复动作模式**计（同输入工具调用），非按拒绝计；observe→steer→escalate→block→stop 五级——先低干预、再干预、再升级（换更强模型＋整对话花费帽）、最后停；诚实列出漏检形态。
**源**：[evidence-o](../../raw/evidence-2026-09-28-o-runaway-incidents.md) S4

### 13. OpenHands — 默认开启的 stuck detector 与误报史

**核心**（一手·PR＋docs，主代理复核 PR）：

> docs："Repeating Action-Observation Cycles: The same action produces the same observation repeatedly (**4+ times**)… Agent Monologue: …(**3+ messages**)… Alternating Patterns: Two different action-observation pairs alternate in a ping-pong pattern (**6+ cycles**)… can automatically halt execution"
> PR#11799（维护者合并）："adds a new configuration option `enable_stuck_detection` to allow users to disable automatic loop/stuck detection… **defaults to True** for backward compatibility… In cases where the stuck detection is **triggering false positives**"

**机制**：量化阈值＋自动 halt；后因长任务合法重复误报改可配置——**闸门自身有误报率，需要调参而不是只有开关**。与 OpenRouter 独立同构（两家各自得出"重复模式检测＋分级动作"）。
**源**：evidence-o S5

### 14. isitdone — 闸门自己的停止条件：3 次放行

**核心**（一手·个人工具，主代理全文复核）：

> "After **three blocked attempts** the hook lets the agent stop and tells me why, so it can **never trap a session**. Malformed input, a broken config, an internal error: all of those allow the stop. **The gate must never be the thing that breaks the tool.**"

**机制**：连闸门都要有兜底——阻断 3 次放行＋一切异常放行；"能弄死 agent 的闸门一天内就会被卸载"是闸门设计的生存约束。
**源**：[evidence-p](../../raw/evidence-2026-09-28-p-practitioner-gates.md) S1

---

## 四、失控实录（②的存在理由层）

### 15. cline#3418 — 交互式无限循环烧钱（一手 issue，已复核）

**核心**：

> "I am getting a **constant infinite loop** on cline - it doesn't matter what model I choose... **It's burning credits like crazy.** … It is stuck constantly reading files. It never does the work... I have burned an excessive amount of cash trying to resolve this."
> 跟帖："I did 'exit' on all my terminals and it finally started working again. **Burned probably $50** trying to figure this out."
> 维护者（2025-05-12）："models getting confused when working on very large tasks and looping endlessly is a **known issue**, and unfortunately there isn't a simple fix. What tends to happen is **the context fills up with too much instruction or intermediate output, and the model ends up repeating steps without forward progress**…"

**机制**：上下文塞满→重复无前进；发现＝人盯着，停止＝手动杀终端；维护者确认机制且当时无产品级修复（issue 以 not_planned 关闭）。
**源**：[evidence-o](../../raw/evidence-2026-09-28-o-runaway-incidents.md) S1

### 16. claude-code#46787 — 僵尸循环穿透"关闭"动作（canonical，已复核）

**核心**：

> "…a period during which **I was asleep for 14 of those 25 hours** … my account consumed **31% of my weekly usage limit** and 12% of the current 5-hour rate limit session **before I even opened a new terminal**."
> 根因："2 'ralph' automation loops (tmux sessions…) — I had explicitly turned these off days earlier, **but the kill did not propagate to the actual tmux sessions**"；"1 stuck --resume session... running since Thursday"；"53 **orphaned headless Chromium browser processes**... The oldest were **194 hours old (8+ days)**"
> "There is **no built-in mechanism** in Claude Code to detect or alert users about orphaned processes that are silently consuming their usage quota."

**机制**：zombie 循环能穿透显式关闭（kill 传导断裂）；发现＝事后查面板；厂商无内建检测（issue stale 关闭，仅有 bug+area:cost 分诊标签）。
**源**：evidence-o S2

### 17. 用户侧补救 — 进程年龄审计钩子

**核心**（同 issue，报告者自建）：

> "Built a session-start audit hook (process-audit.sh) that now runs on every new Claude Code session and alerts me about **stale Claude processes (>2h)**, tmux sessions, ralph loops, **orphaned browsers (>6h)**, launchd agents, and **stuck --resume sessions (>4h)**"

**机制**：厂商缺位时的用户侧兜底——按**进程年龄分级报警**（2h/4h/6h 三档），在会话启动时跑。
**源**：evidence-o S2

### 18. （记录一笔放弃）Reddit $6k 定时循环案

一手原帖全通道 403，媒体转述两源在任务内容与次数上互相冲突，**无逐字硬核内容可取——按收录口径不入本表**。其机制骨架（30 分钟 cron × 上下文滚到 ~800k token × prompt cache TTL 5 分钟 → 每次全价重建；发现＝超限邮件，面板延迟数天）保留在 [insights #11](../02_hard_caps/insights.md)，仅作转述级参考。
**源**：evidence-o S3（转述级标注）

---

## 五、反例极：故意无限

### 19. Huntley · Ralph — 上限外置给人

**核心**（一手·个人实践）：

> "`while :; do cat PROMPT.md | claude-code ; done`"（bash 循环原文）
> "**Ralph can be done with any tool that does not cap tool calls and usage.**"
> 失控时："you'll wake up to a broken codebase that doesn't compile from time to time… This is where you need to put your brain on. You need to make a judgment call. **Is it easier to do a `git reset --hard` and to kick Ralph back off again? Or do you need to come up with another series of prompts to be able to rescue Ralph?**"

**机制**：内建 vs 外置两极的"外置"端——循环故意无限（前提：工具不限用量），熔断由人执行（看 TODO、`git reset --hard`、换 prompt）。与 Claude Code 家的"上限做成原语"构成谱系两端。
**源**：evidence-b §1

---

## 六、候选与未合并设计（不与已发布行为混计）

### 20. OpenAI Codex PR#20672 — 熔断后从硬停转人工决定（提案，未合并）

**核心**（一手·官方仓库 PR，2026-05-01 提交、05-21 关闭、**merged_at: null**；evidence-f 收录）：

> 标题：`core: escalate repeated auto-review denials to user approval`
> "When Auto-review rejects too many approval requests in one turn, **hard-stopping the turn is abrupt and removes a useful recovery path.**"
> "The request that tripped the breaker can still be handed to the user for an explicit manual decision **without changing the session's approval mode**."
> "This changes the fallback after repeated Auto-review denials from 'stop the turn' to '**ask the user**', while keeping the existing denial thresholds intact."
> "**preserve approval attribution across escalation**: the breaker-triggering Auto-review denial is still recorded as `source=AutomatedReviewer`; the final manual decision is recorded separately as `source=User`."
> 测试名：`guardian_rejection_circuit_breaker`、`guardian_auto_review_warns_after_three_consecutive_denials`

**机制**：明确的升档状态机——重复拒绝触发 circuit breaker → 触发熔断的那次动作转人工 → **机器拒绝与人的决定分开记账**（两个 source 字段）→ 决定后重置 breaker。**不是已发布行为**（PR 未合并），不能当 OpenAI 产品事实引用。
**源**：[evidence-f](../../raw/evidence-2026-09-27-f-autonomy-gates.md) Source 2

### 21. Codex — 上下文 compact：容易误当成停止条件的资源兜底（⚠️ 候选未复核）

**核心**（检索工具摘录，直接页面 403 待独立复核；evidence-k 收录）：

> 机制记录：上下文满了会 compact，**不是质量验收**。早期要人敲 `/compact`；现在超过 `auto_compact_limit` 就自动调用 `/responses/compact`。**文中没有给出这个阈值的数字。**
> 同文边界："compact 是资源兜底，和 assistant message 不是同一种停。"（assistant message 终止态见 [③](../03_verdict_split/practices.md) #8）

**机制**：compact 防的是**上下文物理耗尽**，与质量验收、轮次上限都是不同种的停——把"上下文兜底"混进"停止条件"会污染②的分类。
**源**：[evidence-k](../../raw/evidence-2026-09-27-k-unrolling-codex-agent-loop.md)

---

**同向票数**（判定归 digested/03）：硬上限构件五处一手同向（Anthropic 2024 / `/goal` / auto mode / `/loop` / auto-review）＋I 路 Copilot 补强；框架默认值与失控实录为 2026-09-28 深挖批（Q/O/L 路），不改收敛票数；#20/#21 为未合并提案与候选摘录，不计票。
