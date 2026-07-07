# 参考文献按 Topic 索引

编号与 [references-full.md](references-full.md) 一致。同一编号可出现在多个 Topic（原文交叉引用）。

## Topic 1 — RE 背景与范式地图

**Primary:** 1, 2, 14, 24, 26, 44

| 编号 | 侧重 |
|------|------|
| 1 | User story 总览（地图中的敏捷一格） |
| 2 | 敏捷演进语境 |
| 14 | User stories 与 requirements 的区分 |
| 24 | User stories 相对 requirements / use cases 的优势（地图对比） |
| 26 | INCOSE 视角下从脆弱到敏捷 |
| 44 | Requirements vs User Stories 对比 |

## Topic 2 — User Story 教程

**Primary:** 1, 3, 4, 5, 15, 19, 35, 52

| 编号 | 侧重 |
|------|------|
| 1 | 定义与背景 |
| 3 | Martin Fowler User Story |
| 4 | 反模式与破坏故事 |
| 5 | Atlassian 模板与示例 |
| 15 | AI 生成 user stories 讨论 |
| 19 | Requirements vs stories vs acceptance criteria |
| 35 | LLM 生成与评估 user stories |
| 52 | LLM 生成类 user stories |

## Topic 3 — EARS 教程

**Primary:** 6, 7, 8, 10, 11, 12, 13, 18, 20, 21, 22, 23, 25, 27, 46, 47

| 编号 | 侧重 |
|------|------|
| 6 | EARS 官方指南 |
| 7 | EARS 论文 PDF |
| 8 | EARS Slideshare |
| 10 | EARS 教程 PDF (IARIA) |
| 11 | EARS 实践文章 |
| 12 | 何时不使用 EARS |
| 13 | Visure 采纳 EARS |
| 18 | Jama 采纳 EARS |
| 20–23 | ISO 26262 / 功能安全（§4.2 语境） |
| 25 | Reddit 社区讨论 |
| 27 | Inflectra + EARS 分析 |
| 46–47 | INCOSE 需求意义与 GTWR 摘要 |

## Topic 4 — 趋势与证据（AI、实证、质量自动化）

**Primary:** 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 48, 49, 50, 51, 45, 15, 52

| 编号 | 侧重 |
|------|------|
| 28 | AI 对开发者生产力（广义语境） |
| 29 | User prompts 叙事 |
| 30 | Prompt engineering 框架 |
| 31–32 | 结构化提示与代码生成 |
| 33–36 | LLM 与需求/代码实证 |
| 37 | sMBSAP vs Scrum 度量 |
| 38 | Roost / USDD 叙事 |
| 45 | Copilot4DevOps 对比 stories vs requirements |
| 48–51 | INCOSE 自动化、AI 与 RE 工具 |
| 50 | 需求管理优化建模 |
| 15, 52 | 与 Topic 2 重叠：AI + user stories |

## Topic 5 — 互补、BDD、选型矩阵

**Primary:** 9, 16, 17, 37, 38, 39, 40, 41, 42, 43, 19, 44, 14, 20, 21, 22, 23, 6, 27

| 编号 | 侧重 |
|------|------|
| 9 | EARS → BDD 桥梁 |
| 16–17 | Given-When-Then / Gherkin 示例 |
| 37 | 结构化规约 vs 纯 Scrum（对照 pipeline） |
| 38–43 | TDD/BDD/ATDD 语境 |
| 41 | Cucumber Gherkin 规则 |
| 19 | 需求、故事、验收关系 |
| 44 | Requirements vs User Stories 选型 |
| 14 | Stories vs requirements |
| 20–23 | 安全关键合规案例 |
| 6, 27 | EARS 与工具链（映射到测试生成） |

## Topic 6 — 最强 Coding Agent / Harness 的需求格式实证与选型（一轮新增）

**Primary:** 暂无（本轮新增研究线，原文 52 条未覆盖；所有一手材料在 [_reference/](_reference/) 中以 `06-agent-format-*` 或 `00-shared-*` 命名落库）。

该研究线时间窗严格为 **2024Q3–2026Q1**，证据主要来自官方文档、官方仓库模板与工程团队公开案例。见 [topic-06-agent-format.md](topic-06-agent-format.md) §2 观察对象清单与 §3 Wave 0 基线清单。

| 侧重 | 锚点 |
|------|------|
| IDE 级 agent / harness 官方格式 | Cursor Rules、Anthropic Claude Code（CLAUDE.md / Skills / Plugins）、OpenAI Codex CLI、Amp、Aider、Continue、Cline |
| Spec-as-Code 流程工具 | Amazon Kiro、GitHub Spec Kit、OpenSpec |
| 跨工具事实标准候选 | `AGENTS.md` 约定 |
| 失败模式 | context rot、rules bloat、skills vs rules 冲突、spec drift |

## 快速统计

| Topic | 约含编号数（含重叠） |
|-------|----------------------|
| 1 | 6 |
| 2 | 8 |
| 3 | 16 |
| 4 | 18 |
| 5 | 18 |
| 6 | 0（新增研究线，一手材料走 [_reference/](_reference/) 而非原文 52 条） |

全文 52 条均在 [references-full.md](references-full.md)；按 Topic 阅读时无需打开全部 52 条。Topic 6 的一手证据统一走 [_reference/](_reference/) 的 Authoritative Copy，不纳入原 52 条编号系统。
