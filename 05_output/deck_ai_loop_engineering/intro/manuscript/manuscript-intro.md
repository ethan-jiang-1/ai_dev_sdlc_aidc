---
title: 文稿 — Loop Engineering 入门场
status: draft-for-review
source: intro/outline/outline-intro.md
revised: 2026-09-28
---

# 文稿 — 入门场

> 本稿与 [`../outline/outline-intro.md`](../outline/outline-intro.md) 同步。每页 `CLAIM` 必须与 outline 的 subtitle 完全相同；引用块不上屏，只给讲者和做片方。

## 术语

目标（Goal）｜边界（scope）｜行动（Action）｜环境反馈（Environment Feedback）｜评估（Eval）｜继续（Continue）｜停止（Stop）｜交还（Escalate）｜验收（Accepted）｜外部结果待观测（Outcome pending）。

---

### I01 · 它说做完了

**CLAIM**：你离开后它继续跑，回来听到“完成”；真正的问题是这句话凭什么可信。

**上屏**

- title: 它说做完了
- subtitle: 你离开后它继续跑，回来听到“完成”；真正的问题是这句话凭什么可信。
- content · 必须写出：
  - 你离开了，系统继续工作。
  - 你回来，它说：完成。
  - 先别问它聪不聪明，先问：凭什么信？

**展开**：这场不从“Agent 能做什么”开始，而从一个交付现场的风险开始：停下来的东西，未必已经做完。

**接到下一页**：要回答“凭什么信”，先把一轮里面发生的事情画出来。

---

### I02 · Loop 不是一圈箭头，是一条控制链

**CLAIM**：一轮从目标和边界出发，经行动、环境反馈、评估，走向继续、停止或交还。

**上屏**

- title: Loop 不是一圈箭头，是一条控制链
- subtitle: 一轮从目标和边界出发，经行动、环境反馈、评估，走向继续、停止或交还。
- content · 必须写出：
  - Goal / 边界：要做到什么，不能动什么？
  - Action → Feedback → Eval：做了什么，环境返回什么，按什么判断？
  - Continue / Stop / Escalate：继续、停下，还是交给人？

**展开**：这是本场的研究抽象，不是某位 KOL 的原话。吴恩达的三环适合解释反馈如何在编码、开发者和真实用户之间回流；今天我们把镜头拉近到一轮运行。

**接到下一页**：没有目标和边界，“完成”就没有对象。

---

### I03 · 先给 Goal，再谈完成

**CLAIM**：没有可观察的目标、范围和不可变约束，循环没有可以验收的完成对象。

**上屏**

- title: 先给 Goal，再谈完成
- subtitle: 没有可观察的目标、范围和不可变约束，循环没有可以验收的完成对象。
- content · 必须写出：
  - 目标：要达到的可观察终态。
  - 检查：用什么命令、结果或证据确认它？
  - 约束：路径上什么不能改变？

**展开**：把“把搜索做得更好”改成“固定数据集上 p95 延迟低于 300ms，公共 API 不变，并运行 benchmark”。前者是愿望，后者才有可能进入循环。

**边界**：Goal/eval 的构造方法属于上游 `agent_goal_eval`；本场只说明它必须成为循环的起点。

**接到下一页**：有了目标，系统这一轮到底可以做什么？

---

### I04 · Action 不是固定自动化

**CLAIM**：系统可以在目标和授权边界内选择下一步；自动触发仍可叠加，不是旧自动化被新东西取代。

**上屏**

- title: Action 不是固定自动化
- subtitle: 系统可以在目标和授权边界内选择下一步；自动触发仍可叠加，不是旧自动化被新东西取代。
- content · 必须写出：
  - 固定自动化：步骤由人排好，到点执行。
  - loop：根据当前目标和反馈选择下一步。
  - 选择权不等于无限权限：本轮授权仍有范围、对象和期限。

**展开**：一个定时任务可以没有自主选择；一个 loop 也可以被时间或事件唤醒。不要讲成“新自动化取代旧自动化”。

**接到下一页**：选择了动作之后，下一步的依据从哪里来？

---

### I05 · Feedback 必须来自环境事实

**CLAIM**：工具结果、测试、构建或真实路径返回的事实，必须改变下一步；不看上一轮结果的重跑只是重试。

**上屏**

- title: Feedback 必须来自环境事实
- subtitle: 工具结果、测试、构建或真实路径返回的事实，必须改变下一步；不看上一轮结果的重跑只是重试。
- content · 必须写出：
  - Action 产生环境事实：退出码、结果文件、页面行为、拒绝理由。
  - 下一轮必须读到这条事实。
  - 不看结果只再跑一次，是 retry，不是 feedback loop。

**展开**：反馈不是模型说“我试过了”，而是环境给出能复查的结果。

**接到下一页**：环境返回事实，还需要一个判定者解释它是否满足目标。

---

### I06 · Eval 不是 Feedback

**CLAIM**：反馈是环境返回什么，评估是按什么判据解释它；检查要事先写好、机器能判，且不能只靠执行方自述。

**上屏**

- title: Eval 不是 Feedback
- subtitle: 反馈是环境返回什么，评估是按什么判据解释它；检查要事先写好、机器能判，且不能只靠执行方自述。
- content · 必须写出：
  - Feedback：环境说发生了什么。
  - Eval：这是否满足 Goal？
  - 证据：判据、输入、执行位置和签署权都要能复查。

**展开**：测试结果是反馈；“所有目标条件满足”是评估结论。一个能写代码的执行方，不应独自定义、修改、执行并签署自己的验收。

**接到下一页**：评估之后，系统不是只有“通过/失败”两个出口。

---

### I07 · 继续、停止、升级不是同一个出口

**CLAIM**：未满足但可继续就继续；满足预设产出才可停止候选；不可判、高风险、拒绝或无恢复路径就交人。

**上屏**

- title: 继续、停止、升级不是同一个出口
- subtitle: 未满足但可继续就继续；满足预设产出才可停止候选；不可判、高风险、拒绝或无恢复路径就交人。
- content · 必须写出：
  - Continue：反馈指出可修复缺口，下一步有资格执行。
  - Stop：预设产出满足，进入验收，不是自动完成。
  - Escalate：无法判定、风险越界、持续拒绝或无法恢复，交给人。

**展开**：把“没通过”拆开：有些是继续修，有些是停下保全状态，有些是交人。出口不同，状态和责任也不同。

**接到下一页**：最容易犯的错，是把所有停下都叫完成。

---

### I08 · Stop ≠ Accepted

**CLAIM**：超时、资源耗尽、无进展或模型自己收尾，都只说明控制流停了，不说明产出已验收。

**上屏**

- title: Stop ≠ Accepted
- subtitle: 超时、资源耗尽、无进展或模型自己收尾，都只说明控制流停了，不说明产出已验收。
- content · 必须写出：
  - `stopped`：控制流停了。
  - `accepted`：预设产出通过验收。
  - 两者不是同一字段，也不是同一证据。

**展开**：硬上限是资源保护，不是质量分。到时间停下来的东西，可能接近完成，也可能完全错误；不能因为它停了，就替它签完成。

**接到下一页**：如果状态不分开，长任务最后只剩一句“还在跑”或“已完成”。

---

### I09 · 状态和结果要分账

**CLAIM**：`running`、`blocked`、`awaiting_human`、`stopped` 是控制状态；`accepted` 是预设产出验收，`outcome_pending` 是外部结果尚不可见。

**上屏**

- title: 状态和结果要分账
- subtitle: `running`、`blocked`、`awaiting_human`、`stopped` 是控制状态；`accepted` 是预设产出验收，`outcome_pending` 是外部结果尚不可见。
- content · 必须写出：
  - 控制状态：现在循环处于什么处置状态？
  - 产出状态：预设交付物是否验收？
  - 外部结果：真实用户/业务结果是否已经观测？

**展开**：日志能记录发生过什么，但不自动回答谁批准、谁改了优先级、卡在哪里、谁验收。更不能把“PR 已生成”说成“业务成功”。

**接到下一页**：状态和结果混在一起，最典型的后果就是提前宣告完成。

---

### I10 · 第一类失败：提前宣告完成

**CLAIM**：文件变多、语气很满、能打开的空壳，都不是完成证据；目标敌人是“尚未完成却被标为完成”。

**上屏**

- title: 第一类失败：提前宣告完成
- subtitle: 文件变多、语气很满、能打开的空壳，都不是完成证据；目标敌人是“尚未完成却被标为完成”。
- content · 必须写出：
  - 文件多了，不等于目标满足。
  - 回复完整，不等于环境状态正确。
  - 能打开的空壳，不等于功能完成。

**callout**：过早地宣布胜利。——Anthropic 官方失败模式

**展开**：不要把它归结成“模型撒谎”。它是控制设计问题：完成宣告、验收证据和外部结果被压成了同一个信号。

**接到下一页**：停止三件骨架，正是把这三个信号拆开。

---

### I11 · 三件停止骨架各管一件事

**CLAIM**：机器闸门拦已知错误；硬上限只管资源熔断；验收与干活分离；三件不能合成一句“它停了”。

**上屏**

- title: 三件停止骨架各管一件事
- subtitle: 机器闸门拦已知错误；硬上限只管资源熔断；验收与干活分离；三件不能合成一句“它停了”。
- content · 必须写出：
  - 机器闸门：这轮的环境事实是否通过？
  - 硬上限：系统还允许继续消耗资源吗？
  - 验收分离：谁有资格签署完成？

**展开**：三件骨架是控制内核。停止条件专项深挖里的“双环三层”是研究抽象；本场只讲已经收敛的三件分工，不把它说成统一行业标准。

**接到下一页**：能不能少守，不能靠一句“测试通过”判断；先用负例验证门真的会失败。

---

### I12 · 负例控制决定能不能少守

**CLAIM**：把已知错误放进链路；如果门拦不住，普通动作也不能自动放手。负例只证明一个必要条件，不单独证明质量或业务成功。

**上屏**

- title: 负例控制决定能不能少守
- subtitle: 把已知错误放进链路；如果门拦不住，普通动作也不能自动放手。负例只证明一个必要条件，不单独证明质量或业务成功。
- content · 必须写出：
  - 放入一个已知错误。
  - 检查必须明确失败，并把原因传回下一轮。
  - 失败 ≠ 真实质量已证；只是说明门没有完全失灵。

**展开**：这是必要条件，不是充分条件。还要同时看反馈是否驱动停续、验收是否独立、停止后能否交接。

**接到下一页**：所以人不是被移出所有判断，而是留在几个控制关口。

---

### I13 · 人要守的是控制关口

**CLAIM**：高风险动作、说不清的目标、拒绝后的接手、最终验收和外部结果；人不是被移出循环，而是从机械 QA 转到上下文和责任判断。

**上屏**

- title: 人要守的是控制关口
- subtitle: 高风险动作、说不清的目标、拒绝后的接手、最终验收和外部结果，仍需要人承担判断和责任。
- content · 必须写出：
  - 风险动作：执行前看清对象、范围和风险。
  - 歧义目标：先补上下文或缩小目标。
  - 拒绝/熔断：有人接、看得见、能恢复。
  - 最终验收：产出和外部结果分开签。

**展开**：人从逐轮机械 QA 移到上下文、授权、责任和产品判断，不等于人退出。

**接到下一页**：不是所有工作都值得建立这套控制链。

---

### I14 · 什么时候不要自动继续

**CLAIM**：一次就能做完的任务不必建循环；完成条件写不成可观察的句子，就拆小、人工标样或交人，不靠增加轮次硬跑。

**上屏**

- title: 什么时候不要自动继续
- subtitle: 一次就能做完的任务不必建循环；完成条件写不成可观察的句子，就拆小、人工标样或交人，不靠增加轮次硬跑。
- content · 必须写出：
  - 一次性小任务：直接做，不建循环脚手架。
  - 可拆成小目标：先缩小，再设检查。
  - 外部结果不可见或标准漂移：交人/待观测，不伪造自动完成。

**展开**：没有可观察条件，不是多跑几轮就会变清楚；探索可以继续，但验收责任必须留在可见的人或上级环。

**接到下一页**：最后不是记住一个口号，而是回去审计一条真实链路。

---

### I15 · 回去先做控制链审计

**CLAIM**：写 Goal/边界 → 定义可观察 Eval 和一个已知错误 → 接入真实 Feedback → 分开 Stop 与 Accepted → 演练升级和恢复；前置失败就保留逐轮值守。

**上屏**

- title: 回去先做控制链审计
- subtitle: 写 Goal/边界 → 定义可观察 Eval 和一个已知错误 → 接入真实 Feedback → 分开 Stop 与 Accepted → 演练升级和恢复；前置失败就保留逐轮值守。
- content · 必须写出：
  - 先写目标、边界和不能改变的东西。
  - 再用负例验证 Eval 会失败。
  - 再检查停、交人、恢复后的状态是否可见。
  - 最后才讨论减少逐轮值守。

**展开**：这场不证明更快、更好或更省人。它只给出一个判断：当控制链不能被审计，就不要把人的逐轮判断拿走。

**收束**：Loop Engineering 的硬核部分，不是让系统跑得更久，而是让每次继续、停止、升级和交还都有依据。

---

# 讲者硬核备课卡（不上屏）

> 本节补充每页可追问的实战材料，不增加页面。示例中的搜索任务和数值是本主题示意，不是厂商实测；产品参数只按对应产品实例讲，不当通用阈值。Goal/Eval 的构造方法权威在 `02_research/agent_goal_eval/`，本稿只讲它如何接入 loop 控制。

## I01 · 它说做完了

- **状态例子**：`PR created; CI failing; accepted_by=null; outcome_status=pending`。这比一句“搜索完成”更诚实：产出已生成，但没有验收签署，外部采用率也没有观测。
- **真实对照**：`stop_conditions/03_verdict_split/practices.md` 的 dotnet PR 案中，Agent 两次自称 fixed，CI 至少一次证伪；这是反例，不是发生率结论。
- **追问**：完成钩子检查的是哪棵工作树、哪个版本、哪次证据？

## I02 · 控制链

- **贯穿例子**：`goal=搜索路径可用 → action=改分页 → feedback=浏览器第2页按钮无效 → eval=未满足 → continue=修路由`。
- 这是本场研究抽象，不是某产品固定状态机；真正实现还必须记录 `goal_rev / action_id / evidence_ref / verdict / decision_source / state_rev`。
- **边界**：画出链条不等于产品已经实现全部节点。

## I03 · Goal

- **弱写法**：`Improve the search experience until it feels good.`
- **可核写法**：终态、检查、约束、停止语句四件套；例如 Lighthouse ≥92、LCP<1.8s、不改 hooks API、连续两轮无改善 abort、最多 10 轮。这是 Osmani 的实例，数字不可外推。
- **追问**：若业务指标不可观测，结论只能是 `outcome_pending`，不能自动 `Met`。

## I04 · Action

- 同一个动作拆三把钥匙：`trigger=CI failure`、`choice=读日志选修复`、`authorization=仅当前分支编辑，不含 push`。
- 触发器唤醒不等于获得无限权限；动作、目标、分支和有效期变化，必须重新授权。
- 沙箱和单次动作约束属于 harness；本场只讲它们如何成为下一轮的资格条件。

## I05 · Feedback

- 示意管道：`cmd → exit_code + stdout/stderr artifact → durable evidence_ref → next action`。
- Aider 的形状是非零 lint → 询问是否修复 → 将 lint 错误回灌下一轮；如果输出滚走、下一轮只重复命令，就没有真正消费反馈。
- 数据工程例应读取结构化 `run_results.json` 的状态和失败数，并注意 DAG 下游的修复—震荡；不要只解析自然语言终端输出。

## I06 · Eval

- 同一个 `test exit=0` 只是反馈；Eval 还要核页面路径、API 约束和测试保护。
- `/goal` 的三值可讲成：`Not yet met + reason → continue`、`Met + evidence → acceptance candidate`、`Impossible → stop/escalate`。独立小模型只核预设硬规则，不自动判断内容品味。
- **失败例**：评估输出漏掉必需的 `pass` 字段又没有 threshold，score=0 仍可能默认放行；判定接口也要 fail closed。

## I07 · 三出口

- `Not yet met + known repair` → continue；`Met + evidence` → 停止候选并验收；认证失败、策略硬拒绝或审批入口不可达 → `blocked/awaiting_human`。
- 单次拒绝可带理由继续寻安全路径；不要把一次拒绝直接讲成熔断。
- `Impossible` 是条件逻辑上不可满足，不是“业务指标暂时看不到”。

## I08 · Stop ≠ Accepted

- 对照记录：`stop_reason=turn_limit; accepted_by=null` 与 `stop_reason=goal_gate; accepted_by=reviewer; evidence_link=CI run` 是两种不同状态。
- `/goal` 的 `stop after 20 turns` 只限制消耗；`/loop` 的 fallback/过期只控制循环寿命。产品参数不能变成行业刻度。
- 手册要求 `stop_reason` 和 `accepted_by/evidence_link` 分开记录。

## I09 · State / Outcome

- 本主题建议的虚构记录：`feature_id=search-42; status=blocked; stop_reason=human_pause; accepted_by=null; outcome_status=pending; owner=业务负责人; next_check=下周`。
- 进度文件和 git history 能帮助恢复工作，但不天然回答授权史、优先级变更、阻塞原因、验收人四列。
- 多 feature 控制行是本主题试点，不是已证明有效的行业标准。

## I10 · 提前完成

- Anthropic feature list 初始所有 `passes:false`；只有端到端浏览器验证后才翻 `true`。单测或 curl 通过、按钮仍不可用时不能翻。
- Kent Beck 的实战反例是 Agent 删除或禁用测试；因此“测试通过”还要问测试是否被削弱。
- 这防的是提前完成的一类形态，不等于业务结果已达成。

## I11 · 三件停止骨架

- `test exit=1` → 机器拒绝；`turns=10/10` → 资源熔断并保留状态；`test exit=0 + independent verifier` → 才是验收候选。
- 机器闸门、硬上限、验收分离分别回答“这一轮过不过”“还允许消耗吗”“谁能签收”。不能合成“它停了”。
- `stop_conditions/README.md` 的“双环三层”是专项提炼，尚未回流判定层，本场不把它说成行业架构。

## I12 · 负例控制

- 做一次故障注入：故意把搜索断言改成错误期望或植入 dummy API key，运行同一 `make check`；必须得到非零、明确原因并回到下一轮。
- 测试削弱检测器关注 skip、删文件、断言降级、`|| true` 等模式。
- 负例通过只证明这类已知错误能被拦，不证明漏做需求、真实质量或业务成功。

## I13 · 人的关口

- 人保留在危险动作、模糊目标、拒绝/熔断恢复、最终验收和外部业务结果。
- Ng 的“context advantage”解释的是人为什么仍在环：人掌握模型不知道的用户、业务和场景信息；不是人必须继续做每轮机械 QA。
- 没有审批入口、指定 reviewer 和 resume pointer，不能声称“已经升级给人”。

## I14 · 不要自动继续

- 小改文案拼写：一次做完，不建循环脚手架。
- “UI 直到好看”：先人工标样、拆成可核局部目标或交人；不要靠更多轮次逼出品味。
- 标准漂移、外部结果不可见、判据无法写出时，分别走拆小、待观测、人工核对三条路。

## I15 · 回去审计

让听众对真实任务填一张卡：`Goal/Scope | check+negative_control | feedback_link | stop_reason | accepted_by+evidence_link | outcome_owner+next_check | escalation_reviewer+resume_pointer`。缺可观察 Goal、负例拦不住、或升级不可达，就保留逐轮值守。

**不能说**：这些机制已证明更快、更好、更省人。它们首先证明的是“能否建立可治理的控制链”。

---

# 一套可以现场拆开的实战样本（不上屏）

> 下面是一个完整的虚构样本：给站内搜索增加分页。样本的价值是把每个控制节点落成工件；其中数值、分支名和命令都是演示模板，不是厂商默认值，也不是实测收益。

## 1. Goal 工件：先把“做完”写成可判定对象

```json
{
  "goal_id": "search-pagination-v1",
  "terminal_state": "结果列表第二页可打开、可返回、查询条件不丢失",
  "checks": [
    "npm test -- search-pagination",
    "npm run e2e -- search-pagination.spec.ts"
  ],
  "constraints": [
    "只改 search 分支",
    "不得修改公共 API",
    "不得删除或放宽既有测试"
  ],
  "stop_clause": "两次连续无改善或达到项目资源上限时停止并保全状态",
  "outcome": "用户采用率另行观测，不作为本轮自动 Met"
}
```

讲者要指出四个细节：终态不是“搜索体验变好”；检查不是“模型觉得可以”；约束不是备注而是不可越过的边界；用户采用率不在当前运行中可见，所以只能是 `outcome_pending`。

## 2. Action 工件：每次只拿一张可审计的动作单

```json
{
  "action_id": "act-0042",
  "principal": "search-agent",
  "action": "edit",
  "target": "src/search/pagination.ts",
  "branch": "agent/search-pagination",
  "scope": ["src/search", "tests/search"],
  "expires_at": "2026-09-28T18:00:00Z",
  "approval": "reviewer-17",
  "denied": ["commit", "push", "public-api-change"]
}
```

把 `edit` 改成 `push`、把 branch 改成 `main`、把目标移到 `deploy/`，都应被当成新动作重新审批。一次批准不能靠文字相似度继承。

## 3. Feedback 工件：把环境返回物落盘

```sh
set -o pipefail
mkdir -p .loop/runs/run-0042
npm run e2e -- search-pagination.spec.ts \
  > .loop/runs/run-0042/stdout.log \
  2> .loop/runs/run-0042/stderr.log
status=$?
printf '{"run":"run-0042","exit_code":%s,"commit":"%s"}\n' \
  "$status" "$(git rev-parse HEAD)" \
  > .loop/runs/run-0042/result.json
exit "$status"
```

这个模板故意保存退出码、标准输出、错误输出和 commit。下一轮不是重新问“刚才发生什么”，而是先读 `result.json`，再读失败日志，最后选择动作。命令形态需按项目 shell 和 CI 改写，不能把这段当通用安全脚本。

## 4. Eval 工件：反馈和判定分开

```json
{
  "eval_id": "eval-0042",
  "goal_id": "search-pagination-v1",
  "evidence": [
    ".loop/runs/run-0042/result.json",
    ".loop/runs/run-0042/stderr.log"
  ],
  "verdict": "NotYet",
  "reasons": ["page_2_button_click_failed"],
  "evaluator": "search-checker-v3",
  "rubric_hash": "sha256:...",
  "missing_fields_are": "reject"
}
```

`exit_code=0` 只是一个环境事实；`verdict=Met` 还必须覆盖页面路径、API 约束和测试保护。评估器输出缺少 `verdict` 或 `evidence` 时，本模板选择拒绝，而不是猜测通过。

## 5. 状态迁移：停止、验收、业务结果必须拆开

```text
running
  ├─ feedback=NotYet, retryable ───────→ running
  ├─ feedback=Met, artifact complete ──→ stopped_candidate
  ├─ hard limit / no progress ─────────→ stopped
  ├─ permission / dependency ───────────→ blocked
  └─ ambiguity / reviewer needed ───────→ awaiting_human

stopped_candidate + independent sign-off → accepted
accepted + external metric unseen       → outcome_pending
```

必须能回答：“为什么停？”“谁验收？”“验收依据在哪？”“外部结果谁在什么时候复查？”因此示意记录不能只写 `status=done`。

## 6. 负例演练：先证明门会拒绝

在正常运行前临时把分页断言改成错误期望，或在测试中植入一个 dummy API key，然后运行同一个 `make check`。合格的反馈至少包含：非零退出码、明确失败位置、对应 evidence link、下一轮可读的修复理由。恢复负例后再跑正常路径。

负例通过只证明这一类已知错误能被拦住；它不能证明遗漏需求、真实用户满意或业务指标已改善。若门没有失败，先停止升档，不要用“模型通常做得不错”补证据。

## 7. 熔断交接单：人真正接得住才叫升级

```yaml
feature_id: search-42
state: awaiting_human
stop_reason: policy_denial
last_action: edit src/search/pagination.ts
last_feedback: page_2_button_click_failed
accepted_by: null
evidence_link: .loop/runs/run-0042/result.json
reviewer: product-owner-7
resume_pointer: run-0042/action-0043
next_check: 2026-09-29T09:00:00Z
```

`reviewer` 为空，或 `resume_pointer` 指不到状态和证据，就不能对外说“已升级”。硬拒绝也不能改名成“等待审批”；它是 `blocked`，恢复路径由权限负责人决定。

## 8. 现场审计顺序

1. 先拿 `goal.json`，问终态、约束和检查是否可观察。
2. 再拿动作单，问这次授权是否覆盖当前目标、分支和动作。
3. 再读反馈 artifact，问下一轮是否真的消费了它。
4. 再读 eval，问判据版本、证据和裁判是否独立。
5. 最后看状态、验收和外部结果是否分账。

任何一项答不上来，都保留逐轮人工判断。这里的“保留人工”是控制决策，不是失败。

## 9. 这套 YAML 怎么泛化

这些字段不是行业标准，也不是要求团队照抄的协议。泛化时不要从字段名出发，而要从控制问题出发：

| 控制问题 | 示例字段 | 换到别的系统仍要保留的语义 |
|---|---|---|
| 要达到什么 | `terminal_state` | 可观察的产出终态 |
| 不能做什么 | `constraints` | 不可越过的范围、对象和路径约束 |
| 凭什么判断 | `checks` / `evidence` | 外部可复查的证据和判据 |
| 谁能做什么 | `approval` / `scope` | 动作、目标、有效期和授权主体 |
| 为什么下一步这样走 | `verdict` / `reasons` | 判定及其理由能回到下一行动 |
| 现在停在哪里 | `state` / `stop_reason` | 控制状态与停止原因分开 |
| 谁接手、怎么恢复 | `reviewer` / `resume_pointer` | 责任人、恢复位置和所需证据 |
| 产出是否真的带来结果 | `outcome_status` | 外部结果独立于产出验收 |

迁移到 CI、数据管道、客服工单或发布系统时，可以改字段名，甚至改存储方式；但不能删掉这些语义。反过来，如果一个系统有很多字段，却回答不了“谁验收、为什么停、怎么恢复”，它并没有因为字段多而更可治理。

**最小迁移法**：先用纸或表格填这 8 个问题；再映射到已有的 issue、数据库、事件总线或 CI artifact；最后用一个已知错误和一次拒绝演练验证记录真的会改变下一步。不要先设计一套漂亮 YAML。
