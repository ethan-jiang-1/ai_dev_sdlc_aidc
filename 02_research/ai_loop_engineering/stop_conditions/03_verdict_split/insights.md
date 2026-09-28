# ③ 验收与干活分离 — 思考洞察与失败模式

> 初盘 2026-09-28。每条带来源指针；判定级表述以 [`digested/03`](../../digested/03-构件.md) 为准。

1. **分离的动因是利益冲突，不是能力分工**。auto-review 给出了最清楚的一句官方理由：干活的模型优化"完成任务"，会把一切边界（包括验收）当"又一个要克服的障碍"（evidence-b §4d）。所以干活模型自判完成＝让当事方当自己的法官——这与①的目标敌人（提前宣告完成）**直接同构**，这就是"最弱一极"的机制解释。

2. **分离 ≠ 判得对**。分离解决利益冲突，不解决裁判能力：`/goal` 的 evaluator 官方澄清只核 transcript 里的 hard rules，"不看内容好不好"（evidence-a）；LLM-as-judge 可被讨好（与①的 grader 风险共享）。上屏时"用了独立 evaluator"不能被暗示成"验收质量有保证"。

3. **防当事人改写裁判有两招，打在两个部位**：**输入防操纵**（auto mode 分类器 reasoning-blind——裁判只看原始对话与动作，不看当事人的自辩）与**判据防改写**（测试不可删改 / 只许改 `passes` 字段 / Beck 删测试＝作弊——护的是裁判依据的本体）。一招护输入、一招护本体，互不替代（evidence-b §3/§4b）。

4. **裁判权五极是选型空间，不是成熟度阶梯**。五极（人判/清单/独立模型/自判/审批方）之间没有"高级→低级"关系，只有任务信任级别与成本的匹配；把它画成进化序列就越界（digested/03 §一"这不是缺陷，是设计空间"；实践层已落成选型表）。

5. **Ralph 与 Claude Code 是两极活样本**：Ralph 把完成判定整个外置给人（TODO 耗尽是 taste，清单随时可扔）↔ Claude Code 把它做成每轮运行的原语（小模型三值判定）。两极都活着，说明③的实现位置和①②一样开放（evidence-b §1/§4a）。

## 开放问题

- 小快模型当裁判的判定力边界（`/goal` 用 small fast model——为什么"快"优先于"准"，官方没说）。
- 裁判与干活模型同源时的污染证据（目前只有正向说法）。
- 验收标准的生成路径分布：initializer 生成（Anthropic）/ reviewer 持有（Spec Kit）/ 人写——各自适用场景。
- Codex 候选（assistant message 终止态）若复核成立，"干活模型自判"一极会获得最强的机制描述——值得优先回源（README 待挖关联 evidence-k）。

## 增补（2026-09-28 深挖批：evidence-m/n）

6. **"分离≠判得对"从直觉升级为有实证清单的机理谱**。四类失效机理各不相同：**顺序劫持**（调换候选即翻转 66/80——输入构造缺陷）、**self-preference**（裁判偏自己的输出，与 self-recognition 线性相关——同源利益冲突）、**谄媚偏好**（对 PM 优化牺牲真实性——目标信号本身脏）、**Goodhart 过优化**（对 proxy RM 优化过度损害真实表现——代理目标失真）。对应三族防护：**异源化**（模型分离）、**输入校准**（位置平衡/剔除 system prompt 污染/证据先行）、**目标节制**（KL 预算/花费帽）。选防护族之前先问失效机理是哪类（evidence-m）。

7. **"分离度"是可设计的连续量，三个维度彼此独立**：①判据内容可见性（METR：判定代码对 agent 可见时被绕过率高 43×——判据对干活者**保密**也是分离的一部分）；②判定执行位置（同 agent 会话内〔spec-kit converge/OpenSpec〕vs 独立进程〔CI/review bot/另一 agent〕vs 独立模型调用〔/goal/auto-review〕）；③判定权归属（模板约束自判 vs 独立判定 vs 人）。现有各家做法都能在这三个维度上定位，选型表可以按维度重写（evidence-n S6–S8；evidence-m）。

8. **CI-as-judge 的历史断面**：2025-05 的 dotnet PR 里 CI 判定进 agent 循环**靠维护者人肉转述日志**；2026 年 GitHub 把"CI 失败→agent 修"做成一键按钮、Devin 给出完整 workflow YAML。机制一年内从人工中转走到产品化——但两者都保留"人终审"。CI 判定的信号是 job 结论（机器可核），它天然是③与①的交界：判定信号来自环境闸门（①），判定权在流水线不在模型（③）（evidence-n S1–S3）。

9. **"谁来判判定器"已有三种实战形态**：Graphite 的元评估（每条 rule 的 acceptance rate/投票率——用户反馈闭环）、METR 的另一模型 monitor＋人工复核（两法互漏、检出数疑低估）、isitdone 的削弱测试检测器＋192 例标注基准。共同点：裁判的准确性被当成**需要单独测量的量**，不是默认可信（evidence-n S5/S8；evidence-p S1）。

10. **裁判输出契约本身有生产级坑**：promptfoo 实录——模型漏返 `pass` 字段且未设 threshold 时，score 0 也默认放行。判定接口的设计（显式 boolean、缺省语义、threshold 双条件）与模型选型同等重要（evidence-m S7）。

11. **SDD 阵营修正**（对 evidence-f 旧条目）：Spec Kit 的 /verify 已不在现行命令集（404），判定职能并入 implement→converge；其反自判设计（"completion claims are not evidence"＋append-only＋字节不变约束）说明**同 agent 自判是默认形态，模板防御是补偿**——与 OpenSpec "verify 不阻断 archive" 互证：SDD 工具的完成判定权实际也留在干活 agent 手里，独立性靠约定而非机制（evidence-n S6/S7）。

12. **end-state oracle 是 ①+③ 的汇合点**（2026-01）。ReliabilityBench 用 deterministic state-based oracle 代替 LLM judge 或文本匹配，把"完成"定义为"end-state 等价"（Action Metamorphic Relations）：同语义任务应产生相同最终环境状态（`reservations[flight_id].status == "confirmed"`）。这在学术层确认了 ① 的"环境 ground truth"在非编码域同样可行，也为 ③ 的"裁判输出契约"提供了可量化的实现形态——不是问 LLM"做完了吗"，是断言环境状态（evidence-r S2）。

13. **advisory mode 是 hard gate 的渐进部署路径——分离度可以逐步提升**（2026 观测）。Augment Code 的 CIV 模式：Verifier 先跑 advisory mode（不阻断，只评论），收集 false-approve rate 数据，校准 spec 准确性；达标后升级为 blocking hard gate。这与 ③ insight #7 的"分离度三维度"对应：执行位置从"同 agent 内"到"独立 PR bot advisory"再到"独立 bot blocking"，是连续可控的升级。工程含义：③的部署不是非此即彼，可以从最低分离度开始逐步强化（evidence-r S4）。

14. **物理沙盒（Worktree）+ Living Spec 使得“分离”从提示词约定进化为架构契约**（2026 演进）。在 Intent/Cosmos 架构中，实现（Implementor）必须在隔离的 git worktree 中并行，无法触碰外层协调上下文；验证者（Verifier）不看 Implementor 的自我证明，只根据 Coordinator 产出的 Living Spec 与环境运行事实做比对。这推进了 insight #7 的“执行位置分离”：以往仅是 session/prompt 分离，2026 年已下沉到文件系统与进程空间隔离（evidence-s S3）。
