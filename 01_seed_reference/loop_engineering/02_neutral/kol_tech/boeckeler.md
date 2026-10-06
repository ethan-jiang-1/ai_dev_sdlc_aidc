---
type: kol_evidence
directory: 02_neutral/kol_tech
observation_date: 2026-10-06
---

# boeckeler — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：Thoughtworks Distinguished Engineer，AI-assisted delivery 专职角色（2023 起全职投入该领域）
> **背景**：Birgitta Böckeler——德国；Thoughtworks Distinguished Engineer，2023 年起公司内首个 “AI-assisted delivery” 专职研究角色；martinfowler.com《Exploring GenAI》系列主笔；steering loop / guides-sensors 概念提出者（台账 §B）。
> **号召力**：①＋② guides/sensors 定义者
> **人物全景**：[_raw_people/20_birgitta_bockeler.md](../../../voices/_raw_people/20_birgitta_bockeler.md)
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**方向**：审慎实证持续（方法一致、结论未定）
**起点**：审慎实证（harness engineering 系列延续）
**终点**：审慎实证（'even best practices need evals'）
**弧线**：07-22 SE Radio 裸基线先行 → 08-10 TDD-in-loop eval 证伪默认信条（'until I see evals'）
**关键转折**：08-10 自跑 eval 证伪循环内 TDD 有益——方法论驱动，非立场翻转
## Birgitta Böckeler 于 SE Radio 730（2026-07-22）

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

## 《TDD inside the agent loop - theater or actual value?》（2026-08-10）

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

---

# 增量补挖（2026-10-07 第二轮：09-01→10-06 增量）

> 通道：martinfowler.com master feed（抓至 2026-10-04，确认她窗口内无新文——作者页与 genai 系列页 404/403，缺口由 master feed 补判）；LinkedIn 免登录渲染页实取（登录墙下正文与部分评论可见，"See more comments" 以下不可达，如实标注）。

## LinkedIn 后续贴：回应 Emily Bache，重申暂不让 agent 做 TDD（2026-09-30）

- URL：https://www.linkedin.com/posts/birgittaboeckeler_the-last-year-has-changed-everything-i-knew-activity-7511156369211973634-NBTC （免登录渲染页实取全文；缓存 boeckeler-linkedin-post-tdd-followup.txt）
- **与 loop engineering 的挂钩**：**验证回路**——TDD 是"放进 agent loop 的经典验证实践"，此条是她 08-10《TDD inside the agent loop》之后的最新表态：loop 内验证该装什么仍未解决。
- 逐字摘录：

> "I personally do not ask my agents to do TDD for now, because of two things:"

> "it did create some hypotheses why it might make quality worse or not make much of a difference, at high token cost."

> "most of the benefits of TDD are for the human, in a way that definitely goes away when the agent does it by itself, so we have a huge gap to fill there with other practices."

> "many people seem to take it for granted that agents get the same benefit from TDD as we do"

> "To get agents to refactor more, we need to use much more than TDD to get them to do that"
（08-10 文的实证结论被她本人确认沿用：TDD 收益属人类、token 成本高——对"把人类验证实践原样搬进循环"持续保留，需 sensors/habit hooks 与严格 eval 补位。）

- 立场：**复合（loop 内验证实践暂缓＋替代机制探索）**。

**本轮最小主张**：Böckeler 09-10 月唯一增量＝09-30 LinkedIn 贴：重申暂不让 agent 做 TDD（收益属人类、成本高、需严格 eval 与 sensors 补位）——验证回路内容物仍在探索，审慎立场未变。10-01 职业贴（宣布转投 Unblocked 做上下文工程）不挂七类钩，按底线弃收——轨迹注记：她的关注点从 loop 内验证转向 loop 外上下文设施。其余通道（martinfowler.com、个人 newsletter、bsky/mastodon）窗口内无新发声。
