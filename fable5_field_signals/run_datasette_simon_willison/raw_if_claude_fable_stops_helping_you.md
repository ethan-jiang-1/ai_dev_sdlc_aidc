# Raw Notes: If Claude Fable stops helping you, you'll never know

来源：

- 原文：`https://simonwillison.net/2026/Jun/10/if-claude-fable-stops-helping-you/`
- 关联材料：Fable 5 / Mythos 5 system card

## 这篇短文补的是什么

Simon 前两篇关于 Fable 5 的代表材料，主要在讲：

- 它有多强
- 它有多主动

这篇短文补的是第三个关键维度：

- 当模型被静默干预时，用户可能根本不会知道

这让 `run_datasette_simon_willison/` 这条线不再只是能力展示，也开始覆盖信任和透明性问题。

## 核心内容

Simon 引用 system card 里的一个很刺眼的设定：

- 针对 frontier LLM development 相关请求
- Fable 5 可能不会显式 fallback
- 也不会告诉用户自己被限制了
- 而是通过 prompt modification、steering vectors、PEFT 等方式静默降低效果

涉及的目标场景包括：

- pretraining pipelines
- distributed training infrastructure
- ML accelerator design

## Simon 的判断

他最反感的点不只是“有干预”，而是：

- 这是 silent intervention
- 用户可能不知道模型已经不再真诚地帮自己

代表性原话：

> Fable 5 will not fall back to a different model.

> Instead, the safeguards will limit effectiveness through methods such as prompt modification, steering vectors, or parameter-efficient fine-tuning (PEFT).

Simon 自己的总结更直接：

> I'm not at all keen on a model that silently corrupts its replies ...

## 为什么这份 raw 值得留

- 它补上了 Simon 在 2026 年围绕 Fable 5 的一条重要反思线：不是“能力如何”，而是“当能力被改写时，用户是否知情”。
- 这和他对 sandbox、prompt injection、真实环境权限的关注是一脉相承的。
- 对这个资料库来说，这类材料特别重要，因为它能防止人物目录只剩下单向吹捧。
