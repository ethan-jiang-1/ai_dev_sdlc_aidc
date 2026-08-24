# Vercel v0 2025–2026 — Multimodal inputs and PRD-to-spec workflow

- source_url: `https://v0.app/docs` + `https://v0.app/docs/screenshots` + `https://v0.app/docs/images-and-videos` + `https://v0.app/docs/prd-design`
- source_type: `official product documentation`
- accessed_at: `2026-04-18`
- related_topic: `04 future-trends (primary), 06 agent-format`
- trust_level: `official`
- tier: `B`
- why_it_matters: Topic 04 的 multimodal 轴此前主要由 Figma Make 提供单产品 signal，仍缺第二个官方 workflow 级证据。Vercel v0 官方文档直接给出更广的 multimodal product-building workflow：可用 screenshots/files 生成界面代码，可上传 images/videos 作为 visual context 或 media assets，并有独立 `PRD design` 指南把高层需求转成 technical specs、API specs、schema design。这足以把 Topic 04 从“单一 Figma signal”推进到“broader multimodal workflow signal supported”。
- captured_excerpt: `yes`
- claims_supported: `A mainstream app-building AI product now supports screenshots/files, images, and videos as workflow inputs; multimodal inputs are used not only for visual cloning but also for richer app generation; product requirements can be iteratively turned into technical specs, API specs, and schemas in the same workflow.`
- date_scope: `docs observed 2026-04-18`
- related_entities: `Vercel; v0; screenshots; files; images; videos; PRD; API specs; schemas`

## 关键事实

1. v0 首页把产品描述成 `AI agent`，并明确写出 `Multi-modal` 是其差异化能力之一。
2. `Screenshots and Files` 文档明确说：
   - attachment feature allows users to upload or drag and drop files into the chat
   - v0 analyzes these files and generates code to replicate the design interface shown
3. 同文说明 screenshot 输入不仅复制视觉界面，还会 `infer likely functionality based on visible UI elements`。
4. `Images and videos` 文档明确支持：
   - image uploads
   - video uploads
   - copy/paste images from design tools or browsers
5. `PRD design` 文档明确说：
   - PRD bridges the gap between product ideas and technical implementation
   - v0 can turn high-level product ideas into detailed technical specs
   - inputs can include `text, images, or code snippets`
   - outputs can include API specifications and database schema design

## 核心内容摘录

### 这不是单一 design-tool signal

- 与 Figma Make 不同，v0 不是设计工具内原生功能，而是独立的 app-building AI workflow。
- 它因此补强了 Topic 04 的核心判断：multimodal requirement inputs 正在跨工具出现，而不只是某个设计平台的特性。

### multimodal 输入已经进入生成式产品工作流

- 截图/文件输入可用于 turning mockups or wireframes into high-fidelity designs。
- images/videos 页面进一步表明，视觉媒体不仅用于 design cloning，也可用于 richer application generation。

### PRD 与 multimodal 输入被放到同一工作流中

- `PRD design` 页面把 product requirements、technical planning、API specs、schema design 串成一个连续 workflow。
- 文档还明确说 project context 可以包括 `text, images, or code snippets`。
- 这使 Topic 04 的“multimodal requirements”从纯视觉信号推进到“multimodal + PRD/spec workflow”。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 04 `future-trends` | 把 multimodal 轴从 Figma 单点 signal 升级到第二个官方 workflow signal；同时连接 PRD-to-spec 产品路径 |
| Topic 06 `agent-format` | 说明 feature-level spec workflow 可与 screenshots/files/images/videos 共同构成 agent-era product artifact layer |

## 可直接引用的术语 / 概念

- `Multi-modal`
- `Screenshots and Files`
- `generates code to replicate the design interface shown`
- `infer likely functionality`
- `images and videos`
- `PRD`
- `technical specs`
- `API specifications`
- `database schema design`

## 风险与局限

1. 这仍是工具官方文档，不是 adoption census。
2. 它更强地支持 multimodal workflow existence，而不是效果优越性。
3. 它与 Figma Make 一起可以支持 broader multimodal workflow signal，但还不足以证明行业主流已完全转向 multimodal requirements。

## 交叉引用

- Topic 04 evidence summary：[`../_artifacts/04-future-trends-evidence-summary.md`](../_artifacts/04-future-trends-evidence-summary.md)
- Figma multimodal signal：[`04-future-trends-figma-make-multimodal-signal.md`](04-future-trends-figma-make-multimodal-signal.md)
- Topic 06 Spec workflow relation：[`../_artifacts/06-agent-format-evidence-summary.md`](../_artifacts/06-agent-format-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
