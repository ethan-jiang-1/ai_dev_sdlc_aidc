# Evidence 2026-09-27 · A3 · 按引用链看谁在谈论

- 观测日期：2026-09-27
- 本档案回答：上一轮把「窗内一手少」写成了「没什么人在说」。顺着已打开页面的引用再走一截，谈论的人不少；没沉淀、仍在摸索，是另一件事
- 不回答：这些人各自的 goal 写法是否已经可操作。没打开的页只登记链，不摘句

## 链 1 · LangChain → Latent Space

Runkle 2026-06-16 点名 swyx 的 loopcraft，给出的 URL `https://www.latent.space/p/ainews-loopcraft-the-art-of-stacking` 在观测日返回 404。活页面是：

- URL：https://www.latent.space/p/loopcraft
- 发布窗口：页眉写 “AI News for 6/10/2026–6/11/2026”。署名栏是 Latent Space 的 AINews，swyx 办的通讯
- 访问/观测日期：2026-09-27【公开部分主验；付费墙之后未读】
- 原文摘录（公开部分）：
  > “Don’t fix things yourself, as you have done historically. Instead focus on systems that scale with more agents, like goals and orchestration.”
- 该摘录支持的最小主张：2026-06 中旬这份通讯把 goal 说成该往上叠的一层，不是某一条完成条件怎么写。同页声明扫过 12 个 subreddit、544 个 Twitter。这是社区在传，不是一份做法。
- 不支持什么：付费墙后的名单和原帖没有读到。不能从「通讯在汇总」推出每个被点名的人已经会构造 goal。

同站另一页已打开：

- URL：https://www.latent.space/p/aiewf-daily-dispatch-loops
- 访问/观测日期：2026-09-27【主验】
- 原文摘录：
  > “swyx began by commenting on the evolution of AI engineering from 2022: from chat, to tools, to goals.”
  > “These days, we’re all about automations,” he added. “We’re all about cron jobs and loops.”
- 该摘录支持的最小主张：会场日记确认开场标题是 Loopcraft，并把演化说成从 chat 到 tools 到 goals。同页没有一条完成条件，也没有检查句子。
- 不支持什么：这是记者的转述，不是 swyx 讲稿全文。不能从「谈到 goals」推出他已经写出可核终态。

## 链 2 · Hamel → 还在摸标准的人

- URL：https://parlance-labs.com/blog/posts/auto-evals.html
- 发布日期：2026-07-11。作者 Antaripa Saha、Hamel Husain
- 访问/观测日期：2026-09-27【主验】
- 原文摘录：
  > “You need criteria to grade outputs, but grading outputs is how you discover your criteria, a phenomenon known as criteria drift.”
  > “Fully automated approaches always failed to catch interactions that “looked correct” but fell short of providing a great user experience.”
  > “No system we tested did the one thing that would have helped most: interview us.”
- 该摘录支持的最小主张：他们用 100 条真实租赁对话、39 个亲手标出的失败，去对 Braintrust Loop、Arize Alyx、LangSmith、Codex、Factory Droid、Claude Code。最好的召回 87.2%（Braintrust），但每家都漏掉「看起来对、其实没达到产品目标」的一类。作者写明这是一个数据集，不能给厂商排名。标准是边看边长出来的，不是先写死再自动跑。
- 页内点名：Shreya Shankar。口播已核对，见 [`evidence-2026-09-27-a5-shankar-talk.md`](evidence-2026-09-27-a5-shankar-talk.md)。criteria drift 的论文是 2024 的 arXiv:2404.12272，只作她被引用的旧锚，不入本窗证据。
- 不支持什么：不证明 87% 可以外推。不证明「先看数据再写标准」已经是行业步骤。

## 谁在说（只计本主题已打开的页，或该页上的实名引用）

| 谁 | 状态 | 依据 |
|---|---|---|
| Osmani、Runkle、Hamel、Anthropic 文档与博客、OpenAI cookbook、Cursor changelog | 已有一段可操作说法，分见 A / A2 | 已主验 |
| Saha | 与 Hamel 同一篇 7 月 11 日实验的共同作者 | 本档案链 2。不另算一家 |
| Shankar | 窗内在教「先标注、再让 agent 找同类失败」；标准会漂移是她被引用的理由 | 口播已核对。个人站已打开，是学术主页，没有完成条件写法 |
| swyx / Latent Space AINews | 2026-06 中旬在汇总「把 goal 当成可叠的一层」；会场开场把演化说成 chat → tools → goals | 公开段和会场日记已读。Loopcraft 付费墙后仍未读。日记里没有完成条件 |
| Runkle 点名的 Steipete、Boris、Andrej、Satya | 被写成「也到达了循环」 | Steipete 见 A9。Boris 见 A4。Karpathy 见 A10，两帖都在窗边。Satya 仍没有完成条件原文 |
| Yeret | 技术完成条件和业务结果的差别 | 日期已核为 2026-05-27，节拍在 C 档 |

## 判读

- 观察：从一篇公司博客走到通讯，从一篇 eval 实验走到共同作者和课程搭档，名字会变多。变多的那一层里，很多是「在谈 goal / 在谈标准还没定」，不是「已经写出可核的完成条件」。
- 推断：这个题目新，所以沉淀薄。薄不等于没人说。下一轮继续沿已打开页面的出链走，不回到全网泛搜。
- 与 A / A2 的关系：不改它们已写的机构机制。只撤销「没什么人在说」这种读法。

## 负结论与限制

- Loopcraft 公开段于 2026-09-27 再读到 Twitter 回顾为止。公开段把 goal 说成该往上叠的一层，没有检查句子。付费墙从 Reddit 回顾开始，墙后仍未读。会场日记已读，也没有检查句子。
- 推文被点名不等于那个人写过 goal 构造。Steipete、Boris、Karpathy 已另档主验。Satya 仍停在引用关系。
- 87.2% 是一个租赁数据集上的召回，作者自己禁止把它读成厂商排名。
