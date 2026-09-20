# Spec-Driven Development (SDD) 研究目录

> 独立研究层，2026-09-20 从 `requirements_engineering/deep_research_topics/topic-07` 升格而来。
> 话题体量（工具生态 × 方法论辩论 × 厂商采纳三条线）已超出单 topic 承载力。

## 与 `requirements_engineering/` 的分工（不重叠）

| 层 | 管什么 | 例子 |
|---|---|---|
| `requirements_engineering/` | **spec 怎么写**：需求表达格式与工程方法 | User Story、EARS、BDD、INCOSE GTWR |
| `spec_driven_development/`（本目录） | **spec 如何驱动整个开发工作流**：工具、流程、采纳与趋势 | Spec Kit、OpenSpec、Superpowers、BMAD、Kiro、Tessl、TW Radar 定级、SDD 批判潮 |

事实只写一处：两个目录互引用指针，不复制正文。

## 当前内容

| 文件 | 作用 | 观测日期 |
|---|---|---|
| [sdd-tooling-landscape-2026-09.md](sdd-tooling-landscape-2026-09.md) | 工具生态全景：六大项目对比表（stars/活跃度/趋势/证据强度）、公认头部结论、两极辩论期判断、局限标注 | 2026-09-20 |
| [comparison.md](comparison.md) | **横向比较**：总览矩阵、三条路线分野（硬工件链/行为纪律/角色化流程）、选型速查、趋势总结 | 2026-09-20 |
| [comparison-field-reports.md](comparison-field-reports.md) | **实战比较**：只收一线团队复盘的"spec 写作质量 × 工程控制"两维对比，每格挂真实案例 | 2026-09-20 |
| [lineage.md](lineage.md) | 思想谱系：MDD→DbC→形式化方法→BDD→SDD，史实/分析分层 | 2026-09-20 |
| [alternatives.md](alternatives.md) | 替代/后继形态：五种路线 + "重 spec↔零 spec"光谱图 | 2026-09-20 |
| [tools/spec-kit.md](tools/spec-kit.md) | GitHub Spec Kit 深挖 | 2026-09-20 |
| [tools/openspec.md](tools/openspec.md) | OpenSpec 深挖（change-delta 双目录机制） | 2026-09-19/20 |
| [tools/superpowers.md](tools/superpowers.md) | Superpowers 深挖（含"它不是传统 SDD"辨析） | 2026-09-20 |
| [tools/bmad-method.md](tools/bmad-method.md) | BMAD-METHOD 深挖（角色化敏捷方法论） | 2026-09-20 |
| [tools/kiro.md](tools/kiro.md) | Amazon Kiro 深挖（厂商数字已标证据强度） | 2026-09 |
| [tools/tessl.md](tools/tessl.md) | Tessl 深挖（spec-as-source，融资为二手报道口径） | 2026-09 |
| [tools/others-and-declining.md](tools/others-and-declining.md) | claude-task-master（被放弃）+ 边缘项目存目 | 2026-09-20 |
| [debate/README.md](debate/README.md) | **评判综合**：矛盾裁决、加权六点判断、团队落地结论 | 2026-09-20 |
| [debate/signals-2026h2.md](debate/signals-2026h2.md) | 2026.6–9 最新信号全景（矛盾信号以此裁决） | 2026-09-20 |
| [debate/authoritative-verdicts.md](debate/authoritative-verdicts.md) | TW Radar Vol.34 / InfoQ / arXiv 权威评判 | 2026-09-20 |
| [debate/critiques.md](debate/critiques.md) | 批判汇编（影响力加权聚类 5 类） | 2026-09-20 |
| [debate/endorsements-and-experiences.md](debate/endorsements-and-experiences.md) | 正面/经验池（厂商降权，FIXER 为最强独立证据） | 2026-09-20 |
| [debate/team-practices.md](debate/team-practices.md) | 团队协作/工程控制/迭代机制（含活样本与推荐组合） | 2026-09-20 |
| [debate/chinese-community-verdicts.md](debate/chinese-community-verdicts.md) | 中文社区评判（结构性偏差已标注） | 2026-09-20 |

## 一句话结论（层级不同，引用时注意时效）

- 工具格局：公认头部 **Spec Kit（大厂官方）+ Kiro（商业企业验证）+ OpenSpec（中立轻量）**；Superpowers 社区热度第一（~289k stars）但属方法论/skills 形态；BMAD 为重流程流派。
- 趋势判断**以 [debate/README.md](debate/README.md) 为最新权威**（2026H2：话语退潮 + 工件固化，结构性企稳）；本文的"两极辩论期"是 2026-09-20 快照口径，[sdd-tooling-landscape](sdd-tooling-landscape-2026-09.md) 同理。

## 已知缺口（动态清单，2026-09-20 二轮更新）

1. ~~Superpowers 零覆盖~~（tools/ 已补）~~2026H2 信号~~（debate/ 已补）~~大规模团队案例~~（已补：NodeSource/网易智企/Scott Logic，"几十人以上一手实证"仍缺）~~Kiro/BMAD 团队实例~~（已补：仅弱证据——Delta Air Lines 机器转写 + OCTO Talks PO 复盘；`.kiro/` 生产实例仍缺位）~~TW Vol.34 定级~~（已官方直读确证：SDD 主条目 NOT ON CURRENT EDITION）
2. ~~思想谱系未梳理~~（已补：[lineage.md](lineage.md)——"SDD=MDD 的承诺+BDD 的模板，LLM 改变成本结构后的第三次重试"；"SDD=新瀑布"现在有史实坐标可对照）
3. ~~替代/后继形态未成篇~~（已补：[alternatives.md](alternatives.md)——五种形态+"重 spec↔零 spec"光谱图；团队级收敛点=harness 治理路线）
3.5 实战团队场景比较已补：[comparison-field-reports.md](comparison-field-reports.md)——只收一线复盘的"spec 写作质量 × 工程控制"横向比较，每格挂真实案例、无证据的格子如实标注。
4. 全部数据为 2026-09-20 单日快照，趋势判断依赖少量第三方历史锚点（如 OpenSpec 55.9k @06-22），无自建时间序列。

## 约定

- 数据一律 GitHub API 直读 + 交叉验证，标注观测日期；stars 等快照数字随时间失效，引用时带日期。
- 厂商自述数字（Kiro 用户数、Tessl 估值）单独标注证据强度，不当事实引用。
- 每个 tool 一个文件（`tools/<name>.md`，统一模板：定位/起源/工件链/指标/采纳/趋势/批评/适用场景/来源）；横向结论只写 `comparison.md`，单文件不重复。
- ~~后续扩展建议子目录：`tools/`（单项目深挖）、`debate/`（方法论批判与反批判）、`adoption/`（企业案例）。~~ `tools/` 已于 2026-09-20 落地；`debate/`、`adoption/` 仍待建。
