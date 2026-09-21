# Requirements Engineering Final Report System Outline Package
> 状态：本轮已收口（completed / closed_for_current_round）。过程件仅作回溯，修改 final/ 勿据本文，以 final/ 现状为准。

> status: `structure_locked`
> last_updated: `2026-04-19`
> purpose: `Stage 2-3 详细大纲包；已把包级 thesis、读者路径、共享例子、00-06 七张 file cards 与 structure lock 决议固定下来`
> source_gate_context: `findings_reviewed`
> next_target_gate: `overview_and_main_ready`
> execution_surface: `final_drafting`
> drafting_permission: `yes`

## 0. 使用说明

这不是 reader-facing 文档，也不是正文草稿。

它的职责只有三个：

1. 固定整包交付的统一 thesis、读者路径、共享例子与边界 guardrails。
2. 为 `00/01/02/03/04/05/06` 七个最终文件提供可扩展的 file card 骨架。
3. 为后续 `Stage 3` 的 structure lock review 提供 review ledger 落点。

在当前阶段：

- 允许继续把 file cards 扩展到 review-ready 细度。
- 不允许把这里的段落直接当成 `final/` 正文。
- 不允许跳过本文件直接开始写 `requirements_engineering/final/*.md`。

## 1. Package Frame

### 1.1 Approved File Set

当前批准的最终交付文件集合固定为：

- `00-report-system-overview.md`
- `01-main-guide.md`
- `02-pm-guide.md`
- `03-spec-architecture-guide.md`
- `04-user-story-examples.md`
- `05-ears-examples.md`
- `06-reference-appendix.md`

当前包级产出顺序固定为：

`00 -> 01 -> 02 -> 04/05 -> 03 -> 06`

### 1.2 Unified Thesis Ledger

本包统一主线固定为：

> AI 时代的需求工程，不是在 User Story、EARS、BDD、Agent Spec 之间选一个赢家，而是在更高层次上重组一套分层、可追溯、可执行的需求表达体系。

所有正文文件都必须与下面五层口径对齐：

| layer | 中文名称 | 核心职责 | 默认主工件 |
| --- | --- | --- | --- |
| `L1` | 意图层 | 说明为什么做、给谁做、价值是什么 | Story / PRD / Story Map |
| `L2` | 行为契约层 | 说明系统在什么条件下必须做什么 | EARS / structured requirements |
| `L3` | 确认与验证层 | 说明如何证明需求被满足 | Examples / Gherkin / tests |
| `L4` | 执行与工作流层 | 说明 agent 和团队如何拿这些信息工作 | `AGENTS.md` / scoped rules / `spec-plan-tasks` |
| `L5` | 治理与追溯层 | 说明如何审查、追踪、合规和变更管理 | 29148 / GtWR / traceability / review workflow |

全包必须稳定复用的判断包括：

- `User Story` 是意图与对话层，不是完整合同。
- `EARS` 是强行为契约层，但不是万能格式。
- `Examples / Gherkin` 是确认层，不是需求本体替身。
- `AGENTS.md / CLAUDE.md / rules` 适合短 team/repo contract，不适合塞 feature 细节。
- `spec / plan / tasks` 代表 feature-level 可执行工作包组织。
- 治理与审计压力提升了结构化、可追踪规格的价值，但不等于所有团队都该一夜之间形式化升级。

### 1.3 Cross-Doc Reader Routes

| reader | first stop | second stop | third stop | optional deepening | success target |
| --- | --- | --- | --- | --- | --- |
| 工程师 / Tech Lead | `00` | `01` | `04/05` | `03`, `06` | 理解五层结构，并能解释工件如何组合 |
| 传统 PM / 产品负责人 | `00` | `02` | `04` | `05`, `01` | 把 PRD / Story / AC 升级成更可执行表达 |
| PM + 架构师 / 系统负责人 | `00` | `01` | `03` | `05`, `06` | 能把轻量需求推进成规格、验证与工作流 |
| 技术管理者 / 平台治理负责人 | `00` | `01` | `03` | `06` | 看懂最小可行推进顺序与治理边界 |

时间预算口径在 `00` 中固定为：

- `15 分钟`：先看 `00`
- `45-60 分钟`：`00 + 01` 或 `00 + 02`
- `半天`：按角色路径读 `00 + 目标主文档 + 对应示例手册`

### 1.4 Shared Example Map

| example | role in package | primary files | usage policy |
| --- | --- | --- | --- |
| `Example A: 手机银行主屏余额` | 低门槛贯穿主例子 | `01`, `02`, `04`, `05`，必要时在 `03` 简短回指 | 用来展示 Story -> AC/Examples -> EARS 的层间切换；保持表述简洁，不让例子淹没主线 |
| `Example B: 自动紧急制动（AEB）` | 高风险 / 高合规深例子 | `03`, `05`, `06` | 用来展示为什么轻量工件不够、为何需要契约、决策边界、验证链和治理锚点 |
| `Micro Examples: 登录态、异常、性能、安全、配置、规则组合` | 训练层补位样例池 | `04`, `05` | 只在示例手册高密度使用，不进入 `01/02` 主叙事 |

例子分配规则固定为：

- `01/02/03` 只保留少量贯穿或高价值 worked example。
- `04/05` 承担高密度正例、反例、重构与验法训练。
- `06` 不新增正文教学例子，只收术语、映射和可信参考。

### 1.5 Shared Terminology Ledger

| term | preferred wording | note |
| --- | --- | --- |
| `User Story` | `用户故事（User Story）` | 首次出现时明确它是意图/对话层 |
| `Acceptance Criteria` | `验收标准（Acceptance Criteria, AC）` | 与 Story 分开解释，不混写成 Story 模板一部分 |
| `Examples` | `示例 / 例子（Examples）` | 默认指可用于确认的具体例子 |
| `BDD / Gherkin` | `行为驱动开发 / Gherkin 场景` | 统一放在确认与验证层讨论 |
| `EARS` | `EARS 受控自然语言需求写法` | 明确是行为契约层，不是唯一规范形式 |
| `Agent context file` | `agent 上下文文件` | 指 `AGENTS.md`、`CLAUDE.md`、rules 等 team/repo 级说明 |
| `feature workflow` | `feature 级规格工作流` | 指 `spec / plan / tasks`、`requirements / design / tasks` 一类工件链 |
| `traceability` | `可追溯性（traceability）` | 统一放在治理与追溯层 |

### 1.6 Boundary Guardrails

所有 file cards 都必须遵守下面边界：

- 不制造“某一种格式统治一切”的错觉。
- 不把 `Story` 写成完整规格。
- 不把 `EARS` 写成复杂决策逻辑的唯一容器。
- 不把 `Gherkin` 或测试场景写成需求本体。
- 不把 `AGENTS.md` 或 rules 写成 feature 细节仓库。
- 不把 `06` 写成理解正文的前提。
- 不把研究执行痕迹带入 reader-facing 文档，包括 `topic-*`、`wave`、`round`、`W2`、`claims audit` 等标签。
- 涉及标准和官方锚点时，必须显式保留 `full-text-pending` 风险边界，不做逐条条文断言。

### 1.7 Cross-Doc Visual Policy

整包应优先准备下列高价值视觉化表达：

- 一张五层需求表达体系图，服务 `01`
- 一张工件职责对照表，服务 `01/02/03`
- 一张升级条件 / 选择边界表，服务 `01/02/03`
- 一张读者路径与阅读顺序表，服务 `00`
- 一组坏例 -> 好例并排对照块，服务 `04/05`
- 一张 `Story / EARS / decision table / Gherkin / agent files` 的边界表，服务 `03`

### 1.8 Cross-Doc Example Density and Handoff Rules

为避免 `02` 与 `04/05`、`03` 与训练层重新重叠，整包固定采用下面的例子密度规则：

- `00`
  不做教学例子，只点名两条贯穿例子的用途。
- `01`
  只保留 `Example A` 这一条主例子，用来解释五层之间如何分工；其他例子只点到为止。
- `02`
  只允许保留：
  - `1` 条端到端示范，默认就是 `Example A`
  - 每个核心概念最多 `1` 组简短 mini bad -> better 对照
  - 不建立分类样例库，不做高密度连续练习
- `04`
  承担 Story 与 AC / Examples 的主训练面；可以有分类样例库、成组重构和连续坏例。
- `05`
  承担 EARS 与 decision boundary 的主训练面；可以有五模式库、退出判据库和成组重构。
- `03`
  只保留 `1` 条低门槛轻例 + `1` 条高风险深例 + `1` 个 compact workflow 例子；
  不扩张为第三本训练册。
- `06`
  不承载教学例子，只承载术语、映射、外部可信入口和风险标签。

跨文档交接口径固定为：

- `02 -> 04`
  当读者需要连续看正反例和重构练习时，交给 `04`。
- `02 -> 05`
  当读者已经遇到“Story / AC 不够、需要契约化”时，交给 `05`。
- `01 -> 03`
  当读者问“什么时候必须升级为更严格规格和工作流”时，交给 `03`。
- `03 -> 06`
  当读者需要查标准、工具、术语和来源锚点时，交给 `06`。

### 1.9 Standards and Risk-Label Policy

整包对标准、工具成熟度和证据边界统一采用下面口径：

- `01/02`
  只讲结构性结论，不做条文级标准陈述。
- `03`
  可以使用标准和工具作为定位锚点，但必须显式提醒：
  - `29148` 是 scope / catalog 级锚点，不做 clause-by-clause 断言
  - `GtWR` 是官方 presentation / summary 级锚点，逐条映射仍保留 `full-text-pending`
  - `SysML v2` 只作为 model-layer 定位锚点，不把 `03` 扩成 MBSE 教材
- `06`
  承担正式风险标签和进一步阅读入口的收口，不反过来承担正文解释。

## 2. File Cards

### 2.1 `00-report-system-overview.md`

- `file_role`:
  整包导读层；在最短时间内告诉不同读者“这套报告怎么读、先看什么、每个文件负责什么”。
- `primary_reader`:
  所有读者，尤其是第一次接触整包的工程师、PM、技术管理者。
- `reader_problem_to_solve`:
  我只有很少时间，如何快速知道这套包的价值、阅读顺序与与我相关的部分。
- `must_cover`:
  - 这套报告系统解决什么问题
  - 按读者角色划分的阅读路径
  - 全文件地图与每个文件的一句话职责
  - 建议阅读顺序与时间预算
  - 示例手册与附录如何配合使用
  - “如果只看一份先看什么”的压缩建议
- `must_not_cover`:
  - 不能膨胀成 `01` 的摘要替代品
  - 不能在这里展开大量方法论教学
  - 不能依赖读者补读 `topic-*` 才能看懂路径
- `section_skeleton`:
  1. 这套报告系统解决什么问题
  2. 先看一张包级地图
  3. 按读者角色选择阅读路径
  4. 按时间预算选择阅读顺序
  5. 七个文件分别负责什么
  6. 示例手册和附录怎么用
  7. 如果时间有限先看什么
- `section_detail_notes`:
  - `1`
    用两段以内解释“为什么这不是一份大全，而是一套分工清楚的包”。
  - `2`
    用一张文件地图表或 Mermaid，把 `00-06` 的层次关系直接讲清。
  - `3`
    按四类读者给出 first stop / next stop / optional deepening。
  - `4`
    给 `15 分钟 / 1 小时 / 半天` 三档阅读方案；不需要更细。
  - `5`
    每个文件只写一句职责和一句“不负责什么”。
  - `6`
    解释 `04/05` 是训练层，`06` 是支撑层，不能替代主文档。
  - `7`
    为时间极少的读者给一个最短入口。
- `worked_examples_or_example_policy`:
  不展开 worked example；只允许用一句话点名 `Example A` 和 `Example B` 的分工。
- `drafting_watchouts`:
  - 不把 `00` 写成 `01` 的摘要版
  - 不让读者必须理解五层全部细节才能开始阅读
  - 不展开研究材料来源历史
- `required_visuals_or_tables`:
  - 读者角色 -> 推荐阅读路径表
  - 时间预算 -> 阅读顺序表
  - 00-06 文件职责地图表
- `cross_doc_dependencies`:
  依赖 `01/02/03/04/05/06` 的一句话职责稳定后再精修；但骨架阶段先锁定默认读者路径。
- `self_contained_notes`:
  即使读者只看这一份，也应能理解为什么交付被拆成 7 个文件，而不是一份大全。

### 2.2 `01-main-guide.md`

- `file_role`:
  主叙事文档；建立整套分层需求表达体系的共享心智模型。
- `primary_reader`:
  工程师 / Tech Lead / Staff Engineer；PM 与技术管理者也应能顺读。
- `reader_problem_to_solve`:
  AI 时代需求工程到底改变了什么，为什么不能再把 Story、EARS、BDD、Agent 文件混成一团。
- `must_cover`:
  - 为什么 AI 时代要重新理解需求工程
  - 五层结构总图
  - Story / EARS / Examples / Agent Workflow / Governance 的角色划分
  - 从模糊意图推进到可执行工作包的路径
  - `Example A` 的贯穿式讲解
  - 什么时候需要升级到更严格的规格
  - 为什么 AI coding workflow 改变了需求写法
  - 团队落地的最小可行路径
  - 常见误区与边界提醒
- `must_not_cover`:
  - 不做高密度例子库
  - 不做条文级标准综述
  - 不把 `03` 的深规格细节提前搬进来
  - 不把 `04/05` 的训练任务吞进正文
- `section_skeleton`:
  1. 为什么 AI 时代要重新理解需求工程
  2. 一张图看懂五层分层表达体系
  3. 几种核心工件分别解决什么问题
  4. 从意图到契约、验证与执行工作流
  5. `Example A: 手机银行主屏余额` 的分层改写
  6. 什么时候该升级到更严格的规格
  7. AI coding workflow 为什么放大了输入质量问题
  8. 团队最小可行推进路径
  9. 常见误区
  10. 结论
- `section_detail_notes`:
  - `1`
    把问题从“要不要写需求文档”改写成“怎样让需求同时对人和 agent 有用”。
  - `2`
    用五层图先给读者一个稳定地图；避免一开始就在 Story / EARS 之间做辩论。
  - `3`
    明确区分 Story、EARS、Examples/Gherkin、agent context files、feature workflow、governance。
  - `4`
    讲清从 why -> contract -> confirmation -> work package 的推进链。
  - `5`
    用 `Example A` 演示同一需求如何在不同层次被不同工件承载。
  - `6`
    给出升级触发条件：
    复杂条件、NFR、异常路径、合规压力、多团队协作、agent-heavy execution。
  - `7`
    解释为什么短 team/repo context 不能替代 feature-level spec。
  - `8`
    给一个务实顺序：先分清工件职责，再加 selective EARS，再加 examples/tests，再加 feature workflow。
  - `9`
    集中拆解银弹幻觉和格式滥用。
  - `10`
    回到统一 thesis，不做空洞总结。
- `worked_examples_or_example_policy`:
  以 `Example A` 为唯一主例子；其他例子只允许点到为止，用来解释边界而不是扩张样例密度。
- `drafting_watchouts`:
  - 不把 `01` 写成技术管理白皮书
  - 不让 `03` 的复杂内容提前挤爆主线
  - 不用大量 bullet 代替解释性段落
- `required_visuals_or_tables`:
  - 五层体系图
  - 工件职责对照表
  - 升级条件表
  - 团队最小推进顺序图
- `cross_doc_dependencies`:
  为 `02/03/04/05` 提供统一口径；需与 `06` 的术语、风险标签保持一致。
- `self_contained_notes`:
  不得依赖 `04/05/06` 才能理解五层结构；引用训练手册时必须让正文单独成立。

### 2.3 `02-pm-guide.md`

- `file_role`:
  PM 迁移文档；把传统 PM 熟悉的 PRD / Story / AC 写法，迁移到 AI 时代更分层的表达体系。
- `primary_reader`:
  传统 PM / 产品负责人。
- `reader_problem_to_solve`:
  如果我已经会写 PRD、Story、AC，应该怎样升级，而不是被新术语直接替代。
- `must_cover`:
  - 给传统 PM 的起点与迁移逻辑
  - PRD、Story、AC、Examples、EARS 各自负责什么
  - 怎样写出有用的 User Story
  - 怎样写出可工作的 AC 与 examples
  - 什么时候需要升级到 EARS 或更强规格
  - PM 与工程、测试、架构师、agent 的接口
  - 常见文档反模式
  - 一个端到端示范
  - PM 的最小方法包
- `must_not_cover`:
  - 不进入深度架构或 traceability 细节
  - 不承担高密度句型训练册职责
  - 不把 EARS 讲成所有 PM 都必须精通的唯一形式
- `section_skeleton`:
  1. 给传统 PM 的起点
  2. PRD、Story、AC 到底各自负责什么
  3. 怎样写出有用的 User Story
  4. 怎样写出可工作的 AC 与 Examples
  5. 什么时候需要 EARS 或更强规格表达
  6. PM 如何与工程师、测试、架构师、agent 协作
  7. 常见文档反模式
  8. `Example A` 的端到端示范
  9. PM 的最小方法包
- `section_detail_notes`:
  - `1`
    先承认 PM 现有写法有价值，再解释为什么 AI 时代需要更明确的分层。
  - `2`
    把 PRD、Story、AC、Examples、EARS 放到同一流程图里，不让它们继续抢一个位置。
  - `3`
    讲 Story 的职责：对齐角色、结果和价值，不装作完整规格。
  - `4`
    讲 AC / Examples 如何承接 Story 留白，而不是把细节继续塞回 Story。
  - `5`
    明确升级信号：规则复杂、NFR 明确、异常路径多、合规和接口边界上升。
  - `6`
    重点讲接口，不展开 agent runtime 机制。
  - `7`
    反模式以“为什么它会误导工程和 agent”为主轴。
  - `8`
    用 `Example A` 把 Story -> AC -> selective EARS -> tasks 串起来。
  - `9`
    收束为一个 PM 最小方法包，而不是理论回顾。
- `worked_examples_or_example_policy`:
  只保留少量示范性写法，以 `Example A` 为主；坏例/好例重构和批量例子外移到 `04/05`。
- `example_density_red_lines`:
  - 不超过 `1` 条完整端到端示范
  - 每个核心概念最多 `1` 个微型改写对照
  - 不建立“按场景分类的连续例子池”
  - 不把 `02` 写成练习册或参考手册
- `drafting_watchouts`:
  - 一旦开始连续展示多个坏例 / 好例，就应回切到 `04/05`
  - 一旦开始讲 decision table / traceability / agent workflow 细节，就应回切到 `03`
- `required_visuals_or_tables`:
  - PRD / Story / AC / EARS / Examples 角色分工表
  - PM 升级触发条件表
  - PM 与工程/测试/架构/agent 接口表
  - 常见反模式对照表
- `cross_doc_dependencies`:
  依赖 `01` 的统一工件分层口径；需与 `04/05` 显式切清“示范性写法”与“训练册”的边界。
- `self_contained_notes`:
  即使不读 `04/05`，PM 也应能看懂什么时候该升级写法；但如果要练手，文中应给出可选阅读指向。

### 2.4 `03-spec-architecture-guide.md`

- `file_role`:
  深度规格与架构文档；把需求表达推进到架构、验证、工作流和治理层。
- `primary_reader`:
  PM + 架构师 / 系统负责人；工程负责人和技术管理者可选读。
- `reader_problem_to_solve`:
  当需求进入复杂条件、合规、NFR、多团队协作或 agent-heavy workflow 时，应该怎样从轻量工件升级到更严格规格。
- `must_cover`:
  - 为什么高级需求表达会进入规格与架构问题
  - 规格分层总图与 traceability 链
  - EARS 的适用边界与退出判据
  - 复杂条件、decision table、DMN、状态建模的接口
  - 从需求到架构约束的转换
  - BDD / Gherkin 在验证层的正确位置
  - agent 工作流中的规格组织
  - traceability、治理与标准锚点
  - `Example A` 的轻例回指与 `Example B` 的深例讲解
  - 高级反模式与失败模式
  - 升级路线
- `must_not_cover`:
  - 不退化成纯标准综述
  - 不变成 topic 拼盘
  - 不承担大规模句型训练册职责
  - 不把 appendix 写进正文
- `section_skeleton`:
  1. 为什么高级需求表达一定会进入规格与架构问题
  2. 规格分层总图与可追溯链条
  3. EARS 作为行为契约层的适用边界
  4. 复杂条件、决策逻辑与状态建模
  5. 从需求到架构约束
  6. BDD / Gherkin / Examples 在验证层的正确位置
  7. Agent 工作流中的规格组织
  8. Traceability、治理与标准锚点
  9. `Example B: AEB` 的深度 worked example
  10. 高级反模式与失败模式
  11. 结论与升级路线
- `section_detail_notes`:
  - `1`
    把问题从“写得更严谨”推进为“如何让需求、架构、验证和执行组织起来”。
  - `2`
    给出 textual layers + feature workflow + governance 的一张总图。
    在本节插入一个很短的 `model-layer positioning sidebar`：
    `SysML v2 / model layer` 只用于说明文本规格之上还可能有模型层，不展开成 MBSE 教材。
  - `3`
    讲 EARS 能做什么，不能做什么，何时退出。
  - `4`
    把复杂组合逻辑明确交给 decision table / DMN / state model，而不是继续往 EARS 里塞。
  - `5`
    解释需求如何外溢成接口约束、性能约束、异常和部署边界。
  - `6`
    把 Gherkin 放回确认层，强调它不是上游 discovery 和 contract 的替代。
  - `7`
    给出短 `AGENTS.md` + feature `spec / plan / tasks` 的组织示意。
  - `8`
    用标准和治理锚点帮助读者知道为什么需要追溯和审查，但避免条文化。
  - `9`
    让 `Example B` 负责高风险和高合规压力，必要时用半页 parallel micro example 帮助纯软件读者进入。
  - `10`
    把 clause overload、decision logic 混层、context bloat、traceability 空挂名等失败模式拆开讲。
  - `11`
    收束为升级路线，而不是再做一次总论。
- `worked_examples_or_example_policy`:
  保留一个低门槛轻例子回指 `Example A`，一个高风险深例子 `Example B`；不再扩张成第三本训练册。
- `model_layer_policy`:
  在 `Section 2` 放一个短侧栏即可：
  - 允许说明 `SysML v2` 代表模型层的存在与定位价值
  - 不允许展开工具比较、语法教学或 MBSE 流程教程
  - 如需来源或延伸阅读，一律下沉到 `06`
- `drafting_watchouts`:
  - 一旦开始长篇讲标准背景，应缩回到“为什么这对规格和治理有用”
  - 一旦例子密度升高到训练册水平，应回切到 `05`
- `required_visuals_or_tables`:
  - 规格分层与 traceability 图
  - `Story / EARS / decision table / DMN / Gherkin / agent files` 边界表
  - feature-level `spec / plan / tasks` 组织图
  - 升级条件与退出判据表
- `cross_doc_dependencies`:
  依赖 `01` 的五层口径、`05` 的 EARS 训练边界、`06` 的标准与工具映射标签。
- `self_contained_notes`:
  即使读者不看 `06`，也应能理解为什么需要治理和标准锚点；附录只补出处与延伸阅读，不承担核心解释。

### 2.5 `04-user-story-examples.md`

- `file_role`:
  User Story 训练手册；通过高密度例子教读者怎么写、怎么验、怎么重构。
- `primary_reader`:
  PM、工程师、Tech Lead。
- `reader_problem_to_solve`:
  我已经理解 Story 的定位，但还不会判断自己写得好不好，也不会稳定重构坏例。
- `must_cover`:
  - 这份手册怎么用
  - 一套最小判断尺子
  - 典型正例
  - 典型坏例
  - 坏例到好例的重构对照
  - Story 与 AC / Examples 的分界示例
  - 快速自检方法
  - “怎么验写得是否足够好”
  - 按场景分类的样例库
- `must_not_cover`:
  - 不重复 `01/02` 的大段概念叙事
  - 不扩张成完整 BDD 教材
  - 不替代 `02` 的迁移说明文
- `section_skeleton`:
  1. 这份手册怎么用
  2. 最小判断尺子
  3. 典型正例
  4. 典型坏例
  5. 坏例 -> 好例重构对照
  6. Story 与 AC / Examples 的分界示例
  7. 怎么快速自检
  8. 怎么验写得是否足够好
  9. 按场景分类的样例库
  10. 结尾：先写对，再写多
- `section_detail_notes`:
  - `1`
    用极短篇幅解释 Story 在整套体系中是意图层，不要求读者先补读 `01/02`。
  - `2`
    判断尺子固定围绕角色、结果、价值、边界、可协商性、可验证性。
  - `3`
    正例优先短小，让读者先形成手感。
  - `4`
    坏例类型至少覆盖：伪规格、角色错位、NFR 硬塞、价值空泛、技术任务伪装成 Story。
  - `5`
    重构对照以“小步修改 + 为什么更好”为主。
  - `6`
    明确 Story 留什么，AC / Examples 接什么。
  - `7`
    自检应足够轻量，适合写完即扫一遍。
  - `8`
    “怎么验”从协作、实现输入、测试可行性三侧检视。
  - `9`
    样例库至少按产品功能、平台/API、异常、NFR、探索型需求分类。
  - `10`
    结尾强调先写对，再追求覆盖更多场景。
- `drafting_watchouts`:
  - 训练层开头必须重新交代位置，不能假定读者读过 `02`
  - 不把 AC / Gherkin 的理论边界讲成大段方法论
- `worked_examples_or_example_policy`:
  `Example A` 作为主训练样例；再补登录态、异常、NFR、平台/API、探索型需求等 micro examples。
- `required_visuals_or_tables`:
  - Story 质量尺子表
  - 坏例 -> 好例并排对照块
  - Story 与 AC / Examples 边界表
  - 场景分类导航表
- `cross_doc_dependencies`:
  与 `02` 对齐 Story / AC 边界；与 `01` 对齐 Story 只是意图层的判断；必要时向 `05` 交接到验证层接口。
- `self_contained_notes`:
  即使读者没先看 `01/02`，也要在开头用极短篇幅解释 Story 在整套体系中的位置。

### 2.6 `05-ears-examples.md`

- `file_role`:
  EARS 训练手册；通过模式、边界、反例和重构，教读者写稳行为契约。
- `primary_reader`:
  工程师、架构师、Tech Lead、需要升级规格表达的 PM。
- `reader_problem_to_solve`:
  我理解 EARS 是什么，但不会稳写，也不知道什么时候该停止写 EARS 转去 decision table / DMN / state model。
- `must_cover`:
  - 这份手册怎么用
  - 一套最小判断尺子
  - 五种核心模式的正例
  - 复合模式的正确写法
  - 典型坏例
  - 坏例到好例的重构对照
  - 快速自检方法
  - “怎么验写得是否足够好”
  - 什么时候不要继续写 EARS
  - 按模式与场景分类的样例库
- `must_not_cover`:
  - 不扩张成 DMN 教材
  - 不代替 `03` 的规格分层叙事
  - 不把所有复杂规则硬塞回一句 EARS
- `section_skeleton`:
  1. 这份手册怎么用
  2. 最小判断尺子
  3. 五种核心模式的正例
  4. 复合模式的正确写法
  5. 典型坏例
  6. 坏例 -> 好例重构对照
  7. 怎么快速自检
  8. 怎么验写得是否足够好
  9. 什么时候不要继续写 EARS
  10. 按模式与场景分类的样例库
  11. 结尾：先写稳，再写复杂
- `section_detail_notes`:
  - `1`
    用极短篇幅解释 EARS 在整套体系中是行为契约层。
  - `2`
    判断尺子围绕主语清楚、触发清楚、响应可测、原子性、不过载。
  - `3`
    五模式正例先用短句建立基本手感。
  - `4`
    复合模式重点讲“何时组合，何时不该组合”。
  - `5`
    坏例类型至少覆盖形容词堆砌、主语漂移、多条件过载、把规则网塞进一句。
  - `6`
    重构对照要让读者看到从自然语言走向可测契约的过程。
  - `7`
    自检强调是否可测、是否原子、是否触发和响应边界清晰。
  - `8`
    验法从测试、架构审查、agent 输入可用性三侧展开。
  - `9`
    退出判据必须写得比“复杂了就别写”更具体，例如：
    `>3` 前置条件、复杂逻辑组合、公式/表驱动规则、状态爆炸。
  - `10`
    样例库至少按模式、性能、安全、异常、配置、规则边界分类。
  - `11`
    结尾强调会停笔比会继续写更重要。
- `drafting_watchouts`:
  - 不把 decision table / DMN 教成完整课程
  - 不为了“结构化”而牺牲可读性
- `worked_examples_or_example_policy`:
  `Example A` 用于低门槛教学，`Example B` 用于展示高风险场景；同时补性能、安全、异常、配置、规则边界类 micro examples。
- `required_visuals_or_tables`:
  - 五模式模板表
  - 退出 EARS -> 转向 decision table / DMN / state model 的判据表
  - 坏例 -> 好例重构对照块
  - 测试/架构/agent 输入检查表
- `cross_doc_dependencies`:
  与 `03` 对齐 EARS 的边界与退出判据；与 `01` 对齐“EARS 是契约层但不是万能格式”的主判断。
- `self_contained_notes`:
  即使读者不读 `03`，也要在文中独立解释何时停用 EARS，并给出至少一套进入 decision logic 层的清晰信号。

### 2.7 `06-reference-appendix.md`

- `file_role`:
  支撑附录层；整理术语、外部可信 URL、标准/工具映射与证据边界说明。
- `primary_reader`:
  想回查术语、外部来源或标准/工具映射的所有读者；尤其是架构师和技术管理者。
- `reader_problem_to_solve`:
  我想知道关键术语怎么定义、有哪些可信外部入口、标准与工具之间怎样映射，但我不想让附录绑架正文理解。
- `must_cover`:
  - 关键术语表
  - 外部可信 URL 清单
  - 标准与工具映射表
  - 证据分级与表达边界说明
  - 正文未展开但适合延伸阅读的入口
- `must_not_cover`:
  - 不承担正文教学职责
  - 不把内部本地路径暴露为对外参考
  - 不靠“更多链接”替代正文解释
- `section_skeleton`:
  1. 关键术语表
  2. 外部可信 URL 清单
  3. 标准与工具映射表
  4. 证据分级与表达边界说明
  5. 进一步阅读入口
- `section_detail_notes`:
  - `1`
    术语表只收正文高频概念，不做百科。
  - `2`
    URL 清单按标准、方法论、工具、进一步阅读分组。
  - `3`
    映射表要回答“哪个锚点支持哪一层工件或治理活动”。
  - `4`
    把 `supported inference`、`trend signal`、`full-text-pending` 一类边界用自然中文讲清。
  - `5`
    延伸阅读入口只做精选，不堆链接。
- `drafting_watchouts`:
  - 不把本地文件路径暴露为面向最终读者的引用
  - 不让附录变成正文逻辑的必经之路
- `worked_examples_or_example_policy`:
  不承载 worked example；只允许在标准/工具映射表中引用 `Example B` 所需的治理锚点说明。
- `required_visuals_or_tables`:
  - 术语表
  - 标准 -> 工件 -> 团队实践映射表
  - 工具/工作流类型对照表
  - 风险标签与表述边界表
- `cross_doc_dependencies`:
  依赖 `01/03` 的标准、治理、工作流锚点口径；依赖整包 terminology ledger 稳定后再精修。
- `self_contained_notes`:
  必须明确声明“附录增强可信度，但不是理解前三层主文档和两份示例手册的前提”。

## 3. Review Ledger

### 3.1 Disposition Ledger

| id | question | affects | disposition | blocking_for_structure_lock | final decision |
| --- | --- | --- | --- | --- | --- |
| `RL-01` | `02` 中“示范性写法”的密度上限如何具体表述，才能彻底避免和 `04/05` 重叠 | `02`, `04`, `05` | `fixed_now` | `no` | `02` 只保留 `1` 条端到端示范与每个核心概念最多 `1` 组 mini 对照；连续训练例子、分类样例库与高密度重构全部下沉到 `04/05` |
| `RL-02` | `03` 是否需要在正文中加入一个非常短的 SysML v2 / model-layer 定位侧栏，还是仅保留在治理锚点中点到为止 | `03`, `06` | `fixed_now` | `no` | `03` 在 `Section 2` 放一个极短 model-layer positioning sidebar；只做定位，不展开 MBSE 教学；来源和延伸阅读全部留给 `06` |
| `RL-03` | `Example B` 目前锁定为 `AEB`；是否还需要一个软件更贴近的高风险平行微例子，帮助通用软件读者进入 | `03`, `05` | `accepted_for_now` | `no` | 结构锁定阶段不强制新增第二条高风险主例子；允许在 drafting 时酌情加半页 parallel micro example，但不改变文件职责边界 |
| `RL-04` | `00` 的时间预算是否需要细分到“45 分钟 PM 路径 / 45 分钟工程路径”两个单独版本 | `00` | `accepted_for_now` | `no` | 先保持 `15 分钟 / 45-60 分钟 / 半天` 三档通用预算；如 drafting 时发现读者路径仍不够清晰，再做当前文件内 minor fix，不触发重开 |

### 3.2 Structure Lock Note

- `ready_for_structure_review`: `yes`
- `structure_lock_passed`: `yes`
- `structure_lock_reason`:
  `七张 file cards 已扩展到 review-ready 粒度，reader route、shared terminology、example policy、标准与风险标签口径已对齐；所有阻塞 structure lock 的问题都已完成 disposition。`
- `locked_decisions`:
  - `00/01/02/03/04/05/06` 文件集合冻结，不新增第八个 reader-facing 文件
  - `02` 的示范性写法密度红线冻结，不承担训练册职责
  - `03` 的 model-layer / SysML v2 只保留短侧栏定位，不展开 MBSE 教学
  - `Example A = 手机银行主屏余额`，`Example B = AEB` 的包级分工冻结
  - `04/05` 分别承担 Story 与 EARS 的主训练面，`03` 只保留高价值高级例子
- `allowed_post_lock_changes_without_reopen`:
  - wording 打磨
  - 微调章节标题
  - minor visual reordering
  - 在不改变职责边界前提下补半页 parallel micro example
- `changes_that_require_reopen`:
  - 新增或删除 reader-facing 文件
  - 改变 `02` 与 `04/05` 的职责边界
  - 让 `03` 扩张为 MBSE / DMN 教材
  - 让 `06` 承担正文教学职责
