---
type: evidence_archive
collected_by: 主代理直采（web_fetch 全文取得；服务 capability_ladder 阶位升降与界限刻画）
collected_at: 2026-09-30
serves: capability_ladder/{00-map,rung-01..05}
status: 五篇全文逐字取得（S1–S4、S6）；S5 全文取得；S7 正文截断仅脚注转述
quality_bar: 官方 changelog/工程博客/顶会 workshop 在审论文＝一手；Walden/Carlini/Ronacher 为个人作者一手；注意 S5 是 2025-06-13（词源周前一年的机制谱系票）
---

# 回源档案 U：词源周前后 KOL/社区批——阶梯升降票（观测 2026-09-30）

> **任务**：用户要求给 capability_ladder 补 2026-06 之后的高影响力 KOL/社区支撑，并允许分歧、要求清晰界限。
> 本批拿到 **六篇一手＋一篇待补**，直接决定 R4 升格、R3/R1 的官方语义核销、以及全梯的 dissent 边界。

## Source 1 · Armin Ronacher《The Coming Loop》（2026-06-23，词源周后 16 天）

- URL：https://lucumr.pocoo.org/2026/6/23/the-coming-loop/ ｜ 作者：Armin Ronacher（Flask 作者，Pi harness 作者）
- 来源类型：个人一手博客（全文取得）；CC BY-NC 4.0

**逐字摘录**：

- **双层循环的界限（R2↔R3 分界的最清晰表述）**：
  > "There is already an agent loop inside every coding agent. The model calls a tool, incorporates the result, calls another tool, reads a file, edits a file, runs tests, and eventually produces some answer. … The other loop is the harness level loop: the loop outside the agent loop."
- **词源名句第四个流传版本**（evidence-a 三版本对照表需增补）：
  > "I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops." — 引 Boris Cherny
- **R2 判据性质的 nuance（与"机器可核"纪律的张力）**：
  > "The harness just needs some signal that lets it continue. It does not have to be objective or binary, it just has to be useful enough to drive another iteration."
- **循环适用域（R1–R3 的任务边界）**：
  > "They either do not generate new code, but transform code that already exists, or they produce code that intentionally does not have a long shelf life."
  > "loops that produce artifacts without necessity of longevity or that create some form of clearly verifiable mechanical translation matters more than the general ability of a harness to mechanically measure a goal."
- **dissent 主张（放权放大坏品味）**：
  > "If each iteration adds another small defense, the system slowly becomes less understandable while appearing more robust. The more hands-off you are, the more that happens."
  > "present-day hands-off harnesses like Claude Code with ultracode produce worse code than what we were producing last autumn."
  > "It also teaches really bad practices when tools like this are given to juniors without clear guidance."
- **dissent 主张（人的角色与责任）**：
  > "In the harness operated loop I'm not sure what my role even is. Even the 'done' signal loses all meanings … My role is reduced to that of a messenger."
  > "Looping is powerful but it removes responsibility more and more."
- **不可退出（趋势判定的证词）**：
  > "If attackers and reporters loop, defenders will eventually need to loop too to keep up."
  > "the question is not whether we will loop because clearly we will."

**该摘录支持的最小主张**：词源周后头部实践者确认趋势不可逆，同时给出**三条界限**——长寿命代码/品味密集任务不宜全放权；判据只需"足以驱动下一轮"不必二值；人的角色被压缩是真实成本。

## Source 2 · Walden Yan（Cognition）《Multi-Agents: What's Actually Working》（2026-04-22）

- URL：https://cognition.com/blog/multi-agents-working ｜ 前作：《Don't Build Multi-Agents》（2025-06）
- 来源类型：厂商工程博客（一手，全文取得）

**逐字摘录**：

- **R4 共识形态（对多代理的修正票）**：
  > "multi-agent systems work best today when writes stay single-threaded and the additional agents contribute intelligence rather than actions."
  > "The practical shape is map-reduce-and-manage: a manager splits work, children execute, the manager synthesizes and reports back."
  > "We think the unstructured-swarm approach, arbitrary networks of agents negotiating with each other, is mostly a distraction."
- **R4 升阶闸门（可验证性界限）**：
  > "they all share a property most real software doesn't: a simple, verifiable success criterion. Real software requires a system that scales human taste and decision-making."
- **验收分离实证（干净上下文评审）**：
  > "Devin Review catches an average of 2 bugs per PR, of which roughly 58% are severe"
  > "we found this technique to work best when the coding and review agents do not share any context beforehand."
  > "Context Rot is a well-documented phenomenon … With a shorter context, the improved intelligence naturally leads to increased detection of nuanced issues."
- **大小模型分层（"聪明朋友"模式及其失败条件）**：
  > "The cost and speed wins were real, but the quality ceiling was set by the primary, and the primary wasn't strong enough."
  > "The delegation logic becomes a capability router rather than a difficulty escalator."

**该摘录支持的最小主张**：从"反多代理"到"受约束的多代理"的演化本身是 R4 的共识形成过程——**写入保持单线程、其余代理贡献智能而非动作**是当前收敛形态；demo 可行域需要"简单可验证的成败判据"。

## Source 3 · Nicholas Carlini（Anthropic）《Building a C compiler with a team of parallel Claudes》（2026-02-05）

- URL：https://www.anthropic.com/engineering/building-c-compiler ｜ 一手工程博客（全文取得）

**逐字摘录**：

- **R4 变体形态（无编排器的文件锁同步）**：
  > "Claude takes a 'lock' on a task by writing a text file to current_tasks/ … If two agents try to claim the same task, git's synchronization forces the second agent to pick a different one."
  > "I don't use an orchestration agent. Instead, I leave it up to each Claude agent to decide how to act."
- **规模与成本参数**：16 agents；近 2,000 Claude Code sessions；2B input + 140M output tokens；约 $20,000；100k 行编译器可编译 Linux 6.9（x86/ARM/RISC-V）。
- **R2/R4 闸门质量（验证器即方向）**：
  > "it's important that the task verifier is nearly perfect, otherwise Claude will solve the wrong problem."
- **专用角色**：去重 agent、性能 agent、代码质量 agent、文档 agent——"Parallelism also enables specialization."
- **dissent/警示（作者本人）**：
  > "it is easy to see tests pass and assume the job is done, when this is rarely the case."

## Source 4 · Cursor 官方 changelog 两篇（一手，核销 evidence-t §1 Cursor 讹变）

**S4a · Auto-review Run Mode（2026-05-29，Cursor 3.6）**：https://cursor.com/changelog/auto-review
- **R1 三级处置语义（逐字）**：
  > "Auto-review applies to Shell, MCP, and Fetch tool calls. Allowlisted calls run immediately, and calls that can be sandboxed run in the sandbox. All other agent actions go to a classifier subagent that decides whether to allow the call, try a different approach, or ask for your approval."
  > "Auto-review is a new run mode that allows Cursor to work for longer with fewer approval prompts and safer execution."
- 设置路径：Settings > Cursor Settings > Agents > Approvals & Execution；分类子代理可被用户指令 steering。
- **核销记录**：evidence-t §1 "Run Mode/Auto review/Command Allowlist" 三名词**真实存在**（changelog 逐字）；"Run Everything" 未在此页出现（该模式名待 run-modes docs 复核，仍挂 ⏳）；"File Deletion Protection" 未核（⏳）。

**S4b · Shared Canvases and /loop Skill（2026-05-20，Cursor 3.5）**：https://cursor.com/changelog/shared-canvases
- **R3 官方语义（逐字，三种子条件）**：
  > "With /loop, Cursor can run a prompt repeatedly on a local schedule, until a certain outcome is achieved, or until you stop it. If you don't specify a fixed interval, the agent decides when or what event should wake it."
- 注：R3 的授权面证据再＋1（时间/结果/事件三种唤醒条件，与 CC time-based/goal-based 分类同构）。

## Source 5 · Anthropic《How we built our multi-agent research system》（2025-06-13，谱系票）

- URL：https://www.anthropic.com/engineering/multi-agent-research-system ｜ 一手（全文取得）。**词源周前一年**，作 R4 机制谱系票不作"6 月后"票。

**逐字摘录**：
- 架构：> "our architecture uses a multi-agent architecture with an orchestrator-worker pattern, where a lead agent coordinates the process while delegating to specialized subagents that operate in parallel."
- 效果参数：> "outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval"；> "agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats."
- **适用域边界（编码 vs 研究）**：> "most coding tasks involve fewer truly parallelizable tasks than research, and LLM agents are not yet great at coordinating and delegating to other agents in real time."
- **编排尺度规则（参数级）**：> "Simple fact-finding requires just 1 agent with 3-10 tool calls, direct comparisons might need 2-4 subagents with 10-15 calls each, and complex research might use more than 10 subagents with clearly divided responsibilities."
- **失败模式（参数级）**：> "Early agents made errors like spawning 50 subagents for simple queries, scouring the web endlessly for nonexistent sources"
- **R5 惊喜票（agent 改写 harness 自身）**：> "Let agents improve themselves. … it attempts to use the tool and then rewrites the tool description to avoid failures. … resulted in a 40% decrease in task completion time"

## Source 6 · arXiv:2608.21884《Loop Engineering: Building Blocks, Adoption, and Impact》（2026-08-22 v1 / 08-26 v2）

- URL：https://arxiv.org/abs/2608.21884 ｜ 作者：Lulla, Nersesyan, Mohsenimofidi, Treude, Baltes ｜ JAWs@ASE 2026 在审，CC BY 4.0
- 来源类型：**学术综述＋实证挖掘**（共识的最硬形态；摘要逐字，全文待挖）

**摘要逐字**：
- **共识构件清单（与 ladder 五构件高度同构）**：
  > "the emerging gray literature … largely agrees on what a well-engineered loop contains: **triggered agent runs bounded by machine-checkable stop conditions, persistent state files, verifier sub-agents, token budgets, and defined points of escalation to humans**."
- **实证结果**：> "We confirmed the operation of autonomous agent loops in 217 of the 256 repositories our heuristics matched. The repositories commit the configuration around these loops, but almost none commits the state files the discourse prescribes, and the loops' runtime state remains outside version control."
- **研究议程**：> "a planned controlled study of agent autonomy levels and their effect on effort and outcomes."
- **与主题的衔接**：①"triggered runs + machine-checkable stop conditions + escalation points"正是 R1–R3 交接面的学术口径；②"verifier sub-agents"是 R4 的写单线程形态票；③**状态文件不入库**（217/256 确认运行、几乎无 state file 提交）＝跨 feature 可观察性缺口（digested/07 四列）的实证回响；④"autonomy levels"受控研究＝主题"可跟踪预言"的学术对照物。

## Source 7 · Anthropic《The advisor strategy》 ⏳ 待补

- URL：https://claude.com/blog/the-advisor-strategy（2026-06 后；本环境抓取正文截断，仅获导航）
- 机制（转述自 Source 2 脚注 [2]）：让小模型在卡壳时调用大模型——与 Walden "smart friend" 同构的官方形态。日期与正文待补。

## 与 ladder 的对账

| 阶 | 本批变化 |
|---|---|
| R1 | **官方语义落定**（S4a 三级处置逐字）——Cursor 讹变部分核销 |
| R2 | 判据性质 nuance（S1"不必二值"）＋闸门质量实证（S3"verifier 不完美→解错题"） |
| R3 | 官方第二票（S4b /loop 三种唤醒）；人角色成本证词（S1） |
| R4 | **升格票集齐**：Anthropic 编排器-工人（S5）＋Walden 写单线程共识（S2）＋Carlini 文件锁变体（S3）＋视频概念位——建议升正式阶，共识形态＝"写入单线程＋智能旁路" |
| R5 | 第二票挂上（S5"Let agents improve themselves"＋40% 参数）；操作素材仍待缺口 5 搬运——维持候选，票况记入 00-map |

## 不支持什么

- S5/S6 的"效果数字"（90.2%、217/256 等）是**各自评测口径**下的结果，不构成 loop 设计的因果效果证据（P-outcome 缺口照旧）。
- S1 的品味判断（"worse code than last autumn"）是个人经验证词，记 dissent 不记事实主张。
- "90% 开发者"类传播数字本批未获任何佐证。
