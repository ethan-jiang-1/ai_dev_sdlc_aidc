# kim_maida — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

**（第五轮挖掘（2026-10-06）：会议 transcript 全量扫）**

### 中-5 · Kim Maida（身份核：开发者关系/身份认证领域，Auth0-Okta 背景；页面未带机构字段）· AIEWF 2026《It's 10pm. Do You Know Where Your Agents Are?》（视频上传在库页实录）

- URL：https://ai.engineer/talks/I3znWC3MEXM-its-10pm-do-you-know-where （curl 实取全文）
- 号召力口径：③弱——**仅作会议层样本**。
- **挂钩**：预算与熔断（身份/权限熔断）＋无人值守运行（监控缺位）。
- 逐字摘录：

> "Agents with API keys are indeed out past 10:00. They're overprivileged, so this means they are able to act freely on decisions that they make that you may or may not agree with, and they can do this even with your supervision."

> "We can't just solve this with human-in-the-loop. We spent decades solving access management for humans, so just blindly trusting a human who might be a little bit consent fatigued, or who might be tired enough at night, this isn't really going to be enough."
>（**对"什么事都上 human-in-the-loop"的正面否定**——中性偏疑，且给出替代解：RFC 8693 token exchange 按工具调用缩权。）

- 官方分节："Find the enforcement point in the agent loop""Exchange delegated access for a tool-specific credential"。
- **最小主张**：agent 循环的强制点在 MCP/运行时边界，用委托换工具级短时凭据，而不是在人身上堆审批。
- **派别适配**：**中性票**。
