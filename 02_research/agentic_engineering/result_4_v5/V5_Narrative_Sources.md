# 📚 V5 叙事核心论据与引用溯源 (Sources & Citations: Post-Oct 2025)

> **文档说明**：本文档旨在为《AI-Coding 范式变迁》V5 版本中第 16、17、18 页的极端对立叙事（治具派 vs 集群派，主控派 vs 卸载派）提供坚实的客观新闻与工程实录支撑。所有引用均发生于 2025 年 10 月至 2026 年初的真实技术演进时间线中。这些不仅是修辞，而是真实验证过的工程实践。

---

## 🔵 叙事一：大厂基础设施的底座之争 (OpenAI vs Anthropic)

### 1. OpenAI: “治具工程”与百万行代码实验
*   **出处/时间**：2025 年底至 2026 年初，业界披露的 OpenAI 内部基于 GPT-5 (Codex) 的工程实验与方法论（"Harness Engineering"）。
*   **核心事实**：
    *   3 名人类工程师耗时 5 个月，带领基于 GPT-5.2-codex 的 Agent，交付了约 100 万行代码的 Beta 产品，期间实现“零人类手写代码”（zero lines of manually-written code）。
    *   为了防止代码溃烂，他们不依赖自由生成，而是构建了严格的**四大工程治具 (Harness)**：上下文工程、架构约束拦截器 (Architecture Linter)、AGENTS.md 全局系统提示词宪法，以及专门清理冗余代码的 GC Agents。
*   **在 PPT 中的转化**：转化为了 **Page 17 的“治具工程派”**，代表人类对系统解空间的极端不信任和绝对约束。

### 2. Anthropic: “并发集群”与十万行 C 编译器重构
*   **出处/时间**：2026 年 2 月，Anthropic 安全研究员 **Nicholas Carlini** 随 Claude Opus 4.6 官宣发布的工程博客《Building a C compiler with a team of parallel Claudes》。
*   **核心事实**：
    *   Carlini 展示了 **Agent Teams（智能体团队）** 这个破坏性创新的惊人威力。
    *   实验中，他让 16 个 Claude 子智能体在一个主控 Agent 的分发下，几乎在零干预（zero-shot/unsupervised）状态下，并行阅读并用 Rust 重写了多达 10 万行的 C 编译器（且支持编译 Linux 内核）。
*   **在 PPT 中的转化**：转化为了 **Page 17 的“集群并发派”**，作为对立面，代表着放弃人工脚手架，用多开的算力暴力推演架构的“暴力美学”。

---

## 🔴 叙事二：顶级工程思想布道者的对决 (Truell vs Cherny)

### 3. Cursor CEO Michael Truell: 抨击“Vibe Coding”，捍卫“Clarity” 
*   **出处/时间**：2025 年 12 月至 2026 年 1 月，Cursor CEO **Michael Truell** 的多次公开受访及内部工程实验复盘（包括 Cursor 百个 Agent 一周重写百万行浏览器的实验）。
*   **核心事实 / 原文引用**：
    *   Truell 极度排斥脱离代码底层的“闭眼开发（Vibe Coding）”。他警告这会导致在摇摇欲坠的地基上持续加盖，最终系统全面崩塌（"If you close your eyes and don't look at the code... things start to kind of crumble"）。
    *   2026 年的共识：交付极快极廉价（Shipping fast is easy），但在庞然大物般的逻辑黑盒中维持**“清晰度 (Clarity)”** 才是真正稀缺的顶级工程能力。必须要让人与底层的状态保持链接。
*   **在 PPT 中的转化**：转化为了 **Page 18 的“务实主控派”**。说明在 SDD（Spec驱动）的大前提下，人类依然需要紧贴底层架构。

### 4. Claude Code 缔造者 Boris Cherny: 彻底的激进卸载
*   **出处/时间**：2025 年末至 2026 年初，**Boris Cherny**（Anthropic Claude Code 产品核心缔造者）关于颠覆终端开发者体验的论述。
*   **核心事实 / 原文引用**：
    *   Cherny 展现了最极端的全自动化开发样板：他个人在长达一个月的时间里**完全没有打开过任何传统的 IDE**。期间他完成了 259 个 Pull Requests，涵盖数万行代码的增删，且全部由 Claude Code（Opus 模型）在后台生成并提交。
    *   他信奉完全外包流水线：开发者只需要给出一个精确的 Spec（意图）和 Ticket 看板，让智能组队打样，并在终点验证。
*   **在 PPT 中的转化**：转化为了 **Page 18 的“激进卸载派”**，代表着将代码完全视作随时由大模型抛弃和重构的临时消耗品。
