---
type: org_evidence
directory: 01_advocates/orgs
observation_date: 2026-10-06
---

# goose — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

**对抗轴**：Adversary Mode fail-open 自认 vs OpenAPPA fail-closed（[_治理工具](../_治理工具.md)）——护栏两派正面对撞。

### Goose（Block → AAIF）——recipe 重试回路、hooks 事件面、对抗审查器

来源：goose-docs.ai（2026-04-07 起官方新 docs，llms.txt 实取）＋ GitHub API。组织变更实锤（官方博客 2026-04-07 逐字）："Block has donated goose to the Agentic AI Foundation (AAIF) at the Linux Foundation, alongside Anthropic's Model Context Protocol (MCP) and OpenAI's AGENTS.md."；仓库迁 `github.com/aaif-goose/goose`。甲方大厂捐赠证据（双料证据升级：Block 出品＋基金会治理）。

- **Recipe Retry 字段（参数级，docs/guides/recipes/recipe-reference）**。schema 逐字："max_retries Number ✅ Maximum number of retry attempts／checks Array ✅ List of success check configurations／timeout_seconds Number - Timeout for success check commands (**default: 300 seconds**)／on_failure_timeout_seconds Number - Timeout for on_failure commands (**default: 600 seconds**)／on_failure String - Shell command to run when a retry attempt fails"。机制逐字："2. Success Validation: After completion, all success checks are executed in order 3. Retry Decision: If any success check fails and retry attempts remain: Execute the on_failure command (if configured) … Increment retry counter and restart execution"。终止条件逐字："All success checks pass (success)／Maximum retry attempts are reached (failure)"。checks 类型逐字：`type: shell` ＋ `command: $validation_command`。
  **挂钩：验证回路＋停止条件**（recipe 级声明式"跑完→shell 验收→不过则重跑"回路，默认超时参数级）。
- **Hooks（循环外部脚本化，2026-05-14 官方博客逐字）**："goose now supports lifecycle hooks. … If you've used Claude Code's hooks or git hooks, it's the same idea. If you haven't: **the agent loop is now scriptable from the outside, without writing any Rust or any MCP server.**" 事件全表逐字："SessionStart, SessionEnd, Stop／UserPromptSubmit／PreToolUse, PostToolUse, PostToolUseFailure／BeforeReadFile, AfterFileEdit／BeforeShellExecution, AfterShellExecution"；配置路径逐字：`~/.agents/plugins/<name>/hooks/hooks.json`（user scope）或 `<project>/.agents/plugins/<name>/`（project scope），matcher 为正则；失败语义逐字："Hooks that fail or time out are logged but won't crash the host tool"。
  **挂钩：循环产品化机制＋验证回路**（把 Claude Code 式 hooks 事件面搬进甲方开源 agent，PostToolUseFailure→人工通知示例官方给出）。
- **Adversary Mode（docs/guides/security/adversary-mode）**。机制逐字："Adversary mode adds a silent, independent agent reviewer that watches tool calls before they execute … It evaluates the tool call against your rules and returns ALLOW or BLOCK. 3. Blocked tool calls are denied — the agent sees the rejection and cannot retry. 4. **If the reviewer fails for any reason, the tool call is allowed through (fail-open)**"。规则文件：`~/.config/goose/adversary.md`，存在即开启。（fail-open 的缺口面判读见 skeptics 卷。）
  **挂钩：预算与熔断**（工具调用前的独立审查闸门，LLM 审查器派开源实现）。
- **自改进循环的官方玩法（2026-06-17 官方博客逐字，Douwe Osinga）**："The loop is to run the benchmark, have goose compare a task where one harness succeeded and another failed, and ask it to explain the difference in concrete terms. A human then looks across a few of those failures, decides what the general lesson is, and asks goose to implement that broader improvement." ＋ "**The human step keeps the loop from collapsing into benchmark tricks.**" 落地增量逐字："goose would sometimes keep exploring after it had enough information to finish. … **PR #9636 added turn count awareness to MoIM**, the context goose injects to keep the model oriented. So now goose knows when it is time to call it a day." 工具面逐字：`./evals/harbor/cmd.py`，子命令 "run, list, show, task, compare, and pull"。
  **挂钩：验证回路＋停止条件**（把"该停了"写进上下文注入物——turn-count awareness 是停止条件的上下文实现法，非硬限位）。
- **Issues are the new PRs（2026-07-30 官方博客，外层调度重排）**。状态机逐字："New issues enter the Inbox. During triage … move to Accepted / design … the issue moves to Ready. At that point an agent can write the code. The issue moves to In progress … and **Verification when the result is ready for a human to confirm that it works. Only then is it Done.** PRs that do not implement a ready issue will be closed."
  **挂钩：外层调度**（goose 官方仓库把 agent 参与门槛前移到 issue 层、把人工验证设为 Done 前置态——SDLC 外环重构的一手样本）。
