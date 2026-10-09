# 104 来源台账

## 使用口径

本轮是仓库材料消化，不是外部研究；没有在线访问原文、核准产品配置或运行示例。指定playbook的917行已完整读取（1–687、688–917）；日期、作者、产品名与设置名均是仓库留存文本自述，不表示本轮确认当前有效性。

来源级别固定为三类，不用文件自带的 `verified/S` 标签代替本轮判断：

- **仓库留存厂商文章**：有原始URL的厂商正文，支持“厂商这样建议/描述”，不自动支持跨组织效果或通用规范；不是本轮在线核准。
- **已有研究归纳**：仓库判读、回源摘录和实践主干；可作机制解释与设计线索，不升级为厂商逐字原话。
- **本场教学设计**：104合成工单助手的机制、字段及测试预期；未实现、未运行，不填成功率、实测日志或批准凭据。

本文件维护来源与主张强度；转化和限制见[工程阅读笔记](<01-engineering-reading-notes.md>)。行号对应本轮读取版本，原文改变须重新定位。

## 来源与可用主张

| ID | 来源级别与来源 | 核心可用主张 / 锚点 | 104使用边界 |
|---|---|---|---|
| S01 | 仓库留存厂商文章：[AI-native SDLC playbook](<../../02_research/02_ai_sdlc/02_industry_playbooks/anthropic/org/ai-native-sdlc-playbook.md>)；[原始URL](https://claude.com/blog/the-ai-native-sdlc-playbook)。文件1–3行自述Louis Claxton、2026-08-21 | 49–60行：意图、规格、计划、变更与审阅形成交接和审计链；96、174–177行：人纠正与批准；262–270行：逐工件指定权威系统 | 主对象是开发Agent及交付流程。工件存在不等于正确，git作者不等于有权批准者；不把“代码已不是瓶颈”当所有团队事实 |
| S02 | 同S01 | 204–219行：实施前写计划、指明文件与验证、偏离时同步；274–287行：运行入口和高频错误知识版本化；325–367行：技能触发测试与advisory性质 | 取工程思路，不介绍未核准的plan/auto mode行为与设置；skill是辅助指令，不是权限控制 |
| S03 | 同S01 | 374–386、607–660行：程序化拦截与批准门；662–720行：管理设置、沙箱、凭据及工具范围组合；720行明确“起点，非复制推荐” | hook只约束实际经过且匹配的路径；短语匹配门禁与环境变量不构成有效生产授权；配置名、版本和日志能力未在线核准 |
| S04 | 同S01 | 392–412行：独立任务/worktree与共享文件串行；443–464行：可执行反馈、先复现再修复及保护检查；445行：独立验证上下文与持续反馈环不同 | 独立上下文/worktree不自动隔离数据库、凭据、网络或业务对象。冻结测试仅增强特定回归证据，不能证明全局可靠 |
| S05 | 同S01 | 493–510行：配置变更触发eval、事故补回归；512–537行：CI示例；541–546行：记录与比较结果 | 示例评估开发Agent，不是业务助手评估集。20–50是起步建议；样例没有逐题重建干净工作区/隔离状态，不能直接当可复现实验 |
| S06 | 同S01 | 568–598行：审阅发现与人批准分开；729–747行：受限凭据、先只读、按环境放权及演练回滚；781–822行：事件触发、确定性检测与门禁处置 | 独立审阅不自动准确；1σ/2σ/3σ及30日窗口只是示例，不是风险等级或正确性置信度。部署回滚不撤销外部副作用 |
| S07 | 仓库留存厂商文章：[Building effective agents全文](<../../02_research/02_ai_sdlc/03_org_and_management/teams/raw/anthropic_building_effective_agents.md>)；[原始URL](https://www.anthropic.com/engineering/building-effective-agents)。文件3–5行标2024-12-19、Erik Schluntz/Barry Zhang | 19–28、154–164行：预定义流程与模型自主路径区别，先选最简单方案，复杂性须有收益；61–78行：链式检查与路由；133–141行：环境事实、人工检查点、停止条件与沙箱测试 | 补业务Agent架构依据；厂商经验不是“全部业务必须图工程”的证明。留存正文含后续产品名称，不拿文件日期推断全部内容当年已存在 |
| S08 | 同S07 | 174–196行：客服与编码是不同应用，编码自动测试仍需人审；200–217行：工具定义要解释边界、例子、输入要求并测试使用行为 | 支持工具接口建设，不直接提供幂等、事务或业务授权完整规范；客服退款举例不能成为104退款授权 |
| S09 | 已有研究归纳：[loop入口](<../../02_research/01_agent_engineering/loop_engineering/README.md#L46-L69>)；[反馈接口判读](<../../02_research/01_agent_engineering/loop_engineering/digested/09-feedback-harness-interface.md#L9-L51>) | 入口53–69行：目标→行动→反馈→裁决→继续/停止/升级；反馈18–20、45–51行：有日志不等于被消费；证据绑定版本，异常与目标失败分开，有恢复和接手依据 | 仓库研究归纳；反馈97–101行明确机制证据非效果。“未执行/失败/结果未知”分账是104设计，不冒称产品统一实现 |
| S10 | 已有研究归纳：[机器门摘录](<../../02_research/01_agent_engineering/loop_engineering/stop_conditions/01_machine_gates/practices.md#L26-L82>)；[资源上限摘录](<../../02_research/01_agent_engineering/loop_engineering/stop_conditions/02_hard_caps/practices.md#L11-L61>)；[裁决分离摘录](<../../02_research/01_agent_engineering/loop_engineering/stop_conditions/03_verdict_split/practices.md#L11-L69>) | 环境检查、硬预算与干活/裁决分工是不同控制件；资源停止不代表质量通过；独立裁判有能力边界 | 转引档案，非本轮逐产品核准；不照抄固定轮数、产品默认值或“不会说谎/近乎不可能”等强措辞 |
| S11 | 已有研究归纳：[goal构造](<../../02_research/01_agent_engineering/goal_eval_engineering/digested/01-goal-构造.md#L9-L25>)；[eval调优](<../../02_research/01_agent_engineering/goal_eval_engineering/digested/02-eval-调优.md#L26-L42>)；[难设计](<../../02_research/01_agent_engineering/goal_eval_engineering/digested/03-难设计.md#L5-L29>) | 可见终态与不可见业务结果分开；先观察失败再构造判据，裁判与人对齐；验不动时切小块、补观测或保留人工判断 | 不搬研究效果数字当本场收益；样本量、评分刻度和场景不互套；eval集变更后分数不能无条件横比 |
| S12 | 已有研究归纳：[graph入口](<../../02_research/01_agent_engineering/graph_engineering/README.md#L59-L84>)；[工作流转述档案](<../../02_research/01_agent_engineering/graph_engineering/raw/evidence-202603-anthropic-workflow-patterns.md#L19-L30>)；[状态机转述档案](<../../02_research/01_agent_engineering/graph_engineering/raw/evidence-2026-langgraph-temporal-state-machines.md#L21-L53>) | 提供节点依赖、工件接口和状态恢复研究视角，帮助识别“谁推进状态、谁交付什么” | 后两件没有具体逐段URL/版本，虽自标S/verified，本轮只按研究转述；入口“必然上限/终局”等不当行业实证。最小架构原则主引S07，不引拼接引句 |
| S13 | 已有研究归纳：[实践总入口](<../../03_practice/README.md#L6-L23>)；[harness入口](<../../03_practice/harness_governance/README.md#L51-L55>)；[loop入口](<../../03_practice/loop_governance/README.md#L41-L48>)；[graph入口](<../../03_practice/graph_governance/README.md#L43-L52>) | 环境约束、循环控制及跨节点协作分工；知识、规格与规则需维护，不只增加文件；检查点和接手明确负责人 | 仓库方法归纳而非厂商标准；graph中的≤3次重试、≤2次重排、100%/终局不升格为104规范；不引入不需要的复杂多Agent拓扑 |
| T01 | 本场教学设计；范围依据[104定位](<../README.md#L13-L17>)和[表达边界](<../CONTEXT.md#L13-L39>) | 售后工单助手先分流/检索/建议，有效授权后创建内部任务；禁止退款、承诺赔付及对外发送。工具契约、幂等、原子保存、恢复查询、评估与发布记录由104明确设计 | 未运行，字段、流程和故障注入都是提案/预期；具体案例以104案例源为权威，本台账不复制案例事实或另定数值 |

## 不采用的推断

不把官方建议、仓库研究判断与104设计合成“行业已证明”；不把一次通过、独立上下文、结构化JSON、短语命中、环境变量存在或代码回滚解释成稳定、隔离、真实、批准、授权或业务撤销。未在线核准的产品行为只能说“留存材料描述”，不能说“当前已验证”。
