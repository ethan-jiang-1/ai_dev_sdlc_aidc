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

Each version owns its own subdirectory. The `05_output` root contains only this README and version folders. Build metadata such as `.inspect.ndjson`, rendered PNGs, and QA reports stay in the private build workspace rather than alongside delivery files.

## Source Inputs

- Template: `talk-ai-coding-evolution/_asset/CLAWTIME贵客松模板-留白版.pptx`
- Content: `talk-ai-coding-evolution/04_drafts/ppt-text-v5-sep.md`

## Update Workflow

1. Copy the latest version only as a reference; preserve all previous `.pptx` files.
2. Create a matching `v<N>/` directory and increment the version number before export.
3. Add a row to the version table with the practical change summary.
4. Keep build metadata outside `05_output`.
5. Render every slide and run overflow and template-fidelity checks before publishing.
