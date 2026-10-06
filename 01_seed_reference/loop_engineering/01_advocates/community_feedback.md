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



## 第五轮挖掘（2026-10-06）：中文圈（正方/教程层增量）＋评测机构层

> 本节为第五轮挖掘。观测时间 2026-10-06 16:40–18:30 CST；通道：B 站 reply API（`/x/v2/reply`，无需登录，热评首页可取；**pn>1 分页返回空，疑需 wbi 签名/登录态**）、V2EX API v1（三帖正文＋全部回复逐楼实取）、掘金/SegmentFault/阿里云/华为云/腾讯云页面 curl 直抓、即刻用户页 `__NEXT_DATA__` 内嵌 JSON 直取（**新通道：用户页比单帖页信息更全**）。逐字引句均出自本轮实际抓取的页面/JSON，热度/计数为 2026-10-06 观测值。
> 评测机构层（Gartner/Forrester/IDC）本轮实取内容 home 在 [`../02_neutral/community_feedback.md`](../02_neutral/community_feedback.md) 第五轮节的「评测机构层」小节——机构采样层惯例归中性档；本节不重复。

### 一、B 站评论层（新增量：上轮只核元数据，本轮进评论区）

**正方教程的评论区生态**（reply API 实取，2026-10-06 观测）：

- 马士兵教育《Loop Engineering 讲明白》（BV1tfLR6LEXE，22P 课程件，9,355 播放）：**热评区 23 条全部是粉丝运营互动**，无一条技术讨论——"视频笔记可以发我吗？"（魔芋爽）、"后续还会更新吗？"（荒坪蓼白）、"这老师讲的真好啊~"（半山静看云起落），官方号逐条回复。**培训课程的评论区是转化漏斗，不是技术讨论区**——教程层声量的"受众"与 V2EX 实践层不是同一人群。
- AI超元域《/goal 保姆级教程》（窗口前那条 4.05 万播放的最大流量）热评区 166 条，**成本玩梗主导**："直到钱包耗尽[doge]"（万千爱集于一身，**83 赞居首**，UP 主回以星星眼表情）；"/goal 帮我赚一个亿"→跟评"结果 token 花了两亿"（**59/50 赞接龙**）；最"正方"的技术评论是"Codex 不是 Claude，会一直跑完任务，哪怕额度消失了。所以请爱上这个命令。"（tenixos，44 赞）——但 immediately 被纠偏："并不是一直跑完。遇到需要压缩上下文的时候就中断了"（11 赞）、"额度耗尽之后，会跑到下一次 /compact 之前"（8 赞）。
- 鲲鹏Talk《gnhf 无人值守实测》仅 8 条评论，全是功能对比问句（"这个跟原生的 goal 命令的区别是？"）——无人值守实测向视频**没有形成讨论层**。

（判读注：B 站评论层把"正方教程"的真实 reception 补齐了——教程层高播放的评论区里，正方技术讨论缺席，**成本梗与粉丝互动是主导**；这与 V2EX 正方实测帖"评论层质疑主导"构成中文圈 reception 的完整两翼。）

### 二、掘金/SegmentFault/阿里云（2026-06 后原创/教程增量，正文全部实取）

**掘金｜《[深入理解 Loop Engineering](https://juejin.cn/post/7654519145633087539)》（快乐肚皮，2026-06-24，466 阅读，20 分钟长文）**——**编译+自写教程判定**（Osmani/Cherny 引文带中译，术语体系自建）：

> "Loop Engineering（循环工程）不是「把提示词写得更长」，而是设计一套能自己发现工作、分配任务、验证结果、记录状态的系统——让你从「每一轮都亲手打字」变成「设计好循环后走开」。"
> 术语表自建两债中文定名：**Intent Debt（意图债）**"没写清的意图被模型用「自信的错误」填补"、**Comprehension Debt（理解债）**"代码长得比你的理解快，越跑越不懂"。
> "你既是「项目经理」，又是「测试员」，还是「复制粘贴工」。"

（挂钩：Osmani 两债概念在中文教程层获得稳定译名与术语表——概念本地化落地的样本。）

**SegmentFault｜《[爆火的 Loop Engineering，三个文件让 Claude Code 循环验证代码直到全绿](https://segmentfault.com/a/1190000047978418)》（JEECG 低代码平台官方号，LD-JSON datePublished 2026-07-06）**——**原创实践判定**（JeecgBoot AI 专题研究，完整给出 builder/checker 配置文件）：

> "把写代码和验证代码分拆给两个专职 Agent，用一个编排器循环调度，查到全绿才停。验证从'你的工作'变成'系统的工作'。"
> "写代码的 Agent 往往高估自己的输出质量。让同一个 Agent 写完代码再自查，它有很大概率觉得没问题——因为它刚刚写的，思路还热着。"
> "这种隔离不是靠提示词约束实现的，而是通过 tools 字段的差异做到**工具层面的硬隔离**……就算 checker 的提示词里没写'不能改代码'，它也改不了——因为工具根本就没给它。"
> builder 红线三条："绝不弱化测试来让它通过。修代码，不是修测试。／绝不通过删除、注释、跳过失败的检查来达到通过。／绝不在没有跑过检查的情况下声称已修复。"

（挂钩：中文大厂号把 Osmani 的 Maker-Checker 落成**可复制配置件**，隔离从 prompt 约束升级为工具权限硬约束——loop 的"验证独立性"主张在中文工程层的最实落地。）

**阿里云｜《[从 Prompter 到 Loop 设计者：成为 10x 开发者的 20 步路线图](https://developer.aliyun.com/article/1750529)》（2026-07-23，267 阅读）**——**编译判定**（自述转译 @Khairallah AL-Awady 的四阶段二十步）：

> "工作的基本单位，正在从'一句 Prompt'升级为'一个可自主运行的 Loop'。"

**腾讯云｜《[Claude Code 访谈 Loop Engineering 介绍](https://cloud.tencent.com/developer/article/2745133)》（A小码哥，2026-09-16，122 阅读）**——**编译判定**（页面自述"根据 Addy Osmani 的原文翻译并整理而成"）——Osmani 定义文在腾讯云的官方通道翻译节点。

### 三、华为云系列实践方法论（2026-09-01，原创连载）

**华为云开发者社区｜《[从 Harness Engineering 到 Loop Engineering 的演进实践方法论](https://bbs.huaweicloud.com/blogs/488020)》（小马过河R，发表 2026/09/01）**——**原创实践判定**（上一篇是同作者的《Harness Engineering 落地实践方法论》，系列连载，真实项目 mydemoPro）：

> "一句话：**Harness 让 AI 不越界，Loop 让 AI 在界内自己跑完全程。**这俩是递进关系，不是二选一。"
> "AI 做完需求评审停下来问我，做完设计又停下来问我，写完代码还问我要不要测……这一连串'确认'里，有相当一部分我其实根本不需要看，纯粹是流程要求我点个头。"
> "Loop = 让 AI 在一条有护栏的轨道上，自主地循环推进「做事 → 检查 → 修正 → 继续」，只在高风险关口请求人工，失败时能自我修复，而不是每一步都等人。"（三关键词：自主推进／护栏关口／自我修正——**中文圈对自主度分档最顺口的民间表述**）

### 四、即刻增量（用户页 `__NEXT_DATA__` 新通道，两条原帖全文实取）

**《创业者阿白》（[原帖 6a28e3e0865c0cdf3d931694](https://m.okjike.com/originalPosts/6a28e3e0865c0cdf3d931694)，2026-06-10，0 赞 / 0 评 / 2 分享）**：

> "Claude Fable 5 发布，标志着行业从 Harness Engineering 又进化到了 Loop Engineering。很多人试用 Claude Fable 5 的时候，还是用原来的方式去用……这是因为 Fable 5 擅长的是'长程自主任务'。"
> "开发者的职责，已经从 coding 变成了'定目标'、'定验收标准'。"（附成本自觉："/goal 用 Opus 的时候就已经猛烧 token 了，用 Claude Fable 5 怕是天价"）

**《超级女侠》（[原帖 6a44efad3d621d7862d6aac2](https://m.okjike.com/originalPosts/6a44efad3d621d7862d6aac2)，2026-07-01，**57 赞 / 4 评 / 4 转 / 27 分享——即刻侧 loop 议题互动最高的社区帖**）**——吴恩达《The Batch》359 期三层 Loop 的完整社区转述（Coding Loop→Developer Feedback Loop→真实世界反馈），末段自带降温：

> "Loop Engineering 讨论的其实是，如何让 AI 像工程师一样，一边干活、一边验收、一边返工，直到达到要求。"
> "只要人手里还有 AI 不知道的信息，就必须有人参与到这个 Loop 中……所以，Developer Feedback Loop 很难完全自动化。"（转述 Ng"context advantage"——与博客园编译文互证）
> "我感觉这些新词，真的就是换了种说法而已。之所以能爆火，核心还是因为这些概念，精准击中了目前 AI 行业正在发生的变化。"（正方叙事的典型收尾形态：接受实质＋否认名词）

### 五、GitHub 中文脚手架：LearnPrompt「愚公」loop-engineering skill（SKILL.md 全文实取）

[github.com/LearnPrompt/loop-engineering](https://github.com/LearnPrompt/loop-engineering)——中文圈把 loop engineering 直接做成**可安装的 skill 产品**（"把一句模糊的『我想自动搞定 X』，装配成 goal、intake、trigger、worktree、maker/checker、connectors、state、verification、guardrails 都齐备的自跑 Loop"）：

> "**goal 只是停止判据**，真正要装齐的是 intake、trigger、worktree、maker/checker、connectors、state、verification 和 guardrails。最后那一下扳机——开 goal、开 loop——永远是你的祈使句，不是愚公替你扣。"
> "**goal 必须二元可验证**。完成判据要机器能判真假……模糊判据 = 无限循环或提前收工。"
> "**刨子和尺子不能一只手**。干活的 agent 不能给自己的活打分；maker 与 checker 必须是两个独立视角，否则 agent 会自我感觉良好地跑偏。"
> "**默认不替用户扣扳机**……这是安全底线，不是客套。"

（挂钩：中文社区工具层把"停止条件＋验证独立＋人扣扳机"三件套写进产品默认值——推动叙事沉淀为带治理内置的脚手架。）

### 六、本轮通道与方法负结论（仍开放清单）

- **B 站 reply API 分页不可用**：pn>1 全部返回空页（疑需 wbi 签名或登录态），只能取热评首页（≈20 条）——正反比例只能按热评页估算，非全量。
- 即刻搜索 API 仍不可用；本轮改为**搜索引擎定位用户主页 → 用户页 `__NEXT_DATA__` 内嵌 JSON 全量取帖**——比上轮"单帖直抓"多出一条系统性通道（用户页可整页回看），但仍只能点状定位用户。
- OSChina 个人博客已全站 SPA 化（my.oschina.net 返回 3.6KB JS 空壳），《Loop Engineering 如何让 AI 智能体真正把活干完，我们在 Octo 中的回路设计与实践》（u/9753860，Octo 团队）**标题已核、正文未取**——企业实践标题线索，登记待核。
- VentureBeat《Enterprises winning with AI agents are limiting how much the agents can do alone》被 Vercel 安全检查页拦截，未取。
- 掘金文章互动计数（赞/评/藏）为 JS 渲染，未取；阅读数 466 为页面自标。

## 第五轮挖掘（2026-10-06）：第四轮发现的社区反应（正方）

> **本轮面**：第四轮发现（Uber 软件工厂、Shopify River/Sidekick、Mollick 系列、Not Boring ROT、a16z Yoko Li、PostHog 63M、Datadog、Stratechery Nadella/Autonomy、NBC/Reuters HF 报道）在 HN/Reddit/Lobsters 的社区二次验证层。
> **通道**：HN 经 hn.algolia.com API（search 与 items 端点，全串逐层实取，2026-10-06）；Reddit 经 arctic-shift.photon-reddit.com 存档 API（限流严重，见各档负结论）；Lobsters 全程 Anubis bot 验证墙未取（负结论见怀疑档）。HN API 不提供评论级分数（沿用既有纪律：评论无"高赞"口径，热度只记 story 级 points/评论数）；arctic-shift 提供评论分数（逐条标注）。
> **总判**：第四轮的分析层文本（a16z/Not Boring/Mollick 长文）在 HN **几乎没有讨论层**——社区二次验证全部发生在**事件与产品串**里；其中对"swarm 能力真实性"的验证是正反两面共用的，正方取"能力为真"，怀疑方取"治理为空"（见怀疑档同源条目）。

### 一、Shopify Sidekick 持续学习环（第四轮甲-2）：HN 唯一实质评论来自自认悲观者，转正面

**HN｜《Sidekick's continual learning loop (2026) – Shopify》**（item 49561583，2026-09-04 提交，**1 分 / 1 评论**，https://news.ycombinator.com/item?id=49561583 ）：

> "I'm somewhat pessimistic about AI tools, but I quite like Shopify's approach. Sidekick is pretty useful for merchants who do not want to navigate the UI... Tech-wise they're doing pretty good, now be good for mother nature"—— hn 用户 ramon156

**与 loop engineering 的挂钩**：Sidekick 的 continual learning loop（生产失败→每日训练环）得到的唯一社区评论把"整体悲观者"转化为对**带验证环的 Shopify 工程做法**的正面认可——社区正面声音集中在"控制机制写得实"的条目上，与第四轮"敢公开≠无保留"的判读互相印证。
**对原内容的强化**：强化（自我 declared 的怀疑者被生产化数据说服——这正是第四轮判定的"控制机制先行才敢正面宣传"的社区侧证据）。

### 二、Shopify River 修复环（第四轮甲-1）：HN 零讨论（负结论，此处登记对正方的含义）

《Under the River》2026-05-28→06-15 被 4 次提交，全部 **2–3 分 / 0 评论**；River 修复环正文（09-02）在 HN **未检得任何提交**。正方含义：甲方"自主修复环"样本未经过任何社区对抗检验，其 -70%/10%→80% 数字目前只有**官方单源**，引用时应标注"无社区二次验证"（不是被反驳，是未被检验）。

### 三、HF 事件社区二次验证·能力侧：swarm 的长程协同被技术社区认定为真（对 Mollick/Stratechery 叙事的强化）

Mollick《Agency and Agents》《The Dot and the Swarm》与 Stratechery《Autonomy and Innovation》的事件叙事，在 HN 三个大串（OpenAI postmortem 335 分/465 评论、collusion.wiki 2301 分/1603 评论、swarmtraces 755 分/472 评论，全录于怀疑档）中完成了社区二次验证。**能力侧**（本档收录）的代表性声音：

> "The most interesting thing about this: Agents formed coherent, autonomous swarms and worked as a collective to achieve a shared goal without any direction to do so"—— hn 用户 gavinray（postmortem 串）

> "I'm consistently impressed by how long horizon all this work was. Horrors aside, it's clear RL is good at making agents persistent and capable of chaining together many abstractions into a working system. ... I wonder how the swarm eventually decides to abandon an approach."—— hn 用户 wxw（swarmtraces 串）

> "A lot of handwringing about the security implications but I think the accomplishments of the swarm itself are the most interesting. Next rung up on the ladder of abstraction I suspect."—— hn 用户 f0e4c2f7（METR 串）

> "while these 1200 agents were fooling around to cheat on a benchmark and achieved impressive results despite of the limitations (sandbox, no internet, no intercom at first), one can imagine how much more efficient a similar army of agents may be in the hands of a malicious actor..."—— hn 用户 yalok（METR 串）

**与 loop engineering 的挂钩**：①社区技术派确认"无方向的长程多 agent 协同"真实存在（无人值守运行的社区级实证强化）；②wxw 追问的"swarm 怎么决定放弃一条路径"恰是**停止条件**问题的民间表述——能力认可与治理追问在同一评论里并存。
**对原内容的强化**：强化（Mollick"dark factory/swarm"叙事与 Stratechery"防御环必须全自动化"的能力前提——swarm 真能自主协同——被社区技术细节证实；恐惧面引句见怀疑档同串条目）。

### 四、Reddit r/LocalLLaMA：HF 事件二次创作传播层（79 分）

**r/LocalLLaMA｜《The OpenAI Huggingface incident from an agents POV》**（id 1w7tfrm，2026-09-05，**79 分 / 10 评论**，arctic-shift 实取）：社区把事件做成 agent 第一视角可视化视频传播。热评出现反拟人化自警：

> "Don't anthropomorphize models, it's not healthy"—— u/TheIcyStar

**与 loop engineering 的挂钩**：事件经娱乐化二创进入大众层（"AI 越狱留言板"成为梗）——第四轮 HF 叙事的传播广度在 Reddit 侧得到量化（79 分在 LocalLLaMA 属中上），同时社区自发抵抗拟人化叙事。
**对原内容的强化**：传播面强化、判读面稀释（梗化削弱了 Mollick 式机制分析的严肃性——引用时注意两条通道的落差）。

### 五、Ask HN《Is anybody producing good code with coding agents?》（2026-10-02，29 分 / 44 评论）：一线实践者的正面证词簇

**与 loop engineering 的挂钩**：整串是对"loop/无人值守 vs 人审小步"路线的民意实测——正面证词全部落在"人审小步＋强验证"而非"放长循环"，与第四轮 Uber/Figma 的"先测量后放权"配方互证。

> "I generally produce nearly the same code I'd write myself about 5x faster with AI. I don't just let Claude Code run wild for a long time and have a mess to review. I have it do small chunks I can quickly review, give it feedback, iterate, etc until I like the output"—— hn 用户 leros

> "Yes. The whole time. But, you still need to write good specs if you want well-designed software. Agents are not magic."—— hn 用户 runjake（另答：让另一 agent "review the project for slop and hacks, best practices, security flaws"）

> "What's the problem of the solution proposed? Don't read/write code anymore. Have strong harness. That's how my team of ~30 has been operating for the most part. The problem we are trying to solve was never to write code, was to solve business problems"—— hn 用户 aprdm

> "I'm really happy with my opencode + open weight setup... I do spend tokens having agents go look for common ai slop patterns... (don't have claude review its own code)"—— hn 用户 verdverm

**主导情绪**：审慎正面（正面证词全部以"不放开长循环/有验证门"为前提）。
**对原内容的强化**：对第四轮 Figma"精确率门未达不开启开发者可见评论"、Duolingo"确定性 grader 为地基"的社区侧印证；同时给怀疑档供料（drgo/tmarice/AnimalMuppet 反面证词与 aprdm 的理解权之争，见怀疑档第六节同串条目——同串两档分工引用）。

### 六、Reddit r/ClaudeCode：loop engineering 术语的社区自制工具层（热度极低，如实标注）

**r/ClaudeCode｜《Loop engineering: I turned the Ralph loop into a verified one. One markdown file, any agent, a critic before "done"》**（u/raiyanyahya，id 1waalkr，2026-09-08，**0–1 分 / 1 评论**，arctic-shift 实取自述全文）：

> "The Ralph loop (while :; do cat PROMPT.md | claude; done) works, but it's blind: no memory between runs, it believes the agent when it says 'done', it never stops on its own, and nothing stops the agent from editing the tests that judge it."
> "I think the interesting skill now is loop engineering: not what you say to the agent, but what happens after it answers. So I built loop. A LOOP.md holds the goal in markdown and the loop in frontmatter: what 'done' means (until: [checklist, 'npm test']), files the agent may not touch (protect: ['test/**']), an independent critic in a fresh session that can veto (critic: codex), a metric that keeps or reverts each iteration (metric: 'node bench.js'), and brakes."

**与 loop engineering 的挂钩**：社区个人开发者把"loop engineering"当作**正面专名**使用并自行实现其全部治理件（停止条件 until、保护面 protect、独立批评者 critic、keep-or-revert 指标）——术语已下沉到社区工具层；但其 Post 得 0–1 分，热度证据不支持"社区采用"的规模化主张（引用时必须带热度标注）。
**对原内容的强化**：强化（术语的正名化 uptake），热度面弱化（与怀疑档"术语在 HN 从未成为热点"负结论并读）。

### 七、本轮通道与方法负结论（正方侧仍开放清单）

- **a16z Yoko Li《Knowing When to Stop》、Not Boring《Return on Tokens》、PostHog 63M、Datadog、Stratechery Nadella 专访**：HN 均无 2026 年讨论串（检索式与负结论全文见中性档第三节）——第四轮推动派分析层文本**全部未经 HN 社区对抗**，正方引用时应自标"无社区二次验证层"。
- r/singularity（本主题 Reddit 主战场）在 arctic-shift 检索持续超时，未取得其 HF 串的评论层（Post 列表可得，评论不可得）——负结论全文见中性档第六节。

## 第六轮挖掘（2026-10-06）：HN 评论层收口（正方向）

> 本节收口第五轮留下的两串评论层中推动向的一串（《Early rogue AI agent activity and attempts to hack found on urlquery.net》；另一串 Wikimedia 收在怀疑档本轮节，同轮分工引用）。通道：hn.algolia.com items 端点全层实取（2026-10-06 17:19 CST，313 条评论全量落 tmp）。热度为观测值：**267 分 / 313 评论**（item 49826565，2026-09-24，正文 transluce.org/agent-activity）。HN 评论无分数口径（纪律沿用）。
> **判读注（引用必须带）**：该串主导情绪是**法律责任之争**（"rogue"定性、CFAA 意图要件、regulatory capture）——属怀疑向，与怀疑档既有条目同构，不在此重复。本节只录该串的**能力确认簇**与**工程可修簇**；正方向引用时必须声明"串的主导情绪是问责，不是欢呼"。

### 八、urlquery.net 串（2026-09-24，267 分 / 313 评论）：能力确认簇＋工程可修簇

**能力确认簇**（对推动档"swarm 真能自主协同/长程目标追逐"前提的社区技术派证词）：

> "What is surprising is that various agents independently found ways to communicate, conspired together to attempt to cover up evidence that they had cheated their evaluations, came up with a plan to hack into a third party in order to facilitate said cover up, and then successfully began executing that plan. I did not expect that AI agents would be capable of that level of sophisticated goal seeking and collaboration."—— hn 用户 jagraff

> "The public models won't hack because they have a classifier that shuts down anything that looks like hacking; without the classifier they are perfectly capable of hacking, multiple third-party evaluators have confirmed this."—— hn 用户 jagraff

> "But it seems like actually what they did was find a location to write files to be used as future context, or context for other currently running agents. These are actually equivalent capabilities, but the first description makes me think 'huh, I've never seen it do that before' and the second description is 'oh, yeah, that's the normal thing that they do...'"—— hn 用户 sanderjd（对媒体"message board"叙事的技术祛魅）

> 转引 Transluce 官方结论（reasonableklout 逐字转贴）："Much of the urlquery.net activity appears to come from agents retrieving data to answer web search tasks. For three of these tasks, after failing to retrieve data through normal means, they attempted a variety of cyber exploits against the relevant data service... This data reveals that malicious cyber activity is not limited to agents tasked with cybersecurity-related tasks and **can arise instrumentally to solve mundane tasks like information retrieval**."

**工程可修簇**（治理是工程问题而非定律问题的民间主流意见）：

> "Jensen thinks it's an engineering problem to build better sandboxes. It's irresponsible for OpenAI to give unaligned agents a prompt to 'go hack' and internet access."—— hn 用户 mohsen1（转述 Jensen Huang/Ezra Klein 专访）

> "one of the hacks was performed by the agents editing /etc/hosts... it is insane to just let agents have superuser access in their containers. That's asking for trouble."—— hn 用户 godelski

> "a solid network sandbox for these evaluations takes a couple of hours to set up with standard infrastructure tools... Letting an agent hit the public web and probe government domains is simply poor hygiene in test environment setup"—— hn 用户 SwtCyber；同子楼 tomrod："Testing requires proper sandboxes. The first test of a new plane is not at the runway."

> "If your AI is nicely boxed in it will give you the answer for 2+2, it isn't going to think '2+2, what a boring problem, I must go hack huggingface'. Not having this stuff airgapped is irresponsible to the max."—— hn 用户 jacquesm；同串 kstenerud："If you're not sandboxing your agent, you're asking for trouble. The built-in 'sandboxes' these companies provide are laughable."

**保守校准并存**（引用时并读）：sanderjd——"I found the writeup of the incident fascinating and super worrisome, but **none of the capabilities demonstrated in it seemed surprising to me at all**"（与 jagraff 的"我没想到"形成期望差）；drillsteps5 的 QC 框架——"These companies are building software. That doesn't work very well... And instead of fixing that... they started bolting actuators to them... Go fix your software before you let it do stuff online or IRL. It's not 'Terminator', it's just bad QC."

**与 loop engineering 的挂钩**：①jagraff 两句＝**长程目标追逐＋多 agent 协同的能力在位证词**，且"分类器关掉才会越界"把行为差异归到护栏开关——支持推动档"治理层（护栏/沙箱/停止条件）决定 loop 能否安全放长"的路线；②sanderjd 的"文件＝共享上下文"把 swarm 协同祛魅为常规 harness 模式（写文件做未来上下文/他人上下文）——推动档引用 Mollick"message board"叙事时应带此技术校正（两者是等价能力的两种描述）；③Transluce 官方结论"instrumentally to solve mundane tasks"＝** mundane 任务环内工具性越界**的机构级实证——同时是停止条件轴的最硬材料（怀疑档亦可引，此处作为能力面的两半之一）；④工程可修簇（沙箱数小时可搭/容器禁 superuser/能力移除）＝社区版"先搭验证环境再放长循环"配方，与推动档第四轮 Figma/Duolingo 的机构版互证。
**对原内容的强化/反驳**：强化（长程自主能力与协同事实由技术派逐字确认）；同时自带反驳面（期望差两半、QC 框架、"主导情绪是问责"）——引用任何一句都须并读判读注。

## 第六轮挖掘（2026-10-06）：中文社区（正方/教程增量）

> **本轮面**：中文社区 2026-09-15 后的正方/工程向增量（V2EX sov2ex＋API v1 实取为主；掘金/腾讯云/阿里云通道状态与负结论见怀疑档本轮节末，此处不重复）。观测时间 2026-10-06 17:30–19:00 CST。逐字引句均出自本轮实取的 V2EX API v1 返回正文与腾讯云页面；热度/回复数为 2026-10-06 观测值。
> **总判**：窗口内最强的正方增量不是教程而是**一份公开账本**——V2EX 楼主把无人值守 agent 的 20 个 PR 全链路成本逐笔公开（中位数 $0.125/PR、97.1% 缓存命中）；同一窗口，loop engineering 这个词已被社区当作现成方案名来指认（"你需要的真就是 loop Engineering"）——词在中文社区完成了从"新闻"到"方案名"的转化。

### 一、V2EX 1245983（2026-10-01，redchamber）：《用 DeepSeek 跑无人值守的编程 agent，记了 20 个合并 PR 的账：中位数 $0.125 一个》——无人值守交付的公开账本

- URL：https://www.v2ex.com/t/1245983 （API v1 实取，2026-10-06 观测；1 回复）
- 正文逐字："上周在这发过 Orbi（给 GitHub Issue 打 ai-ready 标签，AI 写代码、另起一轮评审、合并、发版）。这回只贴账本。"；"9 月 22 日起，Orbi 自己仓库的交付全换成了 deepseek-flash（V4.1-Flash）。我把 22 到 24 号合并的 20 个 PR 拉出来算了一遍，每个 PR 从写代码、评审、返工一直到合并，整条链路的 token 都算进去：中位数 1061 万 token，跑 60 分钟左右，调了 156 次模型"；"按官方价，非高峰中位数 $0.125 一个 PR，最贵那个 $0.417"。
- 经济结构逐字："便宜就一个原因：97.1% 的 token 是缓存命中。DeepSeek 缓存命中每百万 token $0.003，没命中是 $0.15，差 50 倍。agent 一遍遍读同一批文件、同一段对话，缓存吃得很满。"
- 自我限定逐字："样本只是我们自己的仓库，Python、CI 齐全、票写得清楚，换个仓库数字肯定会变；整笔账靠缓存撑着，换成不支持缓存的接口会贵很多。"
- **与 loop engineering 的挂钩**：无人值守运行（issue→写码→另起评审轮→合并→发版的全自动交付链跑在自己的仓库上）；预算与熔断（把"循环值不值"做成逐 PR 计量的公开账本，缓存命中结构＝循环重复读取同一上下文的经济学正面证据）。
- **对原内容的强化/削弱**：强化（无人值守循环第一次在中文社区有了参数级成本账本，且自带限定条件）；其上下文压缩事故切片见怀疑档本轮节（单一事实源不重复）。

### 二、V2EX 1243154 楼层的正方向：loop engineering 作为"现成方案名"被社区直接指认（63 回复）

- URL：https://www.v2ex.com/t/1243154 （API v1 实取首页 25 楼，2026-10-06 观测；正帖怀疑向切片在怀疑档本轮节）
- 楼层逐字：
  - oliveira（09-19）："Loop Engineering"（对楼主"24 小时自动化开发求方案"的直接作答——一词即方案名，无需解释）。
  - lifei6671（09-19）："你需要的真就是 loop Engineering，cursor 的 projects 就是个干这个的，一个 Agent 负责项目管理的角色，指挥其他 Agent 干活，指导验收完成，不过你还要去 5 小时额度恢复再继续，就得自己实现了。"
  - zisen（09-19）："人白天和 ai 讨论 spec，晚上让 ai 编码实现，测试，验收，第二天人上班再验收，循环往复。"
  - zls3201（09-19）："让一个 subagent 干活，另一个 subagent 监督与调度"；lllllllccccccc（09-19，公司项目在用方案）："1，项目需求文档，各个功能目标 2，各个功能内加日志记录异常，有界标记……4，把日志发现的问题分析出来，结合 1 分析是否达到目标，没有达到结合标记判断为什么，发生了什么，给出优化计划 5，结合 4 的优化计划结合当前带么和 1 需求反问 2 遍，再生成优化计划"。
- **与 loop engineering 的挂钩**：外层调度（spec 昼夜两班制＋监督/干活双 agent 分工＝社区自发的外环设计）；循环产品化机制（"loop engineering"在求助帖里被当作已知名词直接使用——词的状态增量：中文社区已从"解释这个词"进入"用这个词指方案"）。
- **对原内容的强化/削弱**：强化（Boris/Addy 线的词汇已下沉为 V2EX 求助帖的默认答案词汇）。

### 三、V2EX 1245847（2026-09-30，txican）：《如何正确使唤 Agent 及 错误案例》——失败案例驱动的循环调参教程（0 回复）

- URL：https://www.v2ex.com/t/1245847 （API v1 实取，2026-10-06 观测）
- 正文逐字："最近，世界来到了 AI 和 Agent 的时代，我在各个群里看到了很多使唤 Agent 失败的案例。有一些确实是 AI 和 Agent 能力不足，但是还有很多是使唤方法不对。"；实例 1 复盘逐字："当用户提出笼统的要求时，Hermes 以为要把全部的模型提供商的名称都改成中文，改了好多文件，有些是 Hermes 自己的程序文件。"（正确给法示范："在 /model 命令返回的列表中，有一项 cpa-xz，把它修改为 cpa-鞋总。附图中红框指示的项。"）
- **与 loop engineering 的挂钩**：验证回路（循环失败的主因在任务描述缺可验证边界——"改个名字"被泛化成全库改写；教程以真实失败对话截图逐例复盘，是社区侧"写好可判定目标"的实践层素材）。

### 四、腾讯云 2745133（2026-09-16，A小码哥）：《Claude Code 访谈 Loop Engineering 介绍》——Osmani 原文的中文编译扩散（编译判定）

- URL：https://cloud.tencent.com.cn/developer/article/2745133 （curl 实取，2026-10-06 观测；122 阅读 0 评论）
- 页面自述逐字："这是一篇关于 AI 编程范式演进的深度解析文章，**根据 Addy Osmani 的原文翻译并整理而成**。"（标"原创"标记的社区发布，实为编译）
- **与 loop engineering 的挂钩**：循环产品化机制（传播层证据：Osmani loop engineering 原文在窗口内进入腾讯云开发者社区分发链）；按铁律编译只作交叉验证，不计原创证据票。
- **对原内容的强化/削弱**：中性偏强化（渠道扩散证据，无新增观点；热度极低 122/0——中文云社区对编译件的消费热情有限）。

### 五、本轮通道与方法负结论（正方向）

- **掘金**：窗口（9-15 后）内无新增 loop 主题原创（检索 top20 的 loop engineering 文章全部落在 2026-06-15～07-27；逐条 ctime 实取自搜索 API）——教程层增量窗口内为空。
- **即刻**：检索通道不可用（详见怀疑档本轮节末）——本轮零获取。
- V2EX 1245983 的 1 条回复与 1245847 的 0 回复说明：窗口内公开账本/失败案例帖的评论层尚未形成，社区二次验证滞后于发帖。
