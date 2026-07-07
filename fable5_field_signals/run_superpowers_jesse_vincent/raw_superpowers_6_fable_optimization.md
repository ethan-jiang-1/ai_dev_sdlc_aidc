# Raw Notes: Superpowers 6 and Fable-Driven Optimization

来源：

- 原文：`https://blog.fsck.com/2026/06/15/Superpowers-6/`

## 这篇材料补的是什么

这篇是 Jesse 在 2026 年围绕 Fable 5 最值得单独留的一篇更新。

因为它展示的不是“如何用 agent 编程”，而是：

- Jesse 直接用 Fable 优化了自己的 agent 开发方法
- Superpowers 不只是静态流程，而是被 Fable 反过来重新设计

## 关键背景

Jesse 先交代了一个长期痛点：

- Superpowers 出好结果，但很慢
- token 消耗很高
- autonomous subagent orchestration 的慢和贵会影响体验

然后 Fable 上线后，他做了一个很直接的实验：

- 让 Fable 优化 `Subagent Driven Development`
- 原本只期望省下 `15%` token
- 结果远超预期

## Fable 做了什么

### 1. 优化 reviewer handoff

Fable 分析了大量 Superpowers 会话，发现 reviewer 子 agent 会花很多 token 在 `git` 命令上。

它给出的改法是：

- 不再让 reviewer 自己去摸索 diff
- 由前一步先打包出 review package
- 里面直接附带格式化 diff 和 metadata

结果：

- token 消耗下降约 `10%`
- wall-clock time 也下降

### 2. 过夜自动研究

Jesse 睡前给 Fable 下了一个 `/goal`：

- 继续优化 cost-efficiency
- 用 Opus 做 coordinator
- 建 hypothesis log
- 跑实验
- 至少做 `25` 个实验

Fable 随后：

- 搭了完整的 autoresearch harness
- 跑完了 `25` 次实验
- 还记录 backlog
- 把结果写成可复用文档

相关仓库：

- `https://github.com/prime-radiant-inc/superpowers-autoresearch`

## 关键结论

Jesse 总结里最值得保留的有几条：

- 合并 spec compliance reviewer 和 code quality reviewer
- 预打包 reviewer diff packet
- 根据任务类型调整 orchestrator 对 implementer model tier 的选择

整体结果：

- wall-clock runtime 降低约 `50%`
- token spend 降低约 `60%`

## 更重要的部分

Jesse 还记录了很多“看似省钱，实际上有害”的失败路线：

- 限制 controller thinking 反而更差
- 给 plan 设太紧的字数预算会伤害测试内容
- Sonnet 做 plan generation 会伤害任务结构
- reviewer 只看 diff package 会误把“全局约束”当 spec

这和 Jesse 一贯的方法是一致的：

- 好方法不是靠感觉选出来的
- 要靠 evals、假设日志、失败记录和反例收敛

## 为什么这份 raw 值得留

- 它说明 Jesse 在 2026 年围绕 Fable 5 的发言并不只停留在播客和理念上。
- 他已经用 Fable 直接重构了自己的开发体系，并量化了结果。
- 对这个人物目录来说，这份材料特别重要，因为它把 Jesse 从“制度设计者”进一步推进成“制度迭代实验者”。
