---
title: Phase 4 — 视觉风格
stage: phase_4
position: visual_style
type: guide
summary: 设计视觉系统，生成 Style Master 锚点图，锁定后所有 slide 以此为视觉基准。
depends_on:
  - v1/session_design/deck-brief-v1.md
feeds_into:
  - v1/production/
agent_action: guide
---

# Phase 4: 视觉风格

> 本阶段目标：为 Keynote 设计一套视觉系统，产出 Style Master 锚点图。锁定后，所有 slides 的生成都以这张图为视觉基准。

## 输入

`v1/session_design/deck-brief-v1.md`（Phase 3 产出——理解内容调性）

## 产出

### `visual-style-v1.md`
视觉规范文档，包含：
- Color Palette（主色、强调色、背景色、文字色）
- Typography（标题字体、正文字体、KICKER 字体）
- Layout Grid（标题区、body 区、margin）
- Component Patterns（卡片、图表、时间线、引用框）
- 装饰元素（线条、图标、数据 vis 风格）

### `style_master.jpg`
一张参考图——将上述规范展示为一张"母版"图片。这张图的作用是 **visual anchor**：生成每一页 slide 时传给 AI 模型，让模型"看到"并"匹配"这套视觉系统。

## 方向建议

战略 Keynote 的主题是"AI 时代 SDLC 变革"，建议视觉方向：
- **Dark Executive**：深色底，科技感蓝/青强调——适合技术战略
- **Clean Clinical**：白底，数据驱动——适合证据密集型论述
- **Warm Editorial**：暖色底，人文感——适合"变革叙事"

## 参考

- `_ppt_framework_v1/01_visual_style_master/`
- `_ppt_framework_v1/01_visual_style_master/presets/`（视觉预设）

## ⛔ 闸门

Phase 4 完成标准：
- [ ] Color Palette 已锁定
- [ ] Typography 已锁定
- [ ] Style Master 图片已生成
- [ ] 用户确认：视觉风格符合内容调性
