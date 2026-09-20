# 验证优先 / 可验证 spec——「未被验证器消费的 spec 没有控制力」

```yaml
topic: SDD 替代形态之一：验证优先/可验证 spec（VSDD、compilable specs、facts）
accessed_at: 2026-09-20
parent: ../alternatives.md#1
scope: 2026 年材料优先（VSDD 提案 2026-02-28；av/facts 2026-05-04；specdown / whenwords 2025Q4–2026）
sources:
  一手:
    - VSDD gist 原文 https://gist.github.com/dollspace-gay/d8d3bc3ecf4188df049d7a4726bb2a00
    - HN 47197595 全部 118 条评论（hn.algolia.com API 抓取，211 分）
    - av/facts README（github.com/av/facts）+ HN 48008906 作者回帖（7 分/4 评）
    - specdown README（github.com/corca-ai/specdown，可执行 Markdown spec，dogfooding + live report）
    - whenwords 仓库及 issue #6（github.com/dbreunig/whenwords）
    - Verus-SpecGym arXiv 2605.26457（标题已回源确认）
  二手:
    - Midas Tools《VSDD: The AI Coding Methodology Actually Worth Stealing》(dev.to, 2026-03-01/修订 2026-04-14)
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
2. **spec 是你唯一还能完全掌控的产物**（virgilp）：spec 值得花比实现更多的时间，因为它是你还能完整读、完整懂的部分；有了好需求，你才有资格"回头问另一个 AI：实现符合 spec 吗"。他直接反驳 _pdp_：你无法要求 AI 建出好的"某个东西"，除非你能说清那个东西是什么；需求越含糊，只有在"很多人造过同类东西"时才碰巧可行。
3. **压缩后的瀑布不再是瀑布**（virgilp/zozbot234）："months 压缩到 days/hours，90 年代的人不会认出这是 waterfall"；而且 spec 反正必然存在——区别只在它是显式的、有人参与的文档，还是 improvised 在 AI 的隐藏思维 token 里。"总有一个 spec，包括你发的每条非正式 prompt。"
4. **代码成本归零改写了 spec 的旧账**（noosphr）：旧时代 spec 最大的痛是"prover 通过后才发现漏了一个 business case，全部推倒"；现在 bottom 98% 可以交给机器人 + 明确的成功信号，改 spec 的代码成本也为零。baq 的提法最凝练：**spec 是 coding pipeline 各产物的 ECC（纠错码）**——spec 与代码正交，两边都可以迭代。
5. **实践自证的小生态**（多条）：mirekrusin 给出 SPEC.md（追问到 ok 才过）→ PLAN.md（拓扑排序步骤）→ 逐步实现+测试 的循环；michaelbrave 描述 Claude 写文档/Gemini 写测试与代码/Codex 跑流水线修 bug 的多模型分工；gck 主张 clean-room 整体重写循环——"增量 spec 化不 work，agent 永远不会选那条难而正确的路，除非只带上一轮的重要教训从零再来"。theptip 给出适用边界：vibe coding 会杀死探索乐趣，但**大系统 core 里 vibe coding 本来就进不去**，那里需要的正是更形式的东西。

### 1.4 社区把这个提案修正成了什么样

原提案的**全套门禁（Epics/beads/Sarcasmotron/数学证明）没有整体落地者**；讨论收敛出一个被二手文（Midas Tools）明确公式化的"80/20 修正版"：**偷 spec 纪律，跳过仪式**——写 5–10 句"做什么/绝不做什么/三种最可能的失败模式"，交给 agent；产出贴进全新上下文要最狠的批判；修真问题、无视理论问题。三个方向性的修正仍在讨论里成形：

- **门禁从 prompt 移到模型外**：cadamsdotcom 的 CodeLeash 用 Claude Code hooks 强制 TDD 流程——"模型不能忘记或跳过步骤"；他同时给出 compilable specs 的工具化愿景："SDD 大概意味着造出跟踪 code↔spec 映射的工具，把映射当数据管理，然后查询数据确认全部映射——而不是反复礼貌地请求昂贵且不可靠的模型"。tinodb 独立复述了同一思路（enforced TDD 状态机）。
- **对抗 reviewer 的可信度升级**：teiferer 只买形式化验证的账——"把 AI verifier 换成骗不了的东西我就上车"；mirekrusin 的折中是把验证谱系摆开：自然语言 spec 也算一种（模糊的）验证表达，另有 typechecker、测试、linter（正确性向的 lint 规则）。
- **LLM 自产测试的去毒化**：WestN 的 BDD 替代论获得附议（esperant 指出 vitest 等 BDD 风格已是主流默认），指向"spec 编译目标应是人类可读的行为断言而非 LLM 自由发挥的测试代码"。

---

## 2. compilable specs 的实践样例（2026 年，真实团队/项目）

**学术锚**：Verus-SpecGym（arXiv 2605.26457，标题已回源）把"spec→形式规约"的 autoformalization 做成 agentic 评测环境——说明"从 NL spec 编译出可验证约束"已被当作可度量的模型能力来评测，而非只是口号。近旁还有 Specification Grounding 与测试有效性关系的实证线（semantic scholar 收录）与 arXiv 2605.01160 的"specification-driven governance"治理框架。Sadogursky 的 "intent integrity chain"（意图→验证管线保证人类意图存活到生产）常被引为实践方法论，但其原文章节在观测日已 404，只作转引。

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
5. **验证物自身的漂移与作弊**：whenwords #6 证明编译产物（tests.yaml）与母本（SPEC.md）会冲突且需人裁；LLM 写的测试会同义反复、mock 过度、断言实现细节（Sarcasmotron 清单自认）；让验证层完全依赖 LLM 等于把合约交回给被合约约束的一方。**编译没有消灭 consistency tax，只是把它从 spec↔code 转移为 spec↔tests↔code 三角**——这正是 dbreunig 三角模型的原始含义。

---

## 5. 团队落地建议

**什么信号说明你该用这形态**：
- 失败成本不对称：正确性敏感的核心（支付、权限、解析器、协议、数据完整性），一个 escape bug 的代价 >> 写验证spec 的成本；
- spec 与实现的复杂度比有利（alpaylan 条件）：你能用比代码短得多的语言说清"什么必须为真"；
- 已出现 spec 债症状（spec 与代码打架、没人敢删旧 spec）但任务本身契约清晰——这是 facts 形态的入场信号；
- 多人/多 agent 并行需要**共享的机器可查合约**，而不是又一轮 prompt 谈判；
- brownfield core：vibe coding 进不去、必须有人类可审计的验证层的地方（theptip 条件）。

**不该用的信号**：探索期产品（先 prototype onion 再冻结）、spec 复杂度逼近实现的领域算法、需求方不投入前期反馈（daveac：AI 把瓶颈移到了需求发现/签核端，验证 spec 救不了不参与的 sponsor）。

**起步三步**：
1. **事实化**：把现有 spec（或直接从代码逆向，zozbot234 指出 AI 逆向 spec 无瀑布先例）压缩成 facts 式原子清单：每条一句声明 + 生命周期标签；凡是能用命令核对的，立刻加 `command`（grep/test/单测均可），跑起来并接 CI——这就是你的最小 compilable spec，一天内可完成，不需要任何新框架。
2. **门禁移出模型**：为新功能写 5–10 句行为契约（做什么/绝不做什么/三类失败模式），把每条契约编译为可执行断言（测试或 command-fact），并用 hooks/CI 强制"无失败测试不写实现"——借鉴 CodeLeash 的原则：强制力放在模型外，靠提示词维持的纪律必然衰减。
3. **加对抗闭环 + 回写规则**：冻结后把产出交给全新上下文的 reviewer（LLM 或同事均可）做超批判审查，重点抓 tautological tests 和"标为 test-only 其实该 prove 的性质"；同时把"spec 更新了吗？"写进 DoD——whenwords #6 与 dbreunig 自我推翻已经证明：没有回写规则的可验证 spec，只是把漂移问题搬进了测试文件。

---

## 6. 一段话回填光谱

验证优先形态在底稿光谱上处于"中左：持久但必须机器可校验"。深挖后其真实边界更窄也更硬：它**不是** SDD 的加强版，而是把 SDD 的合法性判据从"写清楚了"换成"被验证器消费了"；其最可行的载体依次是 command-fact（成本最低）、编译为测试（工程主流）、形式化属性（仅限纯函数核心）；其永恒的例外是 discovery、意图性需求与 spec≈implementation 的领域。HN 118 条评论的最大产出不是给 VSDD 盖章，而是把"验证"从提案里的一个 Phase 变成了整个讨论的公理——包括最激烈的反对者也在争论"哪种验证、多早验证"，无人再为"裸 markdown spec 足够"辩护。
