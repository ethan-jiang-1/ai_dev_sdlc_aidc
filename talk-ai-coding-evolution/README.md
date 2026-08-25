# Talk: One Person Company 的 AI Coding 深度 —— 从 Prompt 到 Harness 一路向上

本目录是这场 talk 的推敲工作区。**目的只有一个：把故事线推敲出来。**

**主题速记**：更大的主题是 **一人公司（one person company）**：一个人要真正熟练地掌握 AI Coding 的各种工具，
掌握到什么深度？依赖现成还是自己做？**五层演变（Prompt→Context→Harness→Loop→Graph）+ DSH**
都是为回答这个问题服务的素材；DSH 作为 flexible harness，一个能罩住 harness/loop/graph 三层，
正好是收尾的落点。听众：懂 AI coding 的程序员 / 产品经理 / 投资人（深度深浅不一），
时长 45–50 分钟，基调：通俗易懂、抓要害、引发共鸣。

## 工作区地图

```text
talk-ai-coding-evolution/
├── README.md                                # 本文件：地图 + 素材说明 + 工作方式
├── AGENTS.md                                # 【agent 手册】harness 的操作步骤 + 规则
├── rawdata_ai-coding-evolution-final/       # 【symlink】原始数据 ① 五层演变最终报告
├── rawdata_dsh-faq-on-digested/             # 【symlink】原始数据 ② DSH Harness 机制问答
├── 01_storyline/                            # ★ 故事线推敲主战场（本 talk 的核心产物）
│   ├── 00-storyline-map.md                  #   故事线总图：一句话弧线 + 幕结构
│   ├── 01-thesis-and-positions.md           #   核心论点与立场（待推敲）
│   ├── 02-turning-points.md                 #   转折点 / 锚点清单（待推敲）
│   ├── 03-audience-and-pitch.md             #   听众、带走什么、一句话 pitch（待推敲）
│   └── 04-open-questions.md                 #   悬而未决的问题（推敲中随手记）
├── 02_evidence/                             # 素材卡片：数字、金句、事件（从 rawdata 摘，标来源）
├── 03_outline/                              # talk 大纲：章节结构、slide 骨架
└── 04_drafts/                               # 讲稿 / 逐页草稿 / 版本迭代
```

## 两份原始数据是什么

### ① `rawdata_ai-coding-evolution-final/` —— 宏观故事线素材
指向 `ai_tool_deepresearch/dpt_rb_ai-coding-evolution/final`，是一份**五层演变的最终研究报告**：
Prompt engineering → Context engineering → Harness engineering → Loop engineering → Graph
engineering（2025–2026）。核心主张：**五层是叠加而非替代**；驱动机制是"模型越强，单次交互
的边际工程收益越低，工程杠杆点越往上移"；并带成熟度标尺（前三层成熟可信，Loop/Graph 是
2026 夏才冒头的新兴叙事、低置信度）。

→ 它给 talk 提供**整条故事线和论点骨架**。

### ② `rawdata_dsh-faq-on-digested/` —— 微观机制素材
指向 `deepseek-harness/_faq_on_digested`，是对 DeepSeek Harness 消化材料 + 源码的**二次研究问答**：
目录组织、Spec-Driven Development、模型 vendor 接入、根入口文档的设计与导航、SPEC 变更路径、
"别的项目怎么借鉴 Harness 思路"（知识外置 / 正确路径 / 可执行反馈三条腿）等 7 个探究过的问题。

→ 它给 talk 提供 **Harness 层的"show, don't tell"实证案例**：一个真实 harness 到底怎么让
coding agent 不糊涂、不乱发挥。讲 harness era 时，DSH 是最好的活例子。

**两者分工：① 讲"为什么和往哪走"（宏观弧线），② 讲"具体长什么样"（微观机制）。**

## 工作方式

agent 的操作手册在 [`AGENTS.md`](./AGENTS.md)：每次进来先读它，按它定的步骤走、把状态落回源文件。
人只需记住一句：**推敲主线在 `01_storyline/`，先故事线后 slide，两个 symlink 只读。**
