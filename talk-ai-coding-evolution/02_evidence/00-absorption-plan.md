# 内容吸纳清单（v1.1）· 什么吸进 talk、什么舍弃

> 依据：三份 rawdata 研读（era 章节 + DSH FAQ + `_digested`）。映射到 [`../03_outline/00-page-structure-23.md`](../03_outline/00-page-structure-23.md)（23 页现场版）。
> 每一条标来源。这是"内容填充"前的进货单——先定进什么货，再逐页填。
> **编号说明**：表中 S 编号对应内容文件内部小节（素材锚点，与旧 27 页编号一致）；现场页编号以 P 为准。

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
   - "加模型提供方：在 ctx.llm 上注册 adapter……加面向模型的能力：在 ctx.tools 上注册……都不必改 loop。"（_digested tools-prompt-llm）

## 二、按幕 / 页映射（进货单）

### 开场（S1–3）
| 吸什么 | 来源 |
|---|---|
| 角色表：五角色 → "被同一人承担" = 一人公司 | 06 章 |
| 钩子金句：Cherny / Steinberger（人从写 prompt 到写 loop） | 04 章 |

### 第一幕 五层（S4–10）
| 页 | 吸什么 | 来源 |
|---|---|---|
| S4 发动机 | METR「50% 可靠性任务长度每 ~7 个月翻倍」+ Anthropic「prompt 措辞越来越不重要」 | 01/02 章 |
| S5 Prompt | 「行为控制面」；「把系统问题塞进更长 prompt，只是把缺失的控制面伪装成提示复杂度」；SWE-bench 最小脚手架「The agent has a prompt, a Bash Tool, and an Edit Tool」 | 01 章 |
| S6 Context | 定义「策划并维护最优 token 集合」；context rot（Lost in the Middle 两头好中间差）；「更多 context ≠ 更好回忆」 | 02 章 |
| S7 Harness | （埋雷）「单次运行容器」 | 03 章 |
| S8 Loop | 定义「replacing yourself as the person who prompts」；黄金法则「只有上次结果改变下次行动才算 loop」；反转「loop 可能错得更贵」（Woliveiras） | 04 章 |
| S9 Graph | 双源定义「state graphs」/「From Individual to System Intelligence」；反转「不是新东西」+「术语先于发布」 | 05 章 |
| S10 叠加 | 「扳手/螺丝刀」比喻；「概念火六周就被接棒 = 叙事期」 | 06 章 |

### 第二幕 harness（S11–17）
| 页 | 吸什么 | 来源 |
|---|---|---|
| S11 转折 | 口径：报告把 Context 与 Harness **并列**；"harness 最重要"是我们的判断，用三线撑（结构/哲学/风险） | 03/06 章 |
| S12 定义 | "Agent = Model + Harness"；harness = 模型之外的一切 | 03 章 |
| S13 两套控制 | Guides（前馈）+ Sensors（反馈） | 03 章 |
| S14 comp vs infer | 确定性可审计、概率不可审计；确定性优先 | 03 章 |
| S15 抓要害 | 圈住 / 拦住 / 看清（见 06-harness-internals.md） | 03 章 |
| S16 承重墙 | 结构线（Osmani「one floor above」/ Macedo「engine & pilot」）+ 哲学线（验证梯渗透 + GraphARC 门禁）+ 机制金句「假设下层正确是 bug 的来源」 | 04/05/06 章 |
| S17 反面 | 2026 CVE「authorize at execution, not at generation」 | 03 章 |

### 第三幕 固定 vs 灵活（S18–21）
| 页 | 吸什么 | 来源 |
|---|---|---|
| S18 抉择 | 固定 vs 灵活轴（不是"自己做 vs 现成"的二选一）；精装公寓比喻 | 立场（故事线 v1.2，自拟） |
| S19 现成的好 | 「harness 组件随产品交付（民主化）」：Claude Code 沙箱、Copilot sandboxes、MCP 生态 | 03 章 |
| S20 现成的卡 | 想改 harness 本身受限；反例 = 2026 CVE（执行时授权）+ loop blast radius | 03/04 章 |
| S21 本质 | 不是"别用现成"，是"别只能现成"；装自己的 + 借现成的 | 自拟（06 章两线支撑） |

### 第四幕 DSH（S22–24）
| 页 | 吸什么 | 来源 |
|---|---|---|
| S22 DSH | "There is no privileged core to patch: extend by mounting a plugin beside the others." | FAQ 01 / architecture |
| S23 双向灵活 | 装自己的 = 挂模型（ctx.llm adapter）+ 挂工具（ctx.tools）+ 换后端（capability seam）+ 挂插件（mount a plugin beside the others）；借现成的 = vendor / adapter（协议兼容纯配置）。金句：「都不必改 loop」 | _digested tools-prompt-llm/capability-seams + FAQ 03 |
| S24 哲学 | "Agents follow enforced gates far more reliably than prose conventions." + GraphARC 门禁作行业先例 | FAQ 07 / 05 章 |

### 收尾（S25–27）
| 页 | 吸什么 | 来源 |
|---|---|---|
| S25 回答 | 角色表回扣：一人公司 = 被同一人承担五角色，harness 这格要能改 | 06 章 |
| S26 slogan | 装自己的，借现成的（待定） | — |

## 三、口径红线（引用前必查）

| # | 事项 | 正确口径 |
|---|---|---|
| 1 | Steinberger graph 帖浏览量 | 260 万 / 2 天（"2.6 亿"是误传） |
| 2 | Loop 定义 → 被接棒 | 约 6 周（一说两个月） |
| 3 | corpus 百分比（70%/22%/74%/20%/32%） | Macedo 50-loop 样本，非 974 资源 |
| 4 | 三范式量化表（60/75/90%） | 二手渠道（Tencent Cloud），慎用 |
| 5 | Anthropic 三 Agent 实验 | n=1 示例，非定律 |
| 6 | Andrew Ng graph playbook | 出处未经证实，避开 |
| 7 | "挂 MCP" | DSH 不用 MCP；`_digested` 里 MCP 仅 2 处顺带（ACP 明确"故意不保证 MCP"）。DSH 挂的是 ctx.llm adapter / ctx.tools / capability seam / plugin。MCP 只在 Context era（S6）作生态事件提 |

## 四、待验证（下一步）

- [x] DSH 是否支持 MCP：**不支持为原生机制**（`_digested/surfaces/02-acp与jsonrpc.md`：ACP 明确"故意不保证 MCP"，`session/new` 的 mcpServers 非空即拒绝）。S23 说"挂模型 / 挂工具 / 换后端 / 挂插件"；MCP 只在 Context era（S6）提。
- [ ] Steinberger loop 帖原始浏览量（多渠道口径不一，以 X 为准）。
- [ ] 若引用 LoopsBench 数字，用 arXiv 2608.00267（112 任务 / 8 语言 / 9 领域 / 37,296 测试）。
