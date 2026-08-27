# 信息脉络图 · 上游 → 加工 → 页面（talk 的 provenance + trace）

> **用途**：推敲某一页时，脉络一眼清楚——这页的内容从哪来、改一处会牵动哪些页。
> 对应现场版 `../03_outline/00-page-structure-23.md`（P1–P23）；加工层引用的内容文件小节 = 同名 P 编号。
> 口径红线见 [`00-absorption-plan.md`](./00-absorption-plan.md) 第三节。

## 正向脉络：页 → 加工层 → 上游

| 页 | 关键内容 | 加工层（内容文件 + 吸纳清单） | 上游来源 |
|---|---|---|---|
| P1 封面 | 官方题目 + 开场问题 | 01-opening P1 | 用户定题（无上游） |
| P2 钩子 | 五角色阶梯；Cherny 金句 | 01-opening P2；吸纳 §一.1/.4 | 06 角色表；04 Cherny |
| P3 路线图 | 四站 | 01-opening P3 | 故事线 v1.2（自拟） |
| P4 发动机 | METR 7 个月翻倍；prompt 措辞不重要 | 01-opening P4；§二 P4 | 01（METR）；02（Anthropic） |
| P5 Prompt+Context | 行为控制面；伪装成提示复杂度；context rot；MCP/RAG | 01-opening P5；§二 P5 | 01；02（context rot、MCP/RAG） |
| P6 Harness 埋雷 | Agent=Model+Harness；单次运行容器 | 01-opening P6；§二 P6 | 03 §一/§七 |
| P7 Loop+Graph | 黄金法则；blast radius；有道理但只解决特定；260 万 | 01-opening P7；§二 P7 | 04；05 |
| P8 叠加观+成熟度 | 扳手/螺丝刀；成熟度标尺 | 01-opening P8；§二 P8 | 06 |
| P9 转折 | 承重墙判断 + 口径（我们的判断，三线撑） | 02-act2 P9；§二 P9 | 06（Context/Harness 并列） |
| P10 定义 | Agent=Model+Harness；SWE-bench 脚手架金句 | 02-act2 P10；§二 P10 | 03 §一；01 §二 |
| P11 两套控制+comp/infer | Guides/Sensors；npm test vs AI；教小孩做菜 | 02-act2 P11；§二 P11 | 03 §一 |
| P12 圈住拦住看清 | 模型给能力 harness 给可靠性；84% | 02-act2 P12；§二 P12 | 03 §五；01_storyline/06-harness-internals |
| P13 承重墙 | one floor above；engine & pilot；GraphARC；假设下层正确 | 02-act2 P13；§二 P13 | 04；05（GraphARC）；06 |
| P14 CVE | authorize at execution | 02-act2 P14；§二 P14 | 03 §二 |
| P15 抉择 | 固定 vs 灵活轴；精装公寓比喻 | 03-act3 P15；§二 P15 | 故事线 v1.2 立场（自拟） |
| P16 固定的好 | 民主化；84%；simplest viable system | 03-act3 P16；§二 P16 | 03 §二/§五；04（Osmani） |
| P17 DSH 爆发 | GitHub 近 20 万 star（14 天快照）；2,286 条生态快照；爆发不等于成熟 | 03-act3 P17；§二 P17 | GitHub REST API（2026-08-27）；`rawdata_dsh-plugin-ecosystem-distribution` |
| P18 OPC 收益 | 省手 / 敢放手 / 可复用；生态是可借用的已踩路径 | 03-act3 P18；§二 P18 | `rawdata_dsh-plugin-business-ladder/answer.md` |
| P19 DSH 定位 | 可组合 Harness runtime，而非商店或更强 Loop | 04-act4 P19；§二 P19 | `_digested/system`；FAQ 01 |
| P20 只有插件不够 | 产品公开合同；能力进入真实执行时的合同、门禁、记录 | 04-act4 P20；§二 P20 | FAQ 08；`_digested/session-and-loop` |
| P21 最终控制权 | 接入 / 替换 / 放行 / 重建；enforced gates | 04-act4 P21；§二 P21 | FAQ 07 / 08；`_digested` |
| P22 回答+slogan | 角色表回扣；装自己的借现成的 | 04-act4 P22；§一.1 | 06 角色表；slogan（用户定方向） |
| P23 收尾 | 谢谢 + slogan | 04-act4 P23 | 结构（自拟） |

## 反向索引：上游 → 用到它的页

| 上游源 | 用到它的页 |
|---|---|
| `../_reference/rawdata_ai-coding-evolution-final/final_v4/01-2025-prompt-era.md` | P4, P5, P10 |
| `../_reference/rawdata_ai-coding-evolution-final/final_v4/02-mid-2025-context-era.md` | P4, P5, P17 |
| `../_reference/rawdata_ai-coding-evolution-final/final_v4/03-2026-harness-era.md` | P6, P10, P11, P12, P14, P16, P17 |
| `../_reference/rawdata_ai-coding-evolution-final/final_v4/04-2026-loop-era.md` | P2, P7, P13, P16 |
| `../_reference/rawdata_ai-coding-evolution-final/final_v4/05-2026-graph-era.md` | P7, P13, P21 |
| `../_reference/rawdata_ai-coding-evolution-final/final_v4/06-five-layer-forward.md` | P2, P8, P9, P13, P22 |
| `../_reference/rawdata_dsh-plugin-ecosystem-distribution` | P17 |
| `../_reference/rawdata_dsh-plugin-business-ladder` | P18 |
| `../_reference/rawdata_dsh-plugin-seam-maturity` | P20, P21 |
| `../_reference/rawdata_dsh-faq-on-digested/01_repository-organization` | P19 |
| `../_reference/rawdata_dsh-faq-on-digested/07_borrowing-harness-idea` | P18（收益）+ P21（门禁） |
| `../_reference/rawdata_dsh-digested/system` | P19 |
| `../_reference/rawdata_dsh-digested/tools-prompt-llm` | P21 |
| `../_reference/rawdata_dsh-digested/capability-seams` | P21 |
| `../_reference/rawdata_dsh-digested/surfaces` | P17/P20 口径（MCP 结论） |
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
