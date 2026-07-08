---
title: Visual Style v1 — Warm Editorial
version: v1
direction: Warm Editorial
status: locked
created: 2026-07-08
---

# Visual Style v1: Warm Editorial

> 高端杂志长文的视觉语言——人文温度、故事张力、克制的权威感。像《纽约时报杂志》或《Monocle》的版面，不是 Bloomberg 终端。

---

## 1. Color Palette

### Surface（背景）

| 用途 | 色值 | 说明 |
|------|------|------|
| Primary Surface | `#F5F0EB` | 暖米白——主背景，像未漂白的书页 |
| Secondary Surface | `#EDE5DA` | 稍深的米色——卡片、引用框、分区 |
| Dark Accent Surface | `#3D2B1F` | 深棕——Section Divider 底、footer |

### Ink（文字）

| 用途 | 色值 | 说明 |
|------|------|------|
| Primary Ink | `#2D1B11` | 深棕黑——正文、CLAIM。不是纯黑，带暖调 |
| Secondary Ink | `#6B5B4F` | 中棕灰——标注、页码、来源 |
| Muted Ink | `#9B8B7F` | 浅棕灰——装饰文字、水印级信息 |

### Accent（强调）

| 用途 | 色值 | 说明 |
|------|------|------|
| Primary Accent | `#D97706` | 琥珀——KICKER 线、关键强调、链接 |
| Secondary Accent | `#B45309` | 深琥珀——hover、重点数据高亮 |
| Warm Glow | `#FDE68A` | 淡金黄——光效、AI 光核、渐变亮部 |

### Status（状态色——少用）

| 用途 | 色值 |
|------|------|
| Positive | `#5B8C5A`（橄榄绿） |
| Warning | `#D97706`（复用琥珀） |
| Negative | `#B91C1C`（深红） |

### 渐变规则

- 只用双色渐变，从暖米到更暖的米：`#F5F0EB` → `#EDE5DA`
- 光效渐变：`#FDE68A` → transparent（AI 光核、发光线）
- 绝不用冷色渐变（蓝→紫等）

---

## 2. Typography

### 中文字体

| 层级 | 字体 | 大小 | 字重 | 用途 |
|------|------|------|------|------|
| CLAIM | Noto Serif CJK SC | 28-36px | Regular 400 | 每页核心论点——衬线体，像杂志标题 |
| BODY | Noto Sans CJK SC | 16-18px | Regular 400 | 正文段落 |
| KICKER | Noto Sans CJK SC | 13-14px | Medium 500 | 全大写标签，4-6 词 |
| CAPTION | Noto Sans CJK SC | 11-12px | Regular 400 | 来源、页码、标注 |

### 英文/数字

| 层级 | 字体 | 用途 |
|------|------|------|
| KICKER | Inter 或 SF Pro | 全大写，letter-spacing: 3-5px |
| CLAIM（英文） | Georgia 或 Cormorant Garamond | 衬线，像高端杂志英文标题 |
| BODY（英文） | Inter 或 SF Pro | 无衬线，与中文 BODY 匹配 |
| 数字/数据 | Tabular figures (Inter) | 等宽数字，表格对齐 |

### 排版规则

- KICKER 后跟一条 1px 琥珀横线（`#D97706`, opacity 0.5, 宽 40-60px），线距 KICKER 12-14px
- CLAIM 与 KICKER 之间留白 ≥ 24px
- BODY 段落 line-height: 1.7-1.8（中文需要更松的行距）
- 英文引语用斜体 Georgia，配琥珀色引号装饰

---

## 3. Layout Grid

```
┌──────────────────────────────────────────────┐
│  margin: 56px                               │
│  ┌────────────────────────────────────────┐  │
│  │  KICKER                                │  │
│  │  ── (1px amber line, 40-60px)         │  │
│  │                                        │  │
│  │  CLAIM                                │  │
│  │  (主标题区，占画面 30-40%)             │  │
│  │                                        │  │
│  │  BODY / VISUAL                        │  │
│  │  (内容区，占画面 50-60%)              │  │
│  │                                        │  │
│  │                              PAGE N    │  │
│  └────────────────────────────────────────┘  │
│  margin: 56px                               │
└──────────────────────────────────────────────┘
```

- 标题区在左上，不在居中——像杂志版面，不对称但平衡
- 正文/视觉区在标题下方或右侧
- 页码在右下角，muted ink（`#9B8B7F`），小字

---

## 4. Component Patterns

### 引用框（Pull Quote）

```
┌─────────────────────────────────────┐
│  "                                 │
│  Build is cheap.                   │
│  Argument is expensive.            │
│                    "               │
│  —— Simon Willison                │
│  Datasette 创始人                  │
└─────────────────────────────────────┘
```
- 左边 1px 琥珀竖线
- 引文用 Georgia 斜体，Primary Ink
- 引用人用 Secondary Ink，小字
- 背景：Secondary Surface（`#EDE5DA`），微圆角 4px

### 数据对比表

```
  │  SDLC              │  BPM               │
──┼────────────────────┼────────────────────┼──
  │  需求 → 代码       │  信息 → 决策       │
  │  瀑布→敏捷→AI-SDLC │  泰勒→BPR→Agentic  │
──┴────────────────────┴────────────────────┴──
```
- 表头行底部 1px 琥珀线
- 数据行底部 1px Secondary Surface 线
- 文字用 Secondary Ink，highlight 用 Primary Ink
- 无斑马条纹，保持干净

### 时间线

```
1970 ─────── 1980 ─────── 2001 ─────── 2026
瀑布           V模型        敏捷          ?
  │              │           │           │
  └──────────────┴───────────┴───────────┘
            同一个前提：人必须先想清楚
            2026: AI 挖掉了这个前提
```
- 时间轴 1px Secondary Ink 线
- 节点用 6px 圆点，Primary Accent 填充
- 标注用 Caption 大小

### 对比框架（Split）

- 左右两栏，中间 1px 竖线（Secondary Surface）
- 每栏独立标题（CLAIM 级别大小）
- 栏内正文用 BODY 大小

### AI 光核（装饰性视觉元素）

- 一个发光的几何点/球——暖金黄 `#FDE68A`
- 外层有扩散光晕，用 `radial-gradient`
- 不是霓虹灯——是烛光/日出那种暖光
- 用于表示 AI Agent、智能节点、信息流中的 AI 工位

---

## 5. 装饰元素规则

- **纹理**：全局覆盖一层极淡的噪点/纸纹（opacity 0.02-0.03），像纸张触感
- **线条**：只用 1px 细线。琥珀色（Primary Accent）或 Secondary Surface 色。不出现 2px+ 粗线
- **几何装饰**：极简——偶尔用一个菱形 `◆` 或小圆点做分隔。不出现复杂图形
- **图标**：线性图标（1.5px stroke），Secondary Ink 色。不用实心/彩色图标

## 6. Style Master 锚点图

### style_master.jpg 应该包含

1. **Primary Surface 全幅背景**（暖米白 + 纸纹纹理）
2. **KICKER 示例**："THE PREMISE IS GONE" — 全大写，letter-spacing 4px，下方 1px 琥珀线
3. **CLAIM 示例**："瀑布、V模型、敏捷都是同一个前提下的参数变体" — Noto Serif CJK SC, 32px, Primary Ink
4. **Pull Quote 示例**：Simon Willison 的引用，左侧琥珀竖线，Georgia 斜体
5. **配色色块**：Primary Surface / Secondary Surface / Primary Ink / Secondary Ink / Primary Accent 五个色块排成一行
6. **AI 光核示例**：一个暖金黄发光圆点，带 radial-gradient 光晕
7. **数据对比表示例**：2 列 × 3 行，琥珀表头线

### 生成方式

将此文件中的 Color Palette + Typography + 上述 7 个元素描述传给 AI image model，生成一张 1920×1080 的锚点图。这张图之后作为每次 slide 生图的 visual reference 传入。

---

## 7. Slide 类型适配

| VISUAL TYPE | Warm Editorial 适配 |
|-------------|-------------------|
| Title Opener | 全幅暖米背景，大号衬线 CLAIM，琥珀线，纸纹理 |
| Concept Split | 左右分栏，左边 CLAIM+正文，右边概念图（光核/链条） |
| Evidence | 引用框 + 数据表为主，视觉元素克制 |
| Framework | 居中架构图，暖色调，线框风格 |
| Section Divider | Dark Accent Surface（`#3D2B1F`）满屏，琥珀字 |
| Closer | 黑底或 Dark Accent Surface，一行白/金文字，极简 |

---

## 版本记录

| Date | Change | Why |
|------|--------|-----|
| 2026-07-08 | 创建 v1, 锁定 Warm Editorial | 用户选定 C 方向——高端杂志感，人文叙事调性 |
