# Fable 5 洞察地图

> 这不是目录清单，也不是维护计划。
> 它是一张一页地图：谁在用 Fable 5，他们各自贡献了什么 insight，你该先看谁。
> 如果你第一次进这个目录，先看这张图，再决定要不要点进具体目录。

---

## 一眼先抓住

- `Fable 5` 最突出的定位，不是通用默认模型，而是更适合被委托去跑长任务、复杂任务和整段工作流。
- 它真正拉开差距的地方，不只是写代码，而是会自己推进、自己验证、自己补工具动作。
- 真正的阻力也很清楚：成本、延迟、NDA、数据保留、同意、fallback，这些都会决定它能不能落地。
- 同一个组织里，不同角色会把 Fable 放在完全不同的位置，说明“怎么安放它”比“要不要用它”更重要。
- 强模型时代，人越来越像 brief、review、sign-off 的人，而不是每一步都手动驾驶的人。

---

## 人物与洞察总表

这列里的“来源分量”不是绝对真伪评级，而是帮你先判断：这是厂商内部、一线产品团队、头部观察者，还是普通外部实测。

| 最值得抓住的 insight | 关键词 | 角色 / 位置 | 来源分量 | 来源 |
| --- | --- | --- | --- | --- |
| Fable 可以接住长任务式知识工作和增长实验，不只是补代码片段 | 长任务 / 委托 / 应用落地 | 应用团队 / 增长 | 一线应用团队 | `run_every_austin_tedesco/` |
| 强模型适合放进 `AI sandwich` 的中间执行层，人负责上下文和验收 | AI sandwich / 分工 / 协作 | builder / workflow 设计 | 一线应用团队 | `run_every_kieran_klaassen/` |
| 复杂坏工作流要靠清楚的目标、上下文和 definition of done 才救得回来 | workflow 修复 / 上下文 / 执行 | Applied AI 工程 | 一线应用团队 | `run_every_nityesh_agarwal/` |
| 实际采用看的是 trade-off 和协作舒适度，不是只看 benchmark 榜单 | trade-off / 采用决策 / 协作感 | 平台 / builder | 一线应用团队 | `run_every_willie_williams/` |
| 一碰到 NDA 和客户机密，强模型就不能无脑接手，边界管理变成主问题 | NDA / 保密 / 治理边界 | 咨询 / 客户交付 | 一线应用团队 | `run_every_mike_taylor/` |
| Fable 的区别在主动调试、主动验证和持续推进，但透明性与干预边界也更敏感 | debugging / verification / 风险 | 独立开发者 / 外部观察 | 头部外部观察者 | `run_datasette_simon_willison/` |
| Fable 可以直接拿去做安全审计和 UX 审计，说明它开始能承担更完整的专业任务块 | audit / security / UX | 外部实测者 | 中腰部实干者 | `run_generativeai_net_martin_musiol/` |
| 多 prompt 实测能看出 Fable 在复杂任务里更主动，但也更需要明确约束与观察 | prompt 实测 / 主动性 / 控制 | 外部实测者 | 普通外部实测 | `run_digital_life_khazix/` |
| 强的地方不是文采，而是会自己测、自己加日志、自己验证修复 | self-verification / tools / debugging | 模型侧工程 | 厂商内部一线 | `run_anthropic_boris_cherny/` |
| Fable 开始能接 whole projects 的一大段，人更像委托、评审和拍板的人 | whole projects / 委托 / 角色变化 | 产品负责人 | 厂商内部一线 | `run_anthropic_mike_krieger/` |
| 真正稀缺的变成 `unknowns`、上下文组织方式和如何让模型帮你发现盲区 | unknowns / context / 方法论 | 方法论 / field guide | 厂商内部方法论 | `run_anthropic_thariq_shihipar/` |
| agent 工作流会反过来改变团队制度，形成 brief-review-signoff 的工作方式 | agent 制度 / review / sign-off | 工程制度设计 | 头部实践者 | `run_superpowers_jesse_vincent/` |
| 人机关系正在从“操作者”转向“委托人”，工作的重心变成给目标、看结果、负责任 | patron 模式 / 人机角色 / 委托 | 教学 / 观察者 | 头部观察者 | `run_wharton_ethan_mollick/` |
| 产品化落地时最难的不是接 API，而是 consent、retention、fallback 和用户信任 | 产品化 / consent / fallback | 产品接入 / BYOK | 一线产品团队 | `run_zed_richard_feldman/` |
| Fable 更像需要被外科式接入的能力，不是整套系统一把梭替换 | surgical adoption / rollout / review | 插件 / 工程接入 | 公开工程证据 | `run_mclayer_plugin_codeforge/` |
| 产品经理关心的不是模型炫技，而是它在哪些任务里能真正改变 PM 的工作方式 | PM workflow / 角色迁移 / 使用边界 | PM 视角 | 领域实务作者 | `run_product_compass_pawel_huryn/` |

---

## 按问题看人

### 如果你想看“谁真的在拿它干活”

- `run_every_austin_tedesco/`
- `run_every_kieran_klaassen/`
- `run_every_nityesh_agarwal/`
- `run_generativeai_net_martin_musiol/`
- `run_anthropic_mike_krieger/`

### 如果你想看“它为什么像长任务引擎”

- `run_every_austin_tedesco/`
- `run_every_kieran_klaassen/`
- `run_anthropic_mike_krieger/`
- `run_wharton_ethan_mollick/`

### 如果你想看“它为什么会自己推进和验证”

- `run_datasette_simon_willison/`
- `run_anthropic_boris_cherny/`
- `run_generativeai_net_martin_musiol/`
- `run_digital_life_khazix/`

### 如果你想看“边界和治理为什么是主问题”

- `run_zed_richard_feldman/`
- `run_every_mike_taylor/`
- `run_every_willie_williams/`
- `run_datasette_simon_willison/`
- `run_mclayer_plugin_codeforge/`

### 如果你想看“人和组织的角色怎么变了”

- `run_wharton_ethan_mollick/`
- `run_anthropic_thariq_shihipar/`
- `run_superpowers_jesse_vincent/`
- `run_anthropic_mike_krieger/`

---

## 只读 5 个

- `run_every_austin_tedesco/`：看 Fable 怎样接住委托式长任务
- `run_datasette_simon_willison/`：看主动 debugging、验证和风险边界
- `run_zed_richard_feldman/`：看产品化落地时的 consent、retention 和 fallback
- `run_superpowers_jesse_vincent/`：看工程制度怎样被 agent workflow 重写
- `run_anthropic_thariq_shihipar/`：看强模型时代的方法论核心为什么变成 `unknowns`

---

## 这张图说明了什么

- 这套库现在已经不只是“谁夸过 Fable 5”，而是能横向比较不同角色、不同任务、不同边界条件下的真实使用方式。
- 读这套库最好的方法，不是按目录顺序点进去，而是先确定你要看哪类问题，再顺着这张图反查样本。
