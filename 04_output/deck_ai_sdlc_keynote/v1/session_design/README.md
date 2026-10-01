---
title: Phase 3 — Slide 规格
stage: phase_3
position: slide_specs
type: guide
summary: 将文稿转化为四层 slide 规格——这是生产管线的直接输入。
depends_on:
  - v1/manuscript/manuscript.md
feeds_into:
  - v1/style/visual-style.md
agent_action: guide
---

# Phase 3: Slide 规格（四层）

> 本阶段目标：把叙事内容转化为机器可执行的 slide 规格。这是内容和生产的桥梁。

## 输入

`v1/manuscript/manuscript.md`（Phase 2 产出）

## 产出

`deck-brief.md`——完整的四层 slide 规格文件。

## 四层规格模板

每张 slide 包含四个独立层：

### Layer 1: Meta（给 pipeline 脚本读）

```markdown
- VISUAL TYPE: [Title Opener / Concept Split / Direction / Evidence / 
               Framework / Section Divider / Closer / Image Direct]
- KICKER: [3-6 词全大写标签，如 THE PROBLEM]
- TITLE / CLAIM: [完整的、可争论的句子]
- IMAGE TYPE: [normal / image_direct]
```

### Layer 2: Concept（给人类 reviewer 读）

```markdown
- MUST communicate: [这张 slide 必须传达什么]
- MUST NOT: [什么不能出现在画面上]
- Bridge: [这张 slide 在叙事流中的位置——前一张是什么，后一张是什么]
```

### Layer 3: Image Prompt（给 AI image model 读）

```markdown
200-500 字的精确视觉描述。包括：
- 构图（Split / Full bleed / Grid / ...）
- 主体元素和空间关系
- 颜色氛围（引用 style master）
- 数据可视化形式（如有）
- 文字在画面中的角色（如有）——注意：标题不走 AI，走 Header-Lock
```

### Layer 4: Speaker Note（给演讲者读）

```markdown
口语化的完整演讲内容。包括：
- 核心叙事
- 术语解释
- Takeaway
- 语言：中文为主，关键术语保留英文
```

## 参考

- `_ppt_framework_v1/02_content_design/03-specify-slides-multi-layer.md`
- `_ppt_framework_v1/02_content_design/template-deck-brief.md`
- `_ppt_framework_v1/03_image_prompts/`（写 IMAGE PROMPT 时参考）

## ⛔ 闸门

Phase 3 完成标准：
- [ ] 每张 slide 四层规格完整
- [ ] VISUAL TYPE 分布合理（~80% normal, ~20% image_direct）
- [ ] 每张 IMAGE PROMPT 有明确的视觉焦点和构图描述
- [ ] Speaker Note 是"可以读出来"的口语，不是书面语
- [ ] 用户确认：deck brief 锁定，可以进入视觉设计
