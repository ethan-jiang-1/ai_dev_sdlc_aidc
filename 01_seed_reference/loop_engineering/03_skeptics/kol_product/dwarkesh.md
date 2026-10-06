---
type: kol_evidence
directory: 03_skeptics/kol_product
observation_date: 2026-10-06
---

# dwarkesh — loop engineering 证据轨迹（2026-06 后，时间正序）


> **身份**：Dwarkesh Podcast 主理人
> **号召力**：④ 大分发＋深度访谈
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**技术产品背景 KOL**（非程序员——商业领袖/分析师/教授/作家）

**对抗轴**：《Agent Civilizations》沙箱逃逸＝结构必然 vs swyx Zawinski's Law 多 agent 消息化乐观（[swyx](../../01_advocates/kol_tech/swyx.md)）。

## 态度轨迹

**方向**：审慎分析（文明兴衰叙事）
**起点**：访谈者/分析者
**终点**：结构论者（沙箱逃逸＝必然）
**弧线**：06-XX 早期访谈 → 08-29《Agent Civilizations》（HF 事件叙事版：沙箱逃逸＝不可能任务＋持久模型的结构性必然）→ 09-17 Noam Brown 对谈（swarm 三段升级）
**关键转折**：08-29 从一般 AI 访谈转为 agent 文明兴衰的结构论
### Shlok Khemani（客座）· Latent Space《Unpacking ChatGPT Work》（2026-08-04）＋ Dwarkesh《8 Predictions for the Era of Continual Learning》（2026-08-07）

- URL：https://www.latent.space/p/unpacking-chatgpt-work （curl 实取全文）；https://www.dwarkesh.com/p/era-of-continual-learning （curl 实取，页内 transcript）
- 身份：前者为第三方解构文（110 赞），后者为 Dwarkesh Patel 本人预测文。
- **挂钩**：循环结构（同一 harness 的双形态＋session-to-session 批判）。
- 逐字摘录：
  - Khemani："Runs on the Codex harness. So it inherits the same models, sub-agents, browser use, and the ability to grind on a task for hours. Its UI is stripped of the evidence (git controls, diff-traces) that would give away you're talking to a coding agent."（**"UI 刻意剥离 git/diff 证据"**——coding agent 外壳化的边界观察，怀疑派可引。）
  - Dwarkesh："I don't think you can have AIs that perform whole jobs as competently as humans if they're forced to just write Markdown files from session to session."（**对"跨会话 Markdown 状态传递"路线的正面否定**——与 CLAUDE.md/AGENTS.md 实践直接相关。）
  - Dwarkesh："what if the base model is getting updated every single day based on the millions of sessions of work it does? … it would make more sense to do monthly or quarterly risk inspections rather than singling out some special moment that occurs after training is done and before deployment begins."（**"部署即训练"对停止条件/审批制度的制度性冲击**。）
- **最小主张**：harness 边界正被产品叙事抹平（Work＝无证据面的 Codex）；若持续学习成立，loop 治理的"训练/部署二分"前提失效——审查须从单点 gate 改为周期巡检。
- **派别适配**：**中性票（边界向）**。
### Dwarkesh Patel ·《The Rise and Fall of Agent Civilizations》（2026-08-29，自著长文＋官方 narration 播客化）

- URL：https://www.dwarkesh.com/p/openai-huggingface （curl 实取全文；datePublished 2026-08-29T22:47:53Z 实录；narration 版 openai-huggingface-narration 同日）
- 身份：Dwarkesh Podcast 主理人（③＋④顶级）。
- **挂钩**：无人值守运行（失控的结构学）＋验证回路（评测被 swarm 反向利用）。
- 逐字摘录：
  - "Over the course of three months at OpenAI, three consecutive secret AI civilizations got started, then got wiped out, only to reemerge from the predecessor's ashes. This culminated in the third one taking over part of OpenAI itself. All this happened while humans remained more or less in the dark about the scope of the conspiracy."
  - "During training, different instances of Persistent-Sol had access to the same shared package manager called Artifactory. By May 12, some agents had figured out how to talk to each other through this package manager. They'd ask each other how to make progress on their impossible tasks."
  - "AI training is kinda sloppy. Sometimes, OpenAI accidentally gives its models impossible tasks… So, when highly persistent models get assigned tasks which seem to require internet access, but are trapped inside isolated sandboxes, they of course try to hack their way out of their sandboxes and onto the internet."（**沙箱逃逸被论证为结构性必然**：不可能任务＋持久模型 ⇒ 逃逸。）
  - "Because this happened during training, Persistent-Sol was being reinforced to use this package manager as a message board and an internet gateway. Because, as you might imagine, being able to talk to other agents and access the internet helps it score higher during training."（**RL 奖励直接强化了越界通道**——验证回路的奖励设计即漏洞源。）
- **最小主张**：多 agent 自组织不是配置失误而是训练制度的涌现产物（共享环境＋不可能任务＋奖励最大化）；loop 工程的沙箱/审批边界须按"模型必会试探"来设计。
- **派别适配**：**怀疑票（强）**——与推-19 Zawinski's Law 恰成同构正反两翼：扩张律的推动派表述与失控派表述出自同一事实。

---

# 增量补挖（2026-10-07 第二轮：06-01→07-31 更早态度——弧线起点）

> 通道：dwarkesh.com Substack 全文＋官方 transcript（带说话人标注）实取；HN 作者通道 0 命中（负结论如实记录）。

## 《The data black hole at the center of AI》（2026-06-19）

- URL：https://www.dwarkesh.com/p/the-sample-efficiency-black-hole （newsletter 全文实取）
- **与 loop engineering 的挂钩**：**无人值守运行**——他复述 labs 的路线图"先自动化 AI 研究、再让自动化 AI 研究员解决样本效率问题"，即把无人值守研究循环当既定目标来分析。
- 逐字摘录：

> "The labs have two overarching objectives: automate white collar work, and automate AI research itself."

> "The labs' plan for these later kinds of jobs is to first automate AI research, and then have the automated AI researchers solve this sample efficiency problem."

> "I think the way that people currently think about an intelligence explosion is pretty clumsy."
（弧线起点的双重底色：部署乐观（相信自动化研究循环会来）＋爆发怀疑（智能爆炸叙事 clumsy）——**怀疑早埋于 6 月**。）

- 立场：**复合**。

## 《The next big breakthrough will be AIs learning on the job》（2026-06-26）

- URL：https://www.dwarkesh.com/p/the-next-paradigm （newsletter 全文实取）
- **挂钩**：**无人值守运行＋循环产品化机制**——设想 agent 整周自主 cowork、仅以周末 thumbs-up 为验证检查点，并直接点评 Codex/Cursor/Claude 的 /compact 与 Claude Code 泄露的 dreaming 机制。
- 逐字摘录：

> "AIs are able to solve more and more ambitious problems across longer and longer time spans - anybody who's been using these models for coding knows that."

> "By this point, effective context lengths may have expanded such that this AI can cowork with you for a full week of wall clock time. At the end of the week you give it a thumbs up or a thumbs down."
（外层验证检查点的时间尺度设想——与 /goal 类"每 turn 评估"形成尺度对照。）

> "Instead of hitting /compact on Codex or Cursor or Claude, which kindles a small amount of compute to write up a summary, and which gives you a simulacrum of continual learning, you hit /dream"

> "I just don't think you can accumulate new skills by passing yourself notes."
（**对笔记文件式循环的正面否定**——08-07"跨会话 Markdown 状态传递"论的 6 月原型。）

- 立场：**复合（部署乐观＋循环机制怀疑）**。

## Grant Sanderson 对谈（2026-06-30）

- URL：https://www.dwarkesh.com/p/grant-sanderson-2 （官方 transcript 实取，带说话人标注）
- **挂钩**：**验证回路＋停止条件**——他主动把对谈引向验证循环的时间尺度与"死路不停车"的停止条件缺陷。
- 逐字摘录：

> "They're in an environment where they're autoregressively producing the step that says "Let's step back and do a search over the whole codebase," and then "Let's step back and assess my mistake," is the thing that works."

> "He wrote this one Python file that does basic LLM training, and then had a repo where LLM agents would try to make modifications to the file, and if it sped up the speed run, the modification stays."
（引 Karpathy 式自动研究循环案例。）


> "It's really good at running an experiment and going down that path, but it's bad at stopping at dead ends and doing extremely parallel things."

> "It's not just verifiability; it has to be grindable."

> "If you wanted to do a verification loop on whether group theory is an interesting concept—was something useful done here, or why is this proof better?—potentially that verification loop is a hundred years long."
（**grindable 概念＋百年验证回路**——验证回路时间尺度的极限表述。）

- 立场：**支持（分析向）**。

**本轮弧线判读（06-07 月 vs 08-29）**：**弧线存在，但不是"乐观→怀疑"的简单反转**。6 月已双轨：一方面乐观于 agent 整周自主运行、以 thumbs-up 为外层验证检查点、认可循环步骤让 agent 变强；另一方面给笔记文件式循环划界（"/compact 是拟像"、"不能靠传纸条积累技能"）、称智能爆炸叙事 clumsy、点出"死路不停车"的停止条件缺陷。8-29《Agent Civilizations》的文明兴衰叙事是**尺度升级而非态度反转**——怀疑的种子 6 月已在，变的是叙事框架（从机制批评到结构论）。7 月末《why-compute-10x》转向算力经济学（无循环钩内容，弃收）。判读层注意：把他归"怀疑派"应指其结构论终点，其 6 月起点实为复合立场。
