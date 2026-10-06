---
type: org_evidence
directory: 03_skeptics/orgs
observation_date: 2026-10-06
---

# amazon — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。

### Gregor Vand & Sean Falconer · Software Engineering Daily #SED News《The Kimi Moment, Runaway AI, and Tokenmaxxing》（2026-08-11，官方 transcript .txt 实取）

- URL：https://softwareengineeringdaily.com/podcasts/sed-news-the-kimi-moment-runaway-ai-and-tokenmaxxing/ ；transcript：https://softwareengineeringdaily.com/wp-content/uploads/2026/08/SED1953-Transcript.txt （curl 实取）
- 身份：SED 常驻主持人档（②——媒体层，非 KOL；价值在事实链而非观点）。
- **挂钩**：预算与熔断（**Amazon 860% 超支案**＋token 计量不可靠）。
- 逐字摘录：
  - "They had about 860% budget overrun over five months, and this was basically, in their word, caused by bad agent loops, just didn't crash loudly enough, and they've just kept being billed."（**Amazon/FT 860% 超支案**：循环不响亮失败＋账单持续——"熔断缺失"迄今最大的具名企业案例，转引自 FT。）
  - "If you build a leaderboard to encourage people to use AI, and that's the metric you're optimizing for, but there's no connection to the value of the use of that AI, what do you think's going to happen? This is really Goodhart's law, essentially, showing up on some sort of schedule. You're rewarding people for tokens consumption, so it's like, you're giving people a license to be wasteful…"（**tokenmaxxing 的组织激励论**。）
  - "he points out towards the end that Claude doesn't provide reliable methods of counting tokens, despite live showing token counts, reporting token counts used for sessions, and billing for tokens… It's just crazy that we do actually have a system at the moment where you literally just don't know what is happening and exactly what it's going to cost and why."（**计量层与账单层脱钩**——预算控制的技术前提不成立。）
  - "I think that all this really ends up coming back to some human decision-making, right?… It really comes back to some human level of control and guardrails in place."（runaway AI 叙事的"人祸"定性。）
- **最小主张**：860% 案把"预算即停止条件"从设计议题变成事故议题；循环的熔断缺失＋计量不可靠＋内部激励错置三层叠加，与第五轮怀疑档"观测层只告警不封"发现闭环。
- **派别适配**：**怀疑票（事故实证向，媒体转述档——FT 原文未取，引用时注明转述链）**。

### FT 原文坐实：《Amazon finds cases of AI causing runaway spending on tech projects》（2026-07-30）——上条 SED→FT 转述链升一手

- URL：FT 官方授权转载（FT中文网互动版，中英双语）：https://app003.ftchinese.com/interactive/289106 （英文版 …/289106/en ；更新于 **2026-07-30 20:07**，作者拉夫•罗斯纳-乌丁；全文经页内官方音频转写 JSON 实取）。二手交叉：TNW 2026-07-30《Amazon spent $1.8m on a Claude job that failed, and it sells the fix》（curl 实取全文）。
- **挂钩**：**预算与熔断**（无人值守部署超支 860% 五个月无告警＝熔断与计量双双缺席）＋**无人值守运行**（错误配置不崩溃、只计费）。
- 逐字摘录（FT 官方中译，全部实取）：

> "在本周的一次内部演示中，员工听取了这样一个案例：亚马逊使用Anthropic的Claude Sonnet模型，将作者资料与集团电商网站上的商品条目进行匹配。尽管这一部署最终失败，公司仍为此花费了180万美元。"
> "这笔支出比项目预算高出860%，而公司过了五个月才发现问题。"

> 连带两案（同一内部演示）："另一个项目中，亚马逊因开发财务审计工具产生了约54.1万美元的意外成本"；"第三起事件涉及利用AI提高物流网络的配送速度，意外支出达到13.4万美元，而且两个多星期后才被发现"。

> "员工被告知，在传统系统中代价'低到几乎可以忽略不计'的编码错误，随着团队开始使用AI模型完成任务，正变得'昂贵到堪称灾难性'。"＋高级员工对 FT："很难弄清楚任何与AI相关的东西到底要花多少钱。"
（**计量层不可用**＝预算熔断的技术前提不成立，与 SED 主持人"Claude doesn't provide reliable methods of counting tokens"互证。）

> **组织激励轴一手坐实**："亚马逊今年早些时候还关闭了一个内部排行榜。该榜单按照员工使用Kiro开发平台的情况进行排名，结果引发了所谓的'刷Token'现象：员工为了提高排名，刻意增加AI Token的消耗量。"
（SED 转述的 Goodhart 定律段由此升为一手——上条"内部排行榜"引句的 FT 原文出处。）

> 亚马逊官方回应（全文两条都录，防断章）："与任何新科技一样，我们也在不断试验、学习并改进使用它的方式，包括如何提高成本效益。"；"挑出少数彼此独立、团队仍在相互学习的案例，并把它们描述为公司的日常状况，并不能反映亚马逊各团队使用AI的真实情况。"（演示材料自注：涉事仅少数团队，30 万员工／季度营收约 1800 亿美元。）

- TNW 机制句（二手，交叉验证用）："When a person writes buggy code, it throws an error and crashes. When a model does the work, a bad configuration just keeps running and quietly bills you. A retry loop that re-sends the same prompt... produces no crash. It produces an invoice."＋讽刺层：AWS 自己卖着 Bedrock 批量推理/Flex 档/prompt 缓存/路由——"The overspend came from picking the frontier model by default and leaving the guardrails off"。
- **口径勘误（对上条 SED 档）**：SED 的 "860% budget overrun **over five months**" 与 FT 原文有差——FT 是"超预算 860%"＋"**过了五个月才发现**"；SED 的 "caused by bad agent loops, just didn't crash loudly enough" 在 FT 中译全文未见逐字（归因句疑为 SED 自家 gloss，TNW 机制归因同向但措辞不同）。引用 860% 案一律以本条 FT 口径为准，SED 句降为播客转述档。
- **该条支持的最小主张**：$1.8M/860%/五个月盲跑＋两起连带＋排行榜刷 Token 被关——"预算即停止条件"的缺失在最大型科技公司内部复现，且发现机制是内部演示而非任何自动护栏。
- **派别适配**：**怀疑票（事故实证向，一手 FT 档——迄今最大具名企业的预算失控白卷）**。
