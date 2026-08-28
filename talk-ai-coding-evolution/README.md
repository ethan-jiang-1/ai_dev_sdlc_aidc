# OPC 航海指南：OPC 与 Harness，AI 协作之道

本目录是这场 talk 的推敲工作区。**目的只有一个：把故事线推敲出来。**

**官方题目**：OPC 航海指南：OPC 与 Harness，AI 协作之道（**OPC = One Person Company，一人公司**）。

**主题速记**：更大的主题是 **一人公司（one person company）**：一个人要真正熟练地掌握 AI Coding 的各种工具，
掌握到什么深度？依赖现成还是自己做？**五层演变（Prompt→Context→Harness→Loop→Graph）+ DSH**
都是为回答这个问题服务的素材；DSH 作为可组合的 Harness runtime，帮助说明为什么部件可以借、
运行边界却要保有最终决定权。听众：懂 AI coding 的程序员 / 产品经理 / 投资人（深度深浅不一），
时长 45 分钟（硬上限 50），基调：通俗易懂、抓要害、引发共鸣。

## 工作区地图

```text
talk-ai-coding-evolution/
├── README.md                                # 本文件：地图 + 素材说明 + 工作方式
├── AGENTS.md                                # 【agent 手册】harness 的操作步骤 + 规则
├── _reference/                              # 上游素材 symlink（只读），说明见其 README
│   ├── README.md                            #   symlink 一览 + 引用约定 + 规则
│   ├── rawdata_ai-coding-evolution-final/   #   【symlink】五层演变最终报告
│   ├── rawdata_dsh-faq-on-digested/         #   【symlink】DSH Harness 机制问答
│   ├── rawdata_dsh-digested/                #   【symlink】DSH 源码消化（底层机制）
│   ├── rawdata_dsh-plugin-business-ladder/  #   【symlink】插件对 owner 的收益阶梯
│   ├── rawdata_dsh-plugin-ecosystem-distribution/ # 【symlink】插件生态分布快照
│   └── rawdata_dsh-plugin-seam-maturity/    #   【symlink】插件接缝与成熟度
├── 01_storyline/                            # ★ 故事线推敲主战场（本 talk 的核心产物）
│   ├── 00-storyline-map.md                  #   故事线总图（v1.6）：一句话主线 + 幕结构 + 各幕要点
│   ├── 01-thesis-and-positions.md           #   核心论点与立场（摘要）
│   ├── 02-turning-points.md                 #   转折点 / 锚点清单
│   ├── 03-audience-and-pitch.md             #   听众、时长、pitch
│   ├── 04-open-questions.md                 #   已决 / 待办（随手记）
│   ├── 05-five-layer-reading.md             #   对源报告五层叠加的解读
│   └── 06-harness-internals.md              #   harness 里头干啥（圈住 / 拦住 / 看清）
├── 02_evidence/                             # 素材与脉络
│   ├── 00-absorption-plan.md                #   内容吸纳清单（按页进货单 + 口径红线）
│   └── 01-info-flow-map.md                  #   信息脉络图（上游 → 加工 → 页面 + 反向索引）
├── 03_outline/                              # 页面结构与逐页内容（上屏文字 + 讲点）
│   ├── 00-page-structure-23.md              #   ★ 现场版（23 页，45 min，每页必讲要点）
│   ├── 01-opening-and-act1-content.md       #   开场 + 第一幕逐页内容（P1–P8）
│   ├── 02-act2-harness-content.md           #   第二幕逐页内容（P9–P14）
│   ├── 03-act3-flexibility-content.md       #   第三幕逐页内容（P15–P18）
│   └── 04-act4-dsh-content.md               #   第四幕 + 收尾逐页内容（P19–P23）
└── 04_drafts/                               # 口语讲稿（备用）与术语规范
```

## 上游素材是什么

> 上游 symlink 都收在 [`_reference/`](./_reference/README.md) 下，只读。

### ① `_reference/rawdata_ai-coding-evolution-final/` —— 宏观故事线素材
指向 `ai_tool_deepresearch/dpt_rb_ai-coding-evolution/final`，是一份**五层演变的最终研究报告**：
Prompt engineering → Context engineering → Harness engineering → Loop engineering → Graph
engineering（2025–2026）。核心主张：**五层是叠加而非替代**；驱动机制是"模型越强，单次交互
的边际工程收益越低，工程杠杆点越往上移"；并带成熟度标尺（前三层成熟可信，Loop/Graph 是
2026 夏才冒头的新兴叙事、低置信度）。

→ 它给 talk 提供**整条故事线和论点骨架**。

### ② `_reference/rawdata_dsh-faq-on-digested/` —— 微观机制素材
指向 `deepseek-harness/_faq_on_digested`，是对 DeepSeek Harness 消化材料 + 源码的**二次研究问答**：
目录组织、Spec-Driven Development、模型 vendor 接入、根入口文档的设计与导航、SPEC 变更路径、
"别的项目怎么借鉴 Harness 思路"（知识外置 / 正确路径 / 可执行反馈三条腿）等 7 个探究过的问题。

→ 它给 talk 提供 **Harness 层的"show, don't tell"实证案例**：一个真实 harness 到底怎么让
coding agent 不糊涂、不乱发挥。讲 harness era 时，DSH 是最好的活例子。

### ③ `_reference/rawdata_dsh-digested/` —— 源码消化（底层机制）
指向 `deepseek-harness/_digested`，是 DSH 源码的**消化分析**（system / composition / session-and-loop /
capability-seams / tools-prompt-llm / surfaces 等专题）。讲清 DSH"挂模型 / 挂工具 / 换后端 / 挂插件"的
真实机制——**DSH 不用 MCP**，挂的是 `ctx.llm` adapter、`ctx.tools`、capability seam、plugin。

→ 它给 talk 提供第四幕"灵活性"的**底层证据**。

**三者分工：① 讲"为什么和往哪走"（宏观弧线），② 讲"具体长什么样"（机制问答），③ 讲"底层机制怎么实现"（源码消化）。**

另外三份专题素材分别回答：DSH 插件给 owner 什么收益、生态扩展如何分布、插件进入真实执行链后要补哪些合同与门禁。它们只提供 P17–P21 的证据，不替代故事线判断。

## 工作方式

agent 的操作手册在 [`AGENTS.md`](./AGENTS.md)：每次进来先读它，按它定的步骤走、把状态落回源文件。
加工顺序固定为 **故事线 → 证据口径 → 页面职责 → 生产事实稿 → PPTX → 文字/视觉 QA**；review 后若成稿发生变化，再反向同步到上游。`_reference/` 下所有 symlink 只读。
