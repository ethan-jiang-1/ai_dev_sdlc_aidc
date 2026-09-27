# Evidence 2026-09-27 · A6 · 实战：完成条件与判定怎么写

- 观测日期：2026-09-27
- 本档案回答：动手时按什么步骤写 goal / eval。重心从「谁在说」转到「句子怎么写、用什么判」
- 不回答：哪一套已经让 loop 的结果变好。步骤是来源自己写的，效果另计

## Source 1 · Anthropic《Demystifying evals for AI agents》

- URL：https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- 发布日期：2026-01-09。窗边。作者署名为 Anthropic 工程博客，不另开人物
- 访问/观测日期：2026-09-27【主验】
- 原文摘录：
  > “A good task is one where two domain experts would independently reach the same pass/fail verdict.”
  > “Everything the grader checks should be clear from the task description.”
  > “it’s often better to grade what the agent produced, not the path it took.”
  > “We recommend choosing deterministic graders where possible, LLM graders where necessary or for additional flexibility, and using human graders judiciously for additional validation.”
  > “20-50 simple tasks drawn from real failures is a great start.”
- 该摘录支持的最小主张：他们把一条 eval 拆成任务、多次试验、grader、transcript、环境里的 outcome。实操顺序是：从你已经在手工查的行为和用户报过来的失败里抽 20 到 50 条；每条写到两位领域专家会独立给出同一个过或不过；grader 要查的每一项都出现在任务说明里；先准备一份已知能通过全部 grader 的参考解；该发生和不该发生的两边都测。能用测试或环境状态（订票是否真的写进数据库，而不是 agent 说已经订了）就用。必须用模型判的时候，每个维度单独一只裁判，并允许它回答 Unknown。人用来校准，不用来每条都判。路径（工具调用顺序）判得太死会把没预料到的正确解判失败。
- 他们自己的反例：Opus 4.5 在 CORE-Bench 上先是 42%，改掉过严的数字格式、含糊说明和不可复现的任务后到 95%。METR 有的任务让模型优化到某个阈值，评分却要求超过该阈值，听话的模型吃亏。0% 的 pass@100 多半是任务写坏了，不是模型不会。
- 不支持什么：这是 1 月的工程帖，不是 6 月以后的新产品机制。42% 到 95% 是他们转述的一次修 grader，不是本主题做的对照。

## Source 2 · OpenAI《Evaluation best practices》（活文档）

- URL：https://developers.openai.com/api/docs/guides/evaluation-best-practices
- 发布日期：页上没有文章日期。同页写 Evals 平台 2026-10-31 起对现有用户只读，2026-11-30 关闭。观测日 2026-09-27【主验，活文档】
- 原文摘录：
  > “Define eval objective. What’s the success criteria for the eval?”
  > “LLMs are better at discriminating between options. Therefore, evaluations should focus on tasks like pairwise comparisons, classification, or scoring against specific criteria instead of open-ended generation.”
- 五步写在页上：写下成功标准；收集数据（合成、领域、购买、人工、生产、历史）；定义怎么检查；跑并比较；每次改动都再跑，并把新的不确定案例加进集合。摘要例子把标准写成数字：留出的 1000 条上 ROUGE-L 至少 0.40，G-Eval 连贯性至少 80%。问答例子写成上下文召回至少 0.85、精确率超过 0.7、70% 以上的回答被评为正。
- 该摘录支持的最小主张：官方活文档把 eval 写成「先有一句成功标准，再有一批数据，再有一个可自动打的数」。裁判适合做比较、分类、按条目打分，不适合开放生成后再让模型自由发挥。
- 不支持什么：页上没有日期，不能算 2026-06 的新文。例子是单轮摘要和问答，不是 agent 循环的终态。与 2026-05-09 Codex cookbook 的六段合同不是同一篇，不互相加票。

## Source 3 · AdaRubric（论文，窗边）

- URL：https://arxiv.org/abs/2603.21362 ，HTML 为 v3，页眉 arXiv:2603.21362v3，2026-05-10
- 作者：Liang Ding（悉尼大学）。访问/观测日期：2026-09-27【主验】
- 原文摘录：
  > “evaluation dimensions should be a function of the task, not a fixed property of the evaluator.”
  > “A valid rubric satisfies: (i) Task-relevance: d_j derived from T’s success criteria; (ii) Orthogonality … (iii) Completeness … (iv) Calibration: γ_3 = “acceptable”, γ_1 = “broken”, γ_5 = “exemplary”.”
- 做法：把任务描述交给 LLM，让它从参数知识里抽出成功标准，收成默认 5 个互不重叠的维度，各给权重，并为 1 到 5 分各写一句带具体行为的说明。生成后做三项自动检查：维度名余弦距离大于 0.3、权重和为 1、五档都写满。失败就重试一次，再失败就退回该领域的模板。然后按步、按维度打分，带置信度。部署标准写成两次独立评分的 Krippendorff’s α 至少 0.80。
- 该摘录支持的最小主张：论文把「写不出固定 rubric」处理成「让模型按任务现生成 rubric」，再用人的排序相关（WebArena 上 Pearson r = 0.79）当质量。这是研究流程，不是产品里的 `/goal`。
- 不支持什么：生成 rubric 的是模型，不是 Shankar 口播里那个保留新类型的人。两套不能并成一步。r = 0.79 是三个基准上对人类排序的相关，不是某个产品 loop 因此跑得更好。

## 和已有档案怎么接

已经主验、这里不重抄的实操句：

- 循环能跑的那种 goal：可核终态、证据出现在 transcript 或测试里、次数上限、另一只模型只回答尚未达到 / 达到 / 不可能。见 A、A2。Osmani 把「把界面做好」排除在外。
- 写不出来时：人在 trace 上标失败，agent 只把已说出的类型铺开，再按出现频率决定先改哪 20%。见 A5。Anthropic 的「20 到 50 条真实失败」是这套的起点数量，不是另一套理论。

## 判读

- 观察：实战步骤在来源之间是接得上的。先从真实失败拿出几十条两人都能判过不过的任务；查得了环境状态就用确定性检查；查不了再上分维度的 rubric，并用人对一下。循环里的 goal 就是其中一条任务加上可见证据和停止次数。标准还在人脑子里时，先标，不要让模型宣布失败类型。
- 推断：AdaRubric 把「生成维度」交给模型，和 Shankar「新类型留给人」正面不一样。实战上先按人标的类型写任务，不把论文的自动生成当成已经可以替换这一步。
- 与效果：修 grader 能把分数从 42 抬到 95，说明分数先取决于任务和 grader 有没有写坏。这不是「有了 eval，agent 就更好」的证据。

## 负结论与限制

- arXiv:2606.17819 的页面抽取仍然失败，本档没有它的句子。
- OpenAI 活文档无发布日。
- Steinberger 原帖仍未打开。本档不需要那两句热度句才能写出步骤。
