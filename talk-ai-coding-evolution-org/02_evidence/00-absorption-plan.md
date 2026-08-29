# 内容吸纳清单：六阶段 + 15 play 进货单（v0.2）

> 源：`../_reference/rawdata_anthropic-ai-native-sdlc-playbook.md`（Anthropic "The AI-Native SDLC playbook"，Louis Claxton，2026-08-21）。
> 本表是铺页面的骨架：**每一阶段 → 每个 play → 传统→AI-native 转变 → 工件/机制 → 治理 → 度量 → 五层/harness 落点**。
> 五层映射用 `-opc` 的口径：Prompt/Context = 任务层，Harness = 平台层（圈住/拦住/看清），Loop/Graph = 治理层。

## 零、贯穿全文的主线（不进任何单页，处处引用）

- **代码不再是瓶颈**：build 被压扁，慢的是 plan / review / test / deploy（人的速度）。
- **AI-native SDLC = loop**：线性 → 循环；AI 嵌在每个点；自动交接 / 触发。
- **工件链 = 审计链**：`intent.md → spec.md → plan.md → diff+tests → PR+review → incident`；每一阶段落一个工件，下一阶段读它；commit 链记录「谁要的 / agent 产出了什么 / 谁批的」。
- **人守 gate，不逐行**：human judgment at gates；确定性优先；authorize at execution, not at generation。

## 一、六阶段 shifts 总表（第一幕/第二幕总览用）

| 阶段 | Traditional SDLC | AI-native SDLC |
|---|---|---|
| Plan | 委员会收集需求、工作坊、签字，手写 | Claude 从源头合成痛点，写进 `intent.md`（人可读、机器可执行） |
| Design | 分析师写 spec，设计师再解读 | 需求+设计压缩成一次会话，standards 编码为 skills、git 版本化 |
| Build | 测试/代码手写，文档事后补 | AI 生成测试+代码，制度知识 = 版本化 `AGENTS.md` + skills |
| Test | QA 在阶段边界设闸 | 连续 evals 贯穿实现 |
| Deploy | 人逐行 review，治理靠 review 周期（常不一致） | 分层 agentic review，人只审受监管/关键代码；治理在 AI 行动时以 hooks 作为审批 gate 强制执行 |
| Maintain | 人盯生产抓 bug | agent 监控线上，越界即诊断并写成新 `intent.md` 写回 loop |

## 二、15 个 play 进货单

### Plan（1 play）

| Play | 传统→AI-native 转变 | 工件 / 机制 | 治理 | 度量（leading / lagging） | 五层落点 |
|---|---|---|---|---|---|
| Capture as `intent.md` | backlog/用户故事/故事点/细化会 → originator 用自己的话 + Claude 头脑风暴出 proto-spec | `intent.md`（author、problem、outcome、affected、constraints、open questions） | 产品 owner 审批（merge=accept，close=reject）；git history 是证据 | L：首次对话→committed `intent.md`（多周→小时）；G：`intent.md` 被接受进 Design 的存活率 | Prompt/Context 组织化（任务层起点） |

### Design（1 play）

| Play | 转变 | 工件 / 机制 | 治理 | 度量 | 五层落点 |
|---|---|---|---|---|---|
| Requirements and design | 需求+设计分离两个团队 → 单次会话合一，skills 施加政策 | `spec.md`（与 `intent.md` 成对）；front-end 可用 Claude Design 出 mock | skills 作为约束施加；spec+prompt+skill 版本都进版本库；产品 owner 签字，风险项路由给 policy owner | L：`intent.md`→`spec.md` 时间；G：build 开始后的 spec 返工次数 | Context + 治理前移 |

### Build（5 play，最重）

| Play | 转变 | 工件 / 机制 | 治理 | 度量 | 五层落点 |
|---|---|---|---|---|---|
| Claude Code plan mode | 读完设计直接写码（计划在脑里）→ plan mode 先出可审计划 | `plan.md`（files / order / risks / proof） | 设计 review 在写码前；plan mode 强制（不接受计划不改文件）；高风险走 tech lead | L：一次实现就 merge 的比例 + 批准→merge 时间；G：rework cycles + diff 与 `plan.md` 匹配度 | Harness（提议/计划） |
| The `AGENTS.md` | 知识在人脑/wiki → 文件 agent 每会话开头读 | `AGENTS.md`（commands / conventions / architecture / things the agent gets wrong） | 版本受控、可审、可审计；code owner 批准变更 | L：agent 重复犯错次数；G：新人首次 merge PR 时间 | Context/知识外置（Knowledge Map 雏形） |
| Skills as institutional knowledge | 政策执行不一致 → skill 把制度知识操作化 | `.claude/skills/<name>/SKILL.md`（frontmatter 触发条件 + 正文） | skill 是 advisory control；必须始终成立的政策需 hook 兜底；policy owner 审 skill 变更 | L：政策批准→skill merge 时间；G：PR review 引用该政策的 findings（应趋零） | Guides（前馈） |
| Hooks as build-time guardrails | 习惯性守则 → 代码化 guardrail | block 保护路径 / 跑 formatter+lint / 挡住 credentials | hook 是确定性层；快而窄（只对改动文件）；重检查放 commit/PR；需人批准的 gate 放 Deploy | — | 圈住/拦住（确定性优先） |
| Parallel sessions and subagents | 一人一任务 → 一人多会话（worktree）+ 子 agent | worktree 隔离；subagent 定义在 `.claude/agents/` | 控制来自 repo 配置（hooks+permissions）；日志归属到启动它的工程师 | L：每人并发会话数（review 质量 hold）+ steering vs waiting 占比；G：每人每周 merge 数 + rework rate | Loop/Graph 雏形（编排/并行） |

### Test（2 play）

| Play | 转变 | 工件 / 机制 | 治理 | 度量 | 五层落点 |
|---|---|---|---|---|---|
| Give Claude a feedback loop | 信号晚到（CI/测试/生产）→ 会话自己验证 | `make test` 单一目标；量化目标；bug fix 先写失败测试；UI 视觉闭环；hook 禁改测试文件 | 验证是 done 的一部分；证据来自工具链输出；记录在 session transcript + PR check | L：agent 改动首次 CI 通过率；G：每 PR review 时间 + change failure rate | Sensors（反馈）+ 确定性门禁 |
| Continuous evals in CI | 阶段闸门 QA → 对配置变更的回归测试 | 20–50 真实任务成 eval；`AGENTS.md`/skills/hooks 变更时跑；每个生产事故加 eval | pass-rate 阈值作 merge check；配置变更团队审批 | L：eval pass rate 趋势 + 事故→eval 时间；G：CI 抓到 vs 生产发现 | 对 harness 配置的确定性回归（治理） |

### Deploy（3 play + 1 实例）

| Play | 转变 | 工件 / 机制 | 治理 | 度量 | 五层落点 |
|---|---|---|---|---|---|
| AI in the PR review loop | 人 review 所有 → 同一套 review passes + 人看意图与风险 | `REVIEW.md`（passes / severity / threshold）；PR 历史 = 审计记录 | 职责分离（写码的 agent 不能批）；人通过 branch protection 批；发现喂回 `AGENTS.md` | L：first review 时间 + 无需人碰分支解决的评论占比；G：merge 前 vs 逃逸生产 | 拦住/看清 + 职责分离 |
| Hooks as approval gates | 审批靠流程 → 代码化 gate | PreToolUse hook 允许/询问/阻止；team hooks in `settings.json` + non-negotiable in managed settings | gate 每次对每人都执行；allow/block 带时间戳日志；定义什么算审批 | L：每个审批 gate 等待时间；G：hooks 前后逃逸生产的违规 | 拦住（authorize at execution） |
| CI/CD integration and deployment | pipeline 只跑确定性脚本 → Claude 非交互跑判断步骤，沙箱+scoped credentials | 只读判断起步 → 写步骤走 PR → MCP 暴露 deploy → 按环境分层自主；rollback 最常排练 | agent 到生产 gate 为止，不能过 gate；每次 run 用 agent 自己身份 | L：无需 pager 解决的 pipeline 失败占比；G：DORA | 提议/执行分离（生产 gate） |

> **Deploy 附·worked example（受监管企业 managed settings）**：`permissions.deny/allow`（守秘密、预批准安全内循环）、`disableBypassPermissionsMode`+`allowManagedPermissionRulesOnly`（个人不可放宽）、`sandbox`（OS 级文件/网络隔离，failIfUnavailable）、`credentials`（封死 ssh/aws 凭据读取）、`allowManagedHooksOnly`（只有平台 hooks 生效）、`strictKnownMarketplaces`+`disableSideloadFlags`（一切 skill/agent/hook/MCP 都经组织核准市场）、`requiredMinimumVersion`（低于评估过的版本拒绝启动）。→ 这是「统一平台 + 治理边界」最硬的一段证据。

### Maintain（3 play）

| Play | 转变 | 工件 / 机制 | 治理 | 度量 | 五层落点 |
|---|---|---|---|---|---|
| Maintenance and closing the loop | 被动运维（等人）→ 触发器无人在环调用 Claude → 诊断写回 `intent.md` | 确定性检测脚本（mean/std + Western Electric）；`bands.yaml` 分层（1σ log / 2σ 只读诊断 / 3σ 提议 PR/runbook）；写 `intent.md` 重新入环 | 分层边界版本受控；生产权限 deny；人 triage+批；触发 runbook 预先批准 | L：breach→`intent.md` 时间；G：变 merge fix 的 findings 占比 + 同类重复事故 | Loop/Graph 组织化（组织责任实例） |
| Recurring codebase scans | 一次性安全事件 → 定时扫描，findings 走同一 gate | 首扫为 baseline；每周调度；置信度 rating + 有理由 dismiss；小修走 PR、大修写 `intent.md`；修复后加 eval | admin 集中控制（repo/seat/spend）；finding 有验证+置信度；dismissal 有理由；修复走 PR gate | L：接入 repo 比例 + finding→PR gate 时间；G：定时扫描 vs 生产/外部发现的漏洞 + 每扫 finding 趋势 | 看清（观测）+ 治理 |
| Claude on call (Claude Tag) | 10pm Slack 事件等人 → Claude 以自己身份进 channel 立即 first responder | channel 是审计记录；MCP 验证 metric 回 baseline；写 post-mortem 到 lessons 文件 | 人在 channel 里可引导/授权；小修走 PR、大修写 `intent.md` | — | Loop 闭环 + 审计 |

## 三、口径红线（本 talk 增补版）

- 「代码不再是瓶颈」是 **Anthropic 的论点**，引用标注来源，不讲成普适事实。
- playbook 是 **Claude / Anthropic 视角**的操作手册；讲「机制」讲透，别把产品名（Claude Code / Claude Security / Claude Tag）讲成唯一答案。
- `-opc` 红线仍适用：前三层成熟、Loop/Graph 新兴；DSH 不是 MCP（`ctx.llm`/`ctx.tools`/capability seam/plugin）；star/生态数据是 2026-08-27 快照；CVE 只讲因果链。
- 工件名（`intent.md`/`spec.md`/`plan.md`/`REVIEW.md`/`AGENTS.md`）是 playbook 的约定，讲时说明「这只是命名约定，换成你们组织的工件系统同理」。
- **命名随大流、工具不可知**：playbook 原文的 `CLAUDE.md`（及 `.claude/skills`、`.claude/agents`、`.claude/settings.json` 等路径）是 Claude Code 专属命名；本 talk 统一用主流/工具不可知的名字——`CLAUDE.md` → **`AGENTS.md`**，`.claude/skills` → **skills（版本受控目录）**，`.claude/agents` → **subagents**，其余同理。机制讲透，不绑定任何单一产品。

## 四、DSH 帮助流程：三条腿 + 机制 → org 映射（第三幕素材）

> 源：`rawdata_dsh-faq-on-digested/07_borrowing-harness-idea/`、`rawdata_dsh-digested/harness-idea/`、`session-and-loop/`、`capability-seams/`、`rawdata_dsh-plugin-business-ladder/`、`rawdata_dsh-plugin-seam-maturity/`。

**一句话**：DSH 不训练「更聪明的 agent」，而是把「怎么正确参与」外置成运行时语法——让「读对、改对」成为阻力最小路径，「读错、改错」在离错误源头最近处被机器拒绝。三条腿：

| 腿 | DSH 机制 | 金句 | org 落点 |
|---|---|---|---|
| **知识外置** | 一个事实一个 owner；当前状态与决策理由分开；负知识（为什么不做 X）也外置 | 「不糊涂靠外置，不靠聪明」 | 工件链（intent/spec/AGENTS.md + ADR + rejected notes） |
| **正确路径** | 扩展点路由四问（事实/拦截/能力/loop）；参与阶梯 patch→扩展点→seam→loop；归属路由 | 「不乱发挥靠正确路径」 | 治理的准入/替换（谁能改什么、改哪里先问归属） |
| **可执行反馈** | 类型/load/测试/snapshot/invariant/CI 门禁；**门禁本身被测试**（证明无效案例会被拒绝） | 「Agents follow enforced gates far more reliably than prose conventions」 | 确定性优先 / 人守 gate |

**运行时基底** = 插件图（系统现在由什么组成）+ 事件流（系统刚才做过什么，append-only，「模型可见 ⟺ 已记录」）+ loop（两者之间取能力、写事实）。

**定制/替换** = capability seam 三角色（Service Definition / Provider / Consumer）——「换一个后端，整面产品跟着变，Consumer 不用改」→ 支撑「给不同环节定制」。

**审计/重建事实** = append-only session log + 审批成对 `asked/decided` + fail-closed（无人可答就失败关闭）+ 会话格式版本纪律。

**诚实标尺** = 可替换率 **39.3%**（28 条 seam 中 11 条 P≥2）；饱和区（执行世界 / 会话底座 / LLM 注册面 / 四入口复用 spine）vs 缺口区（渠道通知 / 长期记忆 / 审批人类形状与多方编排 / workflow 持久化 / authorization）。→ 这本身就是「成熟度诚实」的样本：敢把数字摊开。

## 五、待补

- 信息脉络图（上游 → 加工 → 页面 + 反向索引）→ `01-info-flow-map.md`。
- 组织特有反面案例 / 供应链事故（补 managed settings worked example 之外的证据）。
