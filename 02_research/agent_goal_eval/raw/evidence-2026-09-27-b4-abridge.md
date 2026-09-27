# Evidence 2026-09-27 · B4 · Abridge 把一条病历拆成可核对的规则

- 观测日期：2026-09-27
- 本档案回答：窗内还有没有公司自己写下检查句子、并且改完之后有人给过数。Abridge 这一篇有
- 不回答：91% 能不能外推到别的产品

## Source 1 ·《Offline Evaluations to Improve Our Systems》

- URL：https://tech.abridge.com/blog/offline-evaluations-to-improve-our-systems
- 发布日期：2026-08-17。作者 Catherine Chen、Samir Khan、Michael Oberst、Alex Chouldechova。不另开人物
- 访问/观测日期：2026-09-27【主验】
- 来源类型：公司工程博客。文中例子是合成的，用来代替真实病历

检查怎么建：临床专家按专科、按一次就诊写规则。规则是「病历必须写上某件已经发生的事」，不是「写得好不好」。皮肤科要记下病人在用 Dove 香皂，眼科则不该写。平均一次就诊约 10 条，复杂的到 50 条。已覆盖 20 个以上专科、几千次就诊。系统在旧版本上写砸过的就诊，会再加进集合，避免基准饱和。

打分：模型按条给过或不过。人用 40 份病历、300 条规则对过这个裁判：真阳性率 0.78，假阳性率 0.07。他们写明裁判不完美，只作开发时的方向。集合拆成训练集和测试集，避免对着同一批就诊改到过拟合。

他们举的一次改动：一个 agent 从既往病历往当次病历里抽信息。规则指出三类错：抽了不该抽的、放错段落、漏了该留的。按这个信号改完之后，临床专家盲比，91% 的比较更倾向新输出。

腹部疼痛那次就诊的规则长这样（页上合成例子，节选）：

> “The note must include that the patient describes epigastric location of pain.”
> “The note must include the onset of the pain as 3 months ago.”
> “The note must include the absence of rebound tenderness.”

- 该摘录支持的最小主张：窗内有一套把「一份好病历」拆成就诊专属的必须项，用模型逐条打过/不过，并用 300 条规则对过裁判。一次迭代之后，专家盲比 91% 更倾向新稿。91% 是人的偏好，不是规则通过率从多少到多少。
- 不支持什么：不证明 0.78 的真阳性率在别的领域成立。不证明 91% 只来自改了某一条规则。页上没有规则通过率的前后数。

## 判读

- 观察：和 Harvey 的逐条 rubric 是同一类形状：人先把「怎样算对」写成可单独打的句子，模型再打。Abridge 的句子更死，是「必须出现某事实」，而且按这一次就诊现写，不是一份通用量表。
- 推断：数动了的那一截是改 agent 之后的盲比，不是把裁判本身调到同意。裁判先用 300 条对过，然后才拿来当迭代信号。
- 与 B3 的关系：Ramp、Harvey、Shopify 的读数仍以 B3 为准。这里补的是 8 月、窗内、规则原文看得见的一家。

## 负结论与限制

- Robinhood 2026-08-25《The loop stays dumb so the model can be smart》（https://robinhood.com/us/en/careers/blog/loop-stays-dumb-so-the-model-can-be-smart/）写了他们靠一套 eval 集比较新旧系统才敢上线。没有公开检查的句子，也没有他们自己的质量读数。文中「分数高 10–15%、token 少 41–66%」是转引 OpenAI，不是 Cortex 的数。不入做法。
- 同系列还有持续监测、实时纠错等篇。这轮只打开这一篇。
- 不能推出：逐条「必须写上」适合所有生成任务；0.78 / 0.07 已经够当上线门。
