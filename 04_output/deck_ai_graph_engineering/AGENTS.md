# AGENTS.md — 这场 keynote 的叙事与交付规范

> 2026-10-02 立项（用户定）：本目录的 agent 提供**内容**——两场 keynote 的叙事（入门通识场 `intro/`、技术产品场 `advanced/`）、练习件（`practice/`）与图工程治理手册（`manual/`）。画面、PNG、母版、PPTX 不在本目录的工作范围内；历史稿若有出图脚本，当作停掉的试验，不续做、不修图。
> 整个交付以**图治理四问与两层自愈体系**为核心脊柱，叙事性与调性把控进入每轮打磨的固定考核（见 `WORKFLOW.md` Phase 3）。

---

## 做完的标准

一次内容改动做完，当且仅当下面四条同时成立：

1. **结构**：每一页只推进故事的一步——**一页一个概念**。content 必须写出行数不超过三条，一个页面里出现第二个概念就拆页；页数预算（入门 25+／技术 35+）是下限，宁可加页、加承接页/呼吸页，不硬挤。两场都是平铺单档；追问的答案进备注，不开加深页。
2. **系统**：**图治理四问**贯穿全场——
   - **依赖怎么定？**（固定元图还是动态数据？谁定前后置？）
   - **工件怎么交？**（伪群聊还是强类型 Schema + Worktree 物理隔离？）
   - **失败怎么治？**（L1 局部微循环退避还是 L2 局部子图切片替换？）
   - **人在哪里看？**（哪些关键节点设 Checkpoint 审批？如何优雅熔断与保留现场？）
   四问在开场提出、逐章给答案、收尾回扣。
3. **叙事**：听众能用一句话接上下一页。接不上的页，删或并。
4. **自洽**：各场大纲（`intro/outline/outline-intro.md`、`advanced/outline/outline-advanced.md`）的主张句与该场文稿的 CLAIM 是同一句。上屏的 subtitle 用这一句。研究层与实践层的边界写在讲者备注或 callout，不另起一套主张。

内容权威是大纲，展开在文稿。

**章节与交付**：每章聚焦一个问题，给出听众能带走的判断，再说明为何进入下一章；章首和章末承担定向与回收。最终 PPT Agent 只接收该场 `intro/manuscript/manuscript-intro.md` 或 `advanced/manuscript/manuscript-advanced.md`，所需全场背景、术语、章节地图、逐页洞察与推理、案例前提、关系表达和证据边界集中稿内。大纲与来源链接供维护核验，不是做片的必读依赖。逐页说明须提供具体理解，只有 CLAIM 复述或通用禁令不算知识交付；修后按 `WORKFLOW.md` 的单稿盲审复核。

---

## 项目定位

- **讲的事**：当一个 Agent 干不完长程任务、多角色必须协同推进时，如何用显式图拓扑、强类型工件与状态机治理，消灭失控的群聊与上下文腐败，实现高可靠的 Agentic SDLC。
- **两场分稿**：
  - `intro/` 入门场（**27 页**，60 分钟，面向业务负责人、研发主管、被 Multi-Agent 概念轰炸但落地频频翻车的管理者，主讲**从自由群聊的幻觉走向组织同构与交付契约**）；
  - `advanced/` 技术/产品场（**37 页**，90 分钟，面向正在搭或维护 Multi-Agent 架构的资深工程师与产品经理，放开讲**固定元图、Session 外持久化状态机、L2 子图切片、2026 顶级模型五大病理的机器级防御**）。
  - 脊柱＝从单体 Loop 瓶颈到图工程治理体系：开场痛点 → 图治理四问 → 拓扑/工件/状态机/两层自愈逐层展开 → 机器级防御与熔断 → 终局架构与带走。两场各自 outline → manuscript → practice，互不搬页。
- **三件套分工**：两场 talk 回答「为什么走向图拓扑」与「多节点协作链怎么治理」；听众带走的操作件是本目录 [`manual/图工程与多智能体协作治理手册.md`](manual/图工程与多智能体协作治理手册.md)——单文件双篇（上篇通识诊断层＋下篇工程操作层）。两场收尾页的「带走」指向手册，操作规程不在两场稿里重复。
- **语言**：用自然中文句法说明问题、因果与判断；重要新概念保留英文名称，如 Graph、DAG、State Machine、Artifact、Failure Envelope、Sub-graph Splicing、Worktree、HITL。首现给准确中文解释，后续稳定用法；不为了全中文把概念辨识度译掉，也不把英文句法生搬成中文。术语表置于各场文稿头部。
- **源**：上游两处——研究层 `../../02_research/01_agent_engineering/graph_engineering/`，实践层 `../../03_practice/graph_governance/`。主张不超出它们的成稿：研究层 `result/landscape.md`、9 篇 digested 议题判读、生态实证；实践层 `backbone.md` 与 `manual.md`。本目录是它们的加工下游。

---

## 内容流程

```
素材里哪几句能进故事    →  research/source-synthesis.md
入门场的故事与每页主张  →  intro/outline/outline-intro.md
入门场每页怎么说        →  intro/manuscript/manuscript-intro.md
入门场练什么、怎么判卷  →  intro/practice/（exercises 学员版 + facilitator 讲者卡）
技术产品场的故事与主张  →  advanced/outline/outline-advanced.md
技术产品场每页怎么说    →  advanced/manuscript/manuscript-advanced.md
技术产品场练什么、怎么判卷 →  advanced/practice/（exercises + facilitator）
听众带走的操作件        →  manual/图工程与多智能体协作治理手册.md
每页上屏                →  同场文稿的 title / subtitle / content
```

上屏给后面的做片用——**做片方未必懂 Graph Engineering，写少了会乱发挥**。承重页给完整例子、来源边界和做片说明；callout 必须保留署名/机构与日期。title 短，subtitle 等于主张句，只读二者应能跟上论证。content 是必须保留的最小正文，最多三条；补充推理、例子与机制留在同页备注。

---

## 源材料路径速查

| 想看什么 | 路径 |
|---------|------|
| Graph Engineering 研究全景白皮书 | `../../02_research/01_agent_engineering/graph_engineering/result/landscape.md` |
| 当前研究态 | `../../02_research/01_agent_engineering/graph_engineering/CURRENT.md` |
| 9 篇深度议题判读 | `../../02_research/01_agent_engineering/graph_engineering/digested/` |
| 7 份一手证据档案（KOL/论战/实录） | `../../02_research/01_agent_engineering/graph_engineering/raw/evidence-*.md` |
| LangGraph 与 DeerFlow 生态解剖 | `../../02_research/01_agent_engineering/graph_engineering/harness_langgraph_ecosystem/` |
| 四大前沿 Harness 体系解密 | `../../02_research/01_agent_engineering/graph_engineering/harness_frontier_systems/` |
| Graph 实践主干（backbone §0–§7） | `../../03_practice/graph_governance/result/backbone.md` |
| 操作规程与 Schema（manual §0–§7） | `../../03_practice/graph_governance/result/manual.md` |
| Loop 治理主干（节点微循环对照） | `../../03_practice/loop_governance/` |
| Harness 治理主干（沙箱环境对照） | `../../03_practice/harness_governance/` |

---

## 三条铁律

1. **用户做选择题，你做创造性劳动。** 生成候选方案，让用户选。
2. **闸门不可跳过。** 每个 Phase 结束等用户确认。
3. **源文件是 single source of truth。** 改动永远从 markdown 开始。
