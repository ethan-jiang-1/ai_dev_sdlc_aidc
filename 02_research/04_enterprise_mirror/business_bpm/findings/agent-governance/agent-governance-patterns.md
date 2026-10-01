---
title: Agent 治理模式 — 身份、权限、审计、熔断
date: 2026-07-08
source: web_search (Round 9)
type: deep_dive
status: draft
---

# Agent 治理模式：身份、权限、审计、熔断

> Round 9 深挖。Agent 治理是 2026 年企业 AI 最激烈的战场——传统 IAM 不是为自主 Agent 设计的，整个治理栈正在从零重建。

---

## 一、为什么传统 IAM 对 Agent 失效

| Actor 类型 | 传统模型 | 为什么对 Agent 失效 |
|-----------|---------|-------------------|
| 人类用户 | 窄权限，通过变更请求获取 | N/A |
| 服务账号/bot | 宽静态权限，受代码约束 | Agent 结合了人类式推理 + 机器速度 |
| **AI Agent** | 不属于任何一类 | 通过实时委托链继承权限——每一环都可能放大风险 |

**Orchid Security 的关键数据**：
- 67% 的非人类账号是**本地的**（中心 IAM 看不到）
- 57% 的企业身份是 **"Identity Dark Matter"**（隐藏本地账号、硬编码凭据、过度权限）
- Agent 没有制造这些暴露面——但它们在**加速**这些暴露面的风险

---

## 二、两大参考架构

### A. Five-Plane 参考架构（Tallam, June 2026）

四个运行时治理原语：

| 原语 | 描述 |
|------|------|
| **五平面分解** | 一个推理平面裁决意图 + 四个执行平面：**网络、身份、端点、数据** |
| **Stop-anywhere 调解** | 在 Agent 工作流的任意点中断执行 |
| **复合主体 + 能力衰减** | 权限沿委托链逐级衰减——Agent A 把任务委托给 Agent B 时，B 只有 A 权限的子集 |
| **审计作为结构化证据基底** | 防篡改审计轨迹，可重建完整执行过程 |

**性能**：裁决在个位数微秒内完成。衰减正确性和证据可重建性在每次试验中都成立。

### B. AGL-1：企业 AI 治理层（Walia, July 2026）

厂商中立控制平面参考模型，七个治理域：

1. **Identity-aware retrieval** — 检索时感知 Agent 身份
2. **Policy enforcement** — 策略执行
3. **Provenance management** — 来源管理
4. **Memory governance** — Agent 记忆治理
5. **Knowledge integrity monitoring** — 知识完整性监控
6. **Agentic execution control** — 熔断/杀开关
7. **Trust observability** — 信任可观测性

---

## 三、Agent 身份体系：三大路径

### 路径 1：Agent-as-User（Microsoft Entra Agent ID）

每个 Agent 获得**独立身份**——跟人类员工同样的模型：最小权限 + 即时访问。

- 2026 年 1 月发布
- Agent 365 治理面板中可观测、可管控每个 Agent
- 跟 M365 权限体系深度绑定

### 路径 2：Identity Propagation（Workato VUA）

Agent 不拿自己的身份，而是**传播最终用户的真实身份**。

- **Verified User Authentication (VUA)** — 已获专利
- 源系统（如 Salesforce）看到的是**真实员工**，不是共享服务账号
- Agent 是身份的"载体"，不是身份的"拥有者"

### 路径 3：Intent-Based Access Control（TrustLogix IBAC）

不只是评估**谁**在请求和**能访问什么**——还评估**为什么**这个 Agent 在请求访问。

- 权限被约束到**特定任务、上下文和资源**
- 任务完成后权限自动回收
- 运行时可中断，不依赖静态 RBAC

---

## 四、熔断与杀开关

多种运行时中断能力正在形成共识：

| 厂商 | 机制 | 能力 |
|------|------|------|
| **TrustLogix TrustAI** | 运行时 kill switch | 瞬间切断高风险 Agent 对所有连接数据平台的访问，不影响其他 Agent |
| **Orchid Security** | Agentic Guardrails | 运行时执行最小权限和身份卫生 |
| **Google Cloud** | Agent Gateway + runtime policy | 杀开关条件作为正常 IT 控制嵌入 |
| **Workato** | Tool-level RBAC + field-level security | 作用域权限，可即时撤销 |

**六种中断原语**（Tallam 论文）：不只是允许/拒绝的二元决策——正在向**分级响应**演进（警告→限制作用域→暂停→撤销→隔离）。

---

## 五、审计追踪标准

正在形成的标准：**机器可读遥测，在动作发生时创建，而非事后人工重建。**

必需的审计元素：
1. 指令/prompt
2. 被 grounded 的数据来源
3. 发起的工具调用
4. **Agent 身份**（含完整委托链）
5. 生成的输出
6. 审批决策（human-in-the-loop 检查点）
7. 防篡改日志完整性

被引用的合规框架：SOC 2、GDPR、HIPAA、NIST AI RMF、ISO 42001、EU AI Act。

---

## 六、Control Plane vs Execution Plane

2026 年最关键的一个架构区分：

| 平面 | 功能 | 孤立时的局限 |
|------|------|------------|
| **Control Plane** | 治理——身份、权限、审计、合规 | 管了 Agent **可以**做什么，但不管**怎么做**（脆弱的、一次性的 API 即兴调用） |
| **Execution Plane** | Agent 实际执行操作 | 执行高效但无身份验证、无作用域权限、无审计轨迹 |

**统一控制与执行平面**（Workato 的术语）：架构坐在 **Agent 和企业系统之间**——而非用户和模型之间。实现跨 Agent 框架（LangChain, AutoGen, Copilot Studio, Agentforce）的模型中立治理。

---

## 七、企业运营模型（Google I/O 2026）

平台功能不足以替代内部运营模型。每个企业必须回答六个问题：

1. 哪些 Agent 已经在使用或试点？
2. 每个 Agent 可以访问哪些工具、应用和数据源？
3. 哪些动作可以不经人类审批？
4. 审批记录存在哪？
5. **谁可以暂停、撤销或禁用 Agent？**（杀开关权限）
6. 如果 Agent 导致安全、合规或客户影响事件，有什么证据？

**必需的实操控制**：Agent 清单（命名所有者、用途、连接系统、允许动作、审批点）、权限地图（RBAC 应用于 Agent 动作）、动作阈值（哪些动作需要人类审批）、证据日志。

---

## 八、对 SDLC 治理的映射

| 企业 Agent 治理 | SDLC 等价 | 状态 |
|----------------|----------|------|
| Agent 身份（Entra Agent ID） | CI/CD service account / bot identity | SDLC 侧服务账号已成熟，但 Agent 身份还在早期 |
| 权限预提交（Agent 计划→人 approve） | PR approval / code review | **SDLC 侧已成熟**——企业侧正在追赶 |
| 熔断/杀开关 | Pipeline abort / rollback | **SDLC 侧已成熟** |
| 审计追踪 | CI/CD audit log / git history | **SDLC 侧更成熟**（git 是不可篡改的理想审计基底） |
| 复合主体 + 能力衰减 | CODEOWNERS + protected branches | SDLC 侧有等价物但缺少委托链衰减的形式化 |
| Intent-Based Access | — | **SDLC 侧缺少等价物**——CI 不评估"为什么这个 Agent 在改这个文件" |

**关键洞察**：SDLC 治理在某些维度（审计追踪、审批流程、熔断）**比企业侧成熟**——因为 git + CI/CD 已经提供了不可篡改的证据链和清晰的审批门。但在 Agent 身份和意图评估上，**企业侧在快速领先**。
