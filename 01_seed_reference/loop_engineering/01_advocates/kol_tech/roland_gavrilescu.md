---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# roland_gavrilescu — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

### Roland Gavrilescu（Introspection 联合创始人，前 xAI agent infra）· AIEWF 2026《The Loop Is the Product》（视频上传 2026-09-26）

- URL：https://ai.engineer/talks/7taOQBfjDyE-loop-is-product （curl 实取全文）
- 身份：Introspection 联创（自述"my co-founder and I were in this mythical place called xAI working hard on agent infra"）。
- 号召力口径：③弱（新创创始人）——**仅作会议层样本，不入册候选**；但其议题名把循环产品化推到正题名级。
- **挂钩**：循环产品化机制（正题名级）＋验证回路＋外层调度。
- 逐字摘录：

> "We've started with everything goes down to RL… We then quickly moved to harnesses and how the model is a commodity and it's all about the harness. And now we're talking about loops and how you should build these loops and not touch code anymore."
>（RL→harness→loop 的三段谱系，会议层口径。）

> "What matters here is the quality of the signal determines the success rate of the loop, and the quality of the verifier is able to calibrate if that success is actually correct or not. But there's another loop here… how do you generate these artifacts at the end of the first loop to then run a second loop on and have a way to continuously improve."
>（信号质量定成功率、verifier 定校准——第二环吃第一环的产物。）

> "Failure patterns should become judges and evals. Repeated behavior should become skills and prompts."
>（循环产物的资产化清单——循环产品化的操作句。）

> "Valued work per watt is how you should measure am I making progress or not."
>（单位能耗有效功＝循环经济学的收口指标。）

- **最小主张**：loop 时代的产品本体是"agent recipe"（可版本化、可移植、含 evals 与人的 taste），循环负责把运行痕迹蒸馏成 recipe。
- **派别适配**：**推动票（会议层）**。

### Roland Gavrilescu（Introspection 联创/CEO，前 xAI）· Latent Space 访谈《Autoresearch: The feedback loop behind self-improving agents》（2026-07-01）

- URL：https://www.latent.space/p/autoresearch-introspection （curl 实取全文）
- 身份：在册（推-7，AIEWF《The Loop Is the Product》）；本条为**同一人的长访谈新载体**，机制表述比会议talk更完整。
- 号召力口径：③弱＋④（会议层样本升级为访谈层样本）。
- **挂钩**：外层调度（inner/outer loop 定义）＋循环产品化机制（agent recipe）＋预算与熔断＋停止条件（自主度渐进）。
- 逐字摘录：
  - "The first is that the loop is the product. We have moved from focusing on models, to harnesses, and now to loops. The key question is whether you can define the right feedback mechanisms so agents can take on more work without generating more slop."（**"不加 slop 的前提下让 agent 接更多活"＝外层调度的核心命题**。）
  - "You can think of the system as having an inner loop and an outer loop. The inner loop is the primary system interacting with users and performing the work. Autoresearch is more concerned with the outer loop: another system that studies and maintains the primary system."（内外环的教科书定义。）
  - "An orchestra might retain a human conductor who controls how the loops operate. A factory implies something more fully autonomous… But you should build toward the factory rather than assume you can create a completely autonomous factory on the first day."（**orchestra/factory 之争被重述为"自主度档位"问题**——与 Charlie Holtz 中-1 对冲。）
  - "During its first few loops, an agent may rely heavily on asking questions and learning what a human would do. Over time, it accumulates those preferences and can become increasingly autonomous. It is similar to an employee joining a new company."（人作为工具/信号源的自主度渐进化。）
  - "The second requirement is control over cost. You do not want to wake up to an unexpected thousand-dollar bill because an agent has been running an inefficient loop."（**"千美元账单"警句＝预算与熔断**，与 Amazon 860% 超支案互证，见怀疑档疑-11。）
  - "Everything is Git-based, and Git becomes the audit log that you maintain over time."
- **最小主张**：autoresearch＝外环研究内环；agent recipe（evals＋judges＋人类专长＋失败史）是循环的可移植资产；自主度按"先问后做"渐进放权，成本控制是建环第二前提。
- **派别适配**：**推动票**。
