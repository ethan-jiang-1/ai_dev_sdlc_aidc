# ISO 26262-8:2018 — Road vehicles — Functional safety — Part 8: Supporting Processes (Overview)

- source_url: `https://www.iso.org/standard/68390.html`（ISO 编目页，2026-04-17 检索时 403，可通过 `https://committee.iso.org/standard/68390.html` 访问元数据）+ `https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=...` 相关 IEEE 联合页（付费）+ 结构性重述 `https://piembsystech.com/iso-26262-part-8-supporting-processes/`（2026-04-17 抓取正文）
- source_type: `standard (international)`（原文全文受付费墙控制；本 Authoritative Copy 为\"结构与关键概念的二次重述\"）
- accessed_at: `2026-04-17`
- related_topic: `shared (04 future-trends, 05 integration-bdd 限制面；03 ears 的\"安全/合规\"落地；02 user-story 的\"不能覆盖什么\"反证)`
- trust_level: `official (ISO) for structure; secondary (PiEmbSysTech industry primer) for excerpt`
- tier: `C`（因原文付费墙、仅可用二次重述；属于\"限制 / 反证\"面的充分材料，不作为主张性结论唯一证据）
- why_it_matters: 安全关键领域对\"需求格式\"的约束是**非 agile、非 BDD 思路**最强的反证。ISO 26262 Part 8 **第 6 条**（Specification and Management of Safety Requirements）与 **第 11 条**（Confidence in the Use of Software Tools）直接说明：安全需求必须**双向可追溯、完整、一致、可验证、无歧义**，且\"需求管理工具\"本身要做 Tool Confidence Level（TCL）判定。这是本轮 Topic 02 / 05 选型矩阵\"User Story 不能单独承担安全关键系统需求\"的硬证据，也是 Topic 04 / 06 \"AI 生成需求 / agent 格式是否合规\"讨论的参照线。
- captured_excerpt: `yes`（基于二次重述的结构化摘要；原文逐字引用需 ISO 付费访问或 IEC Webstore 订阅）
- notes: 因 ISO 直站返回 403、全文付费，本页明确列出\"可信度层级\"与\"不可核对项\"。Topic 05 / 04 在 W1 deep-dive 时如需要逐条规则级证据，必须走 IEEE SA（同时发布联合标准的渠道）或机构订阅。

---

## 关键事实（结构与内容要点）

1. **标准基本信息**
   - 标题：`ISO 26262-8:2018 — Road vehicles — Functional safety — Part 8: Supporting processes`
   - 出版：**2018-12（Edition 2）**，60 页；ISO/TC 22/SC 32/WG 8 主持。
   - 适用范围：**乘用车及 ≤ 3500kg 卡车**的安全相关电子电气（E/E）系统（2018 版扩展到\"所有道路车辆\"）。

2. **Part 8 的性质**
   - Part 8 是 ISO 26262 \"支撑过程（supporting processes）\"卷：覆盖**跨阶段**的质量基础设施，与 Part 3（概念）/4（系统）/5（硬件）/6（软件）/7（生产）并行适用。
   - 本卷定位是\"让整个安全案例可追溯、可配置、可文档化、工具可信\"；没有 Part 8，Parts 3–7 的技术工作**即使做得技术正确也无法证明合规**。

3. **主要条款结构（Clause 5 – 14）**

   | Clause | 中文主题 | 本研究线关心的映射 |
   | --- | --- | --- |
   | **5** | 分布式开发接口（DIA, Development Interface Agreement） | 多组织协作场景下的\"需求所有权\"归属 |
   | **6** | **Specification and Management of Safety Requirements** | **本卷最相关**：安全需求的工程质量硬要求 |
   | 7 | Configuration Management | 需求/设计/测试作品的版本一致性 |
   | 8 | Change Management | 安全影响分析作为需求变更的强制步骤 |
   | 9 | Verification | 验证/评审独立性（不得自审） |
   | 10 | Documentation | 生命周期内可保留与可审计 |
   | **11** | **Confidence in the Use of Software Tools (TCL)** | 需求管理工具 / 生成工具 / agent 都受约束 |
   | 12 | Qualification of Software Components | 复用既有件的合规路径 |
   | 13 | Evaluation of Hardware Elements | 非按 26262 开发的硬件件复用 |
   | 14 | Proven in Use Argument | 以现场证据替代部分开发流程 |

4. **Clause 6（安全需求规约与管理）的核心硬要求**
   - **双向可追溯（bidirectional traceability）**：从\"Safety Goal → 功能安全需求（FSR）→ 技术安全需求（TSR）→ 硬件安全需求（HSR）→ 软件安全需求（SSR）\"向下，以及\"实现件 / 验证件\"向上，**每一个安全需求都必须**双向链回来源与实现与验证。
   - **质量四件套**：\"完整性（Completeness）、一致性（Consistency）、可验证性（Verifiability）、无歧义（Unambiguity）\"——每条需求必须可被客观测试或分析，**且只能被唯一解读**。
   - **工具支持**：业界做法是 IBM DOORS / Polarion / Jama Connect / Codebeamer 等专用 RM 工具。

   **研究线含义**：
   - Topic 05 选型矩阵里，"User Story + INVEST + 3C" 覆盖不到\"**无歧义 + 双向追溯 + 可验证到单元测试**\"这 4 条硬要求中的前 3 条；这是\"story 不适合作为安全关键需求主载体\"的**标准级证据**。
   - Topic 03（EARS）恰好对齐\"无歧义 + 可验证\"两条，因此在 automotive / aerospace 场景下被企业广泛采用（与 Topic 04 未来趋势里的 \"INCOSE + EARS-in-compliance\"产业事实一致）。
   - Topic 06（agent 格式）：**CLAUDE.md / AGENTS.md 目前都不内建双向追溯**——若要在合规项目里作为需求主载体，必须外挂 RM 工具。这是\"agent 格式 ≠ RM 工具\"的硬边界。

5. **Clause 11（工具置信度 TCL）对\"AI 需求生成工具\"的含义**
   - TCL 判定路径：**TI（Tool Impact）× TD（Tool Error Detection）** → TCL1/2/3。
   - 需求管理工具典型判定：`TI = TI2`（工具故障可能破坏 traceability 数据）。
   - **如果 AI agent（Cursor / Claude Code / Copilot）被用于\"生成或改写安全需求\"**：
     - 直接落 `TI = TI2`；
     - TD 取决于下游是否有\"独立人类/工具双重检查\"；若无 → `TD3` → `TCL3`，必须采用 Method 1c（validation）或 Method 1d（按安全标准开发）。
     - **现状**：2026-Q1 的 Cursor / Claude Code / Codex 官方**均未**提供 TCL2/3 等级的 Tool Qualification Support Kit；因此**在 ASIL-B 以上安全需求工作流中，这些 agent 不能作为需求规约的唯一工具**。
   - **研究线含义**：这是 Topic 06 \"AI 时代 agent 格式是否替代传统需求\"**最重要的反方证据**。

6. **Clause 8 的变更管理 + Safety Impact Analysis**
   - 任何涉及安全需求的变更都必须走\"安全影响分析 → 分类 → 批准 → 可追溯地实施 → 验证 → 更新全部受影响工件\"的链路。
   - **研究线含义**：\"story 的 Negotiable\"（INVEST-N）在安全需求上被**显式禁用**——这是 Fowler / Cohn / Patton 的 agile 文献**完全没有覆盖**的合规缺口。Topic 05 必须以此区别 story 与 safety requirement 的可协商度。

---

## 原文直引 / 结构性引用

以下为二次重述的关键论断（PiEmbSysTech 2025 综述，原文付费无法逐字核对；Topic 05 / 04 W1 deep-dive 若需成为主张性结论证据，应以 IEEE Xplore / ISO 付费全文为准）：

> "Without Part 8, the safety case falls apart. Requirements cannot be traced if there is no requirements management process. Design changes cannot be controlled if there is no change management process. Work products cannot be trusted if there is no configuration management process. Test results cannot be relied upon if the testing tools have not been qualified."

> "Requirements must be checked for **completeness** … **consistency** … **verifiability** … and **unambiguity** — every requirement has a single, clear interpretation."

> "A verification review of a work product **shall be performed by a person or persons different from the author(s)** of the work product."

> "The fundamental question [of tool qualification] is: 'If this tool malfunctions, could it introduce an error into the safety-related product or fail to detect an error?'"

## 桥接

- → `00-shared-incose-gtwr-v4-summary.md`：GtWR 的 15 特征与 Clause 6 的\"4 条硬要求\"有精确对应关系（unambiguous / verifiable / complete / consistent），这是两份材料**可互为主锚**的原因。
- → `00-shared-iso-iec-ieee-29148-2018.md`：29148 是\"需求工程通用过程标准\"，ISO 26262-8 是\"汽车功能安全的特化应用层\"；两者在合成时应展示为\"通用 → 行业特化\"的层级关系。
- → `00-shared-mavin-2009-ears-re09.md`：EARS 是\"符合 29148 / 26262-8 Clause 6 硬要求\"的一种**语法层落地**。
- → `00-shared-cohn-user-stories-primer.md` / `00-shared-patton-story-mapping-primer.md`：两份 agile story 方法论**不对\"合规\"建模**，这恰好构成对 \"story 不能作为安全关键需求主载体\"判决的正负对比组。
- → `00-shared-claude-code-official.md` / `00-shared-codex-agents-md-spec.md`：agent 格式在安全关键场景下必须外挂 RM 工具；若未外挂，则被 Clause 11 的 TCL 机制直接拉到 TCL3 的 \"不能作为唯一工具\"层级。

## 限制

- 本 Authoritative Copy 的\"引用层\"**来自 PiEmbSysTech 综述**（2025 年工业博客），**不是对 ISO 原文的逐字复核**；正式主张性结论阶段应回到 IEEE Xplore 联合版或 ISO 付费全文。
- ISO 26262 Part 8 仅约束\"道路车辆\"；对应的航空（DO-178C/DO-254）、铁路（EN 50128/50129）、医疗（IEC 62304）、工业（IEC 61508）有各自平行体系；Topic 05 限制面 W1 时可按需补一条 IEC 61508 作为\"通用功能安全根标准\"锚点。
- 本卷不涉及\"AI/LLM 在安全关键工具链中的定性\"；这部分需看 **ISO/PAS 8800 / ISO/TR 4804 / EASA AI CP**（本轮视时间裕度决定是否进入 Wave 1）。
