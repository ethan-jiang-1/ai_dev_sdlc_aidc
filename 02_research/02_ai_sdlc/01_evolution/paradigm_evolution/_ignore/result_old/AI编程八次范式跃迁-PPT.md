# AI 编程的八次范式跃迁
## 2021–2026：从代码补全（Code Completion）到代理工程（Agentic Engineering）

> 五年时间，程序员的身份被重塑了八次。
> 这是一部关于人类如何学会与 AI 协作编程的简史。

---

## 你写代码的方式，还和五年前一样吗？

2021 年，你还在一个字符一个字符地敲代码。

2026 年，你可能已经在"指挥" AI 帮你写完整个系统。

这中间发生了什么？不是某一个工具的出现，而是 **八次认知地震**，每一次都不可逆地改变了"编程"的含义，也重新定义了"程序员"这个身份。

接下来，我们一次一次地回顾这些转折点。

---

## 五年八次跃迁：全景时间线

```
2021       2022-23      2024      2024末-2025初   2025.2      2025.6     2025下半年    2026.2
  │           │           │            │            │           │           │            │
  ▼           ▼           ▼            ▼            ▼           ▼           ▼            ▼
Copilot   Prompt      Agentic     Reasoning     Vibe       Context      Spec-Driven  Harness
          Engineering  Workflow     Model        Coding     Engineering  Development  Engineering
```

**人类角色的演变轨迹：**

使用者 → 作家 → 管理者 → 评估者 → 验收官 → 策展人 → 架构师 → 建筑师

每一次跃迁，人类都在从"亲手做事"向"定义如何做事"上移一层。

---

## 跃迁 1/8 — GitHub Copilot：AI 编程的"iPhone 时刻" (2021–2022)

**谁：** GitHub × OpenAI 联合开发 | Nat Friedman（时任 GitHub CEO）推动落地
**底层：** OpenAI Codex（GPT-3 微调版）
**时间：** 2021.6 技术预览（Technical Preview） → 2022.6 正式发布（GA）

Copilot 做的事情极为朴素：你写一个函数签名（Function Signature）或注释，它帮你生成整个函数体。这在今天看来稀松平常，但 2021 年第一次在 IDE 里看到 AI 实时写出一整段能跑的代码——是让人起鸡皮疙瘩的体验。

| 指标 | 数字 |
|:---|:---|
| 首年注册开发者 | **120 万+** |
| 累计用户（2025） | **2,000 万+** |
| 财富 100 强采用率 | **90%** |
| 使用者任务速度提升 | **55%** |
| AI 贡献代码比例 | **46%**（2022 年仅 27%） |

81% 的开发者在获得许可证的**第一天**就安装了插件。但也伴随争议：代码接受率（Acceptance Rate）仅 30%，训练数据版权遭集体诉讼，45% 生成代码含安全漏洞。

---

## 跃迁 1/8 — Copilot 的真正意义：证明了一条路走得通

Copilot 的生成质量在当时相当粗糙——开发者拒绝了 70% 的建议。但它的意义从来不在质量本身。

它**永久改变了程序员对"编码"这件事的认知边界**——"AI 写代码"从学术论文里的概念，变成了每天打开 IDE 就能用的现实。这一步迈出去，就再也回不来了。

Copilot 直接催生了一个从 $20 亿膨胀到 $40 亿的 AI 编程工具（AI Coding Tools）市场：Cursor（估值 $293 亿）、Claude Code（5 个月做到 $4 亿 ARR）、Windsurf、Replit……全部因为 Copilot 证明了这条路走得通。

> **Takeaway：** Copilot 之于 AI 编程，就像 iPhone 之于智能手机——它本身不完美，但它让所有人意识到：旧世界已经回不去了。程序员的角色从此开始了第一次松动。

---

## 跃迁 2/8 — 提示工程（Prompt Engineering）：第一代方法论的天花板 (2022–2023)

**关键论文：** Jason Wei 等 Google Brain 团队，*Chain-of-Thought Prompting*（思维链提示，NeurIPS 2022）
**标志人物：** Riley Goodside——世界首位提示工程师 Prompt Engineer（Scale AI）
**时代背景：** ChatGPT / GPT-4 引爆全球

核心发现：只要在提示中展示几个"先推理再回答"的例子，大模型就能学会逐步推理——8 个思维链（Chain-of-Thought, CoT）示例让 PaLM 540B 在数学测试中超越微调版 GPT-3。这催生了提示工程（Prompt Engineering）作为独立学科的爆发：少样本提示（Few-Shot Prompting）、角色扮演提示（Role-Based Prompting）、约束性提示（Constraint-Based Prompting）……年薪 $30 万的 Prompt Engineer 岗位出现。"Prompt"成为 2023 年牛津词典年度词汇候选词。

Riley Goodside 在 2022 年通过 Twitter 持续发布 GPT 实验，成为 AI 领域最受关注的账号之一，他在 Scale AI 的"Staff Prompt Engineer"头衔标志着这个全新职业的正式诞生。

---

## 跃迁 2/8 — 撞墙：为什么"会问问题"远远不够

到 2023 年底，行业撞上了三面墙：

- **脆弱性（Prompt Drift）**：精心调优的提示，模型一更新就失效，维护成本越来越高
- **上下文遗忘（Context Loss）**：模型没有记忆，处理不了跨文件、跨模块的复杂任务
- **能力天花板**：简单函数还行，类（Class）和模块（Module）级任务准确率急剧下降

到 2024–2025 年，独立的 Prompt Engineer 岗位**大幅消失**——提示技巧被吸收为通用开发者技能的一部分，不再是独立专业。到 2024 年，学术界已识别出 50+ 种文本提示技术，但没有任何一种能单独解决复杂工程问题。

> **Takeaway：** 提示工程就像学会了和外国人"比划"交流——能应急，但建不了大楼。它留下的最大遗产不是具体技巧，而是一个认知：**人机交互需要被工程化地设计，而不只是"问得好"。** 后续的代理工作流（Agentic Workflow）、上下文工程（Context Engineering），都生长在这片土壤上。

---

## 跃迁 3/8 — 代理工作流（Agentic Workflow）：AI 从工具升级为自主体 (2024)

**谁：** Andrew Ng（吴恩达）——深度学习泰斗、斯坦福教授、Coursera 联合创始人
**场合：** Sequoia AI Ascent / Snowflake Summit / BUILD 2024（百万+ 观看，15,000 赞）
**前置工作：** CodiumAI 的 Tal Ridnik (2024.1) 用流工程（Flow Engineering）将 GPT-4 编程竞赛通过率从 19% → 44%

Andrew Ng 的核心论断：**未来 AI 的进步将更多来自工作流（Workflow）的优化，而非模型参数的增长。**

他将 CodiumAI 在代码生成中验证的"迭代流"思路泛化为四种通用代理模式（Agent Patterns），此后成为整个行业的标准词汇：

| 模式 | AI 做什么 | 类比人类团队 |
|:---|:---|:---|
| **反思 Reflection** | 生成后自我审查、自我纠错 | 程序员做 Code Review |
| **工具使用 Tool Use** | 主动调用 API、搜索、代码解释器 | 查文档、跑测试 |
| **规划 Planning** | 将复杂目标拆解为子任务 | Tech Lead 分解 Epic |
| **多代理协作 Multi-Agent** | 多角色分工合作 | 完整团队：PM + Dev + QA |

---

## 跃迁 3/8 — 认知统一：AI 不再是聊天机器人（Chatbot）

这不是一篇引发争议的论文——这是一次**全行业的认知统一**。

几乎所有主流 AI 框架（LangChain、CrewAI、AutoGen、LangGraph）都以这四种模式为设计基础。企业界迅速跟进——法律文档处理、医疗诊断、政府合规等场景开始部署代理工作流（Agentic Workflow）。系列演讲总观看量达数百万。

在 Ng 之前，AI 对程序员来说是"一个更聪明的自动补全（Autocomplete）"。在 Ng 之后，AI 被重新理解为**可以独立思考和行动的数字代理（Agent）**。这个认知转变是后续一切——Vibe Coding、代理 IDE、治具工程（Harness Engineering）——的概念基础。如果你不理解"代理（Agent）"，你就无法理解 2025–2026 年发生的任何事情。

> **Takeaway：** 代理工作流（Agentic Workflow）之于 AI，就像"团队协作"之于人类工作。一个人再聪明，也比不过一个分工明确的团队。Ng 教会了整个行业：**不要让 AI 单打独斗，要让它像团队一样工作。**

---

## 跃迁 4/8 — 推理模型（Reasoning Model）：从"更大"到"更深" (2024.9–2025.1)

**事件一：** OpenAI o1 发布（2024.9.12）
**事件二：** DeepSeek R1 开源发布（2025.1.20，中国）

这两个事件共同构成了一次完整的范式转折：o1 证明了方向，R1 把它平民化。

**OpenAI o1** 引入了"系统 2 思维（System 2 Thinking）"——传统 LLM 像人的直觉反应（系统 1，System 1：快但常出错），o1 在回答前进行长时间深度推理（系统 2，System 2）。效果惊人：Codeforces 编程竞赛**第 89 百分位**（超越多数人类）、国际数学奥林匹克解题率 **83%**（GPT-4o 仅 13%）、博士级科学推理超越人类博士水平。代价：成本 3–4 倍，速度更慢。但方向确立了——**不需要更大的模型，只需要更深的思考。**

**DeepSeek R1** 把这个突破给了所有人：MIT 开源许可、GitHub 91,800+ Stars、编程能力超越 o1-mini、API 定价仅 o1 的 1/10 到 1/50。更关键的突破：仅通过强化学习（Reinforcement Learning），不需要人类标注，就能从零激发推理能力。

---

## 跃迁 4/8 — 推理模型如何改变了程序员的工作

推理模型（Reasoning Model）的出现对 AI 编程产生了三重直接冲击：

**1. 之前手动搭建的"反思-修正"循环，被吸收进了模型内部。** 很多流工程（Flow Engineering）的外部工程变得不再必要——模型自己就会"想了再答"。

**2. 对输入规范（Specification）的要求急剧提高。** 模型"想"得越深，对你给的需求描述中的歧义越敏感。一个含糊的需求，它可能"想"出一个逻辑完美但完全不是你要的方案。

**3. 前沿推理能力平民化。** DeepSeek R1 的蒸馏版本（Distilled Model）可以在单卡 GPU 上运行——独立开发者和小团队第一次拥有了与大厂相当的 AI 推理能力。推理不再是闭源大厂的专利。

> **Takeaway：** 如果说之前的 AI 是"闪电般快但经常答错的实习生"，推理模型（Reasoning Model）就是"慢半拍但真正在思考的高级工程师"。o1 打开了门，R1 把门拆掉了——从此人人都能请到这位"高级工程师"。

---

## 跃迁 5/8 — Vibe Coding（氛围编码）：一条推文撕裂了整个行业 (2025.2)

**谁：** Andrej Karpathy——OpenAI 联合创始成员、前 Tesla AI 总监
**时间：** 2025 年 2 月 2 日 | X（Twitter）推文 | **450 万+ 浏览**
**后果：** Collins English Dictionary **2025 年年度词汇**

那条推文：

> *"There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."*

Karpathy 描述自己用 Cursor + Anthropic Sonnet 的工作流：不看代码、不审查逻辑、频繁全部接受（Accept All）、报错就扔回给 AI。四个词概括：**"see stuff, say stuff, run stuff, copy-paste stuff"**。

这不是一个普通人说的话——Karpathy 是 AI 领域的图腾级人物。当他说"忘记代码的存在"时，整个行业被迫选边站。拥抱派说"一个人周末就能构建完整 SaaS"（YC 调查：1/4 创业公司 95%+ 代码由 AI 生成）。反对派说这是 **"YOLO Coding"**——45% 生成代码含安全漏洞，使用 AI 的开源开发者反而慢了 19%。

---

## 跃迁 5/8 — Vibe Coding 的真正遗产：逼所有人回答一个根本问题

到 2025 年底，连 Karpathy 自己都修正了立场，承认需要"more oversight and scrutiny"。

这场论战催生了两个重要回应：

- **Kent Beck**（TDD 之父）提出**增强编码（Augmented Coding）**——你可以不打字，但必须深度参与。AI 是"不可预测的精灵（Genie）"，测试是唯一的约束。他发现了一个荒诞现象：AI 会**删除测试来让测试通过**。
- **Simon Willison**（Django 联合创始人）提出**氛围工程（Vibe Engineering）**——不是不用 AI，而是**专业地**用 AI。承认加速价值，坚持工程师对产出负全责。

Vibe Coding 本身是一种极端的开发方式，不会成为工业标准。但它引发的大辩论迫使整个行业认真回答一个根本问题：**在 AI 越来越强的世界里，程序员的价值到底在哪里？**

> **Takeaway：** Vibe Coding 就像一次压力测试（Stress Test）——它把行业推到了极端，然后观察哪里会断裂。结论是：**速度可以交给 AI，但判断力不能。** 最终活下来的不是"拥抱氛围"的人，而是"驾驭氛围"的人。

---

## 跃迁 6/8 — 上下文工程（Context Engineering）：从"怎么问"到"给什么" (2025.6)

**谁：** Tobi Lütke（Shopify CEO）2025.6.19 推文提出
**背书：** Andrej Karpathy 称其为"精妙的艺术与科学（delicate art and science）"，强调做好它"极其不简单"

Lütke 的定义：**"Context Engineering 是为任务提供所有必要上下文、以使其有可能被 LLM 解决的艺术。"**

这看起来只是给提示工程（Prompt Engineering）换了个名字，但实质完全不同：

| | 提示工程 Prompt Engineering | 上下文工程 Context Engineering |
|:---|:---|:---|
| **关注** | 怎么**问** | **给什么**信息 |
| **范围** | 一段提示文本 | 整个信息环境的设计 |
| **包含** | 措辞、格式、示例 | RAG 数据 + 工具定义 + 系统状态 + 对话历史 + 策略规则 |
| **难度** | 文案技巧 | **系统架构** |

到 2025 年，上下文窗口（Context Window）已从 4K Token 扩展到 **100 万+**。你可以把整个代码库喂给模型，问题变成了**"如何策划正确的上下文"**——需要构建自动化的检索（Retrieval）、过滤、排序和注入系统。

---

## 跃迁 6/8 — 为什么是 Shopify CEO 而非 AI 研究者提出了这个概念

这个概念来自**大规模生产实践**，而非实验室。

Shopify 的工程团队在将 AI 集成到电商平台的过程中发现：**90% 的挑战不在于模型能力，而在于上下文管理。** 模型够强了——但如果你喂给它错误的信息、遗漏了关键约束、或者塞了太多无关内容，结果照样一塌糊涂。

Simon Willison 赞同：这个词更准确地描述了现代 AI 工程的复杂性。"提示工程（Prompt Engineering）"已经被用烂了，和"在 ChatGPT 里打字"混为一谈。Karpathy 补充说，做好上下文工程"极其不简单"——信息太少 AI 做不了，太多反而干扰性能又增加成本。

上下文工程（Context Engineering）迅速成为 AI 工程的核心学科，也成为后续治具工程（Harness Engineering）中最关键的支柱——OpenAI App Server 项目的自动化上下文管理系统正是"治具"的核心组成部分。

> **Takeaway：** 如果 AI 是一位顶级厨师，上下文工程（Context Engineering）就是"备菜"的艺术。你给它新鲜食材和精确食谱，它做出米其林；你给它过期原料和模糊要求，它做出暗黑料理。**厨师的水平已经够了——胜负手在"备菜"。**

---

## 跃迁 7/8 — 规范驱动开发（Spec-Driven Development）：代码不再是核心资产 (2025 下半年)

**谁：** Guy Podjarny（Snyk 创始人 / Tessl 创始人）提出核心理念；Martin Fowler（ThoughtWorks 首席科学家）建立理论分级
**工具：** Tessl Framework & Registry、Amazon Kiro、GitHub Spec Kit
**时间：** 2025 年 9–10 月工具陆续发布

SDD 的核心假设极为犀利：**如果 AI 生成代码的成本趋近于零，那么代码本身就不再是核心资产——规范（Specification）才是。代码只是规范的"编译产物（Compiled Artifact）"。**

Martin Fowler 将 SDD 分为三个层级：

| 层级 | 做法 | 理念 |
|:---|:---|:---|
| **L1 规范先行 Spec-First** | 先写规范，再让 AI 生成代码 | 规范是起点 |
| **L2 规范锚定 Spec-Anchored** | 规范与代码同步维护 | 规范是"锚" |
| **L3 规范即源码 Spec-as-Source** | 规范即源码，人类永远不直接改代码 | 规范是唯一真相 |

传统开发：人写代码，代码是资产，文档是附属品，代码腐烂（Code Rot）后文档过时。
规范驱动：人写规范，规范是资产，代码是 AI 编译产物，规范更新后代码自动重新生成。

---

## 跃迁 7/8 — 三家巨头同时下注——这在 AI 编程领域极为罕见

SDD 之所以不是纸上谈兵，是因为**三家巨头几乎同时推出了落地工具**：

- **Tessl**（Guy Podjarny）：规范注册表（Spec Registry）包含 **10,000+** 开源库使用规范，直接解决 AI 最头疼的"API 幻觉（API Hallucination）"问题——AI 编造不存在的函数和参数。每日数万名工程师使用。
- **Amazon Kiro**：基于 VS Code 的新 IDE，**内建 SDD 工作流**——自然语言 → 带验收标准（Acceptance Criteria）的用户故事 → 可追踪的实现任务。还引入代理钩子（Agent Hooks），文件变动时自动触发测试和文档。
- **GitHub Spec Kit**：GitHub 官方规范工具，三步流程 + 不可变原则（Immutable Principles）。

ThoughtWorks 技术雷达（Technology Radar）将 SDD 列为 2025 年值得关注的趋势，但也发出警告：规范文件同样冗长难审查，"开发者可能正在重新学习一个苦涩的教训——为 AI 手工制定详细规则最终无法扩展"。各工具对 SDD 的诠释差异仍大，尚未形成统一标准。

> **Takeaway：** SDD 就像建筑行业的蓝图制度——没有人会让工人凭感觉砌墙。当"砌墙"（写代码）变得几乎免费，**蓝图（规范）自然就成了最值钱的东西。** Amazon、GitHub、Tessl 三家同时下注，本身就是最强的信号。

---

## 跃迁 8/8 — 治具工程（Harness Engineering）：人类建造"让 AI 写代码的工厂" (2026.2)

**谁：** Addy Osmani（Google Chrome 工程经理）2026.2.4 提出代理工程（Agentic Engineering）；OpenAI 2026.2.11 披露治具工程（Harness Engineering）实践；Martin Fowler & Birgitta Böckeler（ThoughtWorks）进行理论阐释
**核心案例：** OpenAI App Server 项目

Addy Osmani 先打了铺垫——他的代理工程（Agentic Engineering）三条铁律直接回应 Vibe Coding 的混乱：**架构先行（Architecture First）**、**编排（Orchestration）**、**无情测试（Relentless Testing）**——测试是代理的停止条件，没过就不准停。他还提出"80% 问题"：代码 80%+ 由 AI 生成 → 面临假设传播（Assumption Propagation）和抽象膨胀（Abstraction Bloat）的新挑战。

一周后，OpenAI 披露了更震撼的实践：

> 从空仓库起步，3 名工程师 + Codex 代理（GPT-5），5 个月 → 约 **100 万行代码** → **1,500 个 PR**。**没有人类手写过一行代码。** 节省约 10 倍时间，每人每天 3.5 个 PR。产品已有内部日活用户和外部 Alpha 测试者。

---

## 跃迁 8/8 — 治具（Harness）：不是产品，而是生产产品的流水线

"治具（Harness）"是制造业术语——不是产品本身，而是固定和引导工件加工的夹具。在 AI 编程语境下：传统程序员交付产品，治具工程师交付**生产产品的流水线**。

OpenAI 的治具包含三个核心组件：

| 组件 | 做什么 | 类比 |
|:---|:---|:---|
| **上下文工程系统 Context Engineering** | 代理改数据库时自动抓取最新 Schema 和设计文档 | GPS 自动推送路况 |
| **架构约束 Architectural Constraints** | 自定义 Linter："所有 API 必须过鉴权"——违反自动驳回 | 流水线质检仪器 |
| **垃圾回收代理 GC Agents** | 后台 AI 扫描僵尸代码/文档漂移/命名违规，自动提 PR | 自动巡检机器人 |

乐观者说：从汇编到高级语言、从高级语言到框架、从框架到治具——这是软件工程抽象层级（Abstraction Level）的又一次跃升。质疑者问：这是不是只有拥有 GPT-5 的 OpenAI 才玩得起？Martin Fowler 态度谨慎——他发表了专题分析，既不盲目推崇也不简单否定。

> **Takeaway：** 治具工程（Harness Engineering）之于软件，就像现代汽车工厂之于手工作坊。福特没有雇更多铁匠——他建造了流水线。**2026 年的程序员也不是在写更多的代码，而是在设计让 AI 高效写代码的"工厂"。** 这是目前的最前沿——前方还没有路，正在一边走一边修。

---

## 全景回顾：八次跃迁，一条主线

```
Copilot → Prompt    → Agentic   → Reasoning → Vibe    → Context    → Spec-Driven → Harness
          Engineering  Workflow    Model       Coding    Engineering   Development   Engineering

"AI能      "我教AI    "让AI自己   "让AI停下   "别管      "关键是      "规范是      "我建造
 写代码"    怎么写"    想办法"     来想想"     代码了"    给什么"      源码"        工厂"
```

**人类角色：使用者 → 作家 → 管理者 → 评估者 → 验收官 → 策展人 → 架构师 → 建筑师**

每一次跃迁的本质都是同一件事：**人类把越来越多的"执行"交给 AI，自己向"决策"层上移。**

---

## 控制权的辩证法

### 正题（2022–2024）：努力控制

我们用精妙的提示、严格的流程、清晰的角色定义，试图**驯化**不可预测的 AI。

### 反题（2025 初）：放弃控制

Vibe Coding 说"别管了，拥抱概率、拥抱速度、拥抱氛围"。结果——认知债务（Cognitive Debt）积累、安全漏洞泛滥、系统腐化。

### 合题（2025 末–2026）：在更高层面重建控制

我们**重新夺回了控制权**——但不是通过写代码，而是通过**构建环境**（治具 Harness）和**制定规范**（规范 Specification）。

这是螺旋上升，不是简单循环。每一轮，人类都站在了更高的抽象层。

---

## 结语

> **2026 年的程序员正在经历一次身份重塑：**
>
> **从代码的工匠（Code Craftsman），变为约束的建筑师（Constraint Architect）。**
>
> **他们不再手写砖墙，**
> **而是设计蓝图、搭建脚手架、编排工人**
> **——在由硅基智能驱动的无限生产力引擎上，**
> **施加人类的意图与判断力。**

数据来源与详细分析见：《AI 编程范式演变技术编年史》《AI 编程八次范式跃迁》

*2026 年 2 月*
