# AI 软件工程的深水区：自动化代码工厂的四大核心基建 (Agentic Engineering V1)

---

## 引言：从"辅助驾驶"到"工厂流水线"的跃迁

*   **背景**：早期的 AI 辅助开发（Copilot）建立在 SDD（规范驱动开发）假设上：只要 Prompt 描述精确，AI 就能写出好代码。这个假设在百万行级的多 Agent 协作场景下彻底失效——大语言模型本质是概率预测机器，"软约束（Prompt）"无法阻止熵增，代码腐化速度与生成速度成正比。

*   **问题核心**：当 AI 生成代码的速度远超人类 Review 吞吐量时，传统的"人盯代码"模式成为瓶颈，工程组织面临两个方向的压力：
    *   **代码质量下限**：AI 幻觉与架构漂移如何被系统性阻断，而非人工发现？
    *   **交付吞吐上限**：单体 Agent 的串行输出速度远不够，如何安全地扩展并发？

*   **行业现状**：没有标准答案，但已经跑出了**两大门派，四种实战模式**。

---

## 全景总览：两大门派与四大模式

| 大类 | 代表模式 | 发起方 | 时间 | 官方名称 |
| :--- | :--- | :--- | :--- | :--- |
| 🔵 护栏与物理沙盒 | OpenAI Harness | OpenAI 内部研发团队 | 2025 年 8 月起 | **Harness Engineering（驾驭工程）** |
| 🔵 护栏与物理沙盒 | StrongDM Dark Factory | StrongDM（项目：`Attractor`） | 内部实施：2025 年 7 月；公开披露：2026 年 2 月 | **Dark Factory（暗黑工厂）** |
| 🔴 高并发协同集群 | Vibe Kanban | BloopAI（开源）/ OpenAI Symphony（探索中） | Vibe Kanban 首版：2025 年 6 月；Symphony 开源预览：2026 年 3 月 | **Vibe Kanban** / **Symphony** |
| 🔴 高并发协同集群 | Anthropic Agent Teams | Anthropic（Nicholas Carlini，Safeguards） | 2026 年初 | **Agent Teams（智能体兵团）实验** |

---

## 流派 1.1：OpenAI 驾驭工程 (Harness Engineering)
### 【Page 1】模式概述

**核心主张**：不依赖 Prompt 软约束，改为在构建流水线上建立硬性物理拦截。

> **来源**：**OpenAI** 内部研发团队 | **2025 年 8 月**起公开披露 | 官方名称：**Harness Engineering（驾驭工程）**

*   **案例数据**：OpenAI 内部（2025 年 8 月起）— **3 名工程师，5 个月，~100 万行代码**的 Beta 产品，全程无人工手写源代码。引擎累计合并约 1,500 个 PR；每位工程师每天平均合入约 **3.5 个大体量 PR**（Linters 和 CI 系统承担了原本由人工承担的质量把关）。

*   **核心机制**：Agent 生成的代码如果越过预定的架构层级边界，在构建层面直接被物理弹回（Build Failed）。AI 不需要"理解规则"，只需要根据构建失败的反馈不断修正，直到代码符合所有静态检查。这一模式被称为 **Harness Engineering（驾驭工程）**。

---

## 流派 1.1：OpenAI 驾驭工程 (Harness Engineering)
### 【Page 2】模型主力在做什么？

*   **架构阻断器（Architectural Linters）**：Agent 提交的代码一旦违反架构分层约束，CI 流水线中预设的静态检查器（Linters）立即返回构建失败，进入强制重构循环，直到通过为止。不靠 Prompt 叮嘱，靠硬性阻断。

*   **持续运行的垃圾回收 Agent（GC Agent）**：系统内部常驻一批专用 Agent，全天候扫描代码库中的过时文档、不一致命名、违规冗余代码，持续提交修复 PR——自动偿还技术债，不需要人工触发。

---

## 流派 1.1：OpenAI 驾驭工程 (Harness Engineering)
### 【Page 3】人类主要做什么？

*   **上下文工程（Context Engineering）**：人类不再写具体业务代码，而是维护高质量的背景文档（如 `AGENTS.md`），以及接入实时的系统可观测性数据（Observability），让 Agent 自主拉取当前状态做决策。

*   **定义并维护硬性防线**：将架构决策转化为可执行的 Lint 规则、类型约束、CI 阻断脚本——凡是无法被机器检验的规范，都不算真正的规范。这是驾驭工程的核心理念：**规范不是写给 AI 看的，是执行给 AI 的。**

---

## 流派 1.2：StrongDM 暗黑工厂 (Dark Factory)
### 【Page 1】模式概述

**核心主张**：完全取消人工 Code Review，用高保真的隔离沙盒做端到端验收。

> **来源**：**StrongDM**（网络安全公司）| 内部实施：**2025 年 7 月**；公开披露：**2026 年 2 月 7 日**（Simon Willison 文章 "How StrongDM AI team build serious software without looking at code"）| 项目代号：**`Attractor`** | 官方名称：**Dark Factory（暗黑工厂）**，Dan Shapiro "第五级 AI 架构（Level 5）"愿景

*   **案例**：网络安全公司 StrongDM 的 `Attractor` 编码 Agent 项目，内部推行：**零手工编码（No hand-coded software）+ 取消人类 Code Review。** 这一模式呼应了业界称之为"黑灯工厂（Dark Factory）"的第五级 AI 架构愿景。

*   **极端颠覆**：`Attractor` 的 GitHub 仓库里不存在任何传统源代码逻辑——充当"源代码"的，**仅仅是 3 个极度详尽的 Markdown 规范文件**（Spec-as-Source）。人类工程师的身份完全转变为 **Specification Writers（规范编写者）**。

---

## 流派 1.2：StrongDM 暗黑工厂 (Dark Factory)
### 【Page 2】模型主力在做什么？

*   **数字孪生宇宙（Digital Twin Universe, DTU）**：Agent 生成的代码不交给人看，而是直接部署进与生产环境物理隔离的本地沙箱。沙箱中，Okta、Jira、Slack、Google Drive 等第三方服务被编译为本地 Go 语言独立二进制克隆体（Behavioral Clones）。

*   **持续评估循环（Evaluation Loops）**：Agent 每小时在沙箱内跑数千个端到端场景（Holdout Sets），无需担心触碰外网限流或账单。不通过则原地打回重写——循环执行，直到代码行为收敛于 Markdown 规范 100% 的描述意图。

---

## 流派 1.2：StrongDM 暗黑工厂 (Dark Factory)
### 【Page 3】人类主要做什么？

*   **转型为规范编写者（Specification Writers）**：Markdown 是这套体系的唯一"源代码"。人类的核心输出从代码转为极度详尽、边界清晰的规范文本。这对写作质量的要求甚至高于写代码。

*   **沙盒建设与算力成本承担**：这是重资产基建路线。据业内披露，单个工程师名下的 AI Token 沙盒运算成本每日约 **$1,000 美元**——人类把用于写代码和 Review 的时间，换成了"写规范 + 用沙盒穷举验证"的成本结构。

---

## 流派 2.1：流水线看板与 Git 隔离 (Kanban & Pipeline)
### 【Page 1】模式概述

**核心主张**：利用 Git 底层的目录隔离机制，让多个 Agent 在物理上互不干扰地并发执行。

> **来源**：**BloopAI** 开源（**Vibe Kanban**，**2025 年 6 月**首版发布，后端 Rust 编写）；**OpenAI** 内部平行探索 **Symphony**，已于 **2026 年 3 月**作为 project preview 开源

*   **案例**：BloopAI 开源的 **Vibe Kanban**，以及 OpenAI 内部正在探索的 **Symphony** 项目。它们将传统项目管理看板（Jira/Trello 风格）与底层 Git 文件系统深度绑定。

*   **核心解法**：当工程师在看板上将两张卡片（如"修复 DB 连接"和"重构 UI 按钮"）同时拖入 In Progress，系统在服务器底层并发执行 `git worktree add`，让每个 Agent 在**物理隔离的独立硬盘目录**里工作，彻底消除文件锁冲突。

---

## 流派 2.1：流水线看板与 Git 隔离 (Kanban & Pipeline)
### 【Page 2】模型主力在做什么？

*   **基于 Git Worktree 的物理隔离并发**：Vibe Kanban 后端（由 Rust 编写）在每张卡片触达 In Progress 时，自动执行 `git worktree add <隔离路径> <新分支>`。Agent A 和 Agent B 工作在服务器物理硬盘的**完全不同的目录**里，但安全地**共享同一个 `.git` 历史元数据**。

*   **零文件锁冲突的高并发**：无论多少 Agent 同时并发修改文件、执行 `npm install` 与 `build` 编译，都不会产生任何文件锁冲突。卡片完成后，系统自动提交带有说明的 Pull Request，等待人工确认。

---

## 流派 2.1：流水线看板与 Git 隔离 (Kanban & Pipeline)
### 【Page 3】人类主要做什么？

*   **任务切割的精度决定并发质量**：这套模式的关键约束是：并发的多个子任务必须在文件层级互不重叠（Non-overlapping sub-tasks）。如果两张卡片最终都需要修改同一个底层共享模块，隔离就会失效，合并时出现冲突。**工程师的价值从「写代码」转移到「精确切割任务边界」。**

*   **最终合并的人工判断**：当所有分支汇聚时，少量残余的合并冲突仍需人工处理。这是人类在整个流程中最后的直接介入点。

---

## 流派 2.2：去中心化集群与原子锁 (Decentralized Agent Teams)
### 【Page 1】模式概述

**核心主张**：放弃中央调度器，用原始的文件锁 + TDD 作为去中心化集群的唯一协调机制。

> **来源**：**Anthropic** | 安全研究员 **Nicholas Carlini**（Safeguards 团队）主导 | **2026 年初**公开披露 | 官方描述：**Agent Teams（智能体兵团）**实验

*   **案例**：Anthropic 安全研究员 Nicholas Carlini（2026 年初）的实验：**16 个 Claude Opus 4.6 实例**，共享同一个 Git 仓库，无中央调度，连续运行两周，目标是用 **Rust 编写一个 C 语言编译器**（共计约 10 万行代码）。

*   **结果**：集群共运行约 **2,000 个任务 Session，消耗约 20 亿 Input Tokens，API 账单约 $20,000 美元**。最终成功编译 Linux Kernel 6.9、QEMU、PostgreSQL、运行《Doom》，在 GCC Torture Test Suite 中通过 **99%** 的测试用例。

---

## 流派 2.2：去中心化集群与原子锁 (Decentralized Agent Teams)
### 【Page 2】模型主力在做什么？

*   **基于文件的原子任务锁（Git-based Lock Files）**：仓库根目录的 `current_tasks/` 文件夹存放待处理任务文件。Agent 要认领某个任务，先创建对应的锁文件（如 `parse_if_statement.txt`）并立即 `git push`。如果另一个 Agent 慢了一秒，Git 同步阻塞会强迫它放弃，去选择其他空闲任务——用文件系统实现去中心化任务分配。

*   **共享黑板传承上下文（Shared Markdown）**：Agent 之间不直接通信，但共同参考仓库中的一份全局 Markdown 文档。前序 Agent 记录的踩坑经验（如"不要用 Regex 解析宏定义"），后续 Agent 第一步就会读取，实现跨 Session 的知识传承。

---

## 流派 2.2：去中心化集群与原子锁 (Decentralized Agent Teams)
### 【Page 3】人类主要做什么？

*   **TDD 作为协调神谕（Testing as Coordination Oracle）**：在没有中央 Tech Lead 仲裁的环境里，测试用例承担了原本属于人类的裁判职责。Agent 提交代码后直接跑测试，跑绿则获得合并权并释放文件锁，跑红则继续修改——TDD 是这个无主集群的唯一共识机制。人类的职责是**提前构建足够覆盖、足够严苛的测试套件**。

*   **接受高算力成本换低协调成本的权衡**：这套模式的代价是真实的算力账单（本实验为 $20,000）。没有复杂的调度系统，没有精心的任务切割——代替它们的是更多的并发 Token 消耗和更长的试错时间。是否值得，取决于任务的可测试性和算力成本结构。

---

## 收尾：这些都是进行中的工程实验

**没有哪一套是最终答案。**

这四种模式都在 2025–2026 年被真实推进，但都处于早期探索阶段，各自有明确的适用边界和成本代价：

*   **护栏/沙盒路线**适合需要极高代码质量保证的场景，代价是重资产的基建投入（DTU 构建成本、$1,000/天的 Token 沙盒）。
*   **并发集群路线**适合可以被清晰切割或可测试性极高的任务，代价是算力账单和协调机制的缺失。

对工程团队来说，真正的挑战不是"用哪个模型"，而是：**如何把你们的系统、流程和基础设施，改造成能够容纳和放大 AI 输出的环境。** 这是一个组织和工程架构问题，不是一个提示词问题。
