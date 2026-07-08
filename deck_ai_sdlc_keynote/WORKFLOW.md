---
title: WORKFLOW — 信息流全景图
stage: root
position: workflow
type: reference
summary: 人类可读的工作流指南。从哪里开始、每一步做什么、产出什么、闸门是什么。
---

# WORKFLOW — 信息流全景图

> 这是你的地图。任何时候想知道"我在哪、下一步做什么"，回来看这个文件。

---

## 总览：五阶段加工流

```
源材料（aidlc_reference_kol/）
        │
        ▼
┌─────────────────────────────────────────────┐
│  Phase 0 · research/                        │
│  做什么：从 14 位 KOL + 3 场事件 + 共识/信号  │
│         中抽取关键主题，组织为信号图谱        │
│  产出：source-synthesis.md                  │
│  闸门：信号抽取准确、无重大遗漏              │
└────────────────────┬────────────────────────┘
                     │  → 进入 v1/
                     ▼
┌─────────────────────────────────────────────┐
│  Phase 1 · v1/outline/                      │
│  做什么：找核心隐喻、写可证伪公式、          │
│         画叙事弧线、定 slide 清单             │
│  产出：outline-v1.md（每张 slide 一句话 claim）│
│  闸门：隐喻确认、公式可证伪、故事线成立      │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│  Phase 2 · v1/manuscript/                   │
│  做什么：逐张 slide 展开完整论述，           │
│         附证据引用 + 过渡逻辑 + speaker note  │
│  产出：manuscript-v1.md                     │
│  闸门：论述准确、证据充分、逻辑连贯          │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│  Phase 3 · v1/session_design/               │
│  做什么：把文稿转化为四层 slide 规格         │
│         （Meta / Concept / Image Prompt /     │
│          Speaker Note）                      │
│  产出：deck-brief-v1.md（生产管线的直接输入） │
│  闸门：四层规格完整、VISUAL TYPE 分布合理    │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│  Phase 4 · v1/style/                        │
│  做什么：设计视觉系统，生成 Style Master     │
│  产出：visual-style-v1.md + style_master.jpg │
│  闸门：视觉风格锁定、与内容调性匹配          │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│  Phase 5 · v1/production/                   │
│  做什么：跑生产管线——生图 → 标题叠加 → PPTX  │
│  产出：ppt/*.pptx（最终交付物）              │
│  闸门：成品可交付                            │
└─────────────────────────────────────────────┘
```

---

## 逐步详解

### Phase 0 — 素材抽取（research/）

**你在哪个目录工作**：`research/`

**做什么**：
- 不创造新内容，只从已有源材料中提取和归类
- 目标不是"读完所有材料"，而是找到能支撑叙事的核心信号

**产出文件**：`research/source-synthesis.md`

**产出内容**（六个维度）：

| 维度 | 回答什么问题 | 示例 |
|------|-------------|------|
| 共识区 | 哪些判断大家都在说？ | "经典实践（TDD/CI/CD）反而更重要了"——Fowler、Farley、Willison、Beck 都同意 |
| 分歧区 | 哪些问题吵得厉害？ | "AI 能否作为半黑盒信任"——Willison 说可以，Fowler 说不行 |
| 已死流程 | 什么做法被宣布过时了？ | PR review 被 AI review 替代、手动写 user story... |
| 新概念 | 什么新术语在成型？ | Harness Engineering、Cognitive Debt、Middle Loop、Supervisory Engineering |
| 关键引用 | 哪句话最有冲击力？ | "SDLC is built around 200 lines a day" — Willison |
| 数据点 | 有什么量化证据？ | Laura Tacho: 450+ 公司 12 万开发者数据 |

**源材料在哪里**：
```
../aidlc_reference_kol/
├── _raw_kol/              ← 14 位 KOL（Fowler, Farley, Willison, Beck, Karpathy...）
├── _raw_frontier/         ← 跨公司共识（Anthropic/OpenAI/Cursor/Google 七人）
├── _raw_fable5/           ← Fable 5 变革信号（16 个使用样本）
├── _raw_agile_manifesto_2026/  ← Deer Valley Retreat（Feb 2026）
├── _raw_promatic_summit_2026/  ← Pragmatic Summit（Feb 2026）
└── _raw_engelberg_2026/        ← Engelberg Retreat（Jul 2026）
```

**Agent 的工作方式**：
1. 读各子目录的 README（已有共识/分歧矩阵和索引）
2. 提取跨源重复出现的主题
3. 标注证据强度（⭐⭐⭐ 多人独立验证 / ⭐⭐ 单人公开发言 / ⭐ 断言级）
4. 呈现给你审核——哪条不对？哪条漏了？

**⛔ 闸门**：你确认信号抽取准确、无重大遗漏 → 进入 Phase 1

---

### Phase 1 — 叙事大纲（v1/outline/）

**你在哪个目录工作**：`v1/outline/`

**做什么**：
- 从素材中找到那个"5 秒能讲清"的隐喻
- 写出可证伪的公式（能驱动整份 deck 的论证引擎）
- 画出叙事弧线（观众从哪出发 → 经过什么认知颠覆 → 到达哪里）
- 定 slide 清单（每张一句话 claim）

**产出文件**：`v1/outline/outline-v1.md`

**产出结构**：
```
1. Core Metaphor（2-3 个候选 → 你选一个）
2. Core Formula（A + B = C，可证伪）
3. Narrative Arc（旅程地图）
4. Block 结构（每个 Block 的叙事目的 + slide 归属）
5. Slide Map（完整清单：序号 / VISUAL TYPE / 一句话 CLAIM）
```

**信息流**：
```
research/source-synthesis.md ──→ 提供素材基础
                                        │
                                        ▼
                              你 + agent 做创造性决策：
                              隐喻、公式、弧线、slide 清单
                                        │
                                        ▼
                              outline-v1.md（锁定故事骨架）
```

**⛔ 闸门**：隐喻不是"差不多"是"就是它"、公式可证伪、故事线成立 → 进入 Phase 2

---

### Phase 2 — 完整文稿（v1/manuscript/）

**你在哪个目录工作**：`v1/manuscript/`

**做什么**：
- 把每张 slide 的一句话 claim 展开为完整论述段落
- 给每一条关键主张配上证据引用和来源路径
- 写 slide 之间的过渡句
- 写 speaker note 草稿（口语化）

**产出文件**：`v1/manuscript/manuscript-v1.md`

**每张 slide 展开为**：
```
## Slide N: [CLAIM]

### 核心论述（150-300 字）
→ 不是 bullet list，是可以读出来的连贯段落

### 证据/引用
→ 来源 + 引文 + 证据强度标注

### 视觉概念（初步）
→ 这张 slide 画面长什么样（方向描述，非 final prompt）

### 过渡句
→ 从哪来、到哪去

### Speaker Note 草稿
→ 演讲时怎么说（中文口语）
```

**工作节奏**：逐 Block 推进——写完一个 Block（3-7 张），停下来让你审核，确认方向对了再继续。

**信息流**：
```
outline-v1.md ──→ 提供 slide 清单和每张的 claim
                          │
                          ▼
                每张 slide 展开为完整论述
                证据从 research/source-synthesis.md 回溯到原始源文件
                          │
                          ▼
                manuscript-v1.md（锁定完整叙事）
```

**⛔ 闸门**：论述准确、证据充分、从前到后通读不跳跃 → 进入 Phase 3

---

### Phase 3 — Slide 规格（v1/session_design/）

**你在哪个目录工作**：`v1/session_design/`

**做什么**：
- 把文稿转化为四层 slide 规格
- 这是"给机器读的"——生产管线的直接输入
- 重点是 IMAGE PROMPT（200-500 字的精确视觉描述）

**产出文件**：`v1/session_design/deck-brief-v1.md`

**四层规格**：

| 层 | 名称 | 给谁读 | 内容 |
|----|------|--------|------|
| L1 | Meta | Pipeline 脚本 | VISUAL TYPE、KICKER、CLAIM、IMAGE TYPE |
| L2 | Concept | 人类 reviewer | 必须传达什么、不能出现什么、叙事位置 |
| L3 | Image Prompt | AI image model | 200-500 字视觉描述（构图、元素、色彩、数据 viz） |
| L4 | Speaker Note | 演讲者 | 口语化完整演讲稿 |

**信息流**：
```
manuscript-v1.md ──→ 提供完整论述
                            │
                            ▼
                  每张 slide 拆成四层
                  关键转化：文字论述 → 视觉画面描述（L3 Image Prompt）
                            │
                            ▼
                  deck-brief-v1.md（生产管线的 single source of truth）
```

**⛔ 闸门**：四层完整、VISUAL TYPE 分布合理（~80% normal + ~20% image_direct）→ 进入 Phase 4

---

### Phase 4 — 视觉风格（v1/style/）

**你在哪个目录工作**：`v1/style/`

**做什么**：
- 设计色彩、字体、布局
- 生成 Style Master 锚点图
- 锁定后所有 slide 的画面都以这张图为视觉基准

**产出文件**：
- `v1/style/visual-style-v1.md`（视觉规范）
- `v1/style/style_master.jpg`（锚点图）

**⛔ 闸门**：视觉风格与内容调性匹配 → 进入 Phase 5

---

### Phase 5 — 生产管线（v1/production/）

**你在哪个目录工作**：`v1/production/`

**做什么**：
- 跑脚本：markdown → JSON → 生图 → 标题叠加 → 合成 PPTX
- 大部分是脚本自动执行，你审核中间产物

**信息流**：
```
deck-brief-v1.md + style_master.jpg
              │
              ▼
     Stage 1: 解析 markdown → JSON specs
              │
              ▼
     Stage 2: 生成每页画面（AI image model）
              │ 产出 → page_images/*.png
              ▼
     Stage 3: 标题叠加（Python/Pillow，精确文字渲染）
              │ 产出 → header_locked/*.png
              ▼
     Stage 4: 合成 PPTX
              │ 产出 → ppt/*.pptx
              ▼
     Stage 5: 注入 Speaker Notes
              │ 产出 → ppt/*.pptx（最终版）
```

**⛔ 闸门**：成品可交付

---

## 迭代期：改动了怎么办？

不是每个改动都要从头重跑。走哪条编辑链取决于你改了什么：

| 你改了什么 | 走哪条链 | 重跑范围 | 大约耗时 |
|-----------|---------|---------|---------|
| 改某页 speaker note | 链 C | Phase 5 Stage 5 only | ~30s |
| 改某页标题/claim | 链 A | Phase 3 → 5（单页） | ~5min |
| 改某页 IMAGE PROMPT | 链 B | Phase 3 → 5（单页） | ~5min |
| 加/砍/重构若干 slide | 全链 | Phase 1 → 2 → 3 → 5 | 数小时 |
| 改核心隐喻/公式 | 全链 | 创建 v2/，从头重跑 | 需要新版本快照 |
| 改 color palette | 全链 | Phase 4 → 5 | 需重新生成所有画面 |

**版本快照触发条件**：
- 砍/加/重构 slide → `cp -r v1 v2`
- 改隐喻/公式/视觉方向 → `cp -r v1 v2`
- 改几个字/几张图 → 直接在 v1 改，不新建版本

---

## 速查：我在哪？下一步是什么？

| 如果... | 你在 | 下一步 |
|---------|------|--------|
| `source-synthesis.md` 不存在或未完成 | Phase 0 | agent 读完源材料，提取信号，你审核 |
| `outline-v1.md` 不存在 | Phase 1 | agent 基于合成材料生成隐喻候选、slide map |
| `manuscript-v1.md` 不存在 | Phase 2 | agent 逐 Block 展开论述，你审核 |
| `deck-brief-v1.md` 不存在 | Phase 3 | agent 把文稿转化为四层规格 |
| `style_master.jpg` 不存在 | Phase 4 | agent 设计视觉方案，你选方向 |
| 以上全齐了 | Phase 5 | 跑生产管线 |

---

## 三条铁律（再说一遍）

1. **不跳闸门。** 每个 Phase 结束停下来确认。下游改动的成本是指数级的。
2. **源文件是 single source of truth。** 改内容去 markdown，绝不要直接改 PNG/JSON/PPTX。
3. **用户做选择题，agent 做创造性劳动。** 不问你"隐喻是什么"——生成候选让你选。
