# R2 目标驱动（正式阶）——交出多轮的路径选择，人只给可观察的完成条件

> **交接面**：人不再描述"每步做什么"，只描述**可观察的最终状态**（测试通过、构建成功、调用点清零）；
> 循环自己决定每轮改哪里、怎么改，由独立评估者对状态逐轮判定。人保留的东西：目标措辞、验收判据、边界。

## 一、定义（跨源最小交集）

入口是粗目标＋完成条件；循环以 goal 为终止判据多轮自驱。判据必须是**机器/环境可观察的**，这是本阶与 R1 的本质差。

## 二、支撑条目（自说明）

**① Osmani `/goal`（转述自台账，逐字在 evidence-a）** ⏳ 逐字待补
- 要点（转述 [`raw/kol-roster.md`](../raw/kol-roster.md) §A `addy_osmani` 行）：`/goal` 评估器**只核 transcript 硬规则、不判内容好坏**；
  分层运行模式第二级即 `/goal`。锚 [evidence-a](../raw/evidence-2026-09-26-a-originators.md)。

**② Anthropic quickstart 源码（本区唯一已带逐字的条目）**——一手源码，观测 2026-09-28，全文在 [evidence-l](../raw/evidence-2026-09-28-l-quickstart-code.md)：
- 驱动层退出路径逐字：
  > `while True:` / `iteration += 1` / `if max_iterations and iteration > max_iterations:` →
  > `print(f"\nReached max iterations ({max_iterations})")` / `break`
- **循环内没有完成检查**：`run_agent_session` 成功时恒返回 `("continue", response)`；驱动层不读通过率、不判"全部 passes"。
- 通过率的实际住处：`count_passing_tests` 读 `feature_list.json` 的 `passes` 字段——**算给人看**（每轮打印），不以 `passing == total` 停机。
- 对本阶的教训（落差即发现）：**博客叙事里的"goal 完成"，在配套驱动代码里是靠人看进度 summary 实现的**——R2 的"交出判停权"在工程上并不自动成立，判据住哪一层是设计决定。

**③ 可观察措辞纪律** ⏳ 逐字待补
- 中文传播层的转述与本主题判读同构（[evidence-t](../raw/evidence-2026-09-30-t-shenmejiaoqq-video-zh.md) §2，侦察级）：
  > "你不能写让代码达到生产就绪，因为AI没法验证，你必须写测试通过且lint检查无误，这样评估者才能通过读取终端输出判断是否真正完成。"
- 主题侧权威表述在 [`../agent_goal_eval/`](../agent_goal_eval/README.md)（goal/eval 怎么构造归那个主题，此处只指针）。

## 三、反例位

- goal 措辞含糊 → 循环烧钱无果：行为面反例矩阵待收口（CURRENT 缺口 5），落位后搬入 ⏳。
- 评估者只读 transcript 的局限（Osmani 口径）→ 与 ③ 验收分离（[`stop_conditions/03_verdict_split/`](../stop_conditions/03_verdict_split/README.md)）衔接。

## 四、升 R3 的闸门

R2 的循环仍靠"人开一次会话"起跑。当任务需要**定时起跑或事件触发**（CI 轮询、夜间跑批），交出去的就是
"开不开跑"本身——必须先补**硬上限与熔断**（[`stop_conditions/02_hard_caps/`](../stop_conditions/02_hard_caps/README.md)），
否则无人值守＝无人拉闸。
