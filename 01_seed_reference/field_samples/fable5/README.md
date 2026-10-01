# Fable 5 样本库

> 这是一个围绕 `Claude Fable 5` 的人物与组织样本库。
> 它不是新闻堆，也不是论文综述，而是尽量回答一个更实际的问题：谁真的拿 Fable 5 干活了，他们怎么用，它改变了什么，又卡在什么地方。

---

## 先看这里

如果你第一次进这个目录，不要一个个目录盲点。

先按下面这条路读：

1. 先看 `fable5_developer_insights_index.md`
2. 先在那张图里找到你关心的问题和对应的人
3. 再去点具体样本目录

这张图现在负责回答 4 件事：

- 谁真的在用 `Fable 5`
- 他们各自贡献了什么最值钱的 insight
- 哪些主题已经可以横向比较
- 如果你只读 3 到 5 个样本，最该先读谁

如果你只想先抓感觉，推荐从这 6 条线开始：

- `run_every_austin_tedesco/`
  - 看 Fable 5 怎样接住长任务式知识工作和增长实验
- `run_datasette_simon_willison/`
  - 看 Fable 5 在真实 debugging 里到底做了什么，以及风险边界长什么样
- `run_zed_richard_feldman/`
  - 看产品团队把 Fable 5 真接进产品时，会遇到哪些隐私、同意和 fallback 问题
- `run_superpowers_jesse_vincent/`
  - 看 agent 工作流怎样被制度化，以及 Fable 5 怎样反过来优化这套制度
- `run_wharton_ethan_mollick/`
  - 看 Fable 5 为什么会让人从“操作者”变成“委托人”
- `run_anthropic_thariq_shihipar/`
  - 看强模型时代为什么重点变成了 `unknowns`、上下文和协作方法

## 先用这张图找方向

如果你不想自己归纳，直接按问题找：

- 想看长任务和委托式工作：去看 `run_every_austin_tedesco/`、`run_every_kieran_klaassen/`、`run_anthropic_mike_krieger/`
- 想看主动 debugging 和 self-verification：去看 `run_datasette_simon_willison/`、`run_anthropic_boris_cherny/`、`run_generativeai_net_martin_musiol/`
- 想看治理、风险和产品边界：去看 `run_zed_richard_feldman/`、`run_every_mike_taylor/`、`run_mclayer_plugin_codeforge/`
- 想看人的角色怎么变：去看 `run_wharton_ethan_mollick/`、`run_anthropic_thariq_shihipar/`、`run_superpowers_jesse_vincent/`

---

## 怎么读

### 如果你想看“谁真的在用”

先读：

- `run_every_austin_tedesco/`
- `run_every_kieran_klaassen/`
- `run_every_nityesh_agarwal/`
- `run_generativeai_net_martin_musiol/`

### 如果你想看“它到底强在哪”

先读：

- `run_datasette_simon_willison/`
- `run_anthropic_boris_cherny/`
- `run_anthropic_mike_krieger/`
- `run_wharton_ethan_mollick/`

### 如果你想看“风险和边界”

先读：

- `run_zed_richard_feldman/`
- `run_every_mike_taylor/`
- `run_every_willie_williams/`
- `run_datasette_simon_willison/`

### 如果你想看“工作流怎么迁移到 AI 时代”

先读：

- `run_anthropic_thariq_shihipar/`
- `run_superpowers_jesse_vincent/`
- `run_every_austin_tedesco/`
- `run_every_kieran_klaassen/`

---

## 每个目录怎么看

每个 `run_*/` 目录尽量保持同一种读法：

- `profile.md`
  - 先告诉你这人是谁，为什么值得留
- `quotes.md`
  - 先抓住最值钱的原话和判断
- `sources.md`
  - 再看证据从哪里来、还缺什么
- `raw_*.md`
  - 最后看原始材料整理
- `analysis_*.md`
  - 只在值得单独展开时才会有

如果你只看一个文件，先看 `profile.md`。
如果你想快速扫一圈，先看 `quotes.md`。
如果你准备认真消化，再看 `raw_*.md`。

---

## 辅助文档

- `fable5_developer_insights_index.md`
  - 当前最重要的一页地图：人、样本、insight、主题都在那里
- `fable5_source_pool_map.md`
  - 来源池备忘，偏采集视角，不是读者第一入口

---

## 一句话总结

这个目录现在已经不只是“谁夸过 Fable 5”，而是开始形成一套可读的样本库：

- 有人在拿它跑长任务
- 有人在拿它修复杂烂摊子
- 有人在拿它做安全和 UX 审计
- 有人在把它编进工程制度
- 也有人明确指出它不能用在什么地方
