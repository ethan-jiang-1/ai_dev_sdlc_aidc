# OpenAI 2026 — Harness engineering: leveraging Codex in an agent-first world

- source_url: `https://openai.com/index/harness-engineering/`
- source_type: `official engineering blog`
- accessed_at: `2026-04-18`
- related_topic: `06 agent-format (primary), 04 future-trends`
- trust_level: `official`
- tier: `B`
- why_it_matters: 这是 Topic 06 当前最强的一手 failure-mode / mechanism source。它直接回答“大而全 AGENTS.md 为什么失败”“团队级 AGENTS.md 与 deeper docs / plans 应该如何分层”“为什么 plan 必须是一等 artifact”。
- captured_excerpt: `yes`
- claims_supported: `context management 是大型 agent 任务的核心难点；one big AGENTS.md 在 OpenAI 内部实践中失败；短 AGENTS.md 应充当 table of contents；repo docs 才是 system of record；plans 应被视为 first-class artifacts；progressive disclosure 比 upfront 大注入更有效。`
- date_scope: `published 2026-02; accessed 2026-04-18`
- related_entities: `OpenAI; Codex; AGENTS.md; docs/; execution plans; CI; doc-gardening agent`

## 关键事实

1. OpenAI 明确写道：`Context management is one of the biggest challenges`，这把 Topic 06 的核心难点直接定在上下文管理，而不是语法本身。
2. 文章明确记录：他们尝试过 `one big AGENTS.md`，并且 `failed in predictable ways`。
3. 失败原因至少有四类：
   - 占用稀缺上下文，挤掉 task / code / relevant docs
   - “everything is important” 导致没有真正重点
   - 单体文档迅速 stale / rot
   - 难以机械验证 freshness / ownership / cross-links
4. OpenAI 给出的替代方案非常明确：`AGENTS.md` 不是 encyclopedia，而是 `table of contents`。
5. 真正的 system of record 放在结构化 `docs/` 目录中，短 `AGENTS.md` 只做 map，并把 agent 引到更深的 source of truth。
6. 文章还明确说 `Plans are treated as first-class artifacts`，复杂工作应以 execution plans + progress / decision logs 的形式 check into repository。
7. 整体方法论是 `progressive disclosure`：先给稳定、小的入口，再引导 agent 去读下一层，而不是一次性注入全部上下文。

## 核心内容摘录

### 失败模式：one big AGENTS.md

- OpenAI 直接写明他们尝试过 `one big AGENTS.md`。
- 失败机制包括：
  - context scarce
  - too much guidance becomes non-guidance
  - rots instantly
  - hard to verify

### 分层策略：AGENTS.md 作为目录，不是百科全书

- 文章原文给出的替代方案是：不要把 `AGENTS.md` 当 encyclopedia，而要把它当 `table of contents`。
- 他们把 repo knowledge base 放在结构化 `docs/` 目录，短 `AGENTS.md` 约 100 行，只做 map。

### plans 是一等 artifact

- 文章明确写道：`Plans are treated as first-class artifacts.`
- 小改动可以用轻量 plan，复杂工作则进入 check-in 到 repo 的 execution plans，并带 progress / decision logs。

### 机械约束

- OpenAI 不只靠提示约定，还通过 lint / CI 校验知识库是否过时、是否交叉链接、结构是否正确。
- 甚至有 doc-gardening agent 持续扫描 stale docs 并开修复 PR。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 06 `agent-format` | 这是 Topic 06 目前最关键的机制与失败模式锚点：它直接支持“team-level AGENTS.md 应短小、feature / domain knowledge 放 deeper docs / plans”的结论 |
| Topic 04 `future-trends` | 支撑 agent-first repo 的演化方向：docs、plans、linters、doc-gardening 都成为 agent scaffolding 的一部分 |

## 可直接引用的术语 / 概念

- `Context management`
- `one big AGENTS.md`
- `failed in predictable ways`
- `table of contents`
- `system of record`
- `Plans are treated as first-class artifacts`
- `progressive disclosure`
- `doc-gardening`

## 风险与局限

1. 这是 OpenAI 单一组织的内部实践总结，不自动代表所有团队都应复制相同目录结构。
2. 它强力证明了“大而全单文件”的失败，但没有单独量化“100 行是否最优”；100 行更像经验量级而非硬阈值。
3. 该材料主要回答 mechanism / failure mode，不替代其他工具（Kiro、Spec Kit）在 feature-level workflow 上的官方说明。

## 交叉引用

- adopter case：[`06-agent-format-openai-codex-adoption.md`](06-agent-format-openai-codex-adoption.md)
- shared 基线：[`00-shared-cursor-rules-official.md`](00-shared-cursor-rules-official.md)
- shared 基线：[`00-shared-claude-code-official.md`](00-shared-claude-code-official.md)
- shared 基线：[`00-shared-codex-agents-md-spec.md`](00-shared-codex-agents-md-spec.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
