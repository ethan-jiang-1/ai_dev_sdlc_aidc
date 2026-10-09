# 103 来源台账 — 主张到来源

> 本文件维护 103 采用哪些主张及其强度；案例和模板属于教学转译，不由出处直接担保效果。上游只读。Grill-me 的一手源码核准与研究摘录集中在 [研究笔记](<01-grill-me-requirements-acceptance.md>)，不复制正文。

## 证据等级

- **A：本轮一手回源**——作者源码、作者文档或官方正文；说明是可核对的方法主张，不自动证明方法效果。
- **B：仓库既有回源档案／实践归纳**——本轮已读内部材料，外部原文复读情况另标；不伪装成此次独立抓取。
- **C：本场教学提案**——故事线、案例、表单、练习、收口与试验设计；可讨论、可演练，没有实测背书。

## 采用映射

| 编号 | 103 要使用的主张 | 来源与锚点 | 强度／限制 |
|---|---|---|---|
| S1 | 用关键决定的依赖结构追问，先查可查事实，人确认取舍 | [Grill-me 核准笔记](<01-grill-me-requirements-acceptance.md>)中的作者源码／文档 | A 的具体范围以笔记为准；不是完整需求工程标准，也不是验收体系 |
| S2 | 需求要包含可观察结果、边界与判断依据 | [需求工程入口](<../../03_practice/requirements_engineering/README.md>)及研究笔记中引用的具体实践段落 | B；本场需求小单是 C，不要求采用完整规格格式 |
| S3 | Harness 环境需要现行事实的唯一维护处；指引与执行分开 | [实践主干](<../../03_practice/harness_governance/result/backbone.md>) §1.3、§2 工件4–6；[操作规程](<../../03_practice/harness_governance/result/manual.md>) §7 | B：内部已确认实践；“docs只写now”等归纳有适用范围，不从本场引申为所有文档禁历史 |
| S4 | 每种检查只证明可观察的性质；检查自身要经反例验证 | [实践主干](<../../03_practice/harness_governance/result/backbone.md>) §3.1、§3.7；[操作规程](<../../03_practice/harness_governance/result/manual.md>) §6 | B：多源原则与内部操作归纳；引入正常例、报价证据表为 C |
| S5 | 执行者自评有偏向，验收需要实际证据，AI 判断应校准 | [既有一手摘录](<../../03_practice/harness_governance/research/02a-harness-convergence-evidence.md>) A5.3–A5.4；官方原文 [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps) | B：本轮复读仓库回源记录；不把自评偏差讲成所有模型／任务必然夸大，也不把独立评审讲成保证 |
| S6 | 约束需有执行点、反馈及持续调优；不触发也可能是检测不足 | [既有一手摘录](<../../03_practice/harness_governance/research/02a-harness-convergence-evidence.md>) A3.2；[Böckeler 作者原文](https://martinfowler.com/articles/harness-engineering.html) | B：本轮复读既有档案；四项治理动作是本场 C 分组 |
| S7 | 真正失败可成为环境改进的锚点；新增约束需要复核 | [实践主干](<../../03_practice/harness_governance/result/backbone.md>) §4；[操作规程](<../../03_practice/harness_governance/result/manual.md>) §2、§7.6；[Hashimoto 作者文](https://mitchellh.com/writing/my-ai-adoption-journey) | B：本轮对 Hashimoto 的 web_fetch 被工具拒绝（hostname 解析为 non-public IP），采用内部既有回源；“第二次”是上游操作阈值，本场不用作通用门槛 |
| S8 | Harness 组件隐含能力假设，模型改进后值得复检与简化 | [Anthropic 既有一手摘录](<../../03_practice/harness_governance/research/02a-harness-convergence-evidence.md>) A5.3；[实践主干](<../../03_practice/harness_governance/result/backbone.md>) §4.3 | B；保持条件可比、正常／边界例、适当重复、恢复路径的试撤方案是 C；模型一次不犯错不构成删规则依据 |
| S9 | 可验证目标与评价需要匹配；难评价时不能假装已有可靠信号 | [Goal／Eval 研究入口](<../../02_research/01_agent_engineering/goal_eval_engineering/README.md>)与研究笔记的对应读取段落 | B；本场仅借鉴验收尺度与不可观测边界，不讲搜索／调度算法 |
| T1 | 业务要求→试做→直接反馈→修订与重验的对齐循环，由验收证据和环境治理承接 | [故事线](<../01_storyline/00-storyline-map.md#二主轴与推导>) | C：本场综合，不署成某位作者原框架 |
| T2 | 报价草稿案例、正反样本、证据表、变更处理与受控试撤 | [案例源](<../01_storyline/02-case-walkthrough.md>) | C：合成、未实现、未运行；不能引用成稳定性或业务收益证据 |
| T3 | 业务理解撑住需求与验收两头；对齐难、依赖经验与反复打磨，转述容易失真 | 用户本轮直接定调，唯一解释处为 [CONTEXT](<../CONTEXT.md#一听众基准>)；[案例试做](<../01_storyline/02-case-walkthrough.md#看输出才说出脑子里的标准>)作教学展示 | 用户定位＋C：不声称 Grill-me 作者提出此整套论点；没有直接沟通相对转述的效果测量，不推导协作者必然导致失真 |

> 上游引用使用文件链接与表内段落名定位，不修改上游标题或重复其正文。

## 对外使用约束

1. 方法归纳可直接讲具体动作，外部作者只为其真实主张署名；不要在每页贴机构名营造背书。
2. Grill-me 与 grilling 的关系以钉版源码核准，不按用户拼写猜产品，不拿本机另一个同名技能替代作者原文。
3. “金额检查不证明来源有效”“规则变了旧证据需识别影响”是本场案例的逻辑，不拿统计数字装成实证。
4. 既有 OpenAI 材料有半回源／转述边界。本轮抓取 [官方文](https://openai.com/index/harness-engineering/)同样被工具拒绝，故不追加其具体效果、吞吐与规模数字。
5. 上游含“自评必然自夸”“新模型不再犯就删”等较强表达，103 采用有条件表述：已观察到的偏向需要独立证据；试撤需要多类样本、适用条件和恢复路径。这是适用范围收窄，不改上游方法权威。
6. 无真实运行报告；来源研究不能代替产品验收。证据缺口只在 [开放问题](<../01_storyline/04-open-questions.md#证据与演练缺口>)登记。
