# 01_seed_reference — 种子参考（Kicker & Reference）

**定位**：冷启动参考与初始物料（静态参考库 / Kicker）。分析产物在 `02_research/`，实践方法论在 `03_practice/`，产出交付在 `04_output/`。

> **说明**：真正高频迭代、鲜活海量的一手素材（如 DSH 源码消化、Pi 源码、305 张一手卡片等）在仓库外的四个素材根，通过各 talk 的 `_reference/` 软链接挂入。本目录仅存放冷启动种子及背景参考。

## 目录一览

> 组织逻辑是**双轴**：来源形态轴（voices=人/组织/事件的意见、corp=厂商材料、papers=论文、weixin=渠道、field_samples=使用行为）+ 话题轴（loop_engineering、graph_engineering，两波命名事件的一手素材；跨话题判读在 `02_research/`）。

| 子目录 | 是什么 | 入口 |
|---|---|---|
| `field_samples/` | 真实使用样本（agentic 开发者洞察索引、fable5 样本池 + synthesis） | `field_samples/agentic/agentic_developer_insights_index.md` |
| `loop_engineering/` | Loop Engineering 一波声音（2026-06 起，一人一目录一手素材；判读在 `02_research` 同名主题） | `loop_engineering/README.md` |
| `graph_engineering/` | Graph Engineering 与 DAG 拓扑编排（2026-07 起，从单循环走向状态机编排与多 Agent 协作） | `graph_engineering/README.md` |
| `voices/` | 声音库——人物、组织与事件（意见来源三轴：`_raw_people/` 人卡 + `_raw_orgs/` 组织卡 + `_raw_event_*` 三场 2026 聚会）；来源/时间铁律 + 滚动更新规矩都在其 README | `voices/README.md` |
| `corp/` | 企业/厂商/分析机构参考库（AWS 方法论 + 生态全景） | `corp/README.md` |
| `papers/` | 学术论文参考，`raw → digested → result` 管道 | `papers/README.md` |
| `weixin/` | 微信公众号原文归档（HTML → MD + 原图） | `weixin/README.md` |
| `_abandoned_no_reference/` | 无源可溯内容收容所（跨库公共设施，不删） | `_abandoned_no_reference/README.md` |

> 2026-10-03：原 `reference/` 薄壳撤销，`kol/`、`corp/` 提升到种子层顶层（扁平化，与其它子目录同轴）。
> 同日**净化**：话题/合成目录出 `kol/`——`_raw_loop_engineering` → `loop_engineering/`、`_raw_graph_engineering` 并入 `graph_engineering/`、`_raw_fable5` 并入 `field_samples/fable5/synthesis/`、`_raw_frontier` 迁 `02_research/.../paradigm_evolution/frontier_synthesis_2026-07/`、收容所上移本层顶层。
> 同日晚：**`kol` → `voices` 更名**（意见来源库三分：人 `_raw_people/` / 组织 `_raw_orgs/` / 事件）；ThoughtWorks 卡迁 `_raw_orgs/`（组织非个人，归属修正）。
> 同日夜：三场事件目录统一 `_raw_event_*` 前缀——`promatic` 拼写修正为 `pragmatic`、`agile_manifesto` 名实对齐为 `deer_valley`（事件官方名 Future of Software Development Retreat @ Deer Valley）。

**参考库的"来源 / 时间铁律"**见 `voices/README.md` 与 `corp/README.md`；
统一纪律：一手源优先、来源可溯、标注观测日期。`_abandoned_no_reference/` 为放弃条目收容所，不删。
