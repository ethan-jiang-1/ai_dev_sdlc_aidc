# 信息脉络图（v0.7 · 软件 SDLC · 固定 50 页）

> 每个页面落点都必须回到软件价值流：交付什么工件、哪个 gate 执行规则、哪个 owner 承担判断、什么 feedback 回流。
> 核心主张的来源类型与口径见 [`02-claim-ledger.md`](./02-claim-ledger.md)。

## 一、正向信息流（source → 判断 → 页面）

```text
Anthropic AI-Native SDLC playbook
  │
  ├─ 瓶颈转移 / six-stage shifts / committed artifacts / governance / measures
  │    └─→ C1–C4、C6 → P2–P3、P6–P40、P48–P50
  │
五层演变 + Böckeler Harness 资料
  │
  ├─ Prompt / Context / Harness / Loop / Graph 深度镜头
  └─ Guides / Sensors；确定性 / 概率性控制
       └─→ C4–C5 → P4–P5、P12、P14/P17/P20/P26/P30/P35、P40

DSH digested / FAQ / seam 资料
  │
  ├─ 知识外置 / 正确路径 / 可执行反馈
  ├─ 插件图 / 事件流 / loop / capability seam
  └─ enforced gate / invariant / append-only log / asked-decided / fail-closed
       └─→ C3–C5 → P41–P47

本 talk 的综合判断
  │
  ├─ 可执行 SDLC = 工件可交接 + gate 可执行 + owner 可问责 + feedback 可回流
  ├─ 工件链是审计骨架；身份/版本/证据/审批/不可绕过的 gate 使它可追溯、可问责
  ├─ 共享控制面，分布领域知识
  └─ 先工件 → 再 gate → 最后关 loop
       └─→ P9–P12、六阶段收口页、P39、P48、P50
```

## 二、固定 50 页反向索引（页面 → 主来源）

| 页 | 叙事任务 | 主来源 / 主张 | 口径要点 |
|---|---|---|---|
| P1 | 题目与软件 SDLC 范围 | `01_storyline/03-audience-and-pitch.md` | 不泛化为一般 AI 组织 |
| P2–P3 | 诊断张力 + Anthropic 观点 | playbook 「Code is no longer the bottleneck」；C1 | 不虚构翻倍数据；要求听众自证 |
| P4–P5 | 五层深度镜头 + 共享 harness 控制面 | `rawdata_ai-coding-evolution-final/final_v4*`；C5 | 五层不是第二条主线 |
| P6–P8 | 瓶颈转移后，旧控制为什么失配 | playbook 开篇三个后果 + security example；C1 | 只说来源主张与软件价值流意义 |
| P9 | 新控制模型 | playbook human judgment / gates + C2/C4 | 机器守确定性 gate，人守判断 gate |
| P10 | 工件链是审计骨架，留下条件问题 | playbook committed artifact 段；C3 | 不把 git history 自动等于合规 |
| P11 | six-stage shifts | playbook shifts table | 保留传统 / AI-native 的光谱，不绑定产品 |
| P12 | 全场四问导航 | C2 + `01_storyline/00-storyline-map.md` | 工件 / gate / owner / feedback 是本 talk 综合框架 |
| P13 | 阶段顺序 ≠ 采用顺序 | playbook Plays + dependency graph；C6 | 不从自动化整个 loop 开始 |
| P14–P16 | Plan：意图交接 | playbook 「Capture as intent.md」 | 工件=`intent.md`；gate=accept/reject；owner=product owner；feedback=耗时/存活率 |
| P17–P19 | Design：政策和矛盾前置 | playbook 「Requirements and design」 | 工件=`spec.md`+concerns；gate=风险处理；owner=product/policy owner；feedback=rework |
| P20–P25 | Build：受控执行 | playbook Build 5 plays + harness 圈住/拦住/看清 | 工件=`plan+diff+tests`；gate=沙箱/权限/hooks；owner=engineer+platform；feedback=rework/plan match |
| P26–P29 | Test：产品证据 + harness 回归 | playbook feedback loop + continuous evals | 工件=test/eval evidence；gate=threshold；owner=QA+config owner；feedback=pass/escape/failure trend |
| P30–P34 | Deploy：提议权 / 执行权分离 | playbook PR review / approval gates / managed settings / CI-CD；C4 | 工件=PR/release evidence；gate=branch+production；owner=code/release owner；feedback=wait/failure |
| P35–P38 | Maintain：事实回流同一受控路径 | playbook closing loop / scans / on-call | 工件=incident/diagnosis/intent；gate=triage+PR/runbook；owner=service owner；feedback=recovery/recurrence |
| P39 | 回答 P10：工件链何时具备审计能力 | C3 + playbook 多段 governance evidence | 五个条件是本 talk 综合，不冒充外部合规标准 |
| P40 | 确定性 / 概率性控制的责任分工 | Böckeler Guides/Sensors + playbook governance；C4 | AI review 可留痕，但不冒充确定性证明 |
| P41–P45 | DSH 三条腿：知识 / 路径 / 反馈 | DSH FAQ 07 + harness-idea | DSH 是参考实现；每个机制必须回指前面软件 SDLC 问题 |
| P46 | 可替换能力合同 | DSH capability-seams | 统一合同，不统一每个后端 |
| P47 | 可重建事实 | DSH session-and-loop / approval pipeline | 模型可见输入、tool result 与 approval 的日志语义要分清 |
| P48 | 四项治理决定 + 采用顺序 | C5/C6 + DSH 机制索引 | 先工件 → 再 gate → 最后关 loop；生态数量不承担结论 |
| P49 | 回答开场 | C1/C2 | slogan 保留，同时重申诊断条件 |
| P50 | 软件价值流试点 | C6 + communication job | 选最慢的交接，补齐一个 artifact/gate/owner/feedback |

## 三、引用与责任约定

- 页面所用外部非平凡主张，必须可回到 `_reference/` 下具体文件或 `02-claim-ledger.md` 的对应 claim。
- 「工件 / gate / owner / feedback」、「审计五条件」与「共享控制面，分布领域知识」是本 talk 综合框架；现场不归属给 Anthropic 或 DSH 原文。
- 产品名、工件名与具体路径是实现示例；主线讲机制与组织责任，不讲成唯一方案。
- 本索引只适用于软件 SDLC，不得用它支撑销售、市场、客服、财务、人力或一般企业组织结论。
