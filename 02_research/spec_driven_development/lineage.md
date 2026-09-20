# SDD 思想谱系——它从哪里来

> 定位：补齐"SDD 是否只是新瀑布"这一审计缺口。本文件梳理 Spec-Driven Development（SDD）的智识前身，逐节点给出年代 / 人物 / 原始文献 / 与 SDD 的对照。
>
> **史实与分析的区分约定**：标注【史实】的条目有文献锚点；标注【分析】的是本文件的推断，不能当史实引用。

```yaml
metadata:
  file: 02_research/spec_driven_development/lineage.md
  accessed_at: 2026-09-20
  method: web_search + web_fetch 逐节点核实原始出处
  key_sources_verified:
    - https://dannorth.net/introducing-bdd/          # 原文（含 colophon：首发 Better Software 2006-03）
    - https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html   # Böckeler, 2025-10-15
    - https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/  # GitHub spec-kit
    - https://ai.engineer/talks/8rABwKRsec4-specifications-are-the-new-code # Sean Grove, AI Engineer World's Fair 2025
    - https://eu.36kr.com/zh/p/3388182127870345     # 对 Grove 演讲的"新瀑布"批评（二手中文报道）
  limitations:
    - MDA/OMG 未直接抓取 OMG 官方规范页，MDD 失败教训部分依赖 Böckeler 一手亲历叙述 + 学术文献线索，证据强度中。
    - Meyer DbC 以 OOSC 教材讲义（se.inf.ethz.ch）为锚，未核对 1986 原始 IEEE Software 论文原文。
```

---

## 1. 直接前身

### 1.1 Model-Driven Development / MDA（OMG，2001 起）

- **年代/人物**：OMG 于 2001 年发布 Model-Driven Architecture（MDA）白皮书，主张以平台无关模型（PIM）→ 平台相关模型（PSM）→ 代码为正向生成链路。【史实】
- **原始文献**：OMG MDA 官方页（omg.org mda 规范族）；亲历者一手叙述见 [Böckeler《Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl》](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)（2025-10-15）"MDD never took off for business applications" 一节。
- **与 SDD 的机制同构点**【史实层面的对应关系，判断为分析】：模型/规范为源、代码为生成产物、"维护即演进模型"——这三条正是今天 spec-kit"Tessl 式 spec-as-source"（代码标注 `// GENERATED FROM SPEC - DO NOT EDIT`）的直接翻版。Böckeler 原话：MDD 里"The models in MDD were basically the specs"。
- **失败教训**【分析，有 Böckeler 一手亲历佐证】：①工具化过度——需要自建解析器与代码生成器，成本前置且刚性；②与代码漂移——生成后开发者直接改代码，模型沦为一次性脚手架；③抽象层级尴尬——MDA 卡在"太具体不能当需求、太抽象不能当代码"的位置。
- **对照一句话**：SDD 复刻了 MDD"规范为源"的承诺，而 LLM 移除的是"自建生成器 + 可解析规范语言"这两项刚性成本；但"规范与代码漂移"这一失败根源并未被工具消除，只被改写为"规范债"问题。

### 1.2 Design by Contract（Meyer，1986/1992）

- **年代/人物**：Bertrand Meyer，1986 年首篇论文，随 Eiffel 语言在《Object-Oriented Software Construction》（1992/1997）系统化。【史实】
- **原始文献**：[ETH 教材讲义（DbC 章）](http://se.inf.ethz.ch/old/teaching/ss2005/0250/lectures/oosc_12_dbc_4up.pdf)；[ACM 相关文献](https://dl.acm.org/doi/pdf/10.1145/1144366.1144369)。
- **与 SDD 的亲缘**【分析】：前置条件 / 后置条件 / 不变式 = 今天 SDD 验收标准（Kiro 的 GIVEN/WHEN/THEN 验收条款、spec-kit 的 checklist"definition of done"）的约束化前身——都是把"完成"从主观判断变成可机械判定的契约。
- **对照一句话**：DbC 证明了契约可执行但只在接口粒度规模化（语言级支持才可行），SDD 把契约提升到功能/系统粒度，靠的是 LLM 生成验证物而非编译器强制——粒度扩大是新的，"契约写全很难"这一点没变。

### 1.3 形式化方法（Z / VDM / SPARK，1980s–1990s）

- **年代/人物**：Z（Oxford PRG，1970s 末–80s）、VDM（IBM 维也纳，1970s）、SPARK（Alsys/ Praxis，1988 起，高保障领域存活至今）。【史实，学术综述线索见 [ACM 论文提及 IBM CICS 用 Z](https://dl.acm.org/doi/pdf/10.1145/3815784)】
- **为什么没规模化**【分析，主流学术共识】：规范书写 + 证明义务的人力成本远超多数商业软件的风险预算；形式规范语言对从业者的学习曲线陡峭；商业应用正确性要求与证明成本不匹配。
- **SDD 是否改变其成本结构**【分析】：部分改变。"写规范"这一半成本被 LLM 大幅降低（自然语言替代形式记法、机器起草替代人工誊写）；但"证明正确"这一半没有——SDD 的验证仍以测试/验收为主，不是语义等价证明。所以 SDD 是形式化方法的"低保证、低成本"表亲，不是它的规模化复现。

---

## 2. 敏捷时代的过渡：BDD（Dan North，2006）

- **年代/人物**：Dan North，《Introducing BDD》首发于 Better Software 杂志 2006 年 3 月，个人博客版本发布于 2006-09-20。【史实】
- **原始文献**：[dannorth.net/introducing-bdd/](https://dannorth.net/introducing-bdd/)（本次直接抓取原文核实，含 colophon）。
- **机制**【史实】：把验收标准写成 Given/When/Then 场景，片段映射为可执行代码（JBehave），即"验收标准应当是可执行的"——这是"可执行 spec"的第一次成体系尝试；其思想源头是 DDD 的 ubiquitous language（North & Matts 明确引用 Evans 2003）。
- **2010s 的衰退**【分析，业界普遍叙述，本次未找到权威定量文献，保守表述】：Gherkin 场景与代码/测试的双份维护成本高，step 定义碎片化，非技术角色实际很少参与编写，最终多数团队发现场景文件"写了没人看、改了没人跟"，退化为昂贵的重复测试。Cucumber 社区 2010 年代后期的自我反思（如 Aslak Hellesøy 的相关演讲）与此一致，此处标注为待补证的弱锚点。
- **对 SDD spec 债风险的意义（最重要的历史参照）**【分析】：BDD 已经演示过一次"规范成为长期资产"的完整周期——起步兴奋 → 维护负担显现 → 规范与实现漂移 → 规范被弃用。SDD 的 spec-anchored / spec-as-source 层级与 Gherkin 场景的区别仅在于：这次规范是给 LLM 读的，读者存在了；但"谁保证规范随现实更新"的机制问题和当年完全同构。这直接回响 `debate/critiques.md` 中对 SDD 的 spec 漂移批判：**若 SDD 无法回答"规范过期后 LLM 照着过期规范生成错误代码，比 Gherkin 过期更危险"，BDD 的结局就是它的先例。**
- **对照一句话**：BDD = 人工时代"可执行 spec"的成本不可行版；SDD = LLM 时代同一承诺的重试，赌注是"机器消化维护成本"能否兑现。

---

## 3. AI 时代的重新发声（2024–2025）

### 3.1 条件变化【史实层面的事实 + 分析的混合，逐条标注】

- **Kiro（AWS，2025-07 preview）**【史实】：Requirements → Design → Tasks 三件套 markdown 工作流，验收标准用 GIVEN/WHEN/THEN——直接继承 BDD 模板。来源：[Böckeler 对 Kiro 的实测](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)、[kiro.dev](https://kiro.dev/)。
- **GitHub spec-kit（2025-09）**【史实】：Constitution → Specify → Plan → Tasks；GitHub 官方口号"maintaining software means evolving specifications / code is the last-mile approach"。来源：[GitHub Blog](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)、[spec-kit 仓库](https://github.com/github/spec-kit)。
- **Sean Grove（OpenAI）"The New Code: Specifications are the Source of Truth"**【史实+核实结果】：原始出处是 **AI Engineer World's Fair 2025 演讲**，见 [ai.engineer 官方 talk 页](https://ai.engineer/talks/8rABwKRsec4-specifications-are-the-new-code)。核心论点：代码只承载程序员价值的一小部分，结构化沟通（规范）才是稀缺资产；"一份 100 行规范胜过 10 万行代码"。网络流传的"Specifications are the future"是其转述形式；该演讲在中文圈被广泛转述为"提示词工程已死、规范编程才是未来"（[36kr 报道](https://eu.36kr.com/zh/p/3388182127870345)，该报道同时给出了"SDD=瀑布回魂"的批评视角，可与本仓库 critiques 呼应）。**注意：Grove 是观点/预测，不是史实结论。**
- **Böckeler/Fowler 站点锚点（2025-10-15）**【史实】：本谱系梳理的第三方权威锚，[原文](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)。其贡献：①区分 SDD 三个实现层级（spec-first / spec-anchored / spec-as-source）；②明确建议把 MDD（而非常被类比的 TDD/BDD）作为 spec-as-source 的历史参照；③警告 SDD 术语已[语义扩散](https://martinfowler.com/bliki/SemanticDiffusion.html)。她同时给出与 MDD 失败直接相关的判断："spec-as-source 可能同时继承 MDD 的僵化和 LLM 的非确定性"。【该判断为分析，出自身份是 practitioner 亲历】

### 3.2 为什么"自然语言 spec 直接驱动实现"这次成本可行【分析】

三条新条件，缺一不可：
1. **LLM 消化了"spec→代码"的执行成本**：不再需要自建可解析规范语言与代码生成器（MDD 的死因之一）。
2. **LLM 消化了"规范理解"的读者成本**：自然语言规范第一次有了机器读者；BDD 时代业务方不读 Gherkin，现在 agent 读。
3. **验证闭环半自动化**：spec 内的验收标准可由 agent 转为测试并自检——但"半"字是关键，这正是与 BDD 死结的对赌点（见 §4）。

---

## 4. 结论：历史重演 vs 真新事物

**重演的部分（风险项）**【分析】：
- "规范为源、代码为产物"的承诺 = MDD 逐字重演；MDD 的三个死因中，工具成本已被 LLM 消解，但**抽象层级尴尬**（Böckeler 的"问题规模/清晰度四象限"质疑：小任务用 SDD 是牛刀杀鸡）和**规范与实现漂移**（spec-kit 每个 spec 开新分支的做法说明它实际只是 spec-first 而非 spec-anchored）依然在。
- "一次性大前置规范"对敏捷"小步迭代"原则的背离 = 36kr 所称"瀑布回魂"批评，与 2000 年代 agile 对 Big Design Up-Front 的批判完全同构。
- "可执行验收标准"的模板 = BDD Given/When/Then 直系复用（Kiro 的 requirements.md 结构可证）。

**新条件下的真新事物（机会项）**【分析】：
- 执行成本换手：spec→代码的翻译成本从"人类工具链"转移到"LLM 推理"，且 LLM 能消化非结构化输入——这是 MDD/BDD 都不具备的条件。
- 规范读者从零到一：BDD 的"业务可读规范"从未真正有人读；agent 是第一个每份规范都会被完整消费的读者。
- **未决的对赌**：SDD 若只用规范做一次性引导（spec-first），它是安全的，但也只是昂贵的 prompt；若做 spec-as-source，就必须回答 BDD 答不上来的问题——规范的持续维护机制。"可执行验证"（agent 从 spec 生成测试）理论上能缓解漂移，但测试本身也由 spec 生成，等于同源验证，不能证明 spec 与现实一致。**BDD 的维护成本死结没有被解决，只是被推迟到规范债积累之后。**

**给审计的一句话**：说"SDD=新瀑布"或"SDD=全新范式"都缺据；有据的说法是——**SDD 是 MDD 的承诺 + BDD 的模板，在 LLM 改变成本结构后的第三次重试；前两次死因中一条被消解（工具成本）、两条仍在（漂移、粒度失配），成败取决于 spec 维护机制而非 spec 编写体验。**
