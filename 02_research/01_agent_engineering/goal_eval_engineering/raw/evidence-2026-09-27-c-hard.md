# Evidence 2026-09-27 · C · 验不了、或终态看不见时怎么写

- 观测日期：2026-09-27
- 本档案回答：Q3。设计不出好 eval 时，Hamel 把产品改成能核对的小块；终态是业务结果、agent 看不见时，Yeret 把 goal 的高度分开
- 不回答：这两套哪一套该当唯一做法。气味那一句已在 A 档，这里不重抄

## Source 1 · Hamel Husain《“It’s Hard to Eval” Is a Product Smell》

- URL：https://hamel.dev/blog/posts/eval-smell
- 发布日期：2026-06-29
- 访问/观测日期：2026-09-27【主验】
- 来源类型：作者本人。三个例子是他给产品做的设计草图，文末写明不是可运行的应用
- 原文摘录：
  > “What does the user actually need to check?”
  > “What trusted thing can they compare it against?”
  > “Are there signals or heuristics that experts use to aid in verification?”
  > “What smaller units can they accept, edit, or reject?”
  > “you can verify that the plan retrieval picked a sensible anchor, and each edit honors the constraints.”
  > “Now there are scoped units to grade, such as whether a contradiction is real or whether a citation supports a claim.”
- 做法：先问用户到底要核什么、拿哪一份已经信得过的东西来比、专家平时用什么启发式、哪些小块可以单独接受或打回。数据助手不要只交一个数，要交出来源、假设、拆开的分布，以及核对不了的项。课程计划挂在一份已有人在用的教案上，只审 diff。长篇医学意见先抽出带页码的事实、矛盾和空档，报告从已经核过的条目组装。核对面变小以后，eval 才写得下去：锚点选得对不对、每一处修改是否守住约束、矛盾是不是真的、引用是否支撑那句话。
- 该摘录支持的最小主张：窗内这篇文章把「很难 eval」收成四问，再把产物改成可单独接受或打回的小块。eval 写在这些小块上，不写在整份生成物上。
- 不支持什么：草图不是上线前后的对照。不证明改完界面之后标注更便宜，或循环因此更准。

## Source 2 · Yuval Yeret《Goal-Based Loop Engineering》

- URL：https://yuvalyeret.com/blog/ai-agent-completion-goals-aim-at-outcomes
- 发布日期：**2026-05-27**（页面 `datePublished` 与 `<time>`）。窗边，不是 2026-06 以后
- 访问/观测日期：2026-09-27【主验】
- 来源类型：作者本人
- 原文摘录：
  > “The first move is to ask, for every goal you set: is this a completion condition for an output, or for an outcome? If it is output, is that output reliably connected to the outcome you actually care about, and do you have enough signal to know when it is not?”
  > “what I often observe when giving an agent an outcome oriented goal without the observability loop, is that rather than running endless turns, they simply stop and hand it back”
  > “Can your agents only effectively seek output-oriented ‘/goal’ statements right now? That might be a good place to draw the border between agent autonomy and human responsibility.”
- 做法：写每一句 goal 之前先问它停的是产出还是结果。若是产出，再问它和在乎的结果是否连得上，以及连不上时有没有信号。他举的一场工作坊：把「拆开一张过大的表」追问成「让财务团队能用 Claude 更及时地分析、看懂并清理数据」。agent 看不见结果时，他看到的是停下来交还，而不是无限跑。眼下的分界是：agent 对产出型 `/goal` 自己跑，人留在还没有定量证据的结果上；同时去补能让结果被观测到的遥测。
- 该摘录支持的最小主张：窗边有一套把 goal 分成两层高度的问法。看得见的完成条件交给 agent；看不见的业务结果先留在人这边，并标明缺的是观测，不是再写一句更响的 goal。
- 不支持什么：交还是他的观察，没有次数。财务团队那个目标是追问之后的方向，他故意没有写成可核终态。技术条件与结果的那句对照已在 A 档，这里不重抄。

## 判读

- 观察：两套都站得住，盖的情形不同。Hamel 的产物还能被改成可核对的小块。Yeret 的结果在系统外面，agent 现在判不了，他就把高度切开，而不是假装那句 goal 已经可核。
- 推断：设计不出来的时候，材料里至少有两条路，一条把核对面缩小，一条把判不了的高度还给人。没有一篇写「这时就不要做了」。
- 与现有材料关系：A 档只留气味句和 Yeret 的一句对照，日期与节拍以本档为准。Shankar 口播里「人先标失败」仍是另一条，不并进来。

## 负结论与限制

- Yeret 在 2026-05-27，标窗边。
- 两个来源都没有「改完之后指标移动了多少」。
- 不能推出：所有难 eval 都应先改产品；所有业务 goal 都应留给人。
