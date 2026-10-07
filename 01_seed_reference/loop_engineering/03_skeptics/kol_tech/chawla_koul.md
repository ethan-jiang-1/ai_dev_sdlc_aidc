---
type: kol_evidence
directory: 03_skeptics/kol_tech
observation_date: 2026-10-06
---

# chawla_koul — loop engineering 证据轨迹（2026-06 后，时间正序）


> **背景**：Tisha Chawla & Susheem Koul——微软工程师组合（Chawla：Commerce and Ecosystem Data Platform 软件工程师，VIT 2024；Koul：高级软件工程师，BITS Pilani 2019）；两人共同创建 AgentPlane（Chronicle agent 执行录制/回放＋TokenOps run 级 token 成本治理）；AIEWF 2026 合讲两场（故障复现＋AI FinOps）。（履历核：ai.engineer 讲者页，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察（一手来源已核）；第九轮（2026-10-07）补全推荐面节（见文末增量）。
### Tisha Chawla & Susheem Koul · AIEWF 2026《Your Agent Failed in Prod. Good Luck Reproducing It.》（视频上传 2026-06-29）

- URL：https://ai.engineer/talks/Lc8zRh9muoY-your-agent-failed-in-prod-good-luck （curl 实取全文）
- 身份：页面无机构字段（同场另有其二人《FinOps for AI Agents》议题）——**仅作会议层样本**。
- **挂钩**：验证回路（可复现性缺失）＋无人值守运行（失控后取证）。
- 逐字摘录：

> "Instead of doing the math, the agent sells the raw number one thousand and dumps it straight into the quantity field… it sells one thousand shares instead. At a hundred and ninety bucks a share, a thousand dollar intent will become a hundred and ninety thousand dollars disaster… The API returned a clean two hundred OK in thirty milliseconds. Zero exceptions, zero alerts."
>（无人值守错单实录：一切监控绿灯、错单已成。）

> "The reflex here is to just turn the model temperature down to absolute zero… But that's a complete misconception. Setting the temperature to zero doesn't fix a broken reasoning path… temperature zero isn't even truly deterministic on a hardware level… The real culprit is batch variance here, because your request gets grouped with whatever else hits the server that millisecond."
>（temperature=0 迷思的四点拆解——采样确定性≠系统确定性。）

> "We've been asking the wrong question all along… The wrong question is, how do I make the model deterministic?"
- **最小主张**：agent 生产事故不可复现是常态；应记录"语义边界/执行包络"并重放状态转移，而不是追逐模型层确定性。
- **派别适配**：**怀疑票（工程实证向）**。

---

# 增量补挖（2026-10-07 第九轮·怀疑者替代推荐专项：推荐面）

> 通道：ai.engineer 讲稿页重取（官方逐字稿＋8 分节全列，fetch 成功）。本轮引句全部当日 fetch 逐字取得。

**官方分节名（全列）**："The production failure that disappears locally"／"Temperature zero does not freeze the serving system"／"Recover the run instead of regenerating it"／"Record semantic boundaries"／"Find where dollars became shares"／"Replay the bad decision against the repaired tool"／"Test enforcement and behavior separately"／"Keep the execution envelope as a test case"。

## 处方面（从确定性改追 replayability）

**逐字摘录（均为仓库新引句）**：

> "The wrong question is, how do I make the model deterministic? And I've seen teams burning weeks on that and walk away deciding the system's just unknowable. The right question is, how do I debug and retest a run I can't reproduce?"
（**正确问题**：不是让模型确定，而是调试并重测不可复现的运行。）

> "The other one is replayability, which is rebuild a run that already happened well enough to debug it. That's observability. You don't need the model deterministic. You need the run recorded, and you don't freeze the model, you capture what it did."
（**确定性 vs replayability**：前者是可控性（拿不到也不想要），后者是可观测性（记录运行而非冻结模型）。）

> "Record at the boundary instead because you need to capture what enters each node and what leaves it, the meaning of each step and not the packets. What replay adds here is a deterministic CI where you stub the model, you'll rerun the exact failure offline with zero model calls."
（**语义边界记录**：记录进出每个节点的含义而非数据包；replay＝stub 掉模型的确定性 CI，零模型调用离线重放原失败。）

> "You cannot control the LLM. That's what this entire discussion is about. You cannot enforce bitwise determinism. What you can do is you can put guardrails on your tools to enforce some level of, uh, credibility on your production agent."
（**工具侧护栏**：控制不了模型，就给工具加护栏。）

> "There are two ways of testing AI agents, and both of them are equally important. There's the deterministic testing and then the behavioral testing."
（**双轨测试**：确定性测试＋行为测试并重。）

> 五条 takeaway（逐字连排）："First, stop chasing bitwise determinism through the API. … Second, know what are variables for your session. For example, your LLM version or your build ID or your RAG chunks, and make sure that you are logging these. Third, capture the full envelope. Don't focus on just the prompt. … Fourth, use the replays to debug. … Fifth and final, keep the generation time variation alive. Don't try to pin the temperature to zero. After all, that is what brings the agency into your agent."
（**五条处方**：停止追位级确定性／记录会话变量（模型版本/构建号/RAG 块）／抓全执行包络／用 replay 调试／**保留生成期随机性**——"那正是把 agency 带进 agent 的东西"。）

- **replay 边界（诚实注记）**：执行包络不含边界内副作用（"side effects inside a boundary are not automatically captured"）；流式捕获仍在计划；replay 本身不是安全屏障（destructive tool 需 gated execution 或 sandbox）。
- **最小主张（增补）**：agent 生产事故的正解是"语义边界记录＋执行包络重放"——把同一 trace 当确定性回归测试，而非追逐模型层确定性。

## 本轮推荐面小结（一句）

替代方案＝**replayability 路线**：语义边界记录、会话变量日志、全执行包络捕获、stub 模型的确定性 CI 重放、原失败 trace 作回归测试、双轨（确定性＋行为）测试、生成期随机性保留。
