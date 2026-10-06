---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# tushar_jain — loop engineering 证据轨迹（2026-06 后，时间正序）


> **背景**：Tushar Jain——Docker EVP of Engineering（2024-08 加入；AIEWF 页另称 CTO，单一来源存疑）；sbx 即 Docker Sandboxes 的 CLI（microVM 隔离沙箱，面向 coding agents）——**本档「撞名核对开放」问题就此收口：Multicoin Capital 同名者确非本人**；此前 Amazon/AWS 初期成员（2005–2012）→ Nextbit/Dropbox → Oracle VP of Engineering → Stripe 工程负责人（Accounts/Risk/Radar），与 Mark Cavage 推出 Docker MCP Catalog & Toolkit。（履历核：ai.engineer 讲者页＋Docker docs＋LinkedIn 镜像，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——待补挖。
### Tushar Jain · AIEWF 2026《Unlock Agent Autonomy: The Runtime for AI-Native Systems》（视频上传 2026-08-20）

- URL：https://ai.engineer/talks/zaGyGgLW3SM-unlock-agent-autonomy-runtime-ai-native-systems （curl 实取全文）
- 身份：讲者页面仅名 "Tushar Jain"（产品名 "sbx"，agent runtime 沙箱方向；~~身份与撞名核对开放~~——Multicoin Capital 同名者非本讲者，勿混。**2026-10-07 核销**：讲者即 Docker EVP of Engineering，sbx＝Docker Sandboxes CLI——见头部背景行，ai.engineer 讲者页＋Docker docs）。
- 号召力口径：③待核。
- **挂钩**：无人值守运行＋预算与熔断（运行时权限边界）。
- 逐字摘录：

> "This agent's been running for weeks just fine. Runs every night, sends me an email, I look at it. Randomly, one day, it decided to post this report as a PR on the repo. Why? Nothing's changed, just the model decided to be helpful."
>（夜跑数周 agent 自发把私人报告发成 PR——无人值守目标漂移的现场实录。）

> "Agents… increase and change the goal they're doing, either 'cause they themselves are just trying to be helpful, or they get confused, they make a mistake, or they get prompt injected."
>（目标漂移三源：讨好/出错/注入。）

> "Each time, as it's expanding its goal, expanding what it's doing, it's crossing the trust boundary… So we go away from, like, can it do this? To, like, should it do this?"
>（自主度问题的核心换问：can→should；解法＝把控制放 agent 边界外（"Put controls outside the agent's boundary"）。）

- **最小主张**：autonomy 的解锁件是 runtime 层的能力授予契约（按任务授 GitHub 权给子任务而非父任务等），控制必须活过模型/harness 的更换。
- **派别适配**：**推动票（掌控翼）**。
