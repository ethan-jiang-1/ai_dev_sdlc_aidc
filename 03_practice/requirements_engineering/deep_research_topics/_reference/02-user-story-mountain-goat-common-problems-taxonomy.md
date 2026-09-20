# Mountain Goat Software 2026 — common user-story problems and non-story item taxonomy

- source_url: `https://www.mountaingoatsoftware.com/training/roles/product-owner`
- source_type: `official training curriculum page`
- accessed_at: `2026-04-18`
- related_topic: `02 user-story (primary), 01 re-landscape, 05 integration-bdd`
- trust_level: `official / practitioner`
- tier: `B`
- why_it_matters: Topic 02 已有 Cohn book TOC、Story Smells preview/taxonomy 和 one-smell discussion，但仍需要更广的 multi-smell / anti-pattern coverage。Mountain Goat 官方 Product Owner training page 不是书章正文，但它系统列出 Cohn/Mountain Goat 课程中的 user-story problem taxonomy，包括 stories with too much detail、spending too much time splitting stories、stories involving more than one team、stories that are really tasks、managing the need for a requirement document，以及 `Not Everything Needs to Be a User Story` 下的 NFR、bugs、Job Stories 等。它能补一个 practice-facing multi-problem taxonomy，避免最终教程只围绕 `stories too small` 单点展开。
- captured_excerpt: `partial`
- claims_supported: `Mountain Goat's official product-owner curriculum treats user-story quality problems as a broader taxonomy, including excessive detail, over-splitting, multi-team stories, stories that are really tasks, managing requirement documents, and non-story items such as nonfunctional requirements, bugs, and job stories. This supports a multi-problem anti-pattern frame while still not replacing full Chapter 14 discussion text.`
- date_scope: `page accessed 2026-04-18`
- related_entities: `Mike Cohn; Mountain Goat Software; user stories; Better User Stories; Product Owner training`

## 关键事实

1. Mountain Goat 官方 Product Owner course 页面包含 user-story 相关课程结构。
2. `Adding Detail with Conditions of Satisfaction or Acceptance Criteria` 部分列出：
   - adding detail over time
   - how much detail is appropriate
   - working with teams that want too much detail
   - definition of ready risk
3. `Splitting Stories` 部分列出：
   - complex and compound stories
   - SPIDR splitting
   - spending too much time splitting stories
4. `Overcoming Common Problems` 部分直接列出多类问题：
   - managing dependencies between stories
   - stories with too much detail
   - stories involving more than one team
   - stories that are really tasks
   - managing the need for a requirement document
5. `Things That Are Not User Stories` 部分列出：
   - nonfunctional requirements
   - stories and bugs
   - job stories
6. 这说明 Cohn/Mountain Goat 的实践体系中，story anti-pattern 不只包括 too-small stories，还包括：
   - detail boundary
   - task/story confusion
   - team boundary
   - NFR / bug / job-story object boundary
   - requirements-document handoff boundary

## 核心内容摘录

### 为什么这条能补 multi-smell gap

- O'Reilly / InformIT 已锁定 Chapter 14 `Story Smells` 的书级结构。
- Cohn 2024 已对 `too small` 这一 smell 给出 discussion-level support。
- Mountain Goat official curriculum 进一步补足 practice-facing taxonomy：
  - too much detail
  - really tasks
  - more than one team
  - requirement document need
  - not everything needs to be a user story

### 当前可稳妥支撑的边界

- 适合支撑：
  - `multi-problem-story-taxonomy-supported`
  - `not-everything-is-a-user-story-supported`
  - `task/story/nfr/job-story-boundary-supported`
- 不适合支撑：
  - Chapter 14 full text captured
  - 每个 story smell 的完整 repair template 已捕获
  - Beck original-book full text 已补齐

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 02 `user-story` | 补足 practice-facing multi-smell / multi-problem taxonomy |
| Topic 01 `re-landscape` | 支撑 Story 与 NFR、requirements document、task、job story 等对象边界 |
| Topic 05 `integration-bdd` | 支撑 acceptance criteria / conditions of satisfaction 是 story 细化层，不是 story card 本体 |

## 可直接引用的术语 / 概念

- `Stories with Too Much Detail`
- `Stories That Are Really Tasks`
- `Managing the Need for a Requirement Document`
- `Not Everything Needs to Be a User Story`
- `Nonfunctional Requirements`
- `Job Stories`

## 风险与局限

1. 这是官方课程目录 / curriculum page，不是 Cohn book Chapter 14 的正文。
2. 它证明 Mountain Goat practice taxonomy 的范围，但不提供每个 smell 的完整 discussion。
3. Topic 02 因而可以升级为 `multi-problem taxonomy supported`，但仍应保留 `full Chapter 14 discussion pending` 和 `Beck full-text pending`。

## 交叉引用

- InformIT taxonomy TOC：[`02-user-story-cohn-story-smells-informit-toc.md`](02-user-story-cohn-story-smells-informit-toc.md)
- Cohn 2024 too-small story discussion：[`02-user-story-cohn-too-small-stories-2024.md`](02-user-story-cohn-too-small-stories-2024.md)
- Cohn book-level anchor：[`02-user-story-cohn-book-excerpts.md`](02-user-story-cohn-book-excerpts.md)
- Topic 02 evidence summary：[`../_artifacts/02-user-story-evidence-summary.md`](../_artifacts/02-user-story-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
