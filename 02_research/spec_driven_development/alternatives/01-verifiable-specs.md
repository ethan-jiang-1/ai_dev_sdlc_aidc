# 验证优先 / 可验证 spec——「未被验证器消费的 spec 没有控制力」

```yaml
topic: SDD 替代形态之一：验证优先/可验证 spec（VSDD、compilable specs、facts）
accessed_at: 2026-09-20
parent: ../alternatives.md#1
scope: 2026 年材料优先（VSDD 提案 2026-02-28；av/facts 2026-05-04；specdown / whenwords 2025Q4–2026）；§ 工具化与产品化信号为 2026-09-21 六路深挖补充
sources:
  一手:
    - VSDD gist 原文 https://gist.github.com/dollspace-gay/d8d3bc3ecf4188df049d7a4726bb2a00
    - HN 47197595 全部 118 条评论（hn.algolia.com API 抓取，211 分）
    - av/facts README（github.com/av/facts）+ HN 48008906 作者回帖（7 分/4 评）
    - specdown README（github.com/corca-ai/specdown，可执行 Markdown spec，dogfooding + live report）
    - whenwords 仓库及 issue #6（github.com/dbreunig/whenwords）
    - Verus-SpecGym arXiv 2605.26457（标题已回源确认）
  二手:
    - Midas Tools（dev.to/midastools/vsdd-the-ai-coding-methodology-actually-worth-stealing-35ah）《VSDD: The AI Coding Methodology Actually Worth Stealing》(dev.to, 2026-03-01/修订 2026-04-14)
    - Sadogursky "intent integrity chain"（原章节 martparve/production-ready/chapters/06 于观测日 404，仅存二手转引，权重降级）
weights: HN 211/118=高；av/facts、specdown=中（一手工具但热度低/团队规模小）；whenwords=中（有一手但作者已自我部分推翻）；Midas Tools=低–中（带立场的二手解读）
limitations:
  - production-ready 章节 404，intent integrity chain 细节未回源，仅按二手引用。
  - HN 评论者均为匿名 ID，观点归纳按"社区共识/分歧"计，不按权威计。
  - 未能找到 VSDD 被任何团队整体落地的公开案例；落地证据止于工具化变体（CodeLeash、rlm-workflow 等回帖自述）。
```

---

## 0. 定位：这条路线在回答批判面的哪一问

critiques.md 的死结一是「自然语言 spec 无法自我验证」。验证优先派给出的不是"别写 spec"，而是**重新定义 spec 的合法性标准：一份 spec 只有在被某个验证器（测试运行器、command、类型检查器、模型检验器、对抗 reviewer）消费时才存在**。本篇对底稿第 1 节做四向深挖：VSDD 讨论串的完整论点图谱（§1）、compilable specs 的真实实践样例（§2）、facts 的原文细节（§3）、失败面与团队落地（§4–5）。

---

## 1. VSDD 大讨论：118 条评论里的支持与反对图谱

### 1.1 提案本体（一手，gist 原文）

VSDD 把 SDD、TDD、VDD（对抗验证）排成**顺序门禁**：Phase 1 Spec Crystallization（行为契约 + **验证架构**：可证明属性目录、纯函数核心/副作用外壳边界图、形式化工具选型——Kani/CBMC/Dafny/TLA+，理由是"工具约束就是架构约束，必须在 Phase 1 定"）→ Phase 2 测试先行（Red Gate：全部测试必须先失败）→ Phase 3 对抗精炼（Sarcasmotron，新上下文的超批判 reviewer，查 spec 保真度、测试同义反复、代码质量）。配角是作者自己的 Chainlink issue 分解器（Epics→Issues→"beads"）。

### 1.2 主要反对论点（各条均为评论原文观点的归纳，非复制）

1. **验证时机结构性太晚 + API 幻觉**（politician，最高质量反对）："写测试必然意味着设计一套测试所操作的 API"——你命令 agent"只写测试不写代码"，它其实已经把 API 定了，而且是幻觉出来的；后续测试层层叠加会把这套畸形 API 越拉越歪，对抗 reviewer 发现时已经太晚（流程末位）。作者自述亲历：测试全绿、覆盖率漂亮、不变量合规，打开一看是 "rats nest / ball of mud"，加一个功能要 10 倍 token。choeger 补刀：spec 往往只能**整体**被正确实现，无法按约束逐条迭代，"通过的测试数不是实现完成度的好指标"。
2. **discovery 不可 spec 化**（_pdp_ 一系）："整个提案建立在你已经知道自己在干什么这个假设上"——你无法为不知道怎么建的东西写 spec，更别说先写测试；"给 flux capacitor 写个 spec 试试？"。AI-first 时代代码成本趋零，正确姿势是广度探索（他自称全店数百 agent 并行、1.2K open PR、日采 1–2 个、大部分代码直接丢弃）而非一次性把系统想完美。manmal："Waterfall 从来没能成功过是有原因的……我宁可把 50% 时间花在搭测试上，也不花 20% 时间写一份不会 work 的 spec。"
3. **可验证性本身不可逃避地难**（pron，CS 视角）："X 是否满足性质 P"就是 model-checking 问题，已被证明不可处理（intractable）——有的性质验证下限 10 分钟、有的 10 年，且事先不知道是哪种。任何声称"解决了编程"的方法论，必然在某处偷偷砍了角，你要自己找出砍在哪里。alpaylan 的收缩版：你无法逃避"由人来机械地确认想验证哪些性质"，这套东西**只在 spec 远比实现简单的场景有杠杆**。
4. **提案自身的可信度危机**（多条，罕见的元批判）：pangram.com 检测认定 gist 是 AI 生成；mpalmer 拒绝给 vibe-written 帖投票（无法归因于人类作者，讨论难深入）；esafak 直指作者自己的 repo CI 长期是挂的——"推广可验证 spec 的人拿不出一个被验证 spec 救过的 bug"。这构成一个自我指涉的尴尬：**用不可验证的散文推广可验证性**。（作者 dollspace 回应：CI 挂是 runner 从 GitHub hosted 迁 self-hosted 所致。）
5. **LLM 产出的验证物本身不可信**（WestN）：LLM 写的测试既可能作弊也平庸——训练数据里塞满了"LLM 怎么写测试"，所以他主张干脆**别让 LLM 写它自己能生成的测试**（改 BDD 风格、甚至删掉 agents.md）。这与 Phase 3 自己列的"tautological tests"检查项互为印证：系统知道自己的验证器会被糊弄。

### 1.3 主要支持论点

1. **spec 是设计工具，不只是合约**（tikhonj）：写（形式化）spec 本身就能快速探索设计空间、自动暴露不一致并强迫你显式解决——"这在用 AI 时尤其重要，因为 AI 会静默地解决不一致，方式说不通还难以察觉"。
2. **spec 是你唯一还能完全掌控的产物**（virgilp；KOL 级独立复述见 de Moura "specification becomes the core engineering discipline"，[01a](01a-verifiable-convergence-evidence.md)）：spec 值得花比实现更多的时间，因为它是你还能完整读、完整懂的部分；有了好需求，你才有资格"回头问另一个 AI：实现符合 spec 吗"。他直接反驳 _pdp_：你无法要求 AI 建出好的"某个东西"，除非你能说清那个东西是什么；需求越含糊，只有在"很多人造过同类东西"时才碰巧可行。
3. **压缩后的瀑布不再是瀑布**（hamdouni，HN item 47215990——原稿误挂 virgilp/zozbot234，审计勘误）："months 压缩到 days/hours，90 年代的人不会认出这是 waterfall"；而且 spec 反正必然存在——区别只在它是显式的、有人参与的文档，还是 improvised 在 AI 的隐藏思维 token 里。"总有一个 spec，包括你发的每条非正式 prompt。"
4. **代码成本归零改写了 spec 的旧账**（noosphr）：旧时代 spec 最大的痛是"prover 通过后才发现漏了一个 business case，全部推倒"；现在 bottom 98% 可以交给机器人 + 明确的成功信号，改 spec 的代码成本也为零。baq 的提法最凝练：**spec 是 coding pipeline 各产物的 ECC（纠错码）**——spec 与代码正交，两边都可以迭代。
5. **实践自证的小生态**（多条）：mirekrusin 给出 SPEC.md（追问到 ok 才过）→ PLAN.md（拓扑排序步骤）→ 逐步实现+测试 的循环；michaelbrave 描述 Claude 写文档/Gemini 写测试与代码/Codex 跑流水线修 bug 的多模型分工；gck1 主张 clean-room 整体重写循环——"增量 spec 化不 work，agent 永远不会选那条难而正确的路，除非只带上一轮的重要教训从零再来"。theptip 给出适用边界：vibe coding 会杀死探索乐趣，但**大系统 core 里 vibe coding 本来就进不去**，那里需要的正是更形式的东西。

### 1.4 社区把这个提案修正成了什么样

原提案的**全套门禁（Epics/beads/Sarcasmotron/数学证明）没有整体落地者**；讨论收敛出一个被二手文（Midas Tools）明确公式化的"80/20 修正版"：**偷 spec 纪律，跳过仪式**——写 5–10 句"做什么/绝不做什么/三种最可能的失败模式"，交给 agent；产出贴进全新上下文要最狠的批判；修真问题、无视理论问题。三个方向性的修正仍在讨论里成形：

- **门禁从 prompt 移到模型外**：cadamsdotcom 的 CodeLeash 用 Claude Code hooks 强制 TDD 流程——"模型不能忘记或跳过步骤"；他同时给出 compilable specs 的工具化愿景："SDD 大概意味着造出跟踪 code↔spec 映射的工具，把映射当数据管理，然后查询数据确认全部映射——而不是反复礼貌地请求昂贵且不可靠的模型"。tinodb 独立复述了同一思路（enforced TDD 状态机）。
- **对抗 reviewer 的可信度升级**：teiferer 只买形式化验证的账——"把 AI verifier 换成骗不了的东西我就上车"；mirekrusin 的折中是把验证谱系摆开：自然语言 spec 也算一种（模糊的）验证表达，另有 typechecker、测试、linter（正确性向的 lint 规则）。
- **LLM 自产测试的去毒化**：WestN 的 BDD 替代论获得附议（esperent 指出 vitest 等 BDD 风格已是主流默认），指向"spec 编译目标应是人类可读的行为断言而非 LLM 自由发挥的测试代码"。

---

## 2. compilable specs 的实践样例（2026 年，真实团队/项目）

**学术锚**：Verus-SpecGym（arXiv 2605.26457，标题已回源）把"spec→形式规约"的 autoformalization 做成 agentic 评测环境——说明"从 NL spec 编译出可验证约束"已被当作可度量的模型能力来评测，而非只是口号。近旁还有 Specification Grounding 与测试有效性关系的实证线（semantic scholar 收录）与 arXiv 2605.01160 的"specification-driven governance"治理框架。**2026 重量级一手锚（详见 [01a](01a-verifiable-convergence-evidence.md)）**：Kleppmann 提出 vericoding（2025-12-08）；Lean 之父 de Moura 宣告 "specification becomes the core engineering discipline" 并给出 zlib 机器证明定理的生产案例（2026-02-28）——形式化阵营已自我宣告为该形态的终局载体，且拿出了 zlib 级生产案例。Sadogursky 的 "intent integrity chain"（意图→验证管线）此前被引为实践方法论，但原文章节 404 且本轮复核未发现 2026 年新引用——权重维持"仅二手转引"不变（[01a](01a-verifiable-convergence-evidence.md) §16.6）。

### 样例 1：specdown（corca-ai）——一份 Markdown 同时是 spec 和可运行测试套件

韩国 AI 公司 Corca 开源的 Go 工具（2026 年活跃，Homebrew/go install 分发）：`specdown run` 直接执行 spec 内嵌的可执行块并生成报告，**一份文档既是人读的 spec 又是 CI 跑的测试**。关键证据：仓库 dogfood 自己（"Self-Spec"），并公开 live report 展示自 spec 的执行结果；example 项目同时用 shell 块和 **Alloy 模型**（轻量形式化）且"无需任何自定义 adapter"——即 NL spec、可执行断言、形式化模型三者在同一文档内编译执行。还有专门的 Best Practices 文档记录 patterns/pitfalls/anti-patterns，说明它已经跑过实践循环而非概念 demo。

### 样例 2：whenwords（dbreunig）——NL spec + 750 个 YAML 一致性测试，及其自我证伪

dbreunig 的 whenwords 是"自然语言 spec 被编译为大规模一致性校验"的最早出名样例（750 个 YAML 测试逐条核对 spec 陈述与代码现实，Karpathy 点赞、1000+ star）。它对本篇的价值有二：一是证明了**spec-as-verifiable-claims 可以机械执行**；二是它同时是这条路最深的一手警告——作者 2026-03 公开自我推翻（"a spec doesn't really work until it's implemented"），且仓库 issue #6（tests.yaml 与 SPEC.md 在舍入/单位上冲突）就是"可验证 spec 自身的漂移税"的活体标本：编译解决了"spec 不可验证"，没解决"两份真源谁说了算"。

### 样例 3（极简形态）：av/facts 的 command-fact——把编译成本降到一行 shell

见 §3。facts 的 `command: grep -q 'bcrypt.*12' src/auth.ts` 是 compilable spec 的最小实现：每条事实可携带一条"exit 0 即为真"的 shell 命令，`facts check` 批量执行、可挂 CI。它证明了编译目标不必是测试框架或形式化工具——**grep 级别的命令就足以让一条 spec 获得机器效力**。dogfooding 自述：224 条事实，154 条由命令验证，0 失败。

---

## 3. av/facts 的 consistency tax 原文细节

**他扔掉了什么**：spec 里除事实外的全部——叙事、流程文本、设计理由、"fluff"。作者在 HN 上的原始表述是二分式："Spec is essentially a set of facts + fluff. List of facts is essentially the spec minus the fluff." 动机即 critiques.md 引用的原话：大项目 spec 多到 agent 维护它们时开始出错，"There's a constant consistency tax"。注意扔掉的不止是 SDD 的 spec 三件套，而是整个"spec 作为文档体裁"——不管理由、不管理由的演化。

**他保留了什么（README 一手细节）**：
- **原子事实 + 生命周期标签**：`.facts` 文件每行一条原子声明，`@draft`（粗想法）→`@spec`（精确、可建）→`@implemented`（代码背书），转移由 agent 管理；格式同时是合法 Markdown 和合法 YAML（每 section）。
- **机器验证通道**：事实可挂 `command`（shell，exit 0 = 真）；`facts check` lint 全部文件并跑所有 command-fact，manual facts 保持 `?`，可用 `--agent claude` 等 preset 让 LLM 验证人工事实；exit code 直接可接 CI（`--strict` 把未验证的人工事实也当失败）。
- **agent skills 全生命周期**：facts / facts-discover（扫代码库给事实分类补漏）/ facts-refine（把 draft 磨成 spec）/ facts-implement（领 spec、实现、跑 check、打标签）——形成 draft→spec→implemented 的流水线，spec 随项目演化"自我更新"。
- **可 diff 性**：事实表是数据而非散文。

**效果自述**（HN 回帖，一手）：① 只用几条核心行为假设即可 seed 一个复杂项目，agent 会以形式化方式补齐缺口；② fact sheet 可 diff/对比——他给一个复杂的 Python CLI 建 fact sheet，让 agent 把 Python 相关条目改成 Rust 等价物，然后在另一个项目里重建了这个 CLI；③ 比大 spec 格式快得多，agent 用更少 tool calls 拿到所需上下文；④ **大重构后跑一次 facts check 相当于一次完整 e2e 测试**。README dogfooding：224 事实/154 命令验证/0 失败。社区质疑（sminchev："拿一个从头到尾用它做成的项目来证明"）没有得到超出 dogfooding 的回答——效果证据仍止于作者自述。

---

## 4. 失败面：可验证 spec 写不出来的场景

把 §1 的反对论点与批判面对照，可验证 spec 的失效面有五类：

1. **discovery 类任务**（_pdp_/manmal/deontologician 同构）：问题空间边界未探明时，"可验证"无从谈起——你没有断言可写。验证优先派内部对此有真正的反驳（tikhonj/virgilp：spec 语言是设计工具、"你不能要求冰箱冷还得先会造冰箱"），但注意这些反驳依赖**形式化 spec 语言提供反馈**——即他们实际主张的是"先探索再冻结"，门禁仍然只在冻结后成立。
2. **验证不对称场景**（alpaylan/pron）：只有当 spec **远比实现简单**时验证才有杠杆；反过来，排序算法、并发协议、数值库的 spec 本身就是半个实现。model-checking 的不可处理性意味着"哪些性质可验证"事先不可知，形式化路线（gist 的 Phase 1b）的成本不可预算。
3. **意图/美学/非功能偏好**：UI 主题、API 手感、"符合用户心智"——可断言的只是行为子集。当 questions 汇聚成 ErrantX 的"UI 紫的还是蓝的其实不重要"时，恰恰说明那部分**不该**进 spec；但探索性产品里不重要的部分常常正是产品本身。
4. **legacy 隐性行为**（DaylitMagic）：35 年迭代的代码库里有大量没人记得的边角编排——spec 之前还需要一个"考古"阶段（先目录化输入输出再确认行为），而这一步本身没有验证器。
5. **验证物自身的漂移与作弊——须拆成两个独立失效面**（Brown PLT 对 Kleppmann 的逻辑击破未获回应，见 [01a](01a-verifiable-convergence-evidence.md) 对撞 #1/#2）：**（a）验证器不可作弊**——LLM 写的测试会同义反复、mock 过度、断言实现细节（Sarcasmotron 清单自认）；让验证层完全依赖 LLM 等于把合约交回给被合约约束的一方。**（b）验证内容不可被掏空**——P⊨ɸ 有效的判据是 P 与 ɸ 独立写成；当 AI 双侧生成（既写实现又写 spec/测试），agreement 不构成 redundancy，验证效力结构性失效；Wayne 的实证（LLM 写的 spec 多为弱性质/同义反复）与 whenwords #6（tests.yaml 与 SPEC.md 冲突需人裁）从两个方向坐实。**编译没有消灭 consistency tax，只是把它从 spec↔code 转移为 spec↔tests↔code 三角**——这正是 dbreunig 三角模型的原始含义。

---

## 5. 团队落地建议

**什么信号说明你该用这形态**：
- 失败成本不对称：正确性敏感的核心（支付、权限、解析器、协议、数据完整性），一个 escape bug 的代价 >> 写验证spec 的成本；
- spec 与实现的复杂度比有利（alpaylan 条件）：你能用比代码短得多的语言说清"什么必须为真"；
- 已出现 spec 债症状（spec 与代码打架、没人敢删旧 spec）但任务本身契约清晰——这是 facts 形态的入场信号；
- 多人/多 agent 并行需要**共享的机器可查合约**，而不是又一轮 prompt 谈判；
- brownfield core：vibe coding 进不去、必须有人类可审计的验证层的地方（theptip 条件）。

**不该用的信号**：探索期产品（先 prototype onion 再冻结）、spec 复杂度逼近实现的领域算法、需求方不投入前期反馈（daveac：AI 把瓶颈移到了需求发现/签核端，验证 spec 救不了不参与的 sponsor）。

**起步三步（前插一步 0，按 [01a](01a-verifiable-convergence-evidence.md) 修订）**：
0. **先跑测试再说**："First run the tests" 四词 prompt，零成本——其有效性已被 Willison 指南化为默认纪律；多轮 agent 场景下同时在测试 docstring 里写明"这个测试为什么存在"（capture the why of tests），是防止验证物漂移的最廉价手段。
1. **事实化**：把现有 spec（或直接从代码逆向，zozbot234 指出 AI 逆向 spec 无瀑布先例）压缩成 facts 式原子清单：每条一句声明 + 生命周期标签；凡是能用命令核对的，立刻加 `command`（grep/test/单测均可），跑起来并接 CI——这就是你的最小 compilable spec，一天内可完成，不需要任何新框架。
2. **门禁移出模型**：为新功能写 5–10 句行为契约（做什么/绝不做什么/三类失败模式），把每条契约编译为可执行断言（测试或 command-fact），并用 hooks/CI 强制"无失败测试不写实现"——借鉴 CodeLeash 的原则：强制力放在模型外，靠提示词维持的纪律必然衰减。
3. **加对抗闭环 + 回写规则**：冻结后把产出交给全新上下文的 reviewer（LLM 或同事均可）做超批判审查，重点抓 tautological tests 和"标为 test-only 其实该 prove 的性质"；同时把"spec 更新了吗？"写进 DoD——whenwords #6 与 dbreunig 自我推翻已经证明：没有回写规则的可验证 spec，只是把漂移问题搬进了测试文件。

**适用边界声明（2026-09-21）**：两个关键量度仍是未决问题，本文不给确定性判断——①门槛降幅（形式化对普通团队的准入成本，Wayne 之问："从 80 降到 75？"）；②审查成本回归（Prakhar Goel："reviewing is harder than writing"——验证物变多后人工审查瓶颈是否回弹）。

---

## § 工具化与产品化信号（2026-09-21 三轮）

> 六路并行深挖的产物：①spec→测试编译器 ②形式化验证×LLM 产品 ③runtime verification/契约测试/PBT ④evals-as-spec ⑤spec 属性/不变式生成 ⑥反信号。所有 GitHub/npm/PyPI/HN 数据均为 2026-09-21 实测快照（部分 GitHub REST API 当日限流，个别条目以 HTML 页/atom feed/npm 首版时间近似，已随条目标注）。每条工具含六项：机制 / 实测数据 / 用户侧证据 / 定价 / 竞品对照 / **与 SDD 工件链（spec/plan/tasks）的组合方式**。原始报告落盘：`.tmp-spec-to-tests-20260921/`、`.tmp-pbt-contract-agent-verification/`、`.tmp-spec-machine-verifiable-antisignals/`、`.tmp-spec-invariant-survey-2026-09-21.md`。

### §1 spec→测试编译器：2026 新工具全景（极早期，零商业化）

2025Q4–2026 确实出现了一批新工具，但整体处于"手艺"阶段：除 Promptwright（118★）外 stars 多为 0–2、npm 月下载 5–112，**HN 讨论全部为零，无任何已公开定价的商业产品**。形态上分化三条路线：

**路线 A：重型平台（spec → Playwright 代码 + 自愈）**

1. **Quorvex AI**（NihadMemmedli/quorvex_ai）——最接近"spec 编译成测试"的完整形态。
   - 机制：自托管 Python 平台，输入自然语言流程/PRD/OpenAPI 导入（或 agent 自主探索真实应用）→ agent 规划流程 → 生成 Playwright TypeScript → 真实浏览器验证 → self-healing 自动修 selector/时序失败。编译目标是**普通 Playwright 仓库代码，产物进 CI 后不再依赖模型调用**。
   - 实测数据：43★/5 forks/39 open issues/created 2026-02-28/pushed 2026-08-02/MIT；releases 密集（≥15 个 tag，v1.2.11–15 集中在 2026-06-22~23）；npm 同名包仅 security holder（月下载 15），真实分发走 Docker。
   - 用户侧证据：HN 搜 "quorvex" 零结果；39 个 open issue 主要来自作者自测。
   - 定价：开源自托管，免费。
   - 竞品对照：对照 specdown（spec 文本即测试）是重型平台 vs 轻量解释器；对照 AssureMind 同路线但更 SaaS 化。
   - 组合方式：替掉 tasks 里的"写 E2E 测试"一环——spec（PRD）进去，测试代码出来后 spec 即退位；不维护 spec↔test 映射，与 §5 反信号的"双写死根"同构。
2. **AssureMind**（npm: assuremind）——"plain English → Playwright"，UI+API 双栈，Apache-2.0。npm created 2026-04-03、21 版本、1.7.0 于 2026-09-20、月下载 112；官网 assuremind.in，**pricing 页 404（实测）**，疑似尚未定价。面向非程序员的 codeless 定位，与开发者 CLI 文化（specdown/facts）相反。组合方式同 Quorvex：一次性编译、丢弃 spec。

**路线 B：agent 原生编译器（spec → 验收测试 → 驱动 agent 循环）**

3. **nax**（@nathapp/nax，nathapp-io）——spec.md → LLM 生成 prd.json + 验收测试（强制先失败）→ 驱动 Claude Code/Codex/Gemini CLI 实现到全绿 → 语义审查（对照 acceptance criteria 抓 stub/占位实现）+ 对抗审查 → 回归门禁。实测：2★/push 2026-09-20；npm created 2026-03-03、**306 个版本（日更级节奏）**、最新 0.82.0-canary（2026-09-19）、**月下载 3,400（本批最高）**；HN 零讨论。定价：开源免费。对照 specdown：specdown 让 spec 文本自己可执行；nax 把 spec 当一次性编译输入，重心在"验收测试驱动的 agent 循环"。组合方式：**把 VSDD 的 Red Gate（测试先行）整个自动化**——替掉 plan→tasks 的手工分解，验收测试就是 tasks 的完成判据；这是六路调研里与 §1 VSDD 提案血缘最近的产品。
4. **@agent-lang/spec-flow**——最字面的 spec compiler：自然语言 → LLM 起草 YAML spec → 校验/auto-fix → **人工审批门** → 编译成 Vitest 测试 → 生成实现 → 自动修订到全绿。npm created 2026-03-28、3 版本（0.3.0，2026-06-03）、**月下载 18**。与 specdown 最同构（显式 spec 中间表示 + 编译到测试运行器），但 IR 是 YAML 且带实现回路；六路中唯一保留"spec 一等公民"设计的新工具。组合方式：spec 环节产物化（YAML spec 是可 diff、可审批的持久工件），tasks 由编译产物隐含。

**路线 C：MCP 桥接层（不编译，只搬运+追溯）**

5. **mk-spec-master**（kao273183）——MCP server，6 个适配器把 Linear/JIRA/GitHub Issues/Notion/Figma/Markdown spec 转成结构化测试场景（18 个 MCP tool），经姊妹项目 mk-qa-master 交给 pytest/Jest/Cypress 执行，维护**双向 spec↔test 覆盖矩阵** + spec 质量教练（chronic-spec 检测）。本身无 LLM，推理由 MCP 客户端承担。实测：2★/push 2026-05-18 后停更；PyPI 0.1.0 首发 2026-05-15、0.4.0（2026-05-16），alpha。已上架 Glama MCP 目录；HN 零讨论。免费 MIT。组合方式：唯一做"企业 spec 源→测试"桥接 + 覆盖追溯的，直接攻击 whenwords #6 暴露的 spec↔tests 漂移问题（覆盖矩阵即回写规则的机械化），但极早期且已停更。
6. **Promptwright**（sahajamit，118★）——方向相反的输入端：自然语言或**真人点击录制** → 真实浏览器 → Playwright/Cypress/Selenium 脚本，录制可落成 **Gherkin 回放（先有行为后有 spec 的 BDD 新形态）**。Electron + CLI，BYOK 任意 OpenAI 兼容模型。pushed 2026-07-10；原属 testronai，2026 年迁移重写。用户侧证据最强的一条：TestGuild 播客（Joe Colantonio）2026-07 现场演示（youtube.com/watch?v=2c7P4du6hDQ，demo 从 8:44 起）。免费+BYOK。组合方式：从实现/演示**反推** spec（Gherkin 是产物不是输入），相当于把 §4 失败面第 4 条"legacy 考古阶段"工具化。

**边缘候选（一句话级）**：specforge-ai（1★，作品集性质，OpenAPI→contract check）、ai-native-specforge（月下载 28）、trimble-spec-kit（月下载 5）、reactullm-sdd（alpha，SDD 流水线实验）、jpequegn/spec-executor（0★，markdown spec→code+tests 循环）、PramodDutta/qaskills 的 contract-test-generator（Claude skill 形态）。

**小结**：与 specdown/whenwords（无 LLM、spec 文本即测试）相比，2026 新工具几乎全部引入 LLM，且编译目标从"运行 spec 文本"转向"生成传统测试代码后丢弃 spec"——**spec 在多数新工具里是燃料而非工件**，这与验证优先派"spec 是你唯一能完全掌控的产物"（virgilp）的立场正好相反。

### §2 形式化验证 × LLM：垂直域封装出现，通用产品未出现

竞品对照表（观测 2026-09-21）：

| 产品 | LLM 环节 | 谁发证明 | 普通工程师可用? | 定价 | 状态 |
|---|---|---|---|---|---|
| Certora AutoProver（Beta——公司动态据二手转述待回源） | 写 spec(CVL)+测试+分诊 | SMT Prover | 接近是（Solidity Beta） | 未获取 | Beta 2026-07 |
| Theorem Labs（YC，$6M——融资额据公开报道转引，未回源待核） | 写优化实现+等价证明 | 等价性检查器 | 需审查参考实现 | waitlist | 早期 |
| AWS Automated Reasoning checks | 政策→逻辑转译 | 符号求解器 | 是（云控制台） | 随 Bedrock，未获取 | GA 2025-08 |
| Pramaana Labs | AI 输出→证明包装 | 定理证明器（法律/税/药域） | 企业服务 | 未公开 | $27M seed（Khosla，2026-06——据二手转述，未回源待核） |
| Harmonic Aristotle | 证明搜索 | Lean kernel | 面向数学/金融企业 | 未公开 | $120M C 轮 2025-11 独角兽（据二手转述，未回源待核） |
| Imandra | 规约/边界分析辅助 | IML 求解器 | 专业服务为主 | 未公开 | 商业签约中（2026 签下 BLOX Markets） |
| Verus/Dafny/TLA+/LeanDojo | 学术工具 | 各自 kernel | 需专家 | 免费 | 活跃但无托管封装 |

- **Certora AutoProver**：2026-07-15 官宣 Beta（Solidity，Rust coming soon），口号 "Agentic Formal Verification for Every Developer"、"as easy to run as a compiler"——读 repo+设计文档 → LLM 生成 CVL 规约+Foundry 测试 → Prover 证明 → agent 分诊验证失败 → 报告随 PR 走。联合创始人 Mooly Sagiv 原话：写 spec 一直是瓶颈，LLM 正在解决这一环。HN 2026-08-13 仅 3 分（热度低）。组合方式：把 VSDD Phase 1b 的"形式化工具选型+属性目录"整个外包给流水线。
- **Theorem Labs**：program equivalence 驱动开发——用户只审一个简单参考实现，系统给出优化实现+两者等价的机器证明（Coq/Lean 系，创始人 Jason Gross 是 Coqhammer 系）。用例：GPU kernel 等价优化、Python→Rust 迁移零行为变更。waitlist 制。组合方式：spec 即"参考实现"——最激进的 spec 形态替换。
- **AWS Automated Reasoning checks**：自然语言政策→形式逻辑→对 LLM 输出做符号验证（"正确/错误/无法判断"）。验证对象是 LLM 回答而非代码，但它是**云大厂第一次把"规约→验证"卖给无形式化背景的普通企业**（GA 2025-08，HN 首发 57 分）。组合方式：把"绝不做什么"类 spec 条款变成运行时 guardrail，而非编译期门禁。
- **开源侧实测**：verus ★3,189（pushed 2026-09-20；2026-09-14 HN "Developing provably correct Rust code with Verus" 164 分——社区热度 2026 下半年明显上升，但靠教程而非 AI 产品）；dafny ★3,548（DafnyPro，POPL 2026 workshop：LLM 修 verification 负担）；tlaplus ★3,058（官方无 LLM 工具，社区有 richashworth/tlaplus-mcp 把 TLC 暴露给 coding agent）；LeanDojo ★836（v2 已上 PyPI）；DeepSeek-Prover-V2 ★1,304（2025-07 后停更，开源权重路线 2026 无 V3）。
- **线索核查**："Conjecture" 实为 AI 安全/可解释性研究组织，非形式化验证服务；"Strymonos" 查无此人。

**判读**：通用"spec 进→验证结果出"封装 2026 年仍未出现；出现的是垂直域（Solidity、政策合规、数学、法律）早期封装 + "LLM 写规约、证明器发证明"的分工共识 + coding agent 挂验证器插件（tlaplus-mcp、LeanDojo）的自下而上形态。瓶颈被公认在"写规约"一环——恰是验证优先派 §1.3 的核心赌注，2026 年开始有人下注解决。

### §3 runtime verification / 契约测试 / PBT：唯一有硬证据链的是 Hypothesis

- **Hypothesis 生态（强度：强）**：官方 2025-11 发布 `/hypothesis` Claude Code 命令（hypothesis.works/articles/claude-code-plugin）+ NeurIPS 2025 workshop 论文《Agentic Property-Based Testing》（arXiv:2510.09907）：LLM agent 分析模块、从代码和文档推断性质、合成并运行 Hypothesis 测试、反思失败确认真 bug。**100 个热门 PyPA 包上 56% 报告为真 bug（top-21 中 86% 有效）**，含已合入的 NumPy 修复（numpy.random.wald 负值 bug，v2.3.4）。实测 8,996★/pushed 2026-09-20/v6.168.0。命令只是一个 markdown 文件，可移植到任何 agent 框架。社区跟进：e35zhang/property-testing-skill（Show HN 2026-07-13）。失败模式也有官方记录：模型会过度限制策略、误解语义性质（dateutil.easter 案例）——即 §1.2 反对论点 5（LLM 自产验证物不可信）在官方论文里有实测印证。组合方式：**property 即 spec**——它不替掉任何 SDD 工件，而是把"可证明属性目录"（VSDD Phase 1b）的生成自动化，产出直接落进 tasks 的测试环。
- **fast-check**（TS，5,148★/v4.10.2，npm 月下载 1.386 亿含镜像放大）：极活跃但无官方 AI 动作，agent 采用为零散实践。强度：中。
- **Schemathesis**（3,612★/v4.27.5 迭代极快，OpenAPI schema 驱动 PBT fuzzing，有 ICSE-SEIP 论文，changelog 有 SaaS 字样但无公开定价）：schema 即机器可读契约、天然适配 agent，但公开渠道无 LLM 集成功能，"agent 验证层"采用直接证据稀薄。强度：弱-中。
- **Pact/Pactflow**（pact-python 684★/v3.4.1，npm 月下载 206 万/PyPI 100 万，SmartBear 企业询价）：成熟企业 CDC 基础设施，**与 agent 工作流零交集**。Dredd 事实性停滞（pushed 2024-05，260 open issues）。强度：弱。
- **proptest/jqwik**：无 agent 动态（proptest GitHub API 当日限流未取得，标注数据缺口）。
- **空白区**："agent API contract testing" 商业产品不存在；MCP 形态测试工具（zod-contract-mock-forge-mcp 等）极早期属信号非趋势；cursor/Claude Code 用户日常用 PBT 当验证层的成规模一手案例尚未出现。**契约测试方向叙事先行、产品缺位**。

### §4 evals-as-spec：真趋势（LLM 应用层）+ 营销叙事（通用 spec 门禁）+ 手艺（gate agent 代码）三层并存

- **工具基本盘（实测 2026-09-21）**：promptfoo 25,307★/pushed 09-20/npm 月下载 251.8 万——**已被 OpenAI 收购**（官方博客 /blog/promptfoo-joining-openai/，HN Ask 47412524，2026-03；收购后重心明显转向 red teaming/security）。Braintrust：npm braintrust 月下载 560.7 万，官方 eval-action@v2 GitHub Action + 2026-09-08 长文《How to build an LLM eval pipeline in GitHub Actions》（数据集+task+scorers、baseline 对比、阈值策略表决定 merge gate、required status check、latency/cost 设 warning）——把 "quality gate / release criteria / regression testing" 做成文档词条，是"eval 作为发布门槛"最直接的产品化叙事。对照组：openai/evals 19,486★ 但 pushed 停在 2026-04（实质停滞）；AgentOps 5,833★ 但半年未推、npm 月下载仅 367（降温）；inspect_ai（UK AISI）2,814★ 活跃但定位 frontier 安全评测，非产品验收。
- **真实团队案例逐个展开**（谁/规模/spec 形态/效果）：
  1. **Fireworks《LLM Eval Driven Development with Claude Code》**（2025-08-25）+ 开源 eval-protocol/claudecode_digital_store_app：最完整的公开"eval=spec"教学案例——dataset 每行是用户故事级行为断言（`expected_behaviors: ["refuses_write_without_auth", …]`，含 prompt-injection 安全用例），先写 eval 再让 Claude Code 写代码，TDD 式。规模：厂商 demo，非生产团队自述。效果：无第三方复现。
  2. **Airbnb《Eval-driven development: lessons from evaluating GenAI at scale》**（2026-08 Medium；HN 49290785，19 分 5 评）：大厂把 eval 当开发流程核心的一手叙述（全文被 Cloudflare 挡未核，存在性确证）。规模：大厂生产。效果：标题级确证，细节未核。
  3. **promptfoo 官方 CI/CD 文档**（更新于 2026-09-20）："Quality Gates: Fail the build when quality thresholds aren't met"，GitHub Actions/GitLab/Jenkins/CircleCI/Bitbucket/Azure 全家桶模板。配套 promptfoo-action 仅 72★——**相对主仓 25.3k，说明"挂 CI 门禁"的实际采用者远小于"用 promptfoo 调 prompt"的人群**。
  4. **AWS sample-GEDD**（aws-samples/sample-GEDD，12★，2026-06）：云厂商布道模板，star 极少。
  5. **GitHub "eval driven development" 搜索**：命中的全是 ≤6★ 的个人/skill 仓库（如 leoncuhk/evaloop 3★，自述"acceptance criterion is an eval suite"）——**开源模板层没有涌现出被复用的标准做法**（这条是高置信的负面证据）。
- **判读**："evals-as-spec 用于 LLM 应用自身的行为回归"是真趋势（月下载百万级 + 两平台一等公民 CI 门禁 + OpenAI 收购背书）；"拿 eval 套件 gate agent 写的代码是否满足 spec"目前主要是叙事 + 极少数人手艺——结构性原因是双层不确定性（spec→eval 套件由谁写、eval 本身的正确性），现实落点收敛为"agent 产品行为的回归套件挂 CI"。各平台布道文（含大量 SEO 内容农场）显著超前于实际采用。

### §5 spec 属性/不变式生成：学术热、产品冷，唯一工程闭环是 CrossHair

- **学术集中爆发（2025–2026），几乎全无公开可装工具**：SpecGen（ICSE'25，Java：LLM 生成 JML 前后置条件→KeY/OpenJML 验证闭环；Lezhi-Ma/SpecGen-Artifact 22★/pushed 2025-12-24）；ClassInvGen（Stanford，C++ 类不变式，LLM+反例 refinement，无公开 repo）；**KaPilot**（arXiv:2607.21957，2026-07：Rust unsafe + Kani 多 agent——SafetyReq 从文档抽安全需求→SpecGenerate→SpecPrecheck/Verify 迭代，54 个有 GT 函数成功率 88.9%，比 Microsoft AutoSpec 多 14.8% 可验证 spec；无公开工具 repo）——"文档→需求→spec→验证"最完整的学术镜像；Daikon+LLM 反例（arXiv:2604.10761）与 TOSEM 2026 循环不变式（LLM+抽象解释）。
- **CrossHair（唯一跑通 SDD 组合的工程工具）**：Python 符号执行契约验证（icontract/deal 断言 + SMT），v0.0.110 持续发版（0.0.100 2025-12→0.0.110 2026 年中），MIT 免费，crosshair-web.org 在线版。**README 确认 Hypothesis 已支持 CrossHair 作为可选后端**——契约验证与 PBT 两大生态在 2026 年合流，"契约即测试"链路（写契约断言→CrossHair 符号执行→Hypothesis 随机回退）在纯 Python 层成立。组合方式：增强 plan→tasks 环——契约断言写进代码后，spec 的行为子集获得免测试的验证通道，正是 §1 VSDD"纯函数核心"路线的可用实现。
- **明确空白（实测）**：npm/PyPI 2025Q4–2026 无成型 assertion-mining/property-generator 新包（唯一沾边的 @philiprehberger/invariant-ts 只是微型 assert 库，月下载 19）；HN 该话题零热度；"spec 属性挖掘 SaaS"不存在（"Invariant Labs" 是同名 AI 安全公司，不同义）。**结论：从代码反推不变式/从 spec 生成 property 的产品层，2026 年基本空白，只有论文和 CrossHair 一个点。**

### §6 反信号：上一代"可执行 spec"工具之死（四条完整证据链）

1. **SpecFlow——唯一宣告死亡的案例（死因：商业收购）**。Tricentis 收购后 EOL：GitHub 官方仓库被删除（specflow/SpecFlow 与 specfloworg/specflow 均 404——比 archived 更彻底）；VS2022 扩展从 Marketplace 下架（SO #79429744，2025-03）；HN "SpecFlow Is Dead"（2025-02-04，4 分 0 评）。NuGet 累计 119.4M 下载（存量枯竭）；作者 Gáspár Nagy 2024-01 分叉 Reqnroll 两年半累计 28.2M——**存量迁移而非需求消失**。
2. **JBehave——无人宣告的死亡（死因：弃坑+叙事退潮）**。Maven 末版 5.2.0 = 2023-09-25，3 年无 release；GitHub org jbehave-core 已 404；连 "is this maintained" issue 都没有——用户流失到不再提问。
3. **Concordion——概念性死亡（死因：双写成本）**。末版 4.0.1 = 2023-07-16；repo pushed_at 2025-05；247 stars；OpenHub 标 activity decreasing。"living documentation" 的 HTML+fixture 双写成本从未解决。
4. **Cucumber——工具不死，叙事已死（反例）**。cucumber-js pushed 2026-09-20 活跃；@cucumber/cucumber npm 月下载 2024-01=3.71M → 2026-03=8.67M **在增长**（CI 存量+管道惯性）；但旧包 `cucumber` 月下载 1.80M→0.77M 腰斩；HN 相关帖 2024 后全部 1–6 分 0 评；testRigor 等营销文公开宣告 "Cucumber is Dead, AI is Replacing It"。**自然语言规格层的存在理由（让非程序员读懂测试）正被"LLM 直接读懂/生成测试"掏空。**
5. （补充）**新一代的死法变了：冷启动失败**。Spaceport（Show HN 2024-12-30，2 分 0 评，repo 已无）、Testified（2025-01-11，6 分 0 评）——不是停更而是 launch 即无人问津，连尸体都不留。对照活跃度：Karate repo 活跃（8.9k★）但 Maven Central 停在 1.4.1（2023-10，分发退化）；FitNesse 半死不活（GitHub 镜像 pushed 2023-12 vs Maven 20250223 release，数据张力引用需标低置信）。

**共同死根**：spec 文件与 step 绑定的**双写成本**从未被消除，漂移后 spec 变负债。对 2026 浪潮的警示：若新编译器仍要求人写结构化 spec，LLM 只是自动化了绑定代码生成——死根未除；存活形态是 Cucumber 式"管道惯性存量"，而非新增需求。

### §7 总判读（五句）

1. 这条路线 2026 年处于**产品化前夜、且按子方向严重分化**：工具化信号密集但商业层几乎空白（六路调研中仅 Braintrust/Pactflow/Certora 有商业定价，且无一家公开报价单）。
2. **先跑通的是"验证器插进 agent 循环"形态**，而非"spec 编译器"形态：Hypothesis /hypothesis 命令（官方产品化+56% 真 bug 率论文背书）和 nax 式验收测试驱动循环是仅有的两个有真实分发/效果数据的点。
3. **spec→测试编译器本身仍是手艺阶段**：2026 新工具 stars 0–118、月下载个位数百位数、HN 全零讨论，且多数把 spec 当一次性燃料丢弃——恰与验证优先派"spec 是可持久工件"的核心主张背道而驰。
4. **形式化验证的瓶颈（写规约）正被资本和共识认领**（⚠ 本行及上表融资数字均为二手转引未回源，证据链强度：中）（Certora/AWS/Theorem/学术 SpecGen 系全部押注"LLM 写 spec、证明器发证明"），但其产品化被锁在垂直域，通用封装未出现。
5. **反信号给出最硬的边界条件**：上一代死于双写成本与漂移负债，下一代若不解决 spec↔tests↔code 三角的回写规则（mk-spec-master 的覆盖矩阵、facts 的 @implemented 标签是目前仅有的机制化尝试），2026 浪潮会以同样方式退潮——区别只是这次连尸体（低 star、零讨论）都更难观测。

---

## 6. 一段话回填光谱

验证优先形态在底稿光谱上处于"中左：持久但必须机器可校验"。深挖后其真实边界更窄也更硬：它**不是** SDD 的加强版，而是把 SDD 的合法性判据从"写清楚了"换成"被验证器消费了"；其最可行的载体依次是 command-fact（成本最低）、编译为测试（工程主流）、形式化属性（仅限纯函数核心）；其永恒的例外是 discovery、意图性需求与 spec≈implementation 的领域。HN 118 条评论的最大产出不是给 VSDD 盖章，而是把"验证"从提案里的一个 Phase 变成了整个讨论的公理——包括最激烈的反对者也在争论"哪种验证、多早验证"，无人再为"裸 markdown spec 足够"辩护。
