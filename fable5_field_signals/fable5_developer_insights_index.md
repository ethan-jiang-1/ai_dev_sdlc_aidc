# Fable 5 洞察总览

> 这份文档不再做目录清单。
> 它只回答一个问题：看完当前这些样本以后，最值得先抓住的结论是什么。
> 如果你是第一次进这个目录，请先看 `README.md`。

---

## 先说结论

### 1. Fable 5 不是“默认模型”，而是“可委托长任务模型”

当前样本里，最稳定的共识不是“什么都用 Fable”，而是：

- 大任务
- 长任务
- 复杂任务
- 可委托任务

更适合 Fable 5。

代表样本：

- `run_every_austin_tedesco/`
- `run_every_kieran_klaassen/`
- `run_anthropic_mike_krieger/`

### 2. 它真正拉开的差距，不只是写代码，而是会自己推进和验证

很多外部样本反复提到的，不是“更会写”，而是：

- 会自己测
- 会自己加日志
- 会自己验证修复
- 会自己组合工具链

代表样本：

- `run_datasette_simon_willison/`
- `run_anthropic_boris_cherny/`
- `run_generativeai_net_martin_musiol/`

### 3. 代价和边界不是附属问题，而是主问题

现在已经很清楚了：

- token 成本
- 延迟
- NDA
- 数据保留
- silent intervention
- refusal / fallback

这些不是边角料，而是决定 Fable 5 能不能上线、能不能日用的关键变量。

代表样本：

- `run_zed_richard_feldman/`
- `run_every_mike_taylor/`
- `run_every_willie_williams/`
- `run_datasette_simon_willison/`

### 4. 组织里的不同角色，真的会把 Fable 放在不同位置

`Every` 这一组样本已经说明：

- 增长负责人会把它当 long-loop 执行器
- builder 会把它放进 `AI sandwich` 的中间层
- 平台负责人会更关心协作舒适度和 trade-off
- 咨询负责人会先看保密边界
- 应用 AI 工程师会把它拿去修复杂 workflow

代表样本：

- `run_every_austin_tedesco/`
- `run_every_kieran_klaassen/`
- `run_every_willie_williams/`
- `run_every_mike_taylor/`
- `run_every_nityesh_agarwal/`

### 5. 强模型时代，人越来越像 brief、review、签字的人

这组样本反复指向同一件事：

- 人不再主要负责逐步驾驶
- 人更像提出目标、补上下文、验收结果、承担责任的人

代表样本：

- `run_wharton_ethan_mollick/`
- `run_anthropic_thariq_shihipar/`
- `run_superpowers_jesse_vincent/`
- `run_anthropic_mike_krieger/`

### 6. 这套库现在已经有 4 种比较清楚的样本类型

当前最清楚的 4 类是：

- 组织角色样本
- 第三方实测样本
- 方法论样本
- 治理 / 产品化样本

这意味着这个目录已经开始可以做横向比较，而不只是收人名。

---

## 当前最值得先读的样本

### 如果你只能读 5 个

- `run_every_austin_tedesco/`
  - 看 Fable 5 怎样接住长任务和委托式知识工作
- `run_datasette_simon_willison/`
  - 看行为证据、风险边界和政策回滚
- `run_zed_richard_feldman/`
  - 看产品化落地时的 consent、retention 和 fallback
- `run_superpowers_jesse_vincent/`
  - 看工程制度怎样被 agent 化
- `run_wharton_ethan_mollick/`
  - 看人机关系怎么变

### 如果你想看“应用公司怎么用”

- `run_every_austin_tedesco/`
- `run_every_kieran_klaassen/`
- `run_every_nityesh_agarwal/`
- `run_every_willie_williams/`
- `run_every_mike_taylor/`

### 如果你想看“外部人第一次被打疼的地方”

- `run_datasette_simon_willison/`
- `run_generativeai_net_martin_musiol/`
- `run_digital_life_khazix/`

### 如果你想看“工程治理和制度”

- `run_superpowers_jesse_vincent/`
- `run_mclayer_plugin_codeforge/`
- `run_zed_richard_feldman/`

---

## 当前还缺什么

这套库已经有样本，但还缺几类更成体系的总结：

- 一份横向比较：哪些人把 Fable 用在长任务，哪些人用在修复 / review / 审计
- 一份边界比较：哪些团队因为成本、延迟、保密、同意而只部分使用
- 一份角色比较：增长、咨询、平台、Applied AI、独立开发者分别怎么安放 Fable

换句话说，人物样本已经开始够了，下一步会越来越适合沉成模式总结。
