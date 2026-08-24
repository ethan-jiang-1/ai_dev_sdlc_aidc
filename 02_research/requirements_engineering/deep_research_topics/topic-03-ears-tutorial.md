# Topic 3 — EARS（教程向独立主题）

> 本文件面向 **独立 Deep Research** 使用：嵌入了原文 §3.2 的完整语法表与 §4.1 / §4.2 的 worked examples，不依赖打开源文即可完成一轮研究。

## 研究问题（Deep Research 入口）

1. **无约束自然语言**需求的典型缺陷（歧义、遗漏、不可测试等）在工业审计中如何归类？EARS 的**固定子句顺序**为何能缓解这些问题？
2. 五种核心模式 + 复合模式：各自**语义角色**、**典型主语（系统/子系统）**与**常见误用**是什么？
3. **何时不用 EARS**（复杂布尔、决策表、数学/算法式需求）的实践准则与替代制品？
4. **INCOSE GTWR** 与 EARS 联用时，哪些规则最常与自动化工具有效结合？
5. EARS 能否/如何用于 **纯软件 SaaS** 项目，而不只是安全关键硬件？边际收益在哪？

## 原文锚点（供回溯）

| 章节 | 主题 |
|------|------|
| §2.2 | 劳斯莱斯 / 适航语境；无约束自然语言八大问题；RE09；轻度约束自然语言；时间逻辑模板 |
| §3.2 | 基础架构（前置、触发、系统名、响应）；**五模式 + 复合** 全表与工业例（本文件已完整复刻）|
| §4.1（后半）| 手机银行：状态驱动 + 有害行为（超时）示例（已嵌入）|
| §4.2 | ISO 26262、ASIL、AEB：复合逻辑 + 有害行为（已嵌入）|
| §5.2 | 优势：FSM 同构、跨语言团队；边界：多前置条件、决策表、公式/伪代码、缺商业原因 |
| §8.2 | INCOSE 与 EARS 交集：Necessary、无歧义、原子化、系统中心与主动语态 |

---

## 1. 起源与核心哲学（原文 §2.2 压缩）

- 2009 年，Alistair Mavin 等在劳斯莱斯（Rolls-Royce）分析飞机发动机控制系统适航需求时创立；同年在 IEEE RE09 发布。
- 审计无约束自然语言时归纳出八大缺陷：**歧义（Ambiguity）、模糊（Vagueness）、复杂（Complexity）、遗漏（Omission）、重复（Duplication）、冗长（Wordiness）、不适当的实现描述（Inappropriate implementation）、不可测试（Untestability）**。
- 核心哲学：**轻度约束自然语言（Gently Constrained Natural Language）**——不引入数学符号/图形语言，而是用少数关键字（While / When / If / Where / shall）强制固定子句顺序，使自然语言获得接近机器代码的确定性。

## 2. 句法构件与关键字

EARS 基础架构要求子句按**固定顺序**出现：

```
[precondition(s)]  [trigger]  <system name>  shall  <system response>
   While / Where        When / If         the <subject>    必要动作
```

**规则**（原文 §3.2）：

- **零个或多个**前置条件（precondition/state）。
- **零个或一个**触发器（trigger/event）。
- **唯一**的系统名称作为主语，**主动语态**。
- **一个或多个**系统响应（shall 动词 + 可测量结果）。

**关键字语义**：

| 关键字 | 作用 | 对应模式 |
|--------|------|---------|
| `The <system>` + `shall` | 任何条件下都成立 | Ubiquitous |
| `When <trigger>` | 有限时长的事件/触发 | Event-driven |
| `While <state>` | 持续状态，期间持续生效 | State-driven |
| `If <trigger>, then` | 不期望的 / 异常触发 | Unwanted |
| `Where <feature>` | 可选特性/配置装配时 | Optional |
| 任意两者组合 | 复合时序 | Complex |

---

## 3. 五模式 + 复合：完整语法模板表（原文 §3.2 复刻）

> 本表是 EARS 学习的**核心教具**。中文模板来自原文；英文模板是社区标准形式（Mavin 官方站 [6]、Jama [18]、Visure [13]）。

| # | 模式 | 逻辑定位 | 英文语法模板 | 中文模板 | 典型工业例 |
|---|------|---------|---------------|----------|-----------|
| 1 | **Ubiquitous**（无处不在型）| 任何条件下都必须具备的基础属性、约束、NFR | `The <system name> shall <system response>.` | `<系统名称> 必须 <系统响应>` | 手机的质量必须小于 XX 克。 |
| 2 | **Event-driven**（事件驱动型）| 系统在接收到外部触发/内部事件时的即时响应（软件最常见）| `When <trigger>, the <system name> shall <system response>.` | `当 <触发器> 发生时，<系统名称> 必须 <系统响应>` | 当选择"静音"功能时，笔记本电脑必须抑制所有音频输出。 |
| 3 | **State-driven**（状态驱动型）| 系统在持续状态/模式期间必须维持的行为；状态为真需求即激活 | `While <precondition(s)>, the <system name> shall <system response>.` | `在 <前置条件/状态> 期间，<系统名称> 必须 <系统响应>` | 当 ATM 机内没有插入银行卡时，ATM 机必须显示"请插入卡片以开始服务"。 |
| 4 | **Unwanted behaviors**（有害行为型）| 错误、失效、非法输入、异常事件；保证鲁棒性 | `If <trigger>, then the <system name> shall <system response>.` | `如果 <异常触发器> 发生，那么 <系统名称> 必须 <系统响应>` | 如果输入的数据格式无效，那么系统必须生成一条详细的错误日志并拒绝执行。 |
| 5 | **Optional features**（可选特性型）| 仅当系统部署了可选硬件/软件模块时才生效 | `Where <feature>, the <system name> shall <system response>.` | `在包含 <可选特性> 的情况下，<系统名称> 必须 <系统响应>` | 在安装了全景天窗的车型中，车辆控制系统必须提供独立的天窗开闭控制按钮。 |
| 6 | **Complex**（复合需求）| 多模式组合，描述复杂时序 | `While <state>, when <trigger>, the <system name> shall <system response>.` | `在 <前置条件> 期间，当 <触发器> 发生时，<系统名称> 必须 <系统响应>` | 当飞机处于地面状态时，如果接收到反推指令，发动机控制系统必须立即启用推力反向器。 |

**结构同构性**：`While / When / If / Where` → `Given / When / If / Where`（BDD 场景）→ `if / while / switch / event handler`（代码控制流）。这是 EARS 在 LLM 时代被重新发现的根因（详见 [topic-04-future-trends-and-evidence.md](topic-04-future-trends-and-evidence.md) §2）。

---

## 4. Worked Examples（原文 §4.1 / §4.2 完整嵌入）

### 4.1 互联网金融：手机银行"主屏余额"

**原始 User Story（对比基线）**：

> 作为一个银行应用的用户，我希望在应用程序的主屏幕上直接看到我的账户余额，以便于我无需进行繁琐的点击就能随时了解我的财务状况。

**EARS 拆解（同一需求的系统级契约）**：

- **EARS-1（State-driven）**：*While the user is in the authenticated session, the Mobile Banking App shall render the real-time balance on the home screen within 1 second of screen load.*
  `在用户处于已认证登录状态期间，手机银行 App 必须在主屏加载 1 秒内渲染实时余额。`

- **EARS-2（Unwanted）**：*If the core accounting backend does not respond within 3 seconds, then the Mobile Banking App shall display a skeleton placeholder and log the timeout event with request ID.*
  `如果后端核心账务系统接口响应时间超过 3 秒，那么 App 必须显示占位骨架屏并用 RequestID 记录超时事件。`

- **EARS-3（State-driven, NFR）**：*While the user is not authenticated, the Mobile Banking App shall mask the balance field with "****".*
  `用户未登录期间，App 必须用 **** 遮蔽余额字段。`

**教学点**：User Story 保留**商业价值叙述**，EARS-1~3 补齐**缓存刷新、异常降级、未登录掩码**三类故事留白。二者不是替代，而是"北极星 → 契约"的分层。

### 4.2 自动驾驶 AEB（ISO 26262 ASIL D）

**反面：若用 User Story**

> 作为一个驾驶员，我希望汽车在遇到前方有行人时能够自动刹车，以便保证行车安全。

对 ASIL D 开发**毫无指导意义**：没有感知延迟、制动梯度、传感器冗余、降级策略。

**EARS 合规拆解**：

- **EARS-1（Complex：State + Event）**：*While the ego-vehicle speed is between 10 km/h and 80 km/h, when both the LiDAR and millimeter-wave radar detect a stationary obstacle within 10 m ahead, the Braking Subsystem shall apply a deceleration of at least 0.8 g within 50 ms.*
  `在本车速度介于 10–80 km/h 期间，当激光雷达与毫米波雷达同时探测到前方 10 m 内静止障碍物时，制动子系统必须在 50 ms 内施加不低于 0.8 g 的减速度。`

- **EARS-2（Unwanted + Fallback）**：*If the primary radar loses signal or fails, then the System Architecture shall seamlessly switch to the backup ultrasonic sensor network and raise a Level-1 audiovisual alert on the dashboard to request driver takeover.*
  `如果主雷达信号丢失或硬件失效，那么系统架构必须立即切换至备用超声波传感器网络，并通过仪表盘发出最高级声光报警请求驾驶员接管。`

**教学点**：EARS 的**物理阈值（10–80 km/h、10 m、0.8 g、50 ms）** 是可测量、可签入 HARA 的审计锚点，这是 ISO 26262 合规的硬要求。

---

## 5. 反模式 → 重构对照

### 反例 A：形容词堆砌 + 被动语态

**坏例（违反 §8.2）**：
> 系统应尽可能快地对用户请求作出响应，确保良好的用户体验。

**问题**：`尽可能快` `良好` 都是主观形容词；被动语态主语缺位；不可测试。

**重构（Event-driven + Ubiquitous）**：
> *When the user submits a search query, the Search Service shall return the first page of results within 500 ms at the 95th percentile under a load of 100 RPS.*
> `当用户提交搜索请求时，Search Service 必须在 100 RPS 负载下以 P95 延迟 ≤ 500 ms 返回首页结果。`

### 反例 B：多前置条件堆叠进一句

**坏例（违反 §5.2）**：
> 当用户已登录、且订阅有效、且未欠费、且位于大陆地区、且设备为 iOS 14+、且已同意个性化推荐协议时，推荐服务必须展示个性化 Feed。

**问题**：6 个前置条件挤一句，不可读、不可单独验证；EARS 官方推荐在 >3 个前置条件时放弃单句、改用**决策表**（参考 [12] *When Not to Use EARS*）。

**重构**：

1. 提取为决策表：

| 登录 | 订阅 | 欠费 | 区域 | 平台 | 同意协议 | Feed 类型 |
|------|------|------|------|------|---------|-----------|
| 是 | 有效 | 否 | 大陆 | iOS 14+ | 是 | 个性化 |
| 其他任一不满足 | - | - | - | - | - | 降级为热门 Feed |

2. EARS 只保留高层触发：
   > *When the user opens the Feed tab, the Feed Service shall select a Feed variant per the decision table DT-Feed-01.*

**教学点**：EARS 不是万能钥匙，**知道何时退出 EARS** 与知道如何用 EARS 同等重要。

---

## 6. 边界与"何时不用 EARS"（§5.2 + 参考文献 [12]）

- **并发前置条件 > 3**：用列表或决策表。
- **核心算法规约**（定价、加密、FFT、控制率）：用数学公式或伪代码。
- **早期产品探索 / 价值假设**：EARS 缺"商业原因"维度，应让位 User Story（详见 [topic-02-user-story-tutorial.md](topic-02-user-story-tutorial.md)）。
- **纯 UI 走查 / 布局规格**：EARS 勉强但非最佳，Figma + 注解更经济。

## 7. INCOSE GTWR 与 EARS 的质量交集（§8.2 摘录）

- **C1 Necessary**：每条需求须可追溯到上位需求、合规或全生命周期概念，禁止过度设计。
- **Unambiguous & Clear**：禁用"快速""足够好""用户友好"等主观词；性能指标转为可测物理量。
- **Stand-alone / Atomic**：一句一响应，禁止 AND/OR 嵌套。
- **System-centric + Active voice**：主语必须是系统模块，主动语态。

自动化工具（QVscribe、Visure Requirements ALM、Inflectra.ai）可基于上述规则实时扫描 EARS 句子，打"需求质量分数"（详见 [topic-04-future-trends-and-evidence.md](topic-04-future-trends-and-evidence.md) §3）。

---

## 8. 待补文献与检索方向

- Mavin 原始论文 [7] 与官方站 [6]：八类缺陷与 RE09 发布细节。
- *When Not to Use EARS* [12]：决策表 vs EARS 的一手判断准则。
- Jama [18]、Visure [13]、Inflectra [27]：工程化采纳与工具链。
- ISO 26262 / ASIL [20][21][22][23]：AEB 例的合规语境（与 Topic 5 交叉）。
- INCOSE GTWR v4 [47]、自动化白皮书 [48]：INCOSE 规则全集。

## 9. 本 Topic 参考文献（摘自原文编号）

见 [references-by-topic.md](references-by-topic.md) 中 **Topic 3**；完整条目见 [references-full.md](references-full.md)。

**编号快查：** 6, 7, 8, 10, 11, 12, 13, 18, 20, 21, 22, 23, 25, 27, 46, 47

## 10. Deep Research 查询种子

**英文（投喂给 Perplexity / Gemini DR / ChatGPT Search）**：

1. `"EARS notation" Mavin 2009 original paper eight problems unconstrained natural language`
2. `"When not to use EARS" decision table alternatives complex preconditions`
3. `EARS requirements ISO 26262 ASIL automotive case study 2023..2026`
4. `INCOSE Guide to Writing Requirements v4 rules EARS mapping automation`
5. `EARS notation SaaS software project adoption tradeoffs vs user stories`

**中文**：

1. `EARS 需求语法 五模式 完整模板 中文`
2. `ISO 26262 功能安全 需求表述 EARS 案例`
3. `决策表 vs EARS 何时不用 需求工程实践`
4. `QVscribe Visure Inflectra 需求质量自动评分 对比`
5. `INCOSE 需求编写指南 中文 v4 规则`

## 11. 交叉引用

- 范式背景：← [topic-01-re-landscape-and-paradigm-map.md](topic-01-re-landscape-and-paradigm-map.md)
- 与 User Story 的分层协作：→ [topic-05-integration-bdd-selection.md](topic-05-integration-bdd-selection.md)
- AI、工具链、实证：→ [topic-04-future-trends-and-evidence.md](topic-04-future-trends-and-evidence.md)
- 高流量断言可信度：→ [claims-audit.md](claims-audit.md)

## 12. 历史摘要（保留，不修改）

- 本主题的历史正文保留在 §1–§11：它完整复刻了 EARS 起源、五模式与复合模式、worked examples、边界与“何时不用 EARS”、以及与 INCOSE GTWR 的质量交集。

## 13. 本轮新增证据

- post-RE09 官方方法与边界已经补齐：[`_reference/03-ears-mavin-2016-ears-guidelines.md`](_reference/03-ears-mavin-2016-ears-guidelines.md)。
- 近年 empirical anchor 已补齐：[`_reference/03-ears-uusitalo-2023-plc-empirical.md`](_reference/03-ears-uusitalo-2023-plc-empirical.md)。
- 工业 authoring / review 工具链信号已补齐：[`_reference/03-ears-jama-industrial-primer.md`](_reference/03-ears-jama-industrial-primer.md)。
- software-scope 官方边界已补齐：[`_reference/03-ears-software-scope-guidance.md`](_reference/03-ears-software-scope-guidance.md)。

## 14. 本轮新增机制理解

- Topic 03 现在可以更准确地把 EARS 定义成“受控自然语言中间层”，而不是“介于 Story 与形式化之间的静态模板集合”。
- 它的核心机制是通过固定子句顺序，把自然语言压到足够稳定、足够可测、足够可审查的形态，并把复杂度边界显式暴露出来。
- 同时，当前证据也明确指出 EARS 不是万能层：
  - completeness 是高频风险
  - >3 前置条件、复杂逻辑、公式、决策表场景应退出 EARS
  - 因而“会用 EARS”与“知道何时不用 EARS”同等重要

## 15. 本轮新增趋势与难点

- EARS 进入软件范围的官方适用性现在已经可以成立，但 SaaS / non-safety software 的公开生产实证仍未补齐；本轮多次 targeted search 后继续保持 deferred。
- 工具链层面，EARS 与 INCOSE rules、advisor / linting、以及 agent-era structured workflow 的联动价值已经显现，这为 Topic 04 / 06 提供了方法外溢。
- `GtWR v4` 全文与 rule-by-rule mapping 仍受访问限制，导致 Topic 03 在合规 / 逐条对齐论证上必须继续保留 full-text-pending 风险标签。

## 16. 当前判断（本轮综合后）

- Topic 03 现在可以稳写成：
  - `five-pattern-core-supported`
  - `official-guide-supported`
  - `software-scope-supported`
  - `when-not-to-use-boundary-supported`
  - `industrial-tooling-supported`
  - `recent-empirical-anchor-supported`
  - `saas-empirical-pending`
  - `gtwr-rule-by-rule-mapping-pending`
- 因而当前判断是：EARS 适合作为系统行为契约层和 AI 编程时代的结构化 requirements 输入，但不能被表述为跨所有域、所有复杂度都优于其他方法的万能格式。
