# AI-Native 研发组织：从产品到实施的 SDLC 转型之道

本目录是这场 talk 的推敲工作区。**目的只有一个：把故事线推敲出来。**

> 姊妹目录 [`../talk-ai-coding-evolution-opc/`](../talk-ai-coding-evolution-opc/README.md) 针对 **OPC（一人公司）**；
> 本目录针对 **研发整体组织（AI-Native 研发组织）**。两者共享「五层演变 + DSH」这套**深轴**素材，但**问题、对象、篇幅完全不同**。

**官方题目（待定）**：AI-Native 研发组织：从产品到实施的 SDLC 转型之道。

**主题速记**：`-opc` 问「一个人要把 AI Coding 掌握到多深」；本 talk 问「**一个研发组织要把 AI Coding 建成怎样的能力**」——
而且范围是**从产品一路到底到实施、再到运维**（整条 SDLC），不是「组织 + harness」的单焦点。核心论点借自 Anthropic
《The AI-Native SDLC playbook》：**代码不再是瓶颈**，慢的是代码左右两边的流程与治理，所以转型对象是整条 SDLC 的六阶段
（Plan→Design→Build→Test→Deploy→Maintain），贯穿主线是「**每一阶段落一个工件，工件链即审计链；人的判断守在每个 gate 之上**」。
**篇幅档位 A**：单场加长 Keynote，75–90 min，目标 ~45–60 页（不再受 23 页约束）。
**独立成篇**：不依赖、不承接 `04_output/deck_ai_sdlc_keynote`（听众不同）。
听众：研发整体组织的决策者——CTO / 平台工程 / 产品 / QA / 安全 / 发布 / 运维负责人。

## 工作区地图

```text
talk-ai-coding-evolution-org/
├── README.md                                # 本文件：地图 + 素材说明 + 工作方式
├── AGENTS.md                                # 【agent 手册】harness 的操作步骤 + 规则
├── _reference/                              # 上游素材 symlink（只读）
│   ├── README.md                            #   symlink 一览 + 引用约定 + 规则
│   ├── rawdata_anthropic-ai-native-sdlc-playbook.md # 【symlink】★ 宽轴：六阶段 SDLC 转型 playbook
│   ├── rawdata_ai-coding-evolution-final/   #   【symlink】深轴：五层演变最终报告
│   ├── rawdata_dsh-faq-on-digested/         #   【symlink】DSH Harness 机制问答
│   ├── rawdata_dsh-digested/                #   【symlink】DSH 源码消化（底层机制）
│   ├── rawdata_dsh-plugin-business-ladder/  #   【symlink】插件收益阶梯
│   ├── rawdata_dsh-plugin-ecosystem-distribution/ # 【symlink】插件生态分布快照
│   └── rawdata_dsh-plugin-seam-maturity/    #   【symlink】插件接缝与成熟度
├── _asset/                                  # 视觉资产（模板待定：风格不限制，按内容选）
│   └── README.md                            #   模板选型原则
├── 01_storyline/                            # ★ 故事线推敲主战场（本 talk 的核心产物）
│   ├── 00-storyline-map.md                  #   故事线总图（v0.5）：一句话主线 + SDLC 主轴 + 引子 + 三幕
│   ├── 01-thesis-and-positions.md           #   核心论点与立场（摘要）
│   ├── 02-turning-points.md                 #   转折点 / 锚点清单（待补 playbook 锚点）
│   ├── 03-audience-and-pitch.md             #   听众、时长、pitch
│   ├── 04-open-questions.md                 #   已决 / 待办（随手记）
│   ├── 05-five-layer-reading.md             #   五层「引子」的理论底（组织读法）
│   ├── 06-harness-internals.md              #   harness「引子」的核心（圈住 / 拦住 / 看清）
│   └── 07-narrative-thinking.md             #   ★ 叙事思路笔记：看了什么 / 被什么启发 / 思路演化 / 决策理由
├── 02_evidence/                             # 素材与脉络
│   ├── 00-absorption-plan.md                #   ★ 六阶段 + 15 play 进货单（铺页面的骨架）
│   └── 01-info-flow-map.md                  #   信息脉络图（待补）
├── 03_outline/                              # 页面结构与逐页内容
│   └── 00-page-structure.md                 #   ★ 现场版页面结构（50 页 · 75–90 min 骨架）
├── 04_drafts/                               # 口语讲稿 / 生产事实稿（待写）
└── 05_output/                               # PPTX 交付（待产出）
```

> **临时目录约定**：与 `-opc` 相同——一次性产物放仓库根目录、以 `.tmp-org-talk-*` 前缀命名，不入库；版本收口后清理。细则见 [`AGENTS.md`](./AGENTS.md)。

## 两套素材怎么合成

- **宽轴 = 六阶段 SDLC**（`rawdata_anthropic-ai-native-sdlc-playbook.md`）：组织转型的**范围**。
- **深轴 = 五层演变 + Harness**（`rawdata_ai-coding-evolution-final` + DSH 系列）：每一个动作的**可靠性边界**。
- **咬合点**：playbook 每个 play 都能落回五层的某一层；harness 从「编码这一格的边界」扩为「整条链的平台层 + 治理层」。
  逐 play 映射见 [`02_evidence/00-absorption-plan.md`](02_evidence/00-absorption-plan.md)。

一句话：**`-opc` 说「harness 是每一次动作的可靠性边界」；本 talk 说「把这个边界铺满整条 SDLC」。**

## 工作方式

agent 的操作手册在 [`AGENTS.md`](./AGENTS.md)：每次进来先读它，按它定的步骤走、把状态落回源文件。
加工顺序固定为 **故事线 → 证据口径 → 页面职责 → 生产事实稿 → PPTX → 文字/视觉 QA**；review 后反向同步。
当前为 **v0.5 初稿**，`_reference/` 下所有 symlink 只读。

## 与 `-opc` 的关系（一句话）

`-opc` 回答「一个人要掌握多深」→ 答案是 **harness**，原则「部件可借，边界自己定」；
本 talk 回答「组织要转型整条 SDLC 的什么」→ 答案是 **代码不再是瓶颈，流程才是**，原则「工件链即审计链，人守 gate」。
