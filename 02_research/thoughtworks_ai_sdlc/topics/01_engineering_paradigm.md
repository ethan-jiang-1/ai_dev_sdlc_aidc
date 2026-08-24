# Deep Research Topic 01: 工程纪律重构与“质量防线”的转移
(The New Engineering Paradigm)

## 1. Topic 核心定义
当 AI 智能体全面接管代码生成，代码本身逐渐成为一种“按需生成且廉价的副产品”。基于此，软件工程的“严谨性”并未消失，而是急剧向上游（需求规格）和周边（测试、约束）转移。传统的代码审查防线失效，取而代之的是由 TDD（测试驱动开发）、形式化约束和风险映射构成的“新质量防控自动化底座”。

## 2. 行业宏观与技术商业视角 (Industry & Tech-Business View)
* **产业破局点**：旧的防线被突破，软件工程过去十年积累在代码审查、静态扫描工具上的流程架构面临重写。未来的核心价值将从单纯的“代码生成能力”向“系统验证与质量约束能力”转移。
* **技术演进与实践方向**：行业亟需高度结构化的需求格式（如现代化的 EARS 或状态机生成器）、以及能将 TDD 转化为 AI Agent 可靠“护栏”的基础设施和开发流水线平台。

## 3. 深度的背景与上下文 (Imported Context)
* **上移至规格说明评审**：“预先评审计划，事后评审工程”。如果 AI 根据规格说明生成代码，那么规格说明就是捕获错误的最高杠杆制品。糟糕的规格说明会大规模地产生糟糕的代码。传统的用户故事太模糊，团队正在重新采用结构化方法（状态机、决策表）。
* **转入测试套件，使之成为一等制品**：TDD 能从 AI 编码智能体中获得显著更好的结果。TDD 被重新定义为一种“提示工程”，测试先于代码存在，防止了智能体编写测试验证其错误行为的失败模式。
* **转入类型系统与约束**：探索如何让错误的代码“无法被表达”。将规格说明（改变什么）与约束（不能触碰什么、爆炸半径）分离。当必须打破约束时，提示系统需要重构。
* **转入持续理解与 XP（极限编程）复兴**：当代码变化极快，传统通过 Review 建立的系统理解崩塌。团队正在通过重拾极密的 XP 实践（结对编程、集体代码所有权、高频持续集成）来对抗因代码泛滥而造成的“认知债务”。
* **DORA 指标的逆转与“大批量发布”回潮**：由于用 AI 产出大规模变更集太容易，团队正不自觉地回到类似瀑布流的模式，用大量、低频的发布取代小量、高频的发布。这导致系统稳定性大幅度下降，是过去十年 DevOps 最佳实践（小批量=高稳定性）遭遇的最危险倒退。

## 4. Deep Research 核心切入点 / Open Questions
1. **替代传统用户故事的下一代“规格语言”是什么样子的？** 我们到底需要多精确的伪代码或语义模型，才能稳定驱动 Agent？
2. **AI 原生的 TDD 框架演进方向**：是否存在一种通过自动生成具有确定性的核心测试套件，用以作为所有变异模型“沙盒校验”的自动化链条？
3. **彻底抛弃人类 Review 的临界点在哪里？** 是否存在一个纯粹通过类型系统约束和全覆盖测试，达到“零人类干预信任”的工程范式闭环？
4. **如何打破“大批量变更陷阱（Big Batch Trap）”？** 面对智能体几分钟生成的上千行重构 PR，我们在 CI/CD 环节如何强制通过架构切片手段将它重新碾碎为高频小步迭代，以保证大盘稳定性？

## 5. 历史摘要（保留，不修改）

本文件现有第 1-4 节即为历史摘要，保留原文，不做删改。

## 6. 本轮新增证据

- 结构化自然语言规格有成熟先例，EARS 通过有限模板降低需求歧义与波动风险，适合作为“比用户故事更精确、又比重型形式化更易采用”的中间层规格语言。参考：`_reference/01-engineering-paradigm-01-ears-structured-requirements.md`
- 对于复杂 reactive behavior，statecharts 提供了更适合 AI 理解和人类审查的行为规格结构，并可与模拟、一致性检查和性质验证联动。参考：`_reference/01-engineering-paradigm-02-statecharts-reactive-specification.md`
- TDD 在 LLM 场景下不是单纯的测试补充，而是代码生成的迭代 steering mechanism。参考：`_reference/01-engineering-paradigm-03-llm4tdd-best-practices.md`
- 测试本身可以成为 prompt 与 verification interface，说明“spec 的可执行部分”会越来越重要。参考：`_reference/01-engineering-paradigm-04-tests-as-prompt-tdd-benchmark.md`
- GenAI 可以辅助 TDD，但若缺乏增量约束和人工监督，会生成迎合提示而不是满足真实质量目标的代码。参考：`_reference/01-engineering-paradigm-05-genai-for-tdd-preliminary-results.md`
- 基于 constraint dependency graph 的 test-driven generation 显示：将测试和语义要求转换成显式约束，有助于提高正确性和修复能力。参考：`_reference/01-engineering-paradigm-06-llm4tdg-constraint-reasoning.md`
- type-constrained decoding 证明类型系统可以前移到生成阶段直接约束输出，而不只是事后编译报错。参考：`_reference/01-engineering-paradigm-09-type-constrained-code-generation.md`
- formal specification generation 如果没有 validator feedback，容易因语法、逻辑和不完整推理而失败；这说明“让 AI 生成规格”本身也需要验证回路。参考：`_reference/01-engineering-paradigm-10-autorespec-formal-spec-generation.md`
- AI-assisted coding 会把 review 推向系统瓶颈，尤其是大 PR 导致 reviewer 丧失 intent reconstruction 能力。参考：`_reference/01-engineering-paradigm-07-salesforce-scaling-code-reviews.md`
- 真实企业实践已经把关注点从“更快产码”转到“更安全发版”：测试覆盖、验证工作流、AI-assisted review 和人工审批共同构成新的质量防线。参考：`_reference/01-engineering-paradigm-08-salesforce-ai-tooling-quality-safety.md`
- DORA small-batch guidance 说明，小批量不是偏好，而是 CI 与 trunk-based development 的必要条件；关键测量面包括 release cadence、feature slice size、是否能在完整 feature 结束前提交与发布。参考：`_reference/01-engineering-paradigm-11-dora-working-in-small-batches.md`
- DORA trunk-based development 进一步把机制落到 branch lifetime、active branch count、daily merge、fast automated tests 和 code-freeze elimination。参考：`_reference/01-engineering-paradigm-12-dora-trunk-based-development.md`
- GitHub branch protection 与 merge queue 说明 required checks、review、deployment gate、linear history 和队列验证可以成为强制 merge control。参考：`_reference/01-engineering-paradigm-13-github-branch-protection-merge-queue.md`
- Google SRE canarying 说明 release slicing 不止发生在代码合并前，也发生在 feature exposure、traffic rollout、metric evaluation 与 rollback 阶段。参考：`_reference/01-engineering-paradigm-14-google-sre-canarying-releases.md`

## 7. 本轮新增机制理解

- `规格 -> 测试 -> 代码` 正在取代 `需求描述 -> 代码 -> review` 成为更稳健的 agentic coding 主链路。
- “测试即 prompt”意味着测试套件不再只是验收工具，而是行为约束与任务分解的一部分。
- 结构化规格语言和行为模型之所以关键，不只是因为 AI “理解更好”，而是因为它们更容易被拆成 machine-checkable constraints。
- 类型系统与 formal spec validator 代表两类不同但互补的 guardrail：前者限制可生成空间，后者限制可接受空间。
- 传统 code review 的问题不是价值消失，而是吞吐与认知极限被 AI 生成速度打穿，所以 review 必须被重新定位为高判断密度的 checkpoint，而非主质量阀门。
- 小批量交付可以被拆成可测量、可强制的控制链：`work slicing -> short-lived branch -> fast CI -> protected merge -> queue validation -> deployment gate -> canary exposure`。
- 对 AI-generated change 来说，真正的 release discipline 不应只限制 PR 行数，而要限制未验证意图、跨模块扩散、队列冲突和生产暴露比例。

## 8. 本轮新增趋势与难点

- 趋势：规格与测试正在变成更前置、更结构化、更可执行的制品。参考：`_reference/01-engineering-paradigm-01-ears-structured-requirements.md`, `_reference/01-engineering-paradigm-04-tests-as-prompt-tdd-benchmark.md`
- 趋势：AI-assisted code review 会越来越像 `intent reconstruction + risk surfacing`，而不是逐行 diff 浏览。参考：`_reference/01-engineering-paradigm-07-salesforce-scaling-code-reviews.md`
- 趋势：AI-heavy pipeline 会越来越需要把 small-batch delivery 做成平台默认，例如 branch lifetime budget、required status checks、merge queue、deployment gates 和 canary rollout。参考：`_reference/01-engineering-paradigm-11-dora-working-in-small-batches.md`, `_reference/01-engineering-paradigm-12-dora-trunk-based-development.md`, `_reference/01-engineering-paradigm-13-github-branch-protection-merge-queue.md`, `_reference/01-engineering-paradigm-14-google-sre-canarying-releases.md`
- 难点：测试 prompt 变长、任务跨多个 feature 或跨模块时，instruction loss 和 intent fragmentation 会显著上升。参考：`_reference/01-engineering-paradigm-04-tests-as-prompt-tdd-benchmark.md`
- 难点：没有人工监督的 AI-TDD 容易对非资深开发者形成误导，导致“看似遵守流程，实际没有守住质量底线”。参考：`_reference/01-engineering-paradigm-05-genai-for-tdd-preliminary-results.md`
- 难点：虽然类型约束和 formal specification generation 的研究证据已经出现，但真正企业级流水线如何把这些 guardrails 接到 CI/CD 里仍需继续补。参考：`_reference/01-engineering-paradigm-09-type-constrained-code-generation.md`, `_reference/01-engineering-paradigm-10-autorespec-formal-spec-generation.md`
- 难点：这些控制能约束交付批量和暴露节奏，但仍不能单独证明 AI 生成意图正确；必须与规格、测试、约束和风险评分联动。

## 9. 当前判断（本轮综合后）

- 当前最可信的判断不是“AI 会淘汰 review”，而是“review 不再足以独自承担质量防线”，质量主战场正在向规格、测试、约束和发版验证迁移。参考：`_reference/01-engineering-paradigm-03-llm4tdd-best-practices.md`, `_reference/01-engineering-paradigm-07-salesforce-scaling-code-reviews.md`, `_reference/01-engineering-paradigm-08-salesforce-ai-tooling-quality-safety.md`
- 在 AI-native SDLC 中，下一代规格语言很可能不是纯自然语言，也不是全面形式化证明，而是 `structured NL + behavior model + executable tests` 的组合。参考：`_reference/01-engineering-paradigm-01-ears-structured-requirements.md`, `_reference/01-engineering-paradigm-02-statecharts-reactive-specification.md`, `_reference/01-engineering-paradigm-04-tests-as-prompt-tdd-benchmark.md`
- TDD 正在从“写代码前先写测试”的习惯，升级为“给 agent 提供高精度意图约束与自动验证回路”的控制机制。参考：`_reference/01-engineering-paradigm-03-llm4tdd-best-practices.md`, `_reference/01-engineering-paradigm-05-genai-for-tdd-preliminary-results.md`, `_reference/01-engineering-paradigm-06-llm4tdg-constraint-reasoning.md`
- 除测试外，类型系统和 formal specification validator 也正在成为 AI-native coding 的前置质量护栏，这比传统“代码写完再编译/再 review”更接近新的工程闭环。参考：`_reference/01-engineering-paradigm-09-type-constrained-code-generation.md`, `_reference/01-engineering-paradigm-10-autorespec-formal-spec-generation.md`
- 大批量变更陷阱不是抽象担忧，而是已有企业信号表明会在 AI 生成速度下迅速放大；最可信的缓解路径是将 `small batch + trunk-based development + protected merge + deployment gate + canary rollout` 合成默认流水线控制。参考：`_reference/00-shared-02-dora-gen-ai-impact-software-development.md`, `_reference/01-engineering-paradigm-07-salesforce-scaling-code-reviews.md`, `_reference/01-engineering-paradigm-08-salesforce-ai-tooling-quality-safety.md`, `_reference/01-engineering-paradigm-11-dora-working-in-small-batches.md`, `_reference/01-engineering-paradigm-12-dora-trunk-based-development.md`, `_reference/01-engineering-paradigm-13-github-branch-protection-merge-queue.md`, `_reference/01-engineering-paradigm-14-google-sre-canarying-releases.md`
