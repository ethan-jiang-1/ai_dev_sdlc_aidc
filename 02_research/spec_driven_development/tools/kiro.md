# Amazon Kiro（AWS 的 spec-driven IDE）深挖

> 元数据
>
> - **source**: kiro.dev 官方文档与博客（一手）、martinfowler.com / ThoughtWorks（独立第三方）、公开媒体转载
> - **accessed_at**: 2026-09
> - **trust_level**: 官网/官方博客内容为厂商自述（一手，但非独立可验证）；Fowler/ThoughtWorks 为独立从业者观察；所有"用户数/案例效果"类数字均属**厂商自述，证据强度弱于开源可验证数据**

## ① 一句话定位

Kiro 是 AWS 内部一个小团队打造的"agentic 开发环境（IDE/CLI/Web/Mobile）"，核心卖点是**首创 spec-driven development 工作流**：把一句 prompt 变成结构化的 requirements → design → tasks 三分文件，再由 AI agent 按任务落地，用"超越 vibe coding"的确定性流程来约束 agent 输出（来源：[kiro.dev/about](https://kiro.dev/about/)，官方自述，观测 2026-09）。

## ② 起源与时间线

- **2025-07-14**：Kiro IDE 以 preview 形式发布（来源：Kiro 官方博客"One year of Kiro"，2026-07-14，作者 Deepak Singh / VP DevEx & Agents——官方一手自述）。
- **2025-11**：Kiro 正式 GA（generally available），同期推出 property-based testing（验证代码是否符合 spec）、checkpointing（回滚 agent 改动）、Kiro CLI 与企业版能力（来源：同上官方博客）。
- 之后陆续推出：remote MCP、全局 steering 文件、Auto agent、并行 agent、GovCloud 可用性、Powers、Web/Mobile 端、Pro Max 档位等（官方博客，观测 2026-09）。
- 组织归属：官方明确"由 AWS 内部一个小而有主见的团队构建和运营"（[kiro.dev/about](https://kiro.dev/about/)）。

## ③ Spec 工作流（核心机制）

**三分文件**（每个功能一个 spec 目录）：

1. **requirements.md** —— 需求列表，每条需求以 User Story（"As a…"）表述 + 验收标准。官方文档采用 **EARS 格式**（Easy Approach to Requirements Syntax，"WHEN/IF…THE SYSTEM SHALL…"）；独立观察者实测中也见到 GIVEN/WHEN/THEN 风格（来源：官方 specs 文档 + [Birgitta Böckeler, martinfowler.com, 2025-10-15](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)，观测 2025-09 使用）。EARS 本身的语法与工程方法属 RE 层职责：完整模式表与教程见本仓库 [`../../requirements_engineering/deep_research_topics/topic-03-ears-tutorial.md`](../../requirements_engineering/deep_research_topics/topic-03-ears-tutorial.md)（指针，不复制）。
2. **design.md** —— 技术设计：组件架构、数据流、数据模型、错误处理、测试策略、迁移策略等章节。
3. **tasks.md** —— 可逐条执行、可回溯到需求编号的任务清单，Kiro UI 为每项任务提供"逐个运行 / 查看变更"的交互。

**Steering（记忆库）**：跨会话的项目级上下文文件，默认生成 product.md / tech.md / structure.md（官方 + Fowler 实测一致）。

**Agent Hooks**：事件触发的后台 agent，如自动更新文档、生成单元测试、性能优化（官方自述）。

**Powers**：可按需加载的能力扩展包（最佳实践 + 上下文 + 工具连接）。官方称上线时约十余家伙伴（Figma、Postman、Stripe、Supabase、Netlify 等），现有 100+ 官方精选 powers、社区创建 15,000+ 个 powers（**厂商自述，2026-07 官方博客，数字无独立验证**）。

**多形态**：IDE（动手写码）、CLI（终端/CI/CD）、Web（自主协作）、Mobile（远程控制台），共享 steering 与模型配置（官方自述）。

## ④ 数据指标（⚠️ 全部为厂商自述，证据强度弱）

| 指标 | 数值 | 观测日期 | 证据强度 |
|---|---|---|---|
| 发布 5 天内试用 IDE 的开发者 | >100,000 | 2026-07 官方博客追述 | 厂商自述，无独立可验证数据 |
| 到 2025-10 用户数 | "翻倍以上"（即 >20 万） | 同上 | 厂商自述，模糊口径 |
| 之后"开发者数量逐季翻倍" | 未给绝对数 | 同上 | 厂商自述 |
| Siemens 案例 | 生产级 serverless guardrail 服务，"传统需 3-4 月多人 → 2 周单架构师" | 同上 | 厂商自述案例 |
| SmugMug/Flickr | "根本性改变开发方式"（无数字） | 同上 | 厂商自述案例 |
| Appian | "数小时出 PoC"（无数字） | 同上 | 厂商自述案例 |
| 社区 powers | 15,000+ | 同上 | 厂商自述 |

**定价与产品线**（官方 pricing 页，2026-09 观测；价格属官方一手、随时可变）：

- Free：$0，50 credits/月，开源权重模型 + Claude Sonnet 4.5
- Pro：$20/人/月，1,000 credits
- Pro+：$40/人/月，2,000 credits
- Pro Max：$100/人/月，5,000 credits
- Power：$200/人/月，10,000 credits；加购 $0.04/credit
- Enterprise：集中计费、SSO、用量分析、安全管控（联系销售）
- 模型：付费可用 Claude Sonnet 5 / Opus 5、开源权重模型、Auto 档；2026-07 官方博客称加入 OpenAI GPT-5.6 系列模型（厂商自述）

> 采信纪律：以上所有效果类数字（用户数、案例提速）均为**厂商自述**，属于一手但利益相关信源，只能作为"厂商宣称"记录，不可当作独立验证事实引用；定价页本身是一手可复核来源。

## ⑤ 采纳与影响力

- 被 [ThoughtWorks（Birgitta Böckeler, 2025-10-15, martinfowler.com 站点）](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)列为 SDD 三大代表工具之一（与 GitHub spec-kit、Tessl 并列），并认为 Kiro 是其中"最轻量"的一个；Kiro 官方也自称"首个把 SDD 带入 AI 编码工具"。
- "spec-driven development" 已进入 [ThoughtWorks Technology Radar](https://www.thoughtworks.com/radar/techniques/spec-driven-development)（作为 technique 条目提名）。
- 社区生态：Ambassadors 计划、Discord、Kiro Labs（GitHub 开源组织）、Kiro for Students（每月 1,000 免费 credits 一年）与 Kiro for Startups（一年 Pro+）计划（官方自述）。
- 衍生影响：催生了大量第三方"SDD 工作流"复刻项目（如社区 spec-kit 类工具生态）。

## ⑥ 趋势判断

- Kiro 把 SDD 从"个人纪律"产品化成**默认工作流 + 配套 UI（逐任务运行/回看变更）+ 商业化（credits 计价）**，代表 AI IDE 从"聊天补全"走向"流程编排"。
- 演进方向明显从"spec-first 一次性工件"向"**spec-anchored / 长期可维护工件** + 企业治理（GovCloud、SSO、用量分析）"扩展，同时用 powers/hooks 生态对冲纯 workflow 的僵硬。
- 多端（IDE/CLI/Web/Mobile）+ 多模型（Anthropic/OpenAI/开源权重）表明 AWS 的策略是做 agent 时代的"入口层"，spec 只是入口的抓手。

## ⑦ 批评与局限（独立信源）

来自 Böckeler 实测（martinfowler.com, 2025-10-15，独立观察）：

- **杀鸡用牛刀**：一个小 bug 被展开成 4 条 user story、16 条验收标准；对多数真实规模的任务，三分文件工作流过重。
- **只适合 spec-first**：实测中未看到需求文档跨任务长期维护（spec-anchored）的机制说明——"spec 写完怎么演化"基本留白。
- **审阅负担转移**：从"审代码"变成"审 markdown"，冗长且重复；作者直言"宁可审代码"。
- **虚假控制感**：模板/checklist 俱全，agent 仍会无视或过度遵循指令（幻觉、重复生成已存在代码）。
- **通用性存疑**：单一 opinionated 工作流难以覆盖不同大小/类型的变更；目标用户（开发者？产品？）不明确。
- 另注：Kiro 为闭源商业产品，其效果宣称（第④节）均无独立基准可比。

## ⑧ 适用场景

- **适合**：从零搭建的新功能/新服务（greenfield）、需要需求-设计-任务留痕的团队协作与企业合规场景、原型到生产级 guardrail 的"结构化提速"、CI/CD 中用 CLI 跑 agent 流程。
- **不适合/慎用**：小 bugfix 与微小改动（工作流开销远超收益，独立实测确认）；深度 brownfield 重构（spec 与存量代码的对齐机制不成熟）；需要高度迭代式、探索式开发的工作。

## ⑨ 来源列表

1. [Kiro 官方 About](https://kiro.dev/about/) —— 定位与团队归属（官方一手，观测 2026-09）
2. [Kiro Docs: Specs](https://kiro.dev/docs/specs/) —— 三分文件工作流（官方一手）
3. [Kiro Pricing](https://kiro.dev/pricing/) —— 档位与定价（官方一手，2026-09 观测）
4. [One year of Kiro（官方博客, 2026-07-14）](https://kiro.dev/blog/one-year/) —— 时间线、用户数、企业案例、powers 生态（厂商自述）
5. [Birgitta Böckeler: Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl（martinfowler.com, 2025-10-15）](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) —— 独立实测与批评
6. [ThoughtWorks Technology Radar: Spec-driven development](https://www.thoughtworks.com/radar/techniques/spec-driven-development) —— 行业雷达提名
