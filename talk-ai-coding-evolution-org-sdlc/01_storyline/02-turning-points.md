# 转折点 / 锚点清单（v0.5）

> 本 talk 两轴各有一组锚点。**深轴**（五层 + harness）锚点与 `-opc` 共享；**宽轴**（六阶段 SDLC）锚点来自
> Anthropic playbook。完整按页进货单见 `../02_evidence/00-absorption-plan.md`。

## 深轴锚点（五层 + harness，与 -opc 共享）

| Era | 锚点 | 日期 | 在本 talk 里的读法 |
|---|---|---|---|
| Prompt | METR 长任务评估；SWE-bench Verified 最小脚手架 | 2025-03 / 2024-10 | 任务层起点：一线工程师的"表达"能力 |
| Context | Anthropic context engineering；context rot | 2025-09 / 2023 | 任务层：组织知识如何被"策展"成模型所见 |
| Harness | Böckeler "Agent = Model + Harness"；Claude Code 沙箱（-84% 权限提示） | 2026-02/04 / 2025-10 | 平台层：铺满整条 SDLC 的可靠性边界 |
| Loop | 定义爆发；黄金法则；"六周热度" | 2026-06 | 治理层：跨运行反馈（≈ Maintain 的关 loop） |
| Graph | Steinberger 引爆；GraphARC admission gate | 2026-07/08 | 治理层：编排 + 门禁 = 审计语言 |
| 风险 | 2026 CVE——authorize at execution, not at generation | 2026-08 | 治理层：授权事故的组织代价 |

## 宽轴锚点（六阶段 SDLC + 工件链，来自 Anthropic playbook）

| 锚点 | 内容 | 作用 |
|---|---|---|
| **代码不再是瓶颈** | build 压到小时级，慢的是 plan/review/test/deploy | 全场主论点（Anthropic 论点，标注来源） |
| 三个后果 | 瓶颈左移右移 / 旧控制失效 / 治理成本上升 | 论证"为什么整条 SDLC 要转型" |
| **工件链 = 审计链** | `intent → spec → plan → diff → PR → incident` | 贯穿主线（谁要的 / 产出了什么 / 谁批的） |
| intent.md | 意图一次捕获，originator 自己的话 + 产品 owner 审批 | Plan 的转变 |
| spec.md + skills | 需求+设计合一，政策在写 spec 时施加 | Design 的转变 |
| plan.md + AGENTS.md + hooks | plan mode / 知识外置 / 确定性 guardrail | Build 的转变（harness 主战场） |
| evals | 对 harness 配置的回归测试 | Test 的转变（治理） |
| managed settings | permissions/sandbox/credentials/marketplaces/min version | Deploy 的治理（受监管企业实例） |
| 关 loop | control-band breach → intent.md 重新入环 | Maintain 的转变（Loop/Graph 组织化） |
| **人守 gate，不逐行** | human judgment at gates；确定性优先 | 治理主线 |
