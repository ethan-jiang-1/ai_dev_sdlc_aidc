# moritz_johner — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

**（第五轮挖掘（2026-10-06）：会议 transcript 全量扫）**

### 中-3 · Moritz Johner · AIEWF 2026《We Gave an Agent Production Code Access and Then Tried to Sleep at Night》（视频上传 2026-07-20）

- URL：https://ai.engineer/talks/LqLoYksJ6do-we-gave-agent-production-code-access-then （curl 实取全文）
- 身份：甲方工程负责人（自述"thousands of repositories"的依赖修补场景）。
- 号召力口径：③弱——**仅作会议层样本**。
- **挂钩**：无人值守运行（风险与控制设计）＋预算与熔断。
- 逐字摘录：

> "InfoSec came around the corner and asked a very reasonable question, 'Is this automation, or is this a supply chain incident waiting to happen?' A useful coding agent is a supply chain actor, whether you plan for that or not. That's the thesis of this talk."
>（"有用的 agent＝供应链行为者"——怀疑派可直接引的定性句。）

> "The CVE remediation agent actually just modifies files in the file system. It doesn't commit, it doesn't push, it doesn't create a PR, it doesn't watch CI itself… And once it's done, it hands back control to the controller, to the deterministic bit."
>（**确定性控制器包住推理 agent**：agent 无提交权、无 PR 权、无 CI 观察权——预算与熔断的教科书式分工。）

- 官方分节："Keep the PR lifecycle outside the agent""Separate application capabilities from agent credentials"。
- **最小主张**：无人值守依赖修补的可行形态＝"boring 外壳＋受限 agent 内核"，PR 生命周期与凭据全部留在 agent 外。
- **派别适配**：**中性票（含强怀疑引句）**。
