# CURRENT — repo_agent_friendliness 热区

> 更新于 2026-09-21。冷区（历史轮次）暂无——升级为评估系统前的推敲记录见 git log 与 `10-spec/adr/`。

## 一句话

定义层已定型（v1.3 九维 + A/B 两线 + 聚合结构），系统刚完成目录重组与 agent 操作化（AGENTS.md）；下一步是**器械层落条**（checklist-A 优先），然后自举试测喂效标。

## 状态表

| 组件 | 位置 | 状态 |
|---|---|---|
| framework v1.3（九维/门禁加权/tier/效标协议） | `10-spec/framework.md` | ✅ 定型 |
| 九维定义 + 边界声明 | `10-spec/dimensions/01–09` | ✅ 判据族为草案级 |
| A/B 分型 + 两线评估面 | `10-spec/archetypes.md` + `line-a/b` | ✅ 定型 |
| 结构裁决（八维→九维） | `10-spec/adr/2026-09-21-dimension-sufficiency-review.md` | ✅ |
| checklist-A / checklist-B | `20-instruments/`（规划见其 README） | ❌ 下一交付 |
| harness-profiles | `20-instruments/` | ❌ 待建 |
| tier-0 扫描脚本 | `20-instruments/scan/` | ❌ 待建 |
| 权重数值 | — | 有意不给，待效标回归 |
| runs | `30-runs/`（模板就绪） | 空，待首跑 |

## 下一步（顺序）

1. **checklist-A 落条**（九维 × 行为描述判据，tier-0/1 优先，⑧挂条件判据，每条带 schema 字段）→ `20-instruments/checklist-a.md`。
2. checklist-B 落条（B 子族优先，逐条标共识/探索）。
3. 本仓库自举试测 = 第一个 A 线 run（`30-runs/`，-pilot），同时验证 AGENTS.md 仪式可被零上下文 agent 执行。
4. harness-profiles（从 dimensions 各维"泛化注意"里已拆出的 harness-specific 条目归集）。
5. 多仓库 pilot → 效标回归 → 权重定型（framework §4.4）。

## 遗留的设计开放题（落 checklist 时逐条裁决）

- **短板制公式语义**（framework §4.3）：❌ 记 0 分时"最低条目分×2"使单条 ❌ 直接清零整维——是否本意？需定义 ✅/⚠️/❌ 的数值映射后再检验公式。
- **评级刻度未定义**：§4.2 提到"D 级（不合格）"但 A–D 刻度全文无定义（raw 90 有旧刻度但已归档不继承）——checklist-A 落条时定。
- **⑤ 门禁 ⚠️ 的处置**：不降级只进整改，还是部分 ⚠️ 也降级（05 维开放问题）。
- **③⑨ gitignore 卫生双算**：03 判据族 2 与 09 判据族 1 共享表面，落条时按"03 管配置模板分离、09 管提交卫生"注明归属。
- **⑨ 一手依据薄**：并行 agent/工作流判据多为经验/共识，落条时逐条标注，试测后回填一手出处。
- **B 线六层映射 × ⑨ 的交叠**（archetypes v1.3 已记）：L3/L6 与⑨的重叠部分待 B 线试测后决定是否补映射表。
- **可复现性承诺的对象**（framework 设计约束 3）：spec 写"两个审计者结果一致"，AGENTS 仪式是单 agent 执行——agent 语境下的等价承诺（同模型复跑一致？跨模型允许多大偏差？）未定义，落 checklist 时一并定。
- **根级路由待更新（需动根 AGENTS.md，用户定）**：根级仍称 02_research 为"沉淀状态"且研究层分法写的是 raw/digested/result——与本目录"活跃评估系统 + 四层分法"已不一致，未来 agent 按根级路由可能误判本目录性质。
