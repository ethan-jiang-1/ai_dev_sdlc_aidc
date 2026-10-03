# _raw_orgs — 影响 AI Coding 话语的组织卡

> 机构作为"发声体"的立场与言论：技术雷达、工程博客、官方研究、公司级宣言。
> 人物卡在 [`../_raw_people/`](../_raw_people/README.md)；厂商的产品/方法论材料在 [`../../corp/`](../../corp/README.md)。
> **收录原则（2026-10-03 用户定）**：只留**塑造 AI Coding 话语的 top 组织**，不做当量组织全量档案——被 AI 淘汰的当事人、产品利益喉舌、纯评论者不入卡位（评估过的次级组织压入下方「收档表」，一行一信号）。

## 定位与分工边界（三问三答）

| 问题 | 边界 |
|---|---|
| **组织卡 vs 人物卡**（`../_raw_people/`） | **署名主体**：机构署名 → 本库；个人署名 → 人物卡。机构×个人可以**双卡位并存**（例：37signals 官宣 pencils down 是组织卡素材，DHH 的 Lex 访谈是人物卡素材；LangChain 官方四环模型是组织卡，Sydney Runkle 个人言论走人物/台账判定） |
| **组织卡 vs corp**（`../../corp/`） | corp 收"**厂商材料**"——他们怎么做/卖什么（AWS AI-DLC 方法论、生态全景）；本库收"**机构作为思想者的立场言论**"——他们主张什么（雷达主题、公司级判断、工程博客的判断性输出）。同一机构可双卡位（AWS 方法论在 corp，若其雷达/博客有立场性主张可在此开卡） |
| **组织卡 vs 事件库**（`../_raw_event_*/`） | 单次活动（峰会/retreat）→ 事件库；机构的持续立场 → 本库。FOSE retreat 是 TW 主办的活动（事件库），TW 的雷达与技术主张是持续立场（本库） |
| **Google 卡内的 DORA 节** | DORA 是 Google Cloud 旗下 program（dora.dev 页脚口径），研究谱系（2012 起、TW 血统）独立但归属在同一集团——**立场线并入 [`google.md`](google.md) 的 DORA 节，不单独开卡**（2026-10-03 收档定调） |

## 入册判据（2026-10-03 挖掘批按此执行；同日加严）

1. **机构署名的官方输出**：技术雷达、工程博客、官方论文、公司级宣言（机构渠道＋机构系列＝机构署名；个人执笔须标注）；
2. **有立场性主张**：是"他们主张什么"，不是产品说明书或 changelog（产品口径重的条目降权收录并标注）；
3. **2026 时间窗 + 来源铁律**：同 [`../README.md`](../README.md) 的来源/时间铁律（2026-01 硬底线，一手英文源，逐条回源核验）；
4. **持续发声**：一次性新闻稿不够格，至少有跨时间的立场轨迹可追（年内跨时间 ≥2 次，或年度机构系列在窗一期）；
5. **话语塑造力（2026-10-03 新增，top 收录的门槛）**：该组织的立场是否**改变别人怎么做**——被淘汰的当事人（如 SO）、产品护城河喉舌、纯评论者不占卡位。

## 卡片结构

沿用人物卡标准件：frontmatter（org / source_urls / key_concepts）→ 当前立场小结 → **思想变迁轨迹（2026）表 + 判语** → 专题节 → Source 尾链。

## 现有卡（6 张，2026-10-03 收束后）

**基准卡**：

- [`thoughtworks.md`](thoughtworks.md) —— 技术雷达 Vol 34（"拐点"定调、认知债、harness 学科化背书）；本库的当量参照系。

**平台/基建编纂谱系**（用产品默认值定义"好的开发方式"）：

- [`google.md`](google.md) —— 工程化收口派：SRE AI 白皮书、DORA ROI＋amplifier 论（并入卡内）、harness 工程正名（Lopopolo coinage 官方归名）、「从写到审」。
- [`microsoft_github.md`](microsoft_github.md) —— 生态卡：GitHub（Continuous AI、cost of saying yes、80 万行 Rust 旗舰、harness 产品化收编）＋微软（Customer Zero「软件工厂→agent 工厂」、24% PR 研究、oversight 四分类）。

**产品公司自证谱系**（"做给你看再写下来"，决策即话语）：

- [`37signals.md`](37signals.md) —— Rails World 2026 keynote "pencils down on hand-written code" 公司级断代宣言＋REWORK 全年线。
- [`shopify.md`](shopify.md) —— back to native（agent 成本曲线推翻 2020 年 RN 全押）、harness>model、River（1/8 PR coauthored）、Helix checkpoint 循环。
- [`stripe.md`](stripe.md) —— hard/soft steering 设计轴（loop 台账在引）、Minions 周千级无人值守 PR、100% accuracy benchmark。

## 当量对标 ThoughtWorks——挖掘结果（2026-10-03）

**问题**：TW 是软件研发史上影响当量很大的组织，有没有同等当量的组织？它们 2026 年以后的影响是什么？

**当量的四维标尺**（TW 基准）：A. 正典输出（Refactoring / Continuous Delivery——Humble/Farley 均出自 TW）；B. 实践采纳（XP/Agile 咨询交付、CI/CD 普及）；C. 机构化发声（Tech Radar 双年刊）；D. 2026 仍在发声（Vol 34＋harness 学科化背书）。

| 分组 | 组织 | 结论 |
|---|---|---|
| **当量高＋2026 有声＋话语塑造力强**（6 家开卡） | ThoughtWorks、Google（含 DORA）、Microsoft+GitHub、37signals、Shopify、Stripe | 现有 6 卡。平台编纂（把 agent 编排进原语）与产品自证（用决策演示）两种形态；与 TW 的分野：TW 收紧（经典实践是制衡力量），平台派吸收（把 agent 装进既有原语） |
| **当量高＋2026 有声＋话语塑造力次级**（7 家收档，见下表） | JetBrains、Stack Overflow、Atlassian、GitLab、Spotify、O'Reilly、（DORA→已并入 Google 卡） | 全部通过 4 条旧判据，但按判据 #5 收档：数据权威非立场权威／被 AI 淘汰的当事人／产品喉舌／体量声量次级／评论者非实践者 |
| **当量高＋2026 无声** | **Pivotal Labs**（exclude：labs.pivot.al 站点已死、tanzu labs 页 404——XP 咨询双雄仅 TW 存活到 2026 并发声）；**Netflix**（watch：官方渠道全年 20+ 篇零 SDLC 立场输出、culture memo 无 2026 更新；QCon SF 2026-11-18 "How Netflix Retrofitted Its SDLC for AI Coding Agents" 开讲后复查）；**IBM/Rational**（watch：RUP 谱系遗产，有一篇真方法论文 Radical AD 2026-07-07） | 谱系存亡本身是发现：咨询谱系死了只剩 TW；文化输出谱系（Netflix）选择了沉默 |
| **新生当量**（无历史纵深、话语场现役） | Anthropic、OpenAI、LangChain、Cursor/Anysphere、Cognition、Sourcegraph/Amp | 2026 影响力大但属另一个轴——AI 时代话语的**发起者**而非历史实践权威的**继承者**（见候选清单 A/B） |

## 收档表（次级组织——已评估、不开卡，一行一信号，2026-10-03）

> 2026-10-03 挖掘批的完整评估（历史当量、判据核验、逐条证据）曾成卡后按收录原则收束；此表保留各家**最强单条信号**与主 URL，供回查与再评估。若后续某家话语塑造力升级（出现被广泛引用的立场转向），可凭此表重启开卡。

| 组织 | 收档理由 | 最强单条信号（主 URL） |
|---|---|---|
| **JetBrains** | 数据权威非立场权威（与 IDE 存亡题绑定） | DES 2026：90% 开发者周用 agent、~47% 代码全由 agent 写（[blog.jetbrains.com，2026-08-18](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/)）——年度采用数据锚 |
| **Stack Overflow** | **被 AI 淘汰的当事人**：知识入口已被 agent 替代，发声多为存亡自辩 | 信任缺口：79% 用 AI 但仅 29% 信任（[stackoverflow.blog，2026-02-18](https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/)）；"human review remains the gold standard"（05-27） |
| **Atlassian** | 产品护城河喉舌（叙事服务 Jira/Rovo） | Agentic Pivot：88% 需要 vs 19% 已建 governed system of work（[atlassian.com，2026-09-03](https://www.atlassian.com/blog/company-news/the-agentic-pivot)） |
| **GitLab** | 体量与声量次级 | CEO 论纲 "Producing code is getting cheap. Trusting it is not."（[about.gitlab.com，2026-08-24](https://about.gitlab.com/blog/when-code-is-abundant/)，直接回应 Anthropic playbook）；handbook "Fix the environment, not the prompt"（[handbook，2026-03-27](https://handbook.gitlab.com/handbook/engineering/workflow/ai-assisted-development/)） |
| **Spotify** | 实证质量高但声量次级 | SVP 旗舰："AI increased the capacity to produce change. The next constraint became our ability to verify it."＋事故复盘未见 AI 代码为主要致因（[engineering.atspotify.com，2026-09-16](https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity)） |
| **O'Reilly** | 评论者非实践者 | "2026 is shaping up to be a return to discipline."（[oreilly.com/radar，2026-07-27](https://www.oreilly.com/radar/ai-demands-more-engineering-discipline-not-less/)，经 Wayback 核验） |

## 候选评估清单

**A. 已有库内素材、话语场现役（新生当量，待开卡）**：

| 组织 | 库内素材位置 | 意见面主张（开卡理由） |
|---|---|---|
| **Anthropic** | loop 台账 §A `anthropic_org`（evidence-b/c 全文） | 官方 loop 原语（`/goal` 三值判定、auto mode 熔断）、AI-Native SDLC playbook（GitLab CEO 已公开回应它）、Applied AI |
| **OpenAI** | loop 台账 §B 机构条目（auto-review "separation of roles matters"）＋ `09` 卡 | harness engineering 官方文、auto-review 论文 |
| **LangChain** | loop 台账 §A（Sydney Runkle 条目背后） | 四环模型官方文 |
| ~~Google Cloud~~ | `09` 卡（GC 官方博客 09-25） | **已开卡**（并入 [`google.md`](google.md)，含 Agent Factory 锚点） |

**B. 话语场高影响**：

| 组织 | 信号 | 状态（2026-10-03） |
|---|---|---|
| **AWS** | 意见面证据已备：Vogels《A return to two-pizza culture》（2026-06-30，allthingsdistributed——CTO 个人渠道注记）公开修订 Working Backwards 20 年流程（原型先行取代 PR/FAQ 先行）；Swami《How frontier teams are reinventing AI-native development》（2026-06-10，官方 Thought Leadership 标签）有真判断但立场营销混合 | **ready-to-card，切磋中**：corp 已有方法论卡，是否补意见面双卡位——按判据 #5（话语塑造力）严审中 |
| **Meta** | Orosz 06-17 批判的对象兼发声者 | 未深挖：组织行为本身成为话语事件，非编辑性发声 |
| **Sourcegraph/Amp** | orbs / dial / "Steer, Don't Queue" 产品词汇 | 未深挖：与 `19` Thorsten 卡分工 |
| **Cognition** | 《Don't Build Multi-Agents》反并行论（台账 §B 已有） | 未深挖 |
| **Cursor/Anysphere** | IDE 叙事中心 | 未深挖：产品口径为主 |

**C. 当量轴排除/观察（2026-10-03 挖掘结果）**：

| 组织 | 结论 | 依据 |
|---|---|---|
| **Pivotal Labs** | **exclude** | 站点已死（labs.pivot.al SSL 失败）、tanzu labs 页 404、Tanzu blog 纯产品营销——XP 咨询谱系仅 TW 存活发声 |
| **Netflix** | **watch**（2026-11-18 回查点） | 官方渠道窗口内零 SDLC 立场输出；QCon talk abstract 立场极强（"The codebase is now the agent's runtime."）——开讲后复查 |
| **McKinsey** | **watch**（不可核验） | 《The state of AI in 2026》等候选存在，但 mckinsey.com 网络不可达＋Wayback 全 403，按来源铁律不作证据 |
| **IBM** | **watch** | 《Radical application development》（2026-07-07）为真方法论立场文；若 Q4 有后续或被业界引用可升 ready-to-card |

**D. 勘误登记（本库旧条目修正）**：

- ~~「Shopify 生产事故回溯研究：agent 评审的 PR 出更少事故」~~——**核不到**：shopify.engineering 2026 年全部 25 篇 sitemap 无此文；最接近的真实对应物是 agentic harness 文（**安全**发现回溯）与 Helix 对抗性评审闭环。疑为第三方转述（BI 对 Tobi 访谈的报道）误记。已撤销，[`shopify.md`](shopify.md) 卡内有完整勘误记录。

**E. 待切磋的原则问题**：

1. 机构×个人双卡位的判定（署名主体）——37signals/DHH、GC/Lopopolo 两对已按「组织卡只收机构署名输出」落卡。
2. corp×orgs 双卡位（AWS 案例）＋判据 #5 的适用：意见面证据已备但话语塑造力存疑（立场营销混合）——**是否开卡由用户裁决**。
3. loop 台账的 `anthropic_org` 行与本库 Anthropic 卡的关系（台账管 loop 主题名单，org 卡管全景立场——素材引用不复制）。
4. 收档表的再评估触发：以「被广泛引用的立场转向」为信号（如 SO 若转型成功、JetBrains 若出立场级转向文）。

**跨卡关键发现**（判读归研究层，此处只登记指针）：①「harness」一词的四家收编路径——TW 学科化 / GitHub 产品化（Copilot=harness）/ Google 正史化（官方归名 Lopopolo）/ Shopify 资产化（harness>model、可审计）；②「AI 生产力」三角纠偏——TW 认知债 / DORA 放大器＋J 曲线（google 卡内） / O'Reilly 纪律回归（收档表）——对冲厂商 4.5x 类数字；③ 组织署名的「agent 产出占比」三家样本——Stripe Minions（周千级 PR）/ Shopify River（1/8 PR）/ GitHub Toub（80 万行 Rust）。

## 待回查日历（2026-10-03 登记的窗口内未出件）

| 时间 | 事件 | 关联卡 |
|---|---|---|
| 2026-10-20 | SRE 书第 2 版发行（O'Reilly，794 页）——若含 AI 章则补为 SRE 书系 2026 续作 | `google.md` |
| 2026-10 月底–11 月 | Octoverse 2026 年度头条 | `microsoft_github.md` |
| 2026-10-28/29 | GitHub Universe 2026（Fort Mason）keynote 方法论主张 | `microsoft_github.md` |
| 2026-09–11（惯例） | DORA 2026 年度 Report | `google.md` DORA 节 |
| 2026-11-18 | QCon SF「How Netflix Retrofitted Its SDLC for AI Coding Agents」开讲 | Netflix watch |
| 随时 | TW Radar Vol 35（2026-10-03 核验未出） | `thoughtworks.md` |

---

**最后更新**：2026-10-03（深夜·二）：**收束为 top 卡位（13 → 6 张）**——按用户定调「只留塑造话语的 top 组织」新增判据 #5（话语塑造力），7 家次级组织收档：Stack Overflow（被 AI 淘汰的当事人）、JetBrains（数据权威非立场权威）、Atlassian（产品护城河喉舌）、GitLab、Spotify（体量声量次级）、O'Reilly（评论者非实践者）压入收档表（一行一信号＋主 URL），DORA 立场线并入 `google.md` DORA 节（amplifier 论、反 tokenmaxxing、2026 年报回查点）；待回查日历同步收窄。当量对标评估框架与负发现（Pivotal 消亡、Netflix 失声）保留。

- 2026-10-03（深夜）：**当量对标挖掘批**——以「TW 同当量组织是否存在、其 2026+ 影响是什么」为题，6 路并行回源（约 80 个一手页面逐条核验），新增 12 张组织卡（google / microsoft_github / 37signals / shopify / spotify / stripe / gitlab / atlassian / jetbrains / stack_overflow / dora / oreilly）；新增「当量对标」评估节与待回查日历；候选清单勘误一条（Shopify 事故研究核不到）；AWS 意见面证据备齐待用户裁决、Pivotal exclude、Netflix/McKinsey/IBM watch。评估底稿 `.tmp-*` 已清理。
- 2026-10-03：建库（架子）；ThoughtWorks 卡自 `_raw_kol/01` 迁入；候选清单为切磋底稿。
