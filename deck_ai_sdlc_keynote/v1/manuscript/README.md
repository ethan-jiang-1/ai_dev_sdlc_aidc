---
title: Phase 2 — 完整文稿
stage: phase_2
position: manuscript
type: guide
summary: 将每张 slide 的一句话 claim 展开为完整论述，含证据引用、过渡逻辑、speaker note 草稿。
depends_on:
  - v1/outline/outline-v1.md
feeds_into:
  - v1/session_design/deck-brief-v1.md
agent_action: guide
---

# Phase 2: 完整文稿

> 本阶段目标：把骨架填上血肉。每张 slide 不只是"要说什么"，而是"完整地说出来"。

## 输入

`v1/outline/outline-v1.md`（Phase 1 产出）

## 产出

`manuscript-v1.md`，为每张 slide 展开：

### 每张 slide 的完整内容

```markdown
## Slide N: [CLAIM]

### 核心论述（150-300 字）
完整的论证段落——不只是 bullet points，而是可以读出来的连贯文字。

### 证据/引用
- 来源人物/事件 + 具体引文 + 源文件路径
- 标注证据强度（⭐⭐⭐ 多人独立验证 / ⭐⭐ 单人公开发言 / ⭐ 断言级）

### 视觉概念（初步）
- 这张 slide 的视觉隐喻/场景（不是 final IMAGE PROMPT，是方向描述）
- 例："一个仪表盘显示堵车（交通拥堵），但 GPS 在建议 Exit 47（决策）。Split scene。"

### 过渡句
- 从上一张 slide 到这一张的桥梁
- 从这一张到下一张的桥梁

### Speaker Note 草稿
- 演讲时怎么说（口语化的完整段落）
- 中文为主，关键术语保留英文
```

## 工作方式

- Agent 逐张 slide 展开论述
- 每完成一个 Block（3-7 张），停下来让用户审核
- 用户确认该 Block 的论述方向后，继续下一个 Block

## ⛔ 闸门

Phase 2 完成标准：
- [ ] 每张 slide 有完整论述段落（不是 bullet list）
- [ ] 所有关键主张有证据引用 + 来源路径
- [ ] 证据强度已标注
- [ ] 过渡逻辑连贯（可以从前到后通读一遍而不跳跃）
- [ ] 用户确认：论述准确、证据充分、逻辑连贯
