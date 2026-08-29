# 故事线总图（v0.7 · 软件 SDLC 定调 · 固定 50 页）

> **对象**：软件 SDLC 上的跨职能研发与交付组织——从产品意图、需求与设计，到 Build / Test / Deploy / Maintain。
> **题目已定**：AI-Native 软件研发组织：从产品意图到生产运维的 SDLC 转型之道。**slogan**：代码不再是瓶颈，流程才是。
> **范围红线**：只讨论软件价值流和 SDLC 控制系统，不外推到销售、市场、客服、财务、人力或一般企业组织设计。
> **篇幅档位 A**：单场加长 Keynote（75–90 min，**50 页已定**）。**独立成篇**（不承接 `deck_ai_sdlc_keynote`）。
> **已锁定结构**：**SDLC 六阶段是主轴**；五层（Prompt→Context→Harness→Loop→Graph）作深度镜头，
> DSH 作参考实现，均在自然接点嵌入，不另起一条主线。本轮只在 50 页内收紧命题、页面职责与转场。

## 沟通任务

> 到结束时，CTO、平台、产品、QA、安全、发布与运维 owner 应该能够共同选出一条价值流试点，
> 用「工件 / gate / owner / feedback」重画它，因为只加速编码会把瓶颈与治理成本推向代码两侧，不会自动改善端到端交付。

## 一句话主线

当 Build 不再是瓶颈，组织要重建的是整条 SDLC：**每个阶段留下可交接的工件，每次转换经过可执行的 gate，
每个判断有 owner，每个结果能回流成下一次 intent**。六阶段说明改造范围，五层说明控制深度，
DSH 说明知识外置、正确路径和可执行反馈如何变成共享 runtime。

## 主轴 + 引子（一张表看全）

| SDLC 主轴 | 深度镜头（五层） | 这一阶段要外置的东西 |
|---|---|---|
| **Plan** | **Prompt**：意图能否被清楚表达 | `intent.md` + product owner 的取舍 |
| **Design** | **Context**：约束能否在建造前被策展 | `spec.md` + 当时生效的 policy/skill 版本 |
| **Build** | **Harness**：执行能否被圈住、拦住、看清 | `plan.md` + 知识 + 沙箱/权限/hooks |
| **Test** | **Sensors + Loop**：证据能否在会话内返回 | product checks + harness evals，两套验证 |
| **Deploy** | **Harness**：提议权与执行权能否分离 | PR evidence + execution-time authorization |
| **Maintain** | **Loop / Graph**：事实能否沿同一受控路径回流 | deterministic trigger → diagnosis → `intent.md` → same gates |
| （收束） | **DSH 参考实现** | knowledge map / capability seam / enforced gate / append-only log |

> 五层只是观察外置与控制深度的镜头，不声称「Plan 的本质就是 Prompt」这类一对一等式。
> 统一落点是「**把怎么正确参与外置成系统**」：工件外置事实，gate 外置机械判定，owner 承担价值判断，feedback 让事实回流。

## 故事弧线（开场 + 三幕）

| 幕 | 内容 | 作用 | 时间(约) |
|---|---|---|---|
| 开场 | 当编码变快，交付为什么没同步变快 | 让听众对照自己的价值流 | 0–6 |
| 第一幕 | 瓶颈转移后，旧控制为什么失效 | 建立「可执行 SDLC」中心命题 | 6–16 |
| 第二幕 | 六阶段如何逐段补齐工件 / gate / owner / feedback | 证明中心命题可落地 | 16–64 |
| 第三幕 | 怎样把六阶段的规则做成软件交付共享控制面 | 用 DSH 参考实现解释工程化与采用顺序 | 64–84 |
| 收尾 | 从最慢的一次交接开始试点 | 把论点变成组织下一步 | 84–90 |

## 5–8 分钟口述主线（内容锁验收稿）

这场 talk 从一个需要听众自己验证的现象开始：当 agent 已经显著压缩 Build 时间，端到端交付是否也同步变快？如果没有，就不要再只看代码生成速度，而要把一条真实软件价值流拆开来看：需求等待了多久，第一次 review 等了多久，测试证据补了几轮，生产审批排了多久，故障信息又花了多久才回到下一次规划。Anthropic 把这个变化概括为「Code is no longer the bottleneck」。这里不把它当成所有组织都成立的事实，而把它当成一个诊断入口：一旦 Build 不再是主要约束，瓶颈就会向代码两侧迁移。

问题在于，传统 SDLC 的控制方式是围绕「代码稀缺、步骤主要由人执行」建立的，默认处理的是人力规模的变更与人速交接，所以会议、文档提醒、逐行检查和阶段闸门还能维持。当 agent 把产出容量突然放大，控制容量却没有一起扩大，系统只会出现两种结果：一种是更多工作排队，交付并没有更快；另一种是为了追赶速度而减少检查，风险和返工转移到下游。于是 AI-native 转型的对象不能只是编码工具，而必须是整套软件交付系统。

这套系统可以用四个问题重新设计：这一阶段留下什么可交接的工件？哪一道规则能够成为真正执行的 gate？谁对不能机械判断的价值、风险和例外作最后决定？什么 feedback 能证明这次改造改善了交付？工件让下一角色不必重新猜测上游意图；gate 把可以确定性判断的规则从文字提醒变成机器关卡；owner 保留人的判断与问责；feedback 则让结果不止停在报表里，而能回到下一次 intent。四个问题合起来，才是一条可执行、可追溯、能持续学习的软件价值流。

沿六阶段看，改造不是给每段各塞一个 AI 助手。Plan 要把模糊需求收成带取舍和验收边界的 intent；Design 要把约束、政策和冲突收成当时有效的 spec；Build 要先有 plan，并在受控环境中执行；Test 不只验证产品改动，也验证 harness 和 gate 本身是否仍然有效；Deploy 要把 agent 的提议权与生产执行权分开，在动作发生时授权；Maintain 要让事件、扫描与生产事实沿同一受控路径回流，重新形成 intent，再经过相同的 gates。这样，六个阶段不再是六段松散流程，而是由工件链接力、由 feedback 闭环的一套运行系统。

五层模型在这里不另起一条故事线。Prompt、Context、Harness、Loop、Graph 只是五个能力与控制深度镜头：意图有没有说清楚，事实有没有给对，执行有没有被圈住、拦住、看清，结果能不能安全回流，多个执行单元能不能在明确合同下协作。它们不等于五个团队，也不与六阶段一一对应。真正的组织原则是共享控制面、分布领域知识：平台提供沙箱、权限、工具准入、门禁、观测和审计的共同基线；产品、架构、服务与政策 owner 继续掌握 intent、context、取舍与例外；治理定义不可绕过的授权和审计规则。

DSH 在最后出现，不是作为唯一答案，而是作为这套控制面可以被工程化的参考实现。它用知识外置减少部落知识，用正确路径把变更路由到明确扩展点，用可执行反馈证明无效动作真的会被拒绝，再用 capability seam 和 append-only log 支撑替换、审批与事实重建。它要证明的不是某个产品更强，而是制度可以进入 runtime：机器守确定性 gate，人守判断 gate，两者都留下可追溯证据。

因此采用顺序也很明确：先让一次交接留下可读工件和明确 owner，再把必须成立的规则做成 gate，等事实可读、门禁可信之后，最后才关 loop。结尾不要求听众重做整个 SDLC，只要求从一条软件价值流里找出最慢的一次交接，为它补齐一个 Artifact、一道 Gate、一个 Owner 和一个 Feedback 指标。这样「代码不再是瓶颈，流程才是」就不只是一句 slogan，而变成一个可以用真实变更和真实数据验证的试点。

## 每一幕的要点

### 开场（钩子 + 五层预告 + harness 引子先立住）
- 问题：**如果**组织的 Build 已经显著加速，端到端交付为什么没同步变快？让听众先用自己的 lead time / queue time 对照，不虚构「翻倍」数据。
- 钩子：**Code is no longer the bottleneck**（Anthropic，标注来源）。
- **P4 五层预告**：五层是后面观察「外置与控制深度」的镜头，不是第二条故事线。
- **P5 harness 引子（先立住）**：模型给能力，harness 给可靠性；组织需要集中建共享控制面，同时把领域 intent/context 留给一线 owner。

### 第一幕：为什么整条 SDLC 要转型
- 当 Build 加速 → 三个后果（瓶颈左移右移 / 旧控制失效 / 治理成本上升）。
- 传统 SDLC 的控制假设：每一步都是人做的；逐行 review、阶段闸门跟不上 agent 产出。
- 转型的本质：从「人启动 / 人交接 / 人机械检查」转向「agent 执行 / 工件交接 / 机器守确定性 gate / 人守判断 gate」。
- 贯穿主线早埋：`intent→spec→plan→diff+tests→PR+review→incident` 是审计的骨架；身份、版本、证据、审批和不可绕过的 gate 让它具备可追溯与问责能力。
- 六阶段 shifts 总表（传统 vs AI-native）。

### 第二幕：六阶段转型（同一组问题，逐段回答）

每阶段都明答四问：**交付什么工件？哪个 gate 能机械执行？谁作最后判断？什么 feedback 证明改造有效？**

- **Plan（Prompt 镜头）**：把模糊需求变成可交接 `intent.md`；product owner 对价值与取舍负责。
- **Design（Context 镜头）**：把政策、标准与矛盾变成带版本的 `spec.md` 与 concern list；policy owner 处理例外。
- **Build（Harness 镜头）**：把执行圈住、拦住、看清；`plan.md`、知识文件、hooks 和隔离环境共同缩小 blast radius。
- **Test（Sensors / Loop 镜头）**：同时验证产品改动和 harness 配置；QA 从逐单执行者转为验证系统 owner。
- **Deploy（Harness 镜头）**：用职责分离、execution-time authorization 和环境分级确保「agent 到 gate 为止」。
- **Maintain（Loop / Graph 镜头）**：确定性触发只在越界时调 agent，结果回流成 `intent.md` 并经过同一组 gates；Graph 只作新兴编排镜头，不宣称已成熟。

### 第三幕：共享控制面 + DSH 参考实现
- 先说清工件链如何具备审计能力：身份、版本、证据、审批、不可绕过的 gate 与可重建事实缺一不可。
- 共享控制面不等于统一所有业务：平台统一权限、工具准入、门禁、观测和审计；领域 owner 管 intent / context / 例外。
- **DSH 参考实现的三条腿**：知识外置、正确路径、可执行反馈。它证明这些不只能写成制度，也能做成 runtime 合同。
- 用插件图 / 事件流 / loop、capability seam、enforced gate、append-only log 分别回答「现在由什么组成 / 刚才做过什么 / 如何替换 / 如何放行 / 如何重建事实」。
- 落地顺序只留一条：**先工件 → 再 gate → 最后关 loop**。插件数、star 和可替换率不进核心故事，避免把组织决策带向生态热度与实现细节。

### 收尾
- 带走一句：**代码不再是瓶颈，流程才是。**
- 回到开场：先用数据找到自己链上最慢的一次交接，选一条价值流，补齐一个工件、一道 gate、一个 owner 和一个 feedback 指标。

## 口径红线

- 前三层成熟，Loop / Graph 新兴（沿用 `-opc`；本 talk 只用它们检查反馈与编排的控制深度，不讲成既定生产范式）。
- 「代码不再是瓶颈」是 Anthropic 论点，引用标注来源；playbook 是 Claude 视角，机制讲透、产品名不唯一。
- 「代码不再是瓶颈」在叙事中作诊断假设；不虚构「代码产出翻倍 / 交付不变」数据，让听众用自身数据验证。
- 不把工件链直接说成审计链；严格口径为「工件链是审计的骨架，加上身份 / 版本 / 证据 / 审批 / 不可绕过的 gate 才具备可追溯与问责能力」。
- DSH 原生机制不是 MCP；说 `ctx.llm`、`ctx.tools`、capability seam、plugin。
- DSH 作参考实现，不讲成唯一产品选型或组织转型的必要前置。
- DSH 命名随大流：`CLAUDE.md` 概念 → `AGENTS.md`；`.claude/skills` → skills 目录；`.claude/agents` → subagents。机制讲透，不绑定 Claude Code。

## 素材索引

- 六阶段 + 15 play：`../_reference/rawdata_anthropic-ai-native-sdlc-playbook.md`
- 五层结构：`../_reference/rawdata_ai-coding-evolution-final/final_v4.md` + `final_v4/`
- Böckeler（Guides/Sensors）：`../_reference/rawdata_ai-coding-evolution-final/final_v4/03-2026-harness-era.md`
- DSH 机制：`../_reference/rawdata_dsh-faq-on-digested/07_borrowing-harness-idea/answer.md`、`../_reference/rawdata_dsh-digested/`
