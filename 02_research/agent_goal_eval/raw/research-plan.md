# agent_goal_eval 研究推进计划

> 状态：v0.3，2026-09-27。定调全文在 [`../README.md`](../README.md) §1，时间窗在同文 §3。本节不重述。
>
> **读法**（用户同日校正）：按引用链走，谈论 goal / eval 的人并不少。稀的是沉淀。通讯、主题演讲、课程和推文叠在一起，很多仍在摸索。分开记三列：谁在说、有没有可操作做法、是否还在摸索。不得把「还没沉淀」写成「没什么人在说」。
>
> **再校正**：这里很难拿到唯一的确定性做法。感觉站得住的做法都保留，并列写各自适用的地方，不收成一条标准步骤。
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
| A goal 构造 | Q1。定调写明重心在 goal，所以这是第一路 | ✅ A / A2 / A3 / A4 / A9 / A10。判读在 [`../digested/01-goal-构造.md`](../digested/01-goal-构造.md) |
| B eval 与调优 | Q2 | ✅ 构造在 B，动作在 B2，工程读数在 B3，Abridge 在 [`evidence-2026-09-27-b4-abridge.md`](evidence-2026-09-27-b4-abridge.md)。判读在 [`../digested/02-eval-调优.md`](../digested/02-eval-调优.md) |
| C 难设计 | Q3 | ✅ [`evidence-2026-09-27-c-hard.md`](evidence-2026-09-27-c-hard.md)。判读在 [`../digested/03-难设计.md`](../digested/03-难设计.md) |

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

1. 判读已写在 `digested/01`–`03`。做法并列，不收成一步。
2. 仍只有链、不挡阅读：Lenny 第三步聚类表（付费墙）、Loopcraft 全文（付费墙）、Cherny 7 月 17 日步骤表的构件页。
3. 再收工程帖时，仍要有检查的句子，以及改了哪一步、哪个数动了。见解不入档。

## 6. 每轮收口

1. 新增了什么可回源的事实？（链到 evidence；没有就写没有）
2. 哪一条问题的不确定性缩小了？（链到 digested；没有就写没有）
3. 下一轮只做哪一个问题？
