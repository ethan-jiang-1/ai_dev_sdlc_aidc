# R1 授权执行（正式阶）——交出单轮内的工具与命令执行权

> **交接面**：人不再逐句批准"能不能跑这条命令/改这个文件"，改为一次性划定**授权面**（允许哪些工具、哪些命令模式），
> 循环在面内自主、面外拒绝或升级。人保留的东西：授权面本身＋机器可核判据（测试门）。

## 一、定义（跨源最小交集）

循环在**一轮之内**可以自主调用工具、执行命令、读写文件；失败自动重试；人的介入点从"每次动作"后移到"授权规则"。

## 二、支撑条目（自说明）

**① Anthropic（deny-and-continue 授权语义）** ⏳ 逐字待补
- 出处：auto mode / Claude Code docs（已回源，锚 [evidence-b](../raw/evidence-2026-09-26-b-stop-and-scheduling.md) / evidence-c）
- 要点：面外动作不中断循环，拒绝并继续（deny-and-continue），拒绝计数累积触发熔断（3/20 口径，转述自台账 `anthropic_org` 行）
- 逐字摘录待补齐后此条才可外引。

**② Cursor 官方语义（✅ 一手已核，2026-09-30 锚 [evidence-u](../raw/evidence-2026-09-30-u-post-june-kols.md) S4a）**
- Cursor 3.6 changelog（2026-05-29）逐字：
  > "Auto-review applies to Shell, MCP, and Fetch tool calls. **Allowlisted calls run immediately**, and **calls that can be sandboxed run in the sandbox**. **All other agent actions go to a classifier subagent** that decides whether to allow the call, try a different approach, or ask for your approval."
  > "Auto-review is a new run mode that allows Cursor to work for longer with fewer approval prompts and safer execution."
- 设置路径：Settings > Cursor Settings > Agents > Approvals & Execution；分类子代理可被用户指令 steering。
- **核销**：evidence-t §1 的 "Run Mode/Auto review/Command Allowlist" 三名词真实存在；"Run Everything""File Deletion Protection" 仍未在本页出现（⏳ 待 run-modes docs 复核：cursor.com/docs/agent/security/run-modes）。
- **界限价值**：官方把授权面切成**三级处置**（allowlist 直行 / 沙箱内跑 / 分类器裁决→人）——这正是"授权面"不是开关而是**分级处置表**的最好说明。

**③ 本仓自证（DSH 授权面即此阶实现）**——指针：[evidence-g](../raw/evidence-2026-09-27-g-dsh-control-surface.md)（沙箱模式/审批策略即 R1 授权面的运行实例）。

**④ Anthropic auto mode：deny-and-continue 全机制（✅ 逐字，[evidence-b §4b](../raw/evidence-2026-09-26-b-stop-and-scheduling.md) → auto mode 博客 2026-03-25）**
> "When the transcript classifier flags an action as dangerous, that denial comes back as a tool result along with an instruction to treat the boundary in good faith: find a safer path, don't try to route around the block. If a session accumulates 3 consecutive denials or 20 total, we stop the model and escalate to the human."
> "The classifier sees only user messages and the agent's tool calls; we strip out Claude's own messages and tool outputs, **making it reasoning-blind by design**."
- 参数级：**3/20 拒绝熔断，官方明写不可配置**（docs：> "These thresholds are not configurable."）；headless 下无人可问→直接终止进程。
- 教学点：拒绝不是终点而是**引导信号**（"find a safer path"）＋裁判输入隔离防操纵。

**⑤ OpenAI Codex 源码级授权判据（✅ 逐字，[evidence-f Source 1](../raw/evidence-2026-09-27-f-autonomy-gates.md) → exec_policy.rs，commit 1f4c473）**
> "If the command is flagged as dangerous or we have no sandbox protection, we should never allow it to run without approval."
> "In restricted sandboxes, do not prompt for non-escalated, non-dangerous commands; let the sandbox enforce restrictions without a user prompt."
> "Projects marked untrusted require approval for every command that is not explicitly allowed by an exec policy rule."
- 三维授权判定：**危险启发式 × 沙箱能力 × 项目可信度**——授权面比"白名单"多两维。

**⑥ 工具名粒度的 interrupt policy（✅ 逐字，[evidence-f Source 7](../raw/evidence-2026-09-27-f-autonomy-gates.md) → LangChain HITL docs）**
> `"write_file": True,  # All decisions (approve, edit, reject) allowed`
> `"read_data": False,  # Safe operation, no approval needed`
> "the action can be approved as-is (`approve`), modified before running (`edit`), or rejected with feedback (`reject`)."
- 人在环三动作：approve / **edit** / reject——"edit"是授权面里最容易被忽略的中间选项。

**⑦ 授权语义的三重边界（✅ 反例，[evidence-f Source 4](../raw/evidence-2026-09-27-f-autonomy-gates.md) → claude-code issue #95749）**
> "Editing files must not imply authorization to commit."
> "Authorization to commit must not imply authorization to push."
> "Authorization for one push must not become standing authorization for later pushes."
- 授权的三个独立维度：**动作类别 × 目标 × 时间有效性**——窄授权被当广授权用是真实事故报告。

**⑧ R1↔R2 的官方分界线（✅ 界限信号，evidence-b §问题2.2）**
> "Auto mode on its own approves tool calls **within a single turn** but doesn't start a new one. Claude stops when it judges the work done."
- R1 的自主度**封顶在单轮内**；跨轮续跑权是 R2 才交的东西。这句是两阶之间最硬的界限。

## 本阶 dissent

- **预写规则实测证伪**（[evidence-c 4a.1](../raw/evidence-2026-09-26-c-autonomy-and-convergence.md) → marmelab 引 arXiv 2608.27443）：> "The rule writers blocked **20.1 percentage points** fewer bad actions… **93% of permission prompts get approved**. **A rule that ends in a prompt isn't a rule.**"——授权面写了没人执行是实测结论，不是猜测。
- **行业执行缺口**（evidence-c → marmelab 2026-09-24 审计）：> "Everybody writes instructions, **almost nobody enforces them** … Only **12** of the 391 repositories commit a single `deny` rule."
- **拒绝后无升级路径**（evidence-f Source 3 → issue #67519）：> "The denial is final, even when the user is actively in the conversation and has explicitly, repeatedly authorized the exact action in chat."——升级可达性是独立于拒绝合理性的第二个控制问题。

## 反例位

- 授权面过大＝R1 直接升级成事故面：失控实录三案（practices ②，[stop_conditions](../stop_conditions/README.md)）里有命令级越权案例 ⏳ 引句待搬。
- "Run Everything 只在 demo 用"——中文传播层与 Anthropic 分档口径同构（evidence-t §3），升阶前先核对官方原文。

## 四、升 R2 的闸门

单轮授权跑顺后，瓶颈移到"每轮都要人来判停/续"——此时需要**可观察的完成条件**（机器闸门 ①）与
**验收分离**（③）才能把"判停权"交出去。停止条件三件的对应做法在
[`stop_conditions/01_machine_gates/`](../stop_conditions/01_machine_gates/README.md) 与 [`03_verdict_split/`](../stop_conditions/03_verdict_split/README.md)，不复制。
