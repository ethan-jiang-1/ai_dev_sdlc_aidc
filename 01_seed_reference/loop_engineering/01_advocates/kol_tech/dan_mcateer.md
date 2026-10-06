

### 推-18 · Dan McAteer（Attention Heads 作者，Latent Space 客座）《The Evolution of the Agent Harness》（2026-08-22）

- URL：https://www.latent.space/p/attention-interface （curl 实取全文）
- 身份：AI 写作者/agentic engineer（③弱——**仅作专栏层样本，但机制综合价值高**）。
- **挂钩**：循环结构（harness 演化三段论）＋外层调度（注意力接口）。
- 逐字摘录：
  - "An agent harness is everything besides the model weights that makes the agent work. The environment, tools, context and guardrails that surround the model. Without the harness the model is a brain in a vat."
  - "Harness-Bench ran the same model over the same 106 tasks in different harnesses, and scores ranged from 52.4 to 76.2: a 23.8-point spread with zero change to the model."（**同模型跨 harness 24 分差**——循环结构权重的量化证据。）
  - "Adding only retained reasoning and compaction, GPT-5.6 Sol's ARC-AGI-3 score tripled from 13.3% to 38.3%."
  - "This, then, is the loop of model / harness evolution: **train -> absorb -> shed -> repeat**. The model climbs to the next thing it can't do yet."（harness 演化的收口公式。）
  - "The measure of the pace of agent harness evolution is how much of the harness you get to delete, while retaining the same capability level."（**"删多少 harness"＝harness 进步的度量**——引用 Thariq "deleted 80% of Claude Code's system prompt"。）
  - "I predict that within a year, every company building agentic AI will ship a human attention policy surface in the way that every agentic AI company shipped AGENTS.md… The attention-interface will tell the agent how to work with you. It will govern when it's allowed to interrupt you, when it should keep working, which decisions it can make alone."（**"注意力接口"＝人审位的声明式化**——外层调度的新原语预测。）
- **最小主张**：模型/harness 双曲线从 bolt-on 到 co-training 到吸收-删除；harness 的终局是"人注意力策略面"——可中断性、可独自决策域须显式声明。
- **派别适配**：**推动票（结构综合）**。

**（第六轮挖掘（2026-10-06）：播客层第二轮）**
