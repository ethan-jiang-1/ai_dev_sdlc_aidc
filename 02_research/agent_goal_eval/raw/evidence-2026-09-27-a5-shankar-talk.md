# Evidence 2026-09-27 · A5 · Shankar 口播：eval 不能先写死

- 观测日期：2026-09-27
- 本档案回答：设计不出来的时候，eval 怎么弄。依据是 Shreya Shankar 2026-07-03 的口播，不是别人的转述
- 不回答：coding agent 的 `/goal` 终态句怎么写。这场讲的是产品 eval 的失败分类怎么长出来

## 来源

- URL：https://www.youtube.com/watch?v=tqUDjc1HzO4
- 标题：How to Automate AI Evals (Correctly)
- 频道：Hamel Husain。上传日：2026-07-03。时长：1639 秒（yt-dlp 元数据，2026-09-27）
- 主讲：Shreya Shankar。访问日期：2026-09-27
- 取得方式：YouTube 页面上的 Transcript。yt-dlp 列字幕时被挡成机器人；Chrome cookie 抽取挂起后已停。口播里有自动字幕的误听（evals 听成 emails，Hamel / Antaripa Saha 听成 Amel / Antariksha Dasgupta）。引句按字幕原文，误听在主张里改回她指的人
- 全文：[`transcript-2026-07-03-shankar-automate-evals.md`](transcript-2026-07-03-shankar-automate-evals.md)

## 她给出的做法

三步循环，产品变了就再走：error analysis（从 trace 里找出失败类型）→ 量每种失败有多常见 → 改产品。她说分析是最难的一步，因为没有现成标签。「什么叫 slop」是看见才知道。

AI 放在哪：分析这一步是口味，她说 AI 不擅长自动化；越往后，量化和改 prompt，AI 越能做。

三条不要：

1. 不要把 trace 丢给 agent，说「去找出问题」。会漏掉只存在于人脑子里的问题，还会自己宣称哪条最优先，而且下次重跑不保留中间结果。
2. 不要只看一遍。她自己的研究：再看已经标过的 trace，会冒出新的失败类型。外环是反复过数据，内环是在一条数据里换假设。
3. 不要所有应用用同一条准确率。对用户的要高，内部摘要可以松。她会把 trace、应用说明或代码交给 Codex，先问最坏情况，再倒推要哪些 eval 和护栏。

她自己的 skill 把人留在判定上，agent 做缩放：

- agent 先读一批数据，做视觉编码，搭三个视图（逐条、地图、进度），再聚类抽样，人不用条条看。
- 人在原文上划词写下判断。判断存进文件。agent 用 monitor 盯着新标注，把它们收成失败分类，并回到已看过的 trace 里找同类。
- 新的失败类型由人加。她试过让 agent 提议新类型，觉得是在替 agent 的口味背书，就改掉了。人说出来，agent 把它用到更多 trace 上。
- skill 是开放的，聚类方法不写死。她说自己还在改，不认为已经有人做出很好的 error discovery skill。

## 原文摘录

> “What good means for your product is living in your head. It's not in the traces.”
> “you can't just farm out evals to your AI coding agent, but you can still use AI to help you.”
> “80% of issues in the data are often caused by 20% of failure modes.”
> “I don't tell the agent to find me entirely new examples of failure modes. It's not changing the taxonomy. That's really left to me.”
> “there will be some human element in Evals always.”

## 最小主张

- 支持：窗内她本人的做法是，完成标准从标注里长出来，不在看数据之前写死。否决权在人：人决定一种失败算不算、优不优先。agent 负责把已说出的标准铺到更多 trace，并维持分类。量化发生在第二步，量的是每种失败有多常见，然后优先改那 20%。
- 不支持：没有给出 coding loop 的可核终态句，也没有独立小模型三值判定。80% / 20% 是她说「我们在 eval 里常见」，不是这次口播里的对照实验。她预告的厂商对比是后来 2026-07-11 的 Parlance 文（A3），口播里只说通用 coding agent 往往比专用发现工具更穷尽，没有工具能又全又准。字幕误听过人名，那句不单独当出处。

## 与已有档案

- A3 里「她自己的站未打开、视频未核对」作废。站 https://www.sh-reya.com 这次只在视频描述里出现，站本身仍未打开。
- 这场不给 Anthropic `/goal` 或 Osmani 的硬规则加票。它回答的是定调里「设计不出来」。
