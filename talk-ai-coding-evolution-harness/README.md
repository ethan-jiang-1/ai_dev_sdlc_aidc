# AI Coding 演变指南：从 Prompt 到 Harness

本目录是这场 talk 的内容与生产工作区，也是跨对话的项目记忆。
**目的只有一个：把故事线推敲出来，再让它变成一份能站住脚的 PPT。**

> **题目为工作稿，待确认**；副标题候选「生成不是瓶颈，交付才是」。见 [`01_storyline/04-open-questions.md`](./01_storyline/04-open-questions.md) Q4。

**主题速记**：听众是**做团队协作开发、交付物对可靠性 / 合规 / 审计要求高、质量门槛高**的软件团队
（产品经理 + 程序员）。他们已经有 AI Coding 基础，不需要科普 prompt 和 context。
本 talk 的问题不是"一个人要把 AI Coding 掌握到多深"，而是：
**同一个模型，为什么交出来的东西不一样？** 答案落在模型外面那圈叫 **harness** 的东西上——
它是交付质量的真实变量，而且已经出现把 harness 做成可替换件的路线。

**规格**：75–90 min · **正文 36 页 + 呼吸页 B1–B6（不编页码）= 42 张 slide**（按约 79 min 排）。
视觉方向：纸白底 + 代码终端母题，全原生矢量。

**★ 版本单一纪律（2026-09-17 定，违反即会造成改稿摇摆）**：
每一类产物**目录里只留当前版本**。被取代的旧版本一律**移出本目录**，归档到仓库根
`.tmp-harness-talk-archive-YYYYMMDD/`（`.gitignore` 已覆盖，不入库，仅供回查）。
**不允许**在两个文件里维护同一份内容，也不允许"新版在下、旧版还在旁边"——
旧版本号、旧页码留在目录里，就是下一轮改错稿的来源。

**两条硬约束**（详见 [`AGENTS.md`](./AGENTS.md) 的对象红线）：
1. 全场 audience-facing 文字**不出现 OPC / 一人公司 / 姊妹项目引用**。
2. **不点听众所属行业名、不用行业专属术语**——按特征描述，换观众不用改稿。

## 工作区地图

```text
talk-ai-coding-evolution-harness/
├── README.md                                # ★【新对话从这里开始】本文件：地图 + 素材说明 + 工作方式
├── AGENTS.md                                # 【agent 手册】进入仪式 + 门禁 + 规则 + 已知陷阱 + 生产工具链
├── CURRENT.md                               # 【当前态权威】现在做到哪一步、下一步动哪个文件
├── CONTEXT.md                               # 【术语权威】本 talk 的局部 glossary + 禁用词
├── _reference/                              # 上游素材 symlink（只读），说明见其 README
│   ├── README.md                            #   十三份素材的分工 + 引用约定
│   ├── rawdata_ai-coding-evolution-final/   #   【symlink】宏观：五层演变最终报告
│   ├── rawdata_harness-selection-final/     #   【symlink】★ 尾巴主料：Harness Agent 选型研究
│   ├── rawdata_harness-selection-wave1/     #   【symlink】逐 topic 证据摘要
│   ├── rawdata_harness-selection-wave2/     #   【symlink】跨话题综合
│   ├── rawdata_pi-digested/                 #   【symlink】★ Pi 源码消化（harness 评价 / 边界短板 / 扩展 / 配置哲学）
│   ├── rawdata_pi-faq-on-digested/          #   【symlink】★ Pi 二次研究问答（含 Pi vs DSH 逐面对照）
│   ├── rawdata_dsh-faq-on-digested/         #   【symlink】DSH Harness 机制问答
│   ├── rawdata_dsh-digested/                #   【symlink】DSH 源码消化（底层机制）
│   ├── rawdata_dsh-plugin-seam-maturity/    #   【symlink】插件接缝与成熟度
│   ├── rawdata_dsh-plugin-business-ladder/  #   【symlink】插件对 owner 的收益阶梯
│   ├── rawdata_dsh-plugin-ecosystem-distribution/ # 【symlink】插件生态分布快照
│   ├── rawdata_ai-coding-evolution-reference/ # ★【symlink】一手来源卡片 137 张（回源 / 引文 / 核口径来这层）
│   └── rawdata_harness-selection-reference/ # ★【symlink】一手来源卡片 168 张（P25 官方博客卡、P26 flash 原始卡在这）
├── 01_storyline/                            # ★ 故事线推敲主战场
│   ├── 00-storyline-map.md                  #   故事线总图（v2.1）：主轴 + 六步脊柱 + 五层表 + 两类程序表 + 节奏
│   ├── 01-thesis-and-positions.md           #   核心论点与立场（主张 / 支撑 / 强度）
│   ├── 02-turning-points.md                 #   推导句清单（〔前提〕〔推导〕〔结论〕〔边界〕）
│   ├── 03-audience-and-pitch.md             #   听众、时长、目的、基调、三个禁止
│   ├── 04-open-questions.md                 #   历史决策流水（已决 / 待确认 / 待办 / 已排除）
│   └── 06-harness-internals.md              #   harness 里头干啥（抓要害的讲法 + 团队映射）
├── 02_evidence/                             # 素材与口径
│   └── 00-absorption-plan.md                #   ★ 进货单 + 解释性结论 + 十五条口径红线
├── 03_outline/                              # 页面结构与承载
│   ├── 00-page-structure-v3.md              #   ★ 36 页页面职责（每页答哪一步 + 时长 + 呼吸页 B1–B6）
│   └── 01-visual-carrier-plan.md            #   ★ 页面承载规格（四层承载 + 载体类型库 + 密度自检）
├── 04_drafts/                               # 生产事实稿
│   └── ppt-text-v3.md                       #   ★ 当前页面文案（36 页 + 呼吸页，四层承载）
└── 05_output/                               # PPTX 交付物
    ├── v0.1/visual-samples.html             #   视觉样片 4 张（已认可，视觉基准）
    └── v0.4/AI Coding 演变指南/             # ★ 当前 REVIEW 对象：42 张 PPTX + 42 个 .slide 源 + DESIGN.md
```

## 上游素材分工

**十三份**素材全部收在 [`_reference/`](./_reference/README.md) 下，只读。**分三层**（详见其 README）：

- **综合层** —— `*-final/`：报告正文（二手），给故事线与结论骨架。
- **一手来源卡片层** —— `*-reference/`（**305 张**）：每张带 `tier` / `source_type` / 可引原文。
  **引文、口径、日期、证据强度一律以这一层为准**；P6 / P7 / P25 三处回源核对就是靠它完成的。
- **消化层** —— `rawdata_pi-*` / `rawdata_dsh-*`：源码级消化，带锚点，第四幕的硬料。

四条主线：

- **宏观弧线** —— `rawdata_ai-coding-evolution-final/`：五层演变的最终研究报告。给整条故事线和论点骨架。
- **尾巴主料** —— `rawdata_harness-selection-final/`（+ wave1 / wave2）：Harness Agent 选型研究，
  11 候选评分卡 + **Pi 深挖** + **DSH 深挖** + `Product First vs Framework First` 路线对照。
  这是第四幕不用现编的原因。
- **Pi 的机制与代价** —— `rawdata_pi-digested/` + `rawdata_pi-faq-on-digested/`：
  Pi 的源码消化层（**`harness/02-Boundaries/` 那四条短板带源码锚点**，比二手报道扎实得多）
  与 Pi vs DSH 逐面对照。**第四幕 Pi 页的证据基座。**
- **DSH 的机制细节** —— `rawdata_dsh-*`：DSH 的机制问答、源码消化、插件接缝与生态数据。

## 工作方式

agent 的操作手册在 [`AGENTS.md`](./AGENTS.md)：每次进来先读它，按它定的步骤走，把状态落回源文件。
加工顺序固定为 **故事线 → 证据口径 → 页面职责 → 生产事实稿 → PPTX → 文字/视觉 QA**；
review 后若成稿发生变化，再按 **生产事实稿 → 页面职责 → 证据脉络 → 故事线** 反向同步。

**当前状态只认 [`CURRENT.md`](./CURRENT.md)**，词义只认 [`CONTEXT.md`](./CONTEXT.md)。
`_reference/` 下所有 symlink 只读。

## 临时目录约定

所有一次性产物（构建中间体、逐页 inspect、审稿草稿、模板试验）一律放在**仓库根目录**、
以 `.tmp-harness-talk-` 前缀 + 主题命名；工具自动生成的随机名目录（`.ppt-build-*`、`.tmp-xxx.XXXX`）算同类。
这些目录已被 `.gitignore` 覆盖、永不入库。**版本收口时清理**：某一版 PPTX 落进 `05_output/` 并完成 review 后，
对应的 `.tmp-harness-talk-vN*` 及散落目录即删，不跨版本堆积。
