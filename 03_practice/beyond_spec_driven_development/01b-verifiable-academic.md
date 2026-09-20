# spec 机器可验证方向的学术前沿（2025Q4–2026）——01-verifiable-specs.md 的学术侧深挖

```yaml
topic: SDD 替代形态之验证优先：学术前沿深挖（autoformalization / spec 可验证性基准 / 工业级 LLM×形式验证 / AI-for-Math 外溢 / 负面结果）
accessed_at: 2026-09-21
parent: ./01-verifiable-specs.md
scope: arXiv 2025Q4–2026 + ICML/ICLR/AAAI/OSDI/CAV/ICSOFT 2026；不重复 01 篇已述的社区/工具面，Verus-SpecGym(2605.26457) 与 Consort(2609.09671) 只做展开
sources: 一手回源 20+ 篇，全部经 arxiv.org/abs/<id> 或官方会议页确认（观测日 2026-09-21）；HTML 全文路径见各条目
weights:
  - 高（abs + 摘要全回源）：2605.26457, 2609.09671, 2606.16541（机构未取得）, 2512.10187, 2606.05792, 2603.19715, 2603.17150, 2607.13303, 2607.09900, 2510.11986, 2509.09810, 2511.12869, 2605.29955, 2601.07421, 2607.26306, 2608.21356, 2608.07614（机构未取得）, 2606.26300, 2605.26169, Coins(ICML 2026 页)
  - 中：Aria(ICLR 2026 proceedings 页)、PutnamBench(NeurIPS 2024 页)、两篇综述(2505.23486 / 2407.11214)
  - 低（存在性回源、细节未取）：seL4 LLM theorem proving 第二篇（Semantic Scholar 403/202）；Show Me The Money（CAV 2026，仅 Zenodo artifact）
limitations:
  - "局限自述"以论文摘要自陈为主，未逐条核对正文 limitations 章节；量化数字均为论文自述，未独立复跑。
  - 工业成本数字中，智能合约审计市价（$25k–100k）转引自 ESBMC 综述 PDF 内的二手行业价，属转引非实测。
  - 2605.26457 / 2609.09671 在 01 篇已出现，本篇仅深化不重复。
```

---

## 0. 定位

01 篇回答"社区在怎么用可验证 spec"；本篇回答"学术界把这条路线推到了哪、卡在哪"。核心发现一句话：**2025Q4–2026 学术界把战场从"代码对不对"整体移到了"spec 对不对"——spec autoformalization 成了独立可评测任务，四种忠实度评测方案同季出现；同时"证明经济学"被 LLM 改写（Lean 里买来基础主义证明已被实证），工业案例首次越过玩具域（MakerDAO 合约、RISC-V 流片、Lockheed Martin 部署）；但所有工作共同确认的边界是：意图没有 oracle，验证器永远是代理。**

---

## 1. Autoformalization 进展（NL → Lean/Dafny/TLA+）

### 1.1 miniF2F-Dafny（arXiv 2512.10187，2025-12 v1 / 2026-06 v3）

- **机构/作者**：Cambridge（Baksys、Holden）+ AWS（Zetzsche、Bouissou）。Preprint。
- **一手**：[abs](https://arxiv.org/abs/2512.10187)、[HTML](https://arxiv.org/html/2512.10187v3)。
- **设置**：miniF2F 第一次移植到 Dafny（auto-active 验证器）；8 个现成 LLM，pass@4 累计，对照空证明基线。
- **量化结果表**：

| 配置 | 结果 |
|---|---|
| Dafny 自动化、空证明 | 39–44%（同批题在 ITP 需大量人写引导） |
| 最佳模型 Claude Opus 4.6 | 62.7% pass@4（全 test 集） |
| 空证明基线 | 38.9%（差 23.8pp） |

- **意义**：证明"LLM 高层引导 + SMT 兜底"的分工模式可行——这是最接近工程形态的线，因为 Dafny 本就是软件验证语言。**开源**：[dafny-lang/miniF2F](https://github.com/dafny-lang/miniF2F)。

### 1.2 ConjectureBench（arXiv 2510.11986，2025-10，Edinburgh）

- **一手**：[abs](https://arxiv.org/abs/2510.11986)、[HTML](https://arxiv.org/html/2510.11986v1)。
- **设置**：指出现有评测把结论白送给模型；真实流程必须先自产猜想。GPT-4.1、DeepSeek-V3.1，Lean-FIRe 推理时方法。
- **量化**：自产猜想后 autoformalization 成绩**被大幅高估**（摘要原文 substantially overestimated）；Lean-FIRe 首次端到端 autoformalization：PutnamBench 上 GPT-4.1 解 **13 题**、DeepSeek-V3.1 **7 题**（绝对值个位到十位）。
- **局限自述**：猜想与形式化的正确耦合是开放问题。开源：部分（框架给出，无独立 repo 链接于 abs 页）。

### 1.3 TLA+ 首个系统评测（arXiv 2606.05792，ICSOFT 2026，Best Paper 候选）

- **机构**：Loyola Chicago 等（Bisharat、Thiruvathukal、Laufer、Abuhamad）。
- **一手**：[abs](https://arxiv.org/abs/2606.05792)、[HTML](https://arxiv.org/html/2606.05792v1)。
- **设置**：30 LLM（8 家族）× 205 TLA+ spec；25 开源模型 × 4 种 prompting（2600 runs）+ 5 专有 few-shot（130 runs）；SANY + TLC 双层判定。
- **量化结果表**：

| 指标 | 结果 |
|---|---|
| 语法正确率上限 | 26.6% |
| 语义正确率上限 | 8.6%（仅 progressive prompting） |
| 规模效应 | 无——DeepSeek r1:8b 全面胜 70B 版 |
| 代码特化模型 | 一致垫底（负迁移） |

- **局限自述**："当前 LLM 没有专家监督**不能**生成可靠 TLA+ spec。"五类幻觉可溯源训练数据偏置。**开源**：评测框架+数据集（摘要自述）。

### 1.4 软件断言线补充

- **Monty**（arXiv 2607.13303，2026-07，UIUC Madhusudan 组，[abs](https://arxiv.org/abs/2607.13303)）：NL → Java 集合类断言，conformance score + 有效性测试过滤幻觉；541 任务/22 类上精确率平均提升最多 **20pp**。
- **NL2ACSL**（Knowledge-Based Systems Vol 335, 2025, [dl.acm.org](https://dl.acm.org/doi/10.1016/j.knosys.2025.115177)）：NL → ANSI/ISO C 规约语言，交互式翻译，已过期刊同行评审——C 嵌入式侧的 autoformalization 开始产品化。

### 1.5 哪条线在逼近"工程实用"

不是数学证明线（PutnamBench 个位数、Erdős 一年个位数），而是**软件断言线**（Verus/Dafny/ACSL）：①验证器全自动可判，②测试集是天然 oracle，③规格规模小。数学线的最大贡献是把"忠实度"变成可度量对象（§4.1），方法论正反哺软件线。

---

## 2. AI for Math / 形式化社区的外溢：Lean 生态 2026 年的自动化水平

这是本篇最重要的一节：AI-for-Math 在 2026 上半年发生了三件标志性事件，其对"NL spec → 形式化"路线的启示互相矛盾，值得并列读。

### 2.1 三件标志性事件

1. **Erdős Problem #728 被自主解决**（arXiv 2601.07421，2026-01，Sothanaphan 写up，[abs](https://arxiv.org/abs/2601.07421)、[HTML](https://arxiv.org/html/2601.07421v5)）：**第一个被 AI 系统视为完全自主解决的 Erdős 问题**。系统 = GPT-5.2 Pro（OpenAI）+ **Aristotle**（Harmonic 的 Lean 验证 agent），由人操作（Kevin Barreto），产出 Lean 形式证明，人类数学家反向把它翻译回非正式数学供社区读。Harmonic 同期向 Lean FRO 捐资 $300,000（[公告](https://www.harmonic.fun/news/lean-fro-donation/)）——商业资本在压注"AI 形式化数学"。
2. **AutoformBot / Atlas：教科书级规模形式化**（arXiv 2605.29955，2026-05，FAIR/NYU 系：Kempe、Munos、Cabannes、Hayat 等，[abs](https://arxiv.org/abs/2605.29955)、[HTML](https://arxiv.org/html/2605.29955v1)）：数千 LLM agent + 依赖感知调度 + 协作版本控制，把 26 本开放教材（分析/代数/拓扑/组合/概率）翻译成 Lean 4——**45,000+ 形式声明、50 万行代码**的已验证库 Atlas。摘要结论："研究生级数学核心内容的规模 autoformalization 现在**经济与技术上均可行**"。开源（框架+库）。
3. **系统软件证明自动化**（OSDI'26，arXiv 2603.19715，南京大学，[abs](https://arxiv.org/abs/2603.19715)）：Isabelle 上神经-符号证明搜索，seL4 基准定理自动证明至 **77.6%**，远超以往 LLM 方法与裸 Sledgehammer。**开源**：[SoaringE/seL4-proof-search](https://github.com/SoaringE/seL4-proof-search)。

辅证：**Aria**（ICLR 2026，[proceedings 页](https://proceedings.iclr.cc/paper_files/paper/2026/hash/13d08d8dee96cacff8ccac07d512bf2e-Abstract-Conference.html)）——依赖图驱动的检索式迭代 autoformalization agent；**LeanFlow**（arXiv 2607.20503）——工作流式 Lean autoformalization 案例研究。说明"agentic autoformalization"已是 ICLR/ICML 级别的独立赛道。

### 2.2 关键判断：工程 spec 比数学定理简单还是难？

**陈述更简单，验证更难——难在监督信号反向。**

- **简单的一面**：工程 spec 的形式化对象（输入输出关系、前置/后置条件、不变量）在逻辑复杂度上远低于 Erdős 问题或研究生数学；AutoformBot 证明"翻译这步"在量上可工业化；Dafny 空证明基线就有 39–44%（§1.1）。若只看"翻译成可判公式的难度"，工程 spec 明显更简单。
- **难的一面（结构性）**：
  1. **数学有社区 oracle，工程没有**。Erdős #728 的 Lean 证明能被数学家读回并接受（writeup 论文本身存在就是证明）；Atlas 的每个定义能对 textbook prose 逐句比对。工程 NL spec 的"原文"是意图，**而意图只在用户脑子里**——Lahiri（2603.17150）称之为"没有 oracle，唯一 oracle 是用户"。Verus-SpecGym 靠 Codeforces hacks 造对抗测试，本质是在**人工伪造**数学界免费享有的那套检验生态。
  2. **数学陈述是封闭世界，工程 spec 是开放世界**：教材句子自足；工程 spec 依赖环境假设、未陈述约束——DevIntent（§4.3）实测：连"已澄清的 prompt"里被剥掉的隐含约束都会让一半以上生成违反意图。
  3. **数学证明一次成型，工程 spec 随代码演化**：Atlas 没有"改需求"问题；whenwords #6（01 篇）证明 spec↔tests↔code 三角漂移才是工程的主战场，而这在数学范式里不存在。
- **结论**：Lean 生态的外溢给工程路线的是**方法论**（agentic + 依赖调度 + 机器检查 kernel + 人类只读陈述）而非**直接可用性**。AutoformBot 的架构图（数千 agent、kernel 检查、人类只管陈述层）几乎就是 Consort/CodeLeash 想要的工程管道的数学版——差的正是那个能替代"数学家读回"环节的工程 oracle。

---

## 3. Spec 可验证性基准：SpecGym 及同类

### 3.1 Verus-SpecBench / Verus-SpecGym（arXiv 2605.26457，2026-05，01 篇已提，此处展开）

- **机构**：CMU（Welleck、Parno）+ ETH（Limperg）+ UC Berkeley；作者含 Verus 维护者。**一手**：[abs](https://arxiv.org/abs/2605.26457)、[HTML](https://arxiv.org/html/2605.26457v1)。
- **测什么**：581 个 Codeforces 派生 spec 编写任务，目标 Verus。核心创新是**评测方法**：扩展 `exec_spec` 让形式 spec 作为 Rust 代码执行，跑官方测试 + 从 Codeforces "hacks" 提取的对抗反例——用执行判忠实度，绕开"参考 spec 贵、LLM-judge 抓不住细微错"。
- **量化结果表**：

| 模型档 | 任务通过率 |
|---|---|
| Gemini 3.1 Pro | 77.8% |
| 其他前沿模型 | 51.1–57.8% |
| 开源模型 | 21.5–25.5% |
| LLM-as-judge 漏检 | 漏掉 26%（执行评测可抓到的失败） |

- **失败模式三类**：漏输入前置条件、接受错误输出、拒绝合法输出。**局限自述**："spec autoformalization 对前沿 agent 触手可及，但在它们已能写对代码的题上仍脆弱"——代码能力 ≠ spec 忠实度。**开源**：[verus-spec-gym](https://github.com/formal-verif-is-cool/verus-spec-gym)（代码+数据+日志）。

### 3.2 Coins（ICML 2026 poster，[会议页](https://icml.cc/virtual/2026/poster/66406)、[OpenReview](https://openreview.net/forum?id=41zGzIEpQd)、[代码](https://github.com/taylor-swift-13/Coins)，中科院软件所）

Rocq 上的 spec 质量评测：把被评 spec 在可信测试用例上实例化成具体证明义务，显式建模"证明通过是可靠证据、失败是模糊信号"的不对称。结果：spec 生成"仍是 formidable challenge"，且**验证复杂度遮蔽 spec 质量的真实差异**（"证不出来"≠"spec 错"）。局限：依赖人工 Rocq 参考集，规模限 HumanEval。开源。

### 3.3 同类与反向

- **AfterVibe**（arXiv 2607.09900，IBM Research，[abs](https://arxiv.org/abs/2607.09900)）：反向任务——从 vibe coding 会话恢复 NL spec，用"盲体重生成"打分。72 个真实公司项目：平均再生分 **5.06/6.0**，迭代精炼后 **5.74**。把"spec 好不好"操作化为"另一个模型能否只凭它重建等价代码"。
- **共见局限**：全部基准用"测试/重生成/探针"当 oracle，覆盖率本身是近似；没有一个基准测非功能性意图；Coins 警告验证复杂度污染信号。

---

## 4. LLM×形式验证的工业级案例（非玩具域，逐个列，含规模与成本）

### 4.1 案例表

| # | 系统/域 | 规模 | 验证了什么 | LLM 角色 | 成本/资源数字 | 出处 |
|---|---|---|---|---|---|---|
| 1 | **MakerDAO 等真实以太坊合约**（EVM 字节码 / Lean，EquiVM 框架） | **23 个真实已部署合约端到端证明**，含 MakerDAO 稳定币系统大部分 | 部署字节码 ↔ 高层 spec 的**基础主义（foundational）精化证明**：可执行 EVM 语义 + spec 语言 + 每份证明是可重放的机器检查证书 | LLM agentic 证明开发，人类"minimal guidance"；spec 由人给 | **每合约最高 1 亿 token、100 小时证明时间**；对照：行业审计市价 $25k–100k/中等 DeFi 协议（综述转引价） | [arXiv 2607.26306](https://arxiv.org/abs/2607.26306)（Lazaropoulos & Paraskevopoulou，2026-07） |
| 2 | **RISC-V 处理器流片**（应用→编译器→执行体→芯片，Salt method） | **5 周、1 名研究者、消费级 AI 订阅**驱动 agent 小队：应用代码、已验证编译器与执行体、RISC-V 芯片在社区 shuttle 流片 | 全栈逐层机器检查：Lean 4 kernel 到硅边界的 SAT 等价检查；**没有任何证明经人审、没有任何 RTL 由人写** | LLM 写全部工件与证明；人类只管陈述、设计与裁决；证明 kernel 是"幻觉证明过不去的门" | 5 周人时（floor 计量）、token 预注册计量、错误台账编号至 #256（2026-07-07→07-20 计数），**零错误证明入库** | [arXiv 2608.21356](https://arxiv.org/abs/2608.21356)（Jason Hickey，前 Google，2026-08） |
| 3 | **seL4 微内核**（OS 内核，Isabelle；部署于汽车/国防） | FVEL seL4 基准全量定理，自动证明至 **77.6%** | 在既有人类形式化之上自动补证明脚本；多步证明显著超以往 | LLM 只出证明步；**spec 与定理库全部人类既有** | 未披露 token 成本；对比：seL4 原验证约 20 人年（seL4 SOSP'09 论文及后续公开访谈所载数，未单独回源）量级（历史公开数，非本论文数据） | [arXiv 2603.19715](https://arxiv.org/abs/2603.19715)，OSDI'26 |
| 4 | **Lockheed Martin 国防部署 + NVIDIA-OpenSMA**（ESBMC 模型检验生态） | ESBMC：9 个语言前端、43 次 SV-COMP/Test-Comp 奖、**GB £9.3M + €4.98M 公共研究经费**、VeriBee 分拆、**Lockheed Martin 国防工业部署**、NVIDIA-OpenSMA **首个 agentic 模型检验工业部署** | 嵌入式 C 软件的 bounded model checking；LLM 耦合方向：self-healing 软件、循环不变量生成 | LLM 是"自主验证内核"的驱动方而非被动后端 | 经费/部署数字见综述摘要 | [arXiv 2605.26169](https://arxiv.org/abs/2605.26169)（ESBMC survey，2026-05） |
| 5 | **某公司内部 72 个 vibe-coded 项目**（IBM Research） | 72 项目、真实会话轨迹 | 不验证代码——验证从会话**恢复的 NL spec**（盲体重生成等价性，5.06/6.0） | LLM 提取 spec、重建、判分；人环外 | 分数为主，无成本数 | [arXiv 2607.09900](https://arxiv.org/abs/2607.09900) |
| 6 | **seL4 第二线**（存在性）：Towards Real-World Industrial-Scale Verification: LLM-Driven Theorem Proving on seL4 | 未回源细节（abs 多次 403/202） | — | — | — | [Semantic Scholar](https://www.semanticscholar.org/paper/077b991e67303f589abb20f7b928672ce33094f4) |
| 7 | **Show Me The Money**（CAV 2026，proof-driven software understanding） | 未回源正文；Zenodo artifact 2026-05 公开 | 证明资产再利用/理解 | — | — | [artifact](https://zenodo.org/records/20164192) |

### 4.2 Consort 展开（01 篇已提，补学术面）

arXiv 2609.09671（Kevin Hartman，Databricks Solutions，[abs](https://arxiv.org/abs/2609.09671)、[代码](https://github.com/databricks-solutions/consort)）：把 agent 框架纪律分三模式——persuasion / front-loaded structure / **uneditable controls**（确定性编排 + 人批门禁 + 不可变测试 + 活数据库分支绿灯）。学术价值不在实验（自称 pre-registered hypothesis，未跑实验），而在分类学：Spec Kit、superpowers、BMAD、GSD 全部被归入前两类。

### 4.3 工业案例的诚实结论

非玩具域案例**真实存在且 2026 年密集出现**（金融=MakerDAO、硬件=RISC-V、国防=Lockheed Martin、OS=seL4），但注意其共同结构：**LLM 采购的是"证明产能"，不是"spec 忠实度"**——案例 1/3 的 spec 层全部由人给；案例 2 的突破恰恰是把人类注意力从证明层撤到"陈述层"（statements），即：**越是工业级成功案例，spec 层越依赖人类亲自签核**。完整"NL → 形式 spec → 生产验证"闭环仍无一例。

---

## 5. 负面结果与边界（含 spec↔code 语义 gap 实测）

1. **忠实度鸿沟被量化**（arXiv 2606.16541，*The Faithfulness Gap*，2026-06，[abs](https://arxiv.org/abs/2606.16541)）：形式化语句可 typecheck 且可证，却编码**另一个定理**。BPF+反事实探针，DriftBench 2,183 对 NL/Lean4：

| 判定器 | 漂移检出率（3.0% 假阳） |
|---|---|
| typecheck | 41.2% |
| LLM-judge | 63.3% |
| BPF+探针 | **89.6%** |

   忠实度引导解码降 47% 漂移率。含义：**通过形式验证 ≠ 与意图一致**，且常规检查手段漏检率 36.7%–58.8%（由各论文检出率 63.3%/41.2% 换算，非论文原数）。
2. **不可判定性的 LLM 语境重述**（arXiv 2511.12869，v2 2026-01，TMLR 投稿，[abs](https://arxiv.org/abs/2511.12869)）：对可计算枚举模型族，对角化保证必然失败输入；不可判定查询对所有可计算预测器诱导无穷失败集；信息论/上下文压缩另设天花板。把 01 篇 pron 的 intractable 论证升级为覆盖 LLM 本身的定理框架——**换更大模型不消除验证缺口，只缩小可判定子域内的错误率**。
3. **spec↔code 语义 gap 实测：DevIntent / IVR**（arXiv 2608.07614，2026-08，[abs](https://arxiv.org/abs/2608.07614)、[HTML](https://arxiv.org/html/2608.07614v1)）：Intent Violation Rate——把"已澄清 prompt 里的隐含约束"剥出来做成隐藏测试。49 题试点（HumanEval+ 派生）：Claude Sonnet 4.6 与 GPT 4.1 **陈述测试通过率 >92%，意图违反率 54.5% / 63.5%**，且呈双峰系统模式。这是"测试通过 ≠ 意图满足"的第一批直接量化，从 code 侧镜像了 2606.16541 从 spec 侧的结论。
4. **验证者永远是代理**（arXiv 2606.26300，*The Verification Horizon*，2026-06，Qwen 团队系（确切署名机构未取得），[abs](https://arxiv.org/abs/2606.26300)）：系统级论证"验证比生成更难"的倒转：任何验证器只是意图的 proxy；优化过程主动拉大 proxy↔intent gap（reward hacking、信号饱和）；**没有固定 reward 函数能随策略能力增长持续有效，验证必须与生成器共同演化**。这是对"一次性建好 spec 门禁"想法的直接否定——门禁是运营承诺不是一次性工程。
5. **能力实测否定数字汇总**：TLA+ 语义正确 8.6%（§1.3）；Verus 上漏前置条件恰是最危险失败（§3.1）；Coins"验证复杂度遮蔽 spec 质量"（§3.2）；ConjectureBench"现有分数系统性高估"（§1.2）；LLM-judge 漏检 26%（§3.1）。
6. **规模化边界自述**（2509.09810，AAAI 2026，[abs](https://arxiv.org/abs/2509.09810)）：autoformalization 系统"在精选基准上 work，难以扩展到真实实践"，三子领域基准互不相通。
7. **权威边界宣言**（arXiv 2603.17150，2026-03，Shuvendu Lahiri（Microsoft Research），*Intent Formalization: A Grand Challenge*，[abs](https://arxiv.org/abs/2603.17150)、[博客版](https://risemsr.github.io/blog/2026-03-05-shuvendu-intent-formalization/)）：**spec 正确性没有 oracle，唯一 oracle 是用户本人**；核心瓶颈是 spec 验证的半自动度量。开放难题：超基准规模化、变更组合性、spec 验证度量、丰富逻辑、人机 spec 交互。路线被承认可行，但只在"轻量测试 ↔ 完整功能 spec ↔ 合成用 DSL"权衡谱上局部取舍。

---

## 6. 综合：三层回答

### 6.1 现在（2026-09）能做到什么

- **已经能用（零研究风险）**：①spec 忠实度评测的四种方案（执行式/实例化义务/重生成/双向探针）可直接借为团队 spec 门禁思想——生成 spec 后跑对抗测试而非 LLM-judge（judge judge 漏检：Verus 论文测得 26%；Faithfulness Gap 论文测得 36.7%（由检出率 63.3% 换算）——两数分属不同论文，不可合并为区间）；②LLM 当"证明产能采购"：给已有高价值形式化资产（或 EquiVM 类框架）补证明，成本已是"1 亿 token + 100 小时"量级而非人年；③命令级/断言级 autoformalization（Monty +20pp、NL2ACSL）作为草稿生成器 + 差异探测器，人签核后进 CI。
- **仍不能**：NL → 严肃形式语言（TLA+ 语义 8.6%）直连；无 oracle 的意图补全；把 autoformalization 当编译器（不签核直接信任）。

### 6.2 2027 年可能做到什么

- Verus/Dafny 级断言 autoformalization 在限域内接近"可用草稿 + 自动对抗测试"标准线（前沿模型已 77.8%，失败模式明确可针对性修）；BPF 类忠实度探针会被产品化进验证工具链（对 TLA+/Dafny 的移植是工程活）；agentic 证明自动化从 Lean/Isabelle 扩到工程验证器（OSDI seL4 77.6% → 常态化）；Consort 式"不可编辑门禁 + 形式化验证层"两截管道可能首次接通——因为 2608.21356 已示范"kernel 检查的陈述层 + 人类只管陈述"的组织形态可跑通全栈。
- 前提条件：探针/对抗用例的生成成本继续下降；某一垂直域（合约或内核）先长出可复用的 spec 模板库。

### 6.3 永远做不到什么（结构性障碍）

1. **意图没有 oracle**（Lahiri 定理）：任何验证器都是意图的 proxy；隐含约束的违反率实测 >50% 即使 prompt 已澄清（DevIntent）。"NL spec 完全自动忠实化"在原理上不可达，人类签核陈述层不可撤除——只能压缩，不能归零。
2. **不可判定性**（2511.12869）：对任意可计算验证体系，存在必然漏掉的输入/性质；哪些性质可验、代价多少，事先不可知（01 篇 pron 条的定理化）。
3. **proxy↔intent gap 与生成器共同演化**（2606.26300）：即使某天 spec 门禁完美，它也会被针对它的优化腐蚀；验证是持续运营成本，不是一次性资产——这与 01 篇 facts 的"consistency tax"是同一枚硬币的学术面。
4. **开放世界性**：数学形式化有封闭自足的原文与社区读回机制；工程 spec 绑定环境假设与演化历史，Atlas 式"一次翻译永久成立"的经济学在工程侧不存在。

### 6.4 一段话回填光谱

学术界已证明：可验证 spec 的**评测可做、生成脆弱、证明便宜了、闭环不存在**。2026 年最有信息量的对峙是——2608.21356 展示"人类只写陈述、机器负责其余、kernel 防幻觉"已能流片一颗处理器，而 2606.16541/2608.07614 同时证明"陈述本身对不对"没有机器可判的标准。两条曲线夹出的团队可落地位置，与 01 篇社区收敛的实践（command-fact + 人类签核 + 对抗评测门禁）从两端逼近了同一个中间态：**人类垄断陈述层，机器垄断证明层，门禁必须是活的。**
