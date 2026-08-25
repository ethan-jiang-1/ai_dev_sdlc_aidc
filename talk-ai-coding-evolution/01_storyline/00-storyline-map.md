# 故事线总图（v0 草案，待推敲）

> 状态：**草案**。这一页是故事线的"地图"，不是定稿。推敲就是在这张图上改。
> **已确认主题约束（2025-08 更新）**：talk 的更大主题是 **一人公司（one person company）**：
> 一个人要真正熟练掌握 AI Coding 工具，**掌握到什么深度？依赖现成还是自己做？**
> 五层演变 + DSH 都是回答这个问题的素材。**本页 v0 弧线需要按这个主题整体重推敲**（用户指定回头专门谈）。

## 一句话弧线

AI Coding 的工程注意力在过去两年经历了五级跳迁：**Prompt → Context → Harness → Loop → Graph**。
每一次跳迁都不是取代上一层，而是**叠加**——驱动机制始终是同一个：
**模型越强，单次交互的边际工程收益越低，工程杠杆点就往上移一层。**

## 幕结构（对应五层）

| 幕 | 层 | 时间 | 工程对象 | 故事角色 |
|---|---|---|---|---|
| 开场 | Prompt Engineering | 2025 初 | 提示词本身 | 地基层：人人都能写，很快不够用 |
| 第一幕 | Context Engineering | 2025 中起 | 模型看到什么 | 成熟主体一：context rot、量化机制 |
| 第二幕 | Harness Engineering | 2026 起 | 模型周围的系统（Agent = Model + Harness） | 成熟主体二：沙箱/工具协议/验证门禁/provenance；2026 安全事件风险面 |
| 第三幕 | Loop Engineering | 2026 中 | 多轮运行回路 | 新兴层：定义才几周就爆火（低置信度） |
| 第四幕 | Graph Engineering | 2026 7/8 月 | 多 agent 协作图 | 新兴层："Loop 才火了六周"就被接棒（更低置信度） |
| 收尾 | 叠加上升 / **DSH** | 现在 | 一个 flexible harness 罩住 harness/loop/graph 三层 | 落到一人公司的答案上 |

## 想传达的核心信息（候选，待定）

1. **叠加观**：讲 AI Coding 时"新范式取代旧范式"是错的——五层同时活在 2026 的成熟系统里。
2. **杠杆点机制**：一个可预测的规律（模型能力 → 边际收益 → 注意力上移），比罗列新词更有记忆点。
3. **成熟度校准**：前三层是今天生产的主力；Loop/Graph 还在叙事期，别把"火了六周"当定论。
4. **Harness 是承重墙**：安全事件、可靠性都集中在这一层——"Agent = Model + Harness"。

## 待推敲的关键问题（详见 04-open-questions.md）

- 听众是谁？要带走**一个**什么信息？（决定弧线怎么取舍）
- 五层全讲，还是重点讲前三层、Loop/Graph 只作展望？
- DSH 实证案例（rawdata ②）嵌在第二幕，还是作为全篇的"活例子"贯穿？
- 收尾落在"下一步往哪走"，还是落在"怎么判断一个层成熟了没"？

## 素材索引（后续填充时维护）

- 五层结构与锚点：`rawdata_ai-coding-evolution-final/final_v4.md` + `final_v4/`
- Harness 定义（Böckeler，"Agent = Model + Harness"）：`rawdata_ai-coding-evolution-final/final_v4/03-2026-harness-era.md`
- DSH 实证（根入口文档、SDD、借鉴三条腿）：`rawdata_dsh-faq-on-digested/`（01–07）
