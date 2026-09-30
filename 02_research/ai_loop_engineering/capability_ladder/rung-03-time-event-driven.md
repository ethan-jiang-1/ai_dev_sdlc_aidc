# R3 时间/事件驱动（正式阶）——交出"开不开跑"本身，循环脱离会话在跑

> **交接面**：人不再手动起跑循环。循环由**时间表**（cron/间隔）或**事件**（webhook/渠道消息/状态变化）触发，
> 起跑后人不在场。人保留的东西：触发条件、资源上限、熔断与过期、升级可达性。

## 一、定义（跨源最小交集）

循环的**启动权**交给了调度器或事件源。这是所有来源里"人退出会话"的第一阶——也是唯一一阶
**人不在场看着它跑**的正式阶，所以硬上限/熔断从"保险"变成"唯一刹车"。

## 二、支撑条目（自说明）

**① Runkle event-driven loop（B 类环对应本阶）** ⏳ 逐字待补
- 要点（转述自台账 `sydney_runkle` 行）：四环之三，cron/webhook/channel 触发。锚 [evidence-b §4e](../raw/evidence-2026-09-26-b-stop-and-scheduling.md)。

**② CC 团队 time-based / proactive 两类（A 类双落位）** ⏳ 逐字待补
- 要点（转述自台账 `anthropic_org` 行）：`/loop` 时间驱动、**7 天硬过期**；auto mode 的 deny-and-continue＋**3/20 熔断**。
  锚 [evidence-b](../raw/evidence-2026-09-26-b-stop-and-scheduling.md) / evidence-c。
- 7 天硬过期与 3/20 熔断是本阶"人不在场也要有刹车"的两个已回源参数级实例 ⏳ 参数逐字待补（须锚 docs/源码，本主题纪律）。

**③ Osmani 三/四级** ⏳ 逐字待补：三级 `/loop`/`schedule`、四级 proactive 事件触发无人值守（[evidence-a](../raw/evidence-2026-09-26-a-originators.md)）。

## 三、反例位

- 无人值守×失控＝最危险的组合：失控实录三案（practices ②）中 194h zombie 孤儿进程等案例即本阶事故面 ⏳ 引句待搬
  （锚 [stop_conditions/02_hard_caps](../stop_conditions/02_hard_caps/README.md) practices ②，不复制）。
- **中文传播层在本阶缺位**（[00-map](00-map.md) §三.5）：视频三层从 goal 直接跳编排，无人值守没有切片——传播层把最危险的一阶跳过去了。

## 四、升 R4/R5 的方向

本阶之上不再有共识阶（见 [00-map](00-map.md) 判读）：编排（R4）与自我改写（R5）目前是框架能力/生态做法，
不是概念共识阶。升阶材料见 README 回源队列。

## 五、与缺口的关系

feature 级四列空矩阵（授权史/priority 变更/业务阻塞原因/跨 feature 验收，[`digested/07`](../digested/07-控制问题矩阵.md)）
在本阶**最疼**：人不在场时，这四列是"回来之后还能不能接上"的全部依据。R3 档后续把四列作为观察清单挂靠。
