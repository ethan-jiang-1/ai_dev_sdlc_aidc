# 组织航海指南：组织与 Harness，规模化 AI Coding 之道

本目录是这场 talk 的推敲工作区。**目的只有一个：把故事线推敲出来。**

> 姊妹目录 [`../talk-ai-coding-evolution-opc/`](../talk-ai-coding-evolution-opc/README.md) 针对 **OPC（一人公司）**；
> 本目录针对 **组织（org / enterprise）**。两者共享同一套上游素材（五层演变 + DSH），但**问题和落点不同**。

**官方题目（待定）**：组织航海指南：组织与 Harness，规模化 AI Coding 之道。

**主题速记**：`-opc` 问的是「一个人要把 AI Coding 掌握到多深」；本 talk 问的是「**一个组织要把 AI Coding
建成怎样的能力**」。五层演变（Prompt→Context→Harness→Loop→Graph）+ DSH 仍是素材，但读法变了：组织里五种工程角色
**可以分工**，于是真正的问题不是「个人往深里走到哪」，而是「这些能力该**建在哪、谁拥有、如何不各自为政**」。
组织要掌握的临界点同样是 **harness**，但形态是**共享平台 + 治理边界**：任务归团队，平台归组织，边界归治理。
听众：CTO / 平台工程负责人 / 研发效能与安全合规负责人（有组织决策权，不一定是 hands-on 程序员），
时长 45 分钟（硬上限 50），基调：抓要害、讲治理、引发组织决策者的共鸣。

## 工作区地图

```text
talk-ai-coding-evolution-org/
├── README.md                                # 本文件：地图 + 素材说明 + 工作方式
├── AGENTS.md                                # 【agent 手册】harness 的操作步骤 + 规则
├── _reference/                              # 上游素材 symlink（只读），与 -opc 共享同一批源
│   ├── README.md                            #   symlink 一览 + 引用约定 + 规则
│   ├── rawdata_ai-coding-evolution-final/   #   【symlink】五层演变最终报告
│   ├── rawdata_dsh-faq-on-digested/         #   【symlink】DSH Harness 机制问答
│   ├── rawdata_dsh-digested/                #   【symlink】DSH 源码消化（底层机制）
│   ├── rawdata_dsh-plugin-business-ladder/  #   【symlink】插件对 owner 的收益阶梯
│   ├── rawdata_dsh-plugin-ecosystem-distribution/ # 【symlink】插件生态分布快照
│   └── rawdata_dsh-plugin-seam-maturity/    #   【symlink】插件接缝与成熟度
├── _asset/                                  # 视觉资产（模板待定：风格不限制，按内容选）
│   └── README.md                            #   模板选型原则
├── 01_storyline/                            # ★ 故事线推敲主战场（本 talk 的核心产物）
│   ├── 00-storyline-map.md                  #   故事线总图（v0.1）：一句话主线 + 幕结构 + 各幕要点
│   ├── 01-thesis-and-positions.md           #   核心论点与立场（摘要）
│   ├── 02-turning-points.md                 #   转折点 / 锚点清单
│   ├── 03-audience-and-pitch.md             #   听众、时长、pitch
│   ├── 04-open-questions.md                 #   已决 / 待办（随手记）
│   ├── 05-five-layer-reading.md             #   五层叠加的"组织读法"（vs 个人读法）
│   └── 06-harness-internals.md              #   harness 里头干啥（组织版：公共可靠性基础设施）
├── 02_evidence/                             # 素材与脉络（待推敲）
│   ├── 00-absorption-plan.md                #   内容吸纳清单（待补）
│   └── 01-info-flow-map.md                  #   信息脉络图（待补）
├── 03_outline/                              # 页面结构与逐页内容（待推敲）
│   └── 00-page-structure-23.md              #   ★ 现场版页面结构（23 页 · 45 min，初稿待审）
├── 04_drafts/                               # 口语讲稿 / 生产事实稿（待写）
└── 05_output/                               # PPTX 交付（待产出）
```

> **临时目录约定**：与 `-opc` 相同——所有一次性产物（构建中间体、逐页 inspect、审稿草稿、模板试验）
> 放仓库根目录、以 `.tmp-org-talk-*` 前缀命名，不入库；版本收口后清理。细则见 [`AGENTS.md`](./AGENTS.md)。

## 上游素材是什么（与 -opc 共享）

> 上游 symlink 都收在 [`_reference/`](./_reference/README.md) 下，只读。详细分工见该 README。

- **① `rawdata_ai-coding-evolution-final/`** —— 五层演变最终报告：Prompt→Context→Harness→Loop→Graph（2025–2026）。
  核心主张：**五层是叠加而非替代**；驱动机制是"模型越强，单次交互边际工程收益越低，杠杆点越往上移"。
  → 给 talk 提供**整条故事线和论点骨架**。
- **② `rawdata_dsh-faq-on-digested/`** —— Harness 机制问答，讲"具体长什么样"。
- **③ `rawdata_dsh-digested/`** —— DSH 源码消化，讲"底层机制怎么实现"。
- 后三份专题源（plugin-business-ladder / ecosystem-distribution / seam-maturity）只补生态、收益与成熟度证据。

**对 `-org` 而言，同一批素材换一种读法**：`-opc` 把五层读成"一个人的深度标尺"；`-org` 把五层读成
"组织里五种工程角色的分工图 + 三档责任该落在哪一层"。素材不变，问题与落点变。

## 工作方式

agent 的操作手册在 [`AGENTS.md`](./AGENTS.md)：每次进来先读它，按它定的步骤走、把状态落回源文件。
加工顺序固定为 **故事线 → 证据口径 → 页面职责 → 生产事实稿 → PPTX → 文字/视觉 QA**；review 后若成稿发生变化，
再反向同步。当前为 **v0.1 初稿**，`_reference/` 下所有 symlink 只读。

## 与 `-opc` 的关系（一句话）

`-opc` 回答「一个人要掌握多深」→ 答案是 **harness**，原则「部件可借，边界**自己定**」；
`-org` 回答「组织要建成什么能力」→ 答案同样是 **harness**，但形态是「共享平台 + 治理边界」，原则「部件可借，边界**归治理**」。
