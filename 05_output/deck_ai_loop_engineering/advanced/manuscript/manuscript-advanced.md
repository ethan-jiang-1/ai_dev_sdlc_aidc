---
title: 文稿 — Loop Engineering 技术产品场
status: draft-for-review
source: advanced/outline/outline-advanced.md
revised: 2026-09-28
---

# 文稿 — 技术产品场

> 本稿与 [`../outline/outline-advanced.md`](../outline/outline-advanced.md) 同步。每页 `CLAIM` 与 outline subtitle 完全相同；引用块不上屏。
> 实操轨（2026-09-30 增，90 分钟版）：三道构造档练习，题面与讲者卡在 [`../practice/`](../practice/README.md)，嵌入位置见 outline §8；上屏内容不因练习改动。

## 术语

目标（Goal）｜行动（Action）｜环境反馈（Environment Feedback）｜评估/裁判（Eval/Grader）｜继续（Continue）｜停止（Stop）｜交还（Escalate）｜状态（State）｜结果（Outcome）｜验收（Accepted）。

---

### A01 · 你离开后，它说做完了
**CLAIM**：Loop 的难题不是能否行动，而是回来时凭什么信完成宣告。

**上屏**：你离开了；它继续跑；你回来听到“完成”。**凭什么信？**

**接到下一页**：名称不能替我们回答这个问题。

### A02 · 名称不是方法
**CLAIM**：不同来源的 loop 外延不兼容；本场治理的是可审计控制决策，不站队某一种环数。

**上屏**：同一个名字，可能指运行时循环、轨迹改写环境，或产品反馈三环。本场只谈控制决策。

**接到下一页**：先把我们要审计的链条画出来。

### A03 · 先画完整控制链
**CLAIM**：Goal/边界 → Action/授权 → 环境反馈 → Eval/裁判 → 继续/停止/升级 → State/Outcome；这是研究抽象，不是 KOL 原话。

**上屏**：目标与边界 → 本轮行动与授权 → 环境事实 → 判据与裁判 → 继续/停止/交人 → 状态与外部结果。

**备注**：控制链是本仓研究抽象，不冒充统一 taxonomy。

### A04 · Goal 决定“完成什么”
**CLAIM**：目标必须有可观察终态、检查方式和路径约束；外部业务结果不可见时不能伪装成自动 `Met`。

**上屏**：终态是什么？怎么查？什么不能改？业务结果看不见时，产出只能停在待观测。

### A05 · Action 决定“允许做什么”
**CLAIM**：下一步行动必须落在本轮授权的目标、范围和有效期内；选择下一步不等于权限自动扩大。

**上屏**：能选下一步，不等于能做任何下一步；授权绑定对象、范围、动作和期限。

### A06 · Feedback 是环境事实
**CLAIM**：工具结果、测试、构建、浏览器路径、拒绝和失败原因必须进入下一步；不看反馈就重跑是 retry，不是 loop。

**上屏**：Action → 环境事实 → 下一 Action。没有反馈回路，只是重复执行。

### A07 · Eval 是裁判，不是反馈
**CLAIM**：Eval 用预设判据解释环境反馈；判据要能观察、能复查，并明确谁能修改它。

**上屏**：Feedback 说发生了什么；Eval 判断是否满足 Goal。两者不能写成同一个“通过”。

### A08 · 继续、停止、升级是三条控制路径
**CLAIM**：未满足且可修复才继续；满足预设产出才成为停止候选；不可判、高风险、拒绝或无法恢复就升级/交人。

**上屏**：Continue / Stop / Escalate。出口不同，责任和恢复语义不同。

### A09 · Stop ≠ Accepted
**CLAIM**：资源耗尽、无进展、拒绝熔断、模型收尾和人工暂停都可能停止控制流，但不自动代表产出被接受。

**上屏**：`stopped` 只表示停了；`accepted` 才表示预设产出验收通过。

### A10 · State 与 Outcome 分账
**CLAIM**：`running / blocked / awaiting_human / stopped` 是控制状态；`accepted` 是产出验收；`outcome_pending` 是外部结果等待观测。

**上屏**：控制状态 ≠ 产出状态 ≠ 业务结果。三本账不能合并。

### A11 · 第一类失败：提前宣告完成
**CLAIM**：文件变多、回复很满、空壳能打开或单测通过，都可能不是目标完成；目标敌人是 premature completion。

**上屏**：能打开 ≠ 做完；单测过 ≠ 目标满足；回复满 ≠ 结果正确。

### A12 · 三件停止骨架各管一件事
**CLAIM**：机器闸门拦局部事实错误；硬上限管资源与失控；验收与干活分离处理签署权；三者不可合并为“它停了”。

**上屏**：机器闸门问“这一轮过不过”；硬上限问“还允不允许活”；分离问“谁能签完成”。

### A13 · 闸门必须覆盖真实 feedback path
**CLAIM**：存在一个 bound 或测试不够；实际嵌套反馈路径未覆盖、基线未过、测试被削弱或该做的事没做，仍会产生假通过。

**上屏**：Bound 存在 ≠ Bound 有效。测试存在 ≠ 目标被覆盖。通过 ≠ 该做的事都做了。

### A14 · Eval 分离不等于判得对
**CLAIM**：输入可被操纵、裁判偏好自身输出、代理目标会被过优化；独立模型不是可信度证明。

**上屏**：分离解决利益冲突，不自动解决判定能力、输入操纵和代理目标失真。

### A15 · 裁判要被单独校验
**CLAIM**：用已知失败、人工标注冲突样本和版本化判据检查 false approve/false reject；没有效果阈值就不能伪造通用放行线。

**上屏**：不仅评估 Agent，也评估 evaluator：误放、误拒、冲突、版本漂移。

### A16 · 逐轮判断要改变下一步
**CLAIM**：`Not yet met` 带理由继续；`Met` 只接受预设产出；`Impossible` 停止并交人/改条件；不是问模型“做完了吗”。

**上屏**：判定必须产生下一步语义：继续、接受、停止并交还，不能只有一句自述。

### A17 · 资源上限是包络，不是质量分
**CLAIM**：轮数、时间、拒绝、成本、过期和无进展检测保护系统资源；覆盖不到实际路径的上限等于没有上限，耗尽后先保全状态和交接。

**上屏**：资源耗尽不是验收失败，也不是验收通过。先落盘、标状态、交接，再决定是否恢复。

### A18 · 拒绝不是统一的停机语义
**CLAIM**：单次拒绝可以带理由寻安全路径；持续拒绝可熔断；硬政策拒绝不可改名为“待人批准”；每种出口必须记录原因和恢复语义。

**上屏**：deny-and-continue；重复拒绝熔断；硬拒绝不可绕。拒绝之后去哪里，必须写清。

### A19 · 人工审批必须可达
**CLAIM**：执行前让指定人看到动作、目标和风险，能作决定，并能从同一状态恢复；父线程看不见、无恢复指针时，不能声称“已升级”。

**上屏**：升级不是画一条箭头；要有人看见、能决定、能恢复。

### A20 · 批准只绑定一次动作
**CLAIM**：授权绑定动作、目标、分支和有效期；换 feature、扩大范围或从 edit 变 commit/push 必须重新授权。

**上屏**：一次批准只批准一次动作。旧批准不自动继承到新目标、新分支或发布。

### A21 · 长任务把状态移出对话
**CLAIM**：每轮恢复 State，再从未完成项选择 Action；文件队列和事件触发解决接续，不自动解决 feature 级授权史、优先级变更、阻塞和验收总账。

**上屏**：下一轮先恢复状态，再选工作；能 resume 不等于有总账。

### A22 · 外层调度只决定“何时再跑”
**CLAIM**：条件、时间、事件和持久进度是触发形态；触发前仍要检查目标、权限、反馈和资源资格。

**上屏**：trigger 解决何时醒来；不替你解决能不能继续。

### A23 · 自主度是控制权转移，不是第 N 轮
**CLAIM**：升档要联测负例闸门、独立判据、预算、权限和接手路径；判定冲突或接手不可达就退回人工。

**上屏**：不是跑到第几轮，而是哪些控制权已经有证据可以转移。

### A24 · 先审计链，再撤逐轮值守
**CLAIM**：Goal/边界 → Eval/负例 → 真实 Feedback → State/Outcome → Stop/Escalate/恢复；只证明可治理设计，不宣称效率或质量收益。

**上屏**：先审计控制链，再谈少守。机制存在，不等于效果已证。

**收束**：Loop Governance 的硬核不是让循环活得更久，而是让继续、停止、升级和交还都留下能复查的理由。

**带走**（收束句后接练习 3 的抽查，最后一句口播）：这张升档表今天填不完是正常的——它本来就该对着真实任务慢慢填。填完那天你就知道该不该升、该升哪一档。回去照着《循环交接手册》高级篇走：交动作、交续跑、交唤醒、升一档，按时刻翻；它说做完了之后的放行检查，在「它说做完了」一节。

---

# 工程师追问卡（不上屏）

> 本节按 A01–A24 提供可追问的机制、反例和边界。伪配置是本主题设计题，产品参数保留产品语境；专项 `stop_conditions/README.md` 的“双环三层”仍是研究抽象，SOP 以 `03_practice/loop_governance/result/manual.md` 为准。

## A01–A03 · 先问“控制对象是什么”

- **A01**：追问完成钩子在何时检查、检查哪棵 tree、绑定哪份证据。一个可疑交付状态可以是 `PR created; CI failing; accepted_by=null; outcome_status=pending`；不要用最终 assistant message 推导完成。
- **A02**：Ralph 的 `while :; do ...; done` 没有内建 stop，TODO 耗尽由人凭 taste 判断；Claude `/goal`、`/loop`、auto mode 分别是条件、时间/事件和轮内审批语义，不能合成同一个环。
- **A03**：建议每次控制迁移写事件：`goal_rev/action_id/evidence_ref/verdict/decision_source/state_rev/stop_reason/resume_pointer`。这是本主题设计题，不是产品统一 schema。

来源：`03_practice/loop_governance/result/manual.md` §7、§9–10；`02_research/ai_loop_engineering/raw/evidence-2026-09-26-b-stop-and-scheduling.md` §1、§4a–c。

## A04–A05 · Goal 与 Action

- **A04**：把目标拆成 `terminal_state + check + constraints + stop_clause`。可核实例是 Lighthouse ≥92、LCP<1.8s、不改 hooks public API、连续两轮无改善 abort、最多 10 turns；这是个人实践例，数字不是通用阈值。
- **A05**：授权最小绑定建议：`{principal, action, target, branch, expires_at, nonce}`。edit 的批准不自动覆盖 commit/push、另一分支或另一 feature；目标或动作变化即重问。
- **失败边界**：`cron` 只唤醒，不能代替授权；选择下一步不等于拥有无限权限。具体越权案例只有单用户反例，不能外推发生率。

来源：`manual.md` §2、§6–7、§9；`backbone.md` §3；`raw/evidence-2026-09-27-f-autonomy-gates.md`。

## A06–A07 · Feedback 与 Eval

- **A06**：最小反馈通道：`cmd → exit_code + stdout/stderr artifact → durable evidence_ref → next action`。Aider 的实现形状是 lint 非零 → 确认修复 → 将错误回灌；没有 `evidence_ref` 的“再跑一次”只是 retry。
- **A07**：评估器 schema 必须有明确的 `pass`/verdict 和缺字段语义；promptfoo 记录显示缺 `pass` 且未设 threshold 时 score 0 仍可能放行。Feedback 是事实，Eval 才解释“是否满足 Goal”。
- **工程追问**：判据测目标还是代理指标？执行方能否修改？裁判输入是否包含自我辩护？版本/样本集变化后能否比较？

来源：`stop_conditions/01_machine_gates/insights.md` #13、`stop_conditions/03_verdict_split/insights.md` #10；`manual.md` §10。

## A08–A10 · 三出口与三本账

- **建议状态机**（本主题建议，不是产品统一实现）：
  ```text
  hard_deny → blocked
  verdict=Met + artifact_check → stopped_candidate
  verdict=NotYet + retryable → continue
  unknown / timeout / no_recovery → awaiting_human
  ```
- `stopped` 不代表 `accepted`；资源耗尽、无进展、拒绝熔断和模型收尾都要写 `stop_reason`。`accepted_by + evidence_link` 另记；业务结果另记 `outcome_owner + next_check`。
- 虚构记录：`feature_id=search-42; status=blocked; stop_reason=human_pause; accepted_by=null; outcome_status=pending`。多 feature work-row 是本主题试点，不是已证标准。

来源：`backbone.md` §1–2；`manual.md` §5、§7、§10；`02_research/ai_loop_engineering/digested/07-控制问题矩阵.md`。

## A11–A12 · 提前完成与停止骨架

- **A11**：Anthropic feature list 初始全 `passes:false`，端到端浏览器验证后才翻 true；单测/curl 通过但按钮不可用不能翻。另有删除/禁用测试的第一人称反例。
- **A12**：三张“票”分开：`test exit=1` 是机器拒绝；`turns=10/10` 是资源熔断；`test exit=0 + independent verifier` 才是验收候选。硬上限不是质量分。
- **专项边界**：双环三层是 `stop_conditions` 的专项提炼，尚未回流 `digested/03`，不能在台上说成行业已证架构。

来源：`stop_conditions/01_machine_gates/practices.md` #3；`02_hard_caps/insights.md` #1–3、#17；`03_verdict_split/practices.md` #3。

## A13–A15 · 闸门和裁判也会失效

- **A13**：把嵌套反馈路径画成图，逐边标 bound；IAL-Scan 区分 `bypassed_bound` 与 `ineffective_bound`。内层 agent 有 turn cap，不代表外层 evaluator/retry 没有无限路径。
- **A14**：独立 evaluator 仍可能被样本顺序、自我偏好、谄媚目标或 Goodhart 代理目标操纵；分离解决利益冲突，不等于判得对。METR 的 monkeypatch evaluator/改时钟是压力样本，不外推普通 PR 发生率。
- **A15**：裁判校验集至少分 `known-fail / ambiguous / adversarial / human-conflict`，记录 `judge_version/rubric_hash/false_accept/false_reject`。没有效果阈值，不伪造统一放行线。

来源：`stop_conditions/02_hard_caps/insights.md` #15；`03_verdict_split/insights.md` #6–10；`03_verdict_split/practices.md` 裁判失效条目；`raw/evidence-2026-09-28-m/n/r-*.md`。

## A16–A18 · 逐轮判定、资源和拒绝

- **A16**：`Not yet met + reason → continue`；`Met + evidence → acceptance candidate`；`Impossible → stop/escalate`；unknown/timeout 不要强行归入 Impossible，通常保留为 blocked/awaiting_human。
- **A17**：资源包络至少考虑轮次、wall clock、成本、retry budget、过期、无进展和嵌套路径覆盖；预算耗尽前先落盘/生成部分成果/交接。`RemainingSteps` 是框架机制实例，不是所有运行时默认保证。
- **A18**：`deny_retryable` 可带理由继续寻安全路径；`deny_hard` 不可伪装成待人批准；`circuit_open` 记录拒绝计数与恢复条件。Claude 的 3/20 仅是产品实例，OpenAI 重复拒绝机制未公开相同阈值。

来源：`manual.md` §2、§7；`stop_conditions/02_hard_caps/practices.md` #2–5、#25；`stop_conditions/02_hard_caps/insights.md` #4、#17。

## A19–A20 · 审批可达与授权绑定

- **A19**：人工接手最小包：`feature_id/action/target/thread_id/decision_source/denial_reason/authorized_scope/reviewer/resume_pointer`。分别演练 allow、需人批准、策略 hard deny；没有 reviewer 或 resume pointer 就是 blocked，不是“已升级”。
- **A20**：用变异测试验证授权：把 edit 改成 commit、把当前分支换成 main、把目标换成 release、把时间推进到过期；旧批准都应失效。
- **边界**：未合并 PR 只能作为候选机制，不能说成已发布产品行为。

来源：`manual.md` §7、§9；`backbone.md` §3；`raw/evidence-2026-09-27-f-autonomy-gates.md`。

## A21–A22 · State 与调度

- **A21**：Anthropic 的 `feature_list.json + progress + git` 是长任务单项目实例，不是跨 feature 总账；四列仍要问：授权史、priority、blocked_reason、accepted_by/evidence。
- **A22**：建议唤醒序列：`wake → restore state → validate scope/budget → choose next item → run`。`/goal`、`/loop`、webhook、Stop hook 是不同 trigger；轮内 auto mode 不等于启动下一轮。
- **反例**：能 `resume` 只说明能接续会话，不说明 priority、权限和验收都可见。

来源：`manual.md` §5–6；`backbone.md` §2；`02_research/ai_loop_engineering/digested/07-控制问题矩阵.md`。

## A23–A24 · 升档与最终审计

- **A23**：升档前联测三件事：负例会红；独立裁判可用且冲突可交人；预算、权限和恢复路径都点得通。没有通用“第 N 轮”门槛。
- **A24**：审计卡：`Goal/constraints | eval+negative_control | feedback_artifacts | state/outcome | stop_reason | accepted_by+evidence | reviewer+resume_pointer`。任一字段为空，保持更强的人在环。
- **不可说**：机制存在不等于 loop 已证明提升质量、吞吐或减少返工；这些需要 P-outcome。

来源：`manual.md` §9–12；`backbone.md` §3–4；`02_research/ai_loop_engineering/README.md` §0。

---

# 可直接拆解的控制实验（不上屏）

> 本节不是来源目录，而是一套可运行的演示设计。所有 YAML/JSON/伪代码都是本主题建议模板；要进入生产，必须绑定项目权限、运行器和真实审计存储。产品参数只保留产品语境，不当通用阈值。

## 1. Goal / Eval 合约

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

工程审查不能只问“有没有 goal”，还要问：终态是否可观察、检查是否覆盖实际路径、约束是否由运行器 enforce、`impossible` 是否真的是逻辑不可满足而非暂时不可见。外部采用率不能填成 `Met`。

## 2. Action authorization：把批准做成可失效对象

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

**变异测试**：依次把 `edit` 改为 `commit`，把 branch 改成 `main`，把 target 换成 `deploy/`，把时间推进到过期，把 nonce 换成下一轮。每一次都应该拒绝旧 token，并写出 `authorization_drift` 事件。若变异仍能通过，不能升档。

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

最小事件示例：

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

下一轮只能消费带 `evidence_ref` 的观察结果；“我刚才试过了”不是证据。嵌套工具、retry 和 evaluator 都要纳入实际 feedback path，否则内层通过、外层无限重试仍可能失控。

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

建议的 schema 规则：`verdict`、`reasons`、`evidence`、`rubric_hash` 缺一即拒绝；`Met` 没有证据即拒绝；未知 verdict 不得降级成 false 或 true。promptfoo 的缺 `pass`/无 threshold 反例说明，评估器接口本身也必须测试。

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

至少要保留 known-fail、ambiguous、adversarial 和人工冲突样本。`false_accept=0` 只是这批样本的观察，不是评估器的质量证明；METR 的 reward-hacking 样本说明独立 evaluator 仍可能被输入、时钟或代理目标操纵。

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

`Impossible` 必须区分“逻辑上不可满足”和“当前没有观测”；后者通常是 `blocked` 或 `awaiting_human`。决策表的关键不是状态名称，而是每个分支都带 `reason`、`evidence_ref` 和下一责任人。

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

`max_turns` 只覆盖一个维度；如果 evaluator 或 tool retry 在预算外重调，系统仍可能无限运行。预算耗尽不是验收通过，优先保全状态并交接。产品的 3/20、20m、7d 等数值只能作为对应产品机制举例。

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

演练三条路径：允许动作；一次拒绝后带理由换安全路径；硬拒绝或连续拒绝后熔断。父线程必须能看到子线程最后状态，reviewer 必须能从同一状态恢复。没有这些条件，只写“升级”是假的。

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

这是本主题建议的控制行，不是公开统一标准。单任务 `progress` 和 git history 仍不能自动回答 priority、授权史、阻塞原因和验收人。

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

这份清单验的是控制链能否拒绝已知坏路径，不证明业务质量、收益或组织可规模化。只有每项都能给出 evidence link、stop reason 和责任人，才有资格讨论减少逐轮值守。

## 11. 从示意 YAML 泛化成项目控制面

这些 YAML 是**语义参考模型**，不是 Loop Governance 的标准协议。泛化的对象不是字段名，而是控制不变量：

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

**先分三层，不要把整份 YAML 当成通用标准**：

| 层 | 是否应跨领域保留 | 例子 |
|---|---|---|
| 控制不变量 | 是 | 目标可观察、证据可追溯、判定有理由、停止原因独立、验收有权威、升级可恢复 |
| 承载结构 | 可变 | YAML、JSON、数据库行、事件流、CI artifact、工单字段 |
| 领域策略 | 不可直接搬运 | 阈值、重试次数、谁审批、什么算不可修复、回滚/补数/恢复动作 |

例如 `accepted_by` 这个**语义**可以跨领域保留，但 CI 可能叫 `release_approver`，数据管道可能叫 `data_owner`；`max_turns: 10` 这个**数字**不能因为搜索案例存在就搬到发布或数据回填。

**迁移规则**：

1. 先写领域的终态和不可变约束，不要先复制 `goal.yaml`；
2. 把每个控制动作映射为领域事件，而不是只存最终状态；
3. 给每条判定绑定 evidence、判据版本和责任来源；
4. 明确缺证据、未知、拒绝、资源耗尽是否 fail closed；
5. 用领域特有的已知坏样本做负例，而不是复用搜索案例的负例；
6. 演练恢复：进程重启、权限过期、上游延迟、人工冲突时，能否从同一状态继续或交接；
7. 最后才决定 YAML、数据库、事件流或现有平台字段如何承载。

**三个迁移例子**：

```text
CI：build artifact + test report → gate verdict → retry / block / release approval
数据管道：partition manifest + quality report → freshness/completeness verdict → backfill / pause / owner review
发布：canary health + rollback checkpoint → policy verdict → continue rollout / rollback / incident handoff
```

它们共享控制语义，但不能共享阈值、判据或恢复动作。`p95 < 300ms`、`3 次拒绝`、`10 轮` 等数字必须由领域风险、成本和历史基线决定；如果没有基线，只能标为待定，不能从搜索案例搬过去。

## 12. 两个领域的完整迁移例子

### A. 数据管道：从“页面完成”换成“分区可交付”

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

迁移时保留的是“终态—事实—判定—出口—责任—恢复—外部结果”语义；换掉的是页面路径、浏览器检查和搜索分支。**领域负例**不是“按钮坏了”，而是：row count 为零、freshness 超期、schema drift、已认证分区被覆盖。每个负例都要确认同一质量门会失败，并且失败原因能回到下一步。

### B. 发布系统：从“产出验收”换成“风险可控地推进”

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

发布系统的 `stop` 不是“部署命令返回 0”；可能是回滚、暂停或等待观察窗。**领域负例**包括：部署成功但错误率超预算、artifact digest 不在批准清单、rollback checkpoint 不可恢复。搜索案例的 `npm test`、10 轮和页面按钮都不能搬进来。

## 13. 泛化验收：用变换而不是改名检查

对任何新领域做三轮测试：

1. **换领域**：同一控制语义映射到数据管道和发布系统，能否说清终态、事实、判定、出口、责任和恢复？
2. **换承载**：把 YAML 改成数据库事件或 CI artifact，审计信息是否仍然可追溯？
3. **换失败类型**：把“检查失败”换成权限过期、外部依赖延迟、判据版本漂移、人工冲突，状态是否仍能区分 `blocked / stopped / accepted / outcome_pending`？

若只是替换字段名、但没有定义领域终态、负例和恢复动作，叫“泛化”是假的。若每换一个领域就能保留控制不变量、重写领域策略，并能用负例让门失败，这才是**语义泛化**，不是格式复制。

**判断一个模板是否真的泛化**：至少做三次变换——换领域、换存储、换失败类型；如果只改字段名仍能回答“目标是什么、证据是什么、谁判、为什么停、谁接、如何恢复”，它具有语义泛化性。若必须保留搜索分支、浏览器按钮等具体词才能工作，它只是案例，不是模板。
