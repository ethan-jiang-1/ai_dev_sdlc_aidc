# capability_ladder — Loop Engineering 能力爬梯 · 按交接面横切区

> **给接手的 Agent/协作者**：本文件是协作入口。读完它＋[`00-map.md`](00-map.md) 即可上手，不需要聊天记录。

## 〇、初衷（为什么单开这个目录）

用户 2026-09-30 决定：loop engineering 的素材按"控制问题"横切（[`stop_conditions/`](../stop_conditions/README.md)）
之后，还缺一条**学习者视角**的轴——**从最容易理解的形态到最复杂的形态，一步一步把能力交出去**。
工程上这种"步步为营"的组织最容易被消化；每一阶同时回答两个问题：
**这一阶你把什么交给了循环？要补什么护栏才配升下一阶？**

**定阶门槛（本区第一纪律）**：阶位不由任何单一来源钦定。**≥2 个已回源独立来源站在同一交接面上**，才是**正式阶**；
只有 1 个来源（或需新回源）的，降为**候选阶**，在矩阵里挂着排队，够格才升正式。
——**阶数是挖出来的，不是设计出来的**（用户 2026-09-30 定调：不纠结几阶，要共识阶，从简单到复杂）。

**命名**：`capability_ladder` 是跨各家通用的描述性术语，不沿用任何 KOL 的专属词
（同 [`stop_conditions/`](../stop_conditions/README.md) 命名规则）。⚠️ 措辞红线：**不叫"成熟度模型"、不按"N 轮自主度"切阶**
——缺口 2 明确记录"通用轮次自主度分档 0 一手来源"；本阶梯说的是**交接面逐阶扩大**，不是轮数阈值。

## 一、定位：主题的第三条横切轴

| 视图 | 组织轴 | 权威 |
|---|---|---|
| `raw/evidence-*` | 按路别/来源 | **证据权威**（本区不改写） |
| `digested/*` | 按议题 | **判定权威**（本区不产生新主张） |
| `stop_conditions/` | 按**控制问题**横切 | 深挖区 |
| **`capability_ladder/`（本区）** | 按**学习者交接面**横切 | 深挖区（2026-09-30 立） |

- 每条做法沿用 stop_conditions 的**自说明硬规矩**：**自带核心片段（原句/代码/参数），纯指针条目无效**。
- **升阶闸门**＝[`stop_conditions/`](../stop_conditions/README.md) 三件骨架（机器闸门/硬上限/验收分离）：
  想从 Rn 升 Rn+1，先看对应阶的停止条件补齐没有——两区互相引用，不复制正文。
- 实践层 [`03_practice/loop_governance/`](../../03_practice/loop_governance/README.md) 管**控制轴**（机器怎么跑）；
  本区管**成长轴**（人怎么逐步放权）。harness_governance＝环境轴。三轴各管一侧。
- goal/eval 怎么构造仍归 [`../agent_goal_eval/`](../agent_goal_eval/README.md)，本区只放指针。

## 二、台阶一览（定阶判定见 [`00-map.md`](00-map.md)）

| 阶 | 一句话（学习者交出去什么） | 共识来源 | 状态 | 升阶闸门 |
|---|---|---|---|---|
| **R0 人肉 API** | （基线，非台阶）提示→等待→读→再提示；人自己是循环的传输层 | —（反面基线） | 基线 | — |
| **R1 授权执行** | 交出**单轮内的工具与命令执行权**；人只设授权面＋测试门 | Osmani 运行模式一级 · CC turn-based · Anthropic deny-and-continue · Cursor 设置面（官方一手⏳） | ✅ 正式阶 | 机器闸门（①） |
| **R2 目标驱动** | 交出**多轮的路径选择**；人只给可观察的完成条件 | Osmani `/goal` · CC goal-based · Anthropic quickstart 源码 | ✅ 正式阶 | 可观察停止条件＋验收分离（①③） |
| **R3 时间/事件驱动** | 交出**"要不要开跑"本身**；循环脱离会话在跑，人管触发与熔断 | Runkle event-driven 环 · CC time-based/proactive · Osmani `/loop`/`schedule` | ✅ 正式阶 | 硬上限＋熔断（②） |
| **R4 编排与并发** | 交出**任务分解与子代理调度**；人管拓扑与预算 | 视频三层之三 · Anthropic multi-agent（⏳待回源） | ⏳ 候选阶 | 全三件＋token 预算 |
| **R5 自我改进** | 交出**对 harness 本身的改写权**；人管提案-评估分离与审计谱系 | Runkle hill-climbing 环 · GEPA/DSPy 保护链（缺口5 素材） | ⏳ 候选阶（单源＋生态） | 提案-评估分离＋改写审计链 |

## 三、纪律（沿用＋本区新增）

1. **候选阶不得出现在结论/对外文字里**（同"⏳ 待回源不进结论"铁律）；R4/R5 的整阶引用要先升正式。
2. **社区/论坛素材只作采用度信号**，标注观测日期，不作定义源（README §1 硬排除照常生效）。
3. **中文传播层素材**（如 [evidence-t](../raw/evidence-2026-09-30-t-shenmejiaoqq-video-zh.md) 视频三层）只作
   传播旁证与切片对照，其机制细节引用前先回官方一手（见 evidence-t §1 校验点）。
4. 逐字段补齐前，条目允许挂 `⏳ 逐字待补` 占位，但**升正式阶前必须清零**。
5. 与 deck 的关系：[`05_output/deck_ai_loop_engineering/`](../../05_output/deck_ai_loop_engineering/AGENTS.md) 只写叙事；
   本区供给叙事素材，叙事改动不回写本区判定。

## 四、回源队列（按优先级）

1. **Anthropic《How we built our multi-agent research system》**——R4 头号一手，主题内尚无档案；决定 R4 能否升正式。
2. **Cursor 官方 docs**（Run Mode / Auto review / Command Allowlist / File Deletion Protection）——R1 一手；
   顺带核销 [evidence-t](../raw/evidence-2026-09-30-t-shenmejiaoqq-video-zh.md) §1 校验点里 Cursor 相关讹变。
3. **LangGraph supervisor / orchestrator-worker docs**——R4 第二票（evidence-q/s 有部分，需按控制链归位）。
4. R5 升阶材料：缺口 5 已集齐的 GEPA/DSPy 提案-评估分离素材按自说明格式搬入（不新建回源）。

## 五、文件分工

| 文件 | 职责 |
|---|---|
| `README.md`（本文件） | 定位、纪律、定阶门槛、回源队列 |
| [`00-map.md`](00-map.md) | 六源阶梯对照矩阵＋收敛/分叉判读（**本区判定权威**） |
| `rung-0N-*.md` | 每阶一档：定义、支撑条目（自说明）、反例位、升阶条件、待补清单 |
