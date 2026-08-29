# 转折点 / 锚点清单（v0.7 · 软件 SDLC）

> 本 talk 两轴各有一组锚点。**深轴**（五层 + harness）锚点与 `-opc` 共享；**宽轴**（六阶段 SDLC）锚点来自
> Anthropic playbook。完整按页进货单见 `../02_evidence/00-absorption-plan.md`。

## 深轴锚点（五层 + harness，与 -opc 共享）

| Era | 锚点 | 日期 | 在本 talk 里的读法 |
|---|---|---|---|
| Prompt | METR 长任务评估；SWE-bench Verified 最小脚手架 | 2025-03 / 2024-10 | 意图表达镜头：Plan 能否形成下一角色可读的输入 |
| Context | Anthropic context engineering；context rot | 2025-09 / 2023 | 事实策展镜头：Design / Build 看见的约束是否正确且有版本 |
| Harness | Böckeler "Agent = Model + Harness"；Claude Code 沙箱（-84% 权限提示） | 2026-02/04 / 2025-10 | 运行边界镜头：平台共同基线覆盖 Build / Test / Deploy |
| Loop | 定义爆发；黄金法则；"六周热度" | 2026-06 | 反馈镜头：结果能否安全回流，错误能否在扩大前被 gate 拦住 |
| Graph | Steinberger 引爆；GraphARC admission gate | 2026-07/08 | 编排镜头：多执行单元能否按合同协作并保留责任边界 |
| 风险 | authorize at execution, not at generation | 待具体事件卡片 | 授权原则：护栏必须在工具执行时独立生效 |

## 宽轴锚点（六阶段 SDLC + 工件链，来自 Anthropic playbook）

| 锚点 | 内容 | 作用 |
|---|---|---|
| **代码不再是瓶颈** | 当 build 被显著压缩，慢点会移向 plan/review/test/deploy | 全场诊断入口（Anthropic 论点，需用听众自身数据验证） |
| 三个后果 | 瓶颈左移右移 / 旧控制失效 / 治理成本上升 | 论证"为什么整条 SDLC 要转型" |
| **工件链是审计的骨架** | `intent → spec → plan → diff+tests → PR+review → incident` | 加上身份 / 版本 / 证据 / 审批 / 不可绕过的 gate 才承担审计 |
| intent.md | 意图一次捕获，originator 自己的话 + 产品 owner 审批 | Plan 的转变 |
| spec.md + skills | 需求+设计合一，政策在写 spec 时施加 | Design 的转变 |
| plan.md + AGENTS.md + hooks | plan mode / 知识外置 / 确定性 guardrail | Build 的转变（harness 主战场） |
| evals | 对 harness 配置的回归测试 | Test 的转变（治理） |
| managed settings | permissions/sandbox/credentials/marketplaces/min version | Deploy 的治理（受监管企业实例） |
| 关 loop | control-band breach → intent.md 重新入环 | Maintain 的转变（Loop/Graph 组织化） |
| **机器守确定性 gate，人守判断 gate** | human judgment remains accountable；deterministic controls where expressible | 治理主线 |
