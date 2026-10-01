# Loop Governance 实践主干（定稿层·总纲）

> **本文件是什么**：loop 层（五层框架第 4 层）的实践主干，**§0–§6 共七节**——§0 定义与判据、§1–§4 核心四段（停止条件 / 外层调度 / 自主度分档 / 检查点）、§5 接口、§6 升格依据；
> 每条带源强度与证据指针（指向研究层 evidence 档案与判读篇，**本主题不复制证据**）。
> 手册级操作规程（SOP / 模板 / 选型表展开）在 [`manual.md`](manual.md)——12 节，与本主干同日成稿。

```yaml
topic: Loop Governance —— loop 层的实践主干（Prompt → Context → Harness → Loop → Graph 第 4 层）
doc_layer: result（定稿层 · 总纲，清单级）
produced_at: 2026-09-26
provenance: 2026-09-26 立题＝研究层 evidence-a/b/c + digested 01/03/05；2026-09-27 补充＝evidence-f/i 的机制及限定性反例 + digested/03/07 的边界；后续控制接口引自 agent_goal_eval 的 digested/01/02/03（单源处标注）；用户决定立题并授权命名
filter: ≥2 独立一手来源 → 主干；单源强实践 → 标注"单源"；未收敛点 → 如实标注为设计空间或开放缺口，不冒充共识
evidence_home: 02_research/01_agent_engineering/loop_engineering（循环机制）+ 02_research/01_agent_engineering/goal_eval_engineering（goal/eval 构造）；本主题不建 research/ 层，防双权威
naming: 不沿用 KOL 词 "loop engineering"——词源＝热度碎片、外延未收敛（判定见研究层 digested/01）；按仓库五层框架命名，与 harness_governance 同构成对（环境轴 / 控制轴）
---
```

## 0. 这层管什么（定义与判据）

**Loop 层管"怎么回头"：让上次结果改变下次行动。**（四要素与两判据的权威表述在研究层 [`digested/01 §三`](../../../02_research/01_agent_engineering/loop_engineering/digested/01-命名谱系.md)，框架源出主线 talk storyline；前提链见 §5）

**四要素**：**触发 · 验证 · 停止条件 · 记忆**——触发＝什么开下一轮；验证＝拿什么判这轮好坏；停止条件＝跑到哪算完；记忆＝跨轮状态放哪。

**两个硬判据（什么不算 loop）**：

1. **停止条件不依赖上次结果 → 那是重试，不是 loop**（[`digested/01 §三`](../../../02_research/01_agent_engineering/loop_engineering/digested/01-命名谱系.md) 硬判据）；
2. **单次运行不受控 → loop 只是把错误复制得更快**——与 Ralph 的 greenfield 限定（"There's no way in heck would I use Ralph in an existing code base"，evidence-b §1）、Anthropic 的"每轮先过基线再干活"（evidence-b 问题2 §1）三方同向。

**术语注记**：KOL 词 "loop engineering"（2026-06 命名）经研究层回源判定——**词源＝热度碎片（Cherny 06-02 访谈句未逐字核验、Steinberger 06-08 两句话推文无深度），定义＝事后工程化（Osmani 06-07 → Runkle 06-16 → CC 团队 06-30）**；四人核心同指（系统替人逐轮提示）但**外延不兼容**（Runkle 第 4 环属 harness 层；验证语义分歧）。本主题因此不沿用该词。判定全文：[`digested/01`](../../../02_research/01_agent_engineering/loop_engineering/digested/01-命名谱系.md)。

### 0.2 loop 层失败模式（诊断轴——各节的"防什么"标签）

| 失败模式 | 症状 | 主要由哪些节填 |
|---|---|---|
| ① 重试冒充循环 | 停止条件不看上一轮结果，原地空转 | 判据一（§0）；manual §1 |
| ② 错误复制机 | 单次运行不受控就开循环，错误滚雪球 | 判据二（§0）；manual §9 升档前置 |
| ③ one-shot 冲动 | agent 试图一次做完所有 | §2 一次一件；manual §5 |
| ④ 提前宣告完成 | "declares victory on the entire project too early" | §1 三件骨架；manual §2/§5 |
| ⑤ 未验证标 done | 单测或 curl 过就翻 passes | §1 骨架一/三；manual §5/§10 |
| ⑥ 无进度盘 | 跨轮状态只在人的记忆里，退化为对话催促 | §2 形态一；manual §5 |
| ⑦ 自主度超前 | 门禁还不会红就把人撤出循环 | §3 升档判据；manual §9 |
| ⑧ 操纵裁判 | agent 改测试 / 绕审批 / 哄评估器 | §1 保护裁判；manual §4/§7 |
| ⑨ 授权漂移 / 升级不可达 | 旧批准被拿来执行新动作，或拒绝后无人能接手 | §3 控制路径；manual §7/§9 |
| ⑩ 资源停机冒充验收 | 超时、拒绝或模型收尾被写成任务完成 | §1 停止与验收分离；manual §7/§10 |

（①② 是 §0 两判据的失败面；③④⑤ 来自 Anthropic 官方失败模式表，evidence-b §3；⑥ 的私有一手样本见姊妹仓 FAQ 15 owner 案例·转引；⑦ 由 §3 升档判据推出；⑧ 来自保护裁判与反操纵监控的一手证据——evidence-b §3 测试不可删改 / §4b reasoning-blind / §2.3 反复拒绝熔断；⑨ 是 evidence-f 的源码/文档机制与单用户反例导出的试点检查；⑩ 区分资源上限与任务验收，见 digested/07 停止格。）

## 1. 停止条件（跑到哪算完）

**目标敌人**：**提前宣告完成**。Anthropic 官方把两种头号失败模式写成表格——"Claude declares victory on the entire project too early" / "Claude marks features as done prematurely"（evidence-b §3）；LangChain verification loop 的存在理由同源；Huntley 的对应物是占位实现（"inherent bias to do minimal and placeholder implementations"，evidence-b §1）。**停止条件的全部设计都是在对抗这一条。**

**三件骨架（各 ≥2 独立一手同向，判定见 [`digested/03`](../../../02_research/01_agent_engineering/loop_engineering/digested/03-构件.md) §一）**：

1. **机器可核判据做逐轮闸门**——back pressure（类型 / 测试 / linter / 静态分析 / 安全扫描，evidence-b §1）/ grader（deterministic 优先，agentic/LLM-as-judge 慎用——它是评分不是闸门，evidence-b §4e）。
2. **硬性熔断上限做兜底**——把轮次 / 时间 / 拒绝计数写进条件（`or stop after 20 turns`）；auto mode 3 连拒 / 20 总拒停机；`/loop` 7 天硬过期（"bounds how long a forgotten loop can run"）。（evidence-b §4a/4b/4c）
3. **验收与干活分离**——五处一手跨三家：evaluator-optimizer、"只许改 `passes` 字段"、"/goal adds a separate evaluator… completion is decided by a fresh model rather than the one doing the work"、"The separation of roles matters"、grader 与 agent 分置。（evidence-b 综合节）

**停止原因不等于完成证据**：轮次耗尽、超时、连续拒绝、模型返回消息只说明控制流停止或交还；是否验收仍由预定的检查者和证据决定。长程任务的交接记录应把两者分开（[`digested/07` 停止格](../../../02_research/01_agent_engineering/loop_engineering/digested/07-控制问题矩阵.md)；记录写法见 [`manual.md §7`](manual.md)）。

**产出边界不等于外部结果**：可观察的代码、测试或交付物可作为本轮自动停止条件；系统外的业务结果若当前无观测，就保留待人判或待观测，不能因为产出过闸而自动标成结果达成。品味/标准仍在变化时可做有边界的探索与人工检查，不冒充机器可判的 `Met`。这是控制边界，不在本主题定义 goal/eval 的写法；出处为 [`agent_goal_eval` goal 判读](../../../02_research/01_agent_engineering/goal_eval_engineering/digested/01-goal-构造.md) 与 [`难设计` 三条路](../../../02_research/01_agent_engineering/goal_eval_engineering/digested/03-难设计.md)（其中结果不可见的交还属 Yeret 单人观察，非效果证明），操作分支见 [`manual.md §2`](manual.md)。

**写法（CC 官方三要素，一手）**：**一个可度量终态 + 一个声明式检查 + 路径约束**（"`npm test` exits 0"、"no other test file is modified"，evidence-b §4a）。**实践例证**：Jesse Vincent 的 `/goal` 实验（过夜 25 实验那例——**中文转述·非逐字**，仅作用法样本，不作独立收敛依据；[`fable5/run_superpowers_jesse_vincent`](../../../01_sources/field_samples/fable5/run_superpowers_jesse_vincent/quotes.md)）。
停止条件是**三值状态机**（Not yet met / Met / Impossible），不是布尔（evidence-b §4a）；Osmani 澄清：`/goal` 评估器**只核 transcript 硬规则、不判内容好坏**（evidence-a）——判好坏的是人或上级环。

**裁判权选型**（研究层确认的未收敛点——这里是设计空间，不是缺口）：五型裁判（人判 taste／文件清单逐条／独立小模型每轮／干活模型自判——**最弱**，须配本节骨架二、三与 [`manual.md §4/§7`](manual.md) 补偿／审批对方判定）的**选型表（适用场景＋成本/风险＋源）在 [`manual.md §3`](manual.md)**——单一事实源，此处不复制。

**保护裁判（"agent 修代码时不得削弱对代码的检查"一族）**：测试不可删改 + JSON 选型防整文件改写（Anthropic，单源但机制成型）；评估器输入防操纵（auto mode 分类器 "reasoning-blind by design"）；Ralph 防作弊条款——测试当场写明**为什么存在**，因为 "future loops will not have the reasoning in their context window"（evidence-b §1）。

## 2. 外层调度（下一轮跑什么、何时跑）

**主导形态一：文件即队列。**（Huntley 与 Anthropic 两家独立、句式同构）

- **三件套**：进度规格（feature_list.json / fix_plan.md / loop.md）＋ 叙事日志（progress 文件）＋ git 历史；
- **每轮冷启动重读 + 固定开场序列**：定位 → 读 git log / progress → **选清单里最高优先级的未完成项** → 先过基线再干活（evidence-b 问题2 §1/§4）；
- **在这个文件队列形态中**，下一项从进度规格里的未完成条目取；人可改变清单及优先级，不能把“从文件取题”外推为所有 loop 都不需人决定下一轮；
- 一次只做一件 + 干净收尾（commit + progress 更新）——对抗 one-shot 冲动（Anthropic 点名的失败模式一）。

**主导形态二：触发器即节拍。**条件驱动（`/goal`）/ 时间驱动（`/loop`、cron、Routines——间隔可固定、可模型自选、可 loop.md 定制）/ 事件驱动（webhook，LangChain event-driven loop）/ 脚本驱动（Stop hook）。`/loop` 的内置维护 prompt 是"下一件工作"的清单化变体：固定优先级（未完工作 → PR 偶发维护 → 清理），且**不在该范围外开新动作**（evidence-b §4c）。

**审批作为独立角色**：auto mode 分类器与 OpenAI auto-review 都把"越界判定"做成**独立模型调用**——主 agent 有把审批边界当障碍绕过的压力，所以判定必须分离（"The separation of roles matters"）。单次拒绝**不终止循环**：deny-and-continue，拒绝带理由回给模型换安全路径（过半场景模型自找替代路径，evidence-b §4b/4d）。

**人的位置**：部分公开机制将逐动作同步审批移到风险动作、关键歧义和熔断等检查点；这不证明真实组织里人工审批已退出调度回路（[`digested/03 §二`](../../../02_research/01_agent_engineering/loop_engineering/digested/03-构件.md)）。自动拒绝也不等于有人能接手，升级入口须在具体运行方式中走通。

**外层的接口化（前沿形态）**：Managed Agents 把 session log 独立于 harness 存活，`wake(sessionId)` 从最后事件恢复——"外层"本身正在成为可调用的接口（evidence-b §5，单源·标注）。

**开放缺口（如实登记，与 §3「量化分档未成型」同格式）**：**跨 feature 的在途可见性与逐 feature 验证汇总**——已复核的材料尚未给出同时覆盖授权史、priority 变更、业务阻塞和跨 feature 验收的统一做法（单任务 progress 文件不能替代）。队列与次序有覆盖（本节形态一），在途控制面仍待验证，不冒充行业共识。

**待验证的补法，不是已证规范**：当多项工作同时在途且交接反复丢授权、优先级或验收信息时，可在现有进度文件之外试一行 feature 控制记录；只记工作来源、授权变更、优先级变更、阻塞原因及验收指针，不替代单任务的 feature_list / progress / git。字段和退出条件在 [`manual.md §5`](manual.md)，缺口边界见 [`digested/07 §一`](../../../02_research/01_agent_engineering/loop_engineering/digested/07-控制问题矩阵.md)。尚无对照证明该记录能减少催问或返工。

## 3. 自主度阶梯（人在哪一站、什么时候升档）

**位置分档（已成型）**——两个独立四级阶梯 + 一条官方路径：

| 阶梯 | 档位 | 源 |
|---|---|---|
| Kief Morris | outside → **in** the loop → **on** the loop → agentic flywheel（on＝修 harness 不修产物） | evidence-c |
| Addy Osmani | agentic loop（人写每轮）→ `/goal`（评估器）→ `/loop`（间隔）→ **proactive**（事件触发无人值守） | evidence-a |
| Anthropic playbook | 逐手 prompt → 门禁审阅 → auto-accept → 并行 worktree → **"building and monitoring loops"** | [`anthropic_ai_sdlc/org`](../../../02_research/02_ai_sdlc/02_industry_playbooks/anthropic/org/ai-native-sdlc-playbook.md) |

σ 分层是事件驱动判据的成品样本：**1σ 只记录 / 2σ 只读诊断 / 3σ 限界行动**（只许开 PR 或触发预批 runbook），且**检测全程确定性、模型不参与**（同上）。

**量化分档（未成型——登记为开放缺口，不冒充共识）**：**没有任何一手源给出"跑几轮必须人看"的轮次判据**；现行判据全部事件驱动（风险分数门槛 / 关键歧义触发 / 破坏性动作类别 / σ 分层 / auto-review 停机阈值）。行为面验证被 Böckeler 点名为"减监督"路线的公认短板——**门拦得住动作，拦不住"没做该做的事"**（evidence-c）。

**升档判据**：**机械门可信度决定可授权的自主度**——门会红才配当门（负例控制，衔接 [`harness_governance` 回路 1](../../harness_governance/result/backbone.md)）；门不可信时升档＝把错误复制得更快（本主干 §0 判据 2）。若裁判与指定的人工验收者对同一产出给出冲突判定，暂停自动升档及该产出的自动验收，先由人核对分歧和成功定义；修订后再用可比样本复核，不靠模型自报或提高轮次上限通过。这是借 [`agent_goal_eval` eval 判读](../../../02_research/01_agent_engineering/goal_eval_engineering/digested/02-eval-调优.md) 做的控制门；分歧处理建议出自 Hamel/Shankar 单源 FAQ，**没有前后效果对照，也没有通用一致率阈值**（[`manual.md §9/§10`](manual.md)）。

**升档还须查控制路径**：一次批准绑定本次动作、目标和有效期；下一轮不自动继承到另一分支、另一 feature 或发布动作。对可审批的中断要验证人能看到动作和风险、作决定、从同一状态恢复；对硬政策拒绝只停下并暴露原因，不通过人工提示绕过。动作门和恢复机制见 [`digested/03 §三`](../../../02_research/01_agent_engineering/loop_engineering/digested/03-构件.md) 与 [`evidence-f` Sources 1/7](../../../02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-27-f-autonomy-gates.md)；授权漂移/审批不可达只有单用户反例，不是发生率证据。操作检查在 [`manual.md §9`](manual.md)，动作授权面的划定规程（LE1 交接面的操作化）在 [`manual.md §13`](manual.md)；沙箱与工具策略本身仍归 harness 治理。

**反面声音（一手）**：Steinberger 2025-12 长文明确反对自动编排（"usually I'm the bottleneck"）——与他的 6 月词源推文立场相反（evidence-a）。**自主度升档不是免费的方向**；词源人物自己的摇摆就是证据。

## 4. 检查点与反例（什么时候必须人看 / 什么时候不要 loop）

1. **在 playbook 描述的阶段门集中注意力**："Human attention concentrates at the gates, reviewing what the agent flagged rather than starting each stage from scratch"（playbook）。这是该做法对阶段审阅位置的建议，不等于所有团队都撤掉了逐动作审批；会话内风险动作仍可按 §2 的 ask 规则暂停并交人。
2. **风险分级保留人审**：auth / billing / 破坏性变更 + 回滚计划（引用 [`harness_governance` 组织 6](../../harness_governance/result/backbone.md)，不重复）。
3. **假把控的两面镜**：SDD 侧 "False Sense of Security"（agent 把 verify implementation 标 done 却零单测，marmelab 2025-11-12——**注意出处修正**，evidence-c）↔ loop 侧没有进度盘时退回人的工作记忆与对话催促。**真实把控＝机器可查的门 + 少量真人在环点。**
4. **什么时候不要 loop**：单次小任务（为它建循环脚手架是过度工程）；brownfield 慎用无限循环（Ralph 自限 greenfield）；**先有真实失控，再上循环治理**（对齐 harness_governance 反过度工程条）。
5. **非保证声明要跟着走**："Auto-review should not be treated as a guarantee of security"（OpenAI 官方自述）——机械门自身也是攻击面（DSH 的 CVE-2026-82533 样本，**转引·待回源**——见姊妹仓 FAQ 15，未独立回源前不作主张依据）。
6. **行为面交接异常**：测试被删/关/弱化、额外做了未授权功能、失败测试未说明，都先暂停标完成并转交独立核对（[`evidence-i` Beck/Yegge](../../../02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-27-i-high-influence-control.md)，两个第一人称案例，无效果对照）。测试保护由 harness 执行；本层只管轮末是否继续和谁接手，见 [`manual.md §10`](manual.md)。

## 5. 与兄弟主题的接口

| 主题 | 关系 |
|---|---|
| [`harness_governance`](../../harness_governance/README.md) | **前提层**：单次运行受控（门禁/传感器/漂移清理在那边，诊断轴＝"agent 缺哪句话"①–⑦）。本主题引用其回路 1（门禁可信度）/5（评审外置）/7（反馈分层）与组织 6（风险分级），不复制 |
| [`spec_driven_development`](../../spec_driven_development/README.md) | **收敛证据**：OpenSpec 拆刚性阶段（"No more rigid phases"）、spec-kit 收 Ralph Loop extension 与 Autonomous Run Governance preset；SDD 工件链（intent.md/spec.md）可担任 loop 的检查点（playbook 实证） |
| [`requirements_engineering`](../../requirements_engineering/README.md) | 停止条件的"写清楚"部分（intent / spec 怎么写）归那边 |
| [`beyond_spec_driven_development`](../../beyond_spec_driven_development/README.md) §6.1 | 本主题在形态光谱上的定位：**正交轴**（光谱问"留多少 spec 工件"，本主题问"谁决定下一轮、何时停、人站哪"） |
| [`02_research/01_agent_engineering/goal_eval_engineering`](../../../02_research/01_agent_engineering/goal_eval_engineering/README.md) | **goal/eval 构造权威**：如何写完成条件、校验裁判、设计不出时如何切分，在该主题的 [`digested/`](../../../02_research/01_agent_engineering/goal_eval_engineering/digested/README.md)；本主题只决定判据不可观察或不可信时是否自动续跑、升档、停机及交人，不复制构造方法或案例阈值 |
| [`02_research/01_agent_engineering/loop_engineering`](../../../02_research/01_agent_engineering/loop_engineering/README.md) | **循环机制证据与判读权威**（evidence-a/b/c/f/i + digested 01/03/07 等） |

**依赖方向**：Harness 层保证单次运行受控 → **Loop 层在其上治理多轮** → Graph 层管跨 agent 编排（单 agent 受控是它的前提；不在本主题）。

## 6. 信息流与升格依据（本层纪律）

- **单向加工**：研究层 evidence 档案 → 研究层判读 → 本主干；循环构件依 [`ai_loop_engineering`](../../../02_research/01_agent_engineering/loop_engineering/README.md)，完成条件与裁判边界依 [`agent_goal_eval`](../../../02_research/01_agent_engineering/goal_eval_engineering/README.md)。review 改变本主干结论时，反向核对并同步对应研究层判读，不在本层复制证据。
- **本主题不建 `research/` 层**——证据留在各自研究主题，引用须指明主题和判读篇（防双权威）。
- **升格依据（2026-09-26 触发器评估结果）**：①停止条件——**收敛**（三件骨架各 ≥2 独立一手）；②外层调度——**收敛**（两种主导形态 ≥2 独立一手）；③自主度分档——**位置分档成型**（两个独立四级阶梯＋一条官方路径，见 §3），**量化分档未成型**（如实登记为开放缺口，见 §3）。三条中两条全过、第三条半过——**够格立题，但第三条的空白决定本主干 §3 只能给位置不给刻度**。评估全文见研究层 README §4。
