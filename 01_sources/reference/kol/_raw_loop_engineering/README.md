---
type: index
content_type: readme
directory: reference/kol/_raw_loop_engineering
description: Loop Engineering 一波声音（2026-06 起）——一人一目录的一手素材集合
research_date: 2026-09-26
---

# _raw_loop_engineering — Loop Engineering 一波声音（2026-06 起）

> 本集合收 **2026-06 起**围绕 "loop engineering" 这个公开名字发声的人的一手素材。
> 它是 [`_raw_kol/`](../_raw_kol/README.md)（12 位影响力人物深度拆解，2026-07-08）的**主题波次补充**：
> `_raw_kol/` 按人铺全景，本集合按**一次命名事件**（2026-06 loop engineering 成为公开名字）收一波声音。

**唯一名单权威不在这里**——谁入册、号召力依据是什么、每个人对本主题的主张一句话，
在 [`02_research/ai_loop_engineering/raw/kol-roster.md`](../../../../02_research/ai_loop_engineering/raw/kol-roster.md)。
本 README 只管**素材索引**（这个集合里有什么、卡片怎么写）。

## 收录判据

沿用 [`../README.md`](../README.md) 的两条铁律，另加本集合自己的时间窗：

| 项 | 规则 |
|---|---|
| **时间窗** | 2026-06 起（loop engineering 成为公开名字）。更早的一手源（Ralph Wiggum loop 2025-07、Anthropic《Building effective agents》2024-12）**不入本集合**，只作谱系背景登记在主题的时间线文件里 |
| **来源** | 只接受原始英文一手源（原帖 / 博客原文 / 官方发布 / 播客原版 / 演讲 transcript）。中文编译只作交叉验证，不作唯一引用 |
| **未满足** | 无来源 → [`../_abandoned_no_reference/`](../_abandoned_no_reference/)；不在时间窗内 → 主题时间线的背景行 |

## 卡片格式（一人一目录）

与 [`01_sources/field_samples/fable5/run_*/`](../../../field_samples/fable5/README.md) 同构，四件套：

```text
_raw_loop_engineering/
└── <slug>/                    # 目录名用英文小写下划线，如 andrew_ng
    ├── profile.md             # 这人是谁、为什么在这波里、对本主题的主张
    ├── quotes.md              # 逐字引句（英文原句优先）+ 每句为什么重要
    ├── sources.md             # 来源索引：URL + 类型 + 日期 + 证据强度 + 缺口
    └── raw_*.md               # 原文/原帖/转写归档，一份来源一个文件
```

**已有 `_raw_kol/` 卡片的人不重复建目录**——在那人的 `sources.md` 里放指针，只补 loop 专项增量。

## 集合内容

| slug | 人物 | 状态 | 备注 |
|---|---|---|---|
| [`andrew_ng/`](andrew_ng/profile.md) | Andrew Ng | 四件套齐 | 2026-06-30 X post + The Batch 原文；中文编译一份（低强度，只作交叉验证） |

**建卡规则（2026-09-26 回源轮定，取代"待建卡"清单）**：素材的常态形态是研究主题的
`raw/evidence-*.md` 回源档案（见其 README §1「素材形态」）；四件套卡只给"独立一手长文 ≥3 份"的人。
**当前无待建卡**——词源碎片级（Cherny / Steinberger）与中文编译（alchaincyf）不建卡；
Runkle / Osmani / Huntley 等已回源者的素材在 evidence 档案（a/b/c）里，不为每人建卡；andrew_ng/ 的四件套是**规则设立前的历史卡**（其独立一手长文仅 1 份，因命名事件锚点而保留，不代表达标）。

## 与其他集合的关系

| 集合 | 关系 |
|---|---|
| [`../_raw_kol/`](../_raw_kol/README.md) | 人物全景档案。本集合里若有人已在那边有卡片（Boris Cherny、Kief Morris、Ryan Lopopolo、Karpathy、Gergely Orosz），**只写指针 + loop 专项增量，不复制人物背景** |
| [`../../field_samples/fable5/`](../../../field_samples/fable5/README.md) | 按**模型**（Fable 5）收样本；本集合按**命名事件**收声音。同一人可能两边都有，各收各的角度 |
