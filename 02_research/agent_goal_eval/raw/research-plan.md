# agent_goal_eval 研究推进计划

> 状态：v0.1，2026-09-27。定调全文在 [`../README.md`](../README.md) §1，本节不重述。本文只把定调拆成问题、分路和 backlog。
>
> 回源档案字段、弱模型采样、证据层级沿用方法样本 [`../../ai_loop_engineering/raw/research-plan.md`](../../ai_loop_engineering/raw/research-plan.md) §4、§4.1、§5。本文件不复制那三节。

## 1. 问题树

三问对应三篇待建判读。开题时都没有本主题自己的一手。

### Q1 goal 如何构造，loop 才能跑

前沿来源把 goal 写成什么，循环才有可对照的完成条件，知道何时停、何时再跑。预定判读：`digested/01-goal-构造.md`。

### Q2 eval 如何构造，量化之后如何调优

前沿来源如何把结果量化，量化之后改的是哪一个数、哪一句条件。预定判读：`digested/02-eval-调优.md`。

### Q3 设计不出来时如何思考

大量工作没法容易设计出好的 goal 或 eval。这时的思考方式、实战、洞察。预定判读：`digested/03-难设计.md`。

## 2. 分路

| 路 | 目标 | 当前状态 |
|---|---|---|
| A goal 构造 | Q1。定调写明重心在 goal，所以这是第一路 | 未开 |
| B eval 与调优 | Q2 | 未开。等 A 的档案落盘后再开 |
| C 难设计 | Q3 | 未开。等 A 的档案落盘后再开 |

一个回源档案只回答一个路。档案名：`evidence-<日期>-<路别>.md`。
人、社区、机构出现在档案里；谁进名单按 [`../README.md`](../README.md) §3。社区实战可以进任何一路，不单独占一路。

## 3. 已有线索（指针，未复核）

loop 主题里已有文字。用的时候自行回源，不抄引句，不把对方的侦察回源升成主验。这些线索不挡住第一路：第一路向外搜前沿来源，写档案时再回来核对。

| 线索 | 位置 | 可能服务 |
|---|---|---|
| `/goal` 作为完成条件与另一只模型的判定 | [`../../ai_loop_engineering/raw/evidence-2026-09-26-a-originators.md`](../../ai_loop_engineering/raw/evidence-2026-09-26-a-originators.md)、[`../../ai_loop_engineering/raw/evidence-2026-09-26-b-stop-and-scheduling.md`](../../ai_loop_engineering/raw/evidence-2026-09-26-b-stop-and-scheduling.md)、[`../../ai_loop_engineering/digested/03-构件.md`](../../ai_loop_engineering/digested/03-构件.md) | Q1 |
| outcome 与 grader 一起装配 | [`../../ai_loop_engineering/raw/evidence-2026-09-27-e-cross-feature-observability.md`](../../ai_loop_engineering/raw/evidence-2026-09-27-e-cross-feature-observability.md) | Q1、Q2 |
| 验证格、停止格 | [`../../ai_loop_engineering/digested/07-控制问题矩阵.md`](../../ai_loop_engineering/digested/07-控制问题矩阵.md) | Q3。判读权威在 loop 主题 |
| evals 四人与行为面 | [`../../ai_loop_engineering/raw/evidence-2026-09-27-i2-teams-evals-outcome.md`](../../ai_loop_engineering/raw/evidence-2026-09-27-i2-teams-evals-outcome.md) 切口 b | Q2、Q3。对方标明主验与侦察回源混合，且不入其名册 |
| 一条本地 goal | [`../../ai_loop_engineering/raw/evidence-2026-09-27-j-local-goal-session.md`](../../ai_loop_engineering/raw/evidence-2026-09-27-j-local-goal-session.md) | Q1、Q3。对方写明 n=1，不是效果证据 |

## 4. 证据门

- 观点、机制、效果分开。讲了构造方法，不等于 loop 因此跑起来，也不等于调优因此变好。
- 独立来源按作者、机构和引用链去重。
- 尚未回源的句子状态写「线索」，不写进 `digested/`。
- 「设计不出来」要有来源自己的说法或案例，不用来源没写的空白代替洞察。

## 5. 当前 backlog

1. **A 路**（下一步唯一入口）：前沿一手里，goal 如何构造，loop 才能跑。验收：一份 `evidence-*`，含搜过但未取得的范围，以及不能推出什么。
2. **B 路、C 路**：A 的档案落盘后再开。不在 A 的同一篇里把三问写完。
3. **名单**：A 路出现符合 [`../README.md`](../README.md) §3 的人，再开 `raw/roster.md`。

## 6. 每轮收口

1. 新增了什么可回源的事实？（链到 evidence；没有就写没有）
2. 哪一条问题的不确定性缩小了？（链到 digested；没有就写没有）
3. 下一轮只做哪一个问题？
