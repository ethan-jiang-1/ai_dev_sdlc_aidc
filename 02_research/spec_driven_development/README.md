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
| [tools/spec-kit.md](tools/spec-kit.md) | GitHub Spec Kit 深挖 | 2026-09-20 |
| [tools/openspec.md](tools/openspec.md) | OpenSpec 深挖（change-delta 双目录机制） | 2026-09-19/20 |
| [tools/superpowers.md](tools/superpowers.md) | Superpowers 深挖（含"它不是传统 SDD"辨析） | 2026-09-20 |
| [tools/bmad-method.md](tools/bmad-method.md) | BMAD-METHOD 深挖（角色化敏捷方法论） | 2026-09-20 |
| [tools/kiro.md](tools/kiro.md) | Amazon Kiro 深挖（厂商数字已标证据强度） | 2026-09 |
| [tools/tessl.md](tools/tessl.md) | Tessl 深挖（spec-as-source，融资为二手报道口径） | 2026-09 |
| [tools/others-and-declining.md](tools/others-and-declining.md) | claude-task-master（被放弃）+ 边缘项目存目 | 2026-09-20 |

## 一句话结论（详见上表文件）

- 公认头部：**Spec Kit（大厂官方）+ Kiro（商业企业验证）+ OpenSpec（中立轻量）**；Superpowers 社区热度第一（~289k stars）但属方法论/skills 形态；BMAD 为重流程流派。
- 整体趋势：**上升，进入两极辩论期**（TW Radar 收录 vs HN 批判潮；claude-task-master 停滞标志工具层洗牌）。

## 约定

- 数据一律 GitHub API 直读 + 交叉验证，标注观测日期；stars 等快照数字随时间失效，引用时带日期。
- 厂商自述数字（Kiro 用户数、Tessl 估值）单独标注证据强度，不当事实引用。
- 每个 tool 一个文件（`tools/<name>.md`，统一模板：定位/起源/工件链/指标/采纳/趋势/批评/适用场景/来源）；横向结论只写 `comparison.md`，单文件不重复。
- ~~后续扩展建议子目录：`tools/`（单项目深挖）、`debate/`（方法论批判与反批判）、`adoption/`（企业案例）。~~ `tools/` 已于 2026-09-20 落地；`debate/`、`adoption/` 仍待建。
