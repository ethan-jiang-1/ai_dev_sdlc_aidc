# repo_agent_friendliness — 仓库 Agent-Friendly 评估系统

**定位**：一套**仓库无关**的"代码仓库对 coding agent 友好度"评估系统——九维正交框架 + 可操作判据 + 门禁/加权分离的打分模型。已从研究主题升级为**可被 agent 执行的评估系统**（2026-09-21 重组）：拽任意一个 repo 进来要求评估，按 [`AGENTS.md`](AGENTS.md) 的仪式走完即出报告。

## 分法（系统四层：spec → instruments → runs → archive）

| 层 | 目录 | 是什么 | 变化频率 |
|---|---|---|---|
| 定义层（≈L-core） | [`10-spec/`](10-spec/) | 体系法律：[`framework.md`](10-spec/framework.md)（v1.6 权威，含度量语义定标与无状态裁决）、[`dimensions/`](10-spec/dimensions/README.md)（01–09 一维一文件）、[`archetypes.md`](10-spec/archetypes.md)（A/B 分型）、[`line-a/line-b`](10-spec/line-a-traditional-repo.md)（两线评估面）、[`adr/`](10-spec/adr/)（结构裁决记录） | 慢，版本化 |
| 器械层 | [`20-instruments/`](20-instruments/README.md) | [`bundle-format.md`](20-instruments/bundle-format.md)（run bundle 规范，现役）、checklist-A/B、harness-profiles、tier-0 扫描脚本（**多待建**） | 中，随 spec 版本走 |
| 被测数据（≈L-instance） | **不在本系统** | run bundle 归属被测仓库（`<目标>/agent-friendly-runs/`，评估器无状态）；自举审计同规则，落仓库根同名目录 | 只增不改，随被测仓库走 |
| 冷区 | `90-archive/` | [`framework-v0.md`](90-archive/framework-v0.md)（历史底稿）、[`raw/`](90-archive/raw/README.md)（deer-flow 冻结素材，来源考古） | 不更新 |

目录结构映射体系自己的三层对象模型（framework §1）：10-spec=L-core，20-instruments=L-profile+operational 化判据；**L-instance 不落本系统**——run bundle 归属被测仓库，本目录无运行层。

**当前进展与下一步** → [`CURRENT.md`](CURRENT.md)（热区）。
**评估操作规程**（怎么跑一次审计、manifest/报告模板、打分纪律）→ [`AGENTS.md`](AGENTS.md)。

## 上下游指针（单一事实来源，不复制正文）

- harness/context 治理的**实践方法论**（DSLC、漂移治理）→
  [`../../03_practice/harness_governance/`](../../03_practice/harness_governance/README.md)；
  其 `03b` 的"度量缺口"待由本体系 pilot 校准数据（聚合各自目标仓库 bundle 的 manifest，不入本系统）补度量方案（framework §4.4）。
- 活跃对客交付在 `talk-ai-coding-evolution-harness/`；本主题暂不与其 `02_evidence/` 关联（2026-09-21 用户定）。

## 纪律

一手源优先、来源可溯、标注观测日期；判据须给依据，无依据的标注"经验判据"；体系定义不含任何特定仓库的锚点。

**正交纪律（2026-09-21 用户定，打磨时最高优先）**：

1. **维度正交**：每个维度必须能独立成立、独立回答一个核心问题；两个审计者对一个维度打分时不需要参考另一维度的结论。
2. **宁拆不混**：新话题若横跨两个维度，先按核心问题拆开分属，或立新维；**禁止**为了省条目把两个话题合并成一个"混合判据族"——混合会在打磨中变糊。
3. **边界成文**：每条扩维/并族操作必须同时写明与相邻维度的分界（"X 归此维、Y 彼维，分界是……"），边界声明与判据同置于 checklist，不留在讨论记录里。
4. **同词异义拆开**：社区同一术语的多个含义（如 context rot 的"注意力稀释"与"指令资产腐化"）必须拆成不同判据族，不共用一个词下混评。

**系统纪律（2026-09-21 重组起）**：

5. **runs 只增不改**：报告落盘后不回写；spec/器械变更靠 manifest 断代，不改历史报告。
6. **manifest 必填**：无 manifest 的报告无效（spec/instrument/harness/模型版本必须钉住，否则 tier-1 可复现性承诺不成立）。
7. **结构性裁决进 ADR**：改 spec 前先查 `10-spec/adr/`；新裁决一文件一记录，framework 只留结论。
8. **bundle 随仓库、系统零状态（v1.5–v1.6）**：run 归属被测仓库（`<目标>/agent-friendly-runs/`），评估器运行期对本系统零写入；自举审计同规则，bundle 落本仓库根同名目录；不设任何运行时索引（bundle 的 manifest 即登记）。
