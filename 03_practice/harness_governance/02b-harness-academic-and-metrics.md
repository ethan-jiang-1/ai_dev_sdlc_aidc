# 深挖四-B：学术收敛三群逐篇核验 + harness 度量缺口实证

> **元数据**
> - 观测日期：2026-09-20
> - 上游：`02-harness-governance.md` §7.7（三群学术收敛的初记）与 §7.13-3（Böckeler/Ronacher 两个度量开放问题）。本文为逐篇展开，**不重复** §7 已收的 practitioner 各条
> - 证据分级：**一手** = arXiv HTML 全文 / abs 页 / GitHub README 直接回源（本文 A 部分三篇全部一手回源；B 部分工具两件一手回源）；**半手** = 经摘要页核验但全文未读；**二手/线索** = 仅搜索结果标题级，未回源（逐条标注）
> - 检索记录：4 轮 web 检索（三篇论文定位 / harness 度量 + instruction file coverage / NLAH 代码释放 + 团队理解度量 / 补漏），详见 §B.5（⚠ 审计注：轮一/轮四检索式未逐字留痕，"零命中"断言按"未完整可复现"对待，引用时需带此限定）

---

## A. 学术收敛深挖：2026 年三群互不引用的 harness 治理工作

### A.1 Stanford-led：Meta-Harness（arXiv:2603.28052）

- **出处**：[arXiv:2603.28052](https://arxiv.org/abs/2603.28052)，cs.AI，2026-03-30 提交，HTML 全文一手回源。无会议信息（截至观测日为 preprint）。
- **作者与机构**：Yoonho Lee、Roshen Nair、Qizheng Zhang、Chelsea Finn（Stanford）；Kangwook Lee（**署名 KRAFTON**，非 §7.7 初记的"Stanford+MIT"纯学术组合）；Omar Khattab（MIT）。共 6 人。
- **harness 的操作定义**（论文 §3 原文）："the code that determines what information to store, retrieve, and present to the model"——**一个包裹 LLM 的有状态程序**，形式化为 `H* = argmax_H E[r(τ,x)]`，搜索空间是单文件 Python 程序（改 prompting/retrieval/memory/orchestration）。注意：他们治的是**单 agent 任务 harness**，不是 repo 级治理。
- **实验设置**：外循环是一个 coding-agent proposer（**Claude Code + Opus-4.6**，配一个最小 domain skill），通过文件系统读取全部历史候选的源码/分数/执行轨迹（每轮中位数读 82 个文件、引用 20+ 个前候选），典型一轮跑 ~60 个 harness / 20 次迭代。三个域：①在线文本分类（GPT-OSS-120B；LawBench 215 类 / Symptom2Disease 22 类 / USPTO-50k 180 类；40 个候选）；②检索增强数学（200 道 IMO 级题，5 个 held-out 模型）；③agentic coding（TerminalBench-2，Haiku 4.5）。对照：ACE、MCE、few-shot、Best-of-N（算力匹配对照）、OpenEvolve、TTT-Discover，统一 proposer 配置、search/test 隔离。
- **核心量化结果**：

| 域 | 对照 | Meta-Harness | 关键数字 |
|---|---|---|---|
| 文本分类（3 数据集均值） | ACE 40.9 / MCE 40.0 / 最强 few-shot 40.8 | **48.6** | +7.7 pts，且上下文 token 少 4×（11.4k vs 50.8k）；达到次优方法终值只需 4 次评估（对方 60 次） |
| 数学检索 | — | — | 单个发现的 harness 在 5 个 held-out 模型上平均 +4.7 pts |
| TerminalBench-2 | 超过 Terminus-KIRA | Haiku 4.5 agent 排名 **#1** | 即 §7.7 所记"harness 优化后的 Haiku 4.5 超过更大模型" |

- **harness 治理的具体操作**：治理 = **自动化搜索**。与 practitioner 的"棘轮"（人看到错误→加规则）不同，这篇把治理本身变成 meta-level 的机器：outer loop 无父选择规则、Pareto 前沿保留、proposer 全权诊断。对本文主题的直接贡献是给出"治理可以自动化到什么程度"的上界样本。
- **局限自述**：①成本——每 artifact 评估产生最多 **10M token** 诊断信息，是既有 text optimizer（0.002–0.026 MTok/iter）的**约三个数量级**（Table 1 自列）；②proposer 只见 search 集、结果依赖 search/test 划分；③§5 Discussion 全文未逐字核验（抓取截断），其额外自述局限未收录，引用时注明。
- **可复现性**：**部分开源**。项目页 [yoonholee.com/meta-harness](https://yoonholee.com/meta-harness/)（含交互 demo）；代码仅释出 TerminalBench-2 优化产物 [stanford-iris-lab/meta-harness-tbench2-artifact](https://github.com/stanford-iris-lab/meta-harness-tbench2-artifact)，**搜索循环本身与文本分类/数学域未见公开仓库**。

### A.2 清华 SIGS+哈工大（深圳）：Natural-Language Agent Harnesses / NLAH+IHR（arXiv:2603.25723）

- **出处**：[arXiv:2603.25723](https://arxiv.org/abs/2603.25723)，cs.CL，2026-03-26 提交，HTML 全文一手回源。preprint。
- **作者与机构**：Linyue Pan（通讯后列）、Shuo Guo、Jingchen Ni、Hai-Tao Zheng（通讯，清华深圳国际研究生院）；Lexiao Zou（哈工大深圳）。共 5 人。
- **harness 的操作定义**（⚠ NLAH 已于 2026-05-18 发 v2：后端与 RQ 结构已整套更换，本条及以下 NLAH 数字均基于 v1、待按 v2 复核；v1 §2.1 措辞）："the orchestration layer that governs multiple model or agent calls for a task family"，显式三分：**control**（怎么分解调度）/ **contracts**（产出什么、过什么门、何时停）/ **state**（什么跨步持久）。治理对象是其中可外置的 **design-pattern layer**——把它从 controller 代码里提出来，写成**可执行的自然语言工件（NLAH）**，由共享运行时 IHR（in-loop LLM + 工具后端 + runtime charter）解释执行。这是三篇中唯一把治理对象做成**可迁移、可比、可消融的工件**的——直接回应"harness 难以作为科学对象研究"。
- **实验设置**：后端 Codex CLI 0.114.0 + GPT-5.4（xhigh），Docker 沙箱（每任务 32 vCPU/84GiB 上限）。**自述因预算限制只跑基准子集**：SWE-bench Verified 125 样本、OSWorld 36 样本，单次固定种子采样（作者承诺后续换 GPT-5.4-mini 跑全量）。三个 RQ：行为效应（RQ1）、模块消融（RQ2）、代码→文本迁移保真（RQ3）。对照是同一 IHR 内的逐模块加减。
- **核心量化结果**：

| 实验 | 结果 |
|---|---|
| RQ1（TRAE harness on SWE Verified） | Full IHR 74.4 vs **去掉 runtime skill 反而 76.0**，且 token 减半（16.3M→11.1M）、runtime 减半——共享 charter 不是免费午餐 |
| RQ2 消融（SWE Verified / OSWorld，相对 Basic 75.2 / 41.7） | self-evolution **+4.8 / +2.7**（唯一一致正贡献）；file-backed state +1.6 / +5.5；**verifier −0.8 / −8.4**；multi-candidate −2.4 / −5.6 |
| RQ1 过程指标 | Full IHR 约 90% 的 token/工具/LLM 调用发生在被委派的子 agent 中——行为学证据表明它不是 prompt wrapper |
| RQ3（§7.7 初记的 30.4%→47.2%、LLM 调用 1200→34） | 属 RQ3 代码→文本迁移部分；本次抓取截断未逐字复核，沿用初记数字并标注**半手** |

- **harness 治理的具体操作**：治理 = **表示层工程**——把 harness 写成带 contracts/roles/stage/adapters/state semantics/failure taxonomy 六组件的可编辑文本，使"改 harness"变成 diff 一个工件而非改代码。对本文主题：这是治理**可审计化**的学术版。
- **局限自述**：①样本子集+单种子（明说）；②harness/runtime 边界是分析性的、非绝对；③RQ1 结论本身是"行为改变"而非单调增益——作者明确警告不要把它读成增益故事。
- **可复现性**：**未找到代码仓库**。全文（含参考文献段）未见 GitHub 链接；专门的代码释放检索也未命中（检索记录见 §B.5）。当前**不可独立复现**，引用其消融数字时强度降一级。

### A.3 SWE-Bench Mobile（arXiv:2602.09540，KDD '26）

- **出处**：[arXiv:2602.09540](https://arxiv.org/abs/2602.09540)，cs.SE，2026-02-10 提交；正式发表 **KDD '26**（Proc. 32nd ACM SIGKDD, Vol. 2, pp. 8077–8087，DOI 10.1145/3770855.3818488）。**三篇中唯一有同行评审背书的**。abs 页一手回源（全文 HTML 未逐字读，标注半手）。
- **作者与机构**：Muxin Tian、Zhe Wang、Blair Yang、Zhenwei Tang、Kunlun Zhu、Honghua Dong、Hanchen Li、Xinni Xie、Guangjing Wang、Jiaxuan You，共 10 人。**abs 页未列机构**（通讯 You 通常署 UIUC，但本文不收录未回源的机构指认）。
- **harness 的操作定义**：这里治理对象叫 **agent/scaffold**——商用产品级 scaffold（Cursor、Codex、Claude Code）与开源（OpenCode），即"harness"被操作化为**用户实际能选的整条执行链路**，不是论文自建的组件。
- **实验设置**：benchmark 来自**生产级 iOS 代码库**（Swift/Objective-C 混合、大规模），任务带多模态输入（PRD + Figma 设计）与完整测试套件；评测 **22 个 agent×model 配置**、4 个 agent。防污染设计：**hosted benchmark challenge**（数据不落地本地，公共 leaderboard 在 [swebenchmobile.com](https://swebenchmobile.com)）。
- **核心量化结果**（abs 页）：最好配置仅 **12%** 成功率；**同一模型跨 agent 最高 6× 差距**（§7.7 初记：Opus 4.5 在 Cursor 12% vs OpenCode 2%）；商用 agent 一致优于开源；"Defensive Programming"式简单 prompt 比复杂 prompt 高 **7.4%**。
- **harness 治理的具体操作**：它本身不治理，而是提供**治理必要性的受控测量**：在工业级任务上把"scaffold 差异"从"模型差异"里分离出来，且 6× 这个数字被 Meta-Harness 开篇第一句引用为动机（Meta-Harness 的 6× 引文指向的正是这条线）。
- **局限自述**（abs 页可见范围）：单平台（iOS）、12% 绝对水位说明任务对当前 agent 过难、hosted 形态限制第三方本地复跑。其余局限在全文中，未逐字核验。
- **可复现性**：**部分开放**——leaderboard + 开发工具包公开；但为防污染，任务数据采用 hosted 形态，**独立方无法在本地完整复现评测**。这是 benchmark 设计上的合理取舍，但意味着复现依赖主办方基础设施。

### A.4 三群定义一致吗？收敛是"同词不同义"还是真收敛？

**判定：真收敛，但口径分三层，且需排除一个真正的同词不同义干扰项。**

1. **操作定义不重合但同族**。Meta-Harness 的 harness = 单任务包裹程序（store/retrieve/present）；NLAH 的 harness = 任务族的编排层（control/contracts/state）；SWE-Bench Mobile 的 harness = 产品级 scaffold 整体。三者粒度从"单文件 Python"到"商用产品"差两个数量级，**不可直接互比数字**（Meta-Harness 的 6× 与 SWE-Bench Mobile 的 6× 是不同测量面上的巧合相等）。
2. **但核心命题逐字同构**：三群都在"**固定模型、只变外部执行链路**"的受控设计下测得数倍级差距——这是同一因果主张的三次独立证实，且方法上互为补充（自动化搜索 / 表示层消融 / 产品级横断面）。互不引用方面：NLAH 引的是 practitioner 文献（OpenAI/LangChain/Anthropic）而非另两篇；SWE-Bench Mobile（2 月最早）不引用后两者；Meta-Harness 引 SWE-Bench Mobile 一线的 6× 作动机——即收敛是"独立得出 + 局部事后引用"，不是同一文本扩散。
3. **真正的"同词不同义"在别处**：检索中撞见的 [Coverage-Guided Multi-Agent Harness Generation for Java Library Fuzzing](https://arxiv-org.规范链接 arxiv.org/abs/2603.08616（原 ezproxy 链接）) 一类工作里的 "harness" 指**模糊测试桩代码**——与 agent harness 完全无关。这说明 2026 年文献里 "harness" 一词确已歧义化，引用本节三篇时必须带限定语，但**不妨碍三群内部是真收敛**。

---

## B. 度量缺口深挖：Böckeler 之问与 Ronacher 之塔在 2026-09-20 的答案状态

回顾两问（`02-harness-governance.md` §7.3/§7.8/§7.13-3）：①**Böckeler 之问**——"如果传感器从不触发，是高质量还是检测不足？我们需要类似代码覆盖率之于测试那样的方法来评估 harness 覆盖率和质量"；②**Ronacher 之塔**——团队对代码库的共享理解在无声腐烂，"没有任何 harness 指标会报告这一点"。

### B.1 找到的：harness 度量的**局部**回应确实在 2026H2 出现了

1. **[damson/agent-config-harness](https://github.com/damson/agent-config-harness)**（GitHub，MIT，一手回源 README，eval 样例日期 2026-08-29）——"instruction file test coverage" 线索的**成活实例**。把 CLAUDE.md/AGENTS.md/.cursorrules 当代码治理：LLM rubric 按 clarity/conciseness/completeness/consistency/actionability 五维各 1–5 分（满分 25、给字母等级与逐条 findings）；`bats` 结构测试管 rubric 看不见的不变量（skill frontmatter、必需章节、symlink 不许变回实体文件）；分数按 domain 留**趋势**（区分真改进与"感觉良好的重写"）；以 GitHub Action 形态做 CI 门（`fail-below: C`）。作者自己标注的边界很诚实：LLM 评分 ±1–2 抖动、可被"写给评分器的文本"操纵、只能抓漂移与潦草、抓不了恶意——**门应作 advisory**。
2. **[Zandereins/schliff](https://github.com/Zandereins/schliff)**——独立同向工具：AI 指令文件的**确定性** 8 维质量评分（含 security 维与 anti-gaming 检测，零依赖）。仅标题/README 级核验（线索级），与上一条互不引用，说明"给指令文件打分"已至少两源独立出现。
3. **[arXiv:2604.07236](https://arxiv.org/abs/2604.07236)**（Jung & Son，v4 2026-04-28，abs 一手）——**最接近 Böckeler 之问的学术回应**："harness 的各层到底贡献多少"可以被外部化度量：把规划 harness 拆成信念跟踪/声明式规划/符号反思/LLM 修订门四层，54 局博弈、预注册 heavy-lifting 定义（对主指标的最大正边际），结果：声明式规划 +24.1pp 且零 LLM 调用，LLM 修订门只在 4.3% 回合激活。贡献自述为**方法论的**：harness 分层可测后，LLM 的角色可量化为残差。局限同样明显：单一玩具域（Collaborative Battleship），离 repo 级 harness 的覆盖率度量还差整个抽象层。
4. **[Uncovering AGENTS.md（SCAM 2026）](https://azaidman.github.io/publications/ardicSCAM2026.pdf)**（Ardic & Zaidman 等）——同行评审的实证研究，测的是 OSS 项目给 coding agent 的 testing guidance 的**普及度与内容**，不是质量/覆盖率——即学界已开始把指令文件当研究对象，但"度量其质量"这一步尚未进入。
5. **旁证**：[SIGIL: Compiling Agent Skills into Typed Harnesses](https://arxiv.org/html/2607.27309v1)（类型化 harness，结构约束作为质量的替代物，线索级）；InfoQ 文章 [Comprehension as an Architectural Characteristic](https://www.infoq.com/articles/system-comprehension-evolutionary-architecture/)（把"可理解性"提为架构特性——方向触及理解层，本次抓取只回源到页面骨架，**内容未核验**，列为半手）。

### B.2 没找到的：缺口中仍未闭合的两半

- **Böckeler 之问的后半段无答案**：上面所有工作度量的是**指令文件文本质量**或**单层 harness 的边际贡献**；"**传感器元覆盖率**"——枚举失效模式空间、标注哪些模式没有任何 sensor 在看（"if sensors never fire"的反事实检测）——在 4 轮检索中**零命中**。agent-config-harness 的 rubric 是对"写了什么"评分，不回答"该有而没有的传感器有哪些"。
- **Ronacher 之塔完全无量化**：未找到任何论文/工具/博客给出"团队共享理解腐烂"的可操作指标。唯一疑似命中的 [Level Up (Medium) 文章 "We Can Measure How Fast We Ship. Can We Measure How Well We Understand What We Built?"](https://levelup.gitconnected.com/we-can-measure-how-fast-we-ship-can-we-measure-how-well-we-understand-what-we-built-a5ad2749c8fa) 被 403 拦截（Cloudflare），**仅标题级线索，未核验**——且即便是它，也大概率是思辨文而非指标方案。这条线索留给下一轮（换镜像/搜索引擎缓存）回源。

### B.3 结论：缺口被收窄，但"全行业开放问题"的判断成立

1. **Böckeler 之问**：2026H2 出现了工具级局部回应（instruction-file 评分/回归/CI 门，两源独立 + 一个学术方法论原型），但它度量的是 harness 的**声明层**（文件文本）与**单层贡献**，不是 harness 作为**失效模式覆盖网**的覆盖率。原问题的严格形式仍无方案。
2. **Ronacher 之塔**：观测日止**无任何量化指标**，只有思辨性文章和标题级线索。这是两个缺口中更真空的一侧——与 §7.13-1"连指标都没有"的判断一致，且本轮深挖后**更强**：不是"没找到好的"，是"没有找到任何"。
3. 因此本文对 03 号文档 §7.13-3 的修正案：把"harness 自身的覆盖率/质量如何度量——观测日无任何一方给出可操作答案"改为**分层表述**——"指令文件文本质量度量已有工具级雏形（agent-config-harness/schliff，2026H2）；传感器元覆盖与团队理解层腐烂度量在 2026-09-20 观测日仍为零方案"。后者才是真正无主的开放问题。

### B.4 检索记录（供防重复）

1. 轮一（论文定位）：三篇 arXiv 号 + 作者/机构关键词 → 三篇全部命中并回源。
2. 轮二（度量方案）：`harness coverage metric` / `instruction file test coverage CLAUDE.md AGENTS.md` / `Böckeler harness coverage sensor quality` → 命中 agent-config-harness、schliff、2604.07236、SCAM 2026、SIGIL、InfoQ comprehension 文。
3. 轮三（负结果确认）：`NLAH IHR code github release`（→ 无代码释放证据）；`shared understanding mental model decay metric 2026`（→ 仅思辨文与被 403 的 Medium 线索）。
4. 轮四：InfoQ 文全文抓取（仅得页面骨架，内容未核验）；Medium 全文抓取（403，放弃）。

### B.5 对上游的两个小勘误

1. §7.7 称 Meta-Harness 为"Stanford+MIT"：署名实际为 Stanford×4 + MIT×1 + **KRAFTON**×1（Kangwook Lee），建议改"Stanford/MIT/KRAFTON"。
2. §7.7 三群"互不引用"需加限定：Meta-Harness 开篇引用了 SWE-Bench Mobile 一线的 6× 数字作动机；严格说法是"三群**独立得出**同一命题，观测日可见的引用仅 Meta-Harness→SWE-Bench Mobile 单向、且晚于其自身实验设计"。
