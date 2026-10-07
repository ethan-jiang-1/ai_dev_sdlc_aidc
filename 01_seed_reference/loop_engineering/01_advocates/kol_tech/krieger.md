---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# krieger — loop engineering 证据轨迹（2026-06 后，时间正序）

> **背景**：Mike Krieger——圣保罗出生，Stanford 符号系统 BS/MS；Instagram 联合创始人/CTO（2010–2018，与 Kevin Systrom）；后与 Systrom 合作 Rt.live（2020）与 Artifact（2023，售予 Yahoo）；2024-05 加入 Anthropic 任 CPO，2026-01 卸任转入 Labs（与 Ben Mann 共建——AIEWF 现场稿称 Head of Labs）。（履历核：Anthropic 官方公告＋Wikipedia，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——待补挖。
### Mike Krieger（Anthropic 产品/实验室负责人）· AIEWF 与 swyx 对谈（同上 dispatch，2026-07-03 发）

- 身份：Instagram 联合创始人，时任 Anthropic 产品负责人（现场稿称 Head of Labs）。
- 号召力口径：③＋④。
- 逐字（经现场稿转述）：

> "Don't just fix this bug. Now you are responsible for this part of the codebase, and I want you to monitor this feedback channel and proactively take on tasks."

> "That's really changed how we operate currently. It's much more this multiplayer, async, proactive way."
>（对 Claude Tag（其新内部模型）的使用画像：从单点修 bug 到"领养代码块＋监视反馈频道主动领活"——无人值守循环的组织化形态。）

- **难点自认**（同稿）："Most usage is actually much more delegated"，但团队 "bottlenecked on reviews" 且受限于 "human ability to fully conceptualize what we're doing."
- **最小主张**：Anthropic 内部实践即"多人向 agent 系统分派所有权"的早期软件工厂；同时自认 review 与概念化是瓶颈。
- **派别适配**：**推动票（带难点自认）**——自认句同时是怀疑派可引用的材料，判读时两面都要收。

---

# 增量补挖（2026-10-07 goal 第一批·单点→稳定复核＋谨慎注记）

> 判定：**单点解除 → 稳定（推动翼）**；新增"harness 价值暂态化"注记（与 Debois 商品化预言同构，判读两面收）。

## 《How Anthropic Builds: Lessons from Labs》（ai.engineer 官方笔录全文，WF26——同场由现场稿升级）

- URL：https://ai.engineer/talks/qqrk7CtkuIw-anthropic-builds-lessons-from-labs ｜ fetch 成功
- 逐字/官方要点：

> "The newer workflow begins with the desired result: describe the goal, let Claude work, and discuss questions and tradeoffs as they arise."

> 周末 ~20 万行 Python→TypeScript 迁移："It ported the code, verified and double-checked it, read both versions, and repeatedly worked over its output. By Monday… a completed port that worked and was deployable."

> "Delegation produces a review bottleneck… The deeper constraint is whether a human can conceptualize the change at all."＋"he does not read every line of every pull request… Important reviews remain human-driven."

## Sierra Ventures 21st CXO Summit 对谈（2026-09-28 发）

- URL：https://www.sierraventures.com/content/anthropic-mike-krieger ｜ fetch 成功（全文）
- 逐字：

> "You can't hold your product shapes too strongly. You have to hold them lightly because they may just go away over time."

- 要点级（作者转述）：3 月自建 builder＋verifier 脚手架，会前被更新模型裸跑**击败**（"Months of Engineering, Beaten by a Model Out of the Box"）；"Earlier this year, Claude working autonomously for hours was the exception. Now it's common."；审批分流、风险才升级人审。
（**谨慎注记**：自建脚手架被模型进步侵蚀——harness 投资的回报期问题。）
