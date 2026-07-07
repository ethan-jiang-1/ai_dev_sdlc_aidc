# Seb Rose 2022 — User Stories and BDD Part 1, origin and BDD boundary

- source_url: `https://accu.org/journals/overload/30/171/rose/`
- source_type: `practitioner journal / KOL article`
- accessed_at: `2026-04-18`
- related_topic: `02 user-story (primary), 05 integration-bdd, 01 re-landscape`
- trust_level: `practitioner journal / BDD KOL`
- tier: `C`
- why_it_matters: Topic 02 当前 queue 要求补强 Chapter 14 full discussion 或 Beck full-text-adjacent source。本文不是 Chapter 14 原文，也不是 Beck 书籍全文；但它是 ACCU Overload 发表的 Seb Rose 文章，直接讨论 user story 的起源、XP Planning Game、Beck 2004、C2 Wiki、Jeffries 3C、Connextra template 与 Cucumber/BDD feature-file 误用边界。它比泛摘要更强，适合作为 Beck full-text-adjacent / origin-boundary upgrade，同时继续保留 Chapter 14 full discussion 和 Beck verbatim text pending。
- captured_excerpt: `partial`
- claims_supported: `Seb Rose's 2022 ACCU Overload article states that the original Planning Game description in Beck's Extreme Programming Explained mentions stories but not the phrase user stories, and frames stories as placeholders for conversation created to defer detailed analysis until implementation was near. It also warns that putting a user story at the top of a Cucumber feature file became a cargo-cult pattern and that story templates can be misused as mini-requirements specs. This supports the origin/boundary claim that stories are conversation and value-focusing artifacts, not feature files, BDD scenarios, or full requirements specifications.`
- date_scope: `published in Overload 30(171), October 2022; article references original 2019 blog; accessed 2026-04-18`
- related_entities: `Seb Rose; ACCU Overload; Kent Beck; Extreme Programming Explained; Planning Game; Ron Jeffries; Rachel Davies; Connextra; Cucumber; BDD; Mike Cohn`

## 关键事实

1. 文章标题为 `User Stories and BDD - Part 1`。
2. 作者是 Seb Rose，ACCU Overload 期刊信息为 `30(171):4-6, October 2022`。
3. 文章目标是解释 user story 的起源、用途，以及它们如何与 BDD 方式交互。
4. 文章指出一个实践问题：
   - 很多 feature files 顶部放了类似 user story 的文本
   - 这种做法让很多 Cucumber 用户误以为 feature file 就应从 user story 开头
5. 文章把 story 的核心用途放在 XP / lightweight methodologies 背景下：
   - 做 high-level decomposition
   - 接受 implementation 前仍需 detailed analysis / conversations
6. 文章明确关联 Beck：
   - Beck 2004 `Extreme Programming Explained: Embrace Change`
   - 原始 Planning Game 描述提到 `stories`
   - 但该书没有使用 `user stories` 这个词
7. 文章指出 `user` 一词的加入强化了一个方向：
   - 帮助团队聚焦最大化软件交付价值
   - 但也引发“每个 story 是否都必须来自 end user 视角”的争论
8. 文章回到 Connextra / Rachel Davies template：
   - role
   - capability
   - business value
9. 文章也引用 Rachel Davies 对 template misuse 的警告：
   - template 可能让人更关注文字形式而不是 shared understanding
   - 不适合 template 的 stories 可能被强行塞进模板
10. 文章总结了一个关键边界：
   - story 的重要部分不是卡片上的 words
   - 而是团队形成的 shared understanding

## 核心内容摘录

### 对 Beck gap 的升级方式

- 之前 Topic 02 已有：
  - Beck / Fowler preview-level XP planning anchors
  - XP/C3/Cockburn boundary starter anchor
  - Cohn anti-pattern / Story Smells materials
- 本文进一步补强：
  - Beck 2004 Planning Game 与 `stories` 的关系
  - `story` 到 `user story` 术语演化边界
  - user story 不等同于 Cucumber feature file 或 BDD scenario

### 对 Topic 02 的写法约束

- 可以写：
  - XP/Beck 的 Planning Game 语境中已有 `stories`，但 `user story` 术语后来才稳定下来。
  - user story 的根本作用是聚焦价值、延迟细节、触发 conversation。
  - story template 有教学价值，但被当成 mini requirements spec 会违背原意。
- 不应写：
  - 已拿到 Beck 原书全文
  - 已拿到 Chapter 14 full discussion
  - user story 和 BDD feature / scenario 可以直接互换

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 02 `user-story` | 补强 Beck-adjacent origin/boundary：Planning Game 中的 stories、user story 术语演化、template misuse 风险 |
| Topic 05 `integration-bdd` | 支撑 Story 与 BDD Feature/Gherkin 不应混同，feature file 顶部硬塞 user story 是 cargo-cult 风险 |
| Topic 01 `re-landscape` | 支撑 lightweight/agile story artifact 与 formal requirement/spec artifact 的边界 |

## 可直接引用的术语 / 概念

- `Planning Game`
- `stories`
- `user stories`
- `placeholder for a conversation`
- `Connextra template`
- `mini-requirements specs`
- `shared understanding`
- `feature file`

## 风险与局限

1. 这不是 Beck 原书全文，也不是 Chapter 14 `Story Smells` 的完整正文。
2. 它是 practitioner/KOL article，非 peer-reviewed empirical study。
3. 文章主轴是 user story 与 BDD 的关系，对 Story Smells 只提供边界背景，不替代 Cohn Chapter 14 full-discussion。
4. Topic 02 因而可以升级为 `beck-planning-game-adjacent-supported` / `story-bdd-boundary-supported`，但仍保留 `chapter-14-full-discussion-pending` 与 `beck-full-text-verbatim-pending`。

## 交叉引用

- Beck preview-level anchor：[`02-user-story-beck-planning-xp-previews.md`](02-user-story-beck-planning-xp-previews.md)
- XP / Cockburn boundary：[`02-user-story-xp-origins-cockburn-boundary.md`](02-user-story-xp-origins-cockburn-boundary.md)
- Cohn Story Smells preview：[`02-user-story-cohn-story-smells-preview.md`](02-user-story-cohn-story-smells-preview.md)
- Topic 02 evidence summary：[`../_artifacts/02-user-story-evidence-summary.md`](../_artifacts/02-user-story-evidence-summary.md)
- Topic 05 evidence summary：[`../_artifacts/05-integration-bdd-evidence-summary.md`](../_artifacts/05-integration-bdd-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
