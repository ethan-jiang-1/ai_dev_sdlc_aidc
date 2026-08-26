# 第三幕 · 固定 vs 灵活 —— 逐页内容（P15–P18）

> 对应 `00-page-structure-23.md` P15–P18（8.5 min）。**每节 = 一页现场内容**：上屏文字（标题/正文）+ 讲点素材。
> 素材来源见 `../02_evidence/00-absorption-plan.md` 第二节。立场：不绝对——不是"别用现成"，是"别只能现成"。

---

## P15 抉择（1 min）—— harness 这一格，用固定的还是灵活的？

**上屏文字**
- 标题：harness 这一格：固定，还是灵活？
- 正文：
  - 不是"自己做 vs 依赖现成"的二选一
  - 真正的区别在一条轴：**固定 vs 灵活**
  - 精装公寓 vs 可改造空间

**讲点 / 素材**
- 目的：把一人公司的问题落成具体一格，并明确问题不是"自己做 vs 依赖现成"的二选一。
- 讲点：harness 是承重墙 → 问题落成一格（固定 or 灵活）；不是二选一；区别在一条轴；通俗例子（精装公寓 vs 带标准接口的空间）。
- 转场：先公平地说，固定 harness 到底好在哪。

---

## P16 固定的好（2 min）—— Codex / Claude Code 开箱即用

**上屏文字**
- 标题：固定 harness 的价值：组件随产品交付
- 正文：
  - harness 民主化：沙箱 / 权限 / 可观测性，开箱即用
  - Claude Code 沙箱双重隔离；Copilot 云端沙箱
  - "Start with the simplest viable system." —— Anthropic
  - 绝大多数人，应从现成开始

**讲点 / 素材**
- 目的：公平地讲现成 harness 的价值——它把 harness 组件**民主化**了。
- 讲点：从"自己写 bash 编排"到"组件随产品交付"（Osmani）；Claude Code 沙箱 / Copilot 云端沙箱 / provenance 接 CI 开箱即用；Anthropic 忠告（simplest viable system）；结论：绝大多数人从现成开始。
- 金句："组件随产品交付"——harness 民主化。
- 转场：那卡在哪？卡在你想**改 harness 本身**的时候。

---

## P17 固定的卡（3 min）—— 想改 harness 本身时

**上屏文字**
- 标题：卡住的地方：想改 harness 本身
- 正文：
  - 挂自己的模型 / 工具：厂商支持什么，你才能用什么
  - 换后端：沙箱、工具集定死，没有接口
  - 挂 skill / knowledge map：只能塞进 prompt（context rot：塞得越多记得越差）
  - 补执行时授权？改不了内核，只能等厂商

**讲点 / 素材**
- 目的：讲清固定 harness 的边界——它的 guides/sensors 是写死的、为大众设计的。
- 讲点：写死/为大众设计的本质；四个卡点（挂模型工具 / 换后端 / 挂 skill / 挂 knowledge map）；更硬的证据（2026 CVE 想补执行时授权只能等厂商）；通俗例子（精装公寓改格局走物业流程）。
- 转场：所以问题不是"现成不好"，是"只能现成"不行。

---

## P18 本质（2.5 min）—— 不是别用现成，是别只能现成

**上屏文字**
- 标题：不是别用现成，是别只能现成
- 正文：
  - 灵活 harness = **装自己的 + 借现成的**
  - 装自己的：挂模型 / 挂工具 / 换后端 / 挂 skill / 挂 knowledge map / 自定义门禁
  - 借现成的：成熟 adapter / skill / 模型，直接复用
  - 不逼你二选一

**讲点 / 素材**
- 目的：落到立场——灵活 harness = 装自己的 + 借现成的。呼应 slogan。
- 讲点：立场收束（不是别用现成，是别只能现成）；灵活 harness 两样东西（装自己的 + 借现成的）；不逼二选一；对一人公司的意义（没有团队分摊基础设施，更需要装得下自己、接得上现成）；金句落位。
- 金句：**装自己的，借现成的。**
- 转场：有没有这样一个 harness？有——这就是最后要讲的 DSH。

---

## 本幕素材来源速查

- P16 民主化 / 组件随产品交付：`final_v4/03-2026-harness-era.md` 第二节 + `04-2026-loop-era.md`（Osmani）
- P16 "Start with the simplest viable system"：`final_v4/03-2026-harness-era.md` 第三节（Anthropic Building Effective Agents）
- P17 context rot：`final_v4/02-mid-2025-context-era.md`
- P17 2026 CVE 执行时授权：`final_v4/03-2026-harness-era.md` 第二节
- P18 两线证据（现成的好 + 要能改）：吸纳清单 §二 P16/P17
