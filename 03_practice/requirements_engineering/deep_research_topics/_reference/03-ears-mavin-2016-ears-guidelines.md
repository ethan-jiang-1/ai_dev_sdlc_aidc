# Alistair Mavin / QRA Corp 2019 — The Easy Approach to Requirements Syntax: The Definitive Guide（含 RE 2016 lessons-learned 书目信息锚点）

- source_url: `https://f.hubspotusercontent20.net/hubfs/2367473/LeadGen%20Content/EARS%20-%20The%20Easy%20Approach%20to%20Requirements%20Syntax%20Guide.pdf` + `https://www.es.mdu.se/pdf_publications/6673.pdf`（其参考文献列出 `Listens learned (8 lessons learned applying EARS). 2016 IEEE RE`）
- source_type: `official guide + academic bibliographic trace`
- accessed_at: `2026-04-18`
- related_topic: `03 ears (primary), 01 re-landscape, 05 integration-bdd`
- trust_level: `official practitioner guide; academic-metadata only for RE 2016 trace`
- tier: `B`
- why_it_matters: Topic 03 当前最缺的是 RE'09 之后的“如何真正落地 EARS、何时不用、实施会碰到什么障碍”。公开可抓取的这份官方指南正好覆盖这些缺口；同时它还能把仍未拿到全文的 2016 RE lessons-learned 论文显式挂出来，方便后续升级。
- captured_excerpt: `partial`（2019 guide 正文已捕获；2016 RE 论文仅有书目锚点，未取得全文）
- claims_supported: `EARS 是一种 gently constrain NL 的方法而不是单纯模板；引入 EARS 最好配合 training + coaching；并非所有 requirement 都该强行写成 EARS；当 preconditions 超过 3 个、需求本质上是数学公式或复杂非文本结构时应换表示法；组织落地时 follow-on coaching 很关键。`
- date_scope: `guide PDF last-modified 2019-08-13; RE 2016 paper exists but full text not captured`
- related_entities: `Alistair Mavin; QRA Corp; EARS; Sarah Gregory; Eero Uusitalo; IEEE RE 2016`

## 关键事实

1. 这份 17 页 PDF 是可公开获取的 EARS 官方实践指南，内容明显超出 RE'09 的原始定义，覆盖了实施、障碍、边界和建议。
2. 指南多次强调：EARS 不是重形式化，而是对自然语言做 `gently constrain`。
3. 指南把 EARS 写成一个“方法 / 哲学”，而不只是句法模板库。
4. 它给出三类特别重要的落地经验：
   - 训练不需要很重，但不能没有；
   - follow-on coaching 对组织内嵌入很关键；
   - 不是所有 requirement 都该写成 EARS。
5. “When to and when not to use EARS” 明确给出几条边界：
   - 如果 requirement 变得过度复杂，不应强行文本化；
   - 如果前置条件超过 3 个，优先考虑其他表示法；
   - 数学公式类需求不适合 EARS。
6. 指南在“Challenges / Obstacles”章节里把应用难点显式化，说明 Topic 03 不能只写优点。
7. 2023 MDU 论文的参考文献进一步确认：`Listens learned (8 lessons learned applying EARS)` 以 `2016 IEEE 24th International Requirements Engineering Conference (RE), pages 276–282` 形式存在；但本轮未抓到全文。

## 核心内容摘录

### 定位与哲学

> EARS is not a template. It's a philosophy.

> EARS gently constrains natural language to write better requirements.

### 训练与内嵌

- `The best way to introduce EARS into your RE process is with a bit of expert training and coaching.`
- 指南建议训练最好贴近真实项目开始阶段，不要离应用太远。
- 反复强调 `follow-on coaching`，因为 EARS “易学但并非立即精通”。

### 何时不用 EARS

- `If you have more than three preconditions`
- `When requirements are mathematical formulas`
- `When the requirement extends complexity`

这些边界直接补上了 Topic 03 当前缺的“何时不用 EARS”一手准则。

### 2016 lessons-learned 锚点

2023 MDU 论文参考文献列出：

`Alistair Mavin, Philip Wilksinson, Sarah Gregory, and Eero Uusitalo. Listens learned (8 lessons learned applying ears). In 2016 IEEE 24th International Requirements Engineering Conference (RE), pages 276–282. IEEE, 2016.`

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 03 `ears` | Post-2009 refinement、实施建议、障碍、何时不用 EARS、训练/教练的重要性 |
| Topic 01 `re-landscape` | 说明 EARS 的定位仍是受控自然语言，不是模型或公式的替代品 |
| Topic 05 `integration-bdd` | 支撑“故事/示例/模型/EARS 混用”的边界判断：并非所有表达都应落到 EARS |

## 可直接引用的术语 / 概念

- `gently constrains natural language`
- `EARS is not a template. It's a philosophy.`
- `training and coaching`
- `If you have more than three preconditions`

## 风险与局限

1. 这是一份官方 practitioner guide，不是同行评审论文；因此适合支撑方法论与实施建议，不单独支撑效果主张。
2. 2016 IEEE RE lessons-learned 论文正文本轮未取得；当前仅有书目级锚点，后续应升级。
3. PDF 由 QRA Corp 分发，带明显推广包装；使用时应把“方法论内容”和“营销叙述”区分开。
4. 文件名保留 `2016` 是为了与 queue 当前任务的目标锚点保持一致，但本地可直接摘录的正文主体来自 2019 官方指南；引用时必须写清这一点。

## 交叉引用

- 共享原始定义锚点：[`00-shared-mavin-2009-ears-re09.md`](00-shared-mavin-2009-ears-re09.md)
- Topic 03 empirical anchor：[`03-ears-uusitalo-2023-plc-empirical.md`](03-ears-uusitalo-2023-plc-empirical.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
