---
type: kol_evidence
directory: 02_neutral/kol_tech
observation_date: 2026-10-06
---

# kyle_lee — loop engineering 证据轨迹（2026-06 后，时间正序）


> **背景**：Kyle Jaejun Lee——KAIST 毕业；曾任 VESSL AI 工程负责人（推出开源 agent 工具集成/凭证框架 Hyperpocket，约 2025 初）；2026 年 AIEWF 讲者隶属 KRAFTON（具体职位未公开）——本档「个人实践者」口径据此修正；自建 Overlord 三机 agent 编排系统（即其演讲内容），其余公开履历有限。（履历核：ai.engineer 讲者页 kyle-jaejun-lee，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——待补挖。
### Kyle Jaejun Lee · AIEWF 2026《I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.》（视频上传 2026-07-08）

- URL：https://ai.engineer/talks/4kYl2_mqmnQ-i-run-fleet-ai-agents-across-three （curl 实取全文）
- 身份：个人实践者（非厂商非名人）。
- 号召力口径：无——**仅作会议层样本，不入册候选**。
- **挂钩**：外层调度（人变调度器的失败实录）＋预算与熔断（审批阻塞）。
- 逐字摘录：

> "At that point, I'm not running agents anymore. I've become the scheduler, deciding who does what. I'm the memory, holding what every one of them is doing, and I'm the reviewer, checking all of it. One human, three roles, six contexts. It does not scale."

> "So I built a review gateway. Any layer that wants to act submits its plan, and then it blocks. It waits. Nothing runs until I approve."
>（**"Make approval a blocking operation"**（官方分节名）——审批即阻塞，人审位作为调度原语。）

> 五次故障实录：orchestrator 亲自干活不派活／tmux pane 挤爆／内存耗尽／Git 凭据串仓／笔记本断电全灭（"Everything in flight, just gone"）。
- **最小主张**：小规模多 agent 舰队的瓶颈先是人的注意力，其次才是机器；状态放文件、审批做阻塞是两条幸存经验。
- **派别适配**：**中性票**。
