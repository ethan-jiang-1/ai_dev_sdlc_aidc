# Jeff Patton — *The New User Story Backlog is a Map* (KOL Anchor)

- source_url: `https://jpattonassociates.com/the-new-backlog/`（2008-10-08，2023-04-12 最近更新，2026-04-17 抓取正文）+ 配套书 *User Story Mapping: Discover the Whole Story, Build the Right Product*（O'Reilly, 2014, ISBN 978-1-4919-0490-9）+ 原始 2005 文章 *How You Slice It*（JPA 自托管 PDF）
- source_type: `KOL blog + standard book`
- accessed_at: `2026-04-17`
- related_topic: `shared (02 user-story primary；01 re-landscape、04 future-trends、05 integration-bdd 引用)`
- trust_level: `practitioner (author-owned site + O'Reilly-published reference book)`
- tier: `A`（书本身是 Story Mapping 事实标准；博文 Tier B，合并作为同一 KOL 体系的主锚）
- why_it_matters: Jeff Patton 的 Story Map 补上了**"扁平 backlog 无法解释系统全貌"**这块 Mike Cohn primer 没有直接覆盖的空缺。Patton 的 backbone / walking skeleton / 垂直切片模型，是 Topic 02 从\"单 story 写作\"上升到\"story 集合的结构化组织\"的**唯一事实标准锚点**。同时他在文中公开**反对\"epic\"一词**、反对\"requirement\"一词，这对 Topic 01 术语地图是强 KOL 证据。
- captured_excerpt: `yes`

---

## 关键事实

1. **核心论点：flat backlog 的三大破坏**（Patton 原文）
   - **解释失败**：flat backlog 无法回答\"你在建的系统是什么\"；当 stakeholder 问\"what does the system do\"时，一堆 story 列表答不上来。
   - **完备性失败**：扁平列表让你\"总觉得漏了点什么\"；缺少结构意味着缺少 coverage 检查。
   - **发布规划失败**：120+ story 的平铺 in-out 抉择\"是我人生最悲惨的时段之一\"（原话）。
   - Patton 用隐喻：\"flat backlog 是\"砍了树，只把叶子装在落叶袋里的 mulch\"——**"A bag of context-free mulch."**

2. **Story Map 的结构（backbone / ribs / vertical slice）**
   - **顶层**：**user activities**（大任务块，借用 UX 界 Larry Constantine / Don Norman 的用语），对应\"Managing email\" 这类粗粒度行为。
   - **中层**：**user tasks**（小任务），对应 story 级\"send message / delete message / mark as spam\"。
   - **排列规则**：**从左到右 = 时间顺序**（活动/任务按用户操作的时间先后摆放）。
   - **backbone**：顶部的\"活动轴\"本身**不参与优先级**——它们是\"必要存在\"。
   - **ribs**：backbone 下挂的 task 卡才排优先级，**越上越必要**。
   - **walking skeleton**（Patton 显式借用 Alistair Cockburn 术语）：地图中最高优先级的横切一刀 = 端到端最小可交付系统。

3. **Release Planning 的 car 隐喻（Patton 原文）**
   - 发布不应该在 backbone 上做取舍：\"What's more important, the engine or the transmission?\"——都是必须。
   - 取舍在 ribs 层：\"4-cylinder 还是 6-cylinder、防抱死还是不防抱死\"——这才是 MVP 层级的优先级。
   - 用横向胶带分 release lane + 卡片上下移动表示优先级与所在 release。
   - **研究含义**：Patton 提供了 story 层级 backlog grooming 的**维度化模型**；它在 Topic 02 与 Topic 05 中是\"单 story 质量\"之外的第二根坐标轴（\"story 集合的组织质量\"）。

4. **关键术语立场**
   - **反对 `epic`**：\"There's no hero with a magic weapon slaying a monster\"；他主张用 \"activity / user task\"，因为这类词自带层级含义。
   - **反对 `requirement`**：博文中链回 `requirements_considered_harmful`（JPA 另一篇文章），Patton 在 story 世界里更愿意用\"story / activity / task\"。
   - **研究含义**：Topic 01 术语地图里，\"requirement\"一词在 agile KOL 中是有意被规避的；本研究线在合成时必须点出\"Mavin EARS 恰恰在重建 requirement 的写法\"——两派立场是**方法论层面不可调和**，只能在选型矩阵里分场景并存。

5. **\"Pattern, not innovation\" 论断**
   - Patton 自己明确：\"if they say 'we're doing something like that too!' it's a pattern.\" Story mapping 是**多独立发明者收敛形成的模式**（他提到 Luke Barrett、Indi Young mental model、Todd Warfel task analysis grid 的近源模式）。
   - **研究含义**：Topic 02 不要把 story mapping 写成\"Patton 的发明\"；它在 2014 年才被正式命名并由 O'Reilly 出书规范化。

6. **配套资产**
   - 2014 O'Reilly 书 *User Story Mapping*（含 Martin Fowler 序）是**书级主证据**。
   - 2005 文章 *How You Slice It* 是该方法第一次公开发表，可作为历史锚。
   - Patton 的\"slides\"在博文中公开链接，可作为教学材料二级证据。

---

## 原文直引

> "We spend lots of time working with our customers … we finally get down to the details—the pieces of functionality we'd like to build. In my head I see a tree where the trunk is built from the goals or desired benefits that drive the system; big branches are users; the small branches and twigs are the capabilities they need; then finally the leaves are the user stories small enough to place into development iterations. After all that work … I feel like we pull all the leaves off the tree and load them into a leaf bag—then cut down the tree. **That's what a flat backlog is to me. A bag of context-free mulch.**"

> "Those big things on the top are often the essential capabilities the system needs to have. I refer to them as the **'backbone' of the software** … you'll find that all the stories placed high on the story map describe the smallest possible system you could build that would give you end-to-end functionality. This is what **Alistair Cockburn refers to as the 'walking skeleton'**. I always try to build this first."

> "Keep your epics—but stop calling them that because it bothers me. … At least the terms 'activity' and 'user task' give me some idea of what kinds of stories they are."

## 桥接

- → `00-shared-cohn-user-stories-primer.md`：Cohn 管\"单 story 写法\"，Patton 管\"story 集合的组织\"。两者拼起来才是 Topic 02 的完整 story 方法论。
- → `00-shared-fowler-user-story-bliki.md`：Fowler bliki 本身就链接到 Cohn 书；Patton 2014 书由 Fowler 作序——KOL 引用网络闭合。
- → `00-shared-mavin-2009-ears-re09.md`：EARS 在 story map 中的位置应该是\"rib 下的验收级表达\"还是\"backbone 外的独立文档\"？Topic 05 要做的判决题。

## 限制

- Patton 未处理**安全/合规/可追溯性**要求；Topic 04 / 05 / 06 在相应约束下（ISO 26262, DO-178C, EN 50128）需另外用 INCOSE GtWR + ISO 29148 补。
- 2008 文章对\"工具层落地（Jira/Confluence/Miro 上的 Story Map 插件）\"不覆盖；2014 书与 O'Reilly 后续增量材料需另做 Tier B 补充。
