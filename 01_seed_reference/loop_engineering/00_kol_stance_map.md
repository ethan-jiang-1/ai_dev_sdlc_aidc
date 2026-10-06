---
type: stance_map
content_type: analysis
directory: 01_seed_reference/loop_engineering
description: KOL 立场光谱与滑动可视化——67 档位置总览、23 档时间轨迹、证据四象限普查（图 + 可审计定档表）
map_date: 2026-10-07
authority_note: 派别判定唯一权威在 kol-roster §A2；本文档位是派别之下的细分可视化，不构成第二权威
---

# 00_kol_stance_map — KOL 立场光谱与滑动图（2026-06 → 10）

> **问题**（用户 2026-10-07 提）：三派之外，能不能表达**每个人在哪个位置、位置怎么变化、是怎么滑动的**？
> 本文用三张 SVG 回答：**位置**（图 A 总览）、**滑动**（图 B 轨迹）、**谁在发声的结构**（图 C 普查）。
> 全部数据来自各 KOL 档头部「态度轨迹」节与各条目「派别适配」票面（2026-10-07 抽取）；台账与判读文件零改动。

## 一、定档规则（先于读图）

7 档光谱，**左推动 → 右反对**（与 01_advocates → 02_neutral → 03_skeptics 目录序一致）：

| 档 | 含义 | 锚点例 |
|---|---|---|
| **+3 强推动** | 激进极／世纪级修辞／无人值守默认 | swyx『entire game of the next century』、Yegge 舰队多派 |
| **+2 推动** | 把"设计循环让 agent 自动推进"当默认方向推荐 | Osmani 命名＋教程化、Andrew Ng 三环 |
| **+1 偏推动** | 推动但带边界自认／受约束翼／弱证据登记位 | Mistele 受约束翼、Krieger 难点自认、Nadella（⚠️） |
| **0 中性** | 有条件成立——划边界、给约束、先测再信 | Böckeler eval 实证、Goedecke 对齐派 |
| **−1 偏怀疑** | 部分票／共享怀疑派特定主张（门槛/成本/新瓶旧酒） | Willison 门槛证词、Orosz 调查式怀疑 |
| **−2 怀疑** | 给反证与批评（失败账本/质量退化/安全） | Ronacher 质量反证、Zechner security theater |
| **−3 强反对** | 全盘结构性否定 | **空位**——印证 [landscape §二.1](00_three_camp_landscape.md)：怀疑几乎全部来自实践者内部，无外人唱衰 |

三条铁则：

1. **派别判定唯一权威在 [kol-roster §A2](../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)**；档位只是派别之下的细分刻度。档位与目录归属打架处标 ⚠️，不静默统一（先例：sean_goedecke 头排「Google SWE」冲突——见其档背景行）。
2. **单点档（44/67）不画线**——"证据不足以判弧线"如实呈现（多为 AIEWF 讲者层，各档标「待补挖」）。缺席的弧线本身是证据状态。
3. **⚠️ ＝档内明示证据弱／经转引／待判**（jensen_huang 吹票降级候选、nadella 证据不足、rieseberg 单点转引、david_fowler 全经转引链、walden_yan 厂商利益待判、livingstone 经现场稿、会议层票）——这类位置仅示登记位，不是判定。

## 二、图 A · 立场光谱总览（67 档：谁在哪、谁滑了）

![立场光谱总览：一人一行，起点○→终点●，单点档为单点；顶部分布带显示人群重心漂移](figures/stance-a-overview.svg)

**读法**：一人一行。○＝起点（窗口初或谱系末）→ ●＝终点（2026-10-07 观测）；单点档＝一个实心点。派内排序：滑动者（按滑幅降序）→ 稳定者 → 单点。顶部灰色/彩色分布带＝人群重心漂移（○灰＝窗口初、●彩＝窗口末，单点计入两侧）。

**总览速读**：

- **分布带漂移**（窗口初 → 窗口末）：中性带 **17 → 12**（−5），两翼同时加厚——`+2` 22→24、`−1` 3→6、`+3` 4→5、`−2` 9→8。**中场变薄、两端变厚**：不是单边漂移，是极化。
- **12 个滑动者，两个方向**：向推动滑 7（DHH、Steinberger、Thorsten Ball、Hashimoto、Kent C. Dodds、Mollick、Zechner〔建设面微滑〕）vs 向怀疑滑 5（Huntley、Orosz、Willison、Dwarkesh、Ronacher）。
- **−3 全程空位**＋厂商/商业领袖（Jensen、Nadella、Krieger、Chase、Rauch…）全部在推动侧，怀疑侧清一色一线工程与实证。
- 44 个单点集中在 `+2`/`0` 带（AIEWF 讲者层）——弧线判读的大片待补区。

## 三、图 B · 滑动轨迹（23 档：光谱 × 时间）

![滑动轨迹：横轴光谱、纵轴时间，三派泳道；顶部虚影带为窗口前谱系起点，★为关键转折](figures/stance-b-trajectories.svg)

**读法**：横轴＝7 档光谱（三派各一条泳道），纵轴＝2026-06-01 → 10-07（真实日期线性）。顶部虚影带＝窗口前谱系起点（Steinberger 2025-12 的反对长文、Hashimoto 02-05 的划线、DHH 2023–2025 抵制者时期、Orosz 01-07 grief、Huntley 01-13、Karpathy 04-30）。★＝各档自标注的关键转折；右侧灰虚线＝运动大事参考线（命名帖、AIEWF、auto mode 攻破、Agent Civilizations……）。

**六条大弧线**（图上一眼可读）：

1. **Steinberger**：−2 → +3 → +2——词源人自己的双翻转，07-18『Loop 已死，graph 永生』。
2. **DHH**：−2 → +2——头号抵制者到机制全采纳（词表仍嘲讽——推动派相邻位样本）。
3. **Ronacher**：+1 → −2——审慎接受到内卷判词＋35h 白卷（怀疑派锚点的成形过程）。
4. **Willison**：0 → −1——08-27 auto mode 被指 80% 攻破后安全信任崩塌（预算立场全程稳定，崩的只是对安全机制的信任）。
5. **Hashimoto**：+1 → +3——08-11『600 nightly agents』越过自己 2 月划的线（中性档里唯一的向推动大滑）。
6. **Huntley**：+3 → +1——激进实干极转向验证（07-24 Antithesis）＋对运动话语疏离。

## 四、图 C · 证据四象限普查（谁的结构性在场/缺席）

![证据四象限普查：影响力×技术深度两轴，KOL 四格落位，机构层跨轴单列，群众两格](figures/stance-c-quadrant-census.svg)

**读法**：两轴＝[README 证据分层](README.md)的正交维度（影响力 × 技术深度）。67 KOL 按象限落位；orgs/ 47 档（机构/厂商层）跨两轴单列顶部；community_tech 20 档＋community_product 9 档在群众行。右下格标 ⚠️：README 判读称『community_product 接近零——缺席本身是证据』系 2026-10-06 前口径，community 拆分批落位后现有 9 档，**成色另判**（是否真为非专业群众声音，待专题复核）。

## 五、定档总表（审计用——图从表生，不凭感觉画）

> 每行依据锚点指向对应 KOL 档；改档先改表。`档位`列＝起点→终点（单点档只标单点位）。

| 档 | 人物 | 派 | 档位（起→终 / 单点） | 关键转折（档内口径） | 票面（派别适配） | 依据锚点 |
|---|---|---|---|---|---|---|
| `dhh` | DHH | 推动派 | 怀疑→推动 | 词与机制分离：feed 零 loop 提及、机制全采纳 | 词表不屑＋机制全采纳（相邻位） | [`01_advocates/kol_tech/dhh.md`](01_advocates/kol_tech/dhh.md) |
| `steinberger` | Peter Steinberger | 推动派 | 怀疑→推动 | 07-18 宣告 Loop 时代终结——词源者自己换词 | 推动票（词源人·换词表非转反对） | [`01_advocates/kol_tech/steinberger.md`](01_advocates/kol_tech/steinberger.md) |
| `geoffrey_huntley` | Geoffrey Huntley | 推动派 | 强推动→偏推动 | 07-24 从激进实践转向验证 | 推动票（激进实干→验证瓶颈） | [`01_advocates/kol_tech/geoffrey_huntley.md`](01_advocates/kol_tech/geoffrey_huntley.md) |
| `thorsten_ball` | Thorsten Ball | 推动派 | 推动→强推动 | 09-19 加码至 'code review will die'（Osmani 反驳、Ball 未回应） | 推动票（产品语言·单向加码） | [`01_advocates/kol_tech/thorsten_ball.md`](01_advocates/kol_tech/thorsten_ball.md) |
| `osmani` | Addy Osmani | 推动派 | 推动→推动 | 08-31 skill decay 后不回摆 | 推动票（命名者·持续演进不回摆） | [`01_advocates/kol_tech/osmani.md`](01_advocates/kol_tech/osmani.md) |
| `akshay_nathan` | Akshay Nathan | 推动派 | 偏推动（单点） | — | 推动票（带边界自认） | [`01_advocates/kol_tech/akshay_nathan.md`](01_advocates/kol_tech/akshay_nathan.md) |
| `masad` | Amjad Masad | 推动派 | 推动→推动 | 07-16 从技术层升至组织层 | 推动票（公司级愿景） | [`01_advocates/kol_tech/masad.md`](01_advocates/kol_tech/masad.md) |
| `karpathy` | Andrej Karpathy | 推动派 | 推动→推动 | 无转折——人管判断/品味，agent 管执行 | 推动票（实践者·管理层视角） | [`01_advocates/kol_tech/karpathy.md`](01_advocates/kol_tech/karpathy.md) |
| `andrew_ng` | Andrew Ng | 推动派 | 推动（单点） | — | 术语定义者·三环模型 | [`01_advocates/kol_tech/andrew_ng/profile.md`](01_advocates/kol_tech/andrew_ng/profile.md) |
| `dan_mcateer` | Dan McAteer | 推动派 | 推动（单点） | — | 推动票（结构综合） | [`01_advocates/kol_tech/dan_mcateer.md`](01_advocates/kol_tech/dan_mcateer.md) |
| `eiso_kant` | Eiso Kant | 推动派 | 推动（单点） | — | 推动票（强） | [`01_advocates/kol_tech/eiso_kant.md`](01_advocates/kol_tech/eiso_kant.md) |
| `rieseberg` | Felix Rieseberg | 推动派 | 偏推动（单点） | — | 推动票（弱 ⚠️ 单点转引） | [`01_advocates/kol_tech/rieseberg.md`](01_advocates/kol_tech/rieseberg.md) |
| `rauch` | Guillermo Rauch | 推动派 | 推动（单点） | — | 推动票（强·掌控翼） | [`01_advocates/kol_tech/rauch.md`](01_advocates/kol_tech/rauch.md) |
| `harrison_chase` | Harrison Chase | 推动派 | 推动（单点） | — | 推动票（相邻位·managed agents 词表） | [`01_advocates/kol_tech/harrison_chase.md`](01_advocates/kol_tech/harrison_chase.md) |
| `livingstone` | Ian Livingstone | 推动派 | 推动（单点） | — | 推动票（辩论正方·经现场稿 ⚠️） | [`01_advocates/kol_tech/livingstone.md`](01_advocates/kol_tech/livingstone.md) |
| `jason_lopatecki` | Jason Lopatecki | 推动派 | 推动（单点） | — | 推动票 | [`01_advocates/kol_tech/jason_lopatecki.md`](01_advocates/kol_tech/jason_lopatecki.md) |
| `jensen_huang` | Jensen Huang | 推动派 | 推动（单点） | — | 吹捧票（降级候选 ⚠️ 经媒体转引·一手未取得） | [`01_advocates/kol_product/jensen_huang.md`](01_advocates/kol_product/jensen_huang.md) |
| `jesse_vincent` | Jesse Vincent | 推动派 | 偏推动（单点） | — | 推动票（'教掌控'型·安全边界最强） | [`01_advocates/kol_tech/jesse_vincent.md`](01_advocates/kol_tech/jesse_vincent.md) |
| `justin_smith` | Justin Smith | 推动派 | 推动（单点） | — | 推动票（会议层 ⚠️） | [`01_advocates/kol_tech/justin_smith.md`](01_advocates/kol_tech/justin_smith.md) |
| `kieran_klaassen` | Kieran Klaassen | 推动派 | 推动（单点） | — | 推动票（compound engineering） | [`01_advocates/kol_tech/kieran_klaassen.md`](01_advocates/kol_tech/kieran_klaassen.md) |
| `mistele` | Kyle Mistele | 推动派 | 偏推动（单点） | — | 推动票（受约束翼·定义者之一） | [`01_advocates/kol_tech/mistele.md`](01_advocates/kol_tech/mistele.md) |
| `lance_martin` | Lance Martin | 推动派 | 推动（单点） | — | 推动票（强） | [`01_advocates/kol_tech/lance_martin.md`](01_advocates/kol_tech/lance_martin.md) |
| `laurie_voss` | Laurie Voss | 推动派 | 推动→推动 | 无翻转——从分类学走向治理深化 | 推动票（治理翼） | [`01_advocates/kol_tech/laurie_voss.md`](01_advocates/kol_tech/laurie_voss.md) |
| `krieger` | Mike Krieger | 推动派 | 偏推动（单点） | — | 推动票（带难点自认） | [`01_advocates/kol_tech/krieger.md`](01_advocates/kol_tech/krieger.md) |
| `patrick_debois` | Patrick Debois | 推动派 | 推动→推动 | 商品化预言——loop 本身不会是竞争力 | 推动票（降温注记） | [`01_advocates/kol_tech/patrick_debois.md`](01_advocates/kol_tech/patrick_debois.md) |
| `roland_gavrilescu` | Roland Gavrilescu | 推动派 | 推动（单点） | — | 推动票（会议层 ⚠️） | [`01_advocates/kol_tech/roland_gavrilescu.md`](01_advocates/kol_tech/roland_gavrilescu.md) |
| `sachin_malhotra` | Sachin Malhotra | 推动派 | 偏推动（单点） | — | 推动票（受约束翼） | [`01_advocates/kol_tech/sachin_malhotra.md`](01_advocates/kol_tech/sachin_malhotra.md) |
| `sam_bhagwat` | Sam Bhagwat | 推动派 | 强推动（单点） | — | 推动票（激进预言·Steinberger's law） | [`01_advocates/kol_tech/sam_bhagwat.md`](01_advocates/kol_tech/sam_bhagwat.md) |
| `nadella` | Satya Nadella | 推动派 | 偏推动（单点） | — | 证据不足以定派（档内口径）⚠️ 吹捧层登记位 | [`01_advocates/kol_product/nadella.md`](01_advocates/kol_product/nadella.md) |
| `steve_yegge` | Steve Yegge | 推动派 | 强推动→强推动 | 警示升级但仍是多派（Gas Town 仍在跑） | 推动票（激进多派＋安全警示） | [`01_advocates/kol_tech/steve_yegge.md`](01_advocates/kol_tech/steve_yegge.md) |
| `suraj_gupta` | Suraj Gupta | 推动派 | 推动（单点） | — | 推动票（Warp harness 负责人） | [`01_advocates/kol_tech/suraj_gupta.md`](01_advocates/kol_tech/suraj_gupta.md) |
| `thariq_shihipar` | Thariq Shihipar | 推动派 | 推动（单点） | — | 推动票（强·task budget 涌现 nuance） | [`01_advocates/kol_tech/thariq_shihipar.md`](01_advocates/kol_tech/thariq_shihipar.md) |
| `tim_sweeney` | Tim Sweeney | 推动派 | 推动（单点） | — | 推动票（会议层 ⚠️） | [`01_advocates/kol_tech/tim_sweeney.md`](01_advocates/kol_tech/tim_sweeney.md) |
| `tushar_jain` | Tushar Jain | 推动派 | 偏推动（单点） | — | 推动票（掌控翼） | [`01_advocates/kol_tech/tushar_jain.md`](01_advocates/kol_tech/tushar_jain.md) |
| `zach_lloyd` | Zach Lloyd | 推动派 | 推动→推动 | 从布道转为实测爬坡数据 | 推动票（激进化·实证） | [`01_advocates/kol_tech/zach_lloyd.md`](01_advocates/kol_tech/zach_lloyd.md) |
| `swyx` | swyx | 推动派 | 强推动→强推动 | 无转折——持续推动，08-08 乐观与风险辩证化 | 推动票（造词者·强推动） | [`01_advocates/kol_tech/swyx.md`](01_advocates/kol_tech/swyx.md) |
| `ethan_mollick` | Ethan Mollick | 中性派 | 中性→推动 | 10-01 认错转折——从审慎教学转为'模型自组织、人类只定向' | 中性票（认错式接受·模型自组织派） | [`02_neutral/kol_product/ethan_mollick.md`](02_neutral/kol_product/ethan_mollick.md) |
| `hashimoto` | Mitchell Hashimoto | 中性派 | 偏推动→强推动 | 08-11 越过自己 2 月的划线——六个月内实质升级 | 中性票（升温·越线） | [`02_neutral/kol_tech/hashimoto.md`](02_neutral/kol_tech/hashimoto.md) |
| `orosz` | Gergely Orosz | 中性派 | 中性→偏怀疑 | 07-14 从个人情绪转为系统调查——多数用例是旧物重贴标签 | 中性票（调查式怀疑） | [`02_neutral/kol_tech/orosz.md`](02_neutral/kol_tech/orosz.md) |
| `kent_c_dodds` | Kent C. Dodds | 中性派 | 中性→偏推动 | 从教人怎么用→做成产品给人用 | 中性票（强票·日益操作化） | [`02_neutral/kol_tech/kent_c_dodds.md`](02_neutral/kol_tech/kent_c_dodds.md) |
| `willison` | Simon Willison | 中性派 | 中性→偏怀疑 | 08-27 转折——预算立场全程稳定，崩的是对安全机制的信任 | 中性票（安全信任衰减） | [`02_neutral/kol_tech/willison.md`](02_neutral/kol_tech/willison.md) |
| `alex_zhang` | Alex Zhang | 中性派 | 中性（单点） | — | 中性票 | [`02_neutral/kol_tech/alex_zhang.md`](02_neutral/kol_tech/alex_zhang.md) |
| `andrew_qu` | Andrew Qu | 中性派 | 中性（单点） | — | 中性票 | [`02_neutral/kol_tech/andrew_qu.md`](02_neutral/kol_tech/andrew_qu.md) |
| `boeckeler` | Birgitta Böckeler | 中性派 | 中性→中性 | 08-10 方法论事件：even best practices need evals | 中性票（审慎实证·最强中性样本） | [`02_neutral/kol_tech/boeckeler.md`](02_neutral/kol_tech/boeckeler.md) |
| `charlie_holtz` | Charlie Holtz | 中性派 | 偏怀疑（单点） | — | 中性票（中偏疑） | [`02_neutral/kol_tech/charlie_holtz.md`](02_neutral/kol_tech/charlie_holtz.md) |
| `dan_abramov` | Dan Abramov | 中性派 | 中性→中性 | 把 agent 协作比作非技术经理带天才团队 | 中性票（单点深观察·实践反思） | [`02_neutral/kol_tech/dan_abramov.md`](02_neutral/kol_tech/dan_abramov.md) |
| `darren_shepherd` | Darren Shepherd | 中性派 | 中性（单点） | — | 中性票（架构派·带清醒怀疑） | [`02_neutral/kol_tech/darren_shepherd.md`](02_neutral/kol_tech/darren_shepherd.md) |
| `david_fowler` | David Fowler | 中性派 | 偏推动（单点） | — | 中性偏推动（票弱 ⚠️ 全经转引链） | [`02_neutral/kol_tech/david_fowler.md`](02_neutral/kol_tech/david_fowler.md) |
| `dex_horthy` | Dex Horthy | 中性派 | 中性（单点） | — | 中性票（辩论反方·'not anti-loops'） | [`02_neutral/kol_tech/dex_horthy.md`](02_neutral/kol_tech/dex_horthy.md) |
| `kief_morris` | Kief Morris | 中性派 | 中性（单点） | — | 中性票（flywheel 偏推动张力 ⚠️） | [`02_neutral/kol_tech/kief_morris.md`](02_neutral/kol_tech/kief_morris.md) |
| `kim_maida` | Kim Maida | 中性派 | 中性（单点） | — | 中性票 | [`02_neutral/kol_tech/kim_maida.md`](02_neutral/kol_tech/kim_maida.md) |
| `kyle_lee` | Kyle Jaejun Lee | 中性派 | 中性（单点） | — | 中性票 | [`02_neutral/kol_tech/kyle_lee.md`](02_neutral/kol_tech/kyle_lee.md) |
| `matt_pocock` | Matt Pocock | 中性派 | 中性（单点） | — | 中性票 | [`02_neutral/kol_tech/matt_pocock.md`](02_neutral/kol_tech/matt_pocock.md) |
| `moritz_johner` | Moritz Johner | 中性派 | 中性（单点） | — | 中性票（含强怀疑引句 ⚠️） | [`02_neutral/kol_tech/moritz_johner.md`](02_neutral/kol_tech/moritz_johner.md) |
| `ryan_cooke` | Ryan Cooke | 中性派 | 偏怀疑（单点） | — | 中性票（中偏疑） | [`02_neutral/kol_tech/ryan_cooke.md`](02_neutral/kol_tech/ryan_cooke.md) |
| `sean_goedecke` | Sean Goedecke | 中性派 | 中性→中性 | 无翻转——验证/对齐留在人手是全窗口不变量 | 中性票（稳定审慎·复合立场） | [`02_neutral/kol_tech/sean_goedecke.md`](02_neutral/kol_tech/sean_goedecke.md) |
| `walden_yan` | Walden Yan | 中性派 | 偏推动（单点） | — | 受约束形态（中性票不足·厂商利益 ⚠️ 待判读层裁定） | [`02_neutral/kol_tech/walden_yan.md`](02_neutral/kol_tech/walden_yan.md) |
| `ronacher` | Armin Ronacher | 反对与怀疑派 | 偏推动→怀疑 | 07-04 工具退化反证——从'不可逆但有边界'转为'机制跟不上能力曲线' | 怀疑票（锚点·质量反证代表） | [`03_skeptics/kol_tech/ronacher.md`](03_skeptics/kol_tech/ronacher.md) |
| `dwarkesh` | Dwarkesh Patel | 反对与怀疑派 | 中性→怀疑 | 08-29 从一般 AI 访谈转为 agent 文明兴衰结构论 | 怀疑票（结构论者） | [`03_skeptics/kol_product/dwarkesh.md`](03_skeptics/kol_product/dwarkesh.md) |
| `mario_zechner` | Mario Zechner | 反对与怀疑派 | 怀疑→偏怀疑 | 连续性：循环合法性＝验证者能力——从批评走到建设 | 怀疑票（稳定怀疑·实践反证 13 条） | [`03_skeptics/kol_tech/mario_zechner.md`](03_skeptics/kol_tech/mario_zechner.md) |
| `auriel_wright` | Auriel Wright | 反对与怀疑派 | 怀疑（单点） | — | 怀疑票（工程实证向） | [`03_skeptics/kol_tech/auriel_wright.md`](03_skeptics/kol_tech/auriel_wright.md) |
| `chawla_koul` | Chawla & Koul | 反对与怀疑派 | 怀疑（单点） | — | 怀疑票（工程实证向） | [`03_skeptics/kol_tech/chawla_koul.md`](03_skeptics/kol_tech/chawla_koul.md) |
| `dotta` | Dotta | 反对与怀疑派 | 怀疑（单点） | — | 怀疑票（结构向·方案建设性） | [`03_skeptics/kol_tech/dotta.md`](03_skeptics/kol_tech/dotta.md) |
| `jack_cable` | Jack Cable | 反对与怀疑派 | 怀疑（单点） | — | 怀疑票（强·安全域） | [`03_skeptics/kol_tech/jack_cable.md`](03_skeptics/kol_tech/jack_cable.md) |
| `nick_heiner` | Nick Heiner | 反对与怀疑派 | 怀疑（单点） | — | 怀疑票 | [`03_skeptics/kol_tech/nick_heiner.md`](03_skeptics/kol_tech/nick_heiner.md) |
| `noam_brown` | Noam Brown | 反对与怀疑派 | 怀疑（单点） | — | 怀疑票（厂商核心自认） | [`03_skeptics/kol_tech/noam_brown.md`](03_skeptics/kol_tech/noam_brown.md) |
| `paul_bakaus` | Paul Bakaus | 反对与怀疑派 | 偏怀疑（单点） | — | 怀疑票（立场向·承认前 80% 交 agent） | [`03_skeptics/kol_tech/paul_bakaus.md`](03_skeptics/kol_tech/paul_bakaus.md) |

## 六、与其他文件的分工

| 文件 | 管什么 |
|---|---|
| [`00_three_camp_landscape.md`](00_three_camp_landscape.md) | 三派判读（文字结论） |
| [`00_debates_2026.md`](00_debates_2026.md) | 人对人对峙（10 条交锋轴） |
| **本文** | 每人位置＋时间滑动（可视化＋定档表） |
| [kol-roster §A2](../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md) | 派别判定唯一权威（本文的上位口径） |

## 七、维护

- **新增发声** → 先更新对应 KOL 档「态度轨迹」节 → 再改本文定档表对应行 → 图 A 该行/图 B 该线随之更新（生成脚本为 `.tmp-` 一次性件，SVG 可手改或按表重生成）。
- **单点档升级为轨迹**（补挖到位）→ 图 A 该行由点变哑铃，图 B 加线。
- **派别判定变更** → 以台账 §A2 为准，本文档位跟随调整并在表内标注变更日期。
