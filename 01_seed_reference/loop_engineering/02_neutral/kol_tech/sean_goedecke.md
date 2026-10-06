---
type: kol_evidence
directory: 02_neutral/kol_tech
observation_date: 2026-10-06
---

# sean_goedecke — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**方向**：稳定审慎（工程方法论持续）
**起点**：审慎（alignment not capability）
**终点**：审慎＋方法论深化（tell agents the why）
**弧线**：五篇窗口内全文：06-01 alignment not capability → 06-08 tightly optimize the dev loop → 07-14 weird projects → 08-XX 测量主义 → 09-27 tell agents the why
**关键转折**：无翻转——持续'人管对齐、agent 管能力'立场，方法论逐步深化
### Source A · Sean Goedecke（Google SWE，seangoedecke.com）· 窗口内五篇一手全文（2026-06-01 → 09-27）

- 通道：curl 直取 atom feed（30 条清单）＋博客分页 6 页逐页核日期；正文 5 篇逐字实取（另有 5-31 篇窗口前相邻票）。
- 身份：Google 软件工程师，个人博客为 AI 工程圈高引用源（本窗口内每月 5-8 篇的稳定发声）。
- 号召力口径：②＋③＋④（被 daily.dev 教程、泰语技术媒体等转译引用；HN 高分发）。
- 逐字摘录（全部实取）：

> "my primary value is not that I help the AI write better code, it's that I align the AI with the values of my organization. Human-AI partnerships are for alignment, not capability."（《Human-AI partnerships are for alignment, not capability》，2026-09-27）
>（同文承认 agent 能力已越过自己："When I ask agents to write code, they make fewer mistakes than I do and are orders of magnitude faster."，同时否定无人值守："Purely vibe-coding at work produces awful outputs. But they're not awful because they're bad code, they're awful because they're in bad taste"，并点名回击 "Vibecoding maximalists like DHH argue that…we ought to stop reading the code…If it were just about capability, they might be right."）

> "There is thus going to be enormous pressure to do agentic coding in languages with fast compilers and tests, like Golang, and to tightly optimize the dev loop in agentic codebases."（《Slow developer experience will bottleneck fast models》，2026-09-14——**把"优化 dev loop"立为下一阶段工程科目**；同文："we may see a return of DevEx in the late 2020s, focused on speeding up the experience for AI agents."）

> "There are lots of just-so stories floating around (like that AI agents prefer statically-typed languages because the feedback loop is tighter), but when you actually measure it seems really unclear which tools agents use better."（《Don't build tools for AI agents》，2026-09-12——对 "X for AI agents" 浪潮的测量主义怀疑，直接点到 feedback loop 叙事）

> "give the agent context on your priorities, not just on the specific task you want them to do."（《Tell agents the why, not just the how》，2026-09-15）

> "This list is a kind of existence proof: a bunch of weird projects, useful to at least some people, that would not have existed without AI assistance."（《Weird projects I shipped with AI》，2026-06-01）

- 窗口前相邻票（不入窗口，注记）：《Build agents, not pipelines》2026-05-31、《Programming (with AI agents) as theory building》2026-04-03、《Prompts are technical debt too》2026-05-20。
- **最小主张**：人机分工的新均衡＝"对齐优先于能力"：agent 出码、人出价值观与 trade-off 排序；loop 的下一个瓶颈是 dev loop 本身的速度。
- **派别适配**：**中性**（对齐派；既反"不读码"极限派、也承认能力反超——两面向都有硬表述）。
