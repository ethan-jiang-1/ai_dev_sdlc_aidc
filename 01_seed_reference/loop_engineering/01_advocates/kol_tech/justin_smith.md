---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# justin_smith — loop engineering 证据轨迹（2026-06 后，时间正序）


> **背景**：Justin Smith——Resolve AI 创始产品工程师（本人一手口径 “founding product engineer”，非 co-founder）；15 年以上监控/可观测性经验：Splunk Observability Suite 架构师之一、更早任职 VMware。（履历核：ai.engineer 讲者页，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——待补挖。
### Justin Smith（Resolve AI 创始产品工程师，前 Splunk 可观测性架构师）· AIEWF 2026《Always-on agents run production without the on-call tax》（视频上传 2026-08-09）

- URL：https://ai.engineer/talks/vSx5IULvBns-always-on-agents-run-production-without-on （curl 实取全文）
- 号召力口径：③弱——**仅作会议层样本**。
- **挂钩**：无人值守运行（生产运维侧）。
- 逐字摘录："Seventy percent of the time from an engineer is actually not focused just on writing code. It's actually spent on actually running the code that is shipped into production."；"Unlimited tokens is sort of coming to an end. The token max, right, they're starting to clamp down. Prices are going up."（**厂商侧证实 tokenmaxxing 收敛**——怀疑派/中性亦可引）。
- **派别适配**：**推动票（会议层）**。

---

# 增量补挖（2026-10-07 goal 第一批·单点→稳定复核）

> 判定：**单点解除 → 稳定**（06-23 公司博客 → 08-09 AIEWF 同向：生产侧无人值守循环＋环境上下文是成本本体）。完整发现见 .tmp-goal-movers/batch-B2-advocates.md（tmp 过渡载体）。

## 《Run your daily engineering tasks in prod with agents》（Resolve AI 博客，2026-06-23，本人署名 Founding Engineer）

- URL：https://resolve.ai/blog/background-agents-to-run-daily-engineering-tasks-in-prod ｜ fetch 成功（curl 全文）
- 逐字摘录：

> "task = execution x production context. … The expensive part is navigating the environment well enough to know how to perform the task."

> "Coding agents have made it faster to write and ship software… The other half, keeping what you shipped running, has not improved at the same rate. In many cases, the acceleration on the build side has increased the operational load on the teams responsible for keeping systems healthy."
（**build 侧加速反增运维负载**——与怀疑派 review-bottleneck 同构的厂商侧表述。）

> "Background agents… are always-on agents that run on a schedule or a trigger, carry live context about your production environment, and handle operational work continuously without requiring a human to initiate each task."
