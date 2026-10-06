---
type: org_evidence
directory: 01_advocates/orgs
observation_date: 2026-10-06
---

# kiro — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

### Amazon Kiro —— 解决·强（Autonomous mode/Workflows/Automations/Crew/Hooks 五面全文档化）

- **G1. 官方文档《Autonomous mode》（Kiro Web，living docs，实取 2026-10-06）**
  - URL：https://kiro.dev/docs/web/autonomous-mode/
  - 逐字摘录：

> "Autonomous mode lets the agent own the outcome of a task from start to finish. Instead of iterating with you step by step, the agent builds a plan, delegates work to specialized sub-agents, and opens a pull request or merge request automatically when the work is complete."

> "Autonomous mode is off by default — when it's off, you work with the agent collaboratively in the default mode."

> "A workflow gives the runtime a reusable graph with explicit steps, agents, handoffs, loops, waits, and completion conditions; it can run in the background while you continue the parent conversation."

> "In autonomous mode, the agent selects the model automatically — you cannot choose the model yourself."＋"If the agent needs clarification during execution, the task moves to a Needs attention state and waits for your input."

  - **该条支持的最小主张**：Kiro 官方区分"agent 自主决定内部过程的单任务环"与"显式图工作流（含 loops、waits、completion conditions）"——**"loop"与"completion conditions"作为运行时正式词表出现在 AWS 系厂商文档**。
  - 派别适配：**推动·厂商**（上轮"only 标题"解除）。

- **G2. Changelog 2026-09-30《Introducing Workflows in Kiro Web》＋同日 IDE 1.2＋10-01 CLI 2.27.0**
  - URL/日期：https://kiro.dev/changelog/ （索引页直取；条目日期 Oct 1, 2026 / Sep 30, 2026 实取）
  - 逐字摘录：

> "Workflows are now available as an opt-in feature in Kiro Web cloud sessions. They run reusable, multi-step agent plans in the background while you continue working in the parent conversation."

> "Each step runs in its own agent session, which you open from the Workflows panel; it sees only what earlier steps hand it, and the run pauses when a step needs your input."＋"After a failure, you can retry the failed steps."

> "IDE 1.2 introduces Workflows, strengthens safeguards for untrusted workspaces, and adds enterprise controls for sign-in methods."（IDE 1.2，Sep 30, 2026）

> "Kiro CLI 2.27.0 adds control over how V3 delegates when Workflows are enabled … When Workflows are enabled, the new Workflows: sub-agent tool setting is on by default, so the main chat can delegate directly to sub-agents or through Workflows. Turn it off under /settings features to limit main-chat delegation to Workflows"（CLI 2.27.0，Oct 1, 2026）

  - **该条支持的最小主张**：后台多 agent 工作流（步骤级可查/可答/可暂停/可重试）在 2026-09-30/10-01 三面齐发，且 CLI 侧把"主 chat 能否直接委派 sub-agent"做成默认开、可关的治理开关。
  - 派别适配：**推动·厂商**＋机制登记。

- **G3. 官方文档《Automations》《Running 24/7》《Hooks》《What's new in CLI V3》（living docs，实取 2026-10-06）**
  - 逐字摘录：

> "Automations let Kiro Web run a prompt against your GitHub or GitLab repositories on a schedule, without you starting a session. … Kiro carries it out in autonomous mode."（automations；其官方恶意指令警告进怀疑面增量 I）

> "Crew is designed to run continuously so its Slack bot, cron jobs, and task runner keep working while you're away from your desk."（crew/running-24-7）

> "Hooks run shell commands or agent prompts automatically when specific events happen in your session - the agent modifies a file, invokes a tool, or completes a task."＋"Gate dangerous operations - block tool execution unless preconditions are met (PreToolUse)"（hooks；target 9 Kiro 行）

> "CLI V3 is built on the same unified agent harness that powers the Kiro IDE and Kiro Web."＋"Capability-based permissions — declare structured policies in permissions.yaml for fine-grained, auditable control."（CLI V3；V3 为 early release，发布日未单列，以 10-01 changelog 佐证）

  - **该条支持的最小主张**：Kiro 的无人值守面=定时自主模式（Automations）＋常驻网关（Crew 24/7）＋事件钩子闸门（PreToolUse 阻断）＋统一 harness；controls 与产品同面铺开。

### G · Kiro：hooks schema、Automations、Sandbox（kiro.dev 实取）

- **hooks**（docs/hooks、hooks/types、hooks/actions 实取）：schema 逐字段——`version:"v1"`、`hooks[].trigger`（PascalCase，trigger 全表：Prompt Submit/Agent Stop/Session Start/Agent Spawn/Session End/Pre Tool Use/Post Tool Use/File Create/Save/Delete/Pre/Post Task Execution/Manual，**逐 surface 支持矩阵**）、`matcher`（正则过滤）、`action`（`command` 或 agent prompt）。**退出码语义**：0 → stdout 进 agent 上下文；非零 → stderr 给 agent 且 **Pre Tool Use 下阻断工具调用、Prompt Submit 下阻断提交**；**默认超时 60 秒，设 0 禁用**。成本注记逐字："*Agent Prompt actions consume credits as these actions trigger a new agent loop, whereas Shell Command actions do not.*"
  - 挂钩：**停止条件**（PreToolUse 闸门）＋**验证回路**（hook 非零退出＝程序化否决回注）。
- **Automations**（docs/web/automations.html＋changelog/web/introducing-automations 实取，**2026-06-19 上线**）：Web 上按日程对 GitHub/GitLab 仓库跑 prompt，"*runs it on that cadence in its own sandbox in autonomous mode… opens a pull request or merge request when there's something to review*"；prompt 上限 **10,000 字符**；状态仅 Active/disabled 二态；注入面警语逐字："*The agent learns from and follows instructions in the repository code, even if those instructions are malicious.*"
  - 挂钩：**无人值守运行**＋**循环产品化机制**（定时＋自主模式＋沙箱＝最小完整循环产品）。
- **Sandbox**（docs/web/sandbox.html 实取）：每任务独立沙箱、克隆授权仓库、headless Chrome＋Playwright MCP＋Chrome DevTools MCP 预装；域名白名单、环境变量/secrets、MCP 均可配；"*Keeps the sandbox's file state with the session, so you can reattach from any surface*"，删会话删沙箱。
  - 挂钩：**沙箱与环境**。
