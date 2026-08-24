# Figma Make 2025 — Official multimodal prompt-to-code signal for requirements inputs

- source_url: `https://help.figma.com/hc/en-us/articles/31304412302231-Explore-Figma-Make` + `https://help.figma.com/hc/en-us/articles/31304529835671-Attach-designs-and-images-to-a-prompt`
- source_type: `official product documentation`
- accessed_at: `2026-04-18`
- related_topic: `04 future-trends (primary), 06 agent-format, 02 user-story`
- trust_level: `official`
- tier: `B`
- why_it_matters: Topic 04 的一个剩余缺口是“多模态 requirements 是否已从揣测变成真实工具链信号”。Figma Make 官方文档直接说明：prompt-to-code workflow 不只吃文本，还能附加 design、image、video、audio、text file、PDF，并把 design layers / content 转成 functional code。这足以支撑“需求输入正向多模态扩展”的早期产品化信号。
- captured_excerpt: `yes`
- claims_supported: `Figma Make is an AI prompt-to-code tool for turning ideas and existing Figma Designs into functional prototypes/web apps; prompts can attach designs, images, video, audio, text files, and PDFs; attached designs are interpreted and translated into functional code; attached files act as additional context/reference material.`
- date_scope: `Figma Make open beta announced during Config 2025; help docs current as of 2026-04-18`
- related_entities: `Figma Make; multimodal input; prompt-to-code; design attachment; image attachment; PDF attachment; audio; video`

## 关键事实

1. Figma 官方文档把 Figma Make 定义为 AI-powered `prompt-to-code` tool，可把 ideas 和 existing Figma Designs 转成 functional prototypes / web apps / interactive UI。
2. 官方 `Attach files to a prompt` 文档明确说明，prompt 可以附加：
   - designs
   - images
   - video
   - audio
   - text files
   - PDFs
3. 同文说明：当附加 design 时，AI model can interpret the design and translate the layers and content into functional code。
4. 附件被定义为 `additional context, data, or reference material`，说明需求/规约输入不再局限于纯文本指令。
5. 官方还举例说明可用 `.json` sample API response 作为附件让模型围绕数据生成界面，这进一步说明“结构化 artifact + 多模态 reference”正在进入产品工作流。

## 核心内容摘录

### 多模态输入已经是产品能力，不只是研究设想

- Figma Make 官方文明确把 designs、images、video、audio、text files、PDFs 都列为 prompt attachments。
- 这意味着需求输入可以来自设计稿、参考图、说明文档、甚至录音/视频等多种媒介。

### 设计稿到功能原型

- 官方文写明 AI model interprets the design and translates layers/content into functional code。
- 这不是“把图片贴给模型看看”而已，而是把 design artifact 作为代码生成的输入材料。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 04 `future-trends` | 多模态 requirements / spec inputs 已出现官方产品化信号 |
| Topic 06 `agent-format` | feature-level spec workflow 不再只能靠 markdown，也可能混合 design/image/document attachments |
| Topic 02 `user-story` | 上游意图表达未来可能由 text story 扩展为 story + design/context bundle |

## 可直接引用的术语 / 概念

- `prompt-to-code`
- `functional prototypes`
- `attach designs, images, video, audio, text files, and PDFs`
- `additional context, data, or reference material`
- `translate the layers and content into functional code`

## 风险与局限

1. 这是一份官方产品文档，能证明产品能力和工作流信号，不能单独证明行业大规模采用。
2. 它更直接支撑“multimodal input has emerged”而不是“multimodal requirements are already the dominant norm”。
3. 该信号更偏 UI / product prototyping；是否能迁移到高合规 requirements baseline，仍需额外证据。

## 交叉引用

- Topic 04 evidence summary：[`../_artifacts/04-future-trends-evidence-summary.md`](../_artifacts/04-future-trends-evidence-summary.md)
- Topic 06 evidence summary：[`../_artifacts/06-agent-format-evidence-summary.md`](../_artifacts/06-agent-format-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
