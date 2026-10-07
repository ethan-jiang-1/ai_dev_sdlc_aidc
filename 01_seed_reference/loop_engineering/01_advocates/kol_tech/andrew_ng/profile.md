---
type: kol_evidence
directory: 01_advocates/kol_tech/andrew_ng
observation_date: 2026-10-06
---

# Andrew Ng

- **身份**：DeepLearning.AI 创始人，*The Batch* 通讯作者（本卡素材即出自该通讯 2026-06-30 一期，X 同步转发）
- **背景**：Andrew Ng（吴恩达）——斯坦福大学兼职教授；Google Brain 联合创始人（2011，深度学习浪潮的关键推手）；百度首席科学家（2014–2017，统领百度研究院）；Coursera 联合创始人、DeepLearning.AI 创始人（2017）；《Machine Learning Yearning》作者——AI 教育的全球布道者
- **入册日期**：2026-06-30（X post）
- **入册理由（号召力依据）**：**术语定义者**——在 loop engineering 刚成为热词时给出最完整的一套分层定义（三环嵌套），且被中文圈与工程媒体广泛转述
- **对本主题的主张一句话**：AI 时代的软件开发不是一次性把需求丢给模型，而是设计**一组能持续变好的循环**；三环里外环修正内环方向，人类的价值不是"品味"而是**上下文优势（context advantage）**

## 他在这波里的位置

吴恩达不是这个词的发明者——他在原文里直接写明，这个词火起来是因为 **Boris Cherny（Claude Code 创作者）与 Peter Steinberger（OpenClaw 创作者）**在社交媒体上的讨论走红。他做的是**给这个词补一套可操作的分层**：

| 环 | 节奏 | 谁在跑 | 干什么 |
|---|---|---|---|
| Loop 1 · Agentic coding loop | 每几分钟 | AI 自己 | 拿到 spec（可选加 evals）→ 写码 → 自测 → 迭代到无 bug 且满足 spec |
| Loop 2 · Developer feedback loop | 几十分钟 ~ 几小时 | 人看产品、改判断 | 从"当 QA 找 bug"升级为"做更高层的产品决策"，并把模糊愿景翻译成清晰 spec |
| Loop 3 · External feedback loop | 几小时 ~ 几周 | 真实用户 | 朋友试用 → alpha → A/B；数据回流修正产品愿景，再驱动 spec，再驱动 Loop 1 |

**三环不是并列，是嵌套**：外环的数据修正内环的方向。

## 为什么他这套说法对本主题重要

1. **给出了"loop engineering"的第一份分层定义**（在他之前，这个词主要是热度而非结构）——本主题的时间线把它当作 2026-06 命名事件的第二个锚点。
2. **"context advantage" 替换 "taste"** 是他独有的提法，直接给出了方向：不是"培养说不清的软技能"，而是**缩小人与 AI 之间的信息差**。这句话是本主题"人在环里到底干什么"这一问的最早答案之一。
3. **他明确点名了两个词源人物**（Cherny / Steinberger）——本主题台账收录这两人，依据即来自这一句，不是我们的推测。

## 边界（他不管什么）

- 他讲的是 **0→1 产品的三环方法论**，不是 harness/门禁/管线层的工程治理——那部分归 `03_practice/harness_governance/`。
- 他没有给出**可核的停止条件**的工程化定义（这是 Addy Osmani / LangChain 那一支补上的，见主题 `digested/` 对应篇）。
- 他的三环**不含外层调度系统**（"下一件工作由谁决定"）——这是本主题与 SDD 对照时的一条关键分界。

## 素材

- 一手：`raw_ng_x_post_en.md`（英文原文，The Batch 交叉发布到 X）
- 交叉验证：`raw_thinkinai_zh.md`（中文编译，**低强度**，只作交叉验证，不作唯一引用）
- 来源索引与缺口：`sources.md` · 逐字引句：`quotes.md`

---

# 增量补挖（2026-10-07 goal 第一批·单点→稳定复核）

> 判定：**单点解除 → 稳定**——06-26（The Batch 命名信；X 版 06-30）→ 07-10 → 08-14 → 09-04 五个署名时点同向（推动＋教掌控）；原档"承诺的后续文章未见"缺口**闭合**。完整发现见 .tmp-goal-movers/batch-B1-advocates.md。

## 《Make All Your Tokens (and Your Brainwork) Count》（The Batch，2026-07-10）

- URL：https://www.deeplearning.ai/the-batch/make-all-your-tokens-and-your-brainwork-count ｜ fetch 成功（全文）
- 逐字摘录：

> "AI tokens are cheap; human tokens are gold."

> "when I make key decisions, I often steer the agent to remember that decision somewhere, say in a SPEC.md file… so the agent's stopping criteria in the future require checking that this problem does not occur again."
（**SPEC.md＝把人的判断写进 agent 停止条件**——直接钩停止条件类。）

> "Instead of 'spec drive development' becoming a new waterfall process where writing a spec is a gate to further progress, this allows me to more iteratively refine the spec."
（明确反对把 SDD 做成新瀑布。）

## 《The AI Engineering Skills Map》（08-14）＋《Skills Map Part 4 — Coding Agents》（09-04）

- URL：https://www.deeplearning.ai/the-batch/the-ai-engineering-skills-map-in-detail-using-coding-agents ｜ fetch 成功（全文）
- 逐字（08-14）："…help the agent autonomously close loops by providing verifiers or evals."；"knowing how much to intervene and how much to leave them alone"
- 逐字（**09-04 窗口内最重的审慎句——推动内收紧**）：

> "it is sometimes useful to get agents to run autonomously for hours and burn millions or tens of millions of tokens. But currently the practical utility of very long-horizon tasks — especially relative to their cost — has been amplified beyond reality. Instead, most effective coding agent use is a complex, highly iterative process, and being able to intervene with high-skill judgement gives much better results."
（对无人值守炒作的公开降温——在整体推动框架内，不构成转向怀疑的弧线。）

- 负结论：09-10 月无本人一手新发声（09-18 反恐慌信仅索引级）；AI Engineer NYC 讲题待发布。
