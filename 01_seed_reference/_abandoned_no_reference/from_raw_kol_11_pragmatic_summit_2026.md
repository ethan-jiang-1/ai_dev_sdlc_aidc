---
type: kol_deep_dive
content_type: event_synthesis
event: Pragmatic Summit 2026
verification_status: partially_verified
note: 来源为会议现场报道和社交媒体，多为一手引用但无单一直播链接
source_urls:
  - https://newsletter.pragmaticengineer.com/p/cycles-of-disruption-in-the-tech
key_participants:
  - Kent Beck
  - Martin Fowler
  - Simon Willison
  - Thomas Dohmke (ex-GitHub CEO)
  - Atlassian CTO
---
# Pragmatic Summit 2026 — AI 时代软件工程的"伍德斯托克"

> Gergely Orosz (*The Pragmatic Engineer*) 主办的首届线下大会，2026 年 2 月，旧金山。Beck + Fowler 同台、Simon Willison、前 GitHub CEO + Atlassian CTO——这是 2026 年 AI 时代软件工程最重要的一次线下聚会。

---

## 为什么重要

Pragmatic Summit 有 **"Woodstock for engineering leaders in the AI era"** 的评价。它的特殊之处在于：

1. **Orosz 作为召集人**——*The Pragmatic Engineer* 是 AI 时代最有影响力的工程 newsletter 之一
2. **Beck + Fowler 罕见同台**——Agile Manifesto 两位合著者，在 Agile 25 周年之际联合面对 AI
3. **实操家 + 理论家共存**——不是 vendor conference，没有销售 pitch
4. **Fowler 同时在 Deer Valley 举办了"未来软件开发 retreat"**——与 2001 年 Agile Manifesto 同一地点

---

## Session 1: Beck + Fowler 炉边对话

> 大会最受欢迎的 session。两位 Agile Manifesto 合著者首次以 AI 为主题联合公开对话。

### AI 的量级

Fowler 的开场判断：

> *"Nothing has hit with the magnitude of AI. This is a whole size different from anything we've faced before."*

Beck 补充：AI 是不同的量级——大于微处理器、OOP、互联网、Agile 的总和。这个判断与 Dave Farley 完全一致（"大于所有这些"）。

### Agile 的教训正在 AI 时代重演

Beck 识别出三个正在重演的模式：

| Agile 时代的错误 | AI 时代正在重演 |
|----------------|--------------|
| 公司激励不对齐 | "让团队用 AI"但绩效体系没变 → 表面采用、实际抵制 |
| "蛇油"供应商 | 夸大 AI 能力的工具商 |
| 中层开发者被挤压 | 既不够资深成为编排者，又不够初级快速学习 |

### "Re-Soloing"——Beck 的核心关切

> *"One engineer managing 6 agents in isolation — that's not the same as pair programming with real humans."*

XP 的核心洞见是：软件开发的瓶颈不是打字速度，是**理解、沟通和协作**。Agent 加速了打字但绕过了理解。

Beck 的建议：**两个人 + 一个 Agent 可能优于一个人 + 六个 Agent。** 慢一点的 Agent 是好的——它给人留出真正的对话时间。

### TDD——从"推荐"到"不可协商"

两人一致：TDD 在 AI 时代从"best practice"变成了 **"not optional"**。理由：

- 测试是你对 AI 说"这个东西不能碰"的唯一方式
- Agent 会在测试失败时自动迭代——但如果没有测试，它迭代的方向可能是**删除测试本身**（Beck 的著名轶事）

### 团队规模：缩小还是做更多？

| Beck | Fowler |
|------|--------|
| 团队可能缩小——一个人 + Agent 产出过去一个团队的产出 | 同样规模的团队做**多得多的东西** |

### Agent 倦怠

> *"Managing AI agents is mentally exhausting."*

两人都建议设定边界——当你开始产出"负价值"时停下来。

---

## Session 2: Laura Tacho — DX 数据 + 联合声明

Laura Tacho 呈现了独家 DX 数据：

- **92% 的开发者每月使用 AI 编码工具**
- AI 是**放大器**：健康组织看到 **50% 更少的 incidents**；功能失调组织看到 **2 倍更多** incidents

这精确验证了 Farley 的判断：*"If you're already working well, AI will be a big win. If you're working poorly, you'll just dig a deeper hole faster."*

### Beck + Tacho + Yegge 联合声明

> *"Organizations are constrained by human and systems-level problems. We remain skeptical of the promise of any technology to improve organizational performance without first addressing human and systems-level constraints. We remain skeptical and we remain human."*

---

## Session 3: Simon Willison — Agentic Engineering 的阶段论

Willison 在 Summit 上覆盖了 AI 采用的完整光谱：

| 阶段 | 描述 |
|------|------|
| ChatGPT 阶段 | 用聊天界面生成代码片段 |
| Copilot 阶段 | 编辑器内补全 |
| Coding Agent 阶段 | Agent 自主执行多步工程任务 |
| "不看代码"阶段 | Vibe Coding → 正在与 Agentic Engineering 趋同 |

### 新工具：Showboat

Willison 介绍了 **Showboat**——一个让 Agent 演示/测试自己工作的工具。核心思路：Agent 不只是写代码，还要**证明它是对的**。

### 新概念：Conformance-Driven Development

Tests 不再只是 validation——它们变成了**合规检查**。"Tests are no longer even remotely optional — they're free now."

---

## Session 4: Thomas Dohmke (前 GitHub CEO) + Rajeev Rajan (Atlassian CTO)

> 最具实操深度的 session。前 GitHub CEO（现在自己创业）和 Atlassian CTO 的对话揭示了 Big Tech 内部的真实状态。

### "AI-Native Teams" 的真实面貌

- Atlassian 内部已有工程师团队**零手写代码**——一切由 Agent 完成
- 工程师的角色：编排 Agent、设定规则、验证输出
- Rajeev: AI 的重点**不是减人**，是构建以前不可能构建的东西
- Dohmke: "AI-native"就像 2008 年的"cloud-native"——我们只能事后才真正知道它意味着什么

### 角色坍缩

> PM → Product Engineer · Designer → Design Engineer · Engineer → 半 PM

- 角色之间的 Venn 图重叠**急剧扩张**
- Atlassian 的 PM 在用 AI 写代码，设计师在用 AI 写代码，工程师在做更多产品决策

### "Homer Simpson 车"问题——Dohmke 的警告

> *"When everyone can ship code but nobody is doing architecture/design oversight, you get the Homer Simpson car."*

每个人都能提交代码，但没人做架构监督——结果是辛普森一家的车：什么功能都有，但什么都不对。

### 瓶颈迁移——Rajan 的框架

| 左边（更上游） | 中间 | 右边（更下游） |
|-------------|------|-------------|
| 规划 + Spec | ~~写代码~~（变成免费的） | CI/CD + 部署 + Incidents |

### Atlassian 的内部武器：Rovo Dev

- 基于 Anthropic 模型构建的内部编码 Agent
- **击败了专门的代码 Agent 竞品**——因为能通过 Teamwork Graph（150 亿连接）获取上下文
- 知道谁在哪个 PR 上协作过、哪些 Jira issues 关联、代码变更的历史上下文

### CTO 们又开始写代码了

- Rajeev **自己买了台笔记本电脑**，度假时绕过公司 IT 限制使用 Claude Code 写 Python
- 银行 CTO 晚上用 AI 工具 coding——"我又能写代码了"
- 管理层将压缩——Rajan 引用 Jensen Huang 的 **40-50 个直接下属**模型
- 给工程师的建议：**别急着进管理**——这是 hands-on 的黄金时代

### Token 成本——CFO 们没准备好

- Token 消耗正在吃掉固定工程预算——有团队因为**烧 token 太快被限速**
- CFO 们对这种弹性成本结构毫无准备
- 但两人都同意：**coding 又变好玩了**——把烦人的构建错误丢给 Agent 说"修好它，我不想看"的价值被低估了

---

## Fowler 的平行活动：Deer Valley Retreat

在旧金山 Summit 的同时，Fowler 在 Deer Valley, Utah——**2001 年 Agile Manifesto 诞生的同一个地点**——举办了"未来软件开发 retreat"，约 50 位技术领袖参加。

这个平行活动传递了一个明确的信号：**Agile 社区不是在抵制 AI——他们是在同一个地点、25 年后，重新思考软件开发是什么。**

---

## 五个跨 Session 主题

| 主题 | 来源 | 关键信息 |
|------|------|---------|
| **AI 是放大器，不是修复器** | Tacho, Beck, Fowler | 好团队更好，差团队更差 |
| **角色边界在快速消融** | Rajan, Dohmke, Willison | PM/Designer/Engineer 的 Venn 图重叠急剧扩张 |
| **TDD 不可协商** | Beck, Fowler, Willison | 三人独立得出相同结论 |
| **中层工程师风险最高** | Beck, Dohmke | 不够资深去编排，不够初级去快速学习 |
| **别进管理——现在是黄金时代** | Rajan, Dohmke | CTO 们又开始写代码了。Jensen Huang 的 40-50 下属模型 |

---

## 来源

- [Pragmatic Engineer: Cycles of Disruption in Tech](https://newsletter.pragmaticengineer.com/p/cycles-of-disruption-in-the-tech)
- [Pragmatic Engineer: Future of Software Engineering with AI](https://newsletter.pragmaticengineer.com/p/the-future-of-software-engineering-with-ai)
- [AI Nave: Navigating the AI Revolution](https://ainave.com/tech-news/navigating-the-ai-revolution-insights-from-software-pioneers-martin-fowler-and-kent-beck)
- [Podwise: Building world-class engineering teams in the age of AI](https://podwise.ai/episodes/7546403)
- [17gw.com: 前GitHub CEO和Atlassian CTO圆桌](https://17gw.com/thread-3500-1-1.html)
- [Martin Fowler: Fragments Feb 13, 2026](https://martinfowler.com/fragments/2026-02-13.html)
- [pragmaticsummit.com](https://www.pragmaticsummit.com/)
