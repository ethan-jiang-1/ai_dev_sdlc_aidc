# Grill-me：需求说清楚与验收有方的证据研究

> 用途：103 上游证据；面向业务熟、AI 有初步理解、已在搭 Agent、技术一般的听众。只读上游，仅生成本文件。不是作者技能安装指南，也不是完整需求工程或 eval 综述。

## 1. 结论先行

1. **GILL-ME 很可能是 `grill-me` 的口述／拼写误差，但不能说用户已确认名称。** Matt Pocock 作者仓库确有此名；当前入口明确调用 `grilling`。本机 `grilling` 与作者当前底层技能有源码可核的联系，不能仅因名字不同认作无关，也不能把本机副本直接等同作者某个版本。**强度：一手源码直接，用户意图仍为推定。** 来源：[作者入口 L1–7](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/productivity/grill-me/SKILL.md#L1-L7>)、[本机入口 L1–28](</Users/bowhead/.agents/skills/grilling/SKILL.md#L1-L28>)。
2. **核心不是“让 AI 多问”，而是沿决定依赖形成共同理解：事实能查先查；人决定取舍；回答推动下一枝；不能留下默默猜定的关键决定。** **强度：一手机制直接，未提供效果对照。** 来源：[作者 grilling L6–30](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/productivity/grilling/SKILL.md#L6-L30>)。
3. **需求澄清不自动等于验收设计。** 作者当前 `grill-me` 无状态、不落文件；相邻 `to-spec` 另设 Testing Decisions，TDD 另规定测试边界、独立预期值与逐条实现。**强度：一手机制直接；“两段不能自动合并”为跨源推论。** 来源：[作者说明 L3–5](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/docs/productivity/grill-me.md#L3-L5>)、[to-spec L13–19、59–69](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/to-spec/SKILL.md#L13-L69>)、[TDD L14–37](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/tdd/SKILL.md#L14-L37>)。
4. **不能无限追问。** 作者要求用户控制范围、允许“不知道”；对必须看原型才能决定的问题，明确要求停止 grilling，先做可抛弃原型。**强度：作者一手说明直接，实践建议而非实验结论。** 来源：[作者说明 L23–37、48–62](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/docs/productivity/grill-me.md#L23-L62>)。
5. **103 的验收增量可收成五问：检查什么；拿什么输入／参照；预期是什么；看到什么证据；由谁接受／打回。** 难判时切小核对面、让业务人先判实例、把系统外结果留给人观察。**强度：教学转译，有仓库一手档案支持，未实测本场方案。** 来源：[Hamel 四问与边界 L13–22](</Users/bowhead/ai_dev_sdlc_aidc/02_research/01_agent_engineering/goal_eval_engineering/raw/evidence-2026-09-27-c-hard.md#L13-L22>)、[Yeret 产出／结果 L30–36](</Users/bowhead/ai_dev_sdlc_aidc/02_research/01_agent_engineering/goal_eval_engineering/raw/evidence-2026-09-27-c-hard.md#L30-L36>)、[Shankar 人判失败类型 L28–46](</Users/bowhead/ai_dev_sdlc_aidc/02_research/01_agent_engineering/goal_eval_engineering/raw/evidence-2026-09-27-a5-shankar-talk.md#L28-L46>)。

## 2. 身份与版本核准

作者材料固定到 GitHub commit **`b0618bc436ad893b3c5e84e55fba86586d34a404`**（GitHub API 返回作者 Matt Pocock，commit 日期 2026-10-08）。本轮先读本机入口，再读作者入口、底层实现、作者说明和相邻测试材料。**强度：一手元数据。** [版本锚](<https://github.com/mattpocock/skills/commit/b0618bc436ad893b3c5e84e55fba86586d34a404>)。

| 对象 | 核准结果 | 精确来源与强度 |
|---|---|---|
| 当前 `grill-me` | `disable-model-invocation: true`，用户显式调用入口；正文仅 `Call the Skill tool with "grilling".` | [入口 L1–7](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/productivity/grill-me/SKILL.md#L1-L7>)；一手源码直接 |
| 当前 `grilling` | 设计树；按轮问全部已满足前置条件的 frontier；未解决依赖留到后轮；事实由 agent 查，决定交给用户 | [底层 L6–30](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/productivity/grilling/SKILL.md#L6-L30>)；一手源码直接 |
| 本机 `grilling` | 与上述当前作者底层基本一致，但本机缺作者 L24 的 “Word each question so ‘yes’ accepts your recommended answer.”；不能宣称字节相同或已核准安装来源 | [本机 L6–28](</Users/bowhead/.agents/skills/grilling/SKILL.md#L6-L28>) 与 [作者 L24](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/productivity/grilling/SKILL.md#L24>)；直接对读 |
| 历史 `grill-me` | 历史版本明确“一次一个问题”；沿树逐枝解决依赖、每问给推荐、能查代码库就查代码库 | [历史 commit L6–10](<https://github.com/mattpocock/skills/blob/e74f0061bb67222181640effa98c675bdb2fdaa7/skills/productivity/grill-me/SKILL.md#L6-L10>)；一手源码直接 |
| `grill-with-docs` | 当前作者说明称同一底层访谈，但对齐代码库并记录术语／ADR；这是相邻有状态入口，不能把其落盘行为归给无状态 `grill-me` | [作者说明 L13–17、70–76](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/docs/productivity/grill-me.md#L13-L76>)；作者说明直接，本轮未完整审读其实现 |

**讲法约束：**可以说“沿关键决定逐枝追问”；若讲“一次一问”，必须注明采用历史版本或教学选择。当前作者默认是按轮问 frontier，且允许用户改成一次一问。**强度：一手直接＋教学措辞建议。** [作者说明 L42、54–59](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/docs/productivity/grill-me.md#L42-L59>)。

## 3. 需求怎样形成：源主张与教学转译

| 源主张 | 对该听众的转译 | 来源与强度 |
|---|---|---|
| 每个决定连着依赖它的后续决定；本轮只能问前置已定的问题 | 先确定“给谁用、交什么”，再问价格规则、缺数据时怎么办；别在交付用途未定时先设计发送渠道 | [grilling L6–8、26](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/productivity/grilling/SKILL.md#L6-L26>)；前半一手机制，例子为教学合成 |
| 可从环境查的事实由 agent 找；用户作决定 | 现行价目表在哪、已有接口做什么先查；“是否允许自动发给客户”由授权者定；查不到必须标未知，不能悄悄填默认 | [grilling L28](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/productivity/grilling/SKILL.md#L28>)；事实／决定分工为一手，查不到的处置为教学转译 |
| 每问给推荐答案；用户拥有 scope，不能连说 agreed | 给“建议做销售复核草稿，避免错误直接外发；代价是保留一次人审”，要求人说明接受或改变理由 | [grilling L8](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/productivity/grilling/SKILL.md#L8>)、[作者说明 L23–27](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/docs/productivity/grill-me.md#L23-L27>)；一手支持给推荐与主动参与，“代价”是教学增强 |
| frontier 为空、每枝访问、没有未说出的假设；人确认共同理解后才行动 | 当前范围的结果、关键规则、边界、未知去向能够复述并确认即可转下一步；不把整个业务所有未来细节列成无限问卷 | [grilling L30](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/productivity/grilling/SKILL.md#L30>)、[作者说明 L48–52](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/docs/productivity/grill-me.md#L48-L52>)；一手收口条件，限定“当前范围”为教学转译 |
| 对话不能回答所有问题；不可 grill 的问题应做原型 | “这个复核过程顺不顺手”拿一个可操作样例试；“客户是否因此更愿意购买”留待真实业务观察；未知不靠重复问句消失 | [作者说明 L31–37、61–62](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/docs/productivity/grill-me.md#L31-L62>)、[Yeret L30–36](</Users/bowhead/ai_dev_sdlc_aidc/02_research/01_agent_engineering/goal_eval_engineering/raw/evidence-2026-09-27-c-hard.md#L30-L36>)；一手建议（Yeret 为仓库既有摘录），例子为转译 |

**不能以问句数量证明需求质量。** 作者直接警告：40 次被动认同会产生更确定的假象；200 个问题通常是范围过大，也可能进入上下文质量下降区域；质量取决于回答质量。103 若采用时间盒／轮数上限，这是教学治理建议，不是作者规定的固定数字。**强度：作者说明直接，时间盒为转译。** [作者说明 L25–29、48–52](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/docs/productivity/grill-me.md#L25-L52>)。

## 4. 仓库需求方法：只取承重部分

需求实践入口明确：`raw_dr` 是原始材料；`deep_research_topics` 是消化与证据层；`final` 是交付消化稿，断言强度以研究层为准。本研究因此直接读其原始方法来源摘录，不拿最终教学稿反证作者。**强度：仓库分工直接。** [需求入口 L6–13](</Users/bowhead/ai_dev_sdlc_aidc/03_practice/requirements_engineering/README.md#L6-L13>)。

| 方法 | 可用于 103 的最小主张 | 来源与强度／限制 |
|---|---|---|
| User Story／3C | 一句“谁要什么、为什么”只开出对话；Conversation 与 Confirmation 分开，验收不是聊完自动附带 | [Cohn 来源卡 L16–29、45–53](</Users/bowhead/ai_dev_sdlc_aidc/03_practice/requirements_engineering/deep_research_topics/_reference/00-shared-cohn-user-stories-primer.md#L16-L53>)；[作者站](<https://www.mountaingoatsoftware.com/agile/user-stories>)。仓库既有一手摘录，非本轮网页复验；3C 原创归 Ron Jeffries，不能归 Cohn |
| EARS | 用前置条件、触发、系统、响应把一句规则约束清楚；异常行为同样要写 | [Mavin 作者指南摘录 L38–65](</Users/bowhead/ai_dev_sdlc_aidc/03_practice/requirements_engineering/deep_research_topics/_reference/00-shared-mavin-2009-ears-re09.md#L38-L65>)；[作者站](<https://alistairmavin.com/ears/>)。仓库既有一手摘录；轻量语法不自证可执行验收，不可宣称与 Gherkin 无损同构（同卡 L103–108） |
| Example Mapping | 把 story、规则、具体例子、未决问题分开；先发现，再表达，再自动化 | [Cucumber 来源卡 L17–30、43–58](</Users/bowhead/ai_dev_sdlc_aidc/03_practice/requirements_engineering/deep_research_topics/_reference/05-integration-bdd-cucumber-discovery-formulation-case.md#L17-L58>)；[官方方法](<https://cucumber.io/docs/bdd/example-mapping/>)。仓库既有官方摘录，非本轮复验；不以案例改善数字承诺本场效果 |
| Given／When／Then | 已知状态 → 一个动作 → 可观察结果；Then 对输出判定，而非钻入数据库内部 | [官方 Gherkin 摘录 L27–31、48–58](</Users/bowhead/ai_dev_sdlc_aidc/03_practice/requirements_engineering/deep_research_topics/_reference/00-shared-gherkin-official-reference.md#L27-L58>)；[官方参考](<https://cucumber.io/docs/gherkin/reference/>)。仓库既有官方摘录；“技术一般的人先用中文三句写例子”是教学转译，不要求安装 Cucumber |

以上三种写法分工可互补，但不把“模板填齐”当需求真实完整。其不同层次有源头可核：用户意图／对话、一般行为规则、具体可判例子。**强度：跨源综合；不是任何单个作者提出的统一体系。** 来源即本节表各行。

## 5. 作者相邻测试思想：验收需要补什么

- **测试决定要显式形成。** 当前 `to-spec` 从既有对话综合规格，不再访谈；先提出测试 seam 并向用户确认，规格另列 Testing Decisions 和 Out of Scope。这证明作者本人没有让 grilling 包办全部测试设计。**强度：一手源码直接；不代表本场获准发布 issue。** [to-spec L7、13–19、59–69](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/to-spec/SKILL.md#L7-L69>)。
- **观察行为，不观察实现步骤。** 当前 TDD 主张只在预先确认的公共边界测试；每个边界说明能抓什么、漏什么。对听众可译成“客户或销售能看到的输出是什么；这个检查只证明哪一段”。**强度：一手机制直接＋教学转译。** [TDD L14–24](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/tdd/SKILL.md#L14-L24>)。
- **预期必须有独立依据。** 作者把按实现同样算法重算 expected 的测试列为 tautological；预期要来自可信常量、手算样例或 spec。对听众可译成“别让生成答案的人再按同一猜测给自己打分；先由业务规则／已确认例子定答案”。**强度：一手直接＋教学转译；不推出一切 AI 评审无用。** [TDD L30–32](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/tdd/SKILL.md#L30-L32>)、[测试例 L63–76](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/tdd/tests.md#L63-L76>)。
- **逐条验证可帮助发现遗漏。** TDD 当前是一条测试→一条最小实现，先红后绿；反对把所有想象中的测试写完再实现。对听众的重点是先拿一个代表性例子打通要求、输出、证据，再扩大样本；不要讲编码仪式。**强度：一手机制＋教学转译。** [TDD L32–38](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/tdd/SKILL.md#L32-L38>)。

## 6. Goal／Eval：面向业务人的验收尺度

研究入口定调：goal 描述怎样算达成，eval 判断产物是否达到；否决权在干活的一方之外；重心是可对照完成条件；难设计也必须研究。CURRENT 则明确：步骤执行可以是合法目标，但不能替代隐藏需求验收；难判时有界探索、切片验收或外部结果观察。**强度：仓库本层定调／判读，不冒充所有作者共识。** [README §1 L25–39](</Users/bowhead/ai_dev_sdlc_aidc/02_research/01_agent_engineering/goal_eval_engineering/README.md#L25-L39>)、[CURRENT L3–7](</Users/bowhead/ai_dev_sdlc_aidc/02_research/01_agent_engineering/goal_eval_engineering/CURRENT.md#L3-L7>)。

| 验收问题 | 可用来源主张 | 教学转译及边界 |
|---|---|---|
| “完成了”凭什么？ | Claude 官方：可核终态、已陈述检查、重要约束；裁判只看工作模型已在对话中展示的证据，不独立读文件执行命令 | 写明证据出现在哪里，别只说“检查通过”；“另一个 AI 说达到”仍取决于它看见什么。来源：[既有官方摘录 L15–22](</Users/bowhead/ai_dev_sdlc_aidc/02_research/01_agent_engineering/goal_eval_engineering/raw/evidence-2026-09-27-a-goal-frontier.md#L15-L22>)、[官方页面](<https://code.claude.com/docs/en/goal>)；仓库一手留存，本轮未复验产品现况 |
| 一整份看不过来？ | Hamel 四问：核什么、比什么可信对象、专家怎么看、哪些小块可接受／修改／拒绝 | 先切成“价格引用、金额、缺失项提示、发送边界”等可独立打回的小块。来源：[档案 L13–22](</Users/bowhead/ai_dev_sdlc_aidc/02_research/01_agent_engineering/goal_eval_engineering/raw/evidence-2026-09-27-c-hard.md#L13-L22>)、[作者原文](<https://hamel.dev/blog/posts/eval-smell>)；作者设计草图，无上线效果数据 |
| 什么算好还不确定？ | Shankar：人标失败类型，agent 把已定义类型扩到更多 trace；好坏标准藏在人脑中 | 业务人先看实际输入输出，标“哪一句为何不可接受”，再把标注变成规则；不要先凑一条通用准确率。来源：[档案 L18–46](</Users/bowhead/ai_dev_sdlc_aidc/02_research/01_agent_engineering/goal_eval_engineering/raw/evidence-2026-09-27-a5-shankar-talk.md#L18-L46>)、[本人演讲](<https://www.youtube.com/watch?v=tqUDjc1HzO4>)；既有口播摘录，非本轮复听 |
| “提升成交”怎么验？ | Yeret：先区分 output 与 outcome；系统外业务结果看不见时，人保留责任并补观察 | 验收“生成可复核报价草稿”不等于验收“成交上升”；先定可看见的产出，再另观察结果。来源：[档案 L30–36](</Users/bowhead/ai_dev_sdlc_aidc/02_research/01_agent_engineering/goal_eval_engineering/raw/evidence-2026-09-27-c-hard.md#L30-L36>)、[作者原文](<https://yuvalyeret.com/blog/ai-agent-completion-goals-aim-at-outcomes>)；作者观察，日期窗边，无频率／因果测量 |

### 可教的最小验收卡（教学转译，未运行）

五问是：检查什么；用什么输入与可信参照；预期可观察表现是什么；实际证据是什么；由谁接受或打回。103 的已填报价样本与证据表统一维护在 [案例 §四](<../01_storyline/02-case-walkthrough.md#四验收不是一句测试全绿>)，不在证据层另设一份价目或预期答案。

此卡的设计是把 Cucumber 可观察结果、Matt 的独立 expected、Hamel 的小块核对与 Yeret 的产出边界转成业务语言，**不归名为 Grill-me 原生模板**。用反例检查检查本身、同时用正常例防误伤，是本场建议；它与 TDD 先见失败的思想一致，但本轮没有回源到作者完整的 grader 校准体系。**强度：跨源教学综合，未实测。** 对应来源：[Gherkin 输出语义](</Users/bowhead/ai_dev_sdlc_aidc/03_practice/requirements_engineering/deep_research_topics/_reference/00-shared-gherkin-official-reference.md#L27-L31>)、[TDD 反模式及规则](<https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/tdd/SKILL.md#L30-L37>)、本节前表。

## 7. 研究边界与缺口

- **强度定义：**“一手源码直接”证明作者指令／机制存在；“作者说明直接”证明作者提出这种做法；“仓库既有一手摘录”说明本轮读取带 URL 的留存原文，但没有重新网页主验；“仓库判读”是本仓库综合；“教学转译”是103建议。以上均不自动证明结果改善，也不等于普遍标准。
- `web_fetch` 对 GitHub／作者 EARS 站返回非公网 IP 解析错误；作者 GitHub 材料经 HTTPS `curl`／Python 读取全文并固定 commit。所查 `write-a-prd` 当前路径 404，转读当前确存的 `to-spec`，未把二者当成同一技能。需求方法与 Goal/Eval 非 Matt 来源主要用仓库既有带引文档案，保留原核验日期，不冒充本轮网页复验。
- 已核准当前与历史版本差异，但**未查出本机安装 commit／完整变更时间线**；本机少一句措辞，不影响已核思想，却不能声称它就是固定 commit 的完整副本。
- **没有用户原先所称 GILL-ME 的直接链接。** 名称映射仍为高可信推定，正式对外署名可用“Matt Pocock 的 grill-me”，并在内容反馈时确认所指。
- **没有证明 grilling 会自动产出需求文档、覆盖所有重要需求或验收标准。** 当前作者文档明确其无状态；需要另行把决定、未知、范围与测试决定落入现行工作依据。具体由哪个文件承接是本场治理设计，不来自本 skill。
- **没有本场合成案例的运行证据，也没有 Matt 面向“业务熟、技术一般”听众的效果实验。** 适配建议应经过该受众试讲或真实任务检验。
- 本轮不扩展多 Agent 拓扑、评测产品排名、全套治理制度。103 可用本研究支撑“需求→可判例子→验收证据”的桥；权限执行点、变更重验与旧规则退出的承重一手来源仍由治理证据另补。
