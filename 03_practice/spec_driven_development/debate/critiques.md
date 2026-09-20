# SDD（Spec-Driven Development）批判与失败经验汇编

```yaml
topic: Spec-Driven Development — critiques, doubts, failure reports
accessed_at: 2026-09-20
collector: delegated research agent
scope: 泛 SDD 方法论 + 工具（GitHub spec-kit / AWS Kiro / Tessl / OpenSpec 等）
sort: 时间倒序
weights: 高=知名 KOL/大社区/高热帖；中=有实证的个人博客/团队案例；低=无跟评的个人吐槽
note: 按补正指令，2026 年（尤其 2026Q2–Q3）逐条展开（论点+关键句+论据链+证据强度）；2025Q4 起为背景段压缩；2025 年中以前舍弃。
limitations:
  - reddit.com 直接抓取被 403 拒绝，r/ExperiencedDevs、r/programming 的内容未能回源验证，仅能通过 HN/博客间接覆盖；后续可由有浏览能力的 agent 补齐。
  - web_search 端点在本会话不可用，2026 年材料靠 hn.algolia.com API + 直接抓取原文获得。
```

---

## 一、2026 年批判材料（重点展开，时间倒序）

### 1. Ask HN: What are your thoughts on spec-driven development?
- **日期**：2026-07-24
- **来源**：https://news.ycombinator.com/item?id=49041530
- **核心论点**：持续出现的 Ask HN 表明到 2026Q3 社区仍在质疑 SDD 是否值得用；此类帖子的存在本身就是"热度退潮、怀疑常态化"的信号。
- **针对对象**：泛 SDD
- **传播热度**：4 分 / 2 评（低）
- **影响力权重**：低（合并带过：2026Q2–Q3 还有多条同类 Ask HN，如 "Ask HN: Are you using Spec Driven Development?" 2026-06-12，https://news.ycombinator.com/item?id=48510002，7 分/6 评——楼主自述用了 SpecKit/GSD/OpenSpec 数月后，发现即使有 AGENTS.md 和 Skills，产出代码"coding style and good code hygiene is often lacking"，开始怀疑是否该 abandon SDD；以及 2026-06-12 的提问者困境：spec 越拆越小也没解决"读不懂生成代码"的问题）
- **论据链**：个人实测数月（SpecKit→GSD→OpenSpec 迁移）+ 未解决的可维护性观察。证据强度：一手体验、单案例。

### 2. Show HN: Replacing spec-driven development with just facts（spec 债 / 一致性税）
- **日期**：2026-05-04
- **来源**：https://github.com/av/facts （HN: https://news.ycombinator.com/item?id=48008906）
- **核心论点**：作者直接弃用 SDD 另起炉灶。关键句（原文）："agents are too readily producing fluff, large projects have so many specs agents start making mistakes maintaining them. There's a constant **consistency tax**."——spec 本身成了需要被维护、且会被 agent 维护出错的资产；他把 spec 降级为"一堆 facts"，只保留事实、丢掉流程。
- **针对对象**：泛 SDD（spec 作为长期资产的做法）
- **传播热度**：7 分 / 4 评（低）
- **影响力权重**：低–中（无跟评讨论，但"spec 债/一致性税"是 2026 年新出现的独立批判切面，且作者用行动（另写工具替代）背书）
- **论据链**：自述在大项目中 spec 数量膨胀导致 agent 维护 spec 时出错的一手经验；非量化数据。证据强度：一手体验、单案例、无可验证数据。

### 3. dbreunig《Keep the Spec Driven Development Triangle in Sync》（spec 漂移维护留白 / 团队规模化）— 本批最重要的 2026 年复盘
- **日期**：2026-03-04（MLOps Community "Coding Agents" 大会 talk，2026-03-03 演讲）
- **来源**：https://www.dbreunig.com/2026/03/04/the-spec-driven-development-triangle.html （视频 https://www.youtube.com/watch?v=8TXAlOFkmk0）
- **核心论点**：作者曾靠"无代码库 whenwords"（纯 spec + 750 个 YAML 一致性测试，Karpathy 点赞、1000+ star）成为 SDD 旗手，但随后**自我推翻**："I got this wrong. This is the wrong way to think about it."——SDD 不是"spec+tests+agent→代码"的单向等式，而是 spec/tests/code 三角持续同步的反馈环；"a spec doesn't really work until it's implemented"。批判要点：① **spec 漂移维护留白**："The spec gets written, it gets implemented, it gets released. Is the spec updated? No."——spec 与代码节奏、媒介都不同，更新被当作 overhead；② **复杂度天花板**："As complexity grows, structural choices become more important… every time they fixed a new bug, it broke something else."；③ **流程复杂化只是搬运问题**：引 Steve Yegge 承认 Gas Town "look a lot like Kubernetes mated with Temporal… ugly baby"——"If the process is complex, we're just moving the problem"；④ **团队/开源规模化**：即使 spec 很好，仍出现 20 条评论的长线程争论"什么才是对的实现"，因为 "no spec is perfect"。
- **针对对象**：泛 SDD + spec-as-source 极端形态（whenwords、Anthropic C compiler、Vercel just-bash、Pydantic Monty）
- **传播热度**：HN 4 分/3 评，但大会 talk + Karpathy 关联传播，业界阅读面广
- **影响力权重**：**高**（知名技术博主、大会 talk、有真实项目与同行评审案例；且作者是 SDD 同情者转批判，说服力强）
- **论据链**：**多个公开团队案例实证**——Anthropic 16 个 Claude + $20,000 建 Rust C 编译器"didn't really work"（修一个 bug 破坏另一个，卡在 1% 失败测试）；Pydantic Monty 缺 JSON 标准库；just-bash 未完工；自己 whenwords 的 issue/PR 实录。还引用"AI Coding Boosts Output But Overwhelms Human Reviews"头条佐证评审过载。证据强度：**一手项目 + 多个可回溯的公开团队案例 + 大会报告**。属"有实证的个人博客"上限，接近高权重。

### 4. "Spec driven development doesn't work if you're too confused to write the spec"
- **日期**：2026-02-10
- **来源**：https://publish.obsidian.md/deontologician/Posts/Spec-driven+development+doesn%27t+work+if+you%27re+too+confused+to+write+the+spec （HN: https://news.ycombinator.com/item?id=46955747）
- **核心论点**：从标题即可见其命题：SDD 把"先写清 spec"设为前提，但现实中最大的一类失败恰是**你还糊涂、写不出 spec**——需求不清的问题恰恰需要靠迭代写代码来弄明白，SDD 在这个最需要帮助的场景失效。（Obsidian Publish 页面正文未渲染成功，正文未能回源；此条命题以 HN 标题与转述为准。）
- **针对对象**：泛 SDD（前置假设批判）
- **传播热度**：32 分 / 7 评（低–中）
- **影响力权重**：低
- **论据链**：观点文，未见实证数据。证据强度：低（个人观点）。

### 5. Verified Spec-Driven Development (VSDD) 大讨论（反方背景：SDD 需要"验证层"才可信）
- **日期**：2026-02-28
- **来源**：https://gist.github.com/dollspace-gay/d8d3bc3ecf4188df049d7a4726bb2a00 （HN: https://news.ycombinator.com/item?id=47197595）
- **核心论点**：这篇 211 分高热帖本身是"VSDD"提案而非批判文，但其 118 条评论构成 2026 年对"裸 SDD"的最大规模集体批判场：共识性批判是**自然语言 spec 无法自我验证**，没有可执行验证层的 spec 只是"看似严谨的散文"；discussion 中大量观点指向"markdown spec 是弱合约，必须编译成测试/形式化约束才可信"。
- **针对对象**：泛 SDD（未经验证的自然语言 spec）
- **传播热度**：**211 分 / 118 评（本汇编热度最高的帖子之一）**
- **影响力权重**：**高**（大社区高热帖）
- **论据链**：提案 + 大规模社区辩论；无统一实证。证据强度：中（群体观点收敛，但非实测）。

### 6. Ask HN: Are you still using spec driven development?（SDD 退潮 + spec 漂移警告）
- **日期**：2026-02-03
- **来源**：https://news.ycombinator.com/item?id=46864948
- **核心论点**：楼主提问的直接动因是观察到 **spec-kit "no commits for over a month"**、且未接入 GitHub 新的 agents 集成——官方工具自身的维护停滞成为 SDD 退潮的证据。高评回帖（waldopat）给出团队/个人通用警告："**I'd add caution about drift. The more documentation you shove into the context, the worse things can get. You can also create a beautiful and perfect functional spec that becomes a swiss cheese of gaps when you create your technical implementation plan.**"——文档越堆越多反而恶化 agent 表现；完美的功能 spec 到实现规划阶段可以千疮百孔。
- **针对对象**：泛 SDD + spec-kit
- **传播热度**：6 分 / 7 评（低）
- **影响力权重**：低–中（帖子冷，但"官方仓库停更"这一事实性观察被多个渠道复述，是 2026 年 SDD 退潮叙事的锚点之一）
- **论据链**：可验证的仓库提交记录（spec-kit 停更）+ 个人 brownfield 经验。证据强度：中（事实锚点 + 一手体验）。

### 7. spec-kit #1401：Context tax——SDD 工具自身的成本经济学（2025-12-29 开、2026 全年持续活跃）
- **日期**：2025-12-29（open 至今，2026-08 仍在更新，按其影响期计入 2026）
- **来源**：https://github.com/github/spec-kit/issues/1401
- **核心论点**：spec-kit 的 slash 命令**每个会话固定吃掉约 18.6k tokens** 的上下文（逐命令给出实测 token 数：checklist 4.2k、specify 3.1k、implement 3.1k……），且无论当次是否使用 SDD 都要支付。对 Cursor 默认 20k 上下文约占 **93%**、Copilot 标准 64k 约 29%、Claude Code 200k 约 9.3%。"Context window space is a finite and valuable resource."——SDD 把最稀缺的资源（上下文）系统性挪用给了流程文本。
- **针对对象**：GitHub spec-kit
- **传播热度**：15 reactions、6 comments
- **影响力权重**：中（GitHub 官方仓库、量化数据、长期 open）
- **论据链**：**实测数据**（/context 输出的逐命令 token 表 + 多平台上下文占用比例表）。证据强度：**高（可复现量化实测）**。这是"成本经济学"切面最硬的一条。

---

## 二、2025Q4 背景（压缩带过，为 2026 批判提供源头）

- **2025-11-15 / marmelab 文 HN 讨论（225 分 / 191 评）**：https://news.ycombinator.com/item?id=45935763 。2026 年批判的主要弹药库在此成形：constantcrying（ waterfall 老兵）："SDD is exactly waterfall… the spec locks you in… changes to your spec require half the requirements to subtly change… now your code and spec only superficially look like one another"（**spec 与代码名义同步、实质漂移**）；unreliable-compiler 论（"it introduces an unreliable compiler"）；反方亦有（"SDD 是解锁 >100k 行大代码库的关键"）。
- **2025-11-12 / marmelab《Spec-Driven Development: The Waterfall Strikes Back》**（François Zaninotto，https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html ，权重高）：核心论点——SDD 复辟 heavy documentation before coding：Context Blindness、Markdown Madness（"spending 80% of your time reading instead of thinking"）、Double Code Review、**False Sense of Security**（agent 把"verify implementation"标记为 done 却没写一个测试）、Diminishing Returns（"For large existing codebases, SDD is mostly unusable"）；并断言 SDD 暗含"how do we remove developers from software development"的错误命题。论据链：两个一手实测（spec-kit 给小功能生成 8 文件 1300 行文本；Kiro 在 Atomic CRM 上生成三件套）。
- **2025-11-15 / spec-kit #1191（115 👍，团队向最重磅）**：https://github.com/github/spec-kit/issues/1191 ——多人协作/迭代场景下 spec 无法方便地更新、精化、保持同步：`/speckit.specify` 只为全新特性设计，每次生成新分支+新工件；社区求 `/speckit.update`、tinySpec 等轻量流。关联 #620（"How to keep specs consistent and up-to-date"）、#1130（/implement 之后怎么改 spec）、#442（/implement 之后调试修复无工作流，bug 揭示的 spec 缺口无处回写）。**这是"spec 资产化失败 / spec 债"与团队维护权责留白的官方 issue 级证据。**
- **2025-10-30 / spec-kit #1092《High Level Design Concerns》**：https://github.com/github/spec-kit/issues/1092 ——spec↔bug 归因困境（"is the issue in the specifications or in the implementation?"）、as-specified vs as-implemented gap 需要 KPI、**成本质疑**（"the $ cost of time writing/rewriting specs is costing me more than the $ cost of writing code… If I can get a better implementation without spec-kit at lower $ cost, then Houston has a problem"）、"great specs – no MVP" 警告。
- **2025-10-15 / Birgitta Böckeler（Thoughtworks Distinguished Engineer）on martinfowler.com《Understanding Spec-Driven-Development: Kiro, Spec-Kit, and Tessl》**（https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html ，HN 128 分/32 评，权重高；注：作者为 **Birgitta** Böckeler，非 Jan）：区分 spec-first / spec-anchored / spec-as-source 三级并指出**所有工具对 spec 的长期维护策略含糊其辞**；实测小 bug 被 Kiro 膨胀成 4 个 user story + 16 条验收标准（"sledgehammer to crack a nut"）；spec-kit 大量 markdown "very verbose and tedious to review… I'd rather review code"；**虚假控制感**（agent 忽略 research 笔记、把已有类重新生成一遍造成重复，"I frequently saw the agent ultimately not follow all the instructions"）；MDD 历史类比："spec-as-source might end up with the downsides of both MDD and LLMs: Inflexibility and non-determinism"；结语："Verschlimmbesserung"（越改越坏）。
- **2025-09-08 / spec-kit #75《SpecKit creates the illusion of work, generating a bunch of text》**：https://github.com/github/spec-kit/issues/75 （24 reactions，已锁）——"illusion of work"论：文件无视项目结构、生成数百无意义测试、overengineering；结论"SDD 只适合原型，增量开发不适用"。

---

## 三、批判观点聚类（按影响力权重排序）

1. **【高】waterfall 复辟论 / 虚假控制感**（代表：marmelab 2025-11-12 + 其 HN 225/191 讨论；Böckeler 2025-10-15）：SDD 换皮 waterfall，制造"流程在控制 AI"的错觉，而 agent 实际经常无视 spec（假 done、重复造已有类）。这是声量最大、KOL 背书最强的聚类。
2. **【高】spec 漂移与维护留白 / spec 债（团队向，补正指令重点）**（代表：dbreunig 2026-03-04"Is the spec updated? No."；spec-kit #1191 + #620 + #1130 + #442 官方 issue 群；HN constantcrying"code and spec only superficially look like one another"；av/facts 的 consistency tax）：所有工具都为"新建 spec"优化，没有人为"spec 随迭代保持与代码/测试同步"负责——多人协作下 spec 谁维护、冲突怎么解、bug 揭示的 spec 缺口如何回写，全部留白；spec 从资产劣化为负债。**2026 年批判的重心已明显从"waterfall 复辟"迁移到这一条。**
3. **【高→中】复杂度天花板与规模失控**（代表：dbreunig 引 Anthropic $20k C 编译器停滞、Monty/just-bash 未完工；Gas Town 复杂度自认；marmelab"For large existing codebases, SDD is mostly unusable"）：小项目/greenfield 有效，brownfield 与大团队下流程本身失控，"复杂流程只是把问题搬走"。
4. **【中】成本经济学 / context tax / 评审过载**（代表：spec-kit #1401 的 18.6k token 实测表；spec-kit #1092 的 $ 成本质疑；marmelab Double Code Review；"AI Coding Boosts Output But Overwhelms Human Reviews"）：SDD 把 token、美元、评审时间三类成本系统性抬高，且这部分成本在收益前支付。证据强度最高（可复现实测）。
5. **【中→低】方法论前提批判与退潮观察**（合并带过：deontologician 2026-02-10"too confused to write the spec"；Ask HN 系列 2026-02~07 的"还在用吗/该怎么用"反复发问 + spec-kit 停更事实；VSDD 211/118 讨论中"裸 markdown spec 不可验证"共识）：SDD 预设你写得清 spec、且 spec 值得信任，两个前提在现实中常常同时不成立；社区热度 2026 年转向"验证层/事实层"替代方案（VSDD、facts、compilable specs）。

（未回源说明：Reddit 两子版内容因 403 未能收录；isoform.ai《The Limits of Spec-Driven Development》（2025-12-02，HN 5 分）正文抓取失败，仅存目录条目，未计入聚类。）
