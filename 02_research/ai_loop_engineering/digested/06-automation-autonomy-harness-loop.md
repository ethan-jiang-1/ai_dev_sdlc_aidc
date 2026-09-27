# 06 · Automation、Autonomy、Harness 与 Loop：是阶段迁移还是控制面叠加？

> **证据**：[`raw/evidence-2026-09-27-h-automation-to-autonomy.md`](../raw/evidence-2026-09-27-h-automation-to-autonomy.md)（H 路，2024-12 → 2026-09 的一手时间轴与反证）＋
> [`raw/evidence-2026-09-27-g-dsh-control-surface.md`](../raw/evidence-2026-09-27-g-dsh-control-surface.md)（DSH 一手机制）＋
> [`raw/evidence-2026-09-27-e-cross-feature-observability.md`](../raw/evidence-2026-09-27-e-cross-feature-observability.md)（跨 feature 可见性）＋既有 `evidence-a/b/c`。
>
> **证据层级**：本篇主要是 P-existence/P-mechanism（名称、设计与机制存在）；没有把厂商内部评测或个人案例升级成跨组织 P-outcome。

## 一、先给判断

用户的体感抓到了一个真实的控制问题迁移，但“先 automation、后 autonomy；harness 引发 loop”作为单向行业阶段史，目前站不住。更稳妥的判语是：

> **模型能力、产品原语和失败/验证压力共同把控制对象逐层外移并叠加：automation 负责触发和执行动作；autonomy 允许系统在目标与边界内选择下一步；harness 把单次运行的 context、工具、权限、状态、验证和恢复托住；loop engineering 再把多轮取题、反馈、停止、记忆、调度和人介入设计成一个控制面。**

这是一张**接口依赖图**，不是已被历史数据证明的因果链。loop 的机制早于 2026 年命名；harness 与 loop 更像共同演化、互相暴露接口，而不是前者单独导致后者。

## 二、四个词不要压成一条线

| 概念 | 本篇最小含义 | 它控制的对象 | 不等于什么 |
|---|---|---|---|
| **Automation** | 预先写好的 trigger、规则或固定路径自动执行动作 | 什么时候触发、动作怎么自动跑 | 不等于理解目标、选择策略或判断质量 |
| **Autonomy** | 在目标、范围和约束内，系统根据状态/环境反馈选择下一步、工具、子任务或是否继续 | 下一步决策权与继续/升级权 | 不等于无人监督、正确、安全或跨 session 持续 |
| **Harness** | 包围模型的运行环境与控制面：context、工具、权限、sandbox、日志、状态、测试、评估、hooks、恢复 | 单次运行如何可观察、可约束、可验证、可恢复 | 不等于自动取题，也不等于跨 feature 调度 |
| **Loop** | 触发 → 反复行动 → 反馈/验证 → 状态记忆 → 停止/继续 | 多轮控制与反馈闭环；可进一步加外层调度 | 不等于无限重试、定时任务、自动批准或“模型说 done” |
| **Loop engineering** | 把取题、授权、执行、验证、记忆、停止、升级和复盘从人的逐轮 prompt 中外置成系统 | 循环的控制分配和长期运行 | 不是统一标准；Osmani、LangChain、Claude Code 的外延不完全相同 |

一个定时 automation 可以没有 autonomy；一个单 session loop 可以没有跨 feature scheduler；一个成熟 harness 也可以只服务一次调用。四者是正交但可组合的控制面。

## 三、时间顺序：先有构件，再有命名

| 时间 | 一手材料 | 研究意义 |
|---|---|---|
| 2024-12 | Anthropic《Building effective agents》：workflow 是预定义路径，agent 动态决定过程和工具；环境反馈、循环、停止上限和人类 checkpoint 同时出现 | automation 与 autonomy 从一开始就并存，不是互斥阶段 |
| 2025-07 | Huntley 的 Ralph：Bash while loop、back pressure、外置 TODO/spec、每轮测试，但停止依赖人工 taste，适用 greenfield | loop 构件先于“loop engineering”命名存在；自动运行仍可能脆弱 |
| 2025-11 | Anthropic 长程 harness：initializer/coding agent、feature list、progress、git、增量工作和端到端验收 | 长程自主失败暴露跨 context 状态、取题顺序、提前完成和验证问题；harness 把控制点外置 |
| 2026-02 | Boris Cherny 的 YC transcript：spec+Asana、spawn agents、几天无人干预，但 transcript 中 `loop` 出现 0 次 | 同构实践可以先用 swarm/spec/agent 语言存在，名称后贴上去 |
| 2026-06 | Osmani：loop 被定义为替代人逐轮 prompt 的系统，并称其“one floor above the harness”；LangChain 与 Claude Code 随后分别体系化/产品化 | 新标签把既有构件组合成一个可讨论、可销售、可设计的控制层 |

**时间顺序支持“harness 让 loop 更可设计/更可见”这一机制解释；不支持“harness 是 loop 的充分原因”。**

## 四、当前最强的解释与竞争解释

### H1：控制面逐层外移（当前首选解释）

早期自动化主要替人执行固定动作；模型能处理更长目标后，人把部分下一步选择交给 agent；自主运行暴露了上下文丢失、权限、验证、恢复和提前完成问题，于是 harness 变成单次运行的环境控制面；当单次运行可以持续接续，跨轮的取题、调度、停止和升级才成为显性 loop 问题。

**支持**：Anthropic 2024 的 agent/environment feedback；Anthropic 2025 的长程失败与 harness；Osmani 2026 对 loop/harness 层次的明确说法；DSH `goal`/driver 与 `todo`/`plan` 的边界。

**限制**：这是机制依赖图，不是历史因果证明。

### H2：重命名与产品化

Ralph、tool-calling loop、evaluator-optimizer、progress file、event trigger 早已存在；2026-06 只是 Osmani、LangChain、Claude Code 把不同构件聚拢成 loop engineering 语言。不同作者还对“改 harness 是否属于 loop”“外层调度是否必需”意见不一，说明它仍含有显著的命名和话语层。

### H3：失败模式驱动

驱动力不是模型从 automation 变成 autonomy，而是 agent 产码速度超过人的 review 能力，并暴露失忆、空转、提前完成、危险动作和行为遗漏。于是工程实践把同步逐行动审阅换成机械门、熔断、独立 checker 和异步状态，但仍保留高风险/模糊意图/最终质量的人介入。

### H4：产品能力同步演进

Claude Code、Codex、OpenClaw 等产品把 automation、worktree、skills、connector、sub-agent、goal、schedule、task ledger 同期产品化。使用者感受到的是组合能力的形状，而不一定是一条统一阶段史。

## 五、DSH 为什么会产生这种体感

DSH 的一手机制正好落在“有执行 loop，但没有完整 feature control plane”的位置：

1. `dsh-goal` 支持一个 session 的一个长期目标，跨 turns、resume、fork 和 restart 持久化；`goal-round-driver` 在目标 active、armed、agent idle 时续轮。
2. `goal-round-driver` 明确是 same-session continuation，不负责新 agent、并行目标、Ralph 式独立尝试或异常自动重试；`dsh-goal` 也明写 stores goal state but does not schedule work。
3. `todo` 是 session-level task list，`plan` 是执行前的设计/呈批引导；session persistence 可靠地保存事件，但没有 feature、priority、authorized、in_progress、blocked、accepted、rolled_back 的通用跨 feature 工作语义。
4. 因此 DSH 让“目标驱动的单项执行与续轮”变得自然，却没有自动替插件仓建立一个 OpenSpec 式的全局 feature ledger。你从 SDD 过来时，缺的不是 agent 能不能继续跑，而是候选、授权、次序、在途、阻塞、验收和变更历史是否在一个外部控制面中可见。

这解释了“跑得动但看不清”的体感：**自治被增强了，控制可见性没有等比例增强。**

## 六、与 harness / SDD 的关系

- **Harness**：先把单次运行托住。它回答“模型看到什么、能做什么、哪些动作被拦、结果如何验证、崩溃后怎么恢复”。
- **Loop**：再把多轮运行组织起来。它回答“下一轮为什么启动、下一项从哪里来、何时停止、谁升级、状态如何接续”。
- **SDD**：提供变更/意图/任务/验收的外部产物。它可以成为 loop 的工作来源、状态记忆和验收依据，但不是 loop 的对立面。

因此用户从 SDD 到 DSH 的感觉不是“SDD 被 automation 取代”，而是**原来由 SDD 产物显性承担的工作控制面，在 DSH 中部分落到 goal/对话/agent 临时判断上，而 DSH 原生没有替插件仓补齐 feature-level ledger**。这也是为什么后续 `loop_governance` 需要和 `harness_governance` 成对，而不应吞掉 `spec_driven_development`。

## 七、还不能说什么

1. 不能说 automation 已被 autonomy 取代；自动触发、自动执行、模型自主选择和系统自主继续是不同维度。
2. 不能说 harness engineering 引发了 loop engineering；loop 构件早于命名，且 Ralph 等实践没有成熟 harness 也能运行。
3. 不能说 harness 或 loop 已证明提升 coding quality、减少返工或提高吞吐；当前主要是设计/机制证据，真实 P-outcome 不足。
4. 不能说人退出系统；现有材料反复保留高风险动作、模糊意图、最终验收、品味/体验和熔断升级的人类责任。
5. 不能把 durable memory 写成 feature queue；DSH goal/session log、Anthropic progress、Managed Agents session、OpenClaw task ledger 解决的是不同尺度的记忆/在途问题。

## 八、下一步可检验命题

- 在同一 DSH feature 上对照：单轮 automation、`goal` bounded autonomy、外置 feature ledger + `goal` + 独立 checker，记录下一项选择、目标漂移、提前完成、返工、人工介入和成本。
- 对照逐层加 harness：权限/sandbox → 外部状态 → 机器验证 → 调度器，观察 loop 是否更可见，同时记录新增复杂度和错误复制。
- 把动作面安全（auto mode/auto-review 的 deny）与行为面正确（feature/spec/browser/E2E 验收）分开计量。
- 用跨 feature 的 current pointer、blocked reason、accepted/rolled-back、priority change 作为观察单位，检验单 session loop 是否真正升级为组织级 autonomous workflow。

**本篇判定强度**：概念/机制为中高置信；“harness 放大 loop 可设计性”为中置信机制解释；行业阶段史、效果、采用率为开放问题。
