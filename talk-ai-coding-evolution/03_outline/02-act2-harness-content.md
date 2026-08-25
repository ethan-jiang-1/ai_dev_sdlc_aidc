# 第二幕 · 根本还是 harness —— 逐页内容（现场 P9–P14）

> 对应 `00-page-structure-23.md` P9–P14（10 min）。内部小节编号与分钟为素材锚点，**现场时间以 00-page-structure-23.md 为准**。素材来源见 `../02_evidence/00-absorption-plan.md` 第二节。
> 每页：目的 / 讲点 / 金句 / 通俗例子 / 转场。

---

## S11 转折（1 min）—— 五层讲完，根本还是 harness

- **目的**：把听众注意力从"往上爬"收回到"最底下那层"，制造"等等，关键原来在这"的反转感。
- **讲点**：
  1. 前面把五层往上讲了一遍，好像越往上越新、越炫。
  2. 但请注意一个结构事实：**Loop 每次迭代都会实例化一个 harness；Graph 的每个 agent 节点也各自跑在自己的 harness 里。**
  3. 上面两层是楼上的楼层，而 harness 是每一层都踩着的那个地基。五层讲完，根本还是 harness。
- **口径**：报告把 Context 与 Harness 并列为"成熟主体"；"harness 最重要"是我们的判断——后面三页用三条素材撑（结构 / 哲学 / 风险），不宣称"报告背书"。
- **转场**：先看定义——harness 到底是什么。

---

## S12 定义（1 min）—— Agent = Model + Harness

- **目的**：立住公式，让听众从此用"模型 + 周围一切"的眼光看所有 agent 工具。
- **讲点**：
  1. Böckeler（Thoughtworks 杰出工程师）：**Agent = Model + Harness**。
  2. Harness = "模型之外的一切"——权限、沙箱、工具、验证、trace、CI，全算。
  3. 大白话：你以为你在用一个"聪明的模型"，其实你用的是"模型 + 它周围一整圈系统"。
  4. 这思想早有雏形：2024 年 Anthropic 在 SWE-bench 上故意保持最小脚手架——**"The agent has a prompt, a Bash Tool, and an Edit Tool."** 一个 prompt 加两个工具，就是最早的 harness。
- **金句**："The agent has a prompt, a Bash Tool, and an Edit Tool."
- **转场**：那 harness 里头到底干什么？Böckeler 把它拆成两套控制机制。

---

## S13 两套控制（2 min）—— Guides（前馈）+ Sensors（反馈）

- **目的**：讲清 harness 的内部骨架——这是"harness 里头干啥"的核心。
- **讲点**：
  1. **Guides（引导 / 前馈）**——在 agent 行动**之前**约束它："按这个样式写"、"必须过这个 lint"、"只能用这些工具"。
  2. **Sensors（感知 / 反馈）**——在 agent 行动**之后**把结果喂回去："测试挂了"、"用户拒绝了这个 diff"、"exit code 非零"。
  3. 通俗例子：教小孩做菜。Guides = 事前规矩（先洗手、刀口朝外、火别开大）；Sensors = 事后纠正（尝一口、咸了加水）。一个管"怎么开始"，一个管"怎么修正"。
  4. 没有这两套，等于把一个很聪明的小孩直接丢进厨房——再聪明也会把厨房烧了。
- **转场**：两套控制里，还有一档决定性的区别。

---

## S14 computational vs inferential（1.5 min）—— 确定 vs 概率

- **目的**：讲清"为什么 Böckeler 强调确定性优先"——这是整套设计哲学的要害。
- **讲点**：
  1. 每套控制都分两档：**computational（确定性）** 和 **inferential（概率性）**。
  2. 确定性：测试、linter、类型检查、schema——结果可复现、可审计，你直接信它。
  3. 概率性：AI review、LLM-as-judge——模型给意见，意见本身可能错，你还得判断它判断得对不对。
  4. 所以原则是：**能交给确定性的，绝不靠概率性的。** 确定性优先，模型判断只做兜底。
  5. 通俗例子：`npm test` 全绿 + 类型检查通过 → 可以直接信；AI 说"这代码写得不错" → 你不敢直接信。
  6. 这条原则会一路向上渗透——后面 Loop 章的"五级验证梯"（L1 确定性 → L5 人工）是同一哲学。
- **转场**：把六件套收一收，用三个动词记住 harness 在干嘛。

---

## S15 抓要害（2.5 min）—— 模型给能力，harness 给可靠性；圈住 / 拦住 / 看清

- **目的**：让听众用一句话、三个动词记住 harness 的全部职责。
- **讲点**：
  1. **圈住**（沙箱 + 权限）——让它只能碰该碰的文件、连该连的网、做被授权的操作。Claude Code 沙箱：文件系统 + 网络双重隔离，实测减少 84% 权限提示。
  2. **拦住**（工具协议 + 验证门禁）——把"对错"变成机器可判的关卡，在错误离源头最近的地方就地拦下，而不是等 review 才发现。
  3. **看清**（可观测性 + provenance + CI）——trace / metrics / logs 记下每一步（工具调用、重试、模型步骤、产出），出了问题能还原："它为什么成功 / 为什么循环 / 为什么花太多"。
  4. 一句话收束：**模型给能力，harness 给可靠性。** 你买很贵的模型，买到的是"能力"；"可靠性"是 harness 给出来的——它是"模型 + harness"整个系统的属性。
- **金句**：可靠性是"模型 + harness"系统的属性，不是模型自己的属性。
- **转场**：那为什么说 harness 是承重墙？

---

## S16 承重墙（1 min）—— loop / graph 都站在 harness 上

- **目的**：三条线证明"harness 是五层的承重墙"，呼应第一幕埋的雷。
- **讲点**：
  1. **结构线**：Loop 的定义源自己说——Osmani "Loop engineering sits **one floor above** the harness"；Macedo "The harness supplies the engine; loop engineering writes the pilot."；Graph 每个 agent 节点跑在自己的 harness 里。
  2. **哲学线**：上层自己在长 harness——GraphARC："模型提议一张工作图，一个确定性 checker 放行或拒绝，只有被放行的图才执行。" 跟 Böckeler 的确定性优先是同一套。
  3. **机制金句**（06 章）："**假设下层正确是 bug 的来源；对下层显式验证，是工程成熟的标志。**"——楼盖得越高，地基越不能虚。
- **转场**：上面全是正面论证；反面更直接——2026 年真实出过事。

---

## S17 反面证据（1.5 min）—— 2026 CVE：authorize at execution

- **目的**：用真实安全事件证明 harness 就是可靠性 / 风险所在，给一人公司一个现实理由。
- **讲点**：
  1. 2026-08：AWS、Google（Vertex）、Vercel 的 agent 工具触发漏洞（CVE-2026-18830 / 18236 / 64650 / 64651）。
  2. 关键：这不是 prompt injection，是**执行时授权缺失（missing authorization at execution time）**——工具调用形状的数据被当作权威，攻击者伪造工具调用，**无需运行模型**就触发工具。
  3. 教训：一切护栏如果建立在"模型会发出合法工具调用"这个假设上，当工具调用可以被伪造时，整条验证链失效。
  4. 修复方向：**authorize at execution, not at generation**——审验证点必须能独立于模型判断"工具该不该被执行"。
  5. 对一人公司的意义：你选的 harness 如果只防"模型被诱导"（generation 侧）、不防"工具被绕过"（execution 侧），就是不完整的。这就是"harness 的设计值得你亲自把关"的第一个现实理由。
- **转场**：harness 是什么、为什么重要，讲完了。现在回到你——一人公司，这一层你打算怎么办？（进第三幕）

---

## 本幕素材来源速查

- S12 脚手架金句：`rawdata_ai-coding-evolution-final/final_v4/01-2025-prompt-era.md`
- S13/S14 Böckeler 两套控制：`rawdata_ai-coding-evolution-final/final_v4/03-2026-harness-era.md` 第一节
- S15 圈住 / 拦住 / 看清：`../01_storyline/06-harness-internals.md`
- S16 结构线 / 哲学线 / 机制金句：`final_v4/04/05/06` 章（见吸纳清单第二节）
- S17 CVE：`final_v4/03-2026-harness-era.md` 第二节
