# 视觉样片 v0.10

当前状态：**已生成，等待用户视觉 REVIEW；尚未宣布视觉门禁通过。**

## REVIEW 文件

- `p01-cover.png`：文字主导原生封面。
- `p08-capacity-mismatch.png`：Image 2 连续叙事工程素描 + PowerPoint 精确结果。
- `p20-harness.png`：Image 2 结构剖面工程素描 + PowerPoint 圈住 / 拦住 / 看清。
- `p42-control-plane.png`：PowerPoint 可编辑插件图、loop 与事件流。
- `visual-samples-montage-v0.10.png`：四页 2×2 总览。
- `visual-samples-comparison-v0.9-v0.10.png`：v0.9 3D 实体模型与 v0.10 工程素描逐页对照。
- `AI-Native-SDLC-visual-samples-v0.10.pptx`：四页可编辑样片。

## 本轮改变

- Visual Master Language 改为「工程素描 + 编辑标注」。
- P8 使用平面连续叙事，不再使用微缩输送装置、实体门或排队栏杆。
- P20 使用抽象系统剖面，不再把 harness 画成机器、产品或建筑模型。
- Image 2 主体不生成文字；页面文案和精确标签由 PowerPoint 统一渲染。
- 生成资产使用蓝色键控层生产，提取真实 alpha 后进入固定 `#F7F8F5` 画布。

## 已完成检查

- 四页均由 PowerPoint 反向渲染并逐页检查，与构建预览一致。
- P8/P20 不存在图片矩形、蓝边、白边、残留键控色或页间色差。
- 标题、副标题、眉题、关键结论与精确关系均为可编辑文字或结构。
- `slides_test.py` 未发现溢出。

用户确认视觉门禁后，先建立 P1-P50 页面主体账本，再写生产事实稿并建立完整母版。
