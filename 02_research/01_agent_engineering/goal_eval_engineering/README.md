# agent_goal_eval

**定位**：研究层·分析。定调在 §1（唯一权威）。实践层未开。
管道与证据层级以 [`../loop_engineering/`](../loop_engineering/README.md) 为方法样本；**定调与边界以本文件为准**。

```text
agent_goal_eval/
├── README.md                  # 你在这里：定调 / 边界 / 目录怎么长
├── CURRENT.md                 # 热区：做到哪、下一步动哪个文件
├── raw/
│   ├── research-plan.md       # 问题树 / 分路 / 档案一览 / backlog
│   ├── roster.md              # 人 / 社区 / 机构名单（见 §3）
│   ├── evidence-<日期>-<路别>.md
│   └── transcript-*.md        # 口播全文，归对应 evidence，不是第二份证据
├── digested/
│   ├── README.md              # 问题看板
│   └── NN-<问题>.md           # 01 goal 构造 / 02 eval 与调优 / 03 难设计（有判读再写文件）
└── result/                    # 过筛成稿（空是有意的）
```

不设 `goal/` 与 `eval/` 两个子目录。同一来源经常两面都讲，拆开就会把一段正文放进两处。

---

## 1. 定调

> 2026-09-27 用户定。改这节之前先问用户。其他文件只放指针，不复制本节。

本主题搜**现在前沿的 KOL、社区，以及其他一线来源**，看他们如何考虑、如何构造 **eval** 与 **goal**。

两面是一件事。goal 写下怎样才算达成；eval 判定交出来的东西有没有达到这句话。否决权在干活的一方之外。

**重心在 goal。** goal 要构造到 loop engineering 能跑起来：循环有一句可对照的完成条件，才知道何时停、何时再跑。

**eval 要能把结果量化。** 量化之后，调优有数可改。

**设计不出来，同样在本主题里。** 现实里大量工作没法容易设计出好的 eval 和 goal。要找的是这时如何思考，有没有站得住的实战，有没有说得清的洞察。

循环怎么跑、取题、授权、调度，不在这里回答。

---

## 2. 与相邻主题的分工

> 冲突时以本节为准。对方文件里的指针指向这里，不在对方文件里重写对象。

| 主题 | 管 | 本主题与它的接口 |
|---|---|---|
| **本主题** | 前沿来源如何构造 goal 与 eval，尤其 goal 如何让 loop 跑起来；量化之后如何调优；设计不出来时如何思考、有何实战与洞察。全文见 §1 | — |
| [`../loop_engineering/`](../loop_engineering/README.md) | 循环怎么跑：取题、授权、调度、停止骨架、跨 feature 在途 | 该主题 evidence / digested 里已有的 `/goal`、grader、验证格、停止格**留在原档案**。本主题只登记指针（见 [`raw/research-plan.md`](raw/research-plan.md)），要引用先自行回源 |
| [`../repo_agent_friendliness/`](../repo_agent_friendliness/README.md) | 仓库对 agent 好不好用（九维评估系统） | 被测对象是仓库，不是 agent 交出的结果 |
| [`../../../03_practice/harness_governance/`](../../../03_practice/harness_governance/README.md) | 单次运行的环境约束 | 环境里的门可以是判定的一种材料；门的操作规程仍归该主题 |
| [`../../../03_practice/loop_governance/`](../../../03_practice/loop_governance/README.md) | 循环控制的操作规程 | 本主题不写规程。升格见 §4 |
| [`../loop_engineering/capability_ladder/goal-eval-axis.md`](../loop_engineering/capability_ladder/goal-eval-axis.md) | Loop 能交出多少控制权时，目标/验收证据是否够用的正交判定框架 | 本主题提供构造与困难分支的证据；该页综合 G0–G3 判定能力与任务选择，外部结果观察另列，不取代本主题三篇判读 |

---

## 3. 增长规则

| 增长事件 | 动作 | 不动什么 |
|---|---|---|
| 新一手 | 新开 `raw/evidence-<日期>-<路别>.md` | 不把引句复制进 README / 问题树 |
| 新议题判读 | `digested/NN-<slug>.md`，编号 = 创建序；[`digested/README.md`](digested/README.md) 加一行 | 不改已有编号。三篇的预定名见该看板，有判读再写文件 |
| 结论过筛 | 从 `digested/` 抽进 `result/` | 未过筛的留在 `digested/` |
| 名单增加一条 | 开 `raw/roster.md`（若还没有）加一行 | 不把社区帖写成人物卡。论坛评论者不入册 |

**收录**（写入 `raw/roster.md` 时执行）：

| 类型 | 入册条件 |
|---|---|
| 人 | 对 goal 或 eval 的构造，或对「设计不出来时怎么办」，给出可操作的做法；写明为何算前沿（被谁引用，或一手长文里的机制）。只有热度、没有做法的不入 |
| 社区 | 不进人物名单。第一人称实战写入 `raw/evidence-*`，来源类型标成社区，热度不算证据 |
| 机构 / 产品 | 官方文档里的构造方法是机制证据，作者不因此成为名单上的人 |

**时间窗**（2026-09-27 用户定）：主证据是 **2026-06 及以后**。2026-01 至 2026-05 可以入档，标「窗边」。2025 及更早本主题不挖，除非某篇窗内原文自己引用了它。

回源档案的字段、采样纪律、证据层级（P-existence / P-mechanism / P-outcome）沿用方法样本 [`../loop_engineering/raw/research-plan.md`](../loop_engineering/raw/research-plan.md) 的 §4、§4.1、§5。临时产物放仓库根 `.tmp-agent-goal-eval-`。

---

## 4. 升格

实践目录由用户决定后再建。向用户提出立题之前，研究侧先具备：

- 条件的写法、裁判与产物的关系，各有至少两条独立一手来源，或明确标成单源；
- 至少一类失败模式写得出触发条件、表现和现有保护的盲点；
- 每条承重引句已在本主题回源，循环主题里的「待复核 / 侦察回源」不能直接当依据。

---

## 5. 从哪开始读

| 想知道 | 去哪 |
|---|---|
| 定调 | 本文件 §1 |
| 边界与目录怎么长 | 本文件 §2、文首目录树、§3 |
| 问题树、档案一览、下一步该回源什么 | [`raw/research-plan.md`](raw/research-plan.md) |
| 现在做到哪 | [`CURRENT.md`](CURRENT.md) |
| 判读 | [`digested/README.md`](digested/README.md)（开题时无篇） |
| 成稿 | [`result/README.md`](result/README.md)（空是有意的） |
