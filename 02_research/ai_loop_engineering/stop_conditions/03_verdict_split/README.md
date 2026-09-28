# ③ 验收与干活分离（verdict split）

**本点回答**：完成由谁判？裁判怎么才不被干活的一方操纵/收买？判定权归属有哪几极？

**判定句**（权威在 [`../../digested/03-构件.md`](../../digested/03-构件.md) §一）：
验收与干活角色分离，五处一手同向跨三家（Anthropic 2024/2025、CC `/goal`、OpenAI auto-review、LangChain）；
**唯一未收敛点＝裁判权归谁**（五极设计空间），干活模型自判与"提前完成"直接冲突，是最弱的一极。

## 看板

| 件 | 状态 |
|---|---|
| [`practices.md`](practices.md) | ✅ **自说明版**：28 条（原 26 条＋第二轮深挖批 2 条：end-state oracle 学术实现、Augment CIV advisory mode）；产品层 8＋CI/review bot 5＋SDD 工具 2＋个人实践 2＋裁判谱系论文 6＋工具链 2＋METR 反例 1＋学术层 2 |
| [`insights.md`](insights.md) | ✅ 初盘 5 条＋深挖批 8 条（失效四机理与三族防护、分离度三维度、CI-as-judge 断面、判判定器三形态、输出契约坑、SDD 修正、end-state oracle 汇合点、advisory mode 渐进路径） |
| 新回源 | ⏳ 深挖批主体已收口；**第二批**：ReliabilityBench + Augment CIV 入 [evidence-r](../../raw/evidence-2026-09-28-r-ial-scan-reliability.md)；Spec Kit 旧 tag 考古、CodeRabbit slop-detection 子页、Graphite 底层模型登记待挖 |

## 待挖清单

1. ~~裁判权五极的选型依据~~ → **大幅推进**：改为"分离度三维度"选型（判据可见性/执行位置/判定权归属，insights #7）——维度框架已立，各场景推荐组合仍开放。
2. ~~evaluator 的模型选型~~ → **推进**：promptfoo/Braintrust 给出 judge 独立选型与人类对齐校验法（evidence-m S7/S8）；"快 vs 准"的官方理由仍缺。
3. ~~验收标准从哪来~~ → 仍开放（新增 spec-kit spec/plan/tasks 源一例）。
4. ~~同源污染~~ → **已答（研究域）**：self-preference 受控实证＋线性相关（evidence-m S5）；生产 coding 场景的实例仍缺。
5. ~~SDD 阵营对照~~ → **已答**：converge 口径＋OpenSpec 不阻断＋"completion claims are not evidence"（evidence-n S6/S7）。
6. ~~Horthy 打断点归属~~ → 仍开放（未再挖）。
7. **新开口**：判据内容可见性作为设计维度（METR 43×归因）——对判据保密 vs 可见的 trade-off 待挖（对抗可测性 vs 白盒协作）。
