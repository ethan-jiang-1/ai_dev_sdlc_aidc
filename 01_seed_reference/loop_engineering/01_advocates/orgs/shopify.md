---
type: org_evidence
directory: 01_advocates/orgs
observation_date: 2026-10-06
---

# shopify — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

### 《How River takes security work from a fix to merge》（2026-09-02）

- 公司/作者：Shopify（甲方，全球最大电商 SaaS 之一）；Kaiyi Li（AppSec）
- URL/日期：https://shopify.engineering/river-vulnerability-remediation ｜ Published on Sep 2, 2026（页面实取）
- 来源类型：官方工程博客一手（全文取得，curl＋浏览器 UA）
- 规模口径：River＝公司级 Slack 常驻 agent（底座 Aquifer）；依赖修复工作流上线首 11 天数据；freshness-gated merge queue 自上线以来 10%→80%；单次运行 4 线程/分钟覆盖 35 findings；单批 8 个依赖 PR。系列上下文（窗口边缘登记）：系列首篇《Under the River》（2026-05-28，早窗口 4 天）给出 30 天 59,918 River sessions、5,170 Slack 频道、3,536 River-coauthored PR merged、"one in eight merged pull requests across Shopify is coauthored by it"——本条判定可引用该基数但须标窗口边缘。
- **逐字摘录**：

> "In the first 11 days of running the dependency workflow, the backlog of open issues fell by about 70%. Roughly two-thirds were direct merges, and the rest were confirmed by River as obsolete or already fixed elsewhere. Since launch, security merges through our freshness-gated merge queue went from about 10% to 80%."

> "So River treats every ledger entry as a claim to be checked, not a fact."

> "It didn't rebase the eighth PR. A human had taken over that branch with their own commits, and a second engineer had an open review on it. Rebasing would have overwritten someone's work and pre-empted a design question, so it went back to its author untouched."

> "Owners supply product context, accept risk, review, and merge. They don't shuttle state between Git, CI, Slack, and the tracker."

> "when you can't define the outcome you want, or the evidence that would prove it correct, another edit is a bet rather than a fix."

> "Attackers can tolerate repeated failure but defenders, especially organizations, have to preserve production-intended behavior with every fix."

- **该条支持的最小主张**：甲方公开一手确认"自主修复环"已跑在生产上且有量化结果（积压 -70%、合并队列 10%→80%），同时把自主环的边界写得极具体——账本只是主张不是事实、人的分支不碰、不能定义验收证据就停手。这是"循环外层治理"（ledger 对账、freshness 门禁、handoff 分级）的最佳一手样本。
- 派别适配：**推动·生产化**（正面，但引句时注意其"handoff the decision, not the investigation"是自主度分档表述）。
**与 loop engineering 的挂钩**：自主修复环的完整外层治理一手——ledger 只是主张须逐项对账（验证回路）、freshness-gated merge queue（合并门禁＝停止条件）、"不能定义验收证据就停手"（停止条件）、人接管的分支不 rebasing（自主度上界）；整体＝生产上的无人值守修复运行。

### 《Sidekick's continual learning loop》（2026-08-05）

- 公司/作者：Shopify；Andrew McNamara / Cody Mazza-Anthony
- URL/日期：https://shopify.engineering/sidekicks-continual-learning-loop ｜ Published on Aug 5, 2026（页面实取）
- 来源类型：官方工程博客一手（全文取得）
- 规模口径：GraphQL agent 生产 2,000 RPM；前沿模型服务估算 $27M/年 vs 微调后 ~$1M（-96%）；gisting 把 6,000 token 系统提示压到 ~1,500（350 RPM 下 TTFT -19%、端到端 -38%、同 GPU 吞吐 +16%、GPU 省 ~14%）；self-healing 管线**每天**跑。
- **逐字摘录**：

> "How we compress production failures into model weights every day, beat frontier-model quality, and cut serving costs 96%."（副标题）

> "The flywheel is our answer: a continual learning loop that compresses production experience into the continuous space of the model's weights."

> "The self-healing pipeline runs daily, continually adding new trajectories to the training corpus."

> "If the rubric confuses several product experts who work on this product every day, it will confuse an LLM too. That agreement is the judge's ceiling: even expert annotators do not agree 100% of the time, because some conversations are genuinely ambiguous."

> "Defining quality is the most important step in the loop—and the one that teams most often rush. ... When you get it wrong, everything downstream optimizes the wrong behavior."

- **该条支持的最小主张**：甲方把"生产失败→训练语料→每日微调"做成闭环并给出成本/质量双量化（$27M→$1M、超越前沿基线）——"loop"在这里从推理时循环扩展到"跨天训练环"；同时自认质量定义（rubric＋Cohen's kappa 标定）是全环第一优先级、标 judges 有天花板。
- 派别适配：**推动·生产化**（经济面＋训练环面的一手规模数据；其"judge's ceiling"句同时可被中性档引用）。
**与 loop engineering 的挂钩**："continual learning loop" 即跨天训练环：生产失败→轨迹语料→每日 SFT/GRPO（循环产品化机制）；quality rubric＋Cohen's kappa 标定＝奖励信号（验证回路）；"judge's ceiling"＝评分器置信上界（停止判据边界）。

### 《Building an agentic harness that outlasts the model》（2026-07-29）

- 公司/作者：Shopify AppSec 团队
- URL/日期：https://shopify.engineering/building-an-agentic-harness-that-outlasts-the-model ｜ Published on Jul 29, 2026（页面实取）
- 来源类型：官方工程博客一手（全文取得）
- 规模口径：harness 运行"one of the largest Rails monoliths in the world"；评估新安全微调模型"Over the past five months"；单次审计 30+ 候选漏洞；扫描覆盖最重要公开面。
- **逐字摘录**：

> "We've built an agentic code review and test oracle harness that discovers vulnerabilities in our software, proves them with real tests, and provides Shopify-tuned fixes before presenting them to our developers."

> "In one audit, a model uncovered more than 30 candidate vulnerabilities. After validation, every one was downgraded to low or medium, found to be a false positive, or reclassified as defense in depth."

> "The models are getting better, but the most important piece of the system remains the harness."

- **该条支持的最小主张**：甲方安全团队把"发现→测试证明→修复 PR"agent 环做成平台（内部编排器 Dispatch），并明确"模型在换、harness 是常量"；但同篇自曝 30+ 候选全被验证层降级/判误报——推动叙事与"验证层才是产能"的数据并存。
- 派别适配：**推动·生产化**（"harness outlasts the model"＝把控性主题的正样本）；其 30+ 全降级句**同时是中性档可用的边界数据**（引用时注明双面性）。
**与 loop engineering 的挂钩**：发现→test oracle 实测证明→修复 PR 的验证回路闭环；30+ 候选全部被验证层降级/判误报＝验证层才是实际闸门（停止条件）；"harness outlasts the model"＝循环资产化主张。
- 判读注记：DORA 转引的 "circuit breaker" 一手仍未落点——shopify.engineering 窗口内全部 agent 帖正文（含本篇）grep 均无 "circuit breaker"/"loop detection" 术语；功能性对应物见怀疑档负结论。
