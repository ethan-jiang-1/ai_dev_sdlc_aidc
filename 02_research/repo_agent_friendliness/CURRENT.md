# CURRENT — repo_agent_friendliness 热区

> 更新于 2026-09-21。冷区（历史轮次）暂无——升级为评估系统前的推敲记录见 git log 与 `10-spec/adr/`。

## 一句话

定义层已定型（**v1.5**：九维 + A/B 两线 + 聚合结构 + 度量语义定标 + 无状态评估器——run bundle 归属被测仓库，ADR 见 `10-spec/adr/`），系统已完成目录重组与 agent 操作化；下一步是**器械层落条**（checklist-A 优先），然后自举试测喂效标。

## 状态表

| 组件 | 位置 | 状态 |
|---|---|---|
| framework v1.5（九维/门禁加权/tier/度量语义/无状态评估器） | `10-spec/framework.md` | ✅ 定型 |
| bundle-format（run bundle 规范） | `20-instruments/bundle-format.md` | ✅ 就绪 |
| 九维定义 + 边界声明 | `10-spec/dimensions/01–09` | ✅ 判据族为草案级 |
| A/B 分型 + 两线评估面 | `10-spec/archetypes.md` + `line-a/b` | ✅ 定型 |
| 结构裁决（八维→九维） | `10-spec/adr/2026-09-21-dimension-sufficiency-review.md` | ✅ |
| checklist-A / checklist-B | `20-instruments/`（规划见其 README） | ❌ 下一交付 |
| harness-profiles | `20-instruments/` | ❌ 待建 |
| tier-0 扫描脚本 | `20-instruments/scan/` | ❌ 待建 |
| 权重数值 | — | 有意不给，待效标回归 |
| runs（本仓库自举） | `30-runs/`（仅自举 bundle + pilot 索引；外部 bundle 归属各自仓库） | 空，待首跑 |

## 下一步（顺序）

1. **checklist-A 落条**（九维 × 行为描述判据，tier-0/1 优先，⑧挂条件判据，每条带 schema 字段）→ `20-instruments/checklist-a.md`。
2. checklist-B 落条（B 子族优先，逐条标共识/探索）。
3. 本仓库自举试测 = 第一个 A 线 run（`30-runs/`，-pilot），同时验证 AGENTS.md 仪式可被零上下文 agent 执行。
4. harness-profiles（从 dimensions 各维"泛化注意"里已拆出的 harness-specific 条目归集）。
5. 多仓库 pilot → 效标回归 → 权重定型（framework §4.4）。

## 遗留的设计开放题

- **⑨ 一手依据薄**：并行 agent/工作流判据多为经验/共识，落条时逐条标注，试测后回填一手出处。
- **B 线六层映射 × ⑨ 的交叠**（archetypes v1.3 已记）：L3/L6 与⑨的重叠部分待 B 线试测后决定是否补映射表。
- **映射与短板函数的数值**（1.0/0.5/0.25、×2 系数）：经验设定，属 §4.4 校准事项而非开放题——pilot 数据进来后复核。

**v1.4 已裁决**（原开放题，见 [`10-spec/adr/2026-09-21-metric-semantics.md`](10-spec/adr/2026-09-21-metric-semantics.md)）：数值映射、A–D 刻度、⑤ 门禁 ⚠️ 封顶 B、可复现性承诺改 agent 语境、③⑨ gitignore 归属（03 管行为后果/09 管提交卫生）、根级路由例外（已写入根 `AGENTS.md` §4）。
