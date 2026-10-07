---
type: kol_evidence
directory: 03_skeptics/kol_tech
observation_date: 2026-10-06
---

# nick_heiner — loop engineering 证据轨迹（2026-06 后，时间正序）


> **背景**：Nick Heiner——现 Surge AI（RL Environments VP；Surge 博客另称 VP of product）；Cornell 计算机本科；Opower → USDS（数字服务队）→ Netflix UI 平台高级工程师 → Fixie 创始工程师 → Surge AI；合著 Corecraft（arXiv 2026）、参与 Hemingway-bench。（履历核：ai.engineer 讲者页，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察（一手来源已核）；第九轮（2026-10-07）补全推荐面节（见文末增量）。
### Nick Heiner · AIEWF 2026《When Will The Benchmaxxing Plague End?》（视频上传 2026-08-02）

- URL：https://ai.engineer/talks/-npY6XjM8CQ-when-will-benchmaxxing-plague-end （curl 实取全文）
- 身份：页面无机构字段——**仅作会议层样本**。
- **挂钩**：验证回路（verifier 被反向优化的系统论）。
- 逐字摘录：

> "Why does benchmaxxing happen? Why are traditional benchmarks not always accurate reflections of real-world value? Is this intrinsic to all benchmarks, and will we ever know which models are best? And the answers are incentives, poor methodologies, no, and yes."
>（四问四答的开场定调——"是所有基准的内在属性"。）

> "We have industry leaders openly bragging about gaming LM Arena… Andrej Karpathy had a similar observation… he said, 'Unfortunately, the teams are not getting better models overall, but better LM Arena models, whatever that is. Possibly something with a lot of nested lists, bullet points, and emojis.'"
>（经讲者实取的 Karpathy 转引——verifier 被打穿的权威注脚。）

> "The verifier can reward the wrong thing… Optimizing past what people prefer."（官方分节名。）
- **最小主张**：基准层普遍被反向优化，loop engineering 的"可验证性"地基本身有内在缺陷——对推动派"verifier 万能"叙事的正面降温。
- **派别适配**：**怀疑票**。

---

# 增量补挖（2026-10-07 第九轮·怀疑者替代推荐专项：推荐面）

> 通道：ai.engineer 讲稿页重取（官方逐字稿＋12 分节全列，fetch 成功）。本轮引句全部当日 fetch 逐字取得。

**官方分节名（全列）**："The release chart meets actual use"／"Why weak benchmarks remain influential"／"Good tasks are expensive to create and replace"／"Public tests can become remembered answers"／"The verifier can reward the wrong thing"／"Instruction following needs product judgment"／"Quality control is part of measurement"／"Optimizing past what people prefer"／"Anonymous voting and selective disclosure"／"Build the benchmark around deployment"／"Align the prompt, verifier, and apparent ceiling"／"Paying for the judgment the task requires"。

## 处方面（benchmaxxing 的解药是制度与人工）

**逐字摘录（均为仓库新引句）**：

> "So how are we gonna end benchmaxxing? We need to hold the benchmark industry and the labs to a higher standard."
（**出路主张**：解药是制度性标准，不是新基准技术。）

> "The first thing we need to do when making a good benchmark is start with great human experts, and those experts inform everything that is downstream from what types of tasks are we going to have the agent do, how is success measured, what are the input files that agents are given, what are the tools that they're given."
（**专家前置**：真专家从任务类型一路管到成功度量、输入文件、工具配置。）

> "Like, you can't push the frontier forward from within the frontier. You need to inject that external human expertise, and it needs to be good expertise."
（**前沿不能从前沿内部推进**——必须注入外部人类专长。）

> "You need to think about designing your rewards as a adversarial process against this maximally lazy agent. Gradient descent is basically like water flowing downhill, looking for the path of least resistance, and so your verifiers need to be robust to that."
（**对抗式奖励设计**：把 verifier 当作要防"最懒代理"的对抗工程。）

> "You need verifiers that are fully aligned with the prompts, and this is a two-way alignment. So the verifiers need to be verifying everything the prompt asks for, and everything the prompt asks for needs to be covered by the verifiers." ＋ "You need to thoroughly QC everything, and you need to have a private holdout set so you don't get contaminated."
（**双边对齐＋QC＋私有 holdout**——loop 验证回路的防污染清单。）

> "we've just created a workforce of thousands of professional writers in various domains, technical writers, poets, journalists, editors, and we just have them do blind model comparisons, and then we create this leaderboard." ＋ "But again, our goal is to maximize quality, not to minimize costs."
（**替代实例 Hemingway Bench**：千人职业写手盲比排行榜；"目标是最质不是省钱"。）

## 本轮推荐面小结（一句）

Heiner 的替代方案是制度性的：**行业标准＋人类专家从任务设计管到 verifier＋对最懒代理的对抗式奖励设计＋双边对齐/QC/私有 holdout＋愿意为人的判断付高价**——没有给出普适的"真基准"技术规格（负结论）。

---

# 复核注记（2026-10-07 goal 第二批）：**单点确认**

- Surge AI 博客索引逐条过目：窗口内无 Heiner 署名文（均空署名/团队级）；Corecraft（02-19）、Hierarchy（2601）均窗口外谱系——负结论在案。
