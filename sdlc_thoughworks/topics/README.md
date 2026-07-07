# Deep Research: AI-Native SDLC (基于 ThoughtWorks 研讨会的战略解构)

## 1. 来源与立项背景 (Origin & Background)

本研究计划的所有初始输入与核心概念，均源于 2026 年初 ThoughtWorks 举办的闭门研讨会报告——《软件工程的未来 (The future of software engineering — Retreat Findings)》。该报告汇集了大型科技公司资深工程专家的内部共识，指出 AI 介入后，传统人力时代的软件工程正在发生断裂（Fault lines）。但原报告主要停留在“行业现象观察”和“散点式问题抛出”层面。

**本项目的核心目标**：将这些散落的“断界与痛点”，转化为具有极强落地性、商业指导和系统再造指导意义的 **“Deep Research（深度研究）” 和 “战略蓝图”**。

## 2. 为什么我们要“劈开”它？ (The Rationale for the Breakdown)

如果只有 8-9 个章节顺着读，它永远只是一篇“行业观察连载”。从**软件研发行业宏观与技术业务落地**的视角来看，构建一个面向未来的 AI-Native 研发与交付体系，必须要有 MECE（相互独立、完全穷尽）的架构支柱体系。

我们将这个“未来图景”劈开成为 **4 个核心研究切片**，根本原因在于我们需要重构现代软件研发企业的四大底盘：
* **Topic 01 工程范式 (Process / Paradigm)** 解决的是：**“如何防备产品质量崩塌？”** —— 聚焦在规范与产出方式上的流程再造（TDD、状态机、规格审查）。
* **Topic 02 组织协同 (People / Organization)** 解决的是：**“人机混编后，人该干嘛？”** —— 聚焦康威定律、管理层的角色演化（PM、Staff工程师、中间循环）。
* **Topic 03 底层基建 (Infrastructure)** 解决的是：**“支撑硅基员工干活的地基在哪？”** —— 聚焦知识图谱、语义层和 Agent OS。
* **Topic 04 安全治理 (Risk / Governance)** 解决的是：**“如何不让公司大盘被 AI 炸毁？”** —— 聚焦隔离机制、灾难底线与越权控制。

这 4 个切片即代表了企业架构里的**流程、人、技术与风险**。只有先拆分成独立的子系统去做深钻，才能摆脱泛泛而谈，触及真正的痛点（Pain Points）与解决方案（Solutions）。

## 3. 未来的“合成引擎”：我们最终要产出什么？ (The Synthesis Strategy)

当我们针对四个 Topic 分别完成 Deep Research 后，所有的弹药和研究洞察需要合体。它们的合成逻辑及最终形态如下：

### 最终交付物形态预判
* **对内**：一份完整的、指导新一代产研体系变革的 **“AI-Native 软件工程新常态 (Next-Gen SDLC) 白皮书/标准操作手册 (SOP)”**。
* **对外（技术商业化输出）**：一份 **“针对企业 IT 开发与治理体系演进的 AI-Native 重构方案与前瞻技术白皮书”**。

### 合成路径推演
四个模块在合成时将像搭积木一样形成一个多层级框架模型（Stack Model）：
1. **[底座层 (Foundation)] -> Topic 04 (安全) & Topic 03 (基建)**：这是必须要最先解决的能力网与防护网。它产出了智能体操作系统、知识图谱以及动态红蓝对抗系统。
2. **[执行层 (Orchestration)] -> Topic 01 (工程范式)**：运行在安全与基建层之上的，是具体到日常开发的流水线变更，产出 AI-TDD、强制类型化约束等。
3. **[交互层 (Governance & Synergy)] -> Topic 02 (组织协同)**：悬浮在整个执行层之上的，是由“中间循环工程师”和“新式 PM”构成的调度层，解决业务对齐和最终责任归属。

**总结**：我们现在的“劈开”，是为了深挖垂直水井；未来的“合成”，是在四个井底同时出水后，浇灌出一盘完整的“AI-Native 重大范式重构”的战略棋局。

---

## 4. 本轮 Deep Research 执行入口

本目录现在同时作为本轮研究的 `living output surface`。原始 topic seed 保留在当前目录，后续新增证据、机制理解、趋势判断与当前判断会回填到各 topic 文件的固定章节中。

### 30 秒读取路径

- 计划文件：`/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.md`
- 执行状态：`/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.status.md`
- 执行队列：`/Users/bowhead/ai_dev_sdlc/sdlc_tw/plan/ai_native_sdlc_deep_research_round1.queue.md`
- 本地 reference：`/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference`
- reference 索引：`/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_reference/_INDEX.md`
- 本地 artifacts：`/Users/bowhead/ai_dev_sdlc/sdlc_tw/topics/_artifacts`

### 当前研究线

- `01_engineering_paradigm.md`：工程纪律、规格、TDD、约束与小批量交付。
- `02_organizational_synergy.md`：中间循环、人机混编、组织协同与 AgentEx。
- `03_agent_native_infrastructure.md`：Agent OS、工作账本、语义层、知识图谱与多智能体基建。
- `04_security_and_governance.md`：Agent 权限、安全治理、爆炸半径、审计与对抗评测。
