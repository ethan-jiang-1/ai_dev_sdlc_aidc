# Plan mode 派深挖——内置规划的机制光谱、"就够了"之争与进阶玩法

```yaml
topic: SDD 替代形态之二：plan mode 派（规划内嵌于 agent harness）
accessed_at: 2026-09-20
collector: delegated research agent
base: ./README.md 第 4 节（原单文件底稿 alternatives.md 第 2 节，2026-09-21 重排；本文在其基础上深挖，不复制原文）
related:
  - ./README.md                   # 五形态总览与光谱图
  - ../spec_driven_development/debate/critiques.md        # 批判面来源
weights: 高=官方 docs / 创始人访谈 / GitHub PR；中=Nearform/技术博客；低=HN 回帖与个人实践
key_corrections:
  - "Nearform 反方文的实际发布日期是 2026-03-18（作者 Luca Lanziani），底稿标注的 2026-09 不准；其姊妹比较篇更早。"
  - "「Claude Code 团队谈不再需要 plan mode」的原始出处是 Boris Cherny 的 YC 圆桌访谈（约 2026-02，YouTube PQU9o_5rHC4），而非 2026-09；InfoQ 中文整理 2026-02-19 发布。底稿的时间定位需修正。"
  - "Codex 侧 2026-08-31 有硬动向：update_plan 工具改为 opt-in（openai/codex PR #41744）——内置规划器本身正在被『可拆卸化』。"
limitations:
  - HN 帖（48235526、althacker 47106686）沿用底稿锚点，本轮未能逐条回源展开。
  - Cursor plan mode 以官方博客（2025-10-07）+ 二手分析为准，2026 年内未见其生命周期的重大改版公告。
  - Claude Code plan mode 的会话内细节以官方 permission-modes 页与 GitHub issue 侧写为准。
```

---

## 0. 定位：本文深挖什么

底稿（本 README 第 4 节；原单文件底稿 alternatives.md 第 2 节）给出的骨架是：plan mode = 不留任何 spec 工件、规划是 harness 内置的一次性阶段、"够了"论 vs Nearform 反方。本文补五层：各家机制差异的官方核实、"就够了"正反逐条对照、社区进阶玩法、"不再需要 plan mode"说法的溯源、以及适用边界的收口。

---

## 1. 各家 plan mode 的机制差异（2026 年现状，官方 docs 核实）

四家的共同点是"先规划、经人批准、再执行"，但在**产物生命周期、批准机制、与执行的耦合方式**上分成了三个梯度：

### 1.1 横比表

| | Claude Code | OpenAI Codex | Google Antigravity | Cursor |
|---|---|---|---|---|
| **形态** | 权限模式之一（`plan`），Shift+Tab 循环切换 | 双层：`/plan` 会话式规划模式（collaboration mode 模板）+ `update_plan` 结构化步骤工具 | 执行模式之一（`plan`），`/plan` 指令前缀 | Agent 的 Plan Mode（Shift+Tab 触发），复杂任务自动建议进入 |
| **plan 产物** | 会话内对话产物 + ExitPlanMode 审批对话框；由 harness 生命周期管理，默认不落盘不维护 | 模板层是自由文本计划（`plan.md` 模板）；`update_plan` 维护一份**结构化步骤表**（有序步骤+完成状态），渲染在 TUI plan panel | **持久 Artifact**：Implementation Plan 以工件形式存在，可评论、可迭代、随任务留存 | **可落盘**：生成带文件路径与代码引用的 Markdown 计划，可在编辑器内直接改（增删 todo），可显式保存进仓库 |
| **批准机制** | 计划完成后经批准对话框确认才转执行；某些版本会退化成裸 yes/no（GitHub issue #79024 即此类回归） | 计划由模型自由文本生成、人工 review；执行期间 `update_plan` 持续更新状态，无二次批准 | "Proceed / 评论后 Review"两档：默认执行前强制人工 review plan artifact，可设为 Always Proceed 跳过 | 人工 review/编辑计划后一键从计划启动构建 |
| **与执行的联系** | 同一会话内切模式继续执行；2026 年已支持**自动进入** plan mode（在"人也会想规划"的节点自动触发） | 同会话延续；计划状态跨 compaction/resume 存活——这是 `update_plan` 的核心职能（对抗上下文压缩失忆） | 同一 Agent 会话内从 plan artifact 直接 Proceed 到执行；CLI 与 IDE 均可持久化默认模式 | 从计划直接派发执行；计划文件可供后续会话引用 |
| **会话外残留** | 无（除非用户自己让它写文件） | 计划状态属会话，不属仓库；外部系统（Linear/Jira MCP）需自建 | 有——工件面板里可回看 | 可选——用户决定是否存入 repo |

来源：[Claude Code permission modes](https://code.claude.com/docs/zh-CN/permission-modes)、[Claude Code issue #79024](https://github.com/anthropics/claude-code/issues/79024)、[Codex plan.md collaboration template](https://github.com/openai/codex/blob/main/codex-rs/collaboration-mode-templates/templates/plan.md)、[Vaughan 对 update_plan 的机制考证](https://codex.danielvaughan.com/2026/08/31/codex-cli-update-plan-tool-opt-in-external-planning-competing-surfaces/)、[Antigravity execution modes](https://antigravity.google/docs/cli/modes/)、[Antigravity Implementation Plan artifact](https://antigravity.google/docs/implementation-plan/)、[Cursor Plan Mode 博客](https://cursor.com/blog/plan-mode)。

### 1.2 三个梯度：从"即弃"到"半工件"

1. **即弃端（Claude Code 默认形态）**：plan 只活在会话里，批准即消费。Boris Cherny 明说 plan mode "没什么秘密，就是在 prompt 里加一句'请先不要写代码'"——它在实现上就是**一次 prompt 注入 + 一个审批门禁**，不是数据结构。
2. **状态端（Codex）**：`update_plan` 把计划做成**对抗 compaction 的会话内持久状态**——不是为了人，是为了模型自己在长任务里不忘步骤。这暴露了 plan mode 的隐藏职能：它同时是"人的对齐工具"和"模型的工作记忆"。
3. **工件端（Antigravity / Cursor）**：plan 变成可评论、可编辑、可留存的 artifact/文件。Antigravity 甚至默认强制"执行前 review plan artifact"——这已经踩进 SDD 的领地，只是不要求跨需求维护。

**机制结论**：2026 年的 plan mode 已经不是铁板一块。底稿说的"用完即弃、不进仓库"只准确描述了 Claude Code 的默认形态；Antigravity 和 Cursor 官方支持的"plan 落盘"路线，实际上是 plan mode 向 SDD 的自发滑动（见第 3 节）。

---

## 2. "就够了"论 vs 反方：逐条对照

正方锚点：HN 2026-08 帖多位开发者自述 plan mode 够用（[HN 48235526](https://hn.nuxt.dev/item/48235526)）、Boris Cherny 自述 80% session 从 plan mode 起手。反方锚点：Nearform，Luca Lanziani《Why plan mode is not enough》（**2026-03-18**，非 2026-09，[原文](https://nearform.com/digital-community/why-plan-mode-is-not-enough-better-outcomes-with-spec-driven-development)）。

| # | 议题 | 正方（就够了） | 反方（Nearform） | 本轮核实后的判读 |
|---|---|---|---|---|
| 1 | 规划的对象 | 单人开发者清楚要什么，plan mode 当场对齐即可 | plan mode 只会规划**实现**，不会规划**产品**——feature/library/MVP 够用，"meaningful whole"须由 PO/业务/团队定义 | 两者其实不冲突：正方说的是个人粒度任务，反方说的是组织粒度产品。这是**粒度之争**而非对错之争 |
| 2 | 参与者 | plan mode 是开发者个人工具，一个人一个会话闭环 | 软件开发只是产品团队活动之一，上下游（需求、架构、排期）的人进不了 plan mode 的会话 | 成立。plan mode 的批准者是"发 prompt 的那个人"，无多角色审批面；BMAD 这类多 persona 框架正是补这个位 |
| 3 | 沉淀 | 计划对齐完就该消失，持久工件=spec 债 | 没有跨会话沉淀，下个会话/下个人从零开始 | 各打五十大板：即弃端确实无沉淀，但 Antigravity artifact 与 Cursor 存盘计划说明"轻沉淀"需求真实存在——社区答案是**半步沉淀**（见第 3 节），不是回到全量 spec |
| 4 | 验证 | 人批准计划即验证（当下对齐） | plan mode 无验证层，agent 说"我会做对"不等于做对 | 反方成立但较弱：plan mode 从未声称提供验证，它只提供**意图确认**；验证缺口由测试/harness 派补，不构成 plan mode 被否定的理由 |
| 5 | 方法论归宿 | plan mode 就是日常默认，无需更多 | 行业已承认 SDD 在许多场景产出更好代码，plan mode 只是 SDD 的入口 | 有趣的是反方也承认"plan mode 使能了 SDD"——两派是同一管道的两段，争论的是管道该在哪一站停 |

**对照结论**：反方文本质上是"from feature to product"的论证，其处方（BMAD 多 persona 框架）不是恢复 spec 工件链，而是**把规划的参与者从一人扩展到团队**。它击中的是 plan mode 的组织边界，不是其技术形态。正方在个人粒度上至今无人证伪。

---

## 3. 进阶玩法：2026 年社区的实际操作谱系

按"沉淀多少"递增排列，三种主流形态都**绕开了完整 SDD 工件链**：

### 3.1 planning 会话与 execution 会话分离（上下文卫生学）

规划与执行拆成两个会话/两份上下文：规划会话负责探索、读码、提问、出计划；执行会话拿计划作为输入、上下文干净地开工。动机有二：探索过程的噪声不污染执行上下文；执行 agent 拿到的是**被压缩、被批准过的意图**而非整段协商历史。底稿引的 althacker "Separation of planning and execution" 讨论是代表；Boris Cherny 的多 tab 用法（多个 tab 同时规划、批准后执行）是其单人轻量版；Superpowers 的 subagent-driven development 是其结构化版——计划写成文件，**由全新的 subagent 逐任务执行**并两段式 review（[Superpowers 文档](https://mintlify.wiki/mridullpandey/superpowers/skills/subagent-driven-development)）。这与 Boris 访谈里的 "uncorrelated context windows" 是同一原理：干净上下文是能力，不只是卫生。

### 3.2 plan 文件落盘但不维护（.tmp plan / 即弃文件）

比"会话内即弃"多一步、比"入库工件"少一责：把计划写成文件（有的约定放 `.tmp` 类临时路径或固定草稿位），供执行会话读取，**任务完成后即废弃，不进 repo、不更新、不背一致性义务**。它解决的是分离式工作流里"执行会话怎么拿到计划"的传递问题——文件只是 IPC 通道，不是资产。这是社区对"沉淀 vs spec 债"两难的工程化解法：**要计划的传递性，不要计划的维护税**。与 facts 派的区别：facts 维护的是长期事实清单，.tmp plan 连清单都不维护。

### 3.3 plan→spec 的半步形态（官方支持的滑动）

三家官方功能已经内置了这条半步：Cursor 明确支持"把计划保存为 repo 里的 Markdown 供以后引用"；Antigravity 的 Implementation Plan 是可评论、可回看的持久 artifact；Codex 的计划状态跨 resume 存活。共同点：**计划获得了存储形态，但没人承诺维护它**——它是过期即弃的历史快照，不是需与代码同步的 spec。这正是底稿光谱上 plan mode 与 Spec Kit 之间的过渡带：有工件之形、无工件之责。值得注意的是这半步是**厂商顺着用户行为加的**（Boris 的 latent demand 叙事同样适用于此），而非 SDD 方法论的回潮。

**进阶结论**：2026 年社区的实际玩法收敛为"**按需沉淀、拒绝维护**"——分离会话管上下文质量，落盘文件管传递，半步工件管回看；三者都不接过 SDD 最大的成本项（跨会话一致性维护）。

---

## 4. 关键动向核实："Claude Code 团队说不再需要 plan mode"

**找到了原始出处，但时间需要修正**：这不是 2026-09 的说法，而是 **Boris Cherny（Claude Code 创始人）在 Y Combinator 圆桌访谈**中的表态，视频约 2026 年初发布（[YouTube PQU9o_5rHC4](https://www.youtube.com/watch?v=PQU9o_5rHC4)），InfoQ 中文整理 2026-02-19 刊出（[InfoQ/搜狐转载](https://www.sohu.com/a/988525755_355140)）。逐字要点：

1. plan mode 本质是 prompt 前缀（"先别写代码"），源自用户的 latent demand，一个周日晚上 30 分钟写成上线。
2. Boris 自认是**重度用户**（约 80% 的 session 从 plan mode 起手，多 tab 并行规划），但同时说"plan mode 可能确实有一个比较有限的生命周期"。
3. 判断依据是模型能力曲线：以前 plan 之后还要 babysit，现在（Opus 4.5 之后）"只要 plan 是对的几乎每次都能保持在正确轨道上"——babysit 的位置从"plan 前后"退到"plan 前"；再往后"一发 prompt 自己想清楚做完"，plan mode 作为独立约束会消失。
4. Claude Code 已在做自动进入 plan mode 的实验：在"人类也会想规划"的节点自动触发。

**定性**：这是创始人对产品形态的公开预判（一手、有出处），不是官方 roadmap 承诺；说"不再需要"应精确为"**独立的 plan mode 入口可能消失，被模型自动触发与更强执行吸收**"。旁证动向是 OpenAI 侧的反向操作：2026-08-31 Codex 把 `update_plan` 从默认开启改为 **opt-in**（[PR #41744](https://github.com/openai/codex/pull/41744)，机制考证见 [Vaughan 文](https://codex.danielvaughan.com/2026/08/31/codex-cli-update-plan-tool-opt-in-external-planning-competing-surfaces/)）——动机不是模型变强，而是**与外部规划系统（Linear/Jira MCP）竞争同一张计划面**导致 plan drift。两家合起来看：内置规划器正在从"必经阶段"变成"可拆卸组件"——plan mode 没有 SDD 化，反而在 harness 化（成为 harness 里可替换的 planning surface）。

---

## 5. 适用边界：该停在 plan mode、不往上走的场景

综合官方 docs、访谈与正反两方，以下条件满足得越多，越应停在 plan mode、不引入 spec 工件：

1. **单人可批准**：意图对齐只涉及发 prompt 的本人，无需 PO/架构/业务的签字面（Nearform 反方自己的适用描述也承认这点）。
2. **会话内可完成**：任务的探索、规划、执行、验证能在一个（或分离的少数几个）会话内闭环；不存在跨会话复用同一份"为什么"的需求。
3. **计划不被下游消费**：没有人会拿着这份计划继续工作——一旦计划要传给第二个人/第二个团队/三个月后的自己，即弃假设即破产。
4. **正确性风险由测试兜底**：仓库已有 TDD/回归防线兜住"agent 做错"的风险，规划门禁只需管方向不需管验证。
5. **代码库是自解释的**：agent 自行探索即可获得足够上下文（brownfield 现成代码、小中型 repo）；plan 阶段只是确认方向而非建立共享模型。
6. **任务粒度是 feature/bugfix/research 级**：Nearform 的分界线——feature 以下 plan mode 够用，产品级"meaningful whole"需要团队规划框架。

反向信号（出现即该上探轻量 spec / harness / 测试契约）：跨人跨会话的契约需求、多人并行改同一领域、合规/审计要求留痕、agent 与外部任务系统双轨导致的状态漂移。

**边界收口**：plan mode 派的真实主张应修正为——"规划的价值在当下对齐，沉淀是可选的半步，维护是明确的反模式"。它不是 SDD 的否定，而是把 SDD 从默认动作降格为按需上探的重决策；2026-02 至 2026-09 的动向（自动进入 plan mode、update_plan opt-in）表明这个"降格"正在被两家头部厂商产品化。

---

## 附：本轮新增关键来源

- [Boris Cherny YC 圆桌访谈（InfoQ 整理，2026-02-19）](https://www.sohu.com/a/988525755_355140)；原始视频 [PQU9o_5rHC4](https://www.youtube.com/watch?v=PQU9o_5rHC4)
- [Nearform: Why plan mode is not enough（2026-03-18）](https://nearform.com/digital-community/why-plan-mode-is-not-enough-better-outcomes-with-spec-driven-development)
- [Claude Code permission modes 官方文档](https://code.claude.com/docs/zh-CN/permission-modes)；[issue #79024（plan 审批回归）](https://github.com/anthropics/claude-code/issues/79024)
- [Codex plan.md collaboration 模板](https://github.com/openai/codex/blob/main/codex-rs/collaboration-mode-templates/templates/plan.md)；[update_plan opt-in PR #41744](https://github.com/openai/codex/pull/41744)；[Vaughan 机制考证（2026-08-31）](https://codex.danielvaughan.com/2026/08/31/codex-cli-update-plan-tool-opt-in-external-planning-competing-surfaces/)
- [Antigravity execution modes](https://antigravity.google/docs/cli/modes/)；[Implementation Plan artifact](https://antigravity.google/docs/implementation-plan/)
- [Cursor Plan Mode 官方博客](https://cursor.com/blog/plan-mode)
- [Superpowers subagent-driven development（计划文件+新 subagent 执行）](https://mintlify.wiki/mridullpandey/superpowers/skills/subagent-driven-development)
