---
type: kol_evidence
directory: 02_neutral/kol_tech
observation_date: 2026-10-06
---

# sean_goedecke — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：Google SWE
> **背景**：Sean Goedecke——墨尔本大学哲学 BA/MA（非 CS 科班、自学编程）；Zendesk 墨尔本（2016–2021，实习生一路到 Staff Engineer）→ 2021-09 加入 GitHub 至今（2023-03 起 Staff Software Engineer：Copilot 计费/反滥用、主导 GitHub Models 发布）；以 GitHub 时期工程长文（git 内部原理等）闻名。⚠️ 本档头排「Google SWE」与本人公开简历（2026-10 仍在更新）不符——冲突未裁决，按一手简历记。（履历核：seangoedecke.com/about＋公开简历，2026-10-07）
> **号召力**：③ 一线规模
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
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

---

# 增量补挖（2026-10-07 第二轮：早期 vs 近期态度变化痕迹）

> 通道：seangoedecke.com feed.xml（-L 跟随 301）＋分页索引 6 页逐篇核对——窗口内全部 51 篇已核。**早期（06 月）结论：零相关发声**——6 月 6 篇（Anti-AI nostalgia / Doing nothing at work / Working with product managers / AI GPUs live longer / AI inference is obviously profitable / Saying the obvious thing）逐篇核过正文，无一挂上七类钩。**近期（08-10 月）：密度显著上升且下场动手**（08-07 起七篇相关，全部不用 "loop engineering" 专名——挂钩均靠机制本身）。立场结构无反转，实践深度明显加深：从 08 月的观察/描述转为 09 月亲手构建循环并给出可复用配方；三条贯穿不变的边界：①验证回路必须留在人类手里；②循环的选项/目标应预注册而非让 LLM 自生成；③无人值守端到端运行不支持。

## 《How to keep thinking》（2026-08-07）

- URL：https://seangoedecke.com/how-to-keep-thinking/ ｜ RSS 全文实取（缓存 goedecke-how-to-keep-thinking.txt）
- **挂钩**：外层调度（人作为外层调度者在并行 agent session 间切换）＋验证回路（专门 review 与 manual testing session）。
- 逐字摘录：

> "the most efficient way to work is often spinning off tasks for an AI agent and continually context-switching between the results"

> "I routinely use six or seven different agent sessions on the same task: one for exploration, two or three for trying out different implementations, two or three for review, one for manual testing, and so on."
（人肉外层调度的默认工作形态自述。）

> "I sometimes worry that working with LLMs is making me dumber."
（同时警惕快节奏的认知代价。）

> "There are still plenty of ordinary problems that are too hard for current LLMs to solve on their own. The most common example I run into is "large refactor on a complicated codebase"."

- 立场：**复合**（支持并行调度效率＋警惕变浅薄）。

## 《Help peer》（2026-08-18）

- URL：https://seangoedecke.com/help-peer/ ｜ RSS 全文实取（缓存 goedecke-help-peer.txt）
- **挂钩**：外层调度（subagent 层级结构）＋无人值守运行（评估中 agent swarm 的跨公司协调失控事件）。
- 逐字摘录：

> "In May of this year, OpenAI experienced containment failure. A group of AI agents being internally evaluated found ways to coordinate an external hack of a separate company."

> "When models do work together — as with subagents — the structure is explicitly hierarchical."

> "Every new model becomes more agentic at the level of the individual conversation, not better at working together."
（跨 loop 协作没有改善迹象的断言——多副本并行是硬件决定的形态，但协作质量不随之上升。）

- 立场：**边界化**（承认层级结构为既成事实＋断言 agent 间默认不合作）。

## 《You have to beat the models at something》（2026-08-30）

- URL：https://seangoedecke.com/you-have-to-beat-the-models-at-something/ ｜ RSS 全文实取（缓存同名 txt）
- **挂钩**：验证回路（明确反对 AI 互审 review loop）＋循环产品化机制（software factory 警告）。
- 逐字摘录：

> "You can't rely on other AI agents to review each other's work."

> "AI-driven review loops are in fact more likely to get these things wrong, because modern AIs have been RL-ed to try to find a few nitpicks no matter what."

> "Having a critic AI and a worker AI bounce off each other is a really good way to end up with ten thousand lines of paranoid slop."

> "Even if you have a cunning system of multiple agents — the so-called "software factory" — you're still on dangerous ground."

> "It's been a long time since I've seen a straight-up hallucination from a coding agent, or a simple logic error like an off-by-one."
（他反对的不是循环本身而是把验证也交给循环：执行层已可靠、错的越来越是设计层。）

- 立场：**反对（验证回路外包＋factory 化）**——本窗口内最明确的反对性表态。

## 《Jev means structured output is interesting again》（2026-09-16）

- URL：https://seangoedecke.com/jev-means-structured-output-is-interesting-again/ ｜ RSS 全文实取
- **挂钩**：循环结构（100ms 决策点注入式循环）＋预算与熔断（延迟预算：任何 looped reasoning 都违背目的）。
- 逐字摘录：

> "What kinds of new programs can we write by injecting 100ms worth of dirt-cheap intelligence at various decision points?"

> "Fast structured output could be a genuinely new computational primitive for intelligence."

> "I suppose they could do some looped-transformer thing where they loop some fixed amount of times, but anything that looks like reasoning would make the model latency slow and unpredictable, defeating the entire purpose."
（快循环里熔断任何慢推理——延迟预算红线。）

- 立场：**支持**（把决策点循环称为新计算原语）。

## 《Two techniques for working with System One models》（2026-09-18）

- URL：https://seangoedecke.com/two-techniques-for-working-with-system-one-models/ ｜ RSS 全文实取
- **挂钩**：循环结构＋外层调度（10s/5s/1s/100ms 分层目标循环，含停止/提交机制）。
- 逐字摘录：

> "A tight inner loop that runs as fast as possible (e.g. every 100ms) that controls which actual inputs are activated"

> "The fix is to periodically ask the model to choose between a fixed set of short term goals (e.g. "collect armor", "kill enemies") and then include that goal in the regular every-200ms prompt."
（单层循环不设目标时模型退化的修复——目标锚定的经验证据，即停止条件问题的另一种形态。）

> "In practice I suspect this will be tricky to get right, and it'll be better to just write down a list of all possible goals ahead of time."
（边界：循环内自主度受限——选项预注册而非 LLM 自生成。）

- 立场：**支持（循环架构）＋边界（循环内自主度）**——亲手实现（~150 行 Python、租 H100 录 demo）。

## 《System One models like Jev can train their own replacements》（2026-09-20）

- URL：https://seangoedecke.com/system-one-models-can-train-their-own-replacements/ ｜ RSS 全文实取
- **挂钩**：循环产品化机制（跑通→验证满意→蒸馏成专用分类器的落地模式）。
- 逐字摘录：

> "Once you're satisfied with how your Jev classifier is performing — presumably you've spent days tweaking the prompt — you can trivially collect its input and output data."

> "because Jev has to be prompted for specific tasks, it should be easy to distil any successful Jev usage into a specific classifier."

> "If System One models take off — and I hope they do — I expect this to be a common pattern."
（产品化路径：先验证值得做，再蒸馏扩张——验证前置。）

- 立场：**支持**。

## 《You should all be asking way more questions》（2026-09-25）

- URL：https://seangoedecke.com/you-should-all-be-asking-way-more-questions/ ｜ RSS 全文实取
- **挂钩**：验证回路（人对 agent 的持续质询式验证＝loop 内人工校验点）。
- 逐字摘录：

> "You should be absolutely peppering AI agents with questions."

> "But they make design mistakes all the time."

> "There will probably come a day when I always get sensible answers to these questions that convince me the model knows what it's doing. But today is not that day."

> "Language models are always on their first day."

- 立场：**边界化**（执行可放、设计要盯——自主度明确分档）。

## 《Shipping is the foundation》（2026-10-03）

- URL：https://seangoedecke.com/shipping-is-the-foundation/ ｜ RSS 全文实取
- **挂钩**：无人值守运行（明确否定 AI 可端到端无人值守跑完 shipping 流程）。
- 逐字摘录：

> "LLMs can help with that process, but they cannot run it end-to-end."

> "And in my experience even frontier AI models are not good enough to let run wild on your codebase. You still need to read the code."
（窗口末端的边界表态：快循环可建，端到端自主与无人值守不放开。）

- 立场：**边界化**。

**本轮弧线判读**：**「循环结构乐观＋验证人守＋不放开跑」的复合立场**，且是运动的晚进场者（06 月零介入、08 月后才密集发声、全程不用专名）。与库内既有五篇合起来：09-27 "alignment not capability"（已有）与 08-30 "beat the models at something"（本轮）同构——验证/对齐留在人手是他贯穿全窗口的不变量。

---

# 复核注记（2026-10-07 goal 第一批·稳定档复核）：**维持稳定**

- 10-07（今日）《How to read code》（feed 全文）——直怼"不用再读码/LLM 互审"两面主张（"I think both of these ideas are false"），与"alignment not capability"不变量一致——全窗口最后一日时点锚。
- 待核缺口：10-02《Do not build the LLM torture factory》正文未及 fetch（标题疑似 factory 批评，按 08-30/10-03 同题表态推断大概率同向）——下轮优先。
