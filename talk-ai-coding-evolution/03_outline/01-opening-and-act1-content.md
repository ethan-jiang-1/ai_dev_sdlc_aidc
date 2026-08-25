# 开场 + 第一幕 · 五层演变 —— 逐页内容（现场 P1–P8）

> 对应 `00-page-structure-23.md` P1–P8（3.5 + 12 min）。内部小节编号与分钟为素材锚点，**现场时间以 00-page-structure-23.md 为准**。素材来源见 `../02_evidence/00-absorption-plan.md` 第二节。
> 每页：目的 / 讲点 / 金句 / 通俗例子 / 转场。

---

## S1 封面（0.5 min）

- 标题：**OPC 航海指南：OPC 与 Harness，AI 协作之道**（官方题目）
- 副题（开场问题）：一个人，该把 AI Coding 掌握到多深？
- 讲点：开场白——今天不讲工具教程，讲一条线索：这两年 AI Coding 的工程注意力怎么一层层往上走，以及一个人（你）该站在哪一层。
- 转场：先讲为什么这个话题跟每个人都有关系。

---

## S2 钩子（1.5 min）—— 你的角色一直在变

- **目的**：让听众对号入座——你不是在学新工具，是被往上推。
- **讲点**：
  1. 问台下：两年前你在干嘛？在聊天框里精心打磨 prompt。
  2. 一年前？在 Claude Code 里一行行审它改的代码、给它喂 context。
  3. 现在？有人已经开始写循环、排多 agent 了——Cherny："I don't prompt Claude anymore. My job is to write loops."
  4. 你不是在追新工具，你是被模型一步步往上推——模型越强，你和它的互动方式就越变。
  5. 角色表预览：**说话者 → 策展者 → 环境工程师 → 控制流作者 → 编排者**。
- **金句**："I don't prompt Claude anymore. My job is to write loops."
- **转场**：这条路是怎么走出来的？五层演变。

---

## S3 路线图（1 min）

- 讲点：今天四站：① 五层演变（人机互动怎么变）② 为什么根本是 harness ③ 固定 vs 灵活——你该怎么选 ④ DSH——一个把灵活性交给你的 harness。
- 转场：第一站。

---

## S4 发动机（2 min）—— 一个原因，五层结果

- **目的**：立发动机——整场故事只有一个原因。
- **讲点**：
  1. 五层背后只有一个驱动机制：**模型越强，单次交互的边际工程收益越低，工程杠杆点就往上移**。
  2. 两个硬证据：
     - METR：**50% 可靠性任务长度每 ~7 个月翻倍**——模型可靠干活的时间尺度指数增长。
     - Anthropic："The exact formatting of prompts is likely becoming less important as models become more capable."——prompt 措辞越来越不重要。
  3. 翻译：当模型自己越来越能干，你花在"怎么跟它说话"上的功夫越来越不值钱；值钱的功夫在往上走。
  4. 注意：每一次上移都是**叠加**不是替代——后面每一层都还踩着前面。
- **转场**：从第一层开始看。

---

## S5 Prompt（1.5 min）—— 说话者：我该说什么

- **目的**：第一层，地基层。
- **讲点**：
  1. 工程对象：任务表达——系统提示、few-shot、输出格式、约束。
  2. 一句话定义：**prompt 是行为控制面，不是系统本身**——它塑造模型怎么想，但不决定周围环境。
  3. 反常识：把系统问题塞进更长 prompt，"只是把缺失的控制面伪装成提示复杂度"。
  4. 例证：2024 年 SWE-bench 上 Anthropic 的最小脚手架——"**The agent has a prompt, a Bash Tool, and an Edit Tool.**" 就这么简单。
  5. 人的角色：**说话者**——我写对那句话。
- **金句**："The agent has a prompt, a Bash Tool, and an Edit Tool."
- **转场**：但很快发现，光说得好不够——模型得看到对的东西。

---

## S6 Context（2 min）—— 策展者：它该看到什么

- **目的**：第二层，成熟主体一。
- **讲点**：
  1. 工程对象从"怎么说"移到"**模型此刻该看到什么**"——进入窗口的一切 token：工具返回值、检索结果、仓库事实、任务状态。
  2. 权威定义（Anthropic 2025-09）：context engineering = 策划并维护推理期间**最优 token 集合**。
  3. 量化锚点：**context rot**——token 越多，模型准确回忆越差（Lost in the Middle：两头好中间差）。反转：**更多 context ≠ 更好回忆**——目标是"在保持有用信息的前提下最小化 token"。
  4. 生态级事件在这层：**MCP**（2024-11 宣布、2025 被 Google 采纳）、RAG。注意：技术不新，是"能力到位、注意力上移"才成为焦点。
  5. 人的角色：**策展者**——挑它看什么、给多少 token 预算。
- **反转**：塞得越多记得越差。
- **转场**：看对了，但它在什么环境里跑？

---

## S7 Harness（2.5 min）—— 环境工程师：它在什么系统里跑（埋雷）

- **目的**：第三层，成熟主体二。**埋雷：这是承重墙**（第二幕要用）。
- **讲点**：
  1. 工程对象从"模型看到什么"移到"**模型在什么系统里跑**"：权限、沙箱、工具协议、验证门禁、trace、CI。
  2. 一句定义：**Agent = Model + Harness**（Böckeler）——模型之外的一切都算。
  3. 为什么轮到它：prompt 和 context 都不提供可执行环境——仓库事实、执行权限、失败恢复、测试结果，都不在"模型看到什么"里。
  4. 反面提醒：2026 安全事件集中爆发在这一层（执行时授权缺失）。
  5. **埋雷**：harness 是"单次运行容器"——后面 loop 每次迭代都实例化一个 harness，graph 每个节点也跑在自己的 harness 里。记住这个。
  6. 人的角色：**环境工程师**。
- **转场**：一次运行稳了，但一次不够。

---

## S8 Loop（1.5 min）—— 控制流作者：何时再跑一次

- **目的**：第四层，新兴层、低置信度。
- **讲点**：
  1. 工程对象：跨运行的控制流——**何时、为何、以什么条件重复**。
  2. 定义爆发（2026-06 一个月内四源同发）：Osmani "replacing yourself as the person who prompts the agent"；Macedo 形式化：trigger + goal + execution + verification + stopping rule + memory。
  3. 黄金法则：**只有上次运行的结果改变下次行动，才叫 loop**——固定任务固定调度不算。
  4. 反转：**loop 可能错得更贵**——blast radius = 一次错误 × 循环步数（Woliveiras）。
  5. 置信度：定义才六周就被 Graph 接棒、自动化触发只有 22%——**叙事期，别当定论**。
  6. 人的角色：**控制流作者**——我的工作是写 loop。
- **金句**："I don't prompt Claude anymore. My job is to write loops."
- **转场**：一个人写 loop 够强了，但一件事一个人不够。

---

## S9 Graph（1.5 min）—— 编排者：多 agent 怎么组织

- **目的**：第五层，新兴层、更低置信度。
- **讲点**：
  1. 工程对象：多 agent 系统智能——从"单个 agent 重复"到"多 agent 组织"。
  2. 双源定义：产业流 Steinberger "build agents as **state graphs**"；学术流 "From Individual Intelligence to System Intelligence"（Task Org + Agent Coord + Runtime State）。
  3. 反转 1：**不是新东西**——LangGraph 2024 年就在做组件技术；"新"的是命名的学科意识。
  4. 反转 2：**术语先于发布**——Steinberger 引爆帖 260 万浏览，但 "No framework, model, or capability shipped around the tweet."（口径：260 万，不是 2.6 亿）
  5. 反转 3：**更多连接 ≠ 更好协作**——冗余通信增加成本还放大错误，graph 可能让简单任务更贵。
  6. 人的角色：**编排者**。
- **转场**：五层都过完了。回头看整体——五层不是时间线，是一栋楼。

---

## S10 叠加观 + 成熟度（2 min）—— 不是换代，是叠加

- **目的**：收第一幕，立"叠加"观 + 成熟度标尺，为第二幕的 harness 转折铺垫。
- **讲点**：
  1. **不是换代，是叠加**：五层同时活在 2026 的成熟系统里，只是工程注意力集中在当前"卡脖子"那层。扳手 / 螺丝刀比喻：学会用扳手不等于扔掉螺丝刀。
  2. **成熟度标尺**：前三层（Prompt / Context / Harness）是今天在生产里跑的成熟层——有量化机制、独立证据、真实风险面；后两层（Loop / Graph）是刚冒头的新叙事——"火六周就被接棒"恰恰说明还没沉淀。
  3. 所以今天该重仓的是 1–3 层。这不是保守——是"成熟的组织在所有五层都有显式验证"。
  4. 把话题引向 harness：而五层里，有一层是其他所有层的**承重墙**……
- **金句**：扳手 / 螺丝刀比喻。
- **转场**：为什么说 harness 是承重墙？（进第二幕）

---

## 本幕素材来源速查

- S2 / S8 金句（Cherny / Steinberger）：`final_v4/04-2026-loop-era.md`
- S4 METR / Anthropic：`final_v4/01-2025-prompt-era.md`、`02-mid-2025-context-era.md`
- S5 SWE-bench 脚手架：`final_v4/01-2025-prompt-era.md`
- S6 context rot / MCP / RAG：`final_v4/02-mid-2025-context-era.md`
- S7 Agent = Model + Harness：`final_v4/03-2026-harness-era.md`
- S9 Graph 双源定义 / 反转：`final_v4/05-2026-graph-era.md`
- S10 叠加观 / 成熟度：`final_v4/06-five-layer-forward.md`
