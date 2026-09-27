# 02_research — 研究层 · 分析

**定位**：围绕主线的长期研究沉淀（默认**沉淀状态**；**例外**：`repo_agent_friendliness/` 活跃评估系统、`ai_loop_engineering/` 活跃研究主题——见根 AGENTS §4）。
补素材 / 改结论前先确认是否为某场 talk 服务——**是 → 走该 talk 的 `02_evidence/`，不在根级研究层改**。

## 统一分法

多数主题是自包含的 `raw → digested → result` 管道：`raw_*` 收一手素材，`digested` 收消化稿，
`result` 收成稿。各主题入口见下表；动手前先读该主题 README（没有的，agent 摸清分法后补一个最小 README）。

## 主题一览

| 主题 | 讲什么 | 入口 |
|---|---|---|
| `agentic_engineering/` | AI-Coding 范式变迁主报告（多轮 wave 迭代，result_4_v5 为当前版） | `result_4_v5/` |
| `agentic_management/` | Agentic 管理侧景观（一手 raw 尚未消化，result 为空） | `raw /` |
| `agentic_teams/` | 多智能体团队（Agent Teams PPT 成稿） | `result/agent_teams_ppt.md` |
| `ai_loop_engineering/` | Loop Engineering（2026-06 起这场**被命名的实践运动**，**活跃**）：命名谱系、KOL 一手见解与实战、构件、与 SDD 的边界判定。素材常态在 `raw/evidence-*.md` 回源档案（深度卡仅 Andrew Ng） | `raw/kol-roster.md`（★ 名单权威）+ `digested/README.md`（问题看板）；未来综述 → `result/` |
| `ai_native_rnd/` | 从瀑布 / 敏捷到 AI-Native 研发的跃迁 | `result/AI_Native_Agile_Evolution.md` |
| `ai_sdlc_frontier/` | 前沿议题：各家一线人物访谈 + 上下文压缩六家对比等 followup | `followup_research/` |
| `anthropic_ai_sdlc/` | Anthropic 官方 AI-Native SDLC playbook（英译原文 + 中文编译） | `org/ai-native-sdlc-playbook.md` |
| `repo_agent_friendliness/` | 仓库 Agent-Friendly **评估系统**（九维框架 + A/B 分型 + 门禁/加权分离打分；**活跃**——拽任意 repo 进来按其 `AGENTS.md` 仪式出报告。**例外分法**：`10-spec / 20-instruments / 90-archive` 三层，run 数据归属被测仓库、不落本仓库） | `README.md`（体系权威 `10-spec/framework.md`） |
| `thoughtworks_ai_sdlc/` | ThoughtWorks 方法论视角的 AI-Native SDLC 最终报告 | `final/AI_NATIVE_SDLC_FINAL_ENGINEER_REPORT.md` |

> 2026-09-21 拆出记录：`requirements_engineering/`、`spec_driven_development/` 已移至
> `03_practice/`（用户判定内容已是 practice 而非 research）。
>
> 2026-09-27 合并记录（同名重复目录收口，均保留「有实质内容 + 名字正确」的一方）：
> ① `anthorpic_ai_sdlc/`（拼写错）→ 并入 `anthropic_ai_sdlc/`：仅剩的 `org/figures/`、`raw/figures/`
> 迁回，旧目录删除（此前 org-sdlc talk 的 `rawdata_anthropic-ai-native-sdlc-playbook.md` 断链随此修复）；
> ② `rnd_native_2.0/`（2026-08 脚手架，空目录 + 两句未动工意向）→ 并入 `ai_native_rnd/`，旧目录删除。
>
> **遗留目录不在上表**：`requirements_engineering/`（2026-09-21 拆出后的空壳，仅剩空目录）。

## 纪律

一手源优先、来源可溯、标注观测日期（与 `01_sources/`、`03_practice/` 统一）。
