# CURRENT — repo_agent_friendliness 热区

> 更新于 2026-09-21。冷区（历史轮次）暂无——升级为评估系统前的推敲记录见 git log 与 `10-spec/adr/`。

## 一句话

定义层已定型（**v1.7**：九维 + A/B 两线 + 聚合结构 + 度量语义定标 + 无状态评估器 + **一致性加固**——N/A/条件判据/观察项语义、B 线双路径评级域、tier-2 演练写入豁免与映射补⑥，run bundle 归属被测仓库、系统三层收敛，ADR 见 `10-spec/adr/`）；下一步是**器械层落条**（checklist-A 优先，判据带 `applicable` 字段），然后自举试测喂效标。

## 状态表

| 组件 | 位置 | 状态 |
|---|---|---|
| framework v1.7（九维/门禁加权/tier/度量语义/无状态评估器/N/A 语义） | `10-spec/framework.md` | ✅ 定型 |
| bundle-format（run bundle 规范） | `20-instruments/bundle-format.md` | ✅ 就绪 |
| 九维定义 + 边界声明 | `10-spec/dimensions/01–09` | ✅ 判据族为草案级 |
| A/B 分型 + 两线评估面 | `10-spec/archetypes.md` + `line-a/b` | ✅ 定型 |
| 结构裁决（八维→九维 / 度量语义 D1–D6 / 无状态评估器 v1–v3） | `10-spec/adr/` | ✅ |
| checklist-A / checklist-B | `20-instruments/`（规划见其 README） | ❌ 下一交付 |
| harness-profiles | `20-instruments/` | ❌ 待建 |
| tier-0 扫描脚本 | `20-instruments/scan/` | ❌ 待建 |
| 权重数值 | — | 有意不给，待效标回归 |
| runs | **不在本系统**：bundle 归属被测仓库（`<目标>/agent-friendly-runs/`）；自举 bundle 落仓库根同名目录 | 待自举首跑 |

## 下一步（顺序）

1. **checklist-A 落条**（九维 × 行为描述判据，tier-0/1 优先，⑧挂条件判据，每条带 schema 字段——含 v1.7 新增 `applicable`）→ `20-instruments/checklist-a.md`。
2. checklist-B 落条（B 子族优先，逐条标共识/探索；探索级入观察项不计分，ADR D5/D6）。
3. 本仓库自举试测 = 第一个 A 线 run（bundle 落仓库根 `agent-friendly-runs/`，-pilot），同时验证 AGENTS.md 仪式可被零上下文 agent 执行。
4. harness-profiles（从 dimensions 各维"泛化注意"里已拆出的 harness-specific 条目归集）。
5. 多仓库 pilot → 效标回归 → 权重定型（framework §4.4）。

## 遗留的设计开放题

- **⑨ 一手依据薄**：并行 agent/工作流判据多为经验/共识，落条时逐条标注，试测后回填一手出处。
- **B 线六层映射 × ⑨ 的交叠**（archetypes v1.3 已记）：L3/L6 与⑨的重叠部分待 B 线试测后决定是否补映射表。
- **映射与短板函数的数值**（1.0/0.5/0.25、×2 系数）：经验设定，属 §4.4 校准事项而非开放题——pilot 数据进来后复核。
- **⑥ 可达性判据的适用条件**（v1.7 遗）：演练无卡点时按成文性评分并注明"可达性未采证"——此默认是否成立，试测后复核。

**v1.4–v1.6 已裁决**（原开放题，见 [`10-spec/adr/2026-09-21-metric-semantics.md`](10-spec/adr/2026-09-21-metric-semantics.md) 与 [`10-spec/adr/2026-09-21-stateless-auditor-run-bundle.md`](10-spec/adr/2026-09-21-stateless-auditor-run-bundle.md)）：数值映射、A–D 刻度、⑤ 门禁 ⚠️ 封顶 B、可复现性承诺改 agent 语境、③⑨ gitignore 归属（03 管行为后果/09 管提交卫生）、根级路由例外（已写入根 `AGENTS.md` §4）、run bundle 归属被测仓库且 `30-runs/` 删除（自举落仓库根，不设索引——manifest 即登记，运行时状态不入系统）。

**v1.7 已裁决**（2026-09-21 一致性加固，ADR 同上两份的 v2/v3）：D5 N/A/条件判据/观察项度量语义（schema `applicable`、N/A 不进分母与短板、整维全 N/A 不参与刻度）；D6 B 线双路径评级域；tier-2 演练写入豁免（一次性 worktree/克隆）与演练映射补⑥（⑥判据双层：成文性 tier-0 + 可达性 tier-2）；编辑残留清理（framework §4.1 重复段、03b→02b、"raw 07"→90-audit-checklist、bundle 命名统一、archetypes 表格、05 归侧口径、① 40% 指针、共享表面开放式引用、⑤⑥ 边界成文）。二轮复核追加：③⑧ lockfile 漂移双算收口（03 管入库工件面 / 08 管机器检查）、N/A 语义铺开至 ②⑥⑨ 维（废"加分项"措辞）、混合形态=每产出物一个 bundle、CI 常驻扫描不构成审计 run 不产 bundle、根 README 主题数口径拉平。
