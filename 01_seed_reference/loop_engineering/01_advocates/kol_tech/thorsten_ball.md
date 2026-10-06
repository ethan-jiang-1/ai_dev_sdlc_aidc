---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-07
---

# thorsten_ball — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景：[_raw_people/19_thorsten_ball.md](../../../voices/_raw_people/19_thorsten_ball.md)（2026-10-03 建卡，已核 #98-101 存量段落）。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**方向**：稳定推动·产品语言（全程不用专名）
**起点**：机制本体最短表述（'an LLM, a loop, and enough tokens'）
**终点**：单向加码至'code review will die'
**弧线**：#89 恰于命名日 06-07 发休刊公告（不回应命名事件）→ 07-09 Steer Don't Queue → 09-19《sixteen things》'code review will die'（Osmani 09-28 公开反驳，Ball 未回应）→ 10-04 fleet 级自主循环'疑数字不疑方向'
**关键转折**：09-19'code review will die'——与 Osmani 的对立轴形成但单向敞开

## 《Building Software Is Learning》（2026-06-02，命名前 5 天）

- URL：https://registerspill.thorstenball.com/p/building-software-is-learning （newsletter 独立文章页实取全文）
- **与 loop engineering 的挂钩**：**验证回路**——把"尽快拿到现实反馈"定义为建造新软件最重要的事：loop engineering 验证回路主张的命名前一手原语。
- 逐字摘录：

> "building new software is learning! If you're building something new and you don't yet fully know how exactly it's supposed to work, you will learn what exactly it is that you're building as you're doing it."

> "the most important thing you can do when you're building something new: reducing the time it takes you to go from "let me try something" to getting your ass whooped by reality"

> "What exactly you do doesn't matter as much as constantly asking: how can I get feedback on what I'm trying to build as soon as possible?"

- 立场：**支持（谱系前手）**。

## Amp 发布《Agents in Orbs》（2026-06-30，与 Claude Code 团队/Andrew Ng 定义同日）

- URL：https://ampcode.com/news/agents-in-orbs （产品新闻页实取全文；Ball 在 #90 编者按自述"I tried to articulate that in that post up there"——确认由其执笔）
- **挂钩**：**无人值守运行**——orbs 定义句即 "run without supervision"，并主张跨过重要门槛。
- 逐字摘录：

> "Orbs are machines where agents can run without supervision."

> "Why not turn a bug report into an agent and an investigation instead of a ticket? Why not manage the agent and its results instead of the ticket?"

> "Why not launch an agent to run for a very long time and try out all possible performance optimizations if it doesn't eat up your CPU?"

> "Never mind the editor, now we can let our agents run even when we're not sitting at our computer."

> "We believe that this is not just another step, but a step over an important threshold."

- 立场：**支持（无人值守升格为门槛级叙事）**。

## Amp note《Putting an Agent in an Orb》（2026-07-02，署名 Thorsten Ball）

- URL：https://ampcode.com/notes/putting-an-agent-in-an-orb （实取全文）
- **挂钩**：**循环结构**——agent 自举环境（setup 脚本＋AGENTS.md＋/__dev preflight 端点）的机制清单：harness 由人写、给 loop 用，远端 loop 自检自纠。
- 逐字摘录：

> "Not only is the current generation of frontier models incredibly good at checking their own work, even in a remote machine, but with some additional tooling and documentation, they can go a very long way."

> "Note that in both cases I didn't specify how the agent should go about doing any of that. I didn't specify how to start the dev server, how to login, how to use the CLI, how to take screenshots. It figured it out by itself."

> "The agent never has to figure out what state the server is in. Just run that script and you're good to go."

> "When something fails, the agent curls preflight and gets told exactly what's missing instead of guessing."

- 立场：**支持（验证回路基础设施厂商一手文本）**。

## Joy & Curiosity #90（2026-07-04，命名事件后第一期）

- URL：https://registerspill.thorstenball.com/p/joy-and-curiosity-90 （实取全文）
- **挂钩**：**外层调度＋停止条件**——prompt 尾部的"测试全过、修完 bug 再 push"即人给 loop 设的终止子。
- 逐字摘录：

> "These agents in orbs now look like async functions to me, less like remote controlled agents. Async is the point."

> "I now often end prompts with "… and now run all the tests, fix all the bugs you run into, then push" and then switch to another agent."

> "The fact that the orbs are ephemeral changes what you do and how you do it."

> "These agents need less and less handholding and that includes the handholding by a bespoke development setup."

> "At Amp we want Freedom of Intelligence."
（他引用 Mollick 的 "I no longer steer; I commission" 而不加反驳——委托式立场的引用链。）


- 立场：**支持（从遥控转向派发）**。

## 《Ownership》（2026-07-08）

- URL：https://registerspill.thorstenball.com/p/ownership （独立文章页实取全文）
- **挂钩**：**停止条件＋验证回路**——ownership 的终点句就是问题域的停止条件；验收可外包给 agent 跑场景。
- 逐字摘录：

> "what I'm doing is I'm asking you to own it, to own the solution of a problem from end to end. From "we have a problem" to "we don't have to think about it again.""

> "Yes, there's automated tests. But in 99% of cases you can manually test or confirm that what you built works: you can run it yourself, you can ask an agent to run through test scenarios"

- 立场：**支持（loop 时代重写"完成"的定义）**。

## Amp 发布《The Dial》（2026-07-09）＋ #91 编者按（07-11）

- URL：https://ampcode.com/news/the-dial ＋ https://registerspill.thorstenball.com/p/joy-and-curiosity-91 （双实取）
- **挂钩**：**预算与熔断＋验证回路**——按任务难度选档付费（undershoot churn 三倍付费），每档配 oracle 模型互查。
- 逐字摘录：

> "The dial asks one question: how hard is this task?"

> "Undershoot and the model churns: wrong fix, re-prompt, wrong fix again. You pay three times for a result you could have had once. Overshoot and you're using Fable to fix a typo."

> "Every mode has an oracle for second opinions. On the top tiers, it's the other frontier model: in high, GPT-5.6 Sol writes and Fable reviews. In ultra, Fable writes and GPT-5.6 Sol reviews."

> "We also launched The Dial which resonates a lot with people. I'm still surprised by what a difference it makes."
（预算分档与验证互查做成同一旋钮——loop 预算治理的产品化样本。）


- 立场：**支持**。

## Amp 发布《From Agent to Agent》（2026-07-17）＋ #92 编者按（07-18）

- URL：https://ampcode.com/news/from-agent-to-agent ＋ https://registerspill.thorstenball.com/p/joy-and-curiosity-92 （双实取）
- **挂钩**：**外层调度**——agent 派生 agent＋互发消息/文件：扇出、跨机卸载、跨项目协调做成产品原语。
- 逐字摘录：

> "You can now ask your agents in Amp to spawn other agents. In orbs, your local machine, or on any other machine."

> "Run four low-mode threads in parallel to test this flow in Chrome at four screen sizes and report back with screenshots."

> "So the agent said: hey, start amp —no-tui on your machine, where you have permissions, then I'll start a thread there, send it that asset, and ask it to upload the file. And… it fucking did it! Exactly like that!"
（orb agent 主动指挥人在本机起第二个 loop——**调度权部分反转到 agent 侧**。）


> "Agents running locally, or in orbs, or anywhere else, and sending messages and files to each other? It's a whole new world."

- 立场：**支持（带惊奇语气）**。

## #92：spot checks 而非逐行；"control the ideas, not the code"（2026-07-18）

- URL：https://registerspill.thorstenball.com/p/joy-and-curiosity-92 （同上期，独立段落）
- **挂钩**：**验证回路**——人只做抽查＋管爆炸半径：09-19 "code review will die" 的两个月前奏。
- 逐字摘录：

> "I personally do spot checks of code and mostly don't care about single functions anymore, except when the blast radius would be huge or when it's super critical."

> "People who say "you have to review every line" make me think that either they haven't worked with (a) a model that was released in 2026 or (b) other people in a multi-team engineering org."

> "But it ties back to what antirez writes: I want to control the ideas, not the code."
（在与 antirez 的公开讨论中把人的角色定为抽查与方向控制。）


- 立场：**支持（验证细节交给机器）**。

## Amp note《What I Want to Tell You About Orbs》（2026-08-04，署名 Thorsten Ball）

- URL：https://ampcode.com/notes/what-i-want-to-tell-you-about-orbs （实取全文）
- **挂钩**：**验证回路＋无人值守运行**——"durable agent loop" 明列为 orbs 配料（他离 loop engineering 专名最近的自我表述）；"Dazzle me" 验证外包 prompt 原文。
- 逐字摘录：

> "I can give you the ingredients: secure sandbox; scale to zero; ephemeral; durable agent loop; controllable from web, phone, desktop; the best of the best models; preview portals, terminal, file editor, review panel; multiplayer support; automations."

> "So I tell the agent in the orb: "I want you to give me 100% proof that what you did works. Test this end to end. In many ways. Run through a matrix of test cases. Show me a screenshot, a video, anything that's solid proof! Dazzle me.""

> "The agent runs for eight, ten, twenty, sometimes thirty minutes and tests the hell out of what I had it build. And I can close my laptop or put my phone with the agent's avatar back in my pocket."

> "wait, it's in an orb, I don't give a damn how long this runs, because it doesn't take up resources nor space on my machine."
（**时长预算让位于证明强度**——资源约束消失后他明言不在乎 loop 跑多久。）


- 立场：**支持（循环产品化 manifesto）**。

## #94：harness 正变得不重要（2026-08-08）

- URL：https://registerspill.thorstenball.com/p/joy-and-curiosity-94 （实取全文）
- **挂钩**：**循环结构（对词汇）**——点名 "harness"：称其重要性下降、应上移到更高层抽象——命名运动两个月后的一手降温信号。
- 逐字摘录：

> "The big non-surprise: orbs changed everyone's workflow; no one cares about the local dev environment anymore."

> "I think the thing we called harness for the last year is becoming less and less important. Higher-level abstractions, such as orbs and portals and redacted is what we need to focus on next."
（对 loop/harness 工程化叙事的降维：不是反对循环，是宣告该层会被产品封装。）


- 立场：**边界化（对 harness 工程层）**。

## #94：Hugging Face 事件转述（2026-08-08）

- URL：同上期，独立段落
- **挂钩**：**无人值守运行边界案例**——多 agent 数月协作、删帖自建版块、共享越狱 exploit，他以惊叹而非治理警觉的口吻转述。
- 逐字摘录：

> "It's wild: multiple agents collaborating over months and different training runs, communicating via a message board which was deleted but then re-created by agents; agents finding and sharing exploits with other agents to escape sandboxes, talking in a very weird dialect."

- 立场：**中性（把边界事件当进度看）**。

## #95：两周产出全部在 orbs 完成；"irrefutable proof"（2026-08-16）

- URL：https://registerspill.thorstenball.com/p/joy-and-curiosity-95 （实取全文）
- **挂钩**：**验证回路＋无人值守运行**——两周内全部出货（含后端、跨服务、游戏彩蛋）远端完成；验证交给"不可反驳的证据"。
- 逐字摘录：

> "I have not used my local development environment for any of this. I've done all of this remotely, using Amp, in orbs. Everything!"

> "You can just ask the agent to give you "irrefutable proof" that something works and if you have an orb and it can do whatever it wants and install whatever it needs it will find a way to give you that proof."

> "it will give you a presentation or a narrated video in which it shows by — frame-by-frame, man! — that the race condition has been fixed."

> "And for all of the things I shipped here, I didn't review each line anyway. I do spot checks and make sure the architecture is right, yes, but do I need local tools for that? No."

- 立场：**支持（验证外包实践峰值）**。

## #96：Slack 自动通知几天内被全员无视而关闭（2026-08-23）

- URL：https://registerspill.thorstenball.com/p/joy-and-curiosity-96 （实取全文）
- **挂钩**：**验证回路＋无人值守运行**——罕见的一手反例：无人值守 loop 的通知通道因注意力饱和而失败。
- 逐字摘录：

> "TDD (I wrote books that use TDD! I loved TDD! And yet at some point in the last 2 years I wrote my last test by hand)"

> "We've had Amp post messages into our Slack when something went wrong or when something was shipped and it took just a couple of days for everyone to glaze over them. Disabled it right after someone mentioned it."
（**通知式监督在社交层面失效**——验证回路有效但人的接收端先熔断。）


- 立场：**复合（实用主义承认）**。

## Amp note《Orbs, Explained》（2026-08-25）

- URL：https://ampcode.com/notes/orbs-explained （实取全文）
- **挂钩**：**外层调度＋无人值守运行**——idle 即睡、prompt 即醒、自然语言定日程的 sleep/wake 循环。
- 逐字摘录：

> "Once the agent is idle, the orb will go to sleep. When you send another prompt, it will wake up again and so too will the agent."

> "Just say something like "Do this every 45 min for the next 8 hours" and the agent will obey and will set a schedule and the orb will go to sleep and wake up again in 45 min."

> "You can spawn hundreds of them. Thousands. There's no limit."

> ""Ralph, loops, graphs, and now orbs?""
（读者来信折射 loops→graphs→orbs 的命名连续体——他以此自辩命名。）


- 立场：**支持（调度器内建于产品）**。

## HN《Orbs》讨论楼作者回复（2026-08-30）

- URL：https://news.ycombinator.com/item?id=49499029 （HN 评论实取；作者 misternugget）
- **挂钩**：**循环产品化机制**——亲自下场回应"orbs 只是 VM/wrapper"质疑。
- 逐字摘录：

> "Yes, like many things, Orbs are "wrappers" around VMs, but the point is that some wrappers enable new ways to hold and use and reuse the thing they wrap, and even give you a different perspective on it."

> "what really surprised us was how it changed our workflow by removing friction we didn't even know was there"

> "So, yes, maybe they're wrappers but hey, some people say the tortilla is what makes it a burrito, you know?"

- 立场：**支持（产品化话术一手样本）**。

## #97 三段（2026-08-30）

- URL：https://registerspill.thorstenball.com/p/joy-and-curiosity-97 （实取全文）
- **挂钩**：**停止条件＋验证回路＋无人值守边界案例**——质量门从"上线前防住"改为"上线后缩短 bug 生命周期"；同月既说 harness 不重要、又背书 harnesses 未来图景；HF 事件续报。
- 逐字摘录：

> "With agents, bugs are faster to find and to fix. You can start bug investigations asynchronously and in parallel."

> "You can throw an infinite number of agents on the same bug."
（**验证经济学**：修复近乎无限便宜 ⇒ 预防性 review 的性价比崩塌——他激进立场的机制基础。）


> "We need to find the spot right in the middle, where speed and defects are in balance, where we go so fast that, yes, some bugs might make it through"

> "They'll be directing AIs, creating harnesses, and software factories, and QA and verification systems that ship working software faster than we've ever seen before."
（背书 Paul Dix——与 08-08 "harness 不重要"并存，分歧点在"谁建的 harness"（产品内建 vs 自建），词汇仍在用。）


> "There's been more investigation into the OpenAI & HuggingFace incident and, holy fucking shit man: the agents weren't allowed to get the responses of HTTP requests"

> "The difficulty of understanding incidents and overseeing AI agents appears to be growing faster than the rate at which more capable AIs help us with oversight and understanding."
（HF 续报：转引监督失效警告但无自身治理结论——立场停在"看戏＋引用"。）


- 立场：**支持（验证经济学主导）＋中性（边界事件）**。

## #98 两段（2026-09-06，库内存量之外的未收段落）

- URL：https://registerspill.thorstenball.com/p/joy-and-curiosity-98 （实取全文）
- **挂钩**：**验证回路＋外层调度**——naive interventionism 反讥；逐行 review 已过时的"Nah"；每日 automations 日常化。
- 逐字摘录：

> "Is this what's happening when engineers look at the output of a Sol or a Fable or an Astra and say "it writes bad code, it leaves all these dumb comments"? Bad code? Dumb comments? Really?"

> "Or did it just knock out a feature, end to end, in the 20 minutes you weren't looking, including frontend and backend changes, including internal and external documentation, and tests of course"
（用 Taleb "naive interventionism" 把对 AI 代码的挑剔类比过度医疗。）


> "Doesn't mean that all forms of code reviews are bad, but making Astra and Fable open PRs and then have two people review them line by line in September 2026? Nah."

> "After reading it, I set up a bunch of automations in Amp to run daily and clean up and fix things automatically."
（"code review will die" 发表前 13 天的过渡表述：批的是流程错位而非 review 本身。）


- 立场：**支持**。

## #99 增量段（2026-09-12，库内存量之外的未收段落）

- URL：https://registerspill.thorstenball.com/p/joy-and-curiosity-99 （实取全文）
- **挂钩**：**预算与熔断**——面对 Navier-Stokes 万人 agent 循环烧掉 300B 输出 token，他的回应是引用成本下降曲线而非治理关切。
- 逐字摘录：

> "they used 10,000 agents and they "sent 4.9 million messages and used about 300 billion output tokens. In the process of resolving the Navier–Stokes problem, the agents sent 2.7 million messages and used approximately 130 billion output tokens.""

> "when OpenAI released o3 "it cost ~$500,000 to score 87.5% on ARC-AGI 1. Today, Astra scores higher for ~$20." Maybe in three years you can solve Navier-Stokes for $50?"
（**预算钩子上的纯乐观派**：万人 loop 的正确视角是成本下降速率而非当下账单——不设熔断议题。）


- 立场：**支持**。

## 《What I believe about the future of software development》（sixteen things，2026-09-19）

- URL：https://thorstenball.com/blog/2026/09/19/what-i-believe-about-the-future-of-software-development/ （个人博客实取全文；该文自述"originally posted on X and blew up"——X 原帖登录墙不可达，如实记录）
- **挂钩**：**验证回路＋循环结构**——第一条宣布 code review 已死、第二条宣布 unit tests 或死；预言更聪明的模型 "needs fewer turns"。
- 逐字摘录：

> "Code review will die. I mean: it's already dead. But in the future, humans won't find a bug or an issue with the code produced by a model, at least not in a reasonable time."

> "Humans will only review the system and its composition, but it won't be in PRs and it won't be by looking through every line of the code."

> "Unit tests might die too. Why have training wheels if you never fall over?"

> "But a smarter model makes less mistakes, needs fewer turns. When do you really think "I'm okay with it being wrong a few times?""
（**立场峰值**。互驳点：Osmani 09-28《The Code Nobody Reads》逐条回应——"I agree with much of the list, at least on direction, though I'd put that first one differently. Line-by-line reading is going away for a lot of code. Review, meaning someone deciding what ships and being answerable for it, isn't."——Ball 未回应，对立单向敞开，与其对 Ronacher 的互驳格局同构。）


- 立场：**支持（激进峰值）**。

## #100 增量段（2026-09-20，库内存量之外的未收段落）

- URL：https://registerspill.thorstenball.com/p/joy-and-curiosity-100 （实取全文）
- **挂钩**：**验证回路＋预算与熔断**——对 Brooker "human no role in reviewing code" 只回一个 Yep；用 Jev 小模型原型按 prompt 自动拨 Dial。
- 逐字摘录：

> "Marc Brooker, Distinguished Engineer at AWS: "I believe that, long-term, humans have no role in routinely reviewing code. […] The idea that humans will reliably look through code to find the increasingly rare issues that automated tools miss seems like a fantasy." Yep."

> "Then I built a prototype that uses Jev to turn the Amp Dial, switching between models based on your prompt."
（发布激进主张次日即用"Yep."一次性背书更强版本；Dial 自动化原型显示预算分档正走向机器自决。）


- 立场：**支持**。

## #101 两段（2026-09-26，库内存量之外的未收段落）

- URL：https://registerspill.thorstenball.com/p/joy-and-curiosity-101 （实取全文）
- **挂钩**：**验证回路＋无人值守运行**——一切须对 agent 可读（feedback loop 一句话）；agent 写的测试无人看、可能无效堆积；反 PR 式圈养。
- 逐字摘录：

> "What will matter a lot in the future: performance characteristics, resource usage, failure modes, observability, debuggability, deployments, rollbacks. And all of that needs to be legible to the agent."

> "Why wouldn't a frontier model like Astra or Fable be able to use a new language as long as it can run it and have a feedback loop?"

> "Now we have the very same frameworks being used by agents to write tests god knows how and essentially no one looks at these billions of lines of test code that are generated every day now."
（**其立场中最接近自我怀疑的一段**：测试层可能变成无人消费的废料。）


> "There's no way around it: if you box AI into this little corner where all it can do is change code on your local machine and help you push it up as a PR, you're holding the leash at a fraction of its real size."
（把 PR 流程比作过度收短的绳子——对"loop 必须配人审门"的温和派方案明确说不。）


- 立场：**支持（自主度拉满）＋复合（测试层自我怀疑）**。

## #102 两段（2026-10-04，最新期）

- URL：https://registerspill.thorstenball.com/p/joy-and-curiosity-102 （实取全文）
- **挂钩**：**无人值守运行＋循环产品化机制**——Google 数据中心 fleet 级自主优化循环；平台对 agent 关门。
- 逐字摘录：

> "There's a whole bunch of numbers and percentages in that post and most of them I don't care about or trust, but this paragraph made me purse my lips as if to let out an impressed oooh"

> "A team of Argon agents analyzed fleet-wide profiling telemetry to autonomously identify and apply memory optimizations across Google's data centers, freeing up over 300 TiB of memory once rolled out"
（**疑数字不疑方向**：对厂商宣传数字保留怀疑、对无人值守 fleet 级自改循环本身全盘接受。）


> "Figma doesn't want you to use MCP. Amazon doesn't want you to shop with agents. Reddit won't let Claude access threads. X won't let ChatGPT read tweets. It's starting."

> "So why would all the companies now allow anyone to bring their agent?"

> "I think Sign in with ChatGPT might be one of the most interesting things launched this week. (Amp was a launch partner!)"
（首次承认无人值守 loop 的外部环境在收窄——只作观察不给对策；同周押注 agent 原生身份基建。）


- 立场：**复合（能力折服＋环境边界正视）**。

---

**最小主张**：Ball 是本库"能力极"最完整的连续轨迹样本：窗口内单向加码（orbs→dial→oracle→automations→durable agent loop→"code review will die"），全程不用 loop engineering 专名、不回应命名事件——立场全部以 Amp 产品语言表达；对词汇家族的态度是"用而不名"（durable agent loop 是离专名最近的自我表述；harness 被他宣告过时；用户来信的"Ralph, loops, graphs, and now orbs?"折射命名连续体）。反例仅两处（Slack 通知失效、测试堆积自疑），均不构成方向回调。与 Osmani 的 09 月互驳（code review will die vs answerability）是推动派内部速度边界的标尺。
**通道说明**：ampcode.com notes 索引页 404（各期正文经 feed＋文章页逐篇取得）；Register Spill archive 页客户端渲染无链接；Bluesky 停更于 2026-01-22（频道不活跃而非抓取失败）；X 登录墙（09-19 文自述 X 原帖火爆，原帖不可逐字取证）；HN 作者索引仅 3 条（含 08-30 Orbs 楼作者回复，已全文缓存）。
