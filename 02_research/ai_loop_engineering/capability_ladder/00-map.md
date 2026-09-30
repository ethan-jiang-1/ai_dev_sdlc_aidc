# 00-map — 交接面与证据对照（本区教学判定权威）

> 观测：2026-09-30。这里判定的是**哪些交接面有一手机制支撑、怎样教更不易误解**，不判定行业采用率或效果。逐字材料留在 [evidence-a](../raw/evidence-2026-09-26-a-originators.md)、[evidence-b](../raw/evidence-2026-09-26-b-stop-and-scheduling.md)、[evidence-c](../raw/evidence-2026-09-26-c-autonomy-and-convergence.md)、[evidence-u](../raw/evidence-2026-09-30-u-post-june-kols.md)；本区各档只作教学切片。

## 一、先拆轴，再数阶

| 原始来源 | 来源实际在分什么 | 在本区可支持什么 | 不可推出什么 |
|---|---|---|---|
| Osmani / Claude Code 团队四类循环（[evidence-a D3](../raw/evidence-2026-09-26-a-originators.md)） | turn-based → goal-based → time-based → proactive：**谁启动下一轮、何时启动** | 只支持 R0 的逐次提示 → R2 的目标续跑 → R3 的定时/事件唤醒这条**启动轴**；R1 动作授权另由审批机制支撑 | 四类不含 R1 授权级，也不含“多代理编排→自动改 harness”的后续两阶 |
| Cursor 运行模式与 `/loop`（[evidence-u S4](../raw/evidence-2026-09-30-u-post-june-kols.md)） | 动作审批与唤醒机制 | R1 的授权边界、R3 的定时/事件唤醒 | 审批模式本身不会替人定义完成条件 |
| Runkle 四环（[evidence-b §4e](../raw/evidence-2026-09-26-b-stop-and-scheduling.md)） | agent / verification / event-driven / hill-climbing：**环的功能类型** | R2 的验证、R3 的事件、元循环支线的改写对象 | 功能类型不是每位学习者必经的权限等级 |
| Morris 四位置（[evidence-c §问题3.1](../raw/evidence-2026-09-26-c-autonomy-and-convergence.md)） | 人在环外/环内/环上，以及代理参与改进的 flywheel | 元循环支线“人改 harness → 代理提案 → 有条件地自动应用”的区别 | “人亲自改”不是“代理已获自改权”；Morris 与 Böckeler 同属 Thoughtworks，不计两家独立机构 |
| Ng 三环（[digested/08](../digested/08-kol-alignment-andrew-ng.md)） | 编码、开发者反馈、外部反馈的**时间尺度** | 反馈可以从环境/产品回到方向选择 | 外环不自动等于工具授权、定时触发或代理自改 |
| 中文视频三层（[evidence-t](../raw/evidence-2026-09-30-t-shenmejiaoqq-video-zh.md)） | 下游传播组织法，文字稿未对音频核验 | 对照叙事遗漏与失真 | 不进入定阶计票，也不作为机制的一手票 |

因此旧版“5/6、6/6 落位”撤回：它把不同类型学、传播材料与独立机制放进同一分母；语义可映射不等于原作者主张相同的阶序。[Lulla 等综述 §3 O3](https://arxiv.org/html/2608.21884v2)也明确指出部分灰文献互相承袭，不能按文章数直接计独立票。

## 二、教学结构：三段主线＋两条可选支线

**R0 是反面起点，不是“无工具的 Agent”**：人逐次发起下一项工作和检查结果，单次 agent 调用仍可自行用工具；它与 R1 的区别在于**动作授权怎样处理**，与 R2 的区别在于**谁负责启动下一轮**。

| 位置 | 交出去的决定 | 可回源机制（独立机构/不同机制，不作“行业共识票数”） | 人保留与升档检查 | 判定 |
|---|---|---|---|---|
| **R1 单次运行的有界执行** | 授权范围内的工具动作，不再逐动作手工审批 | Cursor allowlist / 沙箱 / 分类器（[evidence-u S4a](../raw/evidence-2026-09-30-u-post-june-kols.md)）；Claude Code auto mode deny-and-continue（[evidence-b §4b](../raw/evidence-2026-09-26-b-stop-and-scheduling.md)）；Codex 授权门（[evidence-f](../raw/evidence-2026-09-27-f-autonomy-gates.md)） | 划定动作/目标/时间边界，保留随时中断与高风险审批；不把“测试门”误作授予工具权的普遍前提 | **主线：机制已证** |
| **R2 有界目标续跑** | 当前轮后是否再开下一轮，由目标条件与停止策略驱动 | Claude Code `/goal`（[evidence-b §4a](../raw/evidence-2026-09-26-b-stop-and-scheduling.md)）；Osmani 的可度量任务实例（[evidence-a](../raw/evidence-2026-09-26-a-originators.md)） | 目标、检查、约束、预算、无进展出口；独立完成检查**不等于**独立质量验收。Anthropic quickstart [evidence-l](../raw/evidence-2026-09-28-l-quickstart-code.md) 没有自动完成停机，是反例而非正票 | **主线：机制已证** |
| **R3 按时/按事件唤醒** | 何时再次起跑；可以由时间表、事件或外部系统决定 | Claude Code `/loop` / 云端调度的差别（[evidence-b §4c](../raw/evidence-2026-09-26-b-stop-and-scheduling.md)）；Cursor `/loop`（[evidence-u S4b](../raw/evidence-2026-09-30-u-post-june-kols.md)）；Runkle event-driven（[evidence-b §4e](../raw/evidence-2026-09-26-b-stop-and-scheduling.md)） | **先教会话内唤醒，再讨论跨会话持久运行**；后者另需状态、取消传播、硬上限、审批与升级可达性 | **主线：两种运行边界必须分开** |
| **支线 A：多主体编排**（原 R4） | 分工/并行/汇总由何种主体协调 | Anthropic 研究系统编排器-工人、Cognition 受约束并发、Carlini 分布式文件锁（[evidence-u S2/S3/S5](../raw/evidence-2026-09-30-u-post-june-kols.md)） | 任务可分、写入所有权、整树预算、合并与独立验收；可从 R1/R2 进入，**不以 R3 为前置** | **支线：机制已证；拓扑不收敛** |
| **支线 B：改进循环本身**（原 R5） | 对规则/工具描述/配置的修改，从人操作到代理提案、再到受控应用 | Runkle hill-climbing、Morris flywheel（[evidence-a](../raw/evidence-2026-09-26-a-originators.md)、[evidence-c](../raw/evidence-2026-09-26-c-autonomy-and-convergence.md)）；Anthropic 工具描述改写的局部实例（[evidence-u S5](../raw/evidence-2026-09-30-u-post-june-kols.md)） | 将“人工调控”“代理给建议”“自动应用外围改动”“自动改评估器/核心结构”分开；后两者不是已经证明安全的统一高阶 | **支线：局部实证；广义自改待证** |

**判据**：这里的“机制已证”只表示多家可观察到该交接面，不表示所有来源都按这个顺序分级，也不表示提高自主度带来净收益。**高阶不是毕业要求**：R3 的跨会话无人值守、支线 A 的多代理编码、支线 B 的自动自改，可作为方向与特定场景的实践样本；它们的通用成熟度和效果仍待验证。按任务的风险、可撤销性、验证成本选择位置，允许降低放权；不以固定轮数定级。[Osmani 双轴原文（evidence-a D11）](../raw/evidence-2026-09-26-a-originators.md)明确提醒“agency / orchestration”不能塞进一个数值阶梯；[Anthropic《Building effective agents》](https://www.anthropic.com/engineering/building-effective-agents)把编排当可组合工作流而非必经级别。

## 三、三处容易教错的边界

1. **R2 的“检查完成”不是“验收产出质量”**：`/goal` 的独立评估者检查约定条件，但 Osmani 强调它只看 transcript 中的硬规则；测试绿不等于系统需求满足。把真实内容验收与人的判断保留下来（[evidence-a D2](../raw/evidence-2026-09-26-a-originators.md)）。
2. **R3 的 `/loop` 不等于脱离会话**：会话内定时与跨会话云端任务分开教学；[Osmani《Practical Loop Engineering》Fine print](https://addyosmani.com/blog/practical-loop-engineering/)明确说前者 session-scoped，后者 `/schedule` 可在云端持久运行。
3. **支线 A 没有共同的“写入单线程”拓扑**：Cognition 推荐写入单线程；[Carlini 一手案例](https://www.anthropic.com/engineering/building-c-compiler)却由多个代理各自 clone、修改、push、merge，且不用编排代理。共同控制问题是避免冲突、合并和验证，而非特定拓扑。

## 四、分歧与证据边界

| 来源 | 提醒什么 | 教学时怎么放 |
|---|---|---|
| Ronacher（[evidence-u S1](../raw/evidence-2026-09-30-u-post-june-kols.md)） | 放手可能积累防御性代码；下一轮反馈可为非二值信号 | 续跑信号与最终验收分账，长寿命/品味密集工作不自动升级 |
| Walden / Carlini（[evidence-u S2/S3](../raw/evidence-2026-09-30-u-post-june-kols.md)） | 对并发写入采取相反拓扑；测试通过也可能漏验 | 支线 A 摆并列方案，不写单一共识 |
| Morris / Böckeler（[evidence-c](../raw/evidence-2026-09-26-c-autonomy-and-convergence.md)） | 人改 harness 与代理自改的交接不同，同阵营不算独立机构 | 支线 B 画提案/应用权限，不用观点数量冒充效果证据 |
| [Lulla 等研究 §4.1](https://arxiv.org/html/2608.21884v2) | 217/256 仅是筛中仓库的自动 loop 确认；样本中目标/停止条件与 verifier 的 repo 可见命中为零 | 不能把论文构件综述当“R4 verifier 已普及”或效果证明 |

**对外措辞**：这是“有证据的学习路径与可选能力地图”，不是行业成熟度标准。每一步问：这次谁启动下一轮、谁判断是否完成、谁能改变系统、出了错谁能及时停下并接手？
