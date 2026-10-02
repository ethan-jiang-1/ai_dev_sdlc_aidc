# WORKFLOW — 这场 keynote 的叙事流程

> 本目录的 agent 只写内容。页、画面、PNG、PPTX 不在此流程里。
> 范围以 `AGENTS.md` 的规定为准。
> 本场以**图治理四问与两层自愈体系**为主脊柱；新增消灭群聊、双轨元图与 2026 SOTA 模型机器级防御等硬核抓手；**叙事性=调性把控**，进入每轮打磨的固定考核（见 Phase 3）。

---

## 内容怎么往前走

```
素材里哪几句能进故事    →  research/source-synthesis.md
入门场的故事与每页主张  →  intro/outline/outline-intro.md
入门场每页怎么说        →  intro/manuscript/manuscript-intro.md
入门场练什么、怎么判卷  →  intro/practice/（exercises + facilitator）
技术产品场的故事与主张  →  advanced/outline/outline-advanced.md
技术产品场每页怎么说    →  advanced/manuscript/manuscript-advanced.md
技术产品场练什么、怎么判卷 →  advanced/practice/（exercises + facilitator）
听众带走的操作件        →  manual/图工程与多智能体协作治理手册.md（单文件双篇）
```

做完的标准是 `AGENTS.md` 的四条：结构（**一页一概念**）、系统（**图治理四问**）、叙事、自洽。页数预算是下限：入门 25+／技术 35+，宁可拆页加承接/呼吸页，不硬挤。

---

### Phase 0 — 素材合成（research/）

**你在哪个目录工作**：`research/`

**素材来源**：

| 来源 | 提供什么 |
|---|---|
| `02_research/01_agent_engineering/graph_engineering/result/landscape.md` | 综述全景白皮书（定调与架构模型） |
| `02_research/01_agent_engineering/graph_engineering/digested/` | 9 篇深度议题判读（双轨架构、两层自愈、Session内外、工件黑板、模型病理防御等） |
| `02_research/01_agent_engineering/graph_engineering/raw/evidence-*.md` | 7 份一手回源档案（Steinberger 论战、Raven A2A、LangGraph/Temporal 实战等） |
| `02_research/01_agent_engineering/graph_engineering/harness_langgraph_ecosystem/` | LangGraph 动态原语、DeerFlow 2.0 源码实证、GPT Researcher Map-Reduce 标杆 |
| `02_research/01_agent_engineering/graph_engineering/harness_frontier_systems/` | Claude Code, DeepSeek dsh, OpenAI Codex, OpenHands 四大体系解密 |
| `03_practice/graph_governance/result/backbone.md` | 实践主干（双轨元图/外部状态机/工件契约/L2切片/HITL熔断） |
| `03_practice/graph_governance/result/manual.md` | 操作规程 8 节（诊断表/Schema/切片SOP/防线配置/落地梯子） |

**产出**：`research/source-synthesis.md`

**⛔ 闸门**：信号抽取准确、无重大遗漏 → 进入 Phase 1

---

### Phase 1 — 叙事大纲（intro/outline/ 与 advanced/outline/）

**产出**：`intro/outline/outline-intro.md` 与 `advanced/outline/outline-advanced.md`（两场各自过闸）

**内容规范**：

```
1. 开场故事与核心判断（从自由群聊的幻觉，转到组织同构与交付契约；单体 Loop 无法承担长程复杂任务）
2. 图治理四问（贯穿全场：依赖怎么定、工件怎么交、失败怎么治、人在哪里看）
3. Narrative Arc（叙事弧：只读 title+subtitle 应能复述）
4. 页面清单（每页 title + 一句话主张；一页一个概念；承接/呼吸页标出）
5. 架构与控制双路落点（状态机推进基建 / 人的审批把关门禁，各在哪些页承重）
6. 语言纪律（本场红线、术语档、比喻标注）
```

**⛔ 闸门**：隐喻精准非“差不多”、故事只立不贬、递进清晰、四问贯穿 → Phase 2

---

### Phase 2 — 完整文稿（intro/manuscript/ 与 advanced/manuscript/）

**产出**：`intro/manuscript/manuscript-intro.md` 与 `advanced/manuscript/manuscript-advanced.md`（该场大纲过闸后逐场展开）

每张 slide 展开为：所属章节 ＋ 主张句（与大纲相同）＋ 上屏（title / subtitle / content，**content ≤3 条**）＋ 观点推理与例子 ＋ 做片说明 ＋ 接到下一页。subtitle 等于主张句。

**单稿交付**：PPT Agent 只收到该场 `manuscript-*.md`。全场背景、听众、重要术语解释、章节问题／收获／转场、节奏与练习表达方式都写在该稿内。每页做片说明交付具体知识：听众理解怎样变化、观点为何成立、案例支持到哪、图中必须表达的关系及容易误画的关系。

**⛔ 闸门**：主张句与大纲相同，通读能接上下一页，无超载页。

---

### Phase 3 — 调性与叙事的把控（每轮打磨的固定考核）

| 维度 | 考什么 | 具体标准 |
|---|---|---|
| **系统性** | 图治理四问是否贯穿 | 四问在开场提出、逐章给答案、收尾回扣 |
| **结构性** | 章节聚焦、一页一概念、承接/呼吸 | 每章有核心问、带走判断与下一章理由；content ≤3 条；章首定向、章末回收 |
| **一致性** | CLAIM = 大纲主张句 | 逐页比对一致，subtitle 用同一句 |
| **自洽性** | 主张不超上游 | 每条主张能指到 landscape / backbone / manual / digested；参数与机制带锚 |
| **叙事性（调性）** | 它是不是一个好故事 | ①承诺-回收：开场痛点收尾必须闭环；②逐页交接：一句话承接成立；③一线贯穿：消灭伪群聊与两层自愈反复深化；④呼吸节奏：难点后有呼吸页；⑤无孤儿概念 |

**单稿盲审**：用独立 Agent 只读单份稿，不提供大纲与背景。检验其能否完全还原全场论证、章际转折与做片图示关系。

**⛔ 闸门**：五维复核 ＋ 单稿盲审通过。
