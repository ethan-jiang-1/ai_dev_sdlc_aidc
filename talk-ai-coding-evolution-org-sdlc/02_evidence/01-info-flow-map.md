# 信息脉络图（上游 → 加工 → 页面 + 反向索引 · v0.5）

> 组织视角贯穿：每个页面落点都回答「组织该建什么 / 谁负责 / 怎么治理 / 怎么度量」，不滑回个人技能。

## 一、正向信息流（source → 加工 → 页面）

```text
上游素材（_reference/ 只读）               加工产物                      页面落点（03_outline/00-page-structure.md）
─────────────────────────────            ──────────────                 ─────────────────────────────
rawdata_anthropic-ai-native-sdlc-playbook ─→ 02_evidence/00-absorption  ─→ 宽轴主体：
  六阶段 + 15 play                          （进货单）                    P6-P7（论点）P11-P13（定义+shifts+工件链）
                                                                        P14-P36（六阶段逐页）
rawdata_ai-coding-evolution-final       ─→ 01_storyline/05（深轴解读）  ─→ 深轴：
  五层演变 + Böckeler                      + 01_storyline/06（harness）  P8（五层回顾）P19-P24（harness 主战场）
                                                                        P38-P40（治理收束）
rawdata_dsh-faq-on-digested / digested   ─→ 02_evidence/00 §二 DSH 映射  ─→ 平台落地：
  / plugin-*                              + 01_storyline/06             P41-P42（DSH 作为 runtime 证据）
```

## 二、反向索引（页面 → 上游来源）

| 页 | 页面 | 主来源 | 辅来源 |
|---|---|---|---|
| P1–P5 | 开场（钩子 + 对象 + 路线图） | playbook「Code is no longer the bottleneck」 | 五层（深轴铺垫） |
| P6–P7 | 代码不再是瓶颈 + 三个后果 | playbook「Code is no longer the bottleneck」 | — |
| P8 | 深轴：五层演变回顾 | `ai-coding-evolution-final/final_v4` | — |
| P9–P10 | 传统 SDLC 与控制失效 | playbook「traditional SDLC」段 | — |
| P11–P13 | AI-native SDLC 定义 + shifts + 工件链 | playbook「What is an AI-native SDLC」+「shifts」表 | — |
| P14 | 六阶段总览 + loop 图 | playbook「Plays」+ fig-03-loop | — |
| P15–P16 | Plan：intent.md | playbook「Capture as intent.md」 | 五层 Prompt/Context |
| P17–P18 | Design：spec.md | playbook「Requirements and design」 | 五层 Context + 治理前移 |
| P19–P24 | Build：plan.md / AGENTS.md / skills / hooks / 并行 | playbook「Build」全 5 play | 五层 Harness（圈住/拦住/看清） |
| P25–P27 | Test：反馈闭环 + evals | playbook「Give Claude a feedback loop」「Continuous evals」 | 五层 Sensors + 确定性 |
| P28–P32 | Deploy：PR review / gates / managed settings / CI-CD | playbook「Deploy」全 3 play + worked example | 五层 拦住/看清 + authorize at execution |
| P33–P36 | Maintain：关 loop / scans / on-call | playbook「Maintain」全 3 play | 五层 Loop/Graph |
| P37 | 工件链 = 审计链 | playbook「committed artifact」段 | — |
| P38–P39 | 人守 gate + 确定性优先 | playbook「Governance」贯穿 + `06-harness-internals` | 五层 Harness |
| P40 | harness = 统一平台 + 治理边界 | playbook managed settings + `06-harness-internals` | — |
| P41–P42 | DSH 作为 runtime 证据 + 四项治理决定 | `rawdata_dsh-*`（FAQ 07 + _digested） | — |
| P43 | 组织怎么落地（顺序） | playbook「order to adopt」段 | — |
| P44 | 度量总表 | playbook 各 play「How to measure」 | — |
| P45–P46 | 带走一句 + 谢谢 | — | — |

## 三、口径与引用约定

- 每个页面引用素材走相对路径 `../_reference/rawdata_*/…`（见 `_reference/README.md`）。
- 简写：`final_v4/…` = `rawdata_ai-coding-evolution-final/final_v4/…`；`_digested/…` = `rawdata_dsh-digested/…`。
- 「代码不再是瓶颈」是 Anthropic 论点，引用标注来源；playbook 是 Claude 视角，机制讲透、产品名不唯一。
