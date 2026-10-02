# AGENTS.md — 这场 keynote 的叙事

> 2026-09-27 用户定：本目录的 agent 提供**内容**——两场 keynote 的叙事、练习件（practice/）、循环交接手册（manual/）。画面、PNG、风格母版、PPTX 仍不在此范围内；那些文件若已存在，当作停掉的试验，不续做、不修图。
> 2026-10-01 用户定：两场以**阶梯脊柱**完全重排（开场故事→定档→逐级交决定配护栏→高手错觉收尾）；叙事性＝调性把控，进入每轮打磨的固定考核（见 `WORKFLOW.md` Phase 3）。

## 做完的标准

一次内容改动做完，当且仅当下面四条同时成立：

1. **结构**：每一页只推进故事的一步——**一页一个概念**（2026-10-01 用户定）：content 必须写出行数不超过三条，一个页面里出现第二个概念就拆页；页数预算（入门 20+／技术 30+）是下限，宁可加页、加承接页/呼吸页，不硬挤。两场都是平铺单档；追问的答案进备注，不开加深页。
2. **系统**：**定档四问**贯穿全场——谁启动下一轮、谁判断完成、谁能改变系统、出了错谁能停下接手；四问在开场提出、逐档给答案、收尾回扣。多出来的页要写明它服务哪一问（或哪条反馈线）。
3. **叙事**：听众能用一句话接上下一页。接不上的页，删或并。
4. **自洽**：各场大纲（`intro/outline/outline-intro.md`、`advanced/outline/outline-advanced.md`）的主张句与该场文稿的 CLAIM 是同一句。上屏的 subtitle 用这一句。研究层的边界写在讲者备注或 callout，不另起一套主张。

内容权威是大纲，展开在文稿。

**章节与交付（用户本轮定）**：每章聚焦一个问题，给出听众能带走的判断，再说明为何进入下一章；章首和章末承担定向与回收。最终 PPT Agent 只接收该场 `intro/manuscript/manuscript-intro.md` 或 `advanced/manuscript/manuscript-advanced.md`，所需全场背景、术语、章节地图、逐页洞察与推理、案例前提、关系表达和证据边界集中稿内。大纲与来源链接供维护核验，不是做片的必读依赖。逐页说明须提供具体理解，只有 CLAIM 复述或通用禁令不算知识交付；修后按 `WORKFLOW.md` 的单稿盲审复核。

## 项目定位

- **讲的事**：你离开之后它继续跑，你回来时它说做完了。整场回答你凭什么信。
- **两场分稿（2026-09-27 定，2026-09-28 控制链重构，2026-10-01 阶梯脊柱完全重排，2026-10-02 讲感打磨）**：`intro/` 入门场（**27 页**＋判断档三题，60 分钟，没跑过循环的通识听众，业务与管理为主）；`advanced/` 技术/产品场（**37 页**＋构造档三题，90 分钟，在跑循环的工程师与产品，机制放开讲）。脊柱＝capability_ladder 交接面：开场故事（系统接替逐次提示→「写 loop」）→ 定档四问 → 按交接面交决定配护栏 → 高手错觉收尾。基线不算已交动作；阶梯是教学顺序，真实系统三个交接面分别核查，不由 `/loop` 推断前两面成立。两场各自 outline → manuscript → practice，互不搬页。讲感打磨依据 `craft/讲感写作要求.md`（2026-10-02 立）。
- **三件套分工**：两场 talk 回答「凭什么信」与「链怎么治理」；听众带走的操作件是本目录 [`manual/循环交接手册.md`](manual/循环交接手册.md)——单文件双篇（卷首语汇权威＋入门篇判断层＋高级篇操作层，2026-09-30 立项、合册并移入本目录）。两场收尾页的「带走」与练习的「回去照着做」全部指向手册，操作规程不在两场稿里重复——talk 是手册的叙事上游，不是它的第二权威。
- **语言（用户本轮重申）**：用自然中文句法说明问题、因果与判断；重要新概念保留英文名称，如 Loop、Agent、Harness、Goal、Eval、Feedback。首现给中文解释，后续稳定用法；中文解释须准确，不为全中文把概念辨识度译掉，也不把英文句法搬成中文。术语表在各场文稿头部，讲清与相邻概念的区别，不只给中英对照。
- **源**：上游两处——研究层 `../../02_research/01_agent_engineering/loop_engineering/`，实践层 `../../03_practice/loop_governance/`。主张不超出它们的成稿：研究层 `result/landscape.md`（§3.5 交接面）与 `capability_ladder/00-map.md`＋`result-reliability-interface.md`；实践层 `backbone.md` 与 `manual.md`（§0–§13）。本目录是它们的加工下游；核出处时读两个上游各自的 README。

## 内容流程

```
素材里哪几句能进故事    →  research/source-synthesis.md
入门场的故事与每页主张  →  intro/outline/outline-intro.md
入门场每页怎么说        →  intro/manuscript/manuscript-intro.md
入门场练什么、怎么判卷  →  intro/practice/（exercises 学员版 + facilitator 讲者卡）
技术产品场的故事与主张  →  advanced/outline/outline-advanced.md
技术产品场每页怎么说    →  advanced/manuscript/manuscript-advanced.md
技术产品场练什么、怎么判卷 →  advanced/practice/（exercises + facilitator）
每页上屏                →  同场文稿的 title / subtitle / content
```

上屏给后面的做片用——**做片方未必懂 loop engineering，写少了会乱发挥**。承重页给完整例子、来源边界和做片说明；callout 必须保留署名/机构与日期，原句或节选意译在同页备注可复核。教学映射、设计建议与产品机制分开标注，避免把出处当成效果证明。title 短，subtitle 等于主张句，只读二者应能跟上论证。content 是必须保留的最小正文，最多三条；补充推理、例子与机制留在同页备注，做片 Agent 按注明的关系表达，不自行添加另一档正文。知识说明不上屏，按页讲清理解变化、推理关系、案例前提与可推断范围、图中必要关系和具体误画原因；短字幕的限定可由正文承接，但不能漏掉。个别难点页加一句 callout 点睛（自造金句，或已回源复核的署名引语），放页角或底部一行；未复核引语照旧不上屏。红、绿、灯只允许出现在引用块里。本目录仍不出 PPTX、PNG、风格母版。

**练习件与上屏分开（2026-09-30 增）**：practice/ 是新的工件类型，不是页面——不进 title/subtitle，不改任何页的 CLAIM。学员版（exercises）对外自足：不出现内部路径、研究层/实践层命名与代号，数值标教学示意；讲者卡（facilitator）可带内部 evidence 指针，供回源自查。每题答案可核对或给出合格线，不设无锚开放题。技术场操作题限定可回滚环境，并备纸面降级版。

改故事先改该场的大纲，再改该场文稿，使两处的主张句重新相同。

## 源材料路径速查

| 想看什么 | 路径 |
|---------|------|
| Loop Engineering 研究全景 | `../../02_research/01_agent_engineering/loop_engineering/README.md` |
| 当前研究态 | `../../02_research/01_agent_engineering/loop_engineering/CURRENT.md` |
| KOL 台账（6 位核心） | `../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md` |
| 12 份回源档案（逐字引句） | `../../02_research/01_agent_engineering/loop_engineering/raw/evidence-*.md` |
| 命名谱系判读 | `../../02_research/01_agent_engineering/loop_engineering/digested/01-命名谱系.md` |
| 构件判读 | `../../02_research/01_agent_engineering/loop_engineering/digested/03-构件.md` |
| 控制问题矩阵 | `../../02_research/01_agent_engineering/loop_engineering/digested/07-控制问题矩阵.md` |
| 实践主干（backbone 7 节） | `../../03_practice/loop_governance/result/backbone.md` |
| 操作规程（manual 13 节，2026-09-30 增 §13 授权面） | `../../03_practice/loop_governance/result/manual.md` |
| goal/eval 构造 | `../../02_research/01_agent_engineering/goal_eval_engineering/` |
| 讲感写作要求（manuscript 怎么写好讲，2026-10-02 立） | `craft/讲感写作要求.md` |
| harness 治理（环境轴对照） | `../../03_practice/harness_governance/` |
| Andrew Ng 消化稿 | `../../02_research/01_agent_engineering/loop_engineering/digested/kol/andrew_ng.md` |
| Andrew Ng 素材卡 | `../../01_seed_reference/reference/kol/_raw_loop_engineering/andrew_ng/` |
| 边界判定 | `../../02_research/01_agent_engineering/loop_engineering/digested/05-边界判定.md` |

## 故事在哪

各场的顺序、公式落页、口播不说轮数，以该场大纲为准。下面这些是研究层的材料索引，不是幻灯片目录。不要按这个清单把故事改回题目摊开。

| 被追问时才翻 | 路径 |
|---|---|
| 两判据、十种失败、停止三件 | `../../03_practice/loop_governance/result/backbone.md` |
| 哪些已经有公开办法、哪四列是空的 | `../../02_research/01_agent_engineering/loop_engineering/result/landscape.md` |

## 三条铁律

1. **用户做选择题，你做创造性劳动。** 生成候选方案，让用户选。
2. **闸门不可跳过。** 每个 Phase 结束等用户确认。
3. **源文件是 single source of truth。** 改动永远从 markdown 开始。

## 前置条件（Phase 0 之前须满足）

- [x] backbone + manual 用户逐段确认（记录在 `03_practice/loop_governance/CURRENT.md`）
- [x] 研究层 `result/landscape.md`（2026-09-27）
- [x] 听众 / scope / 语言：见 `project-metadata.yaml` 与 outline §6

## 当前稿

内容稿在各场的大纲和文稿。画面、PPTX、出图脚本已按用户要求删除，不重建。

| 稿 | 状态 |
|---|---|
| `research/source-synthesis.md` | 素材参照；已补承重来源落位、非统一阶梯与参数边界，叙事仍以两场大纲为准 |
| `intro/outline/outline-intro.md` | **六章、27 页、60 分钟**；每章问题／收获／回扣／转场明确，基线＋三交接面保留；待排练 |
| `advanced/outline/outline-advanced.md` | **七章、37 页、90 分钟**；分页贯穿、分面门禁、可选支线，章际关系与短导航明确；v5 讲感打磨同步（B06/B07 重构、B20 呼吸页、B37 带走页）；待排练 |
| `intro/manuscript/manuscript-intro.md` | **入门场唯一制作输入**；背景、术语、六章地图、27 页具体知识说明与三题最小题面内嵌；title/CLAIM/subtitle 与大纲同步，4 处署名上屏 |
| `advanced/manuscript/manuscript-advanced.md` | **技术场唯一制作输入**；背景、术语、七章地图、37 页具体知识说明与三题最小题面内嵌；title/CLAIM/subtitle 与大纲同步，9 处署名上屏；附录为不上屏补充。v5 讲感打磨（2026-10-02）：B06 合并为「限制要落在执行层」、B07 改授权漂移现象页、B16 升 promptfoo 反例、B15/B27 subtitle 分拣、新增 B20 呼吸页（四问小结，B20–B36 顺移 B21–B37）、新增 B37 带走页；8 页 content 改事件先行；单稿盲审修复；KOL callout 9 处；37 页 CLAIM=大纲=subtitle 脚本核验一致 |
| `intro/practice/`（README＋exercises＋facilitator） | 三种判断题，嵌 N14/N26/N27；答案位置打散，批处理前提与 flaky 停止候选明确，教学数字不可抄生产 |
| `advanced/practice/`（README＋exercises＋facilitator） | 构造题嵌 **B14/B18/B32**：先目标、再负例、再分面申请；含控制路径演练，纸面产出不算上线资格 |
| `manual/`（`循环交接手册.md`＋AGENTS＋README） | 单文件双篇，逐面审计、契约自足、验收签认、取消三面核对；当前细节见其 `AGENTS.md` |

**当前持续 Goal（v5 讲感打磨已收口，待用户闸门确认与排练）**：按 `craft/讲感写作要求.md` 对技术场做讲感打磨（2026-10-02，用户定「做正确的事、多轮打磨」）。实际审查问题与修订：①B06＋B07 是同一讲拍拆成的两页，合并为「限制要落在执行层」（Cursor 引句降 callout）；②B07 槽位改造成授权漂移现象页（issue #95749 自 B08 上移），第 2 章成为现象→机制→验证顺序；③第 4 章现象先行：B16 升 promptfoo fail-open 反例（官方文档原话上屏）；④B15/B26 subtitle 防御句分拣（修正错误信念的否定句留屏、自保限定下沉，大纲同步）；⑤新增 B36 带走页（逐面门禁三行，35→36 页）；⑥8 页 content 改事件先行（B02/B09/B18/B25/B27/B30/B32/B34），B35 超长行拆薄；⑦单稿盲审（独立 Agent 只读单稿）确认主线完整、无整页失焦，修复其全部发现：上屏钩子 B02/B16/B24/B29、B36 括号页号改自足描述、B06 页块内档案编号移回追问卡、备注层 10 处人名/术语身份补齐（Kief Morris、METR、LangGraph RemainingSteps、Ralph 等，均回源核实）；⑧KOL 金句 callout 增补 3 页（B20 Anthropic premature victory、B32 Carlini 验证器警告、B34 Osmani taste/judgment，均有库内逐字锚），总 callout 9/36 页。36 页 CLAIM=大纲=subtitle 脚本核验一致；content 全员 ≤3 条；稿内层一字未减。轮5 补充（用户定「加呼吸页」）：新增 B20「续跑面的四问答案」呼吸页（呼吸＋续跑面四问收口，B20–B36 顺移为 B21–B37，总 37 页），预算改 讲63＋练23＋缓冲4；各章回扣句经判断保留口播（金句上屏由 9 处 KOL callout 与 B37 承载）；仓库提交等打磨全部完成后统一处理。仍需人判断的边界：ch4–ch5（B15–B23）连续重页区是排练密度检验点，若排练过载则在 B19 后加呼吸页；B12/B32 两处轻度跨页承诺保留（由 B14 与 B33 独立验收兑现）；KOL callout 的现场效果待真实听众验证。

**v5 轮五维复核**：系统性（四问 B04 提出→B32 逐面→B36/B37 回收）与叙事性（承诺-回收、逐页交接）经独立盲审还原确认；结构性（37 页 content 全员 ≤3 条）与一致性（CLAIM=大纲=subtitle）脚本核验一致；自洽性——新增主张（漂移现象、门禁三行、promptfoo 反例）均有库内 evidence 锚。历史轮（2026-10-01）：保留阶梯脊柱与 27/35 页；修掉基线编号错位、公开报告事故化、三账串成状态机等。

**仍需人判断的边界**：60/90 分钟为可加总的分段预算，尚未现场排练；手册新版阅读手感与实践规程 §13 仍待用户复核。配置与失败路径未接真实产品运行器执行，本轮验证是内容、来源与静态一致性；仓库改动未提交。后续优先以排练反馈调节奏，再改同场大纲／文稿，不能从「校验通过」推断效果收益或用户签认。
