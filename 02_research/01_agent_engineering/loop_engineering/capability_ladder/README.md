# capability_ladder — Loop Engineering 学习路径 · 按交接面横切

> 接手先读本文件与 [00-map](00-map.md)：后者是本区**教学分层及证据强度的唯一判定权威**，一手素材仍在 `raw/evidence-*`，议题判读仍在 `digested/`。

## 〇、初衷与定阶纪律

本区从学习者角度，一层层解释“把什么决定交给循环、需要补什么护栏”。区分**主线交接**与**高阶能力分支**，避免把不同维度硬排成人人必经的成熟度模型。

- **编号**：`LE` = Loop Engineering；`LE0–LE3` 只标本区的执行委托交接面，不表示质量分、轮数或产品原生命令。
- **主线**：LE0 人逐次提示（基线）→ LE1 单次运行的有界执行 → LE2 有界目标续跑 → LE3 按时/按事件唤醒；LE3 内把会话内定时与跨会话持久运行分开。
- **两条高阶分支**：支线 A 多主体编排、支线 B 改进循环本身。两者都有一手机制与场景案例，可从有界任务进入；高阶**不要求学员掌握**，展示趋势、适用域与未成熟之处即可。
- **定阶门槛**：独立一手来源能支持某个**交接面存在**，才称“机制已证”；还须单独判断适用场景、运行风险、通用成熟度和效果。对照表的语义落位不计独立票；同机构作者、转述链、未经原声核验的视频不重复计票。不得用“有两个案例”推出普遍最佳实践。
- **不叫成熟度模型、不按 N 轮切级**：阶段是教案，实际授权由任务风险、可逆性和验收成本决定，可以随时退回。学员学会选择**合适的**自主度，比爬到最高阶更重要。

## 一、分工

| 位置 | 组织轴 | 权威 |
|---|---|---|
| `raw/evidence-*` | 来源与原文 | 证据权威，本区只引用 |
| `digested/*` | 跨源议题 | 主题判读权威，本区不覆盖 |
| [`stop_conditions/`](../stop_conditions/README.md) | 停止条件的控制问题 | 机器闸门、硬上限、验收与干活分离的做法 |
| 本区 | 学习者的交接面、教学次序与证据限定 | [00-map](00-map.md) 是**本区**判定权威；阶档为讲解材料 |

- 每条做法带原句/代码/参数及来源，纯指针条目不算自说明做法。未补逐字的条目仅是回源待办，**不用于支撑定阶**；不能凭其他已核条目就把待补条目当已核。
- 升级前检查授权、停止、成本、验收与接手；具体做法回 [`stop_conditions/`](../stop_conditions/README.md)，不在阶档复制。goal/eval **如何构造**见 [`agent_goal_eval/`](../../goal_eval_engineering/README.md)。实践控制规程归 [`loop_governance/`](../../../../03_practice/loop_governance/README.md)。

## 二、给学员怎么讲

| 位置 | 学员回答“交出什么” | 教学定位 | 必须带走的限制 |
|---|---|---|---|
| **LE0 人逐次提示** | 人选下一件事、逐次发起与检查 | 起点，非能力阶 | 一次请求中的 Agent 仍可自行读写与用工具 |
| **LE1 有界执行** | 单次运行中，授权面内的工具动作 | 主线 · 一手机制已证 | 动作/目标/时间授权不同；保留高风险审批和中断 |
| **LE2 目标续跑** | 每次结束后是否继续、下一轮怎样推进 | 主线 · 一手机制已证 | 完成条件须可观察；检查完成不等于验收质量 |
| **LE3 定时/事件唤醒** | 什么时候再次起跑 | 主线 · 一手机制已证；持久无人值守为高风险场景 | `/loop` 会话内，云端调度跨会话；后者需状态、取消、上限、升级 |
| **支线 A 多主体编排** | 谁分工、并行、汇总 | 高阶方向 · 部分场景已落地，非必修 | 写入拓扑未收敛；可验证性、所有权与整树预算 |
| **支线 B 改进循环本身** | 谁提议/应用 harness 改动 | 高阶方向 · 工具描述等外围改动有局部实例，核心自改未成熟 | 人改、代理建议、受控应用和改写判据不可混为一谈 |

**教学收口**：前三个交接问题可以循序演示；高阶展示“这条路往哪走、哪些场景可用、我们还不知道什么”，不是保证学完就能无人值守地并发自改。[00-map](00-map.md) 列各档一手锚点、分歧与效果边界。

**结果可信闭环**：主线 LE0→LE3 只解释交出哪些**控制决定**；结果放行还须接通“目标 → 证据 → 裁决 → 停机/交接 → 后验复核”。尤其 LE3 的静默任务要查目标可观察性、证据完整性、裁判可错性、外层预算及取消/接手。先读 [00-map「结果可信闭环」](00-map.md) 的判定，再用 [结果可信闭环交接页](result-reliability-interface.md) 对具体任务逐项检查；goal/eval 如何构造仍在 [agent_goal_eval](../../goal_eval_engineering/README.md)。新增 [Goal/Eval × Loop](goal-eval-axis.md)：按任务目的选择流程、诊断、修复、优化、探索、巡检；G0–G3 解释发现判据、构造交付、判定迭代与校准验收四种能力，外部结果观察另列。支持有界自动探索和过程型交付，LE3 巡检不以业务指标为前提。

### 技术走读索引

每档正文先看**本档独立 SVG**，再读“技术剖面”的输入、状态、判断、执行与退出；表格中的任务示意是教学推演，不伪称产品运行日志。具体产品的参数与默认值仍以链接的一手档案为准。

| 位置 | 运行时重点 | 独立机制图 | 详细档案 |
|---|---|---|---|
| LE0 起点 | 人手动开轮；轮内仍可用工具 | [LE0 图](figures/rung-00-manual-baseline.svg) | [LE0 逐次发起](rung-00-manual-baseline.md) |
| LE1 有界执行 | 工具请求 → allow / sandbox / ask / deny | [LE1 图](figures/rung-01-authorized-execution.svg) | [LE1 授权面](rung-01-authorized-execution.md) |
| LE2 有界续跑 | goal + grader → 继续 / 达成 / 不可能；另有质量验收 | [LE2 图](figures/rung-02-goal-driven.svg) | [LE2 判停链](rung-02-goal-driven.md) |
| LE3 再次唤醒 | session 内 `/loop` 与跨会话 scheduler 各自持有何种状态 | [LE3 图](figures/rung-03-time-event-driven.svg) | [LE3 调度链](rung-03-time-event-driven.md) |
| 支线 A 编排 | 不同写入拓扑、合并与树级成本/取消 | [A 图](figures/branch-a-orchestration.svg) | [A 拓扑案例](branch-a-orchestration.md) |
| 支线 B 元循环 | 规则/判据改动权限幅度、提案与独立评估 | [B 图](figures/branch-b-meta-loop.svg) | [B 改写边界](branch-b-meta-loop.md) |

一手细节见 [运行时证据 W](../raw/evidence-2026-09-30-w-ladder-runtime-detail.md)、[高阶支线证据 X](../raw/evidence-2026-09-30-x-ladder-branches-detail.md) 与 [结果可信证据 Y](../raw/evidence-2026-09-30-y-long-run-result-reliability.md)。图为这些材料的**教学抽象**，不是跨产品 API 的实现图。

## 三、引用与待办

1. [中文视频文字稿](../raw/evidence-2026-09-30-t-shenmejiaoqq-video-zh.md) 属传播侦察级，不进定阶票；未经核对的产品名和“90%”统计不得对外当事实。
2. [evidence-u](../raw/evidence-2026-09-30-u-post-june-kols.md) S4a/S4b 已收 Cursor changelog；官方 [Run Modes docs（evidence-w W1）](../raw/evidence-2026-09-30-w-ladder-runtime-detail.md) 已核 `Run Everything` 与其无 sandbox/classifier 的边界。`File Deletion Protection` 名称仍待单独核验，不作事实引用。
3. LangGraph supervisor 等可补支线 A 拓扑变体；GEPA/DSPy 属提案-评估结构参考，不作为 coding-agent 自改效果证据；NLAH 原文待核。[arXiv:2608.21884](https://arxiv.org/html/2608.21884v2) 的独立性提醒与仓库挖掘口径已补进 [evidence-u S6](../raw/evidence-2026-09-30-u-post-june-kols.md)，不再只引用摘要。
4. 阶档内的 `⏳ 逐字待补` 优先补齐或移出支撑条目；高阶实践准入还需效果、回滚与负例，不以来源数替代。

## 四、文件

| 文件 | 职责 |
|---|---|
| 本 README | 初衷、分工、教学路线、待办 |
| [00-map](00-map.md) | 本区唯一的分层/证据判定与分歧边界 |
| [结果可信闭环交接页](result-reliability-interface.md) | 将目标、证据、裁决、停机/交接、后验复核接成一条可检查的放行链；goal/eval 的构造判读仍在其专项 |
| [Goal/Eval × Loop](goal-eval-axis.md) | 任务目的 × 控制交接 × 判定能力的选择框架；只有步骤、目标难写时的可执行路径、最小协议与三份任务合同 |
| Goal/Eval 三张图：[双轴与组合](figures/goal-eval-dual-axis.svg)、[任务选型](figures/goal-eval-task-selection.svg)、[每轮判定](figures/goal-eval-decision-loop.svg) | 对应综合页 §2、§3、§5；图是正文的教学视图，保留声明边界与未知出口 |
| [LE0 基线](rung-00-manual-baseline.md) | 人手动逐次发起的可演示对照，不是无工具 Agent |
| `rung-01..03-*.md` | 主线三档：LE1 有界执行、LE2 有界目标续跑、LE3 定时/事件唤醒 |
| [branch-a-orchestration](branch-a-orchestration.md) / [branch-b-meta-loop](branch-b-meta-loop.md) | 可选高阶方向：编排与改进循环本身，非 LE3 后必经阶 |
| 六张档内机制图（[LE0](figures/rung-00-manual-baseline.svg)、[LE1](figures/rung-01-authorized-execution.svg)、[LE2](figures/rung-02-goal-driven.svg)、[LE3](figures/rung-03-time-event-driven.svg)、[A](figures/branch-a-orchestration.svg)、[B](figures/branch-b-meta-loop.svg)） | 每档自足呈现运行流程、交接决定与工程风险，细节回档案/证据源 |
| [主图](figures/capability-ladder.svg) / [证据图](figures/ladder-consensus-map.svg) | 前者讲交接路径与分支，后者讲证据覆盖及未成熟之处；图是 00-map 的视图，不是第二权威 |
