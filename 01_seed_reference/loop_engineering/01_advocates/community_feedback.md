---
type: community_feedback
directory: 01_seed_reference/loop_engineering/01_advocates
description: 推动派——技术社区反馈（2026-06 后，观测 2026-10-06；来自社区，非 KOL）
collected_at: 2026-10-06
---

# 推动派——社区反馈（社区情绪证据）

> **读法**：KOL 侧的推动派素材见本目录 [README.md](README.md)；本档只收**社区侧**（HN/GitHub/Reddit/dev.to/V2EX/掘金/公众号）。
> **纪律**：社区评论者**不是 KOL**，本档不进 KOL 台账、不与研究层 KOL 证据并列引用；厂商 issue 回复标"**厂商声音**"。
> 拆分说明：本档内容自 2026-10-06 三路社区扫描按派别拆入（原扫描档已撤，URL 即出处，观测日期均为 2026-10-06）。

## 一句话总述

**社区层没有推动派的热度**——本派的社区存在感形态是"少数派正方声音 + 中文教程层承担传播 + 自带边界的实践样本"，而热度全在失控/成本侧（见 [`../03_skeptics/community_feedback.md`](../03_skeptics/community_feedback.md)）。

## 一、HN / GitHub

**推动派锚点内容在 HN 的热度现实**（详串在 [`../03_skeptics/community_feedback.md`](../03_skeptics/community_feedback.md)）：
Osmani 定义文 11 分/6 评论、Andrew Ng 4 分/1 评论、LangChain 四环 2 分/1 评论——无一破 40 分；
同窗 Ronacher《Tower》558 分、DN42 账单串 1467 分。Brittany Ellich《108 PRs in eight days》37/10，评论区以"push slop / 免人审被逐字批判"为主。

**散见的社区正方声音**（均出自反对侧主导的串，完整串见 skeptics 档对应条目）：

> "You don't need to 'maintain' a comprehension as you can just ask (with loops as well) anytime you want something... Actually, no model should directly answer to you in a proper workflow, it should always be another agent digesting and verifying."—— hn 用户 pixel_popping（Osmani 定义文串内唯一的正方）

> "Tokenmaxxing was just a way to force employees to start leveraging AI in a meaningful way... It was always a temporary thing to transit..."—— hn 用户 aurarevelop（tokenmaxxing 串内的辩护少数派）

> "Actually now we care even more... AIs don't care, they'll happily write 50 unit tests with slight variations... Now we have at least SOME tests."—— hn 用户 theshrike79（Tower 串内为 AI 测试辩护，随后被顶回）

**受约束的无人值守实践样本**（Ask HN《Do you give AI agent the specs and have it start building unattended?》2026-06-02，5 分/1 评论——窗口开启首日即有同构答案）：

> "I'm using 'harness engineering' to do this: smaller tasks, well defined stop conditions, runs in a VM with --yolo-mode. I've worked up to this, and ended up rolling my own thing because nothing I found did what I wanted: agent fan-out, VM containment, full harnesses with test/exit conditions, runs fully unattended. I expend a lot more energy on plans, though."—— hn 用户 bradleyy

（注意其形状：无人值守＝小任务＋显式停止条件＋容器隔离＋前期投入更大——与 loop engineering 主张同构，但"现成工具都不行、全部自造"印证生态缺口。）

**dev.to 第一人称周报（本派社区层最强正样本）**：Umesh Malik《Is Claude Code Auto Mode Reliable in Production? A Field Report》（2026-06-25，实取全文，dev.to 无评论）：

> "my Claude Code token usage that week ran about **$100/day** in API-equivalent terms, roughly **$710** across the seven days, pulled straight from my session logs with `ccusage`."
> "auto mode is a force multiplier on tasks with a green test suite, and a liability on tasks without one. The tests are the steering wheel. The diff is just the receipt."
> "Used as a fast, tireless implementer behind a human checkpoint, it earned its place in my week. Used as a replacement for the checkpoint, it would have cost me more than it saved."

（判读注：这是"试用后继续用"的 conditional-positive 正样本；但其纪律——行为化目标、人守检查点——恰是中性派纲领。）

## 二、中文圈（推动叙事的主要承担层）

**V2EX｜《seek 的 goal 26 分钟跑了 3 轮，改了 28 个文件》（2026-06-01，亲历帖，sov2ex 全文可核）**：

> "我给它一个目标，它自己跑了 3 轮，期间分解任务、读代码、改代码，最后一共改了 28 个文件。整个过程我没有逐步指挥"
> "它走的是 goal：目标 → 分解 → 并行 worktree 子代理 → 聚合结果 → 本地 commit / 报告。"
> "这不是想说它已经可以放心自动 merge。相反，我现在的默认设计是保守的：无人值守可以跑，但结果默认留在本地，不自动 push/PR，第二天人再 review。"

（即使推动派手里，循环终点也自觉设在"本地 commit＋次日人工 review"——与英文圈"实现者不能自我批准"共识同构。）

**V2EX｜开源 Agent 项目 Maka 架构复盘（2026-07-14，工程派）**：

> "Self-check 不是 authority：模型自己说'我做完了'不算数，需要独立的验证逻辑来判断，防止 agent 自己给自己批卷子。"
> "这个成绩不是因为模型变强了，是 agent loop 里 self-check 机制的两轮迭代带来的。"（附实测：6000 万 token、97.5% 缓存命中、约 4 元人民币）

**公众号原创（程序员鱼皮，2026-06-16 首发，经腾讯云同步页实取，页面计数 4101）**——《还考提示词？知道 Loop Engineering 吗？》：中文圈把 /goal /loop 教学完整落地的一篇（Loop 三要素、熔断"20 轮还没搞定就停下来"），但同时自带三盆冷水：

> "没有判断能力的循环，AI 可能会把错误当成正确答案继续往下跑，越跑越偏。那跟 cron 定时脚本没区别，算不上 Loop Engineering。"
> "对于大多数普通开发者来说，一个月 20 刀的订阅套餐很难撑住高频循环。**跑的不是循环，是你的钱包啊！**"
> "有开发者说：所有人都在冲向 loops，但调试一个已经跑了 47 轮的状态机，比修好一个 prompt 难 10 倍！"
> "Loop 是放大器，能放大你的能力，也能放大你的懒惰。"

（判读注：中文推动叙事由公众号教程作者承担；其自认的成本/可调试性难点，正是 skeptics 档社区证据的主题。）

**掘金｜《我给 Coding Agent 加的 4 层工程约束》（2026-09-20，原创，热度极低仅作内容样本）**：

> "AI 很少因为'语法不会'而写错，它绝大多数时候失控，是因为它在错误的优化目标下，把代码写得'太像那么回事了'。"
> "传统的软件工程规范是为了**对抗人类的惰性与遗忘**；但面对 Agent 时，工程体系必须用来**对抗模型的顺从、过度生成与过拟合**。"

## 三、机构采样层的采用面（指针）

使用率暴涨的机构数据（SO pulse 31%→59%、Claude Code 41%→55%、JetBrains 90% 周用/平均 47% 代码 agent 全生成、"agentic coding is gradually becoming the new normal"）收在 [`../02_neutral/community_feedback.md`](../02_neutral/community_feedback.md) 机构采样节——中间态数据，两派都可引用，home 在中性档。

## 四、通道与方法负结论

- 推动派内容在 HN 的低热是**观测事实**，但不能据此断言"社区反对 loop 实践"——HN 热度与内容质量关联弱（Astra 文四次提交才起飞），且术语层与机制层要分开读。
- 中文教程层（公众号）热度数据只有单篇页面计数（4101），无评论样本；评论区情绪未知。

## 补抓增量（第二轮 · 2026-10-06）：通道重试

> **本节为第二轮补抓，上文对应负结论状态以此节为准**（"社区层没有推动派的热度"的判断需按本节作精细化：实操向正方内容在 Reddit 可获得中等热度，但伴随自推广争议；中文教程层声量仍显著低于质疑向）。
> 方法注记：本轮 `web_fetch` 通道 DNS 沉降不可用，全部改用 curl 直连（浏览器 UA）；Reddit 经 arctic-shift 存档 API 取原文。热度/计数均为 2026-10-06 观测值；所有逐字引句均来自本轮实际抓取的页面/JSON。

### 一、Reddit 正方实践样本（arctic-shift 实取全文）

**《[Senior engineer, loop orchestrator sample setup](https://www.reddit.com/r/ClaudeAI/comments/1wd44vj/)》**（u/croovies，r/ClaudeAI，2026-09-11，**323 分 / 55 评论**——本批 Reddit 正方向热度最高帖）：

> "The reason to use an orchestrator, is you have found yourself waiting too much for a single agent, or you're bouncing between too many. In both cases an orchestrator can help you scale your process as you evolve from directing code, to reviewing outcomes (and tossing out bad code and having it start over instead of worrying about driving every PR). Like a real manager."

方法论构件（正文自列）：agent 互发消息、按 loop 定时唤起 agent（"I usually set it to 90 minutes" ping 一次 orchestrator）、本地 SQLite 记录；mission note 按 Who/任务/验收分段。**社区摩擦注记**：评论区有人质疑自推广——"What is this entitled attitude you are bringing where you essentially shill your product on the Claude sub and then bristle at criticism?"（u/JayArrCoffee，并指出 Orca 等开源替代）——正方实操内容可获中等热度，但"带产品讲方法"会立刻被点破。

**《[Loop engineering: I turned the Ralph loop into a verified one. One markdown file, any agent, a critic before "done".](https://www.reddit.com/r/ClaudeAI/comments/1wa8e8g/)》**（u/raiyanyahya，2026-09-07，0 分 / 3 评论——低热工具帖，正文完整）：

> "The Ralph loop (while :; do cat PROMPT.md | claude; done) works, but it's blind: no memory between runs, it believes the agent when it says 'done', it never stops on its own, and nothing stops the agent from editing the tests that judge it."
> "I think the interesting skill now is loop engineering: not what you say to the agent, but what happens after it answers."

（附实测："Real run with Claude Haiku: three iterations, the loop rejected a premature 'done' in iteration 1 because two checklist items were still open, iteration 3 finished, the critic read the diff and approved. 2m13s."——开源 [github.com/raiyanyahya/loop](https://github.com/raiyanyahya/loop)。其设计要素 protect/critic/metric/brakes 与 skeptics 档的失控清单逐项对位——正方也在修同一张故障表。）

**散见正方声音**：《Claude Code making a "2 week plan" and then finishing it in 30 minutes is still weird to me》（r/ClaudeAI，2026-06-17，254 分 / 58 评论）——对委托加速的惊叹向标题热帖（标题级）。

### 二、B 站正方教程层（新增量，view API 元数据实取，2026-10-06 观测）

- 《[终于有人用一个视频把火遍全网的AI智能体新范式-Loop Engineering给大家一次性讲明白了！【码士集团】](https://www.bilibili.com/video/BV1tfLR6LEXE)》（UP：马士兵教育，2026-06-17）：**9,355 播放 / 608 赞 / 404 投币 / 1,126 收藏 / 95 弹幕**。教程化大纲（简介自列）："1.Agent Loop & Loop Engineering到底是个啥 2.从ReAct到Claude Code，Agent这4年经历了什么 …… 5.设计Loop 的11条军规 6.这7个坑，能让你的Loop原地爆炸 …… 8.手把手带你实现 Loop Engineering 案例"——培训产业已把 loop engineering 做成完整课程件。
- 《[循环工程：让AI自主完成编码 | Matthew Berman](https://www.bilibili.com/video/BV1RpES6LEFn/)》（UP：7k的每日搬运，2026-06-10，66 播放）——海外 KOL 内容的中文搬运层（简介概述"循环由'触发器'和'可验证目标'两部分组成。触发器可以是PR打开、定时任务或人工启动"）。
- **热度对照判读**（更新上文"社区层没有推动派的热度"）：中文圈正方教程（≈0.94 万播放）对质疑向头部【闪客】《新名词诈骗！你管这破玩意叫 Loop Engineering？》（10.98 万播放，见 skeptics 档补抓节）约 **1:12**——正方教程层在传播量级上仍被质疑向压制；但"培训课程化"本身是推动叙事产业化的信号。
- xie.infoq.cn 写作社区三篇推动/工程化向文章（标题＋账号已核，正文 JS 未取，部分解决）：阿里技术《Loop Engineering 概念解析、思考与实践》、容智信息《告别"面向玄学编程"：深度拆解 Loop Engineering 架构与企业级 Agent 避坑指南》、TiDB 社区干货传送门《亲测好用的 PDCA 组队法：玩 Loop 多 Agent，3-4 个才是黄金搭档》（"亲测好用"＝实践正方向）。⚠️ **勘误（第三轮）**：该文实为 2026-05-18 发布、讲的是名为 "Loop" 的团队协作**产品**——窗口外＋对象错位，不计入实践正方样本（详见中性档勘误）。
- 机构层正方向（InfoQ《QQ 飞车》全文，腾讯 300 亿 token/月的 loop 实操）已核，home 在中性档企业接收层（见 [`../02_neutral/community_feedback.md`](../02_neutral/community_feedback.md) 补抓节）——本档不重复。

### 三、本轮通道与方法负结论（仍开放清单）

- **mp.weixin.qq.com 鱼皮文原始页仍未定位**：搜狗微信搜索两次（全称＋短题）均"没有找到相关的微信公众号文章"；鱼皮 AI 导航转贴页（ai.codefather.cn/post/2066793761979092994，标题《提示词工程已死，Loop Engineering 称王！保姆级教程 + 项目实战》）静态 HTML 无微信原文链接——鱼皮文依据维持"腾讯云同步页"口径。
- B 站搜索 API 被风控（返回 HTML 而非 JSON）——本轮 5 条视频系经外部搜索引擎定位 BVID 后以 view API（无需登录）核到元数据；播放数之外的视频内容本体未核看。
- Reddit 层正方内容的评论样本有限（Ralph loop 帖 0 分 3 评、croovies 帖评论含自推广争议），"社区正方声音"仍以散见为主，无独立正方热帖。


## 拉取纪律执行（2026-10-06 用户定：两轮拉不到就放弃）

- **放弃**：Jensen Huang NVIDIA 一手（四路转引一致即终点，吹捧层以转引登记）；Nadella X 原文（经转译全文为终点）；Karpathy "remove yourself as the bottleneck" 原句（两个本人一手载体已足够）；Orosz 付费墙内容（§5–7 与六预测本体，双通道复证墙位不变）。
- **保留**：无（本派无"未发布"类项）。
- 本节之上的"仍开放"表述凡与本节冲突，以本节为准。

## 第三轮挖掘（2026-10-06）：中文圈（正方/教程层）

> 本节为第三轮挖掘。观测时间 2026-10-06 15:00–18:00 CST；通道：sov2ex API＋V2EX API v1（topic/replies 均实取，**本轮 V2EX API v1 恢复可用**，上轮仅 sov2ex）、curl 直抓、B 站 view API（搜索 API 仍 412，BVID 经外部搜索定位）。逐字引句均出自本轮实际抓取的 JSON/页面。V2EX 热度=回复数（API 实取，非页面阅读数）。
> **核心发现（修正上轮"选择性偏差"假设）**：V2EX 术语正方/工程向高回复帖**存在**——2026-06-28 一天出现三帖（25/19/16 回复）、`/goal` 实测报告帖群（13–36 回复）、"24 小时自动化"需求帖（63 回复）；**但这些帖的评论区以质疑/嘲讽为主导**——正方只在"楼主实测数据"层成立，评论层与英文圈同构。详见各条判读注。

### 一、V2EX `/goal` 实测正方帖群（术语已变成日常动词——本层最强正样本）

**V2EX｜《[/goal 跑了 80(62 + 18)h 的结果，18w 行代码。200 多个 commit。](https://www.v2ex.com/t/1228560)》（OP weixind，2026-07-20，13 回复，sov2ex＋V2EX API 全文可核）**：

> "先感谢 codex 最近疯狂重置，总共用了大概 40 亿 token 。"（OP，正文）
> "期间只有一次调整，让 AI 越过在 macOS 处理 Firecracker 的尝试。其他都是 AI 的自主行为，有点行为艺术了。"（OP，正文）
> "目标有强验收机制的情况下成功率会高一些，goal 越准确，跑偏的概率越小，不过跑 goal 会有一种能得出结论就算赚到的感觉，跑不出来在预期之中。"（OP 楼内）
> "架构推翻重来，而不是代码推翻重来。架构满意了以后再跑三天。"（OP 楼内，回应"不会也是💩山吗"）

（判读注：中文圈迄今最完整的 /goal 超长任务实测报告——80h/18 万行/40 亿 token 全部自报 GitHub 分支可查；其边界自觉（"跑不出来在预期之中"）仍是中性派纲领，正方叙事自带止损条款。）

**V2EX｜《[/goal 已经跑了 1d3h，完成 143 个 commit，8w 行代码。跑的我道心破碎。](https://www.v2ex.com/t/1227533)》（同 OP weixind，2026-07-15，25 回复）**：

> "整体的完成度要比我想象中高的多，之前类似的场景还需要很多次打断纠偏……这次我甚至觉得最终能够完成一个成熟的 cloud agent 产品。历史的车轮滚滚而来，已经碾我脸上了。"（OP，正文）

评论区工程派守则与质疑并存（正方守则与质疑侧逐字分别收在中性档与 skeptics 档补抓节同帖条目，此处不重复）。

**V2EX｜《[codex 是真的强 不知道用上 5.6 之后会有多爽](https://www.v2ex.com/t/1225067)》（OP a815584445，2026-07-05，12 回复）**：

> "昨晚丢了一个目标给他我就睡去了，早上醒来他就完美完成了，关键是才花了 73 分钟。这要是搁以前 一个月新 1w+的技术怎么也得 2-3 天吧"（OP，正文；附 agent 完成报告："已完成'切换到阿里云 AI 实时互动/ARTC 语音链路'这一阶段目标。最终用时约 73 分钟，本轮目标累计用量 1211655 tokens 。"）
> "你要先写一个 agetns.md 去约束他 给他 然后再给他目标，要描述详细"—— a815584445（楼内自答）

**V2EX｜《[有什么比较好的方案让 AI 实现 24 小时自动化开发？](https://www.v2ex.com/t/1243154)》（OP ldy619354397，2026-09-19，**63 回复**——本轮窗口内中文圈回复最高的工程向需求帖）**：

> "复杂任务 AI 动不动执行要 1~2 个小时，人不可能一直坐在电脑旁等结果，有没比较好的方案能让 AI 实现 24 小时自动化开发，并且可以设定哪个 AI 负责验收和补充，哪个 AI 负责开发。"（OP，正文）
> "让一个 subagent 干活，另一个 subagent 监督与调度"—— zls3201；"貌似 omo 仓库就已经被 agent 接管了 接收 issue 处理变更 开发测试 提交代码"—— zls3201
> "这个你完全可以自己按需编排 Agents 工作的，一个工作完了就通知另外一个 Agent 起床来验收，完全可以实现 24 小时无人值守。最终能不能真的实现需求，那要看运气了"—— jacketma

**V2EX｜《[codex 新手请教一下](https://www.v2ex.com/t/1223704)》（OP yrhhh，2026-06-29，5 回复）**："你们是怎么让 codex 执行长任务的，几小时的那种，怎么确保他不会在做的过程中做偏"（OP）；"开始压缩上下文效果就容易走偏了，得人工介入。另外高强度使用 Pro 额度很快就用完了"—— Nasdaq。
（判读注：/goal 在 2026-06 后的 V2EX 已从"术语"变成**默认动词**——"跑一个 goal""goal 中相关的几个文档"是自然口语；术语教学层（公众号/B 站）与实践口语层在此会合。）

### 二、V2EX 2026-06-28 术语讨论三连（术语正方向的高回复日）

> 三帖记录收在 [`../02_neutral/community_feedback.md`](../02_neutral/community_feedback.md) 中文圈节（三帖均为混合立场：OP 逐字按其立场拆入本节与 skeptics 档补抓节）。正方向逐字如下：

**《[凑热闹说下我对 Loop Engineering 的理解](https://www.v2ex.com/t/1223494)》（OP c0xt30a，2026-06-28，16 回复）**——OP 自述教学转化："当前 Codex/ClaudeCode 基本上用不完，使用的姿势还是 Prompt Engineering + Harness Engineering 。想尝试下 Loop Engineering 能否带来不同的体验。"（博客全文 fengwang.github.io，自称"文章是我引导 AI 写的，之后认真校对过"）：
> "写的挺好"—— wtcs；"写得不错"—— TrojanL；"我也写了一篇，欢迎交流"（echoVic，附自荐博客链接）
> "全篇我都看完了……日常工作中大部分场景还是停留在 Prompt Engineering 阶段……一线开发更关注的是其中一个点的开发，完成后还要做人工 review，如果真是大片大片的完成，再去人工 review，我是真没耐心"—— 5261（一线开发者长评，接受的边界恰是人工 review 频率）

**《[关于 Loop Engineering 的实践与反思](https://www.v2ex.com/t/1223398)》（OP yunshangzhou，2026-06-28，19 回复）**——OP 给出四阶段实践（发现问题→git worktree 并行→独立 agent 功能验证"防止 yes 幻觉"→MCP 存回 linear/notion/语雀，"再开/loop 以此往复"），但 OP 自己收尾即转怀疑（"本质都是围绕着提示词转悠……水友们你们怎么看？"——此句逐字归 skeptics 档）。评论区内工程派辩护少数派：
> "任务的设计并不只是'玩玩提示词'……如果不在任务中定义清楚偏好和边界（比如 日抛脚本/自用小项目/大型原型/线上老屎山），让 Agent 按自己理解发挥，做重了/做简单了，都是很正常的。所谓 Harness 搭的完善程度，也直接决定了 Agent 能把产出验证到什么程度。假设你让人（ Agent ）来改 css ，但是不给浏览器（ playwright+截图）、只能对着代码瞪眼，不是一样完成不好么？"—— Azure99
> "边界是人类和 AI 一起探索出来的，肯定不是 All in AI 。……从实践中找到了大致的规律，基本能快速上手 AI 领域新出的东西，踩一脚没必要。"—— Retas

### 三、B 站第二轮扩量（view API 实取，2026-10-06 观测；上轮 5 条之外新增 8 条）

| 视频 | UP / 日期 | 播放 / 赞 / 收藏 | 简介/定位 |
|---|---|---|---|
| [Agent 自我进化的基石：Loop Engineering \| 原理篇01](https://www.bilibili.com/video/BV1ktjB6xEDU/) | 极客魔导师 / 2026-06-19 | **3,152 / 92 / 292** | 系列化正方教程："去年所有人都在教你怎么 prompt agent。今年该停一停：你是不是成了循环里最慢的一环？……把自己从循环里换出去。" |
| [【2026最新版】Loop Engineering速通教程](https://www.bilibili.com/video/BV1esKE68Er2/) | 爱玩的小卿吖 / 2026-07-17 | 1,649 / 99 / 129 | 教程件 |
| [我睡觉的时候，AI还在给我打工！实测爆火开源项目 gnhf](https://www.bilibili.com/video/BV1KnEt6MECH/) | 鲲鹏Talk / 2026-06-07 | 1,361 / 40 / 93 | 无人值守实测向："gnhf（good night, have fun）……白天由人工作，晚上由 AI 工作。" |
| [【吊打付费】Loop Engineering实战教程](https://www.bilibili.com/video/BV1tutB6ZEtK/) | AI大模型编程_ / 2026-09-04 | 1,398 / 137 / 103 | 培训化教程（五大构建块＋案例） |
| [智能体Loop循环工程的艺术](https://www.bilibili.com/video/BV1Tnj46aErQ/) | 小工蚁创始人 / 2026-06-25 | 519 / 17 / 31 | 商业 UP 教程 |
| [行业新黑话？AI小白视角带你3分钟速通循环工程](https://www.bilibili.com/video/BV15FgQ6hEvv/) | AI_Funtrue / 2026-07-23 | 105 / 17 / 4 | 标题即"新黑话？"——UP 自嘲"有诸多不严谨的地方"；简介："做好视频之后发现又出现了Graph Engineering" |
| [Claude Code默认开启Auto模式：AI编程进入无人值守时代](https://www.bilibili.com/video/BV1LXgN6BELC/) | -与AI同行- / 2026-08-15 | 76 / 2 / 1 | 8-14 默认 Auto 模式新闻转述（"97%的权限提示被用户习惯性批准"） |
| [🚀Codex /goal命令你真用对了吗？保姆级教程](https://www.bilibili.com/video/BV13KR1BEEBm/) | AI超元域 / **2026-05-05（窗口起点前一个月）** | **40,501 / 777 / 1,478** | **B 站所见 /goal 主题最大流量**，早于术语命名潮——"goal 命令高级技巧……真正内置Ralph Loop"；含"七大不适用场景避坑指南" |

- 疑似质疑向系列目击：《[loop engineering07-循环工程的四笔账——验证债·理解腐烂·认知投降·token 失控](https://www.bilibili.com/video/BV1L23z6eEnN/)》——搜索索引在，B 站 view API 返回 **code 62002 稿件不可见**（已删/自隐）；"07"番号说明存在一个至少 7 集的冷水向系列，本体已不可核。
- 热度对照更新（上轮"正方教程 ≈0.94 万 vs 闪客 10.98 万≈1:12"）：加入本轮 8 条后，正方/教程向合计约 **5.0 万播放**（其中 4.05 万集中在窗口前的 /goal 教程一条），对质疑向头部仍约 **1:2.2**——若剔除窗口前那条 /goal 教程，窗口内正方教程总播放仅约 0.95 万，量级差扩大到约 **1:12** 维持不变。

### 四、博客园 / 华为云 / 阿里云 / 腾讯云教程层（全部 2026-06 后，本轮实取）

**博客园｜《[Loop Engineering 实践教程：从写提示词到设计循环，2026 年 AI 编程的新范式](https://www.cnblogs.com/vibecodinghuanzhe/p/21080664)》（vibecoding患者，2026-07-02，全文实取）**——**编译/整理判定**（自标数据来源：cobusgreyling/loop-engineering 仓库、Osmani 2026-06-07 博文、Ng《The Batch》359 期，"均实时抓取核实"）：
> "Loop Engineering 把你从'出题人'升级为'出题系统的设计者'：定义目的、验证标准和边界，让循环自我供给提示词、按时间表运行、按需生成帮手，直到目标达成。"
> "中环不可自动化：Ng 用'上下文优势'（context advantage）替代'品味'一词——只要人类知道 AI 不知道的事（用户、场景），human-in-the-loop 就必须存在。"

**博客园负结论**：另一篇《提示词工程过时了吗？为什么 2026 年大家开始谈 Loop Engineering》（aiwangjianguo，cnblogs.com/aiwangjianguo/p/20691708）——搜索索引在，本轮实取时页面 302 至"用户中心"，正文已不可得（疑删除/私密）。

**华为云开发者社区｜《[Loop Engineering：让 AI Agent 自己跑起来的工程方法](https://bbs.huaweicloud.com/blogs/483067)》（云宝助手-OpenTiny，发表 2026/07/29，全文实取）**——**编译+自写混合判定**（引用 Steinberger/Cherny/Osmani 原推并给中文时间线；Ralph Loop、/goal、Osmani 五组件）：
> "Loop Engineering 不是智能体工作流。智能体工作流把多步调用串起来，步骤是你提前定好的，模型只负责在每步里填空。路径已知，模型执行。Loop Engineering 更进一步——你不再定义路径，你定义循环和验收标准。Agent 自己决定每轮干什么、怎么干、干完谁来验。路径未知，系统探索。"
> "Loop 的质量完全由停止条件决定——/goal 需要一个不需要人就能判断'完没完'的裁判。"
> "机器能不能独立判断这个产出对不对？能，搭高自主性 Loop；不能，Loop 仍然有用，但你需要参与定义停止条件。"

**腾讯云开发者社区｜《[Loop Engineering 实战：/goal 命令让 AI 自己写完整项目](https://cloud.tencent.com/developer/article/2700164)》（程序员天天困，2026-06-29，正文实取）**——**原创实战判定**（社区首发，无公众号同步标记）：
> "说实话，我第一反应也是「又来？Harness Engineering 还没学完呢」。但上周三晚上，我在 Claude Code 里敲了一行 `/goal` 命令然后去洗澡，回来发现 AI 已经自己建好了项目结构、写完了数据库 Schema、搭了 4 个页面，还自己跑通了构建验证。整个过程我一个字没打。体验完之后我不得不说：这玩意儿是真的有用。"
（质量注：文中把 Peter Steinberger 写成"OpenAI 的 Peter Steinberger"——硬伤，转述需校对。）

**腾讯云｜《[Claude Code 迎来重磅更新！/loop 命令正式内置：让你的 AI 助手真正"24h 值班"](https://cloud.tencent.com/developer/article/2701685)》（不一样的猿生，2026-07-01，正文实取，原创梳理）**：
> "这已经不是简单的助手，而是能真正'替你上班'的 AI 同事了。"（另录 Boris 例句中译："/loop babysit all my PRs. Auto-fix build issues and when comments come in, use a worktree agent to fix them"）

**腾讯云｜《[Claude Code /loop 指令最佳实践：让AI自己盯着你的代码干活](https://cloud.tencent.com/developer/article/2687681)》（老周聊架构，2026-06-12，正文实取，原创教程）**：
> "你有没有过这样的经历：部署了一个服务，然后每隔5分钟手动刷一下页面看它跑起来没有。……恭喜你，你不是在写代码，你是在当人肉监控。"
> "用人话说：你给 AI 发了一条'闲着没事就自己找活干'的指令。"

**阿里云开发者社区｜《[AI Agent 的 4 个工程关键词：Prompt、Context、Loop、Harness 到底是什么？](https://developer.aliyun.com/article/1740864)》（七牛开发者，2026-06-11，页面计数 650，全文实取）**——**原创教程判定**（四词分章拆解）：
> "Loop Engineering 的重点不是让 Agent 无限制地自动干活，而是把执行、反馈、验证、修正、记录、接管这些步骤串起来。Loop Engineering 要解决的是：Agent 怎么持续推进任务，而不是只完成一次回答。"

**阿里云｜《[Loop Engineering：从 Prompt Engineering 到迭代式智能体工程](https://developer.aliyun.com/article/1747820)》（浅浅33，2026-07-15，页面计数 391）**——正文 JS 未取（仅摘要层）：简介自述"Loop Engineering 是2023年起在Agent实践中沉淀的工程方法论"——**时间线硬伤**（术语 2026-06 才命名），疑低质改写，引用需慎。

### 五、即刻（okjike）两条原帖（移动端页直抓，2026-10-06 实取）

**《[分享下我使用 Codex 的一些习惯](https://m.okjike.com/originalPosts/6a56efd69044d15af20d4084)》（小盖fun，约 2026-07〔页面自标"3月前"〕，81 赞 / 4 评论 / 7 转发 / 28 分享，内嵌 JSON 实取）**——即刻侧最接近"社区实践者长文"的样本（非头部 KOL，未核粉丝量）：
> "最近硅谷又开始流行一个概念，叫 Loop Engineering。简单来说，就是让 Agent 在一个任务中持续执行、检查、修正，直到达到目标。我觉得它和 Prompt Engineering 依然有很多弯弯绕绕的关系。到今天为止……提示词依然很重要。"
> "当 AI 可以独立完成越来越多工作之后，人很容易只关注最后的结果。……我们会逐渐失去对项目的理解。这种理解层面的让渡非常可怕，因为后面一旦 AI 出问题，搞不定了，需要我们接手，那我们面对的可能完全是一个黑盒。"

**《[Claude 官方写了一篇关于 Loop Engineer 的入门文章](https://m.okjike.com/originalPosts/6a4c8e2364a7b806f1c1ff8f)》（**歸藏**——KOL 身份，**只作传播节点记录，不作社区声音引用**；约 2026-07〔"3月前"〕，35 赞 / 11 评论 / 5 转发 / 15 分享）**——Claude 官方 Loop Engineer 入门文（四类循环）在即刻的完整转述节点，自带降温框架："其实现在我们所说的 Loop Engineer，所有的底层逻辑在提出这个概念以前就已经具备了……只是被套上了一个新的概念。"

### 六、鱼皮文同步通道补登（解决上轮"腾讯云同步页之外无通道"缺口）

- **阿里云同步页**：《[提示词工程已死，Loop Engineering 称王！保姆级教程 + 项目实战](https://developer.aliyun.com/article/1742077)》（2026-06-17，页面计数 409，实取）——鱼皮 2026-06-16 原文的第二个社区同步通道（第一个为腾讯云 article/2709808，页面计数 4101）。mp.weixin 原始页仍未定位（维持）。
- **腾讯云新同步**：《[Claude Code 的 /loop 与 /goal 到底区别在哪里？](https://cloud.tencent.com/developer/article/2697483)》（乐小野，2026-06-24）等技术拆解文见 [`../02_neutral/community_feedback.md`](../02_neutral/community_feedback.md) 中文圈节。

### 七、本轮通道与方法负结论（仍开放清单）

- **即刻**：web 搜索 API（POST /api/v1/search 等）405；搜索页 JS 空壳；内容经外部搜索引擎定位 m.okjike.com 原帖 ID 后直抓成功——**该组合通道可用**，但系统化检索不可行，只能点状定位。
- **博客园找找看**（zzk.cnblogs.com）：命中前需人机验证，搜索通道不可用；文章直链可抓。cnblogs aiwangjianguo 文已 302 至用户中心（正文消失）。
- **B 站搜索 API 仍 412 风控**（与上轮同）；view API 正常——BVID 定位继续依赖外部搜索引擎。
- DuckDuckGo HTML 版 CAPTCHA、Bing 302——外部搜索引擎通道整体劣化，本轮依赖 web_search 聚合接口定位 URL。
- 奇绩创坛《循环工程：最大化杠杆作用，实现无人值守任务》镜像（news.miracleplus.com/share_link/136657）本轮 404——未取到，不作引句。
