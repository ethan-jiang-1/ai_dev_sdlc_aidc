# _raw_orgs — 影响 AI Coding 话语的组织卡

> 机构作为"发声体"的立场与言论：技术雷达、工程博客、官方研究、公司级宣言。
> 人物卡在 [`../_raw_people/`](../_raw_people/README.md)；厂商的产品/方法论材料在 [`../../corp/`](../../corp/README.md)。

## 定位与分工边界（三问三答）

| 问题 | 边界 |
|---|---|
| **组织卡 vs 人物卡**（`../_raw_people/`） | **署名主体**：机构署名 → 本库；个人署名 → 人物卡。机构×个人可以**双卡位并存**（例：37signals 官宣 pencils down 是组织卡素材，DHH 的 Lex 访谈是人物卡素材；LangChain 官方四环模型是组织卡，Sydney Runkle 个人言论走人物/台账判定） |
| **组织卡 vs corp**（`../../corp/`） | corp 收"**厂商材料**"——他们怎么做/卖什么（AWS AI-DLC 方法论、生态全景）；本库收"**机构作为思想者的立场言论**"——他们主张什么（雷达主题、公司级判断、工程博客的判断性输出）。同一机构可双卡位（AWS 方法论在 corp，若其雷达/博客有立场性主张可在此开卡） |
| **组织卡 vs 事件库**（`../_raw_*_2026/`） | 单次活动（峰会/retreat）→ 事件库；机构的持续立场 → 本库。FOSE retreat 是 TW 主办的活动（事件库），TW 的雷达与技术主张是持续立场（本库） |

## 入册判据（草案，2026-10-03，待切磋）

1. **机构署名的官方输出**：技术雷达、工程博客、官方论文、公司级宣言；
2. **有立场性主张**：是"他们主张什么"，不是产品说明书或 changelog；
3. **2026 时间窗 + 来源铁律**：同 [`../README.md`](../README.md) 的来源/时间铁律；
4. **持续发声**：一次性新闻稿不够格，至少有跨时间的立场轨迹可追。

## 卡片结构

沿用人物卡标准件：frontmatter（org / source_urls / key_concepts）→ 当前立场小结 → **思想变迁轨迹（2026）表 + 判语** → 专题节 → Source 尾链。

## 现有卡

- [`thoughtworks.md`](thoughtworks.md) —— 技术雷达 Vol 34（"拐点"定调、认知债、harness 学科化背书）；2026-10-03 自 `_raw_kol/01_thoughtworks.md` 迁入（组织非个人，归属修正）。

## 候选评估清单（2026-10-03 草案——到底有多少组织影响 AI Coding？待切磋）

**A. 已有库内素材、可直接开卡的**：

| 组织 | 库内素材位置 | 意见面主张（开卡理由） |
|---|---|---|
| **Anthropic** | loop 台账 §A `anthropic_org`（evidence-b/c 全文） | 官方 loop 原语（`/goal` 三值判定、auto mode 熔断）、AI-Native SDLC playbook、Applied AI |
| **OpenAI** | loop 台账 §B 机构条目 + `09` 卡素材 | harness engineering 官方文、auto-review 论文（"The separation of roles matters"） |
| **Google Cloud** | `09` 卡（GC 官方博客 09-25） | The Agent Factory、harnesses shifting left、官方定性 "coined the term agent harness" |
| **LangChain** | loop 台账 §A（Sydney Runkle 条目背后） | 四环模型官方文（agent/verification/event-driven/hill-climbing）——厂商级体系化定义 |

**B. 话语场高影响、尚未入库的**：

| 组织 | 信号 | 备注 |
|---|---|---|
| **37signals** | pencils down 是**公司级**官宣（Rails World keynote） | 与 DHH 双卡位的典型样本 |
| **Stripe** | hard/soft steering 文（"errors block progress but warnings don't"） | loop 台账 §B 已有线索 |
| **Shopify** | 生产事故回溯研究（agent 评审的 PR 出更少事故）+ 放弃 React Native | 数据+决策双重影响 |
| **Meta** | Orosz 06-17 批判的对象兼发声者 | 组织行为本身成为话语事件 |
| **Sourcegraph/Amp** | orbs / dial / "Steer, Don't Queue" 产品词汇 | 与 `19` Thorsten 卡分工 |
| **Cognition** | 《Don't Build Multi-Agents》反并行论 | 台账 §B 已有 |
| **GitHub/Microsoft** | Copilot 时代的官方叙事 | 口径偏产品，判据 #2 需严审 |
| **Cursor/Anysphere** | IDE 叙事中心（Valim 讣告体的对象） | 同上，产品口径为主 |
| **AWS** | corp 已有方法论卡 | 是否补"意见面"双卡位——切磋点 |

**C. 待切磋的原则问题**：

1. 机构×个人双卡位的判定（署名主体）会不会产生重复维护？（倾向：组织卡只收机构署名输出，个人言论不复制）
2. corp×orgs 双卡位（AWS 案例）：方法论材料 vs 立场言论的界线是否成立？
3. loop 台账的 `anthropic_org` 行与本库 Anthropic 卡的关系（台账管 loop 主题名单，org 卡管全景立场——素材引用不复制）

---

**最后更新**：2026-10-03 建库（架子）；ThoughtWorks 卡自 `_raw_kol/01` 迁入；候选清单为切磋底稿。
