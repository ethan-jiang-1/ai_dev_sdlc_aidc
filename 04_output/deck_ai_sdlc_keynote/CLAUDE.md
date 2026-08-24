---
title: CLAUDE.md — AI 时代 SDLC 变革 Keynote
stage: root
position: entrypoint
type: playbook
summary: Agent 操作手册。引导用户完成从 KOL 素材抽取到最终 PPTX 的全过程。
depends_on: []
feeds_into:
  - research/README.md
  - v1/outline/README.md
  - v1/manuscript/README.md
  - v1/session_design/README.md
  - v1/style/README.md
---

# AI 时代 SDLC 变革 — Keynote 制作手册

> 本文件是 agent 的操作手册。Agent 进入本目录后读取此文件，按固定流程引导用户完成全过程。

## 项目定位

- **Topic**: AI 时代 SDLC 的变化
- **形态**: 战略 Keynote（slides 是图片型）
- **语言**: 中英双语（slides 英文为主，演讲可中文）
- **源素材**: `../../01_sources/reference/kol/`（14 位 KOL + 3 场 2026 事件 + 跨公司共识 + Fable 5 信号）
- **方法论文档**: `../../_ppt_framework_v1/`（PPT 四阶段加工流，只读参考）

## 固定流程（不可跳过，不可重排）

```
Phase 0: 素材抽取与合成 → 从 KOL 素材中提取关键信号
    ↓
Phase 1: 叙事大纲 → 核心隐喻 + 公式 + 叙事弧 + Block 结构
    ↓
Phase 2: 完整文稿 → 每一张 slide 的完整论述内容
    ↓
Phase 3: Slide 规格 → 四层规格（Meta / Concept / Image Prompt / Speaker Note）
    ↓
Phase 4: 视觉风格 → 视觉系统 + Style Master
    ↓
Phase 5: 生产管线 → 生成图片 → 合成 PPTX
```

**每个 Phase 结束有 ⛔ 闸门——用户确认后才能进入下一个 Phase。**

## 角色分工

- **Agent owns process**: 流程引导、文件管理、阶段切换、gate check、生成候选方案
- **User owns substance**: 隐喻对不对、论述准不准、数据真不真、视觉喜不喜欢

核心原则：**用户做选择题，agent 做创造性劳动。** 不要问"你的隐喻是什么"——生成 2-3 个候选让用户选。

## 各 Phase 概览

### Phase 0: 素材抽取与合成
- **输入**: `../../01_sources/reference/kol/` 全部源材料
- **产出**: `research/source-synthesis.md`（按主题组织的关键信号 + 引用溯源）
- **参考**: `research/README.md`

### Phase 1: 叙事大纲
- **输入**: Phase 0 合成材料
- **产出**: `v1/outline/outline.md`
- **内容**: 核心隐喻、核心公式、叙事弧线、Block 划分、每张 slide 的一句话 claim
- **参考**: `_ppt_framework_v1/02_content_design/`

### Phase 2: 完整文稿
- **输入**: Phase 1 大纲
- **产出**: `v1/manuscript/manuscript.md`
- **内容**: 每张 slide 的完整论述、数据引用、过渡逻辑、speaker note 草稿

### Phase 3: Slide 规格
- **输入**: Phase 2 文稿
- **产出**: `v1/session_design/deck-brief.md`
- **内容**: 四层规格（VISUAL TYPE + KICKER + CLAIM / Concept 层 / Image Prompt 层 / Speaker Note 层）

### Phase 4: 视觉风格
- **输入**: Phase 3 deck brief（理解内容调性）
- **产出**: `v1/style/visual-style.md` + `v1/style/style_master.jpg`
- **参考**: `_ppt_framework_v1/01_visual_style_master/`

### Phase 5: 生产管线
- **输入**: deck brief + style master
- **产出**: `v1/production/ppt/*.pptx`
- **参考**: `_ppt_framework_v1/04_production_pipeline/`

## 编辑链（迭代期）

| 改动类型 | 重跑范围 | 成本 |
|---------|---------|------|
| 改某页 speaker note | Phase 5 only | ~30s |
| 改某页 IMAGE PROMPT | Phase 3 → 5（单页） | ~5min |
| 改某页 claim/title | Phase 3 → 5（单页） | ~5min |
| 加/砍/重构 slide | Phase 1 → 2 → 3 → 5 | ~数小时 |
| 改核心隐喻/公式 | 全部 Phase | 需新版本快照 |

## 版本快照规则

- 改几个字/几张图 → 直接改，不新建版本
- 砍/加/重构 slide → `cp -r v1 v2`，在新版本中改
- 改核心隐喻/公式/视觉方向 → `cp -r v1 v2`

## 源材料路径速查

| 想看什么 | 路径 |
|---------|------|
| 14 位 KOL 深度拆解 | `../../01_sources/reference/kol/_raw_kol/` |
| 跨公司变革共识（7人） | `../../01_sources/reference/kol/_raw_frontier/` |
| Fable 5 变革信号 | `../../01_sources/reference/kol/_raw_fable5/` |
| Deer Valley Retreat (Feb 2026) | `../../01_sources/reference/kol/_raw_agile_manifesto_2026/` |
| Pragmatic Summit (Feb 2026) | `../../01_sources/reference/kol/_raw_promatic_summit_2026/` |
| Engelberg Retreat (Jul 2026) | `../../01_sources/reference/kol/_raw_engelberg_2026/` |
| AWS AIDLC 方法论 | `../../01_sources/reference/corp/_raw_aws/` |
| 生态全景 | `../../01_sources/reference/corp/_raw_ecosystem/` |
| PPT 方法论（只读） | `../../_ppt_framework_v1/` |

## 三条铁律

1. **用户做选择题，你做创造性劳动。** 生成候选方案，让用户选。
2. **闸门不可跳过。** 每个 Phase 结束等用户确认。跳过闸门的代价是指数级。
3. **源文件是 single source of truth。** 改动永远从 markdown 开始，绝不直接改派生品。
