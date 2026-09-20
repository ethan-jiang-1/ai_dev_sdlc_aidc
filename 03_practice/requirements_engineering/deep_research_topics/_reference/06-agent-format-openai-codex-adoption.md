# OpenAI 2025/2026 — How OpenAI uses Codex

- source_url: `https://cdn.openai.com/pdf/6a2631dc-783e-479b-b1a4-af0cfbd38630/how-openai-uses-codex.pdf`
- source_type: `official product / engineering case study`
- accessed_at: `2026-04-18`
- related_topic: `06 agent-format (primary), 04 future-trends`
- trust_level: `official`
- tier: `B`
- why_it_matters: 这是 Topic 06 需要的 adopter case。它不是抽象产品页，而是 OpenAI 基于内部访谈与使用数据总结的真实采用模式，能回答“agent-facing spec / request / task artifacts 在团队工程里是怎么被消费的”。
- captured_excerpt: `yes`
- claims_supported: `Codex 已在 OpenAI 多个工程团队日常使用；它被用于提升测试覆盖、提升开发速度、保持工作流连续性；工程师会把 user request 或 spec 粘给 Codex 生成 rough draft；后台并行 PR/修复是高频使用形态；agent-friendly artifact 价值在于把需求和任务变成可继续加工的 starter code / plan / tests。`
- date_scope: `document published circa 2025 Q4; accessed 2026-04-18`
- related_entities: `OpenAI; Codex; ChatGPT Enterprise; ChatGPT API; ChatGPT Desktop; Product Engineering; Performance Engineering; API; Infrastructure`

## 关键事实

1. 文档首页明确写明该材料来自 `interviews with OpenAI engineers and internal usage data`，不是单纯市场文案。
2. Codex 已被 OpenAI 内部多个技术团队日常使用，包括 Security、Product Engineering、Frontend、API、Infrastructure、Performance Engineering。
3. 使用场景不是单一“写代码”，而是覆盖：
   - `Improving test coverage`
   - `Increasing development velocity`
   - `Staying in flow`
   - `Exploration and ideation`
4. 对 Topic 06 最重要的 adopter signal 是：工程师会直接把 `user request or spec` 交给 Codex 生成 rough draft，这说明 feature-level spec / request artifact 已进入真实工程循环。
5. 文档还给出一个与 harness / background execution 强相关的信号：工程师在开会时让 Codex 后台工作，之后直接 review / merge PR。
6. 文档里的最佳实践强调先用 Ask Mode 生成 implementation plan，再进入 Code Mode，这说明“spec / plan / code”并不是一次提示完成，而是分阶段推进。

## 核心内容摘录

### 来源与适用范围

- 文档说明其依据是 OpenAI 工程师访谈与内部使用数据。
- 覆盖团队包含 Security、Product Engineering、Frontend、API、Infrastructure、Performance Engineering。

### 与 spec / request artifact 直接相关的句子

- 文档在 `Increasing development velocity` 章节写到：工程师会把 `user request or spec` 粘给 Codex，让它先生成一个 rough draft，后续再回来 refinement。
- 同页案例里写到：工程师“开了一整天会，仍然 merge 了 4 个 PR，因为 Codex 一直在后台工作”。

### 与持续流工作模式相关的句子

- `Staying in flow` 章节强调：Codex 可用于捕获未完成工作、把笔记变成 prototype、把 exploratory task 先丢出去，方便之后继续。
- 这类模式的核心不是“大而全 instruction file”，而是把任务、笔记、spec、反馈变成 agent 可继续执行的中间工件。

### 与 plan-first 相关的句子

- Best practices 章节建议：对大改动先用 Ask Mode 生成 implementation plan，再把该 plan 作为后续 Code Mode 的输入。
- 这意味着在 OpenAI 自己的使用实践里，`plan` 是一等 artifact，而不是纯口头提示。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 06 `agent-format` | 这是 adopter case 主锚点：OpenAI 内部真实采用表明，agent-facing artifacts 不只是 `AGENTS.md` 这种 repo contract，还包括更细粒度的 `user request / spec / plan / test task` |
| Topic 04 `future-trends` | 支撑“spec-as-work artifact”已经进入日常工程，不再只是方法论口号 |

## 可直接引用的术语 / 概念

- `interviews with OpenAI engineers and internal usage data`
- `user request or spec`
- `rough draft`
- `Improving test coverage`
- `Increasing development velocity`
- `Staying in flow`
- `implementation plan`
- `Ask Mode -> Code Mode`

## 风险与局限

1. 这是一份官方案例总结，不是独立第三方实证论文，因此更适合作为 adopter evidence，而不是 ROI 因果证明。
2. 文档证明的是 Codex 在 OpenAI 内部的广泛采用，不直接证明其他公司也会复制同样的 artifact 结构。
3. 它没有详细给出仓库内每种 spec 文件的命名规范；因此它支撑“存在 feature-level artifact 工作流”，但不能单独确定最佳文件布局。

## 交叉引用

- 失败模式 / repo SoR：[`06-agent-format-openai-harness-engineering.md`](06-agent-format-openai-harness-engineering.md)
- shared 基线：[`00-shared-codex-agents-md-spec.md`](00-shared-codex-agents-md-spec.md)
- Topic 06 seed：[`../topic-06-agent-format.md`](../topic-06-agent-format.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
