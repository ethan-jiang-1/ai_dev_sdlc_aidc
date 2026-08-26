# 开场 + 第一幕 · 五层演变 —— 逐页内容（P1–P8）

> 对应 `00-page-structure-23.md` P1–P8（3.5 + 12 min）。**每节 = 一页现场内容**：上屏文字（标题/副题/正文）+ 讲点素材。
> 素材来源见 `../02_evidence/00-absorption-plan.md` 第二节。

---

## P1 封面（0.5 min）

**上屏文字**
- 标题：**OPC 航海指南**
- 副题：OPC 与 Harness，AI 协作之道
- 一行：一个人，AI Coding 要掌握到多深？

**讲点 / 素材**
- 讲点：开场白——今天不讲工具教程，讲一条线索：这两年 AI Coding 的工程注意力怎么一层层往上走，以及一个人（你）该站在哪一层。
- 转场：先讲为什么这个话题跟每个人都有关系。

---

## P2 钩子（1.5 min）—— 你的角色一直在变

**上屏文字**
- 标题：你的角色，两年换了五任
- 正文：
  - 2024 说话者：打磨 prompt
  - 2025 策展者：审代码、喂 context
  - 2026 环境工程师 → 控制流作者 → 编排者
  - "I don't prompt Claude anymore. My job is to write loops." —— Boris Cherny
  - 你不是在追新工具，你是在被模型往上推

**讲点 / 素材**
- 目的：让听众对号入座——你不是在学新工具，是被往上推。
- 讲点：两年前在打磨 prompt → 一年前在审代码喂 context → 现在有人开始写 loop、排多 agent；角色表预览：说话者 → 策展者 → 环境工程师 → 控制流作者 → 编排者。
- 金句："I don't prompt Claude anymore. My job is to write loops."
- 转场：这条路是怎么走出来的？五层演变。

---

## P3 路线图（1.5 min）

**上屏文字**
- 标题：今天四站
- 正文：
  1. 五层演变——注意力一层层上移
  2. 根本还是 harness
  3. 固定 vs 灵活——你该怎么选
  4. DSH——一个把灵活性交给你的 harness

**讲点 / 素材**
- 讲点：四站对应四幕；最后给一句可以带走的话。
- 转场：第一站。

---

## P4 发动机（2 min）—— 一个原因，五层结果

**上屏文字**
- 标题：一个原因，五层结果
- 正文：
  - METR：50% 可靠性任务长度 ≈ 每 7 个月翻倍
  - "prompt 的精确措辞，越来越不重要" —— Anthropic
  - 杠杆点上移：说什么 → 看什么 → 在什么系统里跑
  - **叠加，不是替代**

**讲点 / 素材**
- 目的：立发动机——整场故事只有一个原因。
- 讲点：五层背后只有一个驱动机制（模型越强 → 边际收益越低 → 杠杆点上移）；METR 数字 + Anthropic 原话作双证据；每一次上移都是叠加不是替代。
- 转场：从第一层开始看。

---

## P5 Prompt + Context（3 min）—— 说话者 → 策展者【合并：Prompt + Context】

**上屏文字**
- 标题：第一二层：从"说什么"到"看什么"
- 正文：
  - Prompt 是行为控制面，不是系统本身
  - 把系统问题塞进更长 prompt = 把缺失的控制面伪装成提示复杂度
  - "The agent has a prompt, a Bash Tool, and an Edit Tool."（最小脚手架）
  - Context engineering：决定模型此刻该看到什么
  - context rot：**塞得越多，记得越差**
  - MCP / RAG：能力到位、注意力上移，才成为焦点

**讲点 / 素材**
- 目的：前两层一起讲——从"说什么"到"看什么"，人从说话者变策展者。
- 讲点：prompt 定义与反常识；SWE-bench 最小脚手架例证（后面还会出现）；context 的工程对象；context rot 量化锚点（Lost in the Middle 两头好中间差）；MCP/RAG 反年代学。
- 金句："The agent has a prompt, a Bash Tool, and an Edit Tool."
- 反转：塞得越多，记得越差（context rot）。
- 转场：看对了，但它在什么环境里跑？

---

## P6 Harness（2.5 min）—— 环境工程师：它在什么系统里跑（埋雷）

**上屏文字**
- 标题：第三层：模型在什么系统里跑
- 正文：
  - **Agent = Model + Harness** —— Böckeler
  - harness = 模型之外的一切：权限 / 沙箱 / 工具 / 验证 / trace / CI
  - **单次运行容器**：loop 每次迭代实例化一个 harness；graph 每个节点跑在它自己的 harness 里
  - ⚠️ 2026 安全事件，集中爆发在这一层

**讲点 / 素材**
- 目的：第三层，成熟主体二。**埋雷：这是承重墙**（第二幕要用）。
- 讲点：工程对象移到"在什么系统里跑"；为什么轮到它（prompt/context 不提供可执行环境）；反面提醒（2026 安全事件）；**埋雷**（单次运行容器）；人的角色 = 环境工程师。
- 转场：一次运行稳了，但一次不够。

---

## P7 Loop + Graph（2.5 min）—— 控制流作者 → 编排者【合并：Loop + Graph】

**上屏文字**
- 标题：第四五层：从"迭代"到"编排"
- 正文：
  - Loop = 反馈驱动迭代：模型越强越能"知错改错"——反馈得当，就不断输出更好结果
  - 黄金法则：只有上次结果改变下次行动，才算 loop
  - "A loop can be wrong in ways that are subtle, expensive, and hard to detect."
  - Graph = 编排：用 workflow / DAG 把多 agent 的乱发挥收进显式流程（谁先做、何时分支、何时停）
  - 两盆冷水：不是新东西（LangGraph 2024 早就有 workflow/DAG，只是"编排 agent"当时没凸显）/ 术语先于发布（260 万浏览，无框架发布）
  - **叙事期：火六周就被接棒**

**讲点 / 素材**
- 目的：两个新兴层一起讲——从"迭代"到"编排"，都落在"需要强悍 harness"。
- 讲点：loop 引擎（模型越强越能"知错改错"，反馈得当就越迭代越好——与 harness 的 Sensors 同源，单次反馈连成循环）；定义爆发（Osmani / Macedo）；黄金法则；blast radius 反转；graph 的本质是编排（orchestration：用 workflow/DAG 约束乱发挥、换可靠结果）；"不是新东西"+"术语先于发布"（口径：260 万非 2.6 亿）；叙事期判断。
- 金句："replacing yourself as the person who prompts the agent."
- 反转：blast radius / 不是新东西 / 术语先于发布。
- 转场：五层都过完了，回头看整体——五层不是时间线，是一栋楼。

---

## P8 叠加观 + 成熟度（2 min）—— 不是换代，是叠加

**上屏文字**
- 标题：五层不是时间线，是一栋楼
- 正文：
  - 叠加，不是换代：学会用扳手，不等于扔掉螺丝刀
  - 成熟度标尺：前三层在生产里跑；后两层在叙事期
  - 今天重仓 1–3 层
  - 五层里，有一层是其他所有层的**承重墙**

**讲点 / 素材**
- 目的：收第一幕，立"叠加"观 + 成熟度标尺，为第二幕的 harness 转折铺垫。
- 讲点：叠加观（扳手/螺丝刀比喻）；成熟度标尺（前三层成熟可信、后两层叙事期）；今天重仓 1–3 层；把话题引向承重墙。
- 金句：扳手 / 螺丝刀比喻。
- 转场：为什么说 harness 是承重墙？（进第二幕）

---

## 本幕素材来源速查

- P2 / P7 金句（Cherny / Steinberger / Osmani）：`../_reference/rawdata_ai-coding-evolution-final/final_v4/04-2026-loop-era.md`
- P4 METR / Anthropic：`../_reference/rawdata_ai-coding-evolution-final/final_v4/01-2025-prompt-era.md`、`../_reference/rawdata_ai-coding-evolution-final/final_v4/02-mid-2025-context-era.md`
- P5 SWE-bench 脚手架 / context rot / MCP / RAG：`../_reference/rawdata_ai-coding-evolution-final/final_v4/01-2025-prompt-era.md`、`../_reference/rawdata_ai-coding-evolution-final/final_v4/02-mid-2025-context-era.md`
- P6 Agent = Model + Harness：`../_reference/rawdata_ai-coding-evolution-final/final_v4/03-2026-harness-era.md`
- P7 Graph 双源定义 / 反转：`../_reference/rawdata_ai-coding-evolution-final/final_v4/05-2026-graph-era.md`
- P8 叠加观 / 成熟度：`../_reference/rawdata_ai-coding-evolution-final/final_v4/06-five-layer-forward.md`
