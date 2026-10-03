# Evidence Z — Addy Osmani 增量回源（2026-07-15 → 09-14 八篇）＋ 词汇升级

**观测日期**：2026-10-03。**来源**：addyosmani.com 博客逐篇 curl 实取（web_fetch 本轮 DNS 故障，按纪律切换）；3 篇正文逐字核实（07-15 / 07-20 / 08-31），其余 5 篇标题/存在性已核、正文待回源。**性质**：§A `addy_osmani` 行的增量档案；与 [evidence-a](evidence-2026-09-26-a-originators.md)（命名篇 + 操作篇）相接。

---

## 一、八篇清单（窗口 2026-07-15 → 09-14）

| # | 日期 | 标题 | 状态 |
|---|------|------|------|
| 1 | 2026-07-15 | Own the Outer Loop（AI Engineer World's Fair 2026 闭幕 keynote 书面版） | ✅ 正文已核 |
| 2 | 2026-07-20 | Software Factories, Light and Dark | ✅ 正文已核 |
| 3 | 2026-08-31 | Agentic Skill Decay | ✅ 正文已核 |
| 4-8 | 07-15→09-14 窗口内 | Agentic Code Quality / Practical Loop Engineering / Human judgment doesn't leave the software / Audit your Agent files / Brownfield Agentic Engineering | ⏳ 标题与存在性已核，正文待回源 |

URL 模式：`https://addyosmani.com/blog/<slug>/`（slug 按 HTML title 对应）。

## 二、三篇已核引文（逐字）

**07-15 Own the Outer Loop**：
> "Before, our agents were doing the inner loop of the execution loop. Now they run the inner execution loop. **Engineers own the outer loop.**"
> "**The agent can ship more than you can review.**"
> "just enough autonomy as back pressure"（自主度作为背压）

**07-20 Software Factories, Light and Dark**：
> "**A software factory is harnessing loops at scale.** You can run the loop with humans in it (light factory)… Or you can ignore the humans (dark factory)… **But if people stop reading, they'll stop understanding your software.**"
> （该框架依赖 Dex Horthy "Why Software Factories Fail" 演讲——Osmani 一手转介；Dex 演讲本体仍待回源，见 `_raw_people/README.md` 观察名单）

**08-31 Agentic Skill Decay**：
> "**Agents can finish the task without teaching you anything.** Building expertise now has to be deliberate."
> "**A completed task is not necessarily a rep.**"
> 引 Anthropic 2026 Trio 研究：AI 组测验 50% vs 手写组 67%

## 三、词汇升级（台账注记用）

词表从 6 月的 "loop engineering" 升级为：**loop → harness → factory**（07-20 明示三级）；新增 **outer loop / verdict / answerability / light-dark factory / comprehension debt**；自主度四工位 **constraints loop / sampling loop / audit loop / ownership loop**（07-15）。

## 四、对台账的处置建议（2026-10-03）

1. `addy_osmani` §A 行：**主张一句话**增补"07-15→09-14 八篇把词表升级为 loop→harness→factory，外环所有权/裁决（verdict）为中心"；证据强度维持一手。
2. 人物全景卡：`01_seed_reference/voices/_raw_people/` **评估升个人卡**（他同时定义术语＋给操作件，是厂商一线声音；2026-10-03 用户判：增量回源+升格注记，开卡待下一轮定）。
3. 剩余 5 篇正文回源 → ✅ **已完成**（2026-10-03 同日补），见下节 §五。

## 五、剩余五篇回源（2026-10-03 补，§一 表内 ⏳ 行全部闭合）

| # | 日期 | slug（标题） | 关键引文（逐字） |
|---|------|--------------|------------------|
| 4 | 2026-08-08 | agentic-code-quality | "there's just **too much code for anyone to read**." / "more and more of our quality checks have to happen **in the harness, environment, and operating system around the agent**." / "I still read and review code, but am very intentional about **where I am comfortable with constraints as the check**." |
| 5 | 2026-08-21 | human-judgment-doesnt-leave-the-software | "You'll likely need **humans in the loop upfront for deciding on product intent, system design (if you care) and your quality bar**." / "Do review code (lights-on factory) but be intentional with where it's needed the most." / "Aim for quality checks to happen as **early and continuously** as possible." |
| 6 | 2026-08-27 | audit-your-agent-files | "I now run Claude's /doctor every few weeks, review memory separately, and **ask each instruction to earn its place again**."（AGENTS.md/CLAUDE.md/技能文件治理） |
| 7 | 2026-09-14 | brownfield-agentic-engineering | "**the repository is no longer a complete description of how the thing actually behaves.**" / "Institutional knowledge, duct tape, legacy services, and expectations other teams depend on live outside the tree." / "throw them at an older brownfield codebase unsupervised and you may end up with something that 'works' but with **the wrong system design and brittle tests**." |
| — | 2026-08-14 | practical-loop-engineering | 确认与 evidence-a 操作篇**同篇**（不重复建档） |

**闭合说明**：§一 表 8 篇全部有日期与直链；"Human judgment…" 一篇日期定为 08-21。Osmani 增量回源**完成**——八篇词表升级（loop→harness→factory）+ 五个新概念（outer loop / verdict / answerability / light-dark factory / skill decay）证据链完整。
