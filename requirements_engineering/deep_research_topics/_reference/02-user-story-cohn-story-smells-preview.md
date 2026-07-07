# Mike Cohn 2004 — O'Reilly previews for `What Stories Are Not` and `Story Smells`

- source_url: `https://www.oreilly.com/library/view/user-stories-applied/0321205685/ch12.html` + `https://www.oreilly.com/library/view/user-stories-applied/0321205685/ch14.html`
- source_type: `official book preview pages`
- accessed_at: `2026-04-18`
- related_topic: `02 user-story (primary), 01 re-landscape, 05 integration-bdd`
- trust_level: `official publisher`
- tier: `B`
- why_it_matters: Topic 02 之前已有书级目录和部分章节锚点，但 `Story Smells` 仍缺直接章节内容。O'Reilly 官方预览页给出了 Chapter 12 和 Chapter 14 的章节标题、摘要，以及 `Stories Are Too Small` 这一具体 smell 的 symptom/discussion 片段。这比单纯依赖目录推断更强，足以把 Topic 02 从“Story Smells 仅目录级存在”推进到“至少一个直接 smell preview landed”。
- captured_excerpt: `partial`
- claims_supported: `User Stories Applied Chapter 14 is explicitly a catalog of story smells and solutions; one directly previewed smell is Stories Are Too Small, whose symptom is frequent need to revise estimates and whose discussion ties overly small stories to estimating/scheduling instability; Chapter 12 explicitly frames user stories against use cases, IEEE 830 SRS, and interaction design scenarios.`
- date_scope: `book preview pages accessed 2026-04-18`
- related_entities: `Mike Cohn; User Stories Applied; O'Reilly Online Learning; Story Smells; IEEE 830`

## 关键事实

1. O'Reilly 官方预览页直接给出 `Chapter 14. A Catalog of Story Smells`。
2. 章节摘要明确说：
   - 本章将呈现一组 `bad smells`
   - 每个 smell 都会被描述并给出一个或多个 solution
3. 预览中可直接见到第一个 smell：`Stories Are Too Small`。
4. 该 smell 的 `Symptom` 是：
   - `A frequent need to revise estimates`
5. 该 smell 的 `Discussion` 直接指出：
   - 小故事会在 estimating 和 scheduling 上造成问题
   - 因为它们的估算值会随着实现顺序变化而剧烈变化
6. O'Reilly 对 `Chapter 12. What Stories Are Not` 的预览还明确说 user stories differ from:
   - use cases
   - IEEE 830 software requirements specifications
   - interaction design scenarios
7. Chapter 12 的首个一级节标题就是 `User Stories Aren’t IEEE 830`。

## 核心内容摘录

### Story Smells 不只是目录项

- 现在已不需要仅凭目录推断 `Story Smells` 章节存在。
- O'Reilly 官方预览直接给出了：
  - 章节定位
  - 章节目的
  - 至少一个具体 smell 的 symptom 与 discussion

### 第一个直接落地的 smell

- `Stories Are Too Small`
- `Symptom`: frequently revising estimates
- `Discussion`: overly small stories destabilize estimating and scheduling because effort shifts with implementation order

这使 Topic 02 对反模式的叙述可以从抽象层推进到具体诊断层。

### `What Stories Are Not` 的直接补强

- Chapter 12 不再只是“书里有这一章”。
- 预览页直接说明它把 user stories 与 use cases、IEEE 830 SRS、interaction design scenarios 做区分。
- 因而，Topic 02 的 negative boundary 现在同时有：
  - Cohn 2004 官方 slides
  - O'Reilly 章节预览

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 02 `user-story` | 补强 Story Smells 直接章节证据，并把 `What Stories Are Not` 从目录级存在推进到章节摘要级存在 |
| Topic 01 `re-landscape` | 支撑 user story 与 IEEE-style SRS / use case / interaction scenario 的边界 |
| Topic 05 `integration-bdd` | 间接支持 story 不应被当作完整确认层或 formal specification 的替代品 |

## 可直接引用的术语 / 概念

- `A Catalog of Story Smells`
- `bad smells`
- `one or more solutions`
- `Stories Are Too Small`
- `A frequent need to revise estimates`
- `What Stories Are Not`
- `User Stories Aren't IEEE 830`

## 风险与局限

1. 这是 preview-level chapter content，不是整章全文。
2. 当前仅直接拿到一个 smell 的可核对片段，不足以声称完整 taxonomy 已 fully captured。
3. Topic 02 因而可以升级为 `direct-story-smell-preview-supported`，但不应写成 `full-story-smell-taxonomy-captured`。

## 交叉引用

- 书级主锚：[`02-user-story-cohn-book-excerpts.md`](02-user-story-cohn-book-excerpts.md)
- Cohn 2004 slides：[`02-user-story-cohn-2004-intro-slides.md`](02-user-story-cohn-2004-intro-slides.md)
- Topic 02 evidence summary：[`../_artifacts/02-user-story-evidence-summary.md`](../_artifacts/02-user-story-evidence-summary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
