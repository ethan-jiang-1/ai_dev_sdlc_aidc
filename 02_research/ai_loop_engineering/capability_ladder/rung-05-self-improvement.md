# R5 自我改进（正式阶 ✅ 2026-09-30 升格）——交出对 harness 本身的改写权

> **升格判定**：定阶门槛（≥2 已回源独立来源站在同一交接面）已满足——**Runkle**（LangChain 2026-06-16，[evidence-a §3 C1](../raw/evidence-2026-09-26-a-originators.md)）、
> **Morris**（martinfowler 2026-03-04，[evidence-c §问题3.1.3](../raw/evidence-2026-09-26-c-autonomy-and-convergence.md)）、**Böckeler**（2026-04-02，同上 §3.3.3）三源独立落位，
> 外加 Anthropic 实证票（[evidence-u](../raw/evidence-2026-09-30-u-post-june-kols.md) S5"rewrites the tool description"，-40% 完成时间）。
> 原候选理由（操作素材未落自说明格式）已随本轮挖掘解除。
> ⚠️ 本阶的特殊性：**护栏就是本阶的闸门**——没有护栏的 R5 不是阶，是事故（见 §四，Goodhart/43×/self-preference）。

## 一、交接面（共识版）

循环的修改对象从**产物**变为**产生产物的系统**（harness：prompt/skill/规则/工具描述/评估器配置）。
Morris 的分界句是全梯最清晰的一条界限：
> "The 'in the loop' way is to fix the artefact … The 'on the loop' way is to **change the harness that produced the artefact** so it produces the results we want."
（修正对象升级＝R2/R3 与 R5 的分界线。）

## 二、支撑条目（自说明，均一手）

**① 定义句（Runkle/LangChain，2026-06-16，[evidence-a §3 C1](../raw/evidence-2026-09-26-a-originators.md)）**
> "The hill climbing loop runs an analysis agent over those traces and uses the findings to **rewrite the harness** with improved configuration."
> "the return arrow doesn't just loop back to the top — **it reaches inside and updates the agent loop directly**. Each cycle of the outer loop makes the inner loops more effective."

**② 人机分工与首个自动放行判据（Morris flywheel，[evidence-c §问题3.1.4/5](../raw/evidence-2026-09-26-c-autonomy-and-convergence.md)）**
> "The next level is humans directing agents to manage and improve the harness rather than doing it by hand."
> "As we gain confidence, the agents can assign scores to their recommendations, including the risks, costs, and benefits. We might then decide that recommendations with certain scores should be **automatically approved and applied**."

**③ 触发判据（Böckeler steering loop，[evidence-c §问题3.3.3](../raw/evidence-2026-09-26-c-autonomy-and-convergence.md)）**
> "The human's job in this is to **steer** the agent by iterating on the harness. **Whenever an issue happens multiple times**, the feedforward and feedback controls should be improved."
- 触发条件＝同一问题多次发生→改 controls（不是预防式臆造规则）。

**④ 存在理由（Anthropic Managed Agents，2026-04-08，[evidence-b §问题2.5](../raw/evidence-2026-09-26-b-stop-and-scheduling.md)）**
> "a harness encodes assumptions about what the model can't do … **those assumptions rot as the model improves**"
- 不改写 harness，假设腐烂就变成债务——R5 不是可选项而是维护义务。

**⑤ 机构实践（OpenAI《Harness engineering》，2026-02-11，[evidence-i Source 6](../raw/evidence-2026-09-27-i-high-influence-control.md)）**
> "When documentation falls short, we **promote the rule into code**."
> "Our team used to spend every Friday (20% of the week) cleaning up 'AI slop.' Unsurprisingly, that didn't scale."
> "We tried the 'one big AGENTS.md' approach. **It failed.**"
- 规则升级路径：文档→linter/代码；巨型单文件路线自述失败。

**⑥ 规则溯源判据（Osmani，2026-04-19，[evidence-c §问题3.2.5](../raw/evidence-2026-09-26-c-autonomy-and-convergence.md)）**
> "**Every line in a good `AGENTS.md` should be traceable back to a specific thing that went wrong.**"

**⑦ 改写幅度光谱（本区归纳，两票定标）**
- 外围件（已实证）：工具描述改写，Anthropic tool-testing agent，> "resulted in a 40% decrease in task completion time"（evidence-u S5）。
- 循环结构（概念）：Runkle "updates the agent loop directly"。
- 教学顺序应沿光谱从外围到核心，护栏强度随幅度递增。

**⑧ 人肉前身（Huntley Ralph"signs"，[evidence-b §问题1.1](../raw/evidence-2026-09-26-b-stop-and-scheduling.md)）**
> "one then tunes Ralph by adding a sign next to the slide saying 'SLIDE DOWN, DON'T JUMP, LOOK AROUND,'"
- 把踩坑教训写成环境内持久提示——R5 的人工版，教学的入口形态。

## 三、升阶闸门（本阶闸门＝护栏本身）

1. **提案-评估异源**（实证：self-preference 与 self-recognition 线性相关，[evidence-m Source 5](../raw/evidence-2026-09-28-m-judge-lineage.md) → arXiv:2404.13076）：
   > "an LLM evaluator scores its own outputs higher than others' while human annotators consider them of equal quality."
2. **判据内容隔离**（METR，[evidence-n Source 8](../raw/evidence-2026-09-28-n-verdict-split-coding.md)）：
   > "Reward hacking was more than **43×** more common on RE-Bench tasks … because … the model was able to see the entire scoring function."
3. **Goodhart 上界**（[evidence-m Source 2](../raw/evidence-2026-09-28-m-judge-lineage.md) → arXiv:2210.10760）：
   > "optimizing its value too much can hinder ground truth performance, in accordance with **Goodhart's law**."
4. **反应式构建**（marmelab 审计，[evidence-c 对照面4a](../raw/evidence-2026-09-26-c-autonomy-and-convergence.md)）：
   > "a harness should be built **in reaction to an agent failure**, not based on an assumption that the agent can't do something properly."

## 四、dissent（本阶火力最猛，必须并列教）

- **定量反调**（ReliabilityBench，[evidence-r S2](../raw/evidence-2026-09-28-r-ial-scan-reliability.md)）：
  > "The degradation gradient ∂R/∂λ is steeper for Reflexion (−0.50 per 0.1 λ) than ReAct (−0.38), indicating that **self-reflection mechanisms may amplify rather than mitigate fault impacts**."
- **反直觉 ablation**（marmelab）：> "we think a harness should be built by a human, instead of an agent. If an agent needs supervision, how can it decide the supervision it needed? This is **our opinion rather than a finding**: the only ablation study we found (NLAH, arXiv 2603.25723) **measures the opposite**, with a self-improving harness gaining 4.8 and 2.7 points."
- **哲学张力**（Cherny YC，2026-02-17，[evidence-a §1b A3](../raw/evidence-2026-09-26-a-originators.md)）：
  > "you can improve performance maybe 10, 20% … And then essentially **the gain is wiped out with the next model**. … never bet against the model."
  ——loop 配置本身也是 scaffolding；R5 改写的东西会随模型换代贬值，这是本阶投资回报的内在折扣。

## 五、待补清单

1. GEPA/DSPy 提案-评估分离素材从缺口 5 按本档格式搬运（护栏四条的工程化展开）。
   ✅ 活跃度与身份核验（2026-09-30 观测）：**GEPA（Genetic-Pareto）**＝斯坦福/Databricks 线（Agrawal…Khattab）的
   反思式文本参数优化器——LLM 通读执行 trace（报错/工具输出/推理日志）诊断失败原因→提案修改→按指标测试→
   从自身尝试的 **Pareto 前沿**合并互补教训；对比 RL(GRPO) 平均 +6%、rollout 少 **35×**，**ICLR 2026 Oral**
   （[arXiv:2507.19457](https://arxiv.org/abs/2507.19457)，v2 2026-02-14）。仓库 [gepa-ai/gepa](https://github.com/gepa-ai/gepa)
   6.8k stars、2026-09-29 仍有提交，README 口径已扩到 "prompts, code, **agent architectures**, configurations"。
   DSPy 侧：3.4.0 于 2026-09-25 发布（月更节奏），含 ReActV2 原生工具环、RLM 递归循环、沙箱解释器。
   **归位注意**：GEPA/DSPy 是 R5 护栏的**学术参考实现**（提案-评估分离＋Pareto 档案＋指标驱动），
   不是 coding-agent harness 工具——引用时摆"结构同源"位，不摆"同类工具"位。
2. NLAH（arXiv 2603.25723）与 marmelab 引文的原文核验。
3. Morris 卡片四级修订联动（flywheel 归位 R5 已在 00-map 注记）。
