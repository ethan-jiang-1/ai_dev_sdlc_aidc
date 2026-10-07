---
type: kol_evidence
directory: 03_skeptics/kol_tech
observation_date: 2026-10-07
---

# hillel_wayne — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：Computer Things newsletter 作者；TLA+ 教育者／布道者（learntla.com、《Logic for Programmers》）；2026-05 加入 Antithesis
> **背景**：Hillel Wayne——形式化方法（FM）教育领域最有声量的独立作者之一；长期为"工程师可用"的形式化方法布道；2026-05 加入 Antithesis（formally verified 超低延迟基础设施公司）。**第九轮（2026-10-07）新入册。**（履历核：hillelwayne.com，2026-10-07）
> **号召力**：②＋③（FM 社区头部声音；被 Boris Cherny 触发的"FM 救 agentic 软件"热潮的权威降温者）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)（2026-10-07 第九轮入册）
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**方向**：对"形式化方法救 agentic 开发"叙事降温（不反 agent，反神化）
**起点**：LLM 写的 spec 是弱性质（谱系 2026-03-10）→ **终点**：TLA+ 只管低垂果实，别神化（09-30）
**关键转折**：验证回路的上游缺口是**可表达性质**本身

## 《What TLA+ can and can't check》（Computer Things，2026-09-30）

- URL：hillelwayne.com（Computer Things newsletter 2026-09-30）｜ fetch 成功（全文）
- 来源类型：个人一手 newsletter（全文取得）。触发背景：Boris Cherny（已归档）引发的"TLA+ 会解决 agentic 软件问题"热潮——Cherny 只作触发背景不重复立条。
- **挂钩**：⑤验证回路（形式化验证的能力边界）。

**逐字摘录**：

> "As a long-time advocate of level-headedness, this new euphoria worries me. I read a lot of people saying that formal methods will solve the problem of agentic software development once and for all, and that's nonsense."
（**定调**：FM 一劳永逸解决 agentic 软件开发＝无稽之谈。）

> "to verify a property, we need to have a property to verify! So what are the properties that TLA+ can't even express?"
（**验证回路的上游缺口**：得先有性质可验证——TLA+ 连表达都表达不了某些性质。）

> "These are useful hacks, but they're still hacks. Each one takes a lot of cleverness to figure out and comes with serious drawbacks. Auxiliary variables ruin refinements, self-composition exponentiates your state space, etc."
（对补丁式 hack 的批评：辅助变量毁 refinement、自组合指数级膨胀状态空间。）

> "Ultimately TLA+ is pretty good at picking a lot of low hanging fruit- invariants and liveness cover many things we care about... There's a lot of potential (and a lot of pitfalls) in using TLA+ to check vibe code. But there are also many things it cannot even express, let alone check."
（**定位处方**：TLA+ 的正确位置＝invariants/liveness 的低垂果实；有潜力也有坑；很多性质"连表达都做不到，更别说检查"。）

> "You could also use a different tool with a different focus. CTL can do reachability properties, PRISM probabilistic properties, etc."
（**选型处方**：按性质类别选工具——CTL 管 reachability、PRISM 管概率性质。）

## 谱系（窗口前，2026-03-10）

- 《LLMs are bad at vibing specifications》（2026-03-10，fetch 成功）：
> LLM 写的 FM spec "are tautologically true！" ＋ "LLM properties are weak, intended properties need to be strong."
（**弱性质问题**：agent 产出的性质重言为真——恰是验证回路最不需要的那种；谱系标注：窗口前。）

**该条支持的最小主张**：形式化方法对 loop 验证回路是"低垂果实采集器"而非救世主——上游缺口是可表达性质本身；LLM 自产的性质是弱性质；按性质类别选工具（CTL/PRISM 等）。
**派别适配**：**怀疑票（验证叙事降温向）**——注意他本人是 FM 布道者且已加入验证公司 Antithesis：反的是对自家工具的神化，这个"利益反向"结构使票更硬。
