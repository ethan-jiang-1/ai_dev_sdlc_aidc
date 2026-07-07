---
type: kol_deep_dive
person: Boris Cherny
organization: Anthropic (Claude Code creator)
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://tech.yahoo.com/ai/claude/articles/interview-claude-code-creator-accident-171651759.html
  - https://timesofindia.indiatimes.com/technology/tech-news/anthropics-boris-cherny-once-again-reminds-software-engineering-is-dead/amp_articleshow/130851423.cms
  - https://www.xda-developers.com/set-up-claude-code-like-boris-cherny/
  - https://hub.baai.ac.cn/view/52377
  - https://cloud.tencent.com.cn/developer/article/2669104
key_concepts:
  - software_engineering_is_dead
  - claude_code_design_philosophy
  - terminal_over_ide
---
# Boris Cherny — Claude Code 之父："软件工程已死"

> Anthropic Claude Code 负责人。自从 2025 年 11 月以后没手动写过一行代码。他的论点不是"AI 帮助编程"——而是"手动编程作为一种职业正在终结"。

---

## 核心论点

> *"Software engineering as we knew it is already gone. What replaced it is something closer to what I call a builder — someone who knows what to build, not how to type it out."*

Cherny 的三个关键主张：

1. **手动写代码已经结束**——他自 2025/11 以后未手动编辑过一行代码
2. **"软件工程师"会消失**——2026 年底将被 "Builder"（构建者）取代
3. **Anthropic 内部没有任何人手写代码**——不是工程师，不是 PM，不是设计师，甚至不是财务

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。

## 他的个人工作流

Cherny 的日常工作方式——自称"令人惊讶地朴素"：

| 元素 | 细节 |
|------|------|
| **并行会话** | 10-15 个并行 Claude 会话：5 个终端 tab + 5-10 个 Web 会话 |
| **Plan Mode** | 每个会话从只读探索模式开始，确认方向后才翻转为执行 |
| **Agent 数量** | 每天数百个并行 Agent；夜间数千个跑深度异步任务 |
| **最好的一天** | **150 个 PR 合并**（故意测试极限） |
| **MCP 集成** | Claude 实例通过 **Slack 互相通信**——他的 Claude 会 DM 同事的 Claude 自主解决问题 |
| **CLAUDE.md** | 每个错误变成永久规则——"同样的反馈永远不需要给两次" |
| **模型偏好** | 复杂的长运行架构任务用 Opus 而非 Sonnet |

---

## Anthropic 内部的 "Agent 文明"

Cherny 揭示了 Anthropic 内部 AI 使用的规模：

- **65% 代码**由内部 Claude 生成
- **80-90% 工程师每天使用；~100% 每周**
- Claude 实例通过 **Slack 自主通信**——不是科幻，是日常
- 一位 15 年没写代码的经理入职第一天就开始提交核心产品代码
- 一个周末：工程师 Daisy Hollman 用 **20 个并行 Claude** 构建并发布了整个 Claude Code 插件系统
- 压力测试：**16 个 Agent，2,000 个会话，$20K API 费用** → 构建了能编译 Linux 6.9 跨 x86/ARM/RISC-V 的 Rust C 编译器

---

## Agentic Coding 的三个时代

Cherny 将编程工具的历史分为三个阶段：

| 时代 | 做什么 |
|------|--------|
| **完全 Agentic** | 模型做**全部**编码；人类描述意图 |

> *"You have a model, and you give it tools, and then you give it some sort of context and a task to do. Then, it uses the tools to accomplish the task. It's different than ChatGPT, because it's not one-shot... it will keep going until it's done."*

---

## 2026 预测

| 预测 | 细节 |
|------|------|
| **IDE 将消失** | "大概率年底人们不再使用 IDE"——终端和 Web 是未来 |
| **软件工程师 → Builder** | 每个人都变成能编码的 PM |
| **产品"overhang"将解决** | 模型能力已经超过当前产品提取能力 |
| **Claude Code 可能收敛到 ~100 行代码** | 产品层是弱模型的脚手架；模型变强，脚手架溶解 |
| **下一个稀缺技能** | 不是写 prompt——是**写验收标准、测试边界和审查清单** |

---

## 行业跟进数据

Cherny 的观点不是孤立的——Big Tech 正在跟进：

| 公司 | AI 代码采用率 | 来源 |
|------|-------------|------|
| **Google** | 75% 新代码 AI 生成（2024 年底 25%） | [Sundar Pichai, Google Cloud Next 2026](https://timesofindia.indiatimes.com/technology/tech-news/google-ceo-sundar-pichai-says-ai-generates-75-codes-at-the-company-why-this-number-matters/articleshow/130451126.cms) |
| **Meta** | 强制 65% 工程师在 H1 2026 前 >75% 提交代码由 AI 生成 | [Business Insider, 2026/03](https://www.businessinsider.com/meta-ai-push-employee-goals-tool-adoption-2-026-3) |
| **Snap** | 公司级 65% AI 生成代码底线 | [Reuters/TechRepublic, 2026/04](https://www.techrepublic.com/article/news-snap-ai-layoffs-april-2026/) |
| **Amazon** | 通过 AWS Bedrock 向所有企业员工正式推出 Claude Code | [Business Insider, 2026/05](https://ca.finance.yahoo.com/news/amazon-admits-flagship-ai-coding-143000057.html) |

---

## 他自己承认的限制

尽管极其大胆的修辞，Cherny 有重要的自我限定：

1. **他审查 Claude 产出的每一行。** *"我不认为我们已经到了可以完全撒手的程度。"*
2. [Anthropic 2026 Agentic Coding Trends Report](https://claude.com/blog/eight-trends-defining-how-software-gets-built-in-2026) 显示：工程师 ~60% 时间使用 AI，但**完全委托的任务只有 0-20%**
3. CEO Dario Amodei 称此为**"半人马阶段"**——人类+AI 共同操作，在 AI 超越之前的短暂窗口
4. **"解决"是个人的。** Cherny 说编码对**他**和**他的 TypeScript/React 技术栈**解决了。嵌入式系统、HFT、工业控制代码不是他的范围
5. **设计尚未触及。** 视觉和空间推理仍然是人类领域

---

## 与 Karpathy 的对话

Cherny × Karpathy（2026）增添了哲学层次：

- Karpathy 确认了自己的轨迹：**2025/11：80% 手动 / 20% AI → 2025/12：80% AI / 20% 手动**
- **"Slopacalypse" 辩论**：Karpathy 担忧 AI 生成代码污染；Cherny 更乐观——"在 Anthropic，AI 审查 AI"
- **"Wait for the next model"**——当被追问差距时，Cherny 的回答简单直接

---

## 底线

Boris Cherny 是 Anthropic 内部最突出的声音，主张 **Agentic Coding 已经在前沿 AI 实验室内部终结了手动编程作为一种职业**，而行业其他部分落后 6-18 个月。

他的核心信息：**停止把自己定义为"程序员"，开始定义为"构建者"**——编排 AI Agent、定义意图、审查输出、拥有架构决策权。稀缺技能从**生成**（写代码）转移到**判别**（评估代码）。

他的"编程已死"框架是 provocative marketing 还是准确预测仍在激烈辩论——但 Google、Meta、Amazon、Snap 的采用数字强烈表明方向的真实性。

---

**Source:** [Yahoo/Tech: Interview with Claude Code Creator](https://tech.yahoo.com/ai/claude/articles/interview-claude-code-creator-accident-171651759.html) · [Times of India](https://timesofindia.indiatimes.com/technology/tech-news/anthropics-boris-cherny-once-again-reminds-software-engineering-is-dead/amp_articleshow/130851423.cms) · [XDA Developers: Setup like Boris Cherny](https://www.xda-developers.com/set-up-claude-code-like-boris-cherny/) · [BAAI: Karpathy × Cherny](https://hub.baai.ac.cn/view/52377) · [Tencent Cloud](https://cloud.tencent.com.cn/developer/article/2669104)
