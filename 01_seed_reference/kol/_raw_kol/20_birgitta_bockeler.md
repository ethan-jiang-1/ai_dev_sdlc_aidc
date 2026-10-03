---
type: kol_deep_dive
person: Birgitta Böckeler
organization: ThoughtWorks (Exploring Gen AI series)
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html
  - https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html
  - https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html
  - https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
  - https://martinfowler.com/articles/sensors-for-coding-agents.html
key_concepts:
  - guides_and_sensors
  - computational_over_inferential_sensors
  - tdd_in_agent_loop_experiment
  - steering_loop
  - ashby_requisite_variety
---

# Birgitta Böckeler — Harness Engineering 方法论的第一作者：Guides + Sensors

> ThoughtWorks Distinguished Engineer，martinfowler.com《Exploring Gen AI》系列主笔。**Harness Engineering 作为方法论的第一作者**（Fowler 是发布者与背书者，她是定义者）：Guides（前馈）+ Sensors（反馈）矩阵、"计算传感器优于推理传感器"、以及 2026-08 亲自用实验质疑自己的主张——库内罕见的"自我检验型"声音。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。建卡日 2026-10-03（系列五篇 URL/日期已于当日页面核验；她的早期文章 2025-10-15《sdd-3-tools》等谱系背景见 loop 台账 evidence-c，按时间铁律不入轨迹表）。

## 当前立场小结（2026-10-03 建卡）

1. **Guides + Sensors 矩阵**（2026-04-02《Harness Engineering for Coding Agent Users》）：Guides 喂给 agent（前馈）× Sensors 检查输出（反馈），各分 Computational（确定性工具执行）与 Inferential（LLM 解读）两类。
2. **关键发现：计算传感器被低估**——客观质量检查优先用确定性工具（静态分析、类型检查器、测试套件、变异测试），LLM-as-judge 只作补充。
3. **用实验质疑自己**（2026-08-11《TDD inside the agent loop》）："Based on Opus's judgment of the quality of the outcomes, there was **no clearly discernable difference** based on TDD workflow versus no TDD workflow. On the contrary, more than once Opus ranked the non-TDD workflow solutions slightly higher…"（小样本 + 自评判断，作者自列 caveat）
4. **steering-loop 审慎**：与 Fowler 联名警告 "A weak harness means better prompts just produce more sophisticated bugs"。

---

## 思想变迁轨迹（2026）

> 2026-10-03 系列 URL 核实（curl 直抓原页逐篇取标题/日期）：memo（02-17）、harness-engineering（04-02）、context-engineering（02-05）、tdd-in-the-agent-loop（08-11）四篇 ✅；三篇 sensors 文（05-19/05-20/05-27，据早期研究）URL 待回源。

| 日期 | 立场标记 | 锚点 |
|------|---------|------|
| 2026-02-05 | 《Context Engineering for Coding Agents》——系列先声：context engineering 定义（引同事 Bharani Subramaniam："**curating what the model sees so that you get a better result**"）；Instructions vs Guidance 分类；**"Allowing the LLM to decide when to load context is a prerequisite for running agents in an unsupervised way"** | [已核](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) |
| 2026-02-17 | 《Harness Engineering - first thoughts》定义篇（回应 OpenAI 零人写码实验）：**guides and sensors 原创定义**（"This frames the elements of a harness as **guides and sensors**, which may be computational or inferential."）；"Harnesses attempt to **externalise and make explicit what human developer experience brings to the table**, but they can only go so far."；"A good harness should not necessarily aim to fully eliminate human input, but to **direct it to where our input is most important**."；已预演 topology 思路（"teams pick from a set of harnesses for common application topologies"）并指出 OpenAI 原文 "only mentions 'harness' once" | [已核](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html) |
| 2026-04-02 | 《Harness engineering for coding agent users》：Guides + Sensors 完整心智模型——**精确定义**："**Guides (feedforward controls)** - anticipate the agent's behaviour and aim to steer it before it acts. Guides increase the probability that the agent creates good results in the first attempt. **Sensors (feedback controls)** - observe after the agent acts and help it self-correct."；调节分类三件（Maintainability / Architecture fitness / Behaviour harness）；**Ashby 必需多样性定律**作预定义拓扑的论证（"a regulator must have at least as much variety as the system it governs"）；拓扑愿景："a bundle of guides and sensors that **leash** a coding agent to the structure, conventions and tech stack of a topology"（动词用 leash） | [已核](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html) |
| 2026-05-19→27 | 传感器长文 *[Maintainability sensors for coding agents](https://martinfowler.com/articles/sensors-for-coding-agents.html)*——**单篇持续更新（19 May 发布、20/27 两度更新，2026-10-03 页面核验）**，内含 "The test suite as a regression sensor" 等节（早期研究误拆为三篇，已修正） | 页面已核 |
| 2026-08-10/11 | **TDD inside the agent loop**：实验显示 agent 循环内跑 TDD 无可测收益——对自己的主张做实证检验（页标 08-10，另一回源记 08-11——时区/更新差异待统一；Farley 频道 09-23 已出频道级回应，见 `03` 卡归属勘误） | [已核](https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html) |
| （系列延续，日期待核） | 《The role of developer skills in agentic coding》 | [页已核](https://martinfowler.com/articles/exploring-gen-ai/13-role-of-developer-skills.html)，作者/日期待核 |

**判语**：2026 年内她是"方法论从定义走向实证"的唯一样本——别人在表态，她在做实验；08-11 的 null result 是本库"验证口径拉扯"（见 `02` 卡张力线）的第一块实证砖。且 02-17 memo 已预演 04-02 正式文的 topology 思路——她的方法论是**线性生长**的（定义→分类→实例→实证），与 Fowler 的"背书放大"节奏互补。

---

## 与库内其他人物的立场对照

- **Fowler（`02`）**：发布者/背书者关系——他站内推广她的系列并形容"疯狂的流量"；她提供框架，他提供势能。
- **Cherny（`08`）/ Orosz（`12`）9 月守门叙事**：同向——她 5 月的传感器系列就是这个议题的方法论底座。
- **Huntley（`16`）/ Thorsten（`19`）宽自主派**：对立——她的 steering-loop 审慎与"人定义期望状态"立场正面顶住"让模型决定 workflow"。
- **Beck（`05`）TDD 口径**：她的 08-11 实验给了 Beck 的"TDD 超能力"论一记数据侧质疑（注意小样本 caveat）——两条卡必须并读。
- **谱系注意（2026-10-03 细读 Lopopolo field guide 后修正）**：Lopopolo 的 docs/lineage/ 把她的 02-17 memo 定性为对 02-11 OpenAI 文章的 "**[initial memo]** responded through context, deterministic constraints, LLM review, and recurring feedback"，并与 Zhang 并称 "**both … later interpretations of Ryan's essay**"；其 04-02 正式文的 "constrained service topologies" 段（"committing to a topology narrows that space, making a comprehensive harness more achievable"）即经此谱系被引用核验。**谱系争论现状**：Lopopolo 自指 "seminal essay"、GC 官方称他 "coined the term agent harness"（09-25）、她的 memo 曾猜 "harness" 或源自 Mitchell Hashimoto（该猜源说在 Lopopolo 谱系中零回应）——**引用 harness engineering 概念时须注明采用哪条谱系**。

---

## 关键引用汇总

> *"A weak harness means better prompts just produce more sophisticated bugs."* — 与 Fowler 共同警告

> *"There was no clearly discernable difference based on TDD workflow versus no TDD workflow."* — 2026-08-11 实验

> *"Computational sensors are usually preferable to inferential sensors for objective quality checks."* — 矩阵关键发现（转述）

---

**Source:** [TDD inside the agent loop (2026-08-10/11)](https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html) · [Harness Engineering - first thoughts (2026-02-17)](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html) · [Harness engineering for coding agent users (2026-04-02)](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html) · [Context Engineering for Coding Agents (2026-02-05)](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) · [Maintainability sensors for coding agents（持续更新长文，2026-05-19→27）](https://martinfowler.com/articles/sensors-for-coding-agents.html)
