# AI Coding: Agentic Frontier - 核心信息来源与引用清单 (References)

这份文档汇总了在撰写 `AI-Coding-Agentic-Frontier.md` (智能体工程的前沿探索与五大路径) 演示讲稿时，所引用的所有核心事实、数据、人物言论的来源证明。所有的探索路径均立足于行业顶尖团队与专家的真实公开分享或内部工程实践报告。

---

## Route 1：治具流水线 (Harness Engineering)
**代表团队：** OpenAI 内部 Harness Team
*   **核心叙事：** 3名人类工程师加 GPT-5 级模型，5 个月生成百万行代码，零人类手写代码。通过强大的“治具”（如 GC Agents, Linter 门控）限制 AI 自由度。
*   **信息来源 (外部远端)：**
    *   OpenAI 官方工程博客：[Harness Engineering](https://openai.com/index/harness-engineering/)
*   **信息来源 (本地归档)：** 
    *   `wave4_new/route_1_openai_harness.md`
    *   `wave4_new/route_1_raw_openai.md`

## Route 2：并发集群 (Parallel Agents / Agent Teams)
**代表人物：** Nicholas Carlini (Anthropic 技术领袖)
*   **核心叙事：** 通过 16 个 Claude 模型并发重写 C 编译器，两周内生成 10万行代码。利用基于 Git File-locking 的野生协作模式，以算力并发对抗单模型智力瓶颈。
*   **信息来源 (外部远端)：**
    *   Anthropic 官方工程文章：[Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler)
*   **信息来源 (本地归档)：**
    *   `wave4_new/route_2_anthropic_cluster.md`
    *   `wave4_new/route_2_raw_anthropic.md`

## Route 3：务实主控派 (The Control Faction)
**代表人物：** Michael Truell (Cursor / Anysphere 创始人兼 CEO)
*   **核心叙事：** 猛烈批评彻底放弃审查代码的 "Vibe Coding" 大潮，认为不直视底层代码将在地基不稳的基础上造成毁灭性崩塌 (Crumble)。提出 AI 时代护城河仍然是开发者的 "Clarity" (逻辑清晰度)。
*   **信息来源 (外部远端)：**
    *   《Fortune》(财富) 杂志在 Fortune's Brainstorm AI 大会的独家实录与报道：[Cursor CEO Michael Truell issues 'vibe coding' warning: 'Things start to kind of crumble'](https://fortune.com/2025/12/25/cursor-ceo-michael-truell-vibe-coding-warning-generative-ai-assistant/)
*   **信息来源 (本地归档)：**
    *   `wave4_new/route_3_michael_truell_cursor.md`

## Route 4：激进卸载派 (The Radicals)
**代表人物：** Boris Cherny (前 Meta 核心架构师，Claude Code 缔造者)
*   **核心叙事：** 完全卸载本地代码编辑器 (IDE)，仅靠终端后台挂载 Claude Code。在极短时间内靠 AI 生成合并 259 个 PR。把代码视作沟通意图的过渡态。
*   **信息来源 (外部远端)：**
    *   Anthropic 官方 YouTube 访谈纪录片：[Mastering Claude Code in 30 minutes with its creator, Boris Cherny](https://www.youtube.com/watch?v=6eBSHbLKuN0)
    *   相关访谈：[Head of Claude Code: What happens after coding is solved | Boris Cherny](https://www.youtube.com/watch?v=We7BZVKbCVw)
*   **信息来源 (本地归档)：**
    *   `wave4_new/route_4_boris_cherny_anthropic.md`
    *   `wave4_new/route_4_raw_Boris Cherny.md`

## Route 5：业务编排与集群 (Orchestration & Swarm)
**代表团队/人物：** Stripe 内部 "Minions" 系统、Elvis (@elvissun)
*   **核心叙事：**
    *   **Stripe**: 使用 MCP(Model Context Protocol) 作为大脑，利用一次性抛弃式容库环境(Devbox)每周生成 1300+ 个无人工介入提笔的全自动 PR，采取极致的沙盒硬熔断限频测试机制。
    *   **Elvis / OpenClaw**: 提出“基于个人的开发团队”，将大语言模型的业务心智(Orchestrator)与工程手足(Workers)进行物理隔离（类似 Ralph Loop V2 的事件驱动模型）。
*   **信息来源 (外部远端)：**
    *   Stripe 开发者博客：[Minions: Stripe’s unattended AI coding agents](https://stripe.com/blog/minions) (及多篇技术专栏解析)
    *   Elvis (@elvissun / 零度摩擦) 的技术架构公众号首发解析与 Github 高星项目 `OpenClaw` 宣发文。
*   **信息来源 (本地归档)：**
    *   `wave4_new/route_5_raw_stripe_minions.md` (Stripe 工程细节发掘存桩)
    *   `wave4_new/route_5_raw_openclaw_agent_swarm.md` (Elvis 原文与思维逻辑全解析)
    *   `wave4_new/route_5_industry_kol_research.md`
