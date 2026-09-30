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
| **R4 编排与并发**（任务分解/子代理调度权） | —（四级止于触发方式） | —（四类皆单循环） | —（flywheel 是自转不是编排） | —（四环无编排环） | — | 三层：fan-out＋对抗验证＋大小模型分层 | **1/6 显式落位**（视频，侦察级）＋Anthropic multi-agent 待回源 |
| **R5 自我改进**（改写 harness 本身的权） | — | — | flywheel（"改写 harness 本身"最接近——见下注） | hill-climbing loop（"return arrow reaches inside and updates the agent loop directly"） | 外环修正内环方向（人执行，非 agent） | — | **2/6 概念落位**＋GEPA/DSPy 生态素材（缺口5） |

> **Morris flywheel 归位注**：flywheel 的原文落点是"循环改进循环"，与 Runkle hill-climbing 同指 R5；
> 但 Morris 卡片还是三档旧版（四级修订待办在 [`_raw_kol/10`](../../01_sources/reference/kol/_raw_kol/10_kief_morris.md)），归位按 evidence-c 定性，修订后再固化。

## 三、判读（候选判读——升 digested 前不外传）

1. **R1/R2 是共识阶**（≥5 源落位），**R3 是共识阶**（3 源显式＋Osmani/CC 语义覆盖），→ 立正式阶。
2. **R4 不是概念共识阶，是框架能力**：六个概念来源里只有中文传播层给了显式位；Osmani/CC 的阶梯**止于触发方式**，
   编排是各家框架（Anthropic multi-agent、LangGraph、DSH workflow）的实现层而非共识概念层。
   → **候选阶**；Anthropic multi-agent 档案若给出与视频同构的交接面叙述，R4 可升正式。
3. **R5 概念上收敛但素材单薄**：Runkle hill-climbing 与 Morris flywheel 同指，但均无展开的操作层；
   操作素材在缺口 5（GEPA/DSPy 提案-评估分离/审计谱系），性质是"生态做法"而非"KOL 阶梯位"。
   → **候选阶**，升阶条件＝操作条目按自说明格式落齐且 ≥2 独立来源。
4. **阶梯的两类之分本身是发现**：A 类（运行模式）与 B 类（环类型）被混引时会产生假性分歧——
   digested/01 的"外延不兼容"结论，落到阶位上有一部分其实是**维度错位**而非真分歧。此项为回流候选（→ digested/01）。
5. **视频三层跳过 R3**（从 goal 直接跳编排）——中文传播层对"无人值守/熔断"这个最危险的交接面**没有切片**；
   传播完整性视角的观察，记在 [evidence-t](../raw/evidence-2026-09-30-t-shenmejiaoqq-video-zh.md) 侧，不在本表展开。

## 四、R0（基线，非阶）

"人肉 API"是所有来源共同的**反面起点**（提示→等待→读→再提示），不是能力阶，不设档。
它在叙事上的作用：定义"交出"的零点——R1 起每一阶的"交出什么"都相对 R0 度量。
