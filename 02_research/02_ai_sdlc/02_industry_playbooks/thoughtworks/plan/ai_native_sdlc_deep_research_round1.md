# AI-Native SDLC Deep Research Plan (ThoughtWorks Topics, Round 1)

> 对应状态文件：`/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.status.md`
> 对应执行队列：`/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.queue.md`
> 本文件只记录设计态蓝图；实时状态与连续动作分别写入 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.status.md` 与 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.queue.md`。

## Instance Config

> 这是本轮实例参数的唯一设计态注册点。除 `topic registry` 本体外，后文不再重复定义这些参数。

| field | value |
| --- | --- |
| `plan_name` | `AI-Native SDLC Deep Research Plan (ThoughtWorks Topics, Round 1)` |
| `template_version` | `v8` |
| `round_label` | `一轮` |
| `plan_path` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.md` |
| `status_path` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.status.md` |
| `queue_path` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.queue.md` |
| `seed_dir` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics` |
| `reference_dir` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference` |
| `artifact_dir` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_artifacts` |
| `final_deliverable` | `“AI-Native 软件工程新常态（Next-Gen SDLC）”白皮书 / SOP，以及可外化为企业研发治理重构方案的战略蓝图` |
| `audience` | `内部战略研究、平台工程、研发管理、安全治理负责人，以及后续面向企业 IT 决策者的外部方案读者` |
| `round_focus` | `扩事实 / 补机制 / 补趋势 / 补限制 / 建立跨 topic 综合框架` |
| `derived_topic_count` | `= count(topic registry entries)` |
| `wave0_shared_doc_floor` | `8` |
| `wave1_doc_floor_per_topic` | `8` |
| `primary_source_floor` | `4` |
| `secondary_source_floor` | `2` |
| `recent_source_floor` | `1` |
| `limitation_source_floor` | `1` |
| `hard_gates_enabled` | `no` |

## 调研目的与服务对象

这轮 Deep Research 不是为了产出调研笔记本身。

真正的目的是：为 `“AI-Native 软件工程新常态（Next-Gen SDLC）”白皮书 / SOP，以及可外化为企业研发治理重构方案的战略蓝图` 提供可靠的原材料地基。

最终产出的读者是：`内部战略研究、平台工程、研发管理、安全治理负责人，以及后续面向企业 IT 决策者的外部方案读者`

本轮主任务是：`扩事实 / 补机制 / 补趋势 / 补限制 / 建立跨 topic 综合框架`

这份最终产出至少要满足下面要求：

- 系统性：覆盖关键维度，不遗漏，不失衡
- 逻辑性：每个判断都有证据支撑，推理链条可追溯
- 一致性：跨主题术语统一、口径统一、评估框架统一
- 专业可读：默认读者是专业人士，不需要手把手解释，但需要准确、严谨、无歧义

权威信源优先规则（最高优先级，不可违反）：

> 当权威一手来源已经足以支撑某个判断时，不为满足配额额外引入低质量二手来源。配额是防止搜太浅的下限，不是必须凑满的目标。宁缺毋滥。

## 本轮核心缺口

- Gap 1: 四条主线目前主要是观点与问题定义，缺少可复用的本地证据库、机制解释和反例材料。
- Gap 2: topic 之间已有组合关系设想，但尚未形成统一术语、统一评估框架和可追溯的跨 topic synthesis。
- Gap 3: 还没有把“ThoughtWorks 研讨会观察”转成可指导企业落地的能力栈、治理边界和实施顺序。

## Control Map

本轮实例 plan 只保留最小控制绑定，避免在实例正文里重写模板级 authority tables。

### Minimal Runtime Bindings

- `PLAN_PATH` 只记录设计态蓝图、实例参数、拓扑基线、Wave 设计与验收；不写实时进度、阻塞、worklog 或 active queue
- `STATUS_PATH` 只记录当前状态、gate、阻塞、拓扑 delta、分支处置与恢复上下文；不重写完整设计态蓝图
- `QUEUE_PATH` 是唯一连续派工入口；只记录 active queue、blocked state、refill pool 与 promotion rules
- `setup_ready` 是 gate，不是独立 wave；它表示 execution surface 已初始化完成、尚未关闭第一步 `Wave 0` 证据落库
- 默认 gate 路径为 `instantiation_complete -> setup_ready -> wave0_complete -> wave1_complete -> wave2_complete -> readiness_passed`
- `topic_stop_decision` 是研究线级决策；`primary_source_coverage` 只描述 primary source 覆盖 / 饱和度维度
- `Readiness Check` 是 round closeout gate；`成功标准` 只描述 pass 后的完成态；`Hard Gates` 只作为可选加严层

## 输入建模

本轮研究直接以 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics` 为起点。

输入对象包括：

- 目录中的 topic seed 文件
- 目录中的已有摘要 / 初步判断 / 问题清单
- 上一轮留下的 `_artifacts` 与相关本地 `_reference`（如果存在）

在正式执行前，必须先把输入目录建模成“研究线注册表（topic registry）”。

每条研究线至少要写清楚：

- 编号
- slug
- 主题标题
- 对应 seed 文件
- 当前假设或当前缺口
- 为什么它值得继续深挖
- 本轮必须回答的问题

### 研究线注册表（topic registry）

topic 数量、编号顺序与 slug 统一以这一节为准；其他 section 只引用，不再维护第二份列表。

| id | slug | title | seed_files | current_hypothesis | why_it_matters | must_answer |
| --- | --- | --- | --- | --- | --- | --- |
| `01` | `engineering-paradigm` | `工程纪律重构与质量防线转移` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/01_engineering_paradigm.md` | `代码生成被商品化后，质量主战场上移到规格、测试、类型约束与变更粒度控制。` | `它决定 AI-Native SDLC 是否会在产出提速后出现质量崩塌，是执行层的核心。` | `下一代规格语言需要精确到什么程度；AI 原生 TDD 如何成为护栏；零人类 review 的边界在哪里；如何打破大批量变更陷阱。` |
| `02` | `organizational-synergy` | `组织拓扑崩塌与中间循环新物种` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/02_organizational_synergy.md` | `AI 放大了组织依赖与治理延迟，中间循环工程师将成为人机混编的调度核心。` | `它决定组织是否能吸收 AI 产能，而不是被审批墙、身份危机和治理等待反噬。` | `决策审批自动化的边界；智能体漂移治理最佳实践；中间循环工程师需要什么工具链；AgentEx 替代 DevEx 时如何留住关键人才。` |
| `03` | `agent-native-infrastructure` | `智能体原生底层基础设施` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/03_agent_native_infrastructure.md` | `企业需要 Agent OS、工作账本、语义层与知识图谱，才能让数字员工在可控边界内稳定运行。` | `它是支撑流程自动化、自愈与多智能体协作的地基，没有基建就没有可扩展的 AI-Native 工程体系。` | `Agent OS 与工作账本的调度器形态；企业数字潜意识如何工程化；红蓝对抗或愤怒智能体如何提升自愈可信度。` |
| `04` | `security-and-governance` | `非确定性系统的安全与治理底线` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/04_security_and_governance.md` | `Agent 级权限、审计、隔离与爆炸半径控制是所有 AI 自动化进入主干业务流的前提。` | `它是 foundation 层的一票否决项，决定企业是否敢把 AI 放进生产级交付链路。` | `Zero Trust 如何落到 Agent 行为控制；爆炸半径是否可计算；AI 安全对抗平台怎样嵌入研发与治理流程。` |

### 当前拓扑基线（Current Topology Baseline）

这里写的是本轮实例化时正式采用的 `topology baseline`；它属于 `PLAN_PATH` 的设计态结构，不是执行中的实时工作日志。

- carry_forward_topics: `01-engineering-paradigm; 02-organizational-synergy; 03-agent-native-infrastructure; 04-security-and-governance`
- new_topics: `none`
- recent_change: `formalized the four seed topics into a single round plan with Wave 2 reserved for cross-topic synthesis`
- pending_topic_candidates: `none; 暂按假设执行为四条主线足以覆盖当前 seed baseline，如 Wave 1 出现重复无法安放的对象再 formalize 新 topic`

当前有效 topic 数量始终由 `topic registry` 派生，不在其他 section 单独维护第二个计数器。

执行中的 topic 增减、推进中的结构变化与最近一次正式化说明写入 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.status.md.Topology Delta / Formalization State`；plan/status 哪一侧尚待同步则写入 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.status.md.Plan / Status Sync.topology_sync_state`。

## 输出契约

### 1. Ground Truth 参考材料

- 所有进入最终推理链条的重要来源，都应以独立 `md` 的 `Authoritative Copy` 形式落在 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference`
- `REFERENCE_DIR` 的完成单位不是“看过这个链接”，而是“这个链接已经被整理成可复用、可定位、可引用、可自给自足的独立 `md` 文档”
- `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference/_INDEX.md` 负责 `30-Second Local Evidence Retrieval`，语义上属于 `navigation layer`

### 2. 输入目录的持续生长

`/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics` 不是只读输入，而是这轮研究的 `living output surface`。

每条研究线对应的 seed 文件都应被更新，并新增下面固定章节：

- `历史摘要（保留，不修改）`
- `本轮新增证据`：每条新增事实都带本地 reference 引用
- `本轮新增机制理解`：从描述上升到为什么这样设计
- `本轮新增趋势与难点`：有时间证据支撑的趋势、实践难点与失败模式
- `当前判断（本轮综合后）`：综合历史内容与本轮新增后的判断，每条判断带本地 reference 引用

规则：

- 历史摘要不删改，只保留
- 所有本轮新增内容进入固定章节
- 每条新增关键判断都必须带本地引用
- 如果某个判断被本轮推翻或修正，在“当前判断”中注明，不删除旧内容

### 3. 过程性 Artifacts

`/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_artifacts` 是 `derived synthesis layer`；它承接 evidence summary、question list 与 cross-topic synthesis，但不替代 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference` 存放证据本体，也不替代 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.status.md` 存放当前执行状态。

至少包括：

- 每条研究线一份 `evidence-summary`
- 每条研究线一份 `question-list`
- 一份横向综合 `W2-cross-topic-synthesis`
- 一份 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_artifacts/README.md`

## Wave 设计与验收

### Wave 0：建立共同 Ground Truth 地基

- purpose: 固定共享地基、共同术语和高可信入口，避免各研究线各自从零开始
- minimum:
  - 至少 `8` 份共享型 ground truth
  - 其中大多数来自官方文档、官方仓库、官方规范或高可信研究
  - 至少 1 份来自安全 / 限制 / 约束相关材料
  - 至少 1 份来自高质量对比、实践复盘或失败分析
  - `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference`、`/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_artifacts` 与 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.status.md` 已经先被初始化

### Foundation Sufficiency Check（Wave 0 -> Wave 1）

进入 Wave 1 前至少确认：

- 核心术语已有工作定义，对象分类已有共享地基
- 每条研究线已有明确深挖起点
- `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference/_INDEX.md` 已经可用

### Wave 1：按研究线分别深挖

- purpose: 把每条研究线从“名称和观点”推进到“机制和证据”
- 每条研究线都要从 5 个视角扩展：
  - 证据
  - 根本机制
  - 趋势
  - 难度
  - 争议 / 失败模式
- minimum per topic:
  - 至少 `8` 份该研究线专属 ground truth
  - 至少 `4` 份一手来源
  - 至少 `2` 份高质量二手分析
  - 至少 `1` 份近期趋势来源
  - 至少 `1` 份限制 / 失败 / 争议来源
- 每条研究线都必须形成一份 `evidence-summary` 和一份 `question-list`

只有当该研究线已完成一轮 stop assessment、`must_answer` 已有本地证据支撑、且限制 / 失败模式补搜已明确记录时，才允许使用 `early_saturation`，并且必须写入 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.status.md.Wave 1`。

### Wave 2：横向比对与综合判断

- purpose: 把分题结果重新收束成整体结构和跨主题判断
- minimum:
  - 每个横向判断都能追溯到具体 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference/*.md`
  - 每条研究线至少有 2 个与其他研究线发生交叉验证的结论
  - 明确区分“硬事实”“分析判断”“趋势推测”

### Readiness Check：最终验收闸门

至少覆盖下面 5 项：

- `30-Second Local Evidence Retrieval`
- 每线“机制 + 趋势 + 难点”检查
- 横向综合检查
- 拓扑稳定性检查
- 接手可继续性检查

### 搜够了没有：停止条件（topic-level stop condition）

每条研究线在 stop assessment 完成前，`topic_stop_decision` 保持 `not_assessed`。

完成一轮搜集并进入 stop assessment 后，必须把当前状态明确归类为 `continue / early_saturation / suspend / archive / redirect` 之一。

其中，只有同时满足下面条件，才允许把该研究线视为“已搜够一轮”并进入 `early_saturation / archive / redirect` 这类停止型决策：

- 核心对象清单已经稳定，不再持续新增关键名字
- 新搜到的材料大多在重复已知事实，而不是贡献新信息
- 该研究线的固定问题都已经有证据支撑
- 至少有 1 轮对“反例、限制、争议”的专门补搜
- 已完成一次“官方说法 vs 第三方验证 / 实践证据 / 事故复盘”交叉核验
- 所有重要但未解的问题，都已经被明确归类为 `continue / early_saturation / suspend / archive / redirect`

补充判定：

- `continue`：当前线仍有高价值缺口，且继续深挖预期能改变判断质量
- `early_saturation`：该维度已明显饱和，继续搜索主要只会引入低质量重复材料
- `suspend`：重要，但当前受限于材料、访问或时机，暂不继续
- `archive`：继续下钻的边际收益低，短期内不太可能改变核心判断
- `redirect`：问题重心应转移到其他研究线或新 formalized topic

## 研究线的具体目标

### 研究线 01：engineering-paradigm

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 01/engineering-paradigm`
- wave1_deepen_focus: `把“质量防线转移”拆成规格、测试、约束、变更粒度控制四条证据链，并找到它们在企业流程中的组合方式`
- evidence_priority: `结构化规格方法、AI-assisted TDD、类型系统/约束系统、CI/CD 小批量控制、工程实践复盘`
- difficulty_focus: `区分口号式工程纪律和真正可执行的机制，避免只收集宣称没有验证`
- trend_question: `未来 2 到 3 年内，review、TDD、规格工程和 release discipline 之间的主次关系会如何重排`
- stop_assessment_focus: `必须回答质量防线是否真的上移、上移到哪些制品、以及什么条件下仍需要人工兜底`

### 研究线 02：organizational-synergy

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 02/organizational-synergy`
- wave1_deepen_focus: `把“中间循环”从概念拆成岗位职责、协作拓扑、工具需求、激励机制和治理接口`
- evidence_priority: `组织设计案例、人机协作流程、平台治理实践、角色演化论证、开发者体验与生产力对照材料`
- difficulty_focus: `识别真实组织瓶颈是在审批、依赖、信任还是身份认同，避免把所有问题都归结为培训不足`
- trend_question: `中间循环工程师、PM、Staff 工程师与平台团队之间会形成怎样的新分工`
- stop_assessment_focus: `必须回答组织如何吸收 AI 产能，以及哪些管理机制不升级就会成为硬瓶颈`

### 研究线 03：agent-native-infrastructure

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 03/agent-native-infrastructure`
- wave1_deepen_focus: `把 Agent OS、工作账本、知识图谱、语义层与多智能体编排拆成可落地基础设施栈`
- evidence_priority: `agent runtime、身份与权限模型、任务账本、知识图谱工程、自愈系统、multi-agent orchestration`
- difficulty_focus: `避免把“平台愿景图”误当成已证实架构，需要区分可运行系统、实验性原型和概念比喻`
- trend_question: `企业未来会优先投资哪一层基建，哪些层会先标准化，哪些仍会高度定制`
- stop_assessment_focus: `必须回答没有这些基建时 AI-Native SDLC 为什么不可扩展，以及最小可行地基长什么样`

### 研究线 04：security-and-governance

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 04/security-and-governance`
- wave1_deepen_focus: `把权限、隔离、审计、爆炸半径、对抗测试和多智能体振荡风险串成统一治理模型`
- evidence_priority: `agent security、Zero Trust、least privilege、runtime audit、policy enforcement、事故复盘、对抗评测`
- difficulty_focus: `识别“看似合规但被模型规避”的狭义满足问题，并把治理速度落后于生成速度的断层说清楚`
- trend_question: `企业会先在哪些高风险接口上建立平台级默认安全，以及审计与拦截会多大程度自动化`
- stop_assessment_focus: `必须回答哪些安全底线是 AI 自动化进入主线前的先决条件，以及爆炸半径能否被计算和阻断`

## 成功标准（post-pass success state）

达到下面状态，才算真正满足目标：

- `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference` 中有一批高可信、可追溯的 ground truth 文档
- 每条研究线至少形成一组可复用证据包，而不是临时搜索结果
- 对每条研究线都能解释机制、趋势和难点
- 每个重要判断都能追溯到本地 reference 文档
- 对趋势、难度、争议都有专门证据，而不是顺手一提
- 可以明确说清楚“哪些问题不是没做，而是被主动 `suspend`，以及为什么”
- 后续新的 agent 接手时，只看 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics + /Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference + /Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_artifacts + /Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.status.md + /Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.queue.md` 就能继续往下研究

## Hard Gates（可选）

默认不启用；只有当 `hard_gates_enabled = yes` 时，才把它叠加到 `Readiness Check` 上。

启用时至少检查：

- 没有 P0 级结论处于“只有单一弱来源支撑”的状态
- 所有关键术语都在跨主题范围内完成口径对齐
- 所有高价值结论都已明确标注“硬事实 / 分析判断 / 趋势推测”
- 至少完成一轮针对反例和失败模式的专门检索
