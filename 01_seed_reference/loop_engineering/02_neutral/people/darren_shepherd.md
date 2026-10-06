# darren_shepherd — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

**（第三轮挖掘（2026-10-06）：新 KOL）**

### Source D · Darren Shepherd（Obot AI 创始人，Rancher 联创）· The Weekly Dev's Brew Ep23（2026-09-24）

- URL：https://www.wordman.dev/podcast/darren-shepherd-ai-agent-sandboxes/ （curl 实取；@ibuildthecloud）
- 号召力口径：③（Rancher/Kubernetes 生态知名人物）。
- 逐字（页内 transcript 实取）：

> "you have kind of like the internet hosted agentic loop. But then you also have the Codex CLI and Claude Code that agentic loop, which is client-side and the better architecture is the client-side one. It's not the centralized one. Because the centralized one just has…"

- 官方 Key Takeaways（host 撰，页面实取）："**Sandbox the agent loop, not only the tool calls.** The loop directs code that holds secrets and talks to external systems, so the agent and its tools belong in one sandbox with one policy."＋"Egress is the policy surface, not ingress."＋"Output is not progress. Letting a model barf out thousands of lines feels productive until the regressions pile up, and one estimate raised in the conversation puts a skilled engineer's real gain at around 5 to 10 percent."
- **最小主张**：把 loop 治理落到基础设施层——沙箱边界应包住整个 agent loop（agent＋tools 一个沙箱、一个 egress 策略），而非只包工具调用。
- **派别适配**：**中性**（架构派；"output is not progress" 与 5-10% 实际增益估计带清醒怀疑色彩）。
