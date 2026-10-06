# KOL 台账 — Loop Engineering（2026-06 起）

> ★ **本文件是本主题「谁在说」的唯一名单权威。** 收录判据见 [`../README.md`](../README.md) §1；
> 一手素材统一在 [`01_seed_reference/loop_engineering/`](../../../../01_seed_reference/loop_engineering/README.md)
> （本文件**只放台账与指针，不放人物卡片**）。

**观测日期**：2026-09-26；**2026-09-27 I 路**追加谱系与候选注记；**2026-10-06 三派分野批**（用户定）：§A 9→14（+Orosz / swyx / Yegge / Kent C. Dodds / Cursor），三派判定权威见 §A2，三路深扫档案按用户指示落种子层 [`01_seed_reference/loop_engineering/`](../../../../01_seed_reference/loop_engineering/README.md)；**2026-10-06 第二轮补抓**：§A +1（**Laurie Voss**，两个一手载体齐）、Farley 入 §C1（转写级）、Searls 身份坐实（Doc Searls）但两句仍零命中——补抓档案见种子层三派目录 raw_scan 文末增量节。三路回源见 [evidence-a](evidence-2026-09-26-a-originators.md) / [evidence-b](evidence-2026-09-26-b-stop-and-scheduling.md) / [evidence-c](evidence-2026-09-26-c-autonomy-and-convergence.md)。簇外高影响面见 [evidence-i](evidence-2026-09-27-i-high-influence-control.md)；I2 档案混合主验与侦察回源，侦察条目不计票。**「待回源」= 不可作主张依据。**

> ⚠️ **质量门槛（2026-09-26 用户定，先于本表的一切口径）**：只收真正有影响力的 KOL，
> 且内容必须有深度（操作性洞察）。**论坛评论者不算 KOL、聚合媒体与标题党不入册、碎片推文不作深度证据**——
> 完整判据见 [`../README.md`](../README.md) §1「硬性排除」。

---

## §A 入册名单（2026-06 起对本主题有公开发声，且号召力口径至少满足一条）

| slug | 人物 | 身份 | 号召力口径 | 主张一句话 | 证据强度 | 卡片状态 |
|---|---|---|---|---|---|---|
| `andrew_ng` | **Andrew Ng** | DeepLearning.AI 创始人 / *The Batch* 作者 | ① 术语定义者 | 三环嵌套（agentic coding / developer feedback / external feedback），外环修正内环方向；人类的价值是**上下文优势**而非"品味" | **一手**（X post 已归档） | ✅ 四件套齐 |
| `anthropic_org` | **Anthropic** | 厂商官方（Claude Code / 工程博客 / Applied AI） | ① 术语定义者 + ③ 一线规模 | loop 原语的**最完整厂商落地**：`/goal`（条件驱动，三值判定）· `/loop`（时间驱动，7 天硬过期）· auto mode（deny-and-continue + 3/20 熔断）· feature_list.json · AI-Native SDLC playbook（工件触发 loop + σ 分层自主度）· Managed Agents（外层接口化） | **一手**（evidence-b/c 全文已归档） | ✅ 素材在 [`raw/evidence-*.md`](.) 与 [`02_research/02_ai_sdlc/02_industry_playbooks/anthropic/`](../../../../02_research/02_ai_sdlc/02_industry_playbooks/anthropic/README.md)（既有主题，只引用不复制） |
| `sydney_runkle` | **Sydney Runkle**（LangChain） | LangChain 工程团队 | ① 术语定义者 | **四环模型**（agent / verification / event-driven / hill-climbing）——"loop engineering" 一词的厂商级体系化定义；grader 分 deterministic 与 agentic 两类；hill-climbing 环"改写 harness 本身" | **一手**（2026-06-16 全文已归档，evidence-b §4e） | ✅ 已回源（素材在 evidence-b §4e——**回源档案为常态形态，不建卡**） |
| `addy_osmani` | **Addy Osmani** | Anthropic（Claude Code 团队 MTS；此前 14 年 Google，最高任 Google Cloud AI Director——一手 bio，evidence-a/c） | ① 术语定义者（**本词的命名者**） | **两篇一手全取得**：命名篇 2026-06-07《Loop Engineering》＋操作篇 2026-08-14《Practical Loop Engineering》。**定义**：替代人逐轮提示；分层实为**四级运行模式**（agentic loop → `/goal` → `/loop`/`schedule` → proactive 事件触发无人值守）。**建议**：五件套＋memory spine、`/loop`/`/goal`/`/schedule` 组合、verification skill、最简方案优先。**个人观察**：约 5–10 agents/日、通常最多约 5 个并发，review bandwidth 是上限；敏感/复杂任务需密切观察。`/goal` 评估器只核 transcript 硬规则、不判内容好坏；不要把品味和判断委托给 agent（增量见 evidence-a 补充回源 D5–D10）。**2026-10-03 增量**：07-15→09-14 八篇把词表升级为 **loop → harness → factory**（outer loop 所有权 / verdict / light-dark factory / skill decay），见 [evidence-z](evidence-2026-10-03-z-osmani-increment.md) | **一手**（evidence-a + evidence-z） | ✅ 已回源（增量档案 evidence-z；个人卡评估中） |
| `boris_cherny` | **Boris Cherny** | Claude Code 创作者 | ① **词源**（2026-06-02 访谈句） | **词源是碎片级的**：名句 "My job is to write the loops" 逐字未核验（三个流传版本措辞不一致）；YC transcript（2026-02-17）里 "loop" 出现 **0 次**（他用 swarm / "Mama Claude" / spec+Asana 描述同一机制）；**无个人书面操作定义**（CC 团队 06-30 官方定义 ≠ 本人） | **部分一手**（evidence-a） | ✅ 定性完成：词源位记入时间线，**不建深度卡**（无深度内容可卡） |
| `peter_steinberger` | **Peter Steinberger** | OpenClaw 创作者；**2026-06 已入职 OpenAI**（AIEWF 报道，见种子层扫描档） | ① **词源**（2026-06-08 推文） | **词源是碎片级的，无深度内容**（A 路明确结论）：两句话推文（06-08 02:58 CST，正文未取得）；博客停在 2026-02-14。**重要 nuance**：其 2025-12-28 长文明确**反对自动编排**（"usually I'm the bottleneck"）——与 6 月推文立场相反。深度替代材料＝OpenClaw 官方 docs（standing orders / heartbeat / automation） | **部分一手**（evidence-a） | ✅ 定性完成：同上 |
| `geoffrey_huntley` | **Geoffrey Huntley** | 独立开发者（Ralph loop / repo-per-task） | ① 谱系源头新发声（§B→§A 触发条件满足，2026-10-03） | 纲领句 "**Software doesn't need to be readable by a human. It needs to be explainable to a human.**"；"economics can be cooked… haven't written code by hand for two years"；types as back pressure；软件工厂实践 | **一手**（ghuntley.com/readable 2026-10-02，curl 实取） | ✅ 卡片 [`_raw_people/16`](../../../../01_seed_reference/voices/_raw_people/16_geoffrey_huntley.md)；深挖进行中 |
| `armin_ronacher` | **Armin Ronacher** | Flask/Werkzeug 作者；Pi（earendil-works）协作者 | ③ 一线规模（2026-07→09 十篇连续发声）＋ **质量反证代表** | "AI engineering is **Neijuan (内卷)**"；Better Models: Worse Tools（SOTA 模型工具调用反而更差）；自己的软件工厂 35 小时白卷——"宽自主工厂叙事"的冷水面 | **一手**（lucumr.pocoo.org 两篇已核，十篇其余待补） | ✅ 卡片 [`_raw_people/17`](../../../../01_seed_reference/voices/_raw_people/17_armin_ronacher.md)；深挖进行中 |
| `thorsten_ball` | **Thorsten Ball** | Sourcegraph / Amp co-creator | ③ 一线规模（Amp 产品 + Register Spill 周更） | 机制本体最短表述（"an LLM, a loop, and enough tokens"）→ 2026-09 编排实录（**agent 派生 agent 黑盒测试**）+ "aim higher"——**宽自主乐观极** | **一手**（Register Spill #99 已核；#98/#100 待补） | ✅ 卡片 [`_raw_people/19`](../../../../01_seed_reference/voices/_raw_people/19_thorsten_ball.md)；深挖进行中 |
| `gergely_orosz` | **Gergely Orosz** | The Pragmatic Engineer 作者 | ④ 大分发＋② 被主流媒体/arXiv 引用＋③ 一线访谈规模（~210 条 loop 从业者调查回复） | **2026-07-14 专门发声《What is "loop engineering?"》**（副题即怀疑定调 "Is it a 'here today, gone tomorrow' trend?"）：多数 loop 用例是 cron/trigger 旧物；"Disappointment and 'tokenmaxxing'…loop engineering gets expensive fast"；除 AI 基建工程师外深入研究收益甚微。**引文纠偏**：其原句是 "something **valuable** is being taken away"（非 "precious"，01-07 grief 博客）。§1–4 一手已核、§5–7 付费墙（[种子层扫描档 S8](../../../../01_seed_reference/loop_engineering/03_skeptics/raw_scan_2026-10-06_skeptics.md)） | **一手**（截断） | ✅ 卡片 [`_raw_people/12`](../../../../01_seed_reference/voices/_raw_people/12_gergely_orosz.md)；派别：**中性偏怀疑**（§A2，07-14 回源后定派） |
| `swyx` | **swyx**（Latent Space 主理人） | Latent Space 主理人 | ① 造词者（loopcraft）＋② 被 LangChain 官方博客引用致谢 | loopcraft（2026-06-12）："One might argue the **entire game of the next century** is to be able to stack loops as effectively as possible"；"Salty Lesson for agents: Don't fix things yourself… focus on systems that scale with more agents"；"don't be salty when you lose"；**2026-06-30 AIEWF 开幕主台演讲即以 "Loopcraft" 为题**（[种子层扫描档 S5/§厂商面](../../../../01_seed_reference/loop_engineering/01_advocates/raw_scan_2026-10-06_advocates.md)）。⚠️ 原帖 404，经双镜像取得全文——**引用须标"经镜像"** | **一手·经镜像**（AIEWF 为笔录转述降半级） | ✅ 已回源（404 开放问题收口）；派别：**推动**（§A2，实测非中性） |
| `steve_yegge` | **Steve Yegge** | 40 年一线（Google/Sourcegraph）；Gas Town / Beads / Wyvern 作者 | ① 实践定义者（Gas Town/Beads 被 arXiv 2608.21884 引用）＋③ 一线规模（数十 agent 舰队、日均 175+ commits） | 2026-08《The Shape of Things to Come》：**极端多派内部证词**——Gas Town 被 Opus 4.7 "just two more things" tic 烧毁（循环不收敛）；Wyvern 月烧 ~69B token（等价 ~$87k）；"working on Wheelhouse itself occupies about **20-25% of all my Wyvern work**… roughly constant"；"Building large software remains hard. And it always will be."（[种子层扫描档 S10](../../../../01_seed_reference/loop_engineering/03_skeptics/raw_scan_2026-10-06_skeptics.md)） | **一手**（全文） | §B 升 §A（窗口内新发声，2026-10-06）；派别：**推动·激进多派**（含一手成本证词，§A2） |
| `kent_c_dodds` | **Kent C. Dodds**（⚠️ **不是 Kent Beck**，名字撞车） | 前端教育者（Epic React / Testing JavaScript 作者） | ③ 实践规模（自述 "hundreds of instances"）＋④ 大分发 | 2026-06-23 播客《Pragmatic Loop Engineering》：受约束循环画像——"the human does still need to be in the loop"、"**trading compute for attention**"、"use loop engineering **judiciously**"、"Good agents make code cheaper to generate and good loops make work cheaper to verify"；自认 "I was doing loop engineering before it had a name"（castro.fm transcript，[种子层扫描档 S6](../../../../01_seed_reference/loop_engineering/02_neutral/raw_scan_2026-10-06_neutral.md)） | **一手**（第三方转写） | 新入册（2026-10-06）；派别：**中性**（强票） |
| `cursor_org` | **Cursor**（厂商官方） | AI 代码编辑器厂商 | ① 厂商定义＋③ 一线规模 | 循环产品化第二家：2026-05-20 /loop skill（三种子条件）→ **2026-08-19 /goal 正式发布**＋官方教 /goal+/loop 组合＋愿景句 "without the need for intervention at each loop"（[种子层扫描档·厂商面](../../../../01_seed_reference/loop_engineering/01_advocates/raw_scan_2026-10-06_advocates.md)；evidence-u S4b 已有 /loop 前身） | **一手**（changelog 全文） | ✅ 已回源；派别：**推动·厂商**（§A2） |
| `laurie_voss` | **Laurie Voss** | npm 联合创始人；Arize Head of DevRel | ① 4+1 循环分类学提出者（被 ATO 官方教程文等独立复述）＋③ 一线规模 | **两个一手载体齐（2026-10-06 第二轮补抓）**：Arize《What is a loop in AI engineering, anyway?》（与 Aparna Dhinakaran 合署，全文）＋O'Reilly《What the Hell Is a Loop, Anyway?》（Wayback 全文，07-29）；分类学 execution / task / product / system ＋ **oversight loop——"where the human should live"**（治理翼：把人的监督位内置进循环分类学）；seldo.com《We are all Product Engineers now》（[种子层扫描档＋补抓增量 A/B](../../../../01_seed_reference/loop_engineering/01_advocates/raw_scan_2026-10-06_advocates.md)） | **一手**（全文×2） | ✅ §C1 升 §A（2026-10-06 第二轮）；派别：**推动·治理翼**（§A2） |

**降级出册（2026-09-26 C 路定性）**：

- ~~`alchaincyf`（花叔）~~ —— 《Loop Engineering 橙皮书》经 C 路核实为**英文谱系的中文转述/编译，非独立发明**（作者 README 明写 "based on Addy Osmani's founding post and the official Claude Code / Codex docs"）。按质量门槛**不入册**；保留一条价值：它是**术语在中文圈的传播载体**证据，登记在 [`00-timeline.md`](00-timeline.md) §一，不建卡片、不作引用源。

---

## §A2 三派分野（2026-10-06 用户定——**派别判定唯一权威**；同日三路深扫完成）

> 用户 2026-10-06 定的三派口径：**推动派（发起者＋吹捧者）／中性派／反对与怀疑派**。
> 判定依据是**对 loop engineering 实践的一手表态**（不是对 AI、不是对 agent、更不是对厂商的好恶）。
> 种子层 [`01_seed_reference/loop_engineering/`](../../../../01_seed_reference/loop_engineering/README.md) 的三派目录按本节组织素材；三路深扫档案（[推动](../../../../01_seed_reference/loop_engineering/01_advocates/raw_scan_2026-10-06_advocates.md) / [中性](../../../../01_seed_reference/loop_engineering/02_neutral/raw_scan_2026-10-06_neutral.md) / [反对](../../../../01_seed_reference/loop_engineering/03_skeptics/raw_scan_2026-10-06_skeptics.md)）按用户指示落种子层。
> **本节不因目录结构而改变 §A/§B/§C 的收录判定。**

**判定口径（一句话版）**：

| 派 | 判什么 | 典型话语形态 |
|---|---|---|
| **推动派** | 把"设计循环让 agent 自动推进"当**默认方向**推荐 | 下定义 / 出教程 / 做产品化 / 布道（含厂商营销与媒体吹捧） |
| **中性派** | 承认机制**有条件成立**，划适用边界 / 给约束形态 / 审慎实证 | "什么任务可以、什么任务不行"；"先测再信"；steering/constrained 形态 |
| **反对与怀疑派** | 给**反证或批评**（失败账本 / 质量退化 / 经济 / 人的角色），或反对把放权循环当默认 | 失败账本；质量与工具反证；"放权放大坏品味"；人的责任被抽空 |

**判派规则**：① 以**当前一手表态**为准，历史立场只作轨迹注记（反转样本：Steinberger、DHH——判派不抹平轨迹）；
② 派内允许 nuance（推动者自认边界照记）；③ 词源身份 ≠ 派别；④ **相邻位**（不对本词发声、但对同一实践域有强立场的 KOL）单列，不混入本词派别表；
⑤ ⚠️ **名字陷阱：Kent Beck ≠ Kent C. Dodds**（后者为 2026-10-06 新入册的中性派，前者窗口内沉默）。

### 推动（发起者＋吹捧者）——§A 11 条 + 相邻位

| 人物 | 派内角色 | 判定依据（一手锚点） |
|---|---|---|
| Addy Osmani | **发起者·命名者** | 2026-06-07 命名帖＋08-14 操作篇（evidence-a）；四级运行模式＋五件套教程化。**nuance**：自认 review-bandwidth 上限（~5–10 agents/日）与 skill decay（08-31） |
| Andrew Ng | 发起者·定义扩散 | 2026-06-30 三环模型（一手已归档） |
| Sydney Runkle（LangChain） | 发起者·体系化 | 2026-06-16 四环模型（evidence-b §4e） |
| Anthropic（Claude Code 团队） | 发起者·厂商落地 | /goal /loop auto mode＋AI-Native SDLC playbook（evidence-b/c） |
| Cursor（厂商） | 发起者·厂商产品化第二家 | 2026-05-20 /loop skill → **2026-08-19 /goal 正式发布**＋官方教 /goal+/loop 组合＋"without the need for intervention at each loop"（changelog 一手） |
| Boris Cherny | 发起者·词源（碎片级） | 词源身份成立（AIEWF 06-30 台上版见扫描档，可增补 evidence-a 对照表）；**nuance**：经 Willison 09-11 转引——"Production code written by Claude should have a higher bar than if it was written by a human" |
| Peter Steinberger | 发起者·词源（碎片级，**反转样本**） | 2026-06-08 词源推文；2025-12-28 曾明确反对自动编排；**2026-06 已入职 OpenAI**（AIEWF）＋六月后 "注意力是主挑战" 发言；07-18 "Are we still talking about loops, or have we moved on to graphs?"（2.6M views）文本经 36kr EN＋KuCoin 双独立转载锚定——**性质＝推动派内部换词表（loop→graph），非转反对**；X 原文仍缺（种子层 skeptics 档·补抓增量） |
| Thorsten Ball | 吹捧者·宽自主乐观极（实践者） | #98–100 "aim higher"、验证外包机器证明（`_raw_people/19`） |
| Geoffrey Huntley | 吹捧者·激进实干极（谱系源头） | "on the loop, not in the loop"（`_raw_people/16`）。**nuance（2026-07-24 起）**：加入 Antithesis 转向验证（"Creation is now near-free. Verification/understanding is not, yet"）；对 Ralph 自我祛魅（"it's just a loop"）；对 software-factory discourse 疏离（"strange"/"too fixated"）——目的激进＋路径审慎，判读层注意勿简单归档 |
| swyx | 吹捧者·概念造词（loopcraft） | "entire game of the next century"＋"Salty Lesson"＋AIEWF 主台演讲（经镜像，见 §A 行） |
| Steve Yegge | 吹捧者·激进多派（**含一手成本证词**） | Gas Town 舰队实践；同时公开 Gas Town 烧毁、69B token/月、harness 维护 20–25% 常量（见 §A 行） |

**吹捧层降级登记（2026-10-06 第二轮补抓后状态）**：**Karpathy**——升格：bearblog（04-30 讲座文本）＋autoresearch README 两个本人一手载体全文取得（"agents are like interns. You still have to be in charge of aesthetics, judgment, taste, and oversight"）；"remove yourself as the bottleneck" 原句仍仅存 swyx 转录。**Nadella**——部分解决：X 长文（06-14，28M 阅读）标题/日期坐实，全文经两条转译链取得（"This loop will become the new intellectual property of the enterprise"）——引句须标"经转译"。**Jensen Huang**——四路转引一致＋美联社专访线索，NVIDIA 一手仍开放。中文聚合的无名氏声称（"Anthropic 80% 工程师"）维持**不引用**。

**相邻位（不对本词发声）**：**DHH**——"agent-accelerated development"、37signals "pencils down"（2026-09-23，`_raw_people/15`），同时拒绝 "agentic engineering" 词汇；**Harrison Chase**（LangChain CEO）——"LLMs running in a loop calling tools… the core primitive"（专栏三篇一手），但词表为 harness/managed agents/learning loop，不用本词。

### 中性（边界与审慎）

| 人物 | 派内角色 | 判定依据 | 台账位置 |
|---|---|---|---|
| Gergely Orosz | 一线记录者·**调查式怀疑** | 07-14 专刊（cron 旧物判定、tokenmaxxing、"here today, gone tomorrow"），同时如实收录有效案例——不全面否定（扫描档 S8） | §A（2026-10-06 升） |
| Simon Willison | 循环实践者＋风险警告（**偏怀疑**） | 《Designing agentic loops》实践；2026-09-24 "make software engineering **even harder**… requires extraordinary discipline and knowledge"＋10-03 "hard budget caps need to be the default"；窗口内无本词专门发声（负结论复证） | §C1 |
| Birgitta Böckeler | **审慎实证（最强中性样本）** | 2026-08-10 自跑 eval 证伪"循环内 TDD 有益"默认信条（"I personally have stopped telling my coding agents to write tests first… until I see evals"，TDD 组 token 3–8.5x）＋SE Radio 730 裸基线先行（扫描档 S1/S2） | §B（窗口前）＋窗口内增量 |
| Kief Morris | 阶梯／渐进信任 | PlatformCon 2026-06-23 官方关键句 "As feedback loops tighten across the full cycle, teams progressively trust agents with more"（扫描档 S3） | §B（窗口前）＋窗口内增量 |
| Kent C. Dodds | 受约束循环画像（**强票**） | "the human does still need to be in the loop"、"trading compute for attention"、"use loop engineering judiciously"（扫描档 S6） | §A（2026-10-06 新入册） |
| Mitchell Hashimoto | 皈依派限速（窗口前谱系） | "excruciating" 双轨训练法；明确不跑通宵循环/多 agent；junior 技能塌陷 "deeply worries me"（扫描档 S11，2026-02-05） | 谱系登记（不入 §A，窗口前） |
| Kent Beck | 节拍论；**窗口内沉默** | 2025-06《Augmented Coding》节拍论；2026-02 与 Tacho/Yegge 联署 "We remain skeptical… and we remain human"；06 后无专门一手发声（扫描档负结论） | §B（窗口前） |
| marmelab（Zaninotto） | 审慎实证（偏怀疑） | "SDD adds little benefit"；增量："would be irresponsible in a low-throughput environment"（适用边界参数化）、"Atomic CRM still requires a human review for every PR"（扫描档 S8） | §B（窗口前） |
| Walden Yan（Cognition） | 受约束形态（**中性票不足**——厂商利益） | 写入单线程拓扑（evidence-u S2）；窗口内无新专门一手文；⚠️ "your codebase regressing to your worst engineer" 系 swyx 编辑摘要语，**不得入 Walden 引句** | §B（窗口前） |
| swyx ~~（原候选）~~ | —— | 实测偏推动，2026-10-06 移入推动派（见上） | §A |

### 反对与怀疑

| 人物 | 派内角色 | 判定依据 | 台账位置 |
|---|---|---|---|
| Armin Ronacher | **锚点·质量反证代表** | 四篇一手链（扫描档 S1–S4）：《Tower Keeps Rising》07-13（摩擦＝同步理解载体、"a useful signal is gone"、**塔不倒只是继续长高——理解坍塌无即时失败信号**）；《Astra》09-07（内卷论＋35h/$1200/79 commits 白卷＋"when left unattended, it *will* keep going… even if it burns through an entire subscription"）；《Better Models: Worse Tools》07-04（SOTA 工具调用退化＋harness 锁定）；《Anger》08-24（失向/焦虑情绪证词） | §A |
| David Searls（**身份坐实＝Doc Searls**，Linux Journal 资深编辑） | 候选 | "dark factory"＋"nowhere close… without supervision"——第二轮补抓：doc.searls.com 全文检索 0 命中、02-26/10-02 帖实读排除、**连 10-02 播客是哪个节目都未确认**——线索本身存疑，**维持待回源** | 候选（倾向降级） |
| Peter Steinberger（旧立场） | 轨迹注记 | 2025-12-28 反自动编排——本体在推动派，此行保留反转轨迹 | §A |

**部分票（交叉引用，本体在别派）**：Willison（门槛/成本方向）、Orosz（价值/新瓶旧酒方向）、Kent Beck＋Laura Tacho＋Steve Yegge 联署宣言（组织绩效层，2026-02）、Hashimoto（限速证词，支持"难掌握"不支持"反对"）——上述均见 [反对派扫描档](../../../../01_seed_reference/loop_engineering/03_skeptics/raw_scan_2026-10-06_skeptics.md)。

> **2026-10-06 批落点约定**：三路深扫档案与判读全部落种子层（用户定）；台账除本节、§A 新增 5 行（Orosz/swyx/Yegge/Kent C. Dodds/Cursor）与 §C1/§B 指针更新外不动。
> **「待回源」= 不可作派别判定依据**；Searls、Steinberger 07-18 终结宣言、Voss 的 Arize 原文、Farley transcript 均在此列。
---

## §B 谱系背景（2026-06 前，**不入名册**，只登记在 [`00-timeline.md`](00-timeline.md)）

| 人物 / 机构 | 贡献 | 时间 | 回源 | 已有卡片 |
|---|---|---|---|---|
| **Kief Morris**（Thoughtworks） | **四级阶梯**：outside / in / on the loop → **agentic flywheel**（C 路：四级非三级；脚注澄清 ralph 原始形态里 operator 在 steering） | 2026-03-04 | ✅ evidence-c | [`_raw_people/10`](../../../../01_seed_reference/voices/_raw_people/10_kief_morris.md)（卡片为三档版，**待按四级修订**） |
| **Birgitta Böckeler**（Thoughtworks） | steering loop / guides-sensors：**spec 降格为 feedforward guide 而非审批门**；"False sense of control?"（⚠️ 出处是 **2025-10-15 sdd-3-tools.html**，非 2026-04 harness-engineering） | 2025-10-15 / 2026-04-02 | ✅ evidence-c | [`_raw_orgs/thoughtworks`](../../../../01_seed_reference/voices/_raw_orgs/thoughtworks.md) |
| **Viv Trivedy**（LangChain） | **"Agent = Model + Harness" 公式原创**（Osmani 明写是 Trivedy 的 one-liner；Böckeler 文把公式链到 LangChain；marmelab 记功给 Böckeler 是传播锚点化） | 2026 上半年 | ✅ evidence-c | 无卡片（**候选**：是否入册待判——公式原创者 + LangChain 工程师，可能满足口径①） |
| **Anthropic** | 《Building effective agents》机制句 + stopping conditions 首次成文 | 2024-12-19 | ✅ evidence-b §2 | 见 §A `anthropic_org`（机构连续体） |
| **Anthropic** | 《Effective harnesses for long-running agents》：feature_list.json | 2025-11-26 | ✅ evidence-b §3 | 同上 |
| **marmelab**（François Zaninotto） | "Natural Language Development" 命名 + "SDD adds little benefit" / "False Sense of Security"（⚠️ 两条名言出处是 **2025-11-12《The Waterfall Strikes Back》**，非 2026-09-24 审计文——C 路全文 grep 实锤） | 2025-11-12 / 2026-09-24 | ✅ evidence-c | 无卡片（候选） |
| **OpenAI**（Ryan Lopopolo） | 命名 "harness engineering"。**2026-09-27 正文已取得**：0 行手写 / 约百万行 / 约 1500 PR 为该团队自述；评审循环自称为 Ralph Wiggum Loop；短 AGENTS.md + 仓内 exec-plans；不可外推。**2026-10-03 增注**：本人 2026-07 移至 Google Cloud（Principal Engineer, Agentic GCP——hyperbo.la 自述 + GC 官方博客 09-25 一手已核，种子层 `09` 卡已更新）；GC 官方口径称他 "the person who coined the term agent harness" | 2026-02-11 | ✅ [evidence-i](evidence-2026-09-27-i-high-influence-control.md) Source 6 | [`_raw_people/09`](../../../../01_seed_reference/voices/_raw_people/09_ryan_lopopolo.md) |
| **Paul Gauthier**（Aider） | 2024-05-22 起把「编辑 → lint → 喂回模型」做成产品内环；测试环须显式 `--auto-test`。窗口前，不入 §A | 2024-05-22 | ✅ evidence-i Source 1 | 无卡片 |
| **Dex Horthy**（HumanLayer） | 12-factor agents：反对自由 “loop until goal”，要求在工具选定与执行之间打断。客户向生产 agent 的反模型，不是 coding-agent 采用率证据。窗口前，不入 §A | 2025-03-30 | ✅ evidence-i Source 2 | 无卡片 |
| **Kent Beck** | 《Augmented Coding》：人说 go 才做下一条测试；删/关测试是作弊信号。单人案例。窗口前，不入 §A | 2025-06-25 | ✅ evidence-i Source 3 | 无卡片 |
| **Steve Yegge** | Beads：用 git JSONL issue 替代会失忆的 markdown 计划；做完一个 issue 就杀掉会话。单人观察，alpha。Gas Town 机制本轮未逐段核。~~窗口前，不入 §A~~ → **升 §A（2026-10-06）**：窗口内《The Shape of Things to Come》（2026-08）已核，见 §A 行 | 2025-10-13 | ✅ evidence-i Source 5 ＋ 种子层扫描档 S10 | 无卡片（素材在扫描档） |
| **Andrej Karpathy** | 终结自创的 "Vibe Coding"（2025-02 造词）；**"Agentic Engineering" 为扩散者而非引入者**——该词由 Zed/Nathan Sobo 2025-06-12 引入（一手：zed.dev 两页，2026-10-03 核），Karpathy 公开切换在 2026-02。谱系修正见 [`_raw_people/07`](../../../../01_seed_reference/voices/_raw_people/07_andrej_karpathy.md) 卡内勘误（2026-10-03） | 2025-06-12（引入）/ 2026-02（切换） | ✅（zed.dev 一手；Karpathy 原推 X 墙未核） | [`_raw_people/07`](../../../../01_seed_reference/voices/_raw_people/07_andrej_karpathy.md) |
| **Stripe**（Beswick & Epsteen） | 《You can't whisper at an AI agent》hard/soft steering——"errors block progress but warnings don't"（C 路逐字到手） | 2026-05-14 | ✅ evidence-c | 无卡片（候选：属 harness 侧，与停止条件的同层性待判） |
| **Geoffrey Huntley** | Ralph Wiggum loop 原语（故意无限 bash 循环、无内建停止条件、back pressure、signs、greenfield 限定）——本词公认起点文献，2026 年仍被 LangChain/marmelab 引用 | 2025-07-14 | ✅ evidence-b §1 | **升 §A（2026-10-03）**：窗口内本人新发声已核（10-02 纲领帖 readable→explainable 等），人物卡 [`_raw_people/16`](../../../../01_seed_reference/voices/_raw_people/16_geoffrey_huntley.md)；§A 行见下 |
| **Harrison Chase**（LangChain CEO） | "harness engineering is an extension of context engineering"（播客转述）；LangChain 四环文页尾致谢含他（evidence-b）但非本人署名 | 2026-03 | ✅ 窗口内已核（2026-10-06）：专栏 "Harrison's In the Loop" 三篇（06-30/07-25/08-12，两篇全文）——"LLMs running in a loop calling tools… the core primitive, the core algorithm" | 无卡片；**不升 §A**（他不用 "loop engineering" 一词，词表为 harness/managed agents/learning loop）→ §A2 推动派**相邻位**（种子层扫描档·推动派） |
| **OpenAI**（alignment / Codex 团队） | 《Auto-review of agent actions without synchronous human oversight》：人工同步审批退出调度回路、独立审批 agent（"The separation of roles matters"）、反复拒绝熔断——loop 侧自主度治理的厂商一手 | 2026-04-30 | ✅ evidence-b §4d | 无卡片（机构条目；素材在 evidence 档案） |
| **Thorsten Ball**（Amp co-creator） | 《How to Build an Agent》（⚠️ 一手标题；流传《How to Build a Coding Agent》为二手变体）："It's an LLM, a loop, and enough tokens"——机制本体最短表述的传播源头之一。<400 行可教学。**2026-10-03 升格注记**：窗口内 #98-100（09-06→09-20）持续发声（agent 派生 agent 黑盒测试实录 + "aim higher"），人物卡 [`_raw_people/19`](../../../../01_seed_reference/voices/_raw_people/19_thorsten_ball.md) | 2025-04-15 | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D1【主验】 | ~~无卡片~~ → **升 §A（2026-10-03）**，见下 |
| **Walden Yan**（Cognition 联创） | 《Don't Build Multi-Agents》：单线程 agent ＋ Principles of Context Engineering（Share context / Actions carry implicit decisions）；反并行立场在命名前成形。影响力峰值在 2025-09-01 HN 重投。窗口前，不入 §A。**后续立场修订线索（multi-agents-working）待回源** | 2025-06-12 | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D2【主验】 | 无卡片 |
| **Yichao "Peak" Ji**（Manus 联创兼首席科学家） | 《Context Engineering for AI Agents》：最完整的 "loop until the task is complete" 机制句＋KV-cache 命中率为生产 agent 第一指标＋文件系统外部记忆支撑长循环。窗口前，不入 §A | 2025-07-18 | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D3【主验（loop/KV-cache 段）】 | 无卡片 |
| **Armin Ronacher**（Flask/Werkzeug 作者） | 两篇：《Agentic Coding Recommendations》（派活全权等待完成的实践自述；agentic loop 作性能工程对象，HN 296 分）＋《Building an Agent That Leverages Throwaway Code》（MAX_STEPS＋reachedEndCondition＋逐步缓存的一手伪代码）。**2026-10-03 升格注记**：窗口内 07-04→09-29 十篇（工具退化反证 → 内卷论/slop factory），与 Thorsten 公开互驳；人物卡 [`_raw_people/17`](../../../../01_seed_reference/voices/_raw_people/17_armin_ronacher.md) | 2025-06-12 / 2025-10-17 | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D4/D5【主验】 | ~~无卡片~~ → **升 §A（2026-10-03）**，见下 |

---

## §C1 候选池（有线索、未判）

| 候选 | 线索 | 待判什么 |
|---|---|---|
| **Simon Willison** | 2025-09-30《Designing agentic loops》已回源：他是循环实践者（工具环 + 成功标准 + 测试套件），同时指出 YOLO 的破坏/外泄风险。这不是对本词的反方论文，也不是语义纠偏 alone。**2026-06 后对本词专门发声——负结论复证（2026-10-06，遍查其 tag 页 254 帖），不升 §A**；但其 2026-09-24 note（"they make software engineering **even harder**… requires extraordinary discipline and knowledge"）＋10-03（"hard budget caps need to be the default"）构成**门槛/成本方向的部分票**（种子层扫描档 S5/S6） | 人物全景已在 [`_raw_people/04`](../../../../01_seed_reference/voices/_raw_people/04_simon_willison.md)；本主题引句在 [evidence-i](evidence-2026-09-27-i-high-influence-control.md) Source 4；派别：中性偏怀疑（§A2） |
| **Gergely Orosz** | ~~六预测；"Something precious is being taken away"~~ → **升 §A（2026-10-06）**：07-14《What is "loop engineering?"》为本词专门发声（§1–4 一手＋大纲句逐字）；引文纠偏 "something **valuable**"。派别：中性偏怀疑（§A2） | 人物全景已在 [`_raw_people/12`](../../../../01_seed_reference/voices/_raw_people/12_gergely_orosz.md)；§A 行见上 |
| **swyx**（latent.space） | ~~loopcraft 原帖 404~~ → **升 §A（2026-10-06）**：经双镜像取得全文＋LangChain 官方引用逐字核销＋AIEWF 主台演讲；实测立场**推动**（"entire game of the next century"） | §A 行见上；种子层扫描档 S5 |
| **Dave Farley**（Continuous Delivery 作者/YouTube 教育者） | 2026 年批评 vibe coding 工程质量——AIDEvCon London 2026＋GOTO G^K25 两场逐字到手（**经转写，降半级**；GitHub 镜像 jscraik/Agent-Skills＋lilys.ai）。**派别提示：正面纲领是 executable specification / ATDD（spec-driven 词表），反对对象是 vibe coding 质量 ≠ 反 agent loop 机制**（种子层 skeptics 档·补抓增量） | 候选：中性偏怀疑（转写级；是否满足①待被引用情况核实） |
| **Laurie Voss**（npm 联合创始人；Arize DevRel 负责人） | ~~Arize 原文截断，入册前须补一手~~ → **升 §A（2026-10-06 第二轮）**：Arize 原文＋O'Reilly 文两个一手载体齐 | §A 行见上；种子层扫描档·补抓增量 A/B |
| **Jesse Vincent**（obra / Superpowers 作者） | Superpowers（289k★，口径④＋③一线规模）；其 Fable 5 时代的 `/goal` 实验（过夜 25 实验＋失败日志）是实践层 backbone §1 的例证来源；素材在 [`field_samples/fable5/run_superpowers_jesse_vincent/`](../../../../01_seed_reference/field_samples/fable5/run_superpowers_jesse_vincent/profile.md)（既有，只引用） | **待判更新（2026-10-06）**：blog.fsck.com 2026-07-05《Some new agentic patterns》一手全文已取得（过夜双 agent 协作实录＋未解难题自认："凭据缺口我还没解决"、Lethal Trifecta 无人解决）；独立性待深读后定（种子层扫描档·推动派）。另："shack 刊物"系负结论——博客无此子栏目 |

---

## §C2 已排除（按质量门槛出局的线索，登记在案防止反复）

| 被排除项 | 排除理由 |
|---|---|
| **腾讯云社区《最近疯传的 Loop Engineering，是台印钞机，还是绞肉机？》** | 标题党 + 中文聚合转述。按用户 2026-09-26 质量门槛**直接丢弃**，连"热度旁证"都不作——热度本身不是思考 |
| **HN 评论者**（yoaviram、gsadaka、sermakarevich、constantcrying、conartist6 等） | 论坛随机评论 ≠ 有影响力的 KOL。其观点**不得进入本主题的 KOL 证据**；若需"社区情绪"佐证，单独标注、不与 KOL 证据并列 |
| **openai/codex issue #32389** 等用户 bug 报告 | 官方仓库用户报告非厂商立场文件；仅作《Unwinding Codex's Agent Loop》的**存在性旁证**（B 路已放「不入册·仅社区情绪」，其中 wire 层终止语义句引用须标注"官方仓库用户报告"） |
| **社区镜像仓库 / 媒体转述**（SiluPanda 等 codex-loop 镜像、Ars Technica、Turing Post、Simon Willison/gigazine/36kr 的二手报道） | 非官方复制品与媒体转述，一律不作证据（B 路执行记录） |

---

## §D 线索来源（供复审追溯）

| 来源 | 性质 | 提供了哪些线索 / 已核实哪些 |
|---|---|---|
| [`01_seed_reference/loop_engineering/andrew_ng/raw_ng_x_post_en.md`](../../../../01_seed_reference/loop_engineering/01_advocates/andrew_ng/raw_ng_x_post_en.md) | **一手**（已归档） | Andrew Ng 三环；**Cherny / Steinberger 两个词源人物** |
| [`raw/evidence-2026-09-26-a-originators.md`](evidence-2026-09-26-a-originators.md) | **一手回源档案**（A 路·词源与定义者四人） | Cherny 访谈句三版本对照与 YC transcript「loop 出现 0 次」；Steinberger 推文 snowflake 定位与「无深度内容」结论；Runkle 四环逐字；Osmani 两篇全取得（分层四级）；CC 团队 06-30 官方定义交叉核验——**「词源＝热度碎片、定义＝事后工程化」的判定依据** |
| [`raw/evidence-2026-09-26-b-stop-and-scheduling.md`](evidence-2026-09-26-b-stop-and-scheduling.md) | **一手回源档案**（B 路，9 个一手记录块全文） | Ralph 原文、Anthropic 两篇工程文、Claude Code `/goal`//`/loop`/auto mode 官方文档、OpenAI auto-review、LangChain 四环；**停止条件与外层调度两问判定收敛**；负结论 4 条 |
| [`raw/evidence-2026-09-26-c-autonomy-and-convergence.md`](evidence-2026-09-26-c-autonomy-and-convergence.md) | **一手回源档案**（C 路） | Kief Morris 四级阶梯、Böckeler steering loop 与归属修正、marmelab 两篇辨析、Stripe steering 原句、OpenSpec/Spec Kit 官方动作、橙皮书定性；**自主度位置分档成立/量化分档未成型**；**收敛判定成立** |
| [`talk-harness-201/02_evidence/01-kol-alignment-2026.md`](../../../../talk-harness-201/02_evidence/01-kol-alignment-2026.md) | 本仓证据（2026-09-25 web 检索） | Karpathy、Harrison Chase、Osmani、Böckeler、Huntley、Lopopolo、Stripe。⚠️ 其中"公式出自 Böckeler"已被 C 路一手链推翻，**该文件待复核修正** |
| [`raw/evidence-2026-09-27-i-high-influence-control.md`](evidence-2026-09-27-i-high-influence-control.md) | **一手回源档案**（I 路·簇外高影响面） | Aider lint 环、Horthy 反自由循环、Beck 单测试节拍、Willison 2025-09 相邻专名、Yegge Beads、OpenAI harness 全文、Cursor / Copilot 云端循环。**不升 §A** |
| [`raw/evidence-2026-09-27-i2-teams-evals-outcome.md`](evidence-2026-09-27-i2-teams-evals-outcome.md) | **批次回源档案**（I 路批次 2·五切口；主验与侦察回源混合） | (a) 厂商控制面候选形态；(b) evals 思想；(c) 定量效果成对地图；(d) 谱系候选；(e) SDD×loop 厂商组合。主验条目可进入判读，侦察条目待复验，不增加独立票；**不升 §A** |
| `/Users/bowhead/deepseek-harness/_faq_on_digested/15_loop-engineering-vs-sdd/`（**仓库外**） | 外部研究·转引 | LangChain / Osmani 的日期与定义分界、命名时间线序列、SDD 阵营反方线索——**全部仅作检索方向，本主题结论一律以自己的回源为准** |

---

## §E 本轮已确认的负结论（"搜过什么、没找到什么"）

1. **《Unrolling the Codex agent loop》（OpenAI，Michael Bolin，2026-01-23）**已有检索工具取得的候选文本（[evidence-k](evidence-2026-09-27-k-unrolling-codex-agent-loop.md)）。库内旧题 Unwinding 是错的；assistant message 终止态和「四拍」否定仍待独立一手复核。本环境直接 HTTP 仍 403。不升 §A。harness engineering 全文仍见 [evidence-i](evidence-2026-09-27-i-high-influence-control.md) Source 6。
2. **Claude Code 官方 CHANGELOG 不可达**（raw.githubusercontent.com 网络超时）——auto mode/`/goal`/`/loop` 引入日期未从 changelog 取得，已用官方文档版本锚点替代（v2.1.228 / v2.1.283 / v2.1.269）。
3. **Claude Code auto mode 公告博客正文截断**——标题经搜索逐字确认（"Auto mode is now the default in Claude Code for Pro, Max, and Team plans"），页面发布日期未取得；机制证据已由官方文档 + 工程博客覆盖。
4. **Cherny 访谈句逐字原文 / Steinberger 推文正文未取得**（X 全域不可达）——Cherny 名句三个流传版本措辞不一致（对照表见 [evidence-a](evidence-2026-09-26-a-originators.md)）；Steinberger 推文正文**已获 Osmani 06-07 帖逐字转引**（"You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."，见 evidence-a 补充回源节）——从「未取得」升级为「有日期转引」，直接引用仍须标「经 Osmani 转引」。另两条开放问题：LangChain 帖中 "Boris"→`0xwhrrari` 身份待核、swyx《loopcraft》原文 404（详见 evidence-a §6 与 [`../digested/01-命名谱系.md`](../digested/01-命名谱系.md) §五）。
5. **B 路第 4 条负结论**：Codex auto-review 官方 docs 页 403（机制证据已由 alignment.openai.com 官方博客全文覆盖，见 [evidence-b](evidence-2026-09-26-b-stop-and-scheduling.md) 负结论#4）。
6. ~~Osmani 的 O'Reilly 书名两档案矛盾~~——**已裁决**（2026-09-26 晚补充回源，Osmani 官网 O'Reilly 链接实锤）：正确书名《Agentic Engineering》，evidence-c:57 的《Beyond Vibe Coding》为误（见 evidence-a 补充回源节）。
7. **I-2 批次负结论**（详见 [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) 线索登记与负结论节）：DORA 2025 年报正文具体系数 gated 未取得（官方摘要页口径可用，系数不引）；GitClear 白皮书全文需邮箱下载（落地页摘要已核）；Kiro docs 正文客户端渲染未取得（以官方博客＋官方 README 替代）；Devin docs.devin.ai 被 Mintlify 壳层截断（官方博客一条已回源）；Thorsten Ball 文章一手标题为《How to Build an Agent》（《…Coding Agent》系二手变体，Wayback 本环境不可达未核原始快照）；Manus 文件系统段经第三方镜像补齐（主站截断，主验待补）；AlphaEvolve 白皮书 §2.4–2.5 截断（摘要＋§1–2.1＋图注已核）。
