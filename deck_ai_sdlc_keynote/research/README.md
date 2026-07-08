---
title: Phase 0 — 素材抽取与合成
stage: phase_0
position: pre_phase
type: guide
summary: 从 KOL 源材料中提取关键信号，按主题组织，为叙事大纲提供素材基础。
depends_on: []
feeds_into:
  - v1/outline/outline-v1.md
agent_action: guide
---

# Phase 0: 素材抽取与合成

> 本阶段目标：不是把所有材料读一遍——而是**按叙事线索**提取关键信号，让 Phase 1 有据可依。

## 为什么需要这个阶段

标准 PPT 框架假设你已经有清晰的内容方向。但你的素材是 14 位 KOL + 3 场事件 + 跨公司共识——信息量巨大且互有关联。需要先做一轮结构化抽取，才能进入叙事设计。

## 来源

> ⚠️ **本 Phase 的所有素材来自一个地方：`../aidlc_reference_kol/`**
> 这是整个项目的信息地图——14 位 KOL + 3 场 2026 年关键事件 + 跨公司变革共识 + Fable 5 信号。
> 每一条抽取出来的信号，都必须能回溯到这个目录中的具体文件。

### 源目录信息地图

```
../aidlc_reference_kol/
│
├── _raw_kol/                          ← 14 位 KOL 深度拆解
│   ├── README.md                      ← 含共识/分歧矩阵（必读）
│   ├── 01_thoughtworks.md             ← ThoughtWorks: 认知债、Harness Engineering
│   ├── 02_martin_fowler.md            ← Martin Fowler: "Verified" 定义变化
│   ├── 03_dave_farley.md              ← Dave Farley: CD 让 AI 时代存活
│   ├── 04_simon_willison.md           ← Simon Willison: SDLC 围绕"一天几百行"设计
│   ├── 05_kent_beck_agile.md          ← Kent Beck: XP 在 AI 时代复苏
│   ├── 06_synthesis.md                ← 跨人物主题分析（共识区/分歧区）
│   ├── 07_andrej_karpathy.md          ← Andrej Karpathy: Vibe Coding→Agentic Engineering
│   ├── 08_boris_cherny.md             ← Boris Cherny: Claude Code 之父
│   ├── 09_ryan_lopopolo.md            ← Ryan Lopopolo: 100 万行零人写零人审
│   ├── 10_kief_morris.md              ← Kief Morris: in the loop → on the loop
│   ├── 12_gergely_orosz.md            ← Gergely Orosz: The Pragmatic Engineer
│   ├── 13_laura_tacho.md              ← Laura Tacho: 450+ 公司 12 万开发者数据
│   └── 14_thomas_dohmke.md            ← Thomas Dohmke: 前 GitHub CEO
│
├── _raw_frontier/                     ← 跨公司变革共识（7人 + 3份深度研究）
│   ├── README.md                      ← 含人物速查表 + 来源全量映射
│   ├── 01_变革共识_跨公司方法论趋同.md  ← 七个跨公司共识 + 变革烈度
│   ├── 02_人物深度_每个人的变革视角.md  ← 七人各自触发事件 + 分歧矩阵
│   └── 03_流程死亡清单_什么不再适用.md  ← 22 条被宣布已死的做法 + 替代方案
│
├── _raw_fable5/                       ← Fable 5 变革信号合成（16 个使用样本）
│   ├── README.md                      ← 含来源全量映射 + 证据强度评估
│   ├── 01_Fable5_颠覆了什么_核心信号.md ← 10 个核心信号 + 12 条流程变革清单
│   ├── 02_流程变革_具体模式与检查清单.md ← AI Sandwich、Brief-Review-Signoff
│   └── 03_粗糙信号_早期观察与未成形想法.md ← 8 个弱信号 + 7 个开放问题
│
├── _raw_agile_manifesto_2026/         ← Deer Valley Retreat（Feb 2026）
│   ├── README.md                      ← Agile Manifesto 25 年后同一片山
│   ├── 02_rigor_relocation.md         ← "严苛去哪儿了？"
│   ├── 03_supervisory_engineering.md  ← Supervisory Engineering / Middle Loop
│   ├── 05_cognitive_debt.md           ← Margaret-Anne Storey 命名的新"债"
│   ├── 06_three_tier_developer_split.md ← Junior 安全/Mid 危机/Senior 转向架构
│   └── 07_supervisory_programmer.md   ← 管理多个 Agent 的日常
│
├── _raw_promatic_summit_2026/         ← Pragmatic Summit（Feb 2026）
│   ├── README.md                      ← Beck+Fowler 同台、Willison、Dohmke+Rajan
│   ├── 01_beck_fowler_fireside.md     ← Beck + Fowler 炉边对话
│   ├── 02_willison_agentic_engineering.md ← Simon Willison
│   ├── 03_dohmke_rajan_roundtable.md  ← 前 GitHub CEO + Atlassian CTO
│   ├── 04_tacho_dx_data_joint_statement.md ← Laura Tacho DX 数据
│   └── 06_cross_session_themes.md     ← 跨 session 主题
│
└── _raw_engelberg_2026/              ← Engelberg Retreat（Jul 2026）
    ├── README.md                      ← "从实验到生产的转折点"
    ├── 02_evidence_is_in.md           ← "not slides — production"
    ├── 03_optimiser_vs_learner.md     ← 组织设计框架
    ├── 04_galaxy_brain_debate.md      ← 架构辩论
    ├── 05_harness_engineering_emergence.md ← Harness Engineering 从零到核心议题
    ├── 06_tdd_as_prompt_engineering.md ← TDD = Prompt Engineering
    └── 07_risk_tiering.md             ← AI 生成变更的三级风险分类
```

### 辅助来源

```
../aidlc_reference_corp/
├── _raw_aws/                          ← AWS 官方 AI-DLC 方法论
└── _raw_ecosystem/                    ← 非 AWS 生态全景
```

### 各目录之间的关系

| 如果你关心... | 先看 | 特点 |
|------|------|------|
| 具体的人怎么说 | `_raw_kol/` | 单人观点，有共识/分歧矩阵 |
| 四家公司达成了什么共识 | `_raw_frontier/` | 跨公司合成，有变革烈度评估 |
| Fable 5 具体改变了什么 | `_raw_fable5/` | 16 个使用样本，有证据强度 |
| Agile 社区怎么回应 AI | `_raw_agile_manifesto_2026/` | 概念密度最高，多个新术语发源地 |
| 工业界的大会声音 | `_raw_promatic_summit_2026/` | 公开大会，有数据（Tacho 12 万开发者） |
| 从实验到生产的转折 | `_raw_engelberg_2026/` | 最新（Jul 2026），语气从犹豫→自信 |
| 厂商方法论框架 | `_raw_aws/` | 自顶向下设计，“正确流程应该长这样” |

## 产出

`source-synthesis.md`——按以下维度组织的信号图谱：

1. **共识区** — 哪些判断所有人/大多数人都同意？
2. **分歧区** — 哪些问题上存在根本分歧？
3. **已死/正在死的流程** — 哪些 SDLC 实践被宣布不再适用？
4. **新涌现的概念** — 哪些新术语/新框架在形成？（Harness Engineering、Cognitive Debt、Supervisory Engineering、Middle Loop...）
5. **关键引用** — 最有冲击力的原话（可进入 slides 作为 pull quote）
6. **数据点** — 可引用的量化证据

## 工作方式

- Agent 读取各源目录的 README（已有完整的索引和共识/分歧矩阵）
- 提取跨源重复出现的主题
- 标注每条信号的证据强度（单个 KOL 断言 vs 多人独立验证 vs 有数据支撑）
- 用户审核：哪条信号放错了？哪条漏了？

## ⛔ 闸门

Phase 0 完成标准：
- [ ] 六大维度（共识/分歧/已死流程/新概念/关键引用/数据点）均有内容
- [ ] 每条信号标注了来源文件路径
- [ ] 用户确认：核心信号的抽取准确、无重大遗漏
