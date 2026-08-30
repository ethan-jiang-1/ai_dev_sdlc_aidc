# GPT Image 2 内生图文与字体同源实验（v0.11）

本轮解决 v0.10 的两项问题：PowerPoint 标签与生成主体使用两套坐标系，以及 Image 2 内嵌文字使用手写体、与 PPT 字体不一致。

- `p8-capacity-integrated-raw-v1.png` / `p20-harness-integrated-raw-v1.png`：图文对齐成立、文字逐字正确，但手写批注体未通过字体同源门槛。
- `p8-capacity-integrated-raw-v2.png` / `p20-harness-integrated-raw-v2.png`：入选；使用实际 PowerPoint 页面作为第二张字体参考图，内嵌文字改为统一现代无衬线。
- `*-integrated-alpha-v2.png`：进入 v0.11 PPTX 的透明资产。

P8 最终标签：`控制容量`、`排队`、`审查不足`。

P20 最终标签：`圈住`、`沙箱与权限`、`拦住`、`hooks 与门禁`、`看清`、`观测与来源记录`。

所有字符串已逐字核对。密钥只在运行时从工作区 `.env` 读取，不写入本目录。
