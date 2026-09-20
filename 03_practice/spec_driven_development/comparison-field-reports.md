# 实战团队眼中：各 SDD 方法在「spec 写作质量」与「工程控制」上的横向比较（一线复盘汇编）

```yaml
title: SDD 方法横向比较——只收一线团队实战复盘
accessed_at: 2026-09-20
observation_date: 2026-09-20
author: delegated research subagent (parent: session-f37ceeb1)
time_weighting: 2026-09 信息最重 > 2026Q3 > 2026 上半年 > 2025（仅背景）
inclusion_rule: 只收有一线实战经验的团队/个人复盘（能给出具体流程、文件结构、量化数字或诚实坑清单）；不收厂商营销、不收纯观点评论。厂商案例仅在"有可复核开源仓库"时作弱证据标注。
base_sources: 本仓库 debate/ 目录已核实案例（endorsements-and-experiences.md、team-practices.md、critiques.md、chinese-community-verdicts.md、signals-2026h2.md）+ 本轮专项补挖的 2026-08/09 新复盘
new_this_round:
  - Serverworks（日本云集成商）四工具实测对比（2026-08-25）：https://blog.serverworks.co.jp/spec-driven-development-tools-comparison
  - Peng Qian 团队「弃 OpenSpec 改 AWS AIDLC」迁移复盘（BizStack 转写，2026-09-11）：https://bizstack.tech/why-we-ditched-openspec-for-amazons-aidlc-workflow/
  - 阿里云开发者社区 Spec Kit vs OpenSpec 实操选型问答（2026-06-13）：https://developer.aliyun.com/article/1741277
  - Ask HN: Are you leveraging Spec-Driven development?（2026-09-08，生产环境从业者反馈）：https://news.ycombinator.com/item?id=49618556
```

---

## 1. 比较框架说明

### 1.1 为什么只收实战复盘

SDD 领域的公开语料被三层材料占据：厂商叙事（Kiro/GitHub/AWS 官方博客）、分析师评述（Thoughtworks/martinfowler 系）、以及一线复盘。前两层回答"正在发生什么"和"概念上怎么分"，但都不回答"spec 实际写出来什么样、工程上管不管得住"。本文件只收第三层，判定标准是：**作者必须披露至少一项可复核的实践细节**——真实文件结构、CI 配置、量化数字（行数/耗时/命中率/返工率）、或诚实到损己的坑清单。纯"我觉得 SDD 是/不是新瀑布"的观点文一律不收。

### 1.2 证据性质分级

| 档位 | 定义 | 本文件中的案例 |
|---|---|---|
| **A 一手复盘** | 团队/作者本人自述实践，含流程细节与坑；或 repo 内 CI 配置/工作流文档即实践本身 | FIXER（Spec Kit×Scrum）、NodeSource（OpenSpec 全组织流）、opsx-superpowers（Multi-Engineer 设计）、PostHog sdk-specs（CI 配置即实践）、comic-viewer-helper Issue #61、github/spec-kit 自吃狗粮 constitution、宋振华（腾讯云踩坑实录）、Khorana（Superpowers 六个月）、OCTO Talks（BMAD PO 复盘）、Serverworks 四工具实测 |
| **B 转写** | 一手 session/帖子的机器转写或他人详细转写，内容可回查但措辞非原始 | Delta Airlines×AWS re:Invent DVT209（Zenn 转写）、Peng Qian 迁移复盘（BizStack 转写——原始出处未单独回源，引用需留余地）、InfoQ 企业篇（经 Victorino 详细转述，正文四途径未取得全文） |
| **C 转述/厂商筛选** | 案例真实但经厂商/媒体筛选包装，数字未经独立核验 | 网易智企 7 企业案例集、Kiro 客户案例（Siemens 等）、AWS 中国区 PKFARE 存目 |
| **D 群体观点** | 社区讨论反映共识温度，非实证 | VSDD 211 分讨论、Ask HN 系列、HN "Ask: Why are Spec-kit specs like that"（2026-06-15） |

**使用纪律**：对比表每个单元格标注案例与档位；只有单一案例支撑的结论在 §6 明示。

---

## 2. 维度一：spec 写作质量（spec 实际写出来是什么样）

### 2.1 长度与仪式感：会失控，但失控程度与工具强相关

- **Spec Kit 在无纪律使用下最重**。Scott Logic 实测：写一行应用代码前先产出 **2,577 行 markdown**，耗时是迭代式 prompting 的 **10 倍**（经 Victorino 转述，档位 B；原始实测应回溯 Scott Logic 原文再引用）。marmelab 一手实测（2025，背景级）：小功能生成 8 文件 1,300 行文本（档 A，反方但为实测）。Böckeler 一手实测：小 bug 被 Kiro 膨胀成 4 个 user story + 16 条验收标准，"sledgehammer to crack a nut"（档 A）。
- **Serverworks 2026-08-25 实测给出了目前唯一一份跨工具生成量对照**（档 A）：同一"全流程、排除代码"口径下，AI-DLC 单 unit 40-50 文件（乘法结构：NFR/基础设施设计按 unit 累积）、Spec Kit 每功能约 10 文件、OpenSpec 每 change 约 4 文件。作者同时指出 AI-DLC 的"重"是无序膨胀的反面——是为审计留痕的设计选择，在重统制场景反而是优点。
- **量化成本面**：spec-kit #1401 实测 slash 命令每会话固定吃掉约 **18.6k tokens** 上下文（Cursor 默认 20k 占 93%），属可复现实测（档 A-，量化硬、但是 issue 而非复盘文）。

### 2.2 可评审性：写作质量的核心不是"详不详细"，而是"评审者能否在合理时间内判断对错"

- **FIXER（Spec Kit×Scrum，2026-04~08，档 A，本领域最纯团队证据）**：spec 走到 Clarify 即提 PR，开发者/评审者/PMO 三方在实现前对齐"做什么"；Clarify 可按安全/性能定向反复深挖；第 2 篇补实装者视角——spec 先行后评审争论从"你想做什么"转向"实现是否符合 spec"，评审更聚焦。配套纪律是质量前提：答 AI 提问"不带臆测"（答不了必须问 PMO/客户）、向客户确认"带假设去"（A/B 方案+技术理由）。代价：**onboarding 成本远超预期**，学的是方法不是工具，第一个 sprint velocity 下降。
- **Böckeler 一手实测的反面**："spec-kit 大量 markdown very verbose and tedious to review… I'd rather review code"；且观察到虚假控制感——agent 忽略 research 笔记、重复生成已有类，"I frequently saw the agent ultimately not follow all the instructions"（档 A）。
- **opsx-superpowers 给出评审质量的自检问句**（档 A）：评审者对 spec PR 的两个关键问题——*agent 是实现了 spec 的意图还是字面措辞？eval 通过是因为 spec 写得好，还是 spec 模糊到不可能失败？*——这是公开材料里对"spec 模糊性"最锋利的一手操作化。

### 2.3 写作过程本身的价值：AI 当陪练

- FIXER：AI 在 Clarify 阶段主动追问模糊点，"实施后才发现考虑遗漏"的案例锐减，把 AI 当"规格的壁打对手"（档 A）。
- Apurv Sheth（阿里云译文，2026-07，档 A 弱一档因系译作）：在约 30 个功能上跑 OpenSpec verify，**约 1/3 会发现问题**（缺失错误状态、未覆盖边界）——spec 写作缺陷率的唯一定量一手数据。
- 宋振华（腾讯云，2026-08-18，阅读 5.76 万，档 A）：团队全面推行 SDD，第一个月单接口端到端耗时**比手写多 30%**，第三个月反转为**下降 40%**；**第 6 周是大多数人想放弃的节点**——写作质量的爬坡成本曲线，中文社区目前唯一同时给出负向爬坡与最终收益的一手数据（可回源部分仅标题+作者概述，细节段未抓全）。
- Khorana（Superpowers 六个月，档 A）：七阶段流程（brainstorm→worktree→plan 拆 2-5 分钟任务→subagent+两阶段评审→强制 TDD→severity review）在匹配场景有效（8 小时 session 完成 WordPress 工具、TDD 抓住 2 个正则 bug），但诚实指出琐碎修改/紧急排障时 plan-first 反射是错的；**团队部分成员采用时工件反而干扰协作——"要么全员用，要么没人用"**。
- OCTO Talks（BMAD，2026-03-06，PO 一手复盘，档 A）：2 周交付 vs 传统 feature team 3 个月；但明确短板——**缺标准化审计指标、EPIC↔User Story 关联不清、业务规则不显式、token 消耗高、无功能测试自动化**（档 A，单 mission 单人视角）。

### 2.4 写作质量的系统性上限

- Peng Qian 迁移复盘（2026-09-11，BizStack 转写，档 B）：团队用 OpenSpec 六个多月后识别出五个写作/维护失败模式——①命令语义重叠导致成员用法漂移、部分人退回 vibe coding；②**spec 记录了决定但没记录理由**，评审他人 spec 时看不出"为什么这样设计"，连原作者自己都会忘；③粒度无法校准（粗了出 demo，细了拖速度）；④文档与代码漂移；⑤协作是事后补充。换 AIDLC 后自述代码质量显著提升。这是 2026-09 最新、目标最明确的"OpenSpec 写作质量不足"迁移证据。
- dbreunig 自我推翻（2026-03-04，档 A，MLOps 大会 talk）：曾以纯 spec+750 YAML 测试的 whenwords 成为 SDD 旗手，后承认 "a spec doesn't really work until it's implemented"，spec/代码/测试是必须持续同步的三角——写作质量是必要条件而非充分条件。

---

## 3. 维度二：工程控制（评审流 / CI 机器校验 / drift / 权限与锁定）

### 3.1 CI 确定性校验：OpenSpec 系唯一跑通了完整闭环

- **PostHog sdk-specs（档 A，CI 配置即实践）**：`.github/workflows/openspec.yml`——path-filter 只动 `openspec/**` 才跑、CLI 版本钉死 `@fission-ai/openspec@1.4.1`、`validate --specs --strict --no-interactive`；60+ 能力目录、每能力一个 spec.md，Scenario 用 `@client/@server/@both` 标注适用面，spec 场景直接当验收测试输入。
- **comic-viewer-helper Issue #61（档 A）**：`validate --strict --all` 发现 5 个 spec 结构不合规 → 修复 → 上 GitHub Actions 防复发。印证"裸 spec 目录会自然腐烂，必须机器门禁兜底"。
- **Spec Kit 的门禁是 LLM 而非确定性**：无独立 validate CLI，一致性靠 `/speckit-analyze`、`/speckit-converge` 会话内分析。但其 **constitution 治理是最完整的**（github/spec-kit 自吃狗粮，v1.0.0 Ratified 2026-06-19，档 A）：Principles I–V 为 binding gates，`/speckit.analyze` 把 MUST 冲突判 CRITICAL，constitution 本身走 PR + 治理 SemVer + Sync Impact Report（记录修订波及哪些模板）。
- **Kiro：有产品内评审屏，无确定性校验**。Kiro CLI 2.18（2026-08-12，厂商 changelog，机制性证据）spec 阶段检查点出评审屏、逐行 stage comment 一次性汇成修订请求；2026-08 起嵌套 AGENTS.md 作为"目录级所有权"由工具原生承担。工程控制止步于 IDE/CLI 内，PR/CI 集成需自建；**组织级统制是四家中唯一有平台级答案的**（Serverworks 实测指出：接 AWS IAM Identity Center 可得 SSO/权限集中/审计日志）。
- **BMAD：无确定性校验**（OCTO 复盘的"三问无解"即审计指标缺失的一手确认）；AIDLC：工程控制以 **append-only audit.md 审计轨迹 + 每子阶段审批门（approval mark 出现在 audit.md 才进下一阶段）+ aidlc-state.md 队列**为核心（Peng Qian 复盘，档 B）——是"审批链留痕"路线，不是"机器校验 spec 结构"路线。

### 3.2 评审流：spec 怎么进 PR

- **opsx-superpowers Multi-Engineer（2026-05-26，档 A，目前颗粒度最细的公开多人方案）**：两轨分支模型——小特性一条 `feat/<topic>` PR 走完；大特性先 `spec/<topic>` 分支只提 spec 文件，**PR1=Spec Review（merge 后 tasks 冻结），PR2=Impl Review（查表式轻量评审）**。原则原文："Do not do line-by-line code review. The harness + E2E CD pipeline is the primary quality gate."。配套：propose 前必读所有活跃分支的 proposal.md 把 `depends on/conflicts with` 写进 design.md；一人一 topic 端到端绝不拆分；共享索引文件冻结化防 4-6 人并行写冲突。团队自述瓶颈判断："Bottleneck shifts from implementation to spec quality and PR review bandwidth; Engineer role shifts from executor to judge"。
- **NodeSource 全组织流（2026-08-12，档 A，最强的 ≥7 人一手案例，人数未公开）**：OpenSpec 四工件流（proposal/design/scoped specs/task list）→ **Plannotator 浏览器评审 UI 做人机 inline 评论回传 agent** → 批准后按 task list 实现 → 自动同步为 ZenHub epic/issue（消双事实源）→ PostHog 遥测按 call site 打点（skill 名/change 名/task 名/模型/发起人）做成本切片。作者自述"每个变更都有从 proposal 到 merge 的纸面轨迹，SDD 因此变得 practical"。坑在供应商侧：黑盒账单可滚出六位数月账单、限流中断 CI/评审循环。
- **FIXER**：Clarify 即提 PR + 评审期开发者切换下一个 PBI 的流水线（见 §2.2），是把 spec 评审嵌进 sprint 的最平滑一手方案。
- **Delta Airlines×AWS（DVT209，Zenn 机器转写，档 B 弱）**：spec tasks 经 MCP 同步进 Jira（8 stories/19 subtasks 自动建）、agent hooks 监听 tasks.md 变更；two-pizza team 因 PM 直接进 spec 迭代"数周→数小时"，但**下游 QA/测试跟不上 commit 速度**——与 opsx"瓶颈转移到评审/验证"互证。
- **对照面**：BMAD 的多人类协作用法在官方社区仍是开放讨论题（GitHub Discussion #1617 标题即证据）；Kiro 侧可验证的真实团队 `.kiro/` spec 目录公开实例仍缺位（2026-09-20 多轮检索未命中）。

### 3.3 drift 发现：2026 年批判的重心所在

- OpenSpec 的 delta/archive 流是目前唯一的结构性答案：MODIFIED requirement 与主 spec 机械比对、`validate --archived` 校验 archive 里每个 change 的 tasks.md 全勾完（官方建议挂 pre-commit）、`update` 命令把单点修正与既有 artifact 突击比对（Serverworks 实测确认这一动线是它相对 Spec Kit 的独有差异）。
- Spec Kit 的 drift 治理靠三种 spec 持久化模型（Flow-forward/Living spec/Flow-back）+ LLM converge 循环——确定性弱；其官方 issue 群（#1191 115👍、#620、#1130、#442）就是"spec 更新/回写无工作流"的官方级证据群（2025Q4 背景，2026 年仍是团队向最重磅批判）。
- 一手腐烂实例：dbreunig "The spec gets written, it gets implemented, it gets released. Is the spec updated? No."；av/facts 弃 SDD 另起炉灶，"large projects have so many specs agents start making mistakes maintaining them. There's a constant consistency tax."（2026-05-04，档 A 弱一档、单案例）。
- Peng Qian 复盘第 ④ 条（"开发者中途调实现后再没跑过 OpenSpec 命令，多次迭代后文档变得没有意义"）是 drift 批判在 2026-09 的最新团队级回响。

### 3.4 权限/锁定

- opsx：tasks 在 Spec PR merge 后锁定；只有 Spec Refiner 角色可改 spec（模板仓库 ANTI_PATTERNS.md #7 的"实现者私自改 spec"教训）。
- spec-kit：constitution 修订需 PR+维护者批准+版本号（规则的锁定）；AIDLC：审批门+append-only audit.md（流程的锁定）；Kiro：平台账户层权限（IAM SSO）。
- Kiro Crew 1000 PR 案例的治理四件套（显式协作记录、按项目隔离 memory、host 级权限、不可篡改审计日志"第一天就上"）——注意该案例是厂商员工复盘但有可复核开源仓库，档 C+，只作弱证据。

---

## 4. 对比表

行=方法/工具；每个单元格至少挂一个真实案例；无案例处明确写"无实战证据"。

| 方法/工具 | 写作质量证据 | 工程控制证据 | 最佳实战案例 | 反面案例 |
|---|---|---|---|---|
| **Spec Kit** | FIXER：Clarify 即 PR、评审焦点从意图转向合规、返工显著减少（档 A）；Scott Logic：2,577 行 markdown、10 倍耗时（档 B）；Böckeler：verbose 难评审、agent 常无视指令（档 A） | constitution 治理最完整：github/spec-kit 自吃狗粮 constitution + 治理 SemVer + Sync Impact Report（档 A）；但无确定性 validate CLI，一致性靠 LLM analyze（team-practices M3/M4 实地核查） | FIXER（真实 Scrum 团队嵌入 sprint，2026-04~08 系列） | Scott Logic 失败实测（2,577 行/10 倍耗时）；spec-kit #1401 context tax 18.6k tokens 实测；#1191 系 spec 更新无工作流官方证据群 |
| **OpenSpec** | Apurv Sheth：30 个功能 verify 命中 1/3 缺陷，合并前揪出（档 A 弱一档，译作）；Serverworks 实测每 change 约 4 文件、全工具最轻（档 A） | PostHog sdk-specs：`validate --strict` 进 CI + 版本 pin + path-filter + Scenario 当验收测试（档 A 一手）；NodeSource：Plannotator 评审 UI + ZenHub 同步消双事实源 + 按调用点遥测（档 A）；comic-viewer-helper Issue #61 腐烂→CI 补救路径（档 A） | NodeSource 全组织流（2026-08-12，最强 ≥7 人一手）+ PostHog 跨团队契约仓库 | Peng Qian 团队六个月后弃用迁 AIDLC：理由丢失、粒度难校准、drift、协作事后补（档 B，2026-09-11） |
| **Superpowers** | Khorana：plan 拆 2-5 分钟任务+强制 TDD，8 小时完成工具、TDD 抓 2 个正则 bug；诚实边界：琐碎/紧急任务 plan-first 是错的（档 A） | opsx-superpowers Multi-Engineer：双 PR 门（PR1=Spec Review 锁 tasks）+ severity-based review + eval-log 重试环 + per-capability 防写冲突设计（档 A，2-6 人自述设计文档）；注：这是 OpenSpec 上的自建层，Superpowers 本体无校验机制（M1/M10） | opsx-superpowers（目前公开度最高的一手多人 SDD 工作流设计） | Khorana：部分成员采用时工件干扰协作，"要么全员用，要么没人用"（档 A）；dbreunig 引 Gas Town 复杂度自认"ugly baby"（档 A，属同流派旁证） |
| **BMAD** | OCTO Talks PO 复盘：2 周 vs 传统 3 个月交付（档 A）；但同文披露：业务规则不显式、EPIC↔Story 关联不清（档 A） | OCTO 同文："何时介入、如何审计、用什么标准"三问无解、无功能测试自动化（档 A）；无确定性校验（team-practices M10 实地核查，二手）；多人类协作用于官方社区仍是开放讨论（Discussion #1617） | OCTO Talks（法国咨询公司客户项目一手复盘，2026-03-06） | OCTO 同文的短板清单即最佳反面证据（档 A）；2026-08/09 官方连版自我瘦身（v6.11/v6.12"Build decides how much ceremony"）是最重流程方法论的自我否定（signals，机制性证据） |
| **Kiro** | 无可验证的真实团队 spec 质量一手复盘（`.kiro/` 目录公开实例 2026-09-20 检索缺位）；仅厂商转述客户故事（Siemens 等，档 C）+ Böckeler 单点实测"小 bug 膨胀成 4 story/16 验收标准"（档 A，反例） | 产品内评审屏+嵌套 AGENTS.md 目录级规则（Kiro CLI 2.18 changelog，2026-08，机制性）；组织统制唯一有平台级答案：IAM Identity Center SSO/审计（Serverworks 实测，档 A）；但 PR/CI 集成与确定性校验需自建 | Delta Airlines × AWS re:Invent DVT209（spec tasks MCP 同步 Jira、PM 进 spec 循环"数周→数小时"）——档 B 机器转写，证据弱 | 同上 Delta 案例的下游失速：QA/测试跟不上 commit 速度（档 B）；中文社区讨论被网络可用性问题挤占（掘金实测文，档 A 弱），侧面反映落地摩擦 |
| **（补充行）AWS AIDLC** | Serverworks 实测：单 unit 40-50 文件、人机往复最多，但为审计留痕的结构化设计而非无序膨胀（档 A，2026-08-25） | append-only audit.md 审计轨迹 + 每子阶段审批门 + aidlc-state.md 粒度队列（Peng Qian 复盘，档 B，2026-09-11）；NFR/基础设施进工程分解 | Peng Qian 团队：从 OpenSpec 迁入后"代码质量显著提升"（档 B） | Serverworks 同文：审批门连续、适合围屏同步 mob review 而非异步评审（档 A）——重统制的代价 |

---

## 5. 实战共识与分歧

### 共识（多案例交叉支撑）

1. **spec 评审必须前置进流程，且实现前对齐"做什么"确实减少返工**。FIXER（Clarify 即 PR）、opsx（PR1=Spec Review）、NodeSource（Plannotator 批准门）、AIDLC（audit.md 审批门）四条完全独立的团队路线给出了同构答案（档 A×3 + 档 B×1）。
2. **瓶颈从写代码转移到 spec 质量与评审带宽**。opsx 自述判断 + Delta 案例 QA 失速 + FIXER 估点变难 + InfoQ 企业篇"瓶颈移到意图表达/协调/监督"（档 B 转述）——四个来源、两种档位互证。对策也已收敛：两层评审（spec 高标准 / code 查表不逐行）+ 一人一 topic。
3. **裸 spec 目录必然腐烂，必须有机器门禁或豁免通道**。comic-viewer-helper（5 处腐烂→CI 兜底）、Anti-patterns #1/#3（spec 退化成事后辩护）、av/facts consistency tax、Peng Qian drift 第④条——OpenSpec 系用 `validate --strict` 落地，其余工具要么自建要么承认没做。
4. **写作成本前高后低，爬坡期是真实的、必须明说**。FIXER onboarding 远超预期、宋振华"+30%→第 6 周想放弃→-40%"、网易案例集"3 人团队 prompt 法返工超手写"——中、日、英文社区独立得出同一形状的曲线。
5. **重型仪式在 2026H2 被普遍放弃**：BMAD v6.11/6.12 自我瘦身、superpowers 压缩运动+executing-plans 一次 review、Google Conductor 去命令序列、Kiro 降 spec 叙事权重——方法论供给端集体转向"轻 spec + 按需 ceremony + 验证循环"（signals 2026H2 判读）。这不是观点而是各工具 release notes 的一手机制证据。

### 分歧（真实吵架点）

1. **"重"是缺陷还是特性**：Scott Logic/Böckeler/Peng Qian 视生成量为失败证据；Serverworks 实测同一现象却结论"统制场景下是强项"；AIDLC 用户用审批门换审计轨迹。没有中立裁判数据。
2. **LLM 门禁够不够**：OpenSpec 系坚持确定性校验（可进 CI 才算数）；Spec Kit 生态用 `/speckit.analyze`+constitution 的 LLM 门禁也活得好（FIXER、NodeSource 之外的 Spec Kit 团队无一报告因缺确定性校验而失败）。证据不足以裁决。
3. **spec 应该是"活契约"还是"变更日志"**：OpenSpec 的 delta/archive（specs/ 始终是当前事实源）vs Spec Kit Flow-forward（每 feature 目录即历史）。两者都有一手成功案例，无头对头比较。
4. **要不要全员统一**：Khorana"要么全员用要么没人用" vs Serverworks"四工具按人/场景混搭即可"（且指出并不互斥）——一个来自工作坊协作痛感，一个来自工具选型视角。
5. **"代码是唯一真相源"派 vs spec 治理派**：HN 2026-08-05 "plan mode 就够了"帖（高权重转向信号）代表前者；NodeSource/FIXER 用组织级纸面轨迹的实践回报代表后者。2026-09 时点双方都活看，前者的证据是舆论温度，后者的证据是落地机制。

---

## 6. 局限（诚实声明）

- **单案例支撑的格子**：BMAD 行几乎全部靠 OCTO 一篇（单 mission、单 PO 视角、无 spec 目录布局披露）；AIDLC 行的效果证据只有 Peng Qian 一例且系 BizStack 转写（原始出处未单独回源）；Kiro 写作质量列无任何一手团队复盘，靠反例（Böckeler）+ 机制性 changelog 拼成。
- **数字未独立核验**：Scott Logic 的 2,577 行/10 倍来自 Victorino 转述；宋振华的 +30%/-40% 可回源部分只有作者概述；网易 7 企业案例集是厂商白皮书级；Peng Qian"质量显著提升"无量化口径。
- **规模断层**：>6 人区间最强一手（NodeSource）人数未公开；百人量级只有厂商转述（网易 M14）。20 人以上结论全部是外推。
- **证据时效不均**：Spec Kit 批判最重（#1191 系、#1401）集中在 2025Q4-2026Q1，而 spec-kit 2026-09 已进入 1.0.x 高频发布期并在做平台化拆分——部分反面证据可能已被新版本部分回应，本表未逐项复核新旧版本差异。
- **幸存者偏差**：所有正方案例都是"坚持下来并写了博客的团队"；放弃团队里只有 Peng Qian 和 av/facts 留下了复盘，沉默退出者的比例完全未知。
- **本文件自身**：Kiro/BMAD 的 CI 门禁列靠 team-practices.md 的实地核查（二手）而非直接抓取工具输出；Reddit 内容因 403 从未被收录，可能有系统性盲区。
