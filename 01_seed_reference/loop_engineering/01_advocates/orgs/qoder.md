---
type: org_evidence
directory: 01_advocates/orgs
observation_date: 2026-10-06
---

# qoder — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

### Quest/新 Qoder 应用：Goal 模式（本轮最完整的"循环产品化"官方文档）

- 厂商/产品/功能名：阿里巴巴 Qoder — Quest Goal-driven（目标驱动自主执行）
- URL：https://docs.qoder.com/user-guide/quest/goal-driven.md （curl 直取 `.md`，2026-10-06 观测）
- 日期：文档在线实取于 2026-10-06（站方未标更新时间）
- 逐字引句：
  - "You describe the goal; Quest breaks it down, plans the execution path, and keeps pushing forward without step-by-step instructions. After each round, Quest evaluates the current progress and judges whether the goal is met. If not, it automatically moves on to the next iteration."
  - "Quest evaluates progress after each round and continues automatically if the goal isn't met, ending on its own once the goal is reached."
  - "**Goal-Driven Execution runs for up to 10 turns by default and stops automatically once the limit is reached.** You can raise the maximum turn budget from **Settings → Integrations → Built-in Capabilities → Goal-Driven Execution** to match the complexity of your task."
  - （最佳实践）"Describe a verifiable end state: a good goal is 'test coverage reaches 80%,' not 'write some tests.' Quest needs a clear completion criterion to judge whether the goal is met."
- **与 loop engineering 的挂钩**：循环产品化机制（官方把"多轮迭代＋每轮自评＋未达标续跑"做成一等公民模式）；停止条件（目标达成判定＋默认 10 轮硬上限）；预算熔断（轮数预算，用户可调）。与 Addy Osmani "design the loop, not the prompt" 直接对位：阿里把"每轮评估→判定→续跑/停止"整个写进了产品开关。

### 乙、Qoder — Spec→Goal 组合与 Spec 定时化：规格层与循环层的官方接驳

- 厂商/产品/功能名：Qoder — Quest Spec-driven development（规格模式）
- URL：https://docs.qoder.com/user-guide/quest/spec-driven.md （curl 直取 `.md`，2026-10-06 观测）
- 日期：同上
- 逐字引句：
  - "After a Spec is generated, if you want Quest to iterate on it autonomously and keep pushing it forward, turn on the **Goal** toggle on the Spec card, then click **Build**. Once enabled, Quest runs that Spec in Goal mode — evaluating progress at the end of each round and continuing to iterate until it's done, with no need to issue step-by-step commands."
  - （Spec 转定时）"instead of clicking **Build**, click the **Schedule** button on the Spec card, set the execution time, and save, and Quest will run that Spec automatically at the scheduled time. This is handy for moving time-consuming development work to off-peak overnight hours."
- **与 loop engineering 的挂钩**：循环产品化机制＋外层调度（Spec＝蓝图工件，Goal＝循环执行器，Schedule＝无人值守触发；三层在官方文档里显式互相接驳）。

### 丙、Qoder — Automations（定时自动化）与无人值守授权

- 厂商/产品/功能名：Qoder — Automations（本地/云端定时 Agent 任务）
- URL：https://docs.qoder.com/qoder/automations.md （curl 直取 `.md`，2026-10-06 观测）
- 日期：同上
- 逐字引句：
  - "Start Agent work on a schedule and verify each result in **Run history**."
  - （可自动化判据）"The task should be able to finish without live clarification. It needs clear inputs, an observable completion condition, and resources accessible from its execution environment."
  - （无人值守授权）"review **Execution authorization**, which enables unattended operation. When it is enabled, a scheduled Agent can call tools without waiting for the confirmations used in a regular task. Limit access to the workspace and operations required for the automation."
  - "Write the instructions as a handoff another person could execute directly. Include the input source, allowed changes, prohibited actions, validation method, and expected output."
- **与 loop engineering 的挂钩**：无人值守运行＋停止条件（"observable completion condition" 成为官方给出的可自动化前置判据）＋自主度分档（Execution authorization＝逐次确认→免确认的显式闸门）。官方那句"写成别人可以直接执行的交接文档"正是循环交接思路的厂商版。

### 丁、Qoder — Quest 窗口退役公告（循环产品化载体收拢）

- 厂商/产品/功能名：Qoder — Qoder IDE Quest window retirement notice
- URL：https://docs.qoder.com/release-notes/quest-retirement-notice.md （curl 直取 `.md`，2026-10-06 观测）
- 日期：公告页在线实取 2026-10-06；退役执行日 2026-10-15
- 逐字引句："The **Quest** window in Qoder IDE will be retired on **October 15, 2026, at 23:59 (UTC+8)** and will no longer be available after that time."；"**Migrate to Qoder (recommended)**: If your workflow focuses on task execution and collaboration, you can move your existing work to Qoder."
- **与 loop engineering 的挂钩**：循环产品化机制（承载 Goal/Spec/定时任务的 Quest 窗口自 IDE 收拢进独立 Qoder 应用——任务型循环执行与编辑器分家，"循环作为独立产品形态"的结构性信号）。另：Agent Mode 文档（https://docs.qoder.com/user-guide/quest/agent-mode.md ）含逐轮回滚："The workspace will immediately be restored to the state before that turn's operations"（挂钩：验证回路/回滚安全垫）。

### 辛、通义灵码（阿里）— 智能体模式官方文档（品牌线已并入 Qoder CN）

- 厂商/产品/功能名：阿里云 通义灵码（文档现挂 Qoder CN 品牌）— 智能体模式
- URL：https://www.alibabacloud.com/help/zh/lingma/qoder-cn/user-guide/agent （curl 直取，2026-10-06 观测）
- 日期：页面自标"更新时间：Jul 15, 2026"（窗口内）
- 逐字引句：
  - "智能体在使用工具的过程中，无需开发者确认或干预，可进行自主决策和执行。同时，可根据返回结果决策下一步执行计划。"
  - （终端闸门）"为保障命令执行的确定性，默认每次执行命令前需要开发者进行确认……开发者可以在插件设置中，配置自动执行的命令允许列表，配置好的命令，可以无需确认自动执行。"
  - （规划）"智能体会根据自主意图识别，针对复杂任务自动生成一份方案和规划，您也可以通过 /plan 主动触发生成规划。生成的规划方案会展示给你审阅，确认后即可按照规划执行。"
- **与 loop engineering 的挂钩**：自主度分档（工具层免确认/命令层默认逐次确认＋允许列表白名单＝官方三档闸门）；循环结构（"根据返回结果决策下一步"＝观察-决策循环的官方表述）。结构事实：灵码文档已并入 Qoder CN 命名空间（lingma/qoder-cn 路径），与丁条 Qoder 收拢互证——阿里把编码 agent 产品线收成一棵树。
