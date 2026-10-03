# 01_seed_reference — 种子参考（Kicker & Reference）

**定位**：冷启动参考与初始物料（静态参考库 / Kicker）。分析产物在 `02_research/`，实践方法论在 `03_practice/`，产出交付在 `04_output/`。

> **说明**：真正高频迭代、鲜活海量的一手素材（如 DSH 源码消化、Pi 源码、305 张一手卡片等）在仓库外的四个素材根，通过各 talk 的 `_reference/` 软链接挂入。本目录仅存放冷启动种子及背景参考。

## 怎么读这张地图：每个目录回答一个不重叠的问题

| 问题 | 目录 | 里面有什么 | 入口 |
|---|---|---|---|
| 谁在**主张**什么（人 / 组织 / 事件的言论与立场） | `voices/` | 17 张人物卡 + 6 张组织卡 + 三场 2026 事件 | [`voices/README.md`](voices/README.md) |
| 组织**给出**了什么材料（方法论 / 产品 / 生态盘点） | `corp/` | AWS AI-DLC 方法论 + 非 AWS 生态全景 | [`corp/README.md`](corp/README.md) |
| 学界**论证**了什么 | `papers/` | 学术论文，raw → digested → result 管道 | [`papers/README.md`](papers/README.md) |
| 一线**实际**怎么用（行为证据，非观点） | `field_samples/` | fable5 样本池 + synthesis；agentic 通用占位 | [`field_samples/fable5/README.md`](field_samples/fable5/README.md) |
| 中文圈**当下**在传什么（二手转述快照，不引证） | `zh_discourse/` | 公众号原文归档（一手源铁律的例外收容区） | [`zh_discourse/README.md`](zh_discourse/README.md) |
| 两波命名运动各**收**了什么 | `loop_engineering/`、`graph_engineering/` | 波次一手素材；判读在 `02_research/` 镜像目录 | [`loop_engineering/README.md`](loop_engineering/README.md)、[`graph_engineering/README.md`](graph_engineering/README.md) |
| 无源可溯的放哪 | `_abandoned_no_reference/` | 收容所（跨库公共设施，不删） | [`_abandoned_no_reference/README.md`](_abandoned_no_reference/README.md) |

**两组对仗，记这两句就够了**：

- `voices` 回答「谁**主张**什么」，`field_samples` 回答「谁**真的怎么用**」——观点证据 vs 行为证据。同一个人可能两边都有（如 Simon Willison），各收各的角度。
- `loop_engineering` / `graph_engineering` 按**命名事件**收声音；`field_samples/fable5` 按**模型**收使用样本——fable5 是「以样本形态落地的模型波」，与两波命名运动同代但形态不同，故置于行为库。

## 新素材入座判据（按顺序问）

1. 属于已有波次（loop / graph）的某人一手声音 → 进对应波次目录（各目录有自己的收录判据与时间窗；人物已有 `voices` 卡的只写指针 + 增量，不重复建目录）
2. 是组织的东西？→ **一句话判据：主张什么进 voices，怎么做 / 卖什么进 corp。** 立场/主张（含高管言论、雷达主题、公司级判断）→ `voices/_raw_orgs/` 开卡；方法论 / 产品材料 / 生态盘点 → `corp/`；两类都有 → **双卡位合法，两卡互指**（2026-10-04 定案：AWS 允许双卡位）
3. 是个人或聚会的言论 → `voices/_raw_people/` / `voices/_raw_event_*/`
4. 是学术论文 → `papers/`
5. 是一线真实使用记录 → `field_samples/`（围绕某个模型 → 仿 `fable5/` 建池；非模型专属 → `agentic/`）
6. 是二手中文渠道文章、但有「当下话语怎么被转述」的档案价值 → `zh_discourse/`（例外收容区：只做忠实转录，不作为证据引用；引用时回一手源）
7. 无源可溯 / 超出时间窗 → `_abandoned_no_reference/`

> 双轴说明（2026-10-04 改述）：本层按「问题」分库。`loop_engineering` / `graph_engineering` 两库是**话题波次**的横切聚合，其余五库是**信源 / 证据形态**的纵切分库；跨话题判读与合成一律在 `02_research/`，不落本层。

## 铁律

参考库的「来源 / 时间铁律」见 [`voices/README.md`](voices/README.md) 与 [`corp/README.md`](corp/README.md)：
一手英文源优先、来源可溯、2026-01 硬底线、标注观测日期。`zh_discourse/` 是唯一例外区——收二手中文快照但不作证据。

## 迁移记录

> 2026-10-04：**front door 重写 + `weixin/` → `zh_discourse/` 更名**——顶层 README 改为「一目录一问题」+ 新素材入座判据表；weixin 以渠道名当分类名的错位修正为「中文圈话语快照」（voices 一手源铁律的例外收容区，不改转录纪律）；corp 与 `voices/_raw_orgs` 的边界以一句话判据上门面（**主张什么进 voices，怎么做 / 卖什么进 corp**），双卡位合法化，AWS 双卡位悬案定案（允许）；`field_samples` 保留原名，补与 voices 的对仗定位（观点证据 vs 行为证据）。
> 2026-10-03：原 `reference/` 薄壳撤销，`kol/`、`corp/` 提升到种子层顶层（扁平化，与其它子目录同轴）。
> 同日**净化**：话题/合成目录出 `kol/`——`_raw_loop_engineering` → `loop_engineering/`、`_raw_graph_engineering` 并入 `graph_engineering/`、`_raw_fable5` 并入 `field_samples/fable5/synthesis/`、`_raw_frontier` 迁 `02_research/.../paradigm_evolution/frontier_synthesis_2026-07/`、收容所上移本层顶层。
> 同日晚：**`kol` → `voices` 更名**（意见来源库三分：人 `_raw_people/` / 组织 `_raw_orgs/` / 事件）；ThoughtWorks 卡迁 `_raw_orgs/`（组织非个人，归属修正）。
> 同日夜：三场事件目录统一 `_raw_event_*` 前缀——`promatic` 拼写修正为 `pragmatic`、`agile_manifesto` 名实对齐为 `deer_valley`（事件官方名 Future of Software Development Retreat @ Deer Valley）。
