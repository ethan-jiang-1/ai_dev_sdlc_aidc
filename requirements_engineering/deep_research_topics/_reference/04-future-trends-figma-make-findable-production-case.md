# Figma 2026 — Findable Figma Make app-shell production case

- source_url: `https://www.figma.com/customers/how-findable-moved-50-percent-faster-with-figma-make/`
- source_type: `official hosted customer story / case study`
- accessed_at: `2026-04-18`
- related_topic: `04 future-trends (primary), 06 agent-format`
- trust_level: `vendor-hosted customer story`
- tier: `C`
- why_it_matters: Topic 04 当前 residual gap 是 named real production deployment case 或 independently verified production outcome。本文是 Figma 官方客户故事，不是独立验证；但它给出 named customer Findable、明确产品对象 app shell、明确 design-to-code / prototype-to-handoff workflow，并声明最终 app shell 50% faster、90%+ final product code 来自 Figma Make、code implemented in less than one day。这足以把 Topic 04 从 independent adoption census / hosted early outcome 推进到 named real deployment case supported，同时仍保留 vendor-hosted / not independently verified 风险。
- captured_excerpt: `yes`
- claims_supported: `Figma's official customer story says Findable, an AI-powered document-intelligence platform for the built environment, used Figma Make to redesign and build its app shell. The case reports that the team built a high-fidelity app shell with real navigation and routing logic inside a real architectural skeleton, turned the prototype into a handoff and reusable template, encoded design and architecture rules into the Figma Make template, and delivered the final app shell 50% faster with over 90% of the final product code from Figma Make implemented in less than one day. This supports a named real deployment case for AI-assisted design-to-code workflow, but not independent outcome verification.`
- date_scope: `customer story crawled 2026-04 / accessed 2026-04-18`
- related_entities: `Figma Make; Findable; Riccardo Busato; Ruan Odendaal; Hans Christian Berge; app shell; design-to-code; AI Clarification Guide`

## 关键事实

1. Customer story 标题是 `How Findable moved 50% faster with Figma Make`。
2. Findable 是 2020 年成立的 AI-powered document intelligence platform，服务 built environment / property owners / managers / consultants。
3. 项目对象是 Findable 的 app shell redesign。
4. App shell 被描述为 web application 的基础结构：
   - first thing to load
   - key to UX
   - 包含 navigation、layout、structure
   - 影响后续产品基础
5. 旧流程问题：
   - static design 难模拟 live site complexity
   - detailed handoff process 长
   - design-to-code interpretation gaps 有时到 production 才被发现
6. Figma Make 的使用方式：
   - 生成业务 intelligence platform 的 visuals
   - 构建 app shell structure
   - 复现 design system、components、themes、styles
   - 构建 real navigation and routing logic
   - 形成 real architectural skeleton
7. 结果是 high-fidelity app shell / fully functional working prototype。
8. Prototype 被用作 handoff：
   - states
   - interactions
   - navigation
   - code structure
9. Findable 将 app shell 推成 reusable template：
   - design system foundation
   - layout foundation
   - navigation foundation
   - architectural foundation
10. Figma Make template 里编码了规则：
   - design rules
   - layout patterns
   - architecture constraints
   - code-quality guidelines
   - Tailwind usage rules
11. 页面展示 Findable 的 `AI Clarification Guide`，作为 template 中的 rule set，用于保证新 feature follow consistent architectural patterns。
12. 官方结果：
   - app shell build 50% faster
   - over 90% of the final product code from Figma Make
   - code implemented in less than one day

## 核心内容摘录

### 这条 evidence 补的 gap

- 之前 Topic 04 multimodal / design-to-code 轴已有：
  - Figma Make official workflow signal
  - Vercel v0 workflow signal
  - Vercel/Stripe hosted outcome
  - Personagram independent design-study outcome
  - AI4UI enterprise benchmark
  - UX Tools independent adoption census
- 仍缺 named real deployment case。
- Findable case 直接给出 named customer、named product surface、final product code share 和 delivery-time outcome，因此可升级为 `named-real-deployment-case-supported`。

### 与 Topic 06 的交叉

- Findable 的 `AI Clarification Guide` 和 template rule sets 说明 agent-era / AI design-to-code workflow 也会遇到 rule-layering 问题：
  - design rules
  - layout patterns
  - architecture constraints
  - code-quality guidelines
  - tool-specific implementation rules
- 这与 Topic 06 的 `AGENTS.md` / scoped rules / feature spec 分层模型一致。

### 对最终报告的写法约束

- 可以写：
  - Findable is a named vendor-hosted deployment case for Figma Make-assisted app-shell work.
  - The case reports final-product code reuse and time-to-market improvement.
  - The workflow uses encoded rules/guide material, not raw prompt-only generation.
- 不应写：
  - independent verification proves the 50% or 90% numbers.
  - Figma Make generally produces production-ready code without review.
  - this proves broad market maturity.

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 04 `future-trends` | named real deployment / final product code reuse case for AI-assisted design-to-code / app-shell workflow |
| Topic 06 `agent-format` | supports rule-layered AI workflow: AI Clarification Guide, architecture constraints, code-quality guidelines, Tailwind rules |

## 可直接引用的术语 / 概念

- `Findable`
- `app shell`
- `Figma Make`
- `real navigation and routing logic`
- `real architectural skeleton`
- `AI Clarification Guide`
- `50% faster`
- `over 90% of the code`
- `less than one day`
- `design rules / architecture constraints / code-quality guidelines`

## 风险与局限

1. 这是 Figma 官方 customer story，是 vendor-hosted case，不是 independent third-party audit。
2. 50% faster 与 90% code reuse 是 customer/vendor-reported outcome，未见独立复核。
3. Case 聚焦 app shell，不代表整套复杂 enterprise application 已由 Figma Make 全量生成。
4. 仍不能证明 broad market maturity 或 no-review production readiness。
5. Topic 04 因而可以升级为 `named-real-deployment-case-supported`，但应保留 `independent-production-outcome-verification-pending`。

## 交叉引用

- Figma Make official workflow signal：[`04-future-trends-figma-make-multimodal-signal.md`](04-future-trends-figma-make-multimodal-signal.md)
- UX Tools adoption census：[`04-future-trends-state-of-prototyping-2026.md`](04-future-trends-state-of-prototyping-2026.md)
- AI4UI enterprise benchmark：[`04-future-trends-ai4ui-enterprise-pixel-to-production.md`](04-future-trends-ai4ui-enterprise-pixel-to-production.md)
- Topic 04 evidence summary：[`../_artifacts/04-future-trends-evidence-summary.md`](../_artifacts/04-future-trends-evidence-summary.md)
- Topic 06 evidence summary：[`../_artifacts/06-agent-format-evidence-summary.md`](../_artifacts/06-agent-format-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
