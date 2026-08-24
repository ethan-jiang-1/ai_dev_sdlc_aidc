# Deep Research 主题包：User Story × EARS 长文拆分

本目录将 [User Story vs EARS 深度比较.md](../raw_dr/User%20Story%20vs%20EARS%20深度比较.md) 消化为 **6 个可独立做深度调研的主题** + 1 份**证据强度审查**，每个主题自带研究问题、原文锚点、嵌入式摘录、教程模块、待补方向、参考文献子集与 DR 查询种子。

本轮进入 **一轮 Deep Research 执行态**：

- 计划：[`../plan/dr-round-1.plan.md`](../plan/dr-round-1.plan.md)
- 执行状态：[`../plan/dr-round-1.status.md`](../plan/dr-round-1.status.md)
- 执行队列：[`../plan/dr-round-1.queue.md`](../plan/dr-round-1.queue.md)
- 权威副本层：[`_reference/`](_reference/) · 导航入口 [`_reference/_INDEX.md`](_reference/_INDEX.md)
- 综合产物层：[`_artifacts/`](_artifacts/)

> **🚩 如果你是接手这轮 DR 的 Agent / 新会话**：先读 [`../plan/dr-round-1.status.md` 顶部的 Resume Protocol](../plan/dr-round-1.status.md#-resume-protocol接手此轮-dr-的-agent-第一眼读这里)（5 步，不可跳序），再按 [`../plan/dr-round-1.queue.md`](../plan/dr-round-1.queue.md) `Active Queue.current_task` 开工。当前 gate = `wave0_complete`，下一刀 = 开启 Wave 1 Topic 03 EARS 分支。

## 结构决策（B 方案 + Topic 06 扩展已落地）

采用 **6 个 Topic + 1 份 Claims Audit**：

- **Topic 5 独立**：容纳原文 §4 平行案例、§7 EARS↔Gherkin 桥梁、§9 九维矩阵等无法干净归入单范式教程的内容。
- **Topic 6 新增**：从 Topic 4 §4.6 "IDE 原生的需求原语" 剥离出的独立研究线，面向最强 coding agent / harness 的需求格式实证与选型决策（2024Q3–2026Q1 时间窗）。
- **Claims Audit 独立**：对原文 10 条高流量断言做证据强度分级，防止 DR 报告继承原文立场偏差。

与最初研究提纲相比，本次 B 方案迭代增补：

| 增补项 | 位置 |
|-------|------|
| EARS 五模式 + 复合的**完整中英双语语法表** | Topic 3 §3 |
| 手机银行 / AEB 两条 **worked examples 全文** | Topic 3 §4 |
| User Story / EARS 各 **2 组坏例 → 好例** 重构对照 | Topic 2 §5、Topic 3 §5 |
| **端到端三轨示例**（Story + EARS + Gherkin）| Topic 5 §2.1 |
| **§9 九维对比矩阵**完整复刻 | Topic 5 §3 |
| **6 条可证伪的前瞻维度**（原文未覆盖）| Topic 4 §4 |
| **证据强度审查表**（10 条断言 × 6 级分级）| claims-audit.md |
| **每个 Topic 的 DR 查询种子**（中英文各 3–5 条）| 各 Topic 末尾 |

## 文件一览

| 文件 | 作用 | 新增/升级 |
|------|------|----------|
| [topic-01-re-landscape-and-paradigm-map.md](topic-01-re-landscape-and-paradigm-map.md) | RE 背景与范式地图，12 行范式速查表 | 升级 |
| [topic-02-user-story-tutorial.md](topic-02-user-story-tutorial.md) | User Story 教程向（历史、模板、变体、INVEST、2 组坏→好）| 升级 |
| [topic-03-ears-tutorial.md](topic-03-ears-tutorial.md) | EARS 教程向（完整模式表、2 条 worked example、2 组坏→好、边界、INCOSE）| 升级 |
| [topic-04-future-trends-and-evidence.md](topic-04-future-trends-and-evidence.md) | 现状 + **5 条前瞻维度**（spec-as-code / 多模态 / Agent 反修 / embedding / 监管）—— 原 §4.6 IDE 原语剥离为 Topic 06 | 升级 |
| [topic-05-integration-bdd-selection.md](topic-05-integration-bdd-selection.md) | 三轨分层、§9 矩阵、端到端示例、Playbook | 升级 |
| [topic-06-agent-format.md](topic-06-agent-format.md) | **最强 coding agent / harness 的需求格式实证与选型**（Cursor / Claude Code / Codex / Kiro / Spec Kit / OpenSpec / Amp / Aider / Continue / Cline；2024Q3–2026Q1 时间窗；exploration + exploitation） | **新增** |
| [claims-audit.md](claims-audit.md) | **原文 10 条断言的证据强度标注** | 新增 |
| [references-full.md](references-full.md) | 原文完整 52 条 Works cited（权威副本） | — |
| [references-by-topic.md](references-by-topic.md) | 各 Topic 文献编号索引 | — |
| [_reference/](_reference/) | 本轮新增的权威副本层 | **新增（一轮）** |
| [_artifacts/](_artifacts/) | 本轮新增的综合产物层 | **新增（一轮）** |

## 阅读顺序建议

1. **先读** [claims-audit.md](claims-audit.md)：建立对原文立场与数据可信度的校准，再进入具体 Topic。
2. [topic-01](topic-01-re-landscape-and-paradigm-map.md) 建地图。
3. [topic-02](topic-02-user-story-tutorial.md) 与 [topic-03](topic-03-ears-tutorial.md) 可并行。
4. [topic-05](topic-05-integration-bdd-selection.md) 合流与选型。
5. [topic-04](topic-04-future-trends-and-evidence.md) 趋势与前瞻揣测收尾。
6. [topic-06](topic-06-agent-format.md) 给出面向 coding agent / harness 的选型建议（本轮唯一硬决策输出）。

## 使用方法（给 DR Agent / 外部工具）

- 单文件自足：每个 Topic 已嵌入必要的原文要点，**可单独丢给 Deep Research 工具**而无需附原文。
- 查询即用：每个 Topic 的"DR 查询种子"节可直接复制粘贴到 Perplexity / Gemini / ChatGPT。
- 立场校准：遇到精确数字或绝对化结论时，回查 `claims-audit.md` 对应条目。
