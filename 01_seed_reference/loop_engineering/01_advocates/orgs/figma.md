---
type: org_evidence
directory: 01_advocates/orgs
observation_date: 2026-10-06
---

# figma — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

### 《How Figma stays ahead of vulnerabilities with agents》（2026-07-23）

- 公司/作者：Figma 安全工程；Rohan Sharma / Liam Buchan / Dave Martin
- URL/日期：https://www.figma.com/blog/how-figma-stays-ahead-of-vulnerabilities-with-agents/ ｜ July 23, 2026（页面实取）
- 来源类型：官方工程博客一手（全文取得）
- 规模口径：agent 全量审查每个 PR 已一年＋审计十年老 monorepo；首周精确率 15%（27 中 4）；目标门 70% 精确率（两周回看）；一个月到 80%；双模型冗余（Claude Code + Opus 4.8 xhigh、Codex + GPT-5.6 Sol high）；median $0.50/PR 审查；policy 99 行/2,560 词/68 条 precedents。
- **逐字摘录**：

> "For the past year, agents at Figma have guarded code as it's written, reviewed every pull request, and audited a decade-old monorepo, all on one policy."

> "However, in week one, only about 15% of findings (4 of 27) were valid. That is the trust problem behind OpenAI's argument that precision matters more than recall: Developers stop trusting any tool that floods them with low-quality findings."

> "We held back developer-facing PR comments until precision stayed above 70% over a two-week lookback, with no embarrassingly bad false positives."

> "We currently run both Claude Code with Opus 4.8 at the xhigh (extra-high) effort setting and Codex with GPT-5.6 Sol at high effort, because they miss different bugs. If either model surfaces a finding, we bubble it up."

> "Ninety-nine lines, 2,560 words, and 68 precedents later, this work had a side effect we did not plan for: We had written a complete threat model, in roughly the form we'd want a new hire to read on day one."

- **该条支持的最小主张**：甲方把 agent code review 推进到**无 PR 免审的 merge 基础设施**，路径是先做精确率门（15%→70%→80%）再开闸——"先测量后放权"的可复制配方；policy 即威胁模型（68 precedents）是上下文工程的一手形态。
- 派别适配：**推动·生产化**（其 15% 首周数据同时是中性档"信任不能一步给"的边界证据）。
**与 loop engineering 的挂钩**：agent 审查做成 merge 必经门（"no pull request merges without a completed review pass"）＝验证回路基础设施化；精确率两周回看 70% 门未达不开启开发者可见评论＝渐进放权的停止条件。

### 《How we secure Figma's internal systems with agents》（2026-07-29）

- 公司/作者：Figma 安全工程；Matthew Sullivan / Brad Girardeau
- URL/日期：https://www.figma.com/blog/how-we-secure-figmas-internal-systems-with-agents/ ｜ July 29, 2026（页面实取）
- 来源类型：官方工程博客一手（全文取得）
- 规模口径：告警 time-to-resolution -71%；on-call pages -20%（单靠 RAG 自动降级）；agent 系统＝调查告警→查审计日志→改代码→开 PR→自我记忆。
- **逐字摘录**：

> "Our security team built an AI agent that triages alerts, conducts forensic investigations, queries our security data lake, writes code to fix issues—and remembers what it learns. Here's how we cut alert time-to-resolution by 71% and fundamentally changed how our on-call engineers work."

> "We saw a 20% drop in on-call pages from this change alone."

> "That project eventually grew into a full agentic system that investigates alerts, queries audit logs, writes code changes, opens PRs, and gets better over time through its own memory."

- **该条支持的最小主张**：甲方安全 on-call 的 agent 化给出正收益双数据（-71%/-20%）；注意其含"LLM 自动降级 high/critical 告警"机制（autoResolutionConfidence ≥ 7 即把 severity 改 medium）——该机制是自主环里少见的"agent 自行改低风险等级"实例，判读时可双向使用。
- 派别适配：**推动·生产化**（数据面强；自动降级机制一句供中性档交叉引用）。
**与 loop engineering 的挂钩**：Tines 上以显式工具接口跑 LLM agent loop 做告警分诊（无人值守运行）；LLM 依据 autoResolutionConfidence 自动把 high/critical 告警降级 medium（自主环内改低风险等级＝自主度实例/边界）；"gets better over time through its own memory"＝记忆回路。
