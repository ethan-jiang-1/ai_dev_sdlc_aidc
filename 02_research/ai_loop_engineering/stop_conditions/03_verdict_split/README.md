# ③ 验收与干活分离（verdict split）

**本点回答**：完成由谁判？裁判怎么才不被干活的一方操纵/收买？判定权归属有哪几极？

**判定句**（权威在 [`../../digested/03-构件.md`](../../digested/03-构件.md) §一）：
验收与干活角色分离，五处一手同向跨三家（Anthropic 2024/2025、CC `/goal`、OpenAI auto-review、LangChain）；
**唯一未收敛点＝裁判权归谁**（五极设计空间），干活模型自判与"提前完成"直接冲突，是最弱的一极。

## 看板

| 件 | 状态 |
|---|---|
| [`practices.md`](practices.md) | ✅ 初盘 2026-09-28：11 条做法（含 1 条候选未复核），来自既有 evidence（a/b/f/i/k）＋ digested/03 判定，未做新回源 |
| [`insights.md`](insights.md) | ✅ 初盘：5 条洞察＋开放问题 |
| 新回源 | ⏳ 未开始（待挖清单见下） |

## 待挖清单

1. **裁判权五极的选型依据**：什么任务/信任级别配哪一极裁判（人判/清单/独立小模型/自判/审批方）——实践层已做成选型表骨架，依据列仍薄（指针见 [`03_practice/loop_governance/`](../../../../03_practice/loop_governance/README.md)）。
2. **evaluator 的模型选型**：`/goal` 用 small fast model——小模型的判定力边界在哪，有没有"裁判必须比干活者强/弱"的公开讨论。
3. **验收标准（rubric/清单）从哪来、谁维护**：Anthropic 是 initializer agent 生成 feature_list；别的路径（人写、reviewer 写、模型自写）证据分布待回源。
4. **同源污染**：裁判与干活模型同源（同一家/同一个模型）时的污染证据——目前只有 auto-review"便于评估监控改进"的正向说法。
5. **SDD 阵营的验收分离**：Spec Kit / OpenSpec 的 reviewer-owned checklist 与 loop 阵营的 grader/evaluator 异同——跨阵营对照还没人做过（evidence-f 只有机制条目）。
6. **Horthy 的打断点**（工具选定与执行之间）与完成判定的关系——它管的是授权时机不是完成，归③还是单列，等挖到更多材料再定（evidence-i Source 4）。
