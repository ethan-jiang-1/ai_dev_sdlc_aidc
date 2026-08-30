# GPT Image 2 工程素描实验（v0.10）

本轮为 P8 与 P20 重做生成主体，验证「工程素描 + 编辑标注」Visual Master Language。P1 与 P42 继续使用 PowerPoint 原生主体。

- 主入口：Packy；模型：`gpt-image-2`；尺寸：2048×1152；质量：high。
- 生产背景：纯蓝键控层，生成后提取真实透明通道；PPTX 只显示 `#F7F8F5` 画布。
- 文字分工：生成主体不含文字；标题、说明、精确结果和三层关系由 PowerPoint 渲染。
- 颜色语义：石墨为主体，珊瑚红只表示门禁/风险，青绿只表示运行/反馈，金黄只表示工件/证据。

## 迭代记录

- `p8-capacity-raw-v1.png`：已转为素描，但右侧实体栏杆仍有布景感，不入选。
- `p20-harness-raw-v1.png`：仍像机器产品剖面，只改变了绘画媒介，没有改变视觉观念，不入选。
- `p8-capacity-raw-v2.png` / `p8-capacity-alpha-v2.png`：入选；平面连续叙事素描，宽产出经窄门形成排队与欠审。
- `p20-harness-raw-v2.png` / `p20-harness-alpha-v2.png`：入选；平面系统剖面，边界、门禁和事实轨迹属于同一张工程编辑图。

提示词以 `p8-prompt-v2.txt` 和 `p20-prompt-v2.txt` 为当前入选记录；v1 提示词及资产保留用于说明为什么需要第二轮收紧。密钥只在运行时从工作区 `.env` 读取，不写入本目录。
