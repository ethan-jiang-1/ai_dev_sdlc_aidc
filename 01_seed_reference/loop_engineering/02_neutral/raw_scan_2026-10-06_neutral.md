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
