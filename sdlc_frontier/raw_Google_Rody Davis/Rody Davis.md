# Agent Factory Recap: 100X Engineering with AI Agents in Google Antigravity 2.0

> 嘉宾：Rody Davis，Google 顶级 agentic 工程师
> 主持：Shir Meir Lador，Head of AI Engineering, Google Cloud Developer Relations
> 来源：https://cloud.google.com/blog/topics/developers-practitioners/agent-factory-recap-100x-engineering-with-ai-agents-in-google-antigravity-20/
> 日期：June 18, 2026

---

## Google Antigravity 2.0 概览

从 agentic IDE 进化为完整的 **agent-first 平台**，四个支柱：

1. **桌面 Agent Manager** — 任务编排
2. **CLI** — 服务端/SSH 工作流
3. **SDK** — 自定义 Python agentic 工作流
4. **专业化 IDE** — 可拆卸、可组合

---

## Rody Davis 的核心方法论

### Skills as Context Cheat Sheets

"Skills 就是给 agent 的作弊条。把特定设计系统或 API 文档压缩进 Skill，agent 就更快更准，不用在海量文档里搜索。"

他写了一个 Go CLI，自动把网站解析成 Markdown，批量生成数百个 Skills。

### Bonsai（盆景）代码审查法

"像盆景艺术家一样持续修剪代码库。保持扁平架构，state/UI/data 严格分离，架构违规一眼就能看出来。"

### 分层 Review 策略

- 营销网站 → 审查视觉输出
- 后端逻辑 → 深度审查 API 合约和 schema
- 重复模式 → 人写第一个例子，agent 复制

### 代码库健康是真正瓶颈

"AI 速度的最大瓶颈不是 context window，是糟糕的代码库健康度。"

---

## 100X 工程

AI 加速完整生命周期：
- 同一需求出多个框架版本对比
- 测试套件丰富度远超人工时代
- Bonsai 法分类型审查
- 一键多环境部署 + 自动回滚
- Agent 持续扫描、自动发起清理 PR

---

## 未来预测

1. 非技术创始人将在 2026 年靠纯 vibe coding 上线公司
2. Vibe coding 将引发重大生产事故 → 催生新的软件工程咨询市场
3. 代码库健康度将成为 AI 效率的核心差异化因素
4. Agent 间将出现专业化分工（设计/构建/QA agent）
