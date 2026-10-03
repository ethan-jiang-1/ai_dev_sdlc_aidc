# AIDLC KOL Deep-Dive — 历史上塑造 SDLC 的声音在 AI 时代

> 当 AI 开始重塑软件开发生命周期，那些曾经定义了"好的软件开发方式"的人和公司，现在在说什么？

---

## 这个库为什么存在 & 卡片写作思路（2026-10-03 定）

**为什么是"人"**：AI-SDLC 的术语与立场不是从论文里长出来的，是从具体的人嘴里长出来的（vibe coding→Karpathy、harness engineering→Lopopolo/Böckeler、loop engineering→Osmani、pencils down→DHH）。要追话语的演化，就得追人——**人是口径的单一事实来源**。

**每张卡的标准结构**（写作时按此组织，缺的注明待补）：
1. **frontmatter**：person / organization / verification_status / source_urls（全部一手）/ key_concepts
2. **标题 + 一句话定位引言**
3. **当前立场小结**（建卡时点的 3-6 条，每条可回源）
4. **思想变迁轨迹（2026）★ 本库的构图中心**：阶段 × 日期 × 立场标记 × 一手锚点的表格 + 一段**判语**。范围只收 2026 年以后（时间铁律 2026-01 硬底线）；≤2025 一律压缩为一行"背景"。判语要点名轨迹的**类型**：
   - **反转型**（DHH：抵制→pencils down）
   - **细化/自限型**（Fowler：验证主张加张力；Beck：TDD 口径双重限定；Cherny："已死"→质量守门）
   - **稳定型**（Farley / Tacho / Morris / ThoughtWorks——零漂移本身是事实，也是场内锚点）
   - **产品化直线型**（Dohmke：宣言→机制）
   - **单点宣言型**（Valim：待观察）
   - **上行/下行对轴**（Ball 上行 vs Ronacher 转冷）
5. **正文专题节**：带日期小节，按「确认/延伸/修正」标注与既有口径的关系
6. **与库内其他人物的立场对照**（指针式，不展开判读）
7. **关键引用汇总 + Source 尾链**

**两条库规的落点**：来源铁律（一手英文源）与时间铁律（2026 窗口）见 [`../README.md`](../README.md)；滚动更新的操作流程（回源核查→只进卡片→新人入册→口径显式标注→判读不进种子层）见 [`../README.md`](../README.md)「滚动更新规矩」节。

**库的边界**：本库只收"谁在哪天说了什么（带源）"；跨人的横向判读（话语场转变、阵营划分）沉淀在 `02_research/`（当前：`02_research/02_ai_sdlc/01_evolution/paradigm_evolution/`）。

---

## 文件导航

| 文件 | 人物/公司 | 一句话 |
|------|----------|--------|
| `01_thoughtworks.md` | ThoughtWorks | 技术雷达 Vol.33/34：认知债、Harness Engineering、经典实践不是过时而是 AI 的制衡力 |
| `02_martin_fowler.md` | Martin Fowler | "Verified" 的含义从"我读过"变成"被测试、类型检查器、自动化关隘验证过" |
| `03_dave_farley.md` | Dave Farley | CD 让 AI 时代可以存活；AI 暴露那些从未学会工程师思维的人；12,000 行问题 |
| `04_simon_willison.md` | Simon Willison | SDLC 是围绕"一天几百行"设计的——10x 后全崩；"有没有人每天用了两周"是新质量信号 |
| `05_kent_beck_agile.md` | Kent Beck + Agile 社区 | XP 在 AI 时代复苏；TDD 是 Agent 的理想搭档；"我们保持怀疑，保持人性" |
| `07_andrej_karpathy.md` | Andrej Karpathy | Vibe Coding 造词者；"agentic engineering" 扩散者（该词实为 Zed/Sobo 2025-06 引入，见卡内勘误）；Software 3.0 |
| `08_boris_cherny.md` | Boris Cherny | Claude Code 之父，"软件工程已死"，150 PR/天，零手写代码 |
| `09_ryan_lopopolo.md` | Ryan Lopopolo | OpenAI Harness Engineering 先驱，100 万行零人写零人审，70 PR/周 |
| `10_kief_morris.md` | Kief Morris | IaC 之父，"in the loop → on the loop" 框架，Agentic Flywheel |
| （Pragmatic Summit 2026）→ 独立库 | 峰会专题已独立成库：Beck+Fowler 同台、Willison、前GitHub CEO+Atlassian CTO | [`../_raw_promatic_summit_2026/`](../_raw_promatic_summit_2026/README.md) |
| `12_gergely_orosz.md` | Gergely Orosz | *The Pragmatic Engineer* 作者，六预测（好/坏/丑），"Something precious is being taken away" |
| `13_laura_tacho.md` | Laura Tacho | 前 DX CTO，450+ 公司 12 万开发者数据，"AI 是放大器"，"失望鸿沟" |
| `14_thomas_dohmke.md` | Thomas Dohmke | 前 GitHub CEO，Entire 创始人（$60M 种子轮），"Homer Simpson 车"，"Agent 装配线" |
| `15_dhh.md` | DHH | Rails World 2026 "Pencils down"：37signals 停止手写代码；从头号抵制者到 agent 加速派（"agent-accelerated development"） |
| `16_geoffrey_huntley.md` | Geoffrey Huntley | "代码不需要人类可读，只需要人类可解释"；工厂派纲领（2026-10-02） |
| `17_armin_ronacher.md` | Armin Ronacher | "内卷派"主笔：Better Models Worse Tools、slop factory，与 Thorsten 公开互驳 |
| `18_jose_valim.md` | José Valim | 语言层为 agent 重构：program databases over LSPs、runtime observability over debuggers |
| `19_thorsten_ball.md` | Thorsten Ball | Amp 共创者，"aim higher" 乐观极，agent 派生 agent 黑盒测试实录 |
| `20_birgitta_bockeler.md` | Birgitta Böckeler | Harness Engineering 方法论第一作者：Guides + Sensors 矩阵；08-11 用实验质疑自己的 TDD 主张 |

---

## 快速定位

### 想了解"AI 时代 SDLC 应该怎么改"？
→ [04_simon_willison.md](04_simon_willison.md) + [02_martin_fowler.md](02_martin_fowler.md)

### 想了解"AI 时代什么经典实践更重要了"？
→ [03_dave_farley.md](03_dave_farley.md) + [05_kent_beck_agile.md](05_kent_beck_agile.md)

### 想了解"企业级 AI 开发治理"？
→ [01_thoughtworks.md](01_thoughtworks.md) + [02_martin_fowler.md](02_martin_fowler.md)

### 想了解"最激进 agent 全速派"与"经典工程派"的对撞？
→ [15_dhh.md](15_dhh.md) + [02_martin_fowler.md](02_martin_fowler.md) + [05_kent_beck_agile.md](05_kent_beck_agile.md)

### 想了解全貌和分歧？
→ 本文件下方「共识/分歧矩阵」一节（06 综合篇从未建成，跨人物综合由该矩阵承担）

---

## 共识/分歧矩阵

| 话题 | Fowler | Farley | Willison | Beck | ThoughtWorks | Karpathy | Cherny | Lopopolo | DHH |
|------|--------|--------|----------|------|-------------|----------|--------|----------|-----|
| **经典实践（TDD/CI/CD）更重要了** | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | ✅ | — |
| **SDLC 需要为 AI 吞吐量重新设计** | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Vibe Coding 对生产不负责任** | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| **AI 可以信任为半黑盒** | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| **AI 需要确定性传感器验证** | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | — |
| **AI 是中层级工程师的就业风险** | — | — | ✅ | — | ✅ | — | ✅ | — | — |
| **AI 是嵌入正确实践的最佳机会** | ✅ | ✅ | — | ✅ | ✅ | — | ✅ | — | — |
| **手动编程作为一种职业正在终结** | — | — | — | — | — | ✅ | ✅ | ✅ | ✅ |

✅ = 同意 · ❌ = 反对 · — = 未明确表态

## 新增 KOL

Kief Morris 的 "in the loop → on the loop" 框架已被 ThoughtWorks (Böckeler)、Martin Fowler、OpenAI (Lopopolo) 广泛引用，是 Harness Engineering 思想谱系的基础性贡献。

## 观察名单（2026-10-03 开荒扫描产出）

- **Justin Searls**——10-02 播客《Retiring from programming》+ 自述"意外建了 dark factory"；事件型、书面长文少，**书面化后开卡**。
- **Mitchell Hashimoto**——07-29 创办 Superlogical（"durable session… visible and controllable by people"，人机共栖会话层）；一手仅宣言一篇，**再写人机协作文即升卡**。
- **Alexander Embiricos**（OpenAI Codex 产品负责人）——Lenny 专访付费墙未破、X 登录墙，**无一手可核；transcript 可得后评估**。
- **Dex Horthy**（HumanLayer）——"Harness Engineering is not Enough: Why Software Factories Fail"（AI Engineer World's Fair，经 Osmani 07-20 帖一手转介）；**演讲本体待回源**。
- **Nathan Sobo**（Zed CEO）——"agentic engineering" 命名者（Zed 2025-06），**不建卡**；谱系修正见 `07_andrej_karpathy.md` 卡内勘误。
