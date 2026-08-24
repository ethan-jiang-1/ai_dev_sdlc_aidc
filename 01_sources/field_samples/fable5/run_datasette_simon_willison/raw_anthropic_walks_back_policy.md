# Raw Notes: Anthropic Walks Back Policy That Could Have 'Sabotaged' AI Researchers

来源：

- 原文：`https://simonwillison.net/2026/Jun/11/anthropic-walks-back-policy/`
- 关联背景：前一日的 `If Claude Fable stops helping you, you'll never know`

## 这份材料补的是什么

前一篇短文里，Simon 提出的问题是：

- Fable 5 针对 frontier LLM development 的限制是静默发生的
- 用户不会被告知自己已经拿到被降质的结果

这篇 follow-up 补的是后续演化：

- 研究社区爆发强烈反对
- Anthropic 公开道歉
- 相关 safeguard 从“静默”改成“可见”

## 关键信息

Simon 引用了 Anthropic 对 WIRED 的回应：

> We're changing Fable 5's safeguards for frontier LLM development to make them visible.

> We made the wrong tradeoff and we apologize for not getting the balance right.

随后他又转引了 `@ClaudeDevs` 的更详细说明：

- 以后被标记的请求会显式 fallback 到 `Opus 4.8`
- 用户每次都会看到它发生
- API 也会返回 refusal reason

## Simon 的态度

Simon 认为这是好消息，但还不够：

> It's good news that they're dropping the invisible aspect of this.

> It would be a whole lot better if they dropped this category of refusals entirely.

这很重要，因为它说明 Simon 的关注点不是“赢了一次舆论战”，而是：

- 至少先把不可见干预拿掉
- 但更根本的问题仍然存在：厂商是否应该在这类研究问题上限制模型能力

## 为什么这份 raw 值得留

- 它补全了 Simon 围绕 Fable 5 的一条连续观察链：
  - 先记录能力
  - 再记录风险
  - 再记录厂商如何被迫回滚政策
- 这类 follow-up 对资料库特别重要，因为它让人物目录从静态摘录变成了时间序列证据。
