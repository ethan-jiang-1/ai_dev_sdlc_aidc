# ① 机器可核判据逐轮闸门 — 思考洞察与失败模式

> 初盘 2026-09-28。每条带来源指针；判定级表述以 [`digested/03`](../../digested/03-构件.md) 为准。

1. **裁判不会说谎——闸门的本体论**。判据的可核性来自环境 ground truth（工具结果、退出码、测试结果），不来自模型的自我报告。back pressure 的全部意义是把"这轮算不算过"从模型嘴里挪到环境里（Huntley，evidence-b §1；Anthropic 2024，evidence-b §2）。这是三件骨架里最"硬"的一件：②和③都在处理"判据失效之后怎么办"，①处理的是"判据本身从哪来"。

2. **闸门的目标敌人是占位实现，不是错误**。Huntley 亲述的失败模式是模型 "reward function is compiling code"——编译过就行，占位实现满天飞；Anthropic 官方点名的是"提前宣告完成"（evidence-b §1/§3）。闸门拦的不是"写错了"，是"没写完就说写完了"。

3. **deterministic 与 agentic 是两条不同的信任线**。确定性 grader（测试/CI/退出码）信任环境；agentic grader（LLM-as-judge）信任另一个模型——后者把①的"不会说谎"属性稀释成了"另一个模型的说谎概率"，选型依据是待挖问题（LangChain，evidence-b §4e）。

4. **保护判据本体与保护裁判输入是两招不同的防改写**。本点的保护是**判据防改写**（测试不可删改、JSON 选型、只许改 `passes` 字段、Beck 的"删测试＝作弊"）；③那边的一招是**裁判输入防操纵**（auto mode 分类器 reasoning-blind）。同一族威胁——当事人改写裁判——打在两个不同部位，配罩时别混（evidence-b §3/§4b）。

5. **行为面是公认的缺口**：门能拦"做了不该做的"，拦不住"没做该做的"。Böckeler 点名 behaviour harness 是"减监督"路线的公认缺口；Yegge 的 "A missing test is a passing test" 是它的个体样本（digested/03 §三已知短板；evidence-i Source 5）。**过闸门 ≠ 做对了事**——这句边界话在上屏材料里必须跟着①走。

6. **可核性是域依赖的**。四家一手证据全部出自编码域（代码可自动化测试、问题空间结构化）；非编码域的可核判据目前 0 条一手做法，不能默认①在别的域也成立（evidence-b §2 四条件原文只给了编码域的成立理由）。

## 开放问题

- LLM-as-judge 的可操纵面有多大？（与③的"分离≠判得对"共享）
- 端到端验证（browser automation）的成本/可靠性——Anthropic 只给了方向，没给账单。
- 判据老化：测试本身错了他就照错判——谁复核裁判？
