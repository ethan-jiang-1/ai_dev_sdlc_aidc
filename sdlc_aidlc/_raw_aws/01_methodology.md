# AWS AI-DLC 方法论核心

> AWS 是目前所有云厂商中 AIDLC 方法论最完整的推动者。三阶段模型、自适应执行、Bolt 节奏是它的核心创新。

---

## 三阶段模型

```
INCEPTION（构想）→ CONSTRUCTION（构建）→ OPERATIONS（运营）
      ↓                    ↓                    ↓
   AI 分析需求           AI 生成代码+测试       AI 生成 IaC
   生成User Story        运行构建+修复         生成监控+回滚策略
   人审批准入            人审批准入             人最终审批
```

| 阶段 | 焦点 | 主要产物 |
|------|------|---------|
| **INCEPTION** | "做什么 & 为什么" | 需求文档、架构设计、User Story、Unit of Work 定义、执行计划 |
| **CONSTRUCTION** | "怎么做" | 功能设计、NFR 设计、基础设施设计、代码生成、构建 & 测试 |
| **OPERATIONS** | "部署 & 监控" | 部署自动化、可观测性、生产就绪验证、回滚策略 |

---

## 自适应执行模型

AI-DLC 最大的特征：**工作流适应项目复杂度，而非反之。**

```
                    ┌──────────────────────┐
                    │   用户请求 / Intent    │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │ ① Workspace Detection │  ← 始终执行
                    │  Greenfield / Brownfield│
                    └──────────┬───────────┘
                               │
               ┌───────────────┼───────────────┐
               │ Greenfield    │               │ Brownfield
               ▼               │               ▼
       ┌──────────────┐        │    ┌──────────────────┐
       │ Requirements │        │    │ Reverse          │  ← 条件执行
       │ Analysis     │────────┤    │ Engineering      │
       └──────┬───────┘        │    └────────┬─────────┘
              │                │             │
              └────────────────┼─────────────┘
                               │
                    ┌──────────▼───────────┐
                    │ ② Workflow Planning   │  ← 始终执行
                    │  AI 推荐执行计划       │
                    └──────────┬───────────┘
                               │
    ┌──────────────────────────┼──────────────────────────┐
    │                          │                          │
    ▼                          ▼                          ▼
┌───────────────┐      ┌───────────────┐      ┌───────────────┐
│ Functional    │      │ NFR Design    │      │ Infrastructure│  ← 条件执行
│ Design        │      │ (条件执行)     │      │ Design        │
└───────┬───────┘      └───────┬───────┘      └───────┬───────┘
        │                      │                      │
        └──────────────────────┼──────────────────────┘
                               │
                    ┌──────────▼───────────┐
                    │ ③ Code Generation     │  ← 始终执行
                    │  Plan → Generate      │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │ ④ Build & Test        │  ← 始终执行
                    │  编译 + 测试 + 修复    │
                    └──────────────────────┘
```

**始终执行**的 Stage：Workspace Detection → Workflow Planning → Code Generation → Build & Test
**条件执行**的 Stage：Reverse Engineering（Brownfield）、NFR Design、Infrastructure Design

---

## 关键创新点

### Sprint → Bolt

传统 Agile 的两周 Sprint 被替换为 **Bolt**——数小时到数天的交付周期。AI 可以在 Bolt 内独立完成编码+测试+修复，人类在 Bolt 结束时审查。

### Epic → Unit of Work

Epic 被重构为更细粒度的 **Unit of Work**，每个 Unit 对应一个可独立交付的功能增量。

### 状态管理三元组

```
aidlc-docs/
├── aidlc-state.md       ← 当前阶段/Stage, 项目状态, 活跃上下文
├── audit.md             ← 所有审批操作的审计追踪 (ISO 8601 时间戳)
└── execution-plan.md    ← AI 推荐 + 人类批准的执行计划
```

### Human-in-the-Loop 关隘

每阶段完成后必须等待**人类明确批准**才进入下一阶段。AI 可以推荐，不能自主跨阶段。

### 核心原则

| 原则 | 说明 |
|------|------|
| **方法学 > 工具** | IDE/模型/Agent 无关的设计 |
| **Human-in-the-Loop** | AI 提议，人类批准 |
| **持久化上下文** | 需求、设计决策、测试计划作为产物留存仓库 |
| **自适应严格度** | 复杂度决定 Stage 覆盖深度 |
| **AI-Native 节奏** | Sprint → Bolt, Epic → Unit of Work |

---

## 来源

- [AWS DevOps Blog: AI-Driven Development Life Cycle](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)
- [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows)
