# 智能体编排：全球趋势与实践 Roadmap

历经过去两年 AI 编码助手（如 Copilot, Cursor）的蜜月期，软件行业正向全自动化的“AI软件工厂”跃迁。在这场关于“如何管理和编排 10 到 1000 个自主 Agent 协同写代码”的底层架构革命中，业界逐渐分化出了三大极具代表性、且深刻影响未来技术栈的主流流派。

本系列文档将深度拆解这三大流派背后的核心思想、标志性项目以及所带来的范式转移：

---

### [01] 极限护栏与物理沙盒流派 (The Harness & Sandbox Paradigm)
**(SDD - 规范驱动开发的工业级升华)**
针对“AI产生不可预测的烂代码从而摧毁代码库架构”的痛点。该流派主张放弃用自然语言约束 AI，而是采用极其残酷的物理强制阻断与试错沙箱。在这一流派中，人类只需要编写规格说明（Specs）和拦截器（Linters），AI 自动完形。
* **代表实验与工具**：OpenAI 的 "Harness Engineering" (用架构 Linters 取代人类 Code Review，零人工编写百万行代码)、StrongDM 的 "Dark Factory" 与数字孪生宇宙测试区。
* **详情参阅**：`01_Harness_and_Sandbox_Paradigm.md`

### [02] 高并发协同与集群编排流派 (Parallel Collaboration & Orchestration Paradigm)
针对“人类等待单体 AI 串行生成代码耗时过长”的物理吞吐量瓶颈。该流派致力于通过底层的文件系统隔离和同步机制，让大规模的 AI 集群实现无锁的高效并发。
* **模式 A（流水线看板）**：Vibe Kanban, OpenAI Symphony (利用 Git Worktrees 提供绝对物理隔离的流水线沙盒)。
* **模式 B（去中心化自治）**：Anthropic Agent Teams 架构 (16-Agent C-Compiler 军团，利用 Markdown 共享状态与秒级的 Git 文件锁，实现无中央大脑的狂野生机)。
* **详情参阅**：`02_Parallel_Collaboration_Paradigm.md`

### [03] 确定性通信与大一统基建流派 (Deterministic Protocols & Infra Paradigm)
针对“多节点 AI 流转中因为格式错误或幻觉导致全链路崩溃”的木桶效应。该流派坚持把大模型拉回古典软件工程的泥潭，用强力的分布式架构协议给 AI 套上笼头。
* **代表实验与框架**：SagaLLM (将 AI 编排比作分布式数据库事务，提供错误补偿回滚)、Pydantic AI (利用 JSON Schema 和 `pydantic-graph` 强行约束有限状态机类型安全)、以及大一统的底层协议 MCP 与 A2A (Linux Foundation 的星际通用翻译器)。
* **详情参阅**：`03_Deterministic_Protocols_and_Infra_Paradigm.md`

---

最后，关于这三大流派如何重塑未来十年的开发者技能树和企业级“代码印钞厂”架构，请见最终的总结陈词：
👉 **详情参阅**：`04_Master_Framework_Consolidation.md`
