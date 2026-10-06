---
type: index
content_type: readme
directory: 01_seed_reference/loop_engineering
description: Loop Engineering 一波声音（2026-06 起）——按三派组织的一手素材集合
research_date: 2026-09-26
reorg_date: 2026-10-06
---

# loop_engineering — Loop Engineering 一波声音（2026-06 起）

> 本集合收 **2026-06 起**围绕 "loop engineering" 这个公开名字发声的人的一手素材。
> 2026-10-03 自 `kol/_raw_loop_engineering/` 上移至种子层专题位（话题出库，与 [`graph_engineering/`](../graph_engineering/README.md) 同构）。
> **2026-10-06 重组为三派结构**（用户定）：推动派（发起者＋吹捧者）／中性派（边界与审慎）／反对与怀疑派。
> 它是 [`_raw_people/`](../voices/_raw_people/README.md)（17 张影响力人物深度卡）的**主题波次补充**：
> `_raw_people/` 按人铺全景，本集合按**一次命名事件**（2026-06 loop engineering 成为公开名字）收一波声音，并按立场分派。

**唯一名单与派别权威不在这里**——谁入册、号召力依据、每人主张一句话、**属于哪一派及判定依据**，
在 [`02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md`](../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)（§A 入册名单＋§三派分野）。
本 README 只管**素材索引**（这个集合里有什么、卡片怎么写、三派目录怎么放素材）。

## 收录判据

沿用 [`../voices/README.md`](../voices/README.md) 的两条铁律，另加本集合自己的时间窗：

| 项 | 规则 |
|---|---|
| **时间窗** | 2026-06 起（loop engineering 成为公开名字）。更早的一手源（Ralph Wiggum loop 2025-07、Anthropic《Building effective agents》2024-12）**不入本集合**，只作谱系背景登记在主题的时间线文件里 |
| **来源** | 只接受原始英文一手源（原帖 / 博客原文 / 官方发布 / 播客原版 / 演讲 transcript）。中文编译只作交叉验证，不作唯一引用 |
| **派别** | 入册者归哪一派由台账 §三派分野判定（依据一手表态，立场可随时间移动，轨迹不抹平）；派别目录只影响素材放哪，不影响收录本身 |
| **未满足** | 无来源 → [`../_abandoned_no_reference/`](../_abandoned_no_reference/)；不在时间窗内 → 主题时间线的背景行 |

## 目录结构（2026-10-06 三派重组）

```text
loop_engineering/
├── README.md                  # 你在这里：素材索引 + 卡片规则
├── 00_three_camp_landscape.md # ★ 三派地图与社区实况判读（2026-10-06 批的结论入口）
├── 01_advocates/              # 推动派（发起者＋吹捧者）：把循环放权当默认方向推荐的人
│   ├── README.md              #   素材索引（KOL 侧：人物 → 素材在哪个文件）
│   ├── community_feedback.md  #   ★ 社区反馈（社区情绪证据，按派可读）
│   ├── raw_scan_2026-10-06_advocates.md   #   三派深扫·推动派增量回源档案（2026-10-06 批）
│   └── <slug>/                #   四件套卡（仅 ≥3 份独立一手长者，当前仅 andrew_ng）
├── 02_neutral/                # 中性派（边界与审慎）：承认机制但划适用边界/要求约束形态
│   ├── README.md              #   素材索引（KOL 侧）
│   ├── community_feedback.md  #   ★ 社区反馈（含机构采样层：SO/JetBrains/DORA）
│   └── raw_scan_2026-10-06_neutral.md     #   三派深扫·中性派回源档案（2026-10-06 批）
└── 03_skeptics/               # 反对与怀疑派：反证、失败账本、质量/经济/人的角色批评
    ├── README.md              #   素材索引（KOL 侧）
    ├── community_feedback.md  #   ★ 社区反馈（热度层＋GitHub 故障清单＋中文圈事故向）
    └── raw_scan_2026-10-06_skeptics.md    #   三派深扫·反对/怀疑派回源档案（2026-10-06 批）
```

> **2026-10-06 批的落点约定（用户定）**：本轮三派重组的全部新增素材（三路深扫档案、判读）
> 落在**本目录内**，不进研究层 evidence 档案、不在 digested 开新文件；
> 研究层只保留台账 §A2（派别判定权威）与既有指针。
>
> **社区意见批（2026-10-06 第二批，用户定）**：技术社区的意见（HN/GitHub/Reddit/调查报告/中文社区）**按支持/中性/反对拆进三个派别目录**，
> 各派一份 `community_feedback.md`（KOL 侧与社区侧分开读、来源逐条标注）；按仓库纪律这是**社区情绪证据**：
> 单独标注、不进 KOL 台账、不与 KOL 证据并列引用。根目录不再散列社区扫描文件。
>
> **拉取纪律（2026-10-06 用户定）**：要拉的内容就多通道努力拉；**两轮拉不到就放弃**——降级出档、不留"待回源"半成品挂账，
> 拉不到的内容对 本集合没有价值。**热度/票数从来不是收录理由，一手内容才是**。
> 例外：**未发布 ≠ 拉不下来**（如 SO/DORA/Octoverse 年度报告），保留重扫位。

**四件套卡格式不变**（一人一目录，与 [`../field_samples/fable5/run_*/`](../field_samples/fable5/README.md) 同构）：

```text
<派别目录>/<slug>/             # 目录名用英文小写下划线，如 andrew_ng
├── profile.md                 # 这人是谁、为什么在这波里、对本主题的主张
├── quotes.md                  # 逐字引句（英文原句优先）+ 每句为什么重要
├── sources.md                 # 来源索引：URL + 类型 + 日期 + 证据强度 + 缺口
└── raw_*.md                   # 原文/原帖/转写归档，一份来源一个文件
```

**已有 `_raw_people/` 卡片的人不重复建目录**——在那人的 `sources.md` 里放指针，只补 loop 专项增量；
派别 README 的素材索引表同样只放指针。

## 三派素材分布（入口表）

| 派 | 一句话口径 | 入口 |
|---|---|---|
| **三派总览与社区实况判读** | 三派地图＋痛点对位＋词的状态＋证据边界 | [`00_three_camp_landscape.md`](00_three_camp_landscape.md) |
| **推动派**（发起者＋吹捧者） | 把"设计循环让 agent 自动推进"当默认方向推荐（定义/教程/产品/布道） | [`01_advocates/README.md`](01_advocates/README.md) |
| **中性派**（边界与审慎） | 承认机制有条件成立，划边界、要求约束、审慎实证 | [`02_neutral/README.md`](02_neutral/README.md) |
| **反对与怀疑派** | 给反证与批评（失败账本/质量退化/经济/人的角色） | [`03_skeptics/README.md`](03_skeptics/README.md) |

**建卡规则（2026-09-26 回源轮定，重组后不变）**：素材的常态形态是研究主题的
`raw/evidence-*.md` 回源档案（见其 README §1「素材形态」）；四件套卡只给"独立一手长文 ≥3 份"的人。
**当前无待建卡**——`andrew_ng/`（现位于 `01_advocates/`）的四件套是**规则设立前的历史卡**
（其独立一手长文仅 1 份，因命名事件锚点而保留，不代表达标）。
词源碎片级（Cherny / Steinberger）与中文编译（alchaincyf）不建卡；
Runkle / Osmani / Huntley / Ball 等已回源者的素材在 evidence 档案或 `_raw_people/` 人物卡里，不为每人建卡。

## 与其他集合的关系

| 集合 | 关系 |
|---|---|
| [`../voices/_raw_people/`](../voices/_raw_people/README.md) | 人物全景档案。本集合里若有人已在那边有卡片（Boris Cherny、Kief Morris、Ryan Lopopolo、Karpathy、Gergely Orosz、Huntley、Ronacher、Ball），**只写指针 + loop 专项增量，不复制人物背景** |
| [`../field_samples/fable5/`](../field_samples/fable5/README.md) | 按**模型**（Fable 5）收样本；本集合按**命名事件**收声音。同一人可能两边都有，各收各的角度 |
| [`../graph_engineering/`](../graph_engineering/README.md) | 姊妹专题（2026-07 起的下一波命名）；其"Loop 管局部自愈、Graph 管全局拓扑"的分界见该 README |
