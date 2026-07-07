# Mike Cohn — Mountain Goat Software *User Stories* Primer (KOL Anchor)

- source_url: `https://www.mountaingoatsoftware.com/agile/user-stories`（2026-04-17 抓取正文，Mountain Goat Software 官方站点，Mike Cohn 主理）+ 配套书 `User Stories Applied: For Agile Software Development`（Addison-Wesley, 2004, ISBN 0-321-20568-5，业内事实标准参考书）
- source_type: `practitioner primer + standard book`
- accessed_at: `2026-04-17`
- related_topic: `shared (02 user-story primary；01 re-landscape、05 integration-bdd、06 agent-format 引用)`
- trust_level: `practitioner (author-owned site + industry-standard textbook)`
- tier: `A`（书本身为业界 Standard；官网 primer 为 Tier B，但两者合并作为**同一 KOL 体系**的主锚；Fowler 的 bliki 明确把该书列为\"standard book\"）
- why_it_matters: Mike Cohn 的 *User Stories Applied* 是**\"user story 写作规范 + 3C + 模板\"的事实标准书**，被 Martin Fowler 在 bliki 公开锁定为\"standard\"。本轮 Topic 02 的术语规则、Topic 05 选型矩阵\"story 能覆盖什么 / 不能覆盖什么\"，必须以 Cohn 的定义为主锚，避免二手转述（例如把 3C 写错为 Cohn 原创，实际是 Ron Jeffries）。
- captured_excerpt: `yes`

---

## 关键事实

1. **User Story 的工作定义（Cohn 官方版）**
   - "A user story is a **short, simple description of a feature** told from the perspective of the person who desires the new capability, usually a user or customer of the system."
   - 关键属性：**短、简单、从用户视角、面向\"期望能力\"**。
   - 与 Fowler bliki 互文：**story 是占位符 + 后续对话的触发器**，不是规格书。

2. **标准模板（Cohn 官网明示）**
   - 格式：`As a < WHO >, I want < WHAT > so that < WHY >.`
   - Cohn 强调\"as a / I want / so that\"三段式的**主要作用是\"强制回到动机\"**，不是\"规约完备性\"。

3. **3C 的准确归属（Cohn 官网明确归给 Ron Jeffries, 2001）**
   - **Card** — 写下的描述，用于计划与提醒。
   - **Conversation** — 围绕 story 的对话，补全细节。
   - **Confirmation** — 验收测试，用于判定\"做完了没\"。
   - **研究含义**：3C 把 story 的\"规约-沟通-验证\"三段式**显式拆开**——\"验收测试\"是 story 方法论**必需的第三段**。这条证据在 Topic 05 里直接支撑\"User Story 需要与 BDD 或 EARS 的 confirmation 机制配合，才能覆盖需求生命周期\"。

4. **物理表现 → 数字表现的官方态度**
   - 原文：\"Historically user stories were deliberately kept informal, written on index cards or sticky notes … Today, user stories might just as easily be stored in a Jira issue or Trello board. **Don't let the fact that a user story exists in a tool make you any less willing to discard stories when they are no longer needed!**\"
   - 研究含义：Cohn 官方接受数字化，但**拒绝把数字化当作\"story 永久化\"**——这对 Topic 05、Topic 06（agent 格式中是否\"把 story 永久 pin 在 CLAUDE.md\"）是关键反证。

5. **与其它范式的边界（Cohn 书第 1-3 章要点）**
   - *User Stories Applied* 第 1 章即明确：user story \"is not a requirements document, a use case, or an IEEE-830 specification\"；story **并不是为了替代这些文档**，而是提供**开发计划的轻量单元**。
   - 这条论述是 Topic 05 \"User Story ≠ 全量需求规约\"判决的**书级证据**。

6. **可发现的资源资产**
   - 官网配套有\"200 Real-Life User Stories\"下载（Mike Cohn 自己写过的真实 backlog），是 Topic 02 示例层的二级证据池。
   - 书末附 INVEST（Bill Wake 原创，被 Cohn 收入书中）+ story 估算（story points / planning poker）配套方法。

---

## 原文直引（关键段）

> "A user story is a short, simple description of a feature told from the perspective of the person who desires the new capability, usually a user or customer of the system. User stories typically follow a simple template: As a < type of user >, I want < some goal > so that < some reason >."

> "Historically user stories were deliberately kept informal, written on index cards or sticky notes, stored in a shoe box, and arranged on walls or tables to facilitate planning and discussion. Their impermanence made it easy to tear them up, throw them away, and replace them with new stories as more was learned about the product being developed."

> "Agile user stories are composed of three aspects that Ron Jeffries named in 2001 with the wonderful alliteration of **card, conversation, and confirmation**."

> "User stories have many advantages, but the most important might be that **every user story is a placeholder for a future conversation**."

## 桥接

- → `00-shared-fowler-user-story-bliki.md`：Fowler 把 Cohn 的书锁为\"standard\"；两者一起构成 Topic 02 主证据链的**双锚**。
- → `00-shared-incose-gtwr-v4-summary.md`：GtWR 的\"需求\"定义与 Cohn \"story is not a requirements document\"的立场是**显式张力**——这是 Topic 05 选型矩阵最核心的对比轴。
- → 待落 `00-shared-patton-story-mapping-primer.md`：Patton 的 story map 处理\"多 story 之间的上下文结构\"；Cohn 主要处理\"单 story 的形式与工作流\"。

## 限制

- Mountain Goat primer 是\"科普+营销页\"层面的摘要；精确度仍需回到 Cohn 2004 年 *User Stories Applied* 的 Ch.1-3（Story definition / INVEST / 3C）+ Ch.14（What a story is not）。Topic 02 W1 deep-dive 必须提供书内章节级引用。
- Cohn 未讨论\"AI agent 环境下 story 是否仍是主要载体\"——这一面由 Topic 06 补。
