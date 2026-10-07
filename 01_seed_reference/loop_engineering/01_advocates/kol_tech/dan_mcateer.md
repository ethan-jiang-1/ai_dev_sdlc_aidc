---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# dan_mcateer — loop engineering 证据轨迹（2026-06 后，时间正序）

> **背景**：Dan McAteer（Daniel McAteer）——心理学出身、认知科学方向的 agentic engineer；曾在 Amp 与 Moveworks 任职（AI 工具一线）；现为 Substack 刊物《Attention Heads》作者（AI × 注意力/心智的周更写作）。（履历核：attentionheads.blog/about，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——待补挖。
### Dan McAteer（Attention Heads 作者，Latent Space 客座）《The Evolution of the Agent Harness》（2026-08-22）

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


---

# 增量补挖（2026-10-07 goal 第一批·单点→稳定复核）

> 判定：**单点解除 → 稳定（推动）**——08-22 harness 演化论 → 09 月 Astra 系列同向；付费墙限制多文全文（诚实标注）。

## 自站 Attention Heads 窗口内条目（存档页 fetch 200）

- 09-07《Six Ways to Give GPT-6 Astra More Agency》（免费段实取）："I've only been using Astra since Friday… but I already have more trust than any previous model that it can get the job done, whatever task I give it."；"The limits feel increasingly like my own imagination and how clearly I can specify the goal I want to accomplish."
- 其 context-audit prompt（页面直引）："The goal is not to make your agent less constrained. It is to make the constraints legible, current, and proportional."（**约束的"清晰、现行、成比例"**——推动派语境下的约束治理语言。）
- 其余窗口内条目（标题级）：10-01 ChatGPT Dot、09-23 Jev、09-16 Astral Ambitions（"Astra has me reconsidering the projects I thought were beyond me"）、09-10 goal-driven AI、08-26 Continual Learning、08-05 Orchestrator→Implementer→Advisor、07 月 Group Chat。
- 负结论：多文付费墙截断，全文判断受限。
