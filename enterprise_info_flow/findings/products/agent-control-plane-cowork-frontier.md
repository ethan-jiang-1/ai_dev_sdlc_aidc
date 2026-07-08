---
title: Agent 控制平面 — Anthropic Cowork 与 OpenAI Frontier
date: 2026-07-08
source: web_search (deep)
type: deep_dive
status: draft
---

# Agent 控制平面 — Anthropic Cowork 与 OpenAI Frontier

> 模型公司不直接做 BPM。他们在做更底层的东西——agent 的权限、记忆、工具调用、审计。如果传统 BPM 的流程引擎不再是唯一执行入口，那这个"控制平面"就是替代品。

---

## Claude Cowork 架构

Claude Cowork 跟 Claude Code 共享同一个 agent loop——Claude Opus 做 lead agent（高层规划），Claude Sonnet 做 sub-agent（并行子任务执行）。但 Cowork 的 blast radius 更大：

| 能接触的 | Claude Code | Claude Cowork |
|------|------|------|
| 本地文件 | 授权目录 | 授权目录 |
| 浏览器 | — | ✅ Claude in Chrome |
| 桌面控制 | — | ✅ 点击、输入、截图 |
| 插件 | MCP | ✅ 插件市场 |
| 定时任务 | — | ✅ Scheduled Tasks |
| 代码执行 | ✅ bubblewrap/seatbelt | ✅ VM 隔离 |

> Source: [Claude Cowork vs Claude Code: Enterprise Security Comparison](https://generalanalysis.com/guides/claude-cowork-vs-claude-code), General Analysis, 2026

---

## 企业控制平面的缺口

Anthropic 自己的文档承认 Cowork 在企业控制方面不如 Claude Code：

| 能力 | Claude Code (Enterprise) | Claude Cowork |
|------|------|------|
| 沙箱 | OS 级（bubblewrap/seatbelt） | VM 隔离代码，但**电脑操作路径无沙箱** |
| MCP/插件策略 | `managed-mcp.json` 精确控制 | 插件市场策展——更宽、更不精确 |
| 审计日志 | 完整审计日志 + Compliance API | OpenTelemetry 流——**明确说"不替代审计日志"** |
| 合规工作负载 | HIPAA BAA, DPA, SCIM, SSO | **明确排除** |

**结论**：Cowork 要安全部署在企业，**必须**在外面包一层控制平面——on-device proxy / LLM gateway / policy engine。而这个控制平面，Anthropic 自己没有完全提供。

> Source: [How to Secure Claude Cowork: Enterprise Deployment Guide](https://generalanalysis.com/guides/how-to-secure-claude-cowork), General Analysis, 2026

---

## 2026 年的 Agent 全栈

Anthropic 在 2026 年拼出了完整的 agent 栈：

```
Skills → Sub-Agents → Agent SDK / Managed Agents → Triggers
```

**三种触发方式**（Claude Code Routines）：
1. **Scheduled** — 时钟触发
2. **API webhook** — 外部系统通过 HTTP POST 触发
3. **GitHub event** — PR/release 事件触发

Routines 跑在 Anthropic 管理的云基础设施上——关了笔记本也能继续。权限在创建时预提交（repo、环境、连接器），运行时无权限弹窗。

---

## 第三方控制平面：市场在补缺口

### Rubrik Agent Cloud (Jun 2026)

专门为 Claude Code 和 Cowork 建的弹性和治理层：
- **SAGE**（Semantic AI Governance Engine）——实时意图驱动治理
- **Agent Inventory**——360° agent 风险/权限/策略违规可见性
- **Agent Rewind**——意外 agent 操作的即时回滚
- **Codebase Resilience**——GitHub/Azure DevOps repo 的不可变快照

> Source: [Rubrik Launches Agent Cloud for Anthropic Claude Code & Claude Cowork](https://www.thefastmode.com/technology-solutions/48976-rubrik-launches-agent-cloud-for-anthropic-claude-code-claude-cowork-to-secure-ai-agents), The Fast Mode, Jun 2026
> Source: [Rubrik Agent Cloud BusinessWire](https://www.businesswire.com/news/home/20260609431521/en/Rubrik-Launches-Rubrik-Agent-Cloud-for-Anthropics-Claude-Code), BusinessWire, Jun 2026

### AI Gateway 模式（API7）

集中式 API 流量管理——token 预算、prompt injection 模式阻断、provider failover、完整审计追踪。被定位为企业部署桌面 AI agent 的基础设施。

---

## 跟传统 BPM 流程引擎的本质差异

| | 传统 BPM 流程引擎 | Agent 控制平面 |
|------|------|------|
| 流程怎么定义 | 预设 BPMN 图 | Agent 按需调用能力 + 人在关键节点策展 |
| 执行入口 | 流程引擎 | Agent runtime + 触发机制 |
| 治理方式 | 审批节点 + 合规审计 | 权限边界 + 意图检测 + 行为回滚 |
| 优化方式 | 周期性流程回顾 | 持续监控 + drift detection |

---

## 对"信息加工流"研究的启示

模型公司不直接做 BPM——他们在做 BPM 下面的那层。但这一层的架构决策会影响上面的一切：
- 如果 agent 的权限模型是"预提交"式的（Routines），那流程就不是"走审批流"而是"在预授权边界内自主"
- 如果 agent 的治理是"检测+回滚"式的（Rubrik Agent Rewind），那流程设计就从"防止出错"变成"快速发现和恢复"
- **这跟 SDLC 的 "约束编码进 CI 而不是 prompt" 是同构的**——治理从预防式变成了检测式
