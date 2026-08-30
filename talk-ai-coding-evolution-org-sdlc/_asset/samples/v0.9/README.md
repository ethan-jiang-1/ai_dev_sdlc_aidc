# 视觉样片 v0.9

当前状态：**已完成 REVIEW，未通过视觉门禁。** P8/P20 的 3D 实体模型、微缩布景和机器剖面语言与白底技术编辑系统不一致；本版本只保留为 v0.10 的历史对照。

## REVIEW 文件

- `p01-cover.png`：文字主导原生封面。
- `p08-capacity-mismatch.png`：Image 2 容量失配主体 + PowerPoint 精确后果。
- `p20-harness.png`：Image 2 执行单元剖面 + PowerPoint 三层关系。
- `p42-control-plane.png`：PowerPoint 可编辑插件图、loop 与事件流。
- `visual-samples-montage-v0.9.png`：四页 2×2 总览。
- `visual-samples-comparison-v0.8-v0.9.png`：同页新旧对照。
- `AI-Native-SDLC-visual-samples-v0.9.pptx`：四页可编辑样片。

## 已完成检查

- 四页统一使用 `#F7F8F5` 画布，没有黑底或深浅交替。
- P8、P20 的生成主体已提取透明通道，没有生成图自带的近似白底矩形。
- P8 的“AGENT 产出 / 控制容量”和 P20 的“执行边界 / 工具执行 / 事实轨迹”已经逐字核对。
- 标题、副标题、眉题、关键结论与精确关系均由 PowerPoint 文字层或原生结构承载。
- PowerPoint 反向渲染与构建预览一致；`slides_test.py` 未发现溢出。

## REVIEW 后续

后续由 v0.10「工程素描 + 编辑标注」样片接续 REVIEW。v0.9 不进入完整 50 页生产。
