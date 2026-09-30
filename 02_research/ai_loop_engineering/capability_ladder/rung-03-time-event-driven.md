# R3 按时/按事件唤醒（主线 · 机制已证）——交出再次起跑的时机

> **交接面**：时间表或事件源决定**何时再次启动**，人设范围、成本上限、取消方式与升级路径。**会话内定时续跑**（如 Claude Code `/loop`）与**跨会话持久任务**（如云端调度）是不同运行边界：后者才可能在人不在场、会话结束后继续运行。

## 一、定义（跨源最小交集）

本阶交出启动时机，而不是默认交出会话存续或所有高风险动作的授权。教学先演示会话内唤醒，再讨论跨会话持续运行所需的持久状态、取消传播与可达的人工接手；两者都需界定资源预算。

## 二、支撑、反例与回源待办（⏳ 条目不计入支撑）

**① Runkle event-driven loop（B 类环对应本阶）** ⏳ 逐字待补
- 要点（转述自台账 `sydney_runkle` 行）：四环之三，cron/webhook/channel 触发。锚 [evidence-b §4e](../raw/evidence-2026-09-26-b-stop-and-scheduling.md)。

**② CC 团队 time-based / proactive 两类（[evidence-a D3](../raw/evidence-2026-09-26-a-originators.md)）**
- > "For these, you can trigger when Claude runs with /loop, which re-runs a prompt on an interval."（[evidence-a D3](../raw/evidence-2026-09-26-a-originators.md)）
- `/loop` 的 7 天到期见 [evidence-b §4c](../raw/evidence-2026-09-26-b-stop-and-scheduling.md)；auto mode 的 3/20 拒绝熔断见同档 §4b。两者分别管**调度寿命**与**动作审批**，后者并非本阶专属，也不能代替跨会话任务的停止上限。

**③ Osmani 的实践界限（[evidence-a](../raw/evidence-2026-09-26-a-originators.md)，[2026-08-14 原文 Fine print](https://addyosmani.com/blog/practical-loop-engineering/)）**
- > "loops are session-scoped … If you need something that outlives your session, /schedule runs it in the cloud."——先教“再次唤醒”，再单列“跨会话持久”所需保障。

**④ Cursor `/loop` 官方语义（✅ 2026-09-30 锚 [evidence-u](../raw/evidence-2026-09-30-u-post-june-kols.md) S4b）**
- Cursor 3.5 changelog（2026-05-20）逐字——**三种唤醒条件**，与 CC 分类同构：
  > "With /loop, Cursor can run a prompt repeatedly **on a local schedule**, **until a certain outcome is achieved**, or **until you stop it**. If you don't specify a fixed interval, **the agent decides when or what event should wake it**."
- 注意第三个分句：**唤醒时机本身可以交给 agent 决定**——R3 内部还有一层"触发权"的微阶梯（人定间隔 → 人定结果条件 → agent 自主唤醒）。

**⑤ R2↔R3 分界的最清晰表述（Ronacher，✅ S1）**
- > "There is already an **agent loop** inside every coding agent. The model calls a tool, incorporates the result, calls another tool, reads a file, edits a file, runs tests, and eventually produces some answer. … The other loop is the **harness level loop: the loop outside the agent loop**."
- 教学价值：Ronacher 区分工具调用所在的 agent 内循环与决定是否重新驱动它的 harness 外循环；**内外是控制层次，不是会话边界**。`/goal` 也可能使用外层继续判定；跨会话持久性须另看调度器。

**⑥ 本阶的人本成本证词（Ronacher，✅ S1——dissent）**
- > "In the harness operated loop **I'm not sure what my role even is**. Even the 'done' signal loses all meanings … **My role is reduced to that of a messenger**."
- > "If attackers and reporters loop, defenders will eventually need to loop too to keep up."（不可退出的趋势证词）
- 教学时必须并列给出：这一阶交出去的不只是触发权，还有**"done"的语义**。

**⑦ 官方终止栈（✅ 逐字，[evidence-b §4c](../raw/evidence-2026-09-26-b-stop-and-scheduling.md) → CC scheduled-tasks docs）**
> "Recurring tasks automatically **expire 7 days** after creation. The task fires one final time, then deletes itself. This bounds how long **a forgotten loop** can run."
> "If an iteration ends without either rescheduling or stopping, Claude Code schedules one **fallback wakeup about 20 minutes later** and ends the loop when that iteration doesn't reschedule either."
> "Claude calls the `ScheduleWakeup` tool with `stop: true`, which cancels the pending wakeup immediately."
- 这是**该 `/loop` 机制**的终止路径：人 Esc、模型自停、未续排时的 20 分钟兜底、7 天到期；不等于所有跨会话任务都有同样的默认保护。
- 无 prompt 时循环干什么也有官方规格（范围封顶＋不可逆动作须有授权继承）：> "Claude does not start new initiatives outside that scope, and irreversible actions such as pushing or deleting only proceed when they continue something the transcript already authorized."

**⑧ 环定义原文（✅ Runkle/LangChain，2026-06-16，[evidence-b §问题2.5](../raw/evidence-2026-09-26-b-stop-and-scheduling.md)）**
> "The event-driven loop connects your agent to your ecosystem. An event fires — a new document lands, a schedule triggers, a webhook arrives — and the agent runs. **The agent isn't something you invoke manually**; it's a component running continuously inside a larger system."

**⑨ R1×R3 正交分界句（✅ OpenClaw，[evidence-e §2B](../raw/evidence-2026-09-27-e-cross-feature-observability.md)）**
> "Standing orders define **what** the agent is authorized to do. Automations define **when** it happens."
- 授权面（what）与触发器（when）是两个独立旋钮——教学时别让学员把"常设授权"和"定时触发"混成一个决定。

**⑩ 事故与产品化闸门（✅ 反例，[evidence-o](../raw/evidence-2026-09-28-o-runaway-incidents.md)）**
- zombie 循环穿透显式关闭（issue #46787）：> "2 'ralph' automation loops … I had explicitly turned these off days earlier, **but the kill did not propagate to the actual tmux sessions**"
- doom-loop 检测产品化（OpenRouter）：> "That's a doom loop: **the run keeps spending money without getting anywhere.** … recommended defaults: observe@2, block@3, stop@6"——**默认关闭**也是要点。
- 硬超时样本（Copilot cloud agent，[evidence-i Source 8](../raw/evidence-2026-09-27-i-high-influence-control.md)）：> "maximum execution time of **59 minutes** … cannot be extended or bypassed."

## 本阶 dissent

- > "**a loop running unattended is also a loop making mistakes unattended**" / "**done is a claim and not a proof.**"（Osmani，[evidence-a D7](../raw/evidence-2026-09-26-a-originators.md)）
- > "An AI agent is an LLM **wrecking its environment in a loop**."（Willison 转引 Solomon Hykes，[evidence-i Source 4](../raw/evidence-2026-09-27-i-high-influence-control.md)）
- 放权卡点（Böckeler）：行为面 harness 尚不足以支撑减监督——见 rung-02 dissent 引句；R2→R3 之间最宽的沟。

## 反例位（补充指针）

- 无人值守×失控＝最危险的组合：失控实录三案（practices ②）中 194h zombie 孤儿进程等案例即本阶事故面 ⏳ 引句待搬
  （锚 [stop_conditions/02_hard_caps](../stop_conditions/02_hard_caps/README.md) practices ②，不复制）。
- **传播层未讲无人值守**（[evidence-t](../raw/evidence-2026-09-30-t-shenmejiaoqq-video-zh.md)）：视频从 goal 直接讲并发，没有介绍持久运行的额外风险；这是一处叙事遗漏，不证明必须先掌握 R3 才能并发。

## 四、可选方向：编排与元循环

从有界任务可直接探索[多主体编排](branch-a-orchestration.md)，不必先做跨会话无人值守。另一条是[改进循环本身](branch-b-meta-loop.md)：先由人审核修改建议，再讨论外围件的受控应用；自动改核心判据仍未成熟。两者均不是本阶后必修的高阶方向。

## 五、与缺口的关系

feature 级四列空矩阵（授权史/priority 变更/业务阻塞原因/跨 feature 验收，[`digested/07`](../digested/07-控制问题矩阵.md)）
在本阶**最疼**：人不在场时，这四列是"回来之后还能不能接上"的全部依据。R3 档后续把四列作为观察清单挂靠。
