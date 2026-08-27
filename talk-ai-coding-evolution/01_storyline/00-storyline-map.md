# 故事线总图（v1.4 · DSH 生态与控制权稿）

> **官方题目**：OPC 航海指南：OPC 与 Harness，AI 协作之道（OPC = One Person Company，一人公司）。
> 状态：**v1.4**。已校准五层的关系：它们是注意力与工程对象的叠加，不是运行时大小或严格包容关系。落点 = harness + DSH；立场是「从现成开始，但保有 Harness 最终控制权」。
> 五层作为"故事"的解读见 [`05-five-layer-reading.md`](./05-five-layer-reading.md)；harness 里头干啥见 [`06-harness-internals.md`](./06-harness-internals.md)。

## 一句话主线

**模型能力一直在涨，人机互动行为就一直在变**——人从"亲手做"被一步步推成"设计模型怎么做"。
五层描述的是工程注意力逐步上移，不是谁取代谁、谁在图上最大。一人公司要掌握的临界点是
**harness**：先借现成的可靠运行环境；一旦任务要求改模型、工具、执行世界、门禁或知识组织，就必须保有其最终控制权。

**最终控制权在手，不等于全部自建。**它是 owner 对四件事的最后决定权：接入什么、替换什么、何时放行、如何重建发生过的事实；模型、工具、后端与插件都仍可借用。

## 故事弧线（五幕）

| 幕 | 内容 | 作用 | 时间 |
|---|---|---|---|
| 开场 | 钩子 + 一人公司的问题 | 让人对号入座 | 0–3.5 |
| 第一幕 | 五层演变（人机互动一直在变） | 铺路 + 引发共鸣 | 3.5–15.5 |
| 第二幕 | 根本还是 harness（Böckeler + 为什么） | 转折 + 抓要害 | 15.5–25.5 |
| 第三幕 | 固定 vs 灵活 + DSH 的爆发与收益 | 让 OPC 看见真实需求 | 25.5–34 |
| 第四幕 | DSH 的定位 + Harness 最终控制权 | 落点 | 34–39 |
| 收尾 | 带走一句 + 收尾页 | 收束 | 39–45 |

## 每一幕的要点

### 开场（钩子）
- 问题：一个人开公司，AI Coding 到底要掌握到多深？用现成还是自己做？
- 钩子：两年里你的角色一直在变——写 prompt → 挑 context → 搭环境 → 写循环 → 排图。
  你不是在追新工具，你是在被模型一步步往上推。
- **点题焊点**（06 章角色表）：责任的叠加上移不是岗位替代——一个成熟团队要五种角色（prompt 设计师→context 平台→harness SRE→loop 设计师→graph 架构师），
  一人公司就是"被同一个人承担"的极端情况。

### 第一幕：五层演变（铺路）
- **发动机**：模型越强，单次交互的边际工程收益越低，人机互动行为跟着变，人的动作粒度变粗。
- 五层各一句话（人从"亲手做"到"设计别人怎么做"）：
  Prompt（说话者）→ Context（策展者）→ Harness（环境工程师）→ Loop（控制流作者）→ Graph（编排者）。
- **叠加观 + 成熟度标尺**：不是换代，是叠加；前三层成熟、后两层叙事期。
- **关系模型（必须讲准）**：Prompt 是任务表达，Context 是模型所见，Harness 是单次执行的运行与治理边界；
  Loop 是跨运行的反馈控制；Graph 是多节点的任务依赖与协调。Loop 和 Graph 是按任务需要叠加的组织方式，
  Graph 可以在部分节点使用 Loop；每个可执行节点仍在 Harness 中运行。

### 第二幕：根本还是 harness（抓要害）
- **转折**：五层讲完，根本还是 harness——它是五层的"可靠性承载体"。
- **口径**：报告把 Context 与 Harness **并列**为"成熟主体"；"harness 最重要"是我们的判断，
  用三条素材撑（结构线 loop/graph 实例化 harness、哲学线 反馈同源（Sensors→loop）+ 验证梯渗透 + GraphARC 门禁、风险线 2026 CVE），别讲成"报告背书"。
- **定义**：Böckeler —— **Agent = Model + Harness**；harness = 模型之外的一切。
- **harness 里头干啥**（抓要害的讲法）→ [`06-harness-internals.md`](./06-harness-internals.md)：
  一句话「模型给能力，harness 给可靠性」；两套控制（Guides 前馈 + Sensors 反馈，各分 computational / inferential）；
  三个动词 **圈住 / 拦住 / 看清**；六个构件（沙箱、权限、工具协议、验证门禁、可观测性、provenance+CI）。
- **为什么强调这些（必讲透）**：
  1. **可靠性是系统的属性，不是模型的属性**——是"模型 + harness"整体的属性。你买很贵的模型买的是"能力"，
     但"可靠性"是 harness 给出来的。
  2. **确定性优先**——测试 / lint / 类型能复现、能审计，AI 判断不能。能交给机器门禁的，绝不靠模型自觉。
- **06 章机制金句**：「假设下层正确是 bug 的来源；对下层显式验证，是工程成熟的标志。」——解释"为什么最底下的 harness 最关键"。
- **为什么是 harness**：它不是“最高层”，而是每一次动作都绕不开的可靠性边界。Harness 把单次执行做成
  可授权、可验证、可追溯；Loop 把这类反馈跨运行连起来；Graph 把多个节点的依赖、路由与门禁显式化。
  所以没有可靠的 harness，loop 只会更快地放大错误，graph 只会把不可靠的节点组织得更复杂。
- **反面证据**：2026 CVE——执行时授权缺失。护栏若建立在"模型会发出合法工具调用"上，
  工具调用可被伪造时整条链失效。修复：**authorize at execution, not at generation**。

### 第三幕：固定 vs 灵活（抉择，不绝对）
- 一人公司的问题落成一格：**harness 的边界由谁定义、能否在需要时改变？** 这不是"自己做 vs 依赖现成"的二选一。
- **固定 harness（Codex / Claude Code）的好**：开箱即用，沙箱、安全、provenance 都替你设计好；常见任务够用。
- **固定 harness 的边界**：它的扩展边界由产品定义，常见任务已经足够。只有当你要改变自己的模型、工具、
  执行世界、可执行门禁或知识组织，而现成产品没有开放相应合同，才会真的卡住。
  - 灵活挂模型 / 工具（`ctx.llm` adapter + `ctx.tools`，都不必改 loop）
  - 灵活换后端（capability seam：换 fs / subprocess 后端，Consumer 不用改）
  - 灵活挂 skill（把自己沉淀的过程性记忆按需挂进去）
  - 灵活挂 knowledge map（把项目的地图 / 归属 / 正确路径作为一等对象）
  ——若产品未开放相应合同，这些需求就需要等待厂商、绕行，或转向可组合的 harness。
- **DSH 的爆发是一个信号，不是质量认证**：GitHub 在公开后约 14 天达到近 20 万 star；同一生态快照收录 2,286 条插件。它说明 DSH 已成为开发者注意力与扩展分发的入口；不说明插件已经成熟、可信或值得无差别安装。
- **本质（不绝对的说法）**：不是"别用现成"，是"别只能现成"。对 OPC，生态真正的价值是三件事：**省手、敢放手、可复用**。这三件事要求的不只是装插件，还要求 Harness 能执行 owner 的控制。

### 第四幕：DSH（定位与控制权）
- **定位问题**：它不是插件商店、不是一个更强的 Loop、也不是要替代 Codex / Claude Code 的成品 Agent；DSH 是一套**可组合的 Harness runtime**，让插件围绕同一套合同、执行路径和事实记录一起工作。
- **为什么只装插件不够**：一项能力进入模型可见面或真实执行路径，就会改变权限、门禁与可追溯性。可安装不等于可信；插件化也不天然等于安全。
- **因此 Harness 必须在手**：owner 必须能决定接入 / 替换、授权 / 拦截、记录 / 重建。DSH 用 adapter、capability seam、enforced gate 与 append-only session log 使这一点可操作。
- 回扣：灵活 harness 不会替你设计 loop 或 graph；它让这些组织能力能在清楚的合同、门禁与运行记录上组合起来。

### 收尾
- 回答：一人公司要掌握到 **harness 这一层**——不用从零造，但其最终控制权必须在手。
- 带走一句（候选见 04-open-questions）：**装自己的，借现成的。**（推荐，待定）

## 待定（跟进在 04-open-questions.md）

- 带走的一句 slogan 未定。
- 各幕时间预算是否按上表切（详见 03_outline）。
- **无 demo**（内容已满，45 min 放不下）。

## 口径红线 + 内容吸纳

- 引用前必查的口径（260 万 / 6 周 / 50 样本 / 三范式二手 / n=1 / Ng 出处未证实 / "挂 MCP"未出现）→ [`../02_evidence/00-absorption-plan.md`](../02_evidence/00-absorption-plan.md) 第三节。
- 每页进货单（哪页吸哪个锚点 / 金句 / 反转）→ 同上第二节。

## 素材索引（维护中）

- 五层结构与锚点：`../_reference/rawdata_ai-coding-evolution-final/final_v4.md` + `../_reference/rawdata_ai-coding-evolution-final/final_v4/`
- Böckeler 定义（Guides/Sensors + computational/inferential）：`../_reference/rawdata_ai-coding-evolution-final/final_v4/03-2026-harness-era.md`
- 2026 CVE（authorize at execution）：同上，第六节
- DSH 三问 / 三腿 / 可执行门禁：`../_reference/rawdata_dsh-faq-on-digested/07_borrowing-harness-idea/answer.md`
