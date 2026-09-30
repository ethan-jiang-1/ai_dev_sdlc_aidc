# 00-map — 六源阶梯对照矩阵（定阶判定权威）

> **本文件是 capability_ladder 的判定权威**：哪几阶是共识阶（正式阶）、哪几阶待定（候选阶），以此表为准。
> 每格是该来源的阶梯在对应交接面上的**占位**，一句话版本——逐字与细节在其锚定的 evidence 档案，此处不复制。
> 观测基线：2026-09-30（六源均已回源，唯 Cursor 官方 docs 与 Anthropic multi-agent 尚无独立档案）。

## 一、六源是什么（含一个关键区分）

六副"阶梯"其实分两类，混排会假性冲突：

- **运行模式阶梯**（A 类）：按"循环怎么被触发/被授权"切级——Osmani、CC 团队、Morris、视频三层。
- **环类型学**（B 类）：按"存在哪几种环"分类——Runkle 四环、Ng 三环。B 类不是升级路径，但每个环在 A 类阶梯上有对应落位；落位本身就是本表要做的对照。

| 来源 | 类型 | 阶梯原位（一句话版） | 锚 |
|---|---|---|---|
| **Osmani** 四级运行模式 | A | agentic loop → `/goal` → `/loop`/`schedule` → proactive 无人值守 | [evidence-a](../raw/evidence-2026-09-26-a-originators.md) |
| **CC 团队** 四类循环 | A | turn-based / goal-based / time-based / proactive | [evidence-a](../raw/evidence-2026-09-26-a-originators.md)（D3 逐字核验） |
| **Kief Morris** 四级阶梯 | A | outside the loop → in the loop → on the loop → agentic flywheel | [evidence-c](../raw/evidence-2026-09-26-c-autonomy-and-convergence.md)；卡片 [`_raw_kol/10`](../../01_sources/reference/kol/_raw_kol/10_kief_morris.md)（卡片为三档版，待修订） |
| **Runkle** 四环模型 | B | agent loop → verification loop → event-driven loop → hill-climbing loop | [evidence-b §4e](../raw/evidence-2026-09-26-b-stop-and-scheduling.md) |
| **Ng** 三环嵌套 | B | agentic coding → developer feedback → external feedback（外环修正内环方向） | [evidence-a](../raw/evidence-2026-09-26-a-originators.md)；判读 [`digested/08`](../digested/08-kol-alignment-andrew-ng.md) |
| **视频三层**（为什么叫QQ，中文传播层） | A | 测试驱动自纠正 → goal＋记忆持久化 → 动态工作流并发择优 | [evidence-t](../raw/evidence-2026-09-30-t-shenmejiaoqq-video-zh.md)（侦察级） |

## 二、对照矩阵

| 阶（交接面） | Osmani | CC 团队 | Morris | Runkle | Ng | 视频三层 | 收敛判定 |
|---|---|---|---|---|---|---|---|
| **R1 授权执行**（单轮内工具/命令权） | 一级 agentic loop | turn-based | outside→in（人仍方向盘） | agent loop（授权面未展开） | 内环：agentic coding | 一层：Run Mode/Allowlist＋测试门 | **5/6 落位** |
| **R2 目标驱动**（多轮路径，人只给可观察完成条件） | 二级 `/goal` | goal-based | in→on（人退到指导位） | verification loop（闸门形态） | 内环核心 | 二层：`/goal`＋记忆持久化 | **6/6 落位，最稳** |
| **R3 时间/事件驱动**（"开不开跑"也交出） | 三级 `/loop`/`schedule`＋四级 proactive | time-based / proactive | on the loop（人只管边界） | event-driven loop | —（Ng 环是反馈环，无触发维度） | **缺位** | **3/6 显式落位**；Ng 不适用；视频跳过 |
| **R4 编排与并发**（任务分解/子代理调度权） | —（四级止于触发方式） | —（四类皆单循环） | —（flywheel 是自转不是编排） | —（四环无编排环） | — | 三层：fan-out＋对抗验证＋大小模型分层 | **2026-09-30 升正式**：概念位 1 票（视频）＋机制票 3 张（Anthropic 编排器-工人 / Cognition 写单线程 / Carlini 文件锁）＋学术构件票（verifier sub-agents）——见 [evidence-u](../raw/evidence-2026-09-30-u-post-june-kols.md) |
| **R5 自我改进**（改写 harness 本身的权） | — | — | flywheel（"改写 harness 本身"最接近——见下注） | hill-climbing loop（"return arrow reaches inside and updates the agent loop directly"） | 外环修正内环方向（人执行，非 agent） | — | **2026-09-30 升正式**：3 概念源落位（Runkle/Morris/Böckeler）＋实证票（Anthropic 改写工具描述 -40%）＋操作素材已按自说明落齐（[rung-05](rung-05-self-improvement.md)）——护栏随改写幅度递增 |

> **Morris flywheel 归位注**：flywheel 的原文落点是"循环改进循环"，与 Runkle hill-climbing 同指 R5；
> 但 Morris 卡片还是三档旧版（四级修订待办在 [`_raw_kol/10`](../../01_sources/reference/kol/_raw_kol/10_kief_morris.md)），归位按 evidence-c 定性，修订后再固化。

## 三、判读（候选判读——升 digested 前不外传）

1. **R1/R2 是共识阶**（≥5 源落位），**R3 是共识阶**（3 源显式＋Cursor `/loop` 官方语义第二票，evidence-u S4b），→ 立正式阶。
2. **R4 已升正式（2026-09-30，evidence-u 三票＋学术票）**，但升格同时**收窄形态**：共识不是"任意并发"，
   是 Walden 的 **"writes stay single-threaded, agents contribute intelligence rather than actions"**；
   拓扑收敛于 map-reduce-and-manage（Cognition）与 orchestrator-worker（Anthropic）两种，无编排器的文件锁同步（Carlini）是第三变体；
   unstructured swarm 被明确判为 distraction。原"R4 是框架能力非概念共识"的判断**部分修正**：概念共识形成于词源周前后半年内
   （Anthropic 2025-06 提供机制谱系，2026 上半年三家独立收敛），它是一张**正在固化的阶**。
3. **R5 维持候选**：概念票 2（Runkle hill-climbing、Morris flywheel）＋实证票 1（Anthropic 改写工具描述 -40%），
   但操作层素材（GEPA/DSPy 保护链）尚未按自说明格式搬运；且改写幅度有光谱（外围件→循环结构），升格前先把光谱画清。
4. **阶梯的两类之分本身是发现**：A 类（运行模式）与 B 类（环类型）被混引时会产生假性分歧——
   digested/01 的"外延不兼容"结论，落到阶位上有一部分其实是**维度错位**而非真分歧。此项为回流候选（→ digested/01）。
5. **视频三层跳过 R3**（从 goal 直接跳编排）——中文传播层对"无人值守/熔断"这个最危险的交接面**没有切片**；
   传播完整性视角的观察，记在 [evidence-t](../raw/evidence-2026-09-30-t-shenmejiaoqq-video-zh.md) 侧，不在本表展开。

## 四、分歧带（dissent——允许与主流阶序不一致的声音，教学时必须并列给出）

> 用户 2026-09-30 定调：可以有不同意见，总趋势一致就好。分歧不是阶梯的敌人，是**阶与阶之间"清晰界限"的磨刀石**。

| 分歧者 | 主张（逐字见 evidence 档案） | 针对哪阶 | 对阶梯的修正意义 |
|---|---|---|---|
| **Steinberger**（2025-12-28 长文） | "usually I'm the bottleneck"——反对自动编排（evidence-a 在案） | R3–R5 | 阶梯不是单向自动扶梯：**升阶是可逆决策**，品味密集的活随时退回低阶 |
| **Ronacher**（2026-06-23《The Coming Loop》） | "The more hands-off you are, the more that happens"（放权放大防御性代码）；"My role is reduced to that of a messenger"；认知依赖不可逆；但"the question is not whether we will loop"（趋势确认） | 全梯，火力集中在 R3+ | 每阶要教**人的角色成本**；适用域边界——长寿命/品味密集代码不宜满放权（"artifacts without necessity of longevity"才适合循环） |
| **Walden/Cognition**（2025-06 → 2026-04 演化） | 从"别建多代理"到"写入单线程"——**修正而不是撤回** | R4 | R4 的共识形态是**受约束的并发**；unstructured swarm 是 distraction |
| **Carlini**（2026-02-05） | "it is easy to see tests pass and assume the job is done, when this is rarely the case" | R2/R4 | 升阶闸门（verifier）本身有失效率——闸门质量是工作量主体 |
| **arXiv 实证**（2026-08，217/256 仓库） | "almost none commits the state files the discourse prescribes" | R3 | 话语共识≠工程现实：** discourse 里的构件（state files）在真实仓库几乎缺席**——阶梯教的是应然，实然缺口恰恰在 R3 的可观察性上 |

| **Cherny**（2026-02-17 YC 访谈，[evidence-a §1b A3](../raw/evidence-2026-09-26-a-originators.md)） | "you can improve performance maybe 10, 20% … essentially **the gain is wiped out with the next model**. … never bet against the model" | R5（延伸至全梯） | loop 配置本身也是 scaffolding，随模型换代贬值——本阶投资回报有内在折扣 |
| **Horthy**（12-factor agents，[evidence-i Source 2](../raw/evidence-2026-09-27-i-high-influence-control.md)） | "the number one feature request … we need to be able to **interrupt a working agent and resume later**, ESPECIALLY between the moment of tool selection and the moment of tool invocation" | R1–R3 | 控制流必须归人；打断点是设计要件而非事后补救 |
| **marmelab 引实测**（arXiv 2608.27443，[evidence-c 4a.1](../raw/evidence-2026-09-26-c-autonomy-and-convergence.md)） | "The rule writers blocked 20.1 percentage points fewer bad actions … **93% of permission prompts get approved**. **A rule that ends in a prompt isn't a rule.**" | R1 | 授权面写了没人执行是实测结论——机械门替代文档门的实证理由 |

**逐阶配对**（诚实的爬梯叙事每阶带一条对应 dissent）：R1↔预写规则证伪（93% 顺手放行）· R2↔"AI 生成的测试还不够好"＋自反思放大故障（ReliabilityBench −0.50）· R3↔"unattended 即 unguarded"＋done 只是声明 · R4↔"multi-agent 至今是 open question"（Anthropic 2025-11）＋红队可误导审批代理 · R5↔Goodhart/self-preference/43×＋NLAH 反直觉 ablation。

**总趋势判定（本区一句话）**：分歧行全部针对**升阶的速度与适用域**，没有一条否认**阶序本身**——
"从授权执行到目标驱动到触发外移"的方向在六概念源＋五机制源＋一学术源中无反向案例。阶梯成立，争论在坡度。

## 五、R0（基线，非阶）

"人肉 API"是所有来源共同的**反面起点**（提示→等待→读→再提示），不是能力阶，不设档。
它在叙事上的作用：定义"交出"的零点——R1 起每一阶的"交出什么"都相对 R0 度量。
