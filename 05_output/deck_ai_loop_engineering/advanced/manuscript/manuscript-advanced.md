---
title: 文稿 — Loop Engineering 技术产品场
status: draft-for-review
source: advanced/outline/outline-advanced.md（v3 阶梯脊柱）
revised: 2026-10-01
---

# 文稿 — 技术产品场

> 本稿与 [`../outline/outline-advanced.md`](../outline/outline-advanced.md)（v3 阶梯脊柱）同步。每页 `CLAIM` 必须与 outline 的 subtitle 完全相同；**一页一个概念，content 不超过三条**；引用块不上屏。
> 实操轨（90 分钟版）：三道构造档练习，题面与讲者卡在 [`../practice/`](../practice/README.md)，嵌入位置见 outline §8。

## 术语

档｜授权面｜策略件｜裁判（grader）｜负例｜验收（accepted）｜外部结果（outcome）｜交接单｜反馈回路｜定档四问

---

### B01 · 你离开后，它说做完了

**CLAIM**：Loop 的难题不是能否行动，而是回来时凭什么信完成宣告。

**上屏**

- title: 你离开后，它说做完了
- content:
  - 你离开了；它继续跑；它说：完成。
  - 治理要回答的是：这句话凭什么**被系统接受**。

**接到下一页**：先说这个词为什么突然到处都是。

### B02 · 别写 prompt 了，写 loop？

**CLAIM**：模型已经强到能知错改错——知道错在哪就能改对，所以有人开始不写 prompt，改写 loop；这两个前提，就是本场要工程化的东西。

**上屏**

- title: 别写 prompt 了，写 loop？
- content:
  - 模型很强，而且能知错改错。
  - 所以有人说：别写 prompt 了，写 loop。
  - 这句话是真的——但它是门手艺。

**展开**：故事成立的前提有两条：模型能力够强，**并且反馈进得来**（它得知道错在哪）。今天全场讲的，就是把这两条前提变成工程：反馈落成工件、判断写成判据、护栏可以演练、升档用门禁说话。掌握 loop 需要锻炼——阶梯就是练法。

**接到下一页**：练法的第一步，是定位你在阶梯的哪一级。

### B03 · 你在哪一档

**CLAIM**：治理从定档开始——交动作、交续跑、交唤醒，每一级交出一个决定、配上一组护栏。

**上屏**

- title: 你在哪一档
- content:
  - 第一级 交动作：授权面内的动作不再逐条批。
  - 第二级 交续跑：它自己跑到目标为止。
  - 第三级 交唤醒；再往上有两条支线——局部已证，未成熟。

**备注**：命名争议压缩为背景——各家 loop 外延不兼容，本场治理的是可审计控制决策，不站队环数。Ralph 的 `while :; do...done` 无内建 stop；`/goal`、`/loop`、auto mode 分别是条件、时间/事件、轮内审批语义，不能合成一个环。

**接到下一页**：定档有一把公共的尺。

### B04 · 定档四问

**CLAIM**：谁启动下一轮、谁判断完成、谁能改变系统、出了错谁能停下接手——四问在每个档位都有不同答案，这张表就是全场的检查表。

**上屏**

- title: 定档四问
- content:

| 四问 | 第一级 | 第二级 | 第三级 |
|---|---|---|---|
| 谁启动下一轮 | 人 | 目标条件 | 时间表/事件 |
| 谁判断完成 | 人 | 裁判＋人守验收 | 裁判＋人守总账 |
| 谁能改变系统 | 授权面 | 授权面 | 授权面＋调度配置 |
| 出错谁接手 | 人当场 | 交接单＋人 | 交接单＋升级渠道 |

**备注**：建议每次控制迁移写事件：`goal_rev/action_id/evidence_ref/verdict/decision_source/state_rev/stop_reason/resume_pointer`——本主题设计题，不是产品统一 schema。

**接到下一页**：从第一级开始，逐级看门票与护栏。

### B05 · 授权面是分级处置表

**CLAIM**：交出动作审批，交的不是开关，是一张表：允许直行、沙箱内跑、必须人批、硬拒绝。

**上屏**

- title: 授权面是分级处置表
- content:

| 处置 | 例 |
|---|---|
| 允许直行 | 读目标文件、跑定向测试 |
| 沙箱内跑 | 写指定目录、无网络出站 |
| 必须人批 | commit、外部调用 |
| 硬拒绝 | push、删库、生产配置 |

**展开**：官方样本：Cursor 对 Shell/MCP/Fetch 三级处置（allowlist→sandbox→classifier，2026-05 changelog）；Codex `exec_policy` 按危险启发式×沙箱能力×项目可信度映射 Skip/NeedsApproval/Forbidden。控制迁移建议每次落事件（`action_id/evidence_ref/decision_source`），不是产品统一 schema。

**接到下一页**：表怎么落地——先看最常见的假动作。

### B06 · 规则要写进策略件

**CLAIM**：93% 的权限提示最终被人批准——写在提示词里的规则等于没写，规则必须进策略件。

**上屏**

- title: 规则要写进策略件
- content:
  - 预写规则只让坏动作少拦 20.1 个百分点。
  - 93% 的权限提示，人顺手就批。
  - 391 个仓库里，只有 12 个提交过一条 deny 规则。

**展开**："A rule that ends in a prompt isn't a rule."（arXiv 2608.27443，2026-08）；"Everybody writes instructions, almost nobody enforces them."（marmelab 审计，2026-09-24）。规则要落成 allow/deny 配置与沙箱约束。

**接到下一页**：就算写进了配置，还有一层混淆要拆。

### B07 · 策略偏好不等于执行隔离

**CLAIM**：Auto-review 不是安全边界，宽 allow 规则代替不了沙箱——两层配置不能混为一谈。

**上屏**

- title: 偏好 ≠ 隔离
- content:
  - 偏好规则（permissions.json）：倾向批准/拦截什么。
  - 执行隔离（sandbox.json）：实际能碰到什么。
  - Run Everything：每个调用自动跑，无沙箱无分类器。

**展开**：官方原话 "Auto-review is not a security boundary"（Cursor Run Modes，观测 2026-09-30）；worker 的 `--workdir` 不约束 bash。宽 allow 永远不能替代真正的执行隔离。

**接到下一页**：表和配置都齐了——批准本身的边界要绑死。

### B08 · 一次批准绑三样

**CLAIM**：一次批准只绑定动作、目标、有效期；窄授权被当广授权用是真实事故。

**上屏**

- title: 授权绑三样
- content:
  - 准许编辑 ≠ 准许提交 ≠ 准许推送 ≠ 永久推送。
  - 事故：两行修改的推送授权，被当成大功能发布许可。
  - 最小绑定：`{principal, action, target, branch, expires_at, nonce}`。

**展开**：第一人称事故（issue #95749）："Editing files must not imply authorization to commit…"——14 个文件直推主干。edit 的批准不自动覆盖 commit/push、另一分支或另一 feature。

**接到下一页**：授权面还有一个经常被漏掉的维度——人的入口。

### B09 · 审批要可达

**CLAIM**：人看不到动作与风险、状态不可恢复，就不是「已升级」——审批可达性是独立的控制问题。

**上屏**

- title: 审批要可达
- content:
  - 指定人能看到：动作、目标、风险。
  - 父线程必须能看到子线程的请求。
  - 决定后能从同一状态恢复。

**展开**：反例（issue #67519）：用户在对话里反复明确授权同一动作，拒绝依然不可翻案——拒绝合理性和升级可达性是两个问题。没有审批入口、指定 reviewer 和 resume pointer，不能声称「已升级」。

**接到下一页**：人不在时拒绝怎么处理——拒绝是引导信号。

### B10 · 拒绝是引导信号

**CLAIM**：拒绝作为工具结果返回并附安全路径提示；拒绝预算（3/20，不可配置）是动作熔断，不是轮数上限。

**上屏**

- title: 拒绝是引导信号
- content:
  - deny-and-continue：拒绝回传＋"find a safer path"。
  - 3 次连续或 20 次累计 → 停机升级（官方明写不可配置）。
  - 这是动作拒绝预算，不是轮数上限。

**展开**：分类器只看用户消息与工具调用、剥掉模型自述——"reasoning-blind by design"（auto mode 文档，观测 2026-09-26）。headless 无人可问→直接终止。OpenAI 侧重复拒绝机制未公开相同阈值——参数不通用。

**接到下一页**：这套授权面怎么验证？——用变异测试。

### B11 · 变异测试验证授权

**CLAIM**：把 edit 换成 commit、分支换成 main、时间推到过期——旧批准都应失效；变异仍能通过就不能升档。

**上屏**

- title: 变异测试验证授权
- content:
  - 依次变异：动作 / 分支 / 目标 / 有效期 / nonce。
  - 每次变异都应拒绝旧批准。
  - 写出 `authorization_drift` 事件。

**展开**：若任一变异仍能通过，授权面没有真正生效——不能升档。这是把「授权绑三样」变成可测试断言的方法。

**接到下一页**：第一级到此配齐。第二级的门票，贵了一个数量级。

### B12 · 门票：goal 三要素

**CLAIM**：交出续跑的门票是可测终态、声明式检查、不变式——外加无进展出口与上限子句。

**上屏**

- title: 门票：goal 三要素
- content:
  - 终态：可观察的产出状态。
  - 检查：哪条命令、哪个退出码、哪份输出。
  - 约束：路径上不许变的东西。

**展开**：官方规格（evidence-b §4a）：可核条件 = one measurable end state + a stated check + constraints that matter；轮次或时间子句作上限。全例（Osmani）：Lighthouse ≥92、LCP<1.8s、CLI 输出证明、不改 hooks、两轮无改善 abort、10 轮上限——数字不可外推。合约样式的完整模板见文末控制实验 §1。

**接到下一页**：goal 之外，这一级还有一条生命线——反馈。

### B13 · 反馈是循环的燃料

**CLAIM**：下一轮消费的是落盘的工件和 evidence_ref，不是聊天记忆；没有反馈的重跑是 retry。

**上屏**

- title: 反馈是循环的燃料
- content:
  - 最小通道：命令 → 退出码＋输出 → 落盘证据 → 下一动作。
  - 下一轮先读工件，再选动作。
  - 没有反馈的重跑，只是再抽一次卡。

**展开**：Aider 的形状：lint 非零 → 确认修复 → 错误回灌；数据管道读结构化 `run_results.json`，不解析自然语言输出。判据一：停止或继续不看上一轮结果的重试是 retry——有 feedback_ref 的迭代才是 loop。嵌套工具、retry、evaluator 都要纳入实际反馈路径。

**接到下一页**：燃料之外，这一级还要装两个保险丝。

### B14 · 兜底：无进展出口＋上限子句

**CLAIM**：没有兜底的续跑是烧钱——出口管质量，上限管资源，两个都要有。

**上屏**

- title: 兜底
- content:
  - 出口：连续 N 轮无改善／无工具调用，停。
  - 上限：轮次、时间、成本子句。
  - 只带上限的循环会硬跑到最后一轮。

**展开**：官方规格（evidence-b §4a）："If Claude keeps answering the evaluator without making progress… stops the loop"；`stop after 20 turns` 类子句只限消耗。上限不是质量分。

**接到下一页**：条件立好了——谁来判？

### B15 · 裁判五式选型

**CLAIM**：人判、清单、独立小模型、自判、审批方判定按场景选；干活模型自判是最弱一极，必须配保护与熔断。

**上屏**

- title: 裁判五式
- content:

| 裁判 | 适用 | 风险 |
|---|---|---|
| 人判 | 品味、探索 | 不可规模化 |
| 文件清单 | 目标可枚举 | 清单要保护 |
| 独立小模型 | 会话内目标 | 裁判自身可信度 |
| 自判 | 默认形态 | **最弱**——必须补偿 |
| 审批方判定 | 越界动作 | 可被操纵 |

**展开**：选型次序：优先机器可核；必须人判的，把判断点集中在门上（backbone §4.1）。

**接到下一页**：选完裁判，第一件事是保护它。

### B16 · 保护裁判四件

**CLAIM**：测试不可删改、清单用 JSON、裁判输入防操纵、只认原始证据。

**上屏**

- title: 保护裁判四件
- content:
  - 强措辞条款＋test-file hook 硬拦；清单选 JSON。
  - 分类器剥掉模型自述："reasoning-blind by design"。
  - 只认带运行 ID、版本与原始输出的证据。

**展开**：agent 修代码时不得削弱对代码的检查——promptfoo 反例：评估输出缺 `pass` 字段又无 threshold，score=0 仍可能默认放行；评估接口本身要 fail closed。

**接到下一页**：保护之外，门还有一个覆盖问题。

### B17 · 门要覆盖真实反馈路径

**CLAIM**：门存在不等于门覆盖——嵌套反馈路径要逐边标注哪道门管着它。

**上屏**

- title: 门要覆盖真实路径
- content:
  - 把嵌套路径画成图，逐边标 bound。
  - 区分 bypassed_bound 与 ineffective_bound。
  - 内层有 turn cap，不代表外层 retry 有限。

**展开**：IAL-Scan 的区分方法适用于任何嵌套 agent 结构：外层 evaluator/retry 无限时，内层的门形同虚设。基线带病、检查被跳过、该做的检查没安排——都是同族漏洞。

**接到下一页**：覆盖之外，裁判本身也要被测。

### B18 · 裁判要被单独校验

**CLAIM**：裁判分离只减利益冲突，不保证判对——校验集、判据版本和 fail-closed 接口是裁判自己的门。

**上屏**

- title: 校验裁判
- content:
  - 校验集：known-fail / ambiguous / adversarial / 人工冲突。
  - 记录 `judge_version / rubric_hash / false_accept / false_reject`。
  - 无效果阈值，不伪造统一放行线。

**展开**：独立 evaluator 仍可能被样本顺序、自我偏好、谄媚或 Goodhart 代理目标操纵（METR 的 monkeypatch/改时钟是压力样本，不外推发生率）。判据改版后，新旧分数不直接横比。

**接到下一页**：裁判给判之后，逐轮怎么走。

### B19 · 逐轮判断要改变下一步

**CLAIM**：未达成带理由继续、达成只认预设产出、不可能停并交人——判定及理由必须回到下一行动。

**上屏**

- title: 逐轮判断
- content:
  - Not yet met ＋ 理由 → 继续，理由指导下一轮。
  - Met ＋ 预设产出 → 停止候选。
  - Impossible → 停并交人；unknown/超时不强行归入。

**展开**：不是问模型「做完了吗」；是让判定接口的三值语义驱动控制流。unknown/timeout 通常保留为 blocked/awaiting_human。

**接到下一页**：这一档的专属事故，从这里开始。

### B20 · 专属事故：提前宣告完成

**CLAIM**：交出续跑后最大的敌人是提前宣告完成——「完成」住在哪一层，要追到驱动代码。

**上屏**

- title: 提前宣告完成
- content:
  - 文件多了、语气满了、测试绿了——都可能不是完成。
  - 官方示例驱动循环：唯一退出分支是轮数上限，默认无限。
  - 进度条给人看，驱动层不停机。

**展开**：Anthropic quickstart 源码（观测 2026-09-28）：`while True` ＋ `max_iterations` 分支；`count_passing_tests` 的结果只打印；「不可改测试」只在提示词。博客叙事里「goal 会自己完成」，代码里＝跑到你按 Ctrl-C。

**接到下一页**：防它有三层。

### B21 · 防它第一层：清单逐条判定

**CLAIM**：「整个项目做完了」没法判，「第 37 条通过」可以——只许改完成标记这一个字段。

**上屏**

- title: 第一层：清单
- content:
  - 目标拆成逐条可验证条目，全 `passes:false` 起步。
  - 每轮选最高优先级未完成项，先过基线。
  - 只许改 `passes` 字段；清单用 JSON。

**展开**：官方样例 200+ 条；官方失败模式原话 "declares victory on the entire project too early" / "marks features as done prematurely"——对策分别是设清单与端到端后才翻。

**接到下一页**：第二层管「通过」的成色。

### B22 · 防它第二层：端到端验证才翻完成

**CLAIM**：真实路径走通，单测和 curl 不算——翻「完成」的资格来自真实路径。

**上屏**

- title: 第二层：端到端
- content:
  - 浏览器自动化走真实用户路径。
  - 按钮点得动、页面出得来，才算。
  - 基线带病先修基线，不积新功能。

**展开**：每轮固定开场序列：定位目录 → 读 git log 与 progress → 选未完成项 → 先过基线 → 一次只做一件 → 干净收尾（描述性 commit＋progress 更新）。

**接到下一页**：第三层管绿灯的来源。

### B23 · 防它第三层：测试不可删改

**CLAIM**：删了测试，绿灯就没有意义——硬约束加钩子，不是提示词。

**上屏**

- title: 第三层：测试不可删改
- content:
  - 删、禁、放宽断言都算作弊。
  - test-file hook 硬拦＋强措辞条款。
  - 实战反例：agent 删除或禁用测试（Kent Beck 记录）。

**展开**：测试削弱检测关注 skip、删文件、断言降级、`|| true`。轮末核对清单：对比前后测试清单、列出基线失败与新失败、列出越界改动——出现异常先不翻完成。

**接到下一页**：事故防住之后，是出口与账本。

### B24 · Stop ≠ Accepted；三本账

**CLAIM**：控制状态、产出验收、外部结果三本账分开记——谁停的、谁验收的、结果谁在何时复查。

**上屏**

- title: 三本账
- content:
  - 控制账：`running/blocked/awaiting_human/stopped` ＋ `stop_reason`。
  - 验收账：`accepted_by ＋ evidence_link`。
  - 结果账：`outcome_status ＋ owner ＋ next_check`。

**展开**：建议状态机（本主题设计，非产品统一实现）：hard_deny→blocked；Met＋artifact→stopped_candidate；NotYet＋retryable→continue；unknown/timeout→awaiting_human。`stopped_candidate＋独立签署→accepted；accepted＋外部未见→outcome_pending`。多 feature 控制行是本主题试点，非行业标准。

**接到下一页**：停机的语义还要再拆。

### B25 · 资源上限是包络，不是质量分

**CLAIM**：覆盖不到嵌套路径的上限等于没有上限；耗尽先保全状态并交接。

**上屏**

- title: 资源包络
- content:
  - 轮次、wall clock、成本、retry budget、过期、无进展。
  - 嵌套路径（agent/tool retry/evaluator/scheduler）都要在包络内。
  - 耗尽前：persist state ＋ last feedback ＋ stop reason ＋ reviewer ＋ resume pointer。

**展开**：`RemainingSteps` 是框架机制实例，不是所有运行时的默认保证。Copilot 云端 agent 59 分钟硬超时、不可延长——产品实例，不通用。

**接到下一页**：包络烧尽或熔断触发，系统就会停——停了之后怎么办，是下一页。

### B26 · 停机不是统一语义，交接才是终点

**CLAIM**：为什么停、谁接手、从哪恢复——交接单答不全就不算升级；硬拒绝不能改名「待人批准」。

**上屏**

- title: 停机与交接
- content:
  - `deny_hard` → blocked，不可被普通审批覆盖。
  - `circuit_open` → awaiting_human。
  - 交接单：`feature_id/action/target/thread_id/decision_source/denial_reason/authorized_scope/reviewer/resume_pointer`。

**展开**：父线程必须能看到子线程请求；恢复后重核授权有效期，不继承上次对另一目标的批准。不可恢复错误四类清空目标（认证失败/额度耗尽/上下文溢出/模型不可用），其余错误重试若干次后暂停。

**接到下一页**：机器的部分讲完了——有一路输入不能断：你的。

### B27 · 人的反馈要留在环里

**CLAIM**：纠偏、品味、拒绝的理由回灌下一轮——完全静默不是目标；人的角色是最高处的判断，不是传话筒。

**上屏**

- title: 人的反馈留在环里
- content:
  - 方向纠偏、品味判断——机器判不了。
  - 拒绝的理由，要让下一轮看到。
  - 无人值守≠无人反馈：接手、验收、复查都是反馈。

**展开**：Ronacher 警告：无人值守循环里 "I'm not sure what my role even is… My role is reduced to that of a messenger"——人的反馈断掉后 done 失去含义。Ng 的 context advantage：人掌握模型不知道的业务上下文。技术风险：硬核玩家「放手也行」的隐性护栏不可见也不可迁移——详见文尾。

**接到下一页**：第三级——把「何时再跑」也交出去。

### B28 · 两种运行边界

**CLAIM**：会话内定时与跨会话持久是两种边界——醒来不等于达成。

**上屏**

- title: 两种运行边界
- content:
  - 会话内：`/loop` 固定或动态间隔（1 分钟–1 小时）；关会话即停。
  - 跨会话：云端调度；另配持久状态、取消、预算、接手。
  - 唤醒序列：wake → restore state → validate scope/budget → choose → run。

**展开**：Osmani："loops are session-scoped… /schedule runs it in the cloud."。触发器选型：`/goal`（条件）、`/loop`（时间）、Stop hook（脚本）、webhook/cron（外部）——轮内 auto mode 不等于启动下一轮。能 resume 只说明能接续会话，不说明 priority、权限和验收可见。

**接到下一页**：跨会话的第一件硬事——取消。

### B29 · 取消要传播到 worker

**CLAIM**：面板关闭不算停——调度器和运行中的进程都要收到取消，幂等与防重入要预先设计。

**上屏**

- title: 取消传播
- content:
  - 事故：面板已关，"the kill did not propagate to the actual tmux sessions"。
  - 核对三步：调度器不派新／worker 真退出／副作用停止。
  - 同一事件重复投递怎么办——幂等键预先设计。

**展开**：检查停止要核对三项，不是查开关。fork PR 触发会以 "Fork pull requests not supported" 失败（Cursor Automations 样本）——各平台失败出口不通用。

**接到下一页**：跨会话还要管钱和时间。

### B30 · 预算是花费阀不是完成

**CLAIM**：按会话计不等于跨次总额；被遗忘的循环要有过期时间；异常循环要有检测。

**上屏**

- title: 预算与过期
- content:
  - `"amount":"125"` 是 125 美分＝$1.25（Managed Agents 样本）。
  - 触顶 `budget_reached`：在途可稍超额，新消息 400；恢复原 session 可调预算。
  - 定时任务 7 天过期＋20 分钟兜底唤醒；doom-loop 检测默认关闭。

**展开**：会话状态 `idle/running/rescheduling/terminated`——预算暂停是 `idle`，不是完成也不是销毁。Copilot 59 分钟硬超时是不可延长硬顶。doom-loop 默认 observe@2/block@3/stop@6（OpenRouter 样本）——默认值不通用。

**接到下一页**：三级的护栏都见过了——升档怎么决定。

### B31 · 升档门禁

**CLAIM**：负例会红、裁判独立、熔断配齐，外加一次控制路径演练——缺一不可，不靠轮数说话。

**上屏**

- title: 升档门禁
- content:
  - 门会红吗：负例控制，没红过的门是摆设。
  - 裁判独立且判据可用：冲突时暂停自动验收与升档。
  - 熔断配齐＋控制路径演练：允许／需人批准／硬拒绝三条路都走通。

**展开**：升档前故障注入清单（文末控制实验 §10）：删测、改裁判输入、内层绕预算、token 变异、reviewer 不可达、outcome 不可见、人工冲突——每项都要给出 evidence link 和责任人。演练不通过就退回；退档信号：熔断频发、假把控复现、交接丢信息。

**接到下一页**：门禁之上还有两条岔路——不是必经之路。

### B32 · 支线 A：多主体编排

**CLAIM**：写入拓扑未收敛——共同问题只有避免冲突、合并与验证；改动者不能自行放行。

**上屏**

- title: 支线 A · 编排
- content:
  - 实例：编排器-工人（Anthropic）／受约束并发（Cognition）／各自 clone-push-merge（Carlini，16 代理 $20k）。
  - 共同问题：避免冲突、合并、独立验收。
  - 整树预算、写入所有权先配；验证器近乎完美才可行。

**展开**：Carlini："it's important that the task verifier is nearly perfect, otherwise Claude will solve the wrong problem."——大部分精力在验证器与环境。两条拓扑路线都真实，没有「正确拓扑」；可从有界任务直接进入，不以交唤醒为前置。

**接到下一页**：另一条岔路——让循环改自己。

### B33 · 支线 B：改进循环本身

**CLAIM**：四层权限：人改→代理建议→受控外围→自动改核心；自动改写判据仍未成熟，提案与应用必须分离。

**上屏**

- title: 支线 B · 元循环
- content:
  - 局部实例：工具描述改写（Anthropic，观测 2026-09-30）。
  - 未成熟：自动应用外围、自动改核心判据。
  - 提案与评估分离；改动可回滚、被评估。

**展开**：Morris 的 flywheel 说的是「人在环上修 harness」，不等于代理已获自改权；GEPA/DSPy 的提案-评估结构是参考，不是 coding-agent 效果证据。Shankar criteria drift 反例：判据漂移会让循环悄悄变味。

**接到下一页**：收尾之前，拆一个流传最广的传说。

### B34 · 高手的错觉

**CLAIM**：「完全放手也出色」的传闻，兜底的是看不见的护栏——你教别人放手时，对方复制的是行为，不是你的隐性裁判。

**上屏**

- title: 高手的错觉
- content:
  - 他的技术背景：目标在心里，对错一眼明。
  - 隐性裁判不可见——对持有者也是。
  - 抄行为＝抽卡：问题简单像行，复杂开盲盒。

**展开**：呼应开场那个故事——传说是真的，但燃料与护栏都要显性化。本场的 35 页，翻译成一句话：**把高手那套看不见的护栏，变成看得见、可测试、可交接的工件**。你自己「放手也行」的日子，是这些护栏（或你的隐性版本）在买单。教学含义：向别人推荐「放手」之前，先确认对方有没有你的兜底。

**接到下一页**：回去的第一步，不是配工具。

### B35 · 先定档，再爬

**CLAIM**：四问答不出就留在原级——那是控制决策，不是失败；逐档的检查表就是控制链。

**上屏**

- title: 先定档，再爬
- content:
  - 四问：谁启动／谁判完成／谁能改系统／出错谁接手。
  - 每档检查表：Goal/约束｜负例｜反馈工件｜判据版本｜三本账｜交接单。
  - 反过度工程：单次不建循环、存量库慎无限循环、门不可信不升、先有失控再治理。

**展开**：审计卡任一字段为空，保持更强的人在环。不可说：机制存在不等于 loop 已证明提升质量、吞吐或减少返工——那需要 P-outcome。Steinberger："usually I'm the bottleneck"——调度自动化收益有限，先把人和门摆对。逐档操作：《循环交接手册》。

**收束**：Loop Governance 的硬核不是让循环活得更久，而是继续、停止、升级和交还都留下能复查的理由。它是一门要锻炼的手艺——阶梯就是练法，从你站的那一级练起。

---

# 工程师追问卡（不上屏）

> 按 B 页提供可追问的机制、反例和边界。伪配置是本主题设计题，产品参数保留产品语境；`stop_conditions` 的「双环三层」仍是研究抽象，SOP 以 `03_practice/loop_governance/result/manual.md` 为准。

## B01–B04 · 钩子、故事与定档

- **B01**：完成钩子在何时检查、检查哪棵 tree、绑定哪份证据；可疑交付状态例 `PR created; CI failing; accepted_by=null; outcome_status=pending`。
- **B02 讲法**：故事只讲半分钟——成立的前提两条（模型强＋反馈进得来），全场就是要把它们工程化；「需要锻炼」说一次就够。
- **B03**：Ralph 无内建 stop，TODO 耗尽凭 taste；`/goal`/`/loop`/auto mode 分别是条件、时间/事件、轮内审批语义。
- **B04**：控制迁移事件字段 `goal_rev/action_id/evidence_ref/verdict/decision_source/state_rev/stop_reason/resume_pointer`——设计题非标准 schema。

来源：manual §7、§9–10；evidence-b §1、§4a–c。

## B05–B11 · 第一级

- **B05**：授权最小绑定 `{principal, action, target, branch, expires_at, nonce}`；`cron` 只唤醒，不代替授权。
- **B08**：edit 批准不自动覆盖 commit/push、另一分支或另一 feature；越权案例只有单用户反例，不外推发生率。
- **B10**：3/20 是 Claude auto mode 实例，官方明写不可配置；headless 直接终止；OpenAI 未公开相同阈值。
- **B11**：变异测试逐项改 `action/branch/target/expiry/nonce`，每次都应拒绝旧 token 并写 `authorization_drift` 事件；未合并 PR 只是候选机制。

来源：manual §2、§6–7、§9；backbone §3；evidence-f；evidence-u S4a；evidence-w W1。

## B12–B14 · 门票与燃料

- **B12**：`terminal_state + check + constraints + stop_clause` 四件套；Lighthouse 数字是个人实践例。
- **B13**：最小反馈通道 `cmd → exit_code + artifact → durable evidence_ref → next action`；无 evidence_ref 的「再跑一次」只是 retry；DAG 下游注意修复—震荡。
- **B14**：`/goal` 的 turn/time 子句、无进展停机均有官方规格；上限不是质量分。

来源：manual §2；evidence-b §4a；stop_conditions/01_machine_gates/insights #13。

## B15–B18 · 裁判

- **B15**：五式选型表在 manual §3（单一事实源）；人判 taste 见 Huntley（evidence-b §1）。
- **B16**：promptfoo 缺 `pass`/无 threshold 反例；hook 做法 playbook Test 节；`reasoning-blind by design`（evidence-b §4b）。
- **B17**：IAL-Scan 的 `bypassed_bound/ineffective_bound` 区分；嵌套路径逐边标 bound。
- **B18**：METR monkeypatch/改时钟是压力样本不外推；校验集四类＋判据版本化；Hamel/Shankar FAQ 是单源建议，无效果对照。

来源：stop_conditions/02_hard_caps/insights #15；03_verdict_split/insights #6–10；evidence-2026-09-28-m/n/r-*。

## B19–B23 · 出口与防线

- **B19**：状态机建议（hard_deny→blocked 等）是本主题设计；unknown 不归 Impossible。
- **B20**：quickstart 源码逐行（观测 2026-09-28）；`count_passing_tests` 只打印不停机。
- **B21**：feature_list 结构 `category/description/steps/passes`； initializer 展开；只许改 `passes`。
- **B22**：固定开场序列与基线修复（evidence-b 问题2§1）。
- **B23**：删测反例（evidence-i Beck）；测试削弱检测模式清单。

来源：manual §5、§10；backbone §1–2；digested/07；evidence-i Sources 3/5。

## B24–B26 · 三本账与包络

- **B24**：work-row 控制行试点字段与退出条件（manual §5）；多 feature 行仅当并行且交接丢信息时建。
- **B25**：不可恢复四类清空目标；其余错误重试后暂停；交接单字段全表（manual §7）。
- **B26**：`RemainingSteps` 是框架实例；Copilot 59 分钟硬超时（evidence-i Source 8）。

来源：manual §5/§7；backbone §2；digested/07；evidence-i。

## B27–B30 · 人的反馈与唤醒

- **B27**：Ronacher 无人值守证词（evidence-u S1）；Ng context advantage（digested/08）；Steinberger "usually I'm the bottleneck"（evidence-a，原话未说「自动化更慢」）。
- **B28**：唤醒序列 `wake → restore → validate → choose → run`；trigger 四类对照（manual §6）。
- **B29**：zombie 事故（evidence-o）；Cursor fork PR 失败出口（evidence-w W2）。
- **B30**：Managed Agents 预算语义与会话状态（evidence-w W3/W6）；7 天过期与 20 分钟兜底（evidence-b §4c）；doom-loop 默认关闭（evidence-o）。

## B31–B35 · 门禁、支线、尾巴

- **B31**：门禁三项＋演练（manual §9）；故障注入清单见文末控制实验 §10；退档信号（manual §11）。
- **B32**：Carlini C 编译器案例（evidence-u S3）；Cognition 受约束并发（S2）；Anthropic 编排器-工人（S2）；「不以交唤醒为前置」。
- **B33**：四层权限（00-map 支线 B 行）；工具描述改写（S5）；GEPA/DSPy 只作结构参考；Shankar criteria drift 反例。
- **B34**：抽卡＝retry 的口语版（判据一）；Osmani「别把品味和判断一起委托」；本页不点名真实人物。
- **B35**：审计卡字段（Goal/约束|负例|反馈|三本账|交接）；P-outcome 缺口（landscape §7）；Steinberger 反面声音。

---

# 可直接拆解的控制实验（不上屏）

> 一套可运行的演示设计，对应阶梯各级护栏。所有 YAML/JSON/伪代码都是本主题建议模板；进生产必须绑定项目权限、运行器和真实审计存储。产品参数只保留产品语境。

## 1. Goal / Eval 合约（第二级门票）

```yaml
id: search-pagination-v1
terminal_state:
  - page_2_opens
  - query_and_filters_survive_navigation
checks:
  - command: npm test -- search-pagination
    type: deterministic
  - command: npm run e2e -- search-pagination.spec.ts
    type: environment_path
constraints:
  branch: agent/search-pagination
  forbidden: [public_api_change, test_deletion, push]
stop:
  retryable: [page_2_button_click_failed, route_404]
  impossible: [required_dependency_unavailable]
  resource: [wall_clock, cost, retry_budget, expiry]
external_outcome:
  status: pending
  owner: product-owner-7
```

工程审查四问：终态可观察吗？检查覆盖实际路径吗？约束由运行器 enforce 吗？`impossible` 是逻辑不可满足还是暂时不可见？外部采用率不能填 `Met`。

## 2. Action authorization：把批准做成可失效对象（第一级护栏）

```json
{
  "token_id": "auth-0042",
  "principal": "search-agent",
  "action": "edit",
  "target": "src/search/**",
  "branch": "agent/search-pagination",
  "scope": ["src/search", "tests/search"],
  "expires_at": "2026-09-28T18:00:00Z",
  "nonce": "run-0042",
  "denied_actions": ["commit", "push", "deploy"]
}
```

**变异测试**：依次改 `action`→commit、branch→main、target→`deploy/`、时间→过期、nonce→下一轮；每次都应拒绝旧 token 并写 `authorization_drift` 事件。变异仍通过，不能升档。

## 3. Environment Feedback：证据通道而不是聊天文本

```text
run command
  ├─ exit_code
  ├─ stdout/stderr artifact
  ├─ browser trace / screenshot / network log
  └─ commit/tree identity
          ↓ durable evidence_ref
     evaluator input
          ↓ verdict + reasons
     next action or control state
```

最小事件：

```json
{
  "run_id": "run-0042",
  "action_id": "act-0042",
  "tree": "git:abc123",
  "exit_code": 1,
  "evidence_ref": ".loop/runs/run-0042/",
  "observed": ["page_2_button_click_failed"],
  "created_at": "2026-09-28T16:31:00Z"
}
```

下一轮只能消费带 `evidence_ref` 的观察；嵌套工具、retry、evaluator 都纳入实际 feedback path。

## 4. Eval schema：缺证据必须 fail closed

```json
{
  "verdict": "NotYet",
  "reasons": ["page_2_button_click_failed"],
  "evidence": [".loop/runs/run-0042/browser-trace.zip"],
  "evaluator": "search-checker-v3",
  "rubric_hash": "sha256:...",
  "input_digest": "sha256:..."
}
```

`verdict/reasons/evidence/rubric_hash` 缺一即拒绝；`Met` 无证据即拒绝；未知 verdict 不得降级成 true/false。promptfoo 缺 `pass`/无 threshold 反例说明评估器接口本身要测。

## 5. 裁判校验集与反操纵

```yaml
cases:
  - id: known-fail-route
    expected: NotYet
  - id: known-pass-route
    expected: Met
  - id: ambiguous-copy
    expected: human
  - id: adversarial-test-weakened
    expected: NotYet
  - id: human-conflict-01
    expected: record_conflict
record:
  judge_version: search-checker-v3
  rubric_hash: sha256:...
  false_accept: 0
  false_reject: 0
```

至少保留 known-fail、ambiguous、adversarial、人工冲突四类。`false_accept=0` 只是本批样本观察，不是质量证明；METR reward-hacking 样本说明独立 evaluator 仍可能被输入、时钟或代理目标操纵。

## 6. 控制状态机与决策表

```text
observe feedback
  ├─ hard_deny ------------------------→ blocked
  ├─ unknown / missing evidence -------→ awaiting_human
  ├─ NotYet + retryable + budget ------→ continue
  ├─ Met + artifact complete ----------→ stopped_candidate
  ├─ Impossible ------------------------→ stopped + escalate
  └─ budget exhausted ------------------→ stopped + checkpoint

stopped_candidate -- independent sign-off --> accepted
accepted --------- external observation --> outcome_pending / outcome_met
```

`Impossible` 必须区分「逻辑不可满足」和「当前没有观测」；后者是 blocked 或 awaiting_human。决策表每个分支都带 `reason`、`evidence_ref` 和下一责任人。

## 7. 资源包络与优雅耗尽

```yaml
budget:
  turns: task_specific
  wall_clock: task_specific
  cost_usd: explicit
  retry_budget: explicit
  deadline: explicit
  nested_paths: [agent, tool_retry, evaluator, scheduler]
checkpoint_before_exhaustion: true
on_exhaustion:
  - persist_state
  - persist_last_feedback
  - write_stop_reason
  - assign_reviewer
  - emit_resume_pointer
```

`max_turns` 只覆盖一个维度；evaluator 或 tool retry 在预算外重调仍可能无限运行。耗尽不是验收通过，优先保全状态并交接。

## 8. 拒绝与审批恢复演练

```yaml
deny_retryable:
  record_reason: true
  next: choose_safe_alternative
  max_retries: project_defined
deny_hard:
  next: blocked
  approver_can_override: false
circuit_open:
  next: awaiting_human
  requires: [reviewer, last_action, evidence_ref, resume_pointer]
```

演练三条路径：允许；拒绝后带理由换安全路径；硬拒或熔断。父线程必须能看到子线程最后状态，reviewer 必须能从同一状态恢复。

## 9. 长任务 ledger：不要把三种状态压成 done

```json
{
  "feature_id": "search-42",
  "control": {
    "status": "awaiting_human",
    "stop_reason": "policy_denial",
    "last_action_id": "act-0042",
    "resume_pointer": "run-0042/action-0043"
  },
  "acceptance": {
    "status": "unaccepted",
    "accepted_by": null,
    "evidence_link": null
  },
  "outcome": {
    "status": "pending",
    "owner": "product-owner-7",
    "next_check": "2026-09-29T09:00:00Z"
  },
  "priority": {"old": 2, "new": 1, "changed_by": "release-lead", "reason": "release dependency"}
}
```

本主题建议的控制行，不是公开统一标准。单任务 progress 和 git history 不能自动回答 priority、授权史、阻塞原因和验收人四列。

## 10. 升档前故障注入清单

```text
[ ] 删除/削弱测试：机器闸门是否失败？
[ ] 修改 evaluator 输入：是否被拒绝并记录？
[ ] 让内层 retry 绕过 budget：是否被外层包络拦住？
[ ] 让 token 换 branch/action/expiry：是否重新授权？
[ ] 让 reviewer 入口不可达：是否进入 blocked 而非假升级？
[ ] 让外部 outcome 不可见：是否保持 outcome_pending？
[ ] 让人工与 evaluator 冲突：是否停止自动升档并保留样本？
```

这份清单验的是控制链能否拒绝已知坏路径，不证明业务质量、收益或组织可规模化。每项都有 evidence link、stop reason 和责任人，才有资格讨论减少逐轮值守。

## 11. 从示意 YAML 泛化成项目控制面

| 语义不变量 | 搜索案例字段 | CI / 数据管道 / 发布系统的可能映射 |
|---|---|---|
| 目标与终态 | `terminal_state` | build artifact ready / DAG partition complete / release candidate healthy |
| 路径与动作约束 | `constraints`, `scope` | 允许目录 / 允许表分区 / 允许环境与变更类型 |
| 环境事实 | `evidence_ref`, `exit_code`, trace | test report / run manifest / deploy health events |
| 判定 | `verdict`, `reasons`, rubric | gate result / data-quality rule / canary policy |
| 继续资格 | `retryable`, budget remaining | retry class / backfill budget / rollback window |
| 停止原因 | `stop_reason` | failed gate / budget exhausted / policy denied / human pause |
| 权威与责任 | `accepted_by`, reviewer | release approver / data owner / on-call |
| 恢复 | `resume_pointer`, checkpoint | rerun key / partition cursor / rollback or resume version |
| 外部结果 | `outcome.owner`, `next_check` | adoption / freshness / incident-free window |

**先分三层，不要把整份 YAML 当通用标准**：控制不变量（跨领域保留：目标可观察、证据可追溯、判定有理由、停止原因独立、验收有权威、升级可恢复）／承载结构（可变：YAML、JSON、数据库行、事件流、CI artifact）／领域策略（不可直接搬运：阈值、重试次数、谁审批、什么算不可修复）。

**迁移规则**：①先写领域终态与不可变约束，不复制 goal.yaml；②控制动作映射为领域事件；③判定绑定 evidence、判据版本、责任来源；④明确缺证据/未知/拒绝/耗尽是否 fail closed；⑤用领域特有坏样本做负例；⑥演练恢复（进程重启、权限过期、上游延迟、人工冲突）；⑦最后才决定承载。

**三个迁移例子**：

```text
CI：build artifact + test report → gate verdict → retry / block / release approval
数据管道：partition manifest + quality report → freshness/completeness verdict → backfill / pause / owner review
发布：canary health + rollback checkpoint → policy verdict → continue rollout / rollback / incident handoff
```

共享控制语义，不共享阈值、判据或恢复动作。`p95 < 300ms`、`3 次拒绝`、`10 轮` 必须由领域风险、成本和历史基线决定；没有基线只能标待定。

## 12. 两个领域的完整迁移例子

### A. 数据管道：从「页面完成」换成「分区可交付」

```yaml
terminal_state: partition=2026-09-28 is complete and queryable
constraints: do_not_overwrite certified partitions; source schema unchanged
feedback: run_manifest + row_count + null_rate + freshness_timestamp
verdict: quality_gate_version=12
continue: retry transient source read or backfill missing partition
stop: certified or budget exhausted
escalate: schema drift / owner decision required
accepted_by: data_owner
resume_pointer: dag_run=...; partition=...
outcome_pending: downstream dashboard freshness not yet observed
```

领域负例不是「按钮坏了」，而是：row count 为零、freshness 超期、schema drift、已认证分区被覆盖——每个负例都要确认同一质量门会失败，且失败原因能回到下一步。

### B. 发布系统：从「产出验收」换成「风险可控地推进」

```yaml
terminal_state: canary meets release policy for the observation window
constraints: deploy only approved artifact; no production schema migration
feedback: health events + error budget + rollback checkpoint
verdict: canary_policy_version=7
continue: expand rollout within authorized slice
stop: policy met, then release_approver signs
escalate: error budget breach / rollback unavailable / conflicting verdict
accepted_by: release_approver
resume_pointer: rollout_id + last healthy checkpoint
outcome_pending: incident-free window not yet complete
```

发布系统的 `stop` 不是「部署命令返回 0」；可能是回滚、暂停或等待观察窗。领域负例：部署成功但错误率超预算、artifact digest 不在批准清单、rollback checkpoint 不可恢复。

## 13. 泛化验收：用变换而不是改名检查

1. **换领域**：同一控制语义映射到数据管道和发布系统，能否说清终态、事实、判定、出口、责任和恢复？
2. **换承载**：YAML 改成数据库事件或 CI artifact，审计信息仍可追溯吗？
3. **换失败类型**：权限过期、外部依赖延迟、判据版本漂移、人工冲突——状态仍能区分 `blocked/stopped/accepted/outcome_pending` 吗？

只替换字段名、没定义领域终态/负例/恢复动作的「泛化」是假的。每换一个领域都能保留控制不变量、重写领域策略、并用负例让门失败，才是**语义泛化**。
