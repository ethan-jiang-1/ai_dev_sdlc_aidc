# KOL 言论对齐调查（2026 以来）——本场核心声称 vs 行业公开言论

> **调查日期**：2026-09-25（web 检索；口径遵守"会漂移的值标观测日期"）。
> **用途**：检验 storyline v0.2 的核心声称（三条立场＋关键机制）在 2026 年行业 KOL／研究言论里有没有回声、
> 反声或 nuance。**这不是上屏文案来源**——上屏的 DSH 事实仍以钉版 `46a7f68b09` 为准（见 [00-sources.md](./00-sources.md)）；
> 本文件是"我们讲的东西行业也在说／行业正缺"的外部佐证账本。
> **强度口径**：KOL 博客＝趋势级；arXiv 论文＝研究级（未逐篇核验方法学，引用时注明）；marmelab 审计＝趋势级·带计量（独立咨询方，246 仓库＋57 文献，非同行评审）。

## 一、总判定

**三条立场全部有 2026 年的行业回声；其中立场②（规则可执行）的反差最强**——行业言论恰好证明了
"人人都在写规则、几乎没人在执行规则"，DSH 的做法（门禁）正是全场要讲的那道 uncommon sense。
另有两个 nuance（见第四节）不构成反驳，反而被语料的"分寸"部分预先覆盖。

## 二、逐条对齐

### 立场① · agent 是一等参与者 —— **align（强）**

| 行业言论 | 出处 | 强度 |
|---|---|---|
| OpenAI 正式命名这门学科 "harness engineering"，作者 Ryan Lopopolo 自述 **~100 万行代码、0 行手写、约 1500 个合并 PR**——"agent-first world" | [openai.com/index/harness-engineering](https://openai.com/index/harness-engineering)，2026-02-11 | 一手（厂商自述） |
| 2026-01 以来 **25% 触碰 harness 的提交由 AI 签名**；79 个仓库里 52 个"harness 比 it 治理的代码更 AI 化" | [marmelab 审计](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html)，2026-09-24 | 趋势级·带计量 |
| "treat agents as **first-class users**, not just human users with better memory" | [Stripe 工程博客](https://stripe.dev/blog/ai-steering-experiments)，2026-05-14 | 趋势级 |

### 立场② · 规则是可执行的代码 —— **align（最强，反差型）**

行业数据恰好证明**缺口就是 DSH 的答案**：

| 行业言论 | 出处 | 强度 |
|---|---|---|
| **"Everybody writes instructions, almost nobody enforces them"**：145 个大型开源项目 63% 有 agent 指令文件，但 391 个仓库里只有 **12 个**提交过一条 deny 规则、22 个有 PreToolUse 钩子 | [marmelab 审计](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html) | 趋势级·带计量 |
| **"You can't whisper at an AI agent"**：被动提示（警告、SDK 注释、依赖目录里的 AGENTS.md）全部失效；**hard steering（报错／阻断）可靠生效**——"errors block progress but warnings don't" | [Stripe 工程博客](https://stripe.dev/blog/ai-steering-experiments)，2026-05-14 | 趋势级 |
| 481 个公开 CLAUDE.md 里，安全规则**只有 4.4% 背后有真实控件**（"When 'do not' is not deny"） | [arXiv 2608.23550](https://arxiv.org/abs/2608.23550)，2026-08 | 研究级 |
| Ralph Wiggum loop／"back pressure engineering"：把 agent 循环到**不会说谎的裁判**（测试／linter／类型检查）通过为止 | Geoffrey Huntley，见 [marmelab 收录](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html) | 趋势级 |
| 负例控制的对偶："Test both the cases where a behavior should occur and where it shouldn't. **One-sided evals create one-sided optimization.**"（与 DSH 的 "A guard only guards if the regression fails it" 同构） | Anthropic，[marmelab 转引](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html) | 趋势级 |

### 立场③ · 每类事实有唯一的 owner —— **align（强）**

| 行业言论 | 出处 | 强度 |
|---|---|---|
| **"AGENTS.md is winning"**：189 个仓库根有 AGENTS.md vs 155 个 CLAUDE.md；大型项目里 53 个 CLAUDE.md 有 **36 个是 symlink／短重定向**到 AGENTS.md——与语料证据 #6（`ln -s AGENTS.md CLAUDE.md`，零复制）同型 | [marmelab 审计](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html) | 趋势级·带计量 |
| Anthropic 采纳 OpenAI 的 AGENTS.md 标准，入口文件走向统一 | [36kr 报道](https://eu.36kr.com/en/p/3989811919076098) | 趋势级（媒体） |
| Stripe 的 skill 按**归属**拆分：payments 团队维护 payments skill——"一个事实一个 owner"的组织版 | [Stripe 工程博客](https://stripe.dev/blog/ai-steering-experiments) | 趋势级 |

### 核心命题 Agent = Model + Harness —— **align（已是行业唯一共识）**

| 行业言论 | 出处 | 强度 |
|---|---|---|
| "Agent = Model + Harness" 这条公式出自 Birgitta Böckeler，被 marmelab 称为**全领域唯一共识**（"the only consensus is about what Harness Engineering is"） | [martinfowler.com](https://martinfowler.com/articles/harness-engineering.html)，2026-04-02 | 趋势级 |
| 同一模型过 **8 个 harness、同一 25 个任务：成功率 68% → 88%**——"模型决定上限，那一圈决定你能拿到多少"的量化版 | [Composio](https://composio.dev/content/best-ai-agent-harnesses)，见 marmelab 转引 | ⚠️ 厂商自述·带计量 |

### "那一圈会移动"（harness 假设会腐）—— **align（厂商一手）**

| 行业言论 | 出处 | 强度 |
|---|---|---|
| Anthropic 自述：为治 "context anxiety" 加的 context resets，**模型升级后成了 dead weight**——"a harness encodes assumptions about what the model can't do … those assumptions rot as the model improves" | [Anthropic](https://claude.com/blog/harnessing-claudes-intelligence)，见 [marmelab 转引](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html) | 一手（厂商自述） |
| marmelab 头号建议就是 "Reduce the harness to the strict minimum"——**harness 应当是对 agent 失败的反应，不是对能力缺点的预设**（与语料"有压力再借／不要照搬"同构） | [marmelab](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html) | 趋势级 |

### 渐进披露／注入预算 —— **align（带实测）**

| 行业言论 | 出处 | 强度 |
|---|---|---|
| Stripe 实测：skill 文件**模块化（渐进披露）比单体文件好约 10%**，且省 token——目录给摘要、按需加载正文 | [Stripe 工程博客](https://stripe.dev/blog/ai-steering-experiments) | 趋势级·带实测 |
| "agent-facing developer experience is a **distribution problem, not a content problem**"——内容再好，不在加载路径上就等于不存在 | [Stripe 工程博客](https://stripe.dev/blog/ai-steering-experiments) | 趋势级 |
| Claude Code 逆向分析：五段 compaction——与披露管线层 4 同型 | [arXiv 2604.14228](https://arxiv.org/abs/2604.14228) | 研究级 |

### 静与动（model-visible ⟺ logged／可回放）—— **align（研究方向印证）**

| 行业言论 | 出处 | 强度 |
|---|---|---|
| NovaFabric：为 agent 运行造**防篡改、可回放的证据**——"model-visible ⟺ logged"的学术回声 | [arXiv 2609.12582](https://arxiv.org/abs/2609.12582)（编号为检索所得，未核全文） | 研究级·未核 |

## 三、对 story​line 的直接可用结论

1. **段一开场可以加一句时代注脚**（不上屏 DSH 之外的产品名，口播即可）：这门学科 2026-02 才被 OpenAI 命名，
   全领域唯一共识就是我们那条公式——**本场解剖的是把共识做到极致的一个样本**。
2. **立场②的讲法有了外部杠杆**：先给行业缺口（"63% 在写规则、12/391 在执行"），再给 DSH 的答案（门禁）——
   反差感比单讲 DSH 更强。Stripe 的 hard/soft steering 是最合适的口播参照（不点名也行："有家支付公司做过十几个实验……"）。
3. **Composio 的 68%→88%** 可作 101 canon"模型决定上限／那一圈决定拿到多少"的量化旁证——**标注 ⚠️ 厂商自述＋观测日期**才可上屏（本场红线：外部数字默认不上屏，要用先过这条）。
4. Anthropic 的 "assumptions rot" 引句可进"精选 5–8 句英文"的候选池（非 DSH 原话，标注出处 Anthropic）。

## 四、nuance（不反驳，但要记着）

| nuance | 内容 | 与本场的关系 |
|---|---|---|
| **外置不是免费** | ETH Zurich（[arXiv 2602.11988](https://arxiv.org/abs/2602.11988)，2026-02）：138 个真实任务上，**机器生成的上下文文件比什么都不给还降成功率**（+20% 推理成本）；人写的约 +4%；无论哪种都多烧 14–22% reasoning token | 不反驳立场①③，反而**坐实"写给 agent 读是另一种纪律"**——外置的质量与克制（字数预算、one home）正是 DSH 与随手生成 context 文件的分界；段六"分寸"可引 |
| **harness 定义会过期** | marmelab：任何"好 harness"的定义都会随模型升级过期（中位仓库才 8.7 个月大） | 与"那一圈会移动"同向；提醒本场不把 DSH 形状讲成永恒真理——语料 10 的"不要照搬"已覆盖 |
| **57% 根指令文件超百行** | 行业中位 123 行，OpenAI 自己定的是 ~100 行 | DSH 的字数预算是门禁（≤1,950 词、verify-doc-budgets 卡）——又一个"行业口头同意、DSH 机器执行"的样本 |

## 五、本次检索的主要来源清单

- [The State of AI Harness Engineering 2026 — marmelab（François Zaninotto）](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html)，2026-09-24
- [You can't whisper at an AI agent — Stripe（Beswick & Epsteen）](https://stripe.dev/blog/ai-steering-experiments)，2026-05-14
- [Harness engineering for coding agent users — Birgitta Böckeler / martinfowler.com](https://martinfowler.com/articles/harness-engineering.html)，2026-04-02
- [Harness engineering — OpenAI（Ryan Lopopolo）](https://openai.com/index/harness-engineering/)，2026-02-11
- [Evaluating AGENTS.md — ETH Zurich](https://arxiv.org/abs/2602.11988)；[When "do not" is not deny](https://arxiv.org/abs/2608.23550)；[Claude Code 设计空间逆向](https://arxiv.org/abs/2604.14228)；[NovaFabric](https://arxiv.org/abs/2609.12582)
- [Anthropic 采纳 AGENTS.md 标准 — 36kr](https://eu.36kr.com/en/p/3989811919076098)；[Anthropic：harness 假设会腐](https://claude.com/blog/harnessing-claudes-intelligence)（经 marmelab 转引）

## 六、KOL 点名背书（第二批，2026-09-25 补充轮）

> 用户反馈"背书不够多"后补的**点名个人**。按人归档：引句（或转述）→ 背书的是哪条声称 → 强度。

### Andrej Karpathy —— 背书：立场①＋全场主轴（赛道最大嗓门）

- **言论**（2026-02-04，推文＋视频，经新智元/36kr 转述）：亲自终结自己一年前发明的 "Vibe Coding"，提出
  **"Agentic Engineering（智能体工程）"**——"**99% 的时间不再直接写代码，而是在指挥智能体干活、充当监工**"；
  "利用 LLM Agent 编程已成为专业人士的**默认设置**，只不过监督和审查要更多了"；预测 2026 年
  "模型层 × 智能体层"**双线进化、乘积效应**。
- **背书哪条**：立场①（开发主力就是 agent，人变成驾驭者/监工）——和 DSH 的"开发主力自称 coding agent"
  是同一个时代的两种表述；"工程"二字也正是本场标题《解剖一只优秀的 harness》的立意。
- **出处**：[36kr/新智元报道](https://www.36kr.com/p/3670333435798402)，2026-02-05；一手推文
  [x.com/karpathy/status/2019137879310836075](https://x.com/karpathy/status/2019137879310836075)（**上屏用须先回源核原句英文**——见待回源）。
- **强度**：趋势级（媒体转述一手推文；转述质量可信，上屏前须核原文）。

### Harrison Chase（LangChain CEO）—— 背书：学科命名＋关键反转＋静与动＋隔离边界

- **言论**（2026-03，VentureBeat 播客，经 digitaltoday 转述）：**"Harness engineering is an extension of
  context engineering"**；harness＝让模型循环、调工具、跑长任务的执行环境；AutoGPT 当年消失是因为模型撑不起
  loop；**"跨 200 步的任务要保持一致，需要边走边记录思考的结构"**；LangChain Deep Agents 的 subagent
  **上下文与主 agent 分离**、大任务结果压缩成单一输出。
- **背书哪条**：一次背四条——① harness 是学科（命名级）；② VentureBeat 报道标题即"**better models alone
  won't get your AI agent to production**"（关键反转：光靠更好的模型到不了生产）；③ "边走边记录"＝静与动
  （model-visible ⟺ logged）；④ subagent 上下文隔离＝披露管线层 5。
- **出处**：[digitaltoday 转述](https://www.digitaltoday.co.kr/en/view/28196/langchain-ceo-ai-agent-success-depends-on-context-engineering)，2026-03-07（VentureBeat 播客的韩媒转述；原播客见 VentureBeat）。
- **强度**：趋势级（媒体转述播客）。

### Addy Osmani —— 背书：干活的和验收的不能是同一个

- **言论**：agent harness engineering——**把"生成"与"评估"拆给不同的 agent，胜过让 agent 自我评估**。
- **背书哪条**："干活的和验收的不能是同一个人"（101 canon／本场立场③的验收配套）的 agent 版。
- **出处**：[addyosmani.com/blog/agent-harness-engineering](https://addyosmani.com/blog/agent-harness-engineering/)（经 [marmelab 语料](https://marmelab.com/blog/2026/09/24/the-state-of-ai-harness-engineering-2026.html)收录转述）。
- **强度**：趋势级（KOL 博客，经二手转述——引用前核原文）。

### 中文／国际圈的术语成型 —— 佐证：这条赛道不是我们自说自话

- **Loop Engineering 橙皮书**（中文社区，alchaincyf 编，2026-06）："循环工程"在中文圈已写成体系化的开源书
  （[橙皮书 PDF](https://github.com/alchaincyf/loop-engineering-orange-book)）——与 Ralph Wiggum loop 同一谱系。
- **随机比特／腾讯云社区**（2026）："最近疯传的 Loop Engineering，是台印钞机，还是绞肉机？"——
  讨论热度本身是佐证（[腾讯云社区](https://cloud.tencent.com.cn/developer/article/2696951)）。
- **ITWorld Korea**：标题即判断——"Shopify 证明的：比 agent 更重要的是**工作场的设计**"
  （[itworld.co.kr](https://www.itworld.co.kr/article/4192545/)）——"工作场设计"≈harness 的媒体说法。
- **强度**：趋势级（社区/媒体）。

### 已在第一批、此处归入"个人"的

- **Birgitta Böckeler**（Thoughtworks）："Agent = Model + Harness" 公式出处（[martinfowler.com](https://martinfowler.com/articles/harness-engineering.html)，2026-04）。
- **Ryan Lopopolo**（OpenAI）：命名学科；~100 万行、0 行手写（[openai.com](https://openai.com/index/harness-engineering/)，2026-02）。
- **Geoffrey Huntley**：Ralph Wiggum loop／"不会说谎的裁判"（back pressure engineering）。
- **James Beswick & Peter Epsteen**（Stripe devrel）：[You can't whisper at an AI agent](https://stripe.dev/blog/ai-steering-experiments)，2026-05。

## 七、第二批小结与待回源

- **点名个人已达七位**：Karpathy／Harrison Chase／Böckeler／Osmani／Huntley／Lopopolo／Stripe 团队，
  外加中文圈 Loop Engineering 社区——**立场①②③各有 2–4 位独立背书**，学科命名（OpenAI）与唯一共识公式
  （Böckeler）都是 2026 年上半年的事，本场选题正当其时。
- **对 storyline 的增量**：段一时代注脚可以直接用 Karpathy 的"Vibe Coding 终结 → Agentic Engineering"
  （与 OpenAI 命名 harness engineering 并列，说明"驾驭"已是行业主词）；段二立场②讲行业缺口时，
  VentureBeat 那句"better models alone won't get your agent to production"是关键反转的最媒体化表述（口播用）。
- **待回源（上屏前必须做）**：① Karpathy 推文的英文原句（现只有中文媒体转述）；② Osmani 博客原句；
  ③ Harrison Chase 播客原句。**转述级引用只可口播，不上屏。**
