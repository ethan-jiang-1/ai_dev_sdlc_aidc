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

## 增补（2026-09-28 深挖批：evidence-p/l/m）

7. **"完成宣告无测试背书"首次被个人量化：65%**。单人 591 会话、516 条完成宣告（isitdone 两版口径 69%→65%）。这是"提前宣告完成"这个目标敌人的**首个个体量化数据**——但单人样本，只说明"这事真实且频繁"，不外推比例（evidence-p S1）。

8. **闸门装在哪一层是首要工程决策**。四层可选：prompt 层（官方 demo——判据全在文本里，驱动零检查）、Stop-hook 层（isitdone——声称时刻、当前工作树）、commit 层（pre-commit——"声明已作出，我已走开"）、CI 层（最晚）。isitdone 作者的排序有明确理由：闸门必须在 claim 发生处，否则拦截的是下一次而非这一次（evidence-l S1/S3；evidence-p S1/S2）。

9. **"测试外置于 agent"在两个独立域汇合**。Ken Imoto 从实战得出"If the agent writes both the code and the tests, you get circular validation"；M 档 self-preference 论文给出受控实证（LLM 裁判偏自己的输出，self-recognition 与偏私线性相关）。实战直觉与研究实证同指一处——自评失效是跨域共识（evidence-p S3；evidence-m S5）。

10. **非编码域的①成立，且同构**：docs（退出码即事实）、data（执行结果预览）、math（内核接受/拒绝即停判）、security（扫描器 exit-1）。共同抽象＝**把"事实"与"声称"分开**——可核性不依赖域，依赖是否存在环境侧的判定器。SQL/Great Expectations 域仍未收口（evidence-p 负结论）。

11. **闸门自己也需要停止条件**（与②交界）：isitdone 3 次放行＋"能弄死 agent 的闸门一天内就会被卸载"；OpenHands stuck detector 因长任务误报改可配置。闸门的误报率是真实工程参数，不是理论顾虑（evidence-p S1；evidence-o S5）。

12. **防"削测试转绿"已有可复核的工程化**：检测器清单（skip/删文件/断言降级/|| true/-DskipTests）＋192 例标注基准（0/89 误报、102/103 拦截）＋默认 warn 严格 block。行为面缺口（原第 5 条）由此从"公认缺口"推进到"有可部署的局部解"——但作者自认"不是 lie detector，拦的是诚实错误（约三分之二）"（evidence-p S1）。

13. **back pressure 的最简实现只有三行**：Aider 的 `if lint_errors: ok = confirm_ask("Attempt to fix lint errors?"); reflected_message = lint_errors`——非零退出码→确认→错误文本回灌成下一轮输入。Huntley 的 "back pressure" 概念与 LangChain 的 "grader" 概念，落到框架源码就是这个形状；**闸门不需要复杂机制，需要的是"错误必达模型"的通道**（evidence-q S1）。

14. **闸门的出厂缺省没有共识**：Aider auto-lint 默认开、OpenHands enable_auto_lint 默认关（同一构件、相邻框架、相反缺省）。缺省状态是产品对"用户会不会自己配"的押注——对使用者的工程含义：**别信默认，显式配闸**（evidence-q S1/S2；与② insights #13 同源）。

15. **静态分析首次量化"闸门放错位置"**（2026-07）。IAL-Scan 对 6,549 个真实 agent 仓库扫描，发现最常见 IAL 类型之一是 tool-call iteration without bounds（工具调用迭代无上限）——这正是①闸门失效的对应面：闸门通道里不只有测试/lint，还有 tool dispatch；当工具调用进入无界 feedback loop 时，①的闸门覆盖不到。两个失效模式：bound 不存在（忘加）vs bound 在错误层（framework API 外面有上限但实际 feedback path 不受控）。工程含义：在 LangGraph/AutoGen 等框架里，工具调用反馈路径需要单独核查 bound coverage，不能默认框架帮你兜住（arXiv:2607.01641，evidence-r S1）。
