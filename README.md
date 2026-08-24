# ai_dev_sdlc_aidc

核心主线：**AI Coding 时代，SDLC 如何变化。**

这是一个围绕该主线展开的探索型研究工作站，关注传统 SDLC 在模型能力快速提升后，如何演化为同时面向人和 AI 的新型研发体系。既沉淀长期主题研究，也汇集论文、外部样本、KOL 观点与阶段性综合稿，最终产出可交付的 Keynote。

## 目录结构：按主线分层

资料 → 研究 → 企业视角 → 产出，四个桶按主线顺序排布：

```
ai_dev_sdlc_aidc/
├── 01_sources/                # 证据层：一手信号与资料（输入）
│   ├── field_samples/         #   真实使用样本：fable5 / agentic
│   ├── reference/             #   参考库：kol（人物事件）/ corp（厂商生态）
│   └── papers/                #   学术论文
├── 02_research/               # 分析层：SDLC 变化的分维度研究
│   ├── requirements_engineering/   # 需求侧
│   ├── agentic_engineering/        # 工程实践（兼 deck 脚本）
│   ├── ai_loop_engineering/        # 人机反馈回路
│   ├── agentic_management/         # 管理/编排
│   ├── agentic_teams/              # 多智能体团队
│   ├── ai_native_rnd/              # 研发体系迁移（敏捷/瀑布 → AI-native）
│   ├── thoughtworks_ai_sdlc/       # 方法论
│   └── ai_sdlc_frontier/           # 前沿议题
├── 03_enterprise/             # 企业视角：SDLC 的产业映射
│   ├── business_bpm/               # BPM = 企业侧 SDLC 等价物
│   └── ai_case/                    # 企业 AI 重构案例
└── 04_output/                 # 产出层
    └── deck_ai_sdlc_keynote/       # 主线 Keynote 交付物
```

### 各桶说明

| 桶 | 定位 | 内容 |
| --- | --- | --- |
| `01_sources/` | **证据层** | 一手信号与资料来源，按形态组织：真实使用样本（`field_samples/`）、人物与组织参考库（`reference/kol` + `reference/corp`）、学术论文（`papers/`） |
| `02_research/` | **分析层** | SDLC 变化的分维度研究，每个主题是自包含的 `raw → digested → result` 管道：需求、工程实践、反馈回路、管理、团队、研发体系迁移、方法论、前沿 |
| `03_enterprise/` | **企业视角** | SDLC 在企业/产业的映射：BPM 作为企业信息加工流的 SDLC 等价物，以及企业 AI 重构的一线案例 |
| `04_output/` | **产出层** | 主线交付物：AI 时代 SDLC 变革 Keynote（含完整制作流程与版本管线） |

## 工作区定位

- 这不是单一交付项目，而是一个持续增长的研究工作台。
- 研究对象覆盖方法论、组织协同、需求工程、治理、安全、工作流与外部信号。
- 目标不是只收集资料，而是逐步沉淀出可复用的认知框架、证据库和综合判断。
- 各研究主题遵守统一的信息处理纪律：一手源优先、来源可溯、聚焦当前时刻（详见各参考库 README 的"来源/时间铁律"）。

## Python / uv

本目录已初始化为 `uv` 管理的 Python 项目，并创建了本地虚拟环境 `.venv`。

如果这里需要补充自动化脚本、数据处理脚本或辅助工具，推荐优先使用 Python，以便统一依赖管理、执行方式与后续维护。

- 激活环境：`source .venv/bin/activate`
- 安装依赖：`uv sync`
