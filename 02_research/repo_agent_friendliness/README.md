# repo_agent_friendliness — 仓库 Agent-Friendly 泛化评估体系

**定位**：一套**仓库无关**的"代码仓库对 coding agent 友好度"评估体系——五维框架 + 可操作判据 + 打分模型。研究层活跃推敲主题（2026-09-21 起）。

## 分法（raw → result 管道）

- `raw/` — 借鉴起点：整库引入自 deer-flow 消化层 `/Users/bowhead/deer-flow/_digest/harness/`
  （引入日期 2026-09-21，内容观测日期 2026-06；deer-flow 侧仍在更新，同步需重新拷贝，本目录不回写）。
  **只是素材参考，不是本主题的权威，更不是路线依据**；其中的仓库案例锚点一律不进 result
  （result 侧锚点已于 2026-09-21 全部剔除，v0 历史底稿除外）。
- `result/` — 泛化体系本体，当前权威：[`result/00-framework-v1.md`](result/00-framework-v1.md)
  （v1.3：三层对象模型、判据 schema、证据等级 tier、门禁+加权分离的聚合结构、效标回归校准协议、**九维正交维度框架**）。
  各维展开定义一维一文件：[`result/10-dimensions/`](result/10-dimensions/README.md)（01–09，含边界声明与判据族草案）。
  维度充分性审查：[`result/30-dimension-sufficiency-v1.md`](result/30-dimension-sufficiency-v1.md)。
  **A/B 两线分立**（2026-09-21 用户定）：[`result/40-line-a-traditional-repo.md`](result/40-line-a-traditional-repo.md)
  （传统代码仓库）、[`result/41-line-b-agentic-repo.md`](result/41-line-b-agentic-repo.md)（智能体代码仓库）。
  [`result/00-framework-v0.md`](result/00-framework-v0.md) 为历史底稿（已被 v1 取代）。
  后续交付：checklist-A / checklist-B（判据从九维判据族直接落条，**不从 raw 60 条派生**）、
  harness-profiles、试测报告、权重校准，逐版叠加不覆盖历史判断。

## 上下游指针（单一事实来源，不复制正文）

- harness/context 治理的**实践方法论**（DSLC、漂移治理）→
  [`../../03_practice/harness_governance/`](../../03_practice/harness_governance/README.md)；
  其 `03b` 的"度量缺口"待由本体系补度量方案（见 result 骨架 §5 路线 3）。
- 活跃对客交付在 `talk-ai-coding-evolution-harness/`；本主题暂不与其 `02_evidence/` 关联（2026-09-21 用户定）。

## 纪律

一手源优先、来源可溯、标注观测日期；判据须给依据，无依据的标注"经验判据"；体系定义不含任何特定仓库的锚点。

**正交纪律（2026-09-21 用户定，打磨时最高优先）**：

1. **维度正交**：每个维度必须能独立成立、独立回答一个核心问题；两个审计者对一个维度打分时不需要参考另一维度的结论。
2. **宁拆不混**：新话题若横跨两个维度，先按核心问题拆开分属，或立新维；**禁止**为了省条目把两个话题合并成一个"混合判据族"——混合会在打磨中变糊。
3. **边界成文**：每条扩维/并族操作必须同时写明与相邻维度的分界（"X 归此维、Y 彼维，分界是……"），边界声明与判据同置于 checklist，不留在讨论记录里。
4. **同词异义拆开**：社区同一术语的多个含义（如 context rot 的"注意力稀释"与"指令资产腐化"）必须拆成不同判据族，不共用一个词下混评。
