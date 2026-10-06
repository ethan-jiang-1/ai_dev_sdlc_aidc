# duolingo — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

**（第四轮挖掘（2026-10-06）：甲方工程博客）**

### 甲-7 · Duolingo《Making production-ready agents the default: building Duolingo's agent platform》（2026-08-04）

- 公司/作者：Duolingo；Guadalupe Aliseda-Canton
- URL/日期：https://blog.duolingo.com/production-ready-ai-agent-platform/ ｜ August 4, 2026（页面实取）
- 来源类型：官方工程博客一手（全文取得）
- 规模口径：公司级 agent 平台（Temporal AgentWorkflow）；agent 创建从数周→约 10 分钟；agent 承载修 CI、回应 code review、发布经理 Slack bot 等工作流。
- **逐字摘录**：

> "Once you want to run it in the cloud, the work shifts from prompting to productionizing."

> "It is not enough to ask whether the agent's output sounds reasonable; we need to know whether it made the right change."

> "The LLM-as-judge is useful, but we do not want our only signal to be one model judging another model's work."

> "AI generates code rapidly, but not necessarily high-quality code. It is trivial to have tools like Claude Code or Codex build an agent, but those tools do not automatically consider durability, observability, or evaluation."

> "This platform collapses that tradeoff: the same tools that allow developers and AI to move quickly also ensure what they build is ready for production."

- **该条支持的最小主张**：甲方把"生产就绪"从工程纪律变成**平台默认值**（定义一次、durability/observability/eval 自动继承）；eval 以确定性 grader（diff_assertions/no_op_consistency）为地基、LLM-judge 仅辅助——"评估不信任模型自评"与 Duolingo 自己的"AI 生成快≠质量高"自认并存。
- 派别适配：**推动·生产化**（平台化正样本；末句自认可作中性档交叉引用）。
**与 loop engineering 的挂钩**：Temporal AgentWorkflow＝durable 外层调度（持久化状态、安全重试、等待人工输入、失败可调试）；no_op_consistency 等 grader＝"报告结果须与 repo 实际状态一致"的验证回路；"agents can trigger one another while Temporal manages durability"＝外层调度产品化主张。
