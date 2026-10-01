---
title: AI-Native 创业公司 + 模型公司 — 对传统 BPM 的冲击
date: 2026-07-08
source: web_search
type: analysis
status: draft
---

# AI-Native 创业公司 + 模型公司 — 对传统 BPM 的冲击

> 核心判断：2026 年，BPM 市场正在经历从"桌面到互联网"以来最大的架构重置。不是在老架构上挂 AI——是从数据模型和流程范式层面重建。

---

## 三股力量

### 1. 大厂（Microsoft/Salesforce/ServiceNow）— 在旧架构上挂 AI

- 优势：生态锁定。如果你已经在 M365/Dynamics/Salesforce/ServiceNow 上，他们给你 AI
- 弱点：底层数据模型是 20 年前的。AI 被接入一个不是为它设计的架构

> "You cannot bolt AI-native onto a 20-year-old data model and get the same result as building from scratch."

> Source: [What It Means to Be an AI-Native B2B Company](https://www.forumvc.com/thought-pieces/what-an-ai-native-b2b-company-actually-means), Forum VC, 2026

### 2. 模型公司（OpenAI/Anthropic）— 争夺 Agent 控制平面

模型本身已经不是差异化因素。真正的战场是 **agent orchestration layer**——谁控制工作流的规划、工具调用、数据访问和治理。

- **Anthropic**：Claude Cowork + Managed Agents。走 no-code、角色专用插件路线（Legal, Sales, Finance, Biology Research）。强调 MCP 开放协议和 Constitutional AI 安全
- **OpenAI**：Frontier Enterprise Platform。走通用平台路线。AI "co-workers" 有独立身份、权限、记忆

关键数字：
- Anthropic 占企业 LLM API 支出的 ~40%（2023 年仅 12%）
- OpenAI 从 ~50% 降到 ~27%
- Microsoft 在 agent 编排层占 38.6%，Anthropic 首次出现（5.7%）

**但模型公司不直接做 BPM。** 他们做的是基础能力层——Agent 的执行和治理。BPM 那层留给合作伙伴和客户自己建。

> Source: [Claude's next enterprise battle is not models: it's the agent control plane](https://venturebeat.com/orchestration/claudes-next-enterprise-battle-is-not-models-its-the-agent-control-plane), VentureBeat, 2026
> Source: [Enterprise Agentic AI Landscape 2026](https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/), Kai Waehner, Apr 2026
> Source: [Why Anthropic and OpenAI are doubling down on enterprise AI](https://indianexpress.com/article/explained/explained-sci-tech/why-anthropic-and-openai-are-doubling-down-on-enterprise-ai-and-how-this-will-hit-indian-it-10685298/), Indian Express, 2026

### 3. AI-Native 创业公司 — 从零重建

这才是最值得关注的。几家公司代表了这个方向：

#### Camunda ProcessOS — 最接近"AI-Native BPM"
- 4 个专门 AI agents：流程发现 → 重设计 → 构建/部署 → 持续改进
- 宣称客户 onboarding 流程可以从**数月 → 数天**（不是自动化旧步骤，是结构性重新设计）
- 发现阶段从数月 → 1-2 周
- 解决传统 BPM 的 "shelfware" 问题——流程地图建完就过时

> Source: [ProcessOS: The Operating System for Your Processes](https://camunda.com/platform/process-os/), Camunda, 2026

#### Neo — AI-Native 办公套件（挑战 Microsoft/Google）
- 创始人 Bhavin Turakhia 自投 $30M
- 模型无关（model-agnostic）
- AI 是主动参与者，不是助手——"If you want to build an iPhone, you cannot take Nokia parts"
- 包含文档、项目管理、文件存储

> Source: [Bhavin Turakhia's $30M AI-native workplace platform to challenge Microsoft, Google](https://www.livemint.com/companies/bhavin-turakhia-neo-ai-native-workplace-artificial-intelligence-enterprise-software-workplace-productivity-11782961115580.html), Livemint, 2026

#### Reevo — AI-Native Revenue OS
- $80M 融资（Khosla/Kleiner Perkins），$500M 估值
- 一个平台替代 7+ 工具（CRM + 拨号器 + 序列 + 预测）
- 发布以来需求 4 倍增长

#### Aurasell — AI-Native GTM OS
- 不替换 CRM——**坐在 CRM 上面**
- $30M 种子轮
- 数小时部署

---

## 估值分化：AI-Native vs Legacy

Windsor Drake Q2 2026 数据：

| 类型 | EV/Revenue |
|------|------|
| AI-native agentic 平台 | 14x-22x（公开），20x-30x（私募） |
| 传统独立 RPA | 2.5x-5x（UiPath ~2.3x） |
| 中位数 | ~9x |

大厂在通过**收购**而非自建来应对：ServiceNow $2.85B 买 Moveworks，Salesforce $8B 买 Informatica——都付了 25-30% 战略溢价。

> Source: [AI Workflow Automation Valuations: Q2 2026](https://windsordrake.com/market-intelligence/reports/ai-workflow-automation-valuations-q2-2026/), Windsor Drake, 2026

---

## 传统 RPA 厂商的转型：UiPath 和 Automation Anywhere（Q8 答案）

> 2026 年，传统 RPA 厂商正在经历从"规则驱动的 bot"到"自主 agent"的转型。两家的方法论白皮书揭示了与 SDLC 工具链转型平行的路径。

### UiPath：从 RPA 到 Agentic Automation

UiPath 有正式的方法论白皮书：**"The Definitive Guide to Agentic Automation"**。

**三阶段演化路径**：
| 阶段 | 描述 |
|------|------|
| Traditional RPA | 静态 bot 执行固定规则任务（仅结构化数据） |
| AI-Powered Automation | RPA + ML/NLP/OCR——处理半结构化任务 |
| Agentic Automation | AI agent 自主规划、决策、适应、执行——基于 LLM/LAM 和多模型集成 |

**2026 平台组件**：
- **UiPath Maestro**：Agentic 编排层（BPMN 2.0 + DMN）——"指挥中心"
- **Agent Builder**：低代码 AI agent 创建
- **Autopilot**：自然语言→工作流生成
- **Healing Agent**：运行时自修复（UI 选择器断裂时自动恢复，减少 60-70% 维护成本）
- **AI Trust Layer**：治理、安全、可审计性

**Boris Krumrey（UiPath Global VP）的 2026 技能模型**：agentic 设计基础（目标、约束、grounding/RAG、护栏）→ 编排优先思维（异常路径、HITL 审批、可审计性）→ 多 agent 和自适应案例模式 → BPMN 作为执行骨架，演进到 "Agentic Task" 概念。

> Source: [The Definitive Guide to Agentic Automation](https://www.uipath.com/resources/automation-whitepapers/definitive-guide-to-agentic-automation), UiPath
> Source: [Transforming your Business with Agentic AI](https://www.uipath.com/resources/automation-whitepapers/transforming-your-business-with-agentic-ai), UiPath

### Automation Anywhere：从 RPA 到 Agentic Process Automation (APA)

Automation Anywhere 与 **EY 联合发布了白皮书 "From Robotic to Agentic: Reimagining Process Automation"**，Stanford GSB 也将其作为 2026 年案例研究（Case No. SM411）。

**三大支柱**（Imagine 2026）：
| 支柱 | 功能 |
|------|------|
| Universal Orchestration（Mozart Orchestrator） | 协调人、AI agent、bot、API——跨云、本地、气隙系统 |
| Contextual Intelligence（Process Reasoning Engine + Context Intelligence Graph） | 将企业政策、系统和执行历史结构化为可操作地图——声称准确性提升 30%+ |
| Centralized Governance | 完整审计追踪、PII 遮蔽、AI Evaluations、Process Simulation（预生产测试） |

**Stanford 案例研究数据**：AI 预订量 YoY 增长 45%，占业务 70%+。早期 APA 采用者：Petrobras 三周节省 $120M，Boston Children's Hospital 减少 80% 行政负担。CEO Mihir Shukla 的愿景：将 80% 端到端流程自动化，把人从"机械工作"解放回"工艺"。

> Source: [From Robotic to Agentic: Reimagining Process Automation](https://www.automationanywhere.com/lp/robotic-to-agentic-roadmap), EY & Automation Anywhere
> Source: [Automation Anywhere in 2026: Powering the Autonomous Enterprise](https://www.gsb.stanford.edu/faculty-research/case-studies/automation-anywhere-2026-powering-autonomous-enterprise), Stanford GSB Case SM411
> Source: [Imagine 2026: The Next Phase of Agentic Automation](https://www.automationanywhere.com/company/blog/imagine-2026-dallas-ai-product-announcements), Automation Anywhere

### RPA→Agentic 转型的方法论共识

UiPath 和 AA 在方法论上高度一致——这跟 SDLC 领域的转型也是同构的：

1. **确定性骨架 + Agentic 自主**：BPMN/流程定义仍是治理骨架，但执行从"bot 按步骤跑"变成"agent 在框内自主"
2. **编排层成为核心**：Maestro 和 Mozart Orchestrator 都是"指挥中心"——协调人+agent+bot
3. **治理从附加功能变成一等公民**：AI Trust Layer、Centralized Governance、预提交权限模式
4. **从"省人力"到"重新设计流程"**：AA 的 CEO 明确说目标不是优化现有流程，是"解放人做工艺"


## 对 SDLC-BPM 同构性研究的启示

1. **AI-native 创业公司验证了一个关键假设**：旧架构（基于结构化表单、预定义审批流、关系型数据模型）确实不再适合 AI 时代的灵活信息加工
2. **Camunda ProcessOS 是最近的参照物**：4 个 AI agent 做的事，本质上就是"重新设计业务处理流程"
3. **模型公司没有直接做 BPM**——他们在做更底层的能力。但 Anthropic 的 MCP 协议和角色专用插件暗示了方向：BPM 的未来可能是"Agent-native"的，不是"process-native"的
4. **RPA→Agentic 的转型方法论已经由厂商正式化**——UiPath 的白皮书和 AA+EY 的联合白皮书提供了结构化的转型框架。这跟 SDLC 从"CI/CD 管道"到"Agent 原生编排"的转型完全同构
5. **飞书/钉钉在这个光谱里**：他们比传统 BPM 更灵活（处理非结构化信息），比 AI-native 创业者体量更大（有真实用户基础）。但他们的 BPM 基因弱——这可能恰恰是 AI 时代的优势
