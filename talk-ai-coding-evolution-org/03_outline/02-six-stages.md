# 第二幕逐页内容（P13–P38 · 六阶段转型 · v0.5）

> 主轴 = SDLC 六阶段；每阶段开页先点破「引子」（哪一层），再讲机制/治理/度量。play 细则见 `../02_evidence/00-absorption-plan.md`。

### P13 六阶段总览 + loop 图
- **页面结论**：AI-native SDLC = loop；阶段顺序 ≠ 采用顺序；每个阶段落一个工件、触发下一阶段。
- **上屏**：六阶段 loop + 依赖箭头。
- **讲点**：playbook 的「阶段」与「采用顺序」是两回事——从无依赖的 play 起步，逐步关 loop。每个阶段终点是一个工件，触发下一阶段。
- **视觉**：loop 图 + 依赖箭头。

## Plan（P14–P16 · 引子 = Prompt）

### P14 引子：Plan 的本质 = Prompt
- **页面结论**：组织把「意图」一次说清楚，落成可交接的工件——这就是组织级的 Prompt Engineering。
- **上屏**：「Plan 的本质，是把意图说清楚。」
- **讲点**：Prompt 不是「写一句话」，是**组织怎么让 originator 用自己的话表达意图、再由产品 owner 审批**。传统是委员会+工作坊+签字层层转写，AI-native 是意图一次捕获。
- **视觉**：意图→工件 的转化。

### P15 Plan：intent.md
- **页面结论**：originator 自己的话 + AI 头脑风暴 → `intent.md`。
- **上屏**：`intent.md` 五段（problem / outcome / affected / constraints / open questions）。
- **讲点**：产品 owner 不再替人转写需求；originator 与 AI 头脑风暴出 proto-spec。**归产品 owner 审批**，不是工程师。
- **视觉**：intent.md 样例 + 传统 backlog 对比。

### P16 Plan 的治理与度量
- **页面结论**：merge=accept，close=reject；git history 就是证据。
- **上屏**：审批 = merge；度量 = 存活率 + 首次对话→提交时间。
- **讲点**：组织建「intent 的家」（版本受控目录），平台/工程团队立起来并决定谁能写。leading = 对话→committed intent.md（多周→小时）；lagging = 存活率。
- **视觉**：审批门 + 双指标。

## Design（P17–P19 · 引子 = Context）

### P17 引子：Design 的本质 = Context
- **页面结论**：组织策展「模型该看到什么、该知道什么」——这就是组织级的 Context Engineering。
- **上屏**：「Design 的本质，是策展模型所见。」
- **讲点**：Context 不是「塞更多上下文」，是**组织把政策、标准、知识策展成模型可施加的约束**。传统是分析师写 spec、设计师再解读；AI-native 是需求+设计合一、skills 施加政策。
- **视觉**：context 策展示意。

### P18 Design：spec.md + skills
- **页面结论**：需求+设计合一；政策在写 spec 时就施加。
- **上屏**：`intent.md + skills → spec.md`；skills 施加 brand/security/compliance/UX。
- **讲点**：产品 owner 主导一次会话，把组织政策编码成 skills 约束产出。产品 owner 审 spec，**不写** spec。
- **视觉**：intent→spec 转化 + skills 约束环。

### P19 Design 的治理
- **页面结论**：spec+prompt+skill 版本全进库；风险项路由 policy owner。
- **上屏**：版本库记录 + 「flagged concerns」优先解决。
- **讲点**：spec 连同产生它的 prompt 和当时生效的 skill 版本一起入库。产品 owner 签字，矛盾的/高风险项路由给政策 owner，工程团队看到 spec 前这些已解决。
- **视觉**：政策施加点前移示意。

## Build（P20–P25 · 引子 = Harness 主战场）

### P20 引子：Build 的本质 = Harness
- **页面结论**：圈住 / 拦住 / 看清，在 Build 全部落地——这是 harness 的主战场。
- **上屏**：圈住=沙箱/权限；拦住=hooks/门禁；看清=观测/provenance。
- **讲点**：五层里「harness 是可靠性边界」，在组织里就是 Build 这一格。三个动词翻译成组织动作：统一沙箱、统一门禁、统一观测。这是平台团队最该集中建设的地方。
- **视觉**：harness 三层归位。

### P21 Build：plan mode 出 plan.md
- **页面结论**：计划先于代码，且计划可审、可复核。
- **上屏**：`plan.md`（files / order / risks / proof）。
- **讲点**：工程师在 plan mode 让 agent 只读代码库、产出实现计划；接受前不改文件。计划落 `plan.md`，PR review 拿 diff 对计划。**高风险走 tech lead/architect**。
- **视觉**：plan.md 样例 + plan-mode 门。

### P22 Build：AGENTS.md + skills（知识外置）
- **页面结论**：组织知识从「人脑/wiki」变成「文件，agent 每会话开头读」。
- **上屏**：`AGENTS.md` 四段 + `skills/`（版本受控目录）。
- **讲点**：制度知识操作化——AGENTS.md 承载团队约定，skill 把政策变成按需触发的约束。规则：同一个错犯两次，就写进去。政策 owner 审 skill 变更。
- **视觉**：AGENTS.md 样例 + skill 触发。

### P23 Build：hooks（确定性 guardrail）
- **页面结论**：把「习惯性守则」变成「确定性 guardrail」。
- **上屏**：block 保护路径 / 跑 formatter+lint / 挡 credentials。
- **讲点**：hook 是 skill 背后的确定性层。原则：快而窄；重检查放 commit/PR；需人批准的 gate 放 Deploy。**对应圈住/拦住**。
- **视觉**：hook 拦截示意。

### P24 Build：并行会话 + 子 agent
- **页面结论**：一人多会话（worktree 隔离）+ 子 agent，工程师转向编排。
- **上屏**：worktree 隔离 + `subagents/` 定义。
- **讲点**：这是 **Graph 的雏形**（点出，第六幕展开）——编排能力的起点。控制来自 repo 配置（hooks+permissions），日志归属到启动它的工程师。
- **视觉**：并行 worktree + 子 agent 图。

### P25 Build 小结：harness 主战场
- **页面结论**：计划（plan.md）、知识（AGENTS.md/skills）、确定性（hooks）、编排（并行/子 agent）——harness 在 Build 全落地。
- **上屏**：四件套归位。
- **讲点**：Build 是五层里 harness 的主战场，也是组织最容易「各自为政」的地方——所以平台团队在这里集中建设。
- **视觉**：四件套 + 平台集中。

## Test（P26–P29 · 引子 = Harness 的 Sensors + Loop 起点）

### P26 引子：Test 的本质 = Sensors + Loop 起点
- **页面结论**：会话自己验证（harness 的反馈），这是 Loop 的第一个闭环。
- **上屏**：「验证是 done 的一部分。」
- **讲点**：harness 的两套控制——Guides（前馈）+ Sensors（反馈）——Test 就是 Sensors 的主场；而「反馈→改→再验」正是 Loop 的起点。
- **视觉**：Guides/Sensors 两套控制。

### P27 Test：feedback loop
- **页面结论**：会话自己验证，证据来自工具链。
- **上屏**：`make test` 单一目标；量化目标；「fix the code, not the test」。
- **讲点**：组织保证「验证是 done 的一部分」。bug fix 先写失败测试、hook 禁改测试文件。证据=工具链输出，记录进 session transcript + PR check。
- **视觉**：反馈闭环（写→测→改）。

### P28 Test：continuous evals
- **页面结论**：evals 是对 harness 配置的回归测试。
- **上屏**：20–50 真实任务成 eval；配置变更时跑；每个生产事故加 eval。
- **讲点**：组织把「配置」当「代码」对待——AGENTS.md/skills/hooks 一变就回归。pass-rate 阈值作 merge check。
- **视觉**：eval suite + CI 门。

### P29 Test 的治理
- **页面结论**：确定性门禁，QA 的门跟得上 agent 产出。
- **上屏**：leading = 首次 CI 通过率；lagging = review 时间 + change failure rate。
- **讲点**：QA 角色从「逐单验」变成「维护 eval 套件 + 审配置变更」。确定性优先——能交给门禁的不靠模型自觉。
- **视觉**：QA 角色转变。

## Deploy（P30–P34 · 引子 = Harness 的拦住/看清 + authorize at execution）

### P30 引子：Deploy 的本质 = 拦住/看清 + authorize at execution
- **页面结论**：提议权交给模型，执行权留在治理。
- **上屏**：「authorize at execution, not at generation.」
- **讲点**：Deploy 是 harness「拦住/看清」最硬的一段——2026 CVE 的教训：护栏不能建立在「模型会发出合法工具调用」上，要在执行时独立授权。
- **视觉**：提议/执行分离。

### P31 Deploy：PR review（职责分离）
- **页面结论**：所有 PR 同一套 review passes，人看意图与风险。
- **上屏**：`REVIEW.md`（passes / severity / threshold）；PR 历史 = 审计记录。
- **讲点**：职责分离——写码的 agent 不能批自己；人通过 branch protection 批；发现喂回 AGENTS.md。
- **视觉**：PR 多层 review + 人守 gate。

### P32 Deploy：hooks as gates + managed settings
- **页面结论**：把审批从「流程」变成「代码化 gate」；平台用托管配置封死边界。
- **上屏**：PreToolUse hook（allow/ask/block）+ managed settings（permissions/sandbox/credentials/marketplaces/min version）。
- **讲点**：gate 每次对每人都执行、带时间戳日志。managed settings 让工程师不能放宽、不能旁加载、低版本拒绝启动——**每一行都是一项治理决定**。
- **视觉**：gate 放行/拒绝 + 托管配置清单。

### P33 Deploy：CI/CD（提议/执行分离）
- **页面结论**：agent 到生产 gate 为止，不能过 gate。
- **上屏**：只读判断起步 → 写步骤走 PR → MCP 暴露 deploy → 按环境分层自主；rollback 最常排练。
- **讲点**：开发自由、生产要 release manager 授权（hook 强制）、staging 居中。rollback 是排练最多的路径。每次 run 用 agent 自己身份，日志可分离。
- **视觉**：环境分层 + 生产 gate。

### P34 Deploy 小结：生产 gate 由 hook 强制
- **页面结论**：提议权给模型，执行权留平台/治理。
- **上屏**：提议 → 独立门禁 → 放行/拒绝并记录。
- **讲点**：生产 gate 不是流程自觉，是 hook 强制。这对应深轴的「authorize at execution」。
- **视觉**：门禁强制示意。

## Maintain（P35–P38 · 引子 = Loop 收口 + Graph 编排）

### P35 引子：Maintain 的本质 = Loop 收口 + Graph 编排
- **页面结论**：linear→loop 在这里关环；多 agent 在这里编排。
- **上屏**：「The loop keeps running. Human judgement stays above it.」
- **讲点**：五层的后两层（Loop/Graph）在 Maintain 真正登场——反馈连成闭环（Loop），多 agent 编排 + 门禁（Graph）。
- **视觉**：loop 闭合 + 多 agent。

### P36 Maintain：关 loop
- **页面结论**：触发器无人在环调用 agent，诊断写回 intent.md 重新入环。
- **上屏**：确定性检测（mean/std + Western Electric）+ `bands.yaml`（1σ log / 2σ 只读诊断 / 3σ 提议 PR/runbook）。
- **讲点**：检测确定性、无模型；越界才调 agent。写回 intent.md → 走整条链。服务 owner 或 on-call triage，人不再启动、只审批。
- **视觉**：control-band → intent.md → 环。

### P37 Maintain：scans
- **页面结论**：安全扫描从「一次性事件」变成「定时 + findings 走同一 gate」。
- **上屏**：首扫 baseline；每周调度；置信度 rating + 有理由 dismiss；修复后加 eval。
- **讲点**：安全 lead 集中控制（repo/seat/spend）。findings 走 PR gate，大修写 intent.md。确定性检查留 CI，模型驱动扫描补上下文相关漏洞。
- **视觉**：定时扫描 + 走 gate。

### P38 Maintain：on-call（Claude Tag）
- **页面结论**：agent 以自己身份进 channel，立即 first responder；channel 即审计。
- **上屏**：「10pm 的 Slack 事件不再等人。」
- **讲点**：事件触发 → agent 诊断（MCP 验证 metric 回 baseline）→ 写 post-mortem 到 lessons。人在 channel 里可引导/授权。小修走 PR、大修写 intent.md。
- **视觉**：channel 即审计轨迹。
