# 故事线总图（v1.1 推敲稿）

> 状态：**v1.1**。落点 = harness + DSH；立场软化为「固定 vs 灵活」，不绝对。
> 五层作为"故事"的解读见 [`05-five-layer-reading.md`](./05-five-layer-reading.md)；harness 里头干啥见 [`06-harness-internals.md`](./06-harness-internals.md)。

## 一句话主线

**模型能力一直在涨，人机互动行为就一直在变**——人从"亲手做"被一步步推成"设计模型怎么做"。
这场 talk 要回答一人公司（one person company）的问题：沿着这条往上推的梯子，
**一个人该掌握到多深、哪一格用现成、哪一格要灵活**。答案落在最中间、最承重的那一格——**harness**。

## 故事弧线（五幕）

| 幕 | 内容 | 作用 | 时间 |
|---|---|---|---|
| 开场 | 钩子 + 一人公司的问题 | 让人对号入座 | 0–5 |
| 第一幕 | 五层演变（人机互动一直在变） | 铺路 + 引发共鸣 | 5–20 |
| 第二幕 | 根本还是 harness（Böckeler + 为什么） | 转折 + 抓要害 | 20–30 |
| 第三幕 | 固定 vs 灵活（不绝对） | 一人公司的抉择 | 30–40 |
| 第四幕 | DSH = 灵活 harness 的答案 | 落点 | 40–45 |
| 收尾 | 带走一句 | 收束 | 45–50 |

## 每一幕的要点

### 开场（钩子）
- 问题：一个人开公司，AI Coding 到底要掌握到多深？用现成还是自己做？
- 钩子：两年里你的角色一直在变——写 prompt → 挑 context → 搭环境 → 写循环 → 排图。
  你不是在追新工具，你是在被模型一步步往上推。

### 第一幕：五层演变（铺路）
- **发动机**：模型越强，单次交互的边际工程收益越低，人机互动行为跟着变，人的动作粒度变粗。
- 五层各一句话（人从"亲手做"到"设计别人怎么做"）：
  Prompt（说话者）→ Context（策展者）→ Harness（环境工程师）→ Loop（控制流作者）→ Graph（编排者）。
- **叠加观 + 成熟度标尺**：不是换代，是叠加；前三层成熟、后两层叙事期。
- **埋雷**：harness 是"单次运行容器"，loop / graph 都站在它上面。

### 第二幕：根本还是 harness（抓要害）
- **转折**：五层讲完，根本还是 harness——它是五层的"可靠性承载体"。
- **定义**：Böckeler —— **Agent = Model + Harness**；harness = 模型之外的一切。
- **harness 里头干啥**（抓要害的讲法）→ [`06-harness-internals.md`](./06-harness-internals.md)：
  一句话「模型给能力，harness 给可靠性」；两套控制（Guides 前馈 + Sensors 反馈，各分 computational / inferential）；
  三个动词 **圈住 / 拦住 / 看清**；六个构件（沙箱、权限、工具协议、验证门禁、可观测性、provenance+CI）。
- **为什么强调这些（必讲透）**：
  1. **可靠性是系统的属性，不是模型的属性**——是"模型 + harness"整体的属性。你买很贵的模型买的是"能力"，
     但"可靠性"是 harness 给出来的。
  2. **确定性优先**——测试 / lint / 类型能复现、能审计，AI 判断不能。能交给机器门禁的，绝不靠模型自觉。
- **loop / graph 的地基**：每次 loop 迭代实例化一个 harness；graph 每个 agent 节点跑在自己的 harness 里。
  没有强悍的 harness，loop 只会更贵地犯错（blast radius 更大），graph 只会更乱地通信。
- **反面证据**：2026 CVE——执行时授权缺失。护栏若建立在"模型会发出合法工具调用"上，
  工具调用可被伪造时整条链失效。修复：**authorize at execution, not at generation**。

### 第三幕：固定 vs 灵活（抉择，不绝对）
- 一人公司的问题落成一格：**harness 这一格，用固定的还是灵活的？**（不是"自己做 vs 依赖现成"的二选一）
- **固定 harness（Codex / Claude Code）的好**：开箱即用，沙箱、安全、provenance 都替你设计好；常见任务够用。
- **固定 harness 的卡**：它的 guides / sensors 是**写死的、为大众设计的**。当你想**改 harness 本身**时——
  - 灵活挂 MCP（接自己的数据源 / 工具）
  - 灵活挂 skill（把自己沉淀的过程性记忆按需挂进去）
  - 灵活挂 knowledge map（把项目的地图 / 归属 / 正确路径作为一等对象）
  ——这些在固定 harness 里要么做不到、要么绕。
- **本质（不绝对的说法）**：不是"别用现成"，是"别只能现成"。一个**灵活的 harness** 好就好在
  它既灵活处理各种事，又能 leverage 已有的东西——**自己的装进去，现成的借过来**。

### 第四幕：DSH（落点）
- DSH = 一个**灵活**的 harness：不给你写死的 harness，给你**能改 harness 本身的框架**。
- 它灵活在两个方向：**装自己的**（挂 MCP / skill / knowledge map、自定义可执行门禁）
  + **借现成的**（成熟的 MCP server、skill、模型直接复用）。
- 核心哲学：**Agents follow enforced gates far more reliably than prose conventions.**
- 回扣：一个人用一个灵活的 harness，就把 loop、graph 两格也顺带罩住。

### 收尾
- 回答：一人公司要掌握到 **harness 这一层**——不用从零造，但要能改。
- 带走一句（候选见 04-open-questions）：**装自己的，借现成的。**（推荐，待定）

## 待定（跟进在 04-open-questions.md）

- 带走的一句 slogan 未定。
- 各幕时间预算是否按上表切（详见 03_outline）。
- **无 demo**（内容已满，45–50 min 放不下）。

## 素材索引（维护中）

- 五层结构与锚点：`rawdata_ai-coding-evolution-final/final_v4.md` + `final_v4/`
- Böckeler 定义（Guides/Sensors + computational/inferential）：`rawdata_ai-coding-evolution-final/final_v4/03-2026-harness-era.md`
- 2026 CVE（authorize at execution）：同上，第六节
- DSH 三问 / 三腿 / 可执行门禁：`rawdata_dsh-faq-on-digested/07_borrowing-harness-idea/answer.md`
