# Richard Feldman / Zed：洞察摘录

## 关键言辞

> Because Fable 5 cannot be offered under Zero Data Retention ... this gates the model behind an explicit data-retention consent.

- 这句是整条样本的中心。
- 它说明产品团队面对 Fable 5 时，第一问题不是“厉不厉害”，而是“能不能在现有隐私约束下合法上线”。

> When Fable 5 declines a request, it transparently falls back to Claude Opus 4.8 ...

- 这句非常重要，因为它展示了产品级 fallback 不是“报错就算了”，而是要保证对话能继续。
- 对资料库来说，这种 user-facing 恢复路径比单纯 benchmark 结果更接近真实落地。

> A hard gate in `CloudLanguageModel::stream_completion` that raises a typed `DataRetentionConsentRequiredError` when consent is missing, which is non-retryable.

- 这句说明他们把隐私约束压到了运行时和类型系统里，不是靠文档提醒用户自己注意。
- 这比“建议不要这样用”更像真正的工程治理。

> Adds the `send_to_user` tool plus refusal-fallback model support, gated on the Fable model id prefix.

- 这句补足了另一个关键面：不只是模型配置变了，围绕 Fable 的交互与错误转接机制也变了。

## 总结判断

- `Zed` 这条线很好地补上了“产品集成样本”。
- 它能和 `Every` 的 workflow 样本、`plugin-codeforge` 的治理样本形成三角对照：
- 个人/团队怎么用
- agent 系统怎么编排
- 产品团队怎么上线
