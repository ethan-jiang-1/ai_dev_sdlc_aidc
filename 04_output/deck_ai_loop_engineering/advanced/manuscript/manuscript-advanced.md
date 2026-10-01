---
title: 文稿 — Loop Engineering 技术产品场
status: draft-for-review
source: advanced/outline/outline-advanced.md（v3 阶梯脊柱）
revised: 2026-10-01
---

# 文稿 — 技术产品场

> 本稿与 [`../outline/outline-advanced.md`](../outline/outline-advanced.md)（v3 阶梯脊柱）同步。每页 `CLAIM` 必须与 outline 的 subtitle 完全相同；**一页一个概念，content 不超过三条**；引用块不上屏。
> 实操轨（90 分钟版）：三道构造档练习，题面与讲者卡在 [`../practice/`](../practice/README.md)，嵌入位置见 outline §8。

## 术语

档｜授权面｜策略件｜裁判（grader）｜负例｜验收（accepted）｜外部结果（outcome）｜交接单｜反馈回路｜定档四问

---

### B01 · 你离开后，它说做完了

**CLAIM**：Loop 的难题不是能否行动，而是回来时凭什么信完成宣告。

**上屏**

- title: 你离开后，它说做完了
- subtitle: Loop 的难题不是能否行动，而是回来时凭什么信完成宣告。
- content:
  - 你离开了；它继续跑；它说：完成。
  - 这份完成宣告，谁按什么证据验收？

> 做片说明（不上屏）：本页只立完成宣告的问题；后续贯穿任务是搜索分页。用一段完成消息和验收者的疑问呈现，日志是教学示意。禁止把系统停机画成有权验收者签认，也不在此页引入三本账细节。

**展开**：假设你授权 agent 给站内搜索增加分页，离开后它继续跑，回来收到「完成」。程序有没有停止、用户路径有没有通过、谁验收了这个版本，目前都未确认。后文逐个交出的决定对应到这个任务，B24 再把完成问题拆成三本账。

**接到下一页**：先说这个词为什么突然到处都是。

### B02 · 为什么有人开始「写 loop」

**CLAIM**：Addy Osmani 将这种转变概括为：让系统接替逐次提示 agent；本场要工程化的是反馈、判断和边界。

**上屏**

- title: 为什么有人开始「写 loop」
- subtitle: Addy Osmani 将这种转变概括为：让系统接替逐次提示 agent；本场要工程化的是反馈、判断和边界。
- content:
  - 从你逐次提示，变成系统组织下一轮。
  - 执行 → 检查结果 → 调整做法，而不是反复发同一句。
  - 能收到反馈，不等于每次都能修对。
- callout: 「你设计一个系统，接替自己提示 agent。」——Addy Osmani（原文节选意译，2026-06-07）

> 做片说明（不上屏）：这页讲提示者位置的转移，不讲模型性能跃升。callout 必须上屏并保留署名；它与三行正文是不同层级。禁止改写成「模型总能知错改错」，禁止把 Boris Cherny 或 Peter Steinberger 未核验的名句放进引号。版面用一条执行—检查—调整路径，不再塞第二个分层模型。

**证据**：Addy Osmani，《Loop Engineering》，发布 2026-06-07、观测 2026-09-26，[原文](https://addyosmani.com/blog/loop-engineering/)："Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead." 这是作者定义，不是效果试验。

**展开**：开场承诺之所以值得尝试，是工作结果可以回到下一次决策中。Anthropic 2024 年的环境反馈工作环与 Sydney Runkle 的验证环都给出了机制形状，但没有证明所有任务都能修好。今天把这个形状工程化：输入能复查、判据能测试、出口能交人。掌握它需要锻炼，阶梯是练法，不是保证。

**接到下一页**：第一步不是放手，而是看哪些决定已经交出去了。

### B03 · 你在哪一档

**CLAIM**：治理从定档开始——从基线看动作、续跑、唤醒三个交接面；交出哪个决定，就检查对应护栏。

**上屏**

- title: 你在哪一档
- subtitle: 治理从定档开始——从基线看动作、续跑、唤醒三个交接面；交出哪个决定，就检查对应护栏。
- content:
  - 基线：你发起、你判断；交动作后，边界内不再逐条批。
  - 交续跑：系统按目标条件决定是否再开一轮。
  - 交唤醒：时间表或事件发起任务；不自动获得前两项授权。

> 做片说明（不上屏）：本场教学映射，非 KOL 统一分类、非可靠性排名。阅读顺序是从少交到多交，真实系统必须逐面核查。不要把 `/loop` 排成「前三级都已配齐」，支线在 B32/B33 才展开。

**备注**：各家 loop 外延不兼容，本场治理的是可审计控制决策，不站队环数。Osmani 按 agency/orchestration 两轴拆分；Runkle 按功能拆四环；Ng 按反馈时间尺度拆三环；它们不等于本页阶梯。Ralph 的裸 bash 形态无内建完成检测；`/goal`、`/loop`、auto mode 是三种不同产品机制。

**接到下一页**：定档有一把公共的尺。

### B04 · 定档四问

**CLAIM**：谁启动下一轮、谁判断完成、谁能改变系统、出了错谁能停下接手——四问在每个档位都有不同答案，这张表就是全场的检查表。

**上屏**

- title: 定档四问
- subtitle: 谁启动下一轮、谁判断完成、谁能改变系统、出了错谁能停下接手——四问在每个档位都有不同答案，这张表就是全场的检查表。
- content:

  - 谁发起下一轮，谁按什么证据判断完成？
  - 谁可改代码、判据与调度配置？
  - 出错时，谁能停下、收到原因并恢复？

> 做片说明（不上屏）：第一行含「启动」「判完成」两问，后两行各一问，共四问，不要删成三问。用四个决策节点呈现，不将四行×三列的密表上屏。下面是讲者检查表，不是厂商统一 schema。

**展开（本场教学映射）**：

| 交接面 | 下一轮发起 | 完成判断 | 可改变什么 | 停止与接手 |
|---|---|---|---|---|
| 基线 | 人 | 人看结果 | 每次请求授权 | 人当场 |
| 动作 | 仍由人 | 仍由人 | 已定义授权范围 | 策略拒绝＋审批入口 |
| 续跑 | 目标条件 | 裁判判条件、人守验收 | 授权范围；执行者不自改判据 | 上限/无进展出口＋交接单 |
| 唤醒 | 时间表/事件 | 另查任务原有判定，不凭唤醒新增 | 调度配置另授权 | 取消传播＋恢复指针＋责任渠道 |

建议每次控制迁移写事件：`goal_rev/action_id/evidence_ref/verdict/decision_source/state_rev/stop_reason/resume_pointer`，本场设计字段，不是产品标准。贯穿分页案例：起初你手动检查再说下一步；后来可分别授权文件修改、按目标续跑或夜间起跑。三项必须分别留证据。

**接到下一页**：先看动作档：省掉逐条批准后，边界怎么执行。

### B05 · 授权面是分级处置表

**CLAIM**：交出动作审批，交的不是开关，是一张表：允许直行、沙箱内跑、必须人批、硬拒绝。

**上屏**

- title: 授权面是分级处置表
- subtitle: 交出动作审批，交的不是开关，是一张表：允许直行、沙箱内跑、必须人批、硬拒绝。
- content:

  - 低风险可直行；可回滚改动只在沙箱内跑。
  - 提交、外部调用先人批；删库、生产变更硬拒绝。
  - 本任务逐类配置，不用一个「全部允许」开关。

> 做片说明（不上屏）：四种处置是本场综合设计，动作例是教学分配，不是所有产品默认策略。分四行状态清单即可，不再增加第五种等级；具体配置以所用产品为准。

**展开**：官方样本：Cursor 对 Shell/MCP/Fetch 三级处置（allowlist→sandbox→classifier，2026-05 changelog）；Codex `exec_policy` 按危险启发式×沙箱能力×项目可信度映射 Skip/NeedsApproval/Forbidden。控制迁移建议每次落事件（`action_id/evidence_ref/decision_source`），不是产品统一 schema。

**接到下一页**：表怎么落地——先看最常见的假动作。

### B06 · 规则要写进策略件

**CLAIM**：提示词说明意图，策略件执行限制；重复点击批准不能替代可执行的授权规则。

**上屏**

- title: 规则要写进策略件
- subtitle: 提示词说明意图，策略件执行限制；重复点击批准不能替代可执行的授权规则。
- content:
  - 提示词：告诉执行者你想要什么，不是执行隔离。
  - 策略件：面外动作由工具层批准、隔离或拒绝。
  - 实际触发一条禁止动作，核对记录里是否真的被拦。

> 做片说明（不上屏）：这是本场设计建议。研究与仓库审计是风险线索，不是同一种样本；不用并排大数字营造行业统计。提示词仍可传递要求，禁止改成「提示词毫无用处」。

**展开**：François Zaninotto（marmelab），[《The State Of AI Harness Engineering 2026》](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html)（2026-09-24，观测 2026-09-26）转引 arXiv 2608.27443：113 人比较中，预写规则组少拦了 20.1 个百分点的坏动作；目前依据该博客转引，不标本稿已核论文全文。该文提到 93% 提示被批准，不能与 113 人研究混成同一试验结果。其仓库审计另在 391 个仓库找到 12 个提交 deny 规则，统计入库规则而非所有运行时策略。这些不是行业授权成功率，也不证明可执行策略的通用效果；本页建议将要求变成能用负例验证的工具层限制。

**接到下一页**：就算写进了配置，还有一层混淆要拆。

### B07 · 策略偏好不等于执行隔离

**CLAIM**：Cursor 明确 Auto-review 不是安全边界；审批偏好与执行隔离是两层配置，不能混为一谈。

**上屏**

- title: 策略偏好不等于执行隔离
- subtitle: Cursor 明确 Auto-review 不是安全边界；审批偏好与执行隔离是两层配置，不能混为一谈。
- content:
  - 审批偏好：倾向批准或拦截什么。
  - 执行隔离：实际能碰到哪些路径和网络。
  - Cursor 明确：Auto-review 不是安全边界。

> 做片说明（不上屏）：产品限定必须与第三行同屏；不写「所有自动审查都无安全作用」。两层是概念对照，文件名只在备注，不当跨产品统一配置。

**证据**：Cursor，《Run Modes》（观测 2026-09-30），[官方文档](https://cursor.com/docs/agent/security/run-modes)："Auto-review is not a security boundary"。具体入口随版本变化；原文归档见 evidence-w W1；Cursor 3.6 changelog 是产品模式发布锚，不是活文档的发布日期。

**展开**：Cursor 的 `permissions.json` 与 `sandbox.json` 是两层机制样本，Run Everything 另需评估。即使策略倾向放行，沙箱仍应限定实际副作用；worker 的 `--workdir` 只是工作目录，不自动约束 bash 的路径访问。

**接到下一页**：表和配置都齐了——批准本身的边界要绑死。

### B08 · 一次批准绑三样

**CLAIM**：一次批准只绑定动作、目标、有效期；公开报告提醒我们，窄授权可能被误当成广授权。

**上屏**

- title: 一次批准绑三样
- subtitle: 一次批准只绑定动作、目标、有效期；公开报告提醒我们，窄授权可能被误当成广授权。
- content:
  - 准许编辑 ≠ 准许提交 ≠ 准许推送 ≠ 永久推送。
  - 一个公开报告：窄范围推送授权被扩成大功能发布许可。
  - 本场建议：绑定动作、目标和有效期；变一个就重新批。

> 做片说明（不上屏）：案例是单用户公开报告，根因未经源码确认，不给发生率。绑定规则是本场设计建议，不是 issue 作者已经实现的标准。

**证据与展开**：[Claude Code issue #95749](https://github.com/anthropics/claude-code/issues/95749)（观测 2026-09-27）报告了窄授权被继承为多文件主干推送。分页案例只授权编辑搜索组件，不意味着准许提交或上线。设计题可记 `{principal, action, target, branch, expires_at, nonce}`，字段仅示意；B11 会用变异测试验证它。

**接到下一页**：授权面还有一个经常被漏掉的维度——人的入口。

### B09 · 审批要可达

**CLAIM**：人看不到动作与风险、状态不可恢复，就不是「已升级」——审批可达性是独立的控制问题。

**上屏**

- title: 审批要可达
- subtitle: 人看不到动作与风险、状态不可恢复，就不是「已升级」——审批可达性是独立的控制问题。
- content:
  - 指定人能看到：动作、目标、风险。
  - 父线程必须能看到子线程的请求。
  - 决定后能从同一状态恢复。

> 做片说明（不上屏）：这页承接作用域：即使边界清楚，人若收不到请求仍不能接手。不是说硬拒绝可由普通审批覆盖；页面不展示内部字段串。

**证据与展开**：[Claude Code issue #67519](https://github.com/anthropics/claude-code/issues/67519)（观测 2026-09-27）用户报告反复授权后仍被拒绝，是单用户报告，根因未确认，不能外推为平台全部审批不可达。拒绝合理性与合法升级可达性分开核；本场建议记录指定 reviewer、送达情况、动作目标和恢复指针。无人响应时保持未授权并停止相应动作，不把请求已发出写成已批准。

**接到下一页**：人不在时拒绝怎么处理——拒绝是引导信号。

### B10 · 拒绝是引导信号

**CLAIM**：拒绝作为工具结果返回并附安全路径提示；拒绝预算是动作熔断，不是轮数上限。

**上屏**

- title: 拒绝是引导信号
- subtitle: 拒绝作为工具结果返回并附安全路径提示；拒绝预算是动作熔断，不是轮数上限。
- content:
  - deny-and-continue：拒绝回传＋"find a safer path"。
  - 重复拒绝达到产品预算后，暂停自动尝试并交人。
  - 拒绝计数管动作越界；轮数上限管整体消耗。

> 做片说明（不上屏）：Claude Code auto mode 是本页机制实例，不把拒绝次数写成行业阈值。被策略硬拒绝的动作不能通过普通审批改名放行；安全替代应仍在授权边界内。

**展开**：Claude Code auto mode 官方文档（文档版本锚包括 v2.1.228+/v2.1.283+ 的默认模式说明，观测 2026-09-26；不是拒绝预算的引入版本）记载连续 3 次或累计 20 次拒绝会停机升级且不可配置。headless 无人可问时终止。分类器设计 "reasoning-blind by design"，见 B16；这些语义均限该文档快照，[官方来源](https://code.claude.com/docs/en/permission-modes)。其他产品按各自实现核查，不迁移数字。

**接到下一页**：这套授权面怎么验证？——用变异测试。

### B11 · 变异测试验证授权

**CLAIM**：把 edit 换成 commit、分支换成 main、时间推到过期——旧批准都应失效；变异仍能通过就不能升档。

**上屏**

- title: 变异测试验证授权
- subtitle: 把 edit 换成 commit、分支换成 main、时间推到过期——旧批准都应失效；变异仍能通过就不能升档。
- content:
  - 依次变异：动作 / 分支 / 目标 / 有效期 / nonce。
  - 每次变异都应拒绝旧批准。
  - 写出 `authorization_drift` 事件。

> 做片说明（不上屏）：本场授权设计题，非产品已有通用 token 标准。五种变异属于一个概念：旧批准不能越域。把原授权和一次变异并排即可，完整字段与测试步骤进备注；禁止实际发起越权生产动作。

**展开**：若任一变异仍能通过，授权面没有真正生效——不能升档。这是把「授权绑三样」变成可测试断言的方法。

**接到下一页**：动作档减少打断，但每轮仍由你判断。要把续跑也交出去，先看目标门票。

### B12 · 门票：goal 三要素

**CLAIM**：交出续跑的门票是可测终态、声明式检查、不变式——外加无进展出口与上限子句。

**上屏**

- title: 门票：goal 三要素
- subtitle: 交出续跑的门票是可测终态、声明式检查、不变式——外加无进展出口与上限子句。
- content:
  - 终态：搜索第二页可打开，返回后查询条件保留。
  - 检查：浏览器走该路径，保留断言结果与截图。
  - 约束：不改搜索接口，不削弱已有检查。
- callout: 「完成由 fresh model 判断，而非干活的模型。」——Claude Code 官方文档（节选意译，观测 2026-09-26）

> 做片说明（不上屏）：分页是本场教学示意，不是官方案例。三行分别讲终态、证明方式、路径约束；callout 署机构，不署 Boris Cherny。独立模型只是减少自判冲突，不保证判断正确，B18 会回收。

**证据**：Claude Code，《Keep Claude working toward a goal》，[官方文档](https://code.claude.com/docs/en/goal)（文档恢复逻辑版本锚 v2.1.269+，观测 2026-09-26；非首次引入版本）："completion is decided by a fresh model rather than the one doing the work." 条件要求一个可测终态、声明检查、重要约束。

**展开**：这里把 B01 的模糊「完成」换成别人也能重复验证的终态。Addy Osmani《Practical Loop Engineering》（2026-08-14，观测 2026-09-26）给了 Lighthouse ≥92、LCP<1.8s、CLI 输出、不改 hooks、两轮无改善和 10 轮上限的完整个人示例；这些数字不能外推。资源与无进展退出在 B14 补齐，合约模板见文末控制实验 §1。

**接到下一页**：goal 之外，这一级还有一条生命线——反馈。

### B13 · 反馈是循环的燃料

**CLAIM**：反馈必须让下一轮改变方向；工件和 evidence_ref 让这条反馈可复查，但不是循环的唯一实现。

**上屏**

- title: 反馈是循环的燃料
- subtitle: 反馈必须让下一轮改变方向；工件和 evidence_ref 让这条反馈可复查，但不是循环的唯一实现。
- content:
  - 第二页可开，返回时查询条件丢了——这是下一轮的输入。
  - 改状态保存，再走同一路径；留下结果供裁判与接手者复查。
- callout: 「验证失败时，把结果和反馈送回 agent。」——Sydney Runkle（原文节选意译，2026-06-16）

> 做片说明（不上屏）：本页只讲回流箭头；分页日志是教学示意。工件是本场的审计设计，不是 loop 必须落盘才存在。callout 必须保留作者、日期，不把 LangChain 四环全画成行业阶梯。

**证据**：Sydney Runkle（LangChain），《The Art of Loop Engineering》，发布 2026-06-16、观测 2026-09-26，[原文](https://www.langchain.com/blog/the-art-of-loop-engineering)："The verification loop adds a grader: something that checks the agent's output against a rubric and, if it fails, sends the result back with feedback." rubric 可以规则判或模型判，不等于所有反馈都是硬规则。

**展开**：反馈改变下一步才形成自我修正。内存中的工具结果也能构成反馈回路；跨轮复查与交接需要将它记录成可检索工件。`evidence_ref` 是本场建议字段，非定义条件。Aider 编辑后 lint 失败回灌是早期机制旁证；结构化数据优先读原始结果文件，别把执行者的总结当原始输出。

**接到下一页**：燃料之外，这一级还要装两个保险丝。

### B14 · 兜底：无进展出口＋上限子句

**CLAIM**：续跑要有兜底——无进展出口避免原地打转，上限约束资源，两个都不替代质量验收。

**上屏**

- title: 兜底：无进展出口＋上限子句
- subtitle: 续跑要有兜底——无进展出口避免原地打转，上限约束资源，两个都不替代质量验收。
- content:
  - 出口：连续 N 轮无改善／无工具调用，停。
  - 上限：轮次、时间、成本子句。
  - 目标达成可提前停；未达成又无进展，也应提前收口。

> 做片说明（不上屏）：无进展出口和资源上限是两种停止原因，同属续跑兜底。N 是本任务设定的符号，不是推荐次数。用两个出口并列，目标达成出口已经在前页语境中；不把任何出口画成自动验收。

**展开**：Claude Code `/goal` 官方文档（恢复逻辑版本锚 v2.1.269+，观测 2026-09-26）记载无进展停机；`stop after 20 turns` 是该文档的上限示例，不是推荐轮数，当前实现按[官方文档](https://code.claude.com/docs/en/goal)核查。目标条件满足可提前停，未满足但无进展亦可停；预算只约束消耗，无进展出口本身也不证明质量。

**接到下一页**：条件立好了——谁来判？

### B15 · 裁判五式选型

**CLAIM**：人判、清单、独立评估器、自判、审批方判定按场景选；执行者自判缺少角色分离，需要额外校验与出口。

**上屏**

- title: 裁判五式选型
- subtitle: 人判、清单、独立评估器、自判、审批方判定按场景选；执行者自判缺少角色分离，需要额外校验与出口。
- content:

  - 可枚举条件：用检查清单；可核终态：用独立评估器。
  - 品味与探索：人定标准；越界动作：审批方判定。
  - 执行者自判：缺少角色分离，需要额外补偿。

> 做片说明（不上屏）：五式是本场选型清单，不是五种强弱等级。检查清单不是裁判本人，仍要指定谁按清单判定；独立评估器不保证准确，下一页讲输入保护。

**展开**：按任务选择判据与判定者。Osmani《Practical Loop Engineering》（2026-08-14）提醒，`/goal` 背后的 evaluator 检查 transcript 中硬规则，不直接判断内容好坏；Runkle 的 verification grader 则可按 rubric 评输出。二者不能混成「独立模型万能验收」。本场建议能用确定性检查的先用检查，业务取舍与人工冲突集中到指定验收点。

**接到下一页**：选完裁判，第一件事是保护它。

### B16 · 保护裁判输入

**CLAIM**：裁判只读可信输入，接口缺字段就拒绝放行；保护的是判定边界，不是再加一条提示词。

**上屏**

- title: 保护裁判输入
- subtitle: 裁判只读可信输入，接口缺字段就拒绝放行；保护的是判定边界，不是再加一条提示词。
- content:
  - 原始工具输出带运行 ID、目标版本；不只读执行者总结。
  - 判据与裁判输入不能由执行者单方面改写。
  - 缺字段、格式坏、超时：保持未判定，不默认通过。

> 做片说明（不上屏）：本场设计建议。输入可信度与测试变更不同，后者留到 B23；不要把所有 grader 都说成 reasoning-blind。

**展开**：Claude Code auto mode 的动作分类器有 "reasoning-blind by design" 输入设计（观测 2026-09-26），但不是所有质量裁判都采用它。promptfoo 的压力样本是缺 `pass` 又无 threshold 时零分仍可能默认放行，说明接口要 fail closed，而非仅要求模型「认真审」。分页案例：裁判须看到返回丢失查询条件的原始断言结果，不能只看到「所有功能已实现」的总结。

**接到下一页**：保护之外，门还有一个覆盖问题。

### B17 · 门要覆盖真实反馈路径

**CLAIM**：门存在不等于门覆盖——嵌套反馈路径要逐边标注哪道门管着它。

**上屏**

- title: 门要覆盖真实反馈路径
- subtitle: 门存在不等于门覆盖——嵌套反馈路径要逐边标注哪道门管着它。
- content:
  - 把嵌套路径画成图，逐边标 bound。
  - 区分 bypassed_bound 与 ineffective_bound。
  - 内层有 turn cap，不代表外层 retry 有限。

> 做片说明（不上屏）：本页只查实际路径覆盖。bypassed_bound 是路径绕过约束，ineffective_bound 是有约束却未限住消耗；二者为研究术语。只画分页任务外层重试与内层轮次上限，不另开第二个预算课题。

**展开**：IAL-Scan 的区分给本场一个检查方法：把实际反馈路径逐边画出，分别找绕过上限（bypassed_bound）与上限无效（ineffective_bound）。它不是任意系统已被证实适用的通用检测器。分页案例：检查命令失败后，外层若无限重跑整个 agent，内层 turn cap 无法限制整段消耗。基线带病、跳过检查与没安排检查也要逐项核对；资源耗尽后如何保存交接，留给 B25。

**接到下一页**：覆盖之外，裁判本身也要被测。

### B18 · 裁判要被单独校验

**CLAIM**：裁判分离只减利益冲突，不保证判对——校验集、判据版本和 fail-closed 接口是裁判自己的门。

**上屏**

- title: 裁判要被单独校验
- subtitle: 裁判分离只减利益冲突，不保证判对——校验集、判据版本和 fail-closed 接口是裁判自己的门。
- content:
  - 校验集：known-fail / ambiguous / adversarial / 人工冲突。
  - 记录 `judge_version / rubric_hash / false_accept / false_reject`。
  - 无效果阈值，不伪造统一放行线。

> 做片说明（不上屏）：本场裁判校验建议，不给统一误判率合格线。known-fail 是已知应失败，ambiguous 是有歧义，adversarial 是压力样本。只展示四类样本与版本记录，不伪造已经完成校验的数字；本页之后练习负例。

**展开**：独立 evaluator 仍可能被样本顺序、自我偏好、谄媚或 Goodhart 代理目标操纵（METR 的 monkeypatch/改时钟是压力样本，不外推发生率）。判据改版后，新旧分数不直接横比。

**接到下一页**：裁判给判之后，逐轮怎么走。

### B19 · 逐轮判断要改变下一步

**CLAIM**：未达成带理由继续、达成只认预设产出、不可能停并交人——判定及理由必须回到下一行动。

**上屏**

- title: 逐轮判断要改变下一步
- subtitle: 未达成带理由继续、达成只认预设产出、不可能停并交人——判定及理由必须回到下一行动。
- content:
  - Not yet met ＋ 理由 → 继续，理由指导下一轮。
  - Met ＋ 预设产出 → 停止候选。
  - Impossible → 停并交人；unknown/超时不强行归入。

> 做片说明（不上屏）：三值判定是 Claude Code 产品样本，本场设计要求判定理由改变下一动作。Met 只做停止候选，Impossible 是裁判信号；unknown/timeout 另留未判定，不冒充 Impossible。用分页失败→理由→下一轮呈现。

**展开**：Claude Code `/goal` 的三值判定是产品机制；本场把它映射为交接控制建议，不当跨产品枚举。分页第 1 轮的返回路径失败，Not yet met 必须附理由驱动第 2 轮；路径通过才成为停止候选。无法取到原始证据或裁判超时，不冒充 Impossible，按原因记未知/待人处理。`blocked/awaiting_human` 是本场控制账建议字段。

**接到下一页**：这一档的专属事故，从这里开始。

### B20 · 专属事故：提前宣告完成

**CLAIM**：交出续跑后最大的敌人是提前宣告完成——「完成」住在哪一层，要追到驱动代码。

**上屏**

- title: 专属事故：提前宣告完成
- subtitle: 交出续跑后最大的敌人是提前宣告完成——「完成」住在哪一层，要追到驱动代码。
- content:
  - 分页文件都齐了，不等于返回路径已经通过。
  - Anthropic 官方示例源码：通过数只展示，不驱动完成停机。
  - 检查到目标通过后，谁让驱动程序停？要追到代码。

> 做片说明（不上屏）：这是特定 demo 的源码观察，不是 Claude Code `/goal` 的反例或 Anthropic 生产做法。检查通过与停机分支必须分开画，禁止标题写「官方 agent 永远不停」。

**证据与展开**：Anthropic，[claude-quickstarts/autonomous-coding](https://github.com/anthropics/claude-quickstarts/tree/main/autonomous-coding)（源码观测 2026-09-28；evidence-l 对应 `agent.py`/`progress.py`）：正常迭代路径是 `while True`，`max_iterations` 可限制轮数，`count_passing_tests` 用于打印，无「全部通过即退出」分支。异常、进程终止另计。2025-11-26《Effective harnesses for long-running agents》指出提前宣告完成，并提供清单与端到端检查；demo 的判停实现并未覆盖博客提出的全部目标。这是本场源码判读，不将博客、demo 与 `/goal` 混成同一实现。

**接到下一页**：防它有三层。

### B21 · 防它第一层：清单逐条判定

**CLAIM**：「整个项目做完了」没法判，「第 37 条通过」可以——只许改完成标记这一个字段。

**上屏**

- title: 防它第一层：清单逐条判定
- subtitle: 「整个项目做完了」没法判，「第 37 条通过」可以——只许改完成标记这一个字段。
- content:
  - 分页清单：打开第二页／返回保留条件，分别检查。
  - 每项从未完成起步；只有对应证据成立才改标记。
  - 单项通过≠全项目完成，驱动层另核停机条件。

> 做片说明（不上屏）：清单是本场把官方长程 harness 做法用于分页的示意。JSON、优先级与初始化细节留在展开，不把项目条目数当规模门槛。

**证据与展开**：Anthropic，《Effective harnesses for long-running agents》（2025-11-26，观测 2026-09-26），[原文](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)。官方 claude.ai clone 样例有 200+ feature，全部初始化未通过，要求只翻 `passes` 而不弱化清单，JSON 是该实践选择。分页清单是本场编排：先保留基线，再做最高优先级未完成项，一次一项；完整步骤在手册，不将此实现说成唯一循环定义。

**接到下一页**：第二层管「通过」的成色。

### B22 · 防它第二层：端到端验证才翻完成

**CLAIM**：真实路径要被检查；单测或 curl 只证明各自覆盖的条件，不能单独证明用户路径。

**上屏**

- title: 防它第二层：端到端验证才翻完成
- subtitle: 真实路径要被检查；单测或 curl 只证明各自覆盖的条件，不能单独证明用户路径。
- content:
  - 浏览器输入查询 → 第二页 → 返回，核对条件保留。
  - 接口响应成功，只证明接口；按钮可用还要走用户路径。
  - 留下该版本的断言结果与截图，才有翻标记的依据。

> 做片说明（不上屏）：同一分页任务，服务端通过但返回状态丢失是教学反例。端到端检查有覆盖边界，也不证明用户满意或线上收益。

**展开**：Anthropic 长程 harness 强调端到端自验证，本场将其用于用户路径。单测与 curl 对各自覆盖条件仍有效，不应否定；只是不足以单独证明前端交互。页面加载、查询结果、返回状态逐项断言，先核环境基线与目标版本，保留原始记录。业务采用率仍在 B24 结果账另记。

**接到下一页**：真实路径通过之后，还要确认检查没有被执行者削弱。

### B23 · 防它第三层：检查不能被削弱

**CLAIM**：删、禁或放宽检查不能换来合格产出；检查变更必须独立审查，不能由执行者自行放行。

**上屏**

- title: 防它第三层：检查不能被削弱
- subtitle: 删、禁或放宽检查不能换来合格产出；检查变更必须独立审查，不能由执行者自行放行。
- content:
  - 返回断言被删了：测试通过，也不能翻完成。
  - 核对前后检查清单：删除、跳过、放宽、缺失。
  - 合理新增或调整测试，走独立审查再纳入基线。

> 做片说明（不上屏）：保护检查不等于工程中永不改测试。区别在谁有资格改变验收判据；不要把所有测试修改写成作弊。输入保护已在 B16 讲过，本页只核检查差异。

**展开**：Kent Beck《Augmented Coding: Beyond the Vibes》（2025-06-25，观测 2026-09-27）个人记录把禁用/删除测试列为跑偏信号，不是发生率证据。本场核对 `skip`、删文件、断言降级、`|| true`，并核基线已有失败与新增失败。硬 hook 或写权限能保护指定基线，但新增功能需要新测试，须另行审查；执行者不能一边削弱检查一边宣告成功。

**接到下一页**：事故防住之后，是出口与账本。

### B24 · Stop ≠ Accepted；三本账

**CLAIM**：控制状态、产出验收、外部结果三本账分开记——谁停的、谁验收的、结果谁在何时复查。

**上屏**

- title: Stop ≠ Accepted；三本账
- subtitle: 控制状态、产出验收、外部结果三本账分开记——谁停的、谁验收的、结果谁在何时复查。
- content:
  - 控制账：`running/blocked/awaiting_human/stopped` ＋ `stop_reason`。
  - 验收账：`accepted_by ＋ evidence_link`。
  - 结果账：`outcome_status ＋ owner ＋ next_check`。

> 做片说明（不上屏）：三本账并列呈现，不画 stopped→accepted→outcome 的单条状态迁移。字段是本场设计：控制问为何停止，验收问谁签认何版本，结果问何时查真实用户。每条保留责任主体，不只剩三个英文状态。

**展开**：三本账是本场设计，非产品统一状态机。分页案例的目标检查成立可记录 `verdict=Met`；循环真正停止另记 `control_status=stopped` 和原因；验收者对照需求签认才记 `accepted_by`。用户采用率尚未观测，记 `outcome_status=outcome_pending` 和复查责任人。三个字段能同时成立，不把 `accepted` 当控制账的下一状态。硬拒绝/待人处理也按原因分列，不默认完成。

**接到下一页**：控制账里另一种常见停机原因，是资源耗尽——它不证明质量。

### B25 · 资源上限是包络，不是质量分

**CLAIM**：资源上限只管花费，不替代质量判定；耗尽先保全状态并交接。

**上屏**

- title: 资源上限是包络，不是质量分
- subtitle: 资源上限只管花费，不替代质量判定；耗尽先保全状态并交接。
- content:
  - 预算只限制消耗，不替代目标检查与验收。
  - 耗尽前保存版本、最后反馈、停止原因和恢复指针。
  - 谁接手、何时复核？必须随保存记录一起交出去。

> 做片说明（不上屏）：本场资源交接设计；路径覆盖已在 B17 讲过，这页不重画嵌套图。不要用轮数或时长当质量刻度。

**展开**：分页返回路径还没修好时预算耗尽，应记录未验收并保留失败证据，不能改成「完成」。包络覆盖整棵执行树，需核 agent/tool retry/evaluator/scheduler 的消耗；`RemainingSteps` 只是框架机制实例，不是所有运行时保证。GitHub Copilot 云端 agent 文档有不可延长超时实例（观测 2026-09-27），具体数值只按所用版本文档核查，不抄通用上限。

**接到下一页**：包络烧尽或熔断触发，系统就会停——停了之后怎么办，是下一页。

### B26 · 停机不是统一语义，交接才是终点

**CLAIM**：为什么停、谁接手、从哪恢复——交接单答不全就不算升级；硬拒绝不能改名「待人批准」。

**上屏**

- title: 停机不是统一语义，交接才是终点
- subtitle: 为什么停、谁接手、从哪恢复——交接单答不全就不算升级；硬拒绝不能改名「待人批准」。
- content:
  - `deny_hard` → blocked，不可被普通审批覆盖。
  - 熔断后请求送达 → awaiting_human；接手入口不可达 → blocked。
  - 交接单：为什么停、停在哪个版本、谁接手、从哪恢复。

> 做片说明（不上屏）：状态名是本场控制账示意，产品实际出口以其文档为准。禁止把 hard deny 画成普通「等待批准」；审批不可覆盖强策略。

**展开**：本场建议字段为 `feature_id/action/target/thread_id/decision_source/denial_reason/authorized_scope/reviewer/resume_pointer`，不是标准 schema。父线程须看见子线程请求，恢复前重核当前目标、授权与证据新鲜度。认证、额度、上下文与模型可用性失败如何暂停/清目标，重试几次，由所用运行时决定；不能把某一实现的出口套到所有产品。

**接到下一页**：机器的部分讲完了——有一路输入不能断：你的。

### B27 · 人的反馈要留在环里

**CLAIM**：纠偏、品味、拒绝的理由回灌下一轮——完全静默不是目标；人的角色是最高处的判断，不是传话筒。

**上屏**

- title: 人的反馈要留在环里
- subtitle: 纠偏、品味、拒绝的理由回灌下一轮——完全静默不是目标；人的角色是最高处的判断，不是传话筒。
- content:
  - 把模型不知道的用户与业务约束，写回目标与样例。
  - 纠偏带理由和版本，供下一轮消费；方向与验收另留责任人。
- callout: 人有「上下文优势」，要把模型不知道的知识注入系统。——Andrew Ng（原文节选意译，2026-06-30）

> 做片说明（不上屏）：Ng 说的是信息差，不是人永远比模型有品味。callout 保留姓名与日期。三环是反馈视角，阶梯是决策交接视角；禁止把 Ng 三环改画成三种自主度。

**证据**：Andrew Ng，《Loop Engineering: My 3 Key Loops for Building 0-to-1 Products》，The Batch/X，2026-06-30，[一手归档对应原帖](https://x.com/AndrewYNg/status/2071988145667928442)："So long as the human knows something the AI does not, human-in-the-loop is needed to inject that knowledge into the system." 库内全文已核。

**展开**：Ng 的三环是 agentic coding、developer feedback、external feedback。前者提供快速实现证据，中环把人的新判断写回规格，外环用真实用户行为更新方向；它们可以出现在任何交接档。分页可正确运行，但真实用户不用第二页，业务判断仍要回灌。机器能辅助总结，方向标准和最终责任不能默认转交。Ronacher 2026-06-23 的角色成本是个人旁证，不代替 Ng 的信息差论证。

**接到下一页**：把「何时再跑」也交出去后，这些责任不会消失。

### B28 · 两种运行边界

**CLAIM**：会话内定时与跨会话持久是两种边界——醒来不等于达成。

**上屏**

- title: 两种运行边界
- subtitle: 会话内定时与跨会话持久是两种边界——醒来不等于达成。
- content:
  - 会话内运行：会话结束，任务不再在本机继续。
  - 跨会话调度：持久状态、取消、预算、接手另配。
  - 唤醒先恢复状态、复核授权与预算，再选择工作。

> 做片说明（不上屏）：运行边界与完成判断是两回事。页面无分钟数，禁止把 Claude Code 会话定时与 Managed Agents 云部署画成同一套参数。

**展开**：Osmani《Practical Loop Engineering》（2026-08-14，观测 2026-09-26）区分会话循环与云端调度；Claude Code `/loop` 活文档的固定/动态间隔仅属该产品。Runkle 的 event-driven loop 是事件触发工作，不自动授予完成判定权。`/goal` 处理条件续跑，auto mode 管轮内动作审批，外部 webhook/cron 管起跑；选择要分别核权限和生命周期。唤醒序列是本场设计建议，不是厂商统一 API。

**接到下一页**：跨会话的第一件硬事——取消。

### B29 · 取消要传播到 worker

**CLAIM**：面板关闭不算停——调度器和运行中的进程都要收到取消，幂等与防重入要预先设计。

**上屏**

- title: 取消要传播到 worker
- subtitle: 面板关闭不算停——调度器和运行中的进程都要收到取消，幂等与防重入要预先设计。
- content:
  - 公开报告：任务已关闭，停止信号未传播到 tmux 会话。
  - 核对三步：调度器不派新／worker 真退出／副作用停止。
  - 同一事件重复投递怎么办——幂等键预先设计。

> 做片说明（不上屏）：只称公开报告，不推出平台普遍缺陷。取消核对是本场设计，不把 UI 状态或下次计划列表为空当充分证据。

**证据与展开**：[Claude Code issue #46787](https://github.com/anthropics/claude-code/issues/46787)（2026-04-11，观测 2026-09-28）报告 "the kill did not propagate to the actual tmux sessions"，仅作失败路径样本。检查停止要核三项；Cursor Automations 的 fork PR 失败出口另属该产品。停止与去重证据都要留存，不混成一个面板开关。

**接到下一页**：跨会话还要管钱和时间。

### B30 · 预算是花费阀不是完成

**CLAIM**：按会话计不等于跨次总额；被遗忘的循环要有过期时间；异常循环要有检测。

**上屏**

- title: 预算是花费阀不是完成
- subtitle: 按会话计不等于跨次总额；被遗忘的循环要有过期时间；异常循环要有检测。
- content:
  - 单会话预算≠跨任务总额；总账要有负责人。
  - 被遗忘的任务要过期；触顶后保状态，不记完成。
  - 异常重复要检测并交人，先核产品是否真的启用。

> 做片说明（不上屏）：本页讲跨次预算责任，不讲计价换算。费用、分钟、过期天数全留备注，禁止拼成「通用推荐参数」。

**展开（分产品核查）**：Anthropic Managed Agents（API beta header `managed-agents-2026-04-01`，观测 2026-09-30）的示例 `max_list_cost.amount="125", currency="USD"` 是 125 美分即 $1.25，不是推荐预算；触顶 `budget_reached`，在途可稍超额，新消息 400，可调整预算恢复原会话，按会话计不代表跨次总額。Claude Code scheduled-tasks 文档（观测 2026-09-26）有 7 天过期和约 20 分钟兜底唤醒，另属本机会话任务；不套到云部署。OpenRouter 的 doom-loop 检测是独立产品机制，启用方式与默认值按当前文档，不复制到其他系统。

**接到下一页**：三个交接面的成本都见过了——这次该多交哪个决定？

### B31 · 升档门禁

**CLAIM**：按交接面设置门禁：动作验授权，续跑验目标与裁判，唤醒验取消与恢复；适用检查必须演练，不靠轮数说话。

**上屏**

- title: 升档门禁
- subtitle: 按交接面设置门禁：动作验授权，续跑验目标与裁判，唤醒验取消与恢复；适用检查必须演练，不靠轮数说话。
- content:
  - 动作：授权变异失效；允许／人批／硬拒绝三路走通。
  - 续跑：目标负例被拦；裁判校验、无进展与上限生效。
  - 唤醒：取消到 worker；状态能恢复，跨次预算与接手可达。

> 做片说明（不上屏）：这是本场升档检查编排，不是行业认证。三行分别对应交接面，不能解释为动作档也必须有 goal 与独立完成裁判。适用检查必须做；不适用要写明理由，不靠空格默认通过。

**展开**：先写拟交出的决定，再挑相应负例。动作面做作用域变异与审批路径演练；续跑面用已知失败/成功样本校验目标门与裁判、模拟资源/无进展停止；唤醒面模拟取消、重复投递、reviewer 不可达与恢复后授权过期。若系统组合三个面，各面检查都需通过；只读定时巡检不因使用 scheduler 自动获得写入或 goal 续跑权。人工判定冲突时暂停自动验收与升档，记录判据版本和责任人。完整演练见手册与文末控制实验 §10。

**接到下一页**：门禁之上还有两条岔路——不是必经之路。

### B32 · 支线 A：多主体编排

**CLAIM**：写入拓扑未收敛——共同问题只有避免冲突、合并与验证；改动者不能自行放行。

**上屏**

- title: 支线 A：多主体编排
- subtitle: 写入拓扑未收敛——共同问题只有避免冲突、合并与验证；改动者不能自行放行。
- content:
  - 案例有分工编排，也有各自写入再合并；拓扑未统一。
  - 共同要处理：写入冲突、合并、独立验收。
  - 预算覆盖整树；先核写入所有权和验证器可靠性。

> 做片说明（不上屏）：可选方向，不是唤醒之后的必修等级。下面是不同场景案例，不当跨产品最佳拓扑；不将 Carlini 的个人任务条件写成普遍安全阈值。

**展开**：Anthropic 多主体研究系统（2025-06-13）采用编排器-工人；Cognition/Walden Yan（2026-04-22）建议当前受约束写入；Carlini《Building a C compiler with a team of parallel Claudes》（2026-02-05，观测 2026-09-30）记录 16 代理、约 $20k 的特定任务，各自 clone/push/merge。他的原话 "it's important that the task verifier is nearly perfect, otherwise Claude will solve the wrong problem" 说明该案例的验证器依赖，不保证一般任务可行。三者不能证明共同拓扑或行业收益；可从有界任务进入，不以调度授权为前置。

**接到下一页**：另一条岔路——让循环改自己。

### B33 · 支线 B：改进循环本身

**CLAIM**：四层权限：人改→代理建议→受控外围→自动改核心；自动改写判据仍未成熟，提案与应用必须分离。

**上屏**

- title: 支线 B：改进循环本身
- subtitle: 四层权限：人改→代理建议→受控外围→自动改核心；自动改写判据仍未成熟，提案与应用必须分离。
- content:
  - 权限光谱：人改 → 代理提案／人审 → 受控外围 → 自动改核心。
  - 局部实例：代理改写工具描述；发布与独立验收另核。
  - 自治授权未成熟：提案、评估、应用须分离。

> 做片说明（不上屏）：四层是本场权限光谱，非事实上的四级成熟度。局部工具描述改写不能证明已由代理自主发布、独立验收或获得核心判据修改权。

**证据与展开**：Anthropic，《How we built our multi-agent research system》（发布 2025-06-13，观测 2026-09-30），[原文](https://www.anthropic.com/engineering/multi-agent-research-system)：代理测试 MCP 工具并改写工具描述是外围局部机制实例；原文不建立通用自治授权政策。Morris 的 flywheel 是人在环上修 harness，不等于代理已获自改权；GEPA/DSPy 的提案-评估结构只作参考。Shankar 的 criteria drift 提醒判据可能随评估漂移；自动修改核心验收门仍属未成熟方向。

**接到下一页**：收尾之前，拆一个流传最广的传说。

### B34 · 高手的错觉

**CLAIM**：「完全放手也出色」可能隐藏任务选型、环境和人的判断；只复制放手行为，不能保证复制了这些条件。

**上屏**

- title: 高手的错觉
- subtitle: 「完全放手也出色」可能隐藏任务选型、环境和人的判断；只复制放手行为，不能保证复制了这些条件。
- content:
  - 教学假设：目标与判断藏在高手的上下文里。
  - 放手行为可复制，任务选型与兜底条件却未必被复制。
  - 先写出可验证护栏，再判断自己能交出什么。

> 做片说明（不上屏）：高手画像是教学假设，不指真实 KOL。只讲复制条件的缺口，不证明复杂任务必失败，也不讽刺受众。用放手动作与不可见条件两栏，承接 B33 的权限边界，再回到四问。

**展开**：呼应开场：系统能接替逐次提示，不保证它接替了你心里的判断。所谓「完全放手」可能隐藏了任务选型、测试环境、人的周期纠偏，不能只复制操作行为。本场的教学建议是把这些判断变成可测试、可交接的工件；不声称所有高手每轮都在纠偏，也不拿个人经验证明无人值守安全。Osmani《Practical Loop Engineering》的 taste/judgment 警告是一手支撑，B27 的 Ng 上下文优势解释为什么知识仍要回到系统。

**接到下一页**：回去的第一步，不是配工具。

### B35 · 先定档，再爬

**CLAIM**：四问答不出就留在原档——那是控制决策，不是失败；只为本次交出的决定配相应检查表。

**上屏**

- title: 先定档，再爬
- subtitle: 四问答不出就留在原档——那是控制决策，不是失败；只为本次交出的决定配相应检查表。
- content:
  - 四问：谁启动／谁判完成／谁能改系统／出错谁接手。
  - 动作查授权；续跑查目标与裁判；唤醒查取消、预算与恢复。
  - 单次不用造循环；按风险先配最小护栏，适用检查未过就不升。
- callout: 「建循环，但仍要做工程师，不只是按启动的人。」——Addy Osmani（节选意译，2026-06-07）

> 做片说明（不上屏）：回收 B02 提示者位置转移、B04 四问和 B31 分面门禁。检查项按本次交接选，不把最高档全部字段压到基线。手册书名是操作入口，不追加内部项目名。

**证据与展开**：Addy Osmani，《Loop Engineering》，[原文](https://addyosmani.com/blog/loop-engineering/)（发布 2026-06-07，观测 2026-09-26）："Build the loop. But build it like someone who intends to stay the engineer, not just the person who presses go." 本场收束建议是交一个决定、演练相应护栏，并把停止/验收/外部结果分别记录。机制存在不证明质量、吞吐或返工收益；不将 Steinberger 旧文中的个人瓶颈判断改成一般调度收益结论。逐面操作见《循环交接手册》。

**收束**：Loop Governance 的硬核不是让循环活得更久，而是继续、停止、升级和交还都留下能复查的理由。它是一门要锻炼的手艺——阶梯就是练法，从你站的那一级练起。

---

# 工程师追问卡（不上屏）

> 按 B 页提供可追问的机制、反例和边界。伪配置是本主题设计题，产品参数保留产品语境；`stop_conditions` 的「双环三层」仍是研究抽象，SOP 以 `03_practice/loop_governance/result/manual.md` 为准。

## B01–B04 · 钩子、故事与定档

- **B01**：完成钩子在何时检查、检查哪棵 tree、绑定哪份证据；可疑交付状态例 `PR created; CI failing; accepted_by=null; outcome_status=outcome_pending`。
- **B02 讲法**：半分钟讲 Osmani 的提示者位置转移，核验引句在 B02。反馈让下一步可调整，不保证每轮修对；「需要锻炼」在收束回收。
- **B03**：Ralph 无内建 stop，TODO 耗尽凭 taste；`/goal`/`/loop`/auto mode 分别是条件、时间/事件、轮内审批语义。
- **B04**：控制迁移事件字段 `goal_rev/action_id/evidence_ref/verdict/decision_source/state_rev/stop_reason/resume_pointer`——设计题非标准 schema。

来源：manual §7、§9–10；evidence-b §1、§4a–c。

## B05–B11 · 动作档

- **B05**：授权最小绑定 `{principal, action, target, branch, expires_at, nonce}`；`cron` 只唤醒，不代替授权。
- **B08**：edit 批准不自动覆盖 commit/push、另一分支或另一 feature；越权案例只有单用户反例，不外推发生率。
- **B10**：3/20 是 Claude auto mode 实例，官方明写不可配置；headless 直接终止；OpenAI 未公开相同阈值。
- **B11**：变异测试逐项改 `action/branch/target/expiry/nonce`，每次都应拒绝旧 token 并写 `authorization_drift` 事件；未合并 PR 只是候选机制。

来源：manual §2、§6–7、§9；backbone §3；evidence-f；evidence-u S4a；evidence-w W1。

## B12–B14 · 门票与燃料

- **B12**：`terminal_state + check + constraints + stop_clause` 四件套；Lighthouse 数字是个人实践例。
- **B13**：建议审计通道 `cmd → exit_code + artifact → durable evidence_ref → next action`；没有工件仍可在内存中反馈，区别在下一步是否消费结果。DAG 下游注意修复—震荡。
- **B14**：`/goal` 的 turn/time 子句与无进展停机见同页产品锚（文档恢复逻辑 v2.1.269+，观测 2026-09-26）。目标达成、无进展、资源耗尽三种理由分开，上限不判质量。

来源：manual §2；evidence-b §4a；stop_conditions/01_machine_gates/insights #13。

## B15–B18 · 裁判

- **B15**：五式选型表在 manual §3（单一事实源）；人判 taste 见 Huntley（evidence-b §1）。
- **B16**：promptfoo 缺 `pass`/无 threshold 反例；hook 做法 playbook Test 节；`reasoning-blind by design`（evidence-b §4b）。
- **B17**：IAL-Scan 的 `bypassed_bound/ineffective_bound` 区分；嵌套路径逐边标 bound。
- **B18**：METR monkeypatch/改时钟是压力样本不外推；校验集四类＋判据版本化；Hamel/Shankar FAQ 是单源建议，无效果对照。

来源：stop_conditions/02_hard_caps/insights #15；03_verdict_split/insights #6–10；evidence-2026-09-28-m/n/r-*。

## B19–B23 · 出口与防线

- **B19**：状态机建议（hard_deny→blocked 等）是本主题设计；unknown 不归 Impossible。
- **B20**：quickstart 源码逐行（观测 2026-09-28）；`count_passing_tests` 只打印不停机。
- **B21**：feature_list 结构 `category/description/steps/passes`； initializer 展开；只许改 `passes`。
- **B22**：固定开场序列与基线修复（evidence-b 问题2§1）。
- **B23**：删测反例（evidence-i Beck）；测试削弱检测模式清单。

来源：manual §5、§10；backbone §1–2；digested/07；evidence-i Sources 3/5。

## B24–B26 · 三本账与包络

- **B24**：work-row 控制行试点字段与退出条件（manual §5）；多 feature 行仅当并行且交接丢信息时建。
- **B25**：预算包络与耗尽前状态保全；`RemainingSteps` 与 Copilot 超时只是各自框架/产品实例（evidence-i Source 8）。
- **B26**：停机、硬拒绝、待人处理按原因区别；产品如何清目标或重试要核实现，不外推固定次数。交接字段是本场设计。

来源：manual §5/§7；backbone §2；digested/07；evidence-i。

## B27–B30 · 人的反馈与唤醒

- **B27**：Ronacher 无人值守证词（evidence-u S1）；Ng context advantage（digested/08）；Steinberger "usually I'm the bottleneck"（evidence-a，原话未说「自动化更慢」）。
- **B28**：唤醒序列 `wake → restore → validate → choose → run`；trigger 四类对照（manual §6）。
- **B29**：zombie 单用户公开报告（evidence-o）；Cursor fork PR 失败出口（evidence-w W2）。
- **B30**：Managed Agents 预算与状态限 API beta `managed-agents-2026-04-01`（观测 2026-09-30），evidence-w W3/W6；会话任务过期与兜底限 Claude Code scheduled-tasks（观测 2026-09-26），evidence-b §4c。doom-loop 是 OpenRouter 等具体实现，不通用。

## B31–B35 · 门禁、支线、尾巴

- **B31**：按本次交接面选择授权、目标裁判或唤醒取消检查；适用项留演练证据，不适用写理由。故障注入清单见文末控制实验 §10，不要求低风险动作先交全部目标判停。
- **B32**：Carlini C 编译器案例（evidence-u S3）；Cognition 受约束并发（S2）；Anthropic 编排器-工人（S2）；「不以交唤醒为前置」。
- **B33**：四层权限（00-map 支线 B 行）；工具描述改写（S5）；GEPA/DSPy 只作结构参考；Shankar criteria drift 反例。
- **B34**：抽卡＝retry 的口语版（判据一）；Osmani「别把品味和判断一起委托」；本页不点名真实人物。
- **B35**：按本次交出的决定选择相应检查项，基线可保持人工判断；效果证据缺口见 landscape §7，不以产品机制或个人经验冒充收益证明。

---

# 可直接拆解的控制实验（不上屏）

> 一套待接入真实运行器的演示设计，对应各交接面护栏。所有 YAML/JSON/伪代码是本场设计模板，不是可直接执行的产品 API 配置；接入时须实现项目权限、预算控制与审计存储。例中的编号、时间、样本计数只作教学示意，不可原样用于生产；产品参数另按同页出处核查。

## 1. Goal / Eval 合约（续跑档门票）

```yaml
id: search-pagination-v1
terminal_state:
  - page_2_opens
  - query_and_filters_survive_navigation
checks:
  - command: npm test -- search-pagination
    type: deterministic
  - command: npm run e2e -- search-pagination.spec.ts
    type: environment_path
constraints:
  branch: agent/search-pagination
  forbidden: [public_api_change, test_deletion, push]
stop:
  retryable: [page_2_button_click_failed, route_404]
  impossible: [required_dependency_unavailable]
  resource: [wall_clock, cost, retry_budget, expiry]
external_outcome:
  status: outcome_pending
  owner: product-owner-7
```

工程审查四问：终态可观察吗？检查覆盖实际路径吗？约束由运行器 enforce 吗？`impossible` 是逻辑不可满足还是暂时不可见？外部采用率不能填 `Met`。

## 2. Action authorization：把批准做成可失效对象（动作档护栏）

```json
{
  "token_id": "auth-0042",
  "principal": "search-agent",
  "action": "edit",
  "target": "src/search/**",
  "branch": "agent/search-pagination",
  "scope": ["src/search", "tests/search"],
  "expires_at": "2026-09-28T18:00:00Z",
  "nonce": "run-0042",
  "denied_actions": ["commit", "push", "deploy"]
}
```

**变异测试**：依次改 `action`→commit、branch→main、target→`deploy/`、时间→过期、nonce→下一轮；每次都应拒绝旧 token 并写 `authorization_drift` 事件。变异仍通过，不能升档。

## 3. Environment Feedback：证据通道而不是聊天文本

```text
run command
  ├─ exit_code
  ├─ stdout/stderr artifact
  ├─ browser trace / screenshot / network log
  └─ commit/tree identity
          ↓ durable evidence_ref
     evaluator input
          ↓ verdict + reasons
     next action or control state
```

最小事件：

```json
{
  "run_id": "run-0042",
  "action_id": "act-0042",
  "tree": "git:abc123",
  "exit_code": 1,
  "evidence_ref": ".loop/runs/run-0042/",
  "observed": ["page_2_button_click_failed"],
  "created_at": "2026-09-28T16:31:00Z"
}
```

本节是审计模式模板：下一轮消费原始观察；带 `evidence_ref` 后可跨轮和交接复查。内存反馈也能组织循环，不以该字段定义 loop。嵌套工具、retry、evaluator 都纳入实际 feedback path。

## 4. Eval schema：缺证据必须 fail closed

```json
{
  "verdict": "NotYet",
  "reasons": ["page_2_button_click_failed"],
  "evidence": [".loop/runs/run-0042/browser-trace.zip"],
  "evaluator": "search-checker-v3",
  "rubric_hash": "sha256:...",
  "input_digest": "sha256:..."
}
```

在本场审计模板中，`verdict/reasons/evidence/rubric_hash` 缺一就拒绝自动放行，保留未判定状态；这不是 loop 的存在条件。`Met` 无证据不能进入验收，未知 verdict 不得降级成 true/false。promptfoo 缺 `pass`/无 threshold 反例说明评估器接口本身要测。

## 5. 裁判校验集与反操纵

```yaml
cases:
  - id: known-fail-route
    expected: NotYet
  - id: known-pass-route
    expected: Met
  - id: ambiguous-copy
    expected: human
  - id: adversarial-test-weakened
    expected: NotYet
  - id: human-conflict-01
    expected: record_conflict
record:
  judge_version: search-checker-v3
  rubric_hash: sha256:...
  false_accept: 0
  false_reject: 0
```

至少保留 known-fail、ambiguous、adversarial、人工冲突四类。`false_accept=0` 只是本批样本观察，不是质量证明；METR reward-hacking 样本说明独立 evaluator 仍可能被输入、时钟或代理目标操纵。

## 6. 控制决策与三本账（本场设计，非产品统一状态机）

```text
控制账：观察反馈
  ├─ hard_deny -------------------------→ blocked
  ├─ unknown / missing evidence --------→ blocked；合法请求送达后 awaiting_human
  ├─ Not yet met + retryable + budget ---→ running（带理由下一轮）
  ├─ Met + artifact complete -----------→ 停止候选，实际退出后记 stopped
  ├─ Impossible ------------------------→ stopped（明确理由并交人）
  └─ budget exhausted ------------------→ stopped（保全状态并交人）

验收账：unaccepted --指定验收者签认+证据--> accepted
结果账：outcome_pending --真实用户观测--> outcome_met / outcome_not_met
```

三个账各记事件，可同时是 `control=stopped; acceptance=unaccepted; outcome=outcome_pending`。`Met` 不改变验收账；签认也不改写停止原因。`Impossible` 与证据当前不可见要分开，后者按原因记 blocked 或 awaiting_human。各分支保留理由、证据引用与下一责任人；使用者还需定义异常、暂停和恢复的真实实现。

## 7. 资源包络与优雅耗尽

```yaml
budget:
  turns: task_specific
  wall_clock: task_specific
  cost_usd: explicit
  retry_budget: explicit
  deadline: explicit
  nested_paths: [agent, tool_retry, evaluator, scheduler]
checkpoint_before_exhaustion: true
on_exhaustion:
  - persist_state
  - persist_last_feedback
  - write_stop_reason
  - assign_reviewer
  - emit_resume_pointer
```

`max_turns` 只覆盖一个维度；evaluator 或 tool retry 在预算外重调仍可能无限运行。耗尽不是验收通过，优先保全状态并交接。

## 8. 拒绝与审批恢复演练

```yaml
deny_retryable:
  record_reason: true
  next: choose_safe_alternative
  max_retries: project_defined
deny_hard:
  next: blocked
  approver_can_override: false
circuit_open:
  if_request_delivered: awaiting_human
  if_reviewer_unreachable: blocked
  requires: [reviewer, delivery_record, last_action, evidence_ref, resume_pointer]
```

演练三条授权路径：允许执行；需人批准时请求送达并从同一状态恢复；硬拒绝不可被普通批准覆盖。再模拟拒绝后安全替代、无人响应和熔断：未送达记 blocked，送达待决定才记 awaiting_human。父线程须看见子线程最后状态，恢复前复核授权和当前版本。

## 9. 长任务 ledger：不要把三种状态压成 done

```json
{
  "feature_id": "search-42",
  "control": {
    "status": "awaiting_human",
    "stop_reason": "policy_denial",
    "last_action_id": "act-0042",
    "resume_pointer": "run-0042/action-0043"
  },
  "acceptance": {
    "status": "unaccepted",
    "accepted_by": null,
    "evidence_link": null
  },
  "outcome": {
    "status": "outcome_pending",
    "owner": "product-owner-7",
    "next_check": "2026-09-29T09:00:00Z"
  },
  "priority": {"old": 2, "new": 1, "changed_by": "release-lead", "reason": "release dependency"}
}
```

本主题建议的控制行，不是公开统一标准。单任务 progress 和 git history 不能自动回答 priority、授权史、阻塞原因和验收人四列。

## 10. 升档前故障注入清单

```text
[ ] 删除/削弱测试：机器闸门是否失败？
[ ] 修改 evaluator 输入：是否被拒绝并记录？
[ ] 让内层 retry 绕过 budget：是否被外层包络拦住？
[ ] 让 token 换 branch/action/expiry：是否重新授权？
[ ] 让 reviewer 入口不可达：是否进入 blocked 而非假升级？
[ ] 让外部 outcome 不可见：是否保持 outcome_pending？
[ ] 让人工与 evaluator 冲突：是否停止自动升档并保留样本？
```

这份清单验的是控制链能否拒绝已知坏路径，不证明业务质量、收益或组织可规模化。按本次交接选择适用项，每项都有证据、处理理由和责任人，才有依据减少相应值守。非适用项写明理由，纯动作授权不要求全部完成裁判和结果字段。

## 11. 从示意 YAML 泛化成项目控制面

| 语义不变量 | 搜索案例字段 | CI / 数据管道 / 发布系统的可能映射 |
|---|---|---|
| 目标与终态 | `terminal_state` | build artifact ready / DAG partition complete / release candidate healthy |
| 路径与动作约束 | `constraints`, `scope` | 允许目录 / 允许表分区 / 允许环境与变更类型 |
| 环境事实 | `evidence_ref`, `exit_code`, trace | test report / run manifest / deploy health events |
| 判定 | `verdict`, `reasons`, rubric | gate result / data-quality rule / canary policy |
| 继续资格 | `retryable`, budget remaining | retry class / backfill budget / rollback window |
| 停止原因 | `stop_reason` | failed gate / budget exhausted / policy denied / human pause |
| 权威与责任 | `accepted_by`, reviewer | release approver / data owner / on-call |
| 恢复 | `resume_pointer`, checkpoint | rerun key / partition cursor / rollback or resume version |
| 外部结果 | `outcome.owner`, `next_check` | adoption / freshness / incident-free window |

**先分三层，不要把整份 YAML 当通用标准**：控制不变量（跨领域保留：目标可观察、证据可追溯、判定有理由、停止原因独立、验收有权威、升级可恢复）／承载结构（可变：YAML、JSON、数据库行、事件流、CI artifact）／领域策略（不可直接搬运：阈值、重试次数、谁审批、什么算不可修复）。

**迁移规则**：①先写领域终态与不可变约束，不复制 goal.yaml；②控制动作映射为领域事件；③判定绑定 evidence、判据版本、责任来源；④明确缺证据/未知/拒绝/耗尽是否 fail closed；⑤用领域特有坏样本做负例；⑥演练恢复（进程重启、权限过期、上游延迟、人工冲突）；⑦最后才决定承载。

**三个迁移例子**：

```text
CI：build artifact + test report → gate verdict → retry / block / release approval
数据管道：partition manifest + quality report → freshness/completeness verdict → backfill / pause / owner review
发布：canary health + rollback checkpoint → policy verdict → continue rollout / rollback / incident handoff
```

共享控制语义，不共享阈值、判据或恢复动作。`p95 < 300ms`、`3 次拒绝`、`10 轮` 必须由领域风险、成本和历史基线决定；没有基线只能标待定。

## 12. 两个领域的完整迁移例子

### A. 数据管道：从「页面完成」换成「分区可交付」

```yaml
terminal_state: partition=2026-09-28 is complete and queryable
constraints: do_not_overwrite certified partitions; source schema unchanged
feedback: run_manifest + row_count + null_rate + freshness_timestamp
verdict: quality_gate_version=12
continue: retry transient source read or backfill missing partition
stop: certified or budget exhausted
escalate: schema drift / owner decision required
accepted_by: data_owner
resume_pointer: dag_run=...; partition=...
outcome_pending: downstream dashboard freshness not yet observed
```

领域负例不是「按钮坏了」，而是：row count 为零、freshness 超期、schema drift、已认证分区被覆盖——每个负例都要确认同一质量门会失败，且失败原因能回到下一步。

### B. 发布系统：从「产出验收」换成「风险可控地推进」

```yaml
terminal_state: canary meets release policy for the observation window
constraints: deploy only approved artifact; no production schema migration
feedback: health events + error budget + rollback checkpoint
verdict: canary_policy_version=7
continue: expand rollout within authorized slice
stop: policy met, then release_approver signs
escalate: error budget breach / rollback unavailable / conflicting verdict
accepted_by: release_approver
resume_pointer: rollout_id + last healthy checkpoint
outcome_pending: incident-free window not yet complete
```

发布系统的 `stop` 不是「部署命令返回 0」；可能是回滚、暂停或等待观察窗。领域负例：部署成功但错误率超预算、artifact digest 不在批准清单、rollback checkpoint 不可恢复。

## 13. 泛化验收：用变换而不是改名检查

1. **换领域**：同一控制语义映射到数据管道和发布系统，能否说清终态、事实、判定、出口、责任和恢复？
2. **换承载**：YAML 改成数据库事件或 CI artifact，审计信息仍可追溯吗？
3. **换失败类型**：权限过期、外部依赖延迟、判据版本漂移、人工冲突——控制账仍能区分 blocked 与 stopped、验收账能区分 unaccepted 与 accepted、结果账能保留 outcome_pending 吗？

只替换字段名、没定义领域终态/负例/恢复动作的「泛化」是假的。每换一个领域都能保留控制不变量、重写领域策略、并用负例让门失败，才是**语义泛化**。
