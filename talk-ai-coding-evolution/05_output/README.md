# PPTX Versioning

## Naming Rule

Every published deck uses this filename pattern:

`OPC航海指南-harness-v<N>.pptx`

`<N>` is a positive integer and increments for every meaningful content or layout revision. Do not overwrite an existing versioned deck. Generate the next version alongside prior versions so changes remain traceable.

## Current Version

| Version | File | Summary |
| --- | --- | --- |
| v1 | `v1/OPC航海指南-harness-v1.pptx` | Initial deliverable. Keeps the 贵客松 template for cover and closing; pages 2-22 use a compact brand header, a 130px image footer, and content-specific presentation layouts. |
| v2 | `v2/OPC航海指南-harness-v2.pptx` | 留白版模板：封面和结束页保留完整城市视觉；P2-P22 只保留顶部居中缩小 LOGO，在白色内容区增加候选上屏素材、时间轴、流程、对比与结构图。 |
| v3 | `v3/OPC航海指南-harness-v3.pptx` | V2 的后续内容与版式迭代版本。 |
| v4 | `v4/OPC航海指南-harness-v4.pptx` | 手工调整后的生产基线；后续版本继承其母版、视觉框架和未改页面。 |
| v5 | `v5/OPC航海指南-harness-v5.pptx` | 完全继承 V4；重写 P17-P21 为 DSH 爆发、OPC 收益、定位、控制义务与最终控制权，并微调 P22 收束。 |
| v6 | `v6/OPC航海指南-harness-v6.pptx` | 继承 V5；经文字与视觉双重复核，重写 P12/P13 与 P17-P23，突出 DSH 的 GitHub 注意力爆发、OPC 收益、可组合 runtime 定位与四项最终决定权，并以“部件可借，边界自己定”收束。 |
| v7 | `v7/OPC航海指南-harness-v7.pptx` | 继承 V6；完整通读 P1-P23 后强化前后因果，重写问题地图、Harness 能力/交付分工、OPC 边界判断与 P20-P22 的责任→final say→封面回答链条。 |

Each version owns its own subdirectory. The `05_output` root contains only this README and version folders. Build metadata such as `.inspect.ndjson`, rendered PNGs, and QA reports stay in the private build workspace rather than alongside delivery files.

## Source Inputs

- Visual baseline: `talk-ai-coding-evolution/05_output/v6/OPC航海指南-harness-v6.pptx`
- Content: `talk-ai-coding-evolution/04_drafts/ppt-text-v7.md` and `ppt-text-v7-sep.md`

## Update Workflow

1. Copy the latest version only as a reference; preserve all previous `.pptx` files.
2. Create a matching `v<N>/` directory and increment the version number before export.
3. Add a row to the version table with the practical change summary.
4. Keep build metadata outside `05_output`.
5. Render and inspect every slide twice: narrative/copy first, visual hierarchy and layout second.
6. Run overflow, empty-placeholder, source-note, and template-fidelity checks before publishing.
7. If review changes the deck, reverse-sync the accepted copy into `04_drafts`, `03_outline`, `02_evidence`, and `01_storyline`.
