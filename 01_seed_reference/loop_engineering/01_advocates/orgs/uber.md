# uber — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

**（第四轮挖掘（2026-10-06）：甲方工程博客）**

### 甲-4 · Uber《Running a Software Factory Efficiently at Uber Scale》（2026-08-27）

- 公司/作者：Uber；Uday Kiran Medisetty（Distinguished Engineer）
- URL/日期：https://www.uber.com/blog/efficient-software-factory/ ｜ August 27, 2026（页面实取；eng.uber.com 旧路径 404，www.uber.com/blog 直取成功）
- 来源类型：官方工程博客一手（全文取得；curl＋浏览器 UA）
- 规模口径：70%+ PR 归因 local/cloud agent；3,600+ agent skills；30K+ skill 执行/日；2-8 月 WAU 7x、周 agent 请求 9.4x；AI 总支出 4 月后趋稳；固定模型口径下每千请求成本较峰值 -34%、每 session 成本较 6 月峰值 -52%；MCP 网关 1,000+ server；AI Context Graph 24M 节点/80M 边。
- **逐字摘录**：

> "More than 70% of pull requests are attributed to local or cloud agents. Engineers have built over 3,600 agent skills across the software development life cycle, and executed more than 30K agent skill executions per day."

> "a growing share of sessions aren't initiated by humans, but by automated managed agents handling code review, self-healing CI failures, completing E2E PRs with visual validation, triaging on-call alerts, debugging incoming bugs, and handling a variety of code maintenance tasks with human reviews/escalations."

> "weekly active users across all agentic offerings across all our employees (engineers & non-engineers) grew 7x, and weekly agentic requests grew 9.4x. Meanwhile, our total AI spend has relatively stabilized since April due to optimizations across the board."

> "cost per 1,000 model requests is down almost 34% from its peak, and cost per session is down 52% from its June peak."

> Managed agent outcomes（指标表实取）: "Quality signal (revert rate, F1, MTTR)"; "Outcome-denominated cost (cost per merged PR, cost per review, cost per alert, cost per cleanup)"

- **该条支持的最小主张**：甲方给出迄今最完整的"软件工厂"经济账本：非人发起 session 占比上升（code review/CI 自愈/E2E PR/alert 分诊）、以 revert rate/F1/MTTR 做 managed agent 质量信号、成本方程六项连乘逐项优化——"预算烧光"叙事（见怀疑档）之后 8 月的官方一手回应。
- 派别适配：**推动·生产化**（规模数据 (b) 类最高价值样本；其与媒体"预算耗尽"叙事的关系见怀疑档 Uber 条——两档须对照引用）。
**与 loop engineering 的挂钩**：非人发起 session（code review/CI 自愈/E2E PR/alert 分诊，human reviews/escalations 兜底）＝无人值守运行＋外层调度；revert rate/F1/MTTR 作 managed agent 质量信号＝验证回路；成本方程逐项优化与 spend stabilized＝预算与熔断面治理。
