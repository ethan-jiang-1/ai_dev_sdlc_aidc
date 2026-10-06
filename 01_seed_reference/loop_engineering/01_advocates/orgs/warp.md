# warp — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

**（第三轮挖掘（2026-10-06））**

### 增量 A · Warp —— 解决·强（三载体到手：CEO 署名博客 06-16＋工厂博客 08-27＋Profiles/Permissions 文档）

- **A1. 官方博客《How to build a self-improvement loop for your Skills》**
  - URL/日期：https://www.warp.dev/blog/self-improvement-loop-for-skills ；datePublished **2026-06-16T12:00:00Z**（页面 JSON-LD 实取），dateModified 2026-06-23；author JSON-LD：**Zach Lloyd**（Warp CEO，署名一手）。通道：curl＋浏览器 UA 直取全文（343KB）。
  - 性质（逐字）：**"There's been a lot of chatter about using "loops" lately to drive agents, and I think this has been accompanied by a bit of "what actually is a loop"? I can't speak for everyone else using the term, but I wanted to show a practical approach using Skills and cloud agents for a particularly powerful kind of loop: a self-improvement loop."**——厂商 CEO 亲自给 loop 术语下产品定义，且自认"人人都在用这个词但没说清是什么"。
  - 逐字摘录：

> "This is the idea that an agent can improve the quality of its own Skills over time from external feedback."

> "An inner agent loop: this is where you actually apply the Skill. For issue triage, you could be running it manually, or, more likely, you have an integration with your task tracker that runs the Skill whenever a new issue is filed."

> "An outer agent loop: this is an agent that runs on a schedule and observes the inner loop use of the Skill."＋"Since Skills are just files, this means it should make a diff to improve Skill based on user feedback from past runs."

> "We use self improvement loops to manage the Warp open-source repository, and we extracted the framework behind it for others to adopt."

  - **该条支持的最小主张**：loop engineering 运动进入厂商产品层的一手证据——Warp CEO 在 2026-06-16（运动词源爆发同月）以"inner/outer agent loop"双层结构发布可复制的自改进环产品教程，并自证 Warp 自家仓库就在用。
  - 派别适配：**推动·厂商**（把循环当卖点——inner/outer 双层 loop＋self-improvement 作为产品能力出售）。

- **A2. 官方博客《Closing the loop with self-improving cloud software factories》（slug: agent-self-improving-software-factories）**
  - URL/日期：https://www.warp.dev/blog/agent-self-improving-software-factories ；页面日期 **2026-08-27**（HTML 实取 "2026-08-27"×6 处；站内博客列表同日标注）。作者字段未在页面 JSON 中暴露（如实记录）。
  - 逐字摘录：

> "It's time to apply a true engineering mindset to deploying coding agents. There's too much hand-waving around what agents are best, which models to use, and how to optimize ROI from coding agents over time."

> "The solution is to set up a closed-loop system in the cloud where all of your agents are tracked and measured against your own data and workflows, so you can adjust your setup based on actual data and not vibes."

> "Software factories are automation loops around the SDLC, comprised of agents that triage, spec, implement, verify, review, monitor, etc."

> "Factories should come with built-in evals, improvement loops and benchmarks so you can ensure improvement over time"＋"Your goal as an organization is getting to a "closed-loop" factory"

> "This is the basis of self-improvement: agents that observe how your factory is working and suggest changes to the underlying models, skills, etc."

> "If someone describes a factory product that is local-first, it's not really a factory."＋"First, the goal is agent automation and automatic improvement, and that's simply not possible if your agents are running on developer laptops that might be asleep or off the grid."

  - 同站同系列（站内博客列表实取标题级）：《The Cloud Software Factory Build Guide》Jul 23, 2026；《The missing feedback loop for software factories》Aug 26, 2026；《Adopting the software factory model: crawl, walk, run》Sep 15, 2026——**Warp 已形成"loop→factory"博客产品线**（4 篇窗口内，标题级登记待深挖）。
  - **该条支持的最小主张**：Warp 把"闭环"上升为品类定义（cloud software factory＝SDLC 自动化环），并以"local-first 不配叫 factory"划产品边界；无人值守的前置条件被官方明确为"云端常驻、笔记本会睡着"。
  - 派别适配：**推动·厂商**（loop＝品类卖点）。

- **A3. 官方文档《Profiles & Permissions》（docs.warp.dev）**
  - URL/日期：https://docs.warp.dev/agents/capabilities/agent-profiles-permissions ；页面页脚实取 **"Last updated Oct 6, 2026"**（=实取当日）；通道：官方 `.md` 后缀直取（页面自述 "Markdown versions of each page are available by appending .md to any URL"，9.9KB markdown 实取）。
  - 逐字摘录：

> "Agent Profiles let you configure how agents behave in different situations, including autonomy level, base model, tool access, and command permissions."

> "Set up different profiles for different workflows (e.g., "Safe & cautious", "YOLO mode", etc.)."

> "The denylist takes precedence over your other permission settings."＋"When all Agent permissions are set to **Always allow**, the Agent gains full autonomy ("YOLO mode"); however, any denylist rules will still override these settings."

> "During an Agent interaction, you can give the Agent full autonomy for the current task. When auto-approve is on, every suggested command runs immediately until the task finishes, or you stop it with `Ctrl+C`."（§ Run until completion）

> "Denylist rules your team enforces through the Admin Panel always require approval and are never bypassed."

  - 上轮缺口解除情况：上轮仅有 CEO"选人从哪里进环"一句——本轮补齐**官方文档层的自主度分档（permission 分级 allow/ask/decide）、命令 allowlist/denylist 优先级、Run until completion 任务级全自主、企业 Admin 层不可绕过底线**四件套（最后一句的边界含义进怀疑面文件增量 C）。
  - **该条支持的最小主张**：Warp 的 agent 自主性是"分档可配"的产品机制（profile×permission×denylist 三层），且存在"企业层永久审批"的把控底线。
  - 派别适配：**推动·厂商**（自主度分档做成产品），同时其 YOLO 默认面是"把控性"主题的直接一手材料。

**（第五轮挖掘（2026-10-06）：厂商机制文档深挖）**

### D · Warp：denylist 语法与优先级、Run until completion 与权限的交互（docs.warp.dev `.md` 直取）

- **denylist 语法与优先级**（agents/capabilities/agent-profiles-permissions.md 实取）：allowlist/denylist 均为**正则**（默认 allowlist 空＋示例逐字："`which .*`、`ls(\s.*)?`、`grep(\s.*)?`"；默认 denylist 示例逐字："`wget(\s.*)?`、`curl(\s.*)?`、`rm(\s.*)?`、`eval(\s.*)?`"）。**优先级逐字**："*The denylist takes precedence over both the allowlist and `Agent decides`: if a command matches the denylist, the Agent asks for permission even when that action type is set to **Always allow**.*" 权限五类（Apply code diffs/Read files/Create plans/Execute commands/Full Terminal Use）× 四档（**Agent Decides / Always ask / Always allow / Never**）；全 Always allow＝YOLO，"*however, any denylist rules will still override these settings*"。**例外唯一且逐字**："*The one exception is Run until completion, which bypasses your denylist by default.*" **Run until completion**：`⌘+Shift+I`（Win/Linux `Ctrl+Shift+I`），逐字警语："*Run until completion is the purest form of \"YOLO\" mode: the Agent proceeds without asking for confirmation, and by default it also runs commands that match your command denylist.*" 关闭旁路＝**Settings > Agents > Warp Agent > Input > Allow auto-approve to bypass command denylist**；**Admin Panel 下发的 denylist 永不旁路**："*Denylist rules your team enforces through the Admin Panel always require approval and are never bypassed.*"
  - 挂钩：**审批与权限**（用户级旁路开关 vs 管理员级不可旁路，双层权威设计）＋**停止条件**（任务级"跑到完成为止"＝一次性全放行）。
