# 第二幕 · 根本还是 harness —— 逐页内容（P9–P14）

> 对应 `00-page-structure-23.md` P9–P14（10 min）。**每节 = 一页现场内容**：上屏文字（标题/正文）+ 讲点素材。
> 素材来源见 `../02_evidence/00-absorption-plan.md` 第二节。

---

## P9 转折（1 min）—— 五层讲完，根本还是 harness

**上屏文字**
- 标题：五层讲完，根本还是 harness
- 正文：
  - loop 实例化 harness；graph 节点跑在自己的 harness 里
  - 上层是楼层，harness 是地基
  - 口径：这是我们的判断（报告将 Context 与 Harness 并列）
  - 三条线撑：结构 / 哲学 / 风险

**讲点 / 素材**
- 目的：把注意力从"往上爬"收回到"最底下那层"，制造"等等，关键原来在这"的反转感。
- 讲点：结构事实（loop/graph 都实例化 harness）→ 上层是楼层、harness 是地基 → 五层讲完根本还是 harness。
- 口径：报告把 Context 与 Harness 并列；"harness 最重要"是我们的判断，用三条素材撑（结构 / 哲学 / 风险），不宣称"报告背书"。
- 转场：先看定义——harness 到底是什么。

---

## P10 定义（1.5 min）—— Agent = Model + Harness

**上屏文字**
- 标题：Agent = Model + Harness
- 正文：
  - harness = 模型之外的一切：权限、沙箱、工具、验证、trace、CI
  - 你以为你在用一个聪明的模型，其实你用"模型 + 一整圈系统"
  - 雏形早就在：一个 prompt + 一个 Bash Tool + 一个 Edit Tool

**讲点 / 素材**
- 目的：立住公式，让听众从此用"模型 + 周围一切"的眼光看所有 agent 工具。
- 讲点：Böckeler 定义；harness = 模型之外的一切；大白话（模型 + 一整圈系统）；雏形（2024 SWE-bench 最小脚手架 = 最早的 harness）。
- 金句："The agent has a prompt, a Bash Tool, and an Edit Tool."
- 转场：那 harness 里头到底干什么？Böckeler 把它拆成两套控制机制。

---

## P11 两套控制 + 确定/概率（3 min）—— Guides/Sensors + comp/infer【合并：两套控制 + 分野】

**上屏文字**
- 标题：harness 里头：两套控制，一档分野
- 正文：
  - **Guides**（前馈）：行动前约束——按这个样式 / 必须过 lint / 只能用这些工具
  - **Sensors**（反馈）：行动后喂回——测试挂了 / 用户拒绝 / 退出码非零
  - **computational**（确定性）：测试 / lint / 类型——可复现，可审计
  - **inferential**（概率性）：AI review——意见本身可能错
  - 原则：**能交给确定性的，绝不靠概率性的**
  - Loop 五级验证梯：同一哲学

**讲点 / 素材**
- 目的：harness 的内部骨架 + 设计哲学一起讲——这是"harness 里头干啥"的核心。
- 讲点：Guides / Sensors 两套控制（教小孩做菜比喻：事前规矩 + 事后纠正）；computational vs inferential 分野（npm test vs AI 说不错）；确定性优先原则；渗透到 Loop 五级验证梯。
- 金句：能交给确定性的，绝不靠概率性的。
- 通俗例子：教小孩做菜 / npm test vs AI。
- 转场：把六件套收一收，用三个动词记住 harness 在干嘛。

---

## P12 圈住 / 拦住 / 看清（2.5 min）—— 模型给能力，harness 给可靠性

**上屏文字**
- 标题：三个动词，记住 harness
- 正文：
  - **圈住**：沙箱 + 权限——文件与网络双重隔离（-84% 权限提示）
  - **拦住**：验证门禁——错误在离源头最近的地方就地拦下
  - **看清**：可观测性 + provenance + CI——trace 记下每一步
  - 模型给能力，harness 给可靠性

**讲点 / 素材**
- 目的：让听众用一句话、三个动词记住 harness 的全部职责。
- 讲点：圈住（沙箱+权限，84% 数据）；拦住（验证门禁，就地失败）；看清（可观测性+provenance+CI，能还原）；收束句——模型给能力，harness 给可靠性（可靠性是"模型+harness"系统的属性）。
- 金句：可靠性是"模型 + harness"系统的属性，不是模型自己的属性。
- 转场：那为什么说 harness 是承重墙？

---

## P13 承重墙（1 min）—— loop / graph 都站在 harness 上

**上屏文字**
- 标题：连上层自己的定义，都承认 harness 在底下
- 正文：
  - "Loop sits one floor above the harness." —— Osmani
  - "The harness supplies the engine; loop writes the pilot." —— Macedo
  - GraphARC：plan → check → execute——上层自己在长 harness
  - **假设下层正确是 bug 的来源；对下层显式验证，是工程成熟的标志**

**讲点 / 素材**
- 目的：三条线证明"harness 是五层的承重墙"，呼应第一幕埋的雷。
- 讲点：结构线（Osmani / Macedo + graph 节点跑在自己的 harness 里）；哲学线（GraphARC 确定性门禁 = 上层在长 harness）；机制金句（假设下层正确是 bug 的来源）。
- 转场：上面全是正面论证；反面更直接——2026 年真实出过事。

---

## P14 反面证据（1 min）—— 2026 CVE：authorize at execution

**上屏文字**
- 标题：反面证据：2026 真实事故
- 正文：
  - AWS / Google / Vercel agent 工具触发漏洞
  - 不是 prompt injection：**执行时授权缺失**
  - 攻击者伪造工具调用，无需运行模型
  - 修复方向：**authorize at execution, not at generation**

**讲点 / 素材**
- 目的：用真实安全事件证明 harness 就是可靠性 / 风险所在，给一人公司一个现实理由。
- 讲点：2026-08 三厂商漏洞（CVE 编号）；执行时授权缺失（非 prompt injection）；护栏假设失效；修复方向；对一人公司的意义（只防 generation 不防 execution 就是不完整）。
- 转场：harness 是什么、为什么重要，讲完了。现在回到你——一人公司，这一层你打算怎么办？（进第三幕）

---

## 本幕素材来源速查

- P10 脚手架金句：`final_v4/01-2025-prompt-era.md`
- P11 Böckeler 两套控制 / comp-infer：`final_v4/03-2026-harness-era.md` 第一节
- P12 圈住 / 拦住 / 看清：`../01_storyline/06-harness-internals.md`
- P13 结构线 / 哲学线 / 机制金句：`final_v4/04/05/06` 章（见吸纳清单第二节）
- P14 CVE：`final_v4/03-2026-harness-era.md` 第二节
