# 信息脉络图 · 上游 → 加工 → 页面（talk 的 provenance + trace）

> **用途**：推敲某一页时，脉络一眼清楚——这页的内容从哪来、改一处会牵动哪些页。
> 对应现场版 `../03_outline/00-page-structure-23.md`（P1–P23）。
> 口径红线见 [`00-absorption-plan.md`](./00-absorption-plan.md) 第三节。

## 正向脉络：页 → 加工层 → 上游

| 页 | 关键内容 | 加工层（内容文件 + 吸纳清单） | 上游来源 |
|---|---|---|---|
| P1 封面 | 官方题目 + 开场问题 | 05-opening S1 | 用户定题（无上游） |
| P2 钩子 | 五角色阶梯；Cherny 金句 | 05-opening S2；吸纳 §一.1/.4 | 06 角色表；04 Cherny |
| P3 路线图 | 四站 | 05-opening S3 | 故事线 v1.2（自拟） |
| P4 发动机 | METR 7 个月翻倍；prompt 措辞不重要 | 05-opening S4；§二 S4 | 01（METR）；02（Anthropic） |
| P5 Prompt+Context | 行为控制面；伪装成提示复杂度；context rot；MCP/RAG | 05-opening S5+S6；§二 S5/S6 | 01；02（context rot、MCP/RAG） |
| P6 Harness 埋雷 | Agent=Model+Harness；单次运行容器 | 05-opening S7；§二 S7 | 03 §一/§七 |
| P7 Loop+Graph | 黄金法则；blast radius；不是新东西；260 万 | 05-opening S8+S9；§二 S8/S9 | 04；05 |
| P8 叠加观+成熟度 | 扳手/螺丝刀；成熟度标尺 | 05-opening S10；§二 S10 | 06 |
| P9 转折 | 承重墙判断 + 口径（我们的判断，三线撑） | 02-act2 S11；§二 S11 | 06（Context/Harness 并列） |
| P10 定义 | Agent=Model+Harness；SWE-bench 脚手架金句 | 02-act2 S12；§二 S12 | 03 §一；01 §二 |
| P11 两套控制+comp/infer | Guides/Sensors；npm test vs AI；教小孩做菜 | 02-act2 S13+S14；§二 S13/S14 | 03 §一 |
| P12 圈住拦住看清 | 模型给能力 harness 给可靠性；84% | 02-act2 S15；§二 S15 | 03 §五；01_storyline/06-harness-internals |
| P13 承重墙 | one floor above；engine & pilot；GraphARC；假设下层正确 | 02-act2 S16；§二 S16 | 04；05（GraphARC）；06 |
| P14 CVE | authorize at execution | 02-act2 S17；§二 S17 | 03 §二 |
| P15 抉择 | 固定 vs 灵活轴；精装公寓比喻 | 03-act3 S18 | 故事线 v1.2 立场（自拟） |
| P16 固定的好 | 民主化；84%；simplest viable system | 03-act3 S19；§二 S19 | 03 §二/§五；04（Osmani） |
| P17 固定的卡 | 挂模型/工具/换后端/skill/knowledge map 受限；等厂商；context rot | 03-act3 S20；§二 S20 | 03 §二；02（rot）；_digested（机制对照） |
| P18 本质 | 别只能现成；装自己的 + 借现成的 | 03-act3 S21 | 立场（v1.2）；两线证据 §二 S19/20 |
| P19 DSH | 无特权内核金句 | 04-act4 S22；§二 S22 | FAQ 01（architecture） |
| P20 双向灵活 | 挂模型/工具/换后端/skill/knowledge map；都不必改 loop；15 行 YAML | 04-act4 S23；§二 S23 | _digested tools-prompt-llm / capability-seams；FAQ 03/04 |
| P21 哲学 | enforced gates；GraphARC 同套 | 04-act4 S24；§二 S24 | FAQ 07；05（GraphARC） |
| P22 回答+slogan | 角色表回扣；装自己的借现成的 | 04-act4 S25+S26；§一.1 | 06 角色表；slogan（用户定方向） |
| P23 Q&A | 预埋三问 | 04-act4 S27 | 结构（自拟） |

## 反向索引：上游 → 用到它的页

| 上游源 | 用到它的页 |
|---|---|
| `final_v4/01-2025-prompt-era.md` | P4, P5, P10 |
| `final_v4/02-mid-2025-context-era.md` | P4, P5, P17 |
| `final_v4/03-2026-harness-era.md` | P6, P10, P11, P12, P14, P16, P17 |
| `final_v4/04-2026-loop-era.md` | P2, P7, P13, P16 |
| `final_v4/05-2026-graph-era.md` | P7, P13, P21 |
| `final_v4/06-five-layer-forward.md` | P2, P8, P9, P13, P22 |
| FAQ 01_repository-organization | P19 |
| FAQ 03_model-vendors | P20 |
| FAQ 04_root-entry-doc-design | P20 |
| FAQ 07_borrowing-harness-idea | P21（哲学）+ P17/P18（门禁思路） |
| `_digested/tools-prompt-llm` | P20 |
| `_digested/capability-seams` | P20 |
| `_digested/surfaces` | P17/P20 口径（MCP 结论） |
| 用户输入 | P1（题目）、P22（slogan 方向）、P18（立场软化） |

## 关键事实索引：改一处 → 牵动的页

| 关键事实 / 金句 | 牵动的页 |
|---|---|
| "Agent = Model + Harness" | P6, P10 |
| 84% 权限提示（Claude Code 沙箱） | P12, P16 |
| METR 50% 可靠性 7 个月翻倍 | P4 |
| context rot（塞得越多记得越差） | P5, P17 |
| 260 万（不是 2.6 亿） | P7 |
| 2026 CVE / authorize at execution | P14, P17 |
| "都不必改 loop" | P20 |
| 15 行 YAML 挂 vendor | P20 |
| 五角色阶梯（说话者→编排者） | P2, P22 |
| slogan「装自己的，借现成的」 | P18, P22 |
| 教小孩做菜比喻（Guides/Sensors） | P11 |
| 精装公寓比喻（固定 vs 灵活） | P15 |

## 更新纪律

- **改内容**：先在「正向脉络」改对应页 → 同步「关键事实索引」→ 检查反向索引里同一上游的其他页是否受影响。
- **改口径/数字**：只动 `00-absorption-plan.md` 第三节红线 → 再按「关键事实索引」逐页核对引用。
- **新增页面素材**：先定上游源 → 写进对应内容文件 → 再补进本图三张表。
