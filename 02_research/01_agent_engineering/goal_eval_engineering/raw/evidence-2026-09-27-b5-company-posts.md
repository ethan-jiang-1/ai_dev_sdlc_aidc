# Evidence 2026-09-27 · B5 · 此前只有链的公司帖

- 观测日期：2026-09-27
- 本档案回答：B3 点名未打开的 Rippling、Glean、ElevenLabs。打开之后，哪一篇有检查句子，哪个数动了
- 不回答：这些数能不能外推到别的产品。Lenny 文第三步的聚类表仍在付费墙后，不在这里

## Source 1 · Rippling《Building a MCP server》

- URL：https://www.rippling.com/blog/building-mcp-server
- 发布日期：2026-08-25。作者 Callen Raveret。不另开人物
- 访问/观测日期：2026-09-27【主验】
- 来源类型：公司工程博客

检查怎么建：他们把对外的说明文字当成代码，做了一套打桩的端到端 harness。金数据集一开始 50 条以上。每条是四件：用户提示、参考答案、打好桩的 API 响应、期望执行的代码。例子是问 Michael Mitchell 团队的平均任期，参考答案写明一位直接下属、平均 7.25 年。

同一条在干净上下文里跑过一张矩阵：Claude（Haiku 4.5 / Sonnet 4.6 / Opus 4.8，中档和高档推理）、Codex（GPT 5.4 / 5.4 Mini / 5.5，中档和高档）、Cursor Composer 2.5。agent 只拿到基线系统提示、MCP 说明和工具描述。API 响应是桩，所以每只面对同一份数据。

裁判按参考答案、该用的桩、以及完整 transcript 打分。每条满分 100，四格：

- 函数选择：有没有选对 `codemode.*`
- 函数路径：调用顺序是不是更优的那条
- 调用正确：生成的 JavaScript 跑起来没有，参数对不对
- 最终答案：结果对不对

分数交给一只 optimizer。它分诊失败、改说明文字、重跑。所有 harness、模型和推理档都升的改动才留；只帮到一只模型的丢掉。

两处后来量到的变化：

1. 程序语义对，但串行调用超过沙箱 60 秒。他们把每个函数的 p95 延迟写进描述，并写明串行相加、并行只算最慢的一次。生产环境沙箱超时下降 70%。
2. Claude Code 决定要不要用这个工具时，只看工具描述的前 2,048 个字符。路由规则写在后面，等于看不见。他们在详细说明前加了一段约 2,000 字符的动作头（函数名、箭头、约束，不是散文）。Claude Code 的成绩升 41%。Codex 和 Cursor 没有因此升降。

同页另有一组设计对照，不是这套裁判的分数：同一问题，每 API 一个工具要 11,071 token、22 轮；Code Mode 是 204 token、1 轮。他们写成少 98% token。

- 该摘录支持的最小主张：窗内有一套把「做对」拆成参考答案加期望代码的金数据，裁判同时看选函数、路径、调用和终答。说明文字的改动只在所有客户端配置都升时保留。动作头让 Claude Code 升 41%；写出 p95 之后，生产超时降 70%。
- 不支持什么：41% 不是 Codex 或 Cursor 的数，也不是那 100 分里的某一格从多少到多少。70% 是沙箱超时，不是裁判分。98% token 是两种接口设计的对照，不是这套循环调出来的质量分。页上没有写出 optimizer 前后的总分。

## Source 2 · LangChain 案例里的 Rippling AI

- URL：https://www.langchain.com/blog/how-rippling-went-ai-native-across-every-product-in-6-months-with-deep-agents-and-langsmith
- 发布日期：2026-06-01。作者 Sofia Sulikowski。引句来自 Rippling 的 Laks Srini、Sahin Olut。不另开人物
- 访问/观测日期：2026-09-27【主验】
- 来源类型：厂商案例，转述客户。和 Source 1 不是同一套产品：这篇是 Rippling AI 的多层检查，Source 1 是 MCP 说明文字的 harness

他们写了四层，结果都进 LangSmith：

- 离线：预录的 mock，每次提交在本地跑，不碰外部依赖
- 合并后：300 到 400 条查询打满沙箱（真 API），上线前看系统还在不在
- 挡住部署：大约 10 条关键场景打真系统
- 持续：对着生产数据，一天跑多次

自修循环：从 LangSmith 拉失败 trace，agent 看原因、提几个改法、重跑 eval，直到回归关上。人审完再合并 PR。Sahin Olut 的原话是先拉失败 trace，让 agent 看懂、提方案、重跑，确认有提升再循环到完。

- 该摘录支持的最小主张：窗内他们把检查分成提交、合并后、部署门、生产巡检四层。自动改到回归关上，合并仍要人点头。
- 不支持什么：页上没有某一条检查的原文，也没有质量分的前后数。不能把它和 Source 1 的 41% 或 70% 加成一家的效果。

## Source 3 · Glean skills

- URL：https://www.glean.com/blog/glean-skills-launch-2026
- 发布日期：页眉 “Last updated Feb 09, 2026”。窗边。作者 Abhilash Samantapudi、Matt Ding、Julie Mills。不另开人物
- 访问/观测日期：2026-09-27【主验】
- 来源类型：公司博客

他们写：技能路由一开始做得朴素，技能相对工具的触发率掉了 20%。把反例和边界写进始终加载的技能描述之后，触发率上去了。页上没有上去之后的数。

技能正文里，几条高质量的例子比长系统提示更有效。最大的准确率和延迟变化来自把具体例子放进技能。evals 里，一条带着模型走过多只 Salesforce 工具的技能，准确率 73% 到 85%，首 token 时间少 18%。

- 该摘录支持的最小主张：窗边有一次「把例子写进技能」之后准确率 73% 到 85%、首 token 少 18%。触发率掉 20% 之后他们改的是描述里的反例，改完的触发率没有写出。
- 不支持什么：73% 和 85% 量的是哪些题、谁判对，页上没有。不能把反例改动和这 12 个点加成同一次实验。

## Source 4 · Glean 与 ChatGPT、Claude 的盲比

- URL：https://www.glean.com/blog/enterprise-search-evaluation-2026
- 发布日期：页眉 “Last updated Feb 12, 2026”。窗边。作者 Matthew Zhao、Karthik Rajkumar、Neil Dhruva、Julie Mills。不另开人物
- 访问/观测日期：2026-09-27【主验】
- 来源类型：公司博客。这是一次对照，不是改完自己的系统再重跑

约 280 条查询从 Glean 自己的内部部署里抽，分布去对齐匿名汇总过的客户查询类别，不用客户数据。查询偏「碰到多个数据源」的复杂题。Glean 与 ChatGPT 比的是 GPT-5.1，与 Claude 比的是 Sonnet 4.5，用来把模型差别从搜索栈里分开。ChatGPT 一侧接了 Drive、Calendar、GitHub、Slack。Claude 一侧还接了 Confluence、Jira、Salesforce。他们写 ChatGPT 当时没有 Jira 和 Salesforce，题的复杂度因此受限。

评分：盲、随机换位、五点偏好，再收成文中的类别。两维是正确性（事实和推理相对问题站不站得住）和完整性（问题的各部分和必要步骤盖住没有）。四位评分人先打，再由他们自己的 AI 质量团队核对是否按指南打。超出专长时，评分人可以用 Glean 的专家搜索找人，再确认自己的判断。

有偏好时，正确性上 Glean 相对 ChatGPT 是 1.9 倍，相对 Claude 是 1.6 倍。

- 该摘录支持的最小主张：窗边有一次在自家部署上的盲比。检查是正确性和完整性两句。有偏好时，他们的评分人更常选 Glean。
- 不支持什么：这不是某一次改动前后的数。评分人可以借 Glean 找专家，质量团队也是他们自己的。1.9 倍和 1.6 倍不能读成独立裁判的通过率。

## 判读

- 观察：这些篇里能放进「检查句子写得出、而且数动了」的，是 Rippling 8 月这篇。裁判四格里有一格专门打路径优不优。保留规则是所有客户端配置一起升。Glean 2 月的 73% 到 85% 有数，题目没公开。Glean 的盲比和 LangChain 那四层都不是「改一句再重跑同一套」。
- 推断：点名「也在用 eval」不等于有一条可以抄的检查。抄得到的是金数据长什么样、哪一格在打路径、什么改动允许留下。
- 与 B3、B4 的关系：Ramp、Harvey、Shopify、Abridge 的读数仍以那两档为准。这里不把 41%、70%、73% 到 85%、1.9 倍写进他们的格子。

## 负结论与限制

- ElevenLabs《Eleven v3 is Now Generally Available》（https://elevenlabs.io/blog/eleven-v3-is-now-generally-available）：内部基准 27 类、8 种语言，错误率 15.3% 到 4.9%，用户相对 Alpha 偏好 72%。这是语音模型把数字和符号读对没有，不是 agent 的完成条件。官方页没有发布日期。二手有写成 2026-03-14 的，不把二手当发布日。不入做法表。
- ElevenLabs《Voice agent evaluation framework》（https://elevenlabs.io/blog/voice-agent-evaluation-framework-6-pillars-explained）：六根柱子和行业区间（意图分类大约 85% 到 92%，任务成功率目标高于 85%）。没有他们自己改了哪一步、哪个数动了。不入。
- 不能推出：所有客户端一起升才留，就会得到 41%；打路径最优和「只看环境结果」是同一种检查。
