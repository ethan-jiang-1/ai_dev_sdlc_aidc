# 03 — ears — Evidence Summary

- scope: `Wave 1 starter pack for Topic 03 (EARS): one near-term empirical study + one post-RE09 official guide + one industrial primer + one software-scope guidance anchor`
- status: `closed_for_current_round`
- last_updated: `2026-04-18`
- related_references:
  - [`../_reference/03-ears-uusitalo-2023-plc-empirical.md`](../_reference/03-ears-uusitalo-2023-plc-empirical.md)
  - [`../_reference/03-ears-mavin-2016-ears-guidelines.md`](../_reference/03-ears-mavin-2016-ears-guidelines.md)
  - [`../_reference/03-ears-jama-industrial-primer.md`](../_reference/03-ears-jama-industrial-primer.md)
  - [`../_reference/03-ears-software-scope-guidance.md`](../_reference/03-ears-software-scope-guidance.md)
  - [`../_reference/00-shared-mavin-2009-ears-re09.md`](../_reference/00-shared-mavin-2009-ears-re09.md)
  - [`../_reference/00-shared-incose-gtwr-v4-summary.md`](../_reference/00-shared-incose-gtwr-v4-summary.md)

## 本轮已落地证据

1. 原始定义层：
   - RE'09 原始定义、五模式、ruleset、工业采用名录已在 [`../_reference/00-shared-mavin-2009-ears-re09.md`](../_reference/00-shared-mavin-2009-ears-re09.md)。
2. 后续实践层：
   - [`../_reference/03-ears-mavin-2016-ears-guidelines.md`](../_reference/03-ears-mavin-2016-ears-guidelines.md) 把 post-RE09 的实施建议、training/coaching、何时不用 EARS、复杂度边界补齐。
3. 实证层：
   - [`../_reference/03-ears-uusitalo-2023-plc-empirical.md`](../_reference/03-ears-uusitalo-2023-plc-empirical.md) 给出近年实验观察：同一需求会被写成不同模式，完整性是最常见问题，EARS 驱动的 PLC 测试是可行的。
4. 工业工具层：
   - [`../_reference/03-ears-jama-industrial-primer.md`](../_reference/03-ears-jama-industrial-primer.md) 说明 EARS 已被 Jama 作为 authoring / review workflow 的规则输入之一，并与 INCOSE rules 联动。
5. software-scope 层：
   - [`../_reference/03-ears-software-scope-guidance.md`](../_reference/03-ears-software-scope-guidance.md) 说明 QRA 官方已把 `low-level software requirements specification`、`software developers`、`new IT solution deliverables` 纳入 EARS / textual requirements 的适用范围，同时明确 pseudocode、state diagrams、decision tables 等软件文档边界。

## 当前可支撑的判断

1. EARS 不应再被写成“只有五种模板”的静态教学对象；它是一个从 RE'09 原始语法走向“训练、教练、组织落地、边界判断”的方法体系。
2. EARS 的主价值不是把自然语言变成形式化语言，而是把自然语言压到一个足够稳定、足够可测、足够可审查的中间层。
3. Topic 03 不能只写优点。当前证据已经明确支持至少两个限制面：
   - `Completeness` 是实际应用中的高频问题；
   - 当 preconditions 过多或需求本质上是公式/决策表时，EARS 不是最佳表示法。
4. 工业侧正在把 EARS 与 INCOSE rules、NLP 检查、advisor 工具结合，这对 Topic 04/06 有直接外溢价值。
5. Topic 03 现在可以更谨慎地表述软件域结论：
   - `software-scope-supported`
   - `saas-empirical-pending`

## 对 must_answer 的覆盖进度

| must_answer 子问题 | 当前状态 | 证据 |
| --- | --- | --- |
| Mavin 2009 原论文要点与后续补遗 | `partial` | 原论文已在 shared；后续补遗当前由 official guide + 2016 lessons 书目锚点支撑 |
| 五模式 + 复合官方语法与示例 | `covered` | RE'09 shared + official guide |
| 与 INCOSE GTWR v4 规则逐条映射 | `not_started` | 仍缺官方 PDF 规则全文或更强对照材料 |
| EARS 在纯软件 / SaaS 场景的权威实证 | `partially_narrowed` | QRA official software-scope guidance landed; SaaS empirical case still missing |
| 何时不用 EARS 的一手准则 | `starter_covered` | official guide 已覆盖 >3 preconditions / mathematical formulas / over-complex requirements |

## 当前 deep-dive questions

1. `GtWR v4` 的 42 条规则里，哪些可以与 EARS clauses 做接近逐条对齐，哪些只能做部分映射？
2. 是否存在 2020–2026 的纯软件 / SaaS 团队公开写过“把 EARS 用到 API / platform / workflow requirements”的案例，而不只是 software-scope guidance？2026-04-18 targeted search 再次未找到合格公开强源，缺口继续 deferred。
3. 2016 RE `Listens learned (8 lessons learned applying EARS)` 正文是否还能通过 IEEE / authorship page / institutional mirror 拿到？
4. Tooling 侧除了 Jama，还有没有更强的一手材料说明 EARS 进入 lint / authoring / agent workflow？

## 风险与升级点

- 当前 post-RE09 主锚点仍主要来自 official guide，而非 2016 RE 论文全文；对“lessons learned”的表述应标注为 `official-guide-supported, RE2016-upgrade-pending`。
- 近年 empirical anchor 目前只有 PLC 场景；Topic 03 在本轮多次 targeted search 后仍未找到足够强的非 PLC SaaS / software empirical case，但“软件范围是否适用”这一风险已被官方 guidance 收窄。
- `GtWR v4` 官方 PDF 受 Cloudflare 阻挡，Topic 03 与 Topic 05 后续 assertions 需要单独升级。

## 下一轮建议动作

1. 继续 Topic 03：优先补 `GtWR v4 rule-by-rule mapping`；`SaaS empirical evidence` 在本轮多次 targeted pass 后仍保留为 deferred gap，不用模板识别论文、百科页、厂商泛文档或教学材料替代生产案例。
2. 等 Topic 05 打开后，反向验证 `EARS ↔ BDD / decision-table` 的边界。
3. 在 Wave 2 中把 Topic 03 的限制面接入 `W2-claims-audit-v2.md`，避免 EARS 被写成无条件优解。
