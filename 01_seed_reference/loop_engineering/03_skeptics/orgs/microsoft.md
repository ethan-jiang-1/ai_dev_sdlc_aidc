# microsoft — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

**（第五轮挖掘（2026-10-06）：会议 transcript 全量扫）**

### 疑-6 · Ornella Bahidika & Joel Allou（Microsoft）· AIEWF 2026《Don't Let the LLM Drive》（视频上传 2026-07-20）

- URL：https://ai.engineer/talks/m24UKZomm7k-dont-let-llm-drive （curl 实取全文）
- 身份：Microsoft 讲者（页面 title 带机构）——**仅作会议层样本**。
- **挂钩**：停止条件（控制权外移＝对"模型自主决定下一步"的否定）＋循环结构（状态机包住模型）。
- 逐字摘录：

> "The trick is LLM is not in charge… It nails the demo, then a real user gets in, and halfway through, the agent decides it's done, or skips a state or even loops… But reliability was never a prompting problem. It's a control problem. The model is the talent, and the harness is the director. The model is brilliant at delivering a line, but it's really terrible at remembering if it's on step three of six. So we stop asking it to."
>（**"可靠性不是提示问题而是控制问题"**；agent "even loops" 作为失败模式被点名。）

> "The model never decides where we are… It proposes, but ultimately it is the harness that decides."
>（与推动派"loops 自主跑"叙事正面对冲：推进权收回 harness。）

> "Instead of having a very heavy model like a 4.7, we're actually able to rely on something like a Haiku 4.5… saving money, saving time, and saving latency."
>（控制权外移的经济学红利。）
- **最小主张**：多步 agent 的可靠性来自把"何时结束/走向何方"从模型手里拿走，放进状态机；模型只出提案。
- **派别适配**：**怀疑票（控制权向）**——对 loop 自主化路线的工程学刹车。
