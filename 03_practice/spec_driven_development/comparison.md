# SDD 工具横向比较（2026-09）

> **元数据**
>
> ```yaml
> source: 本目录 tools/ 各深挖文档 + [sdd-tooling-landscape-2026-09.md](sdd-tooling-landscape-2026-09.md)（同目录）
> accessed_at: 2026-09-20
> trust_level: 中高  # 汇总层，数字均可在 tools/ 各文件回溯到一手源；趋势判断含分析成分
> ```
>
> 每个项目的完整证据链见 `tools/` 对应文件；本文件只做横向比较，不复制正文（单一事实源）。

## 1. 总览矩阵

| 项目 | Stars¹ | 创建 | 最近 release | 形态 | 硬度² | 证据强度³ | 趋势 | 主要风险 |
|---|---|---|---|---|---|---|---|---|
| **Superpowers** | 289k | 2025-10 | v6.4.1（09-19） | 方法论 skills 框架 | 软（行为纪律） | 强 | 强上升 | 个人主导、巴士因子、star 泡沫 |
| **GitHub Spec Kit** | 138k | 2025-08 | v1.0.8（09-17，周级） | CLI + Markdown 工件链 | 硬 | 强 | 上升 | 文字量=工作错觉、context 开销 |
| **OpenSpec** | 70k | 2025-08 | v1.13.1（09-17） | 中立轻量 CLI，change-delta | 硬（轻量） | 中强 | 上升 | 贡献头部集中 |
| **BMAD-METHOD** | 53k | 2025-04 | v6.12.0（09-04） | 多 agent 角色化敏捷方法论 | 中（可裁剪） | 中强 | 高位平台偏升 | 流程重、token 成本、双人 bus factor |
| **Amazon Kiro** | —（闭源） | GA 2025-11 | 产品线持续扩张 | spec-driven IDE（EARS 三分文件） | 硬 + 厂商托管 | 事实层强/数字自述=中 | 上升 | 锁定 AWS 生态；数字为厂商自述 |
| **Tessl** | —（闭源） | 2024 | ⚠ 2026-03 起公开停摆⁴ | spec-as-source 平台 | 最硬（spec 为唯一源） | 中 | 停摆转型（改称 Agent Enablement Platform）⁴ | MDD 同构风险、LLM 非确定性、方向弃用 |
| claude-task-master | 28k | 2025-03 | 0.43.1（2026-03-31） | PRD→task 拆解 | 硬 | 强 | **被放弃**（转商业 Hamster） | 已停更 5 个月 |
| spec-workflow-mcp | 4.3k | 2025 | npm 分发 | MCP spec workflow | 硬 | 中 | 平台期偏缓降 | 牌桌边缘 |

¹ 2026-09-20 GitHub API 实测，详见各 tools/ 文件。
² 「硬度」= spec 对 agent 行为的约束方式：硬=机器可校验的显式工件链；软=方法论纪律与 review 流程。
³ 档位定义见 [sdd-tooling-landscape-2026-09.md §3](sdd-tooling-landscape-2026-09.md)。

⁴ 勘误（2026-09-20）：写作时点的"资本上升"已过时；Tessl 自 2026-03 起公开停摆转型，以 [debate/signals-2026h2.md](debate/signals-2026h2.md) 为准。（⁴ 指涉 §1 总览矩阵 Tessl 行的停摆/转型两处上标。）

## 2. 关键分野：三条路线

1. **硬工件链（Spec Kit / OpenSpec / Kiro / Tessl）**：spec/plan/tasks 是机器消费的一等工件，agent 按工件推进。分歧在重量：Spec Kit 全流程最重（constitution→…→converge，三流程+扩展体系），OpenSpec 走 change-delta 轻量线，Kiro 托管在 IDE 里，Tessl 最激进（spec 为唯一源，人不再编辑代码）。
2. **行为纪律（Superpowers）**：没有机器校验的 spec 工件，靠"极细计划 + 两段式 review 对照"软约束 agent。与硬工件是**同题异路、可叠加**（如 Superpowers 的 brainstorm/plan 生成 Spec Kit 的 spec 输入）。
3. **角色化流程（BMAD）**：约束不在 spec 格式而在组织分工——Analyst/PM/Architect/Dev/UX 五角色接力，brief→PRD→架构→spec→故事。适合把"AI 团队"当模拟组织用的人，代价是流程与 token 成本。

## 3. 选型速查

| 场景 | 推荐 | 理由 |
|---|---|---|
| 想要大厂官方默认、生态最广（40+ agent） | **Spec Kit** | GitHub 官方维护、周级发版、社区最大（138k stars）；TW 独立条目未获核验，仅 Vol.33 正文点名（见 [debate/authoritative-verdicts.md](debate/authoritative-verdicts.md) 补遗） |
| 觉得 Spec Kit 太重、要多 agent 并存 | **OpenSpec** | 厂商中立、change-delta 只写增量 |
| 想约束 agent 行为本身而非工件格式 | **Superpowers** | skills 链 + TDD 纪律；可与 1/2 叠加 |
| 团队想模拟完整敏捷组织（PM→架构→开发） | **BMAD** | 角色化产物链完整，接受流程成本为前提 |
| 企业要开箱即用、商业支持 | **Kiro** | AWS 托管、EARS 三分文件；接受生态锁定 |
| 押注"代码消亡、spec 为源"的未来 | **Tessl**（已停摆，仅作方向参照，非推荐） | 资本最重、方向最激进，风险也最大 |

## 4. 趋势总结

> ⚠ 本节为 2026-09-20 快照口径，已被 [debate/README.md](debate/README.md) 的 2026H2 裁决（话语退潮、工件固化、SDD 跌出 Radar 当前版）取代，趋势判断以那边为权威。以下正文保留作快照存档。

- **整体上升，进入两极辩论期**：头部四开源项目 2026-09 仍日/周级发版；同时 HN 批判潮（marmelab "waterfall strikes back" 等）与 claude-task-master 式退出并存，叙事从"银弹"转向"哪种形态对"。
- **洗牌已经发生**：非头部全面停更（others-and-declining.md），生态位被头部收编或被 Kiro 产品化消灭。
- **共同软肋**：所有路线都被独立批评指出同一类问题——spec/计划文字量制造"工作错觉"、长期维护留白、小任务上流程开销大于收益。选型时应按任务规模裁剪而非全量套用。

## 5. 局限

- TW Radar 的 ring 定级：OpenSpec（Assess, 2026-04）已官方直读获得；SDD 主条目与 Spec Kit 条目（后者未命中）的当版 ring 未核验，详见 [debate/authoritative-verdicts.md](debate/authoritative-verdicts.md) 补遗。
- Kiro 用户数、Tessl 估值为厂商自述/二手报道，证据强度弱，已在对应文件标注。
- stars 为单日快照，引用需带观测日期 2026-09-20。
