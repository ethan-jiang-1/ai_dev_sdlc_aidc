---
title: Office 套件 → Agent 平台 — MS/Google/腾讯的三条路线
date: 2026-07-08
source: web_search (Round 7)
type: deep_dive
status: draft
---

# Office 套件 → Agent 平台

> 2026 年，Office 不再是一个"办公套件"——它正在变成 Agent 运行的基础设施。三巨头在同一个方向上跑了三条不同的路线。

---

## Microsoft：Office = Agent 基础设施

### "一个员工 + N 个数字 Agent"

Satya Nadella（AI Tour Berlin 2026）：

> *"在 Agent 时代，企业配置的第一个资源是 Office——因为 Agent 需要在 Teams 频道里跟人协作，需要访问邮箱。"*

旧模型：一个 Office 许可证 = 一个员工。新模型：一个员工 + N 个数字 Agent——每个 Agent 都需要身份、邮箱、日历、文档权限。

### 从 Chat 到 Delegation

Charles Lamanna（Microsoft EVP of Agents & Business Apps）：

> *"2026 是我们走出聊天的年份。"*

**Copilot Cowork**：用户描述目标 → Agent 自主跨 Excel/Outlook/Word/PPT 执行 → 用户回来看到成品。底层集成了 Anthropic 的 Claude Cowork agentic 架构。

### Agent 365 — Agent 的控制平面

IT 集中治理面板——组织内每个 Agent 都可观测、可管控。这是把 Agent 当成跟用户和设备同等级别的管理对象。

### Copilot = 模型无关平台

| 层 | 做什么 |
|------|------|
| Copilot 品牌 | 统一 UX——用户看到的是 Copilot，不是底层模型 |
| Model Router | Researcher Agent 同时调 GPT + Claude，交叉验证 |
| Model Marketplace | Copilot Studio 让企业选 Claude Opus/GPT/Gemini |
| 第三方插件 | Claude for M365 作为原生插件（AppSource），跟 Copilot 并存 |

### MAI：自研模型减成本

- MAI 模型已在 Excel、Outlook 处理数万次周级 prompt，替代 OpenAI/Anthropic 调用
- Mustafa Suleyman：*"我们付给 Anthropic 很多钱。我们的目标是减少并最终消灭那个成本。"*

### 真正的护城河

不是任何一个模型——是：
1. **4.5 亿商业 M365 用户**——任何 AI 实验室无法复制的分发能力
2. **Microsoft Graph**——连接用户、文档、日历、邮件、组织关系的数据层
3. **Azure 基础设施**——Anthropic 承诺 $30B Azure 消费
4. **控制平面**——Agent 365、AppSource、admin consent——所有 Agent（包括 Claude）都在微软的治理框架内运行

> Source: [Charles Lamanna is moving Microsoft Copilot beyond chat](https://www.fastcompany.com/91550785/charles-lamanna-is-moving-microsoft-copilot-beyond-chat), Fast Company, 2026
> Source: [Microsoft joins AI cost-cutting trend by relying more on its own models](https://techcrunch.com/2026/07/07/microsoft-joins-ai-cost-cutting-trend-by-relying-more-on-its-own-models/), TechCrunch, Jul 2026
> Source: [微软开始甩掉OpenAI和Anthropic](https://www.chinaz.com/ainnews/29450.shtml), 站长之家, 2026

---

## Google：Workspace Intelligence — "上下文即护城河"

### 实时知识图谱

2026 年 4 月 Google Cloud Next 发布 **Workspace Intelligence**——横跨 Gmail/Drive/Docs/Sheets/Slides/Chat 的 AI 认知层。从邮件、文件、对话中构建**实时知识图谱**，为自主 Agent 提供上下文。

### 关键能力

- **Ask Gemini in Chat**：自然语言 Agent 界面——每日简报、行动项、日程
- **Gemini in Sheets**：对话式表格构建；"Fill with Gemini" 填数据快 9 倍；Sheet Canvas 交互仪表盘
- **Skills & Workspace Studio**：可共享的自主 Agent 自动化（如自动发票审查），无代码部署
- **Drive AI Overviews**：语义搜索 + 对话式知识库

### 定价策略：捆绑 vs 溢价

Google：AI 捆绑进基础计划（~40% 涨价）。MS：Copilot 作为 $21/用户溢价插件。

**关键数据**：82% Google Workspace 用户报告 AI 产生切实价值 vs MS 的 66%。

> Source: [The battle for corporate brains: Google unveils Workspace Intelligence](https://primetel.com.cy/the-battle-for-corporate-brains-google-unveils-workspace-intelligence-8598), 2026
> Source: [Navigating the AI-Powered Productivity Wars: Microsoft 365 vs. Google Workspace in Mid-2026](https://www.flowdevs.io/blog/post/navigating-the-ai-powered-productivity-wars-microsoft-365-vs-google-workspace-in-mid-2026), FlowDevs, 2026

---

## 腾讯：WorkBuddy — "直接开走的 F1 赛车"

### 定位

> "我们要交给企业的，是一整辆可以直接开走的 F1 赛车，而不是一台仍需自行组装的发动机和配件。" — 腾讯高管

### 数据

- PC 端月访问量 **885 万**，领先第二名 2.6 倍
- DAU 是竞品的 **3-4 倍**
- 月环比增速 **831%**（2026 年 3 月公测后）
- SkillHub 收录 **7 万+ 技能**

### 产品矩阵

**Agent Suite**：腾讯文档 + 腾讯网盘 + 腾讯乐享知识库，原生接入 WorkBuddy。

**三层架构**：Expert（专家）→ Assistant（助理）→ Team（团队）。

### 生态壁垒

- 微信/企微统一账号体系
- 企业微信连接 **1400 万+ 企业**
- 微信小程序云端与本机双模式
- 支持 100+ MCP 协议，预置 10+ Skills

### 核心差异

| | WorkBuddy | MS Copilot | Google Workspace |
|------|------|------|------|
| 模型 | 混元 + DeepSeek 双引擎，11 款可选 | GPT + Claude + MAI | Gemini |
| 分发 | 微信/企微 14 亿用户 | 4.5 亿 M365 用户 | 30 亿 Google 用户 |
| 定位 | 场景封装（开箱即用） | 平台生态（合作伙伴补能力） | 认知层（上下文即护城河） |
| 定价 | 39 元/月起 | $21/用户溢价 | 捆绑进基础计划 |

> Source: [腾讯 Agent Suite 办公智能体套件](https://cloud.tencent.com.cn/developer/article/2685993), 腾讯云, 2026
> Source: [WorkBuddy看腾讯AI的生态壁垒](https://www.dtinsight.com.cn/nd.jsp?id=3937), 数智洞察, 2026

---

## 三条路线，同一个方向

| | Microsoft | Google | 腾讯 |
|------|------|------|------|
| **战略** | Office = Agent 基础设施 | 上下文 = 企业记忆 | 场景封装 + 生态锁定 |
| **护城河** | Graph + 分发 + 控制平面 | 知识图谱 + 捆绑定价 | 微信/企微 + 7 万技能 |
| **Agent 模式** | Copilot Cowork（委托） | Skills & Studio（自主） | WorkBuddy（专家→助理→团队） |
| **治理** | Agent 365 | AI Control Center | Managed Agents + 五级知识治理 |

**共同方向**：Office 套件不再是"人用的工具"——它正在变成 **Agent 运行的基础设施**。每个 Agent 需要一个"办公身份"（邮箱、日历、文档权限、协作频道）。三家在争的是：**谁的平台成为 Agent 时代的操作系统。**

---

## 对"信息加工流"研究的启示

这是信息加工流的**前端**。之前研究的是后端（BPM/流程引擎/编排），现在前端也清楚了：

```
前端: Office / Workspace / WorkBuddy（Agent 的"家"——身份、上下文、协作）
        ↓
中端: Agentic Orchestration / APO / Agentic BPM（工作流怎么编排）
        ↓
后端: CRM / ERP / HCM（记录系统）
        ↓
治理: Agent 365 / AI Control Center / Managed Agents（横切所有层）
```

**三条线都指向同一件事：信息加工流正在从"人用工具处理信息"变成"Agent 在平台上自主加工信息，人在关键节点策展"。**
