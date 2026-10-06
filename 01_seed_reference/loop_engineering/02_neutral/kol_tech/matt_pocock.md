---
type: kol_evidence
directory: 02_neutral/kol_tech
observation_date: 2026-10-06
---

# matt_pocock — loop engineering 证据轨迹（2026-06 后，时间正序）


> **背景**：Matt Pocock——转码前做过 6 年声乐教师；Stately XState core 团队（XState Codegen 作者）→ 2022 Vercel DevRel（参与 Turbopack 发布）；2022-12 起以 Total TypeScript 全职独立教育者，2026 年任 AI Hero Director——产出 AI coding 词典、wayfinder 等 agent skills、Evalite、Sandcastle。（履历核：ai.engineer 讲者页＋Reactiflux 访谈，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——待补挖。
### Matt Pocock · Latent Space 访谈《The /wayfinder Skill: Navigating the "Fog of War" of Planning》（2026-08-20）

- URL：https://www.latent.space/p/wayfinder-skill （curl 实取全文）
- 身份：TypeScript 教育者/AI coding dictionary 作者（③弱——实践者层样本）。
- **挂钩**：外层调度（计划会话的编排层）＋循环结构（map/ticket/session 三文档）。
- 逐字摘录：
  - "What I noticed is I was doing a lot of work with AFK agents [Away From Keyboard] and trying to schedule in a ton of work so that my agents could run virtually overnight… I was finding the planning stage really onerous, because I would have to be constantly thinking about my session management. Like, how many tokens am I into my context window?"
  - "I wanted an orchestrator layer that would basically say, okay, whatever you want to plan, I'm going to handle the planning sessions for you. I'm going to split this out into multiple sessions… And then your specs can be even more detailed, and you can just whack off an AFK agent to go and do tons more work."
  - "One really key idea in wayfinder is the 'fog of war'. So this is the concept of, you can't quite decide everything right at the start… You can make certain decisions, and those certain decisions sort of lead you there and push further out into the fog of war."
  - "Use 'grill me' in cases where you feel like you can plan the whole thing in a single session… For stuff where you don't know the path ahead… use wayfinder."（单环 vs 多环规划的分界判据。）
- **最小主张**：夜间无人值守的瓶颈在**规划阶段的上下文管理**；解法是把规划本身做成多会话编排（map＋ticket 分层），而非把 spec 写满一次。
- **派别适配**：**中性票**。
