# AI-Native 软件研发组织：从产品意图到生产运维的 SDLC 转型之道

本目录是这场 talk 的内容与生产工作区，也是跨对话的项目记忆。故事线与 50 页页面职责已经锁定，P1-P50 已完成中文审校；**v0.11 四张视觉样片已经通过 REVIEW，v0.12 完整稿的整体视觉 REVIEW 未通过，v0.13 完成结构性返工，v0.14 按“图源分界”升级了 7 个视觉主体，v0.15 关闭上一轮 6 个修改项，v0.16 又完成 13 张生成主体修订和 8 张原生精修**。当前进入用户 REVIEW：v0.16 已完成全量渲染、模板保真、占位符和溢出检查，但只有用户明确确认后才算最终视觉门禁通过。

> **总工作规约：先内容，后表现。** v0.7 内容锁已通过，**50 页总页数已定**，作为稳定的生产边界；
> 表现设计服务既定页面职责。完整生产前先过中文编辑门：所有上屏文字、图中标签与讲稿按中文原生句法重写，不把英文句法逐词翻成中文。若表现阶段暴露命题、证据或转场问题，先回写内容源文件，再继续生产。

> 姊妹目录 [`../talk-ai-coding-evolution-opc/`](../talk-ai-coding-evolution-opc/README.md) 针对 **OPC（一人公司）**；
> 本目录只针对 **软件 SDLC 上的跨职能研发与交付组织**。两者共享「五层演变 + DSH」这套**深轴**素材，但**问题、对象、篇幅完全不同**。

**题目**：AI-Native 软件研发组织：从产品意图到生产运维的 SDLC 转型之道。

**主题速记**：`-opc` 问「一个人要把 AI Coding 掌握到多深」；本 talk 问「**软件研发与交付组织要如何重建 SDLC**」。
范围从产品意图、需求与设计，到构建、测试、发布、生产运维；只讨论软件价值流，不外推到销售、市场、客服、财务、人力或一般企业组织设计。
核心命题是把这条交付链重建成「**工件可交接、门禁能执行、责任有人担、结果能回流**」的运行系统。
**篇幅档位 A**：单场加长 Keynote，75–90 min，**50 页已定**。
**独立成篇**：不依赖、不承接 `05_output/deck_ai_sdlc_keynote`（听众不同）。
听众：软件 SDLC 各阶段的决策者——CTO / 技术 VP、产品、架构、平台工程、开发、QA、安全、发布、SRE / 运维负责人。

## 工作区地图

```text
talk-ai-coding-evolution-org-sdlc/
├── README.md                                # 本文件：地图 + 素材说明 + 工作方式
├── AGENTS.md                                # 【agent 手册】harness 的操作步骤 + 规则
├── CURRENT.md                               # 【当前态权威】当前版本、页面实现、QA 与下一步
├── CONTEXT.md                               # 【术语权威】本 talk 的局部 glossary + 禁用混称
├── docs/adr/                                # 难以回退的局部制作决策及理由
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
│   ├── README.md                            #   当前视觉规则入口 + 历史资产索引
│   ├── 01-visual-storyboard-v0.8.md         #   历史视觉分镜 + 八个布局族
│   ├── 02-imagegen-prompts-v0.11.md         #   历史：内生图文、字体同源样片 brief
│   ├── 02-imagegen-prompts-v0.10.md         #   工程素描方向的上一轮记录
│   ├── 02-imagegen-prompts-v0.9.md          #   3D 实体模型方向的历史记录
│   ├── 02-imagegen-prompts-v0.8.md          #   历史探索记录
│   ├── 06-v0.14-review-ledger.md             #   v0.14 逐页 REVIEW 与 v0.15 修改基线
│   ├── 07-v0.15-change-review-ledger.md      #   v0.15 的 6 页变更、来源清理与 QA 记录
│   ├── 08-v0.16-review-feedback-ledger.md    #   v0.15 用户反馈与 v0.16 生产清单
│   ├── 09-v0.16-change-review-ledger.md      #   当前 21 页变更、32/18 实现与 QA 记录
│   ├── experiments/imagegen-v0.8/           #   服务商实验、提示词与候选资产
│   ├── experiments/imagegen-v0.9/           #   3D 实体模型方向的历史实验
│   ├── experiments/imagegen-v0.10/          #   无字工程素描主体实验
│   ├── experiments/imagegen-v0.11/          #   内生图文、PPT 字体参考与最终透明资产
│   ├── experiments/imagegen-v0.13/          #   第一轮完整稿的生成主体
│   ├── experiments/imagegen-v0.14/          #   图源分界升级与 P49 定向可读性修正
│   ├── experiments/imagegen-v0.16/          #   风格基准图、13 张修订主体与最终成片资产
│   ├── samples/v0.8/                        #   第一轮视觉实验（未通过）
│   ├── samples/v0.9/                        #   已否决的 3D 实体模型样片
│   ├── samples/v0.10/                       #   PPT 覆盖标签方式的历史样片
│   └── samples/v0.11/                       #   已通过的内生图文、字体同源样片与 PPTX
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
├── 04_drafts/                               # 口语讲稿 / 生产事实稿；当前为 ppt-text-v0.16.md
└── 05_output/                               # PPTX 交付；当前 REVIEW 对象为 v0.16/
```

> **临时目录约定**：一次性产物放仓库根目录、以 `.tmp-org-sdlc-talk-*` 前缀命名，不入库；版本收口后清理。细则见 [`AGENTS.md`](./AGENTS.md)。

## 两套素材怎么合成

- **宽轴 = 六阶段 SDLC**（`rawdata_anthropic-ai-native-sdlc-playbook.md`）：组织转型的**范围**。
- **深轴 = 五层演变 + Harness**（`rawdata_ai-coding-evolution-final` + DSH 系列）：观察每一步的**外置与控制深度**。
- **咬合点**：playbook 每个 play 都能用五层镜头检查；harness 从「编码这一格的边界」扩为整条软件价值流的共享控制基线。
  逐 play 映射见 [`02_evidence/00-absorption-plan.md`](02_evidence/00-absorption-plan.md)。

一句话：**`-opc` 说「harness 是每一次动作的可靠性边界」；本 talk 说「让共同控制基线覆盖整条 SDLC，同时让领域判断留在明确的责任人手里」。**

## 工作方式

agent 的操作手册在 [`AGENTS.md`](./AGENTS.md)：每次进来先读它，按它定的步骤走、把状态落回源文件。当前做到哪儿、唯一 REVIEW 对象、页面实现和下一步统一看 [`CURRENT.md`](./CURRENT.md)，不要从历史版本文件推断当前状态。
本 talk 的局部术语以 [`CONTEXT.md`](./CONTEXT.md) 为唯一权威来源；讨论、分镜、prompt、样片 REVIEW 和 PPTX 生产都使用其中的词义。用户用词含混或与 glossary 冲突时，先对齐实际所指，再继续制作；新共识立即写回 `CONTEXT.md`。
加工顺序固定为 **故事线 → 证据口径 → 50 页页面职责 → 内容锁定 → 中文编辑 → 视觉样片 → 生产事实稿 → 母版与 50 页 PPTX → 文字/视觉 QA**；
review 若改变了内容，反向同步回上游源文件。

### 权威文件怎样分工

- [`CONTEXT.md`](./CONTEXT.md) 只回答“这些词在本 talk 里是什么意思、哪些叫法容易混淆”。
- [`AGENTS.md`](./AGENTS.md) 只回答“agent 每次按什么顺序工作、必须过哪些门”。
- [`docs/adr/`](docs/adr/) 记录难以回退且存在真实取舍的决定，解释为什么这样定；不承担术语定义或当前状态。
- [`01_storyline/`](01_storyline/) 保存主张、故事线与决策理由；[`02_evidence/`](02_evidence/) 保存来源和可说口径；[`03_outline/`](03_outline/) 保存 50 页页面职责。
- [`_asset/`](_asset/) 保存视觉系统、Image 2 规则、实验、样片和 REVIEW 台账；[`01_storyline/04-open-questions.md`](01_storyline/04-open-questions.md) 保存历史已决事项与待办。

### 新对话怎样接续

不需要依赖旧聊天记录。依次阅读 [`AGENTS.md`](./AGENTS.md)、[`CURRENT.md`](./CURRENT.md)、[`CONTEXT.md`](./CONTEXT.md)、[`01_storyline/00-storyline-map.md`](01_storyline/00-storyline-map.md)、[`01_storyline/07-narrative-thinking.md`](01_storyline/07-narrative-thinking.md)、[`03_outline/00-page-structure.md`](03_outline/00-page-structure.md)。进入表现阶段时再读 [`_asset/README.md`](_asset/README.md)。这些文件共同回答：现在做到哪儿、这里的词是什么意思、为什么讲、对谁讲、50 页怎样推进、视觉为什么这样定、下一步做什么。`01_storyline/04-open-questions.md` 保存历史已决事项与待办，但不替代 `CURRENT.md` 的当前态入口。

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

**v0.11 四张视觉样片已经通过用户 REVIEW**：P1/P42 使用原生主体；P8/P20 的主体内标签、引线和图形由 Image 2 一体构图，中文与英文以实际 PowerPoint 渲染页为字体参考。v0.12 暴露出一条关键失败：不能把“精确关系要可编辑”理解成“绝大多数页面只用基础图元”。失败复盘见 [`_asset/04-v0.12-visual-failure-review.md`](_asset/04-v0.12-visual-failure-review.md)；v0.12 仅作失败基线。当前完整候选稿为 [`05_output/v0.16/AI-Native软件研发组织-SDLC转型-v0.16.pptx`](05_output/v0.16/AI-Native软件研发组织-SDLC转型-v0.16.pptx)。v0.16 将 13 页替换或重生成为 Image 2 主体，并精修 8 张原生页；变更、主体实现和 QA 见 [`_asset/09-v0.16-change-review-ledger.md`](_asset/09-v0.16-change-review-ledger.md)。

## 与 `-opc` 的关系（一句话）

`-opc` 回答「一个人要掌握多深」→ 答案是 **harness**，原则「部件可借，边界自己定」；
本 talk 回答「软件交付组织要怎样重建 SDLC」→ 答案是让**工件可交接、门禁能执行、责任有人担、结果能回流**。
