---
type: analysis
content_type: version_preview
directory: _raw_aws
description: AWS AI-DLC v2 Preview 深度拆解——5阶段32Stage、11 Agent、9范围、68审计事件
research_date: 2026-07-08
verification_status: verified
source_urls:
  - https://github.com/awslabs/aidlc-workflows/tree/v2
  - https://github.com/awslabs/aidlc-workflows/tree/v2/assets
---

# AWS AI-DLC v2 Preview 深度拆解

> v2 是一个**完全重写**——从 Markdown 规则文件进化为原生 harness 实现。5 阶段 32 Stage、11 个领域专家 Agent、9 个自适应范围、68 事件审计追踪。

---

## 从 v1 到 v2：不只是版本号的变化

| 维度 | v1 | v2 |
|------|----|----|
| **本质** | Markdown 规则文件（人类 + AI 共享阅读） | 原生 harness 实现（机器可执行） |
| **架构** | 单层规则文件 | **三层架构**：core/ → harness/ → dist/ |
| **阶段** | 3 阶段（Inception/Construction/Operations） | **5 阶段 32 Stage**（含 Initialization + Operation） |
| **Agent** | IDE 内单 Agent 遵循规则 | **11 个领域专家 Agent** 协作 |
| **深度** | 隐式 | **3 显式深度级别**（Minimal/Standard/Comprehensive） |
| **范围** | 单一 | **9 个自适应范围**（Enterprise → Workshop） |
| **审计** | `audit.md` 手动记录 | **68 事件审计追踪**，自动捕获 |
| **构建** | 无 | bun `scripts/package.ts` 生成 `dist/` |
| **知识** | 规则文件内嵌 | **双层知识体系**（方法论知识 + 用户管理团队知识） |
| **会话** | 基础连续性 | **会话恢复能力** |
| **支持的 harness** | 8 个 IDE/平台 | 4 个（Claude Code, Kiro IDE, Kiro CLI, Codex CLI） |

---

## 三层架构（v2 的核心创新）

```
                    ┌─────────────────────────┐
                    │       core/              │
                    │  Harness-Neutral         │
                    │  方法论源文件             │
                    │                          │
                    │  · tools                 │
                    │  · agents (11 个)         │
                    │  · stage protocol        │
                    │  · conductor             │
                    │  · skills                │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │       harness/           │
                    │  Per-Harness 表面层       │
                    │                          │
                    │  · claude/               │
                    │  · kiro-ide/             │
                    │  · kiro-cli/             │
                    │  · codex/                │
                    └────────────┬────────────┘
                                 │
                         build via:
                    bun scripts/package.ts
                                 │
                    ┌────────────▼────────────┐
                    │       dist/              │
                    │  Generated — Never Edit  │
                    │  用户直接复制使用          │
                    └─────────────────────────┘
```

**设计哲学：**
1. `core/` 是唯一的真理来源——方法论定义在这里，完全与具体 AI 工具解耦
2. `harness/` 是薄适配层——每个 AI 平台（Claude Code、Kiro 等）只需实现表面适配
3. `dist/` 是生成的产物——用户从不手动编辑，保证版本一致性

---

## 5 阶段 32 Stage 全景

```
INITIALIZATION (初始化)
  ├── workspace-detection
  ├── scope-detection          ← 新增：9 个级别自动检测
  ├── depth-selection           ← 新增：3 个深度级别
  └── context-gathering

INCEPTION (构想)
  ├── reverse-engineering       ← 条件执行 (Brownfield)
  ├── requirements-analysis
  ├── user-stories
  ├── workflow-planning
  ├── application-design
  └── units-generation

CONSTRUCTION (构建)
  ├── functional-design
  ├── nfr-requirements
  ├── nfr-design
  ├── infrastructure-design
  ├── code-generation
  ├── build-and-test
  └── review-and-iterate        ← 新增

REVIEW (评审)                   ← 全新阶段
  ├── code-review
  ├── design-review
  ├── security-review
  ├── compliance-review
  ├── quality-gate
  └── approval-gate

OPERATION (运营)                ← v1 只是占位，v2 完整实现
  ├── deployment-planning
  ├── iac-generation
  ├── observability-setup
  ├── rollback-strategy
  ├── production-readiness
  ├── monitoring-config
  └── handoff-documentation
```

**每个 Stage 都有审批门控** — v2 将 HITL 从阶段级别细化到了 Stage 级别。

---

## 11 个领域专家 Agent

v2 将"单一 AI Agent 遵循规则"进化为**多 Agent 协作模型**：

| Agent | 领域 | 职责 |
|-------|------|------|
| **Product** | 产品 | 需求澄清、用户价值判断 |
| **Design** | 设计 | 架构决策、技术选型 |
| **Delivery** | 交付 | Bolt 节奏管理、Unit of Work 拆分 |
| **Architect** | 架构 | 系统设计评审、技术债务识别 |
| **AWS Platform** | 云平台 | AWS 服务选型、成本估算 |
| **Compliance** | 合规 | 合规检查、审计就绪 |
| **DevSecOps** | 安全运维 | 安全最佳实践、CI/CD 流水线 |
| **Developer** | 开发 | 代码生成、重构 |
| **Quality** | 质量 | 测试策略、质量门控 |
| **Pipeline/Deploy** | 部署 | IaC 生成、部署执行 |
| **Operations** | 运营 | 监控、告警、回滚 |

这 11 个 Agent 在 32 个 Stage 中按需激活——不是每个 Stage 都调用所有 Agent。

---

## 9 个自适应范围（Adaptive Scopes）

v2 可以自动检测项目规模并调整工作流深度：

| 级别 | 范围 | 典型场景 |
|------|------|---------|
| 1 | **Enterprise** | 大型企业应用，多团队，严格合规 |
| 2 | **Solution** | 中型解决方案，跨系统集成 |
| 3 | **Application** | 单应用开发 |
| 4 | **Service** | 微服务/后端服务 |
| 5 | **Component** | 组件/库开发 |
| 6 | **Feature** | 单功能开发 |
| 7 | **Prototype** | 原型验证 |
| 8 | **Script** | 脚本/工具 |
| 9 | **Workshop** | 学习/实验 |

**自动检测**在 Initialization 阶段完成，用户可覆盖。范围越往上，执行的 Stage 越多、产出物越详细。

---

## 3 个深度级别

独立于测试策略的显式深度控制：

```
Minimal ─────── Standard ─────── Comprehensive
  │                 │                  │
  快速路径          默认路径           完整路径
  跳过可选 Stage    条件执行           所有 Stage 执行
  最少文档          标准文档           完整文档
  适合原型/Script   适合大多数项目      适合 Enterprise/合规
```

**关键：深度级别独立于测试策略。** 一个 Minimal 深度的项目仍然可以有完整的测试覆盖——深度控制的是**分析和文档**的详尽程度，而非代码质量。

---

## 双层知识体系

### 层 1：方法论知识（随仓库分发）
- 核心工作流规则
- Stage 定义和协议
- Agent 角色定义
- 预装在 `core/` 中，所有项目共享

### 层 2：用户管理的团队知识（项目级别）
- 团队编码规范
- 架构决策记录 (ADR)
- 领域特定术语
- 遗留系统文档
- 存储在项目仓库中，AI Agent 在 Initialization 阶段加载

这个双层设计解决了 v1 的核心痛点：**规则文件无法适应组织特定的上下文。**

---

## 68 事件审计追踪

v2 定义了 68 个标准审计事件类型，覆盖：

- **阶段转换** — Inception → Construction 等
- **Stage 开始/完成**
- **审批操作** — 通过/驳回/有条件通过
- **Agent 活动** — 调用了哪个 Agent，产出了什么
- **工具调用** — MCP 工具调用记录
- **人工输入** — 每次人类决策点
- **异常** — 错误、超时、重试

相比 v1 的"在 `audit.md` 里追加一行"，这是一个质的飞跃。

---

## CLI 工具

v2 提供了 CLI 工具在阶段/Stage 间跳转：

```bash
aidlc jump inception          # 跳到 Inception 阶段
aidlc jump construction       # 跳到 Construction 阶段
aidlc resume                  # 恢复上次会话
aidlc status                  # 查看当前进度
```

这解决了 v1 中"跨会话继续工作"的痛点。

---

## v2 的关键架构决策

### 1. "Core 是真理来源" 而非 "每个 harness 各自实现"

传统做法是每个平台各自写一套规则。v2 选择：
- 在 `core/` 中定义一次方法论
- 用代码生成器输出到每个平台
- 好处：一致性、可维护性、可测试性
- 代价：多了一层构建步骤

### 2. 审批门控在 Stage 级别而非阶段级别

v1 的 HITL 在三阶段之间。v2 在每个 Stage 之后。这意味着：
- 更细粒度的人类控制
- 但也意味着更多中断——需要 CLI 工具来管理节奏

### 3. 双层知识而非单层规则

v1 的规则文件是"一刀切"的。v2 区分：
- **不变的**（方法论本身）
- **可变的**（组织特定上下文）

这是从"框架"到"平台"的进化。

### 4. Agent 专业化而非通用化

11 个领域专家 Agent 替代单一通用 Agent。这呼应了软件工程中"专业化分工"的基本原则——不同角色有不同的上下文和判断标准。但这也引入了多 Agent 协调的复杂性。

---

## 与 v1 的兼容性

v2 仍在 Preview 阶段（v2 分支，228 commits）。v1 继续在 main 分支维护（v1.0.1）。两者目前**独立演进**，尚无迁移工具。

---

## 潜在问题

1. **Stage 级审批门控可能过于细粒度** — 32 Stage × 每个都需审批 = 可能产生大量中断
2. **11 Agent 协调开销** — 多 Agent 系统的 token 消耗和延迟尚未公开数据
3. **构建步骤增加入门门槛** — v1 复制文件即可，v2 需要 `bun install && bun scripts/package.ts`
4. **支持平台缩减** — v1 支持 8 个平台，v2 只有 4 个（Claude Code, Kiro IDE, Kiro CLI, Codex CLI）
5. **Preview 阶段的稳定性风险** — 228 commits 说明仍在快速迭代

---

## 来源

- [awslabs/aidlc-workflows v2 branch](https://github.com/awslabs/aidlc-workflows/tree/v2)
- [AI-DLC Workflows 2.0 Specification PDF](https://github.com/awslabs/aidlc-workflows/tree/v2/assets)
