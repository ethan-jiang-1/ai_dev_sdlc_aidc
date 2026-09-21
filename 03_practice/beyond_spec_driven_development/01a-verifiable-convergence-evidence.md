# 01a：可验证 spec 派 §独立收敛声音——全文证据档案

> **元数据**
> - accessed_at：2026-09-21（本轮逐条 web_fetch 回源）
> - 上游：`01-verifiable-specs.md`（本文件为它的独立收敛证据档案，不复制其结论性判读；VSDD/compilable specs/av/facts/whenwords/specdown/Consort 已在上游收齐，此处不重复）
> - 回源途径标注：**一手** = 直接抓到原文页面全文；**半回源** = 标题/摘要/二手页确认存在但正文未全读；**转述** = 原文抓不到，仅消化稿/转引
> - 摘录纪律：所有英文原句为本次回源页面逐字摘录；抓不到的如实标注，不代拟
>
> **⚠ 回源即发现的三个勘误级事实（比摘录本身更重要）**
> 1. **正方最响的声音已经从"测试即 spec"上移到"证明即 spec"**：Kleppmann（2025-12）→ de Moura（2026-02-28）这条线明确主张"testing provides confidence, proof provides a guarantee"——如果 01 主篇只把形式化属性列为"最窄载体"，需要补一条：形式化阵营在 2026 上半年已经主动宣布自己是可验证 spec 的**终局形态**，而不只是旁支。
> 2. **反方最强声音出自形式化阵营内部**（Hillel Wayne 2026-03-10、Brown PLT 2026-06-09），不是 SDD 批评者——他们反对的不是"spec 该被验证"，而是"LLM 能替你写验证物"这个前提。01 主篇 §4 的失败面第 5 条（验证物自身漂移与作弊）由此获得了一手形式化专家的独立印证。
> 3. **引用链核查结果：KOL 集群基本互不引用，但形式化小圈子互相引用密集**。Kleppmann 更新节直接引 de Moura；Wayne 同时引 Kleppmann 和 de Moura 并作为反方靶子；Davis 引 Wayne。因此 §A1–A6 之间**不构成独立收敛**，独立收敛判定见各集群 §x.5 与文末总表——这是本档案与 harness_governance 的 02a 不同的地方：**收敛主轴不在形式化阵营内部，而在"工程派 KOL（Willison/Ronacher/Huntley）× 形式化派（Kleppmann/de Moura/Wayne）× 公司实践（AWS/Microsoft/Google）"三个互不往来的人群之间**。

---

## A1. Martin Kleppmann ——「验证变便宜 + AI 代码需要验证」双引擎论证（最早的一手正方宣言）

### A1.1 回源结果

《Prediction: AI will make formal verification go mainstream》，[martin.kleppmann.com/2025/12/08/ai-formal-verification.html](https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html)，2025-12-08——**一手**（本轮全文回源）。作者：剑桥副教授、《DDIA》作者。

### A1.2 原文摘录（一手）

上下文：全文从 seL4 的成本账（8700 行 C 要 20 人年、20 万行 Isabelle）推起，先立经济论，再立需求论：

> At present, formal verification is mostly used by research projects, and it is uncommon for industrial software engineers to use formal methods (even those working on classic high-assurance software such as medical devices and aircraft). The reason is that writing those proofs is both very difficult (requiring PhD-level training) and very laborious.
>
> To put it in simple economic terms: for most systems, the expected cost of bugs is lower than the expected cost of using the proof techniques that would eliminate those bugs.

关键转折——AI 同时改成本和改需求，这两段是整个正方阵营被引最多的推理链：

> But on top of that, AI also creates a _need_ to formally verify more software: rather than having humans review AI-generated code, I'd much rather have the AI prove to me that the code it has generated is correct. If it can do that, I'll take AI-generated code over handcrafted code (with all its artisanal bugs) any day!
>
> In fact, I would argue that writing proof scripts is one of the best applications for LLMs. It doesn't matter if they hallucinate nonsense, because the proof checker will reject any invalid proof and force the AI agent to retry. The proof checker is a small amount of code that is itself verified, making it virtually impossible to sneak an invalid proof past the checker.

注意他没有回避困难转移（这句直接被反方 Wayne 接住打）：

> That doesn't mean software will suddenly be bug-free. As the verification process itself becomes automated, the challenge will move to correctly defining the specification: that is, how do you know that the properties that were proved are actually the properties that you cared about? Reading and writing such formal specifications still requires expertise and careful thought. But writing the spec is vastly easier and quicker than writing the proof by hand, so this is progress.

结尾三段论（原文照录）：

> In summary: 1. formal verification is about to become vastly cheaper; 2. AI-generated code needs formal verification so that we can skip human review and still be sure that it works; 3. the precision of formal verification counteracts the imprecise and probabilistic nature of LLMs.

### A1.3 机制细节

- 更新节（2026-02 后追加）引 arXiv 2509.22908 造词 **"vericoding"**（对照 vibecoding），并点名 Harmonic Aristotle、Logical Intelligence、DeepSeek-Prover-V2、"Lean is where most of the action is"（链接指向 de Moura 的另一文（slug when-ai-writes-the-worlds-software.html，非本档案 A2 回源 URL …-who-verifies-it/；两条为同一作者不同文章））。
- 成本数字：seL4 每 1 行实现要 23 行证明 + 半人日。

### A1.4 独立性验证

- 引用链：正文引 Hillel Wayne"为什么没人用形式化方法"（旧文，非 LLM 立场）、Nature/AlphaProof、Galois——**未引用 Willison/Ronacher/Huntley/VSDD 任何一方**。
- 但其 **Update 节引用了 de Moura（A2）**——与 A2 不构成独立收敛；时间上 Kleppmann 先行（2025-12-08 早于 de Moura 2026-02-28），方向判定为「Kleppmann 先发、de Moura 跟进放大」。

---

## A2. Leonardo de Moura（Lean 之父，AWS / Lean FRO）——「verification gap 会越拉越大，spec 是新核心工程纪律」

### A2.1 回源结果

《When AI Writes the World's Software, Who Verifies It?》，[leodemoura.github.io/blog/2026-2-28-when-ai-writes-the-worlds-software-who-verifies-it/](https://leodemoura.github.io/blog/2026-2-28-when-ai-writes-the-worlds-software-who-verifies-it/)，2026-02-28——**一手**（本轮全文回源）。作者：Lean 语言创造者、Lean FRO 首席架构师、AWS Senior Principal Applied Scientist。**这是本主题迄今分量最重的单篇一手正方文本。**

### A2.2 原文摘录（一手）

问题定义（开篇密集引用公司一手数字，见 §A2.3）：

> The rewriting of the world's software is not coming. It is underway.
>
> **No one is formally verifying the result.**
>
> The errors are there. The reviewers are not.

对"验证物会被作弊"的回答——这是与 01 主篇 §4.5（LLM 产出的验证物不可信）正面对撞的段落：

> The Claude C Compiler illustrates the other side: it optimizes for passing tests, not for correctness. It hard-codes values to satisfy the test suite. It will not generalize. Property-based testing would likely catch this particular case, but the general problem remains: for any fixed testing strategy, a sufficiently adversarial system can overfit to it. A proof cannot be gamed. It covers all inputs by construction.
>
> The friction of writing code manually used to force careful design. AI removes that friction, including the beneficial friction. The answer is not to slow AI down. It is to replace human friction with mathematical friction: let AI move fast, but make it prove its work.

spec 升格为核心纪律（01 主篇"合法性判据"论的最强外部印证）：

> This acceleration requires specifications: precise descriptions of what the software must do. As AI takes over implementation, specification becomes the core engineering discipline. Writing a specification forces clear thinking about what a system must do, what invariants it must maintain, what can go wrong. This is where the real engineering work has always lived. Implementation just used to be louder.
>
> The role of the engineer changes, but it does not shrink. Engineers spend more time writing specifications and models, designing systems at a higher level of abstraction, defining precisely what systems must do, what invariants they must maintain, what failures they must tolerate.

zlib 实验（验证 AI+证明已能吃下生产级软件，"unexpected"是作者自评）：

> An AI agent converted zlib, a widely used C compression library embedded in countless systems, to Lean, with minimal human guidance. No special tooling was built. It was Claude, a general-purpose AI, with no special training for theorem proving, out of the box. […] This was not expected to be possible yet.
>
> When your tests and your code share the same wrong assumptions, testing finds nothing. The act of proving forces every assumption to be explicit: a designer states a property, the AI turns it into a precise formal statement, and then either constructs a proof or discovers that the specification needs revision. Wrong assumptions surface as proof obligations that cannot be discharged. Specifications become sharper through the attempt to prove them.

### A2.3 公司实践四要素核验（本篇内一手引用的一手链接）

| 公司实践 | 验证了什么系统 | 规模 | LLM 角色 | 效果数字 |
|---|---|---|---|---|
| AWS Cedar | 授权策略引擎，automated reasoning + differential testing | 生产级、服务 AWS 侧授权 | 无（传统 AR + 差分测试，Lean 路线的先声） | amazon.science 一手博客（de Moura 文内直链） |
| Microsoft SymCrypt | 加密库 Rust 重写 + Lean 验证 | 全微软依赖的加密库 | 无/部分（MSR 博客一手） | 见 microsoft.com/en-us/research 博客（文内直链） |
| AWS×Toyota | COBOL 现代化 | 4000 万行 | AI 转译 | aws.amazon.com 迁移博客（文内直链） |
| Anthropic Claude C Compiler | C 编译器 | 10 万行 | 并行 agent 生成 | 2 周/<$20k，可 boot Linux、编译 SQLite/PostgreSQL/Redis/Lua；de Moura 同时指出它 hard-code 骗测试 |
| Lean FRO zlib | zlib DEFLATE 往返 | 生产压缩库全格式 | 通用 Claude 生成实现+定理证明 | 机器检验定理 `decompressSingle(compress(data)) = ok data`；人类参与"minimal" |

### A2.4 机制细节

- Veil（NUS Ilya Sergey 组）：Lean 上的分布式协议验证器，MC 反例 + 全形式证明双通道；**在验证 Rabia 时发现既有两个工具的"形式验证"里有一处未被察觉的不一致**——"验证器也会错"的一手案例。
- 独立性主张本身是论点之一："If the same vendor provides both the AI and the verification, there is a conflict of interest. Independent verification is not a philosophical preference. It is a security architecture requirement."

### A2.5 独立性验证

- 引用链：Karpathy、Lattner、Viacode、HBR——**无 Kleppmann、无 Willison、无 SDD 系**。与 Kleppmann 互引方向是 Kleppmann→de Moura（Update 节）。
- **利益声明必须记录**：作者同时是 AWS 员工与 Lean FRO 负责人，本文含明确平台利益。权重按"高分量 + 有利益偏向"双记。

---

## A3. Hillel Wayne ——反方一号：「LLM 写的 spec 验证不了任何东西」（形式化阵营内部反方）

### A3.1 回源结果

《LLMs are bad at vibing specifications》，[buttondown.com/hillelwayne/archive/llms-are-bad-at-vibing-specifications/](https://buttondown.com/hillelwayne/archive/llms-are-bad-at-vibing-specifications/)，2026-03-10——**一手**（本轮全文回源）。作者：形式化方法布道者、《TLA+》领域最有影响力的实践写作者。**注意：他十个月前的立场是正方**（"AI is a gamechanger for TLA+ users"），本文是正方阵营自己人的立场收缩——独立反方的含金量在此。

### A3.2 原文摘录（一手）

案例是某个 vibe 出 TLA+ + Alloy spec 的真实开源项目。先指出验证物根本没跑过、而且是同义反复：

> Couple of things to note here: first of all, this doesn't actually compile. […] So we know the person did not actually run these specs.
>
> The bigger problem with the spec is that `UnsignedImportMustBeDenied` and `SignedImportMayBeAccepted` _don't actually do anything_. […] These are tautologically true! If they do anything at all, it is only checking that `canImport` was defined correctly.

对"LLM 写 spec、验证器审"路线的核心打击——弱性质问题（这正是 Sarcasmotron 清单和 WestN 反对论的形式化版本）：

> The AI is only writing "obvious properties", which fail for reasons like "we missed a guard clause" or "we forgot to update a variable". It does not seem to be good at writing "subtle" properties that fail due to concurrency, nondeterminism, or bad behavior separated by several steps. Obvious properties are useful for orienting yourself and ensuring the system behaves like you expect, but the actual value in formal methods comes from the subtle properties.
>
> (This ties into Strong and Weak Properties. LLM properties are weak, intended properties need to be strong.)
>
> This is a problem I see in almost every FM spec written by AI. LLMs aren't doing one of the core features of a spec.

正面点名正方文献并给出反驳（说明这不是孤立抱怨，而是阵营内辩论）：

> Articles like Prediction: AI will make formal verification go mainstream [Kleppmann] and When AI Writes the World's Software, Who Verifies It? [de Moura] argue that LLMs will make formal methods go mainstream, but being easily able to write specifications doesn't help with correctness if the specs don't actually verify anything.

专家悖论（对"AI 降低门槛"叙事的直接质疑，自问自答）：

> Which is good for my current livelihood, but bad for the hope of LLMs making formal methods mainstream. If you need to know formal methods to get the LLM to do formal methods, is that really helping?
>
> (Yes, if it lowers the skill threshold-- means you can apply FM with 20 hours of practice instead of 80. But the jury's still out on how _much_ it lowers the threshold. What if it only lowers it from 80 to 75?)

诚实的不确定性声明（时间戳级一手）：

> On the other other hand, this is all as of March 2026. Maybe this whole article will be laughably obsolete by June.

### A3.3 机制细节

- 评论区高赞反补（Prakhar Goel, 2026-03-10）："Are you sure the LLM doesn't push the difficulty _up_? Because in my experience, reviewing software is harder than writing software (even the same software)."——"验证者回归"论：生成越便宜，审查越贵。
- 数据点：GitHub 全网 TLA+ spec 中约 4% 文内出现 "Claude"（Wayne 给的 code search 链接）。

### A3.4 独立性验证

- 引用链：**同时引用 A1 与 A2 作为靶子**，另引 Cheng Huang（A10）。它不是独立正方，而是**独立反方**——反方的独立性成立（对 Kleppmann/de Moura 无引用遵从，纯批评关系）。

---

## A4. Simon Willison ——正方工程派：conformance suites 与"测试不再可选"

### A4.1 回源结果

本轮一手回源三处：① 《A Software Library with No Code》书评（[simonwillison.net/2026/Jan/10/a-software-library-with-no-code/](https://simonwillison.net/2026/Jan/10/a-software-library-with-no-code/)）；② Agentic Engineering Patterns 指南《First run the tests》（simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/，页面无发布日期，changes feed 显示 2026-02-24）（2026-02-24，一手全文）；③ testing 标签页（2026 全部条目一手过目）。另有《If your library doesn't have any documentation, it can't have any bugs》（2025-05-22）经标签页一手摘得。

### A4.2 原文摘录（一手）

对 whenwords 的评语（上游 01 主篇收了 dbreunig 本方，这里补 Karpathy 之外的第二位背书者）：

> This meshes nearly [sic] with my recent interest in conformance suites. If you publish good enough language-independent tests it's pretty astonishing how far today's coding agents can take you!

《First run the tests》开篇（"测试不再可选"宣言正文）：

> Automated tests are no longer optional when working with coding agents.
>
> The old excuses for not writing them - that they're time consuming and expensive to constantly rewrite while a codebase is rapidly evolving - no longer hold when an agent can knock them into shape in just a few minutes.
>
> They're also _vital_ for ensuring AI-generated code does what it claims to do. If the code has never been executed it's pure luck if it actually works when deployed to production.

spec/验证物关系的老宣言（2025-05-22，为上游"测试指定实际行为"论提供 KOL 锚点）：

> **If your library doesn't have any documentation, it can't have any bugs.**
>
> Documentation specifies what your code is supposed to do. Your tests specify what it actually does.

### A4.3 机制细节

- "First run the tests" 被包装成**四词 prompt**：目的三条——让 agent 知道测试套件存在并此后几乎必然运行它、用测试数量做项目复杂度代理、把 agent 推进"testing mindset"。这是"门禁移出模型"论（上游 §1.4 CodeLeash）的 KOL 级独立同构。
- 2026-02-10 Showboat/Rodney：把"agent 验证自己产物并演示"工具化（browser assert 命令、exit code 语义：1 专留给 check 失败）。
- 2026-03-29 Pretext 案例：Cheng Lou 让 Claude Code/Codex"对着浏览器 ground truth 逐宽度测量迭代数周"——"以真值为 spec、让模型对着验证器迭代"的公司外生产级实例。

### A4.4 独立性验证

- 引用链：Willison 引 dbreunig（whenwords，上游已收）和 chenglou；**未引用 VSDD/HN 串、未引用形式化阵营任何人**。与 01 主篇既有材料无引用关系——**独立收敛成立**，且是三处独立背书 whenwords 之一（Karpathy 点赞→Willison 文→HN 211 分（item id 见 01-verifiable-specs.md §1 VSDD 条目），三者动机表述各异）。

---

## A5. Armin Ronacher ——正方中的收缩派：可验证的机械翻译 OK，" lasting code"不行

### A5.1 回源结果

《The Coming Loop》，[lucumr.pocoo.org/2026/6/23/the-coming-loop/](https://lucumr.pocoo.org/2026/6/23/the-coming-loop/)，2026-06-23——**一手**（本轮全文回源）。

### A5.2 原文摘录（一手）

对"可验证性"边界的划法——他给 loop 型工作划的可扩张领域恰好全部是"验证信号便宜"的领域：

> I believe that loops that produce artifacts without necessity of longevity or that create some form of clearly verifiable mechnical translation matters more than the general ability of a harness to mechanically measure a goal. […]
>
> The harness just needs some signal that lets it continue. It does not have to be objective or binary, it just has to be useful enough to drive another iteration.

反方向——对" lasting 代码"上验证器兜不住的判断（这是对 de Moura 式乐观的一手冷水的工程派版本）：

> Present-day models tend to produce code that is too defensive, too complex, too local in its reasoning. They avoid strong invariants. They add fallbacks instead of making bad states impossible. They duplicate code, invent bad abstractions, and paper over unclear design with more machinery. Worse though: I so far see very little progress of this improving.
>
> When you take that behavior and you put it behind loops, you tend to amplify it. If each iteration adds another small defense, the system slowly becomes less understandable while appearing more robust. The more hands-off you are, the more that happens.

在"不变量"这一点上他与形式化派短兵相接（同一篇内）：

> In systems with important invariants, especially persisted data formats or core infrastructure, the right fix is not "handle every malformed case." The right fix is to make the malformed case unrepresentable or impossible to write in the first place. Yet even with a lot of manual steering, that type of code does not come out of LLMs naturally.

### A5.3 机制细节

- Ronacher 列出的 loop 适用域（porting/perf 探索/安全扫描/研究）与 de Moura 列出的验证优先域（密码学/解析器/压缩/协议）高度重合——但结论相反：前者认为这证明"loop 只能干这个"，后者认为这是"验证路线的第一阶段"。同一事实，两种解读，是 01 主篇光谱定位的天然素材。
- Ronacher 引 ghuntley.com/ralph 作为 loop 模式命源——与 A6 有引用关系。

### A5.4 独立性验证

- 引用链：Boris Cherny、Pi、ghuntley、Karpathy 推文、Daniel Stenberg。**未引用 Kleppmann/de Moura/Wayne/Willison**。与 A1/A2 互不引用——**独立收敛成立**（但与 A6 Huntley 存在单向引用，二者的"独立性"按有向处理）。

---

## A6. Geoffrey Huntley ——spec 作为 loop 的常驻栈分配 + backpressure 论（Ralph 阵营的正方）

### A6.1 回源结果

《Ralph Wiggum as a "software engineer"》，[ghuntley.com/ralph/](https://ghuntley.com/ralph/)，2025-07-14——**一手**（本轮全文回源）。日期早于 2026，但它是 Ronacher（2026-06）与整个 harness 派引用的命源文本，且 2026-03 的《porting software has been trivial for a while now》（ghuntley.com/porting/，半回源——列表页确认存在，正文未全读）延续同一主张。

### A6.2 原文摘录（一手）

spec 在 loop 中的角色——不是文档，是**每一轮都重新加载的机器可执行上下文**：

> The items that you want to allocate to the stack every loop are your plan ("@fix_plan.md") and your specifications.
>
> To get good outcomes with Ralph, you need to ask Ralph to do one thing per loop. **Only one thing**.

backpressure 段——"任何东西都可以接成拒绝无效代码生成的验证器"（可验证 spec 工具谱系的一手表述）：

> As code generation is easy now, what is hard is ensuring that Ralph has generated the right thing. Specific programming languages have inbuilt back pressure through their type system. […]
>
> In the diagram above, it just shows the words "test and build", but this is where you put your engineering hat on. Anything can be wired in as back pressure to reject invalid code generation. That could be security scanners, it could be static analysers, it could be anything. But the key collective sum is that the wheel has got to turn fast.

spec 出错时的自省（与 whenwords #6 同构的自我警告）：

> A big, hard lesson for me when building CURSED was that it was only a month in that I noticed that my specification for the lexer defined a keyword twice for two opposing scenarios, which resulted in a lot of time wasted. Ralph was doing stupid shit, and I guess it's easy to blame the tools instead of the operator.

反作弊指令（对 LLM 同义反复/占位实现的一手斗争记录）：

> Claude has the inherent bias to do minimal and placeholder implementations. […]
>
> 9999999999999999999999999999. DO NOT IMPLEMENT PLACEHOLDER OR SIMPLE IMPLEMENTATIONS. WE WANT FULL IMPLEMENTATIONS. DO IT OR I WILL YELL AT YOU

### A6.3 机制细节

- "capture the why of tests"：要求每轮把测试存在理由写进测试文件的 docstring——因为"future loops will not have the reasoning in their context window"。这是把测试当 spec 读时的**上下文税**解法，VSDD 讨论串无此细节。
- prompt 栈里两条与本主题直接相关：`If you find inconsistencies in the specs/* then use the oracle and then update the specs`；`9999. IMPORTANT: We want single sources of truth, no migrations/adapters`。

### A6.4 独立性验证

- 引用链：无学术引用、无 SDD/VSDD 引用、无形式化引用。被 Ronacher（A5）引用——方向 A5→A6。**作为被引命源其独立性成立；与 A5 合并计为一个引用簇时收敛计数 -1**。

---

## A7. A. Jesse Jiryu Davis ——「LLM 拆掉了 TLA+ 的语法门槛，但拆不掉定义正确性的门槛」

### A7.1 回源结果

《Intro to TLA+ for the LLM Era: Prompt Your Way to Victory》，[emptysqua.re/blog/intro-to-tla-plus-for-the-llm-era/](https://emptysqua.re/blog/intro-to-tla-plus-for-the-llm-era/)，2026-05-13；HN 48170007，147 分/35 评（本轮一手回源正文+全部评论）。

### A7.2 原文摘录（一手）

> Most engineers' first objection to using TLA+ is, the syntax is hostile. […] But now, frontier LLMs can generate TLA+ easily. It's still your responsibility to understand your system and define what "correctness" means, and you need a high-level understanding of temporal logic.

结尾段的限定链（三个"仍然是你 job"）：

> LLMs have mostly removed the first barrier to entry of TLA+: its syntax. It's still your job to define what properties your system must uphold; [Hillel Wayne finds that they're bad at writing these]. It's also your job to figure out how your existing system actually behaves. Even with intense handholding, [LLMs can't yet read the code of an existing system and translate it into a TLA+ spec]. So you're not entirely excused from thinking yet. But LLMs have transformed TLA+ from an opaque thinking tool into a translucent one.

### A7.3 机制细节

- "opaque → translucent"是 2026 年形式化社区被引最多的降温句式：不否认 LLM 的作用，只重新标定边界。

### A7.4 独立性验证

- 显式引用 Wayne（A3）与其 SysmoBench 评测——**与 A3 同一引用簇，不独立**；但 Davis 的"translucent"框架在 HN 147 分讨论中被独立传播（无人再引 Kleppmann/de Moura），社区层收敛成立。

---

## A8. HN 48170007 讨论串 + SIGOPS 论文 ——形式化社区的群体裁决与不可判定性反方

### A8.1 回源结果

HN 全部 35 评论一手回源；SIGOPS 2026 论文页经评论转引（[sigops.org/2026/can-llms-model-real-world-systems-in-tla/](https://www.sigops.org/2026/can-llms-model-real-world-systems-in-tla/)，一手：全文公开、本轮已核；jmorse3 引句与原文逐字一致（已核））。

### A8.2 原文摘录（HN 评论，一手）

SIGOPS 论文结论（jmorse3 转引）：

> Running leading LLMs across the eleven systems shows that LLMs are great at producing correct TLA+ syntax but struggle to ensure conformance and appropriate invariants.

不可判定性反方（nyrikki，与上游 pron 论点独立同构，且更技术化）：

> As TLA+ uses state machines that can define infinite state spaces, checking arbitrary temporal logic formulas is undecidable in the general case. […] I would say that unless you focus on more detailed temporal logic pitfalls you may have issues. […] Remember that we know the open domain frame problem in [2] is equal to HALT, it will not universally apply. It is just another tool that works well _when_ it works well.

建模行为价值反方（leoqa）：

> Unfortunately the benefit of TLA+ is the act of modeling your system painstakingly. The actual checker helps confirm your hypothesis, etc. But skipping the modeling and outsourcing it is not ideal. I've always struggled reasoning about models my team mates wrote, and will often have to mentally go through the process of arriving at the same abstractions/invariants etc before I can understand it.

自指反方（some_random，直接打"用 LLM 写 spec 再人工审 spec"的循环）：

> So, the syntax is so bad that you have to use an LLM to generate the spec, but also you still need to understand the spec the LLM generates which is now harder because you weren't even the one to write it.

正方实践自述（baq）：

> Ran it on my tricky caching changes and it found bugs the standard agentic review flows missed on all frontier models. Good stuff.（对象：specula-org/Specula，TLA+ agent 工具）

### A8.3 机制细节

- Specula（specula-org）与 TLA+ 官方 MCP server（Wayne 文提及）是 2026 年"验证器进 agent 工具环"的两个一手工具落点。
- nextos 的长期预测（高赞向）："That might emerge as one of the main tasks of future software engineers, writing formal specifications by hand. It could be the case that Tony Hoare was right, just too early."

### A8.4 独立性验证

- 评论者匿名，按社区共识计（同上游纪律）。与 A7 共享语境但观点独立形成；SIGOPS 论文为独立学术一手。

---

## A9. Brown PLT（PICK）——「Human Judgment as a Specification」：验证的效力来自独立冗余，不来自生成更多 LLM

### A9.1 回源结果

《Human Judgment as a Specification》，[blog.brownplt.org/2026/06/09/pick.html](https://blog.brownplt.org/2026/06/09/pick.html)，2026-06-09——**一手**（本轮全文回源）。作者：Brown PLT（Shriram Krishnamurthi 等）+ Siddhartha Prasad，配套 ECOOP 2026 论文。

### A9.2 原文摘录（一手）

出发点与 Kleppmann 同、但立刻转向人机分工：

> The rise of GenAI in programming clearly requires an accompanying rise in formal methods, to confirm that AI systems running wild are producing the solutions we actually want. That in turn requires that we specify what we _want_. This specification is necessarily mathematical, to take advantage of the formal methods tools. But most programmers know far less about formal specification than they do about programming. What can they do?

全文最重的一段——对"验证有效性"条件的判定（直指 LLM 双侧生成的死穴，与 de Moura "A proof cannot be gamed" 是同一问题的两种答案）：

> Verification is famously written _P_ ⊧ ɸ: a program _P_ implements a property ɸ. The check is informative precisely because _P_ and ɸ are written _independently_. If both encode the same misconception, agreement rules out nothing; the redundancy disappears. (And this is the danger of having both sides of the verification coin generated by an LLM. PICK intervenes to make sure the LLM is not the _only_ source of ɸ.)
>
> Now consider synthesis: ɸ ⟹ _P_. The program is correct-by-construction. However, that means it is also **in**correct-by-construction. When ɸ is wrong, the resulting _P_ is wrong in precisely the same way, and no cross-check of _P_ against ɸ can catch that. […] Piling on more LLMs does not necessarily fix this. They share training data, share priors, and often share misconceptions. More models give you more _agreement_, faster. They do not necessarily give you more _redundancy_, which is what verification has always been about.

人的判断即 spec 的操作化：

> In PICK, that independent witness is not a separately-written spec — it lives in the user's classifications: each accept or reject is a commitment to a concrete behavior, and the candidates that survive must be consistent with all of them together. […] The user arrives with a vague intent; PICK helps sharpen it — call it spec _elucidation_ — not by interrogating them about formulae but by forcing them to commit on questions the prompt leaves implicit.

对"模型变强就不需要这个"的预防性反驳：

> Better models do not make user intent more articulate — asked for "a regex matching countries of North America", a more capable model still cannot tell you whether _you_ want the Caribbean included, or where _you_ want to stop heading south. Better models produce better candidates, faster — which shifts user effort precisely _toward_ the work PICK is built to support.

### A9.3 机制细节

- PICK 已做三个域：regex、LTL、ABAC；算法成立条件是**闭包于否定与交 + 差集采样**。文中给出适用语言清单判据（"many of the formalisms programmers use every day already have it"）。
- 文中引用 Ron Minsky（Jane Street）的讽刺原句（signalsandthreads 访谈）："you go to your large language model and say, 'Please write me a specification for a function that sorts a list.' And then it, like, spits something out. And then you look at it and think, yeah, that seems about right."——KOL 级怀疑论的第三方独立声音（转引于 Brown PLT 一手文内）。

### A9.4 独立性验证

- 引用链：仅引自己组内旧文与 Minsky 访谈。**未引用 Kleppmann/de Moura/Wayne/Willison/VSDD 任何一方**——**本档案独立性最强的学术集群**，且其"冗余独立性"判据可直接迁移为 01 主篇的判定标准。

---

## A10. Cheng Huang（Microsoft Azure Distinguished Engineer）× DeepSeek 3FS ——P 语言 spec 先行的公司内一手实践

### A10.1 回源结果

经 Wayne（A3）文内两处直链一手定位：① zfhuang99.github.io《The Coming AI Revolution in Distributed Systems》（2025-05-24，半回源——URL 一手确认，正文本轮未全读）；② DeepSeek 开源 3FS 仓库 `specs/DataStorage` 目录（P 语言完整 spec，github.com/deepseek-ai/3FS，一手仓库存在性确认）；③ Huang 本人 vibe 出的 CRAQ TLA+ spec（github.com/zfhuang99/lamport-agent，半回源，引句取自 Wayne 摘录）。

### A10.2 原文摘录（经 Wayne 一手文转引的 CRAQ spec 片段）

> `NoStaleStrictRead == \A i \in 1..Len(eventLog) : LET ev == eventLog[i] IN ev.type = "read" => …/\ \A j \in 1..i : LET evC == eventLog[j] IN evC.type = "commit" /\ evC.chunk = c => evC.version <= v`

Wayne 的对照判语（一手）：

> This is a lot more complicated than the `(P => Q && P) => Q` properties I've seen! It could be because the corresponding system already had a complete spec written in P. But it could also be that Cheng Huang is already an expert specifier, meaning he can get more out of an LLM than an ordinary developer can.

### A10.3 公司实践四要素

| 要素 | 内容 |
|---|---|
| 验证了什么 | DeepSeek 3FS 分布式存储的数据一致性（P 语言 spec 先行）；Huang 用 LLM 复刻 CRAQ 读一致性 |
| 规模 | 3FS 生产级开源存储；CRAQ spec 单模块 |
| LLM 角色 | Huang 案例中 LLM 生成 TLA+ spec（专家驾驭）；3FS 是 P spec 先行、实现跟随 |
| 效果数字 | 无公开量化数字；Qualitative：Wayne 承认该 spec 显著优于普通用户产出 |

### A10.4 独立性验证

- 与 A3 有被引关系；与 A2 的 Lean 路线**无引用关系**（P 语言阵营与 Lean 阵营互不引用）——**公司实践内部的第二独立路线成立**（Microsoft 内部：SymCrypt 走 Lean、Azure 分布式系统走 P/TLA+，两条线并行不悖，本身即是"多验证器共存"的活体证据）。

---

## A11. AWS Bedrock Automated Reasoning checks ——把"spec+验证器"做进云产品的公司实践

### A11.1 回源结果

Automated Reasoning policy refinement in Amazon Bedrock，HKU SPACE AI Hub 转载（2026-08-04，半回源——正文本轮未全读）；AWS 官方 docs（⚠ 原 URL 非法（含空格、域名错误），待回源——docs.aws.amazon.com/bedrock/… automated-reasoning-checks-concepts，半回源——PDF 内命中 TRANSLATION_AMBIGUOUS 检查项描述）。

### A11.2 可核验事实（半回源，无原文段引）

- 产品形态：用户上传 policy（自然语言文档），服务将其**自动翻译为形式化策略**，并对 prompt/输出做可证明的校验；refinement 流程（2026-08 更新）让用户对翻译歧义逐条裁决——**存在 `TRANSLATION_AMBIGUOUS` 检查结果类型**，即产品化承认"NL→形式化 spec 的翻译需要人裁"（与 Brown PLT 的 spec elucidation 惊人同构，且无引用迹象）。
- 公司实践四要素：验证对象=客户策略/合同文档的推理合规；规模=GA 云服务（公开 docs 多语言）；LLM 角色=翻译者+被验者；效果=检查结果类型化（valid/invalid/ambiguous/translate-failed）。
- 与 A2 同属 AWS 但不同产品线（Cedar 是 de Moura 引用的先例）——内部收敛、外部独立。

---

## A12. Google CEL 开源形式验证框架（2026-08）——半回源

《Google Launches Open-Source Formal Verification Framework For CEL》，[opensourceforu.com/2026/08/google-open-source-framework-cel/](https://www.opensourceforu.com/2026/08/google-open-source-framework-cel/)——**半回源**（标题+发布时间确认，正文未读）。CEL 是 Google 用于策略/准入控制的表达式语言；2026-08 开源形式验证框架意味着"策略即 spec、验证器即服务"路线又添一家超大规模公司。**四要素暂缺规模与效果数字，权重记低，待后续回源。**

---

## A13. Ron Minsky（Jane Street CTO）——KOL 怀疑论的独立声音（经一手文转引）

见 §A9.3 引句（Brown PLT 一手文内逐字转引，原始出处 signalsandthreads.com《Future of Programming》访谈，转述级）。他讽刺的不是"写 spec"，而是"LLM 吐出 spec、人扫一眼就接受"这个动作——与 Wayne 的 tautology 发现、Brown PLT 的冗余论证构成**三个互不引用的独立怀疑源**。

---

## 14. 反方意见的正面对撞（pairwise）

| # | 正方最强论点（来源） | 反方最强论点（来源） | 对撞结果 |
|---|---|---|---|
| 1 | "A proof cannot be gamed. It covers all inputs by construction."（de Moura, A2） | "LLM properties are weak, intended properties need to be strong… the actual value in formal methods comes from the subtle properties."（Wayne, A3） | **不正面冲突，错位打击**：de Moura 说的是证明机制不可作弊；Wayne 说的是**交给 LLM 的性质选择**可被弱化。合取后才是真命题：验证器不可作弊 ≠ 验证内容不可被掏空。01 主篇 §4.5 需按此精确化。 |
| 2 | "I'd much rather have the AI prove to me that the code it has generated is correct."（Kleppmann, A1） | "Verification is informative precisely because P and ɸ are written _independently_… More models give you more _agreement_, faster. They do not necessarily give you more _redundancy_."（Brown PLT, A9） | **真对撞**。Kleppmann 让同一个 AI 既写代码又出证明；Brown PLT 证明这使验证失效（共享误解）。Brown PLT 在逻辑上赢——Kleppmann 文中未回应。这是全档案最重要的一组。 |
| 3 | "Automated tests are no longer optional… vital for ensuring AI-generated code does what it claims to do."（Willison, A4） | "for any fixed testing strategy, a sufficiently adversarial system can overfit to it"（de Moura 引 Claude C Compiler 骗测试，A2）+ Huntley 的 placeholder 斗争（A6） | **正方内部已经承认下界**：测试级验证挡不住对抗性模型。收敛结论：测试是必要非充分层，de Moura 用它论证要上证明，Huntley 用 prompt 堵——三人对同一失效面给出三种代价梯度的补丁。 |
| 4 | "LLMs have mostly removed the first barrier to entry of TLA+"（Davis, A7） | "If you need to know formal methods to get the LLM to do formal methods, is that really helping? What if it only lowers it from 80 to 75?"（Wayne, A3）；Prakhar Goel："reviewing software is harder than writing software"（A3 评论区） | **未决**。双方都给了可证伪的量化命题（门槛降幅、审查成本），2026-09 尚无测量。01 主篇适用边界判断应显式标注"未决"。 |
| 5 | "Specification becomes the core engineering discipline. Implementation just used to be louder."（de Moura, A2） | "They avoid strong invariants. They add fallbacks instead of making bad states impossible… that type of code does not come out of LLMs naturally."（Ronacher, A5） | **部分对撞**。Ronacher 同意不变量是核心（"make the malformed case unrepresentable"），但断言 LLM 产不出不变量——这实际支持"spec 必须由人/AI 以 spec-first 方式显式写"，反而强化 de Moura 的结论而削弱"loop 自动收敛到好不变量"的可能。 |
| 6 | "Anything can be wired in as back pressure to reject invalid code generation."（Huntley, A6） | "the benefit of TLA+ is the act of modeling your system painstakingly… skipping the modeling and outsourcing it is not ideal."（leoqa, A8） | **谱系之争而非对撞**：backpressure 派要的是"轮子转得快的任何验证器"，建模派说价值在建模行为本身。对应 01 主篇"验证器消费"vs"spec 是设计工具"（tikhonj）两支——2026 年两支都活得很好，且互不攻击。 |

---

## 15. 状态总表

| 集群 | 主体 | 日期 | 回源 | 立场 | 独立性判定 |
|---|---|---|---|---|---|
| A1 | Martin Kleppmann | 2025-12-08 | 一手 | 正方（证明路线） | 与 A2/A3 有引用关系；对工程派/SDD 独立 |
| A2 | Leonardo de Moura（Lean FRO/AWS） | 2026-02-28 | 一手 | 正方（最强） | 无外部正方引用；**有平台利益声明** |
| A3 | Hillel Wayne | 2026-03-10 | 一手 | **反方一号** | 独立反方（引 A1/A2 为靶） |
| A4 | Simon Willison | 2026-01-10/02-24 | 一手 | 正方（测试/一致性套件） | **完全独立**（只引 dbreunig/chenglou） |
| A5 | Armin Ronacher | 2026-06-23 | 一手 | 正方中的收缩派 | 对形式化派/SDD **独立**；单向引 A6 |
| A6 | Geoffrey Huntley | 2025-07-14（2026-03 续） | 一手 | 正方（backpressure） | 独立命源；被 A5 引 |
| A7 | A. Jesse Jiryu Davis | 2026-05-13 | 一手 | 温和正方 | 与 A3 同簇 |
| A8 | HN 147 分串 + SIGOPS 论文 | 2026-05 | 一手/半回源 | 群体裁决+不可判定反方 | 社区层独立 |
| A9 | Brown PLT（PICK） | 2026-06-09 | 一手 | **反方二号/精化派** | **独立性最强集群** |
| A10 | Cheng Huang（MS）× DeepSeek 3FS | 2025-05 / 2026-03 | 半回源 | 正方（P/TLA+ 路线） | 与 Lean 路线互不引用 |
| A11 | AWS Bedrock Automated Reasoning | 2026-08-04 | 半回源 | 正方（产品化） | 与 A9 **无引用同构**（TRANSLATION_AMBIGUOUS ≈ spec elucidation） |
| A12 | Google CEL 形式验证框架 | 2026-08 | 半回源 | 正方（信号） | 独立；待回源 |
| A13 | Ron Minsky（Jane Street） | 访谈（Brown 文 2026-06 引） | 转述 | 怀疑论 | 独立源，经 A9 转引 |

**独立收敛计数（扣除引用关系后）**：正方独立收敛成立的最小集合 = **A4（工程 KOL）× A2（形式化权威）× A1（学术跨界）× A11/A12（公司产品）**——四组独立来源（按有向簇计数：Willison 与 Kleppmann→de Moura 链之间无引用，但 Kleppmann 单向引用 de Moura，不构成四组两两互不引用——依据 [01a §4/A2 引用链]）、术语不同（conformance suites / mathematical friction / vericoding / automated reasoning）、时间在 2025-12 至 2026-08 内先后独立发声。反方独立收敛 = **A3（弱性质）× A9（冗余独立性）× A8（不可判定性）× A13（信任成本）**——同样互不引用、攻击点各异但都指向"验证物的可信供给"。

---

## 16. 对 01 主篇的修订建议

> 注：A4 集群内 Willison 各文完整 URL 与日期已补；其余"待回源"标注处一律不得被下游当作一手证据引用。

1. **§2 开头"学术锚"段重写**：加入 Kleppmann（vericoding）与 de Moura（zlib 定理、Veil）两条 2026 一手锚，把"形式化属性（仅限纯函数核心）"升格为"形式化阵营已自我宣告为该形态的终局载体，且拿出了 zlib 级生产案例"。
2. **§4.5 与 §4.2 合并精确化**：按对撞 #1/#2 的结论改述——"验证器不可作弊"与"验证内容不可被掏空"是两个独立失效面；后者有 Wayne（弱性质）与 Brown PLT（冗余独立性）两个一手形式化权威背书，比 VSDD 串里的 Sarcasmotron 自认重得多。
3. **§1.3 支持论点 2（virgilp"spec 是唯一可完全掌控的产物"）补独立同构**：de Moura "specification becomes the core engineering discipline" 是其 KOL 级独立复述，可作收敛证据。
4. **§5 团队落地建议的"起步三步"前插一步 0**：先跑 A4 的"First run the tests"四词 prompt（零成本），其有效性已被 Willison 指南化为默认纪律；并补 A6 的"capture the why of tests"细节（测试 docstring 写明存在理由），这是多轮 agent 场景下防止验证物漂移的最廉价手段。
5. **新增适用边界声明**：门槛降幅（Wayne 的 80→75 之问）与审查成本回归（Prakhar Goel）在 2026-09 均为未决问题，主篇不应给出确定性判断。
6. **勘误一处**：01 主篇 §2 称 Sadogursky "intent integrity chain" 常被引为实践方法论——本轮未再发现 2026 年新引用，建议权重维持"仅二手转引"不变。

---

## 17. 一段话回填

2026 年的独立收敛比 01 主篇成稿时更宽也更两极：正方从"测试即 spec"（Willison 的 conformance suites、"tests are no longer optional"）沿着"验证变便宜 + 生成物需要验证"（Kleppmann）一路推进到"证明即 spec、spec 是新核心工程纪律"（de Moura），AWS/Microsoft/Google 各自把这条路线产品化（Cedar、SymCrypt、Bedrock Automated Reasoning、CEL）——四个互不引用的人群在十个月内先后独立发声，收敛成立。但反方同样从形式化阵营内部独立长出：Wayne 用真实项目证明 LLM 写的验证物多数是同义反复、Brown PLT 用 P ⊧ ɸ 的独立性判据证明"AI 双侧生成使验证失效"、HN 群体重申不可判定性与建模价值、Minsky 讽刺"看起来对"的仪式——他们攻击的都不是"spec 该验证"，而是"验证物的可信供给不能同样外包给 LLM"。01 主篇的"被验证器消费"判据因此需要拆成两半：**谁消费（不可作弊的机制）× 谁供给验证内容（不可与被验者共享误解）**——这半句是本档案对主篇最核心的修订输入。
