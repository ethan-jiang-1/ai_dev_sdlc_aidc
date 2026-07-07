# Topic 4 — 趋势、证据与未来揣测（需求表达 × AI × 工具 × 组织）

> 本文件面向 **独立 Deep Research** 使用：嵌入原文 §6、§8.3 的现状与实证数据，并在第 4 节单独提出 **6 条可证伪的前瞻维度**（原文未覆盖、真正属于"揣测"的部分）。

## 研究问题（Deep Research 入口）

1. 将需求视为 **LLM 的"初始条件 / 提示词"** 时，松散 User Story 与结构化规范各自导致何种失效模式（主路径偏好、异常流幻觉、歧义放大）？
2. **结构化提示**（含 EARS 类）与 JSON/YAML/受控自然语言在实证研究中如何量化影响解析质量与代码生成？哪些结论可迁移？
3. **sMBSAP vs 纯 Scrum** 类研究（原文 [37]）中 CR/DD/DL/Velocity 指标的**可重复性**与**外部效度**如何评估？
4. **需求质量自动化**（QVscribe、Visure、INCOSE 规则、Azure Copilot + INVEST）声称的降本比例中，哪些有公开证据、哪些是厂商叙事？
5. **"User Story 已死、Prompt 永生"**（原文 [29]）的强版本与弱版本分别需要什么证据支撑？
6. **未来 3–5 年** 需求表达范式可能的演化路径有哪些（见第 4 节 6 条前瞻维度）？

## 原文锚点（现状部分，供回溯）

| 章节 | 主题 |
|------|------|
| §6.1 | LLM/AI 工具；Prompt = 系统初始条件；User Story 留白 vs 模型缺常识 |
| §6.2 | EARS 作结构化 Prompt；与 AST / 控制流 / 异常分支的同构；量化实证引用 [33][36] |
| §6.3 | sMBSAP 准实验：CR 0.94 vs 0.81；DD 0.63 vs 0.91；DL 0.15 vs 0.20；Velocity 31.8 vs 26.8（单篇 MDPI [37]）|
| §8.3 | QVscribe、Visure ALM；实时 INCOSE/EARS 扫描；Azure Copilot + INVEST；审查时间削减 50–75%（厂商 [48]）|
| §9 结语 | 融合路径：Story 北极星 + EARS 指令网 + Gherkin 防护网 |

> **重要**：上述数据的证据强度需与 [claims-audit.md](claims-audit.md) 对照阅读，避免在 DR 时把"单篇文章 / 厂商白皮书"当作行业共识。

---

## 1. 范式转移：需求 → 提示词（§6.1 压缩）

- **传统流水线**：Idea → User Story → 人类沟通 → 代码。
- **AI 时代流水线**：
  - 上游：PM 用无代码 / Vibe Coding 做初步验证。
  - 中段：**Prompt Porting** 把意图输入给 AI 虚拟开发者。
  - 下游：AI 生成工程化代码 + 测试。
- **混沌类比**：Prompt 是 LLM 输出的**初始条件**，微小扰动放大为巨大差异；模糊 User Story 的"留白"原本是**对话的邀请**，在 LLM 面前变成**幻觉的温床**。

## 2. 为什么 EARS 是高级 Prompt 框架（§6.2 压缩）

- **控制流同构**：`While` → `while`；`When` → 事件处理器 / `case`；`If...then` → `if/else`；`Where` → feature flag / DI。
- **异常前置**：EARS Unwanted 模式强制在 Prompt 输入前就定义失效路径与兜底，正中 LLM "只生成 Happy Path" 的痛点。
- **原文引用的量化提升**（单一文献来源，**见 claims-audit.md**）：
  - ChatGPT 需求解析准确性 **+59.17%**（[33]）。
  - Gemini **+26.07%**（[33]）。
  - 结构化输入可驱动需求→类图→单测的连续链条（[36]）。

## 3. 质量自动化工具链现状（§8.3 压缩）

- **EARS / INCOSE 侧**：QVscribe、Visure Requirements ALM、Inflectra.ai、specinnovations → Word/Excel/ALM 插件；实时扫描模糊形容词、被动语态、>3 前置条件；输出"需求质量评分"。
- **User Story 侧**：Azure DevOps Copilot、Copilot4DevOps → 实时比对 INVEST、检测缺失 AC、预测变更涟漪风险。
- **声称效益**（**厂商来源，需审查**）：评审与返工时间 −50%–75%（[48]）；单项目节省 $150k（[50]）。

---

## 4. 前瞻维度：6 条可证伪的揣测（原文未覆盖）

> 下列揣测是 **本 Topic 的核心原创贡献**。每条给出假设、可观察信号、可证伪手法，便于 Deep Research 时分别追踪。

### 4.1 规约即代码（Spec-as-Code）

- **假设**：未来 3–5 年，需求文件会像代码一样进入 Git、走 PR review、接 lint / CI；EARS 语法将有对应的 `requirements-lint` 工具链，类似 ESLint。
- **早期信号**：OpenSpec、Kiro Spec Workflow、Linear Spec、Notion AI Spec、Anthropic/OpenAI 近期 spec-first 讨论；Cursor / Claude Code 中出现的 `.md` 规约驱动工作流。
- **可证伪**：若 5 年后主流 SaaS 工具（Jira、Linear、Shortcut）仍将需求锁在富文本 DB 里而非 Git，本揣测弱化。
- **DR 提问**：`spec-as-code` vs `docs-as-code` 的成熟度曲线？需求 diff 的语义比较算法？

### 4.2 多模态需求（Multimodal Requirements）

- **假设**：Story/EARS 的纯文本形式会被 **草图 + 视频 + 语音 + 结构化句式** 混合替代。多模态 LLM 直接从 Figma + 白板照片 + 一段语音讲解生成 EARS + Gherkin。
- **早期信号**：Figma Make、v0、Magic Patterns、Claude/GPT 的视觉输入；Atlassian Rovo 从会议转录生成 Story。
- **可证伪**：若三年内多模态输入仍无法在**合规审计**链路被认可（如 FDA、ISO 26262），则仅限消费级场景。
- **DR 提问**：多模态需求的**可追溯性**如何形式化？审计方是否接受"从图生成的 EARS"作为原始凭证？

### 4.3 Agent 反向修订 Spec（Spec ↔ Agent 闭环）

- **假设**：当 Coding Agent 发现代码实现与 EARS 冲突或覆盖不全时，会**自动提交 Spec 修订 PR**，由人类 review。需求不再是单向的"人写 → 机读"，而是双向闭环。
- **早期信号**：GitHub Copilot Workspace、Cursor Composer 的"任务→计划→实现"流；部分 Agent 框架（如 Devin、SWE-agent）已尝试"提议规格变更"。
- **可证伪**：若 Agent 长期只能改代码不能改 Spec，或改了也无组织流程认可，该揣测失效。
- **DR 提问**：Spec 的**可机器写回**形式？谁对 Agent-generated spec 负法律 / 合规责任？

### 4.4 向量化 / 图化需求（Embedding / Graph Requirements）

- **假设**：EARS / Story 最终可能不再以"文本结构"为主载体，而是以 **向量 + 知识图谱** 形式存在——每条需求成为一个 node，触发 / 前置 / 响应成为 edge，查询由语义相似而非关键字完成。
- **早期信号**：Jama Connect 的 impact analysis 已走图谱方向；近期 RAG over specs、"requirements knowledge graph" 的学术讨论。
- **可证伪**：若 5 年后监管仍坚持文本形式的审计凭证（"向量不可读"问题），则只作辅助索引，不替代文本。
- **DR 提问**：需求图谱的**标准化 schema**？如何在向量层做 INCOSE 合规检查？

### 4.5 监管与可追溯性（Regulatory Traceability for AI-authored Specs）

- **假设**：EU AI Act、美国 NIST AI RMF、ISO 42001 等会逐步要求 "AI 生成的需求 / 代码" 必须有**可追溯的结构化规约层**；EARS 成为"AI 编程可审计"的事实性胶水语言。
- **早期信号**：EU AI Act 高风险系统条款；NIST AI RMF 1.0 对文档化的强调；航空 / 医疗领域对 LLM 工具资质认证（DO-178C-like）的讨论。
- **可证伪**：若监管绕过"结构化规约"直接要求"模型 + 测试"组合，则 EARS 只是一种选项而非必需。
- **DR 提问**：哪些行业标准已明文提及 EARS / INCOSE GTWR？与 ISO/IEC 29148 的关系？

### 4.6 IDE 原生的需求原语（Requirements as IDE Primitive）

- **假设**：需求会像 `@file` `@symbol` 一样成为 IDE 的**一等原语**。Cursor / Zed / VS Code 未来可能出现 `@requirement` `@spec` 引用，使 Agent 在生成代码时**强制引用**某条 EARS；离线的 Word / ALM 将被 IDE 内嵌的轻量 Spec 编辑器取代。
- **早期信号**：Cursor 的 Rules / `.cursor/skills/`、Kiro Spec、Claude Code 的 `CLAUDE.md`、各种 `AGENTS.md` 约定。
- **可证伪**：若两年后主流 IDE 仍没有一等的 spec 原语，只停留在文件引用层面，该揣测弱化。
- **DR 提问**：spec 原语的接口设计（链接、锚点、diff、测试绑定）？IDE × ALM 的集成路径？

#### 本轮回填（2026-04-18）

- **近因观察**：IDE 原生需求原语已经不只是揣测。Kiro 已把 `Requirements / Design / Tasks` 作为 IDE 内建 Specs 工作流，并把 `User stories with acceptance criteria in EARS notation` 放进 requirements phase；见 [`_reference/04-future-trends-kiro-spec-workflow-official.md`](_reference/04-future-trends-kiro-spec-workflow-official.md)。
- **并行信号**：GitHub Spec Kit 以 `constitution.md / spec.md / plan.md / tasks.md` 建立 feature-level spec workflow，说明需求、计划、任务正在被显式文件化和版本化；见 [`_reference/04-future-trends-github-spec-kit-official.md`](_reference/04-future-trends-github-spec-kit-official.md)。
- **限制面**：Thoughtworks Technology Radar Vol.33 已把 `spec-driven development` 放入 `Assess`，但同时指出 workflow 仍可能 elaborate / opinionated / hard to review；见 [`_reference/04-future-trends-thoughtworks-spec-driven-development-signal.md`](_reference/04-future-trends-thoughtworks-spec-driven-development-signal.md)。
- **当前判断**：本维度从“轻揣测”升级为“早期已发生趋势”。但更准确的表述不是“所有需求都会进 IDE”，而是：team/repo 级上下文、scoped rules、feature-level specs 三层正在被 coding agent 工具链显式分离；见 [`_artifacts/W2-cross-topic-synthesis.md`](_artifacts/W2-cross-topic-synthesis.md) 和 [`_artifacts/W2-selection-matrix-v2.md`](_artifacts/W2-selection-matrix-v2.md)。

---

## 5. 待证伪与延伸检索

- 逐项核对 [33][36][37] 的样本量、基线设计与可推广域（详见 [claims-audit.md](claims-audit.md)）。
- METR 2025 开发者生产力研究（[28]）**不等于**需求格式的因果链；需分开讨论。
- 监管 / 安全语境下 LLM 生成需求与代码的治理框架（EU AI Act、NIST AI RMF）。
- **独立第三方**对 QVscribe / Visure / Inflectra 的评测（非厂商自述）。

## 6. 本 Topic 参考文献（摘自原文编号）

见 [references-by-topic.md](references-by-topic.md) 中 **Topic 4**；完整条目见 [references-full.md](references-full.md)。

**编号快查：** 15, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 45, 48, 49, 50, 51, 52

## 7. Deep Research 查询种子

**英文**：

1. `"spec-as-code" requirements git PR review lint tooling 2025..2026`
2. `multimodal requirements engineering Figma sketch video LLM extraction`
3. `coding agent "spec revision" pull request Cursor Composer GitHub Copilot Workspace`
4. `requirements knowledge graph embedding semantic search Jama impact analysis`
5. `EU AI Act NIST AI RMF traceability structured requirements specification`
6. `IDE primitive "@requirement" "@spec" Cursor Zed VSCode native integration`
7. `sMBSAP "agile model-based" defect density replication study external validity`
8. `"QVscribe" OR "Visure" independent third-party evaluation INCOSE automation`

**中文**：

1. `规约即代码 Spec-as-Code 需求版本化 Git 实践`
2. `多模态 需求工程 Figma 草图 视频 LLM 提取`
3. `Coding Agent 自动修订 规格 Spec PR 回环 研究`
4. `需求知识图谱 向量化 嵌入 Jama 影响分析`
5. `欧盟 AI 法案 NIST AI RMF 可追溯性 结构化规约`
6. `IDE 需求 原语 Cursor Rules Kiro Spec AGENTS.md`

## 8. 交叉引用

- 范式与互补叙事：← [topic-01-re-landscape-and-paradigm-map.md](topic-01-re-landscape-and-paradigm-map.md)、[topic-05-integration-bdd-selection.md](topic-05-integration-bdd-selection.md)
- User Story / EARS 教程：← [topic-02-user-story-tutorial.md](topic-02-user-story-tutorial.md)、[topic-03-ears-tutorial.md](topic-03-ears-tutorial.md)
- **高流量断言可信度与本 Topic 数据来源**：→ [claims-audit.md](claims-audit.md)（**必读**）

## 9. 历史摘要（保留，不修改）

- 本主题的历史正文保留在 §1–§8：它保留了需求→提示词的范式转移、EARS 作为高级 Prompt 的论证、质量自动化工具链、六条前瞻维度与本轮回填过的 IDE-native requirements primitive 观察。

## 10. 本轮新增证据

- spec-driven / IDE-native workflow 已从单点信号升级为成组信号：[`_reference/04-future-trends-github-spec-kit-official.md`](_reference/04-future-trends-github-spec-kit-official.md)、[`_reference/04-future-trends-kiro-spec-workflow-official.md`](_reference/04-future-trends-kiro-spec-workflow-official.md)、[`_reference/04-future-trends-thoughtworks-spec-driven-development-signal.md`](_reference/04-future-trends-thoughtworks-spec-driven-development-signal.md)。
- governance / traceability 主锚已经落地：[`_reference/04-future-trends-ai-governance-nist-eu-ai-act.md`](_reference/04-future-trends-ai-governance-nist-eu-ai-act.md)。
- 多模态轴已经从 existence signal 走到 workflow + hosted outcome + independent study + enterprise benchmark + adoption census + named deployment case：
  - [`_reference/04-future-trends-figma-make-multimodal-signal.md`](_reference/04-future-trends-figma-make-multimodal-signal.md)
  - [`_reference/04-future-trends-vercel-v0-multimodal-prd-workflow.md`](_reference/04-future-trends-vercel-v0-multimodal-prd-workflow.md)
  - [`_reference/04-future-trends-vercel-v0-stripe-outcomes.md`](_reference/04-future-trends-vercel-v0-stripe-outcomes.md)
  - [`_reference/04-future-trends-personagram-multimodal-design-study.md`](_reference/04-future-trends-personagram-multimodal-design-study.md)
  - [`_reference/04-future-trends-ai4ui-enterprise-pixel-to-production.md`](_reference/04-future-trends-ai4ui-enterprise-pixel-to-production.md)
  - [`_reference/04-future-trends-state-of-prototyping-2026.md`](_reference/04-future-trends-state-of-prototyping-2026.md)
  - [`_reference/04-future-trends-figma-make-findable-production-case.md`](_reference/04-future-trends-figma-make-findable-production-case.md)
- graph / knowledge-graph 轴已经从 substrate 升到 RE / enterprise / product-development：
  - [`_reference/04-future-trends-w3c-shacl-graph-constraints.md`](_reference/04-future-trends-w3c-shacl-graph-constraints.md)
  - [`_reference/04-future-trends-kg-empire-re-knowledge-graph.md`](_reference/04-future-trends-kg-empire-re-knowledge-graph.md)
  - [`_reference/04-future-trends-ibm-enterprise-requirements-kg.md`](_reference/04-future-trends-ibm-enterprise-requirements-kg.md)
  - [`_reference/04-future-trends-bmw-virtual-product-development-kg.md`](_reference/04-future-trends-bmw-virtual-product-development-kg.md)

## 11. 本轮新增机制理解

- Topic 04 现在最重要的机制升级，是把“前瞻揣测”拆成不同证据层级：
  - workflow existence
  - productized workflow
  - hosted outcome
  - independent empirical outcome
  - benchmark
  - adoption census
  - named deployment case
- 这使得本主题不再只是“趋势列表”，而是可以分辨哪些维度只是弱信号，哪些已经出现工具链、研究和案例的多点交叉支撑。
- 同时，Topic 04 与 Topic 06 的关系也更清楚：spec-driven development、IDE-native specs、agent workflow layering 本质上共享同一条“feature-level spec as artifact graph”趋势线。

## 12. 本轮新增趋势与难点

- 多模态与 design-to-code 不再是单厂商存在性信号，但 production outcome 仍主要来自 vendor-hosted case 或 self-reported adoption；独立 production verification 依然缺失。
- graph / knowledge-graph 轴已经有更广泛的底座与案例，但仍不足以写成“成为行业主流载体”。
- spec-driven development 的最大难点已经不只是“有没有工具”，而是 elaborate / opinionated / hard-to-review 的现实成本。

## 13. 当前判断（本轮综合后）

- Topic 04 现在可以稳写成：
  - `spec-driven-workflow-supported`
  - `ide-native-spec-signal-supported`
  - `governance-traceability-pressure-supported`
  - `multimodal-workflow-supported`
  - `multimodal-hosted-outcome-supported`
  - `independent-design-study-outcome-supported`
  - `enterprise-benchmark-supported`
  - `independent-adoption-census-supported`
  - `named-real-deployment-case-supported`
  - `graph-constraint-substrate-supported`
  - `requirements-specific-graph-supported`
  - `enterprise-requirements-kg-supported`
  - `product-development-graph-case-supported`
  - `independent-production-outcome-verification-pending`
- 因而本主题的当前判断应从“轻揣测”升级为“多条趋势已发生，但采用成熟度与独立 outcome verification 仍需谨慎”。
