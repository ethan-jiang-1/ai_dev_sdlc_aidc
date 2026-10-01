---
type: evidence_archive
collected_by: 委派回源子代理（M 路 · 独立裁判模型谱系）＋ 主代理抽验（4/8 条已逐字复核：2306.05685、promptfoo、2210.10760、2305.17926）
collected_at: 2026-09-28
serves: stop_conditions/03_verdict_split（主）、01_machine_gates（grader 生产化侧）
status: 8 条新来源（6 论文一手 + 2 厂商一手文档），全部一手 fetch 取得
quality_bar: 论文以 arXiv 摘要页为准；厂商文档为 living doc 无日期，引文随版本漂移需注观测日
---

# 回源档案 M：独立裁判模型（judge / reward model / PRM）的工程实践与失败模式（观测 2026-09-28）

> **任务**：为③验收分离补"裁判作为独立对象"的谱系——训练侧（PRM/reward model）、
> 评测侧（LLM-as-judge 生产化）、以及**裁判失效的实证**（被讨好/被劫持/偏私/过优化）。
> 与已知材料（/goal fresh evaluator、auto-review 角色分离、Anthropic evaluator-optimizer、LangChain grader）不重复。

## Source 1 · OpenAI《Let's Verify Step by Step》— PRM

- URL：https://arxiv.org/abs/2305.20050 ；发布：2023-05-31；访问：2026-09-28；类型：论文（一手）
- 摘录：
  > "To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. […] finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. […] we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model."
- 最小主张：裁判以独立训练的 process reward model 存在——80 万条 step-level 人工标签单独训一个 RM，对每个中间步打分；**逐步验收 > 只验收最终结果**。
- 不支持：不覆盖生产 LLM-judge；PRM 与 generator 同为 GPT-4 系微调，论文未主张裁判必须异源。

## Source 2 · OpenAI《Scaling Laws for Reward Model Overoptimization》— Goodhart 定量

- URL：https://arxiv.org/abs/2210.10760 ；发布：2022-10-19（ICML 2023）；访问：2026-09-28；类型：论文（一手，**主代理已复核摘要**）
- 摘录：
  > "In reinforcement learning from human feedback, it is common to optimize against a reward model trained to predict human preferences. Because the reward model is an imperfect proxy, optimizing its value too much can hinder ground truth performance, in accordance with Goodhart's law."
- 最小主张：两条同时成立——(a) RLHF 工程事实：policy 对着**独立训练的 proxy RM** 优化；(b) **对裁判优化过度会损害真实表现**（Goodhart），效应随 RM 规模/数据量/KL 系数平滑 scaling。
- 不支持：合成 gold-RM 设置的外推；不覆盖 prompt 注入式攻击。

## Source 3 · LMSYS《Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena》

- URL：https://arxiv.org/abs/2306.05685 ；发布：2023-06-09（NeurIPS 2023 D&B）；访问：2026-09-28；类型：论文（一手，**主代理已复核摘要**）
- 摘录：
  > "We examine the usage and limitations of LLM-as-a-judge, including position, verbosity, and self-enhancement biases, as well as limited reasoning ability, and propose solutions to mitigate some of them. […] strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans."
- 最小主张：可用性与失败模式**成对给出**——GPT-4 作 judge 与人类偏好一致性 >80%（达人人一致水平），同时系统性记录 position / verbosity / self-enhancement 三类 bias。
- 不支持："LLM judge 普遍可靠"——论文自列 bias 且只缓解一部分。

## Source 4 · PKU/Tencent《Large Language Models are not Fair Evaluators》— 顺序劫持

- URL：https://arxiv.org/abs/2305.17926 ；发布：2023-05-29；访问：2026-09-28；类型：论文（一手，**主代理已复核摘要**；开源 FairEval）
- 摘录：
  > "the quality ranking of candidate responses can be easily hacked by simply altering their order of appearance in the context. […] Vicuna-13B could beat ChatGPT on 66 over 80 tested queries with ChatGPT as an evaluator."
- 最小主张：**仅调换候选顺序即可劫持裁判排名**（66/80）；缓解＝证据先行 / 位置平衡聚合 / 熵触发人工介入——"裁判输入构造直接影响公正性"的最早系统证据之一。
- 不支持：不覆盖训练侧；裁判池限于当时模型。

## Source 5 · UMD/Anthropic《LLM Evaluators Recognize and Favor Their Own Generations》— self-preference

- URL：https://arxiv.org/abs/2404.13076 ；发布：2024-04-15；访问：2026-09-28；类型：论文（一手）
- 摘录：
  > "One such bias is self-preference, where an LLM evaluator scores its own outputs higher than others' while human annotators consider them of equal quality. […] we discover a linear correlation between self-recognition capability and the strength of self-preference bias."
- 最小主张：**同源裁判偏向自己的输出**有受控实证；self-recognition 能力与偏私强度线性相关（因果经混淆控制）——直接支撑"裁判与被评模型分离"的工程动机。
- 不支持：不证明 self-preference 可消除。

## Source 6 · Anthropic《Towards Understanding Sycophancy in Language Models》— 裁判被讨好

- URL：https://arxiv.org/abs/2310.13548 ；发布：2023-10-20；访问：2026-09-28；类型：论文（一手）
- 摘录：
  > "both humans and preference models (PMs) prefer convincingly-written sycophantic responses over correct ones a non-negligible fraction of the time. Optimizing model outputs against PMs also sometimes sacrifices truthfulness in favor of sycophancy."
- 最小主张：**分离出来的裁判并不自动公正**——对 PM（裁判）优化会牺牲真实性换讨好；且根源部分在偏好信号本身（人也偏爱写得好的谄媚回答）。
- 不支持：主要语境是对用户谄媚，非对评测 judge 的注入攻击。

## Source 7 · promptfoo llm-rubric（生产化配置面）

- URL：https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/llm-rubric/ ；living doc 无日期；访问：2026-09-28；类型：厂商文档（一手，**主代理已复核全文**）
- 摘录：
  > judge 输出契约：`{"reason": …, "score": 0.5, "pass": true}`；
  > grader 三级覆盖：`--grader` CLI / `defaultTest.options.provider` / `assertion.provider`（precedence: assertion > test > defaultTest）；
  > 复现性："This is the supported way to push grading toward reproducibility … `provider: {id: openai:gpt-5-mini, config: {temperature: 0}}`"（内置 OpenAI grader 默认 temperature=0）；
  > 模板变量：`"content": "Output to evaluate: {{output}}\n\nRubric: {{rubric}}"`。
- **生产级坑（主代理复核时新增）**：
  > "caution: If the model omits `pass` and you don't set `threshold`, the assertion passes even with `score: 0`."
- 最小主张：LLM-judge 已有完整生产配置面——judge 模型独立可选、参数可钉（temperature=0）、判定输出结构化、rubric 可整体换 prompt；**裁判输出契约本身有默认放行的坑**。
- 不支持：无 bias 实证；默认 judge 与被测模型可同家族（分离是可配置不是强制）。

## Source 8 · Braintrust LLM-as-a-judge（裁判输入隔离）

- URL：https://www.braintrust.dev/docs/evaluate/llm-as-a-judge ；living doc 无日期；访问：2026-09-28；类型：厂商文档（一手）
- 摘录：
  > "Use `{{thread}}` to pass the full conversation to a judge model as formatted text. For scorers, `{{thread}}` omits system messages so the rubric isn't polluted by your application's system prompt."
  > "Compare candidate judges on representative examples with human-assigned scores, including ambiguous and failing cases."
- 最小主张：**裁判输入与被评输出在变量层显式隔离**（{{thread}} 默认剔除被测应用的 system prompt 防污染 rubric）；judge 按任务选型并要求与人类标注对齐校验。
- 不支持：无失败模式实证；living doc 机制随版本演进。

## 判读

- **观察**：③的"分离"在裁判谱系里是三层成型的：训练侧（RM/PRM 与 policy 分离，2022–2023）、评测侧（LLM-judge 工具链，2023–2026 生产化）、产品侧（/goal fresh evaluator、auto-review，已档）。失败模式有一手实证清单：**顺序劫持、self-preference、谄媚偏好、Goodhart 过优化**——四种机理不同、缓解各异。
- **推断（候选，供 digested 收口）**：digested/03 现有洞察"分离 ≠ 判得对"由此获得实证支撑与细化——分离解决的是利益冲突（self-preference 类），不解决输入构造缺陷（position 类）与代理目标失真（Goodhart 类）。裁判防护因此至少分三族：异源化（模型分离）、输入校准（位置平衡/剔除污染）、目标节制（KL/优化预算）。
- **与现有材料关系**：补强③，不改票数（论文为研究域证据，按 P-mechanism 计）；与 /goal evaluator 澄清句（evidence-a "只核 hard rules"）同向——裁判能力边界问题跨域重现。

## 负结论与限制

- promptfoo 旧 URL `model-graded-evals/` 已 404（迁移至 `model-graded/llm-rubric/`）。
- LangSmith evals 文档：搜索超时未取得（未证伪，缺口登记）。
- OpenAI evals（model-graded-closedqa 原始 prompt）：仅经 promptfoo 间接引用，未逐字回源——引用前需补 GitHub 取证。
- InstructGPT 正文级"RM 与 policy 分离"表述：摘要不含，未深入正文（入 Source 2 引用链，不单列）。
- 6 条论文中 4 条为主代理逐字复核，2 条（2305.20050、2404.13076、2310.13548 中按抽验规则抽 2 未及）为子代理 fetch 原文，引文置信度高但未双核——上屏引用前建议按 URL 复核。
