---
type: org_evidence
directory: 01_advocates/orgs
observation_date: 2026-10-06
---

# cline_roo — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

### Cline / Roo Code——auto-approve 分档与 checkpoint 双版本

- **Cline auto-approve（docs.cline.bot/features/auto-approve 实取）**。分档表逐字：Read project files／Read all files／Edit project files／Edit all files／Execute safe commands／Execute all commands／Use the browser／Use MCP servers／Enable notifications；约束逐字："'Read all files' and 'Edit all files' only extend the base toggle. If the base toggle is off, the 'all files' option does nothing." 长任务哨兵逐字："when an auto-approved terminal command has been running for **30 seconds**"（OS 通知）。YOLO 档逐字："YOLO mode is Auto Approve on steroids. Check the box and Cline auto-approves everything: file changes, terminal commands, browser actions, MCP tools, **and mode transitions (Plan to Act)**."
  **挂钩：预算与熔断**（自主度分档的产品化：8 档权限 × 全开终档）。
- **Cline 安全判定机制（docs 自认，关键增量）**：逐字："**Cline does not use a fixed allowlist. The model marks each command with a requires_approval flag based on the command and arguments. These are examples, not guarantees.** Commonly treated as safe: npm run build, npm test … Commonly requires approval: npm install <pkg> …"
  **挂钩：预算与熔断**（分档闸门本身由 LLM 打标——capability face 上这是"模型自知边界"的实现，缺口面另记）。
- **Cline Checkpoints（docs.cline.bot/core-workflows/checkpoints）**。机制逐字："Cline maintains a shadow Git repository separate from your project's actual Git history. **After each tool use (file edits, commands, etc.), Cline commits the current state** of your files to this shadow repo." 默认开启；三态恢复逐字：Restore Files／Restore Task Only／Restore Files & Task。与 auto-approve 的关系官方直言："Checkpoints make auto-approve practical."
  **挂钩：验证回路**（快照回滚＝事后验证回路，把试错成本归零的产品化表述逐字："The cost of a mistake drops to nearly zero."）。
- **Roo Code auto-approving（roocodeinc.github.io/Roo-Code 实取）**。总闸＋分档："Enabled (bottom-right): master pause/resume for auto-approval"；命令白/黑名单确定性闸门逐字："**Precedence: Deny rules take precedence when their matching prefix is equally or more specific than the allow match (longest-prefix wins).**" 配置键逐字：`roo-cline.allowedCommands`／`roo-cline.deniedCommands`；危险替换守卫逐字："Even allowed prefixes won't auto-approve if the command contains dangerous parameter or process substitutions (e.g., ${var@P}, subshells inserted into here-strings, zsh process substitution =(...) ...)"；MCP 双闸逐字："Both permissions must be active for a tool to auto-approve."（全局开关＋工具级 Always allow）；追问自动应答逐字："Timeout slider: Use the slider to set the wait time from **1 to 300 seconds (Default: 60 seconds)**"（超时后自动选第一个 AI 建议——无人值守推进档）。
  **挂钩：预算与熔断**（与 Cline 同源的自主度分档，但闸门改为确定性最长前缀——姊妹仓库两派闸门，docs↔docs 对照）。
- **Roo Checkpoints**。参数逐字："'Checkpoint initialization timeout' (**10-60 seconds, default: 30s**)"；**与 Cline 的实现差异逐字**："Checkpoints are recorded when tasks begin and **before file modifications. They are not automatically created before command execution.**"（Cline 是 after each tool use 含命令；Roo 只在文件改动前——同谱系两实现，回滚覆盖面不同）。
  **挂钩：验证回路**。
- **Roo Boomerang Tasks（Orchestrator Mode）**。外环逐字："The parent task (in Orchestrator mode) pauses, and the new subtask begins in a different, specialized mode … The parent task resumes with **only the summary** of the subtask."＋"Approval Required: By default, you must approve the creation and completion of each subtask. This can be automated via the Auto-Approving Actions settings."
  **挂钩：外层调度**（子任务上下文隔离＋摘要上行，编排级循环节点）。
