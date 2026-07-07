# mclayer / plugin-codeforge：来源索引

## 一手来源

- `plugin-codeforge issue #2134`
  - 类型：公开 GitHub Epic / 采用策略 issue
  - 链接：https://github.com/mclayer/plugin-codeforge/issues/2134
  - 价值：直接写明 Fable 5 的采用原则、角色边界、`Claude Code >= 2.1.170` 版本 floor、排除项，以及后续 fallback / retro gate 的治理要求。

- `plugin-codeforge PR #2135`
  - 类型：公开 GitHub foundation PR
  - 链接：https://github.com/mclayer/plugin-codeforge/pull/2135
  - 价值：把 Epic 里的策略真正落到变更面，明确 `ADR-117`、consumer-guide 版本门槛和 lane PR 分拆顺序，证明这不是嘴上规划。

## 为什么这条线值得留

- 它不是模型公司自己的宣传稿，而是公开仓库里可以复核的采用设计。
- 它给出的不是笼统“Fable 更强”，而是在哪些 agent 角色上值得花 2 倍成本，哪些不值得。
- 它同时包含了治理层信息：版本 floor、fallback、retro、orchestrator 不切换，这些都比单纯 benchmark 评价更接近真实生产约束。

## 当前缺口

- 还可以继续补 `#2134` 关联的 lane PR 和 marketplace sync PR，形成更完整的执行链。
- 也可以继续跟进 issue 末尾提到的 runtime fallback codify 和最终 close 决策，观察“治理完成”和“实际运行可用”之间的差距。
