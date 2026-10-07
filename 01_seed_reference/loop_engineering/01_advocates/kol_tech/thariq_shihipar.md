---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# thariq_shihipar — loop engineering 证据轨迹（2026-06 后，时间正序）


> **背景**：Thariq Shihipar——多伦多大学期间联合创办 Chime（2013 被 HubSpot 收购）→ HubSpot 工程师 → MIT Media Lab 研究生（共同创建开源学术出版平台 PubPub）→ 联合创办 YC 投资的 One More Multiverse；现 Anthropic Claude Code 团队 MTS，Claude Code 的 Ask User Question 工具引入者。（履历核：ai.engineer 讲者页，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——待补挖。
### Thariq Shihipar（Anthropic，Claude Code 团队）· Latent Space《Claude Code's Next Era》（2026-09-29）

- URL：https://www.latent.space/p/thariq （curl 实取，页内官方时间戳逐字稿全文在手）
- 身份：Anthropic Claude Code/agent SDK 一线工程师；在册 Source 系谱内新载体。
- 号召力口径：③＋④（Anthropic 一线＋头部播客）。
- **挂钩**：循环结构（agent loop 原语清单）＋预算与熔断（swarm 预算涌现）＋验证回路（按域分档 effort）。
- 逐字摘录（官方逐字稿层）：
  - "I wasn't exactly sure, like, how the bitter lesson would go, when it comes to, like, harnesses… And now as that's got more abstracted, we have like, Claude managed agents, which lets you have that complexity, but still like… a very bare bones like harness that's scoped to your task."（harness 复杂度被吸收进托管层——bitter lesson 的 harness 版。）
  - "Claude Code is like, has the core things of agent loop which are, have gotten more complicated. It's like, it needs a sandbox to operate safely. It needs auto mode to like make sure like the permissions… it needs computer use and MCPs and like all of these like ways of accessing your data… as the models can do more and more, the core harness has to be like quite complex and very secure."（**厂商自报的 agent loop 核心件清单**：沙箱/auto mode/审批/computer use/MCP。）
  - "they were sandboxed on requests, right? And they wanted to make POST request, and they needed to collaborate on this. And the reason they need to collaborate is because they each have fixed compute budgets… 'Hey, we need more agents collaborating on this task. we need more task budget.'… Swyx: That's the paperclip… Thariq: Yeah. And like that just like comes out from there, right?"（**"task budget" 成为 swarm 的自发诉求**——预算与熔断的新证据形态：模型自己要求加预算。）
  - "I think, like, if you're doing, like, UI or something like that, like low and medium… code review and security should be, like, high or max"（推理档位按域分档：验证域拉满、生成域调低。）
- **最小主张**：harness 走向"核心件复杂化＋界面可变"（Claude Mods/mutable software），agent loop 的原语（沙箱/审批/预算）正被厂商原语化；多 agent swarm 的预算诉求是涌现行为，须在 harness 层预置管控。
- **派别适配**：**推动票（强）**——但 "task budget 涌现"段怀疑派亦可直引。

---

# 增量补挖（2026-10-07 goal 第一批·单点→稳定复核；三时点＋转引链闭合）

> 判定：**单点解除 → 稳定（推动，强）**——07-19 播客 → 07-21 fireside chat → 09-29 Latent Space 同向。

## Behind the Craft 播客（2026-07-19，平台元数据级）

- URL：https://podcasts.apple.com/vn/podcast/how-i-plan-build-and-run-loops-with-claude-code-in/id1736359687?i=1000777426705 ｜ curl 成功
- 官方集描述："Thariq works on the Claude Code team… he showed how to use **/goal** to keep Claude working, how he plans with Claude to remove unknowns before building, and how he runs a team of agents"
（与 Jesse Vincent 08-21 的 Evener /goal 实证互为独立来源——**"库内待核 /goal"两路闭合**。）

## Simon Willison《A Fireside Chat with Cat and Thariq》（2026-07-21，AIEWF 现场对谈转写——一手转写层）

- URL：https://simonwillison.net/2026/Jul/21/cat-and-thariq/ ｜ fetch 成功
- 逐字摘录（Thariq）：

> "For me, it's that **rewrites are now good**… I'm pro-rewriting now… **a codebase is a spec, and maybe it's the only copy of the spec that you have**"

> "there's **a Sonnet classifier** that is judging the tool call and also the context of the conversation"＋"auto mode has to be basically flawless for this to work — it's all downstream of our being an AI safety company."

> **转引链闭合**："the **system prompt for Claude Code has been reduced by 80%** because of Claude Fable… we were over-constraining Claude… fewer hard constraints, more context, and fewer instructions overall."
（McAteer 档案引用句"系统提示词 −80%"的原始出处即此对谈。）

- 同场 Cat Wu（Claude Code PM）强引句："**we are trying to move to a world where humans don't need to be in the loop**… there are baby steps that you take to build up trust with code review."
