# Mike Cohn 2024 — Overly small user stories as a concrete story-smell discussion

- source_url: `https://www.mountaingoatsoftware.com/blog/how-programmers-and-testers-and-others-should-collaborate-on-user-stories`
- source_type: `official KOL blog`
- accessed_at: `2026-04-18`
- related_topic: `02 user-story (primary), 05 integration-bdd`
- trust_level: `official / practitioner`
- tier: `B`
- why_it_matters: Topic 02 已有 O'Reilly preview 中 `Stories Are Too Small` 的 symptom，以及 InformIT 的 Story Smells taxonomy TOC；但 queue 当前要找更接近 discussion-level 的材料。Mike Cohn 2024 官方博客直接讨论 super-small stories 的问题，并列出依赖管理、优先级排序、工具跟踪成本三类实际 drawback。这不是 Chapter 14 原文，但作为同一作者的近期官方 discussion，能把 `Stories Are Too Small` 从 preview/taxonomy 再推进到 practical discussion evidence。
- captured_excerpt: `yes`
- claims_supported: `Cohn's 2024 official blog argues that extremely small stories can create dependency-management overhead, make backlog prioritization more challenging and time-consuming, and increase tracking/update overhead. This provides a recent official discussion-level support for the story-smell that stories can be too small, while still leaving full Chapter 14 discussion text and Beck original excerpts pending.`
- date_scope: `published/updated 2024-12-17; accessed 2026-04-18`
- related_entities: `Mike Cohn; Mountain Goat Software; user stories; story size; collaboration`

## 关键事实

1. 文章作者是 Mike Cohn，发布在 Mountain Goat Software 官方站点。
2. 文章主题是如何让 programmers、testers 与其他角色围绕同一个 user story 并行协作。
3. 文中直接讨论一个问题：
   - 是否可以用 `super-small stories` 达到同样效果？
4. Cohn 明确承认自己通常偏好 fairly small stories，但指出 extremely small stories 有 drawbacks。
5. 文中列出的三类主要问题是：
   - 更多 dependencies 需要管理
   - product backlog prioritization 更难、更耗时
   - sprint 中处理更多 stories 会增加 tracking / updating 工具成本
6. 文章最后给出 practical diagnostic：
   - 当这些问题开始影响团队时，stories 就开始 too small。

## 核心内容摘录

### 对 `Stories Are Too Small` smell 的近期解释

- O'Reilly preview 已经给出 `Stories Are Too Small` 这个 smell 与估算频繁变动的 symptom。
- 这篇 2024 官方博客补充了更 operational 的讨论：
  - dependency overhead
  - prioritization overhead
  - tracking overhead

### 对最终教程的意义

- 这条 evidence 适合把 `Small` 的教学写成边界条件：
  - story 应足够小，能在 iteration 内完成
  - 但不应小到失去价值单元、引入大量依赖与管理成本
- 这比“越小越好”的常见误读更稳。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 02 `user-story` | 对 `Stories Are Too Small` 提供近期、同作者、discussion-level support |
| Topic 05 `integration-bdd` | 支撑 story 与 test/verification 的协作粒度需要通过并行小批量协作解决，而不只是拆成大量极小 story |

## 可直接引用的术语 / 概念

- `super-small stories`
- `overly small stories`
- `dependencies to manage`
- `prioritizing the product backlog becomes more challenging`
- `tracking them and updating them`

## 风险与局限

1. 这不是 `User Stories Applied` Chapter 14 原文。
2. 它只强力覆盖 `Stories Are Too Small` 这一类 smell 的 practical discussion。
3. Topic 02 仍不应声称已经拿到 full Chapter 14 discussion；更稳写法是 `one smell has discussion-level support; full chapter discussion pending`。

## 交叉引用

- O'Reilly preview：[`02-user-story-cohn-story-smells-preview.md`](02-user-story-cohn-story-smells-preview.md)
- InformIT taxonomy TOC：[`02-user-story-cohn-story-smells-informit-toc.md`](02-user-story-cohn-story-smells-informit-toc.md)
- 书级主锚：[`02-user-story-cohn-book-excerpts.md`](02-user-story-cohn-book-excerpts.md)
- Topic 02 evidence summary：[`../_artifacts/02-user-story-evidence-summary.md`](../_artifacts/02-user-story-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
