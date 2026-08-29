# AI-Native 软件研发组织：从产品意图到生产运维的 SDLC 转型之道

本目录是这场 talk 的内容与生产工作区。故事线与 50 页页面职责已经锁定，当前只做**视觉预演**；样片通过后再写生产事实稿。

> **总工作规约：先内容，后表现。** v0.7 内容锁已通过，**50 页总页数已定**，作为稳定的生产边界；
> 表现设计服务既定页面职责。完整生产前先过中文编辑门：所有上屏文字、图中标签与讲稿按中文原生句法重写，不把英文句法逐词翻成中文。若表现阶段暴露命题、证据或转场问题，先回写内容源文件，再继续生产。

> 姊妹目录 [`../talk-ai-coding-evolution-opc/`](../talk-ai-coding-evolution-opc/README.md) 针对 **OPC（一人公司）**；
> 本目录只针对 **软件 SDLC 上的跨职能研发与交付组织**。两者共享「五层演变 + DSH」这套**深轴**素材，但**问题、对象、篇幅完全不同**。

**题目**：AI-Native 软件研发组织：从产品意图到生产运维的 SDLC 转型之道。

**主题速记**：`-opc` 问「一个人要把 AI Coding 掌握到多深」；本 talk 问「**软件研发与交付组织要如何重建 SDLC**」。
范围从产品意图、需求与设计，到构建、测试、发布、生产运维；只讨论软件价值流，不外推到销售、市场、客服、财务、人力或一般企业组织设计。
核心命题是把这条交付链重建成「**工件可交接、门禁能执行、责任有人担、结果能回流**」的运行系统。
**篇幅档位 A**：单场加长 Keynote，75–90 min，**50 页已定**。
**独立成篇**：不依赖、不承接 `04_output/deck_ai_sdlc_keynote`（听众不同）。
听众：软件 SDLC 各阶段的决策者——CTO / 技术 VP、产品、架构、平台工程、开发、QA、安全、发布、SRE / 运维负责人。

## 工作区地图

```text
talk-ai-coding-evolution-org-sdlc/
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
├── _asset/                                  # 表现设计与视觉资产
│   ├── README.md                            #   v0.8 系统蓝图式技术编辑风
│   ├── 01-visual-storyboard-v0.8.md         #   50 页视觉分镜 + 八个布局族 + 视觉门禁
│   └── 02-imagegen-prompts-v0.8.md          #   gpt-image-2 样片 brief 与使用边界
├── 01_storyline/                            # ★ 故事线推敲主战场（本 talk 的核心产物）
│   ├── 00-storyline-map.md                  #   故事线总图（v0.7）：沟通任务 + SDLC 主轴 + 三幕
│   ├── 01-thesis-and-positions.md           #   核心论点与立场（摘要）
│   ├── 02-turning-points.md                 #   五层、六阶段与治理锚点清单
│   ├── 03-audience-and-pitch.md             #   听众、时长、pitch
│   ├── 04-open-questions.md                 #   已决 / 待办（随手记）
│   ├── 05-five-layer-reading.md             #   五层「引子」的理论底（软件 SDLC 能力读法）
│   ├── 06-harness-internals.md              #   harness「引子」的核心（圈住 / 拦住 / 看清）
│   └── 07-narrative-thinking.md             #   ★ 叙事思路笔记：看了什么 / 被什么启发 / 思路演化 / 决策理由
├── 02_evidence/                             # 素材与脉络
│   ├── 00-absorption-plan.md                #   ★ 六阶段 + 15 play 进货单（铺页面的骨架）
│   ├── 01-info-flow-map.md                  #   上游 → 主张 → P1–P50 正反向索引
│   └── 02-claim-ledger.md                   #   核心主张证据账本与可说/不可说口径
├── 03_outline/                              # 页面结构与逐页内容
│   ├── 00-page-structure.md                 #   ★ 现场版页面结构（50 页 · 75–90 min 骨架）
│   ├── 01-opening-and-why.md                 #   P1–P12：开场 + 为什么整条链要转
│   ├── 02-six-stages.md                     #   P13–P38：六阶段统一四问
│   └── 03-dsh-and-closing.md                #   P39–P50：共享控制面 + 收尾行动
├── 04_drafts/                               # 口语讲稿 / 生产事实稿（待写）
└── 05_output/                               # PPTX 交付（待产出）
```

> **临时目录约定**：一次性产物放仓库根目录、以 `.tmp-org-sdlc-talk-*` 前缀命名，不入库；版本收口后清理。细则见 [`AGENTS.md`](./AGENTS.md)。

## 两套素材怎么合成

- **宽轴 = 六阶段 SDLC**（`rawdata_anthropic-ai-native-sdlc-playbook.md`）：组织转型的**范围**。
- **深轴 = 五层演变 + Harness**（`rawdata_ai-coding-evolution-final` + DSH 系列）：观察每一步的**外置与控制深度**。
- **咬合点**：playbook 每个 play 都能用五层镜头检查；harness 从「编码这一格的边界」扩为整条软件价值流的共享控制基线。
  逐 play 映射见 [`02_evidence/00-absorption-plan.md`](02_evidence/00-absorption-plan.md)。

一句话：**`-opc` 说「harness 是每一次动作的可靠性边界」；本 talk 说「让共同控制基线覆盖整条 SDLC，同时让领域判断留在明确的 owner 手里」。**

## 工作方式

agent 的操作手册在 [`AGENTS.md`](./AGENTS.md)：每次进来先读它，按它定的步骤走、把状态落回源文件。
加工顺序固定为 **故事线 → 证据口径 → 50 页页面职责 → 内容锁定 → 中文编辑 → 生产事实稿 → 视觉设计 → PPTX → 文字/视觉 QA**；
review 若改变了内容，反向同步回上游源文件。

### 中文表达规则

整套内容以中文演讲者能自然说出口为准。标题先说判断，正文先说动作和结果；阶段写「规划、设计、构建、测试、发布、运维」，必要时在首次出现处补英文。四个贯穿问题统一写成「留下什么工件、哪道门禁必须执行、谁作最后决定、结果怎样回到下一轮」。文件名、产品名和精确机制名可以保留英文，但必须嵌入中文句子，不能用英文词序、斜杠和名词串代替中文表达。逐页生产前按 [`AGENTS.md`](./AGENTS.md) 的“中文编辑门”完成朗读检查。

### 内容锁定门

进入表现阶段前，必须同时满足：

1. 可以用一句话说清听众、期待改变与中心结论。
2. 一个中心命题由 3–5 个必要主张支撑，口径与边界互不矛盾。
3. 各幕之间有因果或问答推进，而不是素材的并列目录。
4. 关键主张都有可追溯来源，并解释对组织决策意味着什么。
5. 开场建立的张力在收束得到解答，听众知道下一步要做什么。
6. 整条主线可以用 5–8 分钟口述，无关键逻辑跳转。

内容锁定后，每页仍先定「叙事职责 + 主要结论」，再做视觉。进入 PPT 阶段时统一使用
`presentations:Presentations` skill，按内容选视觉路线，并完成全量渲染、逐页文字 REVIEW、逐页视觉 REVIEW 和来源追溯。

当前为 **v0.8 视觉预演 + 中文编辑**：v0.7 内容锁已通过；视觉方向采用“统一白底的系统蓝图式技术编辑风”。
下一步先完成 P1-P50 中文审校并验证 P1 / P8 / P20 / P42 四张关键样片；中文编辑门和视觉门禁都通过后，再按八个布局族压 50 页生产事实稿并建立 PPTX。

## 与 `-opc` 的关系（一句话）

`-opc` 回答「一个人要掌握多深」→ 答案是 **harness**，原则「部件可借，边界自己定」；
本 talk 回答「软件交付组织要怎样重建 SDLC」→ 答案是让**工件可交接、gate 可执行、owner 可问责、feedback 可回流**。
