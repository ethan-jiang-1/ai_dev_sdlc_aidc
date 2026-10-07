---
type: kol_evidence
directory: 02_neutral/kol_tech
observation_date: 2026-10-07
---

# martin_fowler — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：martinfowler.com 作者；Thoughtworks 首席科学家
> **背景**：Martin Fowler——《Refactoring》《Patterns of Enterprise Application Architecture》作者， agile 宣言签署人之一；martinfowler.com 站主（Böckeler 等 Thoughtworks 人的 loop 主题文多发布于此站）。**本人此前在本主题零条——本档为 2026-10-07 agile 元老专项新建**。⚠️ 采集陷阱：mf.com master feed 的作者字段恒为"Martin Fowler"，会把 Sadalage/Laycock/Giles 等同事文章在 RSS 层面误标为 Fowler——逐条署名甄别后本档只收本人署名。
> **号召力**：①＋②＋④（agile 元老·行业最高声望作者）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)
> 人群类型：**专业技术 KOL**（程序员/工程师出身）
> **词表注记**：窗口内从未以自己名义使用 "loop engineering"（仅 08-18 原样转引 Rob Bowley 调侃"moved on from Loop Engineering to Graph Engineering"，未评论）——自用词汇为 **harness engineering（背书传播）/ agentic programming（自有 bliki）/ verification（主线词）**。按台账相邻位规则单列（同 Harrison Chase 先例），不混入本词派别计票。

## 态度轨迹

**方向**：审慎建设性持续加深（观察者→验证优先的制度主张；**无翻转**）
**起点**：retreat 观察者（06-02 度量不可信但"暗灯可用"）
**终点**：verification>generation 的激励制度主张＋个人矛盾定盘（"不喜欢但别无选择"）
**弧线**：06-02/06-16 温和积极＋纪律化 → 07-06/07-13/07-21 成为 harness/验证正方陈述者 → 08 月无人值守逐案示警 → 09-08 制度主张（最强句）→ 09-17 情绪定盘 → 09-29 停止条件道德底线 → 10-04 "养育推理系统"总纲
**关键转折**：07-21 验证＝瓶颈（转述背书 TW 报告）→ 09-08 激励制度主张（组织对 agent 一切行为负全责）

## Fragments 2026-09-08 —— verification>generation 的制度主张（本窗口最重）

- URL：https://martinfowler.com/fragments/2026-09-08.html ｜ fetch 成功（直连 TypeError→经 /fragments/ 索引取全文）
- **挂钩**：验证回路（最重）＋预算与熔断（激励制度）。

**逐字摘录**：

> "**I assert that the organizations that build and run agents are responsible for everything those agents do, whether that behavior is intended or emergent.** If they reap counterfeit utility by neglecting verification, they must face consequences: legal, financial, and if necessary: criminal."

> "**To deal effectively with AI, we need to change the incentives involved to ensure people invest more in verification than they do in generation. Otherwise we are driving a car that has a powerful engine, but weak brakes.**"
（**验证投资的激励制度化**——"强引擎弱刹车"是对宽自主放权循环最凝练的元批评之一。）

> 自加（对 Catalini 框架）："The danger is that people use lots AI automation while using incomplete measurements of its effectiveness, leading to short-term dashboards going up, but disaster in longer time-scales."

> 放大 Jessica Kerr："If we want agents to write working, reliable code for us, we have to double down, 10x down on our objective verification."＋放大 Steve Yegge："…you have to keep an iron grip on system size, or it'll run away from you."

## Fragments 2026-07-13 —— 验收不可外包＋sensors>specs

- URL：https://martinfowler.com/fragments/2026-07-13.html ｜ fetch 成功
- **挂钩**：验证回路＋停止条件＋循环结构（guides/sensors）。

**逐字摘录**：

> "**We can outsource many things, but not the acceptance criteria**, at some point there's a human request and a human judgment on whether that request was properly executed."

> "**Conformance tests (sensors) are more valuable than specifications (guides), but it's hard to imagine all the conformance tests that are needed to say what shouldn't happen.**"
（Böckeler guides/sensors 框架的本人背书与边界补注——"不该发生什么"难以穷尽。）

> "When we had our first retreat in Utah early this year, nobody had heard of Harness Engineering. This time we had a whole session on it."＋"We find it reduces token usage, and also allows weaker models to be useful, supporting such things as local hosting of open-weight models."

## article《I don't like LLMs》（2026-09-17）——总立场定盘

- URL：https://martinfowler.com/articles/2026-dont-like-llms.html ｜ fetch 成功（首试 TypeError 复测 200）
- **挂钩**：总立场（情绪＋继续用）。

**逐字摘录**：

> "**I don't like them.** They talk to me in this grating LLM-voice, an uncanny valley of talking to a real human. **They confidently bullshit me** - often giving me useful, helpful answers. But also just making stuff up with the same assurance."

> "**Fundamentally I don't think we have a choice about riding on the AI technology train. It's a wild ride and I just hope we'll get through it OK.**"

> "I have a lot of mixed feelings about AI and LLM technology… On the other hand, I'm fearful of the damage AI might cause: agent swarms taking over our virtual and physical infrastructure, designing bio weapons."

## Fragments 2026-07-06 —— retreat 观察＋成本警觉＋伦理立场（含归属校准）

- URL：https://martinfowler.com/fragments/2026-07-06.html ｜ fetch：TypeError→curl(UA) 成功
- **挂钩**：循环产品化（harness 术语扩散）＋预算与熔断（token 成本）＋无人值守（隔夜质检）。

**逐字摘录**：

> "there was much talk now about harness engineering, when that wasn't even a term in Utah - an example of how rapidly things are moving."

> "a way to measure design quality is to look at token costs. If the same change requires less tokens that indicates a better architecture."＋"overnight quality checks with a report for humans to act on in the morning"

> 伦理立场（**Fowler 自撰概括句**）："Her conclusion however, like mine, is that there's no ethical gain from renouncing the use of AI and castigating those who use it."
（⚠️ 归属校准（G1 溯源）：此句为 **Fowler 的自撰概括**，被放大者 Charity Majors 的逐字对应＝"unilateral disarmament in the face of powerful new tools is neither wise or an effective strategy"（06-15）——见 [charity_majors](charity_majors.md)。引用勿把概括句记到 Charity 名下。）

## Fragments 2026-09-29 —— 无人值守的停止条件道德底线

- URL：https://martinfowler.com/fragments/2026-09-29.html ｜ fetch 成功
- **挂钩**：停止条件＋无人值守运行。

**逐字摘录**：

> "**why are we wondering if they have consciousness - when we should be wondering why they don't have a conscience?**"

> "**Those that train the LLM should be responsible for what it does**, after all if it has such a galaxy brain it should be able to tell if it's doing something wrong and **either stop or get a human's explicit approval.**"
（**"要么停下、要么获得人的明确批准"**——无人值守循环的停止条件道德底线句。）

> "While things like vibe coding get a lot of attention, the real strength of agentic programming relies on more sophisticated techniques - and these are not easy to learn or execute. It's a reason I'm wary of extrapolating my own dabblings into firm opinions about how to use the genie."

## Fragments 2026-07-21 ＋ 08-04 ＋ 09-01 ＋ 10-04 —— 验证瓶颈/失控示警/CI 纪律/总纲

- 07-21（fetch 成功）转述背书 TW 报告："**Code generation is no longer the bottleneck — verification is.**"；"'Harness engineering' is emerging as a distinct, ownable discipline."；

> "**Getting agents to auto-remediate moves us to the next level of capabilities and concerns.** …**Agents don't learn, the best they can do is update the context.**"＋"We hear so much about the incredibly productive things we can do with agentic programming, but has anyone noticed a flood of wonderful applications built with it?"
（对生产率叙事的反问——与 Orosz 调查式怀疑同族。）

- 08-04（fetch 成功）模型方追责："They are morally responsible for any consequences of this, and that should extend to legal liability too."＋"But when does our Challenger-moment appear?"
- 09-01（经索引取全文）CI 纪律："**Continuous Integration is a practice, not just the CI server.** …verification is a necessary part of merging if we want to retain a healthy mainline."＋转述背书 NVIDIA AVO 长周期 agent："persistent memory and supervision… The supervisor monitors the broader trajectory for stagnation or repeated unproductive cycles and can redirect the main agent"（外层调度/停滞熔断的行业实例）。
- 10-04（fetch 成功）总纲：

> "**One of the challenges of working with these systems is understanding what has changed in this shift from building a computational system to nurturing an inferential one, and how our processes need to change in response.**"

## 判定

- **弧线（arc）——底层立场稳定：审慎建设性持续加深，无翻转**。四阶段：06 月温和积极＋纪律化（registers/新鲜上下文）→ 07 月 harness/验证正方陈述者 → 08-09 月制度化（组织全责/激励/追责＋情绪定盘）→ 10 月总纲（"养育推理系统"）。
- **七类挂钩覆盖**：验证回路（最重）✓✓｜停止条件（"stop or get a human's explicit approval"）✓｜预算与熔断（token 成本、supervisor 停滞重定向）✓｜外层调度（AVO 背书）△｜循环结构（registers）✓｜无人值守（案例示警＋隔夜质检背书）✓｜循环产品化（"harness engineering 是可拥有的学科"）✓。
- **派别适配**：**中性（相邻位）**——验证优先＋人审不可外包＋停止底线，是中性派纲领的元老级表述；但词表不同（harness/agentic programming），按相邻位单列不计本词派别票。
- **负结论**：①窗口内从未以自己名义用 "loop engineering"；②无 loop/harness 方法论长文（全部为 fragments 短形式＋一篇 900 词短文）；③mf.com 窗口内其他 AI 文章（Sadalage/Laycock×2/Giles/Garg/Joshi/Kulkarni/Moghe×4/Highsmith）逐条验明**非 Fowler 署名**，不计入；④mf.com 托管的 Böckeler harness 全文（04-02，窗口前）归属在 Böckeler 名下。
