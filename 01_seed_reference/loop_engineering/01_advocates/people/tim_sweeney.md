# tim_sweeney — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

**（第五轮挖掘（2026-10-06）：会议 transcript 全量扫）**

### 推-10 · Tim Sweeney（Weights & Biases，Principal Engineer）· AIEWF 2026《An AI Research Agent That Runs Your Experiments》（视频上传 2026-09-26）

- URL：https://ai.engineer/talks/hd7TOvmyAxU-ai-research-agent-that-runs-your-experiments （curl 实取全文）
- **撞名警示**：此 Tim Sweeney 是 W&B/CoreWeave 主任工程师（自述"principal engineer at Weights and Biases and Coreweave… master's in machine learning from Georgia Tech… previous life was the PM of Twitter's ML stack"），**不是 Epic Games 的 Tim Sweeney**，登记防台账撞名。
- **挂钩**：无人值守运行（研究型长任务循环）＋外层调度。
- 官方要点层逐字："Keep long-running training outside the agent's main loop: ARIA starts experiments through Launch and polls while GPU jobs execute."
- 逐字摘录："It started the queues and now it is simply polling and waiting for our work to be complete."（agent 主环轮询、GPU 长任务外置——无人值守的结构分工）；分节标题 "Keep humans in the loop—and let the experiment finish"。
- **最小主张**：研究型无人值守＝"对话环内不动长任务、外置作业系统跑训练、人审位保留"。
- **派别适配**：**推动票（会议层）**。
