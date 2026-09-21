# Requirements Engineering Final Report System Plan
> 状态：本轮已收口（completed / closed_for_current_round）。过程件仅作回溯，修改 final/ 勿据本文，以 final/ 现状为准。

> plan_status: `design_sor_active`
> last_updated: `2026-04-19`
> scope: `把 requirements_engineering 现有 deep research 材料收束成一套面向工程师、PM、技术管理者的自包含报告系统`
> output_dir: `requirements_engineering/final/`
> primary_constraint: `最终读者不需要访问本仓库中的 topics / _artifacts / _reference，也能完整理解报告内容`
> status_path: `requirements_engineering/plan/final-report-system.status.md`
> queue_path: `requirements_engineering/plan/final-report-system.queue.md`
> outline_package_path: `requirements_engineering/plan/final-report-system.outline-package.md`
> live_runtime_state: `以 STATUS_PATH + QUEUE_PATH 为准`

## 0. Progressive Control Map

这不是一次性短任务，而是一项可能中途暂停、多次恢复的长程任务。

因此，这份文件不能只承担“结构设计稿”的角色，还必须成为 progressive execution system 的设计态 Source of Record。

### 0.1 Runtime Bindings

| field | value |
| --- | --- |
| `plan_path` | `requirements_engineering/plan/final-report-system.plan.md` |
| `status_path` | `requirements_engineering/plan/final-report-system.status.md` |
| `queue_path` | `requirements_engineering/plan/final-report-system.queue.md` |
| `outline_package_path` | `requirements_engineering/plan/final-report-system.outline-package.md` |
| `final_output_dir` | `requirements_engineering/final/` |
| `execution_model` | `progressive / interruptible / resumable` |

### 0.2 Source-of-Record Split

- `PLAN_PATH`
  只记录稳定的设计态蓝图、输出结构、文档职责、阶段定义、gate 设计与验收规则；不维护 live current_task。
- `STATUS_PATH`
  只记录运行态状态、当前 gate、当前 execution surface、已完成里程碑、开放问题、恢复上下文与 worklog。
- `QUEUE_PATH`
  只记录连续动作顺序、当前任务、下一任务、补位任务与完成判据；它与 `STATUS_PATH` 一起构成 live recovery pair。
- `OUTLINE_PACKAGE_PATH`
  只承载正式进入 drafting 前的详细大纲包，不替代 plan / status / queue。

### 0.3 Progressive Gate Path

默认 gate 路径锁定为：

`progressive_plan_ready -> findings_reviewed -> outline_package_ready -> structure_locked -> overview_and_main_ready -> pm_guide_ready -> example_guides_ready -> deep_guide_ready -> appendix_ready -> package_polish_ready -> final_review_passed`

说明：

- `progressive_plan_ready`
  表示本计划已经具备长程执行能力，`status` 与 `queue` 已建立。
- `findings_reviewed`
  表示当前已识别的结构性问题都已做出 disposition：修复、接受、或显式 defer。
- `outline_package_ready`
  表示详细大纲包已经落地，可供 review。
- `structure_locked`
  表示包级结构已冻结，正式进入 drafting。
- `overview_and_main_ready`
  表示 `00` 与 `01` 已完成第一轮成文。
- `pm_guide_ready`
  表示 `02` 已完成第一轮成文。
- `example_guides_ready`
  表示 `04` 与 `05` 已完成第一轮成文。
- `deep_guide_ready`
  表示 `03` 已完成第一轮成文。
- `appendix_ready`
  表示 `06` 已完成第一轮成文。
- `package_polish_ready`
  表示跨文档一致性、自包含、视觉化表达、反 AI 味校正已完成。
- `final_review_passed`
  表示整包通过最终 review，可进入交付态。

### 0.4 Pause / Resume Rules

这套计划必须支持“做到一半停下来，之后无歧义恢复”。

因此固定采用下面规则：

1. 每完成一个 gate，必须同步刷新该 gate 所属执行面允许修改的 Source-of-Record 文件与真实文件面。
   其中 `PLAN_PATH` 只在结构蓝图、验收口径、gate 定义、回退规则发生变化时强制同步；纯运行态推进至少同步 `STATUS_PATH`、`QUEUE_PATH`。
2. `STATUS_PATH` 永远记录“现在做到哪了”，`QUEUE_PATH` 永远记录“下一步唯一该做什么”。
3. 任何 stage 未达到 `done_condition` 前，不得口头视为完成。
4. 如果结构性问题尚未 disposition，不进入下一轮 drafting。
5. 任何中断恢复，都必须先读 `STATUS_PATH`，再读 `QUEUE_PATH.current_task`；只有当 `STATUS_PATH` 指示存在结构争议、职责边界疑问或信息不足时，才回读 `PLAN_PATH`。

### 0.5 Execution Authority Model

为避免“到底能不能继续写正文”的歧义，这里把执行权限固定写死。

| execution_surface | allowed_write_surface | autonomous_progress_allowed | drafting_permission |
| --- | --- | --- | --- |
| `plan_hardening` | `PLAN_PATH`, `STATUS_PATH`, `QUEUE_PATH` | `yes` | `no` |
| `outline_package_building` | `OUTLINE_PACKAGE_PATH`, `STATUS_PATH`, `QUEUE_PATH` | `yes` | `no` |
| `structure_lock_review` | `PLAN_PATH`, `OUTLINE_PACKAGE_PATH`, `STATUS_PATH`, `QUEUE_PATH` | `yes` | `no` |
| `final_drafting` | `requirements_engineering/final/*.md`, `STATUS_PATH`, `QUEUE_PATH` | `yes` | `yes` |
| `package_polish` | `requirements_engineering/final/*.md`, `STATUS_PATH`, `QUEUE_PATH` | `yes` | `yes` |

规则：

- `Stage 0` 与 `Stage 1` 使用 `plan_hardening`。
- `Stage 2` 使用 `outline_package_building`。
- `Stage 3` 使用 `structure_lock_review`。
- `Stage 4` 到 `Stage 8` 使用 `final_drafting`。
- `Stage 9` 使用 `package_polish`。
- 在 `plan_hardening`、`outline_package_building`、`structure_lock_review` 三种 execution surface 下，都不允许开始写 `final/`。
- 在 `outline_package_building` 阶段，不允许跳过大纲包直接写 `final/`。
- 只有当 gate 到达 `structure_locked` 后，`drafting_permission` 才变为 `yes`。

### 0.6 Gate-to-Surface Matrix

为避免恢复时不知道“哪些文件该存在、哪些不该存在”，每个 gate 对应的期望文件面固定如下：

| gate | expected_present | expected_absent_or_optional |
| --- | --- | --- |
| `progressive_plan_ready` | `PLAN_PATH`, `STATUS_PATH`, `QUEUE_PATH` | `OUTLINE_PACKAGE_PATH`, `requirements_engineering/final/*.md` |
| `findings_reviewed` | `PLAN_PATH`, `STATUS_PATH`, `QUEUE_PATH` | `OUTLINE_PACKAGE_PATH`, `requirements_engineering/final/*.md` |
| `outline_package_ready` | `PLAN_PATH`, `STATUS_PATH`, `QUEUE_PATH`, `OUTLINE_PACKAGE_PATH` | `requirements_engineering/final/*.md` |
| `structure_locked` | `PLAN_PATH`, `STATUS_PATH`, `QUEUE_PATH`, `OUTLINE_PACKAGE_PATH` | `requirements_engineering/final/*.md` |
| `overview_and_main_ready` | `PLAN_PATH`, `STATUS_PATH`, `QUEUE_PATH`, `OUTLINE_PACKAGE_PATH`, `final/00-report-system-overview.md`, `final/01-main-guide.md` | `final/02*.md`, `final/03*.md`, `final/04*.md`, `final/05*.md`, `final/06*.md` |
| `pm_guide_ready` | `overview_and_main_ready` 全部 + `final/02-pm-guide.md` | `final/03*.md`, `final/04*.md`, `final/05*.md`, `final/06*.md` |
| `example_guides_ready` | `pm_guide_ready` 全部 + `final/04-user-story-examples.md`, `final/05-ears-examples.md` | `final/03*.md`, `final/06*.md` |
| `deep_guide_ready` | `example_guides_ready` 全部 + `final/03-spec-architecture-guide.md` | `final/06*.md` |
| `appendix_ready` | `deep_guide_ready` 全部 + `final/06-reference-appendix.md` | `none` |
| `package_polish_ready` | `appendix_ready` 全部 | `none` |
| `final_review_passed` | `appendix_ready` 全部 + final review notes in `STATUS_PATH` | `none` |

### 0.7 Gate Transition Sync Checklist

每次 gate 变化时，至少要同步下面字段，任何遗漏都视为状态面不一致：

- `STATUS_PATH.current_gate`
- `STATUS_PATH.next_gate`
- `STATUS_PATH.current_stage`
- `STATUS_PATH.current_execution_surface`
- `STATUS_PATH.drafting_permission`
- `STATUS_PATH.reached_gates`
- `STATUS_PATH.Stage Progress`
- `STATUS_PATH.required_next_step`
- `STATUS_PATH.pending_reopen_trigger`
- `STATUS_PATH.Resume Checkpoint.last_completed_step`
- `STATUS_PATH.Resume Checkpoint.current_focus`
- `STATUS_PATH.Worklog`
- `QUEUE_PATH.Handoff Entry.current_execution_surface`
- `QUEUE_PATH.Handoff Entry.drafting_permission`
- `QUEUE_PATH.Active Queue.current_task`
- `QUEUE_PATH.Active Queue.next_task`
- `QUEUE_PATH.Active Queue.next_after_next`

### 0.8 Findings Disposition Vocabulary

`Stage 1` 只允许使用下面三种 disposition，且它们有固定含义：

| disposition | meaning | required_record |
| --- | --- | --- |
| `fixed_now` | 问题已在当前轮修正到足以不再阻塞下一 gate | 在 `plan/status/queue` 中能看到修正结果 |
| `accepted_for_now` | 问题存在，但当前包级结构中已明确接受其边界，不阻塞下一 gate | 在 `STATUS_PATH` 里写明接受理由与边界 |
| `deferred_explicitly` | 问题暂不解决，但已明确说明为什么 defer，以及未来在什么条件下重开 | 在 `STATUS_PATH` 里写明 defer 原因与重开触发条件 |

`findings_reviewed` 的通过条件不是“主观觉得差不多”，而是：

- 当前开放 findings 全部被赋予上述三种 disposition 之一
- 没有任何 `pending` finding 继续阻塞 `Stage 2`
- `STATUS_PATH` 与 `QUEUE_PATH` 已同步到下一 gate

### 0.9 Runtime Recovery Contract

为避免 `plan` 被误用成 live task board，这里把恢复权威关系固定为：

- `STATUS_PATH + QUEUE_PATH`
  是 live recovery pair，负责告诉执行者“现在做到哪了”和“下一步唯一该做什么”。
- `PLAN_PATH`
  是结构与验收权威，负责裁决职责边界、输出契约、gate 含义与通过条件。
- 如果 `PLAN_PATH` 与 `STATUS_PATH/QUEUE_PATH` 在 live next step 上出现冲突：
  以 `STATUS_PATH + QUEUE_PATH` 为准，再回到 `PLAN_PATH` 修正设计态描述，不能反过来覆盖运行态。

### 0.10 Reopen / Rollback Contract

progressive 执行默认向前推进，但不是“只许前进，不许重开”。

必须显式区分两类情况：

- `minor_fix_in_current_stage`
  局部文字、例子、图表、口径修补，不改变文件职责边界、读者路径、共享例子地图或 gate 定义。
  这种情况可以留在当前 stage 内修补，不必回退 gate。
- `structural_reopen_required`
  一旦出现下面任一情况，必须显式回退并重开，而不是在后续 drafting 中悄悄硬补：
  - 文件职责边界改变
  - 读者路径改变
  - 共享例子策略改变
  - 自包含原则发生冲突，导致某份文档必须新增关键解释层
  - 一个已锁定文件的完成，依赖于尚未锁定结构的另一文件大幅改写

回退规则固定为：

- 如果问题发生在 `Stage 2` 或 `Stage 3`
  回到 `outline_package_building` 或 `structure_lock_review`，并更新 `OUTLINE_PACKAGE_PATH.review ledger`。
- 如果问题发生在 `Stage 4` 到 `Stage 9`，且影响包级结构
  `STATUS_PATH.current_gate` 至少回退到 `outline_package_ready` 或 `structure_locked` 中更早的那个合法 gate；
  `QUEUE_PATH.current_task` 也必须切回对应的结构修订任务。
- 任何回退都必须在 `STATUS_PATH.pending_reopen_trigger`、`STATUS_PATH.Worklog` 与 `QUEUE_PATH.Blocked State` 或 `Active Queue` 中显式记录原因。

## 1. 为什么要单独立这个计划

`requirements_engineering/` 下面现在已经有足够多的研究材料，但它们还属于“研究工作区”，不等于“最终读者交付物”。

当前材料的强项是：

- topic 拆分清楚
- 证据层、本地权威副本层、综合判断层已经存在
- Story / EARS / BDD / agent-format / governance 的分层判断已经基本稳定

当前材料的短板是：

- 读者路径还是研究者路径，不是学习者路径
- 很多结论依赖 topic 之间来回跳转
- `_artifacts/` 与 `topic-*` 仍带有明显的 round / wave / research 过程痕迹
- 如果直接写成一份大文档，工程师、传统 PM、PM+架构师 三类读者会互相拖累

因此，这里不是直接开写 `final/`，而是先锁定一份“最终报告体系计划”，确保后续成文不会退化成：

- topic 拼盘
- 研究档案汇总
- 过度抽象的战略白皮书
- 只会写概念、不会教人落地的说明文

## 2. 这套最终交付物到底是什么

### 2.1 交付对象

这不是“一份总报告”。

这也不是“主报告 + 一堆必须互相引用才能看懂的配套件”。

这里要做的是一套 **三层主文档 + 示例手册层 + 一份支撑附录** 的报告系统：

1. `主文档`
   面向工程师优先，同时让 PM 和技术管理者也能顺畅读懂。
2. `中等文档`
   面向传统 PM，帮助他们把既有 PRD / Story / AC 习惯升级到 AI 时代的分层需求表达。
3. `深度文档`
   面向 PM + 架构师，讲清楚规格、契约、架构分解、验证、agent workflow 与治理的高级做法。
4. `示例手册`
   以写法、验法、正反例、重构对照为主，承担高密度 example 教学，而不是挤占主文档篇幅。
5. `附录`
   放术语、外部可信 URL、标准与工具映射、证据分级说明，但不承担“解释正文”的责任。

### 2.2 最核心的设计判断

不能把这件事写成一份文档，原因不是“篇幅太大”，而是“认知任务不同”。

- 工程师先需要建立整体心智模型：AI 时代需求工程到底重构了什么。
- 传统 PM 先需要建立迁移路径：从熟悉的 PRD / Story / AC 出发，怎样逐步进入更结构化的方法。
- PM 与架构师则需要面对更硬的问题：什么时候应该上 EARS、什么时候应该用决策表或 DMN、agent spec 应该放在哪一层、如何做 traceability 与治理。

如果把这三类任务塞进一份正文，会出现四个问题：

- 入门读者被高级细节压垮
- 高级读者又觉得内容不够“能落地”
- 教学路径被打断
- 自包含要求会逼迫文档变得过长且重复失控

因此，三层主文档不是“拆文件”，而是“拆认知任务”。

同时，示例手册层也必须独立存在，因为“理解方法”与“通过大量样例学会写法”也是两种不同任务。

如果不把样例层单独拆出来，会马上出现两个问题：

- 主文档会因为正反例、重写对照、验收方式说明而膨胀失控
- 深度文档会因为示例密度过高而变成资料册，破坏主线叙事

因此，最终结构应该理解为：

- 三份主文档负责“讲清楚”
- 两份示例手册负责“练明白”
- 一份附录负责“补出处、术语与外部可信参考”

## 3. 总目标与读者任务

### 3.1 总目标

把 `requirements_engineering` 当前工作区中的研究成果，收束成一套 **自包含、可教学、可执行、可做规格落地** 的报告系统。

### 3.2 读者完成后应获得什么

读完这套报告后，目标读者应该能做到：

- 理解 AI 时代需求工程不是“选一个模板”，而是重新组织一套分层表达体系
- 区分 Story、EARS、Examples / Gherkin、Agent Spec / Workflow Files、Governance / Traceability 各自负责什么
- 知道什么时候该保持轻量，什么时候必须升级到更严格的规格形式
- 能开始动手写更好的 user story、acceptance criteria、EARS 条款、feature spec 与 agent 工作包
- 能理解为什么“自包含的规格表达”在 AI 时代比以前更重要

对不同读者，进一步收束成下面的成功结果：

- 工程师 / Tech Lead / Staff Engineer
  读完后应能向团队解释整套分层结构，并能指导需求工件如何组合。
- 传统 PM / 产品负责人
  读完后应能把现有 PRD / Story / AC 写法升级到更可协作、更可执行的层次。
- PM + 架构师 / 系统负责人
  读完后应能把轻量需求推进到更精确的规格、验证与工作流组织。
- 技术管理者 / 平台治理负责人
  读完后应能判断组织最小可行推进顺序、哪些环节必须治理、哪些能力暂时不必重投入。

### 3.3 主要读者与次要读者

| audience | role | 主要诉求 |
| --- | --- | --- |
| `primary_audience_a` | 工程师 / Tech Lead / Staff Engineer | 先理解整体，再知道方法怎么组合，最后能指导团队落地 |
| `primary_audience_b` | 传统 PM / 产品负责人 | 从熟悉的 Story / PRD / AC 出发，知道如何升级而不是被替代 |
| `primary_audience_c` | PM + 架构师 / 系统负责人 | 需要可操作的规格、分解、验证、traceability、治理方法 |
| `secondary_audience` | 技术管理者 / 平台治理负责人 | 看懂为什么组织与流程要改，以及最小可行推进顺序 |

### 3.4 明确不做什么

这套最终报告不负责：

- 复刻 deep research 过程
- 逐条展示所有本地证据副本
- 把 topic 文件原样拼接成最终成品
- 代替正式标准全文
- 代替组织内部的最终模板库或 SOP

## 4. 核心总论点

这套报告系统必须围绕一条统一主线，而不是让每份文档各讲各的。

建议锁定的统一主线是：

> **AI 时代的需求工程，不是在 User Story、EARS、BDD、Agent Spec 之间选一个赢家，而是在更高层次上重组一套“分层、可追溯、可执行”的需求表达体系。**

为避免后续写作漂移，主线进一步收束为下面五层：

| layer | 中文名称 | 主要回答的问题 | 当前最主要来源 |
| --- | --- | --- | --- |
| `L1` | 意图层 | 为什么做、给谁做、业务价值是什么 | Topic 02, Topic 01 |
| `L2` | 行为契约层 | 系统在什么条件下必须做什么 | Topic 03, Topic 01 |
| `L3` | 确认与验证层 | 怎样证明需求被满足 | Topic 05 |
| `L4` | 执行与工作流层 | agent 和团队如何拿这些信息工作 | Topic 06, Topic 04 |
| `L5` | 治理与追溯层 | 怎样让规格可审查、可追踪、可合规 | Topic 01, Topic 04, Topic 05 |

这五层不是五种互斥模板，而是一套协同结构。

它们与当前 topic 的映射关系要在最终报告中稳定表达为：

- `User Story` 更接近意图层，不是完整合同
- `EARS / structured requirement` 更接近行为契约层，但不是万能格式
- `Examples / BDD / Gherkin / decision-table` 更接近确认与验证层
- `AGENTS.md / CLAUDE.md / spec-plan-tasks / workflow files` 更接近执行与工作流层
- `29148 / GtWR / traceability / compliance constraints` 更接近治理与追溯层

## 5. 自包含原则

自包含是最高优先级之一。后续所有成文必须满足这里的约束。

### 5.1 自包含的定义

所谓“自包含”，不是“没有参考资料”，而是：

- 不依赖仓库内的 `topic-*`、`_artifacts/*`、`_reference/*` 才能读懂正文
- 不要求读者知道这轮 research 的 round / wave / status / queue
- 不要求读者沿着本地链接跳读才能理解一个关键判断
- 关键概念、例子、边界、方法选择理由，都在文档内完成解释

### 5.2 自包含的写作规则

最终的 reader-facing 文档必须遵守：

1. 不出现 `topic-02`、`W2-cross-topic-synthesis`、`round-1` 这类内部工作标签。
2. 不把“详见本地文件 X”当成正文解释的替代物。
3. 如果本地 topic 中已经有成熟例子，应把例子完整摘录并改写进正文，而不是只做指针。
4. 外部 URL 只能作为支持性参考，不承担正文教学职责。
5. 即便附录被删掉，三份主文档仍应各自成立。
6. 两份示例手册也必须各自自包含，不能默认读者先读完主文档才看得懂。

### 5.3 对外部 URL 的使用原则

你已经明确要求“最后可以放外部可信 URL，但报告最重要的是自包含”，因此这里锁定：

- `允许`：在附录中放官方标准简介页、官方文档、官方工具说明、可信研究论文、知名方法论作者的正式资料页
- `不允许`：把正文核心论证外包给外链
- `不允许`：把本地路径作为对外参考
- `推荐方式`：正文先讲清楚，再在附录做“进一步阅读 / 证据来源 / 术语出处”

## 6. 输出文件地图

建议在 `requirements_engineering/final/` 中生成下面文件：

| file | status | role |
| --- | --- | --- |
| `00-report-system-overview.md` | `required` | 说明整套交付物怎么读，给三类读者导读 |
| `01-main-guide.md` | `required` | 主文档，建立整套心智模型，工程师优先 |
| `02-pm-guide.md` | `required` | 面向传统 PM 的迁移文档 |
| `03-spec-architecture-guide.md` | `required` | 面向 PM + 架构师的深度文档 |
| `04-user-story-examples.md` | `required` | User Story 示例手册，以写法、验法、坏例/好例、重构对照为主 |
| `05-ears-examples.md` | `required` | EARS 示例手册，以模式、写法、验法、正反例、边界对照为主 |
| `06-reference-appendix.md` | `required` | 术语、外部可信 URL、标准/工具映射、证据分级说明 |

这里的 `00-report-system-overview.md` 不是第四种主文档，而是导读层。

`00-report-system-overview.md` 虽然可以非常短，但在当前 package 设计中仍视为必需，因为它承担跨文档导读、阅读顺序与角色分流。

在这个文件地图里，要明确区分三种层次：

- `01/02/03` 是主文档层
- `04/05` 是示例手册层
- `06` 是附录层

同时要明确：

- `00` 是 package navigation layer
- `01/02/03` 是 explanation layer
- `04/05` 是 training layer
- `06` 是 support layer

## 7. 三份主文档的职责边界

### 7.1 `01-main-guide.md`

**目标**：
建立全局心智模型，让工程师、PM、技术管理者都能先把“这整套东西到底是什么”理解清楚。

**它必须回答**：

- 为什么 AI 时代需求工程需要重组
- 为什么不是选一个模板当银弹
- 五层结构分别负责什么
- Story / EARS / Examples / Agent Workflow / Governance 如何组合
- 团队在什么情形下该升级规格表达
- 为什么这件事与 AI coding workflow 有直接关系

**它不应该承担**：

- 过深的标准条文对照
- 大量语法细节
- 复杂的 decision table / DMN / traceability 设计细节
- 过多文件模板
- 大量成组样例与密集改写练习

**它的主要气质**：

- 深入浅出
- 强叙事性
- 教学优先
- 但不空泛

### 7.2 `02-pm-guide.md`

**目标**：
帮助传统 PM 以最小心理断裂，从既有 PRD / User Story / AC 习惯进入 AI 时代的分层表达体系。

**它必须回答**：

- PRD、Story、AC、Examples、EARS 各自该放在哪
- PM 到底什么时候需要升级文档精度
- 怎样把“模糊的需求描述”变成“足够让工程师和 agent 工作的输入”
- 常见坏 story、坏 AC、坏需求写法怎么重构
- PM 与工程师/架构师的接口在哪里

**它不应该承担**：

- 深度架构分解
- 过多标准和合规条文
- 大量 agent runtime 机制解释
- 大量高密度示例库

**它的主要气质**：

- 迁移式教学
- 以熟悉概念为入口
- 重视“怎么写”和“什么时候升级”

### 7.3 `03-spec-architecture-guide.md`

**目标**：
给 PM + 架构师一份真正能指导规格化、架构化、验证化、工作流化的深度报告。

**它必须回答**：

- 规格分层和系统分解如何对齐
- EARS、decision table、DMN、BDD、traceability 各自的边界是什么
- agent workflow files 与 feature spec / plan / tasks 应怎样配合
- 怎样处理复杂条件、状态、异常、NFR、合规与审计
- 怎样把“可读需求”推进成“可执行工作包”

**它不应该退化成**：

- 纯标准综述
- topic 材料堆砌
- 只有术语没有 worked example 的高冷文档
- 示例手册的替身

**它的主要气质**：

- 规格导向
- 架构导向
- 高密度但仍可教学

## 7.4 示例手册层的职责边界

示例手册层不是附录，也不是主文档补丁。

它是一个独立教学层，专门解决下面的问题：

- “我听懂了，但还不会写”
- “我知道 Story / EARS 是什么，但不会判断自己写得好不好”
- “我需要连续看多个正反例，才能形成手感”

### `04-user-story-examples.md`

**目标**：
把 User Story 的写法、验法、坏例/好例、重构方式，用高密度案例讲透。

**它必须回答**：

- 好的 User Story 到底好在哪里
- 坏的 User Story 常坏在哪
- Story 与 AC 的分界如何落笔
- Story 写完后怎么初步检查、怎么验
- 同一需求如何从坏写法重构到更好的写法

**它应该多放的内容**：

- 短例子
- 坏例/好例对照
- 同一例子的多轮改写
- 常见反模式清单
- “为什么这个写法不行”的判定解释

### `05-ears-examples.md`

**目标**：
把 EARS 的模式、句法、适用边界、验法和重构方式，用高密度案例讲透。

**它必须回答**：

- 五种核心模式分别该怎么写
- 常见 clause 为什么会写坏
- EARS 写完后怎么检查是否可测、是否过载、是否越界
- 什么时候应该退出 EARS，改用 decision table / DMN / 其他规格形式
- 同一行为需求怎样从口语化描述推进到合格 EARS

**它应该多放的内容**：

- 模式分组样例
- 正例 / 反例
- clause 拆分与重写
- “可测 / 不可测”“原子 / 不原子”“该用 / 不该用 EARS”的对照

### 关于确认层与执行层训练面的处理

当前版本故意不再继续新增更多示例手册文件，否则包会快速膨胀。

因此这里明确采用下面的收口策略：

- `04-user-story-examples.md`
  除了 Story 本体，也承担 Story 与 AC / Examples 的接口训练。
- `05-ears-examples.md`
  除了 EARS 本体，也承担 EARS 与 decision table / DMN / verification boundary 的接口训练。
- `03-spec-architecture-guide.md`
  承担 agent workflow / spec-plan-tasks / execution-layer examples 的高级训练面，但只保留高价值例子，不扩张成第三本示例手册。

也就是说：

- 当前计划接受“不为确认层和执行层单独再开一本示例手册”
- 但必须在 `04/05/03` 的职责边界里把训练覆盖写清楚，不能含糊漂移

### 示例手册层与主文档层的关系

必须明确：

- 主文档中只保留少量贯穿例子，用于解释结构
- 示例手册中才承载大量高密度例子
- 主文档引用示例手册时，也不能让读者“非跳转不可”，即主文档自身仍需成立
- 示例手册是“能力训练层”，不是“概念总论层”

## 8. 输出文件的详细大纲草案

这里先锁定“可 review 的章节结构”，避免后续写正文时继续摇摆。

### 8.1 `01-main-guide.md` 建议大纲

1. `为什么 AI 时代要重新理解需求工程`
   讲清楚问题不再是“写需求文档还是不写”，而是“如何让需求对人和 agent 都有用”。
2. `一张图看懂分层表达体系`
   用五层结构搭起全文的第一认知框架。
3. `几种核心工件分别解决什么问题`
   Story、EARS、Examples / Gherkin、Agent Spec / Workflow、Governance 的角色划分。
4. `从模糊意图到可执行工作包`
   讲清从 why 到 contract 到 confirmation 到 tasks 的推进过程。
5. `一个贯穿式 worked example`
   建议以“手机银行主屏余额”做主例子，展示不同层次如何表达同一需求。
6. `什么时候该升级到更严格的规格`
   讲风险、复杂度、NFR、合规压力与多团队协作压力。
7. `AI coding workflow 为什么改变了需求写法`
   讲 agent 对输入质量的敏感性，以及为什么 team-level context 不能代替 feature spec。
8. `团队落地的最小可行路径`
   给工程团队与技术管理者一个务实的起步顺序。
9. `常见误区`
   如“把 Story 当合同”“把 Gherkin 当需求本体”“把 AGENTS.md 当大一统说明书”。
10. `结论`
   重申五层结构与渐进升级的核心观点。

说明：

- 本文只保留少量贯穿式例子
- 大量 Story / EARS 写法样例外移到示例手册层

### 8.2 `02-pm-guide.md` 建议大纲

1. `给传统 PM 的起点`
   从 PRD、用户故事、验收标准出发，而不是一上来讲标准和形式化。
2. `PRD、Story、AC 到底各自该负责什么`
   重新划分角色，避免一个文档承载所有职责。
3. `怎样写出有用的 User Story`
   结合 Topic 02 的坏例 → 好例重构。
4. `怎样写出可工作的 Acceptance Criteria 与 Examples`
   从口语化验收条件推进到更结构化的例子。
5. `什么时候需要 EARS 或更强的规格表达`
   讲升级条件，而不是把 EARS 写成 PM 必须掌握的一切。
6. `PM 如何与工程师、测试、架构师、agent 协作`
   讲接口，不讲过多底层机制。
7. `常见文档反模式`
   例如空洞 story、伪规格、NFR 硬塞、把需求写进 agent rules。
8. `一个从需求到交付的端到端示例`
   用一个适中的业务案例，把 Story、AC、Example、Tasks 串起来。
9. `PM 的最小方法包`
   最终给出“先学会什么，再逐步升级什么”的可执行收口。

说明：

- 本文讲“怎么理解与使用”
- 只保留少量示范性写法
- 大量具体写法例子放到 `04-user-story-examples.md` 和 `05-ears-examples.md`
- 不承担高密度重构训练册功能

### 8.3 `03-spec-architecture-guide.md` 建议大纲

1. `为什么高级需求表达一定会进入规格与架构问题`
   讲需求工程与架构分解本来就连在一起。
2. `规格分层总图`
   意图层、契约层、验证层、执行层、治理层如何形成可追溯链条。
3. `EARS 作为行为契约层的适用边界`
   讲五模式、复杂条件边界、何时退出 EARS。
4. `复杂条件、决策逻辑与状态建模`
   讲 decision table、DMN、状态/触发建模与 EARS 的接口。
5. `从需求到架构约束`
   把 NFR、接口契约、异常行为、部署约束、系统边界连到架构视角。
6. `BDD / Gherkin / Examples 在验证层的正确位置`
   讲 confirmation，不把它们抬成需求本体。
7. `Agent 工作流中的规格组织`
   讲 `AGENTS.md`、`CLAUDE.md`、scoped rules、`spec/plan/tasks`、Kiro / Spec Kit / OpenSpec 一类工作流。
8. `Traceability、治理与标准锚点`
   讲 29148、GtWR、可追踪性、审计、变更管理，但明确 full-text 边界。
9. `深度 worked example`
   建议用双例结构：
   第一例用“手机银行主屏余额”做教学贯穿；
   第二例用“高风险/高合规场景”展示为什么轻量表达不够。
10. `高级反模式与失败模式`
   例如 clause 过载、decision logic 混进 EARS、agent context 膨胀、traceability 只挂名不落地。
11. `结论与升级路线`
   收束为“何时需要把团队从主文档升级到深度方法”。

说明：

- 本文保留少量高价值 worked example
- 不承担大规模句型训练与密集反例库

### 8.4 `04-user-story-examples.md` 建议大纲

1. `这份手册怎么用`
   说明它不是理论总论，而是例子训练册。
2. `先给一套最小判断尺子`
   例如价值、角色、边界、可协商性、可验证性。
3. `典型正例`
   用短例子讲清什么叫写得合适。
4. `典型坏例`
   例如伪规格、空泛价值、NFR 硬塞、角色错位、技术任务伪装成 story。
5. `坏例到好例的重构对照`
   一组一组地改写，并解释为什么更好。
6. `Story 与 AC 的分界示例`
   展示哪些信息应留在 story，哪些应下沉到 AC / examples。
7. `怎么快速自检`
   给一套轻量检查法。
8. `怎么验写得是否足够好`
   从团队协作、实现输入、可测试性几个角度看。
9. `按场景分类的样例库`
   建议按产品功能、平台能力、NFR、异常场景、探索型需求分类。
10. `结尾`
   收束为“先写对，再写多”。

补充说明：

- 本手册要显式覆盖 Story 与 AC / Examples 的接口训练
- 但不扩张成完整 BDD / Gherkin 理论文档

### 8.5 `05-ears-examples.md` 建议大纲

1. `这份手册怎么用`
   说明它是句法与边界训练册。
2. `先给一套最小判断尺子`
   例如主语清楚、触发清楚、响应可测、原子性、不过载。
3. `五种核心模式的正例`
   按 Ubiquitous / Event-driven / State-driven / Unwanted / Optional 组织。
4. `复合模式的正确写法`
   讲何时组合，何时不要硬组合。
5. `典型坏例`
   如形容词堆砌、主语漂移、多条件过载、把决策逻辑塞进一句。
6. `坏例到好例的重构对照`
   把自然语言描述逐步改成合格 EARS。
7. `怎么快速自检`
   看是否可测、是否原子、是否边界清楚。
8. `怎么验写得是否足够好`
   从测试、架构、审查、agent 输入四个角度检查。
9. `什么时候不要继续写 EARS`
   进入 decision table / DMN / state model 的退出判据。
10. `按模式与场景分类的样例库`
   建议按登录态、异常、性能、安全、配置、规则边界分类。
11. `结尾`
   收束为“先写稳，再写复杂”。

补充说明：

- 本手册要显式覆盖 EARS 与 decision table / DMN / verification boundary 的接口训练
- 但不扩张成独立的 DMN 教材

### 8.6 `00-report-system-overview.md` 与 `06-reference-appendix.md` 的骨架要求

虽然 `00` 是导读层、`06` 是支撑附录层，但它们都必须在大纲阶段就被固定下来，不能到 drafting 时临场发挥。

`00-report-system-overview.md` 至少应覆盖：

1. `这套报告系统解决什么问题`
2. `按读者角色划分的阅读路径`
3. `全文件地图与每个文件的一句话职责`
4. `建议阅读顺序与时间预算`
5. `如果时间有限先看什么`
6. `示例手册与附录应怎样配合使用`

`06-reference-appendix.md` 至少应覆盖：

1. `关键术语表`
2. `外部可信 URL 清单`
   按标准 / 方法论 / 工具 / 进一步阅读分组，而不是散乱罗列。
3. `标准与工具映射表`
4. `证据分级与表达边界说明`
5. `正文中未展开但适合延伸阅读的入口`

### 8.7 `OUTLINE_PACKAGE_PATH` 最小契约

`Stage 2` 产出的详细大纲包不是自由发挥文档，而必须至少包含下面三层结构：

1. `package frame`
   至少交代批准文件集合、统一 thesis、跨文档读者路径、共享例子地图、跨文档术语与边界 guardrails。
2. `00-06 七张 file cards`
   每个文件都必须至少包含：
   - `file_role`
   - `primary_reader`
   - `reader_problem_to_solve`
   - `must_cover`
   - `must_not_cover`
   - `section_skeleton`
   - `worked_examples_or_example_policy`
   - `required_visuals_or_tables`
   - `cross_doc_dependencies`
   - `self_contained_notes`
3. `review ledger`
   至少记录 unresolved questions、是否阻塞 structure lock、建议 disposition 方向，以及 `ready_for_structure_review: yes/no`。

## 9. 输入材料如何转译到最终交付

这一节要锁住“本地材料如何服务最终报告”，否则后续很容易写着写着又回到工作区口吻。

### 9.1 输入源分层

| source_layer | 代表文件 | 在最终报告中的用途 |
| --- | --- | --- |
| `topic_docs` | `deep_research_topics/topic-*.md` | 提取已成熟的概念解释、坏例/好例、worked examples、边界判断 |
| `cross_topic_synthesis` | `W2-cross-topic-synthesis.md` | 提取跨 topic 稳定判断，构成三份文档的统一口径 |
| `selection_matrix` | `W2-selection-matrix-v2.md` | 提取选型边界与项目场景建议 |
| `claims_audit` | `W2-claims-audit-v2.md` 和 `claims-audit.md` | 防止过度断言，给风险标签与保守口径 |
| `reference_layer` | `_reference/*.md` | 验证、加固判断；后续转化为附录中的外部可信 URL |
| `plan_context` | `dr-round-1.plan.md`, `README.md` | 理解原始研究目的与范围，不直接进入读者文案 |

### 9.2 明确哪些内容可以直接转译

可以直接“消化吸收后写入最终报告”的内容：

- Topic 02 中对 Story 的角色定义、反模式与坏例/好例
- Topic 03 中对 EARS 的模式、边界、worked examples
- Topic 05 中对 Story / EARS / BDD / DMN 的角色分工
- Topic 06 中对 agent context file 与 feature spec workflow 的边界判断
- W2 synthesis 中已经闭合的跨主题判断

### 9.3 明确哪些内容不能直接搬过去

不能直接搬入 reader-facing 文档的内容：

- round / wave / gate / queue 语言
- “本轮新增证据”“starter-covered”“primary-saturated-for-gate” 这类研究执行标签
- 本地 reference 文件名
- claims audit 中过于内部化的分级措辞

它们可以转化成：

- 更平实的风险提醒
- “当前证据支持到什么程度”的温和表述
- 附录中的“进一步阅读 / 证据说明”

## 10. 教学策略

因为你明确要求“既要一条线、整体熟悉起来，又要有教学性质，还要最终进入具体规格写法”，所以三份文档必须组成一个教学梯度，而不是三种随机视角。

建议锁定下面的教学梯度：

| level | 教学目标 | 主要承载文档 |
| --- | --- | --- |
| `L0` | 先建立全局心智模型 | `01-main-guide.md` |
| `L1` | 从熟悉工件迁移到分层方法 | `02-pm-guide.md` |
| `L2` | 通过大量例子学会怎么写、怎么验 | `04-user-story-examples.md`, `05-ears-examples.md` |
| `L3` | 学会更精确地写规格和验证材料 | `03-spec-architecture-guide.md` |
| `L4` | 学会理解标准、治理、traceability、agent workflow 的高级边界 | `03-spec-architecture-guide.md` + `06-reference-appendix.md` |

### 10.1 建议贯穿使用的例子

为了教学效果稳定，建议最终报告不要每章都换新例子，而是采用“少量贯穿例子，多次升维讲解”的方式。

建议先锁定：

- `Example A`：手机银行主屏余额
  优点：已有 Story 与 EARS 两侧材料，适合主文档和 PM 文档
- `Example B`：高风险 / 高合规行为控制场景
  可选 AEB，也可改写成更贴近通用软件的高风险规则场景
  适合深度文档展示“为什么轻量工件不够”

同时，示例手册层可以在不破坏主文档节奏的前提下，扩展出更多类别：

- discovery / 产品功能类
- 平台 / API / integration 类
- NFR / 性能 / 安全类
- 异常 / 降级 / 风险控制类

## 11. 叙事与文风约束

### 11.1 统一叙事

三份文档都要围绕同一叙事：

- 需求工程不是在多个模板之间做宗教战争
- AI 时代的难点是把表达层、验证层、执行层与治理层重新组织起来
- 文档不是为了“更像标准”，而是为了让人和 agent 都能正确工作

### 11.2 统一文风

所有 reader-facing 文档建议采用：

- 中文主写
- 关键术语第一次出现时给出中英文
- “概念 -> 判断 -> 例子 -> 建议 -> 边界”的推进节奏
- 少讲研究过程，多讲结构与机制
- 不要写成命令式操作手册，也不要写成空泛口号

### 11.3 反 AI 味写作约束

这套报告主要是给人看的，不是给模型看的。

因此，后续所有 reader-facing 文档都必须显式压制“机器人味儿”。

这里所说的“机器人味儿”，在本计划里定义为：

- 追求形式整齐，超过追求读者吸收效果
- 追求信息覆盖，超过追求解释节奏
- 追求看起来很完整，超过真正帮助读者理解

后续写作必须避免下面这些典型问题：

1. `bullet 泛滥`
   不是所有内容都要拆成点。能用自然段讲清楚的，不要硬拆清单。
2. `信息平均用力`
   不能每个点都写得一样重。真正关键的地方要慢下来讲透，次要内容要收。
3. `术语堆积`
   新概念不能连续堆砌。术语第一次出现时，要解释它为什么重要，而不是只给定义。
4. `模板句反复出现`
   要少用“不是 X，而是 Y”“本质上是”“核心在于”这类重复句型，避免形成机械腔调。
5. `像总结，不像解释`
   不能只是把 research 结果整理一下，要写出带读者前进的解释感。
6. `过度对称`
   不要每节都强行写成“三点、五层、八类”的对称结构。结构应服务理解，不应反过来控制表达。
7. `抽象词过密`
   “机制、范式、框架、治理、能力、闭环”这类词可以用，但必须落到例子、判断或动作上。
8. `读者对象漂移`
   每份文档都要持续记住自己主要写给谁，不要一段像给工程师，一段又像给高管。

写作时建议主动追求下面这些更“像人写的”特征：

- 有节奏，而不是满篇同强度输出
- 有解释顺序，而不是概念并列
- 有重点反复强调，而不是平均摊开
- 有自然中文，而不是摘要腔、汇报腔、模型腔
- 有读者引导感，而不是把材料倾倒给读者

### 11.4 视觉化表达约束

对于复杂流程、复杂概念、复杂关系，不应默认只靠长段文字硬讲。

当文字开始出现下面情况时，应优先考虑视觉化表达：

- 涉及多层结构
- 涉及阶段推进
- 涉及工件之间的映射关系
- 涉及条件分支、升级路径、边界判断
- 涉及多角色协作接口

允许并鼓励在最终文档中使用下面这些表达形式：

- `Markdown 表格`
  适合放角色分工、工件分层、选择边界、正反例对照、升级条件。
- `Mermaid 图`
  适合放流程、依赖、层次结构、决策路径、工件流转。
- `代码块 / 规格块`
  适合放 User Story、AC、EARS、Gherkin、spec / plan / tasks 样例。
- `对照块`
  适合放“坏例 -> 好例”“轻量写法 -> 严格写法”“该用 -> 不该用”的并排比较。

但视觉化表达也要遵守两个限制：

1. 不为了“显得高级”而画图。
   图表必须比文字更容易理解，才值得出现。
2. 图表不能取代解释。
   图表负责降低理解负担，正文仍要解释图表在表达什么。

## 12. 风险清单

### 12.1 结构风险

1. `主文档过长`
   最容易把 PM 迁移内容、深度规格内容全塞进去。
2. `中等文档过浅`
   如果只重复 Story / AC 常识，会失去 AI 时代升级的价值。
3. `深度文档过散`
   如果 topic 03、05、06 各写一块，很容易又变回 topic 拼盘。
4. `示例内容挤爆主文档`
   如果不单列示例手册，例子会把主线叙事冲散。

### 12.2 内容风险

1. `重复过多`
   自包含要求会推高重复，但如果不控制，会让三份文档失去各自价值。
2. `过度断言`
   尤其是对标准条款、工具成熟度、agent 语义一致性。
3. `本地化痕迹泄漏`
   把工作区路径、阶段标签写进 reader-facing 文档。
4. `AI 味过重`
   形式太工整、bullet 太多、术语过密、缺乏解释节奏。
5. `复杂内容全靠硬写文字`
   本来应该图表化、流程化、对照化的内容，被大段文字拖垮。

### 12.3 风险化解策略

- 先锁文档职责，再写正文
- 对每份文档都做“本文件必须回答 / 不应该承担”的边界审查
- 保留一个统一的 thesis ledger 与 do-not-say list
- 在附录中承担链接、术语、出处，不把正文写成索引页
- 把高密度案例明确外移到 `04/05` 示例手册层
- 在写作阶段显式做一次“反 AI 味”审校
- 对复杂概念和复杂流程优先做图表化审查

## 13. 产出顺序

不建议三份文档同时开写。

建议采用下面顺序：

1. 先写 `00-report-system-overview.md`
   锁入口、读者路径、总文件图
2. 再写 `01-main-guide.md`
   锁统一叙事和核心口径
3. 再写 `02-pm-guide.md`
   从主文档口径出发，做 PM 迁移
4. 再写 `04-user-story-examples.md`
   先把 Story 的高频写法、验法、重构样例落稳
5. 再写 `05-ears-examples.md`
   再把 EARS 的模式、边界与样例训练册落稳
6. 再写 `03-spec-architecture-guide.md`
   最后进入深度规格、架构、治理内容
7. 最后写 `06-reference-appendix.md`
   把外部可信 URL、术语、标准映射、证据说明整理出来

原因很简单：

- 主文档先定，后面两份不会漂
- PM 文档先于深度文档，可以防止整套交付过早进入“高门槛模式”
- 示例手册先于深度文档，可以先把“写法训练层”铺稳
- 附录必须最后写，否则容易反过来绑架正文

## 14. Progressive 执行阶段

后续真正开始写 `final/` 时，不按“想到哪写到哪”的方式推进，而按下面的 stage / gate 体系推进。

### Stage 0: Progressive Surface Initialization

- purpose:
  把原本偏结构设计的 plan，升级成一套可暂停、可恢复、可跟踪的执行系统。
- outputs:
  `PLAN_PATH` 升级版、`STATUS_PATH`、`QUEUE_PATH`
- writes_to:
  `final-report-system.plan.md`, `final-report-system.status.md`, `final-report-system.queue.md`
- done_condition:
  三份 SoR 已存在，且当前 gate = `progressive_plan_ready`
- gate_transition:
  `none -> progressive_plan_ready`
- current_state:
  `completed`

### Stage 1: Findings Review and Disposition

- purpose:
  在正式 drafting 前，先把当前已经识别出的结构性问题逐条做 disposition。
- outputs:
  findings register、修订后的 plan（如有）、更新后的 status / queue
- writes_to:
  `PLAN_PATH`, `STATUS_PATH`, `QUEUE_PATH`
- done_condition:
  所有当前开放 findings 均被标记为 `fixed_now`、`accepted_for_now` 或 `deferred_explicitly`
- gate_transition:
  `progressive_plan_ready -> findings_reviewed`
- safe_to_pause_after:
  `yes`

### Stage 2: Detailed Outline Package

- purpose:
  在正式成文前，把包级结构细化为可 review 的详细大纲包。
- outputs:
  `OUTLINE_PACKAGE_PATH`
- writes_to:
  `OUTLINE_PACKAGE_PATH`, `STATUS_PATH`, `QUEUE_PATH`
- done_condition:
  详细大纲包已落地，且满足 `8.7 OUTLINE_PACKAGE_PATH 最小契约`：覆盖 `00/01/02/03/04/05/06` 全部当前批准文件的章节骨架、关键图表点位、主要例子、读者路径与 review ledger
- gate_transition:
  `findings_reviewed -> outline_package_ready`
- safe_to_pause_after:
  `yes`

### Stage 3: Outline Review and Structure Lock

- purpose:
  对详细大纲包进行审阅，并锁定后续 drafting 的包级结构。
- outputs:
  structure lock note、必要时的小幅 plan patch
- writes_to:
  `PLAN_PATH`, `OUTLINE_PACKAGE_PATH`, `STATUS_PATH`, `QUEUE_PATH`
- done_condition:
  `OUTLINE_PACKAGE_PATH.review ledger` 中所有阻塞 drafting 的 unresolved questions 都已 disposition，且没有职责冲突、读者路径冲突或自包含冲突继续阻塞 drafting
- gate_transition:
  `outline_package_ready -> structure_locked`
- safe_to_pause_after:
  `yes`

### Stage 4: Draft `00` + `01`

- purpose:
  先建立 package-level 入口和统一主叙事。
- outputs:
  `00-report-system-overview.md`, `01-main-guide.md`
- writes_to:
  `requirements_engineering/final/00-report-system-overview.md`, `requirements_engineering/final/01-main-guide.md`, `STATUS_PATH`, `QUEUE_PATH`
- done_condition:
  `00` 与 `01` 完成第一轮成文，并满足最小自包含与读者路径要求
- gate_transition:
  `structure_locked -> overview_and_main_ready`
- safe_to_pause_after:
  `yes`

### Stage 5: Draft `02`

- purpose:
  完成面向传统 PM 的迁移文档。
- outputs:
  `02-pm-guide.md`
- writes_to:
  `requirements_engineering/final/02-pm-guide.md`, `STATUS_PATH`, `QUEUE_PATH`
- done_condition:
  `02` 完成第一轮成文，并与 `01` 口径对齐
- gate_transition:
  `overview_and_main_ready -> pm_guide_ready`
- safe_to_pause_after:
  `yes`

### Stage 6: Draft `04` + `05`

- purpose:
  先把“写法训练层”落稳，再进入最深的规格文档。
- outputs:
  `04-user-story-examples.md`, `05-ears-examples.md`
- writes_to:
  `requirements_engineering/final/04-user-story-examples.md`, `requirements_engineering/final/05-ears-examples.md`, `STATUS_PATH`, `QUEUE_PATH`
- done_condition:
  两份示例手册均完成第一轮成文，并具备基本的正例 / 反例 / 重构 / 验法结构
- gate_transition:
  `pm_guide_ready -> example_guides_ready`
- safe_to_pause_after:
  `yes`

### Stage 7: Draft `03`

- purpose:
  在前面三层与训练层都稳定后，再进入深度规格与架构文档。
- outputs:
  `03-spec-architecture-guide.md`
- writes_to:
  `requirements_engineering/final/03-spec-architecture-guide.md`, `STATUS_PATH`, `QUEUE_PATH`
- done_condition:
  `03` 完成第一轮成文，并与 `01/02/04/05` 口径一致
- gate_transition:
  `example_guides_ready -> deep_guide_ready`
- safe_to_pause_after:
  `yes`

### Stage 8: Draft `06`

- purpose:
  最后补附录层，把术语、外部可信 URL、标准/工具映射与证据说明收好。
- outputs:
  `06-reference-appendix.md`
- writes_to:
  `requirements_engineering/final/06-reference-appendix.md`, `STATUS_PATH`, `QUEUE_PATH`
- done_condition:
  `06` 完成第一轮成文，且不反过来绑架主文档理解
- gate_transition:
  `deep_guide_ready -> appendix_ready`
- safe_to_pause_after:
  `yes`

### Stage 9: Package Polish and Final Review

- purpose:
  完成跨文档一致性校正、反 AI 味审校、视觉化表达审查与最终交付 review。
- outputs:
  polished package、final review notes
- writes_to:
  `requirements_engineering/final/*.md`, `STATUS_PATH`, `QUEUE_PATH`
- package_polish_done_condition:
  跨文档一致性、自包含、读者路径、图表质量、语言节奏、风险边界已完成包级收口，且 package polish checklist 已逐项记录为 pass / minor_fix / reopen_required，并可把 gate 推进到 `package_polish_ready`
- final_review_done_condition:
  最终 review checklist 已逐项闭合，review notes 已写入 `STATUS_PATH`，且不存在 `reopen_required` 项，可把 gate 从 `package_polish_ready` 推进到 `final_review_passed`
- gate_transition:
  `appendix_ready -> package_polish_ready -> final_review_passed`
- safe_to_pause_after:
  `yes`

## 15. 验收标准

这份计划后续如果进入实施，最终成品至少要通过下面检查。

### 15.1 整体级验收

- 三份主文档各自可独立阅读
- 两份示例手册各自可独立阅读
- 三份主文档与两份示例手册口径一致，不互相打架
- 主文档读完后能形成整体心智模型
- PM 文档读完后能开始改写现有需求写法
- 示例手册读完后能直接模仿写法并做初步自检
- 深度文档读完后能开始构造更严格的规格与工作流
- 技术管理者读完后能判断最小可行推进顺序、关键治理边界与暂不必重投入的能力面
- 附录只是增强，不是理解前提
- 中途即使暂停，也能仅凭 `STATUS_PATH` 和 `QUEUE_PATH` 恢复到正确位置

### 15.2 文档级验收

文档级验收不应一刀切，而应按文档类型区分：

- `00-06 通用要求`
  - 开篇明确“这份文档帮谁解决什么问题”
  - 没有内部研究过程标签
  - 没有依赖本地路径才能看懂的内容
  - 没有明显的 bullet 泛滥、模板句泛滥、术语堆积问题
  - 关键复杂处有足够的解释节奏，而不是只做摘要式归纳
- `解释型文档（01/02/03）`
  - 文中给出最少一个完整 worked example
  - 明确列出“何时适用 / 何时升级 / 何时不要这么做”
  - 对复杂流程、复杂关系、复杂分层，至少一部分使用了合适的视觉化表达
- `导读层（00）`
  - 给出按读者角色和时间预算划分的阅读路径
  - 文件地图与各文件职责边界清楚
  - 不膨胀成正文替代物
- `示例手册（04/05）`
  - 至少包含足够数量的正例 / 反例 / 重构对照
  - 至少包含“怎么写”和“怎么验”两个维度
  - 例子分类清楚，而不是堆成杂乱案例池
- `支撑附录（06）`
  - 术语、外部可信 URL、标准 / 工具映射、证据表达边界组织清楚
  - 不承担正文教学职责
  - 即使删掉附录，主文档仍然可以成立

### 15.3 风险控制验收

- 标准 full-text 不可得的地方必须保守表达
- 工具链成熟度必须区分“存在”“趋势”“通用最佳实践”
- 对 EARS、BDD、agent files 都必须写清边界，不制造“万能格式”错觉
- 图表、表格、Mermaid、代码块必须服务理解，而不是装饰性堆砌
- 任何阶段切换时，`PLAN_PATH`、`STATUS_PATH`、`QUEUE_PATH` 与真实文件面必须保持一致

### 15.4 Review Checklists Minimum Contract

为避免 Stage 9 退化成“感觉差不多”，`STATUS_PATH` 中的 package polish / final review 至少要逐项记录下面检查：

- `cross_doc_consistency`
  thesis、术语、升级条件、工件边界是否一致
- `self_contained_integrity`
  是否存在必须跳回本地 topic 或附录才能理解的关键判断
- `reader_route_integrity`
  `00` 的导读路径与 `01/02/03/04/05/06` 的实际职责是否一致
- `example_policy_integrity`
  主文档是否克制示例密度，训练层是否承担了高密度样例责任
- `visual_support_quality`
  复杂结构是否已被合适表格 / 图 / 对照块减负，而非纯文字硬撑
- `language_quality`
  是否存在明显 bullet 泛滥、模板句泛滥、术语堆积、摘要腔
- `boundary_safety`
  是否制造了 Story / EARS / BDD / agent files / governance 的万能格式错觉

每项至少要标记为：

- `pass`
- `minor_fix`
- `reopen_required`

## 16. 执行中的下一步规则

这份 `PLAN_PATH` 不维护 live next step。

执行中的下一步，一律按下面优先级判定：

1. 先看 `STATUS_PATH`
   确认当前 gate、当前 stage、当前 execution surface 与 required_next_step。
2. 再看 `QUEUE_PATH`
   只执行 `Active Queue.current_task`。
3. 如遇到职责边界、输出契约、验收口径争议
   再回到 `PLAN_PATH` 相关章节裁决。

默认产出顺序仍然是：

`Stage 2 -> Stage 3 -> Stage 4 -> Stage 5 -> Stage 6 -> Stage 7 -> Stage 8 -> Stage 9`

但如果 `STATUS_PATH` 与 `QUEUE_PATH` 已经推进到更后面的 gate：

- 以 `STATUS_PATH + QUEUE_PATH` 为准
- 不要因为 `PLAN_PATH` 的静态说明而倒退执行

## 17. 当前计划所依据的主要本地输入

本计划主要依据下面这些现有材料形成，但这些路径只属于内部工作区语境，不会直接出现在最终 reader-facing 文档中：

- `requirements_engineering/deep_research_topics/README.md`
- `requirements_engineering/plan/dr-round-1.plan.md`
- `requirements_engineering/deep_research_topics/_artifacts/W2-cross-topic-synthesis.md`
- `requirements_engineering/deep_research_topics/_artifacts/W2-selection-matrix-v2.md`
- `requirements_engineering/deep_research_topics/topic-02-user-story-tutorial.md`
- `requirements_engineering/deep_research_topics/topic-03-ears-tutorial.md`
- `requirements_engineering/deep_research_topics/topic-05-integration-bdd-selection.md`
- `requirements_engineering/deep_research_topics/topic-06-agent-format.md`
- `TOPIC_FINAL_ENGINEER_REPORT_GENERATOR.md`

---

当前结论先收束为一句话：

> 这套最终交付物最合理的形态，不是“一份大全”，而是“一条统一主线之下的三层主文档 + 两份示例手册 + 一份附录”的自包含体系，其中主文档负责建立全局，PM 文档负责迁移，深度文档负责规格与架构落地，示例手册负责把写法与验法练明白，附录只负责增强可信度与可追溯性。
