# langchain — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

**（第六轮挖掘（2026-10-06）：开源框架与治理工具）**

### 8. LangGraph/LangChain 增量——配额面上移到 LangSmith，OSS 侧无 budget 参数（如实）

通道：docs.langchain.com sitemap 全量过滤＋usage-and-billing／upsert-usage-limit／llm-gateway-credits 三页直取（2026-10-06）。

- **事实**：LangGraph OSS 文档（oss/python/langgraph/*）本轮 sitemap 中与控制面相关的新页只有 checkpointers／interrupts／use-subgraphs；**未发现 per-agent/per-run 的 budget 或 quota 参数新增**（上轮已收 recursion_limit 仍是 OSS 循环限位主参数）。预算/配额能力在平台层 LangSmith 落地。
- **LangSmith Usage Limits（组织级配额 API）**。API 实取（smith-api/usage-limits/upsert-usage-limit）：`PUT /api/v1/usage-limits`，请求体字段逐字：`"limit_type": "monthly_traces", "limit_value": 123, "tenant_id": …, "scope": "workspace"`。语义逐字："This 429 is the result of reaching your usage limit as configured by your organization admin and is **evaluated in a fixed window starting at the beginning of each calendar month in UTC** and resets at the beginning of each new month." 硬顶逐字："**Each trace is limited to a maximum of 25,000 runs.** Once the trace reaches this limit, LangSmith will reject any additional runs."（另有 plan 级 hourly trace event／ingest／monthly unique traces 三层 429。）
  **挂钩：预算与熔断**（agent 运行配额的托管实现：月窗 UTC＋429＋trace 硬顶；粒度止于 org/workspace，见 skeptics 卷）。
- **LLM Gateway Credits（beta）**。逐字："Gateway Credits let you call LangChain-hosted models through the standard LLM Gateway API without setting up a provider account or key. Authenticate with only your LangSmith API key."；路由逐字："A hosted model slug such as moonshotai/kimi-k3 uses Gateway Credits. A model ID that starts with a configured bring-your-own-key provider … uses that provider's secret instead." Base URL：`https://gateway.smith.langchain.com/v1`。
  **挂钩：预算与熔断**（模型消费侧的统一计费闸口——预算执行点从 agent 代码上移到网关）。
