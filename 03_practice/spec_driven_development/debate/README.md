# SDD 评判综合（正反对冲，按影响力加权）

> **元数据**
>
> ```yaml
> source: 本目录六份调研文件
> accessed_at: 2026-09-20
> 时间纪律: 2026 年（越近越重）为准；2025 仅背景；每条评判的日期/URL/权重回溯各分文件
> ```
>
> 本文件是 debate/ 的唯一综合结论层；细节与引用全在六份分文件里，此处不复制。

## 0. 分文件导航

| 文件 | 内容 | 特点 |
|---|---|---|
| [signals-2026h2.md](signals-2026h2.md) | 2026.6–9 最新信号全景（25+ 条） | **时间权重最高，矛盾信号以此裁决** |
| [authoritative-verdicts.md](authoritative-verdicts.md) | TW Radar Vol.34 / InfoQ / arXiv | 定级来自条目页 JSON，非猜测 |
| [critiques.md](critiques.md) | 批判汇编（按权重聚类 5 类） | 2026 批判重心在 spec 漂移与成本 |
| [endorsements-and-experiences.md](endorsements-and-experiences.md) | 正面/经验池（厂商降权） | 最强独立证据 = FIXER × Scrum |
| [team-practices.md](team-practices.md) | 团队协作/工程控制/迭代机制 | 最贴合落地视角，含活样本 |
| [chinese-community-verdicts.md](chinese-community-verdicts.md) | 中文社区专项 | 结构性偏差已标注 |

## 1. 矛盾裁决（先校正事实，再谈观点）

1. **"spec-kit 停更"不成立**：批判面曾引它作退潮锚点，但 09-20 实测周级发版（v1.0.8，09-17）+ 1.0 后每 2-4 天一版。退潮的是**话语**，不是头部工程投入。
2. **Tessl 定性修正**：tools/tessl.md 的"资本上升"口径已过时——2026H2 信号显示其 3 月起公开停摆、弃用 spec 定位改称 "Agent Enablement Platform"。以 signals-2026h2.md 为准。
3. **Böckeler 名字勘误**：martinfowler 批评作者为 Birgitta Böckeler（非 Jan）；marmelab 原文 URL 含 `-waterfall-` 段。

## 2. 加权后的六点综合判断

1. **概念层：TW 官方已不再收录 SDD 主条目（二轮补遗修正）**。Vol.34（2026-04）官方条目页明文 "NOT ON THE CURRENT EDITION"，timeline 仅剩 Vol.33（2025-11）一格 Assess——即 SDD 作为独立概念**已跌出当前版 Radar**；最新官方定级仍是 Vol.33 Assess（判词全文已落盘，含 "handcrafting detailed rules for AI ultimately doesn't scale"）。工具层：OpenSpec 获官方直读确认于 Vol.34 新增独立条目（Assess）；Spec Kit 的独立条目页未定位到，Vol.33 正文点名（Kiro/spec-kit/Tessl）不等同于独立条目，引用需区分。这与"话语退潮"（下条）同向：行业对 SDD 作为品类已降温，对具体工具仍在逐个体检。
2. **话语退潮、工件固化**（2026H2 最重要信号）：公众讨论冷却（"plan mode 就够了"、SDD=新瀑布类比流通），但 GitHub/Google/AWS 同时把 spec/plan 工件制度化进 agent 平台。SDD 作为独立品类的高光已过，作为 agent 工作流默认工件层正在被大厂固化。
3. **批判重心已迁移**：2025 的"waterfall 复辟/虚假控制感"（高权重但已成背景）→ 2026 转向**spec 漂移与维护留白（spec 债）**——团队向最硬证据是 spec-kit #1191（115👍，spec 无法随迭代保持同步）+ dbreunig 旗手自我推翻复盘（2026-03）；可复现性最强的是**成本经济学**（spec-kit #1401 实测 context tax 18.6k tokens）。
4. **正面证据的天花板很明确**：迄今**没有任何独立量化生产率数据**，量化收益全部来自厂商或个人自述。最强独立团队证据是 FIXER（Spec Kit × Scrum，2026-04~08）：返工锐减、吞吐上升，但诚实报告估点失灵与 onboarding 爬坡。社区已收敛的健康形态共识：**小步 spec + 可执行验证 + 人守冲突裁决**。
5. **团队工程控制的现状**：确定性 CI 校验**只有 OpenSpec 原生提供**（`openspec validate --strict`，PostHog 真实 workflow 在用）；Spec Kit/Kiro/BMAD 的门禁是 LLM 分析或产品内 review 屏。活样本：PostHog/sdk-specs（spec 与实现分仓的跨团队契约）、Spec Kit 官方 repo 自己的 constitution.md（规则文件的 SemVer 治理）。
6. **中文社区的结构性偏差**：厂号渠道以正面实操教程为主，尖锐批判多系译文引入；特有贡献是"**Spec 是需求层的 Harness**"合流视角（2026-04，权重高）与任务三级分流共识（不是所有任务都需要完整 SDD 仪式）。

## 3. 对"团队协作 + 工程控制 + 支持迭代"的落点结论

- **成败变量是治理纪律，不是工具选择**：2026 年权威侧（InfoQ 企业规模化篇、arXiv 2609.00252"团队规模 Agentic SE 的 harness 治理学科"）与社区复盘同向指向这一点。
- **迭代友好度排序（brownfield + 多人）**：OpenSpec delta+archive（delta 机器可校验、change 即评审单元）> Spec Kit 2026 三种持久化模型 + converge（一致性靠 LLM analyze）> Kiro steering > BMAD。
- **推荐组合（5–20 人，依据 team-practices.md）**：OpenSpec 骨架 + PostHog 式 CI 门禁 + 双 PR 评审流（PR1 锁 spec、PR2 轻量查表）+ per-capability 归档；架构治理叠加 Spec Kit 式 constitution；任务三级分流，Lite spec 默认 + 豁免通道。
- **已知失败模式（对策在 team-practices.md §4）**：spec 成死文档→CI 校验；评审带宽成第一瓶颈→两层评审；流程形式化→Lite 默认；实现者私改 spec→PR1 锁定。
- **证据缺口（引用时须声明）**：>6 人规模无比 Multi-Engineer 更大的一手案例；Kiro/BMAD 无公开多人 spec 目录实例；独立量化生产率数据为零。

## 4. 局限

- Reddit 抓取 403（r/ExperiencedDevs 等缺席）；知乎 Kiro 高赞文 403 仅存目；InfoQ 企业篇正文截断未核实——均在分文件标注。
- ~~TW Vol.34 主条目维持 Assess 系高置信推断~~ **已修正（二轮补遗）**：官方直读 "NOT ON THE CURRENT EDITION"，Vol.34 未收录 SDD 主条目；详见 §2.1 与 authoritative-verdicts.md 补遗节。
- Gartner/Forrester 公开渠道未检出。
