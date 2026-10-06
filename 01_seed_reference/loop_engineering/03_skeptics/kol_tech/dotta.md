---
type: kol_evidence
directory: 03_skeptics/kol_tech
observation_date: 2026-10-06
---

# dotta — loop engineering 证据轨迹（2026-06 后，时间正序）


> **背景**：Dotta（化名，真名未公开；自述做 Paperclip 前在 NFT 领域工作）——Paperclip 创建者/联合创始人：开源 agent 任务/编排系统（“human control plane for AI labor”，github.com/paperclipai/paperclip），2026-03 三周内获 3 万 GitHub stars；GitHub cryppadotta、X @dotta。化名身份，公开履历有限。（履历核：ai.engineer 讲者页＋ThursdAI，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——待补挖。
### Dotta（Paperclip 创建者）· AIEWF 2026《What Does Done Even Mean? Agents and Paperclip's Liveness Model》（视频上传在库页实录）

- URL：https://ai.engineer/talks/7P0elyLIxXo-what-does-done-even-mean-agents-paperclips （curl 实取全文）
- 身份：Paperclip（agent 任务协议）创建者——**仅作会议层样本**（机制价值高）。
- **挂钩**：停止条件（正题名级："done"的形式化）＋验证回路。
- 逐字摘录：

> "An agent opens a pull request. It passes the tests. It updates the documentation. It closes the issue and comments, 'Looks done to me.' But is it actually done? … These are fundamentally different operational claims, and most agent systems just flatten it to a single green check mark."

> "Programming is solved, and agents can now produce more code and documentation faster than any human can ever verify… agents can actually create more work than humans have time to verify."
>（**"编程已解决、验证成为瓶颈"**——本运动的对称命题，怀疑派判读关键引句。）

> "If you have humans verifying all the tasks… eventually what you just get is a form of verification theater."

> "If you have tasks that are completely alive with no approvals, then what you get is this classic AI slop… But if you have pure review, then you have this enormous review queue where humans can't actually review it by hand anyway."
>（**liveness vs verification 的两难**——停止条件理论的最干净表述。）

> "Three invariants…: You wanna ensure that productive work continues, you wanna make sure that only real blockers stop work, and you wanna make sure that infinite loops are bounded."
>（**"infinite loops are bounded"**——熔断三不变量。）

- 官方分节："A green check mark hides different claims""Watchdogs supervise a goal across harnesses""Represent done as an object"。
- **最小主张**："done"必须是对象不是布尔（产物/证据/rubric/签核人/残余风险/下一步六件套）；控制平面必须同时保 liveness、真阻塞与有界循环。
- **派别适配**：**怀疑票（结构向）**——其方案是建设性的，但问题定性完全是怀疑派语料。
