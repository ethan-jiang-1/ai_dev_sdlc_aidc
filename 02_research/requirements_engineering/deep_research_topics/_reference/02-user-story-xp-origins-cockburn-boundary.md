# Kent Beck / Martin Fowler / Alistair Cockburn — XP story origins and use-case boundary

- source_url: `https://www.martinfowler.com/books/pxp.html` + `https://martinfowler.com/bliki/UserStory.html` + `https://alistair.cockburn.us/hexagonal-architecture`
- source_type: `official book page + KOL bliki + official author article`
- accessed_at: `2026-04-18`
- related_topic: `02 user-story (primary), 01 re-landscape, 05 integration-bdd`
- trust_level: `official KOL / official author site`
- tier: `B`
- why_it_matters: Topic 02 的剩余高价值缺口之一是 Cockburn / Beck 对 user story roots 与 use-case boundary 的更直接锚点。这份组合证据不能替代 Beck 原版 white book 正文，但足以把风险从“起源与边界不清”收窄为“XP/C3 roots 与 Cockburn use-case boundary 已支持，Beck original-book verbatim text 仍待补”。
- captured_excerpt: `yes`
- claims_supported: `Kent Beck first introduced the term user story as part of XP; C3 and XP planning literature centered on breaking work into stories; stories were intended to stay informal and conversational rather than long written specifications; Cockburn's use cases should be written at the application boundary, independent of external technology, which supports a cleaner boundary between use cases and lighter user stories.`
- date_scope: `Planning XP book page reflects 2000 publication and C3/XP roots; Fowler UserStory page published 2013; Cockburn article published 2005 and still available as official author statement`
- related_entities: `Kent Beck; Martin Fowler; Alistair Cockburn; User Story; Extreme Programming; C3; Use Case; application boundary`

## 关键事实

1. Martin Fowler 的 `UserStory` 页面明确写道：Kent Beck first introduced the term as part of Extreme Programming。
2. 同页说明 user stories 的设计意图是比长规格文档更 informal、更 conversational 的 requirements elicitation style。
3. 同页还说明 story 的本质可以写在一张小卡片上，并故意在进入开发前不展开细节。
4. Fowler 的 `Planning Extreme Programming` 书页说明：
   - C3 was the project that gave birth to Extreme Programming
   - XP planning centered on `breaking down a project into stories`
5. 这说明 user story 在方法起源上与 XP / C3 的 planning practice 直接相连，而不是后来才附会进去的模板。
6. Cockburn 官方文章说明：use cases should generally be written at the application boundary, regardless of external technology。
7. 同文同时批评把 use case 写成带大量外部技术细节的长文档，说明 Cockburn 的 use case 边界仍然比 story 更偏应用行为与事件支持面，而不是单纯价值卡片。

## 核心内容摘录

### User Story 的 XP 起源

- Fowler `UserStory` 页把术语来源直接归到 Kent Beck 和 XP。
- `Planning XP` 页把 C3 定位为 XP birth project，并把 stories 列为 XP planning 的 central techniques。

### Story 为什么天然偏轻量

- Fowler `UserStory` 页强调 stories deliberately not fleshed out in detail until ready to develop。
- 这支持 Topic 02 的核心判断：story 不是 formal requirement，而是为了优先级、对话与 planning 而刻意保持轻量。

### Cockburn 的 use-case 边界

- Cockburn 官方文说明 use cases 应写在 application boundary，描述 application supports 的 functions and events，而不是外部技术细节。
- 这能帮助 Topic 02 区分：
  - Story 更轻、更面向计划和对话
  - Use case 更面向应用行为边界与事件

## 与本研究的关系

| 研究线 | 可直接支撑的内容 |
| --- | --- |
| Topic 02 `user-story` | 把“故事起源与 use-case 边界”从模糊印象升级为 XP/C3 roots + Cockburn application-boundary framing |
| Topic 01 `re-landscape` | 为 Story 与 Use Case 2.0 的地图关系补一个更早期的方法起源锚点 |
| Topic 05 `integration-bdd` | 进一步说明 story 适合做 intent/conversation 起点，而非完整系统行为规格 |

## 可直接引用的术语 / 概念

- `Kent Beck first introduced the term`
- `Extreme Programming`
- `C3`
- `breaking down a project into stories`
- `informal and conversational style`
- `application boundary`

## 风险与局限

1. 这份 reference 仍未直接抓到 Beck original white book 正文，因此不应声称“已完成 Beck 原文级闭环”。
2. Fowler 对 XP/story 的表述是高质量 KOL/一手邻近来源，但不是 Beck 本人逐字原文。
3. Cockburn 的文章提供的是 use-case boundary，而不是专门写给 user story 的对比论文；因此它更适合作为边界支持，而不是“Story vs Use Case 最终定论”。

## 交叉引用

- Topic 02 evidence summary：[`../_artifacts/02-user-story-evidence-summary.md`](../_artifacts/02-user-story-evidence-summary.md)
- shared story anchor：[`00-shared-fowler-user-story-bliki.md`](00-shared-fowler-user-story-bliki.md)
- Topic 01 use-case contrast：[`01-re-landscape-use-case-2-0-official.md`](01-re-landscape-use-case-2-0-official.md)
- 导航入口：[`_INDEX.md`](_INDEX.md)
