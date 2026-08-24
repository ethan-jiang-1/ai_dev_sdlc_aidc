# Richard Feldman / Zed：来源索引

## 一手来源

- `zed PR #58945`
  - 类型：公开 GitHub 产品集成 PR
  - 链接：https://github.com/zed-industries/zed/pull/58945
  - 价值：直接写出 Fable 5 的数据保留限制、显式 consent 设计、typed error、请求拒绝后的 `Opus 4.8` fallback，以及面向用户的恢复交互。

- `Commit: Gate Claude Fable behind Anthropic data retention consent`
  - 类型：PR 中的关键提交
  - 链接：https://github.com/zed-industries/zed/pull/58945/commits/8b7c19366a7caa85d12bb04804ca9eef30664413
  - 价值：把“为什么不能默认开 Fable 5”这件事变成了明确的产品/代码约束，而不是讨论帖里的泛泛提醒。

- `Commit: Fable support`
  - 类型：PR 中的关键提交
  - 链接：https://github.com/zed-industries/zed/pull/58945/commits/f7f370b182a8803ddaa79c2506ec6b5616f1cc42
  - 价值：补充了 refusal-fallback model support，说明这条线不只是在设置页加开关，而是在 agent 交互层处理模型拒绝后的体验。

## 为什么这条线值得留

- 它不是媒体转述，也不是单人使用感想，而是公开产品仓库里的真实集成设计。
- 它把 Fable 5 集成时最容易被忽略的一组问题都显性化了：数据保留、用户 consent、不可重试错误、透明回退。
- 它特别适合作为“产品化样本”保留，因为这里已经不是个人怎么用模型，而是产品团队怎样让模型上线而不把用户体验搞坏。

## 当前缺口

- 后续还可以继续补 `files changed` 里的具体 UI 和设置字段截图，增强产品层证据。
- 也可以继续跟进稳定版 / 预览版的 cherry-pick PR，观察这条集成如何被传播到不同发布通道。
