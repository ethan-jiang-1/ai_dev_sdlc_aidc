# SDD 的替代与后继形态——批判面指向的出路到底长什么样

> **当前结构（定性，2026-09-21）**：本 README 是本目录的**总览与判断层**（机制速览 + 光谱图 + §7 结论）；本地保留三个形态分篇（01 可验证规格 / 02 plan mode / 03 测试优先），深挖与证据以各分篇为权威，本文不复制分篇正文。context engineering 派与 harness 治理派两分篇已于 2026-09-21 抽出升格为独立主题 [`../harness_governance/`](../harness_governance/README.md)（AI 形态下新的 SDLC，含其全部证据档案与图形），**这两篇的内容权威在 harness_governance**；本文件 §2 / §3 速览仅作历史光谱定位，冲突时以那边分篇为准。与 SDD 工具层实践的分工指针见 [`../spec_driven_development/README.md`](../spec_driven_development/README.md)。
>
> **变更史**：2026-09-20 升格独立目录 → 09-21 定名 beyond_spec_driven_development → 09-21 抽出 context / harness 两分篇（抽出前编号 02/03，现 harness_governance 编号 01/02）。

| 形态 | 分篇 | 一句话 |
|---|---|---|
| 验证优先/可验证 spec | [01-verifiable-specs.md](01-verifiable-specs.md) | spec 必须降格为机器可校验的产物（VSDD/compilable specs/facts） |
| Plan mode 派 | [02-plan-mode.md](02-plan-mode.md) | 规划内嵌于 harness，会话内对齐、用完即弃 |
| Context engineering 派 | [01-context-engineering.md](../harness_governance/research/01-context-engineering.md)——已抽出（原本地 02 → 现 harness_governance 01） | 只管 repo 级规则文件纪律，不建 feature 级工件 |
| Harness 治理派 ★ | [02-harness-governance.md](../harness_governance/research/02-harness-governance.md)——已抽出（原本地 03 → 现 harness_governance 02） | 治理对象从 spec 文档转向 agent 执行链路——团队级收敛点 |
| 测试优先回归 | [03-test-first.md](03-test-first.md) | 测试就是 spec：给 CI 读的可执行断言替代文档合约 |

**阅读路径建议**：① 先看两张总图（光谱 → 验证迁移）建立框架 → ② 按优先级读分篇（01 可验证规格为主），每篇先图后文 → ③ 需要溯源进对应证据档案（全部逐字摘录 + 引用链核验，2026-09-21 审计）→ ④ 02 plan mode / 03 测试优先仅作对照。
（2026-09-21 起：context / harness 治理两分篇——**抽出前编号 02 / 03**，非本目录现行 02 plan mode / 03 测试优先——的深挖与证据档案在 [`../harness_governance/`](../harness_governance/README.md)。）

**研究优先级（2026-09-21 用户定，编号对应重排后）**：01 可验证 spec / 02 context engineering / 03 harness 治理曾为重点路线；**02 / 03 已于同日抽出为独立主题 [`../harness_governance/`](../harness_governance/README.md)**，本目录重点收敛为 **01 可验证 spec**；本目录 02 plan mode / 03 测试优先为背景参照、不作为重点——按用户经验：plan mode 是默认实践，够不上独立"后继形态"；测试优先是既有工程常识的延续，不是新范式。引用 plan mode / 测试优先时作对照用，不作主张依据。

**最靠谱判断（2026-09-21）**：harness 治理最靠谱（五形态时期旧号 03，现属 [../harness_governance/research/02-harness-governance.md](../harness_governance/research/02-harness-governance.md)）——判据、排序与新实证见文末 §7。

### 证据档案（逐字摘录 + 引用链核验，全部经 2026-09-21 审计）

| 档案 | 服务的分篇 | 内容 |
|---|---|---|
| [01a-verifiable-convergence-evidence.md](01a-verifiable-convergence-evidence.md) | 01 | 13 集群正反原文摘录 + 独立性判定（含对撞） |
| [01b-verifiable-academic.md](01b-verifiable-academic.md) | 01 | 20+ 篇学术一手回源 + 7 例工业案例 |
| [01c-verifiable-community.md](01c-verifiable-community.md) | 01 | HN 立场分歧 + 中文社区宽度 |
| （01a / 01b / 01c / 02a / 02b，随抽出重编号） | 01 / 02（新编号） | **已随分篇抽出** → [`../harness_governance/`](../harness_governance/README.md) |

图形（SVG）：
- ![形态光谱](figures/spectrum.svg)——九个位置从"重 spec 工件"排到"零 spec 工件"
- ![验证责任迁移](figures/verification-shift.svg)——文档中心 vs 机器中心的结构性对照
- ![consistency tax 三角](figures/01-consistency-tax-triangle.svg)——①篇：三角回写困境与两个失效面
- （渐进披露三层 / context ⊂ harness / harness 收敛地图三张已随 context / harness 治理两分篇抽出（抽出前编号 02/03） → `../harness_governance/research/figures/`）

```yaml
topic: SDD 的替代/后继形态（验证优先、plan mode、context engineering、harness 治理、测试优先）
accessed_at: 2026-09-21  # 一轮 2026-09-20；二轮/三轮深挖与三轮证据审计至 2026-09-21
captain_verdict: 2026-09-21  # §7 判断层：harness 治理最靠谱（判据 + 当日 SSRN/IEEE 补查，新证据此前未收）
promoted_at: 2026-09-21  # 自 spec_driven_development/alternatives/ 升格为独立主题目录（当日先落 02_research、同日归入实践层 03_practice/），用户定名 beyond_spec_driven_development
extracted_at: 2026-09-21  # context/harness 治理两分篇（抽出前编号 02/03）及其证据、图形抽出为 ../harness_governance/（AI 形态下新的 SDLC），用户定
collector: delegated research agent
scope: 2026 年（尤其 2026Q2–Q3）社区材料；承接 ../spec_driven_development/debate/critiques.md「批判观点聚类」第 5 条的出路指向
related:
  - ../harness_governance/README.md                          # 两分篇抽出后的新家（抽出前编号 02/03，现 01/02）（内容权威）
  - ../spec_driven_development/debate/critiques.md          # 批判面（本文的"问题从哪来"）
  - ../spec_driven_development/comparison.md             # SDD 工具横比（光谱图左端的素材）
  - ../spec_driven_development/debate/authoritative-verdicts.md
weights: 高=大厂/学术/高热帖；中=有实证的博客/团队案例；低=个人观点
limitations:
  - isoform.ai《The Limits of Spec-Driven Development》正文抓取失败（critiques.md 已记录），facts 路线以 av/facts（GitHub, HN 7 分）为主要锚点。
  - 「Google 改口 context-driven」未找到 Google 官方逐字表述；本文以 Google 2026-05 白皮书《The New SDLC with Vibe Coding》（Osmani 等）与 Addy Osmani 2026 年系列文章作为该派最接近的官方锚点，措辞按二手转述标注。
  - 部分中文社区帖（知乎/腾讯云）为署名个人文章，权重按中低计。
```

---

## 0. 定位：这五条形态在回答什么问题

critiques.md 的批判聚类收敛到两个死结：**spec 无法自我验证**（裸 markdown 是"看似严谨的散文"）和 **spec 作为长期资产的维护税**（spec 债、一致性税、context tax）。2026 年社区给出的出路不是单一替代品，而是一个**离散谱**：各家在"保留多少 spec 工件、把验证交给谁"上给出不同答案——从"spec 仍是核心工件但必须机器可校验"，到"spec 工件彻底消失、只留下测试与上下文纪律"。本文按"重 spec → 零 spec"顺序展开五条形态，最后合成光谱图。

---

## 1. 验证优先 / 可验证 spec（VSDD、compilable specs、facts）→ 深挖：[01-verifiable-specs.md](01-verifiable-specs.md)

**机制**：承认"spec 先行"的价值，但否定"自然语言 spec 本身可作合约"。spec 必须降格为**机器可校验的产物**——或编译成测试/形式化约束（compilable specs），或收缩为一份事实清单（facts），或加上对抗性验证层（VSDD）。LLM 在这条路线里只做"翻译"：把可验证的规约翻译成实现，而不是从散文里自由发挥。

**代表实践/工具**：
- **VSDD（Verified Spec-Driven Development）**：dollspace-gay 的 gist 提案（2026-02-28），把 SDD、TDD、对抗验证排成顺序门禁：spec 过关才准写测试、测试存在才准写代码、对抗 reviewer 找不出真缺陷才准交付（[gist](https://gist.github.com/dollspace-gay/d8d3bc3ecf4188df049d7a4726bb2a00)，HN 211 分/118 评；二手解读见 [Midas Tools 文](https://dev.to/midastools/vsdd-the-ai-coding-methodology-actually-worth-stealing-35ah)）。
- **compilable specs**：VSDD 讨论串里的主流收敛观点——"markdown spec 是弱合约，必须编译成测试/形式化约束才可信"。学术侧的近亲是 spec 自动形式化（如 Verus-SpecGym，arXiv 2605.26457，评测 spec→形式规约的 autoformalization）；实践侧如 Sadogursky 的 "intent integrity chain"（意图→验证管线，见 production-ready/chapters/06-spec-formalization.md）。
- **av/facts**（2026-05-04）：作者直接弃用 SDD，把 spec 降级为"一堆 facts"——只保留可核对的事实、丢掉流程性文本，动机是原话"agents start making mistakes maintaining them. There's a constant **consistency tax**"（[github.com/av/facts](https://github.com/av/facts)，HN 7 分/4 评）。

**与 SDD 的本质区别**：SDD 相信"写清 spec = 控制住 agent"；验证优先派认为**未被验证器消费的 spec 没有控制力**。控制权从"文档的说服力"转移到"验证器的通过/失败"——spec 不再是给 agent 读的散文，而是给校验器读的输入。facts 是其极简变体：不维护叙事与流程，只维护事实，直接砍掉 spec 债的来源。

**已有证据与热度**：本五形态中热度最高（HN 211/118 是 2026 年 SDD 相关最大讨论场），且直接由批判共识催生。但证据形态仍是"提案+群体辩论"，缺大规模落地实测；facts 是单人工具、热度低但代表"用行动背书"的分化点。

**对团队的适用性**：适合**契约清晰、可测试性强的领域**（API、协议、解析器、正确性敏感的系统）。成本在于把需求写成可验证形式需要专门能力（deontologician 批判在此仍然成立：你还糊涂时写不出可验证 spec）。facts 形态适合小团队止损：与其维护注定漂移的 spec 叙事，不如只维护事实清单。对探索性需求（不知道自己要什么）不适配。

---

## 2. Context engineering 派 → 深挖：[../harness_governance/research/01-context-engineering.md](../harness_governance/research/01-context-engineering.md)（内容权威）

> 本节为抽出前的历史光谱定位，内容权威已在 harness_governance，仅作光谱参照。

**历史光谱定位卡（2026-09-21 抽出时收缩）**：

- **光谱位置**：中右——无 feature 级 spec 工件，仅 repo 级持久上下文纪律。
- **一句话机制**：约束对象从 feature 级 spec 上移为 repo 级规则文件与上下文结构（AGENTS.md / 结构化 docs / 渐进式披露），纪律永久但轻量，feature 级意图不落盘。
- **与 SDD 的本质区别**：治理单位从"变更"（feature 级工件链）变为"环境"（repo 持久上下文质量），放弃工件创建-维护闭环故不产生 spec 债，代价是跨会话"为什么"信息流失。
- **适用场景**：brownfield 与日常迭代的主流解。
- **机制/证据/适用性详见** [../harness_governance/research/01-context-engineering.md](../harness_governance/research/01-context-engineering.md)（内容权威）。

---

## 3. Harness 治理派 ★ → 深挖：[../harness_governance/research/02-harness-governance.md](../harness_governance/research/02-harness-governance.md)（内容权威）

> 本节为抽出前的历史光谱定位，内容权威已在 harness_governance，仅作光谱参照。

**历史光谱定位卡（2026-09-21 抽出时收缩）**：

- **光谱位置**：中——spec（若有）只是 harness 中 scaffolding 的一个组件。
- **一句话机制**：把"让 agent 做对"的工程投入从写文档转移到工程化执行环境（linter/结构测试/可观测性接入/gardener agent），即 Hashimoto 六步模型的 Step 5 "Engineer the Harness"（原注"第六阶段"已按 harness_governance 02 分篇勘误）。
- **与 SDD 的本质区别**：SDD 工件中心（管好 spec 就管住 agent），harness 派系统中心（agent 出错时问"执行链路缺什么能力"）；spec 从"方法论本体"降格为"harness 的一个可替换组件"。
- **适用场景**：有平台能力的团队的中长期解，团队级收敛点。
- **机制/证据/适用性详见** [../harness_governance/research/02-harness-governance.md](../harness_governance/research/02-harness-governance.md)（内容权威）。

---

## 4. Plan mode 派（背景参照）→ 深挖：[02-plan-mode.md](02-plan-mode.md)

**机制**：不引入任何独立 spec 工件。规划作为 agent harness 的**内置阶段**存在：agent 先出计划、人批准、再执行（Claude Code plan mode、Codex 的 plan/approval 机制、Antigravity 的"plan approval before executing"）。规划在 Claude Code 默认形态下是一次性的会话内产物，用完即弃、不进入仓库；但这是 harness 默认生命周期而非普遍事实（Antigravity 持久 Artifact、Cursor 可落盘等反例见 [02-plan-mode.md](02-plan-mode.md) §1）。

**代表实践/工具**：Claude Code plan mode 与 Codex 内置规划；HN 帖中多位开发者自述"plan mode 就够了"——如 [HN 48235526](https://news.ycombinator.com/item?id=48235526)（《AI has a multiplying effect on existing technical skills》，2026-05-22，344 分；"For myself I always found the plan mode to work well"，2026-09-21 经 HN Algolia API 回源核实，原锚点域名 hn.nuxt.dev 为笔误已修正）；更结构化的用法如 "Separation of planning and execution"（[HN 47106686](https://news.ycombinator.com/item?id=47106686)，同名帖，2026-02-22，经同 API 回源核实，原锚点域名 althacker.news 为笔误已修正）：规划会话与执行会话分离，计划以对话形式存在。

**与 SDD 的本质区别**：SDD 把"意图"做成**跨会话的持久资产**；plan mode 派认为持久 spec 工件正是 spec 债的根源，规划的价值在**当下会话内对齐**，对齐完就该消失。另一个区别：plan mode 的产出由 harness 的生命周期管理（不可编辑、不漂移），SDD 的 spec 则必须有人维护——而批判已证明没人维护。反向声音也存在：Nearform《Why plan mode is not enough》（**2026-03-18**，作者 Luca Lanziani；原注 2026-09 有误，详见 [02-plan-mode.md](02-plan-mode.md)）主张 plan mode 规划实现不规划产品、缺多角色参与，处方是 BMAD 多 persona 而非恢复 spec 工件链——两派是同一问题的两个解。另一关键动向（2026-02 Boris Cherny YC 访谈，原注 2026-09 有误）：Claude Code 作者判断 plan mode"生命周期有限、会被模型自动触发吸收"；硬证据是 Codex 2026-08-31 将 `update_plan` 改 opt-in（PR #41744）——内置规划器正被 harness 化为可拆卸组件。

**已有证据与热度**：plan mode 是 2026 年**事实上的默认实践**（所有主流 coding agent 内置），使用基数最大；但"plan mode 就够了"以零散 HN 回帖与个人实践为主，无系统实证。反对文（Nearform）热度中等。整体权重：中（实践普及度高、论证散）。

**对团队的适用性**：单人/小团队、中等复杂度、代码库上下文可被 agent 自行探索的场景——这是大多数日常任务的真实形态。不适合需要跨会话/跨人沉淀契约的团队协作与长周期系统：一次性计划无法承担"可继承的工程记忆"职能（腾讯云 Harness 文中 OpenAI "Agent 看不到的就不存在"论是它的对命题）。

---

## 5. 测试优先回归 → 深挖：[03-test-first.md](03-test-first.md)

**机制**：干脆不写行为 spec——**测试就是 spec**。契约由 TDD 的 red-green-refactor 纪律或性质测试（property-based tests）承载：先写会失败的测试（即先写下"系统应该怎样"的可执行断言），实现使其变绿。漂移问题自动消解：测试随代码同 PR 演化，测试挂了就是 spec 与实现失配的显式报警——这恰好补上 harness 派承认的"Spec 漂移是沉默的"缺口。

**代表实践/工具**：经典 TDD 在 AI 语境的复兴；性质测试作契约（不变量、roundtrip 性质等由 agent 自行探索边界）；**Superpowers** 的 TDD 纪律 skills 链（无机器 spec 工件，靠"极细计划 + 测试先行 + 两段式 review 对照"软约束 agent；2026-09 实测 289k stars、v6.4.1 周级发版，见 [../spec_driven_development/comparison.md](../spec_driven_development/comparison.md)）是此路线最热的方法论载体；学术/工具侧如 Consort（arXiv 2609.09671）"spec-first agent framework for **enforced, test-driven** development"——用数据库分支等机制**强制**测试纪律，是"测试作硬合约"的工具化形态。

**与 SDD 的本质区别**：SDD 的合约是**给人读、给 agent 读的文档**；测试优先派的合约是**给 CI 读的可执行断言**。verify 与 define 合一：不存在"spec 说了但代码没做"的验证留白（marmelab 的 False Sense of Security 案例——agent 把 "verify implementation" 标 done 却零测试——在此结构性不可能）。代价：测试只能表达"可断言的行为"，无法承载意图、理由、非功能约束的"为什么"——它管住行为，不管住方向。

**已有证据与热度**：TDD 作为工程常识无需热度证明；Superpowers 289k stars 说明"行为纪律"路线在 2026 年实际比多数 spec 工具更受欢迎；dbreunig 复盘中的 whenwords（纯 spec + 750 个 YAML 一致性测试）可视为两者的杂交先例——但作者本人已自我推翻其单向等式。权重：中高（实践广、方法论热、独立量化少）。

**对团队的适用性**：测试基础设施成熟的团队几乎无门槛，特别适合**回归保护与行为锁定**场景（重构、bug 修复、给 agent 划红线）。短板与 facts 派对称：表达力上限——探索性/设计密集的工作先没有可写的断言（TDD 圈自己的"测试驱动设计 vs 先想清设计"老争论在 agent 语境重现）。

---

## 6. 形态光谱图：从"重 spec 工件"到"零 spec 工件"

> 图形版见 [spectrum.svg](figures/spectrum.svg)（结构对照）与 [verification-shift.svg](figures/verification-shift.svg)（验证责任迁移的两种落法）；下方 ASCII 为纯文本备援，表格为权威口径。

```
重 spec 工件 ◄──────────────────────────────────────────────► 零 spec 工件

  Tessl          Spec Kit / Kiro    OpenSpec     VSDD / compilable    Harness 治理       Context eng.      Plan mode      facts      TDD/性质测试
  (spec 为唯一源)  (全流程工件链)      (轻量delta)   specs (可验证spec)    (spec=组件之一)     (repo规则文件)     (会话内即弃)    (仅事实)    (spec隐含在测试)
  │◄────────── 经典 SDD 区间 ──────────►│◄───── 后继形态（本文）─────────────────────────────────────►│
```

| 位置 | 形态 | spec 工件地位 | 验证由谁承担 | 漂移风险 | 典型适用场景 |
|---|---|---|---|---|---|
| 最左 | Tessl 式 spec-as-source | 唯一源，人不写代码 | 形式化/工具链 | 极高（MDD 同构） | 押注型实验，2026-03 起已停摆转型 |
| 左 | Spec Kit / Kiro / OpenSpec | 一等持久工件 | 人工 review + checklist | 高（spec-kit #1191 群证实） | greenfield、契约清晰的新功能 |
| 中左 | VSDD / compilable specs | 持久但必须机器可校验 | 验证器 + 对抗 reviewer | 中（验证器逼你同步） | 正确性敏感系统（API/协议/解析器） |
| 中 | Harness 治理（OpenAI 式） | 降格为 scaffolding 组件 | 机器约束 + 反馈回路 + gardener | 低–中（主动检测） | 有平台能力的团队、长期演进的大系统 |
| 中右 | Context engineering（AGENTS.md 纪律） | 无 feature 级，仅 repo 级 | agent 自查 + review | 低（无工件可漂移） | brownfield 日常迭代（当前最普遍默认） |
| 右 | Plan mode | 会话内即弃 | 人工批准当下对齐 | 无（不留存） | 单人/中小任务的日常默认 |
| 更右 | facts（av/facts） | 收缩为事实清单 | 人核对事实 | 低（事实少而稳） | 止损：从 spec 债中撤退的最小形态 |
| 最右 | TDD / 性质测试 | 隐含在可执行断言里 | CI / 测试运行器 | 最低（随代码同 PR 演化） | 测试基建成熟团队的行为锁定与回归 |

**光谱结论（5 句内）**：
1. 2026 年的批判没有杀死"先想清楚"，杀死的是"用不可验证的持久散文去承载它"——整条光谱的共同趋势是**把验证责任从文档迁给机器**（验证器、linter、CI、反馈回路）。
2. 光谱并非替换关系而是**分层叠加**：实践中最稳的组合是右半（context 纪律 + plan mode + 测试契约）做日常，左半只在契约清晰的大变更时按需上探。
3. 越靠右越抗漂移（无工件即无 spec 债），但表达力越低——"为什么这样设计"与跨服务语义契约只有左半能承载，这决定了重工件形态不会归零，只会收缩到值得它的场景。
4. Harness 治理是唯一同时吸收全部三条重批判（验证缺失、漂移留白、context tax）的形态，也是唯一有学术化（arXiv 2609.00252）与大厂一手（OpenAI）双重背书的中间路线，大概率是团队级的收敛点。
5. 对个人与小团队，2026 年的事实默认已经右移到"plan mode + AGENTS.md + 测试先行"；为每个 feature 维护 spec 工件链正在变成需要特别论证的重决策，而非默认动作。

---

## 7. 判断：哪条 alternative 最靠谱（2026-09-21，captain 判断 + 当日补查）

> 权威提示：本节判断对象 harness 治理现属 [../harness_governance/](../harness_governance/README.md)，本节保留为历史判断层；后续修订应回此处而非那边另起。

> **判断人与方法**：2026-09-21 由会话 captain 通读本目录全部分篇、8 份证据档案与 debate/ 综合后给出；另做两路当日网络补查（SSRN 论文 PDF 全文已回源并存档、IEEE 论文仅确认存在性）。本节是**判断层**，不复制分篇正文，证据细节一律回指分篇与档案；逐字引句仅限本次直接回源的新文献。

**结论：03 harness 治理派最靠谱。**"最靠谱"的准确含义有三层，比"团队级收敛点"更强：

**判据一：五条里唯一拿到受控因果证据。** 同一模型、只改执行链路 → 性能差数倍，三群独立得出、接力引用：SWE-Bench Mobile（KDD '26 同行评审，同模型跨 scaffold 最大 **6×**）、Stanford/MIT/KRAFTON Meta-Harness（独立复现，优化后 Haiku 4.5 登顶 TerminalBench-2）、清华 NLAH（消融显示外挂 verifier 模块反而有害，verifier −0.8 SWE-bench / −8.4 OSWorld——**基于 v1，v2 已换后端待复核**）。harness 是一级工程对象已从观点变成可测量事实。其余四条的证据形态全是叙事、采用率或群体辩论，无受控对照。→ 证据：[02a](../harness_governance/research/02a-harness-convergence-evidence.md)、[02b](../harness_governance/research/02b-harness-academic-and-metrics.md)。

**判据二：光谱不是五选一，是四个部分解 + 一个框架解，harness 是那个框架。** 逐条看四条"替代"路线的成熟形态：[01c](../harness_governance/research/01c-context-vs-harness.md) 已判定 **context ⊂ harness**（学术操作化 + CEO 表态 + 受控实验 + 多 practitioner 四层位独立同向，关系判定为最强）；01 的门禁落点（hooks/CI/command-fact/CodeLeash"门禁移出模型"）就是 harness 的 sensor 层；[03](03-test-first.md) Consort 的"agent 不可编辑的控制"（确定性编排器 + 不可变测试 + 真实分支绿灯）是 harness 手法对 TDD 的应用；[02](02-plan-mode.md) 的 `update_plan` opt-in（Codex PR #41744）与自动进入实验表明内置规划正在被 harness 化为可拆卸组件（本目录 02/03 按"对照"口径引用其机制事实，不引其主张）。四条路线没有一条以独立范式存活，全部长成了 harness 的部件——**赢家不是击败对手的那条，是吸收对手的那条**。

**判据三：即使具体处方有错，诊断也对（工程上最值钱的性质）。** 这条路线自己承认的未知都是结构性的：OpenAI 自认全 agent 生成系统的多年架构一致性如何演化"不知道"（原文自述，且原文 403 依赖双消化稿交叉）；清华消融证明机制堆叠有害（harness 自身也要打扫）；Böckeler 之问（harness 覆盖率怎么度量，[02b](../harness_governance/research/02b-harness-academic-and-metrics.md) §B）与 Ronacher 之塔（团队理解层腐烂无任何指标）仍是开放黑洞。它把"自己错了"变成输入的方式（每次犯错 → 工程化消灭该错误类别的棘轮 + 传感器），恰好就是它自己的解法——一条能自我纠错的路线才谈得上"靠谱"。

### 7.1 当日补查的新证据（2026-09-21，此前未收）

| 证据 | 内容 | 对判断的意义 | 强度 |
|---|---|---|---|
| [Does Spec-Driven Development Reduce Defects?](https://zenodo.org/records/19432099)（Brenn Hill，SSRN working paper，2026-04；[PDF](https://zenodo.org/records/19432099/files/ssrn-sdd-null-result.pdf) 全文已回源，本地存档已按 `.tmp-*` 纪律清理，PDF 见 zenodo 链接） | 119 个 OSS 仓库、88,052 个 PR（剔除 12,195 个 bot PR）、25,209 份 spec 工件，按 SDD 工具自己主张的质量维度打分、SZZ 回溯缺陷、同作者自对照 + 12 项稳健性检验（倾向得分匹配、复杂度分层、AI/人类分组）。**五条厂商质量主张全部不成立**：合并比较 spec'd PR 缺陷率反而更高（OR=1.20，作者归因 confounding by indication：越难的任务越写 spec）；同作者口径 +1.4pp（p=0.003）；spec 质量分数不能预测更少缺陷（p=0.164）或更少返工（p=0.860）；spec 不能约束 AI 代码范围（p=0.997）。唯一保护信号出现在**无 AI 采用**的仓库（返工更少，p=0.014）；AI 标记 PR 子样本内 spec 无效应（p=0.424/0.399）。关键句（逐字）："The specification tells the AI what to build. It does not tell the AI what it forgot to specify. **Direction is not quality.**"；"Specifications are, in effect, a lossy compression of code."。另一细节：对 100,247 个 PR 做 `.specify/`/`.speckit/`/`.kiro/`/spec-kit 文本检索**零匹配**——样本里没有一个仓库在用 SDD 工具链 | ①从批判面外部给 harness 治理（旧号 03，现属 [../harness_governance/research/02-harness-governance.md](../harness_governance/research/02-harness-governance.md)）补枪：质量不来自文档工件，来自验证回路——正是 harness 派核心命题；②同时是 01（裸 spec 不可验证）与 03 测试优先（旧号 05，表达力上限）的外部佐证，并支撑光谱整体右移的判断（真实 OSS 世界对 spec 工件链的采用为零）；③部分填上 debate/README §2.4"迄今没有任何独立量化生产率数据"的缺口（缺陷面、OSS 范围） | 中：独立研究者、大样本、同作者自对照可信；但 working paper、未预注册（作者自列）、基础 SZZ 误归因率 46–71%（作者自引 da Costa et al. 2017，且 spec'd PR 改动更大可能造成差分噪声）、测的是有机 spec 而非 SDD 工具产物、OSS 便利样本、多数 PR 早于 agentic 时代（5,989 个 AI 标记 PR 为最近似代理） |
| [Harness Engineering for AI Coding Agents: Emerging Practices and Principles](https://ieeexplore.ieee.org/document/11634633)（IEEE Xplore） | 存在性确认（2026-09-21 检索命中；页面 JS 渲染未取得正文） | harness engineering 已进入 IEEE 出版层，03 的学术化不止 arXiv 一条线 | 低（仅存在性，未回源正文；引用前必须先回源） |

### 7.2 二至五名的一句话排序

| 形态 | 排序理由 |
|---|---|
| 01 可验证 spec | **赔率最高的长期赌注，不是今天的答案。** 学术引擎五条最猛（RISC-V 全流程流片零人写 RTL、MakerDAO 等 23 个真实合约证明、Verus-SpecGym 前沿模型 77.8%），但工业级成功案例全部"人类垄断陈述层"、完整闭环无一例（[01b](01b-verifiable-academic.md) §4.3），意图没有 oracle（Lahiri：spec 正确性唯一 oracle 是用户本人）+ 不可判定性 + proxy 与生成器共同演化三重结构性障碍（[01b](01b-verifiable-academic.md) §6.3），产品层空白（六路调研：spec→测试编译器 0–118★、HN 零讨论、零商业化，且多数把 spec 当一次性燃料丢弃）。作为 2027+ 窄域赌注（合约/内核/解析器）看好，作为通用路线不成立 |
| 02 context engineering（现属 [../harness_governance/research/01-context-engineering.md](../harness_governance/research/01-context-engineering.md)） | **必要、最便宜、采用最广，但它是层不是范式。** [01c](../harness_governance/research/01c-context-vs-harness.md) 判定 context ⊂ harness；自身量化证据是"有用但不保证、写错倒赔"（CTXbench：LLM 自生成 context file 成功率 -2~3% 且成本 +20%+，手写仅边际 +4% 伴随成本 +19%；Umans：无一组配置完全匹配规则），且承载不了跨服务语义契约与"为什么"（[02](../harness_governance/research/01-context-engineering.md) §1.3/§4） |
| 03 测试优先（旧号 05） | **最有战斗力的组件，单独当范式有硬上限。** 测试是唯一骗不过的验证器（verify 与 define 合一），但表达力上限有 24 次重复实验：单轮基线 24/24 次只建 6/8 条规则、丢的总是同样两条钱规则，换最强模型照丢（[03](03-test-first.md) §4.1）——"测试无法在没人想到要写的那条规则上失败" |
| 02 plan mode（旧号 04） | **不是范式，是默认实践，且正被 harness 化。** 自动进入 plan mode 实验 + `update_plan` opt-in 表明内置规划正变成 harness 里可拆卸的 planning surface（[02](02-plan-mode.md) §4）——与本 README 开头"背景参照"的定性一致 |

### 7.3 本判断的局限（诚实声明）

- SSRN 论文为 working paper、未预注册，测的是 OSS 有机 spec 而非 SDD 工具产物——它支持"spec 工件 ≠ 质量"的批判面，**不能直接证明"任何 harness 配方有效"**；受控学术证据证明的是"harness 影响巨大"，不是"OpenAI 式配方就是对的配方"。
- 03 的旗舰案例（OpenAI 1500 PR / 1M 行）仍是自述、原文 403 依赖双消化稿交叉，1500 PR 的质量无独立验证；5–20 人团队级的公开 harness 治理案例仍缺位（[03](../harness_governance/research/02-harness-governance.md) §6-5），worldmonitor 自评 ~25% 是唯一半程样本。
- §7.2 对 01 的排序引用了 plan mode / 测试优先（本目录 02/03）的对照级材料的对照级证据（Smart 实验、update_plan 动向），按本 README 开头的研究优先级口径，这些只作对照不作主张依据。
- 本节为会话 captain 的独立判断，与光谱结论第 4 条同向但判据为其补充（受控因果证据 + 吸收结构 + 新实证），非替代；后续新证据若推翻 §7.1 任一条，应回到此节修订而非另起炉灶。
