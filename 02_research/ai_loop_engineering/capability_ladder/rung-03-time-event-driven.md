# R3 时间/事件驱动（正式阶）——交出"开不开跑"本身，循环脱离会话在跑

> **交接面**：人不再手动起跑循环。循环由**时间表**（cron/间隔）或**事件**（webhook/渠道消息/状态变化）触发，
> 起跑后人不在场。人保留的东西：触发条件、资源上限、熔断与过期、升级可达性。

## 一、定义（跨源最小交集）

循环的**启动权**交给了调度器或事件源。这是所有来源里"人退出会话"的第一阶——也是唯一一阶
**人不在场看着它跑**的正式阶，所以硬上限/熔断从"保险"变成"唯一刹车"。

## 二、支撑条目（自说明）

**① Runkle event-driven loop（B 类环对应本阶）** ⏳ 逐字待补
- 要点（转述自台账 `sydney_runkle` 行）：四环之三，cron/webhook/channel 触发。锚 [evidence-b §4e](../raw/evidence-2026-09-26-b-stop-and-scheduling.md)。

**② CC 团队 time-based / proactive 两类（A 类双落位）** ⏳ 逐字待补
- 要点（转述自台账 `anthropic_org` 行）：`/loop` 时间驱动、**7 天硬过期**；auto mode 的 deny-and-continue＋**3/20 熔断**。
  锚 [evidence-b](../raw/evidence-2026-09-26-b-stop-and-scheduling.md) / evidence-c。
- 7 天硬过期与 3/20 熔断是本阶"人不在场也要有刹车"的两个已回源参数级实例 ⏳ 参数逐字待补（须锚 docs/源码，本主题纪律）。

**③ Osmani 三/四级** ⏳ 逐字待补：三级 `/loop`/`schedule`、四级 proactive 事件触发无人值守（[evidence-a](../raw/evidence-2026-09-26-a-originators.md)）。

**④ Cursor `/loop` 官方语义（✅ 2026-09-30 锚 [evidence-u](../raw/evidence-2026-09-30-u-post-june-kols.md) S4b）**
- Cursor 3.5 changelog（2026-05-20）逐字——**三种唤醒条件**，与 CC 分类同构：
  > "With /loop, Cursor can run a prompt repeatedly **on a local schedule**, **until a certain outcome is achieved**, or **until you stop it**. If you don't specify a fixed interval, **the agent decides when or what event should wake it**."
- 注意第三个分句：**唤醒时机本身可以交给 agent 决定**——R3 内部还有一层"触发权"的微阶梯（人定间隔 → 人定结果条件 → agent 自主唤醒）。

**⑤ R2↔R3 分界的最清晰表述（Ronacher，✅ S1）**
- > "There is already an **agent loop** inside every coding agent. The model calls a tool, incorporates the result, calls another tool, reads a file, edits a file, runs tests, and eventually produces some answer. … The other loop is the **harness level loop: the loop outside the agent loop**."
- 教学价值：R2 的循环在**会话内**（agent loop），R3 的循环在**会话外**（harness loop 决定起跑、续命、换会话）。一句话把两阶的边界钉死。

**⑥ 本阶的人本成本证词（Ronacher，✅ S1——dissent）**
- > "In the harness operated loop **I'm not sure what my role even is**. Even the 'done' signal loses all meanings … **My role is reduced to that of a messenger**."
- > "If attackers and reporters loop, defenders will eventually need to loop too to keep up."（不可退出的趋势证词）
- 教学时必须并列给出：这一阶交出去的不只是触发权，还有**"done"的语义**。

**⑦ 官方终止栈（✅ 逐字，[evidence-b §4c](../raw/evidence-2026-09-26-b-stop-and-scheduling.md) → CC scheduled-tasks docs）**
> "Recurring tasks automatically **expire 7 days** after creation. The task fires one final time, then deletes itself. This bounds how long **a forgotten loop** can run."
> "If an iteration ends without either rescheduling or stopping, Claude Code schedules one **fallback wakeup about 20 minutes later** and ends the loop when that iteration doesn't reschedule either."
> "Claude calls the `ScheduleWakeup` tool with `stop: true`, which cancels the pending wakeup immediately."
- 三层终止：人 Esc / 模型自停（续跑权本身是可调用工具）/ 7 天硬过期；中间还有未续排→20 分钟收尾的兜底。
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
- **中文传播层在本阶缺位**（[00-map](00-map.md) §三.5）：视频三层从 goal 直接跳编排，无人值守没有切片——传播层把最危险的一阶跳过去了。

## 四、升 R4/R5 的方向

R4/R5 均已升正式阶（[00-map](00-map.md) §三判读 2026-09-30 修订）：R4 需"成败判据简单可验"的活才并发（可验证性闸门）；
R5 改写的是 harness 本身，护栏随改写幅度递增。两阶的闸门与 dissent 见各自阶档。

## 五、与缺口的关系

feature 级四列空矩阵（授权史/priority 变更/业务阻塞原因/跨 feature 验收，[`digested/07`](../digested/07-控制问题矩阵.md)）
在本阶**最疼**：人不在场时，这四列是"回来之后还能不能接上"的全部依据。R3 档后续把四列作为观察清单挂靠。
