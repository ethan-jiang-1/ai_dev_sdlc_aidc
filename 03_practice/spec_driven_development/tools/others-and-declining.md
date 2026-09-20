# SDD 赛道「曾经重要 / 不可忽略但非头部」项目盘点

> 观测日期：**2026-09**（GitHub REST API `api.github.com` 实测，抓取于 2026-09-20）。
> 定位：本文件是 `../sdd-tooling-landscape-2026-09.md` 的补充——该文件覆盖公认头部（Spec Kit / OpenSpec / Superpowers / BMAD / Kiro / Tessl），本文件覆盖**曾经重要或不可忽略但非头部**的项目：主要是下降与被放弃者。
> 方法：stars / `pushed_at` / 最新 release 均直读 GitHub API，标注观测日期；商业信号以仓库 homepage、release notes 内容为证。
> 约定：每节按「定位 / 数据指标 / 趋势判断 / 现状定性」模板。

---

## 1. claude-task-master（eyaltoledano/claude-task-master）

### 定位
AI 驱动的 PRD → task 拆解与任务管理系统（`task-master-ai` npm 包 + MCP server），可接入 Claude Code / Cursor / Windsurf / Roo / Lovable 等。**2025 上半年是"PRD 拆成可执行任务链"这一环节的事实标准**：在 Spec Kit（2025-08）、OpenSpec（2025-08）出现之前，它是 SDD 兴起早期最广泛安装的工具（创建于 2025-03-04，本赛道最早的大体量项目之一）。

### 数据指标（GitHub API，观测 2026-09-20）
- **Stars / Forks**：**28,085 / 2,619**；open issues 212；watchers（subscribers）164；license 为自定义 "Other"（非标准 OSI）。
- **创建时间**：2025-03-04。
- **最近 push**：**2026-04-28** —— 至观测日近 5 个月无任何 push。
- **最近 release**：**task-master-ai@0.43.1，2026-03-31**（再往前 v0.43.0 为 2026-02-04、v0.42.0 为 2026-01-15，节奏尚可后骤停）；此后无 release。
- **商业转向信号**：仓库 **homepage 已改为 `https://tryhamster.com`**（Hamster，同作者的商业产品）；2026-03-31 的 v0.43.1 release notes 明确写着"**移除 init 时的 `hamster` / `ham` shell 别名**"——开源仓库的发布流水线已被引导向商业产品。

### 趋势判断（依据链）
**下降 → 被放弃**，证据链四条且相互印证：
1. `pushed_at` 停在 2026-04-28，近 5 个月零提交（对比同赛道头部：Spec Kit / OpenSpec / Superpowers 观测当周均有 push 与 release）；
2. release 流水线 2026-03-31 后停摆，且最后一次发布还在为商业产品做清理；
3. homepage 指向商业产品 tryhamster.com，作者精力已转移（本库 API 报告中 2026-09-20 快照同此）；
4. 外部定位证据：212 个 open issues 无人收敛、社区分叉（存在 developerz-ai/claude-task-master 等社区续命 fork）。功能层面其"PRD→task"生态位已被 Spec Kit 的 tasks 阶段与 OpenSpec 的 change-delta 流程整体覆盖。

### 现状定性：**被放弃**（项目本体转向商业产品 Hamster；28k stars 是历史存量，不是当前动量）

---

## 2. 快速扫描：其他可上台面的非头部 SDD 项目

头部之外逐仓实测后，"还能上台面"的其实很少：多数 spec workflow 工具是 Kiro 工作流的个人仿制品，star 量级个位数到低三位数。按体量筛出以下三个值得记录的对象。

### 2.1 spec-workflow-mcp（Pimzino/spec-workflow-mcp）

- **定位**：非头部阵营中体量最大的"结构化 spec 工作流"工具——MCP server 提供 requirements → design → tasks 三段式工作流工具，配实时 Web dashboard 和 VSCode 扩展，服务 AI 辅助开发。是"把 Kiro 式三文档流程做成 MCP 服务"这条路线的代表作。
- **数据指标**（GitHub API，观测 2026-09-20）：**4,293 stars / 355 forks**；创建 2025-08-07（与 Spec Kit / OpenSpec 同月）；license GPL-3.0；open issues 仅 10；**最近 push 2026-07-03**（观测前约 11 周）；**GitHub Releases 为空**——该项目不经 GitHub release 发布，版本走 npm tag（仓库无 release 页记录）。
- **趋势判断**：早期上升势头好（一年 4.3k stars），但**最近 2 个多月无 push**，与头部项目的周级节奏已明显脱节；10 个 open issues、单维护者主导（个人 repo），活性靠作者个人投入。
- **现状定性**：**平台期偏缓降**（社区存量可观、更新放缓；尚未到"下降"定论，但若 2026 Q4 仍无 push 应下调）。证据强度：中强（API 直读，但缺 release 节奏可参照）。

### 2.2 FredAntB/Spec-Driven-Development（Kiro 式 Claude skill）

- **定位**：Claude skill 形态的 Kiro 工作流仿制品——写代码前先生成 requirements.md / design.md / tasks.md，并为 Claude Code / Cursor / Copilot / Windsurf / Aider 生成配套配置。2026-05-21 以 "Show HN: I Made a Claude Skill for SDD" 上 HN（40 分 17 评，作者自称照 Kiro 的 SDD 管理来做）。
- **数据指标**（GitHub API，观测 2026-09-20）：**154 stars / 16 forks**；创建 2026-05-18；**最近 push 2026-05-23**——上线仅 5 天后即停更；MIT；8 个 open issues。
- **趋势判断**：HN 热度未转化为持续维护，属于典型的"Kiro 被模仿"现象样本：证明 Kiro 的 spec 工作流是公认的模仿对象，但单品无持续投入即迅速沉寂。
- **现状定性**：**下降（昙花一现）**。证据强度：强（API 直读）。

### 2.3 kodik（nkyriakidis/kodik）

- **定位**：自称 "An open source implementation of the Amazon Kiro Agent modes"（Go 实现），是 Kiro 开源仿制中少数明确以"复刻 Kiro agent 模式"为目标的仓库。
- **数据指标**（GitHub API，观测 2026-09-20）：**9 stars / 1 fork**；创建 2025-07-18（Kiro preview 当月）；**最近 push 2025-10-24**——近 11 个月无更新。
- **趋势判断**：从未起量，且 Kiro 本体在 2025-11 GA 后快速扩张（CLI/Web/Mobile），个人复刻失去存在理由。
- **现状定性**：**被放弃**。证据强度：强（API 直读）。同类 Kiro 仿制/微工具还有 hangboss1761/spec-driven-mcp（2 stars，2025-07-29 后停更）等，均不足上台面，此处仅存目。

---

## 3. 小结

- 非头部阵营的整体叙事是**生态位被头部收编**：claude-task-master 的"PRD→task"被 Spec Kit/OpenSpec 的模板流覆盖，Kiro 仿制品被 Kiro 本体的快速产品化（GA + 多端）消灭了存在理由。
- 唯一仍在牌桌边缘的非头部项目是 **spec-workflow-mcp**（4.3k stars），但其更新节奏也已放缓。
- "工具层洗牌"（见全景文档 §2B）在非头部阵营表现得比头部更残酷：头部四强全部周级活跃，非头部要么停更、要么靠历史存量维持。

## 来源清单

- GitHub API repos 端点：`api.github.com/repos/{eyaltoledano/claude-task-master, Pimzino/spec-workflow-mcp, FredAntB/Spec-Driven-Development, nkyriakidis/kodik, hangboss1761/spec-driven-mcp}`（观测 2026-09-20）
- GitHub API releases 端点：claude-task-master（最新 task-master-ai@0.43.1，2026-03-31）、spec-workflow-mcp（空）、其余仓库无 release（观测 2026-09-20）
- 头部项目对比数据引自 [sdd-tooling-landscape-2026-09.md](../sdd-tooling-landscape-2026-09.md)（观测同日）

**已知局限**：① spec-workflow-mcp 无 GitHub release，活跃度只能以 `pushed_at` 判断，npm 下载量未测；② "可上台面"的扫描以 topic 搜索 + HN 线索为准，未穷举全部 `spec-driven-development` topic 仓库；③ claude-task-master 商业产品 Hamster 的用户/收入数据未核实（超出本文件 API 方法范围）。
