# v0.8 四张关键视觉样片

> 状态：**等待用户视觉 REVIEW**。不代表视觉门禁已经通过，不得据此直接铺 50 页。

本轮样片验证四种最难的视觉任务：

- `p01-cover.png`：白底 Hero 与“线性管道开始闭环”的世界观。
- `p08-capacity-mismatch.png`：宽产出撞上窄控制容量，分成排队 / 欠审两个后果。
- `p20-harness.png`：白底圈住 / 拦住 / 看清的 harness 核心母图。
- `p42-control-plane.png`：live plugin graph 与 append-only event stream 的精密控制面。
- `AI-Native-SDLC-visual-samples-v0.8.pptx`：四页可编辑样片 deck。

## 当前实现判断

- P1：先以 PowerPoint 可编辑系统轨道验证构图；ImageGen 实体纸模候选尚未进入项目资产。
- P8：可编辑结构优先，三秒关系为“宽产出 → 窄门 → 排队 / 欠审”。
- P20：可编辑结构优先，gate、执行边界与 evidence path 可独立修改。
- P42：保持为精确可编辑拓扑和时序，不使用生成式位图。

## 技术 QA

- 由 PPTX 反向渲染四页检查。
- `slides_test.py` 通过：未检测到溢出。
- 每页 speaker notes 含 `[Sources]`，标明为本 talk 自制 illustrative visual。

## REVIEW 后分支

- 若视觉语言通过：回写视觉门禁结果，进入生产事实稿，再建立八个布局族的母版。
- 若整体方向不通过：只改这四张样片与视觉 token，不提前生产 P2-P50。
- 若局部页不通过：保留通过页作为母图，只迭代对应视觉语法。
