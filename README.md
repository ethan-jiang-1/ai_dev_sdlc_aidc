# ai_dev_sdlc_aidc

这是一个围绕 AI 时代软件工程重构的探索型工作区，关注传统 SDLC 在模型能力快速提升后如何演化为同时面向人和 AI 的新型研发体系。

这里既包含长期主题研究，也包含论文资料、外部样本、KOL 观点、阶段性综合稿与后续可扩展的辅助脚本。

## 根目录导航

当前根目录按“主题线 + 资料线”展开，尽量做到一眼能看出每个目录在研究什么：

| 目录 | 说明 |
| --- | --- |
| `agentic_engineering/` | Agentic Engineering、AI 编程范式迁移、上下文工程与工程实践演化 |
| `agentic_management/` | 智能体编排、协作、管理与操作模型 |
| `agentic_teams/` | 多智能体协同、Agent Team 模式与团队级工作流 |
| `ai_native_rnd/` | AI-native 研发方式、敏捷与瀑布迁移相关研究 |
| `requirements_engineering/` | AI 时代需求工程、User Story、EARS、Spec Workflow 与治理 |
| `aidlc/` | AI-DLC / AIDLC 方法论、生态、AWS 线索与 KOL 关联研究 |
| `ai_sdlc_frontier/` | AI 时代软件工程前沿话题与 follow-up research |
| `ai_loop_engineering/` | Loop Engineering、人机反馈回路与开发闭环 |
| `thoughtworks_ai_sdlc/` | 基于 ThoughtWorks 线索展开的 AI-native SDLC 专题研究 |
| `ai_sdlc_papers/` | AI SDLC / Agentic Software 相关论文资料库 |
| `agentic_field_signals/` | 泛 agentic 高价值外部样本、方法与信号汇编 |
| `fable5_field_signals/` | 围绕 Claude Fable 5 的一线使用样本与工作流信号 |

## 工作区定位

- 这不是单一交付项目，而是一个持续增长的研究工作台。
- 研究对象覆盖方法论、组织协同、需求工程、治理、安全、工作流与外部信号。
- 目标不是只收集资料，而是逐步沉淀出可复用的认知框架、证据库和综合判断。

## Python / uv

本目录已初始化为 `uv` 管理的 Python 项目，并创建了本地虚拟环境 `.venv`。

如果这里需要补充自动化脚本、数据处理脚本或辅助工具，推荐优先使用 Python，以便统一依赖管理、执行方式与后续维护。

- 激活环境：`source .venv/bin/activate`
- 安装依赖：`uv sync`
