# 深挖四：Harness 治理派——治理对象从 spec 文档转向 agent 执行链路

> **元数据**
> - 观测日期：2026-09-20（2026 材料优先；OpenAI 原文 2026-02-11，Hashimoto 2026-02-05，arXiv 2026-08-31）
> - 底稿：`02_research/spec_driven_development/alternatives.md` 第 4 节（本文为深挖展开，不复制底稿结论）
> - 定位：五形态中**证据最硬、最可能是团队级收敛点**的一条，故挖最深
> - 证据强度说明：OpenAI 一手原文（openai.com）在本次观测中直接抓取被拒（403），细节经两个高保真第三方消化源交叉核验后引用，已逐条标注；一手源（Hashimoto、arXiv HTML 全文）均直接回源
> - 上游文档指针：五形态总览与光谱图见 `alternatives.md`；验证优先派见 `01-*`（同目录系列）

---

## 0. 一句话立场

Harness 治理派的立场不是"不写 spec"，而是**把工程投入的重心从"把 spec 写对"移到"把 agent 的执行环境工程化"**：agent 出错时，标准反应不再是"把 spec 写得更细"，而是"执行链路里还缺什么能力——linter？验证脚本？日志？review loop？"spec 在这套系统里降格为一个**可替换组件**，而非方法论本体。

---

## 1. OpenAI《Harness Engineering》（2026-02-11）：1500 PR / 1M 行的组织方式全文细节

*一手源：[openai.com/index/harness-engineering](https://openai.com/index/harness-engineering/)（Ryan Lopopolo，2026-02-11；原文直接抓取 403，以下细节经 [pankaj28843/agentic-engineering-research](https://github.com/pankaj28843/agentic-engineering-research/blob/main/research/06-openai-harness-engineering/guide/00-README.md) 的逐章消化稿与 [FlorianBruniaux/claude-code-ultimate-guide 的资源评估卡](https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/docs/resource-evaluations/2026-02-11-openai-harness-engineering.md) 交叉核验，两源一致处才收录）*

### 1.1 实验基设

- 5 个月、3 人工程团队、内部 beta 产品、**零手写代码**（Codex 写应用逻辑、测试、CI 配置、文档、可观测性、内部工具、review 评论、生产 dashboard 定义），约 100 万行、约 1500 个 PR，即**约 3.5 PR/工程师/天**。所有数字为一手自述，无独立验证（评估卡原文即如此标注）。
- 中心命题："Humans steer. Agents execute."——人类不再是代码的直接来源，而是**环境设计者**；稀缺资源被明确定义为**人的注意力**，harness 的所有设计决策都从这个约束推出。

### 1.2 三个文档目录的格式与生命周期

仓库知识库是"system of record"：**不在 repo 里的知识，对 agent 而言不存在**。三个目录是这套知识库的三个生命周期阶段：

| 目录 | 承载内容 | 格式要点 | 生命周期 |
|---|---|---|---|
| `docs/product-specs/` | 产品行为、用户可见验收标准、产品原则 | 带 `index.md` 索引； tribal 产品原则（"问团队才知道"的那种）必须落成文档 | 行为变更的**同一 PR 内必须同步更新**（ownership 规则），否则由 doc linter / gardening agent 抓漂移 |
| `docs/design-docs/` | 架构决策与"为什么"（worldmonitor 实例中对应 "Design Philosophy"） | 交叉引用 `ARCHITECTURE.md`，含 source-file 引用与所有权 | 决策变更时更新；陈旧化由 freshness linter 检测 |
| `docs/exec-plans/` | 执行计划（first-class artifact） | `active/` + `completed/` + `tech-debt-tracker.md` 三段结构；active 计划含 goal、验收标准、来源链接、状态、checklist、决策、验证命令、证据产物、**recovery note** | 小改动用轻量计划，复杂工作用完整 exec plan；完成后移入 completed；tech debt 进 tracker 而非散落 |

exec plan 里的 recovery note 是给"无记忆的新 agent"用的恢复内存：长循环挺过 context 压缩、进程重启和交接，靠的是把事实写进计划文件而非聊天记录。这是它与人用 todo list 的本质差异——**读者可能是一个全新 agent**。

入口是**约 100 行的 `AGENTS.md`**，只做"目录/路由"：repo 是什么、哪些命令证明工作、先读哪些 docs、哪些边界不可协商。更深的 docs 因为只在任务相关时才被读取，可以写长——这是 progressive disclosure 在 repo 级的应用（与 Codex Agent Skills 的 name/description 先见、SKILL.md 按需读同一原理）。

### 1.3 doc-gardening agent 怎么工作

- **触发与动作**：周期性后台 agent，扫描"陈旧/过时文档"，**直接开 fix-up PR**（不是发报告）。
- **配套机器**：专门 linter + CI job 校验知识库"最新、互链、结构正确"（链接健康、必需章节、生成文档新鲜度、plan 状态）。生成文档（db-schema、routes、openapi 等）的规则是"**必须新鲜或明确标 stale**"——陈旧的生成 schema 比没有更糟，因为 agent 会信它；CI 用 `git diff --exit-code docs/generated` 兜底。
- **可复刻的下位替代**（消化稿给出的最小实现）：`rg "TODO|TBD|stale|deprecated" docs` + 链接检查 + owner/freshness 元数据表。要点不是 paperwork，而是**让文档变得可被 agent 维护**——有 owner、有保鲜期、有校验，gardening agent 才开得出有用的 PR。

### 1.4 完整模式清单（评估卡归纳的 10 条）

1. AGENTS.md 作 ~100 行 TOC，不是百科全书
2. "agent 看不见的就不存在"：一切隐性约定必须编码为 repo 内容
3. exec plans 为 first-class artifact（active/completed/tech-debt-tracker）
4. **每 worktree 一份临时可观测性栈**（Vector + VictoriaLogs/Metrics/Traces，LogQL/PromQL/TraceQL）——agent 可直接查运行时行为
5. taste invariants：偏好评**机械化为自定义 linter，错误信息写给 agent 读**（错误消息即"善意 prompt 注入"：不只说错，还说怎么修、为什么重要）
6. doc-gardening agent（见 1.3）
7. 反熵：后台 cleanup agent 按域追踪质量分（QUALITY_SCORE.md），技术债变成增量小 PR 而非大重构
8. 分层域架构（Types/Config/Repo/Service/Runtime/UI）**由 linter 强制**——在 agent 规模下是前置条件而非"以后再补"
9. 高吞吐 merge 哲学："修复便宜、等待昂贵"——PR 生命周期短、阻塞门最少、flake 用后续运行解决。**仅在真实 agent 吞吐 + 修复成本低的前提下成立**，直接照搬即鲁莽
10. agent 自主度渐进：从 bug 复现到 PR 到 merge 的全环自主，人类在更高抽象层在环

### 1.5 他们自述的失败与调整（这部分比成功清单更值钱）

- **"一个巨型 AGENTS.md"失败**：他们先试过单文件大全，结果是 context 压力、指导稀释（什么都重要=什么都不重要）、快速腐烂、难以验证。调整为短 TOC + 分层 docs。这是一手承认的结构性失败，直接反驳"把规则都写进一个 CLAUDE.md/AGENTS.md"的常见做法。
- **人类当浏览器的瓶颈**：早期每个 UI 修复都要人肉看页面。调整为 per-worktree 可启动 app + CDP + DOM 截图/导航 skills，让 agent 自证视觉修复；人的 review 从"看每个页面"上移到"审计证据、判断这类检查是否足够"。
- **merge 规范被吞吐倒逼修改**：传统 PR 门禁在高吞吐下变成反生产。他们没有宣布"去掉所有门禁"，而是把门禁与**修复成本对齐**（见 9 条）。
- **明确承认的未知**（原文自述）：①完全 agent 生成的系统**多年后的架构一致性如何演化，他们不知道**——这是核心长期风险；②私有 harness 中哪些要素是本质、哪些是偶然，不清楚；③报告的速度有多少归功模型能力 vs harness 成熟度，无法分离；④brownfield（深遗留约束）场景是否适用，未验证。OpenAI 官方 Codex 文档同时给出自主度边界的下限设计：本地 workspace-write 默认断网、merge 默认拒绝需显式策略。

---

## 2. Hashimoto 六阶段模型逐阶段展开

*一手源：[mitchellh.com/writing/my-ai-adoption-journey](https://mitchellh.com/writing/my-ai-adoption-journey)（2026-02-05，全文已回源）*

**勘误先行**：底稿称"第六阶段 Engineer the Harness"，实际原文是**六步（Step 1–6）结构，"Engineer the Harness"是 Step 5**，Step 6 是"Always Have an Agent Running"。底稿引用时错位了一步，本文按原文展开（建议回改底稿）。

| 阶段 | 一手内容要点 | 对 harness 派的意义 |
|---|---|---|
| Step 1 Drop the Chatbot | chatbot 在 brownfield 项目产出差、来回贴代码低效；"必须用 agent"——最低要求是能读文件、执行程序、发 HTTP 请求 | 起点：把交互面从对话换成有工具回路的执行环境 |
| Step 2 Reproduce Your Own Work | 强迫自己把每个手动 commit 用 agent 重做一遍（做两次），痛苦但形成专家直觉：①拆小任务不要一次画完猫头鹰；②模糊请求拆 planning/execution 两段会话；③**给 agent 验证手段，它多半能自修并防回归** | 第三条直觉是 Step 5 的种子：验证能力是 harness 的第一等公民 |
| Step 3 End-of-Day Agents | 每天最后 30 分钟启动 overnight agent：深度调研、并行试探模糊想法、`gh` 做 issue/PR triage（只出报告、不许回复） | 证明"人不在场的正进度"需要 harness 里有可供 agent 自主消费的报告面 |
| Step 4 Outsource the Slam Dunks | 高置信任务全外包，自己同时做别的**真正的深度工作**；关键纪律：**关掉 agent 桌面通知**——打断权在人不在 agent；对 Anthropic 技能形成论文的回应：委派的任务不形成技能，但手动做的任务继续形成 | 注意力经济学与 OpenAI 的"人是稀缺资源"同一逻辑 |
| **Step 5 Engineer the Harness** | 见下 | 该文对 harness 派的直接命名贡献 |
| Step 6 Always Have an Agent Running | 目标状态（当前只做到 10–20% 工作日有后台 agent）：持续问"现在有没有 agent 能替我做的事"；配 Amp deep mode（GPT-5.2-Codex）等慢模型跑长任务；**明确不为跑而跑**，多 agent 并行暂时不要 | 阶段六是 harness 建成后的"产能利用"问题，本身不是 harness 手段 |

**Step 5 的具体手段清单**（原文完整清单，就两条，但每条都有锚点实例）：

1. **更好的隐性提示（AGENTS.md）**：agent 反复读错命令、找错 API 这类简单错误 → 更新 AGENTS.md。一手锚点：[Ghostty 的 src/inspector/AGENTS.md](https://github.com/ghostty-org/ghostty/blob/ca07f8c3f775fe437d46722db80a755c2b6e6399/src/inspector/AGENTS.md)——**"文件里每一行都对应一个真实的 agent 坏行为"，且这些行几乎完全消除了对应错误**。这就是底稿说的"每次 agent 犯错就工程化地消灭该错误类别"的最小可复制单位：一行坏行为 = 一行规则。
2. **真正的程序化工具**：截图脚本、过滤测试运行器等可执行验证工具，**且通常配套一条 AGENTS.md 告诉 agent 这个工具存在**（工具不写进地图等于不存在——与 OpenAI 第 2 条模式同构）。

Hashimoto 与 OpenAI 的口径差异值得记录：他自述"不知道这有没有行业通用名，我自己管这叫 harness engineering"——即这个词是 2026 年初由 practitioner 独立命名、OpenAI 同期把它组织化、arXiv 论文随后学术化的一条传播链，而非自上而下的发明。

---

## 3. arXiv 2609.00252：technical harness vs methodological harness 的完整框架

*一手源：[arxiv.org/abs/2609.00252](https://arxiv.org/abs/2609.00252) + [HTML 全文](https://arxiv.org/html/2609.00252v1)（Díaz, Gayoso, Cimminio, Pérez；Universidad Politécnica de Madrid；2026-08-31 提交）*

### 3.1 论文的问题意识：productivity paradox

个体生产力上升、团队吞吐/review 能力/稳定性下降。证据链全部引自工业报告：Faros AI（10,000 开发者/1,255 团队：合并 PR +98%，但 review 时间 +91%、人均缺陷 +9%）、DORA 2024→2025（2025 的总结句："AI 不修复团队，只放大既有特征"）、METR RCT（老手在自己 repo 慢了 19% 却自以为快 20%）、GitClear（2020–2024 重构占比 25%→<10%，重复代码块 ×8）。理论化工具是 **Amdahl 定律套 SDLC**：只加速代码生产、review/验证/集成仍按原容量，上游创造的价值被下游瓶颈吃掉。

### 3.2 harness 二分框架

论文把 practitioner 文献里的 harness（"Agent = Model + Harness"，引 Böckeler & Fowler 2026、LangChain 2026）**从模型级扩展到团队级**，正式二分：

- **Technical harness（围着 agent）**：让单个 agent 的能力变成可靠产出的一切技术机制——上下文工程、工具、验证脚本、可观测性、并行隔离等。
- **Methodological harness（围着团队）**：让多个 agent × 多个人变成可治理团队的一切方法机制——规范、咨询结构、验收证据、自主度分级。

操作化为 **8 个 harness 机制**（第 5 节，每个带 worked example）：①context engineering；②persistent shared knowledge（repo 作系统记录）；③executable specifications；④N-version 心智 + 并行 agent（**用 worktree 不用共享分支**）；⑤normative specifications；⑥structured consultation；⑦evidence-backed acceptance；⑧graduated autonomy。前两个偏 technical，后几个本质是 methodological——注意 **③⑤ 两个机制就是"spec"在 harness 内部的两个合法座位**（见第 5 节）。

### 3.3 它对 SDD 的重述与保留

论文不是反 SDD 的，恰恰相反：**它把 SDD 学术化为"ASE 的使能学科"**——

- spec 是人机协作的 **contract substrate**：vibe coding 溶解了三个合约（accountability、verifiability、transferability），SDD 以 spec 为中心形态把它们重建：accountability 变成"对 spec 的合约责任"，verification 从"从 diff 反推意图"变成"审计证据"，onboarding 从"读代码猜"变成"读 spec"。
- 五种人机交互模式重新定义人的角色：briefing、consultation、review、norm encoding、orchestration。
- **方法论的诚实**值得全录：论文明确声明依据主要是 gray literature（实践报告、演讲、工具文档），因为"两个核心构念（团队级 SDD、harness）尚无同行评审研究定义、划界或测度过"；自我定位是"走向学术-工业共识的第一步，不是已验证的理论"。这使它比一般"论文背书"弱一级——引用时应作为**概念框架的先行者**而非实证结论。
- 论文自列的五大风险恰好是第 4 节的成本框架的学术版：talent bifurcation（技能分化）、cultural fracture（文化断裂）、**cost spiral**（成本螺旋）、specification drift（spec 漂移）、platform lock-in（平台锁定）。

---

## 4. 反面与成本：harness 建设的真实代价

### 4.1 平台工程投入的量级

- **OpenAI 样本的隐含门槛**：per-worktree 临时可观测性栈（Vector + Victoria 三件套 + LogQL/PromQL/TraceQL）、CDP 接入、自定义 linter 族、CI 知识库校验、cleanup agent 调度——评估卡的原话是"some patterns require significant investment to replicate"、"assumes infrastructure access not universally available"。3 人 5 个月做出 1M 行的另一面是：**这 3 人的全部时间都花在建设 harness 上，一行产品代码没写**。"no manual code"不是道德律令而是实验的 forcing function——消化稿明确警告不要照抄这一条。
- **厂商激励偏差**：这是 OpenAI 讲的关于 Codex 的成功故事，"unusually concrete and includes caveats, but it is still OpenAI telling a success story"。1500 PR 的质量无独立验证；PR 数/行数本身被消化稿列为**不应作为度量**的虚荣指标（应量：issue→validated PR 时长、每接受 PR 的人工分钟、返工率、merge 后 bug 率、cleanup PR 量、架构 lint 违规趋势、每接受变更 token 成本）。
- **量级参照**：个人级入口约 $200/月（Codex Pro 20x / Claude Max 20x）只买到模型与产品面；"Product subscriptions buy access to models and surfaces. They do not buy the harness." 团队级的真实成本在 observability/CI/linter/cleanup 基建，属典型平台工程预算，无公开定价可比，只能按自建组件数估计。

### 4.2 过度建设的信号

消化稿的"knowledge base smells"清单可直接用作体检表：AGENTS.md 长成手册；docs 里写"问团队"；产品决策只在 ticket 里；生成文档无新鲜度检查；active plan 无状态字段；架构文档与 lint 不挂钩；同一规则在 review 评论里反复出现（→该升格为 lint/doc 了）。另一侧信号是**收益侧的**："如果 PR 数上升而 cleanup 和 bug 上升更快，harness 在生产债务"；cleanup agent 制造 churn 或掩盖更深层设计问题，被列为 open unknown。

### 4.3 小团队：一个可核查的模仿样本（半成功案例）

[worldmonitor 的 harness-engineering-roadmap.md](https://github.com/koala73/worldmonitor/blob/main/docs/harness-engineering-roadmap.md)（2026-03-14）是小团队照 OpenAI 文章自评的公开记录：7 支柱自评，**当时就绪度 ~25%**——强项在纯文档与 lint（P1 支柱 7/10、P2 6/10），弱项恰在平台投入最重的三块（agent 可观测性 2/10、agent-to-agent review 0/10、自愈 GC 0/10）。它的执行顺序本身就证明了正确的小团队路径：**P0 lint/测试进 CI → P1 可观测性 → P2 review loop → P3 自愈 → P4 全自主**，每级都以前一级为安全网（"self-merge pipeline requires P0–P2 as safety net"）。反面教训亦有：进度日志显示一天内完成的多是 lint 类快赢，平台级支柱（可观测性、自愈）数周后仍停留在 P1/P3 待办——**投入梯度与 OpenAI 原文的重要性排序相反，是模仿者最普遍的失真形态**。未找到公开的"全套照搬后失败"案例记录；arXiv 论文也把 organizational adoption pathways 列为 RA4 未来工作——这个空缺本身就是证据：团队级路线尚无成熟轨迹可抄。

### 4.4 场景边界

探索期项目过度设计（底稿已判，维持）；OpenAI 自认 brownfield 未验证；"修复便宜等待昂贵"的 merge 哲学在受监管数据、金融动作、难回滚迁移场景必须反转（消化稿给出风险×merge 姿态矩阵：低风险 agent review+验证即可，中风险定向测试+人/高级 agent review，高风险 auth/billing/破坏性变更必须人审+回滚计划+生产证据）。

---

## 5. 与 SDD 的组合方案：spec 在 harness 里的最佳位置

### 5.1 spec 类文件在 OpenAI 三目录中的角色

OpenAI 体系里，"spec"没有消失，而是被**按生命周期拆位**：`product-specs/` 是产品行为的语义真源（最接近 SDD 的 feature spec），`design-docs/` 承载"为什么"（SDD 的 design doc），`exec-plans/` 承载"怎么干+干到哪"（SDD 的 plan）。与经典 SDD 的关键差别有三：

1. **可发现性结构**：spec 不再是自由文档，而是挂在 ~100 行 AGENTS.md 路由之下、有 index、有 owner、有保鲜期的知识库节点——"写好 spec"不够，必须"agent 找得到、读得对、信得过（新鲜度可验证）"。
2. **漂移有机器管**：spec 与代码行为的漂移由同-PR 更新规则 + doc linter + doc-gardening agent 三层兜底，不再靠人的自觉。这正是底稿指出的"spec 漂移是沉默的"缺口在该派内的解法。
3. **spec 不是唯一合约**：一部分原属 spec 的约束被**下沉为 lint/结构测试**（架构规则、taste），一部分**上浮为验收证据**（可观测性产物、测试输出）。spec 保留了"意图与为什么"，机器约束接管了"可机械判定的部分"——arXiv 论文的 ③executable specifications 与 ⑤normative specifications 正是这两个下沉/保留座位的学名。

### 5.2 已有 SDD 实践团队的渐进 harness 化路径

按 worldmonitor 验证过的 P0→P4 梯度，把 SDD 工件当作第一批发酵底物：

- **P0（零平台投入，两周级）**：spec 目录原样迁入 `docs/` 三段结构；AGENTS.md 砍成 ~100 行路由；`make validate`（测试+lint）成为 handoff 硬命令。SDD 工件的位置变化：spec 从"方法论中心"变为"知识库节点"，**格式与内容不用改**。
- **P1**：把 spec 里可机械判定的条款逐条抽成 lint/结构测试（抽一条，spec 瘦一条）；加 doc 链接/新鲜度 linter；生成类文档加 CI 新鲜度检查。判据：review 评论里第二次出现的规则就升级为 lint/doc。
- **P2**：per-worktree 可启动 + 最小运行时证据（截图/健康端点）；agent review 以 advisory 起步、分角色（正确性/架构/安全）、强制 findings 分类与 author pushback 权利（防 review 噪声死循环）。
- **P3**：doc-gardening / cleanup agent 上线，开 fix-up PR；tech-debt-tracker 接管漂移债。
- **P4**：低风险类目自 merge（必须有 P0–P2 安全网 + 高风险类目保留人审的 merge 姿态矩阵）。

**判断收敛点的口径**：harness 是真的，当它改变了任务完成的方式（新 agent 能沿 AGENTS.md 找到正确文档、挂掉的 validate 会让 agent 自修、gardening PR 真的有用），而不是"我们有了这些文档"。对 SDD 团队，终点形态即底稿那句话的落地：**spec 从方法论本体降格为 harness 中被持续校验的可替换组件**——但它通常恰恰是最后一个该被替换的组件，因为它承载着 lint 和测试都承载不了的"为什么"。

---

## 6. 遗留开放问题

1. OpenAI 全部数字（1500 PR/1M 行/3.5 PR/人/天）仍是一手自述，无独立验证——本次观测亦无法直接回源原文（403），依赖两个独立消化稿交叉一致。
2. 全 agent 生成系统的多年架构一致性：OpenAI 自认不知道，是全派最大未决风险。
3. 团队级采纳路径（arXiv RA4）：尚无成熟轨迹，worldmonitor 是罕见的公开自评样本但只走到 ~25%。
4. cleanup/gardening agent 的净质量收益（churn vs 修复）无量化研究。
5. Hashimoto 模型是个人向的；个人 harness（AGENTS.md+脚本）与团队 harness（observability+review loop+cleanup）之间仍差一个数量级的基建，中间形态（5–20 人团队）的公开案例在观测日仍未出现。
