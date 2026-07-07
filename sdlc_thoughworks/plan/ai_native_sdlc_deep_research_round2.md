# AI-Native SDLC Deep Research Plan (ThoughtWorks Topics, Round 2)

> 对应状态文件：`/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round2.status.md`
> 对应执行队列：`/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round2.queue.md`
> 本文件只记录设计态蓝图；实时状态与连续动作分别写入 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round2.status.md` 与 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round2.queue.md`。

## Instance Config

> 这是本轮实例参数的唯一设计态注册点。除 `topic registry` 本体外，后文不再重复定义这些参数。

| field | value |
| --- | --- |
| `plan_name` | `AI-Native SDLC Deep Research Plan (ThoughtWorks Topics, Round 2)` |
| `template_version` | `v8` |
| `round_label` | `二轮` |
| `plan_path` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round2.md` |
| `status_path` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round2.status.md` |
| `queue_path` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round2.queue.md` |
| `seed_dir` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics` |
| `reference_dir` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference` |
| `artifact_dir` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_artifacts` |
| `final_deliverable` | `“AI-Native 软件工程新常态（Next-Gen SDLC）”白皮书 / SOP 的第二轮强化稿，以及更接近企业落地治理方案的操作级蓝图` |
| `audience` | `内部战略研究、平台工程、研发管理、安全治理负责人，以及后续面向企业 IT 决策者的外部方案读者` |
| `round_focus` | `补 operation-grade gaps / 补企业可执行控制面 / 补 incident 与 role/tool surface / 压实 whitepaper-ready 论证链` |
| `derived_topic_count` | `= count(topic registry entries)` |
| `wave0_shared_doc_floor` | `6` |
| `wave1_doc_floor_per_topic` | `4` |
| `primary_source_floor` | `2` |
| `secondary_source_floor` | `1` |
| `recent_source_floor` | `1` |
| `limitation_source_floor` | `1` |
| `hard_gates_enabled` | `no` |

## 调研目的与服务对象

这轮 Deep Research 不是重做 `round1`。

真正的目的是：在 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.status.md` 与 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_artifacts/W2-cross-topic-synthesis.md` 已经形成的一轮基线上，继续把最影响企业落地可信度的 operational gaps 压实成第二轮证据包。

最终产出的读者是：`内部战略研究、平台工程、研发管理、安全治理负责人，以及后续面向企业 IT 决策者的外部方案读者`

本轮主任务是：`补 operation-grade gaps / 补企业可执行控制面 / 补 incident 与 role/tool surface / 压实 whitepaper-ready 论证链`

这份最终产出至少要满足下面要求：

- 不是只补更多链接，而是优先补最影响企业落地判断质量的机制缺口
- 不重复 `round1` 已经稳定的结论，重点处理能显著改变实施建议的 unresolved gaps
- 每个新增结论都能回扣到 `round1` 的 cross-topic stack，而不是形成新的平行叙事
- 第二轮结束后，应更接近“企业该如何落地”的操作级蓝图，而不只是概念性白皮书

权威信源优先规则（最高优先级，不可违反）：

> 当权威一手来源已经足以支撑某个判断时，不为满足配额额外引入低质量二手来源。配额是防止搜太浅的下限，不是必须凑满的目标。宁缺毋滥。

## 本轮核心缺口

- Gap 1: `Topic 03 agent-native-infrastructure` 仍缺 production-grade `work ledger`、授权/预算/任务状态一体化设计与企业 ontology extraction 的更强公开证据。
- Gap 2: `Topic 02 organizational-synergy` 仍缺 middle-loop operator 的日常 tool surface、staff engineer role redesign 和失败案例证据。
- Gap 3: `Topic 04 security-and-governance` 仍缺更贴近 software delivery pipeline 的 incident corpora 与 diff/tool-call-specific blast-radius evidence。
- Gap 4: `round1` 已足以形成 baseline narrative，但距离更外化的 whitepaper-ready 或 enterprise-playbook-ready 论证链还有一段距离。

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

本轮研究仍直接以 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics` 为起点，但默认承接：

- `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.status.md`
- `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.queue.md`
- `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_artifacts/W2-cross-topic-synthesis.md`
- `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference/_INDEX.md`

在正式执行前，必须把 `round1 closeout` 中的 remaining gaps 映射成新的优先级，而不是重新从零定义问题。

### 研究线注册表（topic registry）

topic 数量、编号顺序与 slug 统一以这一节为准；其他 section 只引用，不再维护第二份列表。

| id | slug | title | seed_files | current_hypothesis | why_it_matters | must_answer |
| --- | --- | --- | --- | --- | --- | --- |
| `01` | `engineering-paradigm` | `工程纪律重构与质量防线转移` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/01_engineering_paradigm.md` | `round1 已经证明质量防线向规格、测试、约束和变更粒度控制转移；round2 的关键是补 AI-specific 端到端 enforced pipeline 例证。` | `它决定交付控制到底能否真正平台化，而不是停留在方法论。` | `有没有更直接的企业案例证明 `spec -> test -> code -> slice -> merge -> canary` 被强制执行；formal guard 与 human-review reduction 的边界能否再压实。` |
| `02` | `organizational-synergy` | `组织拓扑崩塌与中间循环新物种` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/02_organizational_synergy.md` | `round1 已经证明组织 bottleneck 的存在；round2 的关键是补 middle-loop operator 工具面、staff role redesign 与失败案例。` | `它决定企业是否知道该配什么岗位、工具与管理节奏，而不是只知道“组织会变”。` | `middle-loop operator 的最小工具面是什么；staff engineer 如何不被纯协调吞没；哪些 adoption program 失败、为什么失败。` |
| `03` | `agent-native-infrastructure` | `智能体原生底层基础设施` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/03_agent_native_infrastructure.md` | `round1 已经证明 Agent OS 是分层栈；round2 的关键是补 `work ledger` 与 enterprise ontology engineering，使平台建议更可执行。` | `它是当前最影响 enterprise implementation guidance 的缺口，优先级最高。` | `work ledger 到底该记录哪些实体、状态和 control fields；预算、授权、验收标准与恢复点怎样进一个统一设计；企业知识抽取如何从 tickets/postmortems/logs 落到生产任务流。` |
| `04` | `security-and-governance` | `非确定性系统的安全与治理底线` | `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/04_security_and_governance.md` | `round1 已经把 identity 与 graph-based blast-radius proxy 补强；round2 的关键是补 delivery-pipeline incident corpora 和 delivery-specific risk scoring。` | `它决定白皮书能否从“安全必须平台化”进一步推进到“哪些信号最适合做 release-risk gate”。` | `有哪些更直接的软件交付事故或近事故案例；diff/tool-call-specific blast radius 是否已有公开 proxy；能否和 Topic 01 的 merge/deploy controls 合并成统一 release-risk gate。` |

### 当前拓扑基线（Current Topology Baseline）

这里写的是本轮实例化时正式采用的 `topology baseline`；它属于 `PLAN_PATH` 的设计态结构，不是执行中的实时工作日志。

- carry_forward_topics: `01-engineering-paradigm; 02-organizational-synergy; 03-agent-native-infrastructure; 04-security-and-governance`
- new_topics: `none`
- recent_change: `round2 inherits the round1 topology and narrows the focus to the highest-value unresolved operational gaps`
- pending_topic_candidates: `none; unless round2 evidence forces a split between runtime ledger design and organization operating model tooling`

当前有效 topic 数量始终由 `topic registry` 派生，不在其他 section 单独维护第二个计数器。

执行中的 topic 增减、推进中的结构变化与最近一次正式化说明写入 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round2.status.md.Topology Delta / Formalization State`；plan/status 哪一侧尚待同步则写入 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round2.status.md.Plan / Status Sync.topology_sync_state`。

## 输出契约

### 1. Ground Truth 参考材料

- 所有进入最终推理链条的重要来源，都应以独立 `md` 的 `Authoritative Copy` 形式落在 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference`
- `REFERENCE_DIR` 的完成单位不是“看过这个链接”，而是“这个链接已经被整理成可复用、可定位、可引用、可自给自足的独立 `md` 文档”
- `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference/_INDEX.md` 负责 `30-Second Local Evidence Retrieval`，语义上属于 `navigation layer`

### 2. 输入目录的持续生长

`/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics` 不是只读输入，而是这轮研究的 `living output surface`。

每条研究线对应的 seed 文件都应继续被更新，并仅在固定章节下追加 `round2` 新增内容。

规则：

- 不改写 round1 已形成的历史摘要和已稳定判断，除非 round2 证据明确推翻
- 所有 round2 新证据继续进入固定章节
- 所有 round2 关键判断都必须带本地引用
- 如果 round2 改变了 round1 的优先级或架构判断，在“当前判断”中显式写出变化

### 3. 过程性 Artifacts

`/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_artifacts` 是 `derived synthesis layer`；它承接 evidence summary、question list 与 cross-topic synthesis，但不替代 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference` 存放证据本体，也不替代 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round2.status.md` 存放当前执行状态。

至少包括：

- 对被继续推进的研究线更新 `evidence-summary`
- 对被继续推进的研究线更新 `question-list`
- 一份横向综合 `W2-cross-topic-synthesis` 的 round2 增量
- 必要时新增一份更外化的 whitepaper-ready outline artifact

## Wave 设计与验收

### Wave 0：建立 round2 continuation ground truth

- purpose: 固定 `round1 -> round2` 的 continuation context，避免重复搜索已稳定地基
- minimum:
  - 至少 `6` 份共享或跨 topic continuation references
  - 其中至少 2 份直接服务于 Topic 03 的 `work ledger / durable task system` 缺口
  - 至少 1 份直接服务于 Topic 02 的 `middle-loop tool surface / role redesign` 缺口
  - 至少 1 份直接服务于 Topic 04 的 `delivery incident / release-risk` 缺口
  - `round1 closeout` 的 read path 已在 `status` 与 `queue` 中被显式承接

### Foundation Sufficiency Check（Wave 0 -> Wave 1）

进入 Wave 1 前至少确认：

- round1 已形成的稳定结论和 round2 要补的 operational gap 已被清晰分开
- Topic 03 与 Topic 02 的优先级排序已经明确
- `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference/_INDEX.md` 已能作为 round1 + round2 的统一导航入口

### Wave 1：按研究线做定向补强

- purpose: 不再平均铺开四条线，而是优先打深仍能改变企业实施建议的高价值缺口
- 每条被继续推进的研究线都要从 5 个视角扩展：
  - 证据
  - 根本机制
  - 趋势
  - 难度
  - 争议 / 失败模式
- minimum per active topic:
  - 至少 `4` 份该研究线 round2 新增 ground truth
  - 至少 `2` 份一手来源
  - 至少 `1` 份高质量二手分析
  - 至少 `1` 份近期趋势来源
  - 至少 `1` 份限制 / 失败 / 争议来源
- 每条被继续推进的研究线都必须更新 `evidence-summary` 和 `question-list`

只有当该研究线已完成新一轮 stop assessment、`must_answer` 已有 round2 本地证据支撑、且限制 / 失败模式补搜已明确记录时，才允许使用 `early_saturation`，并且必须写入 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round2.status.md.Wave 1`。

### Wave 2：横向综合与 implementation-grade synthesis

- purpose: 把 round2 新证据回扣到 round1 control-stack model，并更接近 enterprise implementation guidance
- minimum:
  - 每个新增横向判断都能追溯到具体 `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference/*.md`
  - 至少补强 `Topic 03 x Topic 02`、`Topic 03 x Topic 04`、`Topic 01 x Topic 04` 三条交叉线
  - 明确区分“hard facts”“analysis judgments”“implementation recommendations”“trend forecasts”

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
- wave1_deepen_focus: `只补仍会改变实施建议的缺口，尤其是 AI-specific enforced pipeline cases 与 formal guard adoption boundaries`
- evidence_priority: `企业流水线控制案例、formal guard adoption、review reduction boundary evidence、release-risk gate examples`
- difficulty_focus: `避免重复 round1 已稳定的 spec/test/constraint 论证，把新增注意力集中到真正影响 rollout guidance 的证据`
- trend_question: `企业是否会把 small-batch enforcement 做成平台默认，而不是团队约定`
- stop_assessment_focus: `必须回答哪些新增证据会真实改变 Topic 01 的 rollout recommendation，而不是只增加重复论证`

### 研究线 02：organizational-synergy

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 02/organizational-synergy`
- wave1_deepen_focus: `把 middle-loop 从组织概念压到操作台、工具面和角色冲突处理机制`
- evidence_priority: `middle-loop operator 工具面、AI workforce 管理岗位、staff role redesign、失败 adoption case`
- difficulty_focus: `区分“需要新岗位”与“现有岗位重构”这两类说法，避免把宏观趋势当成操作级建议`
- trend_question: `middle-loop function 更可能沉到平台团队、EM 体系，还是形成独立运营角色`
- stop_assessment_focus: `必须回答企业到底该配什么工具和角色，而不是只知道“组织会变化”`

### 研究线 03：agent-native-infrastructure

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 03/agent-native-infrastructure`
- wave1_deepen_focus: `把 Agent OS 从分层框架推进到 work ledger、task accounting、authorization/budget coupling 和 ontology extraction 的可执行设计`
- evidence_priority: `durable task systems、agent run ledger、budget/capability/audit coupling、artifact-first execution、enterprise ontology extraction`
- difficulty_focus: `避免把 generic workflow engines 误当成 work ledger；只保留能回答 control fields 与 durable state 的来源`
- trend_question: `企业级 agent runtime 会不会像 CI/CD 一样分化出 ledger、policy、memory、telemetry 的稳定部件`
- stop_assessment_focus: `必须回答 work ledger 是否足以成为 enterprise implementation recommendation 的正式层，而不只是抽象概念`

### 研究线 04：security-and-governance

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 04/security-and-governance`
- wave1_deepen_focus: `从 identity 和 graph proxy 继续推进到 delivery-specific incident evidence 与 release-risk gate design`
- evidence_priority: `software-delivery incidents、near misses、diff or tool-call risk scoring、release gate controls、attack-path-to-release policy coupling`
- difficulty_focus: `避免搜到泛 AI security 事故却无法回扣 software delivery 主干链路`
- trend_question: `blast-radius control 会不会最终与 Topic 01 的 merge/deploy controls 合流成一套 release-risk gate`
- stop_assessment_focus: `必须回答 security controls 如何和 delivery controls 联锁，而不是并列存在`

## 成功标准（post-pass success state）

达到下面状态，才算真正满足目标：

- `/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference` 中新增一批直接针对 round2 operational gaps 的高可信 ground truth
- 至少 Topic 03 和 Topic 02 形成新一轮可复用证据包
- `W2-cross-topic-synthesis` 明确补上 implementation-grade recommendations，而不只停留在 round1 的控制栈判断
- 对每个 high-value unresolved gap 都能明确归类为 `continue / early_saturation / suspend / archive / redirect`
- whitepaper 或 SOP 的外化路径比 round1 更接近企业执行方案
