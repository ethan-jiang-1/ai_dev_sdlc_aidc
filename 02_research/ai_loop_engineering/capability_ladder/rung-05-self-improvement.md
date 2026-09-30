# R5 自我改进（候选阶 ⏳）——交出对 harness 本身的改写权

> **状态**：**候选阶**（[00-map](00-map.md)：概念上 2 源同指——Runkle hill-climbing、Morris flywheel——
> 但均无操作层展开；操作素材在生态侧）。升正式条件：操作条目按自说明格式落齐且 ≥2 独立来源。

## 一、交接面（假设版，待回源检验）

循环不再只执行任务，还**改写约束自己的那层东西**（prompt/skill/评估器/harness 配置）。
人的介入点从"管循环"上移到"管改写权的护栏"——提案与评估分离、改写审计谱系、Pareto 档案。

## 二、支撑条目（自说明）

**① Runkle hill-climbing loop（B 类第四环）** ⏳ 逐字待补
- 台账转述："改写 harness 本身"——"the return arrow doesn't just loop back to the top — it reaches inside and
  updates the agent loop directly"（转述自 [`raw/kol-roster.md`](../raw/kol-roster.md) §A，逐字锚 [evidence-b §4e](../raw/evidence-2026-09-26-b-stop-and-scheduling.md)，待核原文）。

**② Morris agentic flywheel** ⏳ 卡片待按四级修订（[`_raw_kol/10`](../../01_sources/reference/kol/_raw_kol/10_kief_morris.md)），落位注见 [00-map](00-map.md)。

**③ 生态操作素材（缺口 5 已集齐，按自说明格式搬入即可，不新建回源）**：
- GEPA / DSPy：**提案-评估分离**、Pareto 档案、审计谱系（CURRENT 缺口 5 登记，源档案在 evidence 批次内 ⏳ 搬运）。
- Shankar criteria drift 反例、DSPy 官方静默退化反例——本阶的**反面教材主菜**：改写权无护栏时，
  评估器被改写方俘获，指标升、实际退化。

## 三、升阶闸门（若升正式）

提案-评估**物理/契约分离**（[`stop_conditions/03_verdict_split`](../stop_conditions/03_verdict_split/README.md) 的架构级形态）
＋**改写审计链**（谁改的、改了什么、能不能回滚）。R5 的验收分离对象不是任务产出，而是**判据本身**——
这是它比 R4 更后置的原因。

## 四、待补清单

1. evidence-b §4e hill-climbing 逐字核验。
2. 缺口 5 素材按自说明格式搬运。
3. Morris 卡片四级修订联动（跨文件待办，已在 KOL 卡片侧挂号）。
