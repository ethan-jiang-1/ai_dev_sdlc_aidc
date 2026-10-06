# github — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

## Source 12 · GitHub Copilot 官方 · Copilot CLI "Autonomous task completion / fleet"（存在性已核，正文未取得）

- URL：https://docs.github.com/en/copilot/concepts/agents/copilot-cli/autopilot （官方 docs，两次 fetch 均在导航层截断）｜ 作者身份：GitHub 官方
- 来源类型：厂商官方文档（**存在性与标题已核，正文未取得**）
- 号召力口径：②（官方文档体系）——docs 导航可见 Copilot CLI 下设 "Autonomous task completion"（autopilot）与 "Parallel task execution"（fleet）概念页，另有 Cloud agent、Agentic Workflows 等整章
- **负结论为主**：正文两试均截断，无法引句；GitHub 官方是否使用 "loop engineering" 词表未核。仅可记：GitHub 在 2026 年给 Copilot CLI 配置了无人值守（autopilot）与并行代理（fleet）的官方概念文档——与 Cursor 08-19 同向的厂商推动信号，**深度内容待补**。
**派别适配**：**证据不足以定派**（存在性信号正向，内容未核）。

---

**（第三轮挖掘（2026-10-06））**

### 增量 D · GitHub Copilot —— 解决·中（窗口内 changelog 两条＋预算/自动化官方文档；命名漂移如实记录）

- **D1. Changelog 2026-07-29《Copilot code review: Agent skills and MCP now generally available》**
  - URL/日期：https://github.blog/changelog/2026-07-29-copilot-code-review-agent-skills-and-mcp-now-generally-available/ ；datePublished **2026-07-29T14:26:19-07:00**（页面 JSON-LD 实取）。
  - 逐字摘录：

> "Copilot code review support for agent skills and MCP servers is now generally available for all Copilot Pro, Pro+, Business, and Enterprise users."

> "All MCP tool calls performed by Copilot code review will be limited to read-only."

  - **该条支持的最小主张**：agent 审查环接入团队工具/上下文成 GA；同时官方把该环的 MCP 调用硬限为只读（把控面的官方一手，target 9）。
  - 派别适配：**推动·厂商**＋机制登记。

- **D2. Changelog 2026-07-31《Enterprise teams model policy targeting in public preview》**
  - URL/日期：https://github.blog/changelog/2026-07-31-enterprise-teams-model-policy-targeting-in-public-preview/ ；datePublished **2026-07-31T11:11:50-07:00**（实取）。
  - 逐字摘录：

> "This feature empowers AI administrators to set a baseline of models for the entire enterprise and then grant additional models to specific enterprise teams."

> "This public preview is the first step in a broader shift toward team-level governance."

  - **该条支持的最小主张**：模型访问的治理粒度从 org 层下探到 team/user 层——厂商把"给 agent 什么能力"本身做成逐级治理产品。
  - 派别适配：**推动·厂商**（治理即卖点）。

- **D3. 官方文档：预算与自动化（living docs，实取 2026-10-06）**
  - URL：https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/assigning-licenses/managing-your-companys-spending-on-github-copilot
  - 逐字摘录：

> "GitHub offers billing tools to help you visualize your spending patterns, control AI credits consumption with budget controls, receive alerts when you reach budget thresholds, and optimize your license usage."

> "You can set budgets at the user, cost center, and enterprise level to control how AI credits are consumed."

  - URL：https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent （实取重定向至 "Copilot on GitHub.com" 总览页，如实记录）
  - 逐字摘录：

> "Agentic experiences can research a repository, plan changes, and complete multi-step tasks by reading files, editing code, and running tests in a cloud development environment."

> "Automations run repository tasks on a schedule or in response to events, rather than requiring a new prompt each time."

> "Copilot cloud agent can research a repository, plan changes, and implement them in the background."

  - 上轮缺口处理：上轮 Copilot 正文截断——本轮以 docs.github.com 直取（617KB/610KB HTML 实取）补上；上轮要求的 api/raw 载体补抓为 changelog JSON-LD 日期字段实取（D1/D2 的 datePublished 即 API 级元数据）。
  - 通道注记：docs 现行用词是 **"Copilot cloud agent"**，而 blog/changelog 仍用 "coding agent"（2026-07-29 条目原题即 coding agent）——命名漂移如实记录，条目按官方两种用词并存登记。
  - **该条支持的最小主张**：Copilot 的自主任务面（后台多步任务＋定时自动化）与预算上限（user/cost center/enterprise 三层 budget）均为官方文档化机制。
  - 派别适配：**推动·厂商**＋机制登记（target 9 Copilot 行）。

**（第五轮挖掘（2026-10-06）：厂商机制文档深挖）**

### E · GitHub Copilot coding agent / cloud agent：预算三层、MCP 只读默认、审批流（docs.github.com 实取）

- **预算三层＋默认不熔断**（how-tos/manage-and-track-spending/manage-company-spending.html 实取）：逐字——"*Each Copilot license includes AI credits that are pooled across your enterprise. When the pool is exhausted, additional usage is charged at **$0.01 USD per AI credit**, subject to your budget controls.*" 三层：**User-level budgets**（单用户每周期 AI credits 上限，含共享池与超额）、**Cost center budgets**、**Enterprise spending limits**（封超额计费）。**关键默认逐字**："*Enable \"Stop usage when budget limit is reached\" on every spending limit you create. Without it, reaching a limit sends a notification but does not block usage and charges continue to accrue.*"（怀疑面双记：熔断默认 off）。
  - 挂钩：**预算与熔断**（三层预算的参数与默认行为）。
- **MCP 只读默认＋免审批**（concepts/agents/cloud-agent/mcp-and-cloud-agent.html 实取）：默认内置两 server——GitHub MCP（"*connects to GitHub using a specially scoped token that only has **read-only** access to the current repository*"）与 Playwright MCP（"*By default, the Playwright MCP server is only able to access web resources hosted within Copilot's own environment, accessible on `localhost` or `127.0.0.1`*"）；**逐字免审批**："*Copilot will use available tools autonomously, and will not ask for approval before use.*"；**写权限默认关**："*By default, Copilot cloud agent does not have access to write MCP server tools.*"；仅支持 tools 不支持 resources/prompts；**OAuth 远程 MCP 不支持**（"*do not currently support remote MCP servers that leverage OAuth*"）。
  - 挂钩：**审批与权限**（token 收窄＋默认只读＋免审批的组合行为——无人值守面把安全押在工具收窄而非人工闸上）。
- **治理面**（concepts/enterprise/agent-management.html 实取）：企业 AI Controls 四态策略（enabled everywhere / disabled everywhere / selected organizations，组织可选 custom properties——"*evaluated once at the time of configuration*"，后改属性不自动生效）；"*View and filter a list of agent sessions in your enterprise over the last 24 hours*"；agentic audit log。
  - 挂钩：**循环产品化机制**（企业级 agent 会话审计）。
