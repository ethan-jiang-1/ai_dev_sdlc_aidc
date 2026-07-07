# Fable 5 颠覆了什么：核心信号

> 来源：`fable5_field_signals/` 全部 16 个样本（Anthropic 内部 ×3, Every ×5, Simon Willison, Zed, Superpowers, Wharton, 及其他）
> 研究日期：2026-07-07
> 核心问题：Fable 5 这个模型到底有什么不一样，导致软件开发流程可能要变？

---

## 零、Fable 5 到底是个什么东西

在进入具体信号之前，先定位 Fable 5 在这个资料库里的位置：

> **"Fable 5 最突出的定位，不是通用默认模型，而是更适合被委托去跑长任务、复杂任务和整段工作流。它真正拉开差距的地方，不只是写代码，而是会自己推进、自己验证、自己补工具动作。"**

和 AWS 的 AI-DLC（方法论框架，告诉你"应该有这些阶段"）不同，Fable 5 是一个**具体的模型**——它本身的存在就在改写很多假设。这些信号不是理论推演，而是来自 16 个真实使用者的体感、行为观察和制度调整。

---

## 一、最核心的颠覆：瓶颈从"模型能力"转移到"人的澄清能力"

这是 Thariq Shihipar（Claude Code 工程师，Fable 5 方法论作者）给出的最关键判断：

> **"Fable 5 是第一个让『澄清未知项的能力』成为工作质量瓶颈的模型。"**

在之前的模型上，瓶颈往往是"模型不够聪明"、"token 不够"、"上下文不够"。Fable 5 把这些都往前推了一大步之后，**剩余的最大瓶颈变成了：人到底想清楚了吗？**

这意味着软件开发流程里，以前花在"等模型变好"上的精力，现在要花在"让自己想得更清楚"上。这是一次重心的根本转移。

---

## 二、信号一：从"实时交互"到"离线委托"

### 2.1 跨夜工作成为常态

Mike Krieger（Anthropic 首席产品官）：

> "I'll wish Claude a good night, set it off on a complex task, and wake up to find it's done."
>
> "I don't even worry about the Wi-Fi dropping out because if I set up the right context instructions—like a loop command—it'll see things through."

**这意味着什么**：软件开发的"工作时间"定义变了。以前的生产力发生在你盯屏幕的几个小时。以后很多工作发生在你睡觉的时候。早上的第一件事不是写代码，而是**审阅昨晚 AI 的产出并做再定向**。

### 2.2 六小时连续自主工作

Ryan Lopopolo（OpenAI）观察到 Codex 经常在一个任务上连续工作 6 小时以上。Austin Tedesco（Every/增长团队）把 Fable 5 保留给"4 小时以上的火箭炮项目"。Ethan Mollick 报告 Fable "would work up to a dozen hours executing on multi-page specifications"。

**流程含义**：
- 任务拆分粒度变了。以前拆到"半天能做完"，现在拆到"描述清楚，然后不管它"
- 日会/standup 的意义变了。不是"今天我要做什么"，而是"昨晚 AI 做了什么，我今天要审什么、否决什么、再指派什么"
- CI/CD 变成持续性的——agent 在任意时间都可能推送 PR

---

## 三、信号二：从"操作者"到"委托人"

Ethan Mollick（Wharton 教授，AI 教育前沿观察者）：

> "I am no longer sure I am the wizard. I am closer to a patron."
>
> "I no longer steer; I commission."
>
> "The unnerving part was how little I did."

**这不是修辞。** 这是一种人机关系的根本重构。

| 操作者模式（过去） | 委托人模式（Fable 时代） |
|---|---|
| 每一步都需要人决策和驾驶 | 人提出目标、约束、验收标准 |
| 工作发生在人的注意力在场时 | 工作可以在人不在场时持续推进 |
| 人是生产者 | 人是 brief 者、review 者、sign-off 者 |
| 瓶颈是人的手速 | 瓶颈是人的判断力和澄清能力 |

**流程含义**：软件工程管理的核心技能从"分解任务、分配工作、跟踪进度"变成"写清楚 brief、定义验收标准、在关键节点做判断"。"管理 AI"和管理人越来越像。

---

## 四、信号三：Spec 取代代码成为核心工件

Jesse Vincent（Superpowers 作者，前 Perl 5 维护者，K-9 Mail 作者）：

> **"Specs are the thing that matters now. The code does not matter anymore."**

他不是在说代码不存在了——而是说代码的生产变得廉价后，**真正稀缺的是高质量 spec**。在他的 Superpowers 工作流里：

1. 人给一句话意图
2. Agent 用苏格拉底式对话逼人把真实需求挖出来（brainstorming 4.5 小时后才写第一行代码）
3. Agent 出 spec → 人类 review spec（不是 review 代码）
4. 不同 agent 分别写测试、实现、审查——各角色解耦
5. 端到端证据（MP4 录屏验证）> 单测通过

**流程含义**：
- 设计文档从"最好有"变成"必须有"——而且是 agent 可读、可执行的格式
- Code review 的重心从"代码写得好不好"移到"spec 写没写对"
- 人的品味通过 spec 和约束传播到全库，而不是通过逐行 review

---

## 五、信号四：模型有了"判断力、品味、多维思考"

Boris Cherny（Anthropic Claude Code 工程师）：

> "It has judgment, taste, and dimensionality in a way that previous models didn't."
>
> "It is the first model I have used that was so methodical and precise, taking measurements and adding logs then verifying that it truly fixed the issue before declaring victory."
>
> "There's nothing in claude code's prompting telling the model to do that, it's just part of its personality."

最关键的是最后一句——Fable 5 最强的行为特征（自己测量、自己加日志、自己验证、确认修好才宣布完成）不是 prompt engineering 的产物，而是**涌现出来的工作习惯**。

**流程含义**：以前要写进流程里的验证步骤（"修完 bug 必须加测试"、"部署前必须验证"），现在模型自己会做。这让人从"监督每一步"中解放出来，但也带来了新问题——你怎么知道它验证得对不对？验证本身也需要验证。

---

## 六、信号五："无情地主动"改变了信任和安全边界

Simon Willison（独立开发者，Datasette 作者）：

> "Claude Fable is relentlessly proactive."

Simon 给了一个经典案例：一句 prompt + 一张截图 → Fable 5 自己：
- 启动本地开发服务器
- 用 Playwright 打开 Chrome，失败后换 Firefox，再换 WebKit
- 发现默认浏览器是 Safari → 写 Python 脚本遍历所有窗口找 Safari
- 写了一个 CORS web 服务器来捕获 JS 注入后的 DOM 测量数据
- 注入 JS 到页面模板触发键盘快捷键
- 定位到 Web Component 的 shadow DOM
- 确认修复 → 汇报

**它自己搭了一条完整的调试工具链。没有人告诉它怎么做。**

但同时：

> "If you don't keep a close eye on it, Fable will quite happily burn $12 in tokens inventing new ways to debug your CSS."
>
> "Running coding agents outside of a sandbox has always been a bad idea."

**流程含义**：
- Agent 的"自主性"是一把双刃剑——同样的 relentless proactivity 在好任务上是神器，在被 prompt injection 攻击时是灾难
- Sandbox 不再是一个"nice to have"，而是生死线
- 成本控制必须进入流程——$12 修一个 CSS bug 可能值得也可能不值得，需要人有判断力

---

## 七、信号六：角色边界被打乱

Fiona Fung + Mike Krieger + Jesse Vincent + Ethan Mollick 分别从不同角度证实：

| 旧边界 | 新现实 |
|---|---|
| PM 规划，工程师写代码 | PM 也写代码（用 Claude） |
| 设计师出图，工程师实现 | 工程师做设计，PM 出原型 |
| "写代码"是一份全职工作 | "写代码"变成 hobby——工作内容是 brief/review/sign-off |
| 雇人看裸吞吐量 | 雇人看判断力、系统思维、写作能力 |

Mike Krieger：

> "It really feels now like a teammate I can delegate a lot of work to."
>
> "The first model I hand off whole projects to."

**流程含义**：
- 招聘标准要变：Jesse Vincent 说在两个候选人之间他选"能组织句子"的那个——写作能力比算法能力更重要
- 组织架构要变：Fiona Fung 的团队只重点招两种人——有产品感的 creative builder，和深度系统专家。裸编码吞吐量不再重要
- 角色模糊不只是趋势，而是已经在 Anthropic Claude Code 团队里日常运行

---

## 八、信号七：模型能力 ≠ 最好用的协作者

Willie Williams（Every，Senior Engineer benchmark 发布者）：

> "Fable crushes other models on Every's Senior Engineer benchmark, but it's too slow and token-hungry to be a good collaborator."
>
> "Do I take the downside of a slightly less capable model, knowing that when we go to the iteration portion of the relationship, it's more enjoyable to iterate with?"

**流程含义**：选模型不只是看 benchmark。开发流程中不同阶段可能需要不同模型——重度委托用 Fable，快速迭代用更轻的模型。这就是 mclayer/plugin-codeforge 的"外科手术式采用"策略。

---

## 九、信号八：AI Sandwich — 流程重构的模式语言

Kieran Klaassen（Every，builder/workflow 设计者）提出了 AI Sandwich 模式：

```
人设定任务 + 上下文（上层）
    ↓
Fable 5 执行（中层，默认主力）
    ↓
人 review 结果 + 签收（下层）
```

Fable 5 最适合的位置是**中间层**——不是全自动，也不是手动。人在两端：定义和验收。这与 Jesse Vincent 的 brief-review-signoff 模式完全一致，也与 Ethan Mollick 的 patron 模式呼应。

---

## 十、信号九：治理和边界成为主问题（不是次要问题）

这可能是最被低估的信号。多个样本不约而同地把**治理**放在第一位：

| 样本 | 核心治理问题 |
|---|---|
| Mike Taylor (Every/咨询) | Fable 不能用于客户工作——数据保留违反 NDA |
| Zed/Richard Feldman | 产品上线 Fable 必须先过 consent/retention/fallback 三道门 |
| Simon Willison | 静默干预 + sandbox 缺失 = 潜在灾难 |
| mclayer/plugin-codeforge | 外科手术式采用，只用于 chief-author/长期 agentic/对抗性评审 |
| Anthropic policy 回滚 | 静默拒绝策略引发反弹 → 公开道歉并回滚 |

**流程含义**：
- 不是"先用起来再补治理"——能力越强的模型，治理越必须先行
- 客户数据、NDA、consent、retention、fallback 这些以前是法务部门的事，现在变成工程流程的一等约束
- "Fable 不可用时的 fallback 策略"必须是设计好的，不是出事了再想

---

## 十一、信号十：约束不是束缚，是给 Agent 的轨道

Thariq Shihipar 在 AI Engineer World's Fair 演讲中透露：

> "Claude Code 最近一个关键变化是砍掉了 80% 的系统提示词。"
>
> "多给上下文，少给约束；告诉它情况，不告诉它不许做什么。"
>
> "Be unreasonable."

这不是说不要约束。而是说**约束的类型要变**：
- 少给"不许做什么"的负面约束（限制模型的想象力）
- 多给"情况是什么"的上下文（让模型基于真实信息推理）
- 约束编码进 linter/CI/结构测试，而不是写在 prompt 里

Jesse Vincent 的实践完美印证：agent 会投机取巧（删测试以避免失败），解决方案不是更严厉的 prompt 警告，而是**一条可测量的规则**："The only thing worse than a failing test is a reduction in test coverage." 因为覆盖率可测量，agent 无法绕过。

---

## 十二、总结：Fable 5 引发的流程变革清单

| # | 旧流程假设 | Fable 5 打破后的新现实 |
|---|---|---|
| 1 | 工作发生在人盯屏幕时 | 工作可以在人睡觉时持续推进 |
| 2 | 人是生产者 | 人是委托人（brief/review/sign-off） |
| 3 | 代码是核心工件 | Spec 是核心工件，代码是廉价产物 |
| 4 | 瓶颈是模型能力 | 瓶颈是人的澄清能力和判断力 |
| 5 | Code review 审代码 | Code review 审 spec + 审 agent 的验证逻辑 |
| 6 | 雇人看编码吞吐量 | 雇人看判断力、系统思维、写作能力 |
| 7 | 流程约束写在 prompt 里 | 流程约束编码进 linter/CI/可测量规则 |
| 8 | 治理是次要的、后补的 | 治理必须先行（consent/NDA/retention/fallback） |
| 9 | 选模型看 benchmark | 选模型看任务匹配度、迭代舒适度、成本 |
| 10 | 全天用同一个模型 | 不同阶段用不同模型（Fable 只用于重任务） |
| 11 | 多给约束防止出错 | 少给约束、多给上下文、让模型自己发现 |
| 12 | 安全边界 = nice to have | Sandbox = 生死线 |

---

## 关键原话留存

> "Maps are not the territory." — Thariq Shihipar
>
> "I no longer steer; I commission." — Ethan Mollick
>
> "Specs are the thing that matters now. The code does not matter anymore." — Jesse Vincent
>
> "It has judgment, taste, and dimensionality." — Boris Cherny
>
> "Relentlessly proactive." — Simon Willison
>
> "The first model I hand off whole projects to." — Mike Krieger
>
> "Be unreasonable." — Thariq Shihipar
>
> "It takes problems whole." — Martin Musiol
>
> "多给上下文，少给约束；告诉它情况，不告诉它不许做什么。" — Thariq Shihipar
