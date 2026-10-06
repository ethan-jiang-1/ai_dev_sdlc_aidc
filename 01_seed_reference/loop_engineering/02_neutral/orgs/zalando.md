# zalando — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

**（第四轮挖掘（2026-10-06）：甲方工程博客）**

### 中-1 · Zalando《Agentic Engineering at Zalando: a snapshot》（2026-08-14）

- 公司/作者：Zalando（欧洲时尚电商，甲方）；Bartosz Ocytko（Executive Principal Engineer）
- URL/日期：https://engineering.zalando.com/posts/2026/08/agentic-engineering-at-zalando-a-snapshot.html ｜ Posted on Aug 14, 2026（页面实取）
- 来源类型：官方工程博客一手（全文取得）
- 规模口径：250+ 工程团队（治理节又作 ">200 teams"）、2.5 年历程；LiteLLM 代理 2k MAU（6 个 2C4G pod）；风险审批 bot 自动批准 33% 的 PR、PR lead time 降 20-40%；四个对照代码库（go-agentic-only/go-reference/java-with-agents/java-reference）做复杂度演化。
- **逐字摘录**：

> "We have never centrally mandated the use of a single tool. Users make choices for tools, based on available models and their own preferences (IDE vs. CLI)."

> "In addition to a consistent increase in PR sizes of [100,500) we also see growth in the higher buckets since Sonnet 4 release in Q2/2025, esp. [500,1k) and [1k,2k)."

> "For codebases that started with full use of agentic coding, we see complexity to build up very quickly with growth fading out."

> "33% of our PRs are low-risk and are auto-approved by the bot. ... which in our case reduced PR lead time by 20-40% (when compared with all PRs)."

> "The rule set for the approval bot is built based on analysis of our production incidents and the typical drivers for outages. ... Typos that break configuration are assessed as high risk (would have saved us from the metadpata incident )."

> "With >200 teams innovating and broadly exploring the ecosystem, the question arises whether and when to converge. We believe it's way too early for this."

> "we see users becoming too attached to the coding agent they had been using for a while."

- **与 loop engineering 的挂钩**：risk-based PR approval bot（33% 低风险自动批准、规则源自生产事故分析）＝**停止条件/审批门的产品化**；"agentic-only 代码库复杂度快速抬升"＝**循环产出不收敛的量化实证**；PR 尺寸桶上移＝**循环吞吐压向验证回路**的副作用；"too early to converge"＝外层调度（组织级收敛）的边界划定。
- **该条支持的最小主张**：甲方两年半数据表明：不给统一约束时 agent 编码放大既有代码实践（好与坏都放大），公司以"风险分级自动批准"替代人工橡皮章、但拒绝组织级过早收敛。
- 派别适配：**中性**（混合结果＋治理边界，正反数据并存；其复杂度曲线句可被怀疑档交叉引用）。
