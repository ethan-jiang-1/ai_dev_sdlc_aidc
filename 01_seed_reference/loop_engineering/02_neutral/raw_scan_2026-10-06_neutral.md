---
type: evidence_archive
collected_by: 后台回源 agent（2026-10-06 三派分野批·中性派路；经用户指示落种子层）
collected_at: 2026-10-06
serves: 01_seed_reference/loop_engineering/ 三派重组（本档为中性派素材）；供 02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md 三派分野与 digested 判读引用
status: 全文取得 7 条（S1、S4a/S4b/S4d、S5-镜像、S6、S7、S8-复核实段）；截断 3 条（S2 transcript 截至约 21 分钟、S3 仅官方摘要＋二手转述、S4c 付费墙后不可读）；未得若干（见负结论节）
quality_bar: 一手优先；X 不可达；HN/Reddit 评论不作 KOL 证据；负结论必须记；镜像站全文必须标"镜像"；搜索摘要不作引句
---

# 回源档案 AG：三派分野——中性派深扫（观测 2026-10-06）

> **任务**：用户 2026-10-06 委派：loop engineering 三派重组，深扫中性派 KOL（边界划定/受约束形态/审慎判读），优先核实 Huntley / Böckeler / Kief Morris / marmelab / Walden Yan / swyx / Kent Beck 七个方向，并自由搜索识别真正的中性派 KOL。
> **与既有档案的关系**：Huntley 2026-10-02 纲领帖、Böckeler 2025-10-15 与 2026-04-02、Kief 2026-03-04、marmelab 2025-11-12 与 2026-09-24、Walden 2026-04-22、Kent Beck 2025-06-25 均已在库。本档登记的是**窗口内（2026-06 起）新增量**与复核结果。
> **路径说明**：本档所称 evidence-a/b/c/i/u 等档案代号，指仓库根 `02_research/01_agent_engineering/loop_engineering/raw/` 下的 `evidence-*.md` 回源档案（如 evidence-c = `02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-26-c-autonomy-and-convergence.md`）；人物卡代号指 `01_seed_reference/voices/_raw_people/` 下的卡片。时间窗规则（2026-06 起）与本集合 README 一致。

---

## Source 1 · Birgitta Böckeler《TDD inside the agent loop - theater or actual value?》（2026-08-10）

- URL：https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html ｜ 作者身份：Thoughtworks Distinguished Engineer，AI-assisted delivery 专职角色（2023 起全职投入该领域）
- 来源类型：个人一手博客（Thoughtworks "Exploring Gen AI" 系列；全文取得；发布日期 10 August 2026 经系列索引页核对）
- 号召力口径：①＋②——guides/sensors 术语定义者（被 marmelab 2026-09-24 审计列入 founding texts）；SE Radio 730 专访嘉宾；Thoughtworks Distinguished Engineer。
- **库内已有**：2025-10-15 sdd-3-tools（"False sense of control?"）与 2026-04-02 harness-engineering（evidence-c）。**本条为增量**：她 2026-06 后对"循环内部实践"的专门发声＋一次自跑 eval 的实证。

**逐字摘录**：

> "Based on Opus's judgment of the quality of the outcomes, there was no clearly discernable difference based on TDD workflow versus no TDD workflow. On the contrary, more than once Opus ranked the non-TDD workflow solutions slightly higher in design and test quality. There was also no meaningful difference in mutation scores across the solutions."
（中文说明：对"循环内该怎么做"的主流信条（TDD）做了受控对比，结论是无差异甚至略反向——中性派"先测再信"的范本动作。）

> "there is generally more and more evidence that being overly specific about _how_ we want a model to do something is not a sustainable approach. Instead, we should find as many ways as we can to monitor the outcomes and give feedback. That feedback should be automated wherever possible, and we need to carefully think about where we insert ourselves as arbiters of what is good and correct."
（"how 指定不可持续 → 监控 outcome"——这是她对循环内部治理方向的核心判读。）

> "I personally have stopped telling my coding agents to write tests first, let alone do TDD (which I never did, to be honest), until I see evals or other strong arguments that convince me otherwise."
（明确的"证据出现前不采用"立场句——审慎实证派的自我表述。）

> "this is obviously a very small sample size, so take it with a grain of salt"
（她主动标注自己实验的局限——不外推。）

> "Writing the test first doesn't reliably prevent this - it might make it less probable, which is all we can ever hope for anyway with LLMs"
（对 LLM 概率本质的边界认知。）

> "Whatever ends up giving us trust and confidence in our software in the future - I think the role of TDD as we've known it is significantly smaller than pre-GenAI."
（收尾判断：旧信任机制在缩小，但替代物（Approved Scenarios、mutation testing 等）仍在探索——承认未解决。）

成本数据（附录表）：TDD 组 token 为非 TDD 组的 2.96x–8.50x（她自己注明该口径高估真实美元成本，因 cache-read 被等权计入）。

**该条支持的最小主张**：Böckeler 在 2026-06 后继续以"跑小实验→承认不确定→等更强证据"的方式发表循环内部实践的判读；她反对把 how-级指令当默认，主张 outcome 监控＋自动化反馈＋慎重安排人的仲裁位。
**派别适配**：**中性票（最强样本）**。注意：该文围绕 "agentic loop" 机制，**全文未出现对 "loop engineering" 专名的采用或评述**（本路对该文全文未检出该词的专门表态段）。

---

## Source 2 · Birgitta Böckeler 于 SE Radio 730（2026-07-22）

- URL：https://se-radio.net/2026/07/se-radio-730-birgitta-boeckeler-on-harness-engineering-for-ai-agents/ ｜ 主持：Priyanka Raghavan
- 来源类型：播客一手（官方自动生成 transcript，**截断取得**——约至 20:46 处，后半未取到）
- 号召力口径：②——IEEE Computer Society 旗下 SE Radio 是主流工程媒体播客；她为当期唯一嘉宾。
- **库内登记过线索**（evidence-c 记"SE Radio 730（2026-07）专访嘉宾"但未回源）。**本条为增量**：transcript 实取。

**逐字摘录**：

> "you can absolutely just get started plain vanilla without putting anything in there. And I would actually recommend it when you first do agentic coding just to feel what it actually does without it"
（反工具热：先裸跑、建立对裸基线的体感——审慎派方法论。）

> "some people who have already built-up skills and lots of instructions might want to revisit that as well with newer models because some things are maybe not necessary anymore"
（harness 膨胀警示：已有积累要随模型升级回撤。）

> "there's a school of thought that the language models will just get better and better and better until they're just perfect at coding... But yeah, I don't think that's realistic"
（对"模型进步会解决一切"派别的明确不认同。）

> "it turns out that AI needs a lot of the same things that we need to make safe changes to stuff"
（直接反驳"代码可读性不再重要"论——与 Huntley 2026-10-02 "readable→explainable" 纲领（`01_seed_reference/voices/_raw_people/16_geoffrey_huntley.md`，研究层登记见 evidence 系档案）形成跨 KOL 张力点，值得判读层记录。）

> "we're all throwing lots of terms out there and I think that's been a challenge for me, to find the right words to describe what is happening"
（对术语通胀本身的表态：她视术语为思考工具而非宣传品。）

（页面官方摘要另述：harness "require continuous maintenance as underlying foundation models evolve"——此句出自页面 editorial 摘要，非 transcript 逐字，引用需标"官方摘要"。）

**该条支持的最小主张**：2026-07 她在主流工程播客上重申：裸基线先行、harness 需随模型演化做减法、传感器（含静态分析/测试）在大模型下仍然必要。
**派别适配**：中性票。

---

## Source 3 · Kief Morris《Humans on the loop, not in it: Taking agentic engineering end to end》PlatformCon Live Day London（2026-06-23 16:00 BST，30 min，Main stage）

- URL（官方 session 页）：https://2026.platformcon.com/sessions/humans-on-the-loop-not-in-it-taking-agentic-engineering-end-to-end-ldn ｜ 二手现场记录：https://lucaberton.com/blog/kief-morris-human-on-the-loop-platformcon-london-2026/（Luca Berton，2026-07-04）
- 来源类型：演讲——**官方摘要＋关键点全文取得（curl 实取 session 页）**；演讲视频本体未取得（Podwise 摘要页 fetch 失败）；Luca Berton 记录为二手转述。
- 号召力口径：①＋②——"on the loop" 分层框架定义者（martinfowler.com 2026-03-04 文，库内已有，其人物卡在 `01_seed_reference/voices/_raw_people/10_kief_morris.md`）；O'Reilly《Infrastructure as Code》作者、Thoughtworks Distinguished Engineer；PlatformCon 主舞台。
- **库内已有**：2026-03-04《Humans and Agents in Software Engineering Loops》（evidence-c）。**本条为增量**：命名周后 17 天他把它推向端到端交付＋平台工程受众。
- ⚠️ **归属澄清**：Luca Berton 博客称"Kief's article on MartinFowler.com, 'Human on the Loop'"——经核对，该文即 2026-03-04 的 humans-and-agents.html（标题被 Luca 转述改动），**不存在一篇单独的新文章**（martinfowler.com/articles/human-on-the-loop.html 为 404，系列索引无此条）。

**官方 session 页逐字摘录（一手）**：

> "Using AI to generate code isn't enough. Platform engineers can enable teams to put agents to work across the full delivery loop: specify, build, test, release, run, and improve. Humans steer outcomes while agents do the heavy lifting."
（官方摘要——他把循环从"写代码环"扩到全交付环，人的位置=steering。）

> "Teams should focus on defining outcomes and prioritizing improvements, not managing every artifact; humans should stay on the loop, not in it."
（官方 key points 逐字——against 逐件审批。）

> "As feedback loops tighten across the full cycle, teams progressively trust agents with more."
（官方 key points 逐字——**渐进信任**：不是一次性放权，是随反馈环收紧逐级授权。这是中性派"什么时候可以放权"的最清晰官方表述之一。）

> "Platform engineers need to enable the capabilities that make end-to-end agentic workflows reliable, especially for release and operations."
（官方 key points 逐字——可靠性能力建设是平台工程师的职责。）

**该条支持的最小主张**：Kief 在词源周后的公开立场是"人的位置=on the loop 的系统管理层；放权程度随全环反馈质量渐进提升"；官方文本无 hype 语汇。
**派别适配**：中性票（其 agentic flywheel 愿景部分偏推动，但以 sensors/渐进信任为前置条件——归中性，注明张力）。

---

## Source 4 · Geoffrey Huntley：2026-06 后四篇（三条全文＋一条付费墙截断）

- 作者身份：独立研究者，Ralph Wiggum loop 原语作者（2025-07）；**注意 2026-07-24 宣布加入 Antithesis**（确定性测试/形式化验证公司）。人物卡：`01_seed_reference/voices/_raw_people/16_geoffrey_huntley.md`。
- 号召力口径：①＋②＋③——Ralph 原语作者且被 LangChain/marmelab/OpenAI 引用；marmelab 审计把 Ralph 收录为 "back pressure engineering"；库内已升 §A。
- **库内已有**：2026-10-02《readable→explainable》纲领帖。**本批为增量**：2026-06-27 / 07-24 / 09-27 / 10-05 四篇，覆盖他对运动本身的最新姿态。

### 4a《engineer away the slop》（2026-07-24，全文取得）
URL：https://ghuntley.com/slop/

> "It's been a busy six months... the short TLDR is I'm joining the folks over at https://antithesis.com/"
（Ralph 之父的职业选择本身就是立场：转向确定性验证。）

> "Creation is now near-free. Verification/understanding is not, yet. It's time to engineer away the slop."
（他 2026 年中对循环运动瓶颈的定位：生成已免费、验证未免费——把 discourse 从"怎么让循环跑"移到"怎么让循环可验"。）

> "The discipline/techniques of formal verification and deterministic system testing are about to cross the chasm. There's a whole lot of brownfield software out there that's been written over the last 30 years that is being affected by the infinite software crisis... all at once."
（预测：验证学科将跨鸿沟——不是"循环取代工程"，是"验证学科回归"。）

> "one of the things I shared was some deep concerns that we are entering into another Eternal September"
（对放权后果的社会面担忧——与吹捧派拉开距离。）

> "whilst many things have changed, the job of software engineers is to produce experiences without defects."
（不变量声明：无缺陷交付。）

### 4b《A couple of months ago in Miami...》（2026-06-27，全文取得）
URL：https://ghuntley.com/miami/

> "If you cannot demonstrate how a coding agent works, you are just a consumer and have imposed an artificial glass ceiling on your career as a software engineer."
（对"用而不懂"人群的边界判定。）

> "AI is more like a musical instrument than just a tool. Play with it, make discoveries, build intuition, learn where AI is good and where it fails"
（词源月内的边界句：**learn where AI is good and where it fails**——适用边界的显式表述。）

> "If you are curious, you will have a job. If you have not been curious in the last two years, you are replaceable."
（人的位置：好奇心/工程判断，而非打字。）

### 4c《the eighteen-month recap: AI Engineer, Singapore, May 2026》（2026-09-27，**付费墙——前段取得，正文截断**）
URL：https://ghuntley.com/eighteen-month-recap/

> "He's the person behind the Ralph loop, which is now incorporated in many, many tools that are used today."
（会议方引介语——Ralph 的行业渗确认。）

> "As confident as I might seem about these topics, I must say this is quite a provocative title... when you're listening to this, I want you to reflect upon it. Maybe I'm right, maybe I'm wrong."
（开场认识论姿态：明示可能错。）

> "It's been roughly a year and a half since I published the technique of allocating memory in a particular way. If you wrap the tool calls around another loop, it's just a loop. But there's a lot of science in the context engineering needed to actually achieve these outcomes, and it's quite disruptive."
（对 Ralph 的**自我祛魅**：技术本体"就是个循环"，难点在 context engineering——不参与对其原语的神话化。）

### 4d《an application in lisp you grow by talking to it》（2026-10-05，全文取得）
URL：https://ghuntley.com/lisp/

> "It's kind of strange seeing all these discussions about software factories... and the like."
（对运动 discourse（software factory 叙事）的直接态度：strange。）

> "What I haven't seen is people really deeply understanding the power of the new substrate that we have. People are still too fixated on what they have now and how systems have been built to rethink fundamentally how much things can change."
（批评方向不是"循环走太快"而是"讨论仍困在旧范式"——他与保守怀疑派不同。）

> "To me, a software factory isn't just about process automation; it isn't about automating everything you've got as it is now. It's about using this substrate so you can develop your product while it runs whilst in the product itself."
（对运动核心词 software factory 的重新定义。）

> "To me, the idea that an agent writes source code and then there's a costly compilation phase involving CI/CD is now truly undefined now that we have AI."
（激进方向：连 CI/CD 编译循环都要被重想。）

**该条（4 组）支持的最小主张**：Huntley 2026-06 后未拥抱 "loop engineering" 专名（四篇均未以该词为题或展开评述）；他的姿态是：对原语自我祛魅（"it's just a loop"）、对 discourse 表达疏离（"strange"/"fixated"）、把重心移到验证瓶颈（Antithesis）与新基座重构。
**派别适配**：**不是简单中性票**——目的地方向激进（不可读代码、产品自建产品、消灭编译循环），路径判断审慎（验证是瓶颈、Eternal September、maybe I'm right maybe I'm wrong）。建议三派重组时单列为"重构派/超越派"或归中性票但注明双向张力，由 `02_research/01_agent_engineering/loop_engineering/` 的判读层裁定。

---

## Source 5 · swyx《[AINews] Loopcraft: The Art of Stacking Loops》＋同名 X thread（2026-06-12）

- 原始 URL：https://www.latent.space/p/ainews-loopcraft-the-art-of-stacking （**本环境两次实测 404**）；X 原推：https://x.com/swyx/status/2065307558198567206（X 不可达）
- 实际取证途径：plantis.ai 知识库镜像（https://plantis.ai/kb/articles/ainews-loopcraft-the-art-of-stacking-loops-99de1e7d，全文镜像取得，标注 Original: Swyx · 12/06/2026，正文含 "AI News for 6/10/2026-6/11/2026"）；AIHOT 中文镜像（https://aihot.news/items/cmqaifadr0lrkslldffycxcyd，X thread 逐字转引，时间戳 2026-06-12 13:37）。**两处均为镜像，原站不可达——引用须标"经镜像"。**
- 来源类型：个人一手 newsletter op-ed＋X thread（镜像全文取得）
- 号召力口径：①＋②——"loopcraft" 造词者，被 LangChain 官方博客《The Art of Loop Engineering》（2026-06-16）引用致谢（库内已核："This is what loop engineering — or loopcraft, as swyx puts it"）；Latent Space 主理人。
- **库内状态**：kol-roster 开放问题"swyx《loopcraft》原文 404"。**本条为增量：负结论转正——原文站仍 404，但经两个独立镜像取得全文与逐字引句，开放问题可收口。**

**逐字摘录（经镜像）**：

> "One might argue the entire game of the next century is to be able to stack loops as effectively as possible."
（X thread 首句（经 AIHOT 镜像）——世纪级修辞，非中立语体。）

> "In the early days of each phase, it will be valuable to know when to go DOWN a loop when things go wrong (for reliability)… but it will probably be more valuable to know how to go UP a loop as models improve (for leverage). If you don't figure out how to do this, don't be salty when you lose to those that do."
（他的边界 nuance：可靠性向下、杠杆向上——但整体是竞争劝导语体。）

> "Rich has his Bitter Lesson for models. We now have the Salty Lesson for agents: Don't fix things yourself, as you have done historically. Instead focus on systems that scale with more agents, like goals and orchestration."
（经 plantis 镜像的 op-ed 正文——"Salty Lesson"：不要亲手修，建随 agent 数扩展的系统。这是 loopcraft 的纲领句。）

> "We like this a lot and people don't realize how many loops we are already in"
（op-ed 开篇对 loop discourse 的总姿态：欣赏并放大。该期同时逐字转引 Steipete 月度提醒句、Boris 名句、Andrej Karpathy autoresearch 段——后者含 "you have to remove yourself as the bottleneck... I have to arrange it once and hit go"。）

**该条支持的最小主张**：swyx 是 loopcraft 命名者且持明确推动立场（杠杆优先、"don't be salty when you lose"）；其唯一的审慎维度是"知道何时降级求可靠"。
**派别适配**：**偏推动，不入中性派**。本档收录他是为了收口库内开放问题并给三派判读提供反面对照。

---

## Source 6 · Kent C. Dodds《Pragmatic Loop Engineering for AI Coding Agents》Better with Kent Ep.5（2026-06-23，14 min）

- URL：官方站 https://kentcdodds.com/better（未直接取证）；本档取证：https://castro.fm/episode/ZJERe7（含完整自动 transcript 与 shownotes，全文取得）；brapodd.se / iheart / podscan 均不可达（403/fetch failed）
- 作者身份：Kent C. Dodds——**注意：不是 Kent Beck**（前端社区 KOL，Epic React / Testing JavaScript 作者；"Better with Kent" 为其个人播客）
- 来源类型：个人一手播客（transcript 经 castro.fm 第三方转写取得——标"经第三方转写"）
- 号召力口径：③＋④——大规模分发（前端教育者，独立站/播客）；自述实践规模（"hundreds of instances of pasting this exact text in a cloud agent"）。
- **库内状态**：无此人条目。**本条为新 KOL 入册候选＋对任务线索的重要纠错**（任务方向 7 是 Kent Beck；本集是 Kent C. Dodds——名字撞车，勿混）。

**逐字摘录（经 castro.fm transcript）**：

> "I was doing loop engineering before it had a name."
（命名周后两周的表态：把新词当旧实践的标签，而非新宗教。）

> "we're not going to get to a point anytime soon I think, where you can just say agent go make me a million dollars and let it do all of that on its own where there's no stop condition needed. I do think that the human does still need to be in the loop."
（对无人值守派天花板的直接划界。）

> "And no, I don't actually use the slash goal or slash loop skill or whatever. I actually came to loop engineering as a kind of natural thing."
（不追厂商新命令——反工具崇拜的中性姿态。）

> "you do have to be mindful and careful about what your agents are able to do"
（权限边界警示，接其 pocket OS 事故故事。）

> "this can be very expensive. So you need to make sure that the things that you're using this loop engineering for are actually worth the amount of money that they're costing you. So you really, you're trading compute for attention"
（成本边界＋核心交易结构：compute 换 attention。）

> "you want to make sure that you're using loop engineering judiciously to avoid a very expensive surprise bill."
（"judiciously"——审慎使用是本集关键词。）

> "Good agents make code cheaper to generate and good loops make work cheaper to verify."
（收尾格言——把循环的价值锚定在**验证降本**而非生成放量。）

> "Or do you think it's just the next big fad thing that isn't all that useful? I think personally that this is a stepping stone to what we're going to get to."
（对"下一个 fad"质疑的回应：承认可能是过渡石——不押永久性。）

（shownotes 官方摘要句："The key idea is not removing the human. It is widening the loop so more verification happens before your attention is required."——出自官方 shownotes，可引但标出处层。）

**该条支持的最小主张**：一位大规模分发的实践 KOL 在命名周后给出完整的"受约束循环"画像：stop condition 必留、人留在环内关键位、以验证降本为目的、按成本审慎启用、警惕权限。
**派别适配**：**中性票（强）**——同时覆盖任务的三个关切：何时不该放权（million dollars 句）、人站哪（widening loop 句）、先测再信（stepping stone＋成本核算）。

---

## Source 7 · Sanderson Macedo《Stop Hand-Holding Your Coding Agent: Engineering the Loops that Replace Step-by-Step Prompting》（arXiv:2607.00038，2026-06-28 v1）

- URL：https://arxiv.org/abs/2607.00038 ｜ HTML：https://arxiv.org/html/2607.00038v1（摘要＋HTML 关键节实取核对）
- 来源类型：arXiv 预印本（cs.SE，单作者，CC BY 4.0；非同行评审结论）
- 号召力口径：**不满足硬性 KOL 门槛**——单作者、无机构背书、未核到他人引用（区别于库内已收的 arXiv:2608.21884：后者为 JAWs@ASE 2026 在审的灰色文献综述票）。**按门槛如实列"边缘候选"，不计入 KOL 台账，供判读层参考。**
- **库内状态**：无此论文条目。本条为增量（灰色文献新票）。

**逐字摘录（abs/HTML 实取）**：

> "In mid-2026 a slogan reorganized how practitioners talk about coding agents: stop prompting your agent, start designing the loop that prompts it. We take this claim seriously and give it a careful treatment."
（把口号当研究对象做"careful treatment"——学理式中性派姿态。）

> "we argue, against the stronger headlines, that it does not retire prompt engineering; loop and prompt are distinct tools with distinct uses."
（对推动派标题党的直接反驳：loop 不取代 prompt。）

> "Loop engineering moves the human along a spectrum of autonomy rather than removing the human. With a human in the loop, every consequential action is approved before it runs; on the loop, a person monitors by alert or dashboard and intervenes only on exceptions; out of the loop, the agent acts alone with occasional guidance."
（HTML 正文实取——把"人的位置"显式谱系化，与 Kief 的三层互通。）

> "seventy percent of loops verify in the autonomous zone of the ladder and seventy-four percent name their terminal states, while automated triggering and durable memory remain comparatively underdeveloped."
（对 50 个公开真实 loop 的人工编码结果——实践成熟度不均匀的实证。）

> "We close with the limits the practice must respect, including the verification burden, comprehension debt and the risk of cognitive surrender."
（三个极限：验证负担、理解债、**认知投降风险**——对放权循环的人本主义边界，中性派罕见的三连命名。）

**该条支持的最小主张**：2026-06 命名后有学术取向作者对口号做界定＋反夸大＋实证编码＋极限列举；其 "spectrum of autonomy" 与 "cognitive surrender" 可作三派判读的概念工具。
**派别适配**：中性票（证据级别：灰色文献，作者影响力未核）。

---

## Source 8 · marmelab《The State Of AI Harness Engineering 2026》复核（François Zaninotto，2026-09-24）

- URL：https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html（curl 全文实取复核）
- **库内状态**：已在库（evidence-c 4a，"Looping works…fresh-context…written down in files" 与 back pressure 收录条均已核）。**本路为复核＋两条增量段**，不重复抄全文。

**本路复核结果**：evidence-c 所录 loop 判读段逐字仍在（curl 复核通过）。增量段（同文、此前未录）：

> "In their words, 'corrections are cheap, and waiting is expensive'. A bad merge costs one extra PR to fix, while a blocked queue costs everyone, every time. But they warn that the same choice 'would be irresponsible in a low-throughput environment': the right answer depends on how much you ship."
（**适用边界的第一手表述**：同一策略在高低吞吐环境间不可迁移——中性派"边界划定"的参数化样本。注意"their"指被审计团队，原文上下文中具体指代对象需回原文段落核对后再入判读层。）

> "Atomic CRM still requires a human review for every PR."
（marmelab 自家产品的保留项：每 PR 人工评审——审慎立场的自我实践证据。）

**marmelab 后续增量负结论**：2026-09-24 之后至观测日（2026-10-06），Zaninotto 无更新的 loop/harness 主题一手文（博客索引核对：最新 AI 文为 2026-09-29 Symfony AI，作者 Adrien Guernier，非本主题）。
**派别适配**：中性偏怀疑（延续库内既有判定）。

---

## Source 9 · Walden Yan（Cognition）窗口内复核

- 库内已有：2026-04-22《Multi-Agents: What's Actually Working》全文（evidence-u S2）。**本路复核结果：2026-06 后 Walden 无新的专门一手文**（Cognition 博客以 latent.space 访谈为最新大动作）。
- 本路取得的相邻票：Latent Space《The Age of Async Agents — Cognition's Walden Yan & OpenInspect's Cole Murray》（2026-05-28，词源周前，https://www.latent.space/p/cognition ，页面全文取得前段）。**注意窗口外**，仅作谱系补充：
  - 页面内嵌 Walden X 帖（2026-04-22，经 latent.space 嵌入转引）："A year ago, I'd tell people to not build multi-agents and to focus on context engineering fundamentals. Today, many sexy ideas are still impractical, but we've found some setups that actually work"（"sexy ideas are still impractical" 是中性派语体，但他谈的是自家产品形态）。
  - 页面编辑摘要（swyx 撰）列出对谈主题含 "Why pure auto-merge vibe coding breaks down after about two weeks" 与 "the real failure mode of uncontrolled vibe coding: your codebase regressing to your worst engineer"——**这两句是 swyx 的编辑摘要语，非经核实的 Walden 逐字**，引用必须标"经 swyx 摘要转述"，不得入 Walden 引句。
- **派别适配**：受约束形态的代表性人物（写入单线程/manager 拓扑），但作为 Cognition CPO 其发表带厂商利益；归"偏推动中的受约束支"或单列，由判读层裁定。中性票**不足**。

---

## 不支持什么 / 负结论

1. **Kent Beck（任务方向 7）**：未找到 2026-06 后对 loop engineering 的专门一手发声。其 Substack"Still Burning"系列可核到的集数为 2026-03-25《Nobody Knows》、04-08、04-22、05-06《Did We Do This to Ourselves?》，全部窗口前；库内已有 2025-06-25《Augmented Coding》（evidence-i Source 3）。**本路复核结果：无增量，窗口内沉默。**
2. **Peter Steinberger "Loop 时代终结"推文（2026-07-18）**：X 不可达，原文未取得。仅有 InfoQ/36kr 媒体转述（https://eu.36kr.com/en/p/3904771418867330 ，2026-07-21，署名 Tina）与 c114 转载——按门槛**媒体转述降级，不作 KOL 一手票**。转述细节（"Are we still talking about loops, or have we moved on to graphs?"、260 万浏览、六周前 840 万浏览的 design loops 帖、Luis Catacora 回帖 "Loops have a lot of fault tolerance. Graphs force you to acknowledge how much of the workflow isn't really modeled at all."）可供判读层作背景线索，但均须标"经媒体转述、未核原文"。
3. **swyx loopcraft 原文**：latent.space 原帖 URL 404（两次实测），unrollnow thread 阅读器 503（三次）。全文仅经 plantis.ai／AIHOT 两镜像取得（Source 5，已标镜像）。
4. **Simon Willison**：未找到 2026-06 后对 "loop engineering" 专名的专门发声；其《Agentic Engineering Patterns》指南（https://simonwillison.net/guides/agentic-engineering-patterns/ ，索引页实取）自述始于 2026-02-23，窗口前。**维持 kol-roster（`02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md`）既有负结论**（不升 §A）。
5. **Kief Morris 新文章**：不存在单独的《Human on the Loop》martinfowler 文（404；系列索引无）——Luca Berton 转述时改了 2026-03-04 文的标题。PlatformCon 演讲视频本体未取得（官方 session 摘要＋关键点已代替取证）。
6. **Böckeler 对专名的态度**：S1/S2 两篇一手均围绕 agentic loop 机制，未检出她采用或评述 "loop engineering" 专名的段落——"她对运动本身的表态"仍缺直接文本，现有证据只能支持"对循环内实践的审慎实证"。
7. **O'Reilly《What the Hell Is a Loop, Anyway?》**（https://www.oreilly.com/radar/what-the-hell-is-a-loop-anyway/）：403 Access Denied，作者与内容均未能核实——不入册。
8. **Thoughtworks 新文《An Accidental Blackboard》**（Giles Edwards-Alexander，2026-09-02，https://martinfowler.com/articles/exploring-gen-ai/an-accidental-blackboard.html ，全文取得）：10 人团队 4 天用全 agentic 实践造出 IROps 系统，意外发现 repo 作 blackboard 协调模式；作者自述 "because it was accidental... I'm not convinced I would be able to reliably prompt our agents into doing it again"。质量门槛上作者非本主题 KOL（无定义/被引/规模证据），**不入册 KOL**，记为中性倾向的团队实证线索（"emergent, not directed"）供判读层参考。
9. **Huntley 十八个月复盘正文**：付费墙，仅取得引介＋前段 transcript（S4c 标注截断）。
10. **HN/Reddit 社区情绪**：按门槛本轮未收，也未另行整理（时间预算内未做社区情绪小节）。

---

## 对本档案的诚实评估

1. **中性派证据强度：总体强，但集中在两个机构点。** 最硬的证据是 Böckeler（两篇一手：自跑 eval＋主流播客，自我设限措辞完整）与 Kent C. Dodds（完整"受约束循环"画像，三个任务关切全覆盖）；Kief Morris 官方文本提供"渐进信任"这一关键中性句；marmelab 提供参数化的适用边界。这几条足以支撑中性派作为独立一派的成立。
2. **该归别派的人**：swyx 实测为**推动派**（"entire game of the next century"、"don't be salty when you lose"），不应进中性名单——本档收录他只为收口 404 开放问题＋提供对照。Walden Yan 是"受约束形态"代表但厂商身份使其中性票不足。Huntley 是最难归类的：对专名沉默＋对原语自我祛魅＋对 discourse 疏离，但目的地方向（消灭可读性要求、消灭编译循环）比多数推动派更激进——建议三派重组时考虑"重构派"独立或在中性派内单独标注。
3. **最大的覆盖缺口：专名层面的中立表态几乎全部在 X 上。** Steinberger 的"终结宣言"（2026-07-18）、Cherny 的后续表态、swyx 的 thread——这场"这个词该不该存在"的争论主战场 X 不可达，本档只能靠媒体转述与镜像。因此**中性派在"术语层"的证据显著弱于其在"实践层"的证据**。中文媒体（InfoQ/36kr）的转述链本身未核原文，作背景线索用。
4. **边缘件**：arXiv:2607.00038（S7）的 "spectrum of autonomy"／"cognitive surrender" 是很好的判读工具，但作者不满足 KOL 门槛，只作灰色文献票；《An Accidental Blackboard》同理。若判读层引用它们，须与 KOL 票分层标注。
5. **名字陷阱提醒**：本档最重要的流程纠错是 Kent Beck ≠ Kent C. Dodds（Source 6）。三派重组落表时两行都要写清，避免"Kent"撞名污染台账。

## 第三轮挖掘（2026-10-06）：新 KOL（中性与播客会议层）

> **本轮通道状态总览**：web_fetch 对多数域名报解析异常（non-public IP），全部改 curl＋浏览器 UA 实取；逐字引句均来自实取页面。播客层两个重要新载体：**The Weekly Dev's Brew**（Jan-Niklas Wortmann，wordman.dev，页面自带 Key Takeaways＋Pull Quotes＋页内全 transcript）与 **AIEWF 2026 官方 llms-full.md**（会议层全量议题页，2.8MB 实取）。

### Source A · Sean Goedecke（Google SWE，seangoedecke.com）· 窗口内五篇一手全文（2026-06-01 → 09-27）

- 通道：curl 直取 atom feed（30 条清单）＋博客分页 6 页逐页核日期；正文 5 篇逐字实取（另有 5-31 篇窗口前相邻票）。
- 身份：Google 软件工程师，个人博客为 AI 工程圈高引用源（本窗口内每月 5-8 篇的稳定发声）。
- 号召力口径：②＋③＋④（被 daily.dev 教程、泰语技术媒体等转译引用；HN 高分发）。
- 逐字摘录（全部实取）：

> "my primary value is not that I help the AI write better code, it's that I align the AI with the values of my organization. Human-AI partnerships are for alignment, not capability."（《Human-AI partnerships are for alignment, not capability》，2026-09-27）
>（同文承认 agent 能力已越过自己："When I ask agents to write code, they make fewer mistakes than I do and are orders of magnitude faster."，同时否定无人值守："Purely vibe-coding at work produces awful outputs. But they're not awful because they're bad code, they're awful because they're in bad taste"，并点名回击 "Vibecoding maximalists like DHH argue that…we ought to stop reading the code…If it were just about capability, they might be right."）

> "There is thus going to be enormous pressure to do agentic coding in languages with fast compilers and tests, like Golang, and to tightly optimize the dev loop in agentic codebases."（《Slow developer experience will bottleneck fast models》，2026-09-14——**把"优化 dev loop"立为下一阶段工程科目**；同文："we may see a return of DevEx in the late 2020s, focused on speeding up the experience for AI agents."）

> "There are lots of just-so stories floating around (like that AI agents prefer statically-typed languages because the feedback loop is tighter), but when you actually measure it seems really unclear which tools agents use better."（《Don't build tools for AI agents》，2026-09-12——对 "X for AI agents" 浪潮的测量主义怀疑，直接点到 feedback loop 叙事）

> "give the agent context on your priorities, not just on the specific task you want them to do."（《Tell agents the why, not just the how》，2026-09-15）

> "This list is a kind of existence proof: a bunch of weird projects, useful to at least some people, that would not have existed without AI assistance."（《Weird projects I shipped with AI》，2026-06-01）

- 窗口前相邻票（不入窗口，注记）：《Build agents, not pipelines》2026-05-31、《Programming (with AI agents) as theory building》2026-04-03、《Prompts are technical debt too》2026-05-20。
- **最小主张**：人机分工的新均衡＝"对齐优先于能力"：agent 出码、人出价值观与 trade-off 排序；loop 的下一个瓶颈是 dev loop 本身的速度。
- **派别适配**：**中性**（对齐派；既反"不读码"极限派、也承认能力反超——两面向都有硬表述）。

### Source B · Dan Abramov ·《How I Vibed a Proof of Conway's Conjecture》（overreacted.io，2026-09-18）

- URL：https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/ （curl 实取，全文 117 段；页内日期 September 18, 2026）
- 身份：React 核心前成员，前端圈最高分发技术博客之一。
- 号召力口径：④。
- 逐字摘录（全部实取）：

> "It took me an entire month of my free time and a boatload of tokens, but I believe I've obtained a Lean proof of this conjecture posed by John Conway 50 years ago"
>（外行用 agent 一个月拿下 Conway 猜想 Lean 证明——"无人值守"叙事的极限案例；同文自我设限："My proof has not been independently verified by mathematicians."）

> "This let me keep the harness running for days. I didn't understand the math so I limited my involvement to poking the agents, asking what they were doing, and experimenting with their workflows."

> "I set up a 'cafeteria' agent that relayed every message it received to every other agent (emulating a group chat)."

> "I also kept an eye so they don't introduce 'process theater' with audits, as they liked to replace work with bureaucracy."
>（对多 agent 自组织的一手负样本：审计倾向滑向官僚化。）

> "In a sense, I felt like I'm a nontechnical engineering manager rallying a talented but terribly distractable team around a plan that they've promised me would work."

> "However, the models would repeatedly drift and fail to structure the engineering work, so in that sense the answer is no. That said, I believe my role could have been (better?) fulfilled by a dedicated agent that is taught to project-manage other agents, watch out for when they're spiraling or need to be poked."
>（对"人该不该在环上"的双向答案：既证明人可被替代，又实录 drift 失控——本项目"停止条件/外层调度"议题的一手民间数据点。）

- **最小主张**：无人值守多 agent 实验的完整一手复盘——可行性（存在性证明）与失控面（drift/官僚化/需人当"非技术工程经理"）同时入档。
- **派别适配**：**中性**（两面向全；"角色可被项目管理 agent 替代"半句同时是推动派引句）。

### Source C · Dex Horthy（HumanLayer CEO）· AIEWF "great loops debate" 反方＋播客长访谈（2026-07-02 / 08-13）

- C1（经现场稿转述）：https://www.latent.space/p/aiewf-daily-dispatch-locomotives （Richard MacManus，07-03，curl 实取）：
  > "The basic take here is not whether loops are good or bad…Kubernetes is actually built on loops — built on control loops. But they're deterministic loops."
  > "the hype is outrunning the discipline."
  > "I haven't seen proof that we are at a point where we can just step up an abstraction level…I actually think we need to step down an abstraction level, if anything."
  > （软件工厂段落）"you never touch the problem"——建议"build up intuition"、从小 loop 迭代起步而非端到端自动化。
- C2（主持人页内 pull quotes＋全 transcript 在页）：The Weekly Dev's Brew Ep21《What Actually Gets You 2-3x With AI Coding》（2026-08-13，https://www.wordman.dev/podcast/dex-horthy-what-actually-gets-you-2-3x-with-ai-coding/ ，curl 实取）：
  > "You can get 99% of human-quality code, like very good code as if you had written every character by hand, but two to three times faster. You can't get 10x. It can't be done. Not today."
  > "I don't give two damns how your spec is shaped. It should give you leverage."
  > "I think abandoning code quality and system quality, giving engineers permission to ship slop, I don't think that's correct. I think that's going to collapse your codebase into ash much faster than you think."
  > "If you're a manager and you are not trying to help your people adopt AI, you are failing them."
  - 章节含 **"1:14:01 · Vibe coding vs production loops"**；官方 Key Takeaways 含 "Kill a session when the model starts flailing on tests."；Mentioned 清单含 **"Addy Osmani on Loop Engineering"**（其单集官方页面即在引用在册 KOL 的 loop engineering 内容——传播链证据）。
- 身份：HumanLayer CEO/联创；页面 bio 称其 "coined 'context engineering'"，12-Factor Agents 作者。
- 号召力口径：②＋③＋④（AIEWF 主舞台辩手＋头部 newsletter 生态人物）。
- **最小主张**：反的是"无纪律 loop 的 hyper"，不是 loop 本身；生产语境天花板 2-3x；review 是瓶颈、人的时间应花在设计与拆解上。
- **派别适配**：**中性**（辩论反方席但自述 "not anti-loops"——教科书式中性席位）。

### Source D · Darren Shepherd（Obot AI 创始人，Rancher 联创）· The Weekly Dev's Brew Ep23（2026-09-24）

- URL：https://www.wordman.dev/podcast/darren-shepherd-ai-agent-sandboxes/ （curl 实取；@ibuildthecloud）
- 号召力口径：③（Rancher/Kubernetes 生态知名人物）。
- 逐字（页内 transcript 实取）：

> "you have kind of like the internet hosted agentic loop. But then you also have the Codex CLI and Claude Code that agentic loop, which is client-side and the better architecture is the client-side one. It's not the centralized one. Because the centralized one just has…"

- 官方 Key Takeaways（host 撰，页面实取）："**Sandbox the agent loop, not only the tool calls.** The loop directs code that holds secrets and talks to external systems, so the agent and its tools belong in one sandbox with one policy."＋"Egress is the policy surface, not ingress."＋"Output is not progress. Letting a model barf out thousands of lines feels productive until the regressions pile up, and one estimate raised in the conversation puts a skilled engineer's real gain at around 5 to 10 percent."
- **最小主张**：把 loop 治理落到基础设施层——沙箱边界应包住整个 agent loop（agent＋tools 一个沙箱、一个 egress 策略），而非只包工具调用。
- **派别适配**：**中性**（架构派；"output is not progress" 与 5-10% 实际增益估计带清醒怀疑色彩）。

### Source E · 播客层群像（2026-06 后，按证据强度分档）

1. **Latent Space 2026-07-08**：Akshat Bubna（Modal CTO）《Why AI Infrastructure must evolve for Agent Experience》（58min）——经 SignalCast 周报页实取摘要（https://www.signalcast.app/this-week/latent-space/2026-07-06 ）："as AI moves from static model serving toward autonomous decision-making, the underlying platforms must fundamentally rethink how they allocate resources and handle unpredictable execution patterns."（**经摘要转述档**；latent.space 站内正文未取——sitemap/分页均 404）
2. **SE Radio 740**：Raju Dandigam《Building Production AI Agents》（2026-09，https://se-radio.net/2026/09/se-radio-740-raju-dandigam-on-building-production-ai-agents/ ，curl 实取官方简介）："The episode covers behavioral testing against contracts, golden scenarios, and observability that captures the full execution path rather than flat logs, which is the gap behind agent-inspect and its readable execution trees."（官方简介档；SE Radio 不附 transcript）
3. **SE Radio 732**：Jason Gorman《The Effective Use of AI For Software Development》（2026-08，条目级；正文未取）。
4. **Insecure Agents**（Socket 出品，host Allie Howe）：单集《A Reference Architecture for Securing "Software Factories"》（Aaron Stanley / Ahmad Nassri）与 David Cramer 单集（见怀疑档）——iHeart 406，日期未核。
5. **The Weekly Dev's Brew**（Jan-Niklas Wortmann，wordman.dev）：本轮播客层最大发现源——单集页自带 Key Takeaways＋Pull Quotes＋**页内全 transcript**；窗口内 loop 相关四集：Cramer（06-30）、Horthy（08-13）、Mulroy（09-10）、Shepherd（09-24）。主持人摘要语体审慎，可作"经主持人整理档"引用。

### Source F · 会议层数据点（AIEWF 2026 官方全量页＋现场稿）

- **Barr Yaron（Amplify）年度调查**（经 MacManus 现场稿转述）："According to Amplify's data, 95% of respondents now use agents — roughly double last year's share. Among teams using agents, 89% said those agents could write data, up from 52% the previous year."＋"The controls, however, remain comparatively primitive. Human approvals and permissions were the two leading safeguards…"
- **Allie Howe（Keycard）主持设问**（现场稿直录）："is there or is there not a delta between the hype behind loops and what actually works in practice?"
- **Ameya Bhatawdekar**《Your Agent Evolved. Your Evals Didn't.》（llms-full.md 官方摘要实取）："Agent architectures have evolved through six generations; prompt, chain, ReAct loop, workflow graph, modern agent loop, AI harness. And each one quietly breaks the eval strategy of the generation before it."（六代架构谱系句——判读层可用的官方分期表述）
- **Sonar AC/DC**（Anirban Chatterjee）官方摘要（同页实取）："the critical challenge has shifted from generation to verification…making cognitive surrender among human reviewers an acute risk."（"cognitive surrender" 在会议层官方摘要中出现）
- **派别适配**：中性（数据与设问层，非个人 KOL 票）。

### Source G · .NET 线（David Fowler）· 经转引链（2026-09-05）

- 原始载体：Fowler X 帖（X 不可达）；一级转引：Windows Latest《Microsoft engineer says "typing code is absolutely over," and Windows 11 is already being built that way》（2026-09-05，https://www.windowslatest.com/2026/09/05/microsoft-distinguished-engineer-says-typing-code-is-absolutely-over-and-windows-11-is-already-being-built-that-way/ ，curl 实取全文）；二级转引：mynavi（2026-09-08，实取）。
- 身份：Microsoft Distinguished Engineer（SignalR/NuGet/ASP.NET Core 核心，现负责 .NET Aspire）。
- 可引用层级：标题句 **"Typing code is absolutely over"**（经 Windows Latest 转引）；WL 的定性段落（**WL 作者语，非 Fowler 逐字**）："The tools for software development are being redesigned so AI can operate inside the loop."；WL 转述其团队 2026-04 文：AI agents "really good at writing code" 但 "generating code and shipping a full working app" are "very different things"，Aspire 方案＝"letting agents start services, read logs, inspect telemetry, restart what's broken, and test again, without a human copy-pasting error messages back into a chat window."（**这正是"服务起停-观测-重启-再测"的 loop 结构描述，经转述档**）
- 官方博客旁证（devblogs.microsoft.com/aspire feed 实取）：窗口内 Aspire 13.4（2026-06-01）/13.5（08-18）/13.6（09-29，"point your coding agent at them to compare and contrast between runs"——dashboard 记忆化 run 库）。
- Steve Sanderson：**负结论**——窗口内未检出 agent loop 一手。
- 号召力口径：③＋④。**派别适配**：中性偏推动（全部经转引链，票弱，判读引用须降档）。

### Source H · QCon 上海 2026（中文议题——非英语层，边界登记不入英语 KOL 册）

- 官方议题页（搜索命中，未 fetch 正文）：《Code Agent 的 Loop 工程实践：网易智企 CodeWave 的探索与落地》（https://qcon.infoq.cn/2026/shanghai/presentation/7340 ）；另《从 Harness 到 Loop：阿福 Agent 小队如何处理持续涌入的线上 Badcase》（头条转述）。
- **登记含义**："loop 工程/从 Harness 到 Loop" 专名已在中文会议层流通——传播层证据，不计 KOL 票。

### 负结论（第三轮·中性）

1. **Software Engineering Daily**：窗口内相关单集存在（《Docker and Sandboxing AI Agents》《The Terminal as an Agentic Interface》《SED News: OpenClaw Goes Viral…》）但 listennotes/podcastaddict 反爬 403，日期、嘉宾与逐字均未核——开放。
2. **Pragmatic Engineer Podcast**：窗口内 loop 专题单集未定位（仅 2026-02-03 Steinberger《Closing the Loop》窗口前票，cast42 笔记层）。
3. **TWIML**：本轮未及专项核查（通道未开）。
4. **GOTO Copenhagen 2026**（gotocph.com/2026/schedule，10-01 场）：未及扫描——开放。
5. **Goedecke "AI engineers" 一篇**：任务提示中的篇名未在其站内清单检出（atom feed＋6 页分页均核），疑似记忆偏差或改题；已有五篇窗口内一手足以立票。
6. **撞名警示**：sindre-ai（GitHub API 实核：2026-03-25 注册、"Sindre AI"、0 followers）≠ Sindre Sorhus；maskin 仓库不入册。
