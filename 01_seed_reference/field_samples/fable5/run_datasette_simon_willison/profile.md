# Simon Willison

- 身份：Datasette / 独立开发者；Django 联合创始人
- 角色定位：最强的第三方、可审计、可复现实验记录者之一
- 为什么值得单列：Simon 的厉害之处在于，他会把模型到底干了什么一层层扒出来
- 核心贡献：他把 Fable 描述成有 `big model smell`，而且 `relentlessly proactive`
- 最重要的判断：Fable 的差异不只是答得更好，而是会为了完成目标自发搭工具链、改模板、开服务、测浏览器、抓截图、写报告
- 目录现状：现在已同时覆盖总体体验、经典调试案例、silent intervention 风险反思，以及政策回滚 follow-up

## 这人到底说了什么

- 他用一个查询自己开源项目列表的例子，说明 Fable 的世界知识密度明显更高。
- 他用一个 CSS bug 的真实 debugging 过程，说明 Fable 会自行发明和组合调试手段。
- 他还明确提醒，越主动的 agent 越需要 sandbox，因为一旦被 prompt injection 劫持，破坏力会极大。
- 他也公开批评过 Fable 的 silent intervention 设计，认为“模型悄悄不再帮你”是更深一层的信任问题。

## 最值得记住的句子

> “This is something of a beast.”

> “The best way to describe Fable is that it feels big.”

> “Claude Fable is relentlessly proactive.”

## 我的判断

- Simon 是最适合拿来做“行为证据库”的人物。
- 如果没有 Simon 这种拆过程的人，很多人只会觉得 Fable 是个更贵更慢但更强的模型。
- 真正让人意识到它代际变化的，恰恰是他展示出的那些中间动作。
- 现在这条目录已经兼具三层价值：能力感知、行为过程、风险边界。
