# Loop Governance 实践主干（定稿层·总纲）

> **本文件是什么**：loop 层（五层框架第 4 层）的实践主干，**§0–§6 共七节**——§0 定义与判据、§1–§4 核心四段（停止条件 / 外层调度 / 自主度分档 / 检查点）、§5 接口、§6 升格依据；
> 每条带源强度与证据指针（指向研究层 evidence 档案与判读篇，**本主题不复制证据**）。
> 手册级操作规程（SOP / 模板 / 选型表展开）待主干稳定后另立 `manual.md`。

```yaml
topic: Loop Governance —— loop 层的实践主干（Prompt → Context → Harness → Loop → Graph 第 4 层）
doc_layer: result（定稿层 · 总纲，清单级）
produced_at: 2026-09-26
provenance: 升格依据＝研究层三路回源（evidence-a/b/c，全部一手）+ 判读 01/03/05；用户 2026-09-26 决定立题并授权命名
filter: ≥2 独立一手来源 → 主干；单源强实践 → 标注"单源"；未收敛点 → 如实标注为设计空间或开放缺口，不冒充共识
evidence_home: 02_research/ai_loop_engineering（证据与判读权威；本主题不建 research/ 层，防双权威）
naming: 不沿用 KOL 词 "loop engineering"——词源＝热度碎片、外延未收敛（判定见研究层 digested/01）；按仓库五层框架命名，与 harness_governance 同构成对（环境轴 / 控制轴）
---
```

## 0. 这层管什么（定义与判据）

**Loop 层管"怎么回头"：让上次结果改变下次行动。**（四要素与两判据的权威表述在研究层 [`digested/01 §三`](../../../02_research/ai_loop_engineering/digested/01-命名谱系.md)，框架源出主线 talk storyline；前提链见 §5）

**四要素**：**触发 · 验证 · 停止条件 · 记忆**——触发＝什么开下一轮；验证＝拿什么判这轮好坏；停止条件＝跑到哪算完；记忆＝跨轮状态放哪。

**两个硬判据（什么不算 loop）**：

1. **停止条件不依赖上次结果 → 那是重试，不是 loop**（[`digested/01 §三`](../../../02_research/ai_loop_engineering/digested/01-命名谱系.md) 硬判据）；
2. **单次运行不受控 → loop 只是把错误复制得更快**——与 Ralph 的 greenfield 限定（"There's no way in heck would I use Ralph in an existing code base"，evidence-b §1）、Anthropic 的"每轮先过基线再干活"（evidence-b 问题2 §1）三方同向。

**术语注记**：KOL 词 "loop engineering"（2026-06 命名）经研究层回源判定——**词源＝热度碎片（Cherny 06-02 访谈句未逐字核验、Steinberger 06-08 两句话推文无深度），定义＝事后工程化（Osmani 06-07 → Runkle 06-16 → CC 团队 06-30）**；四人核心同指（系统替人逐轮提示）但**外延不兼容**（Runkle 第 4 环属 harness 层；验证语义分歧）。本主题因此不沿用该词。判定全文：[`digested/01`](../../../02_research/ai_loop_engineering/digested/01-命名谱系.md)。

## 1. 停止条件（跑到哪算完）

**目标敌人**：**提前宣告完成**。Anthropic 官方把两种头号失败模式写成表格——"Claude declares victory on the entire project too early" / "Claude marks features as done prematurely"（evidence-b §3）；LangChain verification loop 的存在理由同源；Huntley 的对应物是占位实现（"inherent bias to do minimal and placeholder implementations"，evidence-b §1）。**停止条件的全部设计都是在对抗这一条。**

**三件骨架（各 ≥2 独立一手同向，判定见 [`digested/03`](../../../02_research/ai_loop_engineering/digested/03-构件.md) §一）**：

1. **机器可核判据做逐轮闸门**——back pressure（类型 / 测试 / linter / 静态分析 / 安全扫描，evidence-b §1）/ grader（deterministic 优先，agentic/LLM-as-judge 慎用——它是评分不是闸门，evidence-b §4e）。
2. **硬性熔断上限做兜底**——把轮次 / 时间 / 拒绝计数写进条件（`or stop after 20 turns`）；auto mode 3 连拒 / 20 总拒停机；`/loop` 7 天硬过期（"bounds how long a forgotten loop can run"）。（evidence-b §4a/4b/4c）
3. **验收与干活分离**——五处一手跨三家：evaluator-optimizer、"只许改 `passes` 字段"、"/goal adds a separate evaluator… completion is decided by a fresh model rather than the one doing the work"、"The separation of roles matters"、grader 与 agent 分置。（evidence-b 综合节）

**写法（CC 官方三要素，一手）**：**一个可度量终态 + 一个声明式检查 + 路径约束**（"`npm test` exits 0"、"no other test file is modified"，evidence-b §4a）。**实践例证**：Jesse Vincent 的 `/goal` 实验（过夜 25 实验那例——**中文转述·非逐字**，仅作用法样本，不作独立收敛依据；[`fable5/run_superpowers_jesse_vincent`](../../../01_sources/field_samples/fable5/run_superpowers_jesse_vincent/quotes.md)）。
停止条件是**三值状态机**（Not yet met / Met / Impossible），不是布尔（evidence-b §4a）；Osmani 澄清：`/goal` 评估器**只核 transcript 硬规则、不判内容好坏**（evidence-a）——判好坏的是人或上级环。

**裁判权选型（研究层确认的未收敛点——这里是设计空间，不是缺口）**：

| 裁判 | 适用场景 | 源 |
|---|---|---|
| 人判（taste） | greenfield 探索、清单语义撑不住时 | Huntley（TODO 耗尽是 "a matter of taste"） |
| 文件清单逐条判定 | 功能型长跑、目标可枚举 | Anthropic feature_list.json |
| 独立小模型每轮判定 | 会话内 goal | Claude Code `/goal` |
| 干活模型自判 | 默认形态——**最弱**，必须配骨架 2/3 补偿 | Anthropic 2024 |
| 被审批方提出、审批方判定 | 越界动作 | OpenAI auto-review |

**保护裁判（"agent 修代码时不得削弱对代码的检查"一族）**：测试不可删改 + JSON 选型防整文件改写（Anthropic，单源但机制成型）；评估器输入防操纵（auto mode 分类器 "reasoning-blind by design"）；Ralph 防作弊条款——测试当场写明**为什么存在**，因为 "future loops will not have the reasoning in their context window"（evidence-b §1）。

## 2. 外层调度（下一轮跑什么、何时跑）

**主导形态一：文件即队列。**（Huntley 与 Anthropic 两家独立、句式同构）

- **三件套**：进度规格（feature_list.json / fix_plan.md / loop.md）＋ 叙事日志（progress 文件）＋ git 历史；
- **每轮冷启动重读 + 固定开场序列**：定位 → 读 git log / progress → **选清单里最高优先级的未完成项** → 先过基线再干活（evidence-b §2.1/§4）；
- **决定"下一轮跑什么"的不是人、不是定时器，是规格文件里第一个 `passes: false` 的条目**；
- 一次只做一件 + 干净收尾（commit + progress 更新）——对抗 one-shot 冲动（Anthropic 点名的失败模式一）。

**主导形态二：触发器即节拍。**条件驱动（`/goal`）/ 时间驱动（`/loop`、cron、Routines——间隔可固定、可模型自选、可 loop.md 定制）/ 事件驱动（webhook，LangChain event-driven loop）/ 脚本驱动（Stop hook）。`/loop` 的内置维护 prompt 是"下一件工作"的清单化变体：固定优先级（未完工作 → PR 偶发维护 → 清理），且**不在该范围外开新动作**（evidence-b §4c）。

**审批作为独立角色**：auto mode 分类器与 OpenAI auto-review 都把"越界判定"做成**独立模型调用**——主 agent 有把审批边界当障碍绕过的压力，所以判定必须分离（"The separation of roles matters"）。单次拒绝**不终止循环**：deny-and-continue，拒绝带理由回给模型换安全路径（过半场景模型自找替代路径，evidence-b §4b/4d）。

**人的位置**：**人工同步审批已退出调度回路**（Anthropic 2024→2025 演化 + OpenAI auto-review 标题即立场，两家一线厂商一手）。人留在三处：**熔断升级、ask 规则、显式清除**。

**外层的接口化（前沿形态）**：Managed Agents 把 session log 独立于 harness 存活，`wake(sessionId)` 从最后事件恢复——"外层"本身正在成为可调用的接口（evidence-b §5，单源·标注）。

**开放缺口（如实登记，与 §3「量化分档未成型」同格式）**：**跨 feature 的在途可见性与逐 feature 验证汇总**——本轮全部一手材料均未给出成型做法（Anthropic 的 progress 文件是**单 feature 长跑内**的；姊妹仓 FAQ 15 的 owner 四仓自建队列属外部个案·转引）。队列与次序有覆盖（本节形态一），在途视图没有——不冒充共识。

## 3. 自主度阶梯（人在哪一站、什么时候升档）

**位置分档（已成型）**——两个独立四级阶梯 + 一条官方路径：

| 阶梯 | 档位 | 源 |
|---|---|---|
| Kief Morris | outside → **in** the loop → **on** the loop → agentic flywheel（on＝修 harness 不修产物） | evidence-c |
| Addy Osmani | agentic loop（人写每轮）→ `/goal`（评估器）→ `/loop`（间隔）→ **proactive**（事件触发无人值守） | evidence-a |
| Anthropic playbook | 逐手 prompt → 门禁审阅 → auto-accept → 并行 worktree → **"building and monitoring loops"** | [`anthropic_ai_sdlc/org`](../../../02_research/anthropic_ai_sdlc/org/ai-native-sdlc-playbook.md) |

σ 分层是事件驱动判据的成品样本：**1σ 只记录 / 2σ 只读诊断 / 3σ 限界行动**（只许开 PR 或触发预批 runbook），且**检测全程确定性、模型不参与**（同上）。

**量化分档（未成型——登记为开放缺口，不冒充共识）**：**没有任何一手源给出"跑几轮必须人看"的轮次判据**；现行判据全部事件驱动（风险分数门槛 / 关键歧义触发 / 破坏性动作类别 / σ 分层 / auto-review 停机阈值）。行为面验证被 Böckeler 点名为"减监督"路线的公认短板——**门拦得住动作，拦不住"没做该做的事"**（evidence-c）。

**升档判据**：**机械门可信度决定可授权的自主度**——门会红才配当门（负例控制，衔接 [`harness_governance` 回路 1](../../harness_governance/result/backbone.md)）；门不可信时升档＝把错误复制得更快（本主干 §0 判据 2）。

**反面声音（一手）**：Steinberger 2025-12 长文明确反对自动编排（"usually I'm the bottleneck"）——与他的 6 月词源推文立场相反（evidence-a）。**自主度升档不是免费的方向**；词源人物自己的摇摆就是证据。

## 4. 检查点与反例（什么时候必须人看 / 什么时候不要 loop）

1. **人的注意力集中在门禁**："Human attention concentrates at the gates, reviewing what the agent flagged rather than starting each stage from scratch"（playbook）——审 agent 标记的，不从零开始。（与 §2 的「人留三处」不冲突，是**两个尺度、同一方向**：§2 是会话尺度（CC `/goal` 原语的熔断/ask/清除），本条是 SDLC 阶段尺度（playbook 的工件门）——人都从逐动作、逐轮的同步审批退出，集中到检查点。）
2. **风险分级保留人审**：auth / billing / 破坏性变更 + 回滚计划（引用 [`harness_governance` 组织 6](../../harness_governance/result/backbone.md)，不重复）。
3. **假把控的两面镜**：SDD 侧 "False Sense of Security"（agent 把 verify implementation 标 done 却零单测，marmelab 2025-11-12——**注意出处修正**，evidence-c）↔ loop 侧没有进度盘时退回人的工作记忆与对话催促。**真实把控＝机器可查的门 + 少量真人在环点。**
4. **什么时候不要 loop**：单次小任务（为它建循环脚手架是过度工程）；brownfield 慎用无限循环（Ralph 自限 greenfield）；**先有真实失控，再上循环治理**（对齐 harness_governance 反过度工程条）。
5. **非保证声明要跟着走**："Auto-review should not be treated as a guarantee of security"（OpenAI 官方自述）——机械门自身也是攻击面（DSH 的 CVE-2026-82533 样本，**转引·待回源**——见姊妹仓 FAQ 15，未独立回源前不作主张依据）。

## 5. 与兄弟主题的接口

| 主题 | 关系 |
|---|---|
| [`harness_governance`](../../harness_governance/README.md) | **前提层**：单次运行受控（门禁/传感器/漂移清理在那边，诊断轴＝"agent 缺哪句话"①–⑦）。本主题引用其回路 1（门禁可信度）/5（评审外置）/7（反馈分层）与组织 6（风险分级），不复制 |
| [`spec_driven_development`](../../spec_driven_development/README.md) | **收敛证据**：OpenSpec 拆刚性阶段（"No more rigid phases"）、spec-kit 收 Ralph Loop extension 与 Autonomous Run Governance preset；SDD 工件链（intent.md/spec.md）可担任 loop 的检查点（playbook 实证） |
| [`requirements_engineering`](../../requirements_engineering/README.md) | 停止条件的"写清楚"部分（intent / spec 怎么写）归那边 |
| [`beyond_spec_driven_development`](../../beyond_spec_driven_development/README.md) §6.1 | 本主题在形态光谱上的定位：**正交轴**（光谱问"留多少 spec 工件"，本主题问"谁决定下一轮、何时停、人站哪"） |
| [`02_research/ai_loop_engineering`](../../../02_research/ai_loop_engineering/README.md) | **证据与判读权威**（evidence-a/b/c + digested 01/03/05 + KOL 台账） |

**依赖方向**：Harness 层保证单次运行受控 → **Loop 层在其上治理多轮** → Graph 层管跨 agent 编排（单 agent 受控是它的前提；不在本主题）。

## 6. 信息流与升格依据（本层纪律）

- **单向加工**：研究层 evidence 档案 → 研究层判读（digested 01/03/05）→ 本主干；review 改变本主干结论 → 反向同步研究层判读。
- **本主题不建 `research/` 层**——证据唯一 home 在研究层，引用写法＝`evidence-a/b/c §节号` + `digested/编号`（防双权威）。
- **升格依据（2026-09-26 触发器评估结果）**：①停止条件——**收敛**（三件骨架各 ≥2 独立一手）；②外层调度——**收敛**（两种主导形态 ≥2 独立一手）；③自主度分档——**位置分档成型**（两个独立四级阶梯＋一条官方路径，见 §3），**量化分档未成型**（如实登记为开放缺口，见 §3）。三条中两条全过、第三条半过——**够格立题，但第三条的空白决定本主干 §3 只能给位置不给刻度**。评估全文见研究层 README §4。
