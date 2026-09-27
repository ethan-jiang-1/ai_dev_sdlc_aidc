# Evidence 2026-09-27 · A7 · 几种都站得住的写法

- 观测日期：2026-09-27
- 本档案回答：实战再挖一层。用户校正：很难有唯一的确定性做法，感觉有道理的做法都算
- 不回答：哪一种胜出。下面每条只写它自己的句子和它盖住的情形

## 新增 · Tessl《A Framework for Evaluating Agentic Skills at Scale》

- URL：https://arxiv.org/abs/2606.17819
- 时间：页上写 2026。arXiv 编号 2606.17819。研讨会挂在 KDD 2026-08-09 至 13。投稿日页上未单列
- 作者：Maksim Shaposhnikov、Nicolas Fortuin、Simon Stipcich、Maria I. Gorinova、Amy Heineike、Rob Willoughby（均署 Tessl）。不另开人物行
- 访问/观测日期：2026-09-27【主验】
- 原文摘录：
  > “the relevant question in 2026 is not ‘can the agent solve this task?’ but ‘does the agent solve the task the way I want it to?’”
  > “By default, the pipeline produces two rubric sets: one for task completion and one for instruction following. Each rubric is a natural-language assertion scored on a 1–10 scale, with scores summed to 100 per category.”
  > “A separate verification agent scores the resulting solutions against the rubrics”
- 做法：从一份 skill 生成任务、可执行环境和两套隐藏 rubric。做题的 agent 看不到 rubric。目标完成看产物在不在、对不对。指令遵循看有没有按 skill 里的偏好来：库、命名、禁止项、必经步骤。裁判是另一只 agent，能看到 rubric、解答和日志。他们用的裁判是 Claude Code 里的 Sonnet 4.6。任务说明若泄露步骤或 rubric，就丢掉。人可以在每步改；不改就自动丢弃不合格任务。
- 他们自己的限制：前沿模型的目标完成经常两边都超过 90%，合成任务分不出高低，要更难就得有外部反馈或人在环里。带 skill 的对照按构造就偏向「有 skill」。裁判只有一只，审美类标准尤其不稳。只覆盖好复现的软件任务。
- 该摘录支持的最小主张：2026 有一套把 goal 拆成两句的写法。一句是做完了没有。一句是是不是按我想要的方式做的。后一句用隐藏的、可加总的自然语言断言，由另一只模型打 1 到 10 分。
- 不支持什么：不证明 1 到 10 比过/不过更准。分数是技能有没有改变行为，不是某个产品循环因此更好。

## 已经打开、这一轮才并排的几种

每条都站得住，盖的情形不一样。引句在原档，这里不重抄。

| 写法 | 盖住的情形 | 出处 |
|---|---|---|
| 可核终态，另一只小模型只回答尚未达到 / 达到 / 不可能，加上次数上限 | 知道怎样算做完，而且证据能出现在对话或测试里 | A、A2。2026-06-30 |
| 写不出检查时，先让模型起草，再改掉和通用做法不同的几条 | 检查说不出口，但项目里有几条硬规则 | A2。2026-07-22 |
| 20 到 50 条真实失败；两位专家会给出同一个过或不过；判环境里的结果，不判路径；能用测试就用测试 | 要一套能反复跑的任务集 | A6。2026-01-09，窗边 |
| 部分分：做对几步好过一步都没有。长流程拆成可单独过/不过的里程碑 | 结果不是非黑即白 | A6 的部分分；Hamel 与 Shankar 的 FAQ（2026-07-18 更新）里的 goal checkpoints |
| 人在 trace 上标失败类型，agent 只铺开，不新增类型。再按出现次数决定先改哪一截 | 什么叫好还在人脑子里 | A5。2026-07-03 |
| 规格加上可选的 eval 数据集；同一类问题反复出现之后才建数据集 | 内环先跑起来，eval 后补 | A4。Ng，2026-06-26 |
| 把任务描述交给模型，生成约 5 个互不重叠的维度，各写 1 到 5 分的行为 | 不想手写固定维度，又接受模型来起草标准 | A6。AdaRubric，2026-05-10，窗边 |
| 二元过/不过，不用 1 到 5 | 要标注一致、要逼人做决定 | Hamel / Shankar FAQ，页首 2025-05-28，更新 2026-07-18。见下 |
| 两套隐藏 rubric：做完了没有，以及是不是按我想要的方式。1 到 10，加总到 100，另一只模型判 | 前沿模型大多能做完，差别在做法 | 本档案 Tessl 论文 |

FAQ 里和「1 到 5」并排的原句（https://hamel.dev/blog/posts/evals-faq ，观测日 2026-09-27 已读）：

> “Binary evaluations force clearer thinking and more consistent labeling.”

同页对 agent 工作流还写了两段可以并存：先把整段当成黑箱，问有没有达到用户的目标，并为每个任务写一条精确的成功规则；长流程再拆成可以单独过或不过的检查点。这和 Anthropic 的「判结果、给部分分」说的是邻近的两件事，不是同一句话。

## 判读

- 观察：这些写法在「标准谁来写」和「分有多细」上彼此不同。有的要人先标，有的让模型起草再改，有的让模型直接生成维度。有的只许过/不过，有的要 1 到 5 或 1 到 10，有的要部分分。没有一篇把别的写法判死。
- 推断：挖得越深，越不像会收到一条确定性步骤。并列保留。下次只有在某条写法自己写出「什么时候不要用我」时，才把它从这张表里挪走。
- 与效果：Tessl 写明目标完成在前沿模型上容易饱和。所以「做完了没有」这一句，在难任务上仍然有用，在他们这批合成题上已经分不开。这不是否定那一句，是它的适用边界。

## 负结论与限制

- 聚合站上的 rubric 综述没有打开原文，不进这张表。
- FAQ 的初稿日期在 2025。窗内能钉住的是 2026-07-18 的更新页，不是每一问都是 6 月以后新写的。
- Tessl 的六位作者不因共同署名各算一家做法。
