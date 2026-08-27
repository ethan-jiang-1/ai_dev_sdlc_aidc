# 内容吸纳清单（v1.2）· 什么吸进 talk、什么舍弃

> 依据：三份 rawdata 研读（era 章节 + DSH FAQ + `_digested`，见 `../_reference/README.md`）。映射到 [`../03_outline/00-page-structure-23.md`](../03_outline/00-page-structure-23.md)（23 页现场版）。
> 每一条标来源。这是"内容填充"前的进货单——先定进什么货，再逐页填。页编号以现场版 P 为准。

## 一、本轮新增的「故事线资产」（强到影响讲法）

1. **一人公司点题焊点（06 章角色表）**：「责任的叠加上移，不是岗位替代」；一个成熟团队需要五种角色
   （prompt 设计师 → context 平台 → harness SRE → loop 设计师 → graph 架构师），"或被同一人承担"——
   一人公司就是"被同一人承担"的极端情况。→ 开场 / 收尾直击主题。
2. **承重墙的机制级论据（06 章）**：「假设下层正确是 bug 的来源；对下层显式验证，是工程成熟度的标志。」
   → 解释"为什么最底下那层最关键"。
3. **上层也在长 harness（05 章 GraphARC）**：模型提议工作图 → **确定性 checker 放行/拒绝** → 才执行
   （plan → check → execute）。→ harness 式门禁哲学向上渗透，佐证 harness 是地基。
4. **人机互动线的硬佐证**：Cherny「I don't prompt Claude anymore. My job is to write loops.」/
   Steinberger「designing loops that prompt your agents」/ Walden Yan 一年内从「别建多 agent」改口「有些 setup 真能用」。
   → 开场钩子更实。
5. **DSH 灵活性金句（FAQ）**：
   - "Agents follow enforced gates far more reliably than prose conventions."（07）
   - "Each fact has one home: the tier whose job it is; elsewhere, link there."（根入口文档）
   - "There is no privileged core to patch: you extend dsh by mounting a plugin beside the others."（architecture）
   - "加模型提供方：在 ctx.llm 上注册 adapter……加面向模型的能力：在 ctx.tools 上注册……都不必改 loop。"（`../_reference/rawdata_dsh-digested/tools-prompt-llm`）
6. **DSH 爆发不是成熟度证明**：GitHub API 快照（2026-08-27）显示 `deepseek-ai/deepseek-harness` 自 2026-08-13 创建后约 14 天达到 199,846 stars / 22,820 forks；同一生态数据快照有 2,286 条条目。二者证明注意力与扩展面快速聚集；不证明插件质量、可信度或生产成熟度。
7. **自用 owner 的三层收益**：省手（可换执行底座）、敢放手（成对审批、fail-closed、可重建）、可复用（preset / bundle / patch 跨项目迁移）。生态的意义是有人替你踩过路，不是要 OPC 去经营市场。
8. **最终控制权的机制定义**：当插件进入模型可见面或真实执行路径，owner 必须能控制接入、替换、放行和重建；插件化本身不等于安全，`installable` 也不等于 `trustworthy`。

## 二、按幕 / 页映射（进货单）

### 开场（P1–3）
| 吸什么 | 来源 |
|---|---|
| 角色表：五角色 → "被同一人承担" = 一人公司 | 06 章 |
| 钩子金句：Cherny / Steinberger（人从写 prompt 到写 loop） | 04 章 |

### 第一幕 五层（P4–8）
| 页 | 吸什么 | 来源 |
|---|---|---|
| P4 发动机 | METR「50% 可靠性任务长度每 ~7 个月翻倍」+ Anthropic「prompt 措辞越来越不重要」 | 01/02 章 |
| P5 Prompt+Context（合并） | 「行为控制面」；「把系统问题塞进更长 prompt，只是把缺失的控制面伪装成提示复杂度」；SWE-bench 最小脚手架「The agent has a prompt, a Bash Tool, and an Edit Tool」；context rot（Lost in the Middle 两头好中间差）；「更多 context ≠ 更好回忆」；MCP/RAG 生态事件 | 01/02 章 |
| P6 Harness（埋雷） | 「单次运行容器」 | 03 章 |
| P7 Loop+Graph（合并） | loop 引擎「模型越强越能知错改错，反馈得当就越迭代越好」；「replacing yourself as the person who prompts」；黄金法则「只有上次结果改变下次行动才算 loop」；反转「loop 可能错得更贵」（Woliveiras）；graph 本质 = 编排（orchestration：workflow/DAG 约束乱发挥、换可靠结果）；双源定义「state graphs」/「From Individual to System Intelligence」；定位「有道理，但只解决特定，还在发展」 | 04/05 章 |
| P8 叠加 | 「扳手/螺丝刀」比喻；「概念火六周就被接棒 = 叙事期」 | 06 章 |

### 第二幕 harness（P9–14）
| 页 | 吸什么 | 来源 |
|---|---|---|
| P9 转折 | 口径：报告把 Context 与 Harness **并列**；"harness 最重要"是我们的判断，用三线撑（结构/哲学/风险） | 03/06 章 |
| P10 定义 | "Agent = Model + Harness"；harness = 模型之外的一切 | 03 章 |
| P11 两套控制+comp/infer（合并） | Guides（前馈）+ Sensors（反馈）；computational 可审计 vs inferential 不可审计；确定性优先 | 03 章 |
| P12 抓要害 | 圈住 / 拦住 / 看清（见 06-harness-internals.md） | 03 章 |
| P13 承重墙 | 结构线（Osmani「one floor above」/ Macedo「engine & pilot」）+ 哲学线（反馈同源 Sensors→loop + 验证梯渗透 + GraphARC 门禁）+ 机制金句「假设下层正确是 bug 的来源」；三层同一件事（反馈 + 确定性 → 可靠） | 04/05/06 章 |
| P14 反面 | 2026 CVE「authorize at execution, not at generation」 | 03 章 |

### 第三幕 固定 vs 灵活（P15–18）
| 页 | 吸什么 | 来源 |
|---|---|---|
| P15 抉择 | 固定 vs 灵活轴（不是"自己做 vs 现成"的二选一）；精装公寓比喻 | 立场（故事线 v1.2，自拟） |
| P16 现成的好 | 「harness 组件随产品交付（民主化）」：Claude Code 沙箱、Copilot sandboxes、MCP 生态 | 03 章 |
| P17 DSH 爆发 | GitHub 公开后约 14 天近 20 万 star；生态快照 2,286 条；桥 / 渠 / 窗三类扩展；爆发不等于成熟 | GitHub REST API（2026-08-27 快照）；`rawdata_dsh-plugin-ecosystem-distribution/answer.md` |
| P18 OPC 收益 | 省手 / 敢放手 / 可复用；生态是可借用的已踩路径 | `rawdata_dsh-plugin-business-ladder/answer.md` |

### 第四幕 DSH（P19–21）
| 页 | 吸什么 | 来源 |
|---|---|---|
| P19 定位 | DSH 不是商店、不是更强 Loop；是可组合 Harness runtime，插件围绕共同合同与事实记录工作 | `rawdata_dsh-digested/system/00-map.md`；FAQ 01 |
| P20 只有插件不够 | 固定产品的公开合同决定能改变什么；模型可见能力与真实执行需要合同、门禁、记录；可安装不等于可信 | FAQ 08 / `system` / `session-and-loop` |
| P21 最终控制权 | 接入 / 替换 / 放行 / 重建；adapter、seam、gate、session log 是机制证明；"enforced gates" 金句 | FAQ 07 / FAQ 08 / `_digested` |

### 收尾（P22–23）
| 页 | 吸什么 | 来源 |
|---|---|---|
| P22 回答+slogan（合并） | 角色表回扣：一人公司 = 被同一人承担五角色，harness 这格要能改；slogan「装自己的，借现成的」 | 06 章 |
| P23 收尾 | 谢谢 + slogan 落款 + 联系方式占位 | 结构（自拟） |

## 三、口径红线（引用前必查）

| # | 事项 | 正确口径 |
|---|---|---|
| 1 | Steinberger graph 帖浏览量 | 260 万 / 2 天（"2.6 亿"是误传） |
| 2 | Loop 定义 → 被接棒 | 约 6 周（一说两个月） |
| 3 | corpus 百分比（70%/22%/74%/20%/32%） | Macedo 50-loop 样本，非 974 资源 |
| 4 | 三范式量化表（60/75/90%） | 二手渠道（Tencent Cloud），慎用 |
| 5 | Anthropic 三 Agent 实验 | n=1 示例，非定律 |
| 6 | Andrew Ng graph playbook | 出处未经证实，避开 |
| 7 | "挂 MCP" | DSH 不用 MCP；`../_reference/rawdata_dsh-digested/` 里 MCP 仅 2 处顺带（ACP 明确"故意不保证 MCP"）。DSH 挂的是 ctx.llm adapter / ctx.tools / capability seam / plugin。MCP 只在 Context era（P5）作生态事件提 |
| 8 | DSH GitHub / 插件爆发 | GitHub star 是 2026-08-27 的 API 快照，措辞用“约 14 天、近 20 万 star”，不可暗示持续曲线；2,286 是单一生态数据快照，不能与 5,886 / 11,424 等目录站口径混用；两者均不作质量或安全证明 |

## 四、待验证（下一步）

- [x] DSH 是否支持 MCP：**不支持为原生机制**（`../_reference/rawdata_dsh-digested/surfaces/02-acp与jsonrpc.md`：ACP 明确"故意不保证 MCP"，`session/new` 的 mcpServers 非空即拒绝）。P20 说"挂模型 / 挂工具 / 换后端 / 挂插件"；MCP 只在 Context era（P5）提。
- [ ] Steinberger loop 帖原始浏览量（多渠道口径不一，以 X 为准）。
- [ ] 若引用 LoopsBench 数字，用 arXiv 2608.00267（112 任务 / 8 语言 / 9 领域 / 37,296 测试）。
