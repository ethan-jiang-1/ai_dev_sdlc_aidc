# 前沿顶级 Agent Harness 体系（Frontier Systems）

> 本目录对当前业界最具影响力的四大前沿 Agent Harness 体系——**Anthropic Claude Code、DeepSeek Harness (`dsh`)、OpenAI Codex 体系、OpenHands** 进行横向剖析，重点解密每个体系如何落地 **Dynamic Workflow 与动态 DAG 编排**。

---

## 1. 核心问题意识

当任务进入超大规模工程化阶段（如跨数百文件的系统迁移、分布式微服务联调、SWE-bench 复杂 Issue 攻坚），单体 LLM 的自主循环必然面临“上下文污染、无序并发冲突、缺乏可复现性”的硬瓶颈。

各大前沿机构没有退回传统的静态死板流程，也没有盲目推崇黑盒多智能体自由群聊，而是分别演化出了四种截然不同的动态编排哲学：
1. **Claude Code**：**Code-as-Workflow（代码即编排）**——由 LLM 动态编写 JS/TS 编排脚本，在底层沙箱中调度海量子代理；
2. **DeepSeek Harness (`dsh`)**：**Cordis 插件底座 + 显式 Task DAG**——主控 Captain 动态生成带依赖拓扑的无环图，就绪队列驱动执行；
3. **OpenAI Codex**：**Worktree 物理并行 + 结构化 Manifest**——通过底层 `git worktree` 实现物理隔离调度，配合强门禁保证结果一致性；
4. **OpenHands**：**Manager DAG 分解 + `AgentDelegateAction` 原语**——显式子任务拓扑调度，配合会话历史的 DAG 树形虚拟化防止失忆。

---

## 2. 目录文件全景

| 文件 | 剖析体系 | 动态工作流核心机制 |
|---|---|---|
| [01-claude-code-workflows.md](01-claude-code-workflows.md) | Anthropic Claude Code | 解密其 Dynamic Workflows / Ultracode：LLM 沙箱内动态生成并执行 JS 编排脚本，百级别子代理并发调度与零污染状态汇总 |
| [02-deepseek-harness-dsh.md](02-deepseek-harness-dsh.md) | DeepSeek Harness (`dsh`) | 深度剖析 Cordis 插件底座与 `dsh-agent-teams`：Captain 动态 Task DAG 依赖建模、入度就绪触发与 Web 端 DAG 实时可视化 |
| [03-openai-codex-harness.md](03-openai-codex-harness.md) | OpenAI Codex 体系 | 深入 Codex CLI 与 App Server：基于 Git Worktrees 的物理并发拓扑、Manifest 结构化步骤控制与 MCP 门禁治理 |
| [04-openhands-subagents.md](04-openhands-subagents.md) | OpenHands (原 OpenDevin) | 剖析 Manager Agent 的动态 Subtask DAG 生成、`AgentDelegateAction` 委派原语与会话上下文 DAG 虚拟化架构 |

---

## 3. 四大前沿体系核心技术横向对比矩阵

| 评估维度 | Claude Code (Anthropic) | DeepSeek Harness (`dsh`) | OpenAI Codex 体系 | OpenHands (社区) |
|---|---|---|---|---|
| **编排核心载体** | 可执行代码（JS/TS 脚本） | 显式 Task DAG 数据结构 | Git Worktrees + Manifest | 显式 Subtask DAG + 原语 |
| **动态生成方式** | LLM 编写 Orchestration 脚本 | Captain 模型输出 JSON DAG | Plan-First 模式生成步骤 | Manager 生成依赖拓扑树 |
| **依赖拓扑管理** | 代码内 `Promise.all` / `await` | 调度器动态计算入度（In-degree=0） | 串行/并行 Worktree 聚合分支 | 调度引擎就绪队列拓扑推进 |
| **执行上下文隔离** | 独立 Subagent 进程 + 沙箱 | 插件化沙箱 + 独立 Session | 操作系统级 `git worktree` | Docker 容器 + 虚拟上下文 DAG |
| **失败容错与自愈** | 脚本级 `try-catch` 重试 | 拓扑级节点重试 + 状态回退 | 断言失败中断 + 人工介入 | Agent 自省反思 + 子代理再派发 |
| **可观测性与审计** | 结构化聚合报告 | Web DAG 看板 + 事件溯源日志 | JSON-RPC 事件流 + PR Diff | 交互式轨迹追踪看板 |
