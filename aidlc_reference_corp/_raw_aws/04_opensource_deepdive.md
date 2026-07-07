---
type: analysis
content_type: opensource_deepdive
directory: _raw_aws
description: AWS AI-DLC 三个开源仓库的深度分析——从 Markdown 规则到全栈协作平台
research_date: 2026-07-08
verification_status: verified
source_urls:
  - https://github.com/awslabs/aidlc-workflows
  - https://github.com/aws-samples/sample-ai-driven-development-lifecycle-platform
  - https://github.com/aws-samples/sample-collaborative-ai-dlc
  - https://catalog.us-east-1.prod.workshops.aws/workshops/99049ad5-14fa-4810-85ec-ac23173c9082/en-US
---

# AWS AI-DLC 开源实现深度分析

> 三个互补的 GitHub 仓库构成了 AWS AI-DLC 的开源生态。从 Markdown 规则文件到全栈协作平台，逐层递进。

---

## 全景对比

| 维度 | aidlc-workflows v1 | aidlc-workflows v2 (preview) | Bedrock AgentCore Platform | Collaborative AI-DLC |
|------|-------------------|------------------------------|---------------------------|----------------------|
| **本质** | Markdown 规则文件集 | 原生 harness 实现 | 参考平台实现 | 全栈多用户协作平台 |
| **Stars** | 3.3k | 同仓库 v2 分支 | 16 | 33 |
| **Commits** | 201 | 228 (v2 分支) | 2 | **227** (最活跃) |
| **语言** | Python 85% + Shell | TypeScript (bun) | Python 60% + TS 37% | JS 45% + TS 41% + HCL 13% |
| **部署方式** | 复制文件到项目 | 从 dist/ 复制 | CDK deploy (15-20min) | Terraform deploy |
| **用户模型** | 单开发者 | 单开发者 | 单用户 + Web 门户 | **多用户 + 认证 + RBAC** |
| **数据存储** | 文件系统 (Markdown) | 文件系统 | S3 | **Neptune (图) + DynamoDB + S3** |
| **Agent 运行时** | IDE AI Agent | AI Agent (Bedrock) | Bedrock AgentCore + Strands SDK | **ECS Fargate + 可插拔 CLI** |
| **协作** | 无 | 无 | 基于 Git | **实时 Yjs/CRDT** |
| **可追溯性** | `aidlc-docs/` 产物 | 68 事件审计追踪 | S3 产物 | **图数据库链路追踪** |
| **成熟度** | GA (v1.0.1) | Preview | Sample | Sample |
| **许可** | MIT-0 | MIT-0 | MIT-0 | MIT-0 |

---

## 仓库一：awslabs/aidlc-workflows（核心规则引擎）

**地址：** https://github.com/awslabs/aidlc-workflows
**最新 Release：** v1.0.1 (2026-06-30) | **11 个 Release** (v0.1.0 2026-01-22 起)

### 目录结构

```
aidlc-workflows/
├── aidlc-rules/
│   ├── aws-aidlc-rules/
│   │   └── core-workflow.md          ← 核心工作流定义（唯一文件）
│   ├── aws-aidlc-rule-details/
│   │   ├── common/                   (11 文件)
│   │   ├── inception/                (7 文件)
│   │   ├── construction/             (6 文件)
│   │   ├── operations/               (1 文件)
│   │   └── extensions/
│   │       ├── security/baseline/    (2 文件: rule + opt-in)
│   │       ├── testing/property-based/ (2 文件)
│   │       └── resiliency/baseline/  (2 文件)
├── docs/                             (管理指南、开发者指南、使用指南)
├── scripts/
│   ├── aidlc-codereview/             ← v1.0.1 新增
│   ├── aidlc-designreview/           ← 3 个专业 Agent 评审
│   ├── aidlc-evaluator/              ← Golden test + AI 语义评估
│   └── aidlc-traceability/           ← v1.0.0 新增
└── AGENTS.md
```

### 规则详情文件完整清单

**common/ (11 个)** — 跨阶段通用规则：
- `process-overview.md` — 流程总览
- `depth-levels.md` — 深度级别定义
- `session-continuity.md` — 会话连续性
- `content-validation.md` — 内容校验
- `error-handling.md` — 错误处理
- `overconfidence-prevention.md` — **防止 AI 过度自信**
- `question-format-guide.md` — 提问格式规范
- `terminology.md` — 术语定义
- `welcome-message.md` — 欢迎信息
- `workflow-changes.md` — 工作流变更管理
- `ascii-diagram-standards.md` — ASCII 图表标准

**inception/ (7 个)** — 构想阶段：
- `workspace-detection.md` — 工作区检测 (Greenfield/Brownfield)
- `reverse-engineering.md` — 逆向工程（Brownfield 条件执行）
- `requirements-analysis.md` — 需求分析
- `user-stories.md` — 用户故事生成
- `workflow-planning.md` — 工作流规划
- `application-design.md` — 应用设计
- `units-generation.md` — Unit of Work 拆分

**construction/ (6 个)** — 构建阶段：
- `functional-design.md` — 功能设计
- `nfr-requirements.md` — NFR 需求
- `nfr-design.md` — NFR 设计
- `infrastructure-design.md` — 基础设施设计
- `code-generation.md` — 代码生成
- `build-and-test.md` — 构建与测试

**operations/ (1 个)** — 运营阶段（占位，待扩展）

**extensions/ (3 类 × 2 文件)** — 可插拔扩展：
- `security/baseline/` — 安全基线
- `testing/property-based/` — 基于属性的测试
- `resiliency/baseline/` — 韧性基线

每类扩展包含一个 `规则文件` + 一个 `opt-in.md` 启用文件。

### 核心工作流关键规则

1. **Checkbox 追踪**：每个 Stage 完成后打勾
2. **ISO 8601 审计时间戳**：所有审批操作记录精确时间
3. **仅追加 `audit.md`**：不可修改已完成记录
4. **标准化 2 选项完成消息**：构建阶段结束后必须给两个明确的下一步选项
5. **代码布局约束**：所有应用代码在 workspace 根目录，文档只在 `aidlc-docs/`

### 支持的平台

Kiro IDE/CLI、Amazon Q Developer IDE Plugin、Cursor IDE、Cline、**Claude Code**、GitHub Copilot、OpenAI Codex、及其他 "Other Agents"。

### 辅助工具链

| 工具 | 功能 |
|------|------|
| **AIDLC Evaluator** | Golden 测试用例、AI 语义评估、代码评估（lint/安全/重复）、NFR 评估（token 用量、执行时间、跨模型一致性）、CI/CD 集成 |
| **AIDLC Design Reviewer** | 三个专用 AI Agent（Critique/Alternatives/Gap Analysis）基于 Claude + Bedrock，加权严重度质量评分 |
| **AIDLC Code Reviewer** | v1.0.1 新增，自动化代码评审 |
| **AIDLC Traceability** | v1.0.0 新增，需求到代码的可追溯性验证 |

### 产物结构

**Inception 阶段产出：**
```
aidlc-docs/
├── plans/
│   └── execution-plan.md
├── reverse-engineering/          ← Brownfield only
│   ├── business-overview.md
│   ├── architecture.md
│   ├── code-structure.md
│   ├── api-documentation.md
│   ├── component-inventory.md
│   ├── technology-stack.md
│   ├── dependencies.md
│   └── code-quality-assessment.md
├── requirements/
│   ├── requirements.md
│   └── requirement-verification-questions.md
├── user-stories/                 ← 条件执行
│   ├── stories.md
│   └── personas.md
└── application-design/           ← 条件执行
    ├── application-design.md
    ├── components.md
    ├── component-methods.md
    ├── services.md
    ├── component-dependency.md
    ├── unit-of-work.md
    ├── unit-of-work-dependency.md
    └── unit-of-work-story-map.md
```

**Construction 阶段产出：**
```
aidlc-docs/
├── plans/                        ← 每 Unit 独立计划
├── {unit-name}/
│   ├── functional-design/
│   ├── nfr-requirements/
│   ├── nfr-design/
│   ├── infrastructure-design/
│   └── code/
├── shared-infrastructure.md      ← 跨 Unit 共享
└── build-and-test/
    ├── build-instructions.md
    ├── test-instructions.md      ← 单元/集成/性能/契约/安全/E2E
    └── summary.md
```

---

## 仓库二：aws-samples/sample-ai-driven-development-lifecycle-platform（AgentCore 参考平台）

**地址：** https://github.com/aws-samples/sample-ai-driven-development-lifecycle-platform

### 10 大核心组件

```
┌─────────────────────────────────────────────────────┐
│  ① React Frontend                                    │
│  Vite + React + TypeScript SPA                       │
│  CloudFront + S3 + Cognito PKCE                      │
│  双 WebSocket：Agent 进度 + Yjs 协作                   │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│  ② AgentCore Runtime (Python ARM64, ECR)             │
│  main_ws.py → 加载 SharedState → 构建 Strands Graph  │
│  → stream_async → HITL via asyncio.Queue             │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│  ③ Orchestrator (orchestrator.py)                    │
│  14-Node Strands GraphBuilder Graph                  │
│  Inception: workspace_detection → ... → units_gen    │
│  Construction: functional_design → ... → build_test  │
│  条件执行的 Atlassian 集成 Agent                       │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│  ④ AgentCore Gateway (MCP + Cognito Auth)            │
│  Lambda 目标: file-operations + atlassian             │
└────────────────────────┬────────────────────────────┘
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ ⑤ Memory      │ │ ⑥ File Ops   │ │ ⑦ Atlassian  │
│ Summarization │ │ Lambda       │ │ MCP Proxy    │
│ + Semantic    │ │ S3 CRUD      │ │ Lambda       │
│ Session Mgr   │ │ Presigned URL │ │ Jira+Conf.   │
└──────────────┘ └──────────────┘ └──────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│  ⑧ Integration Config API (Lambda + API Gateway)     │
│  ⑨ Cognito User Pool (Groups → SDLC 角色)            │
│  ⑩ Project S3 Bucket (产物 + 状态 + 审计)             │
└─────────────────────────────────────────────────────┘
```

### 关键技术决策

1. **AgentCore Runtime 为什么是容器而非 Lambda？** — Agent 执行时间长（分钟级），需要持续运行的 Python 进程来维护 Strands Graph 状态和 WebSocket 连接。

2. **HITL 实现** — `asyncio.Queue` + `StreamAdapter`。Agent 执行到审批点时入队等待，前端通过 WebSocket 收到 `approval_required` 事件，用户在 UI 上批准后出队继续执行。

3. **Atlassian MCP Proxy 为何自建？** — `mcp.atlassian.com` 被 Cloudflare 拦截 Lambda IP，所以自建代理绕过。

4. **Memory 策略** — 摘要 + 语义双层策略。Session Manager 在运行时注入短期和长期记忆。

### 部署

```bash
yarn deploy-infrastructure   # CDK 部署基础设施
# CodeBuild 构建容器 (~10-15min)
# 全栈部署 ~15-20min
```

配套 Workshop：https://catalog.us-east-1.prod.workshops.aws/workshops/99049ad5-14fa-4810-85ec-ac23173c9082/en-US

---

## 仓库三：aws-samples/sample-collaborative-ai-dlc（协作平台）

**地址：** https://github.com/aws-samples/sample-collaborative-ai-dlc
**最活跃的仓库**（227 commits）

### 核心差异化：实时协作 + 图追溯

这是三个仓库中最成熟的——不仅是参考实现，而是一个**可直接部署的多用户 AI 协作开发平台**。

### 请求路径（同步，面向用户）

```
Browser (React 19 SPA)
  │
  ├── /api/* ──→ CloudFront ──→ REST API Gateway ──→ 30 个 Lambda
  ├── /ws ────→ CloudFront ──→ WS API Gateway ──→ Lambda + DynamoDB
  └── /yjs/* ─→ CloudFront ──→ VPC Origin ──→ ALB ──→ Yjs Server (ECS)
```

**Cognito 认证**：
- 管理员邀请制注册
- 可选 TOTP MFA
- 三组 RBAC：`member`、`approver`、`owner`
- REST API：Cognito 内置 authorizer
- WebSocket API：自定义 Lambda authorizer
- Yjs Server：进程内 JWT 验证

**30 个 Lambda** — 按图数据库实体一对一映射：projects、sprints、requirements、user-stories、tasks、code-files、reviews、questions、discussions、timeline-events、trackers、github、gitlab、agents、artifacts…

### Agent 运行时（异步路径）

```
用户发起 Agent 运行
  │
  ▼
POST /projects/{id}/agents (agents Lambda)
  │
  ├── 冷启动: ECS RunTask → Fargate Task
  └── 热路径: DynamoDB agent-pool 条件写入 → 复用空闲 Worker
        │
        ▼
ECS Fargate Task (Agent 容器)
  ├── 可插拔 CLI: Kiro CLI / Claude Agent ACP / OpenCode
  ├── MCP Graph Server (Neptune 图操作工具)
  ├── AI-DLC 规则文件 (/opt/aidlc-rules/)
  └── ask_question 工具 → submit-question Lambda
        │
        ▼
EventBridge (agent.*, artifact.*, sprint.phaseChanged)
  └── notify Lambda → WebSocket → 浏览器实时推送
```

**Pool 模型精髓**："DynamoDB 行是邮箱，不是事件源。" 
- 每个 Fargate Task 循环轮询自己的 pool 行
- 热路径通过单次 DynamoDB 条件写入完成分发
- 避免冷启动延迟的同时保持资源效率

**为什么 Agent 跑在 ECS 而非 Lambda？**
1. 执行时间长（分钟级）
2. 交互式——Agent 需要暂停等待人类回答问题
3. 需要工作文件系统

### Yjs 协作服务器（关键设计决策）

**为什么是 ECS Fargate 而非 Lambda？**
> "A CRDT relay needs persistent in-memory state shared across all clients editing the same document" 
> — 这与 Lambda 的无状态模型根本冲突。

- 长运行 Node.js 容器
- WebSocket upgrade 时：先验证 Cognito JWT，再验证短期 HMAC `scope token`（绑定到 Cognito 身份 + sprint/project 范围）
- CRDT 同步（type 0）+ 感知广播（type 1）
- **仅内存状态** — 零 S3/DynamoDB 写入
- Token 过期 → 强制关闭 socket（close code 4401）
- 最后一个客户端断开 60 秒后销毁文档
- **单文档单进程** — 不能水平扩展但保证了 CRDT 一致性

### 数据存储三层架构

| 层 | 存储 | 内容 |
|----|------|------|
| **结构化图** | Neptune (Gremlin) | Requirement → UserStory → Task → CodeFile → Review → AgentRun → Discussion |
| **操作状态** | DynamoDB | WebSocket 连接、Agent 问题/输出、Worker Pool、Session、通知、Yjs 元数据、OAuth 连接 |
| **大对象** | S3 | SPA bundle、产物 body、代码快照、访问日志 |

### 外部集成

- **GitHub OAuth App** — 仓库访问 + PR 创建
- **GitLab OAuth** 
- **Jira Cloud OAuth 2.0** — 只读
- **Secrets Manager** — 平台级应用凭证
- **SSM Parameter Store** — 每用户 token + Agent CLI 认证材料

---

## 三仓库关系图

```
awslabs/aidlc-workflows (规则引擎)
  │  定义方法论——三阶段、自适应、HITL
  │
  ├──→ aws-samples/sample-ai-driven-development-lifecycle-platform
  │      Bedrock AgentCore 参考实现
  │      证明"AgentCore + Strands 可以跑这套规则"
  │
  └──→ aws-samples/sample-collaborative-ai-dlc
         全栈多用户协作平台
         证明"AI-DLC 可以规模化到团队级别"
```

三者构成了一条清晰的成熟度曲线：
1. **aidlc-workflows** — "方法论是什么"
2. **AgentCore Platform** — "单用户怎么跑"
3. **Collaborative AI-DLC** — "团队怎么协作"

---

## 关键设计模式

### 1. 声明式规则而非命令式脚本
aidlc-workflows 选择 Markdown 规则文件而非可执行脚本。这意味着：
- **平台无关** — 任何遵循规则的 AI Agent 都可以执行
- **人类可读** — 评审者可以直接阅读工作流规则
- **版本可控** — Git diff 清晰显示规则变更

### 2. 动态工作流而非静态 Pipeline
```python
# 不是
pipeline = [stage1, stage2, stage3]

# 而是
if is_greenfield:
    skip reverse_engineering
if complexity < threshold:
    skip nfr_design
if has_compliance_requirements:
    add security_baseline_extension
```

### 3. 邮箱模式而非事件驱动
Agent Pool 用 DynamoDB 条件写入做分发，而非 EventBridge 触发。
优点：Worker 主动拉取，避免了冷启动 + 事件丢失 + 并发控制的所有问题。

### 4. CRDT 协作而非 OT
选择 Yjs（CRDT）而非 Operational Transformation，因为：
- 不需要中央服务器做冲突解决
- 离线编辑自然支持
- 但 AWS 仍用了单进程来保证一致性（务实的选择）

---

## 来源

- [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows)
- [aws-samples/sample-ai-driven-development-lifecycle-platform](https://github.com/aws-samples/sample-ai-driven-development-lifecycle-platform)
- [aws-samples/sample-collaborative-ai-dlc](https://github.com/aws-samples/sample-collaborative-ai-dlc)
