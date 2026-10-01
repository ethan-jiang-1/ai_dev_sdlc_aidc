# 当前状态（热区）

> 最近一次更新：**2026-09-30 晚（ladder 回流＋手册立项）**：[landscape](result/landscape.md) 增 §3.5 交接面（LE 四档＋支线＋结果可信检查链，§6 上屏清单已放行）；[digested/07](digested/07-控制问题矩阵.md) §二登记交接面读法；实践层 [manual](../../../03_practice/loop_governance/result/manual.md) 增 §13 授权面划定规程（LE1 操作化，[backbone](../../../03_practice/loop_governance/result/backbone.md) §3 补指针）。承重 ⏳ 清理完成：rung-02 ① 锚 evidence-a §4 D2、rung-03 ① 改锚 evidence-b 问题2 §5（旧锚 §4e 有误）、rung-01 反例位改锚 evidence-f Source 4（原 practices ②「命令级越权」指针有误，实为资源层失控）、rung-02 ③ 标注改「逐字在档·侦察级不支撑定阶」。**LE1–LE3 定阶支撑零 ⏳ 依赖**。
>
> **2026-09-30（LE 主线＋结果可信闭环）**：[00-map](capability_ladder/00-map.md) 以 **LE0→LE3 执行委托线、A/B 可选支线**讲交接决定；[结果可信闭环](capability_ladder/result-reliability-interface.md)讲“目标→证据→裁决→停机/交接→后验复核”。六档各有独立 SVG 和运行示例，[capability_ladder/README](capability_ladder/README.md) 索引。新增 [evidence-w](raw/evidence-2026-09-30-w-ladder-runtime-detail.md)、[evidence-x](raw/evidence-2026-09-30-x-ladder-branches-detail.md)、[evidence-y](raw/evidence-2026-09-30-y-long-run-result-reliability.md)；官方机制、案例与教学设计分列。goal/eval 构造归 [agent_goal_eval](../goal_eval_engineering/README.md)，停止骨架归 [stop_conditions](stop_conditions/README.md)。`File Deletion Protection`、NLAH 与部分 `⏳` 条目尚待核验。
>
> **2026-09-28（stop_conditions 深挖批收口＋自说明改版）**：三件骨架按点深挖第一轮全量回源完成——6 个新 evidence 档案（l 官方 quickstart 源码 / m 裁判谱系 / n coding 验收分离 / o 失控实录 / p 实战闸门与非编码域 / q 框架默认值），32 条新来源，承重引文逐条抽验、缺原句的条目上 web 补齐原文。**用户定的硬要求已落规则**：practices 自说明——每条自带核心片段（原句/代码/参数），纯指针条目无效；取不到硬核内容的条目放弃并记录（Reddit $6k 案即此）。**方法论发现**：两处 docs↔源码默认值打架（LangGraph 1000↔10007、CrewAI 20↔25）——参数类主张必须锚源码/tag。**回流候选已登记**（失控三型→②、裁判失效四机理→③、docs↔源码分歧→引用规范），待进 digested/03。

## 一句话

**八个控制问题里，执行、停止、动作级授权和会话记忆已有公开机制；feature 级的授权史、priority 变更、业务阻塞原因和跨 feature 验收仍是稳定的空。** 一条真实 goal 日志把这四列再看了一遍，还是空，而且 goal 被 resume 时 driver 可以一轮都不计。外置行对照没做，所以这不是「外置记录更有效」。I2 的定量资料补足了“效果证据不是零”，但没有检验 loop 设计本身的因果效果；I2 中未复核的厂商和谱系材料仍只算候选。

## 状态

| 件 | 状态 |
|---|---|
| `raw/evidence-2026-09-26-{a,b,c}-*.md` ×3 | ✅ **A**（词源四人：Runkle/Osmani 全取得；Cherny/Steinberger 定性碎片级）· **B**（停止条件/调度，9 个一手记录块）· **C**（自主度/收敛/归属修正）；**09-27 增量**：Osmani D5–D10 实践细节补入 evidence-a（不新建重复档案） |
| `raw/evidence-2026-09-27-{e,f,g,h,i,j,k}-*.md` ＋ `evidence-2026-09-27-i2-*.md` | ✅ **E**–**I**、**J**（本地 goal，对照臂未跑）；**I2** 已形成五切口档案，但主验与侦察回源混合，未复核条目不计独立票；**K**（Unrolling：候选文本称 assistant message 是 turn 终止态；「四拍」不是原文；直接 HTTP 403，待独立复核） |
| `raw/research-plan.md` | ✅ v0.5：在 v0.4 基础上加入统一控制链（Goal → Action → Environment Feedback → Eval → Continue/Stop/Escalate → State/Outcome）与概念/机制/效果三层证据分离；后续回源按控制节点归位，不再按人物堆料 |
| `digested/06-automation-autonomy-harness-loop.md` | ✅ 初步判读：控制对象逐层外移与叠加；harness 是 loop 可设计/可观察的条件之一，不是单向历史原因；DSH 执行循环与 feature control plane 分离 |
| `digested/07-控制问题矩阵.md` | ✅ A–I1 综合，I2 仅登记候选来源，J 路加本地观察指针：八问只保留已回源做法；feature 四列在已复核材料和这一条 goal 日志里都是空；2026-09-30 增 §二交接面读法（指向 00-map，不改格子判定） |
| `raw/kol-roster.md` | ✅ §A **仍是 6 条，I 路/I2 不升人**。§B 补 Gauthier / Horthy / Beck / Yegge（I 批次 1）＋ **Ball / Walden / Manus / Armin（I2 批次）**，Lopopolo 从 ⏳ 改为 harness 全文已取得。Willison 仍在 §C1：循环实践者，但 2026-06 后对本词无已核发声。evals 四人＋定量机构按 §2.3 纪律**不入册**（证据来源非发声 KOL） |
| `raw/00-timeline.md` | ✅ 词源周精确锚定（06-02 → 06-07 → 06-08 → 06-16 → 06-30，snowflake 解码）；新增 I/J/K 与 2023–2025 谱系候选；Tessl 2026-09-14 行保留为待主验候选，不计第五定义源 |
| `digested/01-命名谱系.md` | ✅ 词源＝热度碎片、定义＝事后工程化；已纳入 Willison/Horthy 相邻实践；Tessl 三层定义保留为侦察回源候选，未升级为第五已证定义 |
| `digested/03-构件.md` | ✅ 停止条件三件骨架；外层调度是长程扩展。动作门四种处置已按出处画出（evidence-f，无新抓取）；没有通用轮次刻度 |
| `digested/08-kol-alignment-andrew-ng.md` | ✅ KOL 概念对齐：共同最小交集、Ng 三环与 stop_conditions / loop_governance 的对应及冲突边界（2026-09-28） |
| `digested/05-边界判定.md` | ✅ 三层分工；收敛成立且双向；**三条引用归属修正**（影响全仓） |
| ~~`raw/org/` · `raw/community/`~~ | ✅ **已撤销**（2026-09-26 评审决定 5）：evidence 档案为素材常态形态，纪律要点已并入 README §1「回源档案纪律」 |
| `result/landscape.md` | ✅ 2026-09-27 入层。过筛结论；未复核的 I2 / K 不进主张；2026-09-30 增 §3.5 交接面（判定源 00-map） |
| `stop_conditions/`（三件骨架深挖区） | ✅ 2026-09-28 立区＋深挖批收口＋**自说明改版**（用户定硬要求：practices 每条必须自带核心片段——原句/代码/参数，纯指针条目无效；取不到硬核内容的条目放弃并记录，如 Reddit $6k 案；**README 已升级为协作入口**：初衷/流程/格式期待）。6 个新档案（l/m/n/o/p/q）；practices ① 20 条（五域＋框架缺省对照＋行为面反例）/ ② 21 条（失控实录 3 案＋docs↔源码分歧 2 处＋候选单列＋放弃记录）/ ③ 26 条（裁判失效四机理实证＋spec-kit 口径修正）；判定权威仍在 digested/03，**回流候选已登记** |
| `raw/evidence-2026-09-30-t-shenmejiaoqq-video-zh.md` | ✅ **T 路**：中文视频传播锚（为什么叫QQ 实操指南）文字稿＋ASR 讹变对照表＋与已回源机制的同构归位候选。侦察级，不进结论；时间线已记传播位，KOL 不入册 |
| `capability_ladder/`（LE 执行委托线＋结果可信闭环） | ✅ [00-map](capability_ladder/00-map.md) 为本区唯一教学判定权威；LE0 基线＋LE1–LE3 主线、A/B 可选支线，各自独立 SVG；[结果可信闭环](capability_ladder/result-reliability-interface.md) 明确目标、证据、裁决、停机/交接和后验复核，不把调度机制冒充可靠结果。evidence-w/x/y 已归档；**2026-09-30 晚：承重 ⏳ 已清（定阶零依赖）、判定已回流 landscape §3.5＋digested/07**；剩余不承重待办：`File Deletion Protection` 名称、NLAH 原文核验 |
| 实践层 `03_practice/loop_governance/` | ✅ backbone 与 manual 已确认。确认记录在该目录 `CURRENT.md`，本行不复制审阅过程 |

## 下一步

1. **研究主轴已升级为控制链。** 后续回源按 `Goal/边界 → 行动 → 环境反馈 → Eval/裁判 → 继续/停止/升级 → 状态与结果分账` 归位；不再只按 KOL 或产品名堆素材。
2. **下一轮唯一优先入口**：Goal/Eval 的可观察性与验收独立性；每条候选机制先填 `research-plan §1.1` 控制链审计卡，再决定是否进入 digested/practice。
3. **硬核验证支线仍未完成。** I2 侦察回源、行为面正反例矩阵、自我改写保护链、DSH 外置行对照都不进 `landscape.md`，直到主验和可重复日志/指标齐备；不用 J 路 `n=1` 代替 P-outcome。
4. **deck 只写叙事。** 页面图和 PPTX 已删除。研究侧不另起主张。
5. **实践层确认不再阻塞。** F 的动作门、I 的行为面反例、四列空格的工作行试点，边界已写在 landscape §5–§7；I2 / K / J 不作效果依据。
6. **三件骨架深挖区已开**（[`stop_conditions/`](stop_conditions/README.md)，2026-09-28）。第一轮回源已全部收口（l/m/n/o/p/q 六档案，32 条新来源；中断的两路补采已完成）。下一步按控制链审计卡归位，并将判定候选回流 digested/03。
7. **跨仓修正三处**（本轮一手证据触发，不属本主题但已查明）：
   - `talk-harness-201/02_evidence/01-kol-alignment-2026.md`：公式 "Agent = Model + Harness" 归属改为 **Trivedy/LangChain 原创 → Böckeler 传播锚点化**；
   - `01_seed_reference/reference/kol/_raw_kol/10_kief_morris.md`：三档 → **四级**（+ agentic flywheel），且 flywheel 是节标题；
   - Böckeler "False sense of control?" 的出处标注改为 **2025-10-15 sdd-3-tools.html**（凡引用处）。
8. **T 路判读候选待处置**（[evidence-t §3](raw/evidence-2026-09-30-t-shenmejiaoqq-video-zh.md)）：六处与已回源机制的同构对号**不重复计票**；"Run Everything 只在 demo 用"的自主度分档句、三个可跟踪预言（编排框架/动态 Loop/云规划+本地 SLM 执行）先填控制链审计卡，再决定是否回流 digested/03。"90%" 统计与 Lance Martin 人物在回源核实前不得引用。
9. **capability_ladder 后续**：2026-09-30 晚承重 ⏳ 清理完成（LE1–LE3 定阶支撑零 ⏳ 依赖），判定经 landscape §3.5＋digested/07 交接面读法回流，实践层 manual §13 补上 LE1 操作化缺口；`Run Everything` 已由官方 Run Modes docs 核实。剩余不承重待办：`File Deletion Protection` 名称核验、NLAH 原文、rung-02 行为面反例矩阵 ⏳。
10. **可跟踪预言**（登记防丢）：若出现第一条可复核自主度/质量放行阈值，回本主题补档、再评估实践层 §3；当前不以固定 N 轮作为目标。


## 缺口

1. **《Unrolling the Codex agent loop》**已有候选原文摘录（[`evidence-k`](raw/evidence-2026-09-27-k-unrolling-codex-agent-loop.md)），但直接打开 openai.com 在本环境仍是 403；assistant-message 终止态可作为待复核机制线索，不能把检索工具摘录当成完全主验的一手证据。
2. **通用轮次自主度分档**仍为 0 一手来源——F 路确认应转向动作/环境/歧义/拒绝预算/升级可达性，不制造“跑 N 轮必须人看”。
3. **统一 feature-level 在途可见性**仍是开放缺口，且已形成四列待填矩阵（见 `digested/07`）：授权史、priority 变更、业务阻塞原因、跨 feature 验收。I2 提供了 Cursor Projects、Jules 等候选控制面形态，但其中部分为侦察回源，不能单独关闭缺口；J 路只说明一条真实 goal 仍缺这四列。
4. **真实 P-outcome**的表述修正：跨机构定量结果已存在，但它们测量的是不同工具、场景、代际或组织结果，且方向不一；没有一项把 loop 设计作为自变量证明效果。METR、DORA、GitClear、Peng 的细节按主验/侦察标记引用，J 路 `n=1` 不构成效果证据。
5. **行为面验证**：I-2 切口 b 已集齐原句级实践（Eugene execution/direction drift 二分＋fresh-context 对照会话；Chip false completion；Anthropic raw-transcripts 原则；GitClear "a passing test, a closed ticket" 概括）＋ 自我改写保护链（GEPA/DSPy 的提案-评估分离/Pareto 档案/审计谱系、Shankar criteria drift 反例、DSPy 官方静默退化反例）。**待 `digested` 层收成正反例矩阵**；F 路的授权可达性反例仍然成立。
6. **Cherny 访谈句三个流传版本措辞不一致**（A 路已列对照表）——上屏引用须先人工核验视频原声。

## 铁律速记

- **素材权威在 evidence 档案与 `01_seed_reference/`，判读权威在 `digested/`，操作权威在 `03_practice/loop_governance/`**。
- **goal 与 eval 如何构造**归 [`../agent_goal_eval/`](../goal_eval_engineering/README.md)（定调在该目录 README §1）。本主题的验证格与 `/goal` 引句留在原档案，不在这里扩成那个主题。
- **`⏳ 待回源` 不进结论**；**B 路**负结论里，Unrolling 候选文本已登记（旧题 Unwinding），但直接页面仍 403，不能当完全主验。其余仍在：CC CHANGELOG、auto mode 公告正文、Codex auto-review docs。台账 §E 收跨路汇总。
- 姊妹仓 FAQ 15 的旧判定（切片层/管线层）**只作对照**——本主题全部结论以自己的回源为准。
