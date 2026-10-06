---
type: evidence_archive
collected_by: 委派回源子代理（A 路 · 词源与定义者四人）
collected_at: 2026-09-26
serves: digested/01（命名谱系）· 03_practice/loop_governance/result/backbone.md（§0 定义与判据 / §4 检查点与反例）
status: 四人中两人已回源（Runkle 四环逐字 / Osmani 两篇全取得·分层为四级）、两人部分回源（Cherny：YC transcript 中 loop 出现 0 次、无个人书面定义；Steinberger：词源=两句话推文、无深度内容）
key_findings: 词源=热度碎片（Cherny 06-02 访谈句未逐字核验 + Steinberger 06-08 推文无深度），定义=事后工程化（Osmani 06-07 命名并定义 → Runkle 06-16 四环 → CC 团队 06-30 官方定义）；四人核心同指（系统替人逐轮提示）但外延不兼容（Runkle 第 4 环属 harness 层）
negatives: 见报告 §6（Cherny 访谈无 transcript、Steinberger 推文原文 X 不可达、LangChain 帖中 0xwhrrari 身份开放、swyx loopcraft 404）
quality_bar: 2026-09-26 用户质量门槛——碎片推文不硬凑；不入册内容单列「不入册·仅社区情绪」
---

# 回源报告 A：词源与定义者（访问日期 2026-09-26）

> **任务**：回源 loop engineering 的四位"词源人物与定义者"——Boris Cherny / Peter Steinberger / LangChain(Sydney Runkle) / Addy Osmani——的一手原文。
> **执行标准**（parent 2026-09-26 追加）：只收真 KOL；深度是硬要求；词源碎片与深度长文分开记录；每条证据附"为什么算 KOL"；聚合媒体/HN 评论进「不入册·仅社区情绪」。
> **方法注记**：本环境 X 平台不可达（直连、oEmbed、nitter、threadreader 均超时），所有推文只能确认"存在 + URL + 精确时间戳（snowflake ID 解码）"，正文以最近时 KOL 的转引为最接近版本，并明确标注"逐字未核验"。日期一律标注页面所示；`date` 实测访问日 2026-09-26（CST）。

---

## 1. Boris Cherny

### 状态：部分回源（词源火花逐字未核验；深度替代材料已全取得）

**为什么算 KOL**：Claude Code 创造者、Anthropic Claude Code 团队负责人；loop engineering 的两个产品原语（`/goal`、`/loop`）出自他的团队；被 Osmani 点名引用、被 LangChain 官方博客以名字并列（"AI leaders like Steipete, Boris, and Andrej"）、被 WorkOS×Acquired 与 YC Lightcone 两个大型活动邀请主讲。

#### 1a. 词源火花（碎片级，逐字未核验）

**一手源记录 A1**：WorkOS × Acquired Unplugged 访谈（词源事件本体）
- URL: https://www.youtube.com/watch?v=RkQQ7WEor7w （视频本体，**无 transcript 取得**）
- 作者：Boris Cherny（受访者），Ben Gilbert & David Rosenthal（Acquired 主持）
- 发布日期：2026-06-02（活动日；据 WorkOS 官方回顾页与多方一致指认）
- 访问日期：2026-09-26
- **状态：已确认存在但正文未取得**。能看到的证据：视频存在于 YouTube；WorkOS 官方回顾页（下）。

**一手源记录 A2**：WorkOS 官方回顾（主办方一手记录，**但为 WorkOS 作者的转述而非逐字引句**）
- URL: https://workos.com/blog/boris-cherny-claude-code-acquired-interview-takeaways
- 作者：Noelle Festa（WorkOS）；WorkOS 是该活动主办方（presented by WorkOS）
- 发布日期：2026-06-02（页面标注）
- 访问日期：2026-09-26
- 逐字引句（WorkOS 自己的行文，非 Cherny 原话）：
  - "Now he doesn't even prompt Claude directly. He writes loops — automated workflows that prompt Claude and figure out what to build next. His job shifted from writing code to orchestrating agents."
    → 支撑主张：Cherny 在 2026-06-02 访谈中陈述了"loops 替我提示 Claude、我的工作变成写 loops"这一工作流转变——即 loop engineering 词源事件的内容本体。
  - "Right now, this is just the golden age of the generalist. People that want to do more than one thing — it's never been more fun."（此句为 WorkOS 以引号标出的 Cherny 逐字原话）
    → 支撑主张：同场访谈中 Cherny 对人类角色的判断。
  - 注意：**WorkOS 回顾全文没有出现 "My job is to write the loops" 这句逐字原话**——该名句的所有流传版本均为二手转述。

**转引版本对照**（"写循环"名句的三个流传版本，措辞互不一致，故逐字不可定）：
| 来源 | 版本 |
|---|---|
| Addy Osmani 博客 2026-06-07（最近时 KOL 转引，注明引自己推文源 x.com/rohanpaul_ai/status/2063289804708835412，该推时间戳解码为 2026-06-06 23:59 CST） | "I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops". |
| 36kr/新智元英译（2026-06-22，二手） | "I no longer write prompts for Claude. It's the loops that are running. They are prompting Claude and figuring out what to do on their own. My job is to write the loops." |
| Pebblous 综述（二手） | "I don't prompt Claude anymore. There are loops running, and it's the loops that prompt Claude and decide what to do. My job is to write the loops." |

→ **结论：该句的逐字原文锁在视频里，未取得。三个版本的意思一致（loops 替他提示 Claude、他只写 loops），但任何一版都不能当逐字引句入册。**

#### 1b. 深度替代材料（一手 transcript，已取得）

**一手源记录 A3**：YC Lightcone《Inside Claude Code With Its Creator Boris Cherny》
- URL: https://www.ycombinator.com/library/NJ-inside-claude-code-with-its-creator-boris-cherny （页面内嵌官方完整 transcript；YouTube ID `PQU9o_5rHC4`，时长约 50 分钟）
- 作者：Boris Cherny（受访）/ Y Combinator（Lightcone 系列，页面元数据 created_at 2026-02-17）
- 发布日期：2026-02-17
- 访问日期：2026-09-26
- 逐字引句（官方自动 transcript，含口语不流畅与转写错误如 "quad"=Claude，引时保留原样、节略处以 [...] 标注）：
  - "Probably the single, for me, biggest principle in product is latent demand."
    → 支撑主张：Claude Code 的产品方法论根基是潜伏需求（用户已在做的事产品化）——loop 原语同理是既有实践的产品化。
  - "you can build for the model and then you can build scaffolding around the model in order to improve performance a little bit. [...] you can improve performance maybe 10, 20%, something like that. And then essentially the gain is wiped out with the next model."
    → 支撑主张：Cherny 的核心工程哲学——围绕模型搭的脚手架收益有限且随模型升级归零。
  - "really I think that's why we stayed in the CLI is because we felt there is no UI we could build that would still be relevant in six months because the model was improving so quickly."
    → 支撑主张：terminal/bash 范式的理由（任务书里点名要核的"terminal/bash 范式"）。
  - "the idea is the more general model will always be the more specific model. [...] essentially what it boils down to is never bet against the model."（同场：办公室墙上挂着 framed copy of the bitter lesson）
    → 支撑主张：他对"专门化 scaffolding"的一贯怀疑——与把 loop engineering 当作长期学科的立场存在张力（见 §5）。
  - "I would bet the majority of agents are actually prompted by quad [Claude] today in the form of uh sub agents. [...] And it's just prompted by we call her Mama Claude."
    → 支撑主张：**2026-02 他已在描述"agent 提示 agent"的机制（loop 词源之前的技术本体），且没用 loop 一词**。
  - "our plugins feature was entirely built by a swarm over w over a weekend. It just ran for like a few days. There wasn't really human intervention." + "an engineer on the team just gave uh gave Quad [Claude] a spec and um told Quad to use a Asana board. And then Quad just put up a bunch of tickets on Asana and then spawned a bunch of agents and the agents started picking up tasks."
    → 支撑主张：spec + 看板 + 自动 spawn 的多 agent 闭环在 2026-02 已经是他的日常实践叙事——这是 June"写 loops"陈述的技术底座。
  - "For me personally, it's been a hundred percent for like since Opus four point five. Um I just I uninstalled my IDE. I don't edit a single line of code by hand."
    → 支撑主张：卸载 IDE、100% 由 Claude Code 写码的个人工作流（媒体广泛转述的"删 IDE"事件的一手出处）。

**关键词源发现**：该 2026-02-17 transcript 中 "loop" 一词出现 **0 次**（grep 全文核验）。Cherny 在 2026 年 2 月用 swarm/subagent/spec/Mama Claude 的语言描述同一套机制；"loop" 措辞出现在约 4 个月后的 2026-06-02 访谈里。**"loop" 是后来贴上去的标签，不是他当时的词汇。**

#### 1c. 团队操作定义（非本人，归属须分清）

Claude Code 团队（Cherny 领导）2026-06-30 官方博客给出了产品的操作定义（作者 Delba de Oliveira & Michael Segner，见 §4 交叉记录）。按回源纪律注明：**这是团队文档，不能直接当 Cherny 个人的定义引用。**

### 结论（Cherny）
- 对 loop engineering **无个人书面的操作定义**（词源贡献是一句访谈工作流陈述，碎片级，逐字未核验）。
- 他的真实深度在两处：① 2026-02 YC transcript 里的设计哲学（latent demand / scaffolding 归零 / never bet against the model / CLI 理由）；② 他团队的产品原语 `/goal`、`/loop` 与官方四类循环定义。
- **词源是碎片级的：访谈一句话被社区贴上术语标签**——这正是"词源是热度而非思考"的样本（Cherny 支）。

---

## 2. Peter Steinberger

### 状态：部分回源（词源火花确认为碎片推文、正文未取得；深度替代材料已取得，但其 2025-12 长文立场与 loop 工程相反）

**为什么算 KOL**：OpenClaw 创造者（开源 agent 网关项目；其 heartbeat 机制被 LangChain 官方博客点名引用为事件环范例）；资深工程师（PSPDFKit 创始人、steipete.me 长期技术写作）；2026-02-14 自述加入 OpenAI；其 2026-06 推文获数百万浏览（浏览量为二手转述，见 §7），是术语扩散的第二支火花。

#### 2a. 词源火花（碎片级，正文未取得）

**一手源记录 B1**：X 原帖
- URL: https://x.com/steipete/status/2063697162748260627
- 作者：Peter Steinberger（@steipete）
- 发布日期：**2026-06-08 02:58 CST**（2026-06-07 美国时间；由推文 snowflake ID 解码得出；Pebblous 引用页标注为 2026-06-08，两说同一时刻）
- 访问日期：2026-09-26（X 不可达，正文未取得）
- 存在性证据（全部一手页面的交叉链接）：
  - Osmani 2026-06-07 帖以 "recently said" 链接此 URL 并给出正文引文；
  - LangChain 官方博客 2026-06-16 以 "Steipete" 链接同一 URL；
  - 时间解码：该推 13 分钟后 @weswinder 发出 Osmani 同帖引用的 token 成本回复（2026-06-08 03:11 CST），说明回复串关系吻合。
- **最接近正文的转引**（Osmani 博客 2026-06-07，逐字转录自他的页面）：
  - "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."
    → 支撑主张：Steinberger 的词源主张本体——停止逐轮提示、改为设计提示 agent 的循环。**注意：这是 Osmani 的转引，原推逐字未核验**（中文媒体转译又作"Stop writing prompts for programming agents..."，措辞不同，恰证转述漂移）。

**词源等级判定：碎片级。** 该帖是两句话的祈使句推文，无机制、无停止条件、无失败模式。Steinberger 个人博客（steipete.me）自 2026-02-14 起无新帖，**没有任何 loop engineering 长文**。按 parent 标准，明确记录：**Steinberger 这一支的词源是碎片级的，无深度内容。**

#### 2b. 深度替代材料（一手，已取得）

**一手源记录 B2**：steipete.me《Shipping at Inference-Speed》
- URL: https://steipete.me/posts/2025/shipping-at-inference-speed
- 作者：Peter Steinberger
- 发布日期：2025-12-28（页面标注，18 min 读长文）
- 访问日期：2026-09-26
- 逐字引句：
  - "The simplest form is text, so by default, whatever I wanna build, it starts as CLI. Agents can call it directly and verify output - closing the loop."
    → 支撑主张：他的"闭环"思想的最早一手表述——**可验证输出（CLI 可被 agent 调用并验证）才是闭环的关键**。
  - "I see many folks experimenting with various systems of multi-agent orchestration, emails or automatic task management - so far I don't see much need for this - usually I'm the bottleneck."
    → 支撑主张：**2025-12 的 Steinberger 明确不认同自动编排循环——他认为人自己是瓶颈、需要留在流内迭代**。与 2026-06"设计循环替你提示"的推文构成显著立场演进（或抽象层级变化），是最重要的 nuance。
  - "These days I don't read much code anymore. I watch the stream and sometimes look at key parts [...] most code I don't read."
    → 支撑主张：他的验收方式是"看流"而非逐行 review——与 loop 工程的 checker 分离主张形成对照。
  - "Whatever you build, start with the model and a CLI first."
    → 支撑主张：与 Cherny 的 CLI 哲学同源。

**一手源记录 B3**：steipete.me《OpenClaw, OpenAI and the future》
- URL: https://steipete.me/posts/2026/openclaw
- 作者：Peter Steinberger；发布日期：2026-02-14；访问日期：2026-09-26
- 逐字引句："I'm joining OpenAI to work on bringing agents to everyone. OpenClaw will move to a foundation and stay open and independent."
  → 支撑主张：他的任职与 OpenClaw 归属（一手，替代二手媒体说法）。

**一手源记录 B4**：OpenClaw 官方文档（项目层一手；页面无发布日期标注）
- URL（已取的三页）：
  - https://docs.openclaw.ai/automation/standing-orders
  - https://docs.openclaw.ai/gateway/heartbeat （LangChain 官方博客点名引用的正是此机制）
  - https://docs.openclaw.ai/automation
- 访问日期：2026-09-26
- 逐字引句：
  - "Standing orders grant your agent **permanent operating authority** for defined programs. Instead of prompting the agent for each task, you define programs with clear scope, triggers, and escalation rules, and the agent executes autonomously within those boundaries"（standing orders 页）
    → 支撑主张：**"停止逐任务提示"思想的机构化形态**——他推文的两句话在 OpenClaw 里被做成"常设授权 + 触发器 + 审批门 + 升级规则"四件套。这是他这一支真正的深度所在（产品/文档级，而非文章级）。
  - "Heartbeat is a system-owned automation that runs **periodic agent turns** in the main session so the model can surface anything that needs attention without spamming you."（heartbeat 页）
    → 支撑主张：事件/定时环（Runkle 四环之第 3 环）的一个被 LangChain 官方引用的实现样本。
- 注：文档为项目官方文档，未逐页署名到 Steinberger 个人，按"官方文档"强度入册。

### 结论（Steinberger）
- 无 loop engineering 长文；词源贡献 = 两句话推文（碎片级，逐字未核验）。
- 其深度在工程产物：OpenClaw 的 automation/standing orders/heartbeat 把"设计循环"落成常设基础设施——且带审批门与升级规则（比推文的口号更审慎）。
- 最重要的 nuance：他 2025-12 长文立场（不需要自动编排、人是瓶颈）与 2026-06 推文之间存在未经他自己解释的演进——一手证据，写进 §5。

---

## 3. LangChain / Sydney Runkle

### 状态：已回源（日期 2026-06-16、作者 Sydney Runkle 均属实）

**为什么算 KOL**：LangChain 是主流 agent 框架的厂商，此文发在其官方工程博客；Sydney Runkle 是 LangChain 的 Deep Agents 工程师（deepagents 框架维护者，官方博客多篇作者），本文致谢栏含 CEO Harrison Chase 审阅——机构级背书。

**一手源记录 C1**：《The Art of Loop Engineering》
- URL: https://www.langchain.com/blog/the-art-of-loop-engineering
- 作者：Sydney Runkle（LangChain）
- 发布日期：2026-06-16（页面标注；任务给的日期核实为**属实**）
- 访问日期：2026-09-26
- 逐字引句（每条注明支撑主张）：
  - "The core agent algorithm is simple: give the LLM context and let it call tools in a loop until it's done. This is the most fundamental loop. But it's far from the only loop that powers agents."
    → 支撑主张：**第 1 环 = agent loop（模型调工具直到做完）**——与任务给的"模型调工具直到做完"一致。
  - "The verification loop adds a grader: something that checks the agent's output against a rubric and, if it fails, sends the result back with feedback."
    → 支撑主张：**第 2 环 = verification loop（验证失败打回）**；注意其 grader 是 rubric 评分（可为 deterministic 或 agentic/LLM-judge），不是纯机器停止条件（与 Osmani 的差异，见 §5）。
  - "The event-driven loop connects your agent to your ecosystem. An event fires — a new document lands, a schedule triggers, a webhook arrives — and the agent runs. The agent isn't something you invoke manually; it's a component running continuously inside a larger system."
    → 支撑主张：**第 3 环 = event-driven loop（事件或定时再跑）**。
  - "The hill climbing loop runs an analysis agent over those traces and uses the findings to rewrite the harness with improved configuration."
  - "The key move here is that the return arrow doesn't just loop back to the top — it reaches inside and updates the agent loop directly. Each cycle of the outer loop makes the inner loops more effective."
    → 支撑主张：**第 4 环 = hill-climbing loop（用运行轨迹改 harness）**——四人中唯一把"改 harness 的元循环"纳入 loop engineering 的人。
  - "AI leaders like Steipete, Boris, and Andrej have all arrived at the same conclusion: the potential in agents is in the loops you build around them."
    → 支撑主张：LangChain 官方把 Steinberger/Cherny(Karpathy) 定位为"同结论的先行者"——即承认词源在别人、操作化在此文。
  - 开篇定位："getting agents to do valuable work reliably takes more than just a good model: it requires a carefully designed harness that's fit to a set of tasks." + 引 swyx 的 "loopcraft: the art of stacking loops"（latent.space）为思想来源。
    → 支撑主张：**"叠在 harness 上的多环"这个框架表述属实**（循环栈服务于 harness；swyx 的 stacking 概念是自认源头；swyx 原文未取回，见 §6）。
- 四环汇总表（原文自带的表格）：agent loop（create_agent）/ verification loop（RubricMiddleware）/ event-driven loop（cron、webhooks、Fleet channels）/ hill-climbing loop（LangSmith Engine）——每环配 LangChain 原语。

### 结论（Runkle/LangChain）
- 任务给的日期（2026-06-16）与作者归属（Sydney Runkle）**均属实**。
- 操作定义 = **四环栈**：agent → verification → event-driven → hill-climbing，每环有具体原语与产品映射。这是四人中最完整的操作性定义，也是唯一含"自我改进元循环"的定义。

---

## 4. Addy Osmani

### 状态：已回源（两篇原文全取得；任务给的分层与引句全部逐字核实）

**为什么算 KOL**：其网站自述（一手 bio）："engineering and evangelism leader and a Member of Technical Staff at Anthropic, where he works on Claude Code. He spent over 14 years at Google leading developer experience across Chrome [...] most recently as a Director at Google Cloud AI."；O'Reilly《Agentic Engineering》作者；**loop engineering 这个名字的命名者**（2026-06-07 帖），且被 marmelab 语料与各方媒体广泛引用。

**一手源记录 D1**：《Loop Engineering》（命名篇）
- URL: https://addyosmani.com/blog/loop-engineering/ （Substack 版 https://addyo.substack.com/p/loop-engineering ；Pebblous 引注 Substack 版日期为 2026-06-08，自站日期 2026-06-07——按自站为准，注差异）
- 作者：Addy Osmani
- 发布日期：2026-06-07（页面标注）
- 访问日期：2026-09-26
- 逐字引句：
  - "Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead. A loop here can be thought of a recursive goal where you define a purpose and the AI iterates until complete."
    → 支撑主张：**命名篇的核心定义**（"把自己从提示者位置上换下来"）。
  - "I believe this may be the future of how we work with coding agents."
    → 支撑主张：命名时的立场强度（may be + 下文的 skeptical）。
  - "Loop engineering sits one floor above the harness." （同段把 harness engineering 定义为 "making the environment one single agent runs inside"）
    → 支撑主张：**与 harness engineering 的分层关系**——loop 在 harness 上一层。
  - "A year ago if you wanted a loop you wrote a pile of bash and you maintained that pile forever and it was yours and only yours. Now the pieces just ship inside the products."
    → 支撑主张：**从手写 bash 循环到产品原语的范式转移**（Ralph→原语的叙事在此篇已确立）。
  - "/goal keeps going until a condition you wrote is actually true, and after every turn a separate small model checks whether you are done, so the agent that wrote the code isnt the one grading it."
    → 支撑主张：**/goal 的机制（评估器模型逐轮判定、干活的不给自己打分）**——注意此篇就把 maker/checker 分离讲清了。
  - 五件套+记忆："Automations that go off on a schedule [...] Worktrees [...] Skills [...] Plugins and connectors [...] Sub-agents" + "Then the sixth thing, the memory."
    → 支撑主张：loop 的组成件清单。
  - "Build the loop. But build it like someone who intends to stay the engineer, not just the person who presses go."
    → 支撑主张：他对人的位置的立场（工程主体性不外包）。
  - 同帖逐字转引 Steinberger 推文与 Cherny 名句（见 §2a/§1a 对照表第一行）——**命名篇的触发结构：Cherny 访谈句 + Steinberger 推文 → Osmani 命名**。

**一手源记录 D2**：《Practical Loop Engineering》（操作篇）
- URL: https://addyosmani.com/blog/practical-loop-engineering/ （自述"originally published on my Substack"）
- 作者：Addy Osmani
- 发布日期：2026-08-14（页面标注；任务给的日期核实为**属实**）
- 访问日期：2026-09-26
- 逐字引句：
  - "A loop is an autonomous, self-correcting feedback cycle where an AI agent repeatedly acts, tests its results and adjusts its approach until a specific goal is met"
    → 支撑主张：**任务给的定义句逐字核实属实**（此句在文中是对其 6 月命名篇的自我引用块）。
  - "In Claude Code you have a **goal** primitive, which can drive a single bounded task forward until you've got a particular goal, like a measurable finish line that's been met. And then **loop** reruns on a timer or a fixed interval, so you can use it to kind of schedule changes."
    → 支撑主张：**/goal 与 /loop 两原语的分工**（完成条件 vs 定时重跑）——任务给的分层核心句。
  - "I remember back before we had primitives baked into Claude Code and Codex, loop engineering was heavily about setting up your own bash loop, a hand-rolled thing. That's how I approached it. And you might remember earlier in the year, a number of us were playing around with the Ralph loop by Geoff Huntley."
    → 支撑主张：**任务给的"Ralph bash loop 是原语出现前的手写形态"转述逐字核实属实**（小节标题即 "Before the primitives were primitives"）。
  - "The evaluator sitting behind goal is not that checker, by the way. It doesn't look at the content to see if it's good or bad in any way, shape, or form. All it does is examine the conversation transcript to see if the hard rules you specified have been met."
    → 支撑主张：**/goal 评估器的边界**——它只核 transcript 里的硬规则，不做质量判断（这是 /goal ≠ 独立审查者的重要澄清）。
  - 转引 Claude Code 团队四类循环（turn-based / goal-based / time-based / proactive）——逐字对照官方原文**一致**（见 D3）。
  - "One sub-agent drafts the change. A separate one verifies it."
    → 支撑主张：maker/checker 分离的操作形态。

**一手源记录 D3**（交叉核验件，官方一手）：Claude Code 团队《Loop engineering: Getting started with loops》
- URL: https://claude.com/blog/getting-started-with-loops （Osmani 帖中引的 X 文章 x.com/ClaudeDevs/article/2074208949205881033 的官方博客版）
- 作者：Delba de Oliveira & Michael Segner（页面署名）
- 发布日期：2026-06-30（页面标注）
- 访问日期：2026-09-26
- 逐字引句（与 Osmani 转引逐字一致，确认他引用无误）：
  - "On the Claude Code team, we define loops as agents repeating cycles of work until a stop condition is met."
    → 支撑主张：**Claude Code 官方定义——停止条件是定义核心**。
  - "Every prompt you send starts a manual loop with you directing each turn. Claude gathers context, takes action, checks its work, repeats if needed, and responds. We call this the agentic loop."
    → 支撑主张：**第 1 级 = agentic loop（人每轮写下一句）**。
  - "Each time Claude tries to stop, an evaluator model checks your condition and sends it back to work until the goal is met or a number of turns you define is reached."
    → 支撑主张：**第 2 级 = /goal（完成条件交给评估器打回）**。
  - "For these, you can trigger when Claude runs with /loop, which re-runs a prompt on an interval."
    → 支撑主张：**第 3 级 = /loop（按间隔重跑）**。
  - 官方还有第 4 级 proactive："Triggered by: an event or schedule, with no human in real time."（Osmani 帖同样转引了此级）
    → 支撑主张：**任务给的分层漏了第四级**——完整分层是四级：agentic loop → /goal → /loop(/schedule) → proactive。

**一手源记录 D4**（交叉核验件，官方一手）：Claude Code 官方文档《Keep Claude working toward a goal》
- URL: https://code.claude.com/docs/en/goal
- 发布日期：页面无日期标注；访问日期：2026-09-26
- 逐字引句：
  - "The `/goal` command sets a completion condition and Claude keeps working toward it without you prompting each step. After each turn, a small fast model checks whether the condition holds. If the model judges it not yet met, Claude starts another turn instead of returning control to you."
    → 支撑主张：**/goal 机制与 Osmani/Runkle 叙述一致（官方文档级确认）**。
  - "/goal adds a separate evaluator that checks your condition after every turn, so completion is decided by a fresh model rather than the one doing the work."
    → 支撑主张：评估器与干活模型的分离是产品机制而非比喻。

### 结论（Osmani）
- **命名者 + 主要定义者**：2026-06-07 命名并给出"替代提示者"定义与五件套；2026-08-14 操作化（分层四级、评估器边界、Ralph 谱系、组合模式）。
- 任务给的四项声称（定义句、/goal 与 /loop 分层、评估器打回、Ralph 前形态）**全部逐字核实属实**；唯一修正：分层是**四级**（agentic loop / goal / loop+schedule / proactive），任务给的描述漏了第四级。

---

## 5. 综合：四人的用法是否同指一件事？

### 5.1 共同核心（一手证据）

四人都指向同一核心主张——**"用你设计的系统替代你本人做逐轮提示"**：
- Cherny（转引，逐字未核验）："I don't prompt Claude anymore. [...] My job is to write loops."
- Steinberger（转引，逐字未核验）："You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."
- Osmani（一手）："Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead."
- Runkle（一手）：四环栈的底两环（agent + verification）即此核心，再向外扩两环。
- Claude Code 团队（一手，非四人之一但为 Cherny 团队）："agents repeating cycles of work until a stop condition is met."

**判断：核心层同指一件事**【一手证据（Osmani、Runkle、Claude Code 团队）＋转引佐证（Cherny、Steinberger 两句）】。

### 5.2 实质差异（最重要的产出）

| 维度 | 差异 | 证据等级 |
|---|---|---|
| **① 范围：有没有"改 harness 的元循环"** | Runkle 的第 4 环（hill-climbing："runs an analysis agent over those traces and uses the findings to **rewrite the harness**"）超出其他所有人。Osmani 的分层止于 proactive loop，且把"改 harness"划给下一层的 harness engineering（"Loop engineering sits one floor above the harness"）；Cherny/Steinberger 词源句中根本没有此层。**按 Osmani 的分层，Runkle 的第 4 环不属于 loop engineering**——两人的"loop engineering"外延不一致。 | 一手（两篇原文对照） |
| **② 验证语义：机器停止条件 vs rubric 评分** | Osmani/Claude Code 团队把**机器可核的停止条件**当定义核心（"deterministic criteria, such as number of tests passed or clearing a certain score threshold, are so effective"；且 Osmani 明确 /goal 评估器"doesn't look at the content to see if it's good or bad"）。Runkle 的 verification loop 是 **rubric/LLM-judge**（"Graders can either be deterministic or agentic"）——质量语义强于 Osmani 的硬规则语义。 | 一手 |
| **③ 词源碎片 vs 定义长文** | 两个"词源人物"（Cherny、Steinberger）的贡献都是碎片级（一句访谈句 + 两句话推文），无操作性定义；操作性定义全部来自"定义者"（Osmani 06-07、Runkle 06-16、Claude Code 团队 06-30）。**这个词的词源是热度（两条 viral 碎片），思考（定义与机制）是事后由另外三家补上的**——parent 假设的"词源是热度而非思考"在 Cherny/Steinberger 两支成立。 | 一手（Osmani 命名篇的触发结构本身就是证据：他引的两句话 → 他命名） |
| **④ 人的位置** | 谱系：Cherny 团队哲学 "never bet against the model"（极简、模型优先）→ Steinberger 2025-12 "usually I'm the bottleneck"（人在流内）→ 2026-06 推文（系统替人）→ Osmani "build it like someone who intends to stay the engineer"（人保判断）→ Runkle "Automation doesn't mean removing humans from the loop"（每环设人工点）→ OpenClaw standing orders（approval gates + escalation rules）。**从"人是瓶颈"到"人设边界"的光谱**。 | 一手（各原文） |
| **⑤ 与 Cherny 团队自身哲学的张力** | Cherny 2026-02："scaffolding 收益 10-20% 且被下个模型抹掉"、"assume that whatever the scaffolding is, it's just tech debt"。loop 配置也是 scaffolding——若按他的哲学，loop engineering 同样会随模型升级贬值。他在 6 月访谈中是否处理了这个矛盾**无法核验**（视频未取得）。这是留给后续回源的开放问题。 | 一手（YC transcript）＋推断（张力部分） |

### 5.3 时间线（全部一手锚定）

| 日期（CST） | 事件 | 一手锚点 |
|---|---|---|
| 2025-12-28 | Steinberger 长文：CLI 闭环、人是瓶颈（反对自动编排） | steipete.me |
| 2026-02-14 | Steinberger 加入 OpenAI；OpenClaw 移交基金会 | steipete.me |
| 2026-02-17 | Cherny YC Lightcone 深谈（swarm/Mama Claude/删 IDE；**"loop" 零次出现**） | YC 官方 transcript |
| 2026-06-02 | Cherny WorkOS×Acquired 访谈："my job is to write the loops"（逐字未核验） | 视频存在 + WorkOS 回顾 |
| 2026-06-06 23:59 | @rohanpaul_ai 发推转述 Cherny 名句（Osmani 的引用源） | snowflake 解码 + Osmani 链接 |
| 2026-06-08 02:58 | Steinberger 词源推文（逐字未核验） | snowflake 解码 + Osmani/LangChain 双链接 |
| 2026-06-07/08 | **Osmani《Loop Engineering》命名**（自站 06-07 / Substack 06-08） | addyosmani.com |
| 2026-06-16 | **Runkle 四环栈** | langchain.com |
| 2026-06-30 | **Claude Code 团队官方定义（四类循环）** | claude.com |
| 2026-08-14 | Osmani《Practical Loop Engineering》操作化 | addyosmani.com |
| 2026-08-22 | arXiv 2608.21884 灰文献综述（研究级二手）：In June 2026, practitioners began to describe a further level called loop engineering [...] developers design systems that prompt agents for them. These systems start agent runs on a schedule or on repository events and stop them when a machine-checkable condition holds. | arxiv.org |

### 5.4 总判定

**同指一件事（核心层），但不是同一个学科（外延层）**：
- 核心层（系统替人提示 + 验证 + 再跑）：四人一致【一手】。
- 外延层：Runkle ⊋ Osmani（多一个改 harness 的元环）；验证语义（硬规则 vs rubric）不同【一手】。
- 词源与定义的错位：词源 = 两条 viral 碎片（热度）；定义 = Osmani/Runkle/官方三家的事后工程化（思考）【一手】。
- 精确的说法：**"loop engineering" 是 Osmani 给 Cherny/Steinberger 的两条碎片贴的名字，Runkle 和 Claude Code 团队各自扩展出了不同的外延**【推断，基于上述一手证据的时间与引用结构】。

---

## 6. 负结论清单（搜了什么、没找到什么）

1. **Cherny 2026-06-02 访谈视频 transcript 未取得**。搜过："Acquired Unplugged Boris Cherny transcript"、"my job is to write the loops" quote；试过：YouTube RkQQ7WEor7w（不可转录）、WorkOS 回顾（无该逐字句）、The New Stack thenewstack.io/loop-engineering/（正文空截断，未取得）。结论：名句逐字锁在视频里，只有三个互不一致的二手版本（§1a 对照表）。
2. **Steinberger 词源推文正文未取得**。X 直连/oEmbed(publish.twitter.com)/nitter.net/xcancel.com/threadreaderapp.com 在本环境全部超时不可达。已固化：URL、精确时间（snowflake 解码 2026-06-08 02:58 CST）、两个一手页面的交叉链接、Osmani 转引文本。
3. **"0xwhrrari" 身份未定（开放问题）**：LangChain 帖把标注 "Boris" 的链接指向 x.com/0xwhrrari/status/2064804504608887040（解码 2026-06-11 04:18 CST）。该 handle 无法确认是否 Boris Cherny 本人（其通常 handle 与此不符），X 不可达无法核。搜过 "0xwhrrari Boris"（无果）。
4. **Steinberger 无 loop engineering 长文**：steipete.me 全部文章列表核过，最新帖为 2026-02-14。
5. **Cherny 无个人博客/长文谈 loop engineering**：搜索结果中他的深度输出全部是访谈/对谈（YC、WorkOS×Acquired、Station F 等），无个人书面长文。
6. **swyx "loopcraft" 原文未取回**：latent.space/p/ainews-loopcraft-the-art-of-stacking 404（经 latent.space 根域跳转）；仅持有 Runkle 对它的引用句。
7. **Andrew Ng 2026-06-30 公开信原文未取得**：仅 Times of India / storyboard18 / otontechnology / 知乎转述（"three loops" 框架）；Ng 的信不是本次四目标之一，未继续追。
   > ⚠️ **调和注记（2026-09-26 评审轮）**：本条指 **A 路未能从 X 重新抓取**（X 全域不可达）。该文**库内早有一手归档**——[`01_seed_reference/loop_engineering/andrew_ng/raw_ng_x_post_en.md`](../../../../01_seed_reference/loop_engineering/01_advocates/andrew_ng/raw_ng_x_post_en.md)（The Batch 交叉发布全文，sources.md 标"一手·全文完整"），台账 §A 的"一手"标记以此为准，**不受本负结论影响**。
8. **ADTmag 2026-07-01 文章 HTTP 403**（标题确认存在：Loop Engineering Emerges as Developers Put AI Coding Agents on Repeat）。
9. **bianews Steinberger 采访（"闭合环路才是编程Agent的唯一生死线"）HTTP 502**；未取得，原访谈出处不明。
10. **awesome-loop-engineering 的 QUOTES.md / HF dataset resources.jsonl 不可达**（raw.githubusercontent.com 与 huggingface.co 在本环境间歇超时）；该库本身是二手聚合，不入册。
11. **cole-medin-knowledge-base 的 boris-cherny.md 未取**（网络超时；同库 steinberger.md 已取，属二手线索库，正文不入册）。
12. 关键词组合搜过：Boris Cherny loop engineering / steipete loop engineering tweet / 0xwhrrari / Andrew Ng loop engineering open letter / Sydney Runkle LangChain / addyosmani loop engineering / OpenClaw loops docs / Acquired Unplugged transcript 等（Bing 系 web_search）。

---

## 7. 不入册·仅社区情绪（热度佐证，绝不与 KOL 证据并列）

以下内容仅证明"这个词在 2026-06 起有热度与争议"，不作 KOL 证据使用：

- **36kr/新智元**（2026-06-22 中文编译《Claude Code之父删了IDE》：转译 Cherny/Steinberger 引句、Claire Vo "era of managers"、THE HIVE/@Av1dlive 复刻、Reddit 质疑、Simpsons 梗图）——时间线与热度佐证；其英译引句与 Osmani 版措辞不同（§1a 已列）。
- **钛媒体/tmtpost**（2026-06-11《龙虾创始人一条推文引800万人围观》）：推文 800 万浏览的数据点；五组件科普为作者自撰。
- **Times of India / storyboard18 / otontechnology / 知乎**：Andrew Ng 公开信的媒体覆盖。
- **Pebblous**（loop-engineering/en/）：2026 年科普综述——正文二手，但其 References 表是本次回源的关键线索源（已据其 URL 回源到一手并全部重新核验）。
- **cole-medin-knowledge-base**（实体卡）：教育者 Cole Medin 的视频笔记，含 "infinite budget like Peter" 的 token 经济吐槽——社区情绪，非 KOL 原文。
- **ADTmag（403）/ The Register / VentureBeat / exawizards（日）/ 121watt（德）/ businessinsider.de（德）/ c114 / 腾讯云社区 / 36kr 德文版**：媒体聚合覆盖。
- **aibuilderclub（Loops or Graphs）/ 36kr《Loop Era 已死?》**：Steinberger 2026 年中后期转向"graph engineering"的后续推文报道——碎片推文 ×2，未回源。
- **blakecrosley / qualixar / dev.to / dutstartupstartup.ai 等**：社区分析与评论。
- **arXiv 2608.21884**（2026-08-22）：研究级二手（灰文献综述），在 §5.3 用作时间线与"共识定义"的学术佐证，不入册为 KOL 证据。

---

## 8. 证据强度总表

| 人物 | 词源火花 | 逐字状态 | 深度一手材料 | 状态 |
|---|---|---|---|---|
| Boris Cherny | 2026-06-02 访谈句 | 未核验（视频无 transcript；三版本不一致） | YC Lightcone transcript 2026-02-17（官方全文）＋团队博客/docs 2026-06-30 | **部分回源** |
| Peter Steinberger | 2026-06-08 02:58 CST 推文（两句话） | 未核验（X 不可达；Osmani 转引最接近） | steipete.me 两长文（2025-12-28/2026-02-14）＋ OpenClaw 官方 docs | **部分回源** |
| LangChain / Sydney Runkle | 《The Art of Loop Engineering》2026-06-16 | **已核验**（全文取得） | 即该文（四环栈+原语映射） | **已回源** |
| Addy Osmani | 《Loop Engineering》2026-06-07（命名篇）＋《Practical Loop Engineering》2026-08-14 | **已核验**（两篇全文取得；对官方文章的转引逐字比对一致） | 即此两篇＋交叉核验的 Claude 官方博客与 docs | **已回源** |


---

## 补充回源（2026-09-26 晚 · 父代理直取，HTTP 200 全文）

> Osmani 两篇原文由父代理直接取得（A 路子代理当时已回源全文；本节为第三轮内容评审后的**终审补充**，逐字句用于替换此前无锚的转述）。出处与日期以页面为准。

### 《Loop Engineering》命名篇（addyosmani.com/blog/loop-engineering/，2026-06-07）

- 定义句："Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead."
- 分层句："Loop engineering sits one floor above the harness."
- **Steinberger 推文逐字（经本帖转引）**："You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."
- **Cherny 语逐字（经 rohanpaul 推文转引，本帖收录）**："I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops"
- /goal 机制句："a separate small model checks whether you are done, so the agent that wrote the code isnt the one grading it"；"the maker and checker split applied to the stop condition itself"
- 判断力警告句："Designing the loop is the cure when you do it with judgement and the accelerant when you do it to avoid thinking"
- **bio（身份与书名裁决依据）**："a Member of Technical Staff at Anthropic, where he works on Claude Code. He spent over 14 years at Google…most recently as a Director at Google Cloud AI"；书名《**Agentic Engineering**》（O'Reilly，官网链接可证）

### 《Practical Loop Engineering》操作篇（addyosmani.com/blog/practical-loop-engineering/，2026-08-14）

- 定义句（块引）："A loop is an autonomous, self-correcting feedback cycle where an AI agent repeatedly acts, tests its results and adjusts its approach until a specific goal is met"
- **含糊目标警告（此前被误并成"品味一起交出去"一句）**："a vague goal would be 'keep going until this UI design is good'. What does that mean? Good to who? How is it being evaluated? Tasks that require human taste, subjective design, or open-ended creative exploration aren't a good fit."
- **品味委托警告**："check yourself, that you are not delegating the taste and the judgment to your agent. You're delegating the task, and then you are actually checking back that it's meeting your bar."
- 评估器澄清（与 §8 强度总表互证）："The evaluator sitting behind goal is not that checker… It doesn't look at the content to see if it's good or bad in any way, shape, or form. All it does is examine the conversation transcript to see if the hard rules you specified have been met."
- **实战 /goal 全例（含全部要素）**："/goal Refactor the data-fetching layer in Dashboard.tsx until Lighthouse performance score is >= 92 and LCP is under 1.8s as shown by the Lighthouse CLI output. Do not change the public API of any hooks. Each turn must improve at least one reported metric; abort if two consecutive turns show no improvement. Stop after 10 turns."
- 细则："Recurring loops expire seven days after creation… loops are session-scoped"；空转判据："same command being tried over and over without any change in the result… a third time with no change from the second and it's probably time to stop"

### 本补充裁决/解决的三个悬案

1. **书名矛盾**：《Agentic Engineering》正确（O'Reilly 链接实锤）；evidence-c:57 的《Beyond Vibe Coding》为误。
2. **此前无锚的"品味警告"**：真实原文为上述两句（含糊目标＋品味委托）；台账/时间线/manual 中旧转述（"停止条件含糊、或把品味一起交出去，这套做法会出问题"）系姊妹仓 FAQ 15 的合并式转述，与原文有出入——各处已按逐字替换。
3. **Steinberger 推文正文**：经 Osmani 06-07 帖逐字转引（上列）——从"未取得"升级为"有日期转引"，直接引用须标"经 Osmani 转引"。

---

## 补充回源（2026-09-27 · Osmani 原文实践细节增量）

> 本节只收本轮对两篇 Osmani 原文的新增展开，不重复 §4 已有定义、四级分层、Ralph 谱系、`/goal` evaluator 边界、maker/checker、含糊目标与品味警告。来源仍是 Osmani 本人一手原文；这些内容按**定义 / 建议 / 个人观察 / 示例**分类，不能互相升格。

### D5 · 命名篇的设计清单：五件套 + 记忆脊柱

- 来源：Addy Osmani，《Loop Engineering》，https://addyosmani.com/blog/loop-engineering/，发布日期 2026-06-07，观测日期 2026-09-27。
- 原文关键句："A loop needs five things and then one place to remember stuff."；"The agent forgets, the repo doesnt."。
- 五件套的操作化细节：
  1. **Automations**：按计划运行，用于发现与 triage；
  2. **Worktrees**：并行隔离工作，但作者明确指出 "YOU are still the ceiling"，可运行数量受人的 review bandwidth 限制；
  3. **Skills**：把 intent/context 外置，避免每轮重新推断；
  4. **Plugins / connectors**：插件是 skills/connectors 的分发格式；connectors/MCP 把循环接到 issue tracker、数据库、staging、Slack，并可开 PR、关联 ticket、等待 CI 变绿后通知；
  5. **Sub-agents**：explore / implement / verify 分工；额外 token 只在 second opinion 值得时花；
  6. **Memory**：状态文件、仓库历史或其他外部记忆是跨轮接续的脊柱。
- 最小主张：Osmani 提供的是一份**设计 checklist 和组合建议**，不是 Claude 官方四类 loop taxonomy，也不是所有 loop 的准入条件。

### D6 · 命名篇的串联示例：从发现到次日恢复

- Osmani 的示例链：每日 automation 读取 CI failures、open issues、recent commits，写入 Markdown/Linear 状态；每个 finding 开隔离 worktree；sub-agent 起草；第二个 agent 依据 skills/tests review；connector 开 PR、更新 ticket；状态文件成为 spine，次日从中恢复。
- 证据性质：**作者建议/示例**，不是他对行业采用率或效果的实证证明。
- 可供后续研究的问题：这种链条是否真正覆盖“候选→授权→在途→阻塞→验收→完成”，尤其在多 feature、并发和优先级变化时如何保持可见性。

### D7 · 命名篇的风险与人的位置

- 原文关键句："a loop running unattended is also a loop making mistakes unattended"；"done is a claim and not a proof"。
- 原文还警告 comprehension debt 与 cognitive surrender 会随着平滑循环加速；直接 prompt 仍然有效，需要平衡自动循环与人工理解。
- 最小主张：Osmani 个人明确把**无人值守错误、完成声明不等于证明、理解债务和认知让渡（cognitive surrender）**视为循环的风险；这应进入反例/风险材料，不应被改写成“loop 一定失控”或“必须人工逐轮”。

### D8 · 操作篇的个人规模与任务适配观察

- 来源：Addy Osmani，《Practical Loop Engineering》，https://addyosmani.com/blog/practical-loop-engineering/，发布日期 2026-08-14，观测日期 2026-09-27。
- 个人实践观察：每日约运行 5–10 个 agents，通常最多约 5 个并发；文档、覆盖率等安全任务可完全委派；auth/security/finance、接触敏感系统，或复杂且 spec/stop 仍可能漏项的任务需要密切观察。
- 证据性质：**个人规模与风险经验**，不是通用并发上限、风险分档或量化自主度标准。

### D9 · 官方四类模式的选型语义与组合

- Osmani 转引并对照 Claude Code 官方四类循环时，分类不只是“自主度等级”，还同时包含 trigger、stop、primitive、task fit；原文明确："Not all tasks require complex loops; start with the simplest solution and use these patterns selectively."
- 组合建议：`/loop` 做 heartbeat/discovery，`/goal` 做单问题闭环；示例是 `/loop every 24h ... if bug exists, use /goal ... until all local tests pass and push branch`；进一步可组合 `/schedule`、`/goal`、skills、dynamic workflows 与 auto mode，再用 adversarial judge 评审多个 worktree 方案。
- 最小主张：这是**组合与选型建议**。`/goal` 是单个 bounded task 的循环，并不要求一个外层 scheduler 才能成立；因此“外层调度”是常见扩展/控制问题，不应被回写成 Osmani 核心定义的必要条件。

### D10 · verification skill 示例与生命周期边界

- Osmani 的 verification skill 示例要求：UI 变化不能仅凭 edit 成功宣告完成；要启动 dev server、进行浏览器真实交互、保存前后截图、确认 console 没有新增错误/警告，并可用 Chrome DevTools MCP 检查 performance/Core Web Vitals；失败后修复，再从步骤 1 重跑。
- 证据性质：**作者建议/示范模板**，不能当作 `/goal` evaluator 已具备的内容质量判断能力。`/goal` evaluator 仍只核 transcript hard rules；真正的质量 verification 由 skill、独立 checker 或人完成。
- 生命周期 nuance：本机 `/loop` 是 session-scoped，关机停止；resume/continue 可在 7-day window 内恢复；跨 session 需要 cloud `/schedule`。这使“循环存在”与“循环能否跨会话持久接续”成为两个不同问题。
- 另一个 triage 示例：贡献指南明确不收 translations，可作为定时任务的可核 stopping condition；这属于作者工作流实例。

### D11 · 自主度与编排是两轴（2026-09-30 增量回源）

- 来源：Addy Osmani，《Agentic Autonomy Levels》，https://addyosmani.com/blog/agentic-autonomy-levels/，发布日期 2026-07-02；本轮观测 2026-09-30（作者个人一手文章，不是效果试验）。
- 原文："almost every autonomy debate I’ve seen conflates two questions that should be separated: **how far away from yourself are we letting this single agent go, and what is our skill at coordinating many agents?**"；"To capture these two dimensions separately, we’ll use two axes: **agency and orchestration**."
- 结构：agency 轴按单代理允许多远走；orchestration 轴按多少代理参与、谁协调。文章把 manager agent 唤醒并持续验证描为前沿形态，但同时指出单一阶梯不足以定位多代理能力。
- 最小主张：能用来校验 [`capability_ladder/00-map`](../capability_ladder/00-map.md) 的教学轴——多主体编排不必排列在定时/事件触发**之后**；不能由该文证明任何具体支线已通用成熟。与 D9 的“按任务组合和选型”同向。

### 本节的判读边界

- **定义**：Osmani 的核心句、`loop` 作为替代逐轮提示的系统、以及其与 harness 的层次关系，见 §4。
- **建议**：五件套、状态 spine、组合模式、verification skill 和“最简方案优先”，见本节 D5–D10。
- **个人观察**：每日 agent 数量、并发量、任务风险分类，见 D8。
- **不能推出**：不能从这些文章推出行业采用率、五件套的普遍必要性、5 个并发是安全阈值、`/goal` 能判断内容质量，或所有 loop 都必须具备外层调度。
