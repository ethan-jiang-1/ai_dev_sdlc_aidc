# 核心主张证据账本（v0.7）

> 目的：让后续 50 页写稿、speaker notes 与现场口径能区分**来源原文**、**本 talk 综合判断**与**听众需用自身数据验证的假设**。
> 范围只限软件 SDLC。

## C1 · 当构建加速，瓶颈会移向代码两侧

- **类型**：外部观点 + 听众自证的诊断假设。
- **来源**：`../_reference/rawdata_anthropic-ai-native-sdlc-playbook.md`，「Code is no longer the bottleneck」。原文主张构建被压缩后，规划、审查与测试、发布仍以人的速度运行，旧控制失配，例外治理成本上升。
- **可说**：「Anthropic 的诊断是：当构建不再是主要约束，瓶颈会移向代码两侧。」
- **不可说**：「所有组织都已经代码产出翻倍，交付却没变。」
- **听众自证**：对比编码时间（coding time）占端到端交付周期（lead time）的比例；再拆分排队时间、首次审查时间、审批等待时间、部署交付周期、返工轮次与变更失败率。
- **页面**：P2–P3、P6、P49。

## C2 · AI-native SDLC 的改造对象是交付系统

- **类型**：本 talk 的中心命题，由 playbook 多处证据综合。
- **来源**：playbook 的「What is an AI-native SDLC?」、six-stage shifts、committed artifact 段、每个 play 的 governance / measure 部分。
- **综合表达**：「工件可交接、gate 可执行、owner 可问责、feedback 可回流」是本 talk 对上述素材的叙事压缩，不是 playbook 原句。
- **页面**：P9、P12、P13–P38、P50。

## C3 · 工件链是审计的骨架，不是自动等于合规

- **类型**：来源事实 + 本 talk 的严格化综合判断。
- **来源事实**：playbook 明确说每阶段提交下一阶段可读的 artifact，commit chain 记录「who asked for what, what the agent produced, and who approved it」。PR history、hook decisions、pipeline identity 与 incident channel 分别补充 review、放行、执行和故障证据。
- **综合判断**：只有能重建「身份 / 当时版本 / 输入与结果证据 / 审批 / 不可绕过的 gate」，工件链才能承担审计。这五个条件是本 talk 的综合框架，不宣称是某一外部标准的完整合规要求。
- **页面**：P10 留问，P39 回答，P47 补「可重建事实」。

## C4 · 机器守确定性 gate，人守判断 gate

- **类型**：多源综合原则。
- **来源**：playbook 的 human judgment / approval gates / separation of duties / authorize-at-execution 机制；`../_reference/rawdata_ai-coding-evolution-final/final_v4/03-2026-harness-era.md` 的 Guides / Sensors 框架；DSH 的 enforced gates / invariant 机制。
- **口径**：确定性可表达的规则不降级为纯概率判断；AI review 可留痕和复核，但不冒充可复现证明。意图、风险、例外与生产授权的最终责任不外包。
- **页面**：P9、P23、P28–P34、P40、P45。

## C5 · 共享控制面，分布领域知识

- **类型**：本 talk 的组织设计综合。
- **来源**：playbook 的 managed settings、organization skills、policy owner、product owner、code owner、release manager 分工；五层组织读法；DSH 的 knowledge ownership / capability seam / gate / session log。
- **综合表达**：平台集中沙箱、权限、工具准入、门禁、观测和审计；领域 owner 负责 intent、context、政策例外与价值取舍。这是「控制集中、知识分布」，不是把所有软件业务强行统一。
- **页面**：P5、P16/P19/P25/P29/P34/P38、P41–P48。

## C6 · 采用顺序是先工件、再 gate、最后关 loop

- **类型**：本 talk 的采用建议。
- **来源支撑**：playbook 强调 plays 的 stage order 与 adoption dependency 不同，每个 play 有 prerequisites；Maintain 依赖 PR review gate / approval gate / `intent.md` / evals。DSH 的正确路径与可执行反馈也要求事实与合同先存在。
- **综合理由**：没有可交接工件，loop 无事实可读；没有可执行 gate，loop 会放大错误。
- **页面**：P13、P48、P50。
