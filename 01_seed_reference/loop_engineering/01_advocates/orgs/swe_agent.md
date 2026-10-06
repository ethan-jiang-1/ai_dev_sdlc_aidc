# swe_agent — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

**（第六轮挖掘（2026-10-06）：开源框架与治理工具）**

### 2. SWE-agent（Princeton）→ mini-swe-agent——控制面文档的历史性收束

来源：swe-agent.com/latest/ 直取（200）；mini-swe-agent.com 直取（200）；均 2026-10-06。

- **本体降级横幅（docs 逐字）**："SWE-agent has been superseded by mini-swe-agent. mini-swe-agent is simpler & more flexible while still being as performant." ＋ "SWE-agent is now in maintenance-only mode. Check out mini-swe-agent."
  **挂钩：循环产品化机制**（SWE-agent 谱系把"最小循环"定为正式继承者——循环结构的减法路线胜出）。
- **ACI 控制面（原文仍在，作维护文档）**。逐字四条经验："1. We add a linter that runs when an edit command is issued, and do not let the edit command go through if the code isn't syntactically correct. 2. We supply the agent with a special-built file viewer … works best when displaying just 100 lines in each turn. 3. … we simply list each file that had at least one match. Showing the model more context about each match proved to be too confusing for the model. 4. When commands have an empty output we return a message saying 'Your command ran successfully and did not produce any output.'"
  **挂钩：验证回路**（编辑过 linter 闸门＝动作级前置验证，ACI 论点的文档化增量）。
- **mini-swe-agent 控制流（源码级逐字，docs/advanced/control_flow）**。`AgentConfig` 默认值逐字：`step_limit: int = 0`；`cost_limit: float = 3.0`（注释逐字："Stop agent after exceeding (!) this cost"）；`wall_time_limit_seconds: int = 0`（"0 means no limit"）；`max_consecutive_format_errors: int = 3`（"Exit after this many format errors in a row (0 = no limit)"）。异常分类学逐字："Submitted is raised when the agent has finished its task … LimitsExceeded is raised when we hit a cost or step limit … FormatError … TimeoutError is raised when the action took too long to execute … UserInterruption is raised when the user interrupts the agent"；退出语义：循环直到 `messages[-1].get("role") == "exit"`，`exit_status` 取值 `LimitsExceeded`／`TimeExceeded`／`RepeatedFormatError`／`Submitted`。完成魔串逐字：`"COMPLETE_TASK_AND_SUBMIT_FINAL_OUTPUT"`（环境检查输出首行命中即 raise Submitted）。设计立场逐字："Using exceptions for the control flow is a lot easier than passing around flags and states." 轨迹格式版本串：`"trajectory_format": "mini-swe-agent-1.1"`。
  **挂钩：停止条件＋预算与熔断**（四限位＋异常即状态的退出码语义，参数级全量）；**循环结构**（`while True: step()` 单文件循环、FAQ 逐字 "Has a completely linear history — every step of the agent just appends to the messages and that's it."、"bash is all you need"）。
- **FAQ 的循环哲学（逐字）**：关于放弃常驻 shell："It's not obvious when a command has terminated. … We've experimented with various heuristics (watching PIDs, watching for the shell to go back to the prompt, etc.) but all of them were flaky. The mini agent doesn't need any of this!"
  **挂钩：验证回路**（把"输出何时算完"这一观测不确定性整体消掉，属循环观测面的减法）。
