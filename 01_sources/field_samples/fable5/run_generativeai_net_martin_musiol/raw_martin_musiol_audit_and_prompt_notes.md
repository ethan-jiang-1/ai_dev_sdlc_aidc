# Raw Notes: Martin Musiol's Audit and Prompt Notes from a 12-Hour Fable Shift

来源：

- `Claude Fable 5 worked my 12-hour night shift`
  - `https://mail.generativeai.net/p/claude-fable-5-worked-my-12-hour-night-shift`

## 这份材料补的是什么

Martin 原来的 raw 已经把整篇 newsletter 收进来了。

这份笔记专门把其中最适合复用的几层拆出来：

- 安全审计
- UX 审计
- 任务设计建议
- effort / 指令文件建议

这样 Martin 这条线就不只是一篇体验文，而是多了一份“拿来就能试”的实战索引。

## 1. 安全审计

Martin 对 Fable 最扎心的判断之一是：

> “The security audit hurt.”

他的解释非常直接：

- 应用已经 review 过
- 也测过
- 已经 live
- 他自己还签字认为 clean

结果 Fable 还是找回了几处真实 bug，而且有些就出在他自己已经放过的代码里。

这说明在 Martin 看来，Fable 的价值不是只会“写”，更在于：

- 重新审视已有系统
- 找回人类已经忽略的风险

## 2. UX 审计

另一条很有意思的发现是：

> “UX audits are underrated.”

他给出的整个 prompt 只有一句：

> “lean, clean, intuitive UI.”

Fable 返回的是：

- flow-level findings
- 达到 senior product designer 水平的反馈

这条样本很值钱，因为它说明 Fable 并不只适合工程 bug 审计，也适合产品体验层面的结构性检查。

## 3. 今晚就该试什么

Martin 在文末给了一个非常具体的建议：

- 找一个你最熟的 repo
- 跑两个 prompts
- 一个做 security audit
- 一个做 `lean, clean, intuitive UI`
- 给它一个小时

他的预测是：

- 你会关掉一些原本根本没意识到的问题

## 4. 怎样给 Fable 任务

Martin 对任务设计的建议，和资料库里别的人物线能形成呼应：

- 交给它的是 objectives，不是 tasks
- 要描述 done looks like 什么样
- 还要描述 how to verify it

他还特别提醒：

- 旧的 agent instruction files 会把 Fable 锚定在过时模式上
- 应该重写这些指令文件

关于 effort levels，他的总结也很实用：

- hand-off 场景用 `high`
- stay-in-the-loop 场景用 `medium`

## 为什么这份 raw 值得留

- 它把 Martin 从“12 小时夜班体验者”补成了“带可操作建议的实战作者”。
- 这类中腰部作者非常有价值，因为他们往往直接告诉你今晚就能怎么测，而不是只给一个宏大判断。
