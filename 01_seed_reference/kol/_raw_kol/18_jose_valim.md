---
type: kol_deep_dive
person: José Valim
organization: Dashbit (Elixir creator)
content_type: thought_leader_analysis
verification_status: verified
source_urls:
  - https://dashbit.co/blog/evolving-ai-era
key_concepts:
  - program_databases_over_lsp
  - runtime_observability_over_debuggers
  - guarantees_over_syntax
  - agent_first_toolchain
---

# José Valim — 语言层为 agent 重构：program databases over LSPs

> Elixir 创造者、Dashbit 创始人。2026-09-24 发表《Evolving programming languages in the AI era》——把"语言/工具该为谁设计"正面摆上台面：**语法与人体工学让位于保证（guarantees）**，IDE/LSP 让位于程序数据库，调试器让位于运行时可观测。文库内真·新面孔（台账零登记，2026-10-03 入册）。

---

> 📎 本文全部内容来源：见文末 "Source:" 节及文件 frontmatter 中的 `source_urls`。本文为单人深度分析，所有引用和判断均基于该人物的公开材料。建卡日 2026-10-03。

## 当前立场小结（2026-10-03 建卡）

1. **反"为 agent 设计语法"**："any new programming language that claims to be made 'for coding agents' and ultimately focuses on syntax is effectively **building around today's limitations**."
2. **IDE/LSP 讣告体**："The death of IDEs has been pronounced several times over the last two years. Once the obituary is finally published, **I don't expect LSPs to survive either.**"——主张 **program databases over LSPs**。
3. **运行时可观测取代调试器**："We should expose the runtime and state in our systems in ways that **agents can query and explore programmatically**."（runtime observability over debuggers）
4. **保证更强了**："there has never been a better time to provide **stronger guarantees** about our software."

---

## 传播链与库内关联

- 文章致谢名单含 **Ryan Lopopolo**（`09`，Harness Engineering 提出者）——新面孔与库内卡片的一手网络直接相连；随即被 Geoffrey Huntley（`16`）10-02 长文引用扩散。
- **与 Huntley 独立同向**：两人都在撤除"人类受众假设"——Valim 说人体工学/语法优先级让位于保证，Huntley 说 readable→explainable。这是 2026-08 后话语场最锋利的新对立轴（人类受众派 vs agent 受众派）的"基础设施派"代表。

---

## 关键引用汇总

> *"Program databases over LSPs."* — 2026-09-24

> *"We should expose the runtime and state in our systems in ways that agents can query and explore programmatically."*

> *"There has never been a better time to provide stronger guarantees about our software."*

---

**Source:** [Evolving programming languages in the AI era（2026-09-24，dashbit.co）](https://dashbit.co/blog/evolving-ai-era)
