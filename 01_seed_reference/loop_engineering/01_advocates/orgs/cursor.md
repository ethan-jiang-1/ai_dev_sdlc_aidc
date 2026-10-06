# cursor — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

## Source 5 · Cursor 官方 ·《Cloud Agents and Cursor Harness Improvements》changelog（2026-08-19）

- URL：https://cursor.com/en-US/changelog/08-19-26 （全文取得）｜ 作者身份：Anysphere（Cursor）官方
- 来源类型：厂商官方 changelog（一手，全文）
- 号召力口径：①＋③——头部 AI IDE 厂商官方；库内已登记其 2026-05-20 /loop skill（02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-26-b-stop-and-scheduling.md 与 evidence-2026-09-30-u-post-june-kols.md S4b 已档），本条是**六月后进一步推动的核销**

**逐字摘录**：

> "We're continuing to improve cloud agents and the Cursor harness so always-on agents can operate as a system, building and shipping software on their own without the need for intervention at each loop."
>（官方愿景句直译：常开 agent 作为系统运行、自主构建与交付软件、**每个循环无需人介入**——无人值守当卖点，白纸黑字。）

> "Use /goal to give the agent a long-lived objective to work towards until it's fully complete. Try `/goal fix all flaky tests and make CI green`… Pair it with a custom mode to follow a playbook, or /loop for recurring check-ins."
>（**/goal 正式发布**且官方教程句明确教 /goal＋/loop 组合——与 Claude Code 的 /goal + /loop 原语在竞品侧完全同构。多源词表收敛的厂商级证据。）

> "Cursor Agent subscribes to an event source (a thread or conversation) and wakes when something happens… Cloud agents automatically subscribe to PRs they create and drive them to completion, fixing CI and addressing bot comments."
>（Subscriptions：事件驱动唤醒＋PR 自动跟进到完成——事件环的产品化。）

> "Subagents can now run on their own virtual machines. Each gets an isolated copy of the project with clean context in its own cloud environment… run a swarm of subagents to test my app for bugs, each in its own environment."
>（子代理 VM 隔离＋官方示例句直接教 swarm——并行循环的官方教学。）

- 相关线（未取得正文）：AI Weekly 报道 "Cursor gives cloud agents subscriptions, /goal and subagent VMs"（二手）；2026-03-06 Automations 发布（dataconomy 报道，二手）。Cursor 官方侧六月后路线：03 Automations → 05 /loop → 08 /goal＋subscriptions＋swarm——**季度级连续推动**。

**该条支持的最小主张**：Cursor 在 2026-06 后继续官方推动循环/无人值守（/goal、事件订阅、子代理 swarm），且官方愿景句把"每循环无人介入"写为产品目标。
**派别适配**：**推动票**（厂商产品化）。

---

**（第五轮挖掘（2026-10-06）：厂商机制文档深挖）**

### C · Cursor：Run Modes/auto-review 分类器、sandbox.json 与 permissions.json 合并规则、/goal 与 /loop 无 docs 页

- **Run Modes**（docs/agent/security/run-modes.md 实取）：三档逐字表——**Auto-review**（"Allowlisted calls run immediately. Other shell commands run in the sandbox when possible. Calls that do not use the sandbox go to the Auto-review classifier."）、**Allowlist**（确定性、无分类器）、**Run Everything**（零提示零沙箱）。分类器流程：沙箱失败的命令 agent 可在沙箱外重跑，**重跑必过分类器**；分类器在 Cursor 后端跑，可对本机做只读 `ReadFile/Grep/Glob/ListDir`；**模型参数**：当前 **Gemini 3.5 Flash Lite**，fallback **Claude 4.5 Haiku**——企业若禁 Haiku，"*Blocking Claude 4.5 Haiku can disable Auto-review there, even when team Run Modes includes it.*" 规则文件 `permissions.json`（`~/.cursor` 与 `<project>/.cursor` **合并**，逐字："*Cursor **concatenates** the arrays inside every field*"），指令为自然语言句子的 `autoRun.allow_instructions` / `block_instructions`；**团队 dashboard 配置存在时忽略两级本地文件**。
  - 挂钩：**审批与权限**（LLM 分类器做审批闸的参数级）＋**验证回路**（分类器可拒绝→agent 换路径或转人工）。
- **sandbox.json**（reference/sandbox.md 实取）：`type` 默认 `"workspace_readwrite"`；`networkPolicy.default` 默认 **`"deny"`**；**deny 永远赢**；合并优先级逐字："`per-user < per-repo < team-admin < hardcoded`"（路径并集、网络 allow 并集但 team-admin 存在时替换、restrictive 布尔 true 赢）；SSRF 默认封 RFC1918/`127.x`/metadata `169.254.169.254`/IPv6 私有；**硬编码保护路径**（`.cursor/*.json`、`.claude/**/*.json`、`.git/hooks/**`、`.git/config`、`.cursorignore` 等）任何配置不可写。平台实现：macOS Seatbelt（`sandbox-exec`）、Linux Landlock+seccomp（内核 ≥6.2，否则退回弹窗审批）、注入 `CURSOR_SANDBOX`/`CURSOR_ORIG_UID`/`CURSOR_SANDBOX_LANDLOCK_STATUS`（`fully_enforced`|`bubblewrap`）。
  - 挂钩：**沙箱与环境**（默认 deny＋四层合并链＋不可削弱层）。
- **/goal 与 /loop 的文档缺口**：cursor.com/docs sitemap（352 URL 实取全列）**无任何 `/loop` 或 `/goal` 专页**；`/goal` 仅见于 changelog（实取，2026-09 系"Cloud Agents and Cursor Harness Improvements"期）：逐字——"*Use /goal to give the agent a long-lived objective to work towards until it's fully complete. Try /goal fix all flaky tests and make CI green in a new chat. Pair it with a custom mode to follow a playbook, or /loop for recurring check-ins.*" 同期叙事逐字："*With this release, cloud agents can automatically pick up work in response to events, hold a goal until it's met, and stay on course through long-running sessions.*" **docs↔实现不一致**：机制在产品里、参数在 changelog 里、docs 无页——与 Claude Code 的 goal.md/scheduled-tasks.md 全参数页成鲜明对照（怀疑面双记）。
  - 挂钩：**停止条件**（"hold a goal until it's met"＝与 Claude Code 同构的模型判停）＋**循环结构**。
- **Automations**（docs/cloud-agent/automations.md 实取）：触发器（cron/GitHub/GitLab/Slack/webhook/Linear）→cloud agent；逐字："*Automations use each model's maximum supported context window because they run as cloud agents. There is no context-window toggle.*"；**computer use 默认全开**："*Computer use lets cloud agents kicked off by automations use a computer just like a developer would… It is included by default for every automation.*"；**Run as → Service account**（管理员可切专用身份）；计费按 cloud agent 用量。
  - 挂钩：**无人值守运行**＋**循环产品化机制**（事件/定时触发器市场化的 agent 常驻）。
