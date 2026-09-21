# 需求工程 Topics Deep Research 一轮
> 状态：本轮已收口（completed / closed_for_current_round）。过程件仅作回溯，修改 final/ 勿据本文，以 final/ 现状为准。

> 对应状态文件：`requirements_engineering/plan/dr-round-1.status.md`
> 对应执行队列：`requirements_engineering/plan/dr-round-1.queue.md`
> 本文件只记录设计态蓝图；实时状态与连续动作分别写入 `requirements_engineering/plan/dr-round-1.status.md` 与 `requirements_engineering/plan/dr-round-1.queue.md`。

## Instance Config

> 这是本轮实例参数的唯一设计态注册点。除 `topic registry` 本体外，后文不再重复定义这些参数。

| field | value |
| --- | --- |
| `plan_name` | `需求工程 Topics Deep Research 一轮` |
| `template_version` | `v8` |
| `round_label` | `一轮` |
| `plan_path` | `requirements_engineering/plan/dr-round-1.plan.md` |
| `status_path` | `requirements_engineering/plan/dr-round-1.status.md` |
| `queue_path` | `requirements_engineering/plan/dr-round-1.queue.md` |
| `seed_dir` | `requirements_engineering/deep_research_topics/` |
| `reference_dir` | `requirements_engineering/deep_research_topics/_reference/` |
| `artifact_dir` | `requirements_engineering/deep_research_topics/_artifacts/` |
| `final_deliverable` | `面向 AI 编程时代的需求表达方法论综合指南（6 topic 教程级深度材料 + 1 份选型建议 + 1 份升级版 claims-audit）` |
| `audience` | `产品负责人、系统架构师、AI 编程实践者；要求 KOL-grade 证据 + 标准合规 + 企业可采纳` |
| `round_focus` | `exploitation-first；单点 exploration 聚焦 Topic 06（coding agent / harness 中的需求格式实证）` |
| `derived_topic_count` | `= count(topic registry entries)` |
| `wave0_shared_doc_floor` | `12` |
| `wave1_doc_floor_per_topic` | `8` |
| `primary_source_floor` | `5` |
| `secondary_source_floor` | `2` |
| `recent_source_floor` | `1；Topic 06 覆写为 3` |
| `limitation_source_floor` | `2` |
| `hard_gates_enabled` | `yes` |

Floor 覆写理由：

- `primary_source_floor = 5`：本轮定位为"KOL-grade + 标准 + 企业可采纳"，一手来源（ISO/IEC/IEEE、INCOSE、IEEE 论文、KOL 原著）必须充足，不能让二手转述挤占判断基础。
- `limitation_source_floor = 2`：`requirements_engineering/deep_research_topics/claims-audit.md` 的立场是"已知断言多为 C/D/E 级"，必须用专门的限制 / 争议 / 失败模式材料双证。
- `recent_source_floor` 对 Topic 06 覆写为 `3`：coding agent / harness 工具链在 2024Q3–2026Q1 变化极快，单份近期来源不足以支撑事实标准判断。
- `hard_gates_enabled = yes`：本轮明确要求 solid / 合规，默认 off 达不到审阅门槛。

## 调研目的与服务对象

这轮 Deep Research 不是为了产出调研笔记本身。

真正的目的是：为"面向 AI 编程时代的需求表达方法论综合指南（6 topic 教程级深度材料 + 1 份选型建议 + 1 份升级版 claims-audit）"提供可靠的原材料地基。

最终产出的读者是：产品负责人、系统架构师、AI 编程实践者；要求 KOL-grade 证据 + 标准合规 + 企业可采纳

本轮主任务是：exploitation-first；单点 exploration 聚焦 Topic 06（coding agent / harness 中的需求格式实证）

这份最终产出至少要满足下面要求：

- 系统性：覆盖关键维度，不遗漏，不失衡
- 逻辑性：每个判断都有证据支撑，推理链条可追溯
- 一致性：跨主题术语统一、口径统一、评估框架统一
- 专业可读：默认读者是专业人士，不需要手把手解释，但需要准确、严谨、无歧义

权威信源优先规则（最高优先级，不可违反）：

> 当权威一手来源已经足以支撑某个判断时，不为满足配额额外引入低质量二手来源。配额是防止搜太浅的下限，不是必须凑满的目标。宁缺毋滥。

本轮对来源质量做显式分级，Wave 0 / Wave 1 入库按下面顺序优先选择：

- Tier A（首选、必须）：ISO / IEC / IEEE 标准（29148、26262）、INCOSE 官方（GTWR v4 Summary Sheet + 完整版）、IEEE 会议论文（RE09 原文等）、同行评审期刊
- Tier B（强烈推荐）：Alistair Mavin 官方站（alistairmavin.com/ears）、Jama / Visure 官方产品文档、Atlassian 官方、Kent Beck / Mike Cohn / Jeff Patton / Alistair Cockburn / Gojko Adzic / Matt Wynne 的书籍与正式演讲、Martin Fowler bliki
- Tier C（可用）：大厂工程博客（GitHub、Microsoft、Google、AWS、Atlassian Engineering、Spotify 等）、Cucumber 官方文档与社区规则、Seb Rose 等 KOL 正式出版物
- Tier D（有限使用）：厂商白皮书 / 案例研究——仅作为"厂商自述现状"引用，不作为效果证据；与 `requirements_engineering/deep_research_topics/claims-audit.md` 的评估对齐
- Tier E（只作趋势信号、不作证据）：Medium / Reddit / LinkedIn / X 上的 KOL 发言——需要至少一条 Tier A/B/C 来源双重验证
- Tier F（禁用为 ground truth）：SEO 聚合页、内容农场、无来源短文

## 本轮核心缺口

- Gap 1: ISO/IEC/IEEE 29148 ↔ INCOSE GTWR v4 ↔ EARS 的三方正式对齐关系仍是转述，`requirements_engineering/deep_research_topics/topic-01-re-landscape-and-paradigm-map.md` 与 `requirements_engineering/deep_research_topics/topic-03-ears-tutorial.md` 需要一手标准文本或官方摘要支撑。
- Gap 2: KOL 在 2023–2026 的最新立场是否调整——Mike Cohn 对 AI 生成 User Story、Gojko Adzic 对 LLM 时代 BDD、Alistair Mavin 对 Generative AI × EARS 的公开表达——Topic 02/03/05 目前引用的多为历史书籍与博文，未覆盖近两年更新。
- Gap 3: 最强 coding agent / harness 中实际采用哪种需求 / 规约格式的第一手观察——Cursor Rules、Anthropic Claude Code（CLAUDE.md / Skills / Plugins）、OpenAI Codex CLI + AGENTS.md、GitHub Spec Kit、Kiro Spec、OpenSpec、Amp、Aider、Continue、Cline 等官方约定、模板库与工程团队实战案例，目前仅以"揣测"形式出现在 Topic 04 §4.6。

## Control Map

本轮实例 plan 只保留最小控制绑定，避免在实例正文里重写模板级 authority tables。

### Minimal Runtime Bindings

- `PLAN_PATH` 只记录设计态蓝图、实例参数、拓扑基线、Wave 设计与验收；不写实时进度、阻塞、worklog 或 active queue
- `STATUS_PATH` 只记录当前状态、gate、阻塞、拓扑 delta、分支处置与恢复上下文；不重写完整设计态蓝图
- `QUEUE_PATH` 是唯一连续派工入口；只记录 active queue、blocked state、refill pool 与 promotion rules
- `setup_ready` 是 gate，不是独立 wave；它表示 execution surface 已初始化完成、尚未关闭第一步 `Wave 0` 证据落库
- 默认 gate 路径为 `instantiation_complete -> setup_ready -> wave0_complete -> wave1_complete -> wave2_complete -> readiness_passed`
- `topic_stop_decision` 是研究线级决策；`primary_source_coverage` 只描述 primary source 覆盖 / 饱和度维度
- `Readiness Check` 是 round closeout gate；`成功标准` 只描述 pass 后的完成态；`Hard Gates` 作为加严层叠加到 `Readiness Check`

## 输入建模

本轮研究直接以 `requirements_engineering/deep_research_topics/` 为起点。

输入对象包括：

- 目录中的 topic seed 文件：`topic-01-re-landscape-and-paradigm-map.md`、`topic-02-user-story-tutorial.md`、`topic-03-ears-tutorial.md`、`topic-04-future-trends-and-evidence.md`、`topic-05-integration-bdd-selection.md`
- 目录中的已有摘要 / 初步判断 / 问题清单：`claims-audit.md`、`references-by-topic.md`、`references-full.md`、`README.md`
- 上一轮留下的 `_artifacts` 与相关本地 `_reference`：本轮为第一轮，尚无历史落库

在正式执行前，必须先把输入目录建模成"研究线注册表（topic registry）"。

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
| 01 | re-landscape | 需求工程范式地图 | requirements_engineering/deep_research_topics/topic-01-re-landscape-and-paradigm-map.md | 双坐标系（用户意图 vs 系统契约 × 结构化程度）+ 12 行范式速查表是当前工作假设；但 User Story / EARS / BDD / Use Case 2.0 / MBSE / 决策表 之间的正式对齐关系仍缺权威锚点 | 地图是其他 5 个 topic 的底座，地图不准则选型与判断悬空 | ISO/IEC/IEEE 29148:2018 与 INCOSE GTWR v4 与 EARS 三方正式对齐关系；Use Case 2.0 与 User Story 的官方边界说明；SysML v2 / MBSE 与文本需求的分工主张 |
| 02 | user-story | User Story 教程与最佳实践 | requirements_engineering/deep_research_topics/topic-02-user-story-tutorial.md | Beck / Cohn / Patton / Cockburn / Fowler 的经典材料已覆盖基础；但 INVEST 的企业落地反例与修复模板、AC 与 Gherkin 的权威分工仍未系统化 | User Story 是 AI 编程时代的上游意图层事实标配 | Kent Beck、Mike Cohn、Alistair Cockburn、Jeff Patton、Martin Fowler 的原始表述与 2023–2026 最新公开立场；INVEST 常见违反与企业级修复模板；Enabler / Spike / Job Story 的权威定义边界 |
| 03 | ears | EARS 教程与合规 | requirements_engineering/deep_research_topics/topic-03-ears-tutorial.md | Mavin 2009 原文 + INCOSE GTWR + Jama / Visure 工具侧已有系统定义；但 EARS 在非安全关键（SaaS）域的工业证据薄弱，与 INCOSE GTWR v4 规则的逐条映射缺一手材料 | EARS 是 AI 编程时代的系统契约层顶梁柱 | Mavin 2009 原论文要点与后续补遗；EARS 五模式 + 复合的官方语法与示例；与 INCOSE GTWR v4 规则的逐条映射；EARS 在纯软件 / SaaS 场景的权威实证；何时不用 EARS 的一手准则 |
| 04 | future-trends | 需求表达未来趋势（轻揣测） | requirements_engineering/deep_research_topics/topic-04-future-trends-and-evidence.md | 5 条前瞻维度（Spec-as-Code、多模态、Agent 反修 Spec、Embedding 化、监管可追溯）大致成立——原 §4.6 IDE 需求原语维度已剥离到 Topic 06 | 下一代 SDLC 方向判断 | 5 条前瞻维度各自在 2023–2026 的早期信号是否真实出现；哪些已被验证 / 证伪；EU AI Act / NIST AI RMF / ISO 42001 对"结构化需求作为审计凭证"的具体条款 |
| 05 | integration-bdd | Story × EARS × BDD 管道与选型 | requirements_engineering/deep_research_topics/topic-05-integration-bdd-selection.md | 三轨分层 + 九维选型矩阵是当前推荐；但矩阵每行都需 KOL / 标准背书；企业三轨治理的真实案例未充分覆盖 | 三轨如何组合是方法论落地的核心 | Gojko Adzic《Specification by Example》与 Matt Wynne《Example Mapping》的当前立场；金融 / 汽车 / 航空 / 医疗 等大型组织三轨治理的公开案例；决策表 / DMN 与 EARS 的权威边界说明；Cucumber 官方对 "from story to scenario" 的正式主张 |
| 06 | agent-format | 最强 Coding Agent / Harness 的需求格式实证与选型 | requirements_engineering/deep_research_topics/topic-06-agent-format.md | 结构化 Markdown（含 EARS 元素）+ 明确任务分解 + 项目规约文件（CLAUDE.md / AGENTS.md / .cursor/rules）可能是当前最佳组合，但证据不足 | 本轮唯一需要"新观察"的研究线；决定方法论能否对齐 2026 工具链 | Cursor Rules、Anthropic Claude Code（CLAUDE.md / Skills / Plugins）、OpenAI Codex CLI + AGENTS.md 标准、GitHub Spec Kit、Kiro Spec、OpenSpec、Amp、Aider、Continue、Cline 等各自推荐的需求 / 规约格式；官方模板库；工程团队公开采用案例；已观察到的失败模式；最终给出方法论选型建议 |

### 当前拓扑基线（Current Topology Baseline）

这里写的是本轮实例化时正式采用的 `topology baseline`；它属于 `PLAN_PATH` 的设计态结构，不是执行中的实时工作日志。

- carry_forward_topics: `01 re-landscape / 02 user-story / 03 ears / 04 future-trends / 05 integration-bdd`
- new_topics: `06 agent-format（seed 文件 requirements_engineering/deep_research_topics/topic-06-agent-format.md 尚未创建；将在 execution entry 后的 current_task 中由 QUEUE_PATH 调度完成）`
- recent_change: `首次实例化；将原 topic-04 §4.6 "IDE 需求原语" 剥离为独立研究线 06`
- pending_topic_candidates: `none`

当前有效 topic 数量始终由 `topic registry` 派生，不在其他 section 单独维护第二个计数器。

执行中的 topic 增减、推进中的结构变化与最近一次正式化说明写入 `requirements_engineering/plan/dr-round-1.status.md` 的 `Topology Delta / Formalization State`；plan/status 哪一侧尚待同步则写入 `requirements_engineering/plan/dr-round-1.status.md` 的 `Plan / Status Sync.topology_sync_state`。

## 输出契约

### 1. Ground Truth 参考材料

- 所有进入最终推理链条的重要来源，都应以独立 `md` 的 `Authoritative Copy` 形式落在 `requirements_engineering/deep_research_topics/_reference/`
- `REFERENCE_DIR` 的完成单位不是"看过这个链接"，而是"这个链接已经被整理成可复用、可定位、可引用、可自给自足的独立 `md` 文档"
- `requirements_engineering/deep_research_topics/_reference/_INDEX.md` 负责 30 秒本地证据检索入口，语义上属于 `navigation layer`
- 命名规范：共享地基 `00-shared-<source-slug>.md`；研究线专属 `<NN>-<topic-slug>-<source-slug>.md`，其中 `<NN>` 与 `<topic-slug>` 严格来自本 plan 的研究线注册表

### 2. 输入目录的持续生长

`requirements_engineering/deep_research_topics/` 不是只读输入，而是这轮研究的 `living output surface`。

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
- 如果某个判断被本轮推翻或修正，在"当前判断"中注明，不删除旧内容

### 3. 过程性 Artifacts

`requirements_engineering/deep_research_topics/_artifacts/` 是 `derived synthesis layer`；它承接 evidence summary、question list 与 cross-topic synthesis，但不替代 `REFERENCE_DIR` 存放证据本体，也不替代 `STATUS_PATH` 存放当前执行状态。

至少包括：

- 每条研究线一份 `evidence-summary`（命名 `<NN>-<topic-slug>-evidence-summary.md`）
- 每条研究线一份 `question-list`（命名 `<NN>-<topic-slug>-question-list.md`）
- 一份横向综合 `W2-cross-topic-synthesis.md`
- 一份本轮专有 `W2-selection-matrix-v2.md`：九维选型矩阵的 KOL / 标准背书升级版，每行带来源
- 一份本轮专有 `W2-claims-audit-v2.md`：基于新证据升级 `requirements_engineering/deep_research_topics/claims-audit.md` 中各条证据强度
- 一份 `requirements_engineering/deep_research_topics/_artifacts/README.md`

## Wave 设计与验收

### Wave 0：建立共同 Ground Truth 地基

- purpose: 固定共享地基、共同术语和高可信入口，避免各研究线各自从零开始
- minimum:
  - 至少 12 份共享型 ground truth
  - 其中大多数来自官方文档、官方仓库、官方规范或高可信研究
  - 至少 1 份来自安全 / 限制 / 约束相关材料
  - 至少 1 份来自高质量对比、实践复盘或失败分析
  - `requirements_engineering/deep_research_topics/_reference/`、`requirements_engineering/deep_research_topics/_artifacts/` 与 `requirements_engineering/plan/dr-round-1.status.md` 已经先被初始化

本轮 Wave 0 必备清单（12 份下限中至少覆盖下列 Tier A/B 条目）：

- ISO/IEC/IEEE 29148:2018（需求工程标准）概要或官方摘要（Tier A）
- INCOSE GTWR v4 Summary Sheet（Tier A）
- INCOSE GTWR v4 完整文档或公开摘录（Tier A）
- Alistair Mavin et al. *Easy Approach to Requirements Syntax (EARS)* RE09 原论文（Tier A）
- Kent Beck *Extreme Programming Explained* 中 User Story 章节或等价一手材料（Tier B）
- Mike Cohn *User Stories Applied* 要点或 Mountain Goat Software 官方文章（Tier B）
- Jeff Patton *User Story Mapping* 要点或官方演讲（Tier B）
- Martin Fowler bliki `UserStory` 与 `GivenWhenThen`（Tier B）
- Cucumber / Gherkin 官方文档与语法规则（Tier C）
- ISO 26262 Part 8（需求相关条款）概要或官方摘要（Tier A，供 Topic 03 / 05 安全关键锚点）
- Cursor Rules 官方文档（Tier B/C，Topic 06 基线之一）
- Anthropic Claude Code 官方文档 CLAUDE.md / Skills / Plugins 规范（Tier B/C，Topic 06 基线之二）
- OpenAI Codex CLI / AGENTS.md 官方规范（Tier B/C，Topic 06 基线之三）

### Foundation Sufficiency Check（Wave 0 → Wave 1）

进入 Wave 1 前至少确认：

- 核心术语已有工作定义，对象分类已有共享地基
- 每条研究线已有明确深挖起点
- `requirements_engineering/deep_research_topics/_reference/_INDEX.md` 已经可用

### Wave 1：按研究线分别深挖

- purpose: 把每条研究线从"名称和观点"推进到"机制和证据"
- 每条研究线都要从 5 个视角扩展：
  - 证据
  - 根本机制
  - 趋势
  - 难度
  - 争议 / 失败模式
- minimum per topic:
  - 至少 8 份该研究线专属 ground truth
  - 至少 5 份一手来源（Tier A / B 优先）
  - 至少 2 份高质量二手分析（Tier B / C）
  - 至少 1 份近期趋势来源；Topic 06 覆写为至少 3 份
  - 至少 2 份限制 / 失败 / 争议来源
- 每条研究线都必须形成一份 `evidence-summary` 和一份 `question-list`

只有当该研究线已完成一轮 stop assessment、`must_answer` 已有本地证据支撑、且限制 / 失败模式补搜已明确记录时，才允许使用 `early_saturation`，并且必须写入 `requirements_engineering/plan/dr-round-1.status.md` 的 `Wave 1` 区。

### Wave 2：横向比对与综合判断

- purpose: 把分题结果重新收束成整体结构和跨主题判断
- minimum:
  - 每个横向判断都能追溯到具体 `requirements_engineering/deep_research_topics/_reference/*.md`
  - 每条研究线至少有 2 个与其他研究线发生交叉验证的结论
  - 明确区分"硬事实""分析判断""趋势推测"
- 本轮 Wave 2 专属产出：
  - `W2-cross-topic-synthesis.md`：跨主题综合判断
  - `W2-selection-matrix-v2.md`：九维选型矩阵升级版，每行带 KOL / 标准来源
  - `W2-claims-audit-v2.md`：基于新证据升级原 claims-audit 中各条证据强度
  - Topic 04 × Topic 06 回填：用 Topic 06 实证数据重写 Topic 04 §4.6（IDE 需求原语），把"揣测"升级为"近因观察 + 判断"

### Readiness Check：最终验收闸门

至少覆盖下面 5 项：

- 30 秒本地证据检索入口可用
- 每线"机制 + 趋势 + 难点"检查
- 横向综合检查
- 拓扑稳定性检查
- 接手可继续性检查

### 搜够了没有：停止条件（topic-level stop condition）

每条研究线在 stop assessment 完成前，`topic_stop_decision` 保持 `not_assessed`。

完成一轮搜集并进入 stop assessment 后，必须把当前状态明确归类为 `continue / early_saturation / suspend / archive / redirect` 之一。

其中，只有同时满足下面条件，才允许把该研究线视为"已搜够一轮"并进入 `early_saturation / archive / redirect` 这类停止型决策：

- 核心对象清单已经稳定，不再持续新增关键名字
- 新搜到的材料大多在重复已知事实，而不是贡献新信息
- 该研究线的固定问题都已经有证据支撑
- 至少有 1 轮对"反例、限制、争议"的专门补搜
- 已完成一次"官方说法 vs 第三方验证 / 实践证据 / 事故复盘"交叉核验
- 所有重要但未解的问题，都已经被明确归类为 `continue / early_saturation / suspend / archive / redirect`

补充判定：

- `continue`：当前线仍有高价值缺口，且继续深挖预期能改变判断质量
- `early_saturation`：该维度已明显饱和，继续搜索主要只会引入低质量重复材料
- `suspend`：重要，但当前受限于材料、访问或时机，暂不继续
- `archive`：继续下钻的边际收益低，短期内不太可能改变核心判断
- `redirect`：问题重心应转移到其他研究线或新 formalized topic

## 研究线的具体目标

### 研究线 01：re-landscape

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 01/re-landscape`
- wave1_deepen_focus: 建立 ISO/IEC/IEEE 29148 / INCOSE GTWR v4 / EARS 的三方正式对齐关系；补齐 Use Case 2.0 与 User Story 的官方边界；SysML v2 / MBSE 与文本需求的公开主张
- evidence_priority: Tier A 标准文本 > Tier B INCOSE 官方与 Jacobson 原著 > Tier C 大厂工程综述
- difficulty_focus: 标准文本付费访问、公开摘要精度不足；SysML v2 2024 发布后的更新跟进
- trend_question: MBSE × AI Agent 的最新主张是否出现统一方向
- stop_assessment_focus: 三方对齐关系是否已有本地权威摘录；Use Case 2.0 是否已获官方摘要入库
- time_window: `1968–2026Q1`
- recency_floor: `2020`

### 研究线 02：user-story

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 02/user-story`
- wave1_deepen_focus: Beck / Cohn / Cockburn / Patton / Fowler 原始表述与 2023–2026 最新立场；INVEST 企业反例与修复模板；Enabler / Spike / Job Story 权威定义
- evidence_priority: Tier B KOL 原著与官方站 > Tier C 大厂 engineering blog > Tier A 同行评审（覆盖偏少，可接受）
- difficulty_focus: KOL 近两年公开材料散落；Story Mapping 企业案例多为 talk 形式
- trend_question: Cohn / Patton 对 AI 生成 User Story 的最新立场
- stop_assessment_focus: 所有 KOL 最新立场已入库或记录 saturate；INVEST 反例模板已有至少 3 个可复用案例
- time_window: `1997–2026Q1`
- recency_floor: `2020`

### 研究线 03：ears

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 03/ears`
- wave1_deepen_focus: Mavin 2009 原论文与后续补遗；EARS 五模式 + 复合官方语法；与 INCOSE GTWR v4 规则逐条映射；EARS 在 SaaS 的工业证据；何时不用 EARS
- evidence_priority: Tier A IEEE RE09 + INCOSE GTWR > Tier B Mavin 官方站 + Jama / Visure 官方 > Tier C 工具厂商非自夸材料
- difficulty_focus: Mavin 官方材料更新节奏慢；SaaS 域 EARS 实证稀少；QRA / QVscribe 厂商材料需 claims-audit 过滤
- trend_question: Mavin 本人近两年对 Generative AI × EARS 的公开表达
- stop_assessment_focus: INCOSE GTWR v4 每条规则与 EARS 的映射已完成；SaaS 域至少 2 个公开案例
- time_window: `2009–2026Q1`
- recency_floor: `2020`

### 研究线 04：future-trends

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 04/future-trends`
- wave1_deepen_focus: 5 条前瞻维度（Spec-as-Code、多模态、Agent 反修 Spec、Embedding 化、监管可追溯）在 2023–2026 的早期信号与反向证据；EU AI Act / NIST AI RMF / ISO 42001 对结构化需求的条款
- evidence_priority: Tier A 法规文本 > Tier B 学术预印本 / 行业协会白皮书 > Tier C KOL 公开发言
- difficulty_focus: 揣测性强、易陷营销叙事；法规文本庞杂
- trend_question: 哪一条前瞻已被验证 / 证伪
- stop_assessment_focus: 每条前瞻至少 2 份早期信号来源；法规条款已有具体摘录
- time_window: `2023Q1–2026Q1`
- recency_floor: `2023`

### 研究线 05：integration-bdd

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 05/integration-bdd`
- wave1_deepen_focus: Adzic / Wynne 当前立场；企业三轨治理（金融 / 汽车 / 航空 / 医疗）公开案例；决策表 / DMN 与 EARS 的权威边界；Cucumber 官方主张
- evidence_priority: Tier B KOL 原著 + Cucumber 官方 > Tier C 大厂案例 + 合规框架
- difficulty_focus: 企业案例多为 talk 形式；Cucumber 官方文档分散
- trend_question: BDD 在 LLM 时代是否有被重构的迹象
- stop_assessment_focus: 至少 2 个行业三轨治理案例；决策表 vs EARS 边界已有权威文献支撑
- time_window: `2000–2026Q1`
- recency_floor: `2020`

### 研究线 06：agent-format

- registry_ref: `PLAN_PATH -> 研究线注册表（topic registry） -> 06/agent-format`
- wave1_deepen_focus: Cursor / Claude Code / Codex / Kiro / GitHub Spec Kit / OpenSpec / Amp / Aider / Continue / Cline 各自推荐的需求 / 规约格式；官方模板库；工程团队公开采用；失败模式；给出选型建议
- evidence_priority: Tier B 官方文档 + GitHub 官方仓库模板 > Tier C 工程博客 + 大厂公开案例 > Tier E 社区发言（需双证）
- difficulty_focus: 工具链更新快；失败模式公开材料稀少；厂商营销叙事密度高
- trend_question: 是否已形成"事实标准"的需求 / 规约文件命名与内容结构
- stop_assessment_focus: 主流 ≥5 款 harness 的官方主张已入库；至少 3 个公开工程案例；至少 2 份明确的失败模式或限制材料；方法论选型建议已在 artifact 中给出
- time_window: `2024Q3–2026Q1`（严格）
- recency_floor: `2024-07`

## 成功标准（post-pass success state）

达到下面状态，才算真正满足目标：

- `requirements_engineering/deep_research_topics/_reference/` 中有一批高可信、可追溯的 ground truth 文档
- 每条研究线至少形成一组可复用证据包，而不是临时搜索结果
- 对每条研究线都能解释机制、趋势和难点
- 每个重要判断都能追溯到本地 reference 文档
- 对趋势、难度、争议都有专门证据，而不是顺手一提
- 可以明确说清楚"哪些问题不是没做，而是被主动 `suspend`，以及为什么"
- 后续新的 agent 接手时，只看 `requirements_engineering/deep_research_topics/` + `requirements_engineering/deep_research_topics/_reference/` + `requirements_engineering/deep_research_topics/_artifacts/` + `requirements_engineering/plan/dr-round-1.status.md` + `requirements_engineering/plan/dr-round-1.queue.md` 就能继续往下研究

## Hard Gates

本轮 `hard_gates_enabled = yes`，下面检查与 `Readiness Check` 叠加验收：

- 没有 P0 级结论处于"只有单一弱来源（Tier D / E / F）支撑"的状态
- 所有关键术语（User Story、EARS、INVEST、INCOSE GTWR、Gherkin、Spec-as-Code、AGENTS.md、CLAUDE.md、Cursor Rules、Spec Kit、Kiro Spec 等）都在跨主题范围内完成口径对齐
- 所有高价值结论都已明确标注"硬事实 / 分析判断 / 趋势推测"
- 至少完成一轮针对反例和失败模式的专门检索，覆盖 6 条研究线
- Topic 06 的选型建议必须至少 5 款主流 harness 的官方主张各自交叉验证
