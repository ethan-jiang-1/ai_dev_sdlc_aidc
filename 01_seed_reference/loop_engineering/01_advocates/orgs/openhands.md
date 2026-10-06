# openhands — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

**（第六轮挖掘（2026-10-06）：开源框架与治理工具）**

### 1. OpenHands（all-hands-ai）——SDK 化后的 stuck detection 与 condenser 全量参数

来源：docs.openhands.dev sitemap 实取（旧站 docs.all-hands.dev 的 `usage/troubleshooting/stuck-loops` 已从 sitemap 消失，经典 stuck loop 文档整体迁入新 SDK 文档 `sdk/guides/agent-stuck-detector`，2026-10-06 实取 200）。

- **Stuck Detector（SDK 内建，默认开启）**。官方逐字：detects five types of stuck patterns——"1. Repeating Action-Observation Cycles: The same action produces the same observation repeatedly (4+ times) 2. Repeating Action-Error Cycles: The same action repeatedly results in errors (3+ times) 3. Agent Monologue: The agent sends multiple consecutive messages without user input or meaningful progress (3+ messages) 4. Alternating Patterns: Two different action-observation pairs alternate in a ping-pong pattern (6+ cycles) 5. Context Window Errors: Repeated context window errors that indicate memory management issues"。参数级：`Conversation(..., stuck_detection=True)`（逐字注释："This is by default True"）；运行期探针 `conversation.stuck_detector.is_stuck()`；判定逐字："Actions are compared by their tool name, action content, and thought (ignoring IDs and metrics) … This allows the detector to identify truly repetitive behavior while ignoring superficial differences like timestamps or event IDs."
  **挂钩：停止条件**（循环内的卡死熔断，阈值 4+/3+/3+/6+ 参数级）。
- **Condenser（上下文压缩）**。SDK 架构页逐字（docs.openhands.dev/sdk/arch/condenser）：组件表 CondenserBase／RollingCondenser／LLMSummarizingCondenser／NoOpCondenser／PipelineCondenser／View／Condensation；配置参数逐字："**max_size**: Event count threshold before condensation triggers (default: 120)／**keep_first**: Number of initial events to preserve verbatim (default: 4)／llm: LLM instance for summarization (often cheaper model than reasoning LLM)"。触发双通道逐字：自动＝"Agent calls condenser.condense() each step"，手动＝"CondensationRequest event added to history (via view.unhandled_condensation_request) … (on LLM context window error) or application code"。PipelineCondenser 逐字："Chains multiple condensers in sequence … Multi-stage compression (e.g., remove old events, then summarize, then truncate)"。指南页（/sdk/guides/context-condenser）逐字收益口径："Up to 2x reduction in per-turn API costs"。
  **挂钩：预算与熔断**（以上下文长度为触发物的预算面，且暴露手动强制触发事件——循环内外的两级触发）。
- **Pause/Resume 与 condense 的 API 化**。Agent Server API 路由实取自 sitemap：`conversations/condense-conversation` 与 `conversations/pause-conversation`；SDK 用法逐字："Pause the agent from another thread or after a delay using conversation.pause(), and Resume … by calling conversation.run() again."
  **挂钩：外层调度**（对运行中循环的暂停/压缩外部控制面）。
- **Critic（验证回路，experimental）**。Agent Canvas 文档逐字（/openhands/usage/agent-canvas/critic）："Iterative refinement lets the critic send the agent back to improve its work when the predicted success score is too low." 参数级逐字："**Critic Threshold** - the success score required to stop refining. **The default is 0.6**.／**Max Refinement Iterations** - the maximum number of retry attempts. **The default is 3**." 运维提示逐字："Lower Max Refinement Iterations if repeated refinement loops are too costly."
  **挂钩：验证回路**（评分驱动的回流再加工，阈值＋迭代上限双参数）。
