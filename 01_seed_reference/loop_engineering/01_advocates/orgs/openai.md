# openai — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

**（第三轮挖掘（2026-10-06））**

### 增量 E · OpenAI Codex / dots —— 解决·强（learn.chatgpt.com 官方 `.md` 直取四件；openai.com 博客通道被拦如实记录）

- **E1. 官方文档《Meet dots》＋《Tasks and memory》（learn.chatgpt.com，living docs，实取 2026-10-06）**
  - 通道：https://learn.chatgpt.com/llms.txt 实取（官方自述 "Each page has a Markdown twin at `/docs/<slug>.md` for direct ingestion"）→ `.md` 直取（16KB/8KB）。openai.com/index/dots/ 直取被 JS 盾拦截（9.9KB 空壳，通道状态如实记录）；dots 发布日未在官方一手载体核到日期，官方状态为 "rolling out gradually"。
  - 逐字摘录：

> "Your dot is an always-on agent that keeps work moving across your tools and projects. You can keep talking to it while it works, and it reaches out with results or decisions that need you."

> "Powered by GPT-6 Astra, your dot lives in the cloud and has its own computer and browser. … It can research, analyze data, prepare documents, and build software, using relevant context from past conversations and your preferences."

> "Your dot keeps working between conversations and follows through as things change. It can decide when to pause and wake up to continue, so you don't need to put every follow-up on a fixed schedule."

> "Your dot can divide work among background agents that run in parallel and report back to it."

  - **该条支持的最小主张**：OpenAI 在窗口内把"常驻自主 agent"做成产品面（云端常驻＋自主决定何时暂停/唤醒＋并行后台 agent 分工）——库内已有 Codex 线索之外的最大新产品面。
  - 派别适配：**推动·厂商**（自主性即产品）。停止语义的官方自限见怀疑面增量 B。

- **E2. 官方文档《Codex Cloud》《Agent approvals & security》《ChatGPT usage limits and spend controls》（同通道 `.md` 实取）**
  - 逐字摘录：

> "Each task has its own workspace and can keep working while your computer is asleep."（cloud.md）

> "By default, the agent runs with network access turned off. Locally, Codex uses an OS-enforced sandbox that limits what it can touch (typically to the current workspace), plus an approval policy that controls when it must stop and ask you before acting."（agent-approvals-security.md）

> "Administrators need user guardrails, workspace-level spend controls, or usage notifications supported by the current plan."＋"GPT-6 Astra Ultrafast is off by default in eligible Enterprise workspaces. … the higher usage rates can consume a user's budget faster."（enterprise/usage-limits.md）

  - **该条支持的最小主张**：Codex 线的把控机制三件套——沙箱/审批门（must stop and ask）、企业级 spend controls、高风险模式默认关闭——全部官方文档化（target 9 OpenAI 行）。
  - 派别适配：**推动·厂商**＋机制登记；`untrusted` approval policy 回撤进怀疑面增量 A。

- **E3. 官方《Codex Security plugin changelog》（带日期的一手 changelog）**
  - URL：https://learn.chatgpt.com/docs/security/plugin/changelog.md （`.md` 实取 22.9KB）
  - 逐字摘录（0.1.25，**September 23, 2026**）：

> "See standard scan progress advance through threat modeling, discovery, validation, attack-path analysis, and reporting as each phase begins."

  - **该条支持的最小主张**：Codex 安全审查环（威胁建模→发现→验证→攻击路径→报告）在窗口内有带日期的官方增量（0.1.24 Sep 9 / 0.1.25 Sep 23 / 0.1.30 Sep 24），即"审查环"产品化的官方一手。
  - 派别适配：**推动·厂商**（安全审查做成多阶段环产品）。

**（第五轮挖掘（2026-10-06）：厂商机制文档深挖）**

### B · OpenAI Codex / ChatGPT Work / dots：approval 全集、auto-review 熔断器、network_proxy 默认表（learn.chatgpt.com `.md` 直取）

- **approval 现行形态**（agent-approvals-security.md 实取）：**`approval_policy = "untrusted"` 已退役**，逐字——"*Codex and ChatGPT Work no longer support `approval_policy = \"untrusted\"`. The retired setting can prevent either client from starting.*" 迁移路径两条：`sandbox_mode = "read-only" + approval_policy = "on-request"`，或保留命令级审批用 `[projects."path"] trust_level = "untrusted"`（项目级 trust，不是 policy 值）。现行全集：`read-only`/`workspace-write`/`danger-full-access` × `on-request`/`never`/**granular**（`granular` 五子开关逐字：`sandbox_approval`, `rules`, `mcp_elicitations`, `request_permissions`, `skill_approval`）；`--dangerously-bypass-approvals-and-sandbox`（别名 **`--yolo`**）；`codex exec --full-auto` 已 deprecated。
  - 挂钩：**审批与权限**＋**沙箱与环境**（双轴模型逐字："*Sandbox mode: What Codex can do technically… Approval policy: When Codex must ask you before it executes an action*"）。
- **auto-review（审批代理化）＋熔断器**（sandboxing/auto-review.md 实取，本轮最大发现）：`approvals_reviewer = "user"`（默认）→ `"auto_review"`——沙箱边界审批交独立 reviewer agent，"*Auto-review is a reviewer swap, not a permission grant. It does not expand `writable_roots`, enable network access, or weaken protected paths.*" **熔断器逐字**："*Codex also applies a **rejection circuit breaker** per turn. In the current open-source implementation, Auto-review interrupts the turn after `3` consecutive denials or `10` denials within a rolling window of the last `50` reviews in the same turn. Any non-denial resets the consecutive-denial counter. When the breaker trips, Codex emits a warning and aborts the current turn with an interrupt rather than letting the agent loop on more escalation attempts.*" 否决语义：逐字注入指令不得绕行（"*Do not pursue the same outcome via workaround, indirect execution, or policy circumvention*"）；人工覆盖 `/approve`——最多记 10 条近期 denial，单次重试仍走 auto-review；reviewer 看紧凑 transcript＋审批请求，**不含隐藏推理**；策略本体在开源仓 `codex-rs/core/src/guardian/policy.md`＋`policy_template.md`，企业覆盖 `guardian_policy_config`、个人 `[auto_review].policy`（**替换不合并**，managed 优先）。前置条件：仅在交互式审批下生效，`approval_policy = "never"`／`--yolo` 时无审批可审。
  - 挂钩：**停止条件**（逐字 "rejection circuit breaker"——**第四轮负发现"无厂商官方文档使用 circuit breaker 术语"被本轮推翻**，主链见怀疑面）＋**验证回路**（审批＝逐动作验证器）。
- **command rules**（agent-configuration/rules.md 实取）：`.rules` 文件＝Starlark `prefix_rule()`，字段 `pattern`（必填，元素可为字面量或并集 `["view","list"]`）、`decision`（**默认 `"allow"`**；三值 allow/prompt/forbidden，**多规则命中取最严**逐字："`forbidden` > `prompt` > `allow`"）、`justification`、`match`/`not_match`（加载时校验的"inline unit tests"）；shell 包装特判：`bash -lc` 线性链用 tree-sitter 拆开逐条评估（例逐字：`["bash","-lc","git add . && rm -rf /"]` → 拆为两条），含变量/重定向/通配则整条不拆；测试命令 `codex execpolicy check`。
  - 挂钩：**审批与权限**（白名单的精确前缀语义＋反夹带拆分）。
- **network_proxy 默认表**（agent-approvals-security.md 实取）：`enabled=false`、`domains` unset（allowlist-first，`deny` 永远赢）、`allow_local_binding=false`（loopback/RFC1918/链路本地默认封）、`enable_socks5=true`、`enable_socks5_udp=true`、`allow_upstream_proxy=true`、`dangerously_allow_non_loopback_proxy=false`、`dangerously_allow_all_unix_sockets=false`；DNS rebinding 尽力检查（解析到非公网即封）；组合行为逐字："*Network off + network_proxy on: network stays off, and the feature does nothing.*" web_search 默认 **`"cached"`**（OpenAI 索引缓存，非实时）——"*This reduces exposure to prompt injection from arbitrary live content.*"
  - 挂钩：**沙箱与环境**（默认关网络＋代理白名单的参数级基线）。
- **dots**（learn.chatgpt.com/docs/dots*.md 实取）：常驻 agent 的官方机制页。动作审批逐字——"*Before your dot takes an action that could affect your accounts or share information, an automatic review checks it against your instructions, permissions, custom rules, and built-in safety requirements. The review determines whether the action can proceed, needs your approval, or includes a step you must do yourself.*"（例：改密码必须用户自己做）。自定义规则四选项表：**Take action without asking / Take action when you say so / Ask before taking action / Hand off to you**；且逐字声明规则是软约束："*They are instructions your dot tries to follow, and it can make mistakes. They don't grant access to an app or computer, override built-in safety requirements, or remove required confirmations such as approval to use a saved login.*" **停止语义分级**（controls.md "Stop work" 节逐字）："*Pause stops your dot's current main task. It doesn't stop every delegated task or cancel future scheduled runs.*"——Pause/停单任务/删计划三者互不联动；自调度逐字："*It can decide when to pause and wake up to continue, so you don't need to put every follow-up on a fixed schedule.*"（tasks-and-memory.md）
  - 挂钩：**无人值守运行**（自主 pause/wake 的产品化）＋**审批与权限**（四档规则＋研究/行动读写分离："research…can't send messages, change app content, or control your browser or computer"）。
- **spend controls**（enterprise/usage-limits.md 实取）：workspace credits 池制；逐字边界——"*Usage controls don't configure feature entitlement or permissions, although exhausted limits can pause access to eligible features.*"；**Ultrafast mode（GPT-6 Astra Ultrafast）企业默认 off**，owner 手动开，"*Existing per-user spend limits apply to eligible Ultrafast usage. Review those limits before enabling access because the higher usage rates can consume a user's budget faster.*" 管理细节外链 help.openai.com（20001001/20001155）。
  - 挂钩：**预算与熔断**（耗尽→pause 为厂商侧"预算即停止条件"的官方表述）。
