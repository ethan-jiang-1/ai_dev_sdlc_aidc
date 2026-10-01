# Evidence 2026-09-27 · B2 · 有了数之后改什么

- 观测日期：2026-09-27
- 本档案回答：Q2 的后半。Hamel 2026-09-15 在 X 上宣布 FAQ 新加了五问。下面是那几页自己写的动作，加上四天后同一 FAQ 里「裁判和人合不上」的一页
- 不回答：这些动作是否让某个产品的数变好。五问的入口帖是 https://x.com/HamelHusain/status/2099929381850468675 ，发布于 2026-09-15 18:32 UTC

页都署 Hamel Husain 与 Shreya Shankar。访问日均为 2026-09-27【主验】。

## Source 1 · 全过，或集合已经旧了

- URL：https://hamel.dev/blog/posts/evals-faq/what-should-i-do-when-my-gold-eval-dataset-becomes-stale.html
- 发布日期：2026-09-15。修改：2026-09-25
- 原文摘录：
  > “If everything keeps passing, this is a sign that the eval is less useful and should be run less often or retired.”
  > “You should phase out expensive evals like LLM-as-a-judge more agressively than cheaper evals.”
  > “As your eval set changes, its scores may no longer be directly comparable with older scores.”
  > “For tracking progress with metrics over longer time horizons, it’s often better to use product metrics in addition to evals.”
- 做法：产品和用户变了，就用新的错误分析换例子或参考答案。一直全过，就降频或退役；贵的裁判比便宜的检查更该先拿掉。集合一换，新旧分数不要横比。要看长时段，另外看流失、活跃、收入这类产品数。
- 该摘录支持的最小主张：数一直全过时，改的是这条 eval 还跑不跑，不是把通过率再往上抬。集合更新之后，这个数不再和旧数比。
- 不支持什么：没有写哪一条产品的通过率因此下降或上升。产品指标的例子不是 agent 循环的终态。

## Source 2 · 裁判和人手标合不上

- URL：https://hamel.dev/blog/posts/evals-faq/what-should-i-do-when-i-cant-get-my-llm-judge-to-agree-with-human-reviewers.html
- 发布日期：2026-09-19。修改：2026-09-21。不在 9 月 15 日那条「新加五问」的清单里，是同一套 FAQ 紧接着的一页
- 原文摘录：
  > “As you collect labeled examples (we recommend at least 50 passing and 50 failing examples), inspect where the judge disagrees with the human labels”
  > “If you have trouble deciding whether an example should pass or fail, this is a sign that you need to refine your definition of success more precisely.”
  > “Inspect a few disagreements manually before trying automated prompt tuning.”
  > “Instead, we recommend building a separate judge for each type of failure.”
- 做法：先有人手标的过和不过，至少各 50 条。合不上时先看几条分歧：缺上下文、指令含糊，或是人自己都判不了。人判不了，就改成功定义，不要先改 agent。自动改裁判的 prompt（他们点名 GEPA）放在亲手看过分歧之后。一个裁判只抓一种失败。留出一批手标，最后才用来看它是否过拟合。
- 该摘录支持的最小主张：不同意的时候，先改的是成功那句话，以及裁判抓的是一种失败还是一锅。自动改 prompt 不是第一步。
- 不支持什么：没有给出「同意率从多少到多少」的对照。50/50 是他们的建议，不是实验阈值。

## 同一次更新里的另外几问

都是 2026-09-13 至 09-14 发布。动作并列，不并进上面两步。

| 页 | 发布 | 做法 |
|---|---|---|
| [标之前要不要先写 rubric](https://hamel.dev/blog/posts/evals-faq/do-i-need-a-reference-answer-before-annotating-data.html) | 2026-09-14 | 不要。先看例子、写开放笔记、再分组。先写好的 rubric 会让人只核清单里的项，漏掉清单外的问题。过一段时间再做一次错误分析，看 rubric 过期没有 |
| [trace 太大](https://hamel.dev/blog/posts/evals-faq/what-if-the-source-material-is-too-large-for-a-person-to-review.html) | 2026-09-13，改于 09-14 | 先看上游第一处失败。工具默认只展开对话，工具输出先折叠。还是太大，就抽出专家要核的证据并链回原文，抽出结果要专家自己验 |
| [给裁判多少上下文](https://hamel.dev/blog/posts/evals-faq/how-much-of-a-trace-should-i-give-an-llm-judge.html) | 2026-09-14 | 每个裁判只拿它那种失败需要的片段。拿掉一块再对人手标，成绩不降就可以留在外面。全文塞给裁判会更差。长 trace 可以给搜索工具，不到必要时不加 |
| [trace 含敏感数据](https://hamel.dev/blog/posts/evals-faq/how-can-i-do-error-analysis-when-production-traces-contain-sensitive-data.html) | 2026-09-14 | 优先找允许看的真数据。看不了，就让有权限的专家在日常工作里改具体的一条主张或一处矛盾，那些决定再变成 eval 数据 |

## 判读

- 观察：这几页把「有了数之后」写成几件不同的事。全过就让这条 eval 退场。合不上就改成功定义、把裁判拆开，自动改 prompt 靠后。trace 太大就先看第一处上游失败，而不是把整段交给模型。
- 推断：调优改的不一定是通过率那一个数。有时改的是还要不要跑这条，有时改的是怎样才算过。
- 与现有材料关系：A8 已有「先标第一条失败」「前 30 条自己读」。这里的「上游第一处失败」是同一方向在长 trace 上的说法，不另算一套理论。B 档的四件套仍是评测怎么搭，不包含这一步。

## 负结论与限制

- 页上没有一条「把某一句 rubric 改掉之后，同意率从 a 到 b」。
- 五问的初稿日期就是 2026-09-13 至 09-15，不是把 2025 年 FAQ 整页算成新写的。
- 不能推出：全过就该删掉 eval；产品指标可以代替任务上的过或不过。
