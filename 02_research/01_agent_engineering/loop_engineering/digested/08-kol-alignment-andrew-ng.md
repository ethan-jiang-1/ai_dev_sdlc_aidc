# 08 · KOL 概念对齐：共同大套路与 Andrew Ng 三环

> **问题**：KOL 反复谈的 loop engineering，是否与本主题的停止条件三件骨架、以及 `loop_governance` 的控制轴同指一套东西？重点核对 Andrew Ng 的三环。
>
> **证据范围**：仓内已回源的一手档案，逐字引句见 [`raw/evidence-2026-09-26-a-originators.md`](../raw/evidence-2026-09-26-a-originators.md)、[`raw/evidence-2026-09-26-b-stop-and-scheduling.md`](../raw/evidence-2026-09-26-b-stop-and-scheduling.md) 与 Andrew Ng 素材卡 [`01_seed_reference/loop_engineering/andrew_ng/`](../../../../01_seed_reference/loop_engineering/)。本文做概念校准，不把厂商机制升级成行业效果证据。

## 一、结论先行

**共同“大套路”的最小交集**不是“让 Agent 无限自动跑”，而是：人给出目标或任务 → 系统反复行动 → 将行动结果作为反馈影响下一步 → 某种完成/交还条件终止这段工作。不同作者对反馈的性质和停止的裁判权并未一致。

**长程自主运行通常还要加的控制件**，但不是每位 KOL 共同的最小定义：跨轮状态/进度外置、可机检闸门、硬上限、独立验收、定时/事件调度和升级给人。Ng 所说的真实用户反馈是产品学习环，不是每个 coding loop 必备的内环。

这与本主题现有判读基本对齐，但有一处必须保持边界：**“共同承认需要反馈和终止控制”不等于“共同承认机器闸门、硬上限、独立验收三件骨架的具体实现”**。三件骨架是跨多条一手机制归纳出的工程控制内核，不是每一位 KOL 都明确写出的完整模型。

## 二、Andrew Ng：概念对齐，但抽象层级不同

Andrew Ng 在 2026-06-30 的本人材料中把 loop engineering 讲成三个嵌套的产品构建环（[X 原文](https://x.com/AndrewYNg/status/2071988145667928442)，The Batch 同源版本的核验缺口见素材卡）：

### Loop 1：Agentic Coding Loop

> “Given a product specification and optionally a set of evals … we can have an AI agent write code, test its work, and keep iterating until the code is bug-free and meets its specification.”

> “using a web browser to check what it had built multiple times before getting back to me, without needing my intervention.”

这与我们的**内环**和①机器可核判据高度对齐：规格/评估条件 → 行动 → 环境测试/浏览器反馈 → 修正 → 再跑。它也支持“人从每轮 QA 中退出、转去更高层判断”，但 Ng 这篇没有展开：判据如何防改写、资源耗尽如何降级、谁拥有最终完成判定。

因此，Ng 的 “bug-free and meets its specification” 不能直接当作可部署停止条件；在工程上必须落成可复查的测试、浏览器检查、eval 或其他环境事实。这正是 `stop_conditions` 对概念的硬化，而不是与 Ng 冲突。

### Loop 2：Developer Feedback Loop

Ng 的开发者在看到当前产品后决定功能、UI、用户流程，并据此更新愿景和 Spec；时间尺度是几十分钟到数小时。他将人的持续参与解释为 **context advantage**：

> “So long as the human knows something the AI does not, human-in-the-loop is needed to inject that knowledge into the system.”

这与我们的“人不退出，而是从动作层移到目标、边界、上下文、检查点和升级层”一致。**但它不是自主度等级**：开发者反馈环不是低自治档，外部用户反馈环也不是更高自治档；Ng 按反馈对象和时间尺度分环，我们按控制权、停止资格和调度方式分层。

### Loop 3：External Feedback Loop

朋友试用、Alpha、A/B 测试等慢反馈修正产品愿景与 Spec，再驱动 Loop 1。它与我们强调的“产出通过 ≠ 外部业务结果达成”相容，甚至为后者提供了概念来源：代码/PR/测试通过只代表本轮产出可验，真实业务结果仍须在更慢的外环观测。

**关键判断**：Ng 的三环是“产品学习与规格演化”的总图；不是停止条件三件骨架的替代 taxonomy，也不是 `agentic → goal → scheduled → proactive` 的运行模式阶梯。

## 三、四类来源的共同交集与差异

| 来源 | 主要回答的问题 | 与本仓对齐处 | 不能强行合并处 |
|---|---|---|---|
| Osmani | 如何替代人逐轮 prompt；系统如何取题、分发、检查、记状态、决定下一项 | 反馈、状态外置、停止/继续、人的位置 | 把 loop 放在 harness 之上；不等于 Ng 的产品反馈三环 |
| Claude Code 官方 | 循环按什么模式运行：manual / goal / interval / proactive | 停止条件、评估器、熔断、调度 | 四类是运行模式，不是成熟度，也不是 Ng 的三层反馈对象 |
| LangChain / Runkle | agent、verification、event-driven、hill-climbing 四环 | 反馈验证、事件调度、外层改进 | hill-climbing 改写 harness 与 Osmani “loop 在 harness 上一层”冲突；rubric/LLM judge 不等于确定性闸门 |
| Andrew Ng | AI 编码、开发者判断、真实用户反馈的嵌套产品环 | 内环反馈、人的上下文优势、外部结果回流 | 不展开状态外置、资源熔断、授权、裁判独立性 |

共同交集应收紧为：**系统替人把一轮推进起来，并用反馈改变下一步；长程系统还必须保存状态，并有停止/升级出口。** 不应把各家的环数、外环对象、触发方式或裁判类型拼成一套“统一官方模型”。

## 四、与 `stop_conditions` 三件骨架的逐项校准

### ① 机器可核判据：高度对齐，但 Ng 只给概念级表达

Ng 的 test / browser / eval 对应环境反馈和 ground truth。Huntley 的 back pressure、Anthropic 的 feature list、Claude `/goal` 的 measurable end state + stated check、LangChain 的 deterministic grader，则把它们具体化为逐轮闸门。Ng 没有反对这一层，只是没有深挖。

### ② 硬性资源上限：Ng 未覆盖，不是冲突

Ng 的案例是 Agent 无人介入运行约一小时，但没有给出轮数、时间、花费、拒绝、无进展或过期上限。不能从“可以跑一小时”推导“不需要熔断”；也不能把 Ng 的时长例子写成通用参数。上限属于控制安全包络，是本仓基于 Claude /goal、/loop、auto-mode、失控实录等材料补出的机制层。

### ③ 验收与干活分离：部分对齐，不能过度归因

Ng 说 Agent 测试自己的工作，开发者稍后看产品并作更高层判断。这支持“机器自检 + 人的更高层反馈”两层结构，但不等于独立 verifier 或 reasoning-blind evaluator。独立裁判、判据保护、worktree/进程隔离来自 Anthropic、Claude Code、OpenAI、METR 等另一组证据。

## 五、真正的冲突，必须显式保留

1. **Loop 的外延冲突**：Osmani 说 loop 在 harness 之上；Runkle 把“用 traces 改写 harness”收作第四环。两者都是机制级一手材料，不能宣布已经统一。
2. **停止裁判冲突**：Claude `/goal` 是独立小模型三值判定；Ralph 是故意无限、由操作者看 TODO 凭 taste；LangChain 接受 rubric/agentic grader。共同项只能写“需要某种反馈/终止控制”，不能写成“行业统一由机器验收”。
3. **人的位置不是退出/留任二元选择**：Osmani、Ng、Runkle、OpenClaw 的共同方向是减少逐轮提示或逐动作审批，但人仍在目标、上下文、风险边界、产品判断和升级处。写成 human-out-of-the-loop 会同时违背 Ng 的 context advantage 与官方 auto-mode 的 escalation 机制。
4. **外部反馈不是 coding loop 必需项**：Ng 的 Loop 3 是产品学习环；对一个 bounded coding task，`/goal` 可以独立成立。它应与 coding loop 组合，而不能成为 loop 的最低定义。
5. **反馈不等于质量证明**：Osmani 明确说 `/goal` evaluator 只核 transcript 中的 hard rules、不判内容好坏；Runkle 的 LLM-as-judge 有自身偏差与操纵风险。故“有 feedback loop”不能自动推出“已经正确收敛”。

## 六、对 `loop_governance` 的校准建议（本篇不直接改实践层）

`loop_governance` 应把 Ng 的三环放在**上位产品反馈图**，而把 `stop_conditions` 放在**控制内核**：

```text
外部用户反馈 ─┐
开发者/产品判断 ─┼→ 更新愿景 / Spec / Eval
Agent 编码内环 ─┘       ↓
                 行动 → 环境反馈/验证 → 继续/停止/升级/交人
```

最不宜发生的概念漂移有三种：

- 用 Ng 的 Loop 2/3 去命名自主度档位；
- 用 Ng 的“bug-free”替代可核停止条件；
- 用 LangChain 的四环或 Ng 的三环抹平 harness / loop / 外部结果的边界。

**最终对齐句**：

> Ng 解释“反馈在哪些时间尺度和决策层回流”；Osmani/Claude Code 解释“系统如何替人推进下一轮”；`stop_conditions` 解释“这套推进机制靠什么不提前宣布完成、不无限烧资源、不让干活者单独当裁判”；`loop_governance` 负责把这些控制决策接成可操作的继续、停止、升级和交接制度。

这四者是互补关系，不是同一套 taxonomy；目前没有证据证明它们在外延上已经完全收敛。
