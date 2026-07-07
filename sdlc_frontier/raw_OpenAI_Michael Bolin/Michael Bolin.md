# Unwinding Codex's Agent Loop（中文编译）

> 作者：Michael Bolin，OpenAI Technical Staff
> 原文：https://openai.com/index/unwinding-codex-agent-loop/ （系列首篇，2026年1月23日）
> 编译来源：36kr、Ars Technica、机器之心

---

## 背景

在 OpenAI 内部，"Codex"涵盖了一系列软件智能体产品，包括 Codex CLI、Codex Cloud 和 Codex VS Code 插件，支撑它们的框架和执行逻辑是同一个 Agent Loop。这是 OpenAI 首次对外公开 Agent Loop 的内部实现细节。

---

## Agent Loop 核心架构

每个 AI 智能体的核心是 Agent Loop，负责协调用户、模型以及工具之间的交互：

```
用户输入 → 构建提示词 → 模型推理 →
  工具调用？→ 执行工具 → 追加输出 → 重新查询模型
  助手消息？→ 返回用户
```

每一轮交互最终以 assistant message 收尾，标志着 Agent Loop 进入终止状态。

---

## 提示词构建：用户输入放在最后

Codex 并非直接把用户输入发给模型，而是拼接一整套精心设计的提示词结构：

1. 模型专属指令（来自 `~/.codex/config.toml` 或内置）
2. 沙箱环境描述（仅限 Codex 内置 Shell 工具）
3. 用户 `developer_instructions` 配置
4. AGENTS.md / AGENTS.override.md（从 `$CODEX_HOME` 到当前目录多层叠加）
5. Skills 元数据与调用说明
6. 本地环境信息（工作目录、Shell 类型）
7. 用户的原始消息

优先级：system > developer > user > assistant

---

## Responses API 驱动

Codex 使用 Responses API 作为推理后端。每次 HTTP POST 发送完整 JSON 负载，通过 SSE 流式接收响应。

Codex **故意不使用** `previous_response_id` 参数——这是为了保持请求完全无状态，兼容 Zero Data Retention (ZDR) 隐私合规。

---

## 提示词缓存：O(n²) → O(n)

缓存命中要求**精确前缀匹配**。Codex 团队为此做了大量投入：

破坏缓存的常见操作：
- 对话中修改工具列表
- 切换模型
- 修改沙箱配置/审批模式
- 修改工作目录
- MCP 工具枚举顺序不一致（已修 bug）

配置变更时，不在早期消息上修改，而是在输入末尾追加新消息。

---

## 上下文压缩

当 token 超过 `auto_compact_limit` 阈值时自动触发：
- 使用专用 `/responses/compact` 端点
- 返回压缩条目 + `encrypted_content` 字段保留语义
- 完全自动化

---

## 沙箱

- macOS：Seatbelt
- Linux：Bubblewrap + seccomp + Landlock
- Windows：OpenAI 自建沙箱

MCP 服务器提供的自定义工具不受 Codex 沙箱限制，需自行防护。

---

## 影响

Codex CLI 已在 GitHub 开源。截至文章发布时，Codex 已接管 OpenAI 100% 的代码编写工作。

社区共识：**"看似平淡的技术最终胜出。OpenAI 证明优秀架构远胜于花哨工具。"**
