# Martin Fowler — bliki `UserStory` (KOL Anchor)

- source_url: `https://martinfowler.com/bliki/UserStory.html`（2026-04-17 抓取正文，Martin Fowler 官方 bliki）
- source_type: `KOL blog (expert practitioner)`
- accessed_at: `2026-04-17`
- related_topic: `shared (02 user-story primary；01 re-landscape、04 future-trends、05 integration-bdd 均会引用)`
- trust_level: `practitioner (author-owned blog, long-running bliki)`
- tier: `B`
- why_it_matters: Fowler 的 bliki 是**软件工程社区最常被引用的"工作定义"来源之一**。`UserStory` 一条把 XP 起源（Kent Beck）、INVEST（Bill Wake）、"As a / I want / So that" 格式、以及 Mike Cohn 的标准参考书串到同一张图上，是 Topic 02 的基础叙事锚。同时 Fowler 在正文尾部明确标出 `UseCasesAndStories` 讨论过\"故事 vs 用例\"的差异——这是后续 Topic 05 (选型矩阵) 要回引的关键节点。
- captured_excerpt: `yes`（关键段落原文已核对）
- notes: Fowler bliki 是稳定 URL，但没有版本号；"last modified" 通常隐含，引用时以 accessed_at 为准。

---

## 关键事实（对齐研究线）

1. **起源定位**
   - Fowler 明确指出 **Kent Beck 在 Extreme Programming 中首次引入 user story 术语**，目的是取代\"long written specifications\"，走向**更轻量、更对话化**（informal and conversational）的需求澄清路径。
   - Fowler 亲自表态**偏好 3" × 5" 卡片**—物理约束强制 story 的\"小\"。
   - Stories 在**准备开发之前刻意不被展开**（"deliberately not fleshed out in detail until they are ready to be developed"）；这里已经埋下了与 EARS / 传统 shall-requirements 最大的方法论分歧——**"故事是占位符，不是规格"**。

2. **INVEST 作为 story 的\"质量特征集\"（Bill Wake 原创）**
   - **I**ndependent — 故事可按任意顺序交付
   - **N**egotiable — 细节由程序员与客户在开发期间共同建构
   - **V**aluable — 被客户/用户视为有价值
   - **E**stimable — 程序员能给出合理估计
   - **S**mall — 应在小规模时间（通常 person-days）内完成；一个 iteration 里能完成多条
   - **T**estable — 能写出测试验证其\"正确工作\"
   - **研究线含义**：这 6 条是 Topic 02 评价 story 质量的**事实标准**；Topic 05 做\"User Story vs EARS\"对比时，会发现 INVEST 与 INCOSE GtWR 15 特征**并不一一对应**，存在\"Negotiable vs Unambiguous\"的结构性张力。

3. **"As a … I want … So that …" 模板的角色**
   - Fowler 原文：\"The 'so that' part provides important context to understand to help get from what the customer think they want to providing what they actually need.\"
   - **关键解读**：模板主要服务**动机（why）对齐**，不是\"规约完备性\"的保证。这点与 EARS 的\"结构化自然语言语法\"形成结构性差异。

4. **权威二次文献线索**
   - Fowler 把 **Mike Cohn 的书**（后续另落 Cohn 独立锚点）标为\"the standard book on writing user stories\"——这是 Topic 02 另一条主 KOL 证据链的官方锁定。
   - Fowler 还把 XP 原始两本书（Beck 白皮书 + 绿皮书 `pxp.html`）列为 story 的方法论根。

5. **Stories vs Use Cases — Fowler 的立场**
   - 正文结尾：\"In an earlier bliki entry I discuss why **UseCasesAndStories** are different.\"
   - 这条链接在 Topic 01/05（范式地图 + 选型矩阵）会被再次回引，作为**"Story ≠ Use Case，不可替换"**的 KOL 证据。

---

## 原文直引（关键段，逐字）

> "Kent Beck first introduced the term as part of Extreme Programming to encourage a more informal and conversational style of requirements elicitation than long written specifications. The essence of a story can be written on a single note card (Kent and I prefer 3" by 5"). Stories are deliberately not fleshed out in detail until they are ready to be developed, you only need enough understanding to allow prioritization with other stories."

> "A common way to formulate stories is the 'As a … I want … So that …' form. … The 'so that' part provides important context to understand to help get from what the customer think they want to providing what they actually need."

> "Mike Cohn wrote what is now the standard book on writing user stories."

## 与其它锚点的桥接

- → `00-shared-incose-gtwr-v4-summary.md`：GtWR 的 15 特征 vs INVEST 的 6 特征，是 Topic 05 选型矩阵第一组对照列。
- → `00-shared-mavin-2009-ears-re09.md`：EARS 五模式是\"语法级结构化\"，story 的 As-a-I-want-So-that 是\"动机级结构化\"——**不是同一层**。
- → 待落 `00-shared-cohn-user-stories-primer.md` 与 `00-shared-patton-story-mapping-primer.md`：Cohn 负责 story 的\"写法规范 + 3C + 卡片-对话-确认\"，Patton 负责\"story map 结构与 backbone/walking skeleton\"。

## 限制 / 未覆盖

- Fowler bliki 不是**学术文献**（tier B，而非 A）；Topic 02 正式主张必须回到 Cohn 书（Tier A 书籍）+ XP 原书 + Wake 的 INVEST 原文做三重交叉。
- Fowler 未给出\"什么时候不该用 user story\"的反向准则；这一点要靠 Topic 02 限制面（safety/regulatory, API spec, etc.）与 Topic 06（agent format）一起补。
