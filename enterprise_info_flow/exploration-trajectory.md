---
title: 探索轨迹 — Enterprise Info Flow 研究
date: 2026-07-08
type: meta
status: living
---

# 探索轨迹

> 这份文件记录了从"不知道往哪挖"到"知道金矿在哪"的全过程。

## 北极星目标

**为 AI 时代的企业信息加工流建立一个清晰的分类体系（taxonomy），并找到它与 SDLC 变革之间的同构关系。**

具体要回答：
1. 传统 BPM 之外，出现了哪些**新品类**？各自叫什么名字？谁定义的？
2. 这些品类之间的**边界和关系**是什么？融合还是替代？
3. 底层范式从"预定义流程"转向了什么？**不同品类用不同的术语在说同一件事吗？**
4. 这一切跟 SDLC 的变革（操作者→委托人、AI Sandwich、Framed Autonomy）**怎么对应**？

探索方法：每轮搜索 → 发现 → 新问题涌现 → 下一轮解决新问题 → 逐步逼近目标。

---

## Round 0：初始假设（搜索前）

**状态**：用户提出假设——软件开发是信息加工流，企业办公也是信息加工流。AI 出现后，原来人做的加工环节 AI 可以做了。想知道外面有没有人研究这个。

**初始问题**：
- 软件有 SDLC 体系化管理信息加工流，办公室里的信息处理有没有等价物？
- 外面有人研究这个吗？在 AI 时代变成正经研究方向了吗？
- 实战和行业上真正落地的东西是什么？

---

## Round 1：广撒网 — "谁在做？"（~4 次并行搜索，2026-07-08）

**状态**：只知道假设，不知道外面有什么。

**搜索方向**：
- `enterprise AI agent automation products 2026 real deployment`
- `enterprise AI workflow automation case study 2026 real results production`
- `ServiceNow Salesforce Microsoft AI agent enterprise workflow comparison 2026`
- `企业 AI Agent 落地 案例 2026 办公自动化`

**关键发现**：
1. 2026 年是"AI 员工全面入职"年——SAP Autonomous Enterprise（200+ agents）、MS Agent 365（160K+ orgs）、ServiceNow AI Control Tower
2. 大量真实案例：Cognizant（200+ agents, 35 万员工）、GE Appliances（800+ agents）、奇瑞（4000+ 智能体）
3. 中文世界：金山 WPS Comate、飞书多维表格智能体、企微"大圆"、来也 Laiye Worker

**这轮的问题**：信息量巨大但都是"产品在做什么"——没有回答"背后的方法论是什么？有没有 SDLC 等价物？"

---

## Round 2：追方法论 — "BPM = SDLC 等价物？"（~6 次搜索）

**状态**：知道了产品层在爆炸，但用户追问方法论。

**搜索方向**：
- `business process management methodology framework information processing flow theory`
- `"office work" "information processing" methodology systematized framework enterprise`
- `Feishu Lark DingTalk enterprise collaboration platform BPM positioning`
- `business process management BPM classic examples scenarios procurement onboarding`

**关键发现**：
1. ✅ **BPM = SDLC 等价物**。从 1980 年代 MIT Office Analysis Methodology 到 2026 年 Contextual Process Digitalization——40 年学术传承。找到了具体论文和框架名称
2. ✅ **飞书/钉钉/企微不是 BPM**。他们是"协同办公平台"——比 BPM 更宽的一层。传统 BPM（泛微/致远）的流程引擎在 AI 时代正在被 CLI 化替代
3. ✅ **经典 BPM 场景**：Procure-to-Pay、Employee Onboarding、Invoice Processing。AI 改变了什么——不需要信息先被结构化
4. 发现三股力量：大厂（旧架构挂 AI）、模型公司（Agent 控制平面）、AI-native 创业（从零重建）

**这轮的 pivot**：从"有什么产品"转到了"方法论叫什么、有哪些玩家、他们之间的关系是什么"。但这些都是名词——还没挖到"东西到底怎么 work 的"。

**仍未回答**：
- 飞书/钉钉这一层，英文世界有没有等价术语？（协同办公 ≠ BPM，但在英文里叫什么？）
- 三股力量做的不同东西，各自有名字吗？
- BPM 学术圈对 AI 有没有系统性的回应？

---

## Round 3：深挖四条矿脉 — "东西到底怎么 work？"（~4 次搜索）

**状态**：知道了玩家和关系，需要聚焦深挖。**四条矿脉是自主选择的，非用户指定。**

| 矿脉 | 为什么选它 | 搜索关键词 |
|------|-----------|-----------|
| Camunda ProcessOS | 唯一老牌 BPM 厂商做的 AI-native 产品 | `Camunda ProcessOS AI agents architecture` |
| Agent 控制平面 | 模型公司对"流程怎么管"的答案 | `Anthropic Claude Cowork enterprise agent architecture` |
| 飞书 CLI 化 | 流程引擎被 CLI 替代的实证 | `飞书 CLI 开源 龙虾 架构 2026` |
| BPM 学术圈 | 有没有人从理论上定义 AI-native BPM？ | `"AI-native BPM" "agentic BPM" survey` |

**关键发现**：
1. **Camunda ProcessOS**：4 个 AI agents（发现→重设计→构建→优化），BPMN = 治理可视化层，Fitness Functions，Organizational Memory。Forrester 把这类东西叫 **Adaptive Process Orchestration (APO)**
2. **Agent 控制平面**：Claude Cowork 缺少企业控制（需要外部控制平面），Rubrik Agent Cloud 在补缺口。Routines 三种触发方式（定时/webhook/GitHub event），权限预提交模式
3. **飞书 CLI 化**：OpenClaw 25 万星（草根爆发），CLI 比 MCP 对 Agent 友好 10-32 倍。2500+ API 变成 AI 可调用的原子指令。钉钉同期走"悟空"统一调度路线
4. **学术圈**：**"Agentic Business Process Management (APM)"** manifesto（Dagstuhl Seminar, 18 位作者）。四大能力：Framed Autonomy、Explainability、Conversational Actionability、Self-Modification。**"Framed Autonomy"是最精确的术语**

**这轮的 pivot**：从"知道有什么"转到了"知道怎么 work"。但——**还没有给这些不同的东西一个统一的分类体系（taxonomy）。**

**仍未回答**：
- Camunda 叫它"Agentic Orchestration"，Forrester 叫它"Adaptive Process Orchestration"，学术圈叫它"Agentic BPM"——这些是一个东西吗？
- 飞书/钉钉在中文世界叫"协同办公"，英文世界有没有对应的成熟品类名？
- 整个企业信息加工流领域，能不能画出一张清晰的分类地图？

---

## Round 4：命名与分类 — "这些东西到底该叫什么？"（~4 次搜索）

**状态**：每个子领域都有术语了，但没有统一分类。用户追问："总得有个叫法吧？"

**搜索方向**：
- Gartner/Forrester 的品类定义
- "agent-native" vs "agentic platform" 的 taxonomy
- Camunda 对自己品类的命名
- 飞书/钉钉的行业分类

**关键发现**：

### 品类名称（终于有了）

| 东西 | 中文叫什么 | 英文叫什么 | 谁定义的 |
|------|-----------|-----------|---------|
| 传统流程管理 | 业务流程管理 (BPM) | Business Process Management | 40 年学术 + 工业共识 |
| 飞书/钉钉/企微 | **协同办公** / 新型协同办公平台 | **Collaborative Work Management (CWM)** | Gartner/Forrester |
| Camunda 的新东西 | — | **Agentic Orchestration** / Adaptive Process Orchestration (APO) | Camunda / Forrester |
| 学术圈的新范式 | — | **Agentic Business Process Management (APM)** | Dagstuhl Seminar (18 位作者) |
| 模型公司做的那层 | — | **Agentic Platform Layer** / Agent Control Plane | Arion Research / VentureBeat |
| 从零重建的创业公司 | — | **Agentic-Native Production Platforms** | xpander.ai / Windsor Drake |

### 三层架构（Arion Research, 2026）

```
Enterprise Platform Layer（CRM, ERP, HCM — 记录系统）
        ↓
Agentic Platform Layer（编排、执行、治理 — 新层）
        ↓
Collaboration Layer（跨 agent 通信）
```

### 四类厂商（Arion Research）

| 类型 | 代表 | 拥有什么 |
|------|------|------|
| **Vertical Integrators** | Oracle, Salesforce, ServiceNow, SAP | 拥有数据 |
| **Horizontal Platforms** | OpenAI, Anthropic | 拥有智能 |
| **Infrastructure/Ecosystem** | Microsoft, Google | 横跨所有层 |
| **Independent/Specialized** | Camunda, xpander.ai | 编排优先，厂商中立 |

### 三级成熟度（xpander.ai）

| 级别 | 代表 | 问题 |
|------|------|------|
| **Retrofitted Automation** | Zapier, n8n, Make | Agent 继承了 trigger-action 的约束 |
| **Build-Only Frameworks** | LangChain, CrewAI | 只管构建，不管部署/监控/治理 |
| **Agentic-Native Platforms** | xpander.ai | 从零为 agent 执行而建 |

---

## Round 6：补齐缺口 — 开源、中小企业、中国市场深度（~3 次搜索）

**状态**：北极星目标基本达成，但 Round 5 留了缺口——开源项目、SMB、中国市场除了 CLI 化还有什么。

**搜索方向**：
- `open source agentic workflow orchestration 2026 self-hosted`
- `SMB mid-market AI workflow automation 2026`
- `钉钉 悟空 Agent OS 架构 开源 原子化`

**关键发现**：

### 开源生态：碎片化但活跃

| 项目 | 定位 |
|------|------|
| **Agyn** | Kubernetes-native agent runtime——把 Claude Code/Codex 从笔记本搬到企业基础设施 |
| **Kiwiq** | 生产级多 agent 编排平台——200+ 企业 agents 验证后开源 |
| **OpenClaw** | 桌面 agent——将安全边界移到推理层而非操作层 |
| **DeerFlow 2.0** | 本地 AI agent 编排器——VentureBeat 深度报道 |
| **Huf** | 自托管多 agent 基础设施——支持 Slack/ERPNext/Discord/Gmail 集成 |

**关键判断**：开源在构建基础设施层——agent runtime、编排、治理。但还没有出现"开源版的 Camunda ProcessOS"。

### 中小企业：不同逻辑

**惊人数据**（Techaisle 2026）：中型市场领先者已经跑到 **144 个 AI agents 对 1 个员工**。小企业 59:1。

**但有一个"流程翻译鸿沟"**：
- 76% 的 SMB 说 GenAI 加速了任务完成
- 只有 **15%** 说改进了业务流程

这不是技术问题——是 SMB 不想优化流程，想让流程**消失**。他们不要更快的审批流，要的是"不需要审批"。

**三条路**（NOC Technology, 2026）：
1. DIY（n8n, OpenClaw）：$445K-$1.13M 五年 TCO——只有 AI 是核心产品才划算
2. SaaS 工具栈（Zapier, Make, HubSpot）：$113K-$453K——标准简单工作流
3. **Managed Intelligence Provider（MIP）**：$79K-$195K——最适合大多数 SMB

### 钉钉悟空：CLI 化的最完整标本

悟空是目前挖到的**最激进、最完整的 CLI 化案例**：

- **Tauri + Rust**，仅 122MB
- **完整 GUI→CLI 重构**：1000+ 原子化指令，覆盖钉钉全场景
- **多 Agent 引擎路由**：Spark（自研）+ Claude Code + Gemini CLI，根据任务特性自动选引擎
- **RealDoc 文件系统**：原子级文件操作、每步快照、秒级回退
- **六层安全**：双层规则 → 统一认证 → 沙箱 → Skill 扫描 → 专属模型 → 网络代理
- **双层熔断**：意图锁（CLI 模式）+ 审批流熔断（钉钉原生）

**关键洞察**：悟空验证了"CLI 化替代流程引擎"的假设——而且做到了比飞书 CLI 更深的程度。不是把审批能力暴露给 Agent 调用，而是**把整个钉钉底层重写为 Agent-native**。

> Source: [钉钉悟空技术解析](https://blog.csdn.net/weixin_44262492/article/details/159266464), CSDN, 2026
> Source: [钉钉、飞书、企微的三条AI路线](https://www.sohu.com/a/1041323154_122578101), 搜狐, 2026
> Source: [阿里悟空发布](https://m.163.com/dy/article/KO7I3JMG0514TTKN.html), 网易, 2026

**搜索方向**：
- `"agentic orchestration" vs "agentic BPM" vs "adaptive process orchestration" terminology`
- `"collaborative work management" vs BPM convergence AI agents`
- `"framed autonomy" enterprise adoption industry`

**关键发现**：

### 三个术语的关系：不同出身，同一个结论

| 术语 | 出身 | 核心主张 |
|------|------|------|
| **Agentic Orchestration** | 厂商/实践者（Nividous, UiPath, AA） | 多 Agent 协调、目标分解、共享记忆 |
| **Agentic BPM (A-BPMS)** | 学术界（Dumas, Calvanese 等） | BPM 的自然进化——5 级自主连续体 |
| **Adaptive Process Orchestration (APO)** | 分析师（Forrester, 2025） | 确定性骨架 + 非确定性 Agent 行为共存 |

**三者的共识**：
> *"确定性编排骨架提供治理、审计和结构。AI Agent 提供适应性、推理和自主。挑战是融合而非选择。"*

UiPath 的 Boris Krumrey：*"混合模式——确定性骨架 + 有边界的 agentic 任务——将主导。"*

### CWM 和 BPM 的融合

CWM（协同办公）和 BPM 不是竞争关系——在 AI 时代它们正在**融合成一个统一的执行层**。

**致远（中国 BPM/CWM 厂商）的三级模型**：
1. **Co-pilot 模式** — AI 辅助人（推荐、分析），人仍是主要行动者
2. **Co-work 模式（Agentic Orchestration）** — AI agent 在**人定义的流程内**执行特定任务。**这是当前企业的主流。**
3. **Autonomous Agent 模式** — 多 Agent 独立分解目标、端到端执行、自纠正。人只是监督者。

**关键判断**：2026 年主流在 Co-work 模式——这跟 SDLC 的"AI Sandwich"（人在两端，AI 在中间）完全对应。

### "Framed Autonomy"的精确含义

**正式定义**（Calvanese 等 18 位作者，2026）：
> *"确保 APM 系统中流程感知和目标对齐的主要机制，通过对 Agent 的知识和目标施加限制来约束其自主性。"*

**框架的两种类型**：
- **Operational frames**：规定具体执行序列
- **Normative frames**：规定允许/禁止的行为（用道义逻辑或声明式语言）

**已经在真实世界验证**：德国能源网公司的 meter-to-cash 流程——Frame Agent 生成流程描述 + Operational Agent 自主执行。预定义规则下 99% 成功执行率。

**企业部署现状**：处于"从研究到实践的桥接阶段"。概念架构和能力已定义，但正式的工程方法论、安全框架和生产级工具仍被列为"仍需建设"。

---

## 北极星目标达成情况

| 目标 | 状态 | 答案 |
|------|------|------|
| 1. 新品类有哪些？各自叫什么？ | ✅ 完成 | CWM（协同办公）、Agentic Orchestration（厂商）、Agentic BPM/A-BPMS（学术）、APO（分析师）、Agentic Platform Layer（模型公司）、Agentic-Native Platforms（创业） |
| 2. 品类之间的边界和关系？ | ✅ 完成 | CWM + BPM 在 AI 时代**融合**而非替代。三级成熟度（Co-pilot → Co-work → Autonomous）。确定性骨架 + Agentic 自主是共识 |
| 3. 底层范式转向了什么？ | ✅ 完成 | **Framed Autonomy**（有框的自主）——框由人定义，框内由 Agent 自主。不同术语在说同一件事 |
| 4. 跟 SDLC 怎么对应？ | ✅ 完成 | SDLC 的"AI Sandwich"/"操作者→委托人" = BPM 的"Co-work 模式" = 学术的"Framed Autonomy"。**完全同构。** 人定义边界和验收标准，AI 在框内自主执行 |

---

## 探索方法论总结（给自己的笔记）

**什么搜索策略有效**：
- 并行搜索 4 个不同方向 → 交叉验证 → 识别模式
- 先广（Round 1-2）→ 再深（Round 3）→ 再合（Round 4 分类）
- 中英文并行搜索——两边信息互补（英文重方法论/架构，中文重产品/案例）

**什么时候该 pivot**：
- 当搜索结果开始重复 → 说明这个方向挖完了
- 当发现新概念反复出现（如"agentic orchestration"） → 新矿脉
- 当用户追问"这叫什么"→ 说明还没挖透，需要分类层

**什么不该做**：
- 不要堆厂商案例（够 5-6 个有数据的就够了）
- 不要搜学术论文逐篇读（找综述和 manifesto，不逐篇）
- 不要在没有明确问题时搜索
