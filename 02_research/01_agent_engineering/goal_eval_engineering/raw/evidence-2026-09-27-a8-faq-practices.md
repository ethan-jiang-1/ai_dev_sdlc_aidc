# Evidence 2026-09-27 · A8 · FAQ 里的具体做法

- 观测日期：2026-09-27
- 本档案回答：用户要看到更多 practice，不要更糊的方向。下面是 Hamel Husain 与 Shreya Shankar 的 FAQ 里已经写明的动作
- 页：https://hamel.dev/blog/posts/evals-faq
- 页首日期：2025-05-28。更新：2026-07-18。观测日打开的是更新页。不能把每一问都当成 6 月以后新写的
- 不回答：这些动作里哪一条是唯一正确的。二元过/不过仍与 1 到 10、部分分并列，见 A7

## 做法

每次大改之后，花 30 分钟亲手看 20 到 50 条输出。质量只由一个懂用户的人定，他们称之为 benevolent dictator。这个人可以听别人的意见，但过不过由他判。觉得一条对话要五个专家才判得了，说明产品范围太宽。

他们做过的项目里，60% 到 80% 的开发时间花在看失败和 eval 上，不是花在搭自动检查上。

通过率 100% 时，先怀疑题目太容易。70% 左右有时才是在压系统。数字是他们的经验，不是对照实验。

看 trace 时像写日志，记下开放的问题，先标第一条失败。后面的失败常常是它带出来的。熟了再标同一条里彼此独立的失败。

问领域专家的句子是结果，不是实现。「预约做成了没有」，不是「工具调用成功了没有」。把确认信、生成的邮件或数据库更新和 trace 放在同一屏，让非技术的人看结果。

错误分析不外包。电话号码、邮箱这种机械核对，可以在内部先把 rubric 写死之后交给外面。把真正的专家雇进来不算外包。他们举的例子是 AnkiHub 雇四年级医学生评医学 RAG，而不是交给通用标注员。

前 30 到 50 条必须自己做开放编码，读原文、记失败。这步不交给模型。记完之后，可以让模型把笔记收成候选分组，分组仍要人改。用来校验 LLM-as-judge 的标签必须手标。模型可以提议改 prompt，采用前要人看。有了一批 eval 之后，自动改 prompt 只适合收尾；它爬的是已知指标，发现不了新失败。

多步流程画一张矩阵：行是最后一次成功的状态，列是第一次失败的位置。热点在哪，调试就投到哪。

多轮对话里的失败，先收成最短的单轮还能不能复现。购物机器人在第 4 轮给错退货政策，先问一句「X1000 的退货窗口是什么」。单轮仍错，就不是上下文问题。

## 原文摘录

> “Spend 30 minutes manually reviewing 20-50 LLM outputs whenever you make significant changes.”
> “we’ve spent 60-80% of our development time on error analysis and evaluation.”
> “If you’re passing 100% of your evals, you’re likely not challenging your system enough. A 70% pass rate might indicate a more meaningful evaluation”
> “Ask ‘Has an appointment been made?’ not ‘Did the tool call succeed?’”
> “If you feel like you need five subject matter experts to judge a single interaction, it’s a sign your product scope might be too broad.”
> “After you’ve open coded 30–50 traces yourself, use an LLM to organize your raw failure notes into proposed groupings.”
> “Always read through the raw traces yourself at the start. … Never skip this or delegate it.”

## 最小主张

- 支持：这页把「看数据」写成可执行的节拍：谁看、看多少、先标哪一条、问哪一句、哪一步才许模型插手。
- 不支持什么：60% 到 80%、70% 通过率没有对照。页的初稿在 2025。聚合博客里的「实习生测试」「80% 同意才自动化」原文已打开，见 [`evidence-2026-09-27-b-eval-shape.md`](evidence-2026-09-27-b-eval-shape.md)：2024 年那句测的是任务实习生能不能做，不是 80% 同意。

## 负结论

- r/AIQuality 一篇生产栈帖抽取为空，不引。
- 厂商 rubric 库（按模板名列十几条语音检查）是产品目录，不是这页这种动手节拍，不并进。
