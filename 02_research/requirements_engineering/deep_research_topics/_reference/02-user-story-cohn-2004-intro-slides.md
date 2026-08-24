# Mike Cohn 2004 — Introduction to User Stories slides as direct anti-pattern / boundary anchor

- source_url: `https://www.mountaingoatsoftware.com/uploads/presentations/Introduction-User-Stories-Software-Requirements%20-Software-Development-Best-Practices-2004.pdf`
- source_type: `official presentation slides`
- accessed_at: `2026-04-18`
- related_topic: `02 user-story (primary), 01 re-landscape, 05 integration-bdd`
- trust_level: `official / practitioner`
- tier: `B`
- why_it_matters: Topic 02 当前缺口之一是 `What Stories Are Not` / `Story Smells` 的更直接内容支撑。Mike Cohn 2004 官方 slides 虽不是完整书页，但直接给出 user story 的本体定义与反面边界：story 是 `placeholders for future conversations`，`Negotiable` 不是 written contracts / requirements，且 `Stories are not use cases`。这比仅靠目录级证据更直接，足以把 Topic 02 的 anti-pattern / not-a-spec 边界再收紧一格。
- captured_excerpt: `yes`
- claims_supported: `User stories are placeholders for future conversations; negotiable means stories are not written contracts and not fixed software requirements to be fulfilled verbatim; stories are not use cases; the point of the card is to preserve enough information to enable future conversation, not to encode complete requirements.`
- date_scope: `presentation dated 2004`
- related_entities: `Mike Cohn; user stories; use cases; INVEST; requirements`

## 关键事实

1. Slides 明确给出定义：user stories are `placeholders for future conversations`。
2. Slides 对 `Negotiable` 的解释非常直接：
   - stories are not written contracts
   - stories are not requirements the software must fulfill
3. Slides 还明确写出：`Stories are not use cases`。
4. Slides 对 placeholder 的解释是：card 上只需保留 enough information to remind everyone what the story was about，后续细节来自 conversation。
5. 这条证据与 Chapter 12 `What Stories Are Not` 的目录级证据形成强互证：即使不拿到全文，Cohn 自己也在 2004 一开始就反复说明 story 不是完整规格合同。

## 核心内容摘录

### story 的本体不是完整规格

- slides 直接把 user stories 定义成 `placeholders for future conversations`。
- 这意味着 story card 的职责是保留协作入口，而不是承载所有产品/系统细节。

### `Negotiable` 的反面边界

- slides 解释 `Negotiable` 时明确强调：
  - not written contracts
  - not requirements the software must fulfill
- 这对 Topic 02 很关键，因为它直接限制了把 story 当 specification baseline 的冲动。

### 与 use case 的区别

- slides 明确写出 `Stories are not use cases`。
- 这使 Topic 02 能更稳地把 Story 与 Topic 01 的 Use Case 2.0 分开，而不只依赖 Cockburn 或后续阐释。

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 02 `user-story` | 直接补强 `What Stories Are Not` 方向：story 不是 written contract、不是 fixed requirements、也不是 use case |
| Topic 01 `re-landscape` | 进一步稳定 Story 与 Use Case 的范式边界 |
| Topic 05 `integration-bdd` | 间接支持“story 之后仍需要 acceptance/confirmation 层”，因为 story 本身不是完整 spec |

## 可直接引用的术语 / 概念

- `placeholders for future conversations`
- `not written contracts`
- `not requirements the software must fulfill`
- `Stories are not use cases`
- `enough information to remind everyone`

## 风险与局限

1. 这是 presentation slides，不是书中完整章节原文；因此更适合作为 anti-pattern / boundary 直引锚，而不是完整 taxonomy 来源。
2. 它补强的是 “what stories are not” 边界，不单独给出完整 `Story Smells` 列表。
3. 若要做更细的 smell catalog，仍应继续寻找更强的书内 extract。

## 交叉引用

- Topic 02 evidence summary：[`../_artifacts/02-user-story-evidence-summary.md`](../_artifacts/02-user-story-evidence-summary.md)
- Cohn book-level anchor：[`02-user-story-cohn-book-excerpts.md`](02-user-story-cohn-book-excerpts.md)
- XP/Cockburn boundary：[`02-user-story-xp-origins-cockburn-boundary.md`](02-user-story-xp-origins-cockburn-boundary.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
