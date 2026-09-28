# ai_loop_engineering — Loop Engineering

**定位**：**2026-06 起 loop engineering 这场被命名的实践运动**——谁在说、说了什么、怎么实操、
与 SDD / harness 治理的边界在哪。研究层·分析，不是操作规程（分工见 §4）。

**分法**：`raw/`（一手素材）→ `digested/`（消化与判读）→ `result/`（成稿）。**两个增长轴独立可加**：
轴一「人」＝台账加一行（素材进回源档案；**建卡是例外**，判据见 §1 素材形态）；轴二「问题」＝加一个议题加一个编号文件。加东西时不改别的文件。
**一个专项深挖区**（2026-09-28 用户决定）：`stop_conditions/`＝停止条件三件骨架按点深挖（每点一孙目录，practices＋insights）；素材仍进 raw、判定仍归 digested，它只装做法与洞察，见该目录 README。

```text
ai_loop_engineering/
├── README.md                  # 你在这里：地图 / 判据 / 分工 / 增长规则
├── CURRENT.md                 # 热区：本轮做到哪、下一步动哪个文件、缺口
│
├── raw/                       # 一手层：原文/原帖/转写 + 台账/时间线/回源档案（判读展开在 digested，时间线只留指向 digested 的压缩注记）
│   ├── 00-timeline.md         #   命名与事件时间线（append-only，每条带日期 + 出处 + 强度）
│   ├── research-plan.md        #   ★ 研究推进控制面：问题树 / 分路 / Agent 委派 / 质量门 / backlog
│   ├── kol-roster.md          #   ★ KOL 台账＝唯一名单权威（收录判据 / 名单 / 号召力依据 / 状态）
│   └── evidence-*.md          #   回源档案：委派回源的逐字摘录 + 引用链（按日期-路别命名；素材的常态形态）
│
├── digested/                  # 消化层
│   ├── README.md              #   问题看板：已答 / 在答 / 待答（增长从这里一眼看见）
│   ├── kol/<slug>.md          #   一人的消化（有料才写；slug 与台账对齐）
│   └── NN-<question>.md       #   跨源综合（编号增长）
│
├── result/                    # 成稿层：landscape.md（2026-09-27 过筛综述）
├── stop_conditions/           # ★ 专项深挖区（2026-09-28 立）：三件骨架按点切片
│   ├── README.md              #   地图 / 分工边界 / 增长规则
│   ├── 01_machine_gates/      #   ① 机器可核判据逐轮闸门（practices + insights + 待挖）
│   ├── 02_hard_caps/          #   ② 硬性资源上限兜底
│   └── 03_verdict_split/      #   ③ 验收与干活分离
└── figures/                   # SVG
```

---

## 1. 收录判据（KOL 台账的执行口径）

**时间窗**：**2026-06 起**（loop engineering 成为公开名字）。
更早的一手源（Ralph Wiggum loop 2025-07、Anthropic《Building effective agents》2024-12、
harness engineering 2025-11）**只入 `raw/00-timeline.md` 作谱系背景，不入 KOL 名册**。

**号召力**（至少满足一条，且**必须在台账里写明是哪一条**）：

| 口径 | 含义 |
|---|---|
| ① 术语定义者 | 给出可操作定义，且被他人引用 |
| ② 被一线引用 | 被厂商官方文档 / 其他入册 KOL / 主流工程媒体转述 |
| ③ 一线规模 | 自述或可核的实践规模（产出量 / 团队 / 项目） |
| ④ 分发规模 | star / 粉丝 / 下载——**只作辅助，不作主证** |

**硬性排除（2026-09-26 用户定的质量门槛，高于上面四条口径）**：

- **论坛评论者不算 KOL**——HN / Reddit 上的用户名（如 yoaviram、gsadaka 之流）是随机评论，不是有影响力的思考。
  它们最多作"社区情绪"旁证，**单独标注、绝不与 KOL 证据并列**。
- **聚合媒体与标题党不入册**——"是台印钞机还是绞肉机"式的内容直接丢弃；中文聚合站转述一律按二手铁律处理。
- **碎片推文不作深度证据**——若某词源人物只有碎片帖（几句话、无机制无洞察），如实记录"**词源是碎片级的，无深度内容**"，
  然后另找该人物真正有深度的长文/访谈；**不硬凑、不用碎片帖冒充洞察**。
- **深度是硬要求**——入册内容必须含操作性洞察（定义怎么下、机制怎么工作、边界与失败模式在哪）。
  有影响力的人背后有深刻思考；只有热度没有思考的内容，只会干扰判断。

**每条入册必须附一句「为什么这人算 KOL」**（职位 / 代表作 / 被谁引用）。

**证据强度**：一手原文 > 本人转述 > 媒体转述 > 二手编译。
中文二手只作交叉验证，不作唯一引用（沿用 [`01_sources/reference/kol/README.md`](../../01_sources/reference/kol/README.md) 铁律）。

**素材形态（2026-09-26 回源轮定，取代上午的"每人建卡"设想）**：
**回源档案（`raw/evidence-*.md`）是素材的常态形态**——按问题组织、带引用链、一次回源一份档案。
深度四件套卡（[`01_sources/reference/kol/_raw_loop_engineering/`](../../01_sources/reference/kol/_raw_loop_engineering/README.md) `<slug>/`）
只给"素材多到一份回源档案装不下"（**≥3 份独立一手长文**）的人。**当前无待建卡**——已有的 andrew_ng 卡是**规则设立前的历史卡**（其独立一手长文仅 1 份；保留它因他是命名事件锚点，**不代表达标**）；
其余入册者的素材留在 evidence 档案，**不为每人建卡**（词源碎片级、中文编译者更不建）。

**回源档案纪律**（2026-09-26 自 org/、community/ 两 README 合并收敛，两者已撤销）：
每条记录带 **URL ＋ 发布日期 ＋ 观测日期（两者分开记）＋ 证据强度**；一手原文优先，
**中文二手只作交叉验证、编译者评论与原作者原话分开标注**；社区帖的价值在第一人称叙述与反例，
**热度不等于证据**；已在别处有唯一 home 的只放指针＋增量摘录，不复制正文。

---

## 2. 增长规则（加东西时照这个走）

| 增长事件 | 动作 | 不动什么 |
|---|---|---|
| 新 KOL 入册 | `raw/kol-roster.md` 加一行；素材走回源档案（**建卡仅当其独立一手长文 ≥3 份**，见 §1 素材形态） | 不改其他文件 |
| 老人出新料 | 追加对应 evidence 档案（或其卡片，若有）→ 台账只改状态列 | 不新建目录 |
| 新证据（任何来源） | 新开一路回源档案 `raw/evidence-<日期>-<路别>.md` → `00-timeline.md` 加行（若有日期锚） | 不改 KOL 侧 |
| 新议题 | `digested/NN-<slug>.md` → `digested/README.md` 看板加一行 | 不改编号顺序（编号 = 创建序） |
| 三件骨架深挖（新做法/新洞察） | `stop_conditions/<点>/practices.md`（或 `insights.md`）加行；新来源仍先进 evidence 档案 | 不动 digested 判定——判定级结论回流 `digested/03`，本目录只留指针 |
| 结论过筛 | 从 `digested/` 抽进 `result/` | 未采纳线索留 `digested/` 原位，不删 |

---

## 3. 与相邻主题的分工边界

> 这是本主题最容易和别处打架的地方，先写死。**冲突时以本节为准。**

| 主题 | 管 | 不管 |
|---|---|---|
| **本主题** | loop engineering **这场运动本身**：命名谱系、KOL 一手见解与实战、构件定义、趋势判定、与 SDD 的边界**判定** | SDD 工具生态 → [`03_practice/spec_driven_development/`](../../03_practice/spec_driven_development/README.md)；harness/context 治理**操作规程** → [`03_practice/harness_governance/`](../../03_practice/harness_governance/README.md)；人物全景档案 → [`01_sources/reference/kol/_raw_kol/`](../../01_sources/reference/kol/_raw_kol/README.md) |
| [`03_practice/harness_governance/`](../../03_practice/harness_governance/README.md) | **单次运行可信**：约束写进环境（门禁 / 传感器 / 漂移清理），诊断轴＝"agent 缺哪句话"①–⑦ | 多轮的**自主治理**（停止条件、外层调度、自主度分档、人在环位置；队列/次序经 feature_list 类进度规格覆盖——**跨 feature 在途可见性＝已登记的开放缺口**）——loop 治理的地盘（判读归本主题、操作规程归 [`03_practice/loop_governance/`](../../03_practice/loop_governance/README.md)） |
| [`03_practice/beyond_spec_driven_development/`](../../03_practice/beyond_spec_driven_development/README.md) | SDD 批判之后的**形态光谱**（本主题与其是**正交轴关系、不是光谱上的一行**——定位说明在该主题 §6.1，本主题只放指针） | 不重复 KOL 一手台账 |
| [`03_practice/spec_driven_development/debate/`](../../03_practice/spec_driven_development/debate/README.md) | SDD 阵营的辩论谱系与工具对照 | 不做 loop 侧的 KOL 调查 |
| [`../agent_goal_eval/`](../agent_goal_eval/README.md) | 前沿来源如何构造 goal 与 eval（定调在该目录 README §1） | 循环怎么跑、取题、授权、调度、停止骨架仍归本主题。本主题已有的 `/goal`、grader、验证格引句留在原档案 |

**一句话分界**：**harness 治理管"约束写进环境"，本主题管"循环怎么跑、谁决定下一轮、人站在哪"。**
前者是**知识/环境**轴，后者是**控制/分配**轴——两个轴不同，故不合并。goal 与 eval 如何构造另立 [`agent_goal_eval`](../agent_goal_eval/README.md)。

---

## 4. 升格触发器 —— 已立题，证据边界在本轮收紧（2026-09-27）

**2026-09-26 的立题链**：三路回源（evidence-a/b/c）→ 判读（digested 01/03/05）→ 触发器评估 → 立题 **[`03_practice/loop_governance/`](../../03_practice/loop_governance/README.md)**（用户 2026-09-26 决定并授权命名）。**2026-09-27 的 E/F/G/H 补证据没有撤销立题，但把“收敛”从普遍规范收紧为“公开机制中反复出现的设计模式”，并新增 automation/autonomy/harness/loop 判读篇 06。

**当前评估**：

| 触发问题 | 结果 | 判定 |
|---|---|---|
| ① 停止条件怎么写 | **机制骨架反复出现**——机器可核判据、硬上限/熔断、验收与干活分离在多机构材料中出现；但来源按机构/引用链去重后，尚无跨组织效果证据 | ✅ 足以立题，不能写成最佳实践已证 |
| ② 外层调度谁做 | **两种公开形态已观察到**——持久进度/任务账本与时间/事件触发；Osmani/DSH/Managed Agents/OpenClaw 均显示不同尺度；但不是 loop 最小定义，也没有统一跨 feature priority/授权/验收盘 | ✅ 足以研究和试验，不能写成行业主导/人工审批已退出 |
| ③ 自主度分档与人在环位置 | **位置词汇与事件判据存在**——四级/σ/运行模式 + 动作边界、歧义、风险、拒绝预算、工具级 interrupt；**通用轮次刻度与质量置信度放行仍缺** | ⚠️ 半过；实践层必须保留开放缺口 |

**结论**：主题仍够格立题；但研究与实践必须把“设计模式存在”“机制如何工作”“真实效果/采用率”分开，不把单一作者 opinion、官方产品文档或内部评测直接升级成行业规范。

**命名**：实践主题不沿用 KOL 词（"loop engineering" 词源＝热度碎片、外延未收敛，判定见 [`digested/01`](digested/01-命名谱系.md)），
按仓库五层框架定名 **`loop_governance`**，与 `harness_governance` 同构成对（环境轴 / 控制轴）。

**为什么不是并进 `harness_governance/`**：那边的诊断轴是"agent 缺哪句话"（①–⑦ 知识缺口），
本主题的轴是"自主度与人的位置"（控制分配）。塞进去会破坏它那条已经用户确认过的干净轴，
且该主题 2026-09-21 已由用户决定转入**维护态**，不宜再开新战场。

---

## 5. 纪律

- **一手源优先、来源可溯、标注观测日期**（与 `01_sources/`、`03_practice/` 统一）。
- **单一事实来源**：素材权威在 `01_sources/`，判读权威在 `digested/`，成稿权威在 `result/`；
  本文件只管地图与规则，**不复制正文**。
- **外部研究只作线索**：姊妹仓库的研究（如 `/Users/bowhead/deepseek-harness/_faq_on_digested/15_loop-engineering-vs-sdd/`）
  可作**线索与对照**登记进 `00-timeline.md` 或 `digested/`，但**其结论未经本主题独立复核前，标注「转引·待回源」，不作本主题的主张依据**。
- **临时产物**一律放仓库根 `.tmp-` 前缀（`.gitignore` 已覆盖），版本收口即清理。

---

## 6. 从哪开始读

| 想知道 | 去哪 |
|---|---|
| 这波谁在说、号召力依据是什么 | [`raw/kol-roster.md`](raw/kol-roster.md)（★ 唯一名单权威） |
| 什么时候发生了什么事 | [`raw/00-timeline.md`](raw/00-timeline.md) |
| 逐字引句与回源过程在哪 | `raw/evidence-*.md`（回源档案，按日期-路别命名） |
| 过筛综述在哪 | [`result/landscape.md`](result/landscape.md) |
| 现在做到哪、下一步干什么 | [`CURRENT.md`](CURRENT.md) |
| 有哪些议题、答了几个 | [`digested/README.md`](digested/README.md)（问题看板） |
| 三件骨架每一点上各家怎么做、为什么工作、边界在哪 | [`stop_conditions/README.md`](stop_conditions/README.md)（按点深挖区，2026-09-28 起） |
| 单个人的完整观点 | [`digested/kol/`](digested/kol/andrew_ng.md)（已消化）/ `01_sources/reference/kol/_raw_loop_engineering/`（素材） |
