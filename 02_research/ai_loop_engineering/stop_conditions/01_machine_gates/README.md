# ① 机器可核判据逐轮闸门（machine gates）

**本点回答**：每轮"接受/拒绝"由什么判？判据从哪来？怎么防判据被当事人废掉？

**判定句**（权威在 [`../../digested/03-构件.md`](../../digested/03-构件.md) §一）：
测试/类型/linter/静态分析/构建退出码做逐轮闸门（Huntley 称 back pressure，LangChain 称 grader）；
判据的可核性来自**环境 ground truth**，编码域天然适合（"Code solutions are verifiable through automated tests"，Anthropic 2024）。
≥2 独立一手同向：Huntley / Anthropic 2024 / Anthropic 2025 / LangChain 四家。

## 看板

| 件 | 状态 |
|---|---|
| [`practices.md`](practices.md) | ✅ 初盘 2026-09-28：9 条做法，全部从既有 evidence（a/b/i）过筛登记，未做新回源 |
| [`insights.md`](insights.md) | ✅ 初盘：6 条洞察＋开放问题 |
| 新回源 | ⏳ 未开始（待挖清单见下） |

## 待挖清单

1. **grader 选型依据**：deterministic 与 agentic（LLM-as-judge）两类的适用边界——什么错误类别只能靠哪类抓（LangChain 案例只有 docs writer 一例，evidence-b §4e）。
2. **grader 失败模式**：判据被讨好/钻空子的实例（auto-review 已官方自述可被误导批准命令，OpenAI；测试 gaming 的具体形态待回源）。
3. **非编码域的可核判据**：docs/迁移/分析类任务怎么做逐轮闸门（现行四家证据全是编码域）。
4. **端到端自验证的工程细节**：browser automation 具体怎么配、成本多大（Anthropic 2025 只给了方向句，evidence-b §3）。
5. **行为面验证（behaviour harness）**：门拦"做错事"，拦不住"该做的没做"（Böckeler 点名的公认缺口）——候选做法待挖。
6. **判据的维护**：测试/清单本身谁来写、谁来更新、失效判据怎么被发现。
