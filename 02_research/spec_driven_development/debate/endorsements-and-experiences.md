# SDD 正面评判、成功案例与经验报告（endorsements & experiences）

```yaml
topic: Spec-Driven Development (SDD) — 正面证据与经验报告
accessed_at: 2026-09-20
author: research subagent (session-f37ceeb1 委派)
scope: 厂商官方叙事 / 独立开发者与团队经验报告 / 社区正面辩护 / Jesse Vincent (obra) Superpowers
bias_note: 本文件只收正面或中性偏正面的材料，作为辩论的正方证据池；反方证据在同级 critique 文件中，评估节会交叉引用
weighting_rule: 依补正指令——厂商自述（AWS/GitHub/Tessl 官方博客）一律降权，仅作参考；主证据为独立团队复盘、知名从业者公开经验、高热社区讨论
sort: 按日期倒序
```

---

## 一、条目清单（按时间倒序）

### 2026

**2026-09-18 | [Kiro 官方博客：How we built a software factory with Kiro Crew to merge 1000 PRs in a week](https://kiro.dev/blog/software-factory-1000-prs/) | 厂商自述（员工工程复盘），利益相关 | 热度：官方旗舰案例 | 影响力权重：低（厂商，但有可复核开源仓库）**
- 团队实践。3 名全职工程师 + 约 500 名社区贡献者，一周合并 1000 个 PR（日均 120+，全部过 CI + review）。
- 可复用细节：提出「并发 session 五阶段阶梯」（1 个手工 session → 多 tab → memory/cron/workflow → agent 流水线 → Crew Mode 编排 agent）。关键工程手段：repo 内一个所有 session 都读的 conventions/纠正文件（即 steering/spec 的最小形态）是「最划算的一步」；流水线用「issue label 当队列」，一种 session 类型认领一种 label；治理四件套——显式持久的 agent 协作记录、按项目隔离的 memory、host 级权限（不是 prompt 里求）、agent 不可篡改的审计日志——第一天就上而不是规模化后补。
- 坑：50+ session 时单个人做「拆解/派发/巡逻/验收/排序」五件杂务成为瓶颈；单个协调 agent 也会丢上下文，需要多角色 agent 分工。注意：该案例更多是「多 agent 并行」证据，spec 的角色体现在任务种子与 feature specifications（仓库公开架构文档 + specs，可独立复核）。

**2026-08-21（更新至 8 月系列）| [FIXER（日本云集成商）：Spec Kit を用いたチーム開発（1）スクラム開発での実用開始](https://ascii.jp/elem/000/004/427/4427352/)（原文 [cloud.config Tech Blog 2026-05-21](https://tech-blog.cloud-config.jp/2026-05-21-spec-kit-develop-1)，[part 0 导入动机 2026-04-09](https://tech-blog.cloud-config.jp/2026-04-09-spec-kit-develop-0)，[part 2 实装者视角](https://ascii.jp/elem/000/004/427/4427374/)） | 独立团队复盘（真实 scrum 团队，非厂商）| 热度：ASCII.jp 转载推荐位 | 影响力权重：高（本清单最像"普通团队"的第一手证据）**
- 团队实践。真实的多人 Scrum 团队（Scrum Master + 开发者 + PMO + 客户），把 GitHub Spec Kit 嵌入正式 sprint 流程，每人并行 2+ 个 PBI。
- 流程细节（可复用）：Specify→Clarify→Plan→Tasks→Implement 四阶段；每个 PBI 走完到 Clarify 就提 PR 评审，**等评审期间开发者切到下一个 PBI 的 Specify**，形成流水线；Clarify 可反复运行并按安全/性能等领域定向深挖。
- 量化/定性收益：①「做什么」在实现前于开发者/评审者/PMO 三方对齐，返工显著减少；② AI 主动追问模糊点，实施后才发现「考虑遗漏」的案例锐减——把 AI 当「规格的壁打（sparring）对手」；③ 总体交付更快，单 sprint 可消化的 PBI 数量上升（虽然 Specify 更花时间）。
- 团队纪律两条：开发者答 AI 提问时「不带臆测」——答不了的必须问 PMO/客户；向客户确认时「带假设去确认」（给出 A/B 方案 + 技术理由），几乎不产生返工。
- 坑（同样是知识传承证据）：① PBI 估点变难（非实现阶段耗时无历史数据），对策是「不过度拆分 PBI + sprint 内设 Specify 截止的中间里程碑」；② **onboarding 成本远超预期**——学的不是工具而是「以 Spec Kit 为前提的开发方法」，第一个 sprint velocity 低于预期，每个新成员都要同样的爬坡期。
- 系列第 2 篇补实装者视角：spec 文档先行让代码评审争论从「你想做什么」转向「实现是否符合 spec」，评审更聚焦。

**2026-07-16 | [Kiro 官方博客：One year of Kiro（一周年总结）](https://kiro.dev/blog/one-year/) | 厂商自述，利益相关（用户数与客户故事全部为厂商口径）| 热度：官方周年文 | 影响力权重：低，但客户名单可逐一外查**
- 数据点（均为自述，未独立审计）：上线 5 天 10 万开发者试用、10 月翻倍；开发者数「逐季翻倍」；社区创建 1.5 万+ powers、官方 100+ 精选 powers。
- 客户案例（厂商转述）：Siemens 用 Kiro spec 工作流以 1 名架构师 2 周交付传统需 3-4 个月多人团队的生产级 AWS serverless guardrail 服务；SmugMug/Flickr「根本改变了开发方式」；Appian 借此建立 AI-DLC 心智、POC 缩到小时级；LMU 两人云团队更新 500 个 Lambda 函数，2 个月工作量变半天；ALO Tech 原型迭代周期缩短 30-40%；Trailflow 复杂物流功能从数周到数天。
- 新人上手角度（厂商转述）：ASU 黑客松参与者反馈「spec-first 让流程自然而非官僚化；中途 pivot 时 spec 吸收了变更而没有打断一切」——spec 作为新人/临时团队的共同锚点。

**2026-06-05 | [Gautam Khorana：How I actually use obra/superpowers（6 个月实践，updated 2026-07-04）](https://gautamkhorana.com/blog/claude-code-superpowers-how-i-actually-use-it/) | 独立个人经验（咨询公司 COO，多客户环境），利益弱相关（有获客动机）| 热度：个人博客，被多处引用 | 影响力权重：中高（独立、细节密、含失败面）**
- 个人实践为主、团队为辅（作者称在 Seahawk Media 全项目使用，并提出团队嵌入咨询——团队部分属自述而非复盘）。
- 方法论细节：Superpowers 七阶段——brainstorming → git worktree 隔离 → writing-plans（拆成 2-5 分钟粒度任务）→ subagent-driven-development（每任务新 subagent + 两阶段评审）→ 强制 TDD → severity-based code review（critical 阻塞）→ 分支收尾（结构化 merge/PR）。框架按任务复杂度自动跳过阶段（typo 修复不做 TDD）。
- 量化效果：WordPress Stack Advisor 工具 8 小时 session 时间完成、TDD 抓住 2 个正则 bug；25 页 deck 从一天缩到 2 小时；多 post 内容集群一天交付。约 40% 用法是非编码任务。
- 坑与边界（诚实面）：琐碎修改、纯探索、紧急线上排障时 plan-first 反射是错的；**团队里只有一部分人装 Superpowers 时，工件（plan 文件、worktree 分支、结构化 commit）反而干扰协作——「要么全员用，要么没人用」**。
- 注：文中「接近 18 万 GitHub stars」等数字未在 obra 仓库核实，引用需降权。

**2026-05-28 | [sermakarevich：Show HN — CCW，用 SDD 方法生成 Claude Code workflow 插件](https://news.ycombinator.com/item?id=48306730)（含自述：自 2026-02 起所有中型以上任务都用 SDD，[前身 sddw Show HN 2026-05-22](https://news.ycombinator.com/item?id=48231575)）| 独立个人经验 + 跨团队传播证据 | 热度：两个 Show HN 共约 25 分 20+ 评论 | 影响力权重：中（有跨团队外部反馈细节）**
- 个人实践、正在走向团队化。核心做法：两维分解（先多步生成 spec：requirements→code analysis→design，再拆子任务逐个实现）；每步之后 /clear 清上下文（控成本 + 保焦点）；spec 落盘持久化；spec 逐层交付以尽早发现 agent 理解偏差。
- 团队传播证据：该工作流已在包括 Google Poland 在内的几家公司做了分享，多家团队反馈想按自己项目规模改造，甚至迁移到非编码任务（市场研究）——说明 SDD 工作流的**组织适配需求**是普遍的。
- 每步产出 spec 工件、后续步骤可感知先前工件——这是「spec 作为团队接口」的最小实现。

**2026-05-28 | [Marc Brooker（AWS 首席工程师，个人博客）：Spec Driven Development isn't Waterfall](https://brooker.co.za/blog/2026/04/09/waterfall-vs-spec.html) | 知名从业者（KOL）公开辩护；利益半相关（AWS 造 Kiro，但博客声明个人观点）| 热度：HN 6 分 + SE Radio/Real Python 播客联动 | 影响力权重：中高（论证质量高，业界广泛引用）**
- 核心主张：SDD 不是设计前置（up-front），而是设计「上提」（pull designs up）——spec 是版本化的、活的工件，实现从 spec 流出；**被迭代的是 spec 而不是实现**，迭代环路与敏捷相同，AI 只是把它加速。
- 论证亮点：承认软件需求天然「不完整、互相冲突、动态变化」——正因如此人类要守住 spec 外环，专责裁决冲突与权衡；最大收益来自「spec 让 agent 可以长时间自主运行」，人退出紧回路。spec 形式可以混合自由文本/RFC2119/EARS/Lean/TLA+，按需混搭形式度。
- 配套材料：SE Radio 第 710 期播客（2026-03）与 Real Python Podcast #277 系统性布道——这是厂商外少见的由一线资深工程师承载的正面理论化。

**2026-04-28 | [superluminar：Spec-Driven Development: Everything Old Is New Again](https://superluminar.io/2026/04/28/spec-driven-development-everything-old-is-new-again/) | 独立咨询公司中性偏正面评论 | 热度：HN 4 分 | 影响力权重：低-中**
- 中性复盘：把 SDD 放回「规格先行」的软件工程史（形式化方法、契约式设计）脉络，结论是 AI 让「写清楚你要什么」从成本中心变成杠杆——「旧学问的新杠杆」，非营销腔，可作正方的历史定位引用。

**2026-04-14 | [VentureBeat：Agentic coding at enterprise scale demands spec-driven development](https://venturebeat.com/orchestration/agentic-coding-at-enterprise-scale-demands-spec-driven-development) | 科技媒体评论（二手，采访多位从业者）| 热度：HN 4 分 | 影响力权重：中（媒体综述，非一手）**
- 主张：企业级多 agent 并行没有 spec 就不可治理——spec 是并发 agent 之间的「合并协议」。可作正方「规模化必要性」论据，但需注意标题即结论的媒体化倾向。

**2026-04-09 | [dbreunig：Learnings from a No-Code Lib: Keep the Spec Driven Development Triangle in Sync](https://www.dbreunig.com/2026/03/04/the-spec-driven-development-triangle.html) | 独立个人经验（知名科技博主）| 热度：HN 4 分 3 评论 | 影响力权重：中低**
- 经验教训型：spec/实现/验证三角必须同步漂移，任一角落后于其他两个，SDD 就退化成新的文档债——正面案例的反面教训，用于校准正方论述的边界。

**2026-02-28 | [Verified Spec-Driven Development (VSDD) — gist + HN 讨论](https://gist.github.com/dollspace-gay/d8d3bc3ecf4188df049d7a4726bb2a00)（[HN：211 分 / 118 评论](https://news.ycombinator.com/item?id=47197595)）| 社区建设性讨论（高热）| 热度：本清单社区热度最高 | 影响力权重：高（社区共识温度计）**
- 主张：SDD 要成立，spec 必须可验证（verified）——把可执行断言/测试作为 spec 的一部分，让「spec 合规」机器可查而非口头承诺。后续 dev.to [VSDD 方法论文章](https://dev.to/midastools/vsdd-the-ai-coding-methodology-actually-worth-stealing-35ah)将其工程化推广。
- 讨论中有大量「哪种形态的 SDD 对」的建设性共识：大而全的前置 spec 被普遍否定，**「小步 spec + 可执行验证 + 人守冲突裁决」**的形态获得多数正面认同——这是对正方最有利的社区形态共识。

**2026-02-10 | [deontologician：Spec-driven development doesn't work if you're too confused to write the spec](https://publish.obsidian.md/deontologician/Posts/Spec-driven+development+doesn%27t+work+if+you%27re+too+confused+to+write+the+spec)（[HN 32 分 7 评论](https://news.ycombinator.com/item?id=46955747)）| 独立个人经验，半正面 | 热度：HN 32 分 | 影响力权重：中**
- 表面是批评，实为正面辩护的精确化：SDD 的失败几乎都发生在「你自己还没想清楚」时；此时写 spec 本身就是强迫澄清思考的诊断工具。评论区形成「spec 的价值在写作过程而非文档」的正面共识。引用时应说明其条件限定。

**2026-01-06 | [Spec Kitty：Kanban / Spec Driven Development（开源项目）](https://github.com/Priivacy-ai/spec-kitty) | 社区工具化实践 | 热度：HN 5 分，项目持续活跃 | 影响力权重：低**
- 证据点：社区把 Spec Kit 改造成带 Kanban 的多人任务板，说明真实存在「多人围绕 spec 工件协作调度」的需求与实践，补 Spec Kit 原生单人倾向的短板。

### 2025（背景压缩）

**2025-11-15 | [Marmelab：Spec-Driven Development: The Waterfall Strikes Back](https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html)（[HN 225 分 191 评论](https://news.ycombinator.com/item?id=45935763)）| 独立代理商评论，**总体偏批判** | 热度：高 | 影响力权重：高（反方旗舰，此处仅作背景）**
- 不收为正面证据；但评论区（191 条）是「哪种形态对」建设性讨论的重要样本：多数评论区分了「写 spec 给 AI 当约束」与「瀑布式前置设计」，前者被广泛接受。正面引用时可用「HN 225 分帖的评论区共识：反对的是文档仪式，不是规格先行」。

**2025-10-16 | [Birgitta Böckeler（Thoughtworks）：Understanding Spec-Driven-Development: Kiro, Spec-Kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)（[HN 128 分](https://news.ycombinator.com/item?id=45610996)）| 独立分析师中性评述 | 热度：高 | 影响力权重：高（martinfowler.com 站点背书）**
- 对三家工具的中立解剖：识别出 SDD 的四个变体形态（spec 即 prompt / spec 即计划 / spec 即契约 / spec 即规格），并指出「spec 作为团队沟通与持久知识工件」是其中最有生命力的用途。中性但客观上为正方提供了概念地图。另：GitHub Spec Kit 已进入 [Thoughtworks Technology Radar](https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit)——独立机构评估（评级的具体档位引用前需回源确认）。

**2025-10-10 | [Simon Willison：Superpowers（转述 obra 的 October 2025 工作流自述）](https://simonwillison.net/2025/Oct/10/superpowers/) | 知名从业者（KOL）背书 + obra 自述 | 热度：高（Willison 博客广泛传播）| 影响力权重：高**
- Willison 转述并正面评价 Jesse Vincent 的 Superpowers：brainstorm→plan→分任务→子 agent 执行→TDD→review 的技能框架，「是 codify 高级工程师工作习惯的认真尝试」。这是 Superpowers 获得独立 KOL 背书的起点节点。

**2025-09-02 | [GitHub Blog：Spec-driven development with AI（Spec Kit 发布文）](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/) | 厂商自述（GitHub 官方博客），利益相关 | 热度：仓库 4 万+ stars（2026-09 观测）| 影响力权重：低（营销），但其四阶段模板被独立团队（如 FIXER）实际采用是外部佐证**
- 主张：把 intent→spec→plan→tasks→implement 固化为开源工具链，声称可解决「vibe coding 在大型代码库不可扩展」的问题。开源、可复核是其超出纯营销的部分。

**2025-07+ | obra（Jesse Vincent）Superpowers 自述系列（blog.plaintexticers / GitHub [obra/superpowers](https://github.com/obra/superpowers) README）| 独立个人自述（作者本人，非厂商）| 热度：项目成为 Claude Code 官方插件市场头部，衍生第三方教程大量出现 | 影响力权重：中高（一手自述 + 大规模第三方采用痕迹）**
- Vincent 自述其全程用 Superpowers/FOAM 类流程重建自己的开发工作：强制 brainstorm 产出设计文档、写 plan 文件、TDD 红绿重构、severity-based 评审；核心论点「agent 是结构性地乐观的，方法论层才能拦住它的乐观」。作为项目作者属自述，但 2026 年第三方独立复盘（本文 Gautam Khorana 条、DataCamp 教程、腾讯云社区文章）构成外部验证链。

---

## 二、正面观点聚类

1. **「Spec 让 AI 可治理」**（规模化论证）：多 agent 并行、长时自主运行、企业审计/权限/合并，都需要显式 spec 作为协调与治理界面（Brooker、Kiro Crew、VentureBeat、HN 共识）。
2. **「Spec 即对齐协议」**（团队协作论证）：spec 在开发者/评审者/PMO/客户之间前置对齐「做什么」，减少返工与臆测（FIXER 系列——最纯的团队证据）；spec 进 PR 评审后，评审焦点从意图转向合规。
3. **「Spec 即思考诊断」**（个体论证）：写 spec 的过程强迫澄清需求；AI 在 Clarify 阶段主动追问补盲区，充当「规格的陪练」（FIXER、deontologician）。
4. **「方法论层拦截 agent 的乐观」**（工程纪律论证）：brainstorm→plan→TDD→review 的强制阶段化是 Superpowers 一脉的核心主张（obra、Willison、Khorana）。
5. **「形态共识」**：几乎所有正面材料共同否定的形态是「大而全前置瀑布 spec」；获得正面认可的形态是「小步迭代 spec + 可执行验证（VSDD）+ 人守冲突裁决 + spec 随代码同漂移」。

## 三、正面证据的强度评估

| 证据层级 | 材料 | 强度判断 |
|---|---|---|
| 厂商营销（**降权，仅参考**） | Kiro 一周年（10 万用户、Siemens/SmugMug/Appian 案例）、GitHub Blog Spec Kit 发布文、Tessl 官方主张 | 全部为厂商口径，无独立审计；客户故事均由厂商转述且客户有商务关系。数字（5 天 10 万、"开发者逐季翻倍"）**不可直接引用为事实**。唯一例外：Kiro Crew 的 1000 PR 案例有公开开源仓库可部分复核 |
| 独立分析师/KOL | Böckeler（martinfowler.com）、Brooker 个人博客、Willison、Thoughtworks Radar | 论证质量高、可独立引用，但 Brooker 的 AWS 雇佣关系要求注明利益半相关；Willison/obra 条为转述+自述叠加 |
| **独立团队复盘（最强）** | FIXER Spec Kit × Scrum 系列（2026-04/05/08）、sermakarevich 跨公司分享、Kiro Crew 工程复盘 | FIXER 系列是本池中唯一的「普通多人团队 + 正式 sprint + 具体流程 + 诚实坑清单」，且同时给出负面上（估点失灵、onboarding 成本大）——正反并存使其可信度最高 |
| 高热社区讨论 | VSDD（211 分）、Waterfall Strikes Back 评论区（225 分）| 反映共识温度而非实证；适合引「哪种 SDD 形态被接受」，不适合引效果数字 |

**总体判断**：SDD 的正面证据呈「厂商叙事先行、独立经验滞后且更精细」的结构。厂商材料提供的是采用规模信号与可能性论证；可独立验证的部分集中在三点——① spec 前置对齐确实减少返工（FIXER，定性）；② 多 agent 规模化治理离不开显式 spec（逻辑强、实证弱）；③ 2026 年社区已收敛出「小步+可验证+人守冲突」的健康形态。**尚不存在的证据**：任何对生产率提升的独立量化测量（现有数字全部来自厂商或个人自述）、spec 进 code review/CI 门禁的多人团队长期复盘。引用时的诚实姿势是：用厂商材料讲「正在发生」，用 FIXER/Brooker/VSDD 讲「什么形态有效」，并明示量化收益暂无第三方验证。

### 补充切面：SDD 对新人上手 / 知识传承的证据（2026）

- **正面（厂商转述，降权）**：Kiro 一周年文中 ASU 黑客松反馈——「spec-first 让新人觉得自然而非官僚；中途 pivot 时 spec 吸收了变更」；LMU 的 Rob Larmon 因 Kiro 在校园开工作坊培训新人（厂商转述）。
- **正面（独立，弱）**：sermakarevich 报告多家团队希望把 SDD 工作流适配到自己规模——间接说明 spec 工件被当作可迁移的组织知识。
- **警示（独立，强）**：FIXER 明确报告 onboarding 成本远超预期——新人要学的不是工具而是整套方法，第一个 sprint velocity 下降，每名新成员都要爬坡期。知识传承收益存在，但**不是免费的**：需要把「团队约定沉淀为 spec 模板/steering 文件」才可复利（Kiro Crew 的「repo 内 conventions 文件是最划算一步」与此互证）。
- 综合判断：SDD 的知识传承效果=「spec 工件 + 沉淀纪律」的组合；只有 spec 工件没有沉淀纪律的团队，传承收益为负（爬坡成本）。
