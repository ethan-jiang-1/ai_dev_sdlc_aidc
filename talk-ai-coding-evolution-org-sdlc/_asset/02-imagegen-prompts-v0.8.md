# ImageGen 样片 brief（v0.8）

> 目的：逐页判断 GPT Image 2 是否能显著改善视觉主体、场景、材质、空间关系、视觉隐喻或整体构图；不把它局限为封面插图，也不把 50 页做成 AI 插画册。
> 已验证多个 `gpt-image-2` 服务入口；当前以 Packy 为主入口、MICU 为备用。实际生成前先用本文件锁定当页职责、图文分层、构图和禁区。

## 使用边界

- v0.8 的 P1 生成资产只保留为实验记录；v0.9 的 P1 改用原生主体，不再生成。
- v0.9 的 P8、P20 使用混合主体。Image 2 承担丰富图文构成与感知关系，容量分叉、三层 harness 关系和关键标签保留可编辑覆盖层。
- P42 经逐页判断后明确不用 Image 2；复杂拓扑、日志、数值、引用和精确映射以 PowerPoint / Graphviz 为主。其他类似页面仍先判断，不按类型机械排除。
- 生成图必须为 `title`、`subtitle`、`kicker`、`callout`、关键结论和精确标签预留安全区；这些文字由 PowerPoint 正常渲染，不烘焙进位图。
- 允许生成与场景不可分割的局部说明、标签、界面字样或环境文字，并让它们承担局部解释；prompt 必须提供逐字文本，产物必须逐字核对。页面文案和精确关系仍留在可编辑层。
- 主体内嵌文字使用标签、短语或一句简短说明，必须在演示距离下直接读清；连续段落不进入生成资产。
- 生成资产默认以透明或易于干净提取的单色底输出，再无缝嵌入固定纸白画布；满版底图必须校准纸白区域，不能带入可察觉的色差。
- 统一视觉媒介：**精密的实体系统纸模 / 建筑模型式 editorial still life**。哑光纸、石墨金属、极少量青绿/珊瑚红/金黄，不用蓝紫渐变、霓虹、机器人、脑神经、浮空 UI。
- 构图为 16:9。样片可先用 2K；选定后再生成最终高分辨率版本。每张图保留明确的标题安全区。
- 任务 JSON、prompt 与生成资产可以留在项目资产目录；密钥、authorization header 与本地 MICU 配置不得写入仓库。

## 每页生成前记录

- **叙事任务**：这页要让观众看见什么关系或状态？
- **Image 2 角色**：不用 / 视觉底图 / 图文一体的视觉主体。
- **文字与关系分工**：页面文案、主体内嵌文字、数字、引用、工件、门禁、责任签名和连接关系分别由谁渲染？
- **安全区**：明确位置与占比，按最长中文文案验证。
- **淘汰条件**：三秒读不懂、关键术语不准、生成文字不可读、颜色语义漂移、精确关系无法复核，任一成立即重做或改用可编辑结构。
- **画布验收**：检查透明边缘、残留底色、图片矩形和页间纸白色差；任一可察觉即重做资产处理。

## P1：v0.8 历史实验，不进入 v0.9

**用途**：记录 v0.8 对全幅封面生成主体的探索。v0.9 已决定 P1 使用原生主体，本 prompt 不再进入生产。

```text
Use case: stylized-concept
Asset type: 16:9 keynote cover background
Primary request: an editorial studio photograph of a meticulously crafted physical model representing a software delivery value stream; a linear track accelerates through a compact build cell, but the downstream review and release gates remain narrow, and the far end of the track begins to curve back into a controlled loop
Scene/backdrop: seamless pale cool-gray paper studio surface, no horizon line, quiet architectural-model presentation
Subject: a precise paper-and-metal systems model; matte off-white planes and graphite rails; small gold artifact tiles moving along the path; restrained coral vertical gates; a thin teal return path beginning to form a loop
Style/medium: premium technical editorial still life, architectural maquette photography, tactile and credible, not a diagram and not science fiction
Composition/framing: wide 16:9; generous clean negative space in the upper-left 42% for editable title text; system model occupies the right and lower portions; readable silhouette at presentation distance
Lighting/mood: soft directional studio daylight, crisp material edges, restrained shadows, calm and authoritative
Color palette: paper white and graphite dominant; teal only for active feedback; coral only for gates; gold only for artifacts
Materials/textures: matte paper, anodized graphite metal, subtle fiber texture, no glossy glass
Constraints: no text, no labels, no letters, no numbers, no people, no robot, no brain, no code screens, no hologram, no dashboard, no company logo, no watermark
Avoid: cyberpunk, neon, blue-purple AI gradients, floating UI, generic network nodes, excessive visual clutter, decorative bokeh
```

**判定**：如果画面只像“抽象未来交通”，而看不出交付轨道、窄 gate 与开始形成的 loop，就淘汰。

## P49：待最终首尾关系决定

**用途**：与 P1 首尾呼应的全幅收束页。必须重新生成，不复用 P1 位图。

生成时把入选的 P1 作为 **Image 1: style and material reference**，只继承材质、摄影、构图语言，不复制形状。

```text
Use case: stylized-concept
Asset type: 16:9 keynote closing background
Input images: Image 1: style and material reference from the selected P1 cover image
Primary request: show the same kind of physical software-delivery systems model after the transformation is complete; the path is now a clear closed loop with visible controlled gates, traceable gold artifacts, and a restrained teal feedback path returning to the beginning
Scene/backdrop: same pale cool-gray paper studio surface and architectural-maquette presentation as Image 1
Subject: a stable closed-loop paper-and-metal system; no congestion; gates remain visible and authoritative; artifacts can be followed around the loop
Style/medium: match Image 1's premium technical editorial still life, materials, lighting, and visual restraint
Composition/framing: wide 16:9; reserve the central-left area for one large editable Chinese statement; model recedes into the lower-right and frame edges
Lighting/mood: calm resolution, soft directional studio daylight, high material clarity
Color palette: match Image 1 exactly; paper/graphite dominant, restrained teal/coral/gold semantics
Constraints: preserve the visual language of Image 1; no text, no labels, no letters, no numbers, no people, no robot, no brain, no code screens, no hologram, no dashboard, no logo, no watermark
Avoid: celebratory confetti, glowing ring, science-fiction portal, blue-purple gradients, generic infinity symbol
```

**判定**：P1 是“开始弯曲”，P49 是“闭环可运行”；两张图看起来必须属于同一个世界，但不能只是同图换裁切。

## P8 v0.9：宽产出撞上窄控制容量

**用途**：v0.9 混合主体的主要样片。Image 2 负责空间压力、排队感和旁路风险；PowerPoint 负责页面文案与两个精确出口。

```text
Use case: stylized-concept
Asset type: 16:9 keynote concept visual for a capacity mismatch
Primary request: a physical editorial systems model where a very wide stream of small gold software-artifact tiles arrives at two narrow coral control gates; one downstream route visibly accumulates into an orderly queue, while a second unsafe bypass route lets sparse unchecked tiles escape
Scene/backdrop: pale cool-gray paper studio surface, same technical editorial maquette language as the deck cover
Subject: wide upstream production lane, narrow review/security/release control gates, two clearly different consequences after the bottleneck
Style/medium: premium architectural-model still life, tactile matte paper and graphite metal, visually simple enough to understand in three seconds
Composition/framing: 16:9; dominant flow from left to right; clean top area for editable headline; no tiny detail
Lighting/mood: neutral studio light, credible and sober
Color palette: graphite structure; gold artifacts; coral gates; teal only on the safe reviewed path
Constraints: no text, no labels, no people, no literal factory, no robot arms, no dashboard, no logo, no watermark
Avoid: disaster imagery, chaotic explosion, traffic jam stock-photo metaphor, neon, generic funnels
```

**判定**：若“排队”与“欠审”不能在不读标签时被区分，就使用 PowerPoint 可编辑版本。

## P20 v0.9：圈住、拦住、看清的执行单元

**用途**：v0.9 混合主体样片。Image 2 为 harness 建立有空间深度的执行单元剖面，最终三层逻辑用可编辑覆盖层表达。

```text
Use case: stylized-concept
Asset type: 16:9 keynote concept visual for a controlled software execution harness
Primary request: a cutaway physical systems model of one software build execution cell; the cell is enclosed by a clear graphite boundary, the active path crosses a narrow coral gate before tool execution, and a visible teal evidence trail records what happened underneath the cell
Scene/backdrop: pale cool-gray paper studio surface, technical editorial maquette, no surrounding office or data center
Subject: one controlled execution cell with three visually distinct functions: boundary, enforced gate, traceable evidence path
Style/medium: precise architectural cutaway model photographed in studio, tactile matte materials, restrained and credible
Composition/framing: wide 16:9, central-right cutaway model with negative space at upper-left for editable title and three short labels
Lighting/mood: crisp softbox light, high edge clarity, quiet authority
Color palette: off-white and graphite dominant; coral gate; teal evidence path; small gold artifact entering and leaving
Constraints: no text, no labels, no people, no cage metaphor, no prison imagery, no robot, no code screen, no floating UI, no logo, no watermark
Avoid: cyber-security shield icon, glowing force field, futuristic lab, blue-purple neon
```

**判定**：若不能稳定区分 boundary / gate / evidence，改用 P20 的 PowerPoint 剖面母图；准确性优先于质感。

## P42 为什么不用 ImageGen

P42 的任务是精确区分：

- live plugin graph = **现在由什么组成**；
- session event log = **刚才做过什么**；
- loop = **如何取用能力并写回事实**。

这是拓扑和时序关系，不是概念气氛。最终页使用 PowerPoint 可编辑节点与事件带；连接线先画、节点后画，关键标签不烘焙进位图。

## 生成后的视觉 REVIEW

1. 看缩略图：是否有明确主轮廓，而不是细节噪声。
2. 覆盖标题：安全区是否真实可用，中文标题是否无需压缩。
3. 检查语义：青绿/珊瑚红/金黄是否仍遵循 runtime/gate/artifact 的固定职责。
4. 检查题材：是否误读成制造业、物流、云产品架构或通用 AI 海报。
5. 检查资产：主体内嵌文字逐字正确、在演示距离下可读，并与画面真正结合；无品牌、无 watermark、无低清边缘和异常材质。
6. P1/P49 成对检查：材质一致、状态不同、首尾能形成叙事闭环。
7. 图文分层：视觉底图与 PowerPoint 文字叠加后是否像一个整体；标题、副标题、kicker 和 callout 不得被底图抢夺对比度或空间。
