---
type: index
content_type: readme
directory: 01_seed_reference/loop_engineering
description: Loop Engineering 证据集合（2026-06 起）——三派组织，铁律见下
research_date: 2026-09-26
reorg_date: 2026-10-06
---

# loop_engineering — Loop Engineering 证据集合（2026-06 起）

> 本集合只收一件事的证据：**loop engineering 这场实践运动**（2026-06 起成为公开名字）。
> 它是 [`_raw_people/`](../voices/_raw_people/README.md)（按人铺全景）的**主题波次补充**，并按**立场分三派**组织。

## 铁律（先于一切，违反即扫出）

| # | 规矩 |
|---|---|
| 1 | **相关性是底线**：每条素材必须与 loop engineering 有**明确挂钩**——循环结构 / 停止条件 / 预算与熔断 / 外层调度 / 验证回路 / 无人值守运行 / 循环产品化机制，七类之一。挂不上的泛 AI/agent 素材**不收**；已在档的发现挂不上，**直接扫掉，不写解释** |
| 2 | **vibe coding 不收**——非专业层讨论，公认不靠谱，与本集合无关 |
| 3 | **拉取纪律**：要拉的内容多通道努力拉；两轮拉不到就放弃，不留待回源挂账。例外：未发布 ≠ 拉不下来（年度报告类保留重扫位） |
| 4 | **热度/票数从来不是收录理由**，一手内容才是 |
| 5 | **时间窗** 2026-06 起（更早一手源只入主题时间线作谱系背景）；**来源**只收一手（原始英文源为主；中文原创社区讨论按社区证据收，编译只作交叉验证） |

扫掉的内容不再留说明——git 历史即档案。

## 证据分层（2026-10-06 用户定：两个正交维度，不是线性三层）

**同一句"难"，出自不同人群是不同证据。** 分层按两个正交维度：

| 维度 | 取值 | 落在结构哪里 |
|---|---|---|
| **① 影响力** | KOL ↔ 群众 | KOL＝`kol_tech/`、`kol_product/`（目录名即两维：kol_=影响力层，tech/product=技术深度）、`orgs/`（组织）；群众＝`community_tech/`（专业程序员群众）、`community_product/`（非专业群众）——与 kol_* 命名对称 |
| **② 技术深度** | 专业程序员 ↔ 非专业（产品经理/创业者/分析师） | **两层里都有**：每个 KOL 文件头部标「人群类型」；`community_tech/`＋`community_product/` 两个子目录（目录名即两维） |

四个象限都要有声音，缺哪个象限就是证据盲区：

| | 专业程序员 | 非专业（产品/商业） |
|---|---|---|
| **KOL** | Ronacher、Willison…（当前库存绝大多数） | Mollick（商学院教授）、Dwarkesh（播客作家）、Nadella/Jensen（商业领袖）、Not Boring/The Diff/a16z（商业分析） |
| **群众** | V2EX/HN/GitHub 一线开发者（现有 community 主体） | 产品经理、indie 创业者、Lovable/Bolt 用户（**当前接近零——缺席本身是证据**） |

数据层（机构采样）弥合统计口径。**判读标准**：跨象限印证（如专业 KOL 说难＋产品群众进不来）才可下结构性结论。

**名单与派别权威**：[`02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md`](../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)（§A 入册名单＋§A2 三派分野）。本 README 只管素材索引与规矩。

## 目录结构

```text
loop_engineering/
├── README.md                  # 你在这里：铁律 + 素材索引
├── 00_debates_2026.md       # 跨人对峙层——10 条交锋轴完整链
├── 00_three_camp_landscape.md # ★ 三派地图与社区实况判读（结论入口）
├── 01_advocates/              # 推动派（发起者＋吹捧者）
│   ├── README.md（索引）＋四象限目录＋orgs/＋events/
│   └── kol_tech/andrew_ng/    #   四件套卡（历史卡；原 kol_scan.md 已拆为一人一档）
├── 02_neutral/                # 中性派（边界与审慎）
│   ├── README.md（索引）＋四象限目录＋orgs/＋events/
└── 03_skeptics/               # 反对与怀疑派
    └── README.md（索引）＋四象限目录＋orgs/
```

## 三派入口

| 派 | 一句话口径 | 入口 |
|---|---|---|
| **三派总览与社区实况判读** | 三派地图＋痛点对位＋词的状态＋证据边界 | [`00_three_camp_landscape.md`](00_three_camp_landscape.md) |
| **跨人对峙层** | 10 条交锋轴完整链 | [`00_debates_2026.md`](00_debates_2026.md) |
| **推动派**（发起者＋吹捧者） | 把"设计循环让 agent 自动推进"当默认方向推荐 | [`01_advocates/`](01_advocates/README.md) |
| **中性派**（边界与审慎） | 承认机制有条件成立，划边界、要求约束、先测再信 | [`02_neutral/`](02_neutral/README.md) |
| **反对与怀疑派** | 给反证与批评（失败账本/质量退化/经济/人的角色） | [`03_skeptics/`](03_skeptics/README.md) |

每派目录入口：`README.md`（索引）＋四象限目录（kol_tech/kol_product/community_tech/community_product）＋orgs/events。KOL 与群众证据分开标注，不并列引用。

**KOL 独立档头部格式（2026-10-07 背景补齐批）**：身份（若有）→ **背景**（一人一段职业履历速写；来源随行括注「履历核」；两处与档内旧口径冲突的——sean_goedecke「Google SWE」、kyle_lee「个人实践者」——已在行内标注修正而非静默改写）→ 号召力（若有）→ 派别权威 → 人群类型。

## 与其他集合的关系

| 集合 | 关系 |
|---|---|
| [`../voices/_raw_people/`](../voices/_raw_people/README.md) | 人物全景档案；本集合只放指针＋loop 专项增量 |
| [`../field_samples/fable5/`](../field_samples/fable5/README.md) | 按**模型**收样本；本集合按**命名事件**收声音 |
| [`../graph_engineering/`](../graph_engineering/README.md) | 姊妹专题（2026-07 起下一波命名） |
