# GPT Image 2 图文资产实验（v0.8）

本目录记录 P1 / P49 概念场景和少量 A/B 视觉样片的生成过程。目标不是评测服务商本身，而是为这套演讲选择一个稳定、可复现、适合“统一白底的系统蓝图式技术编辑风”的图像生成入口。

## 使用边界

- GPT Image 2 可以逐页承担视觉主体、场景、材质、空间关系、视觉隐喻和整体构图，不只用于封面插图；不需要图像的页面不强行生成。
- GPT Image 2 生成时主动为文字层预留安全区；标题、副标题、kicker、callout 和其他面向听众的关键文字由 PowerPoint 统一渲染。
- 工件、门禁、责任签名、反馈路径、数字、引用和复杂拓扑继续使用可编辑的 PowerPoint / Graphviz 图层。
- P1 与 P49 必须生成两张不同的图：材质和摄影语言一致，系统状态分别是“开始弯成闭环”和“闭环稳定运行”。
- P8 与 P20 只做 A/B；生成图不能在三秒内说清关系，就采用可编辑结构。
- P42 不使用生成图，继续保留可编辑的插件图、事件流和 loop。

## 服务商对比方法

所有服务商先使用同一条低成本测试提示、同一模型名 `gpt-image-2`、同一尺寸和同一质量档位。先测连通性，再比较画面，不用不同提示替服务商补救。

选择顺序：

1. 能稳定返回符合 OpenAI Images API 结构的结果，并能保存为本地 PNG。
2. 能遵守“无文字、白底、留出标题安全区、颜色职责固定”等硬约束。
3. 主轮廓在缩略图下仍然清楚，不把软件价值流误画成工厂、物流、机器人或科幻界面。
4. 细节、材质和光线达到演讲封面需要的完成度。
5. 在质量接近时，优先选择响应更稳定、返工更少的入口；单次速度不是第一目标。

## 测试提示

连通性测试只生成一个无文字、低质量方图，避免在不可用入口上浪费正式生成成本：

> A precise editorial studio still life of a small software delivery system model on a seamless paper-white surface: graphite rails, one coral control gate, one gold artifact tile, and one restrained teal return path. Clear silhouette, soft daylight, no text, no letters, no numbers, no people, no robot, no dashboard, no logo, no watermark.

正式 P1 / P49 的完整提示以 [`../../02-imagegen-prompts-v0.8.md`](../../02-imagegen-prompts-v0.8.md) 为准。

## 实验记录

| 服务入口 | 连通性 | 本地文件 | 约束遵循 | 画面判断 | 结论 |
|---|---|---|---|---|---|
| APIMART | 返回响应 | 失败 | 未进入视觉检查 | 返回项没有 `b64_json`，当前 CLI 无法写出 PNG | 不采用 |
| Duck | 成功，约 40 秒 | 成功 | 部分遵循 | 画面干净，但请求 `1024×1024` 时返回 `1536×1024` | 备用，不作主入口 |
| Duck Fast | 失败 | 失败 | 未进入视觉检查 | 服务端报告当前没有可用的 `gpt-image-2` 通道 | 不采用 |
| MICU | 成功，约 33 秒 | 成功 | 遵循 | 颜色和结构清楚，但青绿回路偏强，标题安全区较弱 | 可用备用 |
| Packy | 成功，约 33 秒 | 成功 | 遵循 | 留白最好，结构最克制，颜色职责清楚 | **选作当前主入口** |

## 目录约定

- `provider-tests/`：同一低成本提示产生的连通性样图。
- `p1-candidates/`：封面概念场景候选。
- `p49-candidates/`：收尾概念场景候选。
- 只保留有比较价值的图片；失败响应、调试输出和依赖环境放在仓库根目录的 `.tmp-org-sdlc-talk-*` 临时目录，不进入资产库。

## 当前结论

当前选择 **Packy** 作为 GPT Image 2 主入口，MICU 作为备用。Packy 已完成一张 `2048×1152`、高质量 P1 概念场景，复杂提示、宽屏尺寸和本地 PNG 输出都稳定：`p1-candidates/packy-p1-v1.png`。

另用相同 P1 图做了一次图中文字能力实验：`p1-candidates/packy-p1-integrated-v1.png`。它准确生成了“AI-Native 软件研发组织 / 让产品意图顺畅抵达生产现场”，说明 GPT Image 2 具备较强的图文一体构成能力。**这张图只作能力证明，不进入生产**：50 页的标题、副标题、kicker 和 callout 需要统一字体、字号、位置与颜色，最终仍由 PowerPoint 渲染。

密钥只从工作区 `.env` 在运行时读取，不写入本目录，也不进入 PPTX 来源说明。
