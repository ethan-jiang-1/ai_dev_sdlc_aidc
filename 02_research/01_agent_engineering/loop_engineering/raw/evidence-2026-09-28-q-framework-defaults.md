---
type: evidence_archive
collected_by: 委派回源子代理（Q 路 · 开源框架闸门/上限默认值补采）＋ 主代理抽验（Aider base_coder.py:105-107,1599-1607 / SWE-agent models.py:73-78 经 jsDelivr 逐字复核）
collected_at: 2026-09-28
serves: stop_conditions/01_machine_gates/practices.md（gate 2 条）、02_hard_caps/practices.md（cap 4 条）＋ insights
status: 6 条一手（源码字面量为主）；含 2 处 docs↔源码分歧（双录不仲裁）；取数通道受限见负结论
quality_bar: 源码给 repo+文件+行号+默认值字面量；tag/版本锚定；docs 原句与源码打架时两录并标注
---

# 回源档案 Q：开源 agent 框架的闸门/上限默认值（观测 2026-09-28）

> **任务**：补采前轮中断切口——框架层①闸门与②上限的**出厂默认值**。默认值是工程要领的最小单元：装了没有、默认开不开、超了怎么办。

## Source 1 · Aider — auto_lint 默认开、失败回灌（gate）

- URL：https://github.com/Aider-AI/aider/blob/main/aider/coders/base_coder.py （main；**主代理已复核 105-107 行与 1599-1607 行**）＋ args.py:542-557 ＋ docs（options.html / lint-test.html）；访问：2026-09-28
- 摘录（复核原句）：
  > `auto_lint = True` / `auto_test = False` / `test_cmd = None`（Coder 类属性，main@105-107）
  > 失败流程（1599-1607）：`if edited and self.auto_lint: lint_errors = self.lint_edited(edited) ... if lint_errors: ok = self.io.confirm_ask("Attempt to fix lint errors?") ... self.reflected_message = lint_errors; return`
  > docs："The lint command should accept the filenames of the files to lint. If there are linting errors, aider expects the command to print them on stdout/stderr and return a non-zero exit code."；"Aider will try and fix any errors if the command returns a non-zero exit code."（缺省 linter：Python→flake8，linter.py:136-152）
- 最小主张：编辑后自动 lint **默认开**（auto_test 默认关）；失败路径＝确认后把错误作为 reflected_message **回灌给模型**修复；lint 命令自定义 'lang: cmd' 优先、缺省内置。
- 不支持：采到的代码路径未见固定循环次数上限（未系统排查，不作"无上限"结论）；main 为滚动分支无版本锚。

## Source 2 · OpenHands — enable_auto_lint 默认关（gate）＋ max_iterations=500（cap）

- URL：https://github.com/All-Hands-AI/OpenHands/blob/0.62.0/config.template.toml （308 行）＋ openhands/core/config/sandbox_config.py:68-70（0.62.0；0.24.0:55-57 同字面量）＋ openhands/core/config/app_config.py:70 + config_utils.py:8（0.30.0）；访问：2026-09-28
- 摘录：
  > 模板行（注释态）：`# Enable auto linting after editing` / `#enable_auto_lint = false`（**位于 [sandbox] 段 / SandboxConfig，非 AgentConfig**——对上游口径的修正）
  > schema：`enable_auto_lint: bool = Field(default=False)   # once enabled, OpenHands would lint files after editing`
  > `max_iterations: int = Field(default=OH_MAX_ITERATIONS)` ＋ `OH_MAX_ITERATIONS = 500`（config_utils.py@0.30.0:8）；`max_budget_per_task: float | None = Field(default=None)`
- 最小主张：OpenHands 的**自动 lint 默认关**（双 tag 一致）；Python 时代 max_iterations 默认 **500**、任务预算默认 None（无预算上限）。main 已重构为 TS 栈，500 只锚 Python 线。
- 不支持：模板行是注释示例非用户配置；V1 新栈现行默认未采。

## Source 3 · SWE-agent — 成本上限一族（cap）

- URL：https://github.com/SWE-agent/SWE-agent/blob/main/sweagent/agent/models.py （main；**主代理已复核 73-78 行**）＋ 行为锚 agents.py:306-311,336-339；访问：2026-09-28
- 摘录（复核原句）：
  > `per_instance_cost_limit: float = Field(default=3.0, description="Cost limit for every instance (task).")`
  > `total_cost_limit: float = Field(default=0.0, ...)` / `per_instance_call_limit: int = Field(default=0, ...)`
  > 行为：`if self._total_instance_stats.instance_cost > 1.1 * self.config.retry_loop.cost_limit > 0: ... 'Total instance cost exceeded cost limit... Triggering autosubmit.'`
- 最小主张：**成本上限是一等默认件**（每实例 $3.0，schema 级默认）；总成本与调用数默认 0＝不启用；超 1.1× 触发 autosubmit（错误后交卷而非无限重试）。
- 不支持：call_limit 的运行时 enforcement 点未定位（grep 零命中）；0=关闭的语义部分推断。

## Source 4 · LangGraph — recursion_limit：docs 与源码打架（cap）

- URL：https://docs.langchain.com/oss/python/langgraph/graph-api ＋ PyPI sdist langgraph-1.2.12 `langgraph/_internal/_config.py:32` ＋ main `pregel/main.py:3005-3008`；访问：2026-09-28
- 摘录：
  > docs（.md 原文）："Starting in version 1.0.6, the default recursion limit is set to **1000** steps. … Once the limit is reached, LangGraph will raise GraphRecursionError."
  > 源码（1.2.12 与 main 一致）：`DEFAULT_RECURSION_LIMIT = int(getenv("LANGGRAPH_DEFAULT_RECURSION_LIMIT", "10007"))`
  > 告警原文："Recursion limit of {config[recursion_limit]} reached without hitting a stop condition. You can increase the limit by setting the recursion_limit config key."
- 最小主张：触发行为无分歧（超限抛 GraphRecursionError、有明示告警文案、可用 config 键调）；**默认值两处一手来源打架：docs 1000 vs 发布版源码 10007**——双录不仲裁，引用须注口径。
- 不支持：不支持把任一数字当"当前实际默认"；变更版本号未定位（releases 页/changelog 不可达）。另：langchain-core 层另有 `DEFAULT_RECURSION_LIMIT = 25`（另一层常量，勿混同）。

## Source 5 · CrewAI — max_iter：docs 与同版本源码打架（cap）

- URL：https://docs.crewai.com/v1.15.22/en/concepts/agents ＋ PyPI sdist crewai-1.15.22 `src/crewai/agents/agent_builder/base_agent.py:286-288`；访问：2026-09-28
- 摘录：
  > docs："| **Max Iterations** *(optional)* | `max_iter` | `int` | Maximum iterations before the agent must provide its best answer. Default is 20. |"（示例注释同）
  > 源码（**同版本号 1.15.22**）：`max_iter: int = Field(default=25, ...)`（executor 侧同 25）
  > 触发：`if has_reached_max_iterations(...): formatted_answer = handle_max_iterations_exceeded(...)`
- 最小主张：agent 级迭代上限存在，超限走"给出最佳答案后收尾"（不是硬杀）；**docs 与同版本源码对默认值口径不一致（20 vs 25）**。
- 不支持：不能只引 docs 也不能只引源码；历史 docs 口径未回溯。

## 判读

- **观察**：框架层默认值全景——闸门：Aider lint **默认开**、OpenHands auto-lint **默认关**（同构件相反缺省）；上限：轮次（OpenHands 500、CrewAI 20/25、LangGraph 1000/10007）、成本（SWE-agent $3.0/实例）、预算（OpenHands None）。**没有两家缺省一致**。
- **推断（候选）**：②新增一条工程要领——**默认值必须锚源码/tag，不能引 docs**：两处独立案例（LangGraph、CrewAI）中 docs 与同版本源码字面量不一致；且默认值随版本漂移（OpenHands 500 只锚 Python 线）。上屏参数的引用规范应为"字段＋文件＋tag＋字面量"。
- **与现有材料关系**：对②既有五处厂商上限（Claude Code 家）补上**框架层**对照；对①补"Aider 确认后回灌"这一最简 back-pressure 实现。

## 负结论与限制

- 取数通道：raw.githubusercontent.com 全程不可达（HTTP 000）；api.github.com 60/h 免费额度耗尽（CrewAI main 结构 listing、OpenHands V1 SDK 两项未做）；github blob/releases 页超时——改走 contents API＋jsDelivr＋PyPI sdist 三通道。
- 未定位：LangGraph 1000→10007 变更版本；SWE-agent call_limit enforcement 点；OpenHands V1（TS 栈）现行 max_iterations；CrewAI 历史 docs 的 25 口径。
- PyPI `sweagent` 0.0.1 是占位包，非官方发布通道。
